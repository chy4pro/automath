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
