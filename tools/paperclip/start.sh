#!/bin/sh
# Paperclip control plane for automath, started by the Workbench project container (runtime: system).
# Everything lives on the project volume: Node 24 + packages in /work/.tools, data in /work/.paperclip,
# a durable HOME in /work/.home (CLI logins for claude/codex persist across container rebuilds).
export HOME=/work/.home
export PATH=/work/.tools/node/bin:/work/.tools/npm/bin:$PATH
export PAPERCLIP_HOME=/work/.paperclip
export PORT=3100
# optional non-secret overrides (deployment mode, public URL); created by the coordinator
[ -f /work/.paperclip/env.sh ] && . /work/.paperclip/env.sh
mkdir -p "$PAPERCLIP_HOME" "$HOME"
cd /work
echo "[start] $(date -u +%FT%TZ) node $(node -v) paperclipai $(paperclipai --version)"
# Cloudflare connector: if a tunnel token exists, run cloudflared beside the server (origin = localhost:3100)
if [ -s /work/.paperclip/tunnel.token ] && [ -x /work/.tools/bin/cloudflared ]; then
  (/work/.tools/bin/cloudflared tunnel --no-autoupdate run --token-file /work/.paperclip/tunnel.token 2>&1 | sed 's/^/[cloudflared] /') &
  echo "[start] cloudflared started"
fi
# Owner-facing report pages at /reports/ (static, port 3101; routed by the tunnel ingress path rule)
# Supervised so it can be reloaded (GET /reports/_reload from the docker LAN) without touching Paperclip.
(while true; do node /work/tools/paperclip/www/serve.js 2>&1 | sed 's/^/[reports] /'; sleep 1; done) &
# `run` bootstraps (onboard + doctor) on first run; lan preset binds 0.0.0.0 so the Workbench port publish works.
# Crash forensics (2026-10-11): the container's own log is lost when Workbench recreates it, so the server's output,
# its exit status, a memory sample every 15 s and Node's diagnostic report on a fatal error all go to the volume.
L=/work/.paperclip/logs; mkdir -p "$L"
export NODE_OPTIONS="${NODE_OPTIONS:+$NODE_OPTIONS }--report-on-fatalerror --report-uncaught-exception --report-directory=$L"
F=/tmp/paperclip-out.fifo; rm -f "$F"; mkfifo "$F"
tee -a "$L/server.log" < "$F" &
paperclipai run > "$F" 2>&1 &
P=$!
trap 'kill -TERM $P 2>/dev/null' TERM INT
(while kill -0 $P 2>/dev/null; do
   echo "$(date -u +%FT%TZ) $(grep -h VmRSS /proc/[0-9]*/status 2>/dev/null | awk '{s+=$2} END {printf "container_rss_mb=%d", s/1024}') $(awk '/MemAvailable/ {printf "vm_avail_mb=%d ", $2/1024} /SwapTotal/ {t=$2} /SwapFree/ {printf "vm_swap_used_mb=%d", (t-$2)/1024}' /proc/meminfo) $(awk '/^oom_kill / {printf "vm_oom_kills=%d", $2}' /proc/vmstat) $(for c in /proc/[0-9]*/cmdline; do tr '\0' ' ' < $c 2>/dev/null | grep -q 'paperclipai run' && { d=${c%/cmdline}; awk '/VmRSS/ {printf "paperclip_rss_mb=%d ", $2/1024}' $d/status; }; done)" >> "$L/mem.log"
   sleep 15; done) &
S=0; wait $P || S=$?
while kill -0 $P 2>/dev/null; do wait $P || S=$?; done   # a trapped TERM interrupts the first wait
echo "[start] $(date -u +%FT%TZ) paperclipai exited with status $S" | tee -a "$L/server.log"
exit $S
