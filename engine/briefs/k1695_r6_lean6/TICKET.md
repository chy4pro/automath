# TICKET K6-LEAN6 — Lean: the n = 4 stratum-(b) theorem ("minpoly an irreducible quadratic ⟹ every transposition works")

Continue in `lean/proofenv` (Mathlib; all K1695 modules must stay green: TranspositionLemma,
TranspositionLemmaFull, CyclicVectorThree, CyclicToMinpoly). Add ONE new file `K1695/StratumB.lean`
and register it. Deliver: file, `lake env lean` output with `#print axioms` (no axiom beyond
[propext, Classical.choice, Quot.sound]), `lake build` green, `engine/harvest/k1695_r6_lean6/REPORT.md`
ending with `DONE-K6LEAN6`. No `sorry` in anything listed as proved. Budget ~4 h; keep what compiles;
partial credit is per lemma.

## Target (all over an arbitrary field F)
`theorem stratumB_transposition (A : Matrix (Fin 4) (Fin 4) F) (hA : IsUnit A.det)
  (m : F[X]) (hm : Irreducible m) (hdeg : m.natDegree = 2) (hmin : minpoly F A = m)
  (a b : Fin 4) (hab : a ≠ b) : minpoly F (A * Matrix.swap F a b) = (A * Matrix.swap F a b).charpoly`
(or with `Equiv.swap a b |>.permMatrix F`; state which and why they agree — `l1_matrix_identity`
already relates `transpositionMatrix` to `Matrix.swap`). Use `minpoly_eq_charpoly_of_krylov_linearIndependent`
only if you go through a cyclic vector; the natural route is rank-based: nonderogatory ⟺
∀ μ ∈ L, rank(M − μ) ≥ 3 over a splitting field L; then bridge to minpoly = charpoly (Mathlib:
a matrix is nonderogatory iff its minimal polynomial equals its characteristic polynomial — if this
equivalence is not available as a lemma, prove the direction you need: "rank(M − μI) ≥ n − 1 for all μ
in an algebraically closed extension ⟹ minpoly = charpoly" — via: the minpoly has degree n iff … —
if that is too heavy, deliver the rank-form statement
`∀ μ : L, ((A * P).map (algebraMap F L) − μ • 1).rank ≥ 3` for L = AlgebraicClosure F (or for
L = F⟮root of m⟯ — the argument only needs μ ranging over eigenvalues, and every eigenvalue of A·P
that could be derogatory is a root of m) and SAY SO).

## Proof to formalise (all steps proved on paper; registry §R6.3, §R6.6)
Let P = transposition matrix of (a b), d = e_a − e_b, L ⊇ F a field containing a root μ of m.
1. `l2_rank_identity`: rank(AP − μ) = rank((A − μ) + μ ddᵀ) (over L, for the mapped matrices).
2. If μ ∉ spec(A) (i.e. det(A − μ) ≠ 0 over L): `l4_t0` gives rank ≥ 3. So only roots of m matter
   (charpoly A = m², every eigenvalue is a root of m; use `Matrix.minpoly_dvd_charpoly` and
   irreducibility: charpoly's irreducible factors divide the minpoly).
3. Nullity lemma: for μ a root of m over L: nullity(A − μI) = 2 over L. Proof for the Lean file:
   write m = (X − μ)(X − μ′) over L (μ′ the other root, possibly = μ). Then (A − μ)(A − μ′) = m(A) = 0,
   so im(A − μ′) ⊆ ker(A − μ) and im(A − μ) ⊆ ker(A − μ′), giving rank(A − μ) ≤ nullity(A − μ′) and
   symmetric, i.e. nullity(A − μ) + nullity(A − μ′) ≥ 4.
   (i) μ ≠ μ′: ker(A − μ) ∩ ker(A − μ′) = 0 gives nullity(A−μ) + nullity(A−μ′) ≤ 4, hence = 4 and
   im(A − μ) = ker(A − μ′). To get nullity(A − μ) = 2 exactly use the F-conjugation: the F-algebra
   automorphism of L = F(μ) swapping μ, μ′ (exists since m is the minimal polynomial of both) maps
   ker(A − μ) onto ker(A − μ′) (A is over F), so the nullities agree. If constructing the automorphism
   in Lean is heavy, use instead the dimension count over F: ker_F(m(A)) = F⁴ … and the L-dimension of
   ker(A − μ) equals the F-dimension of … — choose the route that compiles; a clean alternative:
   the F[X]-module F⁴ is a K := F[X]/(m)-vector space (m irreducible ⇒ K a field) of K-dimension 2
   (F-dimension 4 = 2·deg m); tensoring with L: F⁴ ⊗_F L ≅ (K ⊗_F L)² and K ⊗_F L ≅ L × L (separable)
   … — heavy; prefer the automorphism route or the direct kernel-dimension route below.
   (ii) μ = μ′ (inseparable, char 2, m = X² − s): (A − μ)² = 0 so rank(A−μ) ≤ nullity(A−μ) ⇒ nullity ≥ 2;
   nullity ≥ 3 would make A − μ of rank ≤ 1, i.e. A − μ = x yᵀ over L; comparing the entries (A over F,
   μ ∉ F) forces, for i ≠ j, A_ij = x_i y_j ∈ F and A_ii − μ = x_i y_i, and the 2×2 minors of A − μ
   vanish: (A_ii − μ)(A_jj − μ) = A_ij A_ji ∈ F for all i ≠ j ⇒ A_ii + A_jj = t (the X-coefficient of m,
   here 0) for all i ≠ j, and then A_ij A_ji = (c − μ)² ≠ 0 where c = A_ii is common; with x₁ = 1:
   A_ij = A_i1 A_1j /(c − μ) ∉ F for i ≠ j ≥ 2 — contradiction at n = 4. Formalise this or find a
   cleaner argument (e.g. via the F-dimension of ker_F m(A) = 4 and ker(A − μ)² …).
   DIRECT alternative for both cases (recommended if it compiles): nullity_L(A − μ) = nullity_F of the
   F-linear map (A − μ) on L⁴ viewed as F-vector space? — no. Think first; pick one route; if all fail,
   deliver the theorem with the nullity lemma as an explicit HYPOTHESIS `hnull : (A.map (algebraMap F L) − μ • 1).rank = 2`
   and say so clearly (partial credit).
4. T4 quadratic (`l7_quadratic_descent_with_decomposition`, hypothesis form): any w ∈ F⁴ in
   col_L(A − μ) lies in col_F(m(A)) = 0 (since m(A) = 0). To discharge the decomposition hypothesis,
   construct z₀, z₁ from z ∈ L⁴ via the power basis {1, μ} of L = F⟮μ⟯ (`IntermediateField.adjoin`,
   `PowerBasis`, or `Algebra.adjoin.powerBasis'`); alternatively prove T4-quadratic without the
   hypothesis for L = F⟮μ⟯. Conclude d ∉ col(A − μ) and (transpose) d ∉ row(A − μ).
5. `l6prime_t2_corrected` (μ ≠ 0 since A invertible and μ a root of an irreducible m ≠ X):
   rank(AP − μ) = 3. Combine with step 2 for all μ ∈ L (or all μ in an algebraic closure): AP is
   nonderogatory; then minpoly = charpoly.

## Report
Per step: theorem names, PROVED / NOT PROVED / delivered-as-hypothesis, axioms, build log.
End with `DONE-K6LEAN6`.
