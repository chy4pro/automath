# Task R5-A-impl (ETP 677 campaign, Round 5)

Read first: prompts/etp677_R5A_brief.md, problems/etp677/r5a_search.py, and
section 13.1 of problems/etp677/blueprint_ch13.txt.

Context: we hunt a finite 677 magma violating E255 as a fiber extension over
the exceptional base 5x-4y+1 on F_31 (the only translation-invariant base with
no idempotents). Status: TI assignment m=3,4 admit NO extension at all
(SAT-proved); shift-ansatz (fibers s+g_d(t-s)) UNSAT for Z5, Z7 (Z9 and F16
still running); general-table TI m=5 and non-TI (pair-indexed) m=4,5 kissat
runs in flight (do not duplicate raw kissat on the same CNFs).

## Jobs, in priority order

1. **ADVERSARIAL CHECK of root algebra.** Independently re-derive from
   blueprint eq (4):
   - the TI quadruple formulas and pair subscripts implemented in
     r5a_search.py functions `quads()` and `pair_subs()`;
   - the claim that E255-violation at fiber point s0 means:
     for all tau, `T[25][tau][s0] != s0`, where op index 25 = c/A (c=1, A=5);
   - the derangement reduction in `gen3` (violation iff g_25 fixed-point-free).
   Report any discrepancy IMMEDIATELY at the top of your report.

2. **Specialized backtracking searcher** exploiting functional structure:
   each eq-4 instance determines `T[D1(d)]` from `T[D2(d)], T[D3(d)], T[D4(d)]`
   whenever `s -> w3(s,t)` is injective for each t (then T[D1] row t is the
   inverse on the image). DFS over seed ops with propagation and symmetry
   breaking (simultaneous relabeling of M fixing s0=0). Target: general TI
   tables m=5 WITH the violation constraint. Decide UNSAT or find a model.

3. If m=5 decided UNSAT, run m=7 with the same machinery.

4. **Verification duty**: any model found must be verified by rebuilding the
   full 31m-order magma and checking E677 on all pairs plus listing E255
   failures (see `verify` subcommand in r5a_search.py for the pattern).

Write your report to problems/etp677/R5A_codex_report.md.
Honesty rules: mark each claim PROVED / computed / conjectured; never present
a partial search as a classification. Use background terminals for long runs
and checkpoint so work survives interruption.

## RESUME NOTE (added 2026-08-17 10:12 CDT after machine reboot)

Your prior session's work SURVIVED in problems/etp677/: r5a_bt.c / r5a_bt
(compiled), r5a_local.c, r5a_audit.py, r5a_verify_bt.py, run_r5a_bt_m5.sh,
and checkpoints in R5A_bt_m5/ (resumable shard status files).
Division of labor now:
- ROOT (Claude) is already running run_r5a_bt_m5.sh in the background —
  do NOT run it yourself or touch R5A_bt_m5/ shard files.
- YOUR remaining jobs: (1) write the adversarial-check findings from job 1
  (re-derivation of quads/pair_subs/violation/derangement reductions) into
  problems/etp677/R5A_codex_report.md NOW — even if partial; (2) build the
  m=7 variant of the sharded searcher (new dir R5A_bt_m7, do not launch the
  full run yet — just prepare and smoke-test one shard); (3) document r5a_bt's
  algorithm and shard semantics in the report so root can interpret shard
  results independently.
