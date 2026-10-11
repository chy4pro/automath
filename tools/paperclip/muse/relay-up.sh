#!/bin/sh
# Start (idempotently) the muse SSH relay in this AI session container. Run it in the Claude container after a
# Workbench base rebuild, together with tools/paperclip/sshd/sshd-up.sh.
# Paperclip's muse environments connect to <this container's IP>:2223; only the Paperclip host may connect.
set -e
MACHINE=${MACHINE:-muse}; PORT=${PORT:-2223}; PEERS=${PEERS:-$(getent hosts wb-proj-656d7af54e8b | awk '{print $1}')}
[ -f /opt/wb/kernel/local-shim.mjs ] && [ -r /wb/grant/token ] || { echo "no Workbench shim/grant here: not an AI session container"; exit 1; }
[ -n "$PEERS" ] || { echo "cannot resolve the Paperclip host"; exit 1; }
IP=$(hostname -I 2>/dev/null | awk '{print $1}'); S=/work/.tools/sshd/state/ip-$IP; mkdir -p "$S"
P="$S/$MACHINE-relay.pid"
if [ -f "$P" ] && kill -0 "$(cat "$P")" 2>/dev/null; then echo "$MACHINE relay already running (pid $(cat "$P")) on $IP:$PORT"; exit 0; fi
nohup node /work/tools/paperclip/muse/relay.mjs "$MACHINE" "$IP" "$PORT" "$PEERS" >> "$S/$MACHINE-relay.log" 2>&1 &
echo $! > "$P"; sleep 1
kill -0 "$(cat "$P")" && echo "$MACHINE relay up: $IP:$PORT -> $MACHINE.wb:22 (peers $PEERS)"
