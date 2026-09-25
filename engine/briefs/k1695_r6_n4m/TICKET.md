# TICKET K6-N4m — rank-2 stratum (a) at n = 4 by SHAPE parametrisation (the smart version of the cover classification)

Self-contained; no internet; no essay. Output to `engine/harvest/k1695_r6_n4m/` (create): `REPORT.md`
ending with `DONE-K6N4M`, scripts, logs. Exact arithmetic; sympy; msolve at `~/.local/bin/msolve`
(verify on the toy ideals). Caps 20 min / 8 GB per computation. Read `engine/harvest/k1695_r6_n4f/REPORT.md`
(how a pattern becomes a normal form) and `k1695_r6_n4j/REPORT.md` (why the formal enumeration is
too coarse: 5 361 orbits).

## Idea
Do not enumerate the scalar-clause graphs. Split ONLY by the shape of (G_X, G_Y) — the μ = 1 failure
graphs — which is a small list: each of G_X, G_Y ∈ {∅, one edge, perfect matching (2 edges),
triangle} up to S₄ (and X ↔ Y by transposing A). For each shape, PARAMETRISE all (U, W) realising it:
G_X = triangle {abc} ⟺ X = ⟨d_ab, d_bc⟩ exactly; G_X = matching {ab, cd} ⟺ X = ⟨d_ab, d_cd⟩; G_X = {ab}
⟺ X = ⟨d_ab, x⟩ with x ∉ ⟨d_ab⟩ and no other difference in X (open condition); G_X = ∅: X generic (open
conditions). Same for Y. Then U = X-basis · G, W = Y-basis · H for G, H ∈ GL₂ (or absorb: A − I =
[X-basis]·K·[Y-basis]ᵀ with K ∈ GL₂ — 4 parameters) plus the free parameters of x, y when present.
So each shape gives a family A(shape; K, x, y) with ≤ 4 + 4 + 4 = 12 parameters, usually far fewer.
The remaining edges E′ = E(K₄) ∖ (G_X ∪ G_Y) (at least one) must ALL fail at simple eigenvalues of S =
I₂ + WᵀU: for each e ∈ E′ and each ν ∈ spec S ∖ {1}, the failure is "d_e ⊥ ℓ_ν ∧ d_e ⊥ r_ν ∧
1 + ν d_eᵀ(A − ν)^# d_e = 0". Since the eigenvectors of S are explicit in K's entries (2×2), these are
explicit polynomial conditions in the parameters (with ν a root of the quadratic charpoly of S — keep
ν as a variable with its quadratic relation, or split by "S diagonalisable / Jordan / conjugate").

## Task
1. List the shapes (with G_X ∪ G_Y ≠ K₄ — that is all shapes, since two such graphs never cover;
   symmetry-reduce). For each, write the parametrisation and the polynomial system "all edges of E′
   fail at some ν" (as a finite disjunction over the assignment e ↦ ν_e, each conjunct a system).
2. For each conjunct: Gröbner with Rabinowitsch (det(I₂ + WᵀU) ≠ 0, the open conditions of the shape,
   ν ≠ 1, ν₁ ≠ ν₂ where applicable) over ℚ and over GF(2), GF(3), GF(5), GF(7): [1] ⟹ that conjunct is
   impossible in that characteristic; not [1] ⟹ describe the variety and extract the normal form (as
   N4f did) and check which characteristics it lives in (expect: only char 2, exactly the two N4f
   families). Report a table shape × conjunct × characteristic.
3. Consistency: the two N4f normal forms must appear as non-[1] components (in char 2 only); every
   all-six-fail input over GF(4) (216) must land in a non-[1] component; random constrained samples
   over GF(3,5,7,8,9) must produce none outside.
4. If every conjunct is [1] in every characteristic except the two N4f families in char 2, you have
   PROVED: "rank-2 stratum (a), all six transpositions fail ⟹ char 2 and one of the two N4f families",
   hence (with N4f) rank-2 stratum (a) is CLOSED over every field (every double transposition works
   there; a transposition works otherwise). State exactly what is certified per characteristic.
End with `DONE-K6N4M`.
