# Adversarial referee report: Manhattan DDC, Sidon boxes, sonar, kernel perturbation

Date: 2026-10-02. Referee: Claude (Anthropic). The write-ups under review are by
GPT-6 Astra (OpenAI). MANHATTAN.md and BOXES.md describe themselves as OpenAI
reviews of Claude scout derivations. That makes this review cross-vendor for the
Astra text and repairs. For the underlying scout ideas it is **not**
vendor-independent.

Scope. Files read: `COMMON_CAPACITY.md`, `MANHATTAN.md`, `BOXES.md`, `SONAR.md`,
`KERNEL_PERTURBATION.md`, `KERNEL_FUNCTIONAL.md` and the four checkers
`check_manhattan.js`, `check_boxes.js`, `check_sonar.js` and
`check_kernel_perturbation.js` (all in `problems/capacity_transfer/`). I read
nothing else in the repository. In particular I did not read `SONAR_COSINE.md`,
which KERNEL_PERTURBATION §3 cites. I re-derived the part of it that is needed
(see §5). I did no web or literature search, and I did not check sources,
definitions against the papers, priority or novelty. No file under review was
edited.

Method. I re-derived every displayed step by hand before reading the author's
justification. I then ran numerical attacks with python3/numpy/mpmath/sympy/scipy
(≤ 2 threads) and node, with no SAT/ILP solvers. The scratch scripts are not
committed. Each test is described below in enough detail to reproduce it.

## Summary of verdicts

| Claim | Verdict |
|---|---|
| COMMON_CAPACITY (shared input: ν_L, potential 1 on [0,L], energy ≤ L+2/3+200e^{−αL}) | **PASS** (one citation-precision note) |
| MANHATTAN (M1) | **PASS** |
| BOXES (B1) | **PASS** |
| SONAR (1) | **PASS** |
| KERNEL_PERTURBATION (P1–P2 admissibility, J < π²/32) | **PASS** |
| KERNEL_PERTURBATION §3 (P4, sonar coefficient 3v) | **PASS-WITH-REPAIRS** (editorial only: dangling external references; the mathematics was re-derived and holds) |
| KERNEL_FUNCTIONAL (K1, K2) | **PASS** (one optional technical remark) |

I found no false line in the mathematics. The most serious issue concerns
evidence, not the proofs: **the bundled checkers do not test the capacity
step**. `check_manhattan.js` and `check_boxes.js` never use the certificate
energy. In `check_sonar.js` the 41,856 "sandwich" checks cannot fail on their
grid. They use the bound C_L ≤ L+2/3+200(3/4)^L with L ≤ 8. There the 200-term
dominates and the largest ratio Λ/(upper·C) over the whole grid is **0.064**.
Do not cite those counts as evidence for the analytic chain. The meaningful
numerical tests are the ones below. They use C_L ≈ L+2/3 (measured).

---

## 0. Shared input: COMMON_CAPACITY.md

**Statement used downstream.** For every real L ≥ 1 there is a finite signed
measure ν_L with (f*ν_L)(x) = 1 for all x in the closed interval [0,L], and
0 ≤ E_f(ν_L,ν_L) ≤ L + 2/3 + 200e^{−αL}, where α = log(4/3). Here f = h*h̃ with
h = 2(1−t)1_[0,1] is the ramp autocorrelation.

**Re-derived (proved, by hand):**
- f formula (2.2), f(0) = 4/3, ∫f = 1, monotonicity, f = h*h̃ ⇒ Gram identity (2.4)
  and Cauchy–Schwarz for signed measures (2.5).
- Telescoping h/2 = H − U*H. This needs h(0) = 2; I checked t = 0 and t = 1.
  It gives h*g₊ = H and f*g₊ = h̃*H = 1 on [0,∞).
- Lemma 4 contraction:
  - the kernel K_x(y) = e^x − 1_{y≤x}e^{x−y} is ≥ 0, has mass 1 and is ≥ 1/2 on [1/2,1];
  - the ranges [m_n, M_n] are nested and shrink by 3/4.
- Lemma 5: |r| ≤ (3/4)^{⌊t⌋}, ‖q‖_TV ≤ 9/2, the tail bound
  4(3/4)^{⌊L⌋} ≤ (16/3)e^{−αL}, and q(ℝ) = 1/3. The last comes from the
  Laplace-transform expansion 1/(2φ(s)) − 1/s → 1/3.
- Lemma 6: ν_L = g₊ + g₋^L − dt gives V_L = 1+1−1 on [0,L]; |V_L| ≤ 13;
  |ν_L|(ℝ∖[0,L]) ≤ 12e^{−αL}; E − (L+2/3) = ∫_{outside}(V_L−1)dν_L, so the
  error is ≤ 168e^{−αL}.

**Numerical checks (not proof):**
- The renewal density u was evaluated from the closed form
  Σ_k (−1)^k e^{t−k}[(t−k)^k/k! + (t−k)^{k−1}/(k−1)!] with mpmath (40 digits). I
  checked u(1) = e−1 with the right-continuous convention and the renewal
  identity u(t) = ∫_{t−1}^t u (to 15 digits).
- q(ℝ) = 0.333333333333333 and ‖q‖_TV ≈ 0.790. The maximum of |r| on [k,k+1)
  sits well below (3/4)^k for k = 0..9; the actual decay is about e^{−2t}.
- V_L = f*ν_L equals 1 on [0,L] to 4·10⁻¹⁴ (L = 1, 2.5, 7).
- C_L = E(ν_L,ν_L) − (L+2/3) is +8.2·10⁻³ at L = 1, −1.2·10⁻³ at L = 1.5,
  −2.0·10⁻⁴ at L = 2, −9.2·10⁻⁶ at L = 4, and below 10⁻⁸ for L ≥ 10 (quadrature
  noise). All are far inside ±168e^{−αL}.
- A positive-capacity QP on grids of [0,L] (L-BFGS-B, nonnegative weights)
  gives cap₊ ≤ C_L in every case. For example, at L = 1 cap₊ = 1.67447 and
  C_1 = 1.67488. The signed certificate is nearly optimal.

**Note (citation precision, not an error).** The transfer notes cite
"Lemma 6" for potential 1 and the energy bound. Those facts are (4.5) and
(4.7) inside its proof, not its statement. It would be cleaner to state them as
a lemma.

---

## 1. MANHATTAN.md — verdict PASS

**Exact statement checked.** A is a finite subset of ℤ². The map (p,q) ↦ p−q is
injective on ordered pairs of distinct points. This is equivalent to "no two
unordered segments have equal displacement up to sign". All p,q ∈ A satisfy
|p₁−q₁|+|p₂−q₂| ≤ r. Then for every real r ≥ 160³, m = |A| ≤ r/√2 + (4/3)^{1/3}r^{2/3}
+ 9r^{1/3}. There is no row or column restriction. The source definition was not
checked (out of scope).

**Re-derived (proved):**
- **Metric transform.** For (u,v) = (x+y, x−y), max(|Δu|,|Δv|) = |Δx|+|Δy|. So
  both ranges are ≤ r, and an independent translation places the image in [0,r]².
  Differences lie in Λ = {u ≡ v mod 2}. The translated points lie in a coset;
  only differences are used. The map is linear, so difference-injectivity is
  preserved.
- **Product certificate.** Take ρ = pushforward of ν_{r/T} by s ↦ Ts with no
  mass rescaling. Its potential under f(·/T) is 1 on [0,r]; this needs
  L = r/T ≥ 1, i.e. T ≤ r. The potential of ρ⊗ρ under F_T is 1·1 on [0,r]²
  (Fubini; finite TV, bounded kernel). Its energy is E_f(ν_L,ν_L)². This is ≤ D²
  because the energy is a nonnegative Gram value.
- **Signs.** F_T is the autocorrelation of T^{−1}h(u/T)h(v/T). So Cauchy–Schwarz
  holds for the signed product, and m² = E(μ, ρ⊗ρ)² ≤ E(μ,μ)·D². Correct (M3).
- **Lattice sum over Λ.**
  - Λ = 2ℤ×2ℤ ∪ (2ℤ+1)×(2ℤ+1), so the full sum is exactly S_e² + S_o².
  - S_e ≤ T/2 + a by monotone right-Riemann comparison with spacing 2/T.
  - S_o ≤ 2v + T∫_{1/T}^∞ f ≤ T/2 + v ≤ T/2 + a, using ∫_0^{1/T}f ≥ v/T.
  - The T < 1 case is fine.
  - So E ≤ a²m + T²/2 + 2aT + a² (M5). Dropping unrealised vectors uses f ≥ 0.
    (M6) follows.
- **Optimisation.**
  - With T = t x² and t = √2c: x³/√2 + (bt/√2 + a²/(2t²))x², and the coefficient
    is 2c/3 + c/3 = c.
  - This t minimises g(t) = bt/√2 + a²/(2t²): t³ = (8/3)√2 = a²√2/b. I checked
    this independently.
  - The coefficient 3·2^{−4/3}(ab)^{2/3} equals (4/3)^{1/3} exactly.
- **Explicit remainder.**
  - The root bound (M8) and the bracket T/√2 ≤ √B₀ ≤ T/√2 + √2a hold.
  - The seven terms of (M9) are all accounted for: x³/√2, βtx²/√2, √2ax/t,
    √2aβ, a²x²/(2t²), a²βx/t, a²β²/2, and a⁴√2D³/(8T).
  - Each listed comparison holds for all real x ≥ 160. For example,
    √2a/t = c² ≈ 1.21 ≤ 2, and a⁴√2D³/(8T) ≤ a⁴x/c ≈ 2.87x ≤ (128/27)x.
  - εx ≤ 32000e^{−20} < 1/32. The sum is 18529/2160 ≈ 8.578 < 9.
- The remark that the bare two-term bound does not follow is also right: P₀(y₀)
  has x⁵ coefficient 0 and x⁴ coefficient −(c² + 2a/t).

**Numerical tests (not proof):**
1. **Exhaustive maximum DDCs for r = 1..9** (node backtracking in rotated
   coordinates, both cosets). The maxima were m = 2, 3, 4, 6, 7, 8, 9, 10, 11.
   For all stored maximum configurations (≤ 200 per r) I ran 26,304 (config, T)
   tests:
   - E ≤ a²m + S_e² + S_o² − a² ≤ (M5): 0 violations;
   - core capacity inequality m² ≤ C(r/T)²E with C(L) = L+2/3+0.02, the measured
     envelope of C_L: 0 violations, largest ratio 0.86;
   - (M6) with the proof's constants: 0 violations.
2. **Greedy random DDCs, r = 12..80** (m up to 47), 1,050 tests: (M5) and core
   0 violations, largest ratio 0.78.
3. **Dense non-DDC sets.** Full ℤ² and Λ boxes, and a boundary-weighted
   multiset, r ≤ 40, 360 tests of the core inequality: 0 violations, largest
   ratio 0.96.
4. **Final bound** (mpmath, 50 digits). I took the positive root of (M6) at
   T = t x², with the 200e^{−αx/t} term kept, and compared it with (M1) at
   x = 160, 160.001, 161, …, 10⁶. The slack (M1 − root)/x is 6.92 at onset and
   rises to 6.93. The proof needs about 2.07x where it allows 9x. Below the
   onset, (M1) still follows from (M6) down to about x = 40 and fails at x ≤ 20.
   That is irrelevant to the stated theorem.

**Not checked:** fidelity to BEMP Definition 1 and Theorem 9, and novelty.

---

## 2. BOXES.md — verdict PASS

**Exact statement checked.** d ≥ 2 and N ≥ 1 are integers, and A ⊆ {0,…,N−1}^d is
strong Sidon: all unordered sums a+b, including a = b, are distinct. Put
x = N^{d/(2d+2)}. If x ≥ max{120, 4d}, then
|A| ≤ N^{d/2} + c_d N^{d²/(2d+2)} + 2d² N^{d(d−1)/(2d+2)}, with
c_d = ((d+1)/2)(8/9)^{d/(d+1)}. The remainder coefficient is explicit and grows
like 2d². The onset grows with d through x ≥ 4d. The statement is not uniform in
d in the O-sense, and the file says so.

**Re-derived (proved):**
- **Convention.** Strong Sidon ⇔ all ordered nonzero differences are distinct.
  I checked both directions, including p+p = r+q. No factor 2^d is lost.
- **(B3).**
  - The direct sum gives 4/3 + 8n/3 − 2n(n+1)/T + n²(n+1)²/(3T³).
  - The second form is an exact identity: sympy expansion of the difference
    gives 0.
  - The bounds θ(1−θ) ≤ 1/4 and θ(1−θ)|1−2θ| = u(1−u²)/4 ≤ 1/8 hold.
  - So S ≤ T + 7/(16T) for T ≥ 1.
- **Product certificate.** The argument matches §1: potential 1 on [0,N]^d ⊇
  [0,N−1]^d, energy E_f(ν_L,ν_L)^d ≤ D^d because the Gram energy is ≥ 0, and
  Cauchy–Schwarz holds. This gives (B4) and then (B5).
- **Scales.**
  - t = (a^d/b)^{1/(d+1)} ∈ (4/3, 3/2), s = bt = (8/9)^{d/(d+1)}, a^d/t^d = s.
  - T/x = tN^{1/(d+1)} ≥ 1, T ≤ N iff x ≥ t, L = x/t ≥ 1.
  - The linear coefficient is a^dD^d/K = sq(1+w)^d, using x^{d+1} = N^{d/2}. The
    constant term is ((1+w)(1+z))^d.
- **Error budget.**
  - (B6): 200·120e^{−20} < 1/32.
  - (B7): εtq ≤ (3/64)q², and the v coefficient is ≤ 45/64.
  - (B8): (1+u)^d ≤ 1/(1−du) ≤ 16/11.
  - (B9): the three terms bound as stated.
  - The Taylor bound for (1+v)^{d/2} is correct but loose: it uses
    p(p−1) ≤ p² and v ≤ 2q.
  - The final coefficient is 3d²/4 + 3d/2 + 9/32 ≤ 2d² for d ≥ 2.
  - The exponents of Kq and Kq² are as claimed.
- The AM–GM optimisation of (dbt + a^dt^{−d})/2 at t^{d+1} = a^d/b is correct.

**Numerical tests (not proof):**
1. S(T) direct versus (B3) on 59,177 values of T in [1,60], including T = k ± 10⁻⁹:
   largest difference 2.8·10⁻¹⁴. The largest value of T(S(T)−T) is 0.373 ≤ 0.4375 ≤ 0.5.
   For T < 1, S(T) ≤ T + a holds.
2. **Exhaustive maximum strong Sidon sets** (node). Sizes: [2]²: 3, [3]²: 5,
   [4]²: 6, [5]²: 8, [6]²: 9, [2]³: 5, [3]³: 9. On ≤ 300 maximum sets per box and
   30 scales, 22,800 tests of the energy upper bound, the core
   k² ≤ C(N/T)^d·E, (B4) and (B5) all had 0 violations. The largest core ratio
   was 0.71.
3. Greedy Sidon sets in [10..60]², [6..14]³ and [5,7]⁴ (810 tests): 0
   violations, largest core ratio 0.74. Dense full boxes (non-Sidon), d = 2, 3,
   core test: 0 violations, largest ratio 0.80.
4. **Final bound** (mpmath, 60 digits). I took the exact root of (B5), with the
   200-term kept, at the chosen T, for d ∈ {2,3,4,5,6,8,10,16,25,40,64,100,200}
   and x from the onset max{120,4d} up to 10⁴× the onset. (B1) held everywhere.
   The smallest slack is 7.03q² at d = 2, x = 120, against the allowance 8q².
   For large d the slack is about 0.95·2d²q².

**Not checked:** the source definition (arXiv 1405.4227) and comparison with
published constants.

---

## 3. SONAR.md — verdict PASS

**Exact statement checked.** n, m ≥ 1 and y₀,…,y_{m−1} ∈ {0,…,n−1}, with all
(j−i, y_j−y_i), i < j, distinct. Repeated rows are allowed and there is no
modular reduction. Then for every integer n ≥ 48³, m ≤ n + 2n^{2/3} + 3n^{1/3}.
The bound is uniform over sequences and needs no a-priori assumption on m.

**Re-derived (proved):**
- **Kernels.**
  - H = (T₁T₂)^{−1/2}1_[0,T₁](x)h(y/T₂) has autocorrelation f₁(x/T₁)f₂(y/T₂).
    I computed this.
  - The kernel is PD and nonnegative.
  - Cauchy–Schwarz holds for signed measures through the L² representation.
- **Exact marginal.**
  - Put ν = λ⊗ρ with λ = Σ_jδ_j. Then E(μ,ν) = Σ_{i,j} f₁((i−j)/T₁)·1 = Λ
    exactly. This uses y_j ∈ [0,n] and potential 1 there, which needs T₂ ≤ n.
  - E(ν,ν) = Λ·C_L.
  - Λ ≥ m > 0 (diagonal 1, all terms ≥ 0), so dividing Λ² ≤ E(μ,μ)ΛC_L by Λ is
    legitimate. C_L ≥ 1/a > 0 also holds.
- **(6).** Off-diagonal ordered differences are distinct with nonzero first
  coordinate. For integer T₁, Σ_{d≠0}f₁(d/T₁) = T₁−1 exactly, and
  Σ_e f₂(e/T₂) ≤ T₂ + 4/3.
- **(7).** For integer 1 ≤ T₁ ≤ m: Λ = m + 2Σ_{d<T₁}(m−d)(1−d/T₁) = mT₁ − (T₁²−1)/3.
  I recomputed this by hand.
- **§5.**
  - T₂ = x² and U = ⌈2x²⌉ satisfy U ≤ 2x²+1 ≤ n. The case m < U is trivial
    because then m < n.
  - (8): x²(3/4)^x is decreasing for x > 2/α, and 200·48²(1/9)⁶ < 1.
  - (9) follows by dividing by U. aC/U ≤ q < 1/2.
  - In the right-side bound, C(x²+a)/U ≥ x³/(2x²+1) ≥ x/2 − 1/(4x).
  - B(x) expands correctly.
  - The identity 36x³[Y(1−q)−B] = 14x⁴−184x³−81x²−96x−72 is consistent with my
    hand computation of the leading term (7/18)x. The x² terms cancel exactly,
    which is why the coefficient 2 is attained. The shifted form has positive
    coefficients.
  - The coefficient 2 is the optimum of σ/3 + 4/(3τσ) + 2τ/3 at τ = 1, σ = 2,
    i.e. T₂ = x² and T₁ = 2x². I derived this independently.

**Numerical tests (not proof):**
1. **Exhaustive maximum sonar sequences for n = 1..10** (node DFS; 1.4·10⁸
   nodes at n = 10). The maxima were m(n) = 2, 4, 6, 8, 9, 11, 12, 13, 14, 16.
   On ≤ 200 maximum sequences per n, every integer T₁ ≤ m and 12 values of T₂,
   I ran 79,224 tests:
   - (7) against the direct Λ;
   - Λ ≥ m;
   - (6);
   - the core Λ ≤ E·C(n/T₂) with the measured C;
   - (S) with both the proof's C and the measured C.

   There were 0 violations; the largest core ratio was 0.887.
2. Quadratic sequences y_i = i² mod p (m = p+1, n = p) and exponential sequences
   y_i = g^i − 1 mod p (m = p, n = p−1), p ≤ 199, both verified sonar by
   brute force: 825 tests, 0 violations, largest core ratio 0.93. Quadratic
   sequences with p = 997, 2003, 4001 at the near-optimal scales T₂ ≈ x² and
   T₁ ≈ 2x²: 0 violations, largest core ratio 0.96.
3. **Final bound.** I took the exact largest m allowed by (S) at the proof's
   T₁ and T₂, with the 200-term kept, at n = 110592, 110593, 110600, 1.2·10⁵,
   10⁶, …, 10¹⁵. It was always < Y(x). The slack (Y−m)/x is 0.311 at onset and
   tends to 7/18 ≈ 0.389, as the identity predicts. The onset is not far from
   sharp for this method: the bound already fails at n = 27,000.
4. Checker vacuity, as noted above: on the `check_sonar.js` grid the largest
   value of Λ/(upper·C_proof) is 0.064. With C = L+2/3 it would be 0.61. Those
   checks test (7) and (6) but not the capacity step.

**Not checked:** fidelity to the EGRT model beyond the definition as written,
and whether 2n^{2/3} improves the literature.

---

## 4. KERNEL_PERTURBATION.md §§1–2 and KERNEL_FUNCTIONAL.md — verdict PASS

**Exact statement checked.** The class is real, even, nonnegative, integrable
positive-definite f with ∫f = 1. Write J(f) = f(0)∫|x|f.

f₀ is the half-cosine autocorrelation, with h = (π/2)sin(πx) on [0,1],
a₀ = π²/8 and M₀ = 1/4. Put δ = 1/16, θ = 10⁻⁷ and
f_θ = f₀ + θ[b_δ(·−2) + b_δ(·+2) − 2b_δ], where b_δ = δ^{−1}f₀(·/δ).

Claims: f_θ is in the class, and J(f_θ) = (π²/32)R with R = 1 − (129/8)θ − 508θ² < 1.

**Re-derived (proved):**
- **f₀ closed form.** f₀(x) = (π²/8)(1−|x|)cos(πx) + (π/8)sin(π|x|) on |x| ≤ 1.
  I derived this by hand. On |x| ≤ δ, f₀ ≥ a₀(1−δ)cos(πδ) ≥ (465/512)a₀.
- **Pointwise sign.** The subtracted mass is ≤ 2θ·16a₀ = 32θa₀ < a₀/2. The added
  bumps are supported in [31/16, 33/16] and are disjoint from [−1,1]. So f_θ ≥ 0
  everywhere.
- **Moments.**
  - The mass is unchanged.
  - f_θ(0) = a₀(1−32θ).
  - ∫|x|b_δ(x∓2) = 2 exactly, since the support avoids 0, and ∫|x|b_δ = δ/4.
  - So M = 1/4 + (4 − 1/32)θ = 1/4 + (127/32)θ, and aM = (π²/32)(1 − (129/8)θ − 508θ²).
- **Fourier side.**
  - ĥ = e^{−πiξ}cos(πξ)/(1−4ξ²) and f̂₀ = cos²(πξ)/(1−4ξ²)².
  - |ĥ| ≤ min(1, 1/(2ξ²)), because the distributional h″ has total variation
    π² + π² = 2π² and h is continuous at both endpoints.
  - The translates give f̂_θ = f̂₀ − 4θ sin²(2πξ) f̂₀(δξ).
  - The ratio identity is 16θ sin²(πξ)(1−4ξ²)² f̂₀(δξ).
  - The split bound at ξ² = 1/(2δ²) gives ≤ (1+2/δ²)². Above the split it is
    ≤ 4/δ⁴ ≤ (1+2/δ²)².
  - So θK = 0.421 < 1. At the zeros ξ = k+1/2 (|k| ≥ 1), sin²(2πξ) vanishes to
    the same order, and continuity covers them. f̂_θ is integrable (ξ⁻⁴ decay), so
    Bochner and inversion give positive definiteness.
- **KERNEL_FUNCTIONAL.**
  - **K1:** M = 2∫F(1−F), Cauchy–Schwarz and the substitution u = F give
    (π/8)², so aM ≥ π²/32. Equality holds for the sine density.
  - **K2:** with g = f(·/a)/a: 0 ≤ g ≤ 1, ĝ ≥ 0, and B̂(3/2) = −2/(3π). This
    gives ‖g−B‖₁ = 2m ≥ 2/(3π). The two rearrangement bounds are each ≥ m²/4, so
    D ≥ m²/2 ≥ 1/(18π²).
  - Consistency: K1 together with P2 shows that f_θ has no nonnegative
    autocorrelation factor, as the files say.
  - Optional technical remark on K2: if f is not assumed continuous, use the
    Riesz decomposition (f = continuous PD + PD null function). This only
    increases f(0), so K2 is unaffected.

**Numerical tests (not proof):**
1. The f₀ closed form against the direct autocorrelation (mpmath quad) agrees to
   20 digits at x = 0, 0.1, 0.37, 0.8, 0.999. ĥ against direct quadrature agrees
   to 10⁻¹⁷. The bound |ĥ| ≤ min(1, 1/(2ξ²)) held at the sampled points.
2. J by quadrature (40 digits) equals the closed form (π²/32)R to all printed
   digits for θ = 10⁻⁷, 5·10⁻⁷, 9·10⁻⁷. At θ = 10⁻⁷, J/(π²/32) − 1 = −1.6125·10⁻⁶.
   Mass = 1 and a, M match the claims.
3. **Fourier ratio sup (grid step 10⁻⁴ on [0,4000]).**
   - The supremum is 1.98·10⁶, attained near ξ ≈ 14.5.
   - The claimed K = 4,210,704 is a valid bound, about 2.1× loose. As ξ → ∞ the
     ratio tends to 16 sin²(πξ)cos²(πδξ)/δ⁴ ≤ 1.05·10⁶.
   - So the construction is admissible up to about θ* ≈ 5.05·10⁻⁷. At
     θ = 0.9θ* the grid minimum of f̂ is ≥ 0. At 1.2θ* there are 11,141
     negative grid values, and at θ = 10⁻⁵ there are many, so the positivity
     constraint really binds.
   - Near the zeros ξ = 1.5, 2.5, 7.5, 8.5, 23.5, 1000.5, 3999.5 the
     subtracted/f̂₀ ratio at θ = 10⁻⁷ stays between 10⁻⁴ and 0.10.
4. min f_θ on a 4.4·10⁵-point grid over [−2.2, 2.2] is 0, attained only outside
   the supports. On |x| ≤ 1/16 the minimum is 1.21.
5. Size of the effect: the largest J reduction in this one-parameter family is
   about 8·10⁻⁶ relative, near θ*. The result is a strict but tiny separation.

---

## 5. KERNEL_PERTURBATION.md §3 (P4) — verdict PASS-WITH-REPAIRS (editorial)

**Exact statement checked.** For every sonar sequence with n ≥ 160³:
m ≤ n + 3v n^{2/3} + 8n^{1/3}, where v = [(π²/36)R]^{1/3}.

**Re-derived independently.** I did not read SONAR_COSINE.md.
- **Product kernel.** The kernel is f_θ(x/T) ⊗ f₂(y/U) with real T. Its transform
  is the product of two nonnegative integrable transforms, so energy
  Cauchy–Schwarz holds for signed measures through the Fourier representation.
- **Λ_θ.** If (33/16)T ≤ m, the support of f_θ(·/T) lies inside |d| < m. Then
  Λ_θ = mΣ_d f_θ(d/T) − Σ|d|f_θ(d/T).
- **Riemann-sum variation.** |Σ_d g(d/T) − T∫g| ≤ Var(g) is proved
  cell-by-cell.
  - Var f_θ ≤ 2a₀ + 128θa₀ < 3.
  - Var(|x|f_θ) ≤ 2 + θ(6 + 132a₀) < 3. This uses Var(|x|f₀) = 4·max x f₀(x),
    which is ≈ 1.002 ≤ 2. Var(|x|b_δ) is dilation-invariant, and the shifted
    bumps are bounded by ∫ + sup|x|·Var.
  - Hence Λ_θ ≥ m(T−3) − MT² − 3T and Λ_θ ≥ ma > 0.
- **Energy.** E ≤ (4a/3)m + (T+3−a)(U+4/3) ≤ (4a/3)m + (T+2)(U+4/3). Dividing by
  T gives P5.
- **Scales.**
  - With t₁ = v/M and t₂ = 3v/2: Mt₁ = (2/3)t₂ = (4a/3)/(t₁t₂) = v. Checked in
    mpmath: all three equal 0.649629165776307.
  - The brackets 3/5 < v < 2/3, 9/5 ≤ t₁ ≤ 8/3 and 9/10 ≤ t₂ ≤ 1 hold.
  - (33/16)T ≤ (11/2)x² ≤ n ≤ m in the nontrivial case, and U ≤ n.
- **Exponential term.** ε = 200e^{−αx/t₂} ≤ 200(3/4)^x because t₂ ≤ 1.
  x⁴(3/4)^x is decreasing for x > 4/α. At x = 160, (3/4)^{160} < ((3/4)⁴)^{40} < 2^{−40}
  and 200·160⁴ < 2⁴⁰. So ε ≤ x⁻⁴.
- **Expansion.** I redid u = v/x + d/x² + eε/x² with d ≤ 565/243 and e ≤ 80/81.
  The right side expands term by term as:
  - the linear coefficient 8/(9v) + 2/t₁ ≤ 70/27;
  - the constants 35/9 + 2M ≤ 41/9;
  - three further terms, each < 1;

  This gives R_upper = x³ + 2vx² + (70/27)x + 8.
- **Final step.** Y·u expands as vx² + (d+3v²)x + 3vd + 8v + 8d/x + eε(x+3v+8/x),
  which gives the margin (29/27)x − 22 > 0.

**Numerical tests (not proof):**
- The largest |Σ_d f_θ(d/T) − T| over T ∈ [0.5, 3000] was 0.73 ≤ 3. The largest
  (Σ|d|f_θ(d/T) − MT²)/T was ≈ −10⁻⁴ ≤ 3.
- The chain (Λ_θ lower bound, energy upper bound, core Λ_θ ≤ E·C) was tested on
  exhaustive maximum sonar sequences for n ≤ 10 and on quadratic sequences up to
  p = 997: 5,592 tests, 0 violations, largest core ratio 0.93.
- The exact P5 bound (200-term kept) is below Y at x = 160, 161, 200, …, 10⁶.
  The slack (Y−m)/x is 2.95 at onset and tends to about 3.02.
- 3v = 1.948887497, against the nonnegative-factor value
  3(π²/36)^{1/3} = 1.948888545. P4 is in fact numerically below SONAR (1) for
  every x > 5/(2−3v) ≈ 97.8, so throughout its range. The file's disclaimer is
  conservative.

**Repairs (editorial; the mathematics does not change):**
1. §3 says "the same signed-product-certificate argument as in SONAR_COSINE.md"
   and "the same uniform tail proof as C6". The label C6 is not defined in the
   reviewed files. Inline the two facts the proof needs:
   - the Fourier-representation Cauchy–Schwarz for f_θ⊗f₂ with exact marginal
     λ⊗ρ, including Λ_θ ≥ ma > 0 before cancelling;
   - ε ≤ 200(3/4)^x ≤ x⁻⁴ for x ≥ 160, using t₂ ≤ 1, monotonicity of x⁴(3/4)^x
     for x > 4/α, and (3/4)^{160} < 2^{−40}.
2. State explicitly that Var(|x|f₀) = 4 max_{[0,1]} x f₀(x) ≈ 1.002 and that
   x f₀ is unimodal on [0,1]. The current text asserts "at most 2" without
   proof. The fact is true; I verified it numerically, and it is easy to prove,
   e.g. from x f₀(x) ≤ x(π²/8 + π/8) on [0,0.3] together with monotonicity of f₀.
3. Optional: say plainly that the improvement in the coefficient is
   ≈ 1.05·10⁻⁶ in absolute terms. It is a strict separation, not a practically
   better bound.

---

## What is proved versus what is only checked

- **Proved (re-derived by hand, line by line):**
  - (M1) for real r ≥ 160³;
  - (B1) for d ≥ 2 and x ≥ max{120, 4d};
  - SONAR (1) for integer n ≥ 48³;
  - admissibility of f_θ and J(f_θ) = (π²/32)R < π²/32;
  - P4 for n ≥ 160³;
  - K1 and K2.

  Every one of these rests on COMMON_CAPACITY Lemmas 2–6, which I also
  re-derived.
- **Only numerically checked:**
  - the measured values C_L ≈ L+2/3;
  - the finite-configuration tests;
  - the Fourier positivity grid and the numerical threshold θ* ≈ 5.05·10⁻⁷;
  - the final-bound slack tables;
  - the extremal values of m(r), Sidon maxima and m(n) from my own searches,
    which were not independently cross-checked.
- **Not checked:**
  - source and definition fidelity (BEMP, arXiv 1405.4227, EGRT);
  - novelty and priority against the literature;
  - SONAR_COSINE.md and the cosine sonar theorem it contains;
  - Lean formalisation (none exists);
  - whether the explicit constants (9, 2d², 3, 8) or onsets are near optimal.
    They are not claimed to be. The measured slacks show the proofs have room to
    spare.
