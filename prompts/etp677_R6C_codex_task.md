# Task R6-C: build the first NON-idempotent non-right-cancellative 677 magma

Context: read problems/etp677/R6A_selfref_report.md (especially its Section 5
recommendation and the fibre-extension recipe) and problems/etp677/R5C_soff_report.md
(the order-176 construction it modifies).

Motivation: every known non-right-cancellative finite 677 magma (orders 176, 496,
the whole TI theta-family) is IDEMPOTENT, which makes E255 hold trivially and
renders all orbit-type conjectures vacuous. A non-idempotent non-right-cancellative
model is the first object that can genuinely test the (P) program.

Jobs:
1. Follow R6A Section 5's recipe: in the R5-C fibre framework, place a
   NON-idempotent affine 677 magma (e.g. s*t = 4s+t on F_7, verify it satisfies
   E677 and is non-idempotent first) as the d=0 fibre operation, keeping
   degenerate (a_d=0) operations at suitable other indices for
   non-right-cancellativity. Derive the compatibility conditions and solve them
   BY ALGEBRA (paper-and-pencil style, document the derivation).
2. Verify any candidate by building the full Cayley table in Python and checking
   E677 exhaustively, E255 status per element, idempotency (expect: NOT
   idempotent), and column injectivity (expect: some non-injective columns).
   Pure table checks only — NO SAT, NO exhaustive search over model spaces
   (user directive; the machine must stay light).
3. If the recipe obstructs, document the exact obstruction algebraically —
   that is also a result.
4. Apply R6A Section 5's proposed toolkit updates: append the (B5), (B6),
   (NEW-ID), (WARN) entries to prompts/etp677_R3_common.md exactly as the
   report specifies.
5. Also compute, for your new model (if found): tr N, Psi_1 = sum_x N(x\x,x),
   and whether Psi_1 <= tr N (R6A Cor 2.4 criterion) — this is the first
   non-vacuous test of the criterion.

Report: problems/etp677/R6C_codex_report.md. Honesty: PROVED / computed /
conjectured markers; document failures as precisely as successes.
