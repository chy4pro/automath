# Cross-vendor referee B (Claude Opus), independent reconstruction and numerical attack

Date: 2026-10-02. Object under review: `SIDON_BOUND_PROOF.md` (produced by GPT-6 Astra) and
`check_sidon_bound.py`. Isolation: this referee did not read any other `REFEREE_*` file or
`G2_SIDON_20261002.md`. No novelty or priority question is addressed here.
Scope: this is one cross-vendor model review. It is not independent human verification and not
kernel formalization.

Claim under review: every Sidon set `A ⊆ {1,…,N}` satisfies
`|A| ≤ √N + (2√2/3)·N^{1/4} + 1` for every integer `N ≥ 207 360 000 = 120^4 = 14400^2`.

## Verdict: PASS

No failing statement was found. Every inequality claimed for all Sidon sets and all window
parameters held on about 120,000 explicit Sidon sets, with about 65 window values each. Each
analytic object in §3–§4 matched independent high-precision computation. The final arithmetic
is correct and holds for every N ≥ N0. The checker runs in Python, exits 0 and its counts match
§9. The recommendations in §10 are non-blocking; none is needed for correctness.

Three most important findings:

1. **My independent reconstruction gives the same inequality (5.1).** It has the same constants
   `a = f(0) = 4/3` and `b = 2q(ℝ) = 2/3`. The document's version is slightly weaker in two
   places. It uses the support length `N/T` instead of `(N−1)/T`. Its exponential error
   `200·e^{−log(4/3)·L}` is valid but very crude: the true decay rate is about 2.0888 and the
   true error is at most 8.3·10⁻³ at L=1. I confirmed `q(ℝ) = 1/3`, so `b = 2/3`, by three
   independent routes: the Laplace transform, the discrete capacity limit, and the
   outer-factor (spectral factorization) group delay.
2. **Numerical attack: no violations, and the key steps are numerically tight.** The step
   (5.2), `E ≤ T + 4k/3`, reaches a ratio of 0.9987 on Singer sets. I also ran the most
   adversarial finite test of Lemma 6 that exists: the exact discrete capacity
   `1ᵀK⁻¹1`, which is the supremum over all real weightings of grid points. It reaches 0.99913
   of the document's denominator `L + 2/3 + 200e^{−αL}` and never exceeds it. So the constant 2/3
   in (4.1) is correct and essentially sharp.
3. **The onset 120⁴ is a convenience choice and not a rounding of the true onset.** Inequality
   (5.1) already implies the real-number form `k < y` for every N ≥ 4,540,589 (x ≈ 46.16) with
   the document's T. With T optimized per N, it holds for every N ≥ 3,630,447 (x ≈ 43.65). Both
   thresholds are about 50 times smaller than 120⁴; the document correctly says the onset is not
   minimal. No other choice of T in (5.1) gives a constant below 2√2/3: the best T gives
   `root − x² − γx → 4/9`. So the document's restricted "limit" statement in §7 is correct.

## 1. Independent reconstruction (written after reading only §1 and §7)

§7 gave me the numbers `a = f(0) = 4/3` and `b = 2q(ℝ) = 2/3`, and described them as the
"diagonal cost" and the "half-line excess mass". My reconstruction was guided by these two
values. I found the kernel from a = 4/3 and derived b independently before reading §3.

**(R1) Abstract Cauchy–Schwarz step.** Let f be even, nonnegative and positive-definite on ℝ.
Let `A ⊆ {0,…,N−1}` be Sidon with k = |A|, let T > 0, and put `μ_A = Σ_{a∈A} δ_{a/T}`. Let ν
be any finite signed measure whose potential satisfies `f*ν ≥ 1` on `supp μ_A`. Then

    k ≤ ∫ f*ν dμ_A = E(μ_A,ν) ≤ E(μ_A)^{1/2} E(ν)^{1/2}.

Here `E(μ_A) = k f(0) + 2 Σ_{d∈D+(A)} f(d/T) ≤ k f(0) + 2 Σ_{d≥1} f(d/T)`, using Sidon
(r(d) ≤ 1) and f ≥ 0. The smallest possible `E(ν)` is the f-capacity of the support interval.

**(R2) Kernel.** Take `f = h*h̃` with h causal, nonnegative and `∫h = 1`. Let
`H(s) = ∫ e^{−st} h(t) dt` be its Laplace transform. The causal inverse `g_+ = L⁻¹[1/(sH(s))]`
satisfies `h*g_+ = 1_{[0,∞)}`, so `f*g_+ = 1` on `[0,∞)`. Its excess mass over half-line
Lebesgue measure is

    q(ℝ) = lim_{s↓0} (1/(sH(s)) − 1/s) = ∫ t h(t) dt.

This requires H to have no zeros in Re s ≥ 0 (minimum phase). Then
`a·b = ‖h‖₂²·2∫t h`. For nonnegative h, the KKT conditions for "minimize ‖h‖² subject to
∫h = 1 and ∫th = m" give `h = c(ℓ − t)_+`. That yields `a·b = 8/9` for every ℓ, so the ramp
`h = 2(1−t)_+` is optimal in this family. For it, f(0) = 4/3 and ∫th = 1/3, so b = 2/3.

For the ramp, `sH(s) = 2(s − 1 + e^{−s})/s`. The nonzero roots of `s − 1 + e^{−s}` are
`s = 1 + W_k(−1/e)` with k ≠ 0, −1. The rightmost pair is `−2.08884 ± 7.46149i`, so
`g_+ − 1_{[0,∞)}` decays like `e^{−2.0888 t}`.

**(R3) Two ends.** Take `ν = 1_{[0,L]} + q + q_L`. It has potential exactly 1 on [0, L] and
energy `L + 2/3 + δ(L)`, with `|δ(L)| = O(e^{−2.09 L})`. This gives

    k² ≤ ((N−1)/T + 2/3 + δ)·(T + 4k/3).

With `T = √2·N^{3/4}`, this yields `k ≤ √N + (2√2/3)N^{1/4} + 4/9 + o(1)`.

**Comparison with §2–§6, listing every place where the document's inequality differs:**

| Item | Reconstruction | Document | Effect |
|---|---|---|---|
| Kernel, a, b | `h=2(1−t)_+`, 4/3, 2/3 | identical (2.1)–(2.3), (3.14), (4.3) | none |
| Correction measure | equilibrium measure / causal inverse | renewal series `g_+ = ½Σ U^{*n}`, identical object (Laplace transform `s/(2(s−1+e^{−s}))` in both) | none |
| Support length | `(N−1)/T` | `N/T` (stated as permitted, Lemma 7) | doc weaker by 1/T; harmless |
| Exponential error | rate 2.0888, measured `δ(L)`: +8.2e-3 (L=1), −2.0e-4 (2), −1.2e-4 (3), +9.5e-7 (5), −2.8e-9 (8) | `200·e^{−αL}`, α = log(4/3) ≈ 0.2877 (decay proved via a contraction bound of (3/4) per unit) | valid upper bound; crude; it alone forces the large onset |
| T range | any T > 0 | `0 < T ≤ N` (needs L ≥ 1 for (3.13)) | harmless |
| Riemann sum | `Σ_{d≥1} f(d/T) ≤ T/2` | same (Lemma 7) | none (could be sharpened to `T/2 − 2/3 + O(1/T)`; irrelevant) |

No difference affects the theorem. I then read §2–§6 line by line. The telescoping identity
(3.4) holds, including at t = 0. The values (3.6) hold, including the right-continuous
convention `u(1) = e−1`. In the contraction step of Lemma 4: `K_x ≥ 0`, `∫K_x = 1`, `K_x ≥ 1/2`
on [1/2, 1], and the contraction factor is 3/4. The bounds `‖q‖_TV ≤ 9/2` and
`|q|((L,∞)) ≤ 6e^{−αL}` hold, and so does the Laplace limit 1/3. In Lemma 6, (4.4)–(4.7) hold,
including the reflection and evenness step for `f*g_-^L`. In §6, the expansion (6.2), the
algebra (6.3)–(6.7) and the monotonicity of `x e^{−x/6}` for x ≥ 6 are all correct. I found no
gap.

## 2. Numerical attack on every all-N intermediate inequality

The inequalities tested are claimed for every Sidon set `A ⊆ {0,…,N−1}` and every
0 < T ≤ N, with L = N/T and ε = 200e^{−αL}:

* (5.2) identity `E = 4k/3 + 2Σ_{D+} f(d/T)`, checked against the full ordered double sum for k ≤ 40;
* (5.2)/Lemma 7: `E ≤ T + 4k/3` (reported as `(E − 4k/3)/T ≤ 1`);
* Lemma 6 (4.1): `k² ≤ E·(L + 2/3 + ε)`;
* (5.1): `k² ≤ (L + 2/3 + ε)(T + 4k/3)`.

For information I also computed the unclaimed versions without ε. The T-grid per set has
`{0.5, 0.9, 1, 1.5, 2, 3, N/3, N/2, N, √2N^{3/4}}` plus 60 log-spaced values in [1, N]. Every
input set was re-verified as Sidon (sum convention with a ≤ b, including doubles). The checks
used float64; the closest margin to failure was 1.3·10⁻³, far above rounding error.

| Family (all built by this referee's own code) | sets | worst `E≤T+4k/3` | worst Lemma 6 | worst (5.1) | max `k / (√N+γN^{1/4}+1)` |
|---|---|---|---|---|---|
| All maximum Sidon sets of {0..N−1}, N ≤ 60 (all optimal rulers, mirrors and translates; own DFS: G(k)=0,1,3,6,11,17,25,34,44,55, no 11-mark ruler of span ≤ 59) | 117,197 | 0.9651 | 0.3644 | 0.3195 | 0.904 |
| Singer sets, all 43 prime powers q ≤ 127, 4 multipliers × 4 rotations, tight interval | 688 | 0.9987 | 0.8214 | 0.8201 | 0.946 |
| same, placed in [0, m) | 688 | 0.9986 | 0.8208 | 0.7809 | 0.920 |
| Bose–Chowla, all q ≤ 127, same embeddings | 684 + 684 | 0.9921 | 0.8219 | 0.8166 | 0.947 |
| Mian–Chowla prefixes, lengths 1..80 | 80 | 0.9640 | 0.4440 | 0.4214 | 0.797 |
| Random greedy Sidon sets, N = 10…30000 | 48 | 0.8993 | 0.7598 | 0.3549 | 0.806 |
| Random subsets of Singer sets (q = 31, 64, 127) | 30 | 0.9543 | 0.7956 | 0.6947 | 0.862 |
| Adversarial: Singer cluster at left end / right end / middle, N = span·{1,2,4,16,64,1024} | 90 | 0.9982 | 0.8094 | 0.8082 | 0.938 |
| Adversarial: two end clusters (greedy-repaired union) | 30 | 0.9982 | 0.5023 | 0.4549 | 0.705 |
| Adversarial: endpoints only / near-end sparse sets, N up to 10⁶ | 10 | 0.7168 | 0.1503 | 0.1288 | 0.685 |

**Result: 0 violations.** All claimed ratios are ≤ 1. The Sidon step (5.2) is nearly tight
for dense algebraic sets: 0.9987 at Singer q = 127, N = 15321, T ≈ 1123. This is expected,
because almost all small differences occur. So the slack in the final bound comes from the
Cauchy–Schwarz step in Lemma 6, not from the Sidon step.

**Sharpest test of Lemma 6 (discrete capacity).** Lemma 6's proof works for any signed or
positive μ supported in [0, L]. Over all real weight vectors w on the grid `{0,…,N−1}/T`,
`sup (Σw)²/E(w) = 1ᵀK⁻¹1` with `K_ij = f((i−j)/T)`. I computed this by Cholesky
factorization for N ∈ {2,3,5,8,13,20,40,60,100,200,400,800,1600} and about 25 values of T each.
Results:

* The maximum of `1ᵀK⁻¹1 / (L + 2/3 + 200e^{−αL})` was **0.99913** (N = 1600, T = 40:
  capacity 40.63344 against 40.66868). There was no violation, and the bound is essentially
  attained.
* The unclaimed sharper form `≤ (N−1)/T + 2/3` is exceeded by at most 0.0104, at L ≈ 1
  (N = T = 20). This agrees with the measured `δ(1) = +8.2·10⁻³`, so the error term is genuinely
  needed at small L. The document's ε covers it with a large margin.
* As T grows, the capacity excess tends to 2/3: 0.6005, 0.6376 and 0.6532 at T = 20, 40, 80.

**Analytic objects (mpmath, 30–60 digits).** I computed the exact renewal density from the
classical closed form `u = d/dt Σ_j (−1)^j (t−j)^j e^{t−j}/j!`.

* u(0) = 1, u = e^t on [0, 1), u(1) = e − 1, and the left limit at 1 is e.
* The renewal equation `u(t) = ∫_{t−1}^t u` holds to 2·10⁻⁵⁶.
* `max|u−2|` on [n, n+1) divided by `(e−1)(3/4)^n` is 0.58, 0.22, 0.049, … and 1.9·10⁻²⁰ at
  n = 25. So (3.7) holds with enormous slack. The observed decay rate is 2.0816, against the
  predicted 2.0888.
* q(ℝ) = 0.3333333333333333333333333.
* ‖q‖_TV ≈ 0.790, against the bound 9/2.
* `(f*q)(x) = 1 − F(x)` for x ≥ 0 (Lemma 3) holds to 10⁻⁶¹. This implies V_L ≡ 1 on [0, L],
  which is (4.5).
* The outer-factor formula `b = (2/π)∫₀^∞ −log f̂(t)/t² dt` gives b = 0.6666662. This is an
  independent route to 2/3; the same formula gives b = 2 for the Laplace kernel.

## 3. Asymptotic sanity (no hidden lower bound on |A|)

Lemma 6 holds for every finite positive measure, so it does not use Sidon at all. Lemma 7 uses
only `r(d) ≤ 1` and `f ≥ 0`. §6 uses only the sign pattern of a monic quadratic, together with
`k ≥ 0`. Nowhere does the argument assume a lower bound on k, a density property, or that A
reaches the ends of the interval. The numerics agree. Sparse sets satisfy every inequality with
large slack: endpoint-only sets, random greedy sets with k ≈ N^{1/3}, and clusters placed at one
end of an interval 1024 times longer. For Singer-type sets with `|A| ≈ √N`, the second term is
slack as expected (`k/bound ≈ 0.946` at q = 127).

## 4. Final arithmetic and the true onset implied by the argument

* I checked (6.2), (6.5), (6.6) and (6.7) by hand and in exact arithmetic. One instance:
  `P₀(x²+γx+1) = (10/9)x² + (γ/9)x + 1/9`. At N0 the positive root is 14513.58328 and
  y = 14514.13708, so `y − ρ = 0.554`; the true ε at N0 is 5.0·10⁻⁹. The all-N step, that
  `x e^{−x/6}` is decreasing for x ≥ 6, is correct, so the bound holds for every N ≥ N0 and not
  only at grid points.
* **True minimal onset implied by (5.1), real form `ρ(N) < √N+γN^{1/4}+1`**, computed with
  40-digit mpmath and bisection:
  * with the document's `T = √2N^{3/4}`, it holds for every N ≥ **4,540,589** (x ≈ 46.161);
  * with T optimized in (0, N] for each N, it holds for every N ≥ **3,630,447** (x ≈ 43.651).

  Above these thresholds a dense geometric sample up to 120⁴ found no violations, and §6 covers
  everything beyond 120⁴. The integer form `⌊ρ⌋ ≤ y` may hold somewhat earlier, but it is not
  monotone in N because of the floor, so I do not quote it.
* 207,360,000 = 120⁴ = 14400² is **not** a rounding of the true onset, which is about 46⁴. It
  was chosen so that x₀/6 = 20 and (6.3) reduces to integer arithmetic, as the document says
  ("not claimed minimal").
* Informative only, not proved: the true |δ(L)| is about 10⁻² or less. If ε were 0.01 instead
  of 200e^{−αL}, the same scalar inequality with optimized T would give `ρ < y` for every
  2 ≤ N < 2000 and at all sampled N up to 60⁴. The large onset is purely an artefact of the
  crude tail constant.

## 5. Audit of `check_sidon_bound.py`

I ran it for the first time in Python: Python 3.12, default invocation, exit 0, 2.2 s
wall-clock. It reports 91,104 search nodes, 1,368 Sidon subsets for N ≤ 12 and spans
0,1,3,6,11,17,25,34,44,55. These match §9's JavaScript figures and my independent DFS.

What it does:

* It re-checks the algebra of §6 at 10 grid points with rational intervals, plus a symbolic
  check of `P₀(y)` in ℚ[√2]. It takes ε ∈ [0, 1/(32x)] **from (6.3)**, so it does not evaluate
  ε independently.
* It brute-forces maximum Sidon sets for N ≤ 60, with a literal subset audit for N ≤ 12.
* For those small sets and T ∈ {1/2, 1, 3/2, 2, n/2, n}, it checks the (5.2) identity, the
  injection, the kernel-sum bound, the energy bound and "stronger sufficient" versions of
  Lemma 6 and (5.1).

What it does **not** check:

1. Nothing in §3 (Lemmas 3–5): it does not check `g_+`, `u`, the bound (3.7), `q(ℝ) = 1/3`,
   `‖q‖_TV` or the tail bound (3.13).
2. Nothing in §4 beyond the final inequality: it does not check `V_L ≡ 1` (4.5), the value
   `ν_L(ℝ) = L + 2/3` or the error bound (4.7).
3. Its Lemma 6 and (5.1) tests are **non-discriminating**. Over all its own test cases, the
   largest ratio k²/(bound) is 0.288 for Lemma 6 and 0.262 for (5.1). At T ≤ 2, f(d/T) vanishes
   for d ≥ 2. At T = n/2 or n, the term 200(3/4)^{⌈L⌉} ≥ 112 dominates. An error of constant
   size, for example b = 1/3 instead of 2/3, would pass undetected.
4. It never tests a set where the Sidon step is tight (Singer/Bose–Chowla), any N ≥ 61, or
   T ≈ √2N^{3/4} at a meaningful scale.
5. It does not check the optimality and limitation claims of §7.
6. The finite search is logically irrelevant to the theorem, which is stated only for
   N ≥ 2·10⁸. The identity `0.943² − 8/9 = 3241/9000000` is harmless but checks nothing used.

## 6. The optimisation giving 2√2/3

* (7.3)–(7.6) are correct. For any T > 0, `(N/T + b)(T + aκ) ≥ (√N + √(abκ))² = κ²` by AM–GM,
  so `κ_N = x² + γ√(x²+γ²/4) + γ²/2` satisfies every instance of the scalar inequality, even
  with the error term removed. Identity (7.7) checks.
* Numerically, the optimal T has `T_opt/x³ → √2`: 1.4825 at x = 10, 1.4198 at x = 120 and
  1.41421 at x = 10⁶. With the best T, `ρ − x² − γx` equals 0.4549, 0.4453 and 0.444445 at
  x = 10, 120 and 10⁶, so it tends to 4/9. **No choice of T gives a constant below 2√2/3**, and
  the restricted "limit of the method" statement is correct as scoped.
* Stronger than the document claims: within the document's construction family (nonnegative
  causal minimum-phase h, where b = 2∫th), the ramp is the unique optimum, with a·b = 8/9; see
  (R2).
* Exploratory only: I compared kernels outside that family using the outer-factor formula.
  * Askey kernels `(1−|x|)^ν` give a·b = 0.8937, 0.9092 and 0.9222 for ν = 2, 3, 4.
  * 25 random nonnegative non-minimum-phase two-bump h gave a best of 0.8913.

  None beat 8/9. This is not exhaustive, and the document correctly makes no general barrier
  claim.

## 7. What was not verified

* Measure-theoretic applicability (Fubini/Tonelli, local convolution of locally finite
  measures) was checked by reading, not by formalization. No Lean or kernel work was done.
* I did not check the statement for any N ≥ N0 on actual Sidon sets. The tested inequalities
  are N-independent lemmas; the largest sets tested had N ≤ 10⁶ and k ≤ 129.
* No novelty, priority or literature check (G2) was in my scope, and I did not read the G2
  file.
* The minimal-onset figures in §4 are floating-point and mpmath computations, not proofs. They
  concern only what (5.1) implies, not the true extremal function.
* Cost: about 30 CPU-minutes, including one aborted exploratory run, on at most 2 concurrent
  processes, with peak memory well under 1 GB.
  No solvers and no network were used. Model-token cost is not measured here.

## 8. Non-blocking recommendations

1. Update §9: the Python checker has now been run (exit 0, 2.2 s; figures match).
2. Make the checker discriminating. Add the discrete-capacity test of Lemma 6
   (`1ᵀK⁻¹1 ≤ L + 2/3 + ε`; reaches 0.9991), numerical checks of `q(ℝ) = 1/3` and `V_L ≡ 1`, and
   Singer-set tests of (5.2), where the step is tight. For reference, the core test is:

   ```python
   K = f((i[:,None]-i[None,:])/T); w = cho_solve(cho_factor(K), ones(N))
   assert w.sum() <= N/T + 2/3 + 200*exp(-log(4/3)*N/T)
   ```
3. Optional: a sharper tail bound would lower the onset a great deal. For example, use the true
   decay rate 2.0888 or a better contraction constant, and the true size of `|E(ν_L,ν_L) − L − 2/3|`.
   Even unchanged, (5.1) already gives the bound from N ≈ 4.5·10⁶. Any such change would need its
   own proof and review.
