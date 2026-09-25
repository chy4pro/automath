# Danus × ox-alpha — evaluation result (living document; owner-directed 2026-08-24)

## Stage 1–2 (toolchain + toy problem) — DONE 12:4x CDT

**Verdict: Danus runs end-to-end on ox-alpha as the ONLY model, and its verifier-gated fact graph
accepted the toy target in round 1.** Throughput is bounded by free-pool rate limits.

What it took to get there (all sidecar/runtime config; upstream Danus untouched):
| obstacle | fix |
|---|---|
| Danus requires Linux + tmux + `--dangerously-bypass-approvals-and-sandbox` | disposable GCP VM `danus-eval-1` (e2-medium, 4 h TTL, auto-delete; owner-approved ≈$0.14) |
| codex-cli 0.149 dropped `wire_api = "chat"`; OpenRouter `/responses` for `stealth/ox-alpha` returns 429 ~5/6 of the time | LiteLLM proxy on loopback as a Responses→chat bridge; primary OpenRouter, fallback opencode `ox-alpha-free` |
| codex sends a `web_search` server tool → OpenRouter 400 "Server tool request failed" | `web_search = "disabled"` at TOP LEVEL of codex config.toml (appending it after a table header silently puts it in the wrong table) |
| OpenRouter 400 "Reasoning is mandatory … cannot be disabled" | `model_reasoning_effort = "medium"` in config.toml |
| `pkill -f <pattern>` inside an ssh `--command` kills the invoking shell (pattern matches itself) — bitten twice | restart logic lives on the VM as `restart_litellm.sh` |

Measured:
- `codex exec` smoke test over the bridge: "PONG", 9,436 tokens. Tool calling works (ox-alpha
  returned a proper `tool_calls` for a function tool on OpenRouter).
- Toy project (`triangular-sum`, 1 worker `high`, MAX_ROUNDS=3, ROUND_TIMEOUT=900):
  - **Round 1: worker produced the target theorem with a correct induction proof; the Danus
    verifier (also ox-alpha, medium) accepted it → 1 fact in `fact_graph/facts/`, `POST /verify 200`.**
  - Rounds 2 and 3: died immediately on `exceeded retry limit, last status: 429 Too Many Requests`
    — the OpenRouter shared free pool; the opencode fallback fails on tool-bearing requests
    ("Internal server error"), so there is effectively one pool.
  - **Quality red flag:** the accepted fact's `external_refs` cites Mochizuki, "Construction of
    Arithmetic Teichmüller Spaces IV: Proof of the abc-conjecture" (arXiv 2403.10430) "Lemma
    6.3.1(1)" as corroborating context for the triangular-number identity. A hallucinated,
    absurd citation; harmless here (non-load-bearing, the proof is self-contained) but exactly the
    kind of thing our VERIFY_CHECKLIST would have to strip before anything reaches a bank.
- Harvest: `engine/danus/harvest/toy/` (fact_graph + round logs).

## Stage 3 (a real, already-graded problem) — RUNNING from 12:5x CDT
Project `k4rec`: PROBLEM.md = `engine/briefs/k1695_r4_reciprocal/BRIEF.md` (GF(2) reciprocal-root
placement — codex's answer was graded and banked by line-k1695 today as R4.5, so Danus's output can
be graded against a known-correct table/construction/proof). 1 worker, MAX_ROUNDS=4,
ROUND_TIMEOUT=1500. Grade on harvest: facts produced, whether any is the construction or a proof,
429 casualties, and citation hygiene.

### Stage 3, first harvest (13:0x CDT) — the decisive finding
`k4rec` round 1 produced ONE fact, accepted by the Danus verifier (`fact 465931fe71b94b12`,
harvested to `engine/danus/harvest/k4rec/`). **The fact's proof is wrong**, on two counts:
1. The "k distinct positions" are the pairs {jg,(j+1)g}, j=0..r−1 — interior vertices appear
   twice, so the placement has 2 positions, not k (and in char 2 the polynomial telescopes to
   1 + x^{rg}).
2. "1+λ^g ≠ 0 ⟹ P(λ) ≠ 0" ignores the second factor Σ_{j<r} λ^{jg}, which vanishes whenever
   ord(λ) | r (e.g. k=6, n=9: λ of order 3 kills it — exactly k1695's banked k=6 failure cells).
The Danus verifier (ox-alpha, medium effort) accepted it. **Danus's "verifier-gated truth" is
only as strong as the verifier model; with ox-alpha as the verifier it is not a certificate.**
This is the single most important datum of the evaluation and it is why nothing from Danus can
enter our bank without our own VERIFY_CHECKLIST (executable checker + negative control, or Lean).

Backend note (owner asked to prefer opencode): opencode `ox-alpha-free` supports function tools
and streaming directly, but codex-sized prompts (~16k tokens) get HTTP 503 "Endpoint is
unavailable" from it (2/2), while OpenRouter's shared pool 429s intermittently. The bridge now runs
opencode primary + OpenRouter fallback; both pools are flaky at codex scale, so rounds die on
"exceeded retry limit" roughly two times in three. ox-alpha-on-free-endpoints is not a stable
worker backend for an agent swarm; it is fine for single-shot briefs.

## Closed 13:1x CDT — owner verdict: "用处不大" (not worth pursuing now)
VM `danus-eval-1` deleted at 13:1x CDT (≈1.5 h of e2-medium ≈ $0.05 list; actual PENDING Console
reconciliation). k4rec was stopped in round 1 (still working, 1 fact = the wrong one above); its
state is harvested under `engine/danus/harvest/k4rec/`. Local clone kept at
`~/workspace/claudecode/danus-eval` (no secrets in it: config/*.env are gitignored and only ever
held the OpenRouter/opencode keys — rotate them if that ever changes).

What would change the verdict (recorded so the question is not re-litigated from scratch):
- a worker/verifier model that is actually strong (the paper's win was GPT-5.6-sol workers);
  Danus supports `CODEX_BACKEND=chatgpt` natively, i.e. our codex subscription, no bridge — but
  that competes with the codex quota we spend on verification tickets;
- or a free pool without rate limits at codex prompt sizes. Neither exists today.
Its ideas we did take: one-brain-per-line, refuted steps as a search asset, disjunctive targets.

## Interim conclusion (subject to stage 3)
- The architecture works with a free model in the loop; the *binding constraint is the free
  pool's rate limit*, not the software. With a paid/quota-backed backend (ChatGPT-subscription
  codex login is supported by Danus natively — `CODEX_BACKEND=chatgpt`) the bridge is unnecessary.
- Nothing Danus produces enters our bank without VERIFY_CHECKLIST; its verifier is one more
  opinion, not a certificate.
