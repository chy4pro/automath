# TICKET K6-N4e — n = 4, rank-2 stratum (a): PROVE "if all six transpositions fail then some double transposition works"

Self-contained; no internet; no essay. Output to `engine/harvest/k1695_r6_n4e/` (create): `REPORT.md`
ending with `DONE-K6N4E`, scripts, logs. Exact arithmetic. Every lemma: proof over every field +
machine check with a control that can fail. Read first `engine/harvest/k1695_r6_n4d/REPORT.md` — it
PROVED the exact rank-two-update criterion (border reduction (4), explicit clauses for g = 0..3) and
the exact characterisation (6) of "all six transpositions fail" in cases (β-rat), (γ), (δ); reuse its
checks.c primitives.

## Target
A = I + UWᵀ ∈ GL(4,F), rank(UWᵀ) = 2, S = I₂ + WᵀU, spec A = {1,1} ∪ spec S (cases (β-rat) two
distinct rational ν's ≠ 1; (γ) one ν ≠ 1 with a Jordan block; (δ) spec S = {1, ν}; the cases S = νI
and spec S = {1,1} and the conjugate-β case are already closed — cite). Empirical fact (both GF(4)
inputs where all six transpositions fail): ALL THREE double transpositions work. Conjecture to
prove: **if every transposition fails, then every (or at least one) double transposition (ab)(cd)
makes AP_σ cyclic.** If the "every" form is false, find the counterexample and prove the "at least
one" form.

## Tools (all proved; use)
For σ = (ab)(cd) and μ ≠ 0: rank(AP_σ − μ) = rank(E + μ d_ab d_abᵀ + μ d_cd d_cdᵀ), E = A − μI.
So the double transposition is a SEQUENCE of two rank-one updates: E → E + μ d_ab d_abᵀ → + μ d_cd d_cdᵀ,
and Lemma T applies twice: first to A at (ab), then to A′ := A P_(ab) at (cd) — whose eigenstructure
is what Lemma T for A' needs. Key: since (ab) FAILS for A, we know the exact mechanism (which μ and
which clause); e.g. failure at μ = 1 by d_ab ∈ X ∪ Y, or at a simple ν by the level/scalar clauses.
Then A′ = A P_(ab) is derogatory exactly at those μ (g = 2 there) and non-derogatory elsewhere, and the
second update d_cd must (i) reduce g at every derogatory μ of A′ (T2 for A′: d_cd ∉ col(A′ − μ) and
d_cd ∉ row(A′ − μ)) and (ii) not create a new derogatory eigenvalue (T1 for A′ at its simple
eigenvalues). Compute col(A′ − μ) and row(A′ − μ) explicitly from A's data: A′ − μ = (A − μ) −
(a_a − a_b) d_abᵀ … (A P_(ab) = A − (a_a − a_b) d_abᵀ where a_a, a_b are columns of A).
Alternatively use the N4d criterion (4) directly with X = μ[d_ab, d_cd], Y = [d_ab, d_cd]:
nullity(E + XYᵀ) = (g − rank D) + dim T, D = Yᵀ|_{ker E}, C = X modulo im E, Q = I₂ + YᵀGX.
At μ = 1 (g = 2, ker E = ker Wᵀ = Y⊥, im E = X): D = [d_ab, d_cd]ᵀ restricted to Y⊥ — rank D = 2 iff
the functionals d_abᵀ, d_cdᵀ are independent on Y⊥ iff … ; C = 0 iff d_ab, d_cd ∈ X. Work these out:
the double transposition is clean at 1 iff nullity ≤ 1 iff [rank D = 2 and dim T ≤ 1] etc. Note the
complementary structure: the three double transpositions correspond to the three perfect matchings
of K₄, and G_X ∪ G_Y (the μ = 1 failure edges) ⊆ triangle ∪ … — relate "all six transpositions fail"
(the union (6) = K₄) to the matchings.

## Plan
1. From (6) = E(K₄), derive the possible configurations of (G_X, G_Y, level graphs, scalar clauses)
   exactly — a finite list of "covering patterns" (which edges fail at 1, which at ν_j). Print the
   patterns realised in the GF(4) examples and in an exhaustive GF(5)/GF(7) search restricted to
   all-six-fail inputs (enumerate A with rank(A − I) = 2 via (U, W) pairs, filter).
2. For each pattern, prove that a specific double transposition (or each of them) is clean at every
   μ ∈ {1} ∪ spec S and has no derogatory non-eigenvalue μ (T0-type: the 2×2 matrix Q = I₂ + YᵀE⁻¹X
   cannot vanish at a non-eigenvalue — prove or bound).
3. Machine-check: for every all-six-fail input over GF(4), GF(5), GF(7), GF(8), GF(9) (exhaustive
   where feasible, else ≥ 10⁵ presentations), assert the double transpositions predicted clean are
   cyclic by an independent oracle; negative control: the "always P = I" rule and a fixed transposition.
4. Report: lemma per pattern; residual patterns UNRESOLVED with the smallest input. End with
   `DONE-K6N4E`.
