# ATTACK — Erdős Problem #709, round 2 (Qwen seat): exact small values and multi-boundary expansion (TEMPLATE v2.3, prove-or-refute)

## Statement
f(n) = minimal f such that for every set A of n integers ≥ 2 and every interval I of f·max(A) consecutive integers there are DISTINCT x_a ∈ I (a ∈ A) with a | x_a. (Erdős–Surányi 1959: (log n)^c ≪ f(n) ≪ n^{1/2}; site: f(n) ≫ log n/log log n.)
Hall form: f(n) ≤ k iff for every A and every window I of k·max(A) integers, every B ⊆ A has N_I(B) := #{x ∈ I : some b ∈ B divides x} ≥ |B|.

## Established this campaign (round 1, verified by coordinator scripts; use freely)
- Boundary injection: split I into k blocks J_1..J_k of length m = max A; s_j = #{x ∈ J_j : some b ∈ B divides x}. Then |B| ≤ s_j s_{j+1} for each j < k (a ↦ (last multiple ≤ boundary, first multiple > boundary) is injective since a = difference).
- Consequently f(n) ≤ K(n) := min{k : n ≤ R(k)}, R(k) = k² for k odd, k² + k/2 for k even: R(1..6) = 1, 5, 9, 18, 25, 39. So f(n) ≤ ⌈√n⌉.
- f is nondecreasing (scale all moduli by a large d). f(n) ≥ 2 for n ≥ 2 (A = {n+1..2n}, window {C−n+1..C+n} around C = lcm(A)).
- f(6) ≥ 3: A = {71,80,83,91,92,100}, c = 2436242840, I = [c−99, c+100] (200 = 2·100 integers): the multiples of members of A in I are only c−40, c−31, c+40, c+52, c+60. Hence f(6)=f(7)=f(8)=f(9)=3.
- f(19) ≥ 4: 19 moduli a_d = (431+d)Q+1 (Q = lcm(1..97), M = 463Q+1, window 3M) whose multiples in the window lie on 18 points ("three-layer line system": 19 lines with distinct slopes through 3 layers of 6 points each, embedded by CRT).
- Barrier: the single-boundary bound |B| ≤ s_j s_{j+1} is attained at every scale (complete bipartite line systems), so exponent improvements need ≥ 3 boundaries jointly; residue dynamics p_{j+1}(a) ≡ p_j(a) + m (mod a) where p_j(a) = c_j mod a.
- The "layered-line" construction (one multiple per block, generic lines) cannot give exponent > 1/3 (crossing lemma).

## Targets (prove or refute; every claim with a checkable certificate)
T1 (exact values, k = 3 vs 4): Theorem gives f(n) ≤ 4 for n ≤ 18 and f(19) ≥ 4. Determine f(10): either an explicit A with |A| = 10 and a window of 3·max(A) integers whose neighbourhood has ≤ 9 points (give A, the window start x, and a table of multiples — I will verify by direct computation), or a proof that 3 blocks always suffice for n = 10 (this needs an improvement of R(3) = 9 → 10: a 3-boundary compatibility argument). Then push: smallest n with f(n) ≥ 4 (between 10 and 19).
T2 (smaller certificates): find an f(6) ≥ 3 certificate with max(A) < 100 (or prove max(A) ≥ 14 is needed: brute force says all A ⊆ [2,13] with |A| = 6 satisfy the 2·max(A) property), and an f(n) ≥ 4 certificate with fewer moduli or smaller max(A) than the n = 19 one. Method: two-layer/three-layer line systems: choose layers X_0, X_1, X_2 of small integers, lines with distinct slopes d passing through one point per layer (b, b+d, b+2d), then CRT-embed; the number of lines must exceed |X_0|+|X_1|+|X_2|. Search systematically; report the best (lines − points) found for 3 layers with ≤ 6 points per layer.
T3 (three-boundary inequality): for k = 3 blocks and Hall set B with |B| = r, the pairs (ℓ_1(a), r_1(a)) and (ℓ_2(a), r_2(a)) are linked by r_1(a) + t·a = ℓ_2(a) for some t ≥ 0 with the same a. Prove or refute: s_1 + s_2 + s_3 ≥ r whenever r ≤ 10 (equivalently f(10) ≤ 3). If false, the refutation is a T1 certificate.
T4 (lower-bound growth): using the n = 19 three-layer template, can four layers (window 4·max A) be built with more lines than points? Give the layer sets and slopes explicitly; I will CRT-embed and verify.

## Rules
Number every lemma with a status tag (PROVED / CONDITIONAL / REFUTED / OPEN). Every construction explicit (integers, not descriptions). For any claimed f(n) ≥ k certificate: list A, the window, and for each a ∈ A all its multiples in the window. A check that cannot fail counts as no check. Do not claim exponent improvements without a full proof. Final block: "final claim ← lemmas ← unproved items".

## G2 literature (read before working; do not re-derive)
van Doorn–Li–Tang, "Optimal bounds for an Erdős problem on matching integers to distinct multiples", arXiv:2603.28636 (30 Mar 2026), solves #650: for intervals of length 2·max(A) the guaranteed matching number is exactly min(m, ⌈2√m⌉); lower bound by Hall + two-block boundary injection (the same argument as round 1), upper bound f(st) ≤ s+t by CRT constructions (complete bipartite line systems). Consequences for #709: the 2-block case is closed (f(n) ≥ 3 for n ≥ 6 follows from ⌈2√6⌉ = 5 < 6); anything new must concern k ≥ 3 blocks: the k-block matching number g_k(m) (f(n) = min{k : g_k(n) = n}). Round 1 gives g_k(m) = m for m ≤ R(k). Open: is g_k(m) ≍ k√m for k ≤ √m (which would give f(n) ≍ √n), or do k-block constructions with matching number < m stop at k ≈ m^{1/3} (crossing lemma for layered lines), or earlier?
