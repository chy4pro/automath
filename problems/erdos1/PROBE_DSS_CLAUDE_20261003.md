STATUS: PARTIAL. The constant √(2/π) is NOT beaten and the exponent 1/2 is NOT improved. What is proved here (clean room, novelty and priority NOT checked, G2 required) is a parity refinement, a_n ≥ 2·C(n−1, ⌊(n−1)/2⌋) for all n ≥ 2. For even n this equals C(n, n/2). For odd n it is larger than C(n, (n−1)/2) by the factor (n+1)/n. So target (c) is met only in a weak form: for odd n only, the second-order coefficient goes from −3/4 to +1/4, which makes the uniform-in-n bound a_n ≥ √(2/π)·2^n·n^{−1/2}·(1 − 1/(4n)) hold for all n ≥ 2. Also proved: a two-regime reduction that pins down the only regime where improving the constant can fail, conditional "k-fold" bounds, and exact obstruction statements.

# Erdős Problem #1 (distinct subset sums): clean-room probe, 2026-10-03

Rules followed: no web access, no papers, no repository files read. Only standard mathematics and local computation were used. Harper's vertex-isoperimetric theorem (1966) is used as a standard black box.

---

## 0. Conventions and standard facts

- A = {a_1 < … < a_n} ⊂ Z_{>0} has distinct subset sums (DSS). Write β(m) := C(m, ⌊m/2⌋).
- **±1 form.** For ε ∈ Q_n := {−1, 1}^n put X(ε) := Σ_i ε_i a_i = 2·Σ_{i∈T} a_i − Σ_i a_i, where T = {i : ε_i = 1}.
- **(F1)** A is DSS ⟺ X is injective. All values of X lie in the coset s + 2Z, where s := Σ a_i mod 2.
- **(F2)** X(−ε) = −X(ε). So for n ≥ 1, X never vanishes (X(ε) = 0 would give X(ε) = X(−ε)), and exactly 2^{n−1} values of X are negative.
- **(F3)** An open interval of length 2L (L ∈ Z_{>0}) contains at most L points of s + 2Z.
- **(F4)** Every subset of a DSS set is DSS.
- **(H) Harper.** For B ⊆ Q_m let ∂B := {x ∈ B : x has a neighbour outside B} be the inner vertex boundary. If |B| = 2^{m−1}, then |∂B| ≥ β(m).
  *Derivation from Harper's theorem.* Harper's theorem says |N[S]| ≥ |N[I]|, where N[S] = S ∪ (neighbours of S) and I is the initial segment of the simplicial order with |I| = |S|. Note ∂B = N[B^c] ∖ B^c and |B^c| = 2^{m−1}.
  - m odd: I is the Hamming ball of radius (m−1)/2. N[I] is the ball of radius (m+1)/2, so |N[I]| − |I| = C(m, (m+1)/2) = β(m).
  - m even: I is the ball of radius m/2 − 1 together with the β(m)/2 sets of size m/2 that contain a fixed element. N[I] adds the other β(m)/2 sets of size m/2 and the β(m)/2 sets of size m/2+1 that contain the fixed element. So |N[I]| − |I| = β(m).
- **(F5) Halfspace boundary lies in a window.** Let A be DSS with maximum M and let B = {ε : X(ε) < 0} (|B| = 2^{n−1} by F2). Every ε ∈ ∂B satisfies X(ε) ∈ (−2M, 0). Reason: a neighbour ε′ ∉ B differs from ε in one coordinate i, and X(ε′) = X(ε) ± 2a_i > 0 > X(ε) forces X(ε) > −2a_i ≥ −2M. Combining with (H) and (F1) gives #{ε : X(ε) ∈ (−2M, 0)} ≥ β(n). Together with (F3) this is the Harper-type bound a_n ≥ β(n) (rederived here; the brief attributes the √(2/π) constant to Dubroff–Fox–Xu).

---

## 1. Theorem 1 (folded Harper bound)

**Theorem 1.** For every DSS set with n ≥ 2 elements, a_n ≥ 2·β(n−1). If a_n ≡ Σ_i a_i (mod 2), then in fact a_n ≥ 2β(n−1) + 1.

**Proof.** Let Y(ε′) := Σ_{i<n} ε′_i a_i for ε′ ∈ Q_{n−1}. By (F4) A′ := A ∖ {a_n} is DSS, so by (F1) and (F2) Y is injective, odd (Y(−ε′) = −Y(ε′)) and never 0.

1. *Fold.* We have X(ε′, ε_n) = Y(ε′) + ε_n a_n. So X ∈ (−a_n, a_n) holds exactly when either ε_n = +1 and Y ∈ (−2a_n, 0), or ε_n = −1 and Y ∈ (0, 2a_n). Since Y is odd,
   #{ε : X(ε) ∈ (−a_n, a_n)} = #{Y ∈ (−2a_n, 0)} + #{Y ∈ (0, 2a_n)} = 2·#{ε′ : Y(ε′) ∈ (−2a_n, 0)}.
2. *Window.* By (F1) and (F3), the left side is at most #((s + 2Z) ∩ (−a_n, a_n)). That number is a_n, or a_n − 1 when a_n ≡ s.
3. *Harper in dimension n−1.* Apply (F5) to A′, whose maximum is a_{n−1}: #{Y ∈ (−2a_{n−1}, 0)} ≥ β(n−1). Since (−2a_{n−1}, 0) ⊂ (−2a_n, 0), we get a_n ≥ 2β(n−1). ∎

**Comparison with C(n, ⌊n/2⌋).** By Pascal, β(n) = C(n−1, ⌊n/2⌋) + C(n−1, ⌊n/2⌋−1) ≤ 2β(n−1), with equality iff n is even. For odd n, 2β(n−1) = ((n+1)/n)·β(n).

**Asymptotics.** All are of the form √(2/π)·2^n·n^{−1/2}·(1 + c/n + O(n^{−2})), with c as below. The coefficients were also confirmed numerically to 5 digits at n = 20000/20001 (Table B).

| quantity | c |
|---|---|
| β(n), n even | −1/4 |
| β(n), n odd | −3/4 |
| 2β(n−1), n odd | +1/4 |

**Corollary 1.** For all n ≥ 2, a_n ≥ √(2/π)·2^n·n^{−1/2}·(1 − 1/(4n)).

*Proof.*
- **n = 2k even.** By Stirling, C(2k, k) = 4^k (πk)^{−1/2} e^{θ_{2k} − 2θ_k}, with remainders satisfying 1/(12m) − 1/(360m³) < θ_m < 1/(12m). So the exponent is greater than −x − y, where x = 1/(8k) and y = 1/(2880k³). For k ≥ 1, e^{−x−y} ≥ 1 − (x+y) + (x+y)²/2 − (x+y)³/6 ≥ 1 − x, so β(n) ≥ 4^k (πk)^{−1/2}(1 − 1/(8k)), which is the claim.
- **n = 2k+1 odd.** It suffices that (1 − 1/(8k))·√((2k+1)/(2k)) ≥ 1 − 1/(8k+4). This holds because (1 − 1/(8k))²(1 + 1/(2k)) = 1 + 1/(4k) − 7/(64k²) + 1/(128k³) ≥ 1.
- Also checked directly: no violation for 2 ≤ n ≤ 3000. ∎

**Equality cases and small n.** Equality a_n = 2β(n−1) holds for n = 2 ({1,2}) and n = 3 ({1,2,4} and {2,3,4}). For 4 ≤ n ≤ 8, exhaustive search gives min a_n = 7, 13, 24, 44, 84, against 2β(n−1) = 6, 12, 20, 40, 70.

**What this is and is not.** The first-order constant is unchanged. The gain is purely a parity effect. For odd n, the Harper step in dimension n happens at an exact ball size: the half-cube is the radius-(n−1)/2 ball, whose boundary layer C(n, (n+1)/2) is "unlucky" compared with the smooth interpolation. Folding off a_n moves the isoperimetric step to the even dimension n−1, where the count 2β(n−1) is larger. The argument is short, so it may already be in the literature. Do not claim priority without G2.

---

## 2. Other proved statements

### 2.1 Classical bounds, rederived
Constants are in units of 2^n/√n.

- **(a) Second moment.** E X² = Σ a_i². The 2^{n−1} positive values of X are distinct points of s + 2Z, so Σ a_i² ≥ (4^n − 1)/3, hence a_n ≥ ((4^n − 1)/(3n))^{1/2}. Constant 1/√3 ≈ 0.577. The plain Chebyshev-window version gives only 2/(3√3) ≈ 0.385.
- **(b) First absolute moment.**
  - Lower bound: E|X| ≥ 2^{n−1}, by the same counting.
  - Upper bound: t ↦ E|Σ ε_i t_i| is convex, so its maximum over [0, a_n]^n is at a vertex. Also E|S_k| is nondecreasing in k, where S_k is a sum of k independent signs. Hence E|X| ≤ a_n·E|S_n| = a_n·n·β(n−1)/2^{n−1}.
  - Result: a_n ≥ 4^{n−1}/(n·β(n−1)) ~ √(π/8) ≈ 0.627.
- **(c) Parseval.** For DSS sets, ∫_0^1 Π_i cos²(π a_i t) dt = 2^{−n} exactly. On |t| ≤ 1/(2a_n) we have cos²(π a_i t) ≥ cos²(π a_n t). This gives 2^{−n} ≥ C(2n, n)/(4^n a_n), so a_n ≥ C(2n, n)/2^n ~ 1/√π ≈ 0.564. This is weaker because it uses only the L² shadow Σ(count)² = Σ count.
- **(d) Harper.** (F5) with (F3) gives a_n ≥ β(n) ~ √(2/π) ≈ 0.798.

### 2.2 Lemma F (band-limited positive-definite kernel, keeps the variance ratio)
Let ρ := Σ a_i² / (n a_n²) ∈ (0, 1]. Then

a_n ≥ 2^{n−1} ∫_{−1}^{1} (1 − |s|)·cos(πs/2)^{ρn} ds = (1 − O(n^{−1/2}))·√(2/(πρ))·2^n/√n.

**Proof.**
1. *Kernel.* Let K̂(ξ) := h(4a_n ξ), where h(s) = (1 − |s|)_+ = 1_{[−1/2,1/2]} ∗ 1_{[−1/2,1/2]}. Its inverse transform K is ≥ 0 and K(x) = O(x^{−2}).
2. *Fourier identity.* Σ_ε K(X(ε)) = ∫ K̂(ξ) Σ_ε e^{2πiξX(ε)} dξ = 2^n ∫ K̂(ξ) Π_i cos(2πξ a_i) dξ.
3. *Lower bound on the product.* On supp K̂ we have |2πξ a_i| ≤ π/2. The function φ(x) := −log cos √x = Σ_{k≥1} −log(1 − 4x/((2k−1)²π²)) is convex on [0, π²/4) with φ(0) = 0. Hence φ(λx) ≤ λφ(x) for λ ∈ [0, 1]. Taking λ = a_i²/a_n² gives Π_i cos(2πξ a_i) ≥ cos(2πξ a_n)^{ρn}.
4. *Upper bound.* K ≥ 0 and X is injective into s + 2Z, so Σ_ε K(X(ε)) ≤ Σ_{x∈s+2Z} K(x). By Poisson summation this equals ½ Σ_m K̂(m/2) e^{πims} = K̂(0)/2, because supp K̂ ⊂ (−½, ½).
5. *Conclusion.* Substitute ξ = s/(4a_n) to get 2^n (4a_n)^{−1} ∫ h(s) cos(πs/2)^{ρn} ds ≤ h(0)/2. ∎

With ρ = 1 this is a self-contained Fourier proof of the √(2/π) constant. At second order it is weaker than β(n): 0.750 vs 0.790 at n = 79 (Table A).

### 2.3 Theorem 3 (two-regime reduction: where the constant can fail to improve)
Let U := Σ_i (1 − a_i/a_n), the total relative deficit. For every DSS set with n ≥ 2:

- **(i)** a_n ≥ (β(n) − 1)/U.
- **(ii)** a_n ≥ 2^{n−1} ∫_{−1}^{1} (1 − |s|) cos(πs/2)^{n−U} ds = (1 − O(n^{−1/2}))·√(2/π)·2^n/√(n − U).

**Consequence.** Fix ε ∈ (0, 1).
- If U ≤ 1 − ε, then a_n ≥ (β(n) − 1)/(1 − ε).
- If U ≥ εn, then a_n ≥ (1 − O(n^{−1/2}))·(1 − ε)^{−1/2}·√(2/π)·2^n/√n.

So the constant √(2/π) can fail to improve only along DSS sets with **1 − ε < U < εn**.

**Proof.**
- **(i)** Put d_i := a_n − a_i ≥ 0, so Σ d_i = a_n U. Let L be the layer {ε : Σ ε_i = 0} if n is even, or {ε : Σ ε_i = 1} if n is odd. Then |L| = β(n). On L, X(ε) = a_n·(Σ ε_i) − Σ ε_i d_i lies in a fixed interval of length 2a_n U. These β(n) values are distinct points of s + 2Z, so 2(β(n) − 1) ≤ 2a_n U.
- **(ii)** Write u_i := d_i/a_n ∈ [0, 1). Then ρn = Σ (1 − u_i)² ≤ Σ (1 − u_i) = n − U. Since cos(πs/2) ∈ [0, 1], cos^{ρn} ≥ cos^{n−U}. Now apply Lemma F. ∎

**Where the known families sit.** U values were computed for these families:
- Conway–Guy sets: U = 1.125, 1.100, 1.046, 1.023, 1.017, 1.006, 1.002 for n = 6, 10, 14, 18, 22, 30, 40. They are DSS-verified here for n ≤ 22.
- {2^n − 2^i : 0 ≤ i < n}: U = 1 − n/(2^n − 1).

Both families sit at U ≈ 1, inside the hard window. This is the natural threshold for range-type arguments (see O10).

### 2.4 Theorem 2 (k-fold bounds, conditional)
Let S ⊆ {1, …, n−1} with R := {1, …, n−1} ∖ S ≠ ∅. Put c := max_{j∈R} a_j and k := |S| + 1. Then

a_n ≥ 2β(n−k) · #{ε_S ∈ {±1}^S : |Σ_{j∈S} ε_j a_j| ≤ 2(a_n − c)} − 1.

**Proof.**
1. Write X = ε_n a_n + W + Z, where W := Σ_{j∈S} ε_j a_j and Z := Σ_{j∈R} ε_j a_j. Z is injective, odd and never 0.
2. For fixed ε_S, #{(ε_n, ε_R) : X ∈ (−a_n, a_n)} = #{Z ∈ (−2a_n − W, 2a_n − W)} − [−W is a value of Z].
3. If |W| ≤ 2(a_n − c), this window contains (−2c, 0) ∪ (0, 2c). By (F5) and (H) on Q_{n−k}, that set contains at least 2β(n−k) values of Z.
4. Any pair (ε_S, ε_R) with W + Z = 0 gives X(ε_S, ε_R, +1) = a_n. By injectivity there is at most one such pair overall, so the total subtraction is at most 1.
5. Finally #{X ∈ (−a_n, a_n)} ≤ a_n. ∎

**Special cases.**
- S = ∅ is Theorem 1.
- S = {1, …, k−1}: if a_1 + ⋯ + a_{k−1} ≤ 2(a_n − a_{n−1}), then a_n ≥ 2^k β(n−k) − 1 = √(2/π)·2^n·(n−k)^{−1/2}·(1 + O(1/(n−k))).
- n even, S = {1} (condition a_1 ≤ 2(a_n − a_{n−1})) or S = {n−1} (condition a_{n−1} ≤ 2(a_n − a_{n−2})): a_n ≥ 4β(n−2) − 1 = (n/(n−1))·β(n) − 1. This is a conditional second-order gain for even n.

**Honest assessment.** Every hypothesis here needs a large top gap a_n − a_{n−1}. Every optimal set for n ≤ 8 has a_n − a_{n−1} ≤ 3. Every Conway–Guy set has a_n − a_{n−j} = u_j, so its top is extremely clustered. The hypotheses therefore fail exactly on the sets that matter. At first order the k-fold case is subsumed by Lemma F, because its hypothesis forces ρn ≤ n − k + 5.

---

## 3. Numerical sanity checks
Software: Python 3 with numpy and mpmath, at most 2 threads. Total CPU was about 3 minutes.

**Table A.** Bounds, in units of 2^n/√n.

| n | min/CG a_n | (a) var | (b) E\|X\| | β(n) | Thm 1: 2β(n−1) | Fourier ideal* | Lemma F (ρ=1) |
|---|---|---|---|---|---|---|---|
| 5 | 0.9084 | 0.5771 | 0.5963 | 0.6988 | 0.8385 | 0.7592 | 0.6001 |
| 7 | 0.9095 | 0.5773 | 0.6047 | 0.7234 | 0.8268 | 0.7700 | 0.6305 |
| 9 | 0.9434 | 0.5773 | 0.6095 | 0.7383 | 0.8203 | 0.7761 | 0.6505 |
| 20 | 1.1405 | 0.5774 | 0.6345 | 0.7880 | 0.7880 | 0.7880 | 0.7003 |
| 21 | 1.1589 | 0.5774 | 0.6192 | 0.7707 | 0.8074 | 0.7884 | 0.7028 |
| 60 | 1.8302 | 0.5774 | 0.6293 | 0.7946 | 0.7946 | 0.7946 | 0.7428 |
| 61 | 1.8449 | 0.5774 | 0.6241 | 0.7882 | 0.8012 | 0.7946 | 0.7433 |
| 79 | 2.0934 | 0.5774 | 0.6247 | 0.7904 | 0.8004 | 0.7954 | 0.7501 |

- The first column is the true minimum for n ≤ 9 and the Conway–Guy value otherwise.
- *"Fourier ideal" is 2^{n−1} ∫_{−1}^{1} cos^n(πs/2) ds, the supremum over Lemma-F kernels (see O1). For even n it equals β(n) exactly; this was verified numerically for n = 2, 4, 10, 30. For odd n it is below Theorem 1's bound; for example at n = 31 it is 305272238.97, between β(31) = 300540195 and 2β(30) = 310235040.

**Table B.** Second-order coefficient n·(bound/(√(2/π)·2^n/√n) − 1).

| n | β(n) | 2β(n−1) |
|---|---|---|
| 20000 | −0.249998 | −0.249998 |
| 20001 | −0.749961 | **+0.250002** |

**Table C.** Exhaustive enumeration with DFS and big-integer bitsets.

| n | max ≤ | #DSS sets | min a_n | 2β(n−1) | an optimal set |
|---|---|---|---|---|---|
| 3 | 6 | 14 | 4 | 4 | {1,2,4}, {2,3,4} |
| 4 | 9 | 21 | 7 | 6 | {3,5,6,7} |
| 5 | 15 | 31 | 13 | 12 | {3,6,11,12,13} |
| 6 | 26 | 53 | 24 | 20 | {11,17,20,22,23,24} |
| 7 | 46 | 9 | 44 | 40 | {20,31,37,40,42,43,44} |
| 8 | 85 | 7 | 84 | 70 | {20,40,71,77,80,82,83,84} |

**Table D.** Conway–Guy sets, with DSS verified exactly by numpy bitset for n ≤ 22. The construction is u_0 = 0, u_1 = 1, u_{k+1} = 2u_k − u_{k−r}, r = round(√(2k)), and A = {u_n − u_i : 0 ≤ i < n}.
- "occ" is the fraction of lattice points in (−a_n, a_n) that are occupied.
- ∂B′/β(n−1) and ∂B/β(n) measure the Harper steps.
- The identity occ-count = 2·#{Y ∈ (−2a_n, 0)} and all inequalities of the Theorem 1 chain were asserted for every set.

| n | a_n | a_n/2β(n−1) | ρ | occ | ∂B′/β(n−1) | ∂B/β(n) |
|---|---|---|---|---|---|---|
| 10 | 309 | 1.226 | 0.817 | 0.841 | 1.032 | 1.016 |
| 14 | 4484 | 1.307 | 0.876 | 0.775 | 1.012 | 1.007 |
| 18 | 68008 | 1.399 | 0.905 | 0.719 | 1.006 | 1.004 |
| 22 | 1051905 | 1.491 | 0.923 | 0.674 | 1.005 | 1.002 |

**Table E.** Decomposition of the slack a_n − 2β(n−1), as fractions of a_n, using the identity in O2.

| set | holes | 2·(non-boundary Y) | 2·(Harper slack) |
|---|---|---|---|
| opt n=8 (b) | 0.095 | 0.071 | 0.000 |
| Conway–Guy n=22 | 0.326 | 0.000 | 0.003 |
| {2^12 − 2^i} | 0.774 | 0.000 | 0.000 |
| powers of two, n=12 | 0.000 | 0.000 | 0.549 |

**Further assertion checks.** All passed.
- Theorem 2 was asserted for 2733 DSS sets: all sets from the exhaustive enumeration with n ≤ 7, plus random perturbed powers of two with n ≤ 13. For each set, all S ⊆ [n−1] were tested, or 300 sampled.
- The 2-fold counting identity was asserted for 2747 sets.
- Theorem 3 (i) and (ii) were asserted for 2733 sets and for the Conway–Guy sets with n ≤ 40.

---

## 4. Routes tried, with exact obstructions

**O1. Band-limited Fourier barrier (proved).** Let 𝒦_a be the class of K ≥ 0 with K̂ ≥ 0 and supp K̂ ⊆ [−1/(4a), 1/(4a)].
- *Statement.* For n even and every K ∈ 𝒦_a, Σ_j C(n, j)·K(a(2j − n)) ≤ (β(n)/(2a))·K̂(0).
- *Proof.* The left side equals 2^n ∫ K̂ cos^n(2πξa) dξ. Use 0 ≤ K̂ ≤ K̂(0) and Wallis.
- *Consequence.* The non-DSS all-equal vector (a, …, a) with a = β(n) satisfies every inequality Σ_ε K(X(ε)) ≤ Σ_{s+2Z} K used by Lemma-F arguments. For it, the product lower bound in step 3 of Lemma F is an equality. So no kernel can give more than β(n) for even n, or more than 2^{n−1} ∫ cos^n(πs/2) ds < 2β(n−1) for odd n.
- *What would be needed.* Passing this barrier needs test functions of bandwidth > 1/(4a_n), i.e. windows shorter than about 2a_n. There Π cos(2πξ a_i) changes sign, and size information alone gives no lower bound.

**O2. Every step of the Harper chain is exactly tight on a genuine DSS family.** Let λ := #((s + 2Z) ∩ (−a_n, a_n)). Then

a_n − 2β(n−1) = (a_n − λ) + (λ − #{X ∈ (−a_n, a_n)}) + 2(#{Y ∈ (−2a_n, 0)} − |∂B′|) + 2(|∂B′| − β(n−1)).

The four terms are parity loss, holes, non-boundary points and isoperimetric slack. All are ≥ 0.
- **Powers of two:** zero holes. The window is completely filled, and all slack is isoperimetric.
- **{2^n − 2^i}:**
  - It is DSS: a subset sum determines |T| = ⌈sum/2^n⌉, and then Σ_{i∈T} 2^i.
  - X = 2^n·S − Σ ε_i 2^i with |Σ ε_i 2^i| < 2^n, where S := Σ ε_i. So sign(X) = sign(S) for S ≠ 0, and for S = 0 the sign is fixed by the single coordinate i = n−1.
  - Hence {X < 0} is exactly the Harper-extremal set (a ball, plus a star when n is even), and |∂B| = β(n), |∂B′| = β(n−1) exactly. All slack is holes.
- **Conway–Guy, n = 22:** isoperimetric slack 0.3% of a_n, holes 32.6%.

So neither step can be improved separately for all DSS sets. Improving the constant is equivalent to a trade-off "holes + isoperimetric slack ≥ c·a_n", which restates the goal. This is the exact obstruction for the isoperimetric route.

**O3. Local-CLT / variance route.**
- The heuristic: a central window of length L holds about 2^n L/(√(2π)σ) points and at most L/2, so σ ≥ √(2/π)·2^n. Combined with σ² ≤ n a_n², this gives the constant.
- Equality would need ρ → 1 (otherwise Lemma F / Theorem 3(ii) win) and central occupancy → 1.
- **Missing input, packing lemma PL_c.** There are c, K, L_0 > 0 such that: for DSS A with σ ≥ K·a_n, and every interval I of length ≥ L_0·a_n within distance σ of the centre, #{X ∈ I} ≤ (1 − c)|I|/2.
- PL_c implies the constant √(2/π)/(1 − c).
- PL_c is false without the CLT hypothesis σ ≥ K a_n. Powers of two fill every window, and the scaling A = 2^k·B ∪ {1, 2, …, 2^{k−1}} transports any occupancy pattern of B. So PL_c must use the many-near-equal-elements structure in an essential way.
- Erdős' conjecture implies PL_c in this regime. I found no route to PL_c.

**O4. Multi-fold (Theorem 2 family).**
- The k-fold yields 2^k β(n−k) only if the 2^{k−1} shifted Z-windows all cover the central Harper windows. For k = 2 that means a_1 ≤ 2(a_n − a_{n−1}), or a_{n−1} ≤ 2(a_n − a_{n−2}).
- For top-clustered sets (all known near-optimal sets), only half-windows are available. Folding Z once more gives #{|Z| < a_{n−2}} ≥ 2β(n−3), and the total is 2β(n−3) + 2β(n−2) = 3β(n−2) < 4β(n−2)(n−1)/n = β(n), a loss.
- Thresholds shifted off the median lose about β/n by Harper and normalized matching, which cancels the 1/n gain exactly.
- No unconditional second-order gain for even n was obtained.

**O5. Influences / KKL / Talagrand.**
- For f = sign X we have Inf_i = #{Y_i ∈ (−a_i, a_i)}/2^{n−1} ≤ a_i/2^{n−1}.
- Talagrand's inequality then gives only a_n ≳ 2^n·log n/n, which is weaker.
- The level-1 Fourier weight route reduces to the local CLT (O3).

**O6. Parseval and aliasing peaks.**
- The exact identity ∫ Π cos² = 2^{−n} controls only the L² shadow; it gives 1/√π.
- Adding the aliasing peaks of Π cos² near t = k/ā gives the layer-spread condition n²·Var_emp(a) ≳ 4^n/π².
- That improves σ² ≤ n a_n² only by O(4^n/n), a relative O(1/n), which the O(n^{−1/2}) error of the local-limit step swamps.

**O7. 2-adic / cyclotomic.**
- Φ_{2^e} divides 1 + x^b iff e = v_2(b) + 1. So Π(1 + x^{a_i}) has roots of multiplicity r_v = #{i : v_2(a_i) = v} at the primitive 2^{v+1}-th roots of unity.
- a_n < 2^{n−1} forces at least n − ⌊log_2 a_n⌋ − 1 ≈ ½·log_2 n repeated valuations. That forbids exact tilings (Coven–Meyerowitz T1).
- It only yields twisted-moment identities Σ_x g(x) x^j ζ^x = 0 for j < r_v, which any smooth profile satisfies up to O(1). This gives no constraint at scale ≥ 1, so it is a dead end.

**O8. "Structure of the largest elements".**
- Nothing is forced. The optimal sets for n = 4, …, 8 have a_n − a_{n−1} ∈ {1, 3}. Conway–Guy sets have a_n − a_{n−j} = u_j.
- So no gain of the form "a_n > a_{n−1} + …" is available.

**O9. Exponent (target b).**
- Every argument above uses DSS only through two facts: counts in windows of length ≳ a_n are at most length/2, and a_i ≤ a_n.
- A Gaussian density profile with peak exactly ½ is consistent with all of them; O1 makes this exact for band-limited tests.
- In the CLT regime, θ < 1/2 is equivalent to central occupancy → 0, a strong form of PL_c. No partial result was obtained.

**O10. Layer-range arguments stop at U = 1.**
- Theorem 3(i) and its multi-layer variant put the layers −2j, …, 2j, about (2j+1)·β(n) values, in a range of 4j·a_n + 2a_n·U. This gives a_n ≳ β(n)·(2j+1)/(2j+U), which is below β(n) exactly when U > 1.
- Heuristically, smearing each layer uniformly over its range makes the window count exactly β(n) for every U ≥ 1.
- U ≈ 1 is where both the Conway–Guy and the {2^n − 2^i} families sit.

---

## 5. Precise open sub-problems left by this probe
- **(P1)** Prove PL_c (O3) for some c > 0. This would improve the constant.
- **(P2)** The hard window: prove a_n ≥ (1 + c)·√(2/π)·2^n/√n for DSS sets with 1 − ε < U < εn (Theorem 3 handles all other U).
- **(P3)** Second order for even n: prove a_n ≥ β(n) + c·2^n·n^{−3/2}. Theorem 2 gives this when a_1 ≤ 2(a_n − a_{n−1}) or a_{n−1} ≤ 2(a_n − a_{n−2}). The open case is top-clustered sets.
- **(P4)** G2 priority check for Theorem 1 and Theorem 3. Both are short, and either may be known.

## 6. Cost
- One clean-room agent. Wall-clock about 1.5 h, mostly derivation.
- Compute about 3 CPU-minutes in total; the largest item was the exhaustive n = 8 enumeration at 71 s. At most 2 threads; no SAT or ILP; no web; no paid resources.
- Verification level: the proofs above are checked by me (same-vendor self-check only), together with the numerical assertions in §3. There is no cross-vendor review and no Lean formalization.

---

## Appendix: core code (reproducibility)
```python
import numpy as np
from math import comb
beta = lambda m: comb(m, m // 2)
def conway_guy_set(n):
    u = [0, 1]
    for k in range(1, n):
        r = int(round((2 * k) ** 0.5)); u.append(2 * u[k] - u[k - r])
    return sorted(u[n] - u[i] for i in range(n))
def all_pm_sums(a):                      # X(eps); bit i of index = 1  <=>  eps_i = +1
    X = np.zeros(1, dtype=np.int64)
    for ai in a: X = np.concatenate([X - ai, X + ai])
    return X
def is_dss(a):                           # exact, numpy bitset of 0/1 subset sums
    S = np.zeros(sum(a) + 1, dtype=bool); S[0] = True; hi = 0
    for ai in a:
        if np.any(S[:hi + 1] & S[ai:ai + hi + 1]): return False
        S[ai:ai + hi + 1] |= S[:hi + 1]; hi += ai
    return True
def inner_boundary(X, a):                # |∂{X<0}|, a sorted; best exit = highest index with eps=-1
    n, N = len(a), X.size; idx = np.arange(N); m = np.zeros(N, np.int64); f = np.zeros(N, bool)
    for j in range(n - 1, -1, -1):
        b0 = ((idx >> j) & 1) == 0; m[b0 & ~f] = a[j]; f |= b0
    return int(np.count_nonzero((X < 0) & f & (X + 2 * m > 0)))
def theorem1_chain(a):                   # asserts a_n >= #X(-a_n,a_n) = 2#Y(-2a_n,0) >= 2|∂B'| >= 2beta(n-1)
    a = sorted(a); n, an = len(a), a[-1]; assert is_dss(a)
    X, Y = all_pm_sums(a), all_pm_sums(a[:-1])
    occ = np.count_nonzero((X > -an) & (X < an)); yc = np.count_nonzero((Y > -2 * an) & (Y < 0))
    assert an >= occ == 2 * yc and yc >= inner_boundary(Y, a[:-1]) >= beta(n - 1)
```
