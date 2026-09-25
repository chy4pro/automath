# TICKET K6-N4d — n = 4 stratum (a): the 3-cycle / double-transposition witness, from exact criteria

Self-contained; no internet; no essay. Output to `engine/harvest/k1695_r6_n4d/` (create): `REPORT.md`
ending with `DONE-K6N4D`, scripts, logs. Exact arithmetic only. Every lemma: proof valid over every
field + machine check with a control that can fail. Read first: `engine/harvest/k1695_r6_n4c/REPORT.md`
(its failure-set lemmas, permutation-update lemma, and the two GF(4) inputs where ALL SIX transpositions
fail — one β-rational rescued by the 3-cycle (1 2 3), one γ rescued by (0 1)(2 3)). Because of those
inputs, NO transposition-only argument can close stratum (a); the witness must sometimes be a
3-cycle or a double transposition. This ticket builds the exact criterion for those and uses it.

## Setting (proved)
A = I + UWᵀ ∈ GL(4,F), rank(UWᵀ) = k ∈ {1,2}; X = col U, Y = col W; S = I_k + WᵀU; eigenvalues of A:
1 (geometric multiplicity 4 − k) and spec S. For any σ and μ ≠ 0:
`rank(AP_σ − μI) = rank((A − μI) + μ(I − P_σ⁻¹))` (permutation-update lemma). For σ with two cycles
(types (3,1) and (2,2)), N := I − P_σ⁻¹ has rank 2, image Z_σ = {x : Σ_{i∈C} x_i = 0 for each cycle C}
(cycle-sum-zero vectors) and kernel K_σ = {x constant on each cycle}. Both are F-rational and depend
only on the cycle PARTITION; N itself depends on the cyclic orders (for (2,2) there is one order per
partition; for (3,1) two orders per partition, N and Nᵀ-related).
Cyclic ⟺ rank(AP_σ − μ) ≥ 3 for all μ ∈ F̄ ⟺ nullity((A − μ) + μN) ≤ 1 ∀μ.

## 1. Exact rank-two-update criterion (derive, prove, machine-check)
For E := A − μI with nullity g and the rank-2 matrix N = μ(I − P_σ⁻¹) = x₁y₁ᵀ + x₂y₂ᵀ (write N
explicitly in that form for each of the 11 two-cycle permutations: for a 3-cycle (abc) with fixed
point f, N restricted to {a,b,c} is μ(I − shift); for (ab)(cd), N = μ(d_ab d_abᵀ + d_cd d_cdᵀ)):
`nullity(E + N) = nullity of the bordered matrix [[E, X],[Yᵀ, −I₂]]` (X = [x₁ x₂], Y = [y₁ y₂]).
Derive, for each g ∈ {0,1,2,3}, the exact condition "nullity(E + N) ≥ 2" in terms of E's kernel /
cokernel and the vectors x_i, y_i — the analogue of Lemma T's clauses (T0: g = 0 ⟹ nullity ≤ 2, and
= 2 iff I₂ + YᵀE⁻¹X = 0 — the 2×2 "Woodbury" matrix vanishes; g = 1, 2, 3: work it out via the
bordered matrix; g ≥ 4 impossible). Machine-check the derived clauses against brute force over
GF(2), GF(3), GF(4) for ALL A ∈ GL(4,q) (q = 2, 3) resp. a 10⁵ sample (q = 4), all 11 two-cycle σ,
all μ ∈ GF(q²), with a negative control (delete one clause → disagreements must appear).

## 2. Apply to stratum (a)
(a) For the two GF(4) model inputs, print which clause blocks each transposition and which clause
    is satisfied by the rescuing 3-cycle / double transposition — this is the mechanism to prove.
(b) Rank 2, cases (β-rat), (γ), (δ): characterise EXACTLY the configurations where all six
    transpositions fail (use the failure-set lemmas + scalar clause `1 + ν dᵀ(A − ν)^# d = 0`); for
    those configurations prove that some (3,1) or (2,2) permutation satisfies the §1 criterion at
    every μ ∈ {1} ∪ spec S (and no other μ can be derogatory: show the Woodbury 2×2 matrix cannot
    vanish at a non-eigenvalue μ, or handle it). Machine-check the characterisation and the rescue
    rule over GF(3), GF(4), GF(5), GF(7).
(c) Rank 1 (A = I + uvᵀ): here g(1) = 3, so σ must have ≤ 2 cycles and the §1 criterion at μ = 1 with
    g = 3 is exactly the statement "the cycle-sum clauses" (for (2,2): fails at 1 iff [both cycle-sums
    of v vanish] or [both of u vanish]; for (3,1): clean at 1 iff u_f ≠ 0 and v_f ≠ 0 — re-derive both
    from §1). Then the other resonances: −1 (types (4) and (2,2)), ±i (type (4)), ω (type (3,1)).
    Close as many sub-cases as you can with proofs; the all-equal-token case is proved elsewhere
    (cite). Exhaustive machine check over GF(2), GF(3), GF(4), GF(5), GF(7), GF(8), GF(9).

## Report
Per lemma: statement, proof, check line (population, failures, controls incl. "always P = I").
Unclosed cases: UNRESOLVED + smallest configuration. End with `DONE-K6N4D`.
