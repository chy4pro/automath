# Paperclip control plane (project container)

Paperclip (github.com/paperclipai/paperclip, MIT) runs inside the AutoMath Workbench project container
(runtime `system`, image `wb-proj-base`, Debian 13, user `agent`, no root). Nothing is installed in the image;
everything lives on the project volume and survives container rebuilds:

| Path | Content |
|---|---|
| `/work/.tools/node` | Node 24 (user-space tarball; the image has no Node) |
| `/work/.tools/npm` | npm prefix with `paperclipai`, `@anthropic-ai/claude-code`, `@openai/codex` |
| `/work/.paperclip/instances/default/` | config.json, embedded PostgreSQL (`db/`, port 54329), storage, logs, backups, `secrets/master.key` |
| `/work/.home` | durable HOME for the container (CLI logins for `claude`/`codex` live here) |
| `/work/tools/paperclip/start.sh` | the project's `run_cmd` (sets PATH/HOME/PAPERCLIP_HOME, `paperclipai run`) |
| `/work/.paperclip/env.sh` | optional non-secret overrides sourced by start.sh (not created yet) |

Workbench row: `run_cmd = sh /work/tools/paperclip/start.sh`, `port = 3100` (published on the host's 127.0.0.1).
From an AI session container the server is reachable as `http://wb-proj-656d7af54e8b:3100`.
Deployment mode: `authenticated` / `private`, bind `lan` (0.0.0.0 inside the container), allowed hostnames
include localhost, the container name, `paperclip.automath.mozone.io`, `automath.mozone.io`.
`local_trusted` is not possible here: it requires a loopback bind, which Docker cannot publish.

Operate: `node_stop` / `node_start` the project; logs with `node_logs`; health at `/api/health`.
First run printed a one-time bootstrap CEO invite URL in the logs (valid 3 days) — the owner opens it on the Mac
at `http://127.0.0.1:3100/invite/<token>` to create the admin account; it is not stored in the repository.

Public exposure (live since 2026-10-08): `https://automath.mozone.io` → Cloudflare tunnel `automath`
(id 807d2966-…, remote-managed ingress → `http://localhost:3100`) → cloudflared running inside the project container
(started by start.sh when `/work/.paperclip/tunnel.token` exists; binary `/work/.tools/bin/cloudflared`).
Cloudflare Access application "automath paperclip" (self-hosted, domain automath.mozone.io) with one allow policy:
the owner's e-mail only. DNS: proxied CNAME automath → <tunnel-id>.cfargotunnel.com. All created by
`tools/paperclip/cloudflare.sh` (idempotent; needs the Cloudflare token with DNS/Tunnel/Access edit rights).
The console's own tunnel `wb` was left untouched. Paperclip stays in authenticated/private mode with auto base URL;
`automath.mozone.io` is in its allowed hostnames and trusted origins. If logins misbehave behind the proxy, switch to
explicit mode via `/work/.paperclip/env.sh`: `PAPERCLIP_AUTH_BASE_URL_MODE=explicit`,
`PAPERCLIP_AUTH_PUBLIC_BASE_URL=https://automath.mozone.io` (and `PAPERCLIP_DEPLOYMENT_EXPOSURE=public`).
Every restart before the bootstrap CEO invite is claimed regenerates the invite URL (see the latest logs).

Not yet done: agent definitions (coordinator / astra-1 / astra-2), CLI logins in the project container,
routines, budgets, approvals; Cloudflare DNS/tunnel/Access (API token expired on 2026-10-08).

## SSH environments for AI containers (2026-10-09)
Agents can run in other Workbench containers through Paperclip's native `ssh` environment driver: an unprivileged
OpenSSH sshd (Debian bookworm packages extracted to `/work/.tools/sshd`, started by `tools/paperclip/sshd/sshd-up.sh`,
port 2222, pubkey only, `AllowUsers agent`) runs inside the AI container; Paperclip's client key lives in
`/work/.paperclip/ssh/` (private key stored in Paperclip's secret store; `known_hosts` must use the `[ip]:2222` form).
`tools/paperclip/setup_ssh_env.py` registers the container as an environment, probes it and creates an agent bound to it.
Facts learned: the probe from the project container to 192.168.166.3:2222 succeeded; `claude_local` on an ssh target
needs `adapterConfig.engine = "cli"` (the default ACP engine supports sandbox remotes only). Wakeups use
`{"source":"on_demand"}`. Board token: obtained through the CLI-auth challenge flow (`POST /api/cli-auth/challenges`,
owner approves in the browser), stored at `/work/.paperclip/board.token` (0600, git-ignored). Container IPs change on
recreation: update the environment's host and known_hosts then.

Verified 2026-10-09 (run f4cd01c3…): assignment-triggered heartbeat → checkout → work → comment → `done`, 17k input tokens,
subscription-included. Rules that matter: (1) wake agents by **assigning an issue** (the run then carries the issue in its
context; a bare `on_demand` wake cannot write any issue → 403 `cross_issue_influence_run_context_required`); (2) keep the
remote workspace **outside any git work tree** (`/home/agent/pcws/<name>`): inside `/work` Paperclip bundles the whole
repository to the remote every run and Claude Code picks up `/work/AGENTS.md`; (3) the agent runs in
`<remoteWorkspacePath>/.paperclip-runtime/runs/<runId>/workspace`; (4) `jq` is absent in the AI images — instructions
should say "build JSON with python3".

Codex on ssh targets (2026-10-09): `codex_local` is **host-owns-auth** — Paperclip seeds a managed `CODEX_HOME` from the
host's `~/.codex/auth.json` (host = project container, HOME=/work/.home → `/work/.home/.codex/auth.json`) and uploads it
per run; a remote container's own login is shadowed, and an external `env.CODEX_HOME` is resolved on the host and
uploaded too (so pointing it at the remote's `~/.codex` does not work: 401 Missing bearer). Therefore log Codex in once on
the Paperclip host (project terminal, HOME=/work/.home). Also: the Codex AI image has no python3 — agent instructions
must build JSON with node. Codex needs a host-side cwd that exists on the shared volume and is not inside the repo's
work tree: `/work/.paperclip/host-ws/<name>` with its own empty `.git` (tar upload of a tiny dir instead of a repo bundle).

Local patches (2026-10-09, `tools/paperclip/patches/apply.sh`, marker `PAPERCLIP_PATCH_SSH_AUTH`, `.orig` backups):
`codex_local` on ssh environments now uses the REMOTE's own `~/.codex/auth.json` when the host has none — exactly the
behaviour upstream already has for sandbox targets (adapter probe + gate, ssh home-upload fallback, server pre-dispatch
gate). Verified: astra-1 in the Codex container ran with its own login, commented and closed its task.
Re-run the script after every `npm install -g paperclipai`; if an anchor is missing, the upstream code moved — re-derive.
`/work/.paperclip/env.sh` sets `PAPERCLIP_CODEX_AUTH_CACHE=0` so remote workers' credentials are never cached on the host
(the first patched run had created `companies/<id>/codex-auth-cache/<account>/auth.json`; removed).
