# TICKET K6-N4i — rank-2 stratum (a) at n = 4 through (T_3) for "partial identity + rank two"

Self-contained; no internet; no essay. Output to `engine/harvest/k1695_r6_n4i/` (create): `REPORT.md`
ending with `DONE-K6N4I`, scripts, logs. Exact arithmetic; sympy available. Every lemma: proof over
every field + machine check with a control that can fail.

## The route (same as K6-N4h, rank two)
For A ∈ GL(4,F), "e_i cyclic for some A P_σ" (⟹ 16.95 for A) ⟺ (T_3) for R = A[≠i,:]: ∃ column j and
ordering τ of the other three columns with b = R[:,j] a cyclic vector of M = R[:,≠j]P_τ
(det[b, Mb, M²b] ≠ 0). For A = I + UWᵀ (U, W ∈ F^{4×2}, rank 2, det(I₂ + WᵀU) ≠ 0) and i = 4:
  R = [I₃ | 0] + U′ Wᵀ, U′ = U[≠4, :] (3×2): columns c_j = e_j + U′ w_j (w_j = row j of W, j ≤ 3),
  c₄ = U′ w₄.
Closed already (cite, do not redo): S = I₂ + WᵀU scalar; spec S = {1,1}; the conjugate-eigenvalue case;
and the two characteristic-2 cover patterns of K6-N4f (all with a transposition or double-transposition
witness). What remains is a field-uniform proof for (β-rat)/(γ)/(δ) — but THIS ticket does not
stratify by S at all: prove (T_3) for the family R directly.

## Facts to start from
G1. If w₄ ≠ 0 then c₄ = U′w₄ ∈ col U′ =: X′ (2-dim). With b = c₄ and M = (I + U′W′ᵀ)P_τ (W′ = W[≤3,:]),
    M = P_τ + U′ (W′ᵀP_τ): a rank-TWO update of P_τ. Krylov(M, b) for b ∈ X′: compute
    M b = P_τ b + U′ (W′ᵀP_τ b) ∈ P_τ b + X′, M²b ∈ P_τ² b + P_τ X′ + X′ … — derive the exact criterion
    for det[b, Mb, M²b] ≠ 0 in terms of (P_τ, X′, the 2×2 matrices W′ᵀ P_τ U′ …). Note the "2-dim
    cyclic subspace" structure: b, Mb, M²b span F³ iff … (use that X′ is 2-dimensional and P_τ moves it).
G2. If w₄ = 0 (c₄ = 0): then b = c₄ is useless; use b = c_j (j ≤ 3): M = [the other two c's and 0] —
    a matrix with a zero column; Krylov(M, b) with M singular… handle it (rank 2 of R forces structure).
G3. The freedom of the deleted row i (4 choices) and of j, τ (24 choices) — 96 determinants
    D_{i,j,τ}(U, W); compute them symbolically (sympy over ℤ[u_{kl}, w_{kl}], 16 variables) and study
    their common zeros subject to rank(UWᵀ) = 2 and det(I₂ + WᵀU) ≠ 0. Use the symmetries: GL₂ acting
    by U ↦ UG, W ↦ WG⁻ᵀ (same A), coordinate relabelling (S₄), transpose (U ↔ W).
    Normalise: U′ or W in reduced column echelon form to cut variables.

## Method
1. Prove a clean sufficient criterion from G1 (e.g. "if some row i has w_i ≠ 0 and the 2-plane X′_i
   is not P_τ-invariant for some 3-cycle τ then … "), characterise the residual set exactly, and
   push the residual set through G2/G3 (Gröbner with Rabinowitsch, sympy, per characteristic ℚ and
   GF(2,3,5,7,11,13), capped 10 min / 4 GB each; state caps).
2. Machine check exhaustively over all rank-2 A over GF(2) (2 590 distinct), GF(3) (477 750), and
   ≥ 10⁵ presentations over GF(4), GF(5), GF(7): the rule (i, j, τ) yields a Krylov-cyclic e_i;
   independent power-rank cyclicity oracle; "always P = I" control.
3. Report: lemmas with proofs; residual sets printed exactly; UNRESOLVED where applicable. End with
   `DONE-K6N4I`.
