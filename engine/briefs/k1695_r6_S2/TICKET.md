# TICKET K6-S2 — fix the (T_m) routine in scan.c, prove it correct against a reference, rerun cells 4–5

Small, precise task. Work in `engine/harvest/k1695_r6_S/` (existing `scan.c`, binary `/private/tmp/k1695_scan`,
logs in `logs/`). Output: patched `scan.c`, `logs/cell4.log` and `logs/cell5.log` REPLACED, a new
`logs/xcheck.log`, and `REPORT.md` ending with the literal line `DONE-K6S2`. Exact arithmetic only.
Do not touch cells 1–3 (they are graded). Keep your context small: do not print matrices unless asked.

## The bug
`logs/cell4.log` printed 10 511 `FAIL_T` matrices for (T_4) over GF(3). ALL of the first 200 are
FALSE POSITIVES: an independent reference implementation finds a witness for each (e.g. for
R = [[1,1,0,0,2],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]: take j = 0 (column e₀) and order the other
columns as (e₁, e₂, (2,0,0,1), e₀)… i.e. M has columns [e₁, e₂, 2e₀+e₃, e₀] and e₀, Me₀ = e₁,
M²e₀ = e₂, M³e₀ = 2e₀+e₃ are independent). Every false positive has a REPEATED column — suspect the
enumeration of orderings when two columns are equal, or the handling of the "held-out" column index
when columns are given as a multiset. Find and fix it.

## Definition to implement (verbatim)
(T_m)(R): R is m×(m+1) of rank m. R satisfies (T_m) iff there exist a column index j ∈ {0..m} and a
bijection τ from {0..m−1} to {0..m}∖{j} such that, with M the m×m matrix whose column l is column
τ(l) of R, the Krylov vectors b, Mb, M²b, …, M^{m−1}b (b = column j of R) are linearly independent.
Columns are compared BY INDEX, never by value (equal columns are different indices).

## Mandatory cross-check (the ticket is void without it)
1. Reference: `.venv/bin/python3` with `problems/k1695/round6_controllable.py` — its function
   `T_test(cols, m, F)` (cols = list of m+1 column vectors as lists; `F = GF(q)` from the same file;
   returns a witness or None) is the reference decision. Write a tiny harness that generates 3 000
   random rank-m matrices for (m,q) ∈ {(3,2),(3,3),(4,2),(4,3),(2,5)} PLUS all 10 511 FAIL_T matrices
   from the old cell4.log, runs both the fixed C routine and the reference, and prints per cell:
   count, agreements, disagreements (must be 0), and how many are (T)-true / (T)-false (both classes
   must be non-empty in at least one cell, or the check is vacuous — if the reference never returns
   None on random inputs, ADD the known-false-for-a-fixed-j inputs: R = [I_m | 1] with j forced to
   the last column is not a (T)-failure, so instead assert on synthetic inputs where you FORCE a
   single j and compare per-j verdicts: per-(R, j) agreement is the real test).
2. Only after `xcheck.log` shows 0 disagreements: rerun cell 4 ((T_4) over GF(3), all 4×5 rank-4
   matrices up to column order — column multisets, C(85,5) = 32 801 517 of which 26 485 056 rank 4)
   and cell 5 ((T_5) over GF(2), C(37,6) = 2 324 784 multisets, 1 083 264 rank 5). Print per cell:
   population (must match those numbers), failures, wall time; for each failure the matrix.
3. Report: the bug (one sentence), the xcheck table, the cell tables. End with `DONE-K6S2`.
