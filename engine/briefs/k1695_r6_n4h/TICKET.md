# TICKET K6-N4h — rank-1 stratum (a) at n = 4 through (T_3) for "partial identity + rank one"

Self-contained; no internet; no essay. Output to `engine/harvest/k1695_r6_n4h/` (create): `REPORT.md`
ending with `DONE-K6N4H`, scripts, logs. Exact arithmetic; sympy available. Every lemma: proof over
every field + machine check with a control that can fail.

## Why this route
For A ∈ GL(4,F), "e_i is a cyclic vector of A P_σ for some σ" (which implies 16.95 for A) is equivalent
to (T_3) for the 3×4 matrix R = A[≠i, :] (delete row i): ∃ column j and ordering τ of the other three
columns with R[:,j] a cyclic vector of R[:,≠j] P_τ (Krylov vectors b, Mb, M²b independent). [Deflation:
the Krylov vectors of e_i under AP_σ, projected off coordinate i, are b, M'b (+ multiples of b), …]
For A = I + uvᵀ (u, v ∈ F⁴, 1 + vᵀu ≠ 0) and i = 4 (WLOG by relabelling; you may choose ANY i, and
different i give different R — use that freedom): with u′ = (u₁,u₂,u₃), v′ = (v₁,v₂,v₃):
  R = [I₃ | 0] + u′ vᵀ, i.e. columns c_j = e_j + v_j u′ (j = 1,2,3) and c₄ = v₄ u′.
This is (T_3) for a 3×4 matrix that is a rank-one update of a partial identity — a tiny structured
family. Prove (T_3) for it (over every field), and 16.95 for rank-1 A at n = 4 follows.

## Facts to start from (prove them; they are easy)
F1. If v₄ ≠ 0 and b = c₄ ∝ u′, M = (I + u′v′ᵀ)P_τ = P_τ + u′ w′ᵀ (w′ = P_τᵀ v′): then
    Krylov(M, u′) = Krylov(P_τ, u′) (induction: M^k u′ ∈ P_τ^k u′ + span(u′, …, P_τ^{k−1}u′)). So b works
    iff u′ is a cyclic vector of P_τ, iff τ is a 3-cycle and u′ ⊥ no eigenvector of P_τ — i.e. iff
    Σu′ ≠ 0 and û(ω) := u′_{τ⁰} + ω u′_{τ¹} + ω² u′_{τ²} ≠ 0 for the primitive cube roots ω (char ≠ 3;
    if ω ∉ F this just says u′ is not constant on the 3-cycle… work out both orientations); in char 3
    iff Σu′ ≠ 0 (x³ − 1 = (x − 1)³).
F2. If b = c_j = e_j + v_j u′ (j ≤ 3) and M has columns {c_k, c_l, c₄} in some order: write out
    Krylov(M, b) explicitly (3 vectors in F³, entries polynomial in u′, v) and its determinant
    D_{j,τ}(u, v) — a polynomial of low degree; compute all 18 such determinants symbolically (sympy over
    ℤ[u₁..u₄, v₁..v₄]) and print them.
F3. The choice of the deleted row i: the four matrices R^{(i)} = A[≠i,:] give four families; the
    statement needed is that for SOME i and SOME (j, τ) the determinant is nonzero. So the target is:
    the 4 × 24 = 96 polynomials D_{i,j,τ}(u, v) have no common zero with 1 + vᵀu ≠ 0, u ≠ 0, v ≠ 0.

## Method
1. Use F1 to dispose of every (u, v) with some i such that v_i ≠ 0, Σ_{k≠i} u_k ≠ 0 and u restricted to
   [4]∖{i} is not "geometric along both 3-cycles" (make this exact). Characterise the residual set
   E₁ = {(u, v): F1 fails for every i} explicitly (it is small: e.g. v has ≤ 1 nonzero entry, or u has
   all 3-subsums zero, or u is constant on triples…). Handle char 3 separately.
2. On E₁, use the F2 determinants: show by direct algebra (sympy: Gröbner over ℚ and over GF(p) with
   Rabinowitsch for 1 + vᵀu ≠ 0 and the E₁ defining conditions as equations, or by hand) that some
   D_{i,j,τ} ≠ 0. The all-equal-token case u = a𝟙, v = b𝟙 is PROVED elsewhere (aI + bJ theorem) — cite
   it and exclude it, or better, re-prove it here in this language (it should be easy: F1 with any i
   needs Σ_{k≠i} u = 3a ≠ 0 and û(ω) = a(1 + ω + ω²) = 0 — so F1 FAILS for the all-ones case, and the
   witness must come from F2 or from a different structure; that is the (n−1,1)/n-cycle theorem in
   disguise; do it).
3. Machine check: exhaustive over all invertible I + uvᵀ over GF(2), GF(3), GF(4), GF(5), GF(7) (the
   populations N_q = (q⁴−1)/(q−1)·(q⁴−1−q³) are known: 105, 2120, 16235, 77844, 822800): for each,
   verify that the rule you extract (which i, j, τ) yields a Krylov-cyclic e_i, with the independent
   power-rank cyclicity oracle on AP_σ and the "always P = I" control.
4. Report per lemma with proofs; UNRESOLVED residual sets printed exactly. End with `DONE-K6N4H`.
