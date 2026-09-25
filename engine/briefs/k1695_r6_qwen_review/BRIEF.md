# BRIEF K6-QREV — cross-family adversarial review (Qwen3.8-Max web, via dialogue's Chrome; model identity verified on screen before pasting)

You are a hostile referee. Read the three proofs below and try to BREAK them. Do not summarise, do
not praise. For each proof output exactly one verdict line — VALID / GAP (state the step and why the
inference does not follow) / WRONG (give an explicit counterexample: a field, a matrix, and the
computation) — followed by at most ten lines of justification. Held-out design: you receive
statements and proofs only, no computer-verification tables; if you want to test a claim, compute a
small example yourself and SHOW the computation.

Conventions. F is any field, F̄ an algebraic closure. P_σ is the permutation matrix with
P_σ e_j = e_{σ(j)}, so A P_σ has the columns of A permuted. A square matrix M is cyclic
(nonderogatory) iff its minimal polynomial equals its characteristic polynomial iff
rank(M − μI) ≥ n − 1 for every μ ∈ F̄. For a transposition τ = (a b) put d := e_a − e_b.

## Proof 1 (transposition lemma)
Claim. P_τ = I − ddᵀ, P_τ⁻¹ = P_τ, and rank(A P_τ − μI) = rank((A − μI) + μ ddᵀ) for every A and μ.
Consequently, with E := A − μI and g := dim ker E and μ ≠ 0: (T0) g = 0 ⟹ rank(AP_τ − μI) ≥ n − 1;
(T2) g = 2 ⟹ [rank(AP_τ − μI) ≤ n − 2 ⟺ d ∈ col E or d ∈ row E]; (T3) g ≥ 3 ⟹ rank(AP_τ − μI) ≤ n − 2.
Proof. (P_τ)e_a = e_a − d = e_b, (P_τ)e_b = e_b + d = e_a, other basis vectors fixed; hence P_τ² = I.
Then AP_τ − μI = (A − μP_τ⁻¹)P_τ = (A − μP_τ)P_τ and P_τ is invertible, so rank(AP_τ − μI) =
rank(A − μP_τ) = rank(E + μddᵀ). For a rank-one update: rank(E + xyᵀ) ∈ {rank E − 1, rank E, rank E + 1},
and rank(E + xyᵀ) = rank E + 1 iff x ∉ col E and y ∉ row E. Apply with x = μd, y = d. ∎

## Proof 2 (rationality)
Claim. Let μ ∈ F̄ ∖ F have minimal polynomial m over F, of degree k. Then col(A − μI) ∩ Fⁿ = col_F(m(A))
(column space over F̄ on the left; over F on the right), and the same for rows.
Proof. m(A) = (A − μ)h(A) with h over F(μ), so col_F(m(A)) ⊆ col(A − μ) ∩ Fⁿ. Conversely let w ∈ Fⁿ with
w = (A − μ)z, z ∈ F(μ)ⁿ (a linear system solvable over F̄ is solvable over F(μ)). Write z = Σ_{t<k} μᵗ z_t
with z_t ∈ Fⁿ, and m = Xᵏ + m_{k−1}X^{k−1} + … + m₀, so μᵏ = −Σ_{t<k} m_t μᵗ. Then
w = A z₀ + Σ_{t=1}^{k−1} μᵗ(A z_t − z_{t−1}) − μᵏ z_{k−1} = [A z₀ + m₀ z_{k−1}] + Σ_{t=1}^{k−1} μᵗ [A z_t − z_{t−1} + m_t z_{k−1}].
Since w ∈ Fⁿ and 1, μ, …, μ^{k−1} are F-linearly independent, all bracketed vectors with t ≥ 1 vanish,
so z_{t−1} = A z_t + m_t z_{k−1}; unwinding, z₀ = (A^{k−1} + m_{k−1}A^{k−2} + … + m₁) z_{k−1} and
w = A z₀ + m₀ z_{k−1} = m(A) z_{k−1} ∈ col_F(m(A)). No separability is used. ∎

## Proof 3 (the theorem)
Claim. Let A ∈ GL(4,F) have minimal polynomial m, an irreducible quadratic. Then for EVERY
transposition τ the matrix A P_τ is cyclic. (More generally: invariant factors (m, m), m irreducible
of degree n/2, n even.)
Proof. Suppose rank(AP_τ − μI) ≤ 2 for some μ ∈ F̄. By (T0), μ is an eigenvalue of A, hence a root of m,
so μ ∉ F and μ ≠ 0 (m irreducible, m ≠ X since A is invertible). The invariant factors of A over F are
(m, m) (charpoly = m², minpoly = m, f₁ | f₂ = m, f₁f₂ = m²); invariant factors are unchanged by field
extension, so over F̄ the number of invariant factors divisible by (X − μ) is 2, i.e. dim ker(A − μI) = 2
— this holds whether or not m is separable. By (T2), d ∈ col(A − μI) or d ∈ row(A − μI). By Proof 2 and
m(A) = 0, col(A − μI) ∩ F⁴ = col_F(m(A)) = 0, and likewise for rows; but d ∈ F⁴ ∖ {0}. Contradiction. ∎

Attack points we suggest (check them, and anything else): the μ = 0 boundary in Proof 1; the
"solvable over F̄ ⟹ solvable over F(μ)" step and the inseparable case in Proof 2; the claim
"nullity = number of invariant factors divisible by (X − μ)" and its use over an inseparable extension
in Proof 3; whether the generalisation to degree n/2 needs anything not in the 4×4 proof.
