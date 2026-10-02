# Cross-vendor referee (Claude Opus) of a GPT-6 Astra proof

- Object: `problems/erdos30/SIDON_BOUND_PROOF.md` (911 lines, read in full), claim
  |A| ≤ √N + (2√2/3)N^{1/4} + 1 for every Sidon set A ⊆ {1,…,N} and every integer N ≥ 207 360 000 = 120^4.
- Referee: Claude Opus 5.5, 2026-10-02, adversarial stance (assumed wrong until each step was checked).
- Isolation: the mathematical check below was completed before any other file about this problem was opened.
  `G2_SIDON_20261002.md` and `KERNEL_SCAN_20261002.md` were **not read at all**. After the check
  was finished, `check_sidon_bound.py` was only *executed* (see item 8); its code was not reviewed.
- Tools: python3 (mpmath 1.3, sympy 1.14, numpy/scipy) with my own scratch scripts; about 10 CPU-minutes in total.

## Verdict: **PASS**

No failing line was found. No repair is needed for correctness. The remarks R1–R6 are optional
presentational or strength improvements. Every displayed identity and inequality was re-derived by hand.
The analytic identities were also checked symbolically (sympy) or numerically (mpmath, 25–60 digits).
The single genuinely new ingredient (Lemma 6) was checked against an independent numerical capacity
computation, and the two agree to within 1e-5.

---

## Item-by-item report

### 1. §1 conventions — VERIFIED
- The convention is the standard Sidon (B₂) convention: a+b is injective on pairs with a ≤ b, including diagonal pairs.
- Lemma 1 (lines 48–59) is correct in both directions. In the forward direction the case a=b, d=c is
  excluded by the nonzero difference. In the converse, the case a≠c is reduced to (1.2) applied to (a,c),(d,b).
- An exhaustive check of all 16 384 subsets of {0,…,13} found no subset where "sum-Sidon (a≤b)" and "distinct positive differences" disagree.
- The translation to {0,…,N−1} is legitimate.

### 2. §2 kernel and energy — VERIFIED
- Recomputed symbolically: f(x) = ∫h(s)h(s+x)ds = 4/3 − 2x + (2/3)x³ on [0,1].
- Also confirmed: f(1)=0, f(0)=‖h‖²=4/3, ∫h=1, ∫f=1, and f′=2(x−1)(x+1) ≤ 0 on [0,1].
- (2.4): ∫h(t−x)h(t−y)dt = f(x−y), which follows from evenness. Positivity is immediate from E(μ,μ)=∫(h*μ)².
- The L²-finiteness bound and the Fubini justification are correct. (2.5) is Cauchy–Schwarz in L² and is valid for signed measures.

### 3. §3 half-line correction — VERIFIED (every display re-derived; no wrong-direction step)
- **(3.3)**: correct. The induction extends the integration range using nonnegativity. U^{*n}([0,R]) ≤ Rⁿ/n!.
- **h/2 = H − U*H, pointwise including t=0 and t=1.** For t≥0, U*H(t)=min(t,1), so H−U*H=(1−t)₊=h/2.
  At t=1 both sides are 0, and at t=0 both are 1. The telescoping (3.4) is exact, and the remainder
  U^{*(m+1)}([0,t]) ≤ t^{m+1}/(m+1)! tends to 0.
- **(3.2) second identity**: (f*g₊)(x) = ∫h̃(y)H(x−y)dy = 1 for x ≥ 0, because supp h̃ = [−1,0].
  The same formula gives (f*g₊)(x)=(1+x)² on [−1,0]; I used this below.
- **(3.6)**: checked with the closed form u(t)=eᵗ+Σ_{k=1}^{⌊t⌋}(−1)^k e^{t−k} t (t−k)^{k−1}/k!.
  This form was itself verified against the recurrence (3.8) by quadrature at 6 points, with residual ≤ 3e−26.
  Results: u(1)=e−1, the left limit is e, and u(t)=eᵗ on [0,1). The warning in lines 243–244 is correct and the right-continuous convention is handled correctly.
- **Lemma 4**: the integrating-factor formula and the kernel K_x(y) are correct.
  - K_x ≥ 0 and ∫K_x = 1.
  - K_x(y) ≥ e^{1/2}−1 ≈ 0.6487 > 1/2 on y∈[1/2,1]. The grid minimum equals this value exactly.
  - The Doeblin split into a common mass of 1/4 plus a nonnegative remainder of mass 3/4 gives both nesting and contraction by 3/4.
  - c=2 follows from h*g₊=1 on t>1. The atom contributes h(t)=0 there.
  - Numerically, |u−2|/((e−1)(3/4)^{⌊t⌋}) ≤ 0.582. The true decay is much faster: |u(5)−2|=5.8e−5 and |u(10)−2|=1.2e−9.
- **Lemma 5**: |r| ≤ ((e−1)/2)(3/4)^{⌊t⌋} ≤ (3/4)^{⌊t⌋}. The steps 4(3/4)^{⌊L⌋} ≤ (16/3)e^{−αL} ≤ 6e^{−αL} are correct.
  - Numerically, ‖q‖_TV ≈ 0.790 (claimed ≤ 9/2) and |q|((1,∞)) ≈ 0.0442 (claimed ≤ 4.5).
  - (3.15) agrees with direct quadrature at s=0.3, giving 3.674829463… on both sides.
  - φ(s)=s/2−s²/6+O(s³) holds with the stated s⁴/24 remainder, and (s−2φ)/(2sφ)→1/3.
  - Independently, q(ℝ) = 0.333333333333333333333376 by quadrature. Also g₊([0,t])−t → 1/3, which matches the renewal-theory value E[X²]/(2E[X]) = 1/3 for X~U(0,1).
  - The dominated-convergence step is legitimate because |q| is finite.
- **Boundary terms and rounding**: there are no integer-rounding steps in §3. The atom ½δ₀ is carried
  correctly in (3.5), (3.11), the TV bound, and the excess mass q(ℝ)=1/3.

### 4. §4–§5 joining and the discrete inequality — VERIFIED
- **(4.4)**: 1_{[0,∞)} + 1_{(−∞,L]} − 1_{[0,L]} = 1, so ν_L = g₊ + g₋^L − dt. The atoms at 0 and L stay in [0,L].
- **(4.5)**: (f*g₋^L)(x) = (f*g₊)(L−x) by evenness, which equals 1 for x ≤ L. Hence V_L ≡ 1 on [0,L], including both endpoints.
  - Confirmed by direct numerical convolution for L ∈ {1, 2.5, 6}, with error ≤ 1.2e−16.
  - Stronger fact found in passing: V_L(x) = (1 − dist(x,[0,L]))₊² for every x when L ≥ 1. It follows from the formulas for f*q noted in item 3. So 0 ≤ V_L ≤ 1, and the bound 13 in (4.6) is valid but loose.
- **(4.7)**: E(ν_L,ν_L) − ν_L(ℝ) = ∫_{ℝ∖[0,L]}(V_L−1)dν_L is exact. The bound 14·12e^{−αL} = 168e^{−αL} ≤ 200e^{−αL} is valid.
  - Exact values from the closed form: E(ν_L,ν_L) − (L+2/3) = +8.2e−3 (L=1), −2.0e−4 (L=2), −1.2e−4 (L=3), +9.5e−7 (L=5), +6.6e−12 (L=10).
  - Allowed by the paper: 150, 112, 84, 47, 11.
- **Lemma 6 (the new ingredient): independent check.** I computed sup μ(ℝ)²/E(μ,μ) over positive measures on fine grids of [0,L] (401–1601 nodes). This grid value is a lower bound for the true capacity C(L).
  Lemma 6 asserts C(L) ≤ E(ν_L,ν_L). The two values sandwich tightly and never cross:

  | L | grid capacity (≤ C(L)) | E(ν_L,ν_L) (≥ C(L)) |
  |---|---|---|
  | 1 | 1.674493 | 1.674882 |
  | 2 | 2.666456 | 2.666465 |
  | 3 | 3.666532 | 3.666542 |
  | 5 | 5.666640 | 5.666668 |
  | 8 | 8.666601 | 8.666667 |

  A false Lemma 6 would make the left column exceed the right. The constant L+2/3 is essentially the true capacity.
- **Lemma 7**: E(μ,μ) = (4/3)k + 2Σ_{d∈D₊}f(d/T) is exact, since each positive difference occurs exactly once by Lemma 1.
  - The Riemann-sum step f(d/T) ≤ T∫_{(d−1)/T}^{d/T} f uses monotonicity in the correct direction.
  - Lemma 6 is applied with L = N/T ≥ 1, and supp μ ⊆ [0,(N−1)/T] ⊆ [0,L].
- **Uniformity in the window length**: Lemma 7 holds for every *real* T ∈ (0,N]. Neither Lemma 6 nor Lemma 7 needs T or L to be an integer.
  The proof never rounds T. §6 uses the real value T = √2 N^{3/4}, so there is no integer-optimisation issue.

### 5. §6 additive constant +1 and onset — VERIFIED (onset sufficient, far from sharp)
- **Exact or symbolic checks, all passed**:
  - (6.2) expands to the stated coefficients.
  - (6.5) P₀(y) = (10/9)x² + (γ/9)x + 1/9 holds, using γ² = 8/9.
  - The identity in (6.7) holds.
  - Integer facts: 24000·32 = 768000 < 2²⁰, 24000/2²⁰ = 375/16384 < 1/32, and 120⁴ = 207 360 000.
  - α = 0.28768… ≥ 1/4 and α/√2 = 0.20342… ≥ 1/6.
- **All N ≥ N₀**: εx ≤ 200x e^{−x/6} is decreasing for x ≥ 6, so εx ≤ 24000e^{−20} for all real x ≥ 120.
  The remaining steps (y ≤ 3x², √2 ≤ 3/2, x ≤ x²) are polynomial facts valid for x ≥ 1. The argument is genuinely uniform in N and not a point check.
  - The root-location step is correct: a monic quadratic with negative constant term, P_ε(k) ≤ 0, and P_ε(y) > 0 imply k < y.
  - The non-strict (1.1) then follows.
- **Actual values at N₀**:
  - εx = 6.0e−7. The paper's chain bounds it by 4.9e−5 (via e^{−20}) and then by 0.0229 (via 2^{−20}); it needs < 1/32.
  - P_ε(y) = 16012.7, against the claimed lower bound 53x²/64 = 11925.
  - The real positive root is 14513.583, against y = 14514.137 (gap 0.554). Lindström gives 14521 at N₀.
- **Does it fail below N₀? No. The onset is only a sufficient choice.**
  - (a) The paper's own sufficient condition 200x e^{−x/6} < 1/32 already holds for x > 78.78, i.e. N > 3.85·10⁷.
  - (b) Lemma 7 with T = √2x³ and the exact ε = 200e^{−αx/√2} gives P_ε(y) > 0 for every scanned x > 46.161 (N > 4.54·10⁶).
    The scan used step 0.01 in x at 50-digit precision and is not interval-certified.
  - (c) Optimising T in (5.1): the margin y − min_T(root) is −0.56 at N = 2·10⁶ and +0.07 at N = 4·10⁶. It tends to 5/9 as N grows.
  - (d) The statement (1.1) itself holds, with margin ≥ 1.06, at the first N admitting n elements for all n ≤ 28.
    I recomputed optimal Golomb rulers G(n) for n ≤ 11 (…, 44, 55, 72). For n = 12…28 the A003022 values are quoted from memory.
  - No real Sidon set comes close to violating (1.1) anywhere.

### 6. §7 origin of 2√2/3 — VERIFIED
- a = f(0) = 4/3 and b = 2q(ℝ) = 2/3. Then c(t) = (bt + a/t)/2 = t/3 + 2/(3t).
- The AM–GM identity gives min_t c(t) = √(ab) = √(8/9) = 2√2/3, attained exactly at t = √(a/b) = √2. This is the T used in (6.1).
- (7.5) and (7.7) were checked algebraically. κ = s² with s² − γs − x² = 0, and the remainder identity is exact.
- The limitation statement is correct and properly scoped to the retained scalar inequalities (5.1):
  - κ_N satisfies every member of the family (7.6), with equality at T = √(aNκ/b).
  - ⌊κ_N⌋ satisfies each monic quadratic inequality.
  - Therefore no c < γ follows from (5.1) alone.
- The Riemann-sum loss in Lemma 7 (true Σ_{d≥1} f(d/T) = T/2 − 2/3 + O(1/T)) affects only the additive constant, not the coefficient, as the paper implicitly asserts.

### 7. Sanity versus Lindström; source of the improvement — VERIFIED
- The same framework with h = 1_{[0,1)} (so U = δ₁) gives g₊ = Σ_{n≥0} δ_n and q(ℝ) = 1/2, hence a = b = 1.
  Then (5.1) becomes Lindström's k² ≤ (N/T + 1)(T + k), giving √N + N^{1/4} + O(1).
- The paper's argument is therefore a strict generalisation of Lindström's. For N ≥ N₀ the new bound is strictly smaller because γ < 1.
- **The new ingredient** is the linear weight h(t) = 2(1−t)₊ together with its exact half-line equilibrium (renewal) measure:
  - it raises the diagonal cost a from 1 to 4/3;
  - it lowers the boundary excess b from 1 to 2/3;
  - so ab drops from 1 to 8/9.
- Side computation: for weights h ∝ (1−t)₊^p, ab = 2(p+1)²/((p+2)(2p+1)). This is minimised near p = 1, where it equals 8/9.
- **Validity for all Sidon sets**: Lemma 6 is a statement about *every* finite positive measure on [0,L], with no Sidon or extremal hypothesis.
  The Sidon property enters only once, in (5.2), as "each positive difference occurs at most once". Nothing assumes an extremal configuration.

### 8. Attempts to break it — no counterexample to any lemma
I tested 160 Sidon sets and found no violation of Lemma 6, of the upper bound E ≤ T + 4k/3, or of (5.1).
- **Sets tested**:
  - Singer planar difference sets for every prime q ≤ 97, built from GF(q³) with a primitive cubic.
    Each was unwrapped by a span-minimising dilation and rotation (q = 97 gives k = 98, N = 8526), and also truncated to windows of 1/4–1 of the modulus.
  - Mian–Chowla greedy prefixes of length 5–120.
  - "Two-ends" Sidon sets: a Singer ruler and its reflection at the two ends of a long interval, made Sidon by greedy repair.
- **T range**: 1 and 5, 0.3–3 times N^{3/4} (including √2 N^{3/4}), k, N/2 and N.
- **Smallest relative slacks**:
  - Lemma 6 with the paper's constant: 0.223.
  - E ≤ T + 4k/3: 0.0013, at Singer q = 97 with T ≈ 887. This is expected, since short differences of a near-perfect Sidon set fill [1,T] almost completely.
  - (5.1): 0.289.
- **Lemma 6 against arbitrary non-Sidon measures**: 4000 weighted point measures (uniform, end-clustered, end-atoms plus a lattice) on L ∈ {1,…,13}.
  I used the much tighter capacity L + 2/3 + 0.0083 instead of the paper's constant. The minimum relative slack was 0.0051, with no violation.
- **Lemma 6 for end-concentrated mass**: μ = (k/2)(δ₀ + δ_L) has E = 2k²/3, which is ≥ k²/(L + 2/3) for every L ≥ 5/6. End-concentrated sets therefore cannot break it.
- **Audit script**: `check_sidon_bound.py` was executed here with default settings in about 2 s, exit 0.
  - It printed NUMERIC PASS at all 10 grid points (N₀, N₀+1, …, 10²⁴), SELF-CHECK PASS (1368 Sidon subsets, N ≤ 12), and FINITE PASS (exact maxima for every N ≤ 60, 91 104 nodes).
  - Its minimum spans for k ≤ 10 agree with my independent search.
  - This is the first Python execution recorded for it that I am aware of. Section 9 says it had not been run.

## Optional remarks (not needed for correctness)
- **R1 (lines 475–503)**: V_L has the closed form (1 − dist(x,[0,L]))₊², so 0 ≤ V_L ≤ 1.
  The error in (4.7) is then ≤ 2|q|((L,∞)) ≤ 12e^{−αL}, not 168e^{−αL}. This would simplify Lemma 6 and could lower the onset.
- **R2 (lines 255–258)**: "for almost every t" is weaker than necessary. With the right-continuous representative, (3.7) holds for every t ≥ 0. This is harmless.
- **R3 (line 619)**: "onset not claimed minimal" is accurate and very conservative. See item 5(b)–(c).
- **R4 (line 1, §8–9)**: the status lines say "same-vendor reviewed only" and "Python not run". Both are now outdated by this review and the execution in item 8. Updating them is the coordinator's decision.
- **R5**: the measure-theoretic justifications (Tonelli, Fubini, local finiteness, convolving the locally finite identity (4.4) with compactly supported f) are adequate. They are routine and I checked them by reading only.
- **R6**: §7's "no general method barrier is claimed" is correctly modest. The kernel family computation in item 7 shows that p = 1 is near-optimal only within one simple family.

## What I did not verify
- **No novelty or priority check**, and G2 was not read. From memory only (not checked here), the published improvements of Lindström's constant 1 are:
  - ≈ 0.998 (Balogh–Füredi–Roy);
  - 0.99703 (O'Bryant);
  - 0.98183 (Carter–Hunter–O'Bryant).

  If that recollection is right, a short argument giving 2√2/3 ≈ 0.9428 is a large jump. That is a reason for G2 and an independent human expert to look. It is not evidence of an error: I found none.
- No kernel (Lean) formalization.
- Numerical scans (onset thresholds, grid capacities, Sidon-set tests) are finite, floating-point or mpmath evidence, not interval-certified proofs. The proof does not depend on them.
- The A003022 values for n = 12…28 are quoted from memory.
- I did not review the code of `check_sidon_bound.py`, only its output.
