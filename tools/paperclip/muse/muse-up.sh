#!/bin/sh
# Paperclip's access to muse: the loopback sshd plus Tailscale in userspace mode (inbound tailnet TCP to this node is
# forwarded to 127.0.0.1:22). Idempotent and safe to run every minute from a watchdog: it starts what is missing and
# never restarts what is healthy (a restart would cut running Paperclip tasks). Exit 0 = sshd active and Tailscale Running.
#
#   sh /home/hatch/.local/share/paperclip-sshd/up.sh                       # routine check / bring up after a muse restart
#   sh /home/hatch/.local/share/paperclip-sshd/up.sh --restart-tailscale   # force a clean Tailscale restart
#
# /etc and /run are a tmpfs overlay on muse, so the sshd user, the systemd unit and /run files are recreated here.
D=/home/hatch/.local/share/paperclip-sshd
T=/home/hatch/.local/share/wb-tailscale-ws
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin; export PATH
# Tailscale reaches its servers only through the runtime's egress proxy; a watchdog may start with a bare environment.
if [ -z "$HTTPS_PROXY" ] && [ -r /etc/profile.d/hatch-egress.sh ]; then . /etc/profile.d/hatch-egress.sh; fi
rc=0

# 1) sshd (systemd unit; started only when not active)
getent passwd sshd >/dev/null || useradd -r -M -d /run/sshd -s /usr/sbin/nologin sshd
mkdir -p /run/sshd /run/paperclip-sshd; chmod 755 /run/sshd; chmod 700 /run/paperclip-sshd
cmp -s "$D/authorized_keys" /run/paperclip-sshd/authorized_keys 2>/dev/null || install -m 600 "$D/authorized_keys" /run/paperclip-sshd/authorized_keys
U=/etc/systemd/system/paperclip-sshd.service
if [ ! -f "$U" ]; then
  cat > "$U" <<UNIT
[Unit]
Description=Loopback sshd for Paperclip (reached over Tailscale)
After=network.target
[Service]
ExecStartPre=/bin/sh -c 'getent passwd sshd >/dev/null || useradd -r -M -d /run/sshd -s /usr/sbin/nologin sshd; mkdir -p /run/sshd /run/paperclip-sshd; chmod 700 /run/paperclip-sshd; install -m 600 $D/authorized_keys /run/paperclip-sshd/authorized_keys'
ExecStart=$D/sshd -D -e -f $D/sshd_config
Restart=always
RestartSec=5
[Install]
WantedBy=multi-user.target
UNIT
  systemctl daemon-reload
  systemctl enable paperclip-sshd.service >/dev/null 2>&1 || true
fi
if ! systemctl is-active --quiet paperclip-sshd.service; then
  "$D/sshd" -t -f "$D/sshd_config" && systemctl start paperclip-sshd.service
fi
if systemctl is-active --quiet paperclip-sshd.service; then echo "sshd: active"; else echo "sshd: NOT active"; rc=1; fi

# 2) Tailscale (userspace). --restart-tailscale stops only our tailscaled: its pid file must point at the wbws3 daemon
#    running with our state directory (the check the owner's OPERATIONS.txt asks for), then starts it again.
if [ "$1" = "--restart-tailscale" ] && [ -f /run/wb-tailscale-ws/tailscaled.pid ]; then
  P=$(cat /run/wb-tailscale-ws/tailscaled.pid)
  if [ "$(readlink /proc/$P/exe 2>/dev/null)" = "$T/1.104.1-wbws3/tailscaled" ] && tr '\0' '\n' < /proc/$P/cmdline | grep -qx -- "--statedir=$T/state"; then
    kill -TERM "$P"; i=0; while kill -0 "$P" 2>/dev/null && [ $i -lt 50 ]; do sleep 0.2; i=$((i+1)); done
    echo "tailscale: stopped pid $P"
  else
    echo "tailscale: pid file does not point at our tailscaled; not stopping anything"
  fi
fi
node "$T/start-userspace.cjs" >/dev/null || rc=1
i=0; st=""
while [ $i -lt 30 ]; do
  st=$("$T/tailscale" status --json 2>/dev/null | python3 -c 'import json,sys; print(json.load(sys.stdin).get("BackendState",""))' 2>/dev/null)
  [ "$st" = "Running" ] && break; sleep 1; i=$((i+1))
done
echo "tailscale: ${st:-unknown}"
[ "$st" = "Running" ] || rc=1
exit $rc
