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

Orchestration verified (2026-10-09, AUT-9/AUT-10): coordinator-ssh delegated a child issue to astra-1 with a blocker,
Paperclip woke the parent when the child closed, and the parent verified the result (216 Sidon subsets of {1..10}, MATCH).

## The automath org (built 2026-10-09)

| agent | container / env | adapter, model | role file |
|---|---|---|---|
| coordinator (CEO) | Claude box, `ws-coordinator` | claude_local, claude-fable-5-1 | agents/coordinator.md |
| scout | Codex box, `ws-scout` | codex_local, gpt-6-astra, xhigh | agents/scout.md |
| attacker-1, attacker-2 | Codex box, `ws-attacker-N` | codex_local, gpt-6-astra, xhigh | agents/attacker.md (clean room) |
| referee-1 | Claude box, `ws-referee-1` | claude_local, claude-fable-5-1 | agents/referee.md |
| referee-2 | Claude box, `ws-referee-2` | claude_local, claude-opus-5-5 | agents/referee.md |
| formalizer | Codex box, `ws-formalizer` | codex_local, gpt-6-astra | agents/formalizer.md |
| verifier | Claude box, `ws-verifier` | claude_local, claude-sonnet-5-5 | agents/verifier.md |

Everyone reports to the coordinator (`reportsTo`). Publisher/ops duties stay with the coordinator; all
outward actions go through `request_board_approval`. Every agent has its own ssh environment on its
container (`/home/agent/pcws/<agent>`, outside the repo), so agents that share a container never share
a workspace; the per-host key secret is reused. Codex agents additionally need an empty host-side cwd
(`/work/.paperclip/host-ws/<agent>`, `git init`) because the adapter bundles the host cwd per run.

Instructions: `agents/<role>.md` + `agents/_common.md` → the agent's managed bundle (`AGENTS.md`).
Rebuild/refresh everything (idempotent): `python3 tools/paperclip/build_org.py && python3 tools/paperclip/build_envs.py`
(instruction edits are pushed through `PUT /api/agents/{id}/instructions-bundle/file` with the revision base).
IDs land in `/work/.paperclip/agent_ids.json` and `env_ids.json`. `tools/paperclip/pc.py METHOD /path [json]` is the API helper.

Routines (Asia/Shanghai): hourly coordinator tick (`0 * * * *`), 6-hour reflection (`0 */6 * * *`),
weekly scout literature/site sweep (Mon 09:00). All `skip_if_active` / `skip_missed`. The tick and the
reflection are gated `require_external_activity` (company scope): a quiet hour/6 h costs nothing; each
ungated coordinator heartbeat costs ~70–100k input tokens of base context.
Caveat: on PATCH `/api/agents/{id}` the fields `permissions` and `instructionsBundle` are create-only.

## Patch 5: run pools (2026-10-09)

Paperclip caps concurrency per agent only. Patch 5 v2 (`patches/patch5_run_pools.py`, marker `PAPERCLIP_PATCH_RUN_POOLS`)
mirrors upstream PR #14333 (count + claim under a Postgres advisory lock at the single admission point) with the
bucket key generalised: `PAPERCLIP_ADAPTER_CONCURRENCY_LIMITS='{"codex_local":2}'` caps per adapter type, and
named pools: `PAPERCLIP_RUN_POOLS="codex:2:scout,attacker-1,attacker-2,formalizer"` in `/work/.paperclip/env.sh`
caps the simultaneously *running* runs across the named agents (several pools separated by `;`); queued runs wait
and pool-mates are re-checked when a run ends. Combined with per-agent `maxConcurrentRuns: 1` on the Codex
agents, at most two Codex processes run at once. Subagents spawned inside a run are not counted. Upstream has
open issues/PRs in this area (#14564, #7041, #14333, #14995); see the chat record before proposing it upstream.

## Report pages: reload without a Paperclip restart

`start.sh` runs `www/serve.js` under a loop; after editing the server, `curl http://wb-proj-656d7af54e8b:3101/reports/_reload`
from an AI container (LAN only) restarts just the page server. Static pages under `/work/.www` need no reload.

## Container rebuilds (Workbench base failure 2026-10-09)

AI session containers can be recreated: hostname changes, IP and `/home/agent` persist, the user-space sshd dies.
`sshd/sshd-up.sh` keys its state by IP so the host key (and Paperclip's pinned knownHosts) survive; rerun it in
each AI container (the Claude side by the coordinator session, the Codex side by the owner), then set the
interrupted issues back to `todo`. Failed runs count as activity, so gated routines fire once per hour during an
outage at zero token cost; cancel the piled-up routine issues afterwards.

## Claude agents on the Claude API (2026-10-11)

Owner decision: the Claude agents run on the owner's Claude API key ("My Claude API", a Paperclip AI connection with
method api_key, the owner's default); Codex work stays on Codex. `build_api_org.py` creates coordinator-api,
referee-api-1, referee-api-2, formalizer-api, attacker-api-1 (Opus 5.5; formalization and the simpler slot's attacks
moved off Codex on 2026-10-11) and
verifier-api (Sonnet 5.5): same role files plus `agents/api_org.md`, Claude
Code in the Claude container over ssh (`ws-<name>`), runtime binding `{"mode": "responsible_user", "provider":
"anthropic", "method": "api_key"}`, created paused. scout, attacker-1/2 and muse-codex keep GPT-6 Astra and report to
coordinator-api; the Codex formalizer is paused. `build_api_org.py <name>` touches only the named agents (re-pushing a
bundle resets that agent's task sessions). formalizer-api and attacker-api-1 are outside the `claude-api` run pool (adding it needs a
Paperclip restart; the rate limits leave plenty of room). Routines: hourly tick and 6-hour reflection -> coordinator-api, weekly sweep -> scout.
`resume_all.py` (default `api`) resumes the API agents plus the Codex seats; the subscription Claude agents
(coordinator, referee-1/2, verifier) stay paused (`old` / `all` for the rest).
- Budget: company budget policy, billed_cents, lifetime, hard stop, warning at 80%. Subscription and Codex runs record
  0 cents, so it counts only API spend. Until patch 13 (2026-10-11 21:11 UTC) Paperclip charged every resumed Claude run
  the session's running total again (Claude Code restores a session's cost on --resume), so the counter carries $42 of
  over-count; the policy amount is therefore $242, which is the owner's $200 of real spend (watch_api.py subtracts it).
- Background tasks are disabled for the API agents (`CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1`,
  `--disallowedTools=CronCreate,CronDelete,CronList,Monitor`): a background job left at the end of a turn made every later
  resume replay a stale result, and the run died after about 10 s.
- Billing: API runs are recorded as `metered_api`; Paperclip's per-run cost matches list prices (Opus 5.5 $4 / $20 per
  million input / output tokens, cache reads $0.20). Probe runs cost $0.07-0.14. Re-pricing the old org's real work at
  these rates: about $1.9 per coordinator heartbeat, $2.7-3.6 per referee run, $0.27 per verifier run.
- Patch 12 is required: with an AI-connection binding over ssh, Paperclip passed its host-only managed home
  (HOME, XDG_*, CLAUDE_CONFIG_DIR under /tmp/paperclip-ai-*) to the remote run, so sessions never resumed and `~` was a
  throwaway directory. Verified after the patch: same session across runs, HOME=/home/agent, numpy available.
- `api-probe` (paused) is the test seat. Environments of removed or unused agents are archived, never deleted: each
  references secret ssh-key-paperclip, and deleting an environment deletes its secrets.

## Muse seats (2026-10-11)

muse is the owner's extra Linux machine (Workbench local end "muse"; Ubuntu 24.04 systemd-nspawn container in a VM;
2 vCPU, ~7.7 GB RAM behind a virtio balloon, about 5.8 GB usable by one process, no swap, 98 GB free on /home/hatch).
Only /home/hatch persists across a muse reboot; `/`, `/etc` and `/run` are a tmpfs overlay. Three Paperclip seats run
there, all reporting to the coordinator. Run pools (`/work/.paperclip/env.sh`): muse-claude and muse-agy share `muse:2`;
muse-codex is in `codex:2` with the four Codex-container seats, because it uses the same OpenAI account (owner, 2026-10-11).

| Seat | Adapter | CLI on muse | Model |
|---|---|---|---|
| muse-claude | claude_local | /home/hatch/pcbin/claude → claude-keygate | claude-opus-5-5 |
| muse-codex | codex_local | /home/hatch/pcbin/codex → codex-keygate | gpt-6-astra, xhigh |
| muse-agy | agy_local (external) | /home/hatch/pcbin/agy → agy-keygate | gemini-3.1-pro-high |

Path (since 2026-10-11 16:00Z): Paperclip host → the Workbench host Mac's Tailscale (OrbStack containers route
100.64.0.0/10 through the Mac) → DERP over WebSocket → muse's tailscaled in userspace mode → muse sshd on
127.0.0.1:22. Muse's tailnet address is 100.101.197.73. Measured: environment probe 1.5 s, 150 MB copy-back 118 s
(≈1.3 MB/s, no drop). Until 2026-10-11 16:00Z the seats went through a relay in the Claude container and the Workbench SSH bridge (≈3.5 MB/s,
dropped once after 145 MB, depended on the Claude container); the relay was removed at the owner's request. The project
container is not an AI session container, so it has no Workbench grant for the bridge itself; Tailscale needs none.
  Checked 2026-10-11 (start.sh logs it at every start): the project container has the shim on /opt/wb but no grant
  token, no WB_API, no `*.wb` ssh config and no /wb/creds; Workbench issues grants only to AI session containers.
- muse sshd: `/home/hatch/.local/share/paperclip-sshd/` (copies here: `muse/muse-sshd_config`, `muse/muse-up.sh`),
  OpenSSH 9.6p1 from the Ubuntu package the Workbench probe unpacked, pubkey only, root only, loopback only, systemd unit
  `paperclip-sshd`. `SetEnv TAR_OPTIONS=--no-same-owner` is required: /home/hatch refuses chown even for root, and
  Paperclip unpacks its runtime archives with tar.
- Key: secret `ssh-key-muse` in Paperclip only; its public half is in muse's `authorized_keys`. muse host key
  `SHA256:sMdd1B9Rjj7CX2EUvPTK4Hjb2242BuoSbK0ydkhd1zk`, pinned in the environments.
- CLIs: the owner's keygate wrappers (`~/.local/bin/*-keygate`, the owner's gateway, limit 3 concurrent
  requests). `pcbin/<cli>` sets HOME=/home/hatch (ssh logins get HOME=/root); `pcbin/claude` also sets `IS_SANDBOX=1`, without
  which Claude Code refuses `--dangerously-skip-permissions` as root. codex-keygate pins its own
  CODEX_HOME, so Paperclip's managed Codex home is not used on muse; its pre-run credential gate is satisfied by a
  placeholder `OPENAI_API_KEY` that codex-keygate deletes before starting Codex.
- Antigravity: external adapter `agy_local` built from github.com/evgemar/agy-paperclip-adapter (MIT, commit in
  `/work/.paperclip/adapters/agy-paperclip-adapter/SOURCE_COMMIT`), compiled against our patched adapter-utils (symlinked,
  so patches 8–10 apply), registered with `POST /api/adapters/install {packageName: <dir>, isLocalPath: true}`. Patch 11
  lets it use ssh environments. Not the npm package of the same name (different author, no source repository).
- Workspaces: each seat's host-side folder (`host-ws/<seat>`) and fallback home are their own tiny git repositories.
  Without that, git discovery climbs into /work and Paperclip ships the whole repository (~260 MB) over the bridge
  and copies it back on every run.
- Setup and repair: `setup_muse.py` (environments + seats, idempotent). On muse,
  `sh /home/hatch/.local/share/paperclip-sshd/up.sh` (copy: `muse/muse-up.sh`) brings up sshd and Tailscale in userspace
  mode; it is idempotent, never restarts a healthy service, loads the egress proxy settings itself, and exits 0 only when
  both are up, so muse's watchdog runs it routinely. `--restart-tailscale` forces a clean Tailscale restart. Environments `ws-muse-claude-relay-old` / `ws-muse-codex-relay-old` /
  `ws-muse-probe` are archived; each still references secret `ssh-key-muse`, so never delete them (deletion cascades).

## Crash forensics (since 2026-10-11)

On 2026-10-11 14:10Z the Paperclip process died without a clean shutdown (it stopped answering for ~30 s first) and the
container restarted; its output was lost when the container was later recreated, so the cause is not established.
Reproductions of that hour's workload (300 MB copy-back, cancel during copy-back plus deleting the target folder,
repository-sized sync) did not crash it (RSS stayed < 700 MB, health latency 0.1 s). The shared VM (8 GB RAM, 9 GB
swap) has recorded OOM kills since boot, so a VM-wide OOM kill is the leading hypothesis. `start.sh` now keeps:
`/work/.paperclip/logs/server.log` (server output plus `paperclipai exited with status N`: 143 = normal stop,
137 = SIGKILL such as the kernel OOM killer, 134 = fatal Node error, 1 = uncaught exception), `mem.log` (every 15 s:
container and Paperclip RSS, VM available memory, swap used, VM-wide `oom_kill` count) and Node diagnostic reports
on fatal errors in the same directory. Check these before restarting the node after an incident.

## Our own Paperclip repository (2026-10-09)

Fork: https://github.com/chy4pro/paperclip. `master` tracks upstream; branch `automath` carries every customisation
in source form, one commit each (see its `AUTOMATH.md` for the table). Production still runs the npm release with
the dist patches from `patches/apply.sh`; the TypeScript ports on `automath` are the upstreamable form and have not
been type-checked or built on our machines (CI does not run on the fork by default). Upstream threads: #14564,
#14333 and #12930 (comments), issue #15709 and PR #15710 (ours).
