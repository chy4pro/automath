# Paperclip as the automath project-management layer — evaluation (2026-10-08)

Owner suggestion, coordinator research. Sources: github.com/paperclipai/paperclip (README), docs.paperclip.ing (API overview, adapters: http, process, claude_local, codex_local; Docker deploy), paperclip.ing. Not installed; nothing run.

## What it is
MIT-licensed Node.js server + React UI (+ CLI `paperclipai`) that runs a "company" of AI agents: org chart, goals → projects → issues (tasks) with atomic checkout/execution locks, blockers, comments, documents; **heartbeats** (agents wake on assignment, mention, schedule, or manual; DB-backed wake queue with coalescing, budget check, workspace resolution, adapter invocation); **budgets** per company/agent/project with spend tracked by agent/project/goal/issue/provider/model and automatic pause at limits; **routines** (cron-like recurring work, API/webhook trigger); **approvals/governance**; activity/audit log; secrets; plugins; MCP tool gateway. Embedded PostgreSQL by default; `npx paperclipai@latest onboard --yes`. Launched March 2026 (pseudonymous author @dotta), 30k+ stars in 3 weeks; fast-moving. Requires Node ≥ 24.11 (we have 22.23 → user-space Node 24 needed; no root required).

## Adapters that matter for us
- `codex_local`: runs `codex exec --json` with the prompt on stdin; fields `model` (lists `gpt-6-astra`), `modelReasoningEffort` (`xhigh` supported), `instructionsFilePath` (prepended to every prompt), `cwd`, `timeoutSec`, `outputInactivityTimeoutMs`; **subscription (ChatGPT) sign-in on the host is auto-linked**; `--dangerously-bypass-approvals-and-sandbox` by default (can be disabled); session chaining across heartbeats via `previous_response_id`.
- `claude_local`: `claude --print` headless; `model` (`claude-fable-5-1` listed), `effort`, `promptTemplate`, `cwd`, `maxTurnsPerRun` (300), `timeoutSec`; `dangerouslySkipPermissions` defaults true (must run as non-root; fails otherwise); session resume when `cwd` matches; skills injected with `--add-dir`; ACP engine gives token/cost deltas. Auth: `ANTHROPIC_API_KEY` or Bedrock (subscription login mentioned in README for local sign-in).
- `process`: any command with `PAPERCLIP_API_URL`/`PAPERCLIP_API_KEY` injected; stdout/stderr captured. ⇒ a 20-line shim can bridge a Paperclip issue to our file inbox (write `inbox/to_codex*/NNN.md`, wait for the STATUS line, post the report as a comment).
- `http`: POST `{runId, agentId, context:{taskId, wakeReason, commentId}}` to a URL; 2xx = accepted; the remote calls back the API.
- API: `/api/companies/{id}/...` (agents, issues, projects, goals, approvals, costs, activity, routines, secrets); agent keys are company-bound; `X-Paperclip-Run-Id` links mutations to runs.

## What automath would gain (vs the hand-made inbox + ledger)
1. **Continuity without me**: heartbeats/routines are the scheduler we lost (owner cancelled cron; "unattended operation" never re-verified). A 60-min coordinator heartbeat + routines (6-h reflection, weekly quota check, CI watch) would run whether or not a Claude web session is open.
2. **One board instead of STATUS.md + QUESTIONS.md + ledger**: issues with checkout locks replace `to_codex/NNN.md`; comments replace QUESTIONS; activity log replaces part of the ledger; dashboards replace the hand-built 战报 for operational state (the 战报 stays for owner-facing judgement).
3. **Cost ledger**: per-agent/per-issue spend and budget pauses — we have never had token accounting beyond rough counts.
4. **Governance gates as approvals**: publication/X/site-claim/e-mail actions become approval-gated issues — matches the owner's rules structurally rather than by memory.
5. **Multiple Codex/Claude seats as separate agents** with their own homes (the thread-limit problem becomes "hire another agent").

## Risks / mismatches
- **Where it runs.** Our engines live in Workbench AI containers (Claude session = me; Codex = owner's session with subscription login). Paperclip's local adapters need the CLIs logged in on *its* host. Options: (a) run Paperclip inside the Codex AI container (Node 24 user-space; Codex login present; Claude Code CLI would need login there too); (b) a dedicated Workbench project with the official Docker image (`docker/docker-compose.quickstart.yml`; image bundles `claude`/`codex` CLIs) — port publishing and new runtime are owner-gated; subscription logins must be done inside that container once; (c) keep Paperclip only as the board and bridge both engines through `process`/`http` shims to the existing inbox — least invasive, keeps our clean-room discipline, loses cost tracking from ACP.
- **Full-auto defaults** (`dangerouslySkipPermissions`, `--dangerously-bypass-approvals-and-sandbox`): our hard rules (no posting, no deletions, no PRs, privacy grep) must be enforced by prompts/instructions files + approvals, not by the harness. Keep external actions out of agent reach (no browser/X/Gmail/Zenodo tokens in agent homes).
- **Resources**: server + embedded Postgres ≈ 0.5–1 GB RAM, disk small; my container has ~3 GB free RAM — fine but the memory-protection process must know about it.
- **Maturity**: 7 months old, fast-moving; expect breaking changes; self-host only on a private bind (Tailscale/authenticated mode) — never public.
- **Migration cost**: ~1 day to set up; the inbox protocol stays as the fallback.
- It manages work; it does not make proofs. Gains are coordination/continuity/cost visibility only.

## Recommendation
Pilot, bounded: 1 day setup + 1 week trial, success criterion = "the coordinator heartbeat and one Codex agent ran a real task end-to-end while no human and no Claude web session was open, with cost recorded." Preferred topology: (b) dedicated Workbench project running the Docker image (private port), agents: `coordinator` (claude_local, Fable, instructions = AGENTS.md + OPERATIONS summary, cwd = a checkout of the repo), `astra-1`/`astra-2` (codex_local, gpt-6-astra xhigh, instructionsFilePath = inbox/PROTOCOL.md), routines: 60-min coordinator heartbeat, 6-h reflection, weekly quota; approvals: any external publication. Fallback topology: (c) shims to the inbox.

Owner decisions needed: approve the new dependency and the hosting choice (b vs c); approve a private published port for the UI; do the subscription logins inside the Paperclip host; set budgets.
