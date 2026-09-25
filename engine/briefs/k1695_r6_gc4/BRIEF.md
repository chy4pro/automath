# K6-GC4 — rank-one stratum of (GC₄), second attempt: prove g(I + uwᵀ) ≥ 6 with the CORRECT accounting

## Conventions (as before)
P_σ e_j = e_{σ(j)}; AP_σ = P_σ + u w_σᵀ with (w_σ)_j = w_{σ(j)}; B cyclic ⟺ rank(B − μI) ≥ 3 ∀μ ∈ F̄;
g(A) = #{σ : AP_σ cyclic}. A = I + uwᵀ, 1 + wᵀu ≠ 0, F any field.

## Verified facts (exhaustive over all (u,w) for F₂, F₃, F₄; 30 000 samples over F₅, F₇)
* min g(I + uwᵀ) = 6 in every cell — the statement is very likely TRUE.
* The identity and all six transpositions are ALWAYS bad (rank(P_τ − I) = 1, so rank(AP_τ − I) ≤ 2). PROVED.
* Hence g ≥ 6 ⟺ b_(2,2) + b_(3,1) + b_(4) ≤ 11, where b_type = number of bad permutations of that type
  (3 double transpositions, 8 three-cycles, 6 four-cycles).
* A previous attempt claimed b_(3,1) + b_(4) ≤ 8 ("every bad 4-cycle has two good 3-cycle faces"). This is
  FALSE: for the transposition matrix A = P_(24) = I + uwᵀ, u = (0,1,0,−1), w = (0,−1,0,1), ALL six
  4-cycles and four 3-cycles are bad (b_(3,1) + b_(4) = 10) and only one double transposition is bad;
  g = 6 with good set {two double transpositions, four 3-cycles}. Maximum observed b_(3,1) + b_(4) is 10.
* Equality cases (g = 6) with u, w ≠ 0 exist in every characteristic and are NOT only I + γJ:
  transposition matrices (all characteristics); over F₅: u = (4,0,1,0), w = (1,1,4,4) (A has 8 nonzero
  entries, good set = four 3-cycles + two 4-cycles); over F₂ the nontrivial minimizers are exactly the
  4 orbits (u,w) ∈ {(e₃+e₄, e₃+e₄), (e₃+e₄, e₁+e₂), (e₃+e₄, 𝟙), (𝟙, e₃+e₄)} up to simultaneous
  permutation and reciprocal scaling; over F₃ also 4 orbits, three of them non-monomial.
* Cyclicity test for AP_σ: it is bad iff for some eigenvalue μ of P_σ (a root of unity whose order divides
  a cycle length of σ) the rank-one update drops rank(P_σ − μI) by one: with M = P_σ − μI of corank 1
  (μ a simple eigenvalue) this is q ⊥ u, p ⊥ w_σ and 1 + w_σᵀ M⁺ u = 0 (q, p the left/right kernel
  vectors); with corank 2 (e.g. μ = 1 for a 3-cycle, or μ = ±1 for a double transposition) it is
  u ∈ col M or w_σ ∈ row M.

## Task (mark every statement PROVED / CONJECTURED / COMPUTED / FAILED)
1. Prove b_(2,2) + b_(3,1) + b_(4) ≤ 11 for every field and every (u, w) with 1 + wᵀu ≠ 0. Suggested
   route: write each badness as an explicit polynomial condition in (u, w) per (σ, μ); show the 17
   conditions cannot hold for 12 of the 17 permutations simultaneously, e.g. by exhibiting, for every
   12-subset, a polynomial identity (Nullstellensatz certificate) or a direct linear-algebra contradiction;
   organise by the number of bad double transpositions (0, 1, 2, 3) — when all three double
   transpositions are bad show b_(3,1) + b_(4) ≤ 8, when exactly one is bad show ≤ 10, etc.
   Partial credit: the symmetric case w = u; or characteristic 2 (only μ = 1 exists for 2- and 4-cycles and
   μ ∈ {1, ω, ω²} for 3-cycles); or all fields of characteristic ≠ 2, 3.
2. Is every equality case (g = 6) of the rank-one stratum, over an algebraically closed field, of one of
   the forms: A monomial; A = I + γJ with 1 + 4γ a primitive cube root of unity; or A ∈ the orbit of one of
   the explicit sporadic patterns above? Give the complete list or a counterexample.
Do not reuse the face-matching lemma. Web only for literature (DOI).
