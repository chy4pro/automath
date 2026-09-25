# BRIEF K6-LIT — literature search (Gemini / search engines only; NOT a mathematics task)

Purpose: find prior appearances of three statements so that nothing is later claimed new by mistake.
Output: a list of candidate references with EXACT bibliographic data (author, title, venue, year,
DOI/arXiv id) and, for each, a one-line quote of the statement as it appears there; label every item
FOUND-EXACT / FOUND-RELATED / NOT-FOUND. Do not summarise the mathematics; do not judge correctness.
Search both recent (2020–2026) and classical sources; MathOverflow / MathStackExchange included.

1. **Column-ordering / cyclic-vector statement.** "For every m×(m+1) matrix R of rank m over a field
   there is a column b and an ordering of the remaining columns as a square matrix M such that b is a
   cyclic vector of M (the pair (M, b) is controllable)." Equivalent: "for every invertible n×n matrix A
   and every standard basis vector e_i there is a permutation matrix P such that e_i is a cyclic vector
   of AP." Keywords: controllable pair, permutation of columns, cyclic vector, standard basis vector,
   Popov–Belevitch–Hautus, Krylov matrix, column permutation, "controllability under permutation",
   structural/generic controllability (Lin 1974; Shields–Pearson; Glover–Silverman) — note these are
   about GENERIC entries; we need FIXED entries.
2. **Transposition lemma.** "If P is the permutation matrix of a transposition (a b) and
   d = e_a − e_b then P = I − ddᵀ; hence rank(AP − μI) = rank((A − μI) + μ ddᵀ), a rank-one update, so
   AP can be derogatory only at an eigenvalue of A, with exact conditions by geometric multiplicity."
   Keywords: transposition matrix rank-one update, "I − (e_a − e_b)(e_a − e_b)^T", derogatory,
   nonderogatory, geometric multiplicity, rank-one perturbation of eigenvalues (R. C. Thompson 1980;
   Bunch–Nielsen–Sorensen 1978; Bru–Cantó–Urbano 2015), "swap two columns" nonderogatory.
3. **Invariant-factor statement.** "If an invertible matrix A over a field has invariant factors
   (m, m) with m irreducible (e.g. a 4×4 matrix whose minimal polynomial is an irreducible quadratic),
   then for every transposition P the product AP is nonderogatory (cyclic)." Keywords: invariant
   factors, companion matrix direct sum C_m ⊕ C_m, permutation of columns, cyclic matrix, "Thompson's
   conjecture" cyclic matrix Kourovka 16.95 (disambiguate from the conjugacy-class-size Thompson
   conjecture), Dixon 2016 arXiv:1606.02238 (withdrawn), Stasinski.
Also run the object-key openness re-check: any 2025–2026 item mentioning "Kourovka 16.95" or
"Thompson" + "cyclic matrix" + "permutation matrix" (arXiv, MathOverflow, blogs, X/Twitter, GitHub).
Report "NOT-FOUND" per item with the queries used.
