# BRIEF K6-WIDE — widen the search: Kourovka 16.95, everything we know, everything that failed, and an open question

Audience: a strong mathematician with web search allowed FOR LITERATURE ONLY (cite what you find with
exact references; do not use search to "solve" the problem). We do not prescribe a method. We want to
know which of our default assumptions to drop and which machinery from other areas applies.

## 0. The problem (Kourovka Notebook 16.95, J. G. Thompson, 2006; open)
For every field F and every A ∈ GL(n, F) there is a permutation matrix P such that AP is cyclic, i.e.
its minimal polynomial equals its characteristic polynomial (equivalently: AP has a cyclic vector;
equivalently: rank(AP − μI) ≥ n − 1 for every μ in an algebraic closure). The only claimed proof
(Dixon, arXiv:1606.02238) was withdrawn in 2017 after a counterexample to its key proposition.
Conventions here: P_σ e_j = e_{σ(j)}, so A P_σ permutes the columns of A. Equivalent reformulations we
use: (i) rank(A − μ Q) ≥ n − 1 for all μ, with Q ranging over permutation matrices (a matrix pencil
question); (ii) GL(n,F) = {cyclic matrices}·{permutation matrices}.

## 1. What is PROVED (all machine-checked; L = also kernel-checked in Lean 4/Mathlib)
P1. n ≤ 3 over every field. [hand proof + exhaustive verifier; L: the notebook's own statement for n = 3]
P2. (Transposition lemma.) For τ = (a b), d = e_a − e_b: P_τ = I − ddᵀ and rank(AP_τ − μI) =
    rank((A − μI) + μ ddᵀ), a rank-one update. Hence, with g = nullity(A − μI) and μ ≠ 0: g = 0 ⟹ AP_τ is
    non-derogatory at μ; g = 1 ⟹ derogatory at μ iff ℓ_a = ℓ_b, r_a = r_b and a scalar condition
    (ℓ, r the left/right eigenvectors); g = 2 ⟹ iff d ∈ col(A − μI) or d ∈ row(A − μI); g ≥ 3 ⟹ always.
    A transposition is derogatory only at eigenvalues of A. [L]
P3. (Rationality.) For μ ∉ F with minimal polynomial m over F: col(A − μI) ∩ Fⁿ = col_F(m(A)); no
    separability needed. [L: quadratic and cubic cases]
P4. If A ∈ GL(n,F) has invariant factors (m, m) with m irreducible of degree n/2, then EVERY
    transposition τ makes AP_τ cyclic. In particular at n = 4: minpoly an irreducible quadratic ⟹ done.
    [hand + exhaustive over GF(2), GF(3); cross-family review clean; L: rank form nearly assembled]
P5. (Deflation.) e_i is a cyclic vector of A P_σ iff, with R = A[≠i, :] (row i deleted), the column
    b = R[:, σ(i)] is a cyclic vector of the (n−1)×(n−1) matrix R[:, σ(≠i)] (controllable pair). So the
    statement (S′): "for every A and EVERY i some σ makes e_i cyclic for AP_σ" is equivalent to
    (T_{n−1}): "every (n−1)×n matrix of rank n−1 admits a column b and an ordering of the other columns
    making b a cyclic vector". (T_{n−1}) ⟹ (S′) ⟹ 16.95. [L: the deflation and Krylov ⟹ minpoly = charpoly]
P6. (T_1), (T_2) over every field. [hand; L for (T_2)] (T_3) holds over every field of characteristic
    0, 2, 3, 5, 7 when some 3×3 minor of the 3×4 matrix vanishes (Gröbner certificates); the "general
    position" case (all four 3×3 minors nonzero) is open.
P7. (S′) holds on ALL of GL(5,2), GL(4,3), GL(4,4) (exhaustive); (T_3) has no counterexample over any
    GF(q), q ≤ 8, exhaustively; (T_4) over GF(2), GF(3); (T_5) over GF(2). No counterexample to 16.95 in
    ≈ 5×10⁸ matrices over 17 (n,q) cells; frontier n = 4 q ≥ 5, n = 5 q ≥ 3, n = 6 q = 2.
P8. Rank-one family A = aI + bJ (J all-ones): 16.95 holds over every field (n-cycle, else (n−1,1)-cycle),
    and the cyclicity of A P_σ depends only on the cycle type of σ (closed-form criterion). The
    "always take an n-cycle" rule is FALSE (char 2, n ≡ 2 mod 4).
P9. Rank-one A = I + uvᵀ at n = 4: 16.95 holds over every field of characteristic 0 and every prime
    characteristic p < 10⁴ (Gröbner unit-ideal certificates: for any i with v_i ≠ 0 some σ makes e_i
    cyclic for AP_σ). An integer certificate for all characteristics is being computed.
P10. (Local structure of the Krylov dimension.) kd(A,σ,i) := dim Krylov(AP_σ, e_i). Under a column
    transposition, kd changes by an exactly computable rank recurrence; the Krylov space K is
    AP_σ-invariant; a transposition (ab) leaves K fixed iff d ∈ K or dᵀK = 0. Exhaustively on GL(3,q≤7),
    GL(4,2), GL(4,3), GL(5,2): strict hill-climbing on kd has local maxima, but "one neutral step then an
    ascent" always exists, and the potential Φ′ = (kd, −#neutral transpositions) has NO local maximum
    below kd = n on any of these cells. The conjecture (Mono): "at every kd-local maximum some neutral
    transposition strictly decreases the number of neutral transpositions" would prove (S′) for all n.
P11. In the layer kd = n − 1 (K = ker ψ, ψ a left eigenvector with ψ_i = 0), a transposition (ab)
    increases kd iff Res(χ_N^{out}, dᵀadj(M − μI)e_i) ≠ 0 and gcd(gcd(χ_N, adj(xI−N)e_i), χ_M) = 1
    (N = M P_τ; χ_N = χ_M + dᵀadj(xI − M)Md) — exact, machine-checked on 1.5×10¹⁰ pairs.

## 2. What FAILED (each refuted by an explicit object; do not reuse without a new reason)
F1. "Some transposition always works" — false: at n = 4 there are A = I + (rank 2) with all six
    transpositions failing (over GF(4), and over GF(7): A_{ij} = f(i ⊕ j) for the Klein four-group,
    f = (2,3,4,6)). Also rank-one A needs σ with ≤ 2 cycles (nullity count), so transpositions never work.
F2. "All-six-transpositions-fail forces characteristic 2" — false (the GF(7) example).
F3. "Every double transposition works when all transpositions fail" — false (the GF(7) example: 2 of 3).
F4. "The group-algebra families A = Σ_{g∈G} f(g)P_g of regular groups G (n = 4: V₄, Z₄; n = 6: Z₆, S₃;
    n = 8: (Z/2)³, Z₈, Z₄×Z₂, D₄, Q₈) contain hard members" — false in all 20 exhaustive cells over
    GF(3,5,7): the members with the fewest good σ are the monomial ones. For σ inside the regular
    copy of an abelian G, the eigenvalues of A P_σ are χ(σ)·f̂(χ) (characters), so cyclic iff injective.
F5. Case trees over the resonances (roots of unity) for rank-one A at n = 4: 2×10⁸ leaves; the
    "everything blocked at μ = 1" branch is inconsistent (896 Gröbner certificates) but the tree is
    the wrong tool. Formal enumeration of failure-pattern graphs for rank 2: 5 361 unrefuted orbits —
    too coarse.
F6. Naive inductions for (T_m): (a) the deflation lands in a weighted statement "(W_m)(R, v)" which is
    FALSE for general weights (repeated-column matrices); (b) fixed-column weighted deflation is false
    over every field; (c) minimum-support pivot residual false; (d) "every bad choice has a base-field
    witness" false (extension-field eigenvalues); (e) a union bound on left-eigenvector cover sizes
    cannot close (overlaps).
F7. Polynomial methods: the symmetrised Krylov determinants Σ_σ D_i(σ) and Σ_σ sgn(σ)D_i(σ) are not
    det-multiples; the Combinatorial Nullstellensatz coefficient on the factorial-base grid is not a
    det-multiple (it certifies (S′) only off a hypersurface). Dixon's greedy (leading minors) provably
    returns P = I on J − I: leading-minor conditions are the WRONG functional (cyclicity is a
    conjugation invariant; 𝓑-membership is not).
F8. Refined potentials (kd, #axes in K), (kd, support of K), (kd, #separated coordinate pairs) all have
    local maxima; K at a local maximum is not always a sum of complete primary components.

## 3. Methods used so far (so you can see our blind spots)
Rank-one/rank-two update algebra; PBH/controllability; Krylov spaces; Frobenius normal form and
invariant factors; Galois descent; cyclic Fourier analysis on cycles of σ (resonances); graph/clique
combinatorics on the failure sets of edges {a,b}; Gröbner bases (msolve, Singular) with Rabinowitsch
saturation; exhaustive finite-field census with controls; Lean 4 kernel checks. Everything is "local"
(one transposition at a time) or "stratified by how derogatory A is".

## 4. The question
Given all of the above: (a) which of our default assumptions should be DROPPED (e.g. working one
transposition at a time; stratifying by nullity; fixing the cyclic vector to be a standard basis
vector; thinking of σ as a modification of A rather than of the pencil (A, P); finite fields as the
model); (b) which machinery from OTHER areas plausibly applies — e.g. representation theory of the
regular representation / group algebras, permanents and Latin squares (the permutation matrices are
the vertices of the Birkhoff polytope), Hall/König-type marriage arguments, Chevalley–Warning or
other counting over finite fields, invariant theory of the pair (A, P) under simultaneous conjugation,
model theory / transfer between characteristics, the theory of matrix pencils (Kronecker), results on
products of cyclic matrices, "cyclic vector" results for perturbations (Wimmer, Thompson's interlacing),
results on when a coset of a subgroup meets a conjugation-invariant set; (c) give THREE attack
directions orthogonal to ours, each with the FIRST concrete lemma to try and how it would be tested on
n = 4, 5 over small fields. If you know a literature result that already decides (S′)/(T_m) or 16.95
for special classes, cite it exactly.
