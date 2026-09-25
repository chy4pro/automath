# automath-sandbox — QUARANTINE ZONE for untrusted engines (user order 2026-08-22)

The user does not yet fully trust the new engines (ox-alpha, muse-spark-1.2). Rules:

1. **Engines NEVER write into the main repo** (`~/workspace/claudecode/automath`). All
   engine output lands here: `out/ox-alpha/`, `out/muse-spark/`.
2. **Briefs** (outbound prompts) live in `briefs/` — they MAY quote repo content
   (outbound is fine); inbound results are quarantined.
3. **Promotion path**: engine output → Claude-side adjudication (owner/planner 亲核,
   normal S3 discipline) → verified content is REWRITTEN by a Claude agent into the
   repo (never copied blindly) → the sandbox file gets a `PROMOTED-to: <repo path>`
   header. Un-promoted material stays here indefinitely.
4. **Engine roles** (user order): ox-alpha = free/unlimited → VOLUME (mass parallel
   attack drafts, wide sweeps, first-pass reviews, probes). muse-spark-1.2 = high but
   finite quota → PRECISION (targeted subproblems, cross-family S3 votes; it counts as
   the Meta judge family; ox-alpha does NOT count toward cross-family gates while its
   lab identity is unknown).
5. **API access**: keys in `~/.automath_engine_keys` (chmod 600, outside repo — never
   commit or quote them). Endpoints: OpenRouter `stealth/ox-alpha`;
   opencode go `https://opencode.ai/zen/go/v1/chat/completions`, model
   `muse-spark-1.2-contributor`. Ops: max_tokens ≥ 8000 (reasoning burn); word-cap long
   answers in briefs; retry once on 5xx; back off on rate-limit signals.
6. These are API engines — no Chrome lease needed; parallel batch calls are cheap.
   Long computations still obey the repo's hard-timeout/log-to-disk rules
   (`scripts/` here, logs beside outputs).

7. **Rate-limit preset (dialogue diagnostic 08-22)**: empty raw body / "API-ERROR:
   unknown" with 0-byte output = burst-rate DROP, retryable, never a verdict (probe
   showed endpoint healthy). Concurrency cap 4 to start (`engine_batch.sh`, stagger 5s,
   exponential backoff 15/45/135s inside engine_call_big.sh); step up only after a
   clean batch. Distinguish from reasoning-burn: burn has a NON-empty raw with
   finish=length and a preserved trace; drop has an empty raw.


## 2026-08-24 — merged into the main repo (owner order)
This directory is now `<repo>/engine/` (formerly `~/workspace/claudecode/automath-sandbox/`;
that old path is a compatibility symlink). Discipline unchanged: engine output is DATA,
audited before promotion into problems//notes//papers. Old v4 briefs/harvests moved to
briefs/archive_v4/ and harvest/archive_v4/. Junk went to
~/workspace/claudecode/automath-trash-20260824/ (reversible; purge after a few quiet days).
