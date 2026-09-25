# TICKET K6-N4f — n = 4 rank-2 stratum (a): finish the two cover patterns (κ ≠ 0, Q(μ) ≠ 0) using the failure equations as hypotheses, and classify the patterns over every field

Self-contained; no internet; no essay. Output to `engine/harvest/k1695_r6_n4f/` (create): `REPORT.md`
ending with `DONE-K6N4F`, scripts, logs. Exact arithmetic. Read first, in this order:
`engine/harvest/k1695_r6_n4d/REPORT.md` (border criterion (4) and the g-clauses; the failure-set
characterisation (6)), `engine/harvest/k1695_r6_n4e/REPORT.md` (Lemmas 1–3; the two realised cover
patterns; the exact residual). Reuse their C primitives.

## What is missing, exactly (from N4e §2)
Setting: A = I + UWᵀ ∈ GL(4,F), rank 2, X = col U, Y = col W, cases (β-rat)/(γ)/(δ); all six
transpositions fail, i.e. the union (6) = E(K₄). Realised patterns over GF(4):
- **β-rat:** G_X = one edge, G_Y = a triangle; at ν₁: L₁ = a matching M₂, R₁ = a triangle, scalar graph
  C₁ ⊇ the needed edge; at ν₂: L₂ = the matching M₁, R₂ = a triangle. The matching M₀ (the third one)
  is clean at ν₁, ν₂ by Lemma 1. Needed: κ_{M₀} ≠ 0 at μ = 1 (Lemma 2) and Q_{M₀}(μ) ≠ 0 at every
  non-eigenvalue μ (Lemma 3).
- **γ:** G_X, G_Y triangles sharing an edge; L_ν = R_ν = C_ν = the matching M₀. M₁, M₂ are clean at ν by
  Lemma 1. Needed: for M₁ or M₂, κ ≠ 0 at 1 and Q(μ) ≠ 0 off the spectrum.
The key idea this ticket adds: **the hypotheses "every transposition fails" are EQUATIONS** (the
membership relations d_e ∈ X, d_e ∈ Y, level equalities, and the scalar clauses 1 + ν d_eᵀ(A−ν)^# d_e
= 0 for the edges that fail at ν) — use them. E.g. in β-rat, G_Y a triangle on {a,b,c} means
Y = span(d_ab, d_bc) exactly, so W's column space is KNOWN; G_X = {pq} means d_pq ∈ X; the level
graphs pin the eigenvectors' coordinate patterns; the scalar clauses give two more equations. Reduce
(U, W) to a normal form with as few free parameters as possible (up to the symmetries: relabelling
coordinates, transposing A ↔ Aᵀ which swaps X ↔ Y and L ↔ R, scaling), then compute κ_{M₀} and
Q_{M₀}(μ) SYMBOLICALLY in those parameters (sympy over ℚ, and verify the identities mod p) and show
they cannot vanish under the constraints (invertibility det A ≠ 0, rank 2, ν ≠ 1, ν₁ ≠ ν₂ …). Watch
characteristic 2 (all the GF(4) instances live there — is the pattern even possible in odd
characteristic? Use the GF(5..9) census: no all-six-fail input in 4×10⁶ presentations — try to PROVE
that all-six-fail forces characteristic 2, e.g. from d_ab ∈ Y and d_ab ∈ X⊥-type relations that need
1 = −1).
Then the classification: prove that over EVERY field, (6) = E(K₄) in cases (β-rat)/(γ)/(δ) forces one
of the two patterns (or list the others and close them). Use: G_X ∪ G_Y ≠ K₄; each L_j, R_j is a
partition graph (complete iff the eigenvector is constant); R₁ ∩ R₂ ⊆ G_{X⊥}, L₁ ∩ L₂ ⊆ G_{Y⊥};
G_S ∪ G_{S⊥} ⊆ triangle or matching. Handle the constant-eigenvector sub-cases explicitly.

## Machine checks (mandatory)
- The normal forms: enumerate all all-six-fail inputs over GF(4) (216, from N4e's exhaustive census)
  and verify each is in one of your normal forms (print the parameters). Any input outside the list
  = your classification is incomplete: print it.
- The symbolic non-vanishing: evaluate κ and Q(μ) on every one of the 216 inputs and on ≥ 10⁵ random
  parameter choices over GF(4), GF(8), GF(16), GF(3), GF(5) satisfying the constraints (state how you
  sample constrained inputs); zero must never occur.
- Controls: an input where a double transposition is NOT clean (take any A where some transposition
  works and a double transposition fails — they exist) must produce κ = 0 or Q(μ) = 0 as predicted.

## Report
Lemmas with proofs and their check lines; the classification statement with proof; residuals
UNRESOLVED with the smallest configuration. End with `DONE-K6N4F`.
