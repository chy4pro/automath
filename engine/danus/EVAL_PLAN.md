# Danus × ox-alpha evaluation (owner-directed, 2026-08-24 11:2x CDT)

Owner: "你可以让ox-alpha接入它试试". Goal: find out whether frenzymath/Danus (codex branch, v3,
codex-native orchestrator) runs end-to-end with the free stealth/ox-alpha model as the ONLY
backend (main agent + workers + verifier), and whether it produces verifier-gated facts.

## Backend facts established (11:1x CDT)
- ox-alpha is served through OpenRouter (`https://openrouter.ai/api/v1`, model `stealth/ox-alpha`,
  key OR_KEY). Chat-completions ping OK ("PONG", 131 tokens).
- OpenRouter's **Responses** endpoint returned 429 "temporarily rate-limited upstream" 4/4 while
  chat-completions succeeded → Danus's default `wire_api = "responses"` will not work for this
  model. Plan: after `scripts/setup-codex.sh api` writes runtime/codex-home/config.toml, override
  `wire_api = "chat"` in that RUNTIME file (sidecar edit of generated config; upstream untouched).
- opencode zen "go" endpoint (OC_GO_KEY) is a separate pool; fallback if OpenRouter's shared
  free pool keeps 429-ing (check whether ox-alpha is listed there first).

## Host
Danus requires Linux + tmux and runs codex with `--dangerously-bypass-approvals-and-sandbox`;
its README demands an isolated disposable host. → GCP VM, never the Mac.
- e2-medium (2 vCPU shared, 4 GB), Debian 12, ON-DEMAND (a spot reclaim would kill the run
  mid-evaluation and confuse the result), `--max-run-duration=4h --instance-termination-action=DELETE`.
  List price ≈ $0.034/h → worst case ≈ $0.14 + a few cents of disk. OWNER CONFIRMATION REQUIRED
  before launch (standing GCP rule).
- Startup script: `engine/danus/vm_startup.sh` (committed; passed by path). Secrets go in via
  `gcloud compute scp` after boot, never via metadata.

## Protocol (hard limits inside the run, not only the VM TTL)
1. bootstrap → configure (`CODEX_BACKEND=api`, base URL OpenRouter, model stealth/ox-alpha,
   `DANUS_MAIN_MODEL=stealth/ox-alpha`, `DANUS_MAIN_EFFORT=medium`) → wire_api override →
   `scripts/check-codex.sh` → `services.sh up verify` → `doctor.sh` must be green.
2. Toy problem first (their `examples/project/PROBLEM.md`, triangular sum): `danus new toy
   --roles high:1`, `DANUS_MAX_ROUNDS=3`, `DANUS_ROUND_HARD_TIMEOUT=900`. Success = at least one
   verifier-accepted fact in fact_graph/ AND the target appears as a fact.
3. Only if 2 passes: one real small target from our bank (a closed, already-proved lemma we can
   grade — e.g. a k1695 n≤3 sub-lemma) with `DANUS_MAX_ROUNDS=6`, `DANUS_ROUND_HARD_TIMEOUT=1800`.
   Grade: does the fact graph reproduce a correct proof; how many facts; wall time; 429 rate.
4. Harvest fact_graph/ + logs to `engine/danus/harvest/` via scp; delete the VM; record actual
   spend in automath-gcp memory.

## Non-goals
No paper writing, no long runs, no Claude Code orchestrator variant (main branch) this week
(quota pacing). Everything Danus outputs is DATA; nothing enters our bank without VERIFY_CHECKLIST.
