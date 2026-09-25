# TICKET K6-N4g — n = 4, RANK ONE (A = I + uvᵀ): prove it over every field by exhaustive resonance case-analysis, machine-assisted

Self-contained; no internet; no essay. Output to `engine/harvest/k1695_r6_n4g/` (create): `REPORT.md`
ending with `DONE-K6N4G`, scripts, logs. Exact arithmetic; sympy (`.venv/bin/python3`, sympy 1.14) is
available for symbolic work over ℚ(ω, i) and over GF(p). Read `engine/harvest/k1695_r6_n4d/REPORT.md`
§3 for the corrected cycle-sum criterion; everything below is proved and may be used.

## Setting
A = I + uvᵀ, u, v ∈ F⁴, c := 1 + vᵀu ≠ 0. Eigenvalue 1 has geometric multiplicity 3, so σ must have
≤ 2 cycles: six 4-cycles, eight (3,1)'s, three (2,2)'s. For M = P_σ + u wᵀ (w_i = v_{σ(i)}) and a
resonance μ (μ^ℓ = 1 for a cycle length ℓ), Lemma 0: nullity(M − μ) = dim(K_μ ∩ w⊥) + ε, K_μ =
ker(P_σ − μ) (spanned by the geometric vectors (1, μ⁻¹, μ⁻², …) along each cycle of length divisible
by ord μ), ε = 1 iff ∃x: (P_σ − μ)x = −u and wᵀx = 1. At a non-resonant μ the update is rank one on an
invertible matrix: never derogatory.
**Exact clauses (proved):**
- μ = 1: (4): fails iff Σu = 0 ∧ Σv = 0 ∧ e(σ) = 1, e(σ) = Σ_{t<k} u_{σ(t)} v_{σ(k)} over the cyclic
  order; (3,1) and (2,2): fails iff u ∈ Z_σ or v ∈ Z_σ (all cycle sums of u, or of v, vanish).
- 4-cycle at μ = −1 (char ≠ 2): candidate iff the antipodal pair-sums of u are equal AND those of v
  are equal; then fails iff the secular clause holds (compute it: α = wᵀx for the particular solution).
- 4-cycle at μ = ±i (char ≠ 2, i ∈ F̄): candidate iff û(μ) = 0 = ŵ(μ) (cyclic Fourier coefficients
  along the cycle; for i ∉ F this is "antipodal tokens equal" in u and in v); then the secular clause.
- (3,1) at a primitive cube root ω (char ≠ 3): candidate iff û_C(ω) = 0 (= ŵ_C(ω) = 0 automatically
  up to the shift); for ω ∉ F this forces the three tokens on the 3-cycle to be equal in u and in v;
  then the secular clause.
- (2,2) at μ = −1 (char ≠ 2): K_{−1} = span of the two alternating vectors on the 2-cycles; candidate
  iff u and v are orthogonal to them appropriately (derive: it is "u_a = u_b and u_c = u_d"-type? — no:
  derive it exactly from Lemma 0); then the secular clause.
The all-equal-token case u = a𝟙, v = b𝟙 is PROVED (aI + bJ theorem: n-cycle, else (n−1,1)) — cite.

## Method: exhaustive case analysis by Gröbner/resultant elimination
"All 17 permutations fail" is a finite DISJUNCTION over, for each σ, WHICH resonance blocks it
(with its candidate conditions + secular clause). Enumerate the combinations systematically (prune:
a 4-cycle blocked at 1 needs Σu = Σv = 0, which is one condition shared by all six 4-cycles; etc.).
For each combination you get a polynomial system in the 8 unknowns u_i, v_i over ℤ[ω, i] (adjoin
ω with ω² + ω + 1 = 0 and i with i² + 1 = 0 as needed) together with the inequation c ≠ 0 (and
non-all-equal tokens, non-proportionality where the branch assumes it). Show each system is
inconsistent: sympy `groebner` with a Rabinowitsch variable for c ≠ 0, over ℚ(ω, i) (use the
generators ω²+ω+1, i²+1 as extra polynomials) and separately over GF(p) for p ∈ {2,3,5,7,11,13} (in
char 2 and 3 the resonance lists shrink — redo the enumeration there). Cap each Gröbner run at
10 min / 4 GB; report any that does not finish as UNRESOLVED with the system printed.
Exploit symmetry to cut cases: relabelling coordinates (S₄ acts on both u and v), swapping u ↔ v
(transpose), scaling u ↦ λu, v ↦ λ⁻¹v.

## Machine checks
- Every clause above must be checked against brute force (rank of AP_σ − μ over GF(q²)) on all
  invertible I + uvᵀ over GF(2), GF(3), GF(4), GF(5) — with a negative control.
- Every inconsistent system: also confirm by exhaustive search over GF(7), GF(9), GF(13) (all
  u, v) that no solution exists (a consistency check of the case enumeration itself).
- The final decision rule (which σ to take in which case) must be run exhaustively over
  GF(2), GF(3), GF(4), GF(5), GF(7), GF(8), GF(9) with an independent oracle and the P = I control.

## Report
The case tree with, per leaf, the polynomial system, the certificate (basis = [1]) per field, and the
check lines; residual leaves UNRESOLVED with their systems. End with `DONE-K6N4G`.
