# TICKET K6-T2 — PROVE (T_3) over every field (⟹ Kourovka 16.95 for n = 4 in full)

Self-contained; no internet; no essay. Output to `engine/harvest/k1695_r6_T2/` (create): `REPORT.md`
ending with the literal line `DONE-K6T2`, scripts, logs. Exact arithmetic only. A proof is a chain
of lemmas each valid over EVERY field (name where the characteristic matters) with machine checks of
finite instances with controls. You are graded on what you build.

## Statement
F any field. For an m×m matrix M and b ∈ F^m, (M, b) is CONTROLLABLE iff b, Mb, …, M^{m−1}b are
linearly independent iff det[b, Mb, …, M^{m−1}b] ≠ 0.
**(T_3):** for every 3×4 matrix R of rank 3 over F there exist a column j and an ordering (c_1,c_2,c_3)
of the other three columns such that (M, b) is controllable, where M = [c_1 c_2 c_3] and b = R[:,j].
Why it matters: (T_3) ⟺ "for every A ∈ GL(4,F) and every index i some permutation σ makes e_i a cyclic
vector of A P_σ" (delete row i of A: R = A[≠i,:]; e_i cyclic for AP_σ ⟺ (A[≠i,σ(≠i)], A[≠i,σ(i)])
controllable), which implies Kourovka 16.95 for n = 4 over every field. So a proof of (T_3) closes
n = 4 entirely — no stratification needed.

## Known (use freely)
- (T_1), (T_2) hold over every field. The (T_2) proof: with b = (x_j, y_j)ᵀ and remaining columns
  (c_k, c_l) in that order, `det[b, [c_k c_l] b] = x_j·det(c_j, c_k) + y_j·det(c_j, c_l)` (∗); assuming all
  six choices fail forces relations that contradict rank 2 (β² = 1, α = −β, then 2y = 0 …).
- (T_3) has NO counterexample over GF(2), GF(3), GF(4), GF(5), GF(7), GF(8) (exhaustive) and a 77 %
  prefix of GF(9). Tightest instances over GF(2): columns [e₁, e₂, e₁+e₂, 1] (4 witnesses of 24).
- Reductions: (i) if some column of R has a single nonzero entry (row i, column j) then (T_3)(R) ⟸
  (T_2)(R[≠i,≠j]) — so WLOG every column has ≥ 2 nonzero entries; (ii) column operations that add
  multiples of the chosen b to the other columns do not change controllability of (M,b) (feedback
  invariance), so for a fixed choice of b the other columns may be reduced modulo b; (iii) row
  permutations and column permutations of R are harmless; (iv) if R = [C | Cβ] with C invertible then
  the choice b = Cβ works iff β is a cyclic vector of P_τ C for some τ ∈ S_3 (similarity by C).
- The 3×3 Krylov determinant: for M = [c_1 c_2 c_3], det[b, Mb, M²b] is a polynomial of degree 3 in the
  entries of b and degree 3 in the entries of M; expand it in the style of (∗): Mb = Σ b_i c_i,
  M²b = Σ_i b_i M c_i = Σ_{i,k} b_i (c_i)_k c_k. Derive the explicit expansion
  det[b, Mb, M²b] = Σ (products of 3×3 minors / 2×2 minors …) and USE it.
- Failure in eigenvector form: (M, b) fails iff some left eigenvector y of M (over F̄) has yᵀb = 0.

## Suggested route (report every step, including the ones that fail)
1. Reduce to the case where the 4 columns pairwise… no — do NOT assume genericity. Split by the
   kernel vector κ of R (Rκ = 0, unique up to scale): the columns with κ_j ≠ 0 are exactly those
   whose complement is invertible. Case A: some κ_j = 0 (then R[:,≠j] is singular but b = c_j may
   still work — handle it); Case B: all κ_j ≠ 0 (all four 3×3 minors nonzero).
2. In Case B use (iv): for each j, the question is whether β^{(j)} := −κ_{≠j}/κ_j is a cyclic
   vector of P_τ C_j for some τ ∈ S_3 (six τ's, four j's = 24 choices). Write the Krylov determinant
   for the 3-cycles and transpositions explicitly in terms of C_j and β^{(j)}, and show the 24
   determinants cannot all vanish when rank R = 3. Watch characteristics 2 and 3 separately.
3. Machine-check every derived identity and every case lemma exhaustively over GF(2), GF(3), GF(4),
   GF(5) (all 3×4 rank-3 matrices, ~10⁷ at GF(5) — fine in C; in Python use column multisets) with
   the negative control "restrict to a single fixed (j, τ)" which must fail.
4. If a case resists, state the exact residual and print the smallest configuration that you cannot
   close — that is a result. End with `DONE-K6T2`.
