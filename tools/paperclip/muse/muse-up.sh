#!/bin/sh
# Idempotent: (re)create the ephemeral parts (/etc and /run live on a tmpfs overlay on muse) and start sshd
# under systemd. Run after every muse reboot: sh /home/hatch/.local/share/paperclip-sshd/up.sh
set -e
D=/home/hatch/.local/share/paperclip-sshd
getent passwd sshd >/dev/null || useradd -r -M -d /run/sshd -s /usr/sbin/nologin sshd
mkdir -p /run/sshd /run/paperclip-sshd; chmod 755 /run/sshd; chmod 700 /run/paperclip-sshd
install -m 600 $D/authorized_keys /run/paperclip-sshd/authorized_keys
$D/sshd -t -f $D/sshd_config
cat > /etc/systemd/system/paperclip-sshd.service <<UNIT
[Unit]
Description=Loopback sshd for Paperclip (Workbench SSH bridge)
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
systemctl enable --now paperclip-sshd.service >/dev/null 2>&1 || true
systemctl restart paperclip-sshd.service
sleep 1
systemctl is-active paperclip-sshd.service
