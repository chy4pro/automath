STATUS: PARTIAL — target (c) reached in asymptotic form, with a computer-assisted proof checked in interval arithmetic: liminf_{N→∞} s(N)/N^{1/3} ≥ (2/0.83)^{1/3} = 1.3406… > 2^{1/3} = 1.2599… (counting bound). With an explicit threshold: s(N) > 1.3300·N^{1/3} for every N ≥ 3·10^11 (Corollary 6). Targets (a) and (b), the upper bound, remain OPEN. Novelty/priority not checked (clean room).

# Erdős #156: minimal maximal Sidon sets (clean-room probe, 2026-10-03)

Rules followed: no web, no papers, no repository files read. I used only standard mathematics and local computation (Python with numpy, scipy and mpmath; at most 2 threads; no SAT or ILP). I did **not** check priority or novelty (G2 not done). Fourier-analytic improvements of counting bounds are classical for related basis problems (Rohrbach-type bases, difference bases). The method below is in that spirit and may well be known for this problem. Labels used: **[proved]** means a full proof is given here. **[computer-assisted]** means a proof that depends on a stated, reproducible certificate checked in interval arithmetic. **[numerical]** means computed, no proof. **[heuristic]** means no proof.

## 0. Summary

1. **[proved]** Let A ⊂ [1,N] be maximal Sidon with |A| = k. Outside an exceptional set E with |E| ≤ 1.5k² + k, every x ∈ [1,N] has at least **two** ordered representations x = b + c − a with a, b, c ∈ A. This alone gives the counting bound k³ ≥ 2N − O(k²).
2. **[proved]** Reduction to a continuous extremal problem: liminf s(N)³/N ≥ 2/λ*, where λ* is the largest λ for which some probability measure μ on [0,1] satisfies Law(X+Y−Z) ≥ λ·Leb on [0,1], with X, Y, Z iid ~ μ. Trivially λ* ≤ 1, and λ* = 1 would recover 2^{1/3}.
3. **[computer-assisted]** λ* ≤ 0.83. The proof uses Bochner positivity at the frequencies 0, h, …, 4h with h = 0.6, applied to μ, to the localized measure g·μ and to the excess ρ = ν − λ·Leb. A branch-and-bound over (χ(h), …, χ(4h)) ∈ ℂ⁴ has all 1,084,724 leaves re-verified in mpmath interval arithmetic. Consequence: **liminf s(N)/N^{1/3} ≥ (2/0.83)^{1/3} ≈ 1.3406.** Smaller certificates give λ* ≤ 0.843 (n = 3, constant 1.3337) and λ* ≤ 0.853 (n = 2, 8,988 leaves, constant 1.3285).
4. **[numerical]** λ* ≈ 0.71792. The numerically optimal μ is *two-scale*: an atom of mass ≈ 0.473 at 1/2 plus a symmetric density that is largest at the endpoints. If the coarse relaxation were the only obstruction, this would give the constant (2/λ*)^{1/3} ≈ 1.4071. That is the ceiling of this method. Sets whose coarse profile is uniform, as in random constructions, have λ = 1/2, so even with zero fine-scale waste they need k ≥ 4^{1/3}N^{1/3} ≈ 1.587 N^{1/3}.
5. **[numerical]** Exact s(N) for 1 ≤ N ≤ 67 by exhaustive search, independently brute-force cross-checked for N ≤ 30 (§5).
6. **OPEN: (a) and (b).** Obstructions recorded in §6:
   - A proper subset of a Sidon set S is never maximal in an ambient set containing S. So "extract a sub-configuration of a Singer set" constructions must push the unused Singer elements out of the interval.
   - The lifting lemma proved here (ℤ_m → interval) needs the modular set inside an arc of length ≤ (m−1)/3. For Singer sets under the best multiplier, the smallest arc is 0.43m to 0.84m, so the hypothesis fails.
   - Random-greedy and score-greedy maximal Sidon processes show k³/N growing like log N, while k³/(N ln N) stays roughly constant.
   - The naive two-scale design, which the coarse optimum suggests, is blocked by a Sidon difference-cover lemma: diam(C) ≥ (2.062 − o(1))·L whenever C − C ⊇ [1, L].
7. **Honest caveat.** The lower bound uses the Sidon property only through the factor 2 (the two orders of (b, c) when b ≠ c). It therefore holds for every A ⊂ [1,N] with A + A − A ⊇ [1,N] minus o(N) points. I found no Sidon-specific coarse-scale gain and explain why in §4.3. "Forced coincidences" for Sidon sets were not exploited.

## 1. The covering lemma

For A ⊂ ℤ write f(x) = #{(b,c,a) ∈ A³ : b + c − a = x} (ordered triples).

**Lemma 1 [proved].** Let A ⊂ [1,N] be a maximal Sidon set with k = |A|. Define E = A ∪ {2b − a : a, b ∈ A} ∪ {x : 2x = b + c, b ≠ c ∈ A}. Then |E| ≤ k + k² + k(k−1)/2, and f(x) ≥ 2 for every x ∈ [1,N] \ E.

*Proof.* Take x ∈ [1,N] \ E. Then x ∉ A, and by maximality A ∪ {x} is not Sidon. So there are p ≤ q and r ≤ s in A ∪ {x} with p + q = r + s and {p,q} ≠ {r,s} as multisets. Since A is Sidon, x occurs among p, q, r, s.
- x on both sides, say p = r = x: then q = s, so the multisets coincide. Contradiction.
- x twice on one side, x + x = r + s with x ∉ {r, s}: then r, s ∈ A, and r = s would give x = r ∈ A. So 2x = r + s with r ≠ s, i.e. x ∈ E. Excluded.
- x twice on one side and once on the other: then x ∈ A. Excluded.
- So x occurs exactly once: x + a = b + c with a, b, c ∈ A. If b = c then x = 2b − a ∈ E, excluded. So b ≠ c, and the distinct ordered triples (b,c,a) and (c,b,a) both give b + c − a = x. ∎

**Corollary (counting bound).** k³ = Σ_x f(x) ≥ 2(N − |E|), so k³ ≥ 2N − 3k² − 2k and s(N) ≥ (2N)^{1/3}(1 − o(1)).

## 2. Reduction to a continuous extremal problem

For a Borel probability measure μ on [0,1], let ν_μ = Law(X + Y − Z) with X, Y, Z iid ~ μ. Equivalently ν_μ = μ∗μ∗μ̃, where μ̃ is the reflection of μ; it is supported on [−1, 2]. Say μ is *λ-covering* if ν_μ(B) ≥ λ·|B| for every Borel B ⊂ [0,1], i.e. ν_μ ≥ λ·Leb|_{[0,1]}. Let λ* = sup{λ : some μ is λ-covering}. Since ν_μ([0,1]) ≤ 1, λ* ≤ 1. A λ-covering μ is λ'-covering for every λ' ≤ λ.

**Theorem 2 [proved].** Let λ0 ∈ (0,1] be such that no probability measure on [0,1] is λ0-covering. Then for every ε > 0 there is N0(ε) with s(N) ≥ (2/λ0 − ε)^{1/3}·N^{1/3} for all N ≥ N0(ε). In particular liminf s(N)³/N ≥ 2/λ* (applying this with every λ0 > λ*).

*Proof.* Suppose not. Then there are ε > 0 and infinitely many N with k = s(N) satisfying k³ ≤ (2/λ0 − ε)N, so λ_N := 2N/k³ ≥ λ' := (2/λ0 − ε)^{−1}·2 > λ0. Also k → ∞, since k ≥ (2N)^{1/3}(1 − o(1)).

Fix a maximal Sidon A_N ⊂ [1,N] of size k, and put μ_N = k^{−1}Σ_{a∈A_N} δ_{a/N}, a probability measure on [0,1]. Then ν_{μ_N} = k^{−3} Σ_{(b,c,a)} δ_{(b+c−a)/N}. By Lemma 1, for 0 ≤ u < v ≤ 1:

  ν_{μ_N}([u,v]) ≥ (2/k³)·(#(ℤ ∩ [uN, vN]) − |E|) ≥ λ_N(v − u) − 2(1 + |E|)/k³ ≥ λ'(v − u) − O(1/k).

By Prokhorov, pass to a subsequence with μ_N → μ weakly. Then μ_N^{⊗3} → μ^{⊗3} weakly, and by the continuous mapping theorem ν_{μ_N} → ν_μ weakly. Portmanteau for closed sets gives ν_μ([u,v]) ≥ limsup ν_{μ_N}([u,v]) ≥ λ'(v−u) for every closed interval in [0,1]. Hence ν_μ(U) ≥ λ'|U| for relatively open U ⊂ [0,1] (countable disjoint unions of intervals, using inner approximation by closed intervals). By outer regularity of Lebesgue measure and monotonicity of ν_μ this extends to all Borel B ⊂ [0,1]. So μ is λ'-covering with λ' > λ0, and therefore λ0-covering. Contradiction. ∎

## 3. Upper bounds for λ*: Fourier/Toeplitz relaxation and certificate

### 3.1 Necessary conditions

Notation: χ(t) = ∫e^{−2πitx}dμ(x) and ℓ(t) = ∫_0^1 e^{−2πitx}dx = (1 − e^{−2πit})/(2πit).

Key identity: ν̂_μ(t) = E e^{−2πit(X+Y−Z)} = χ(t)²·conj(χ(t)) = χ(t)|χ(t)|².

**Lemma 3 [proved].** Let μ be λ-covering, h ∈ (0,1] and n ≥ 1. Put c_j = χ(jh), so c_0 = 1 and c_{−j} = conj(c_j), and ℓ_j = ℓ(jh). Define ρ_0 = 1 − λ, ρ_j = c_j|c_j|² − λℓ_j and ρ_{−j} = conj(ρ_j) (j ≥ 1), and g_j = ½e^{−iπh}c_{j−1} + ½e^{iπh}c_{j+1} − cos(πh)·c_j. Then the Hermitian Toeplitz matrices

  T1 = (c_{a−b})_{0≤a,b≤n},  T2 = (ρ_{a−b})_{0≤a,b≤n},  T3 = (g_{a−b})_{0≤a,b≤n−1}

are all positive semidefinite.

*Proof.* For any finite positive Borel measure m on ℝ and any v ∈ ℂ^{n+1}:

  Σ_{a,b} conj(v_a)·v_b·m̂((a−b)h) = ∫ |Σ_b v_b e^{2πibhx}|² dm(x) ≥ 0.

Apply this to three measures:
- m = μ gives T1.
- m = ρ := ν_μ − λ·Leb|_{[0,1]} ≥ 0 gives T2. Here ρ̂(t) = χ(t)|χ(t)|² − λℓ(t) and ρ̂(0) = 1 − λ.
- m = g·μ with g(x) = cos(2πh(x − ½)) − cos(πh) gives T3. On [0,1] we have |2πh(x − ½)| ≤ πh ≤ π, so g ≥ 0 there, and (gμ)^(t) = ½e^{−iπh}χ(t−h) + ½e^{iπh}χ(t+h) − cos(πh)χ(t). ∎

**Monotonicity.** As a function of λ, T2(λ) = T2(λ') − (λ − λ')·(ℓ_{a−b}). The matrix (ℓ_{a−b}) is PSD (apply the lemma to Lebesgue measure on [0,1]). So if (T1, T2, T3) is feasible at λ, it is feasible at every λ' ≤ λ.

### 3.2 Certificate

**Proposition 4 [computer-assisted].** In each case h means its IEEE binary64 value, an exact dyadic rational; the lemma holds for any h ∈ (0,1].
- (n = 4, h = 0.6, λ = 0.83) no (c_1, …, c_4) ∈ ℂ⁴ makes T1, T2 and T3 all PSD.

For h = 0.65:
- (n = 3, λ = 0.843) no (c_1, c_2, c_3) ∈ ℂ³ makes T1, T2 and T3 all PSD;
- (n = 3, λ = 0.845) the same. This is implied by the 0.843 case by monotonicity; it was run and checked separately;
- (n = 2, λ = 0.853) no (c_1, c_2) ∈ ℂ² makes them all PSD.

*Certificate procedure.* T1 ⪰ 0 forces |c_j| ≤ 1, so the root box is [−1,1]^{2n} in the coordinates (Re c_j, Im c_j). The box is bisected along its widest coordinate. A box Q becomes a leaf when either:
- (disk) min_{Q} |c_j|² > 1 for some j; or
- (vec) for some T ∈ {T1, T2, T3} and a vector v (in practice the least eigenvector of T at the centre of Q), a rigorous upper bound of v*T(c)v over Q is < 0.

How the bounds are computed:
- v*T1v and v*T3v are real-affine in (Re c_j, Im c_j), so their maximum over a box is exact.
- v*T2v is real-affine in (Re ρ_j, Im ρ_j). The cubic terms ρ_j + λℓ_j = (x + iy)(x² + y²) are bounded by interval arithmetic.

Verification:
- The float search only proposes leaves. Every leaf is re-checked in **mpmath interval arithmetic** at 90-bit precision with outward rounding. ℓ_j, cos(πh) and sin(πh) are enclosed rigorously; λ is the decimal interval enclosing 0.83, 0.843, 0.845, 0.85 or 0.853; v is converted exactly from its floats.
- The disk leaves are checked in exact rational arithmetic.
- The leaf volumes are summed exactly with Python Fractions and equal the root volume 4^n. Leaves arise only from exact midpoint bisection, so they tile the root box.

Runs:

| n | h | λ | boxes | leaves | failed leaf checks | covered volume |
|---|---|---|---|---|---|---|
| 2 | 0.65 | 0.853 | 17,975 | 8,988 | 0 | 16 = 4² |
| 3 | 0.65 | 0.845 | 572,029 | 286,015 | 0 | 64 = 4³ |
| 3 | 0.65 | 0.843 | 972,729 | 486,365 | 0 | 64 = 4³ |
| 4 | 0.6 | 0.83 | 2,169,447 | 1,084,724 | 0 | 256 = 4⁴ |

*Checker sanity test.* Inflating every leaf box by a factor of 7 in each direction made 8,985 of 8,988 leaf checks fail (n = 2). The checker is not vacuous.

*Relaxation values (float search, not certificates).*
- n = 2: smallest λ certified (float) ≈ 0.852 at h = 0.65. I scanned h ∈ {0.55, 0.6, 0.62, 0.65, 0.68, 0.7, 0.75}; the certified values were 0.915, 0.868, 0.858, 0.852, 0.856, 0.863, 0.888. A float-feasible point exists at λ = 0.8507.
- n = 3, h = 0.65: a feasible point was found at λ ≈ 0.8417, so this relaxation cannot certify much below 0.842.
- n = 4: certified at 0.83 (h = 0.6). Local search found float-feasible points near 0.805 (h = 0.6), so n = 4 cannot go much below about 0.81.
- n = 6 (h = 1/3): local search ≈ 0.81. This would need a 12-dimensional branch-and-bound, not attempted.

### 3.3 Main theorem

**Theorem 5 [computer-assisted].** liminf_{N→∞} s(N)/N^{1/3} ≥ (2/0.83)^{1/3} = 1.34065…

Equivalently: for every ε > 0, s(N) ≥ (1.3406 − ε)N^{1/3} for all large N. The counting bound gives 2^{1/3} = 1.25992.

*Proof.* By Lemma 3 and monotonicity, a λ-covering μ with λ ≥ 0.83 would make (T1, T2, T3) feasible at λ = 0.83 for n = 4, h = 0.6. Proposition 4 rules that out. Apply Theorem 2 with λ0 = 0.83. ∎

### 3.4 Effective version

The weak-limit argument gives no explicit N0, but the same certificate can be run on the finite set directly.

Setup:
- Let A ⊂ [1,N] be maximal Sidon with k = |A|, and assume λ_N := 2N/k³ ≥ λ0.
- Put μ = k^{−1}Σ δ_{a/N}. Then T1 and T3 are PSD exactly (μ lives on (0,1]).
- By Lemma 1, ν_μ ≥ κ := (2/k³)Σ_{x∈[1,N]\E} δ_{x/N}. So T2' := Toeplitz((ν̂_μ − κ̂)(jh)) is PSD.
- κ̂(t) = λ_N(ℓ_N(t) − e(t)), where ℓ_N(t) = N^{−1}Σ_{x=1}^{N} e^{−2πitx/N} and |e(t)| ≤ |E|/N.
- Hence T2' = T2(λ_N) + λ_N·Δ, with Δ the Toeplitz matrix of ℓ(jh) − ℓ_N(jh) + e(jh) (diagonal entry e(0)). The Riemann-sum error is |ℓ(t) − ℓ_N(t)| ≤ 2π|t|/N.

Argument:
- Suppose every T2-leaf of a certificate at λ0 has margin δ, i.e. v*T2(λ0)v ≤ −δ with |v| = 1.
- Then on that leaf v*T2'v ≤ −δ + λ_N·Σ_{|j|≤n}|Δ_j|.
- Here λ_N ≤ 1 + 3/k + 2/k² (from Lemma 1), |E| ≤ 1.5k² + k and k ≤ (2N/λ0)^{1/3}.
- For n = 3, h = 0.65, λ0 = 0.85 this gives Σ|Δ_j| ≤ 18.6N^{−1/3} + 9.3N^{−2/3} + 49/N.
- So a certificate with margin δ yields s(N)³ > (2/λ0)N for every N with 1.04·(18.6N^{−1/3} + 9.3N^{−2/3} + 49/N) < δ.

**CERT-EXPLICIT [computer-assisted].** Parameters: n = 3, h = 0.65, λ0 = 0.85, required T2-leaf margin δ = 0.003.
- 387,173 boxes, 193,587 leaves, 0 failures in interval re-verification.
- The minimum certified T2 margin is 0.003150 > 0.003.
- Covered volume 64 = 4³.

**Corollary 6 [computer-assisted, explicit].** s(N) > (2/0.85)^{1/3}·N^{1/3} = 1.3300·N^{1/3} for every N ≥ 3·10^{11}.

Check of the threshold: at N = 3·10^{11}, N^{1/3} ≈ 6694 and k ≥ 8000, so λ_N ≤ 1.0004. Then 1.04·(18.6/6694 + 9.3/6694² + 49/(3·10^{11})) ≈ 0.00289 < 0.003.

Leaf types:
- T1 and T3 leaves contradict the exact PSD property of the discrete μ.
- Disk leaves are impossible since |c_j| ≤ 1.
- T2 leaves give v*T2'v ≤ −0.003 + 0.00289 < 0, contradicting T2' ⪰ 0.

So λ_N < 0.85, i.e. k³ > 2N/0.85. Below 3·10^{11} the exact table (§5) and the counting bound are all I have.

## 4. What the true constant of this method is; the coarse extremal measure

### 4.1 Numerics for λ* [numerical]

Discretize μ on the grid {0, 1/M, …, 1} with weights p. Maximize min_{0≤j≤M} (M+1)·(p∗p∗p̃)(j), which is the fractional, discrete version of the covering problem. The method is softmax parametrization, L-BFGS on a log-sum-exp soft-min with increasing sharpness, and many random and structured starts (single, double and triple atoms, uniform, random).

| M | best λ_M | number of starts |
|---|---|---|
| 60 | 0.71790 | 10 |
| 90 | 0.717903 | 60 (structured) |
| 120 | 0.717901 | 40 |
| 200 | 0.717919 | refinement from M = 120 |
| 300 | 0.717918 | refinement from M = 120 |

Many random starts end at worse local optima (0.59–0.712), but every start family's best run reached the same optimum, of the same shape. This is a non-convex search, so it gives no proof of global optimality. Conjecture: **λ* = 0.7179(2)**, giving the method's ceiling (2/λ*)^{1/3} ≈ 1.4071.

### 4.2 Shape of the optimizer [numerical]

- μ ≈ w·δ_{1/2} + (1 − w)·h(x) with w ≈ 0.473 and h symmetric about 1/2.
- Density in units of total mass, at x = 0, 0.1, 0.2, 0.3, 0.4, 0.49: 0.680, 0.641, 0.580, 0.502, 0.411, 0.324. It is largest at the endpoints.
- On [0,1], ν_μ is flat (equal to λ*) except for the atom w³ ≈ 0.106 at 1/2.
- The mass outside [0,1] is ≈ 0.177.
- So the waste is 0.177 (outside) + 0.106 (atom) = 0.283 = 1 − λ*.

Comparison profiles:
- μ uniform on [0,1]: ν is an Irwin–Hall(3) shift with min density 1/2 on [0,1], so λ = 1/2 and the constant is 4^{1/3} ≈ 1.587. Random constructions have essentially this profile.
- μ uniform on [1/3, 2/3]: λ = 0, because the density vanishes at the endpoints.

### 4.3 Why the Sidon condition is invisible at this scale [heuristic + proved remark]

Sidon says that A − A \ {0} is a set (multiplicity 1). Under the scaling x ↦ x/N, the k² differences sit in [−N, N] with density ~k²/N ~ N^{−1/3} → 0. So Sidon puts no constraint on weak limits of μ_N∗μ̃_N except at atoms. An atom of μ is a cluster C of ~wk elements, and Sidon only forces diam C ≳ (wk)², which is o(N). Every coarse profile, including the two-scale optimizer, is consistent with Sidon. Any Sidon-specific improvement therefore has to come from the fine scale, from how the translates c + (C − C) and b + (A − A) pack. I did not obtain one.

The counting floor N ≤ k³/2 + O(k²) is the bound λ* ≤ 1. The improvement in §3 is purely "uncertainty-principle" in nature: the cube root of a near-uniform ν is not a characteristic function. For λ = 1 exactly, ν = Leb|_{[0,1]} forces χ(t) = e^{−iπt}·sgn(sinc t)·|sinc t|^{1/3}. This violates the 3-point Jensen inequality |χ(2t)| ≥ 2|χ(t)|² − 1 at t = 1/2, since 0 < 2(2/π)^{2/3} − 1 ≈ 0.48. That one inequality alone already gives λ* ≤ 0.954 by hand. Use |ν̂(1)| ≤ 1 − λ and |ν̂(½)| ≥ (2/π)λ − (1 − λ); then (1−λ)^{1/3} ≥ 2((1 + 2/π)λ − 1)^{2/3} − 1 fails for λ > 0.9535.

## 5. Exact values of s(N) [numerical, exhaustive]

The search is a DFS over Sidon sets in increasing order with bitset sums. For each N it tries k upward from the counting lower bound. The pruning rule is safe: a prefix S of size i is discarded if #unblocked(S) > B(k) − B(i), where B(k) = C(k,2)(k−2) + k(k−1) + C(k,2) + k bounds the number of blockable points. Monotonicity in N was *not* assumed. N ≤ 30 was independently brute-forced over all subsets and agrees.

| k | N with s(N) = k | max N with s(N) ≤ k | (max N)/k³ |
|---|---|---|---|
| 1 | N = 1 | 1 | — |
| 2 | 2 ≤ N ≤ 4 | 4 | 0.50 |
| 3 | 5 ≤ N ≤ 10 | 10 | 0.370 |
| 4 | 11 ≤ N ≤ 22 | 22 | 0.344 |
| 5 | 23 ≤ N ≤ 42 | 42 | 0.336 |
| 6 | 43 ≤ N ≤ 67 (search stopped at 67) | ≥ 67 | — |

Sample minimum maximal sets:
- N = 22: {4, 7, 12, 13}
- N = 42: {10, 18, 19, 25, 30}
- N = 43: {1, 2, 4, 13, 32, 37} (no 5-element maximal Sidon set exists, by exhaustive search)
- N = 66: {7, 24, 27, 36, 42, 46}
- N = 67: {13, 24, 30, 33, 45, 52}

For comparison, the asymptotic statements in ratio form max N/k³ are: counting bound 0.5, Theorem 5 0.415, conjectured method ceiling λ*/2 ≈ 0.359. The k = 4 and k = 5 values (0.344 and 0.336) are already below the conjectured asymptotic ratio 0.359. These sizes are far from asymptotic, so this is only a consistency check.

## 6. Upper bound side, targets (a) and (b): OPEN, with obstructions

### 6.1 Subset obstruction [proved, trivial]

If S is Sidon and A ⊊ S lies in an ambient set (an interval or ℤ_m) that contains S, then A is not maximal there: any s ∈ S \ A can be added. Consequently no proper subset of a Singer set is maximal in ℤ_m. Numerically, greedy covering of ℤ_m by A + A − A with A ⊂ S (Singer, q ≤ 43) always ended with A = S. Any "extract from a Singer set" construction must therefore move the unused Singer elements out of the target interval (e.g. by working in a different modulus than the one where S lives). The construction as described in the brief cannot literally be "a subset of S inside the same ambient".

### 6.2 Lifting lemma [proved]

Let A ⊂ ℤ_m be Sidon mod m with A + A − A = ℤ_m. Suppose its representatives lie in {u, …, u + L} with 3L + 1 ≤ m. Then the integer set A is a maximal Sidon subset of every interval I with A ⊂ I ⊂ [u − L, u + 2L].

*Proof.* Sidon mod m implies Sidon in ℤ. Take x ∈ I \ A. Choose a, b, c ∈ A with b + c − a ≡ x (mod m). Both the integer b + c − a and x lie in [u − L, u + 2L], which has 3L + 1 ≤ m points, so b + c − a = x. Then a ∉ {b, c} (otherwise x ∈ A), and x + a = b + c is a nontrivial coincidence in A ∪ {x}. ∎

So s(n) ≤ |A| for every n ∈ [diam A + 1, 3L + 1]. Lifted sets fall under §2–3 with μ supported on an interval of length 1/3 of the target, so they obey the same lower bound. The value of the restricted relaxation was not computed.

Numerics for the arc condition (best multiplier t ∈ ℤ_m^*; minimal arc containing tS, Singer S):

| q | m | minimal arc / m | needed |
|---|---|---|---|
| 2 | 7 | 0.43 | ≤ 1/3 |
| 7 | 57 | 0.61 | ≤ 1/3 |
| 43 | 1893 | 0.84 | ≤ 1/3 |

The arc condition fails and gets worse with q. The lifted Singer set S ⊂ [0, m) is, however, almost maximal in [0, m − 1]: 0 or 1 unblocked points for q ≤ 7. But |S| ≈ √m.

### 6.3 Random and greedy processes [numerical]

A maximal Sidon set is built by repeatedly adding an element y ∈ U, where U is the set of currently unblocked points (the only legal additions), until U = ∅. Every final set was checked to be Sidon and maximal.

| N | random-greedy k | k³/N | k³/(N ln N) | score-greedy k | k³/N | k³/(N ln N) |
|---|---|---|---|---|---|---|
| 10² | 10 | 10.0 | 2.17 | 9 | 7.3 | 1.58 |
| 10³ | 26 | 17.6 | 2.54 | 22 | 10.6 | 1.54 |
| 10⁴ | 59 | 20.5 | 2.23 | 55 | 16.6 | 1.81 |
| 3·10⁴ | — | — | — | 79 | 16.4 | 1.59 |
| 10⁵ | 142 | 28.6 | 2.49 | 129 | 21.5 | 1.87 |
| 3·10⁵ | 211 | 31.3 | 2.48 | — | — | — |
| 10⁶ | 327 | 35.0 | 2.53 | — | — | — |

Each row is a single run (seed 1); no variance estimate. Random-greedy fits k ≈ (2.5·N ln N)^{1/3} well over four decades.

Score-greedy picks y ∈ U maximizing the number of newly blocked points: an FFT pre-score, then an exact check of the top 30. Both processes show k³/N growing roughly like log N (the coupon-collector mechanism). Heuristic reason: once |U| = εN, a legal y blocks about (3/2)k²·ε points of U, so U decays like exp(−Σ (3/2)k_i²/N) = exp(−k³/(2N)). Reaching U = ∅ needs k³ ≳ 2N log(N/k²). The "repair" phase cannot help: repair elements must themselves come from U. **So any construction that is "random-like" at the end game pays the log. Removing the log needs U to be algebraically structured so that one added element blocks a large part of it.**

### 6.4 The two-scale picture and a Sidon difference-cover lemma

The coarse optimizer (§4.2) is a cluster C carrying ≈ 47% of the elements plus a spread set B. The cluster's contribution is the translates b + (C − C). The natural exact design takes:
- C Sidon with C − C ⊇ [−L, L];
- B with gaps in (L, 2L + 1] (perturbed to be Sidon);
- C placed beyond B.

The Sidon cross-conditions for B ∪ C reduce to:
- (B − B) ∩ (C − C) = {0};
- (B + B) ∩ (C + C) = ∅;
- C ∩ (B + B − B) = ∅;
- B ∩ (C + C − C) = ∅.

The simplest way to secure the last condition is to keep B out of the window [min C − D, max C + D] ⊇ C + C − C, where D = diam C. The points between max B and min C are then covered only by b + [−L, L] and c + [−L, L]. That needs D < 2L + O(1), which is impossible:

**Lemma 7 [proved].** If C ⊂ ℤ is Sidon with C − C ⊇ [1, L] and diam C = D, then L ≤ (0.4849 + o(1))·D, i.e. D ≥ (2.062 − o(1))L.

*Proof.* Let k = |C|. Positive differences are distinct, so k(k−1)/2 ≥ L + P, where P = #{pairs with difference > L}. Erdős–Turán gives k² ≤ D + O(D^{3/4}). Write L = βD. Take θ slightly below (1 − β)/2. Then every pair (c, c') with c ∈ [min C, min C + θD] and c' ∈ [max C − θD, max C] has difference ≥ (1 − 2θ)D > L. Each of these two end-pieces contains at least k − √((1−θ)D) − O(D^{1/4}) elements, since the rest of C is a Sidon set in an interval of length (1 − θ)D. With k ≥ √(2βD) this gives

  1/2 ≥ β + (√(2β) − √((1+β)/2))² − o(1).

Solving, β ≤ 0.4849 + o(1). ∎

So the naive design leaves an uncovered gap of length ≥ 0.06L. That gap could still be covered by other triple types such as c + (B − B), so this obstructs only the naive scheme, not two-scale constructions in general. The general requirement is that translates of a Sidon difference set (density ≤ 1/2 in its window) by a Sidon set of translates cover ℤ without collisions. That is a "tiling by Sidon difference sets" problem I could not solve.

Another observation: a Singer set's lifted C − C is a complete residue system mod m. B ⊂ e + mℤ then tiles exactly, but forces B ⊇ an interval of levels, i.e. B not Sidon. With B spread over residue classes, each x has O(1) candidate translates and fails with constant probability. Several clusters with "complementary" patterns would be needed; random choices need ~log N clusters. That is the log again.

## 7. Routes tried that failed or were not finished

- **Single-test-function duality** (λ* ≤ inf_Ψ sup_μ E Ψ(X+Y−Z)/∫_0^1Ψ). It is useless: μ = δ_t gives E Ψ(W) = Ψ(t) ≥ mean Ψ, so the bound is ≥ 1. Any proof must be non-linear in μ; Fourier/Bochner handles atoms.
- **Moment/cumulant route.** κ_{2j}(W) = 3κ_{2j}(X) and κ_{odd}(W) = κ_odd(X), so kurt(W) ≥ 7/3, while Uniform[0,1] has 9/5. This alone gives λ ≤ 0.771 only if the excess mass sits at the centre. Excess mass near −1 or 2 defeats it, so it is not a proof of anything below 1.
- **Box relaxation (only |ρ̂(t)| ≤ 1 − λ, no joint positivity of ρ).** Weak (≥ 0.95).
- **Larger Fourier relaxations.** n = 4 was certified at 0.83 (Theorem 5), and its true relaxation value is about 0.805–0.81. n = 6 would need a 12-dimensional branch-and-bound (not attempted). Converging to λ* ≈ 0.718 would need much larger n or a better relaxation (e.g. localizing ρ on [−1,2], which needs h ≤ 1/3).
- **Sidon-specific coincidence counting for target (c).** Cauchy–Schwarz on the sixth moment Σf² is already saturated by the trivial solutions (≈ 2k³ against k⁶/N ≈ 2k³). Fourier L^∞ bounds give nothing because random Sidon sets are Fourier-uniform. No gain.
- **Upper bound (a)/(b).** None of the routes in §6 gives a construction better than (N log N)^{1/3}; all are reported as obstructions, not results.

## 8. Cost and reproducibility

- Wall-clock ≈ 95 min. CPU ≈ 55–60 min in total (a self-tally, not measured precisely), with ≤ 2 of my processes at any time.
- Heaviest jobs:
  - n = 4 certificate: ≈ 10 min (3 min float search + 7 min interval re-verification);
  - exhaustive s(N) to N = 67: ≈ 10 min;
  - n = 3 certificates: ≈ 1.5–4 min each;
  - relaxation scans: ≈ 15 min in total.
- Scripts (scratch, not committed):
  - the discrete λ-optimizer;
  - the Fourier relaxation local search;
  - the branch-and-bound (float) and the mpmath interval verifier with its volume check;
  - exact s(N) search plus an independent brute-force check;
  - greedy and random processes (FFT);
  - Singer set constructions over F_{q³}.
- No external data. No solvers.

## 9. What would upgrade this

1. G2: check whether a Fourier-type improvement of the 2^{1/3} constant for s(N), or for "A + A − A ⊇ [1,N]" bases, is known. If it is, §3 is a re-derivation.
2. A stronger certificate (n ≥ 5, or localizing ρ with h ≤ 1/3) to push 0.83 toward 0.718. A provably optimal value of λ* looks hard.
3. The real problem (a) needs an explicit "Sidon tiling" (§6.4) or structured end-game blocking (§6.3). No candidate was found.
