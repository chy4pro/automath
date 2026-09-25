# TICKET K6-N4j — rank-2 stratum (a) at n = 4: classify ALL formal cover patterns and refute each unrealised one algebraically

Self-contained; no internet; no essay. Output to `engine/harvest/k1695_r6_n4j/` (create): `REPORT.md`
ending with `DONE-K6N4J`, scripts, logs. Exact arithmetic; sympy available (msolve in ~/.local if K6-T4
built it — check `engine/harvest/k1695_r6_T4/`). Read first `engine/harvest/k1695_r6_n4f/REPORT.md`
(the two realised patterns, their normal forms and the char-2 forcing) and `k1695_r6_n4d/REPORT.md`
(failure-set characterisation (6)).

## Setting (proved facts)
A = I + UWᵀ ∈ GL(4,F), rank 2, X = col U, Y = col W (2-dim), S = I₂ + WᵀU; cases (β-rat) two distinct
rational eigenvalues ν₁, ν₂ ≠ 1; (γ) one ν ≠ 1 with a Jordan block; (δ) spec S = {1, ν}. Edge sets on
K₄ (vertices 0..3): G_X = {e : d_e ∈ X}, G_Y, and for each simple eigenvalue ν: L_ν = {e : d_e ⊥ ℓ_ν}
(left eigenvector level graph), R_ν = {e : d_e ⊥ r_ν}, C_ν = {e : 1 + ν d_eᵀ(A−ν)^# d_e = 0}. All six
transpositions fail iff G_X ∪ G_Y ∪ ⋃_ν (L_ν ∩ R_ν ∩ C_ν) = E(K₄). Structural constraints (proved):
each of G_X, G_Y, L_ν, R_ν is a "partition graph" (disjoint union of cliques); G_X, G_Y have ≥ 2
components (⊆ triangle or ⊆ perfect matching); L_ν, R_ν are complete iff the eigenvector is constant
(iff 𝟙 ∈ Y resp. X and 𝟙 is an eigenvector: constant column/row sums); (β-rat): R₁ ∩ R₂ ⊆ G_{X⊥},
L₁ ∩ L₂ ⊆ G_{Y⊥}; G_S ∪ G_{S⊥} ⊆ triangle or ⊆ perfect matching; G_X ∪ G_Y ≠ E(K₄). Realised over GF(4)
and proved to force characteristic 2: the β pattern (G_X one edge, G_Y triangle, L_j matchings, R_j
triangles) and the γ pattern (G_X, G_Y triangles sharing an edge, L = R = C = one matching).

## Task
1. ENUMERATE, by program, every formal assignment of (G_X, G_Y, L_ν, R_ν, C_ν for each simple ν) to
   subsets of E(K₄) satisfying the structural constraints above (partition graphs; component counts;
   the ⊥ inclusions where they apply; C_ν arbitrary subset of L_ν ∩ R_ν — the scalar clause only
   restricts) such that the union is E(K₄), for each of (β-rat) [two ν's], (γ) and (δ) [one ν]; reduce
   modulo the symmetries (S₄ relabelling; transpose A ↔ Aᵀ swapping X ↔ Y, L ↔ R; eigenvalue swap in
   β-rat). Print the list of orbit representatives with counts.
2. For EACH representative pattern, decide realisability over every field: set up the polynomial
   conditions on (U, W) (memberships d_e ∈ X: rank conditions; level equalities ℓ(a) = ℓ(b) with ℓ = W f,
   f a left eigenvector of S — parametrise S's eigenvectors; scalar clauses as in N4f) and either
   (a) derive a normal form and prove the pattern is realisable exactly in stated characteristics (as
   N4f did — then prove the double-transposition rescue there, or cite N4f if it is one of the two),
   or (b) prove the conditions inconsistent over every field (by hand where the graph combinatorics
   already contradicts — e.g. two triangles + a matching covering K₄ needs the matching's scalar
   clause to hold on the edge outside both triangles while its level clauses hold — or by Gröbner
   with Rabinowitsch per characteristic, capped 10 min / 4 GB, sympy or msolve).
3. Machine check: every all-six-fail input over GF(4) (216) must land in a realisable pattern of your
   list (N4f says exactly two); random constrained samples over GF(3), GF(5), GF(7), GF(8), GF(9)
   (10⁵ presentations each): every all-six-fail input found must land in a realisable pattern — an
   input outside your list = your enumeration is wrong: print it.
4. Report: the enumeration (counts per case, orbit representatives), the per-pattern verdict with
   proof or certificate, and the final statement you can assert about "all six transpositions fail ⟹
   characteristic 2 and one of the two N4f patterns" (per characteristic, exact). End with `DONE-K6N4J`.
