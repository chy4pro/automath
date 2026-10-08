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

Public exposure (planned): `paperclip.automath.mozone.io` → Cloudflare tunnel → host port 3100, Cloudflare Access
(owner e-mail only); `automath.mozone.io` → static site in `/work/site/`, with `/paperclip` redirecting to the
subdomain. Paperclip's UI uses root-absolute asset paths (no `base` in `ui/vite.config.ts`), so it cannot be
served under a path prefix.

Not yet done: agent definitions (coordinator / astra-1 / astra-2), CLI logins in the project container,
routines, budgets, approvals; Cloudflare DNS/tunnel/Access (API token expired on 2026-10-08).
