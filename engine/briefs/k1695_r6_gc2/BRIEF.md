# K6-GC2 — the good-count conjecture at n = 4: prove g(A) ≥ 6 for every A ∈ GL(4,F), every field F

## Setting (same conventions as K6-GC)
P_σ e_j = e_{σ(j)}; AP_σ has columns a_{σ(1)}, …, a_{σ(n)}. B is cyclic iff minpoly = charpoly iff
rank(B − μI) ≥ n − 1 for every μ in the algebraic closure iff I, B, …, B^{n−1} are linearly independent.
g(A) := #{σ ∈ S_n : AP_σ cyclic}.

## What is PROVED (do not re-prove; use freely)
* (GC₃): for every field and every A ∈ GL(3,F) at least two σ make e₁ a Krylov-cyclic vector of AP_σ
  (Δ-lemma: with x_i ∈ F² the projection of column a_i to coordinates 2,3, det(e₁, AP_σe₁, (AP_σ)²e₁) =
  x_{i,1}[x_i,x_j] + x_{i,2}[x_i,x_k] for σ = (i,j,k), and at least two of these six numbers are nonzero).
* g is invariant under A ↦ QAP (Q, P permutation matrices), A ↦ aA, A ↦ Aᵀ.
* Monomial DQ: g ≥ (n−1)! (whenever QP is an n-cycle); aI attains (n−1)! exactly.
* Non-monomial minimizers exist: over F₂ at n = 4 exactly 144 (= permutation + rank one, one orbit);
  over fields with char ∤ 6 containing a primitive cube root ω, A = I + γJ with 1 + 4γ = ω has g = 6
  (only the six 4-cycles are cyclic).
* Exhaustive data: min g over GL(4,2) = 6 (168 minimizers); min g over GL(3,q) = 2 for q = 2,3,4,5.

## What FAILS at n = 4 (proved by exhaustive computation over F₂)
The "fixed cyclic vector" strengthening is false: min over GL(4,2) of #{σ : e₁ is Krylov-cyclic for
AP_σ} is 4 < 6 (576 matrices attain 4). So the n = 3 mechanism does not extend verbatim; a proof of
(GC₄) must let the cyclic vector depend on σ (or avoid cyclic vectors: use rank(AP_σ − μI) ≥ 3, or
the exterior form I ∧ B ∧ B² ∧ B³ ≠ 0, or the Coxeter/Hessenberg criterion "B is conjugate into the
unreduced upper-Hessenberg cell").

## Questions (mark every statement PROVED / CONJECTURED / COMPUTED / FAILED)
1. Prove (GC₄): g(A) ≥ 6 for every A ∈ GL(4,F), every field F. Partial credit for: all fields of a
   fixed characteristic; all F_q with q ≥ q₀ (implies all fields for n = 4 by specialisation + the
   large-field principle); or the weaker g(A) ≥ 2 (two good permutations, which is still new at n = 4).
2. If you cannot prove it, find the most likely place it fails: a family A(t) over some field where the
   good set is forced small, and compute g on it (state the field and the exact permutations).
3. Structural question: is there always a good permutation in at least two different cycle types
   (data: over F₂ the 168 minimizers all have good sets with ≥ 2 cycle types)?
Do NOT assume a standard basis vector is cyclic; do NOT restrict to transpositions or n-cycles.
Web use only for literature (cite with DOI).
