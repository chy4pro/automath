# GPT-6 Astra via local codex — case analysis and first-week plan (2026-09-05, dialogue automath-b6)

## 0. Facts checked today
- codex-cli 0.153.2, account [email] (Pro Lite); `/model` list now includes **gpt-6-astra** (config: model = gpt-5.6-sol default; `codex -m gpt-6-astra` works; reasoning high). Screen session `codex` started with `-m gpt-6-astra`; `/status` confirmed "Model: gpt-6-astra".
- **Quota: weekly limit 0% left, resets 23:00 on 6 Sep** (5h limit not shown separately for the main pool; GPT-5.3-Codex-Spark has its own 100% pools — irrelevant for math). So the first Astra attempt cannot start before Sun 6 Sep 23:00. Size of the weekly pool unknown until the first run: measure consumption via `/status` every 30 min.
- Local Lean: elan + Mathlib present (lean/etp677_ext, Lean 4.34.0-rc1, 15 GB) — Astra can compile Lean certificates locally if asked.
- FrontierMath Erdős (FME, Adamczewski–Bloom, Aug 2026): 68 conjectures / 65 problems (48 from Formal Conjectures + 18 autoformalised); the 70 Bloom numbers: 1,3,5,7,20,23,28,30,39,41,52,61,66,68,74,77,86,89,97,101,104,107,120,126,128,138,165,172,181,184,208,213,241,242,322,324,364,371,376,406,431,478,500,508,548,564,571,583,595,647,672,713,714,723,773,812,821,829,901,952,970,972,975,1003,1020,1057,1083,1159,1206,1207 (77,165,500,901 excluded as estimate-type). Lean statements: github.com/epoch-research/LeanOpenProblems.

## 1. Case analysis — what Astra actually cracked (paper Table 3 + site pages)
| # | type | result | reliability | cost/time |
|---|---|---|---|---|
| 74 | DISPROOF by construction (graph of infinite χ, every n-subgraph bipartite after O(log n/log log n) deletions; 3 distinct arguments) | refutes EHS82 | 6/6 | $47–271, 5–19 h |
| 126 | PROOF of a lower bound (f(n) ≫ n^{1/2}; 3 distinct arguments) — a problem "never seriously attacked" | closes it | 4/4 | $154–249, 8–17 h |
| 1 | DISPROOF by construction (distinct-subset-sum sets with N ≤ ε2^n) | refutes Erdős's "first serious problem" | 2/4 | $405 (27 h), $1384 (84 h) |
| 548 | PROOF (Erdős–Sós tree conjecture, famous; AKSS scaffold existed) | closes it | 1/3 | $363, 20 h |
| 571 | PROOF by construction (Turán exponents for all rationals; Bukh–Conlon scaffold) | closes it | 1/3 | $617, 41 h |
Patterns: (a) 3 of 5 are constructions (explicit witnesses; verifiable by computation + Lean); (b) every win sat on a rich partial-results literature (a "one more idea" gap); (c) the two hardest wins needed >$300 and several attempts; (d) **the other 63 conjectures survived 172 further Astra attempts (2–5 each, some >$300) with zero resolutions**. So a generic re-run of Astra on an FME problem has < 3% odds per attempt and costs 15–40 h of Astra time — probably more than one weekly Pro-Lite pool.
Where our odds are better than Epoch's: Epoch's protocol is fully autonomous (no human input, no hints). We can supply (i) campaign briefs with the literature scaffold and structural hints (prompt doctrine), (ii) our own machine evidence and finite certificates, (iii) multiple cheaper attempts on sub-goals, (iv) fast local verification (Opus referee + scripts + Lean). Partial results count for us (papers), not for FME.

## 2. Candidates, ranked (value × P(success | Astra + our brief) / quota cost)
A. **#708 hot-set-excluded sparse core (our line)** — closes "g(n) ≤ 81n for ALL n" (now n ≤ 10^980). Brief ready (engine/briefs/erdos708_r15_pro.md, 8.8 KB, with two refereed barriers and the referee's escape). Our guidance is maximal, nobody else works on it, verification is cheap. Odds maybe 15–25% per attempt; cost ~2–4 h Astra. **Recommended first run.**
B. **#23 Erdős–Faudree–Pach–Spencer** (FME; FALSIFIABLE): every triangle-free graph on 5n vertices bipartite after ≤ n² deletions; best 1.064n² (Balogh–Clemen–Lidický 2021, flag algebras). Extremal-graph type = Astra's strongest class (#548/#571); a proof would be a top-journal result. We can pre-compute flag-algebra/SDP scaffolding locally. Odds ≤ 5%; cost 15–40 h.
C. **#128 Erdős–Rousseau sparse halves** (FME; FALSIFIABLE, $250): 27/1024 (Razborov 2022) vs 1/50 — same class as B; odds similar. Pick B or C, not both, for the first FME attempt.
D. **#184 Erdős–Gallai cycle decomposition** (FME; famous; O(n log* n) Bucić–Montgomery): the "final push" pattern like #548; but survived 3–5 Astra attempts; odds ≤ 3%; cost high. Second-week option.
E. **#68 irrationality of Σ 1/(n!−1)** (FME; crisp, elementary, "never seriously attacked" flavour like #126): a cheap probe (~1 attempt, a few hours). Odds unknown (5–10%?).
F. **#324 polynomial with distinct pairwise sums** (FME; construction + proof; Ruzsa's near-miss n^5+⌊cn^4⌋): Astra-type (construction); odds ~5%.
G. #709 upper bound n^{1/2−δ}: active human group (van Doorn–Li–Tang), our two-block core is published; not for Astra now.
Not recommended for the first weeks: #3, #20, #30/#39/#241, #61, #89, #138, #508, #714, #812 (famous, no visible "one more idea" gap; each survived multiple Astra runs).

## 3. Protocol for an Astra run (codex TUI in screen `codex`, model gpt-6-astra)
1. Brief = campaign structure (TEMPLATE v2.3): pinned statement, what is proved (with file paths the agent may read), barriers, targets, verification rules, output path `engine/out/astra_<id>/` (report.md + scripts + optional Lean). Tell the agent the wall-clock cap and to write a checkpoint every 30 min.
2. Launch: `screen -S codex -p 0 -X stuff 'Read /abs/path/brief.md and carry out the attack; write results to ...'` then `stuff $'\r'`. Monitor: `hardcopy` every 30 min; `/status` for quota; stop (Esc / Ctrl-C) at the agreed quota share (default: ≤ 50% of the weekly pool per attempt, so two attempts per week are possible).
3. Harvest → Opus referee + our scripts (+ Lean when the statement is finite/elementary) before anything is recorded as a result. No publication while a line iterates (owner rule).
4. Ledger every run: problem, brief, model, hours, quota consumed, outcome (incl. failures) — the FME reporting standard.

## 4. Schedule proposal
- Sun 6 Sep 23:00 (quota reset): run A (#708 r15) first, capped at 50% of the pool or 4 h.
- If pool remains: run E (#68) as a cheap probe; else next week.
- Week of 8 Sep: one FME extremal attempt (B or C) after a day of local scaffolding (flag-algebra numerics, small-case data).
Owner decides: (1) confirm A first; (2) choose B vs C; (3) the per-attempt quota cap.

## 5. Launch protocol for the first run (prepared 09-05 18:1x; owner approved the plan 09-05 morning — no further approval needed)
Preconditions (check at 09-06 23:05): `screen -ls` shows `codex`; `/status` in the TUI shows Model gpt-6-astra and Weekly limit > 0% (the pool has just reset); the brief $HOME/workspace/claudecode/automath/engine/briefs/erdos708_r16_astra.md exists; mkdir -p engine/out/astra_708_r16.
Launch (TUI, screen `codex`, cwd = repo root):
  screen -S codex -p 0 -X stuff 'Read $HOME/workspace/claudecode/automath/engine/briefs/erdos708_r16_astra.md and carry out the attack exactly as specified there. Write checkpoint.md every 30 minutes and report.md at the end under $HOME/workspace/claudecode/automath/engine/out/astra_708_r16/. Hard wall-clock cap 3 hours from now.'
  sleep 1; screen -S codex -p 0 -X stuff $'\r'
Monitoring: every 30 min `screen -S codex -p 0 -X hardcopy <file>` + read; every 60 min `/status` (send only when the agent is idle — if "Working" is on screen, do not type; read the checkpoint file instead). STOP rule: if the weekly pool drops below 50% remaining, or 3 h elapse, send Esc (screen -X stuff $'\e') and wait for the report; if it asks for approvals (permissions "Ask for approval"), answer only for read/run-python within the repo; deny anything else. Harvest: report.md → Opus referee only if PROVED claims of weight; record cost (pool % consumed, wall time) in the ledger.
