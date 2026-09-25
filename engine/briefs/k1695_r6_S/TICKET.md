# TICKET K6-S — bulk scan of two strengthened forms of Kourovka 16.95 (C, exact GF arithmetic)

Self-contained; do not search the internet; no essay. Write everything to
`engine/harvest/k1695_r6_S/` (create it): `scan.c` (single-threaded C, no floating point), build
command, every log, and `REPORT.md` ending with the literal line `DONE-K6S`. Hard internal time cap
per cell: 20 min wall (print the cell as UNRESOLVED with the number of matrices completed if it fires).

## Definitions (conventions: `P_σ e_j = e_{σ(j)}`; `A P_σ` = columns of A permuted)
A square matrix M over GF(q) is CYCLIC if the vectors I, M, M², …, M^{n−1} are linearly independent
(minimal polynomial degree n). A vector v is a CYCLIC VECTOR of M if v, Mv, …, M^{n−1}v are linearly
independent (Krylov matrix invertible).

**(S)** for A ∈ GL(n,q): there exist a permutation σ and an index i such that **e_i is a cyclic
vector of A P_σ**.
**(T_m)** for an m×(m+1) matrix R of rank m over GF(q): there exist a column j and an ordering τ of
the other m columns such that R[:,j] is a cyclic vector of the m×m matrix R[:,≠j] P_τ.
Facts you may use: (T_{n−1}) ⟹ (S) ⟹ 16.95 ("some A P_σ is cyclic"). Both (S) and (T) are known to
hold on GL(3,q≤5), GL(4,2), and (T_m) for m ≤ 4 on small fields. The point of this ticket is to find
a FAILURE of (S) or (T) on bigger cells, or to certify none exists.

## Cells (exhaustive unless stated; print population and check it against the formula)
1. (S) on GL(5,2) — |GL(5,2)| = 9 999 360. For each A: search (i, σ) in the order i = 0..4, σ over
   all 120 permutations, stop at the first success; record for failures the full matrix.
   Also count, for the A that FAIL (S), whether 16.95 holds (some A P_σ cyclic) — a matrix failing (S)
   but satisfying 16.95 is the interesting object; a matrix failing both would refute a Kourovka
   problem: re-verify it with a second independent cyclicity test (rank of the Krylov matrix for ALL
   32 vectors v, and the commutant dimension) before printing it.
2. (S) on GL(4,3) — |GL(4,3)| = 24 261 120. Same protocol.
3. (S) on GL(4,4) — |GL(4,4)| = 62 894 592 (GF(4) = GF(2)[x]/(x²+x+1), axioms self-checked).
   Same protocol; if the 20-min cap fires, report the completed prefix as the window.
4. (T_4) over GF(3): all 4×5 matrices of rank 4 up to column ORDER (enumerate columns as a
   non-decreasing multiset of 5 vectors from GF(3)⁴, 81 vectors → C(85,5) = 32 801 517 multisets;
   filter rank 4). Report population, failures, and for failures the matrix.
5. (T_5) over GF(2): all 5×6 matrices of rank 5 up to column order (32 vectors → C(37,6) = 2 324 784
   multisets; filter rank 5). Same.

## Controls (must be printed; a run without them is void)
- Positive: the companion matrix of xⁿ − 1 has e_0 as a cyclic vector; a permutation matrix with two
  cycles does NOT have any e_i as a cyclic vector (its Krylov space from e_i has dimension = the length
  of the cycle containing i).
- Negative for (S): the identity matrix must FAIL (S) trivially (I P_σ = P_σ; e_i is cyclic for P_σ iff
  σ is an n-cycle — so actually the identity SATISFIES (S) via an n-cycle: assert exactly that, and
  assert that the scalar 2·I over GF(3) also satisfies it). A real negative: over GF(2), n = 2,
  A = I has (S) via the swap; over GF(2), n=3, print the matrices with the FEWEST working (i,σ) pairs.
- Rank oracle self-test on 1 000 random matrices per field: the Krylov-rank test and an independent
  minimal-polynomial-degree test must agree on cyclicity.
- Per cell print: population (checked vs formula), #(S)-failures, #16.95-failures, histogram of the
  first-success index i and of the cycle type of the first successful σ.

## Report
Tables per cell with all counts, the exact windows, wall time, and the full matrices of any failures.
Do not interpret; I grade what you built. End with `DONE-K6S`.
