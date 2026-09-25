# TICKET K6-LEAN2 — finish the transposition lemma in Lean 4 / Mathlib (L6 corrected, L7 quadratic)

Continue in `lean/proofenv/K1695/TranspositionLemma.lean` (existing, builds clean, 0 sorry; do NOT
break the existing theorems — add new ones; keep `lake build` green). Deliver: the file, the
`lake env lean K1695/TranspositionLemma.lean` output with `#print axioms` for every new theorem (must
be exactly [propext, Classical.choice, Quot.sound]), and `engine/harvest/k1695_r6_lean2/REPORT.md`
ending with the literal line `DONE-K6LEAN2`. No `sorry` in anything listed as proved. Time budget
~2 h; keep what compiles, mark the rest NOT PROVED.

Notation as before: K a field, n : ℕ, a b : Fin n, a ≠ b, d := Pi.single a 1 − Pi.single b 1,
P_τ the transposition matrix (your `l1_*`), A : Matrix (Fin n) (Fin n) K, μ : K.

**L6′ (T2, corrected: μ ≠ 0).** If `μ ≠ 0`, `rank (A − μ•1) = n − 2` (with `2 ≤ n`), `d ∉ range
(mulVecLin (A − μ•1))` and `d ∉ range (mulVecLin (A − μ•1)ᵀ)`, then `rank (A * P_τ − μ•1) = n − 1`.
Route: by L2 it is `rank ((A − μ•1) + μ • vecMulVec d d) = n − 1`; prove the general fact
**L6a**: for E : Matrix (Fin n) (Fin n) K and x y : Fin n → K with `x ∉ range (mulVecLin E)` and
`y ∉ range (mulVecLin Eᵀ)`, `rank (E + vecMulVec x y) = rank E + 1` (image of E + xyᵀ contains
image E ⊕ ⟨x⟩ … — use `LinearMap.range`, `rank` = finrank of range; the standard argument: the map
z ↦ Ez + (yᵀz)x has image ⊇ range E, and x ∈ image since y ∉ range Eᵀ gives z₀ with yᵀz₀ ≠ 0 while
… choose z₀ ∈ ker E? no — argue: if x ∈ image, done; else image ⊆ range E + ⟨x⟩ strictly bigger
than range E because some z with yᵀz ≠ 0 exists (y ≠ 0) and then Ez + (yᵀz)x ∉ range E as x ∉ range E).
Then apply with x = μ•d (∉ range since μ ≠ 0), y = d.
**L7 (T4, quadratic case).** F ⊆ K fields (`[Algebra F K]`), A : Matrix (Fin n) (Fin n) F,
μ : K with `μ ∉ Set.range (algebraMap F K)` and `μ * μ = algebraMap F K s + algebraMap F K t * μ`
for some s t : F (i.e. μ is a root of the quadratic X² − tX − s over F). If
`w : Fin n → F`, `z : Fin n → K` and `(A.map (algebraMap F K) − μ•1).mulVec z = fun i => algebraMap F K (w i)`,
then `∃ z₁ : Fin n → F, w = (A * A − t • A − s • 1).mulVec z₁`.
Route (the explicit computation, no Galois theory): 1 and μ are F-linearly independent in K
(μ ∉ F), so write z = z₀ + μ z₁ with z₀ z₁ over F (you may ASSUME this decomposition as a
hypothesis `hz : z = fun i => algebraMap F K (z₀ i) + μ * algebraMap F K (z₁ i)` if constructing it
from the power basis is too heavy — state clearly that you did); expand `(A − μ)z`, use μ² = s + tμ,
compare the 1- and μ-components: `A z₀ − s z₁ = w` and `A z₁ − z₀ − t z₁ = 0`, so `z₀ = A z₁ − t z₁`
and `w = (A² − tA − s) z₁`.
Also add an `example` instantiating L6′ at n = 4 and L7 at n = 2, K = ℚ(√2)-like if a concrete
extension is convenient (else skip the L7 example and say so).

## Report
L6a, L6′, L7: theorem names, PROVED/NOT PROVED, axioms, the build log. End with `DONE-K6LEAN2`.
