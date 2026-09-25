# TICKET K6-LEAN4 — complete Lemma T in Lean: T1 (both directions), the other direction of T2, T4 in general degree

Continue in `lean/proofenv` (Mathlib). Existing files `K1695/TranspositionLemma.lean` and
`K1695/CyclicVectorThree.lean` must stay green; add ONE new file `K1695/TranspositionLemmaFull.lean`
importing the first. Deliver: the file, `lake env lean K1695/TranspositionLemmaFull.lean` output with
`#print axioms` for every theorem (no axiom beyond [propext, Classical.choice, Quot.sound]),
`lake build` green, `engine/harvest/k1695_r6_lean4/REPORT.md` ending with the literal line
`DONE-K6LEAN4`. No `sorry` in anything listed as proved. Budget ~3 h; keep what compiles.

Notation as in TranspositionLemma.lean: K field, n, a ≠ b, d = transpositionVector a b,
P_τ = transpositionMatrix a b, E := A − μ•1, and by L2: rank(A*P_τ − μ•1) = rank(E + μ•vecMulVec d d).

**M1 (rank-one update, decrease direction — general).** For E, x, y: if `x ∈ range E.mulVecLin`,
`y ∈ range Eᵀ.mulVecLin`, and there is z with `E *ᵥ z = x` and `1 + y ⬝ᵥ z = 0`, then
`rank (E + vecMulVec x y) = rank E − 1` (and conversely: if x ∈ range E, y ∈ range Eᵀ but
`1 + y ⬝ᵥ z ≠ 0` for one (equivalently every) such z, then rank is unchanged). Prove: the
well-definedness of `y ⬝ᵥ z` on the solution set (any two solutions differ by a kernel vector k,
and `y ∈ range Eᵀ` gives `y ⬝ᵥ k = 0`); the kernel of E + xyᵀ is `ker E ⊕ ⟨z⟩` in the drop case.
**M2 (rank-one update, "one side out").** If `x ∈ range E` or `y ∈ range Eᵀ` then
`rank (E + vecMulVec x y) ≤ rank E` (the image is inside range E, resp. the transpose argument).
**T2 other direction.** With μ ≠ 0, `rank E = n − 2`: if `d ∈ range E` or `d ∈ range Eᵀ` then
`rank (A*P_τ − μ•1) ≤ n − 2` (from M2 + L2). Together with `l6prime_t2_corrected` this is the full
iff of T2.
**T1 (full).** With μ ≠ 0, `rank E = n − 1`: `rank (A*P_τ − μ•1) = n − 2` iff
[`d ∈ range Eᵀ` ∧ `μ•d ∈ range E` ∧ ∃ z, E *ᵥ z = μ•d ∧ 1 + d ⬝ᵥ z = 0]. (Use M1, M2, L6a.)
**T4 general degree (the hard inclusion).** F ⊆ K fields, A over F, μ : K with minimal polynomial
m over F of degree k ≥ 1 (use `minpoly F μ`, `IsIntegral`), w : Fin n → F, z : Fin n → K with
`(A.map (algebraMap F K) − μ•1).mulVec z = w.map (algebraMap F K)`. Then
`∃ z₁ : Fin n → F, w = (aeval A m).mulVec z₁`. Route: either (a) generalise the K6-LEAN2 argument
to the power basis 1, μ, …, μ^{k−1} (`Algebra.adjoin.powerBasis` / `PowerBasis` of `F⟮μ⟯`, coordinates
of each `z i` in that basis, comparing coefficients using the reduction of μ^k by m), or (b) the
module-theoretic argument: the F[X]-module map given by A; if it is too heavy, prove the cubic case
k = 3 explicitly (same pattern as the quadratic one) and say so. The trivial inclusion
`(aeval A m).mulVec z₁ ∈ col(A − μ)` (m(A) = (A − μ)·h(A)) should also be proved.
Add one `example` per theorem at n = 4 to show non-vacuity.

## Report
Theorems with names, PROVED / NOT PROVED, axioms, build log. End with `DONE-K6LEAN4`.
