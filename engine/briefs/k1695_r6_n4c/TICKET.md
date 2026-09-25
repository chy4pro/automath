# TICKET K6-N4c — n = 4, stratum (a), the four remaining cases, with a worked model proof

Self-contained; no internet; no essay. Output to `engine/harvest/k1695_r6_n4c/` (create): `REPORT.md`
ending with the literal line `DONE-K6N4C`, scripts, logs. Exact arithmetic only. Every lemma: proof
valid over every field + machine check with a control that can fail. Graded on what you build.

## Setting (proved, use freely)
A = I + UWᵀ ∈ GL(4,F), U, W ∈ F^{4×k}, rank(UWᵀ) = k ∈ {1,2}; X = col U, Y = col W; S = I_k + WᵀU;
spec A = {1 (geometric multiplicity 4−k)} ∪ spec S; at ν ∈ spec S: right eigenvector r = Uc (Sc = νc),
left ℓ = Wf (Sᵀf = νf). P_σ e_j = e_{σ(j)}. Cyclic ⟺ rank(M − μI) ≥ 3 ∀μ ∈ F̄.
**Lemma T** (τ = (ab), d = e_a − e_b, E = A − μI, g = nullity E, μ ≠ 0): AP_τ derogatory at μ ⟺
[g ≥ 3] ∨ [g = 2 ∧ (d ∈ col E ∨ d ∈ row E)] ∨ [g = 1 ∧ dᵀr = 0 ∧ dᵀℓ = 0 ∧ 1 + dᵀz = 0, Ez = μd].
A transposition is derogatory only at eigenvalues of A. **Graph lemma**: for a 2-dim S ≤ F⁴, G_S =
{ab : d_ab ∈ S} is a union of cliques with ≥ 2 components (⊆ triangle or ⊆ perfect matching);
G_S ∪ G_{S⊥} ⊆ triangle or ⊆ perfect matching; two such sets never cover K₄.
**Closed already (do not redo):** rank 2 with S = νI (ν ≠ 1); rank 2 with spec S = {1,1}; and:
**Model proof — rank 2, S with a NON-rational eigenvalue pair ν, ν̄ (both ≠ 1).** Failure of (ab) at 1
needs d ∈ X ∪ Y (T2). Failure at ν needs dᵀr = dᵀℓ = 0 with r = Uc, ℓ = Wf; the ν̄-conditions are the
Galois conjugates, hence the SAME conditions on the rational d. Since r, r̄ span X ⊗ F̄ (r is not
rational up to scale, else c would be a rational eigenvector of S), dᵀr = dᵀr̄ = 0 ⟹ d ∈ X⊥; likewise
d ∈ Y⊥. So every failing edge lies in G_X ∪ G_Y ∪ (G_{X⊥} ∩ G_{Y⊥}) ⊆ (G_X ∪ G_{X⊥}) ∪ (G_Y ∪ G_{Y⊥}),
which cannot cover K₄. Some transposition works. ∎
Machine-checked already: exhaustive rank-2 tables over GF(2), GF(3) (every input rescued by a
transposition). Note the scalar clause was NOT needed there.

## The four open cases — close them in this order, each with proof + machine check
**(β-rat) rank 2, spec S = {ν₁, ν₂} ⊂ F, ν₁ ≠ ν₂, both ≠ 1.** Level-set graphs L_j = {ab: ℓ_j(a)=ℓ_j(b)},
R_j = {ab: r_j(a)=r_j(b)}; the ν_j-failure set is ⊆ L_j ∩ R_j ∩ {scalar_j}. Facts: R₁ ∩ R₂ ⊆ G_{X⊥}
and L₁ ∩ L₂ ⊆ G_{Y⊥} (r₁, r₂ span X; ℓ₁, ℓ₂ span Y). A level-set graph is complete iff the eigenvector
is constant, i.e. iff 𝟙 ∈ X (resp. Y) and 𝟙 is an eigenvector of A: A has constant row sums (resp.
column sums) ν_j. Sub-cases: (i) no constant eigenvector: all four level-set graphs have ≥ 2 blocks —
show G_X ∪ G_Y ∪ (L₁∩R₁) ∪ (L₂∩R₂) ≠ K₄ using the ⊥-relations (four "triangle-or-matching" sets CAN
cover K₄ in general, so the relations R₁∩R₂ ⊆ G_{X⊥}, G_X ∪ G_{X⊥} ⊆ T_X etc. are essential — or
bring in the scalar clause `1 + ν dᵀ(A − ν)^# d = 0`, (A−ν)^# = Σ_{λ≠ν} Π_λ/(λ−ν) the group inverse,
an explicit quadratic in the pair {a,b}); (ii) exactly one constant eigenvector; (iii) A has both
constant row and column sums (𝟙 ∈ X ∩ Y). If some sub-case genuinely has all six transpositions
failing, exhibit the family and close it with a 3-cycle or double transposition (rank-2 update:
rank(AP_σ − μ) = rank((A − μ) + μ(I − P_σ⁻¹)), I − P_σ⁻¹ of rank 2 with image = cycle-sum-zero
vectors and kernel = cycle-constant vectors).
**(γ) rank 2, S = one eigenvalue ν ≠ 1 with a Jordan block** (g_A(ν) = 1, ℓᵀr = 0).
**(δ) rank 2, spec S = {1, ν}, ν ≠ 1** (1 has algebraic multiplicity 3, geometric 2; Lemma T's clause at
1 is still d ∈ X ∪ Y; ν simple).
**(ρ) rank 1, A = I + uvᵀ, 1 + vᵀu ≠ 0**: σ must have ≤ 2 cycles. Known: for a 4-cycle, failure at 1 ⟺
Σu = Σv = 0 ∧ e(σ) = 1 (e changes by the 2×2 token determinant under adjacent swaps, so if u ∦ v some
4-cycle is clean at 1; if v = ρu, e is constant); for (3,1) with fixed point f, clean at 1 iff u_f ≠ 0
∧ v_f ≠ 0 — wait: precisely nullity(M − 1) = 1 when u_f ≠ 0 and w_f = v_{σ(f)} = v_f ≠ 0. Other
resonances: 4-cycle at −1 (char ≠ 2: antipodal pair-sums of u and of v equal + secular) and at ±i
(char ≠ 2, i ∈ F̄); (3,1) at primitive cube roots ω (char ≠ 3): Fourier clause û_C(ω) = 0 on the
3-cycle's tokens (forces the three tokens equal when ω ∉ F) + secular; (2,2) at −1. The all-equal
token case (aI + bJ) is PROVED elsewhere (n-cycle else (n−1,1)) — cite, do not redo. Close (ρ) by
sub-cases (u ∦ v; v = ρu with the token multiset not all equal), separately in char 2 and char 3.
Machine check exhaustive over GF(2), GF(3), GF(4), GF(5), GF(7), GF(8), GF(9) (all invertible I + uvᵀ).

## Report
Per case: lemma, proof, the machine-check line (population, failures, controls incl. "always P=I").
Any case not closed: UNRESOLVED with the smallest configuration you could not close. End with
`DONE-K6N4C`.
