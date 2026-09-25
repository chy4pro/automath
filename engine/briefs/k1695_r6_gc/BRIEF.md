# K6-GC — the good-count conjecture (GC_n) for Kourovka 16.95 (early pass; engine = compute, line = judge)

## Setting
F any field, A ∈ GL(n,F), P_σ the permutation matrix with P_σ e_j = e_{σ(j)}. A matrix B is *cyclic*
(nonderogatory) iff its minimal polynomial equals its characteristic polynomial iff I, B, …, B^{n−1} are
linearly independent iff rank(B − μI) ≥ n − 1 for every μ in the algebraic closure.
Kourovka 16.95 (open): for every A some AP_σ is cyclic. Proved so far: n ≤ 3 (all fields), n = 4 partially.

Define g(A) := #{σ ∈ S_n : AP_σ cyclic}. Facts (all verified by exhaustive computation, own code):
* g(aI) = (n−1)! exactly: aP_σ is cyclic iff σ is an n-cycle.
* Every monomial matrix DQ (D diagonal invertible, Q permutation) has g ≥ (n−1)!: DQP is a weighted n-cycle whenever QP is an n-cycle.
* g is invariant under A ↦ QAP (Q, P permutation matrices), A ↦ aA, A ↦ Aᵀ.
* min_{A ∈ GL(3,q)} g(A) = 2 = 2! for q = 2, 3, 4, 5, attained by 6 / 12 / 18 / 48 matrices respectively (monomial matrices with non-scalar D usually have MORE than 2 good σ).
* min_{A ∈ GL(4,2)} g(A) = 6 = 3!, attained by exactly 168 matrices forming two orbits under A ↦ QAP: the 24 permutation matrices and 144 non-monomial matrices, e.g. rows (0,0,0,1), (0,0,1,0), (0,1,1,1), (1,0,1,1) over F₂. So minimizers need not be monomial.
* Histogram over GL(4,2): g ∈ {6, 12, 14, 17, 19, 20, 21, 22, 23, 24} with counts 168, 576, 1176, 768, 288, 6624, 3648, 288, 864, 5760.

## Conjecture (GC_n)
For every field F and every A ∈ GL(n,F): g(A) ≥ (n−1)!.  (Strictly stronger than 16.95.)

## Questions (answer what you can; mark every statement PROVED / CONJECTURED / COMPUTED / FAILED)
1. Prove (GC_3): every A ∈ GL(3,F), F arbitrary, has at least TWO permutations σ with AP_σ cyclic. A complete case-free proof is the goal; a proof for all finite fields F_q with q ≥ q₀ is also valuable (it implies all fields for fixed n by the large-field principle: non-cyclicity is stable under field extension and every counterexample specialises to a finite field).
2. Explain the 144 non-monomial minimizers over F₂ at n = 4: find the structure of the example above (which 6 permutations work, and why the other 18 fail) and a general family of non-monomial matrices with g = (n−1)! for larger n, or prove that for n ≥ 5 (or for q ≥ 3) all minimizers are monomial.
3. Any structural reason for the bound: e.g. an injection from n-cycles into good permutations for arbitrary A, or a counting/character argument over F_q (the count Σ_σ 1_{cyclic}(AP_σ) is a coset–class convolution in GL_n(q)).
Do NOT assume a cyclic vector is a standard basis vector; do NOT restrict to transpositions. Web use only for literature (cite with DOI).
