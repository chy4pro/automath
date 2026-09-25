# K6-GC-LEAN — write a Lean 4 / Mathlib proof of the Δ-lemma and (GC₃) (the line compiles and kernel-checks it)

Target statements (Lean 4, current Mathlib; no `sorry`, no new axioms). You cannot run Lean here:
write complete code, keep every lemma small, prefer `ring`/`linear_combination`/`field_simp`/`decide`-free
algebra, and avoid tactics whose names you are unsure of. Return ONE file `GoodCount3.lean`.

## Lemma 1 (Δ-lemma, pure algebra over a field K)
For x y : K × K write `br x y := x.1 * y.2 - x.2 * y.1` (the 2×2 determinant) and, for three vectors
x₁ x₂ x₃ : K × K, `Δ i j k := (x_i).1 * br x_i x_j + (x_i).2 * br x_i x_k`.
Hypothesis: x₁, x₂, x₃ span K² — encode as: NOT all three pairwise brackets vanish, i.e.
`¬ (br x₁ x₂ = 0 ∧ br x₁ x₃ = 0 ∧ br x₂ x₃ = 0)` together with the fact that if two of them are
collinear with a nonzero third … (simplest faithful encoding: `br x₁ x₂ ≠ 0 ∨ br x₁ x₃ ≠ 0 ∨ br x₂ x₃ ≠ 0`).
Conclusion: at least two of the six values Δ(1,2,3), Δ(1,3,2), Δ(2,1,3), Δ(2,3,1), Δ(3,1,2), Δ(3,2,1)
are nonzero — encode as a disjunction over the 15 pairs, or as a `Finset.filter` card ≥ 2.
Proof sketch (all fields, characteristic 2 included): if some x_i = 0 the other two have nonzero bracket
and give one nonzero Δ each. Otherwise call i silent if both its Δ vanish; for x_i = (p,q), silence is
p·A + q·B = 0 and q·A + p·B = 0 with A = br x_i x_j, B = br x_i x_k, so (p² − q²)·A = (p² − q²)·B = 0;
p² ≠ q² would force A = B = 0, all collinear, contradiction; hence silent ⇒ p² = q² ⇒ (p−q)(p+q) = 0.
Two silent vectors are linearly independent (otherwise the bracket with the third vanishes). In
characteristic 2, p² = q² ⇒ p = q so two silent vectors are dependent — impossible. In characteristic ≠ 2
write x₁ = a(1,1), x₂ = b(1,−1) after scaling; silence of both forces x₃ = (a−b, a+b) and then
Δ(3,1,2) = Δ(3,2,1) = −4a²b ≠ 0. (You may instead give a direct polynomial argument avoiding the
normalisation, e.g. via `linear_combination` certificates.)

## Theorem (GC₃)
For K a field and A : Matrix (Fin 3) (Fin 3) K with `IsUnit A.det`, there exist two distinct
σ τ : Equiv.Perm (Fin 3) such that e₁ is a Krylov-cyclic vector for A * σ.permMatrix K and for
A * τ.permMatrix K, i.e. `det ![e₁, B e₁, B² e₁] ≠ 0` for B each of those (state it with
`Matrix.mulVec` and `Matrix.det` of `Matrix.of ![…]`; Mathlib's `Equiv.Perm.permMatrix` indexes by the
inverse permutation — either convention is acceptable as long as the statement quantifies over all
permutations). Reduction to Lemma 1: with x_i := (A 1 i, A 2 i) (rows 2,3 of column i in 0-based Fin 3
indices 1,2), det(e₁, Be₁, B²e₁) = Δ(i;j,k) where the columns of B are a_i, a_j, a_k; the spanning
hypothesis follows from `IsUnit A.det` (rows 1,2 of A are independent).

Deliver: the Lean file, plus a 10-line summary of which Mathlib lemmas you relied on and where you are
least sure the names are right, so the line can repair compile errors quickly.
