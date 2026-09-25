# TICKET K6-N4b — Kourovka 16.95, n = 4, stratum (a): PROVE it over every field along a given skeleton

Self-contained; no internet; write to `engine/harvest/k1695_r6_n4b/` (create): `REPORT.md` (ending
with the literal line `DONE-K6N4B`), every script (Python with the repo's `.venv/bin/python3`, sympy
1.14 available, or C), every log. Exact arithmetic only. You are graded on what you BUILD: a proof is
a sequence of explicitly stated lemmas, each with (i) a proof valid over EVERY field (name where the
characteristic matters), and (ii) a machine check of the lemma's finite-field instances against
brute force with controls. "It is easy to see" is not accepted; a lemma without (ii) is a claim.

## 0. Setting (all of this is proved; use it)
Field F arbitrary, F̄ an algebraic closure. `P_σ e_j = e_{σ(j)}`. M is CYCLIC iff `rank(M − μI) ≥ n−1`
for all μ ∈ F̄. A ∈ GL(4,F) in **stratum (a)**: `A = I + UWᵀ`, U, W ∈ F^{4×k}, rank(UWᵀ) = k ∈ {1,2}
(scaled so the rational derogatory eigenvalue is 1). 16.95 at n = 4 is already proved outside this
stratum. Goal: **for every such A some σ ∈ S₄ makes A P_σ cyclic.**
Known tools:
- **Lemma T** (transposition τ = (ab), d = e_a − e_b, E = A − μI, g = nullity E, μ ≠ 0): AP_τ is
  derogatory at μ iff [g ≥ 3] or [g = 2 and (d ∈ col E or d ∈ row E)] or [g = 1 and ℓ_a = ℓ_b and
  r_a = r_b and 1 + dᵀz = 0, where ℓ, r span the left/right kernels of E and Ez = μd]. A transposition
  is derogatory only at eigenvalues of A.
- **Graph lemma**: for a 2-dimensional subspace S ⊆ F⁴, the graph G_S = {ab : e_a − e_b ∈ S} is a
  disjoint union of cliques with ≥ 2 components, hence ⊆ a triangle or ⊆ a perfect matching; two
  such graphs never cover K₄. Moreover G_S ∪ G_{S⊥} is ⊆ a triangle or ⊆ a perfect matching (S⊥ =
  orthogonal complement for the standard bilinear form): if G_S is a triangle then G_{S⊥} = ∅; if G_S
  = {ab, cd} then G_{S⊥} ⊆ {ab, cd} (nonempty only in characteristic 2); if G_S = {ab} then
  G_{S⊥} ⊆ {cd} ∪ ({ab} in char 2). VERIFY this lemma by enumeration over GF(2), GF(3), GF(5) (all
  2-dim subspaces) before using it.
- **Lemma 0 / cycle structure** for `M = P_σ + u wᵀ` (rank one; `w_i = v_{σ(i)}` when A = I + uvᵀ):
  `nullity(M − μ) = dim(K_μ ∩ w⊥) + ε`, K_μ = ker(P_σ − μ), ε = 1 iff ∃x: (P_σ − μ)x = −u and wᵀx = 1.
  For a cycle C of length ℓ, ker(P_C − μ) is nonzero iff μ^ℓ = 1, spanned by the geometric vector
  (1, μ⁻¹, μ⁻², …) along the cycle; `im(P_C − μ)` = the kernel of the dual geometric functional. So at
  a resonance μ (μ^ℓ = 1 for some cycle length ℓ) the clauses are cyclic Fourier coefficients:
  `ŵ_C(μ) = Σ_{t} w_{c_t} μ^{t}` and `û_C(μ)` (with the matching orientation), and the "secular"
  clause wᵀx = 1. At a non-resonant μ a rank-k update of the invertible P_σ − μ has nullity ≤ k, so
  for k = 1 only resonances matter, and for k = 2 a non-resonant derogatory μ requires the 2×2 matrix
  `I₂ + Wᵀ P_σ (P_σ − μ)⁻¹ U` to be ZERO.
- Rank-one A needs σ with ≤ 2 cycles (types (4), (3,1), (2,2)); rank-two A needs ≤ 3 cycles.

## 1. RANK 2 — skeleton to fill (S := I₂ + WᵀU, spec A = {1,1} ∪ spec S; X := col U, Y := col W;
##    right eigenvector at ν ∈ spec S is Uc (Sc = νc), left is Wf (Sᵀf = νf); g_A(ν) = nullity(S − ν))
(α) **S = νI₂, ν ≠ 1** (A diagonalisable, eigenvalues 1,1,ν,ν; col(A − ν) = Y⊥, row(A − ν) = X⊥).
    Transposition (ab) works iff d ∉ X ∪ Y ∪ X⊥ ∪ Y⊥. By the graph lemma G_X ∪ G_{X⊥} and
    G_Y ∪ G_{Y⊥} cannot cover K₄. DONE — write it out and machine-check: enumerate all (U,W) over
    GF(2), GF(3), GF(4), GF(5) with S scalar and confirm some transposition is cyclic.
(β) **ν₁ ≠ ν₂, both ≠ 1** (possibly conjugate over F). Transposition (ab) fails iff d ∈ X ∪ Y, or
    for some j: [d ⊥ Wf_j and d ⊥ Uc_j and scalar_j]. Note d ⊥ Uc₁ ∧ d ⊥ Uc₂ ⟺ d ∈ X⊥. Characterise
    the configurations where ALL SIX transpositions fail (use the graph lemma for the μ = 1 part and
    the level-set partitions of the four eigenvectors for the rest; a constant eigenvector — e.g.
    A with constant row sums — makes a level-set graph complete, so treat that sub-case explicitly).
    For every such configuration exhibit a 3-cycle or double transposition that works, with proof.
    Machine-check the characterisation and the rescue rule over GF(3), GF(4), GF(5), GF(7).
(γ) **S has one eigenvalue ν ≠ 1 with a Jordan block** (S ≠ νI): g_A(ν) = 1. Same shape as (β)
    with one eigenvalue; also handle it.
(δ) **1 ∈ spec S, other eigenvalue ν ≠ 1**: A has eigenvalue 1 with algebraic multiplicity 3 and
    geometric 2 (Lemma T's clause at 1 is still d ∈ X ∪ Y), plus the simple eigenvalue ν.
(ε) **spec S = {1,1}**: S = I₂ (then (A − I)² = 0, A ~ J₂(1) ⊕ J₂(1)) or S = J₂(1) (A ~ J₃(1) ⊕ J₁(1)).
    Here the ONLY eigenvalue is 1 (g = 2); Lemma T says a transposition fails iff d ∈ X ∪ Y — and the
    graph lemma gives a working transposition immediately. DONE — write it out and check it.
Deliverable for §1: a decision rule "given (U,W) return σ" whose branches are the cases above, with a
proof per branch, and a machine check over GF(2), GF(3) exhaustively (all A with rank(A − I) = 2) and
over GF(4), GF(5), GF(7) on ≥ 10⁵ presentations, with an independent cyclicity oracle and the
"always P = I" negative control.

## 2. RANK 1 — skeleton (A = I + uvᵀ, c := 1 + vᵀu ≠ 0; tokens (u_i, v_i), i = 1..4)
Resonances: type (4): μ⁴ = 1; type (3,1): μ³ = 1 (and μ = 1 from the fixed point); type (2,2): μ² = 1.
In char 2: x⁴−1 = (x−1)⁴, x²−1 = (x−1)², so types (4) and (2,2) resonate only at 1, type (3,1) also at
the primitive cube roots ω (in GF(4) ⊂ F̄). In char 3: x³−1 = (x−1)³, so type (3,1) resonates only at 1.
Proved facts you may use: for a 4-cycle, failure at μ = 1 ⟺ Σu = 0 ∧ Σv = 0 ∧ e(σ) = 1, where
e(σ) = Σ_{t<k} u_{σ(t)} v_{σ(k)} over the cyclic order, and swapping two adjacent tokens changes e by
the 2×2 determinant of the two tokens (so if u, v are NOT proportional some 4-cycle is clean at 1;
if v = ρu then e is constant). For type (3,1) with fixed point f: clean at 1 whenever u_f ≠ 0 and
v_f ≠ 0 (then nullity at 1 is exactly 1).
Fill in:
(i) **v = ρu (proportional)**: choose f with u_f ≠ 0 and a 3-cycle on the rest. Failure at ω (char ≠ 3)
    needs `û_C(ω) = 0` (the three tokens on C are a geometric progression with ratio ω^{±1}; if ω ∉ F
    this forces the three tokens EQUAL) and the secular clause. Show: unless all four tokens are equal
    (the aI + bJ family — ALREADY PROVED, cite it: n-cycle else (n−1,1)), some choice of f and cyclic
    order escapes; handle ω ∈ F separately (then û_C(ω) = 0 is a 2-dim condition — use the two cyclic
    orders and the ≥ 2 choices of f).
(ii) **u, v not proportional**: some 4-cycle is clean at 1. Remaining resonances of the 4-cycle:
    μ = −1 (char ≠ 2): fails iff the antipodal pairs of the cycle have equal u-sums AND equal v-sums
    (plus secular); μ = ±i (char ≠ 2, i ∈ F̄): fails iff (if i ∉ F) antipodal tokens are equal in u and
    in v, (if i ∈ F) `(u_a − u_c) = ±i(u_b − u_d)` and likewise v, plus secular. The 6 four-cycles
    are 3 antipodal pair-partitions × 2 orientations. Show that all six cannot be blocked unless the
    tokens have the shape u = (a,b,b,a), v = (a′,b′,b′,a′) (up to relabelling) — derive this — and
    close that residual shape by a (3,1) or (2,2) permutation with an explicit proof (use type (2,2):
    resonances ±1 only; K_1 = span of the two cycle-indicators; the clause at 1 is L5-type:
    fails iff [both cycle-sums of v vanish] or [both cycle-sums of u vanish]).
(iii) **char 2 and char 3** deserve their own short paragraphs (fewer resonances, but e(σ) and the
    Fourier clauses degenerate).
Deliverable for §2: decision rule + proofs + machine check exhaustive over GF(2), GF(3), GF(4), GF(5)
(all (u,v) with 1 + vᵀu ≠ 0; note over GF(2) `|supp u|` must be even for invertibility) and ≥ 10⁵
presentations over GF(7), GF(8), GF(9), with the independent oracle and the negative control.

## 3. Report
For each lemma: statement, proof, the machine-check line from your log (population, failures,
controls). If a case resists, say UNRESOLVED and print the smallest configuration (F, U, W) you could
not close — that is worth more than a gap papered over. End with `DONE-K6N4B`.
