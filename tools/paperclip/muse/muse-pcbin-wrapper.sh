#!/bin/sh
# Installed on muse as /home/hatch/pcbin/{claude,codex,agy}, each exec'ing the matching keygate wrapper.
# Paperclip runs CLIs over ssh as root with HOME=/root; the keygate logins live under /home/hatch.
export HOME=/home/hatch
# claude only: muse is itself a sandboxed container; IS_SANDBOX=1 lets Claude Code accept
# --dangerously-skip-permissions as root (it refuses otherwise).
export IS_SANDBOX=1
exec /home/hatch/.local/bin/claude-keygate "$@"   # codex: codex-keygate, agy: agy-keygate (without IS_SANDBOX)

# /home/hatch/pcbin/claude-api (2026-10-12): plain Claude Code on muse's own API login
#   export HOME=/home/hatch; export IS_SANDBOX=1; exec /home/hatch/.local/bin/claude "$@"
