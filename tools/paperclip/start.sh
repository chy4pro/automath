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
# `run` bootstraps (onboard + doctor) on first run; lan preset binds 0.0.0.0 so the Workbench port publish works
exec paperclipai run
