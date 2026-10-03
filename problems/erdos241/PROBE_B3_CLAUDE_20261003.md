STATUS: OPEN — no constant c < 1.5154 proved. What is proved: (i) a self-contained version of the 1.5154-type bound with an explicit error term and an exact slack term; (ii) a computer-verified barrier: no argument that uses only density-level information can certify c < 1.515264, and numerically such arguments stop at 1.515461, which is above 1.5154.

# Erdős #241 (B₃ sets): clean-room probe, 2026-10-03

Probe conditions: clean room. No web, no papers, no repository files read. Python/numpy/scipy only, at most 2 threads, no SAT/ILP solvers (scipy `linprog` was used for continuous LPs only).

## 0. Summary

* For a B₃ set A ⊆ {1,…,N} with |A| = k, the function D(n) = #{nontrivial ({a,b},c): a+b−c = n} is 0/1-valued (Lemma 1). Testing this packing against the density of A gives k³ ≤ (2/λ₂)·N·(1+o(1)), where λ₂ = inf ∫(g*g)² over probability densities g on [0,1]. Theorem A gives this with an explicit error (1+2N^{−1/6})² and an exact slack term. If λ₂ ≥ 0.574635, this is (2/0.574635)^{1/3} = 1.515465, which matches the stated record to every quoted digit. We have not compared it with the literature.
* The slack in that inequality is exactly a weighted count of holes: points of the translates t + A, |t| ≤ 2h, that are *not* in A+A−A. Near-extremal sets must therefore make A+A−A an almost-perfect packing of the bulk of [0,N] (Proposition B). Any improvement of the constant is equivalent, within this framework, to a lower bound on that hole density.
* Every constraint visible in the limiting density profile is captured by two conditions: the D-density (a+b−c) and the T-density (a+b+c). Bounds on A+A and A−A, the 6-fold energy, sub-interval self-similarity and second-order correlations are all implied or vacuous. We computed this relaxation. An explicit 1280-step profile g₀, checked in exact rational arithmetic, satisfies every density constraint at c = 1.515264 (Proposition C). The discretised min-max values Richardson-extrapolate to 0.5746395, i.e. c = 1.515461. So the record is, to about 6 digits, the exact value of the density relaxation, and density-only arguments cannot reach 1.5154.
* An improvement therefore has to use arithmetic information invisible at the density scale. The precise target is statement (O_η) in §5. We did not prove it. Small exhaustive cases show the relevant packings are nearly perfect at small sizes: cyclic B₃ sets fill 82–93% of Z_M for k ≤ 6.

## 1. Conventions

A ⊆ {1,…,N}, |A| = k, and A is B₃: a+b+c = a'+b'+c' (a ≤ b ≤ c, a' ≤ b' ≤ c' in A) implies (a,b,c) = (a',b',c'). We write f = 1_A.

* r(n) = #{(a,b,c) ∈ A³ ordered : a+b−c = n} = (f*f*f̃)(n), where f̃(x) = f(−x).
* r₃(n) = #{(a,b,c) ∈ A³ ordered : a+b+c = n} = (f*f*f)(n).
* D₂ = {a+b−c : a ≠ b, c ∉ {a,b}} and D₁ = {2a−c : a ≠ c}. r' = r − (2k−1)f. δ(n) := 2 − r'(n).
* R(t) = #{(a,b,c,d) ∈ A⁴ : a+b−c−d = t}.
* λ₂ := inf { ∫_R (g*g)² : g ≥ 0 measurable, supp g ⊆ [0,1], ∫g = 1 } (the L² autoconvolution constant).
* μ₁ := inf { sup_x (g*g*g̃)(x) : same g }.

"Numerically" means floating point. "Exact" means rational-integer arithmetic.

## 2. Statements proved

### Lemma 0 (B₃ ⇒ B₂)
If a+b = c+d, then a+b+x = c+d+x for any x ∈ A, so {a,b,x} = {c,d,x}, so {a,b} = {c,d}.

### Lemma 1 (exact structure of r)
(a) For n ∈ A, r(n) = 2k−1.
(b) For n ∉ A, r(n) = r'(n) ∈ {0,1,2}. r'(n) = 2 iff n ∈ D₂, r'(n) = 1 iff n ∈ D₁, and r'(n) = 0 otherwise. In particular A, D₁ and D₂ are pairwise disjoint and δ ∈ {0,1,2}, with δ = 2 on A.

*Proof.* If c ∈ {a,b}, then a+b−c ∈ A. For n ∈ A, the ordered triples with c = a, b = n or c = b, a = n number 2k−1. Now let c ∉ {a,b}, c' ∉ {a',b'} and a+b−c = a'+b'−c'. Then a+b+c' = a'+b'+c, so {a,b,c'} = {a',b',c} as multisets. If c ≠ c', then c ∈ {a,b}, a contradiction. So c = c' and {a,b} = {a',b'}, which leaves 2 ordered representations if a ≠ b and 1 if a = b. If n ∈ A and n = a+b−c with c ∉ {a,b}, then a+b = n+c, and Lemma 0 gives c ∈ {a,b}, a contradiction. ∎

Counting A ⊔ D₁ ⊔ D₂ ⊆ {2−N,…,2N−1} gives the trivial bound k(k²−k+2)/2 ≤ 3N−2. Hence k³ − k² < 6N, i.e. R₃(N) ≤ (6N)^{1/3}(1+o(1)).

### Lemma 2 (exact 6-fold energy)
Σ_n r₃(n)² = 6k³ − 9k² + 4k.

This is the multiset count 36·C(k,3) + 9·k(k−1) + k. It is checked exactly on every set in §3.

### Theorem A (explicit form of the 1.5154-type bound, with exact slack)
For every B₃ set A ⊆ {1,…,N} with |A| = k and every integer h ≥ 1:

  λ₂ k³ / (N + h − 1) ≤ 2 + 2k²/h − Def_h/(k h⁴),

where Λ(t) = #{(u₁,u₂,u₃,u₄) ∈ {0,…,h−1}⁴ : u₁+u₂−u₃−u₄ = t} and Def_h := Σ_{t≠0} Λ(t) Σ_{d∈A} δ(t+d) ≥ 0.

*Proof.* Let φ = f * 1_{{0,…,h−1}} and m = φ*φ. Then Σ_x m(x)² = Σ_t R(t)Λ(t). We have Λ ≥ 0, Λ is even, ΣΛ = h⁴, and Λ(0) = (2h³+h)/3 ≤ h³.

By Lemma 0, R(0) = 2k² − k. For t ≠ 0, R(t) = Σ_{d∈A} r(t+d) = (2k−1)·1_{A−A}(t) + 2k − Σ_d δ(t+d), using Lemma 1 and the fact that #{d : t+d ∈ A} = 1_{A−A}(t) by Lemma 0. Since |(A−A)∖{0}| = k² − k,

  Σ m² ≤ (2k²−k)Λ(0) + 2k(h⁴ − Λ(0)) + (2k−1)(k²−k)Λ(0) − Def_h ≤ 2kh⁴ + 2k³h³ − Def_h.

For the lower bound, let Φ(s) = φ(⌊s⌋). This is a step function supported on an interval of length L = N + h − 1, with ∫Φ = kh. We have Φ*Φ = Σ_x m(x)·Tri(·−x), where Tri = 1_{[0,1)}*1_{[0,1)}. Then

  ∫(Φ*Φ)² = (2/3)Σm² + (1/3)Σ m(x)m(x+1) ≤ Σm².

Rescaling to [0,1] gives ∫(Φ*Φ)² ≥ λ₂(kh)⁴/L. Comparing the two bounds proves the theorem. ∎

**Corollary A′ (explicit o(1)).** For N ≥ 27, R₃(N) ≤ (2/λ₂)^{1/3} (1 + 2N^{−1/6})^{2/3} N^{1/3}.

*Proof.* From k³ − k² < 6N we get k² ≤ 4N^{2/3} for N ≥ 27: if k ≥ 7, then k³ < 7N; if k ≤ 6, then k² ≤ 36. Take h = ⌈2N^{5/6}⌉ in Theorem A. ∎

With λ₂ ≥ 0.574635 (quoted, not verified here), limsup R₃(N)/N^{1/3} ≤ 1.515465. **This is not an improvement.** It reproduces the stated record from scratch and makes its error term and slack explicit.

### Proposition B (near-extremal sets are near-perfect D-packings; conditional improvement)
Define the hole fraction H_A(t) := (1/2k) Σ_{d∈A} δ(t+d) ∈ [0,1]. It is the fraction of the translate t+A outside A+A−A, with D₁ points counted as half-holes. Define the weighted mean H̄ := Σ_{t≠0}Λ(t)H_A(t) / Σ_{t≠0}Λ(t). Then Def_h ≥ 2k h⁴ (1−1/h) H̄, and Theorem A gives

  (1 − 1/h) H̄ ≤ 1 + k²/h − λ₂k³ / (2(N+h−1)).

(i) If λ₂k³ ≥ 2(1−η)N, then with h = ⌈2N^{5/6}⌉ we get H̄ ≤ η + O(N^{−1/6}). Almost every translate t+A with |t| ≤ 4N^{5/6} lies almost entirely inside D₂.
(ii) Conversely, suppose H̄ ≥ η for all B₃ sets A ⊆ [1,N] with |A| ≥ 1.5N^{1/3} and all large N. Then limsup R₃(N)/N^{1/3} ≤ ((1−η)·2/λ₂)^{1/3}. ∎

### Proposition C (density barrier; exact rational verification)
Consider the density relaxation: find the largest c for which some probability measure ν on [0,1] satisfies

  (D) c³ (ν*ν*ν̃) ≤ 2 (as measures vs Lebesgue),
  (T) c³ (ν*ν*ν) ≤ 6,
  (S) ν(I) ≤ |I|^{1/3} for all intervals I ⊆ [0,1].

(D) is the limiting form of Lemma 1, and (T) is the limiting form of uniqueness of 3-sums. (S) says that A ∩ (N·I) is again B₃, in the extremal regime c = limsup. Every other density-level consequence we found is implied by (D), (T), (S) or vacuous (§4).

Facts:
1. Any feasible c satisfies c³ ≤ 2/μ₁ ≤ 2/λ₂. To see this, test (D) against ν: ⟨ν*ν*ν̃, ν⟩ = ‖ν*ν‖₂². So μ₁ ≥ λ₂.
2. **Exact:** there is a symmetric step function g₀ with 1280 equal steps on [0,1], found by sequential LP and rationalised with denominator 10¹². For it, sup(g₀*g₀*g̃₀) ≤ 0.5748641453 and sup(g₀*g₀*g₀) ≤ 0.5748641453. (S) holds on every proper subinterval, checked numerically on a quarter-bin grid: ν(I)/|I|^{1/3} < 1, and the ratio tends to 1 only as I → [0,1]. For I = [ε,1] or [0,1−ε] this is immediate because g₀ ≥ 19 on the end bins. Also ∫(g₀*g₀)² = 0.5747892639.
   The sup bound is rigorous: g*g*g̃ = Σ_t q_t B(x − t/n), where q = p*p*p̃ and B is the density of U₁+U₂−U₃ with U_i uniform on [0,1/n). The translates of B form a partition of unity with sum n, so sup ≤ n·max q, and max q is computed exactly in integers.
   Hence g₀ is feasible for c = (2/0.5748641)^{1/3} = **1.515264**. No argument using only (D), (T), (S) can prove c < 1.515264. Also λ₂ ≤ 0.5747893, so the record's own route can never go below (2/0.5747893)^{1/3} = 1.515330.
3. **Numerical:** the discretised min-max values n·min max(p*p*p̃) for n = 80, 160, 320, 640, 1280 are 0.578249, 0.576440, 0.575539, 0.575089 and 0.574864, with O(1/n) convergence. Richardson extrapolation (2μ_{2n} − μ_n) gives 0.574631, 0.574637, 0.574639, 0.5746395, so μ₁ ≈ 0.5746395 ≈ λ₂. The relaxation value is c ≈ 1.515461, which is **above 1.5154**. A hit through density arguments alone would need μ₁ > 2/1.5154³ = 0.574709, and the evidence says it is not.
   At the optimiser, g*g*g̃ is constant (= μ) on [0,1] (max − min < 1e−13) and ≤ 0.555 on [−1,0) ∪ (1,2]. So the record's g-averaged test loses nothing. g is singular at both ends, with the first-bin value scaling as √n (consistent with g ~ x^{−1/2}), and g(1/2) ≈ 0.645. (T) has slack factor 3: c³·sup(g*g*g) = 2.0 ≤ 6.
4. A closed-form certificate (floating point): the 1600-step discretisation of 0.97·arcsine + 0.03·uniform has n·max q = 0.576477, so c_dens ≥ 1.51385.

### Proposition D (second order gives nothing new)
For every finite A ⊂ Z and every t: Σ_n r(n)r(n+t) = Σ_n r₃(n)r₃(n+t). Both sides count the solutions of x₁+x₂+x₃−x₄−x₅−x₆ = t. Consequently, under B₃, |D₂ ∩ (D₂−t)| = 9|T ∩ (T−t)| + O(k²) for t ∉ A−A, where T is the set of 3-sums of distinct elements. Pair correlations of the D-packing are exactly determined by those of the T-packing, so no inequality can come from comparing them.

### Remark E (cyclic analogue)
Let A ⊆ Z_M be B₃ mod M with u = 1_{A ∪ D₁ ∪ D₂}, F = f̂ and ξ ≠ 0. Then 2û(ξ) = F(ξ)(|F(ξ)|² − 2k + 2) + F(2ξ)·conj(F(ξ)), and Σ_{ξ≠0}|û|² = |U|(M−|U|).

In a perfect tiling (|U| = M = k(k²−k+2)/2), every ξ ≠ 0 has F(ξ) = 0 or ||F(ξ)|² − (2k−2)| = |F(2ξ)| ≤ k. Parseval (Σ|F|² = kM − k², Σ|F|⁴ = (2k²−k)M − k⁴ over ξ ≠ 0) together with Bhatia–Davis on [k−2, 3k−2] then forces F to vanish on at least about M/3 of the characters.

For near-perfect packings, the moment identity E[X(X−2)²] = 2 − k³/M + o(1), with X = |F|²/k, forces X to be concentrated near {0, 2}. However, the norm argument (∏|F(ξ)| ≥ 1 over a Galois orbit) only bounds the packing defect by η ≳ k^{−2}. This does not give a constant improvement, even in Z_M.

## 3. Numerical sanity checks

Every set below was checked as follows: brute-force B₃ check; r' ∈ {0,1,2} and r' = 0 on A; Σr₃² = 6k³−9k²+4k exactly; R(0) = 2k²−k; and R(t) ≤ 2k + (2k−1)1_{A−A}(t) for all t ≠ 0. All passed.

"cover" is the fraction of [min A, max A] lying in A ∪ D₁ ∪ D₂. "sat" is the mean of R(t)/2k over |t| ≤ N/8 with t ∉ A−A; the record inequality is tight only if sat → 1. Sets are shifted so that min A = 0, and N = max A + 1.

| set | k | N | k/N^{1/3} | cover | sat |
|---|---|---|---|---|---|
| exhaustive optimum {0,1,4} | 3 | 5 | 1.754 | 1.000 | – |
| exhaustive {0,1,7,11} | 4 | 12 | 1.747 | 0.917 | – |
| exhaustive {0,1,15,18,23} | 5 | 24 | 1.733 | 0.958 | 0.700 |
| exhaustive {0,2,11,26,42,45} | 6 | 46 | 1.675 | 0.870 | 0.583 |
| exhaustive {0,1,7,50,59,78,82} | 7 | 83 | 1.605 | 0.783 | 0.686 |
| Bose–Chowla q=5 (best dilation/rotation) | 5 | 38 | 1.487 | 0.605 | 0.150 |
| Bose–Chowla q=7 | 7 | 124 | 1.404 | 0.613 | 0.357 |
| Bose–Chowla q=11 | 11 | 628 | 1.285 | 0.513 | 0.383 |
| Bose–Chowla q=13 | 13 | 1153 | 1.240 | 0.499 | 0.411 |
| Bose–Chowla q=17 | 17 | 2744 | 1.214 | 0.490 | 0.424 |
| Bose–Chowla q=19 | 19 | 4049 | 1.192 | 0.460 | 0.393 |
| Bose–Chowla q=23 | 23 | 8032 | 1.149 | 0.454 | 0.403 |
| greedy on [0,10³] | 11 | 745 | 1.213 | 0.438 | 0.382 |
| greedy on [0,10⁴] | 19 | 7839 | 0.957 | 0.240 | 0.265 |
| greedy on [0,10⁵] | 33 | 88545 | 0.740 | 0.120 | 0.156 |
| random-order greedy, best of 20, [0,10³] | 11 | 959 | 1.116 | 0.325 | 0.244 |
| random-order greedy, best of 20, [0,10⁴] | 19 | 9472 | 0.898 | 0.195 | 0.160 |

Notes on the table:

* **Exhaustive rows.** These are minimal-span searches (exhaustive, with reflection symmetry and span pruning). For each k, the minimal N with R₃(N) ≥ k is 5, 12, 24, 46 and 83 for k = 3, …, 7. The k = 8 search did not finish within its 600 s cap.
* **Bose–Chowla rows.** We used F_{q³} with a primitive θ, took A = {log(θ+u) : u ∈ F_q} mod q³−1, and verified B₃ mod q³−1. We then took the best of ≤ 400 dilations by units, each with its optimal rotation.
* **Small N.** The ratios above 1.5154 at N ≤ 83 are lower-order effects. Corollary A′ at N = 83 gives R₃ ≤ 10.34.

**Cyclic exhaustive** (0 ∈ A). The minimal M admitting a B₃ set mod M of size k is 13, 30, 65 and 117 for k = 3, 4, 5, 6. The packing bound is L(k) = k(k²−k+2)/2 = 12, 28, 55, 96, so the fill L(k)/M is 0.923, 0.933, 0.846 and 0.821. The k = 7 search started at M = 154 and did not finish within its 900 s cap.

## 4. Routes tried and the exact obstruction

1. **Using the full D-profile (sup) instead of the ν-averaged test.** The gain is at most 1.515465 → 1.515264 rigorously, and ≈ 4·10⁻⁶ numerically, because the L² optimiser already has g*g*g̃ ≡ λ₂ on [0,1] and smaller values outside (Proposition C).
2. **T-density (a+b+c).** It has slack factor 3 at the extremal profile and cannot bind.
3. **A+A and A−A bounds** (r_{A+A} ≤ 2, r_{A−A} ≤ 1). These are B₂ consequences involving k² = O(N^{2/3}) = o(N) points, so they are invisible at density scale. Their only effect is the O(k²/h) terms in Theorem A.
4. **(A+A) ∩ (A+A+x) (S = A⊕A).** By Lemma 1, the weighted count R(x) is exactly (2k−1)·1_{A−A}(x) + 2k − Σ_d δ(x+d). Using this at x near 0 *is* Theorem A.
   * "Joint compatibility" for a fixed x is automatic. Write x+d = a+b−c with d ∉ {a,b} (otherwise x ∈ A−A). Then x+c = a+b−d. So d ↦ c is an involution on {d : x+d ∈ D}, and saturation at one x imposes nothing further.
   * Compatibility across different x is exactly the global packing question (O_η).
5. **Fourier moments on minor arcs.** With X = |f̂|²/k, we have E X ≈ 1, E X² ≈ 2 and E X³ = 6 − c³∫|ĝ|⁶. The only constraint, E[X(X−2)²] ≥ 0, is c³∫|ĝ|⁶ ≤ 2. This is implied by (D) and weaker than the record. Going further needs an upper bound on the 4-fold energy E₄, but B₃ only gives E₄ ≤ 6k⁵, which is useless after normalisation.
6. **6-fold positive-definite form 3A−3A.** For t ≠ 0, r_{3A−3A}(t) ≤ 2k³ + O(k²). This gives c³∫|ĝ|⁶ ≤ 2, which is weaker.
7. **Second-order correlations of D vs T.** These are identical by Proposition D, so there is no information at second order. Third-order correlations of D and T are different Fourier objects (|F|²F vs F³), but we found no inequality linking them.
8. **Self-similarity on sub-intervals.** Not binding at g₀: ν(I) < |I|^{1/3} on proper subintervals, with the ratio tending to 1 only as I → [0,1].
9. **Joint (a+b+c, a+b−c) lattice counts.** These involve k³L²/N² ≪ L² points per L×L box, which is vacuous.
10. **Cyclic/local packing.** Any argument that sees only local packing would also bound cyclic B₃ sets. Cyclic optima for k ≤ 6 fill 82–93% of Z_M, and Remark E's algebraic route only yields an η ≳ k^{−2} defect. An improving argument must be asymptotic and global.
11. **Exact small windows / Erdős–Turán-style boundary counting.** These only affect lower-order terms. The leading constant is fixed by the density relaxation.

## 5. Precise open target

**(O_η)** There are η > 0 and N₀ such that every B₃ set A ⊆ [1,N] with N ≥ N₀ and |A| ≥ 1.5N^{1/3} has Λ_h-weighted hole fraction H̄ ≥ η, for h = ⌈2N^{5/6}⌉.

In words: A+A−A cannot almost-perfectly pack the εN-neighbourhood of A. By Proposition B(ii), (O_η) implies limsup ≤ (2(1−η)/λ₂)^{1/3}, which is < 1.5154 for η > 1.3·10⁻⁴ if λ₂ ≥ 0.574635.

By Proposition C, (O_η) cannot follow from density-level information. It needs arithmetic input, for example a spectral two-valuedness obstruction localised to [0,N]. We have no such argument.

## 6. Cost

All CPU time was single-process with ≤ 2 threads, about 32 min in total:

| task | CPU time |
|---|---|
| Sequential-LP optimisation, n = 20–1280 | ≈ 3 min |
| Exact rational checks | < 10 s |
| Integer exhaustive search (k ≤ 7 done; k = 8 cut at 600 s) | ≈ 10.2 min |
| Cyclic exhaustive search (k ≤ 6 done; k = 7 cut at 900 s) | ≈ 15 min |
| Constructions and diagnostics | ≈ 45 s |
| Miscellaneous | ≈ 2 min |

No external services were used, nothing was posted, and no agents were spawned. Scripts were run in a scratch area and are not committed. The SLP procedure (trust-region linearisation of max(p*p*p̃) over the simplex, then upsampling) and the exact-check procedure are fully described above.
