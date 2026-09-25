# K6-GC3 — (GC₄) on the rank-one stratum: prove g(I + u wᵀ) ≥ 6 for all u, w ∈ F⁴ (det ≠ 0), every field F

## Conventions (as in K6-GC / K6-GC2)
P_σ e_j = e_{σ(j)}; AP_σ has columns a_{σ(1)}, …, a_{σ(4)}; B cyclic ⟺ minpoly = charpoly ⟺
rank(B − μI) ≥ 3 for every μ in the algebraic closure; g(A) = #{σ ∈ S₄ : AP_σ cyclic}.

## Facts (PROVED unless marked)
* Normalisation (K6-GC2 §1, verified): if g(A) < 6 then, after scaling, right-multiplying by a
  permutation and extending scalars, A = I + R with rank R ≤ 2 and A itself non-cyclic.
* Every sharp example known (g = 6) is a rank-ONE perturbation of a monomial matrix: aI; I + γJ with
  1 + 4γ = ω a primitive cube root (char ∤ 6); over F₂ the 144 non-monomial minimizers are all
  P_w + (rank one) — e.g. P_(14)(23) + (e₃+e₄)(e₃+e₄)ᵀ; and by the normalisation the identity
  permutation may be taken bad.
* COMPUTED over F₃ (13 360 invertible random samples I + uwᵀ): min g = 6, attained by 720 samples; over
  F₅ and F₇ rank ≤ 2 samples: min g = 6 and 11. No g < 6 anywhere.
* The "derangement conjecture" (≤ 3 bad derangements for rank ≤ 2 perturbations of I) is FALSE:
  A = I + uuᵀ with u = (1,1,2,2) over F₃ has g = 8 and its good set consists of eight permutations of
  cycle type (3,1) — all nine derangements are bad. So the good set can avoid 4-cycles entirely.
* For A = I + uwᵀ: AP_σ = P_σ + u (P_σᵀw)ᵀ is a rank-one perturbation of a permutation matrix;
  rank(AP_σ − μI) = rank((P_σ − μI) + u w_σᵀ) with w_σ = P_σᵀ w. For μ not an eigenvalue of P_σ the rank
  is ≥ 3 automatically; so AP_σ is non-cyclic iff for some eigenvalue μ of P_σ (a root of unity of order
  dividing a cycle length of σ) the rank-one update drops rank(P_σ − μI) by one, which happens iff
  u ∈ col(P_σ − μI), w_σ ∈ row(P_σ − μI) and 1 + w_σᵀ (P_σ − μI)⁺ u = 0 in the appropriate sense (the
  transposition-lemma structure T1 of this line; state your own precise version and prove it).

## Questions (mark every statement PROVED / CONJECTURED / COMPUTED / FAILED)
1. Prove: for every field F and all u, w ∈ F⁴ with 1 + wᵀu ≠ 0, g(I + uwᵀ) ≥ 6. (Use the eigenvalue
   description above: for each σ the bad μ must be an eigenvalue of P_σ, i.e. a root of unity; count, for
   each cycle type, how many σ can be killed by the two linear conditions u ⊥ left-kernel(P_σ − μI),
   w_σ ⊥ right-kernel(P_σ − μI) plus the scalar condition, and show the 24 conditions cannot all hold
   for 19 or more σ.) Partial credit: the case w = u (symmetric), or char F = 2, or fields with no
   nontrivial roots of unity of order ≤ 4 beyond ±1.
2. Characterise all (u, w) with g(I + uwᵀ) = 6 over an algebraically closed field.
3. Does the rank-one bound imply the rank-two bound (any idea to reduce rank 2 to rank 1, e.g. by a
   second normalisation using a second bad permutation)?
Web only for literature (DOI). Do not assume a cyclic vector is a standard basis vector.
