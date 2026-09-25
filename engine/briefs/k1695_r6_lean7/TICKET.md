# TICKET K6-LEAN7 — Lean: the rank criterion for "minpoly = charpoly", and the stratum-(b) nullity lemma

Continue in `lean/proofenv` (Mathlib; all K1695 modules must stay green). Add ONE new file
`K1695/RankCriterion.lean` (and, if you finish, extend `K1695/StratumB.lean` from K6-LEAN6 — read
`engine/harvest/k1695_r6_lean6/REPORT.md` for what exists). Deliver: files, `lake env lean` output with
`#print axioms` (no axiom beyond [propext, Classical.choice, Quot.sound]), `lake build` green,
`engine/harvest/k1695_r6_lean7/REPORT.md` ending with `DONE-K6LEAN7`. No `sorry` in anything listed as
proved. Budget ~4 h; partial credit per lemma.

**R1 (the bridge, general n).** For a field K, n ≥ 1, M : Matrix (Fin n) (Fin n) K: if for every μ in
an algebraically closed extension L of K (`AlgebraicClosure K`, or any field L with `[IsAlgClosed L]
[Algebra K L]`) we have `((M.map (algebraMap K L)) − μ • 1).rank ≥ n − 1`, then
`minpoly K M = M.charpoly`. Route: over L the minimal polynomial splits; if minpoly ≠ charpoly then
some root μ of charpoly has geometric multiplicity ≥ 2, i.e. rank(M_L − μ) ≤ n − 2 — formalise via:
minpoly K M = minpoly L M_L (`minpoly.algebraMap_eq` / base change of minpoly, Mathlib has
`Matrix.minpoly_map`? — check), then over L: the L[X]-module structure … — if the structure theory
is too heavy, use the equivalent: `minpoly = charpoly` ⟺ ∃ cyclic vector, and prove "∀ μ, rank ≥ n−1
⟹ ∃ v Krylov-cyclic" directly over L (choose v generic: over an infinite field a vector outside the
finitely many proper invariant subspaces… — also heavy). Choose the cleanest route that compiles;
if none does, deliver the special case n = 4 with an explicit argument, or deliver the converse
"minpoly = charpoly ⟹ rank ≥ n − 1 for all μ" (easier: a cyclic vector exists by
`minpoly_eq_charpoly_of_krylov_linearIndependent`'s converse … no — the converse needs the existence
of a cyclic vector; Mathlib may have `LinearMap.exists_cyclic_vector`-type results for
`minpoly = charpoly`; search).
**R2 (nullity lemma for stratum (b)).** F a field, A : Matrix (Fin 4) (Fin 4) F with
`minpoly F A = m`, m irreducible with `natDegree m = 2`, L = F⟮μ⟯ for a root μ of m (or any L with
μ ∈ L a root): `(A.map (algebraMap F L) − μ • 1).rank = 2`. Suggested proof (both cases): write
m = (X − μ)(X − μ′) over L. (a) rank ≥ 2: from (A − μ)(A − μ′) = 0, im(A − μ′) ⊆ ker(A − μ) so
rank(A − μ′) ≤ nullity(A − μ) = 4 − rank(A − μ); and rank(A − μ) + rank(A − μ′) ≥ … — hmm, one needs
rank(A − μ) ≥ 2: if rank(A − μ) ≤ 1 then (case μ ≠ μ′) A − μ′ = (A − μ) + (μ − μ′)I has rank ≥ 3,
contradiction with rank(A − μ′) ≤ nullity(A − μ) … wait that gives rank(A−μ′) ≤ 4 − rank(A−μ) ≥ 3 —
no contradiction. Use instead: rank(A − μ) ≤ 1 ⟹ A − μ = x yᵀ ⟹ trace/entries argument: (A − μ)² =
(yᵀx)(A − μ) and also (A − μ)(A − μ′) = 0 ⟹ (A − μ)² = (μ′ − μ)(A − μ) ⟹ yᵀx = μ′ − μ … then
A = μ I + x yᵀ over L with A over F: comparing the 2×2 minors of A − μ (all zero) gives
(A_ii − μ)(A_jj − μ) = A_ij A_ji ∈ F for i ≠ j, hence A_ii + A_jj = tr-coefficient of m for all pairs,
so all A_ii equal =: c, and A_ij A_ji = (c − μ)² for all i ≠ j; with x₁ = 1 (scale), A_ij = A_i1 A_1j/(c−μ)
∉ F for i, j ≥ 2 distinct unless A_i1 A_1j = 0, but A_i1 A_1i = (c−μ)² ≠ 0 — contradiction (n = 4 ≥ 3
gives two indices i ≠ j ≥ 2). This handles BOTH the separable and inseparable cases uniformly (it never
uses μ ≠ μ′). (b) rank ≤ 2: rank(A − μ) ≤ nullity(A − μ′) (from the product identity) and by the
symmetric argument applied to μ′ … for the inseparable case μ = μ′ this reads rank ≤ nullity, i.e.
rank ≤ 2 directly. For μ ≠ μ′: rank(A−μ) + rank(A−μ′) ≤ 4 and rank(A−μ) ≥ 2, rank(A−μ′) ≥ 2 ⟹ both = 2.
Formalise (a) and (b); the 2×2-minor computation is finite and explicit (`Fin 4`, `fin_cases`).
**R3 (assemble, if time).** With R2 supplying `hnull`, K6-LEAN6's `stratumB_rank_at_root_of_simple_extension_and_nullity`
gives rank(A_L·P − μ) = 3 at roots; add the nonroot case (`l4_t0` for μ not a root: det(A_L − μ) ≠ 0
because charpoly A = m² … or because m(μ) ≠ 0 and m(A) = 0 ⟹ A − μ invertible via
(A − μ)·(something) = m(A) − m(μ) = −m(μ)·I: indeed m(A) − m(μ)I = (A − μ)·q(A) for the polynomial
quotient, so A − μ is invertible with inverse −q(A)/m(μ)), and conclude rank(A_L P − μ) ≥ 3 ∀ μ ∈ L;
then R1 gives minpoly = charpoly.

## Report
Theorem names, PROVED / NOT PROVED, axioms, build log. End with `DONE-K6LEAN7`.
