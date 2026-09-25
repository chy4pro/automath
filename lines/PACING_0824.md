# LIFTED 2026-08-29 01:2x CDT — quota reset; owner: "[owner message redacted]". Rules below are HISTORY only.

# Quota pacing mode — in force from 2026-08-24 ~10:00 CDT until the weekly reset (Aug 29, 00:00 America/Chicago)

Owner decision (08-24): the Claude weekly limit is at 91% with 5 days left. Both deep lines
STAY UP, but under the following pacing rules, which override the usual "run as long as the
work demands" default until the reset.

## Rules for line-677 and line-k1695
1. **Claude is for adjudication only.** Spend your own turns on: grading engine harvests,
   deciding what is true, writing registry entries, launching/harvesting cloud and codex work.
   Do NOT spend your turns doing exploratory derivation, literature sweeps, or long
   self-dialogue. Exploration is now the free layer's job.
2. **Delegate exploration to the free layer.** Anything of the form "try to prove/refute X",
   "search for a table/witness", "sweep the literature for Y" goes out as an engine brief in
   `engine/briefs/` (Qwen3.8-Max / ChatGPT Pro / ox-alpha / muse-spark / codex / Gemini
   SEARCH-ONLY) — then STOP your turn and wait for the harvest. These cost zero Claude quota.
   Route via SendMessage to the dialogue (`automath-f1`) or write the brief and end the turn;
   dialogue polls `engine/briefs/` every tick.
3. **Short stretches.** Cap each working stretch at one concrete deliverable (one registry
   step, one grading, one launch), then end the turn. No multi-step chains inside one turn
   unless a launched job forces a synchronous harvest.
4. **No subagents.** Do not spawn Claude subagents (Agent tool) for any reason until reset.
   Use codex (screen `codex`, gpt-5.6-sol) for verification tickets instead — its quota is
   separate.
5. **Compute is free of Claude quota.** GCP (owner-approved items, confirm-before-spend
   unchanged), local nohup jobs, codex runs — all fine. Prefer them.
6. Everything else in ARCHITECTURE.md is unchanged: model-tier discipline, Gemini search-only,
   closed-results-only publishing, no inline remote-execution shell (runner scripts live in
   the repo and are referenced by path).

Dialogue side applies the same rules to itself: no subagents, defer Claude-heavy reading
tasks (e.g. the 982 classical-literature read), keep ticks short.
