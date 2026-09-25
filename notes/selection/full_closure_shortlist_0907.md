# Full-closure shortlist — 2026-09-07 (owner question: "有彻底完成的高影响力猜想么？" → none yet; this is the plan to change that)

## 1. Screen (fresh data, teorth/erdosproblems pulled 2026-09-07 07:20 UTC)
- 1217 problems; open 589, falsifiable 25, decidable 9, verifiable 7 (the 41 "finite-shape" ones are the natural full-closure targets:
  a construction, counterexample or finite computation ends the problem).
- Exclusions applied: FrontierMath-Erdős list (68; Astra already spent ~3 attempts each on the 56 unsolved), Star Fleet Math's 27
  "Solution Proposed", VibeMathed's Erdős entries, our own lines. 27 finite-shape problems survive; each page + forum read (scratchpad/ep_pages).
- Verdict on the 27: **no confident 2-hour full-closure target.** Famous-hard (Erdős–Faber–Lovász #19, Erdős–Gyárfás #64, Tuza #167,
  Grimm #375, Brocard #398, Erdős–Lovász–Tihany #628, Gyárfás tree packing #743, AMSE unimodality #993, convex distances #982/#1082,
  lemniscates #114/#1041, LKS #580, Bondy–Erdős #556, Murty–Simon #742, Graham rearrangement #475) or "decidable" only in the sense that
  an ineffective large-n theorem exists (thresholds not explicit ⇒ no finite computation in practice), or crowded (#488 31 comments,
  #617 7 claims, #699 2 claims, #287 Lean-verified reduction to M > 4·10^9 by RexHannes, #506 active computational thread).
  Only #307 (two prime sets with product of reciprocal sums = 1; verifiable) is a clean elementary search target — low visibility, and the
  search is heuristically hopeless without a structural idea (P determines Q through factoring the numerator).
- Lesson: everything "closable and untouched" among Erdős problems has been picked over by FME, Star Fleet, Tao's community and
  VibeMathed's 87 solved entries. A first-pass filter no longer finds cheap complete closures.

## 2. Decision (no owner approval needed; decide-and-reflect)
1. **#708**: Lean gate (Prove2Me mission 5204b3d1, Astra run started 02:34) then freeze. No more constant-chasing.
2. **Astra weekly pool (96%) → famous falsifiable/constructive problems with our harness edge**, one 2-hour PROOF CAMPAIGN each,
   v2.4 route table + judge, prove-or-refute at equal rank, machine tools supplied in the brief:
   - **#324** (polynomial with all pairwise sums f(a)+f(b), a<b, distinct; Ruzsa's near-miss) — construction + injectivity proof;
     our exact-arithmetic verification is cheap. First run tonight.
   - **#23** (Erdős–Faudree–Pach–Spencer: triangle-free on 5n vertices → bipartite after ≤ n² deletions; best 1.064n²) — needs
     flag-algebra/SDP scaffolding (venv cvxpy+scs) prepared by the dialogue before dispatch.
   - **#128** (Erdős–Rousseau sparse halves, $250; 27/1024 vs 1/50) — same class; pick after #23's outcome.
   - **#68** (irrationality of Σ 1/(n!−1)) — cheap probe, no tooling edge.
   Honest expectation: FME measured Astra at 5 closures per 68 problems with ~3 attempts each; our harness adds tools and judge rules,
   not new mathematics. Expected full closures from four runs ≈ 0.2–0.4. This is the highest-value use of the pool nonetheless.
3. Dashboard gets two columns (彻底完成 / 部分进展) so partial results are never presented as closures.

## 3. Bookkeeping
- Candidate table with statements: scratchpad/full_closure_cands.json (27 rows) — copy into this folder if a line is opened.
- G2 for #324 done 02:5x (page + forum read; VibeMathed/Star Fleet: none) — see the brief engine/briefs/erdos324_r1_astra.md.
