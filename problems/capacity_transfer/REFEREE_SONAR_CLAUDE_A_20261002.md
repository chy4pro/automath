# Referee report A: explicit cosine-kernel bound for sonar sequences

Referee: Claude (same-vendor reviewer, adversarial brief), 2026-10-02.
Material reviewed: `problems/capacity_transfer/SONAR_COSINE.md`, `COMMON_CAPACITY.md`,
`KERNEL_FUNCTIONAL.md`, `check_sonar_cosine.js` (same directory). No other repository file
was read, and the web was not consulted. Novelty and priority were **not** checked.

This is a same-vendor review. It is not a cross-vendor review and it is not a kernel
(Lean) formalisation.

## 0. Verdicts

| Item | Verdict |
|---|---|
| Main theorem (C1): for every integer n ≥ 160³ and every sonar sequence with n rows and m columns, m ≤ n + 3(π²/36)^{1/3} n^{2/3} + 4 n^{1/3} | **PASS.** Every step was re-derived and no mathematical gap was found. The editorial repairs R1 and R4 below are optional and do not affect validity. |
| Side claim in SONAR_COSINE line 11 ("KERNEL_FUNCTIONAL.md proves the matching coefficient barrier 3(π²/36)^{1/3}") | **NEEDS REPAIR (wording / overclaim).** See R2. This claim is not part of C1. |
| Capacity lemma as used (ν_L with potential 1 on [0,L] and E(ν_L,ν_L) ≤ L + 2/3 + 200e^{−αL}, L ≥ 1) | **PASS.** COMMON_CAPACITY.md contains a complete, self-contained proof; it is not merely a citation. |
| KERNEL_FUNCTIONAL (K1): aM ≥ π²/32 for f = h∗h̃ with h ≥ 0, h ∈ L¹∩L², ∫h = 1, with equality exactly for the sine density and its translates/dilates | **PASS.** |
| KERNEL_FUNCTIONAL (K2): aM ≥ 1/4 + 1/(18π²) for all nonnegative, positive-definite, integrable, unit-mass even f; hence the bracket 1/4 + 1/(18π²) ≤ inf ≤ π²/32 | **PASS.** Minor regularity wording; see R5. |
| KERNEL_FUNCTIONAL: "sonar method coefficient is 3[(aM)(a_y b_y)]^{1/3}" and "optimal vertical scalar boundary product 8/9" | **NOT PROVED in the reviewed files.** The first is correct only as the leading-order AM–GM optimum of the specific inequality template (C5). The optimality of 8/9 is asserted but not proved. See R2. |
| KERNEL_FUNCTIONAL §3 (exploratory grid; signed-factor rejection) | Correctly labelled exploratory. The signed-factor rejection (lag-1/2 value −3/(50π)) is **confirmed**. The reported grid outcome was **reproduced**. |
| check_sonar_cosine.js | Runs and prints PASS (16 exact rational checks). Its scope is only the rational envelopes, the endpoint arithmetic and the final margin. It does not check the algebraic expansion, which I checked separately with sympy. |

**Most serious issue.** C1 itself has no mathematical defect. The most serious problem is an overclaim
in surrounding text: the "matching coefficient barrier" (SONAR_COSINE line 11 and
KERNEL_FUNCTIONAL §1–2) depends on an unproved optimality claim for the vertical product
a_y b_y = 8/9. It also depends on an informal notion of "the method". It must be reworded before any external use.

## 1. Definition check

The file defines the objects as follows. y_0,…,y_{m−1} ∈ {0,…,n−1}, so m is the number of columns and n the number of rows. Exactly one dot per column. All ordered displacement vectors (i−j, y_i−y_j), i ≠ j, are distinct. Equality of values is allowed. The condition is non-modular.

- This matches the standard (non-modular) sonar condition of Erdős–Graham–Ruzsa–Taylor and Golomb–Taylor as I recall it: an array with one dot per column whose difference vectors are distinct. Equivalently, for each h > 0 the differences y_{i+h} − y_i are distinct. I checked this from memory only; I did not consult the original paper.
- Equivalence with "positive first coordinate distinct" holds, because (d,e) ↦ (−d,−e) is a bijection between the d > 0 and d < 0 halves.
- Modular sonar sequences, where differences are taken mod m, satisfy a stronger condition. They are therefore covered by C1.
- **Ambiguity to flag for any public statement.** Some sources write "m × n" with the roles of rows and columns described differently. The theorem is unambiguous only because the file fixes the convention: m = length = columns, n = alphabet size = rows. Keep this explicit.

## 2. Main theorem: step-by-step re-derivation

I derived each step on paper first and then compared it with the author's text.

1. **Closed form of g = h∗h̃, with h = (π/2)sin(πx) on [0,1].** For 0 ≤ s ≤ 1, g(s) = (π²/4)∫_0^{1−s} sin(πt)sin(π(t+s))dt. Use sin A sin B = ½[cos(A−B) − cos(A+B)]. Then ∫_0^{1−s}cos(π(2t+s))dt = [sin(π(2−s)) − sin(πs)]/(2π) = −sin(πs)/π. This gives g(s) = (π²/8)[(1−s)cos(πs) + sin(πs)/π] = (π²/8)(1−s)cos(πs) + (π/8)sin(πs). **Agrees.** It was also checked numerically against the defining integral (error < 2·10⁻³⁴ at 40 digits).
2. **g(0) = π²/8; mass = (∫h)² = 1, since ∫h = 1.** g ≥ 0 because it is the autocorrelation of a nonnegative function. g′(s) = −(π³/8)(1−s)sin(πs) ≤ 0 on [0,1]. g(1) = 0, so g is continuous at ±1. **Agrees.**
3. **M = ∫|s|g = 1/4.** Using F = (1 − cos πx)/2, M = 2∫F(1−F) = 2∫sin²(πx)/4 = 1/4. This was confirmed by direct quadrature. **Agrees.**
4. **Positive-definiteness of G(x,y) = g(x/T)f(y/U).** g(x/T) is the autocorrelation of k(t) = T^{−1/2}h(t/T). f(y/U) is the autocorrelation of U^{−1/2}h_f(y/U), where h_f is the ramp. G is therefore the autocorrelation of the L²(ℝ²) function K = k ⊗ k_f. Then E_G(μ,ν) = ∫(K∗μ)(K∗ν) for finite signed measures. This holds by the same Fubini argument as COMMON_CAPACITY Lemma 2, since K ∈ L² and |K∗μ|₂ ≤ ‖μ‖_TV‖K‖₂. Cauchy–Schwarz in L² follows. **Signed test measures are legitimate**: no positivity of ρ is used.
5. **Mixed energy.** E_G(μ, λ⊗ρ) = Σ_i Σ_j g((i−j)/T)·∫f((y_i−y)/U)dρ(y). Here ∫f((y_i − y)/U)dρ(y) = V_{n/U}(y_i/U), where ρ is the pushforward of ν_{n/U} under y ↦ Uy. V_L = 1 on the closed interval [0,L], and y_i/U ∈ [0,(n−1)/U] ⊂ [0,n/U]. Hence the mixed energy is exactly Λ = Σ_{i,j} g((i−j)/T). Endpoints are covered, and dilation is handled correctly. **Agrees.**
6. **Self-energy.** By Fubini (bounded kernel, finite total variation), E_G(λ⊗ρ, λ⊗ρ) = Λ·E_f(ν_{n/U}, ν_{n/U}). Dilation invariance holds. **Agrees.**
7. **(C2).** Λ² ≤ E_G(μ,μ)·Λ·E_f(ν,ν). Here Λ ≥ m·g(0) > 0 by g ≥ 0, so dividing gives Λ ≤ E_G(μ,μ)E_f(ν,ν). Then E_f(ν,ν) ≤ C(n/U) by (4.7), and E_G(μ,μ) ≥ 0. This needs n/U ≥ 1. **Agrees.**
8. **Lattice sums for an even, nonnegative, unit-mass w that decreases on [0,∞).** Σ_{d≥1}w(d/T) ≤ T/2 ≤ Σ_{d≥0}w(d/T). This gives T − w(0) ≤ Σ_ℤ w(d/T) ≤ T + w(0) and Σ_{d≠0} w(d/T) ≤ T. **Agrees.** Both g and f are of this type (f′ = −2 + 2x² ≤ 0 on [0,1]).
9. **Total variation of p(s) = |s|g(s).** On (0,1), p′ = g + sg′. ∫_0^1 s(−g′) = [−sg]_0^1 + ∫_0^1 g = 1/2, so ∫_0^∞|p′| ≤ 1/2 + 1/2 = 1, and Var(p) ≤ 2. The actual one-sided value is 0.5009. Partition ℝ into cells [d/T,(d+1)/T). Then |p(d/T) − T∫_cell p| ≤ Var_cell(p), and summing gives |Σp(d/T) − TM| ≤ 2. Hence Σ|d|g(d/T) = TΣp(d/T) ≤ MT² + 2T. **Agrees.**
10. **(C3).** Λ = Σ_{|d|<m}(m−|d|)g(d/T). If T ≤ m, the terms with |d| ≥ m vanish, so the identity with full ℤ-sums is exact. *Remark:* the hypothesis T ≤ m is not needed for the inequality, because the extra terms (m − |d|)g(d/T), |d| ≥ m, are ≤ 0. Then Λ ≥ m(T − a) − MT² − 2T. **Agrees.**
11. **(C4).** The diagonal contributes m·g(0)f(0) = a·a₂·m. The off-diagonal ordered pairs (i,j) ↦ (i−j, y_i−y_j) form an injective map into (ℤ∖{0})×ℤ, by the sonar property. Each vector is counted at most once, and all summands are ≥ 0. So the off-diagonal part is ≤ (Σ_{d≠0}g(d/T))(Σ_e f(e/U)) ≤ T(U + a₂). No dropped term has the wrong sign. **Agrees.**
12. **(C5).** Combine m(T−a) − MT² − 2T ≤ Λ ≤ E_G·C ≤ C(aa₂m + T(U+a₂)) and divide by T > 0. The result is linear in m. It uses no a priori bound on m, so the argument is **not circular**. **Agrees.**
13. **Scales.** x = n^{1/3}, v = (π²/36)^{1/3}, T = 4vx², U = (3/2)vx². These are the AM–GM stationary point of MT + bU + aa₂n²/(UT), which I re-derived with sympy; each of the three terms equals vx². a = (9/2)v³ = π²/8 was checked symbolically.
14. **Bounds on v and α.** From 3 < π < 22/7 we get 1/4 < v³ < 0.2744. Hence 3/5 < v < 2/3, so (3/2)v ≤ 1 and n/U = x/((3/2)v) ≥ x ≥ 160 ≥ 1. The statement α = log(4/3) ≥ 1/4 is true, since (4/3)⁴ = 256/81 > 3 > e, but **it is not justified in the text** (R1).
15. **Applicability of the scales.** T ≤ (8/3)x² ≤ x³ = n ≤ m in the case m ≥ n. U ≤ x² ≤ n. At x = 160, T ≈ 66 522, U ≈ 24 946 and L = n/U ≈ 164.2. **Agrees.** The case m < n is trivial.
16. **(C6).** ε = 200e^{−αn/U} ≤ 200e^{−x/4}. The function x⁴e^{−x/4} decreases for x ≥ 16. At the endpoint, 200·160⁴ = 131 072 000 000 < 2⁴⁰ < e⁴⁰. This proves ε ≤ x^{−4} for **every real** x ≥ 160. **Agrees.**
17. **Algebra.** I recomputed 1−u, R and the full expansion of Y(1−u) − R symbolically in sympy, with v, x, ε treated as free symbols. All three **match the file exactly**. The bounds 13/54 (the coefficient of x), 67/9, 4d/x ≤ 1 and the ε-bracket < 1 were each re-derived. Each uses only monotone substitutions (v² ≤ 4/9, 1/v ≤ 5/3, d ≤ 17/18, ε ≤ x^{−4}), and every ε-term carries a negative sign. These substitutions are valid for all x ≥ 160, not just on a grid. Also 0 < u < 1/2. Since 1 − u > 0 and Y(1−u) − R ≥ 13x/54 − 85/9 > 0, C5 gives m(1−u) ≤ R < Y(1−u), so m < Y. **Agrees.**
18. **"Coefficient < 2".** 3v < 2 ⇔ π² < 32/3, which follows from (22/7)² = 484/49 < 32/3. **Agrees.** For reference, 3v = 1.94888854486…

## 3. Capacity lemma (COMMON_CAPACITY.md), as used

The file reproduces the full proofs (Lemmas 2–6); it is not a bare citation. I checked every inequality that the sonar proof uses.

- **Ramp kernel.** f = h∗h̃ with h = 2(1−t)1_[0,1]. The closed form 4/3 − 2|x| + (2/3)|x|³ was verified analytically and by quadrature. f(0) = 4/3 and mass 1. f is monotone on [0,∞). The signed-measure Cauchy–Schwarz (2.5) is valid via h∗μ ∈ L².
- **Lemma 3.** h/2 = H − U∗H, the telescoping identity (3.4), and the bound U^{∗(m+1)}∗H(t) ≤ t^{m+1}/(m+1)! together give h∗g₊ = H. Then f∗g₊ = h̃∗H = 1 on [0,∞), including x = 0. Associativity holds by Tonelli for nonnegative terms. **Correct.**
- **Lemma 4.** I re-derived the delay equation u′ = u(t) − u(t−1), the kernel K_x(y) = e^x − 1_{y≤x}e^{x−y} (nonnegative, mass 1, ≥ 1/2 on [1/2,1]), the 3/4-contraction and c = 2. **Correct.** Numerically, the maximum of |u−2| / ((e−1)(3/4)^{⌊t⌋}) over t ∈ [0,25] is 0.582 ≤ 1. The true decay is much faster: |u−2| ≈ 1.2·10⁻⁹ at t = 10.
- **Lemma 5.** ‖q‖_TV ≤ 9/2; numerically it is 0.790. The tail bound uses 4(3/4)^{⌊L⌋} ≤ (16/3)e^{−αL}. q(ℝ) = 1/3 by the Laplace-transform argument; the renewal second-moment formula independently gives ½·(μ₂/(2μ₁²)) = 1/3. Numerically, q(ℝ) − 1/3 = −4·10⁻²⁹ with truncation at t = 30. **Correct.**
- **Lemma 6, (4.4)–(4.7).** ν_L = g₊ + g₋^L − dt as locally finite measures. The potential is V_L = 1 + 1 − 1 = 1 on the closed interval [0,L]. |V_L| ≤ 13. The mass outside [0,L] is ≤ 12e^{−αL}, so |E(ν_L,ν_L) − (L+2/3)| ≤ 168e^{−αL} ≤ 200e^{−αL} for L ≥ 1. **Correct.**
- **Constants used by SONAR_COSINE.** a₂ = 4/3, b = 2/3, α = log(4/3), C(L) = L + 2/3 + 200e^{−αL} for L ≥ 1. All are **consistent** with the lemma.

## 4. KERNEL_FUNCTIONAL.md

- **K1 (proved).** M = ∫∫|x−y|h(x)h(y) = 2∫F(1−F), by the threshold identity and Tonelli for h ≥ 0. Cauchy–Schwarz with u = F(x) is valid: F is absolutely continuous and monotone, and the change of variables holds for continuous φ. ∫_0^1 √(u(1−u))du = π/8, which gives aM ≥ 2(π/8)² = π²/32.
  - *Equality.* C–S equality forces h = c√(F(1−F)) a.e. Note that h = 0 a.e. where F ∈ {0,1}. On the open interval {0<F<1}, arcsin(2F−1) is locally absolutely continuous with derivative c. This gives the sine density on one interval, unique up to translation and dilation. The argument is complete.
  - *Class.* h ≥ 0, h ∈ L¹∩L², ∫h = 1; M = ∞ is allowed. **PASS.**
  - *Random test.* 3000 random nonnegative h (four families, including perturbations of the sine) gave minimum aM = 0.308433, against π²/32 = 0.308425. No violation.
- **K2 (proved).**
  - Normalize so that g(0) = 1 and ∫g = 1. Then 0 ≤ g ≤ 1, and ĝ ≥ 0 by Bochner.
  - B̂(3/2) = −2/(3π), checked numerically. So ‖g − B‖₁ ≥ 2/(3π), ‖g − B‖₁ = 2m and m ≥ 1/(3π).
  - The decomposition of D into the two distance-weighted integrals is correct.
  - The bathtub / layer-cake bound gives each integral ≥ ∫(m−2s)₊ds = m²/4. The inner strips fit because m ≤ 1. Hence D ≥ m²/2 ≥ 1/(18π²). **PASS.**
  - Regularity: f should be taken continuous so that f(0) and the 2×2 positive-definite matrices are meaningful. This is standard (a measurable positive-definite function agrees a.e. with a continuous one), but it should be stated (R5).
- **Bracket.** 0.255629 ≤ inf ≤ 0.308425 is valid and correctly stated as not closing.
- **"Barrier" statements (not proved here).** The formula "second-order coefficient 3[(aM)(a_y b_y)]^{1/3}" is the AM–GM minimum of the three leading terms of the C5 template. That makes it a statement about this particular inequality, not a lower bound for every possible kernel-energy argument. "Optimal vertical scalar boundary product 8/9" has no proof in the reviewed files. Consequently, "matching coefficient barrier 3(π²/36)^{1/3}" (SONAR_COSINE line 11) holds only conditionally: for the C5 template with the ramp vertical certificate fixed and horizontal kernels of the form h∗h̃ with h ≥ 0. The same caveat applies to the full-class "barrier" 3[(8/9)(1/4+1/(18π²))]^{1/3}.
- **Remark "a general nonnegative positive-definite f need not be supplied with such a factor".** This is plausible and harmless, but no example or proof is given. Label it as a remark (R6).
- **§3 exploratory.**
  - Signed factor: I recomputed the lag-1/2 autocorrelation analytically as (A²/2 + AB − B²/6)/π with A = 1−e, B = 3e. This equals (1/2 + 2e − 4e²)/π, which is −3/(50π) at e = −1/5; confirmed numerically. The checker's J = (1−2e+10e²)(1+2e−2e²) equals aM/(π²/32) for this family; checked at e = −1/5, −3/20 and 1/10.
  - Grid: I re-ran the family f_cos(1 + λcos ωx) with λ ∈ {k/20}, ω ∈ {k/4 ≤ 40}, using adaptive quadrature. No value fell below π²/32. The small-ω directional derivative is proportional to σ² − E|X|³/(2M) = +0.0066 > 0, so this family cannot beat the cosine kernel near ω → 0.

## 5. Numerical tests actually run

All tests used Python with numpy/scipy/mpmath/sympy, ≤ 2 threads and no SAT/ILP solver, plus node for the author's checker. Total compute was a few CPU-minutes. The scripts were run in a scratch area and are not committed.

1. **Author's checker.** `node check_sonar_cosine.js` printed PASS with 16 exact rational checks.
2. **Kernel identities** at 40 digits: the closed form of g, g(0), mass, M = 1/4, g′, Var(p) on [0,1] = 0.5009, ∫√(u(1−u)) = π/8, aM = π²/32, the ramp f closed form, f(0), mass, and a₂b = 8/9. All agree.
3. **Capacity lemma.**
   - u was computed from the classical renewal-density formula u(t) = Σ_{k≤⌊t⌋}(−1)^k e^{t−k}[(t−k)^k/k! + (t−k)^{k−1}/(k−1)!]. Its values u(0) = 1, u = e^t on [0,1) and u(1) = e−1 match (3.6). The integral equation (3.8) holds to 4·10⁻⁵⁸.
   - ν_L was built on a grid with step 1/4000, including the two half-atoms. Over L ∈ {1, 1.5, 2, 3, 5, 8, 12, 20}:
     - ν_L(ℝ) − (L + 2/3) = −4·10⁻¹⁰;
     - max |V_L − 1| on [0,L] ≤ 3·10⁻⁸, endpoints included;
     - E(ν_L,ν_L) − (L+2/3) = +8.2·10⁻³ at L = 1, −1.2·10⁻³ at L = 1.5, and ≤ 4·10⁻⁷ in absolute value for L ≥ 5.
   - These errors are far inside 200e^{−αL}. In the sonar application L ≥ 164.
4. **Universal lattice lemmas**, for 1000+ values of T ∈ [0.05, 66530]: Σg ∈ [T−a, T+a], Σ_{d≠0}g ≤ T, Σ|d|g ≤ MT² + 2T, |Σp − TM| ≤ 2 (the actual maximum error is 0.27), and Σf ∈ [U−a₂, U+a₂]. **No violation.**
5. **Real sonar sequences.** The sonar property was verified by brute force before each test.
   - Families tested:
     - quadratic y_i = i² mod p, i = 0..p (m = p+1, n = p), for p ∈ {5, 7, 11, 13, 31, 61, 101, 211, 401};
     - exponential y_i = gⁱ mod p − 1, i = 0..p−1 (m = p, n = p−1), for the same p;
     - the best of 200 randomized greedy sequences for n ∈ {6, 10, 20, 40, 80}.
   - For grids of (T, U) with n/U ≥ 1, I checked C3, Λ ≥ am, C4, C2 (with C(L)) and C5. **0 violations.**
   - With the numerically computed E(ν_L), the sharp form Λ ≤ E_G·E(ν_L) has minimum ratio E_G·E(ν_L)/Λ = 1.106 over these sequences.
6. **Cauchy–Schwarz step, non-sonar point sets.** This step does not use the sonar property, so I tested it more aggressively.
   - On 300 random and extreme configurations (constant rows, linear ramps, random), the minimum of E_G·E(ν_L)/Λ was 1.129.
   - I also minimised E_G over continuous y ∈ [0,n]^m with L-BFGS-B (12 random starts, 4 settings of (m,T,n), L ∈ {1,2,3,5}). The minimum ratio was 1.017. The floor is respected and nearly attained.
7. **Exhaustive search for n ≤ 8.**
   - DFS over all sequences, quotienting only by the reflection y ↦ n−1−y, gave these maximum m:

     | n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
     |---|---|---|---|---|---|---|---|---|
     | max m | 2 | 4 | 6 | 8 | 9 | 11 | 12 | 13 |
     | # maximal sequences | 1 | 3 | 6 | 2 | 11 | 4 | 23 | 222 |

   - On every maximal sequence I checked C2, C3, C4 and C5 for T ∈ {0.3,…,12} (including T > m) and L = n/U ∈ {1,…,8}. **0 violations** of any inequality that is claimed for all parameters. The minimum of E_G·E(ν_L)/Λ was 1.141.
   - C1 is not claimed for small n. It is nevertheless far from tight there; for example, at n = 8 the C1 expression is 23.8 while the true maximum is 13.
8. **High-precision final algebra.** At 60 digits, x ∈ {160, 160.5, 161, 170, 200, 300, 500, 10³, 10⁴, 10⁵, 10⁶}.
   - The exact Y(1−u) − R is positive at every sampled x and dominates the crude bound 13x/54 − 85/9: 67.76 vs 29.07 at x = 160, and 4.7·10⁵ vs 2.4·10⁵ at x = 10⁶.
   - The bound R/(1−u) obtained from C5 lies below Y by about 68 at the onset.
   - T ≤ n, U ≤ n, L ≥ x and ε ≤ x^{−4} were asserted at each sampled point; ε = 6.1·10⁻¹⁹ at x = 160.
   - *Observation, not a claim:* with the exact ε, Y(1−u) − R is already positive at x = 40, so the onset 160³ is conservative. The proof only needs it to be valid, which it is.

## 6. Repairs and recommendations

- **R1 (editorial, SONAR_COSINE §3).** Add one line justifying α = log(4/3) ≥ 1/4, for example (4/3)⁴ = 256/81 > 3 > e, with e < 3 as already shown in COMMON_CAPACITY Lemma 4.
- **R2 (wording; required before any external use).** Reword SONAR_COSINE line 11 and KERNEL_FUNCTIONAL §1 (last paragraph) and §2 (last paragraph). The text should say that 3(π²/36)^{1/3} is the best leading coefficient obtainable from the C5 template when the vertical certificate is the ramp (a₂b = 8/9) and the horizontal kernel is h∗h̃ with h ≥ 0. Either drop the word "optimal" for 8/9 or supply a proof. Do not call it a barrier for "the method" without a precise definition.
- **R3 (status line).** SONAR_COSINE line 1 says "the exact checker [is] pending", but the checker exists and passes. Update the line to record the actual review status: same-vendor referee A PASS; cross-vendor review and formalisation not done.
- **R4 (cosmetic).**
  - The symbol e = (3/2)v²ε collides with Euler's number.
  - The hypothesis T ≤ m in C3 can be dropped, because the extra terms are nonpositive. This would also remove the case split m < n.
  - Line 41 should say explicitly that the integrals are over (0,∞).
- **R5 (KERNEL_FUNCTIONAL §2).** State that f is taken continuous (the continuous representative of a positive-definite function) so that a = f(0), the 2×2 test and Bochner's theorem apply verbatim.
- **R6 (KERNEL_FUNCTIONAL §1).** Either label "a general nonnegative positive-definite f need not be supplied with such a factor" as an unproved remark, or give an example.

## 7. Not checked

- Novelty and priority. A G2 literature check is required before any claim. I did not search, and I make no claim about whether this coefficient is new or already superseded.
- The original EGRT definition and theorem statements, which I recalled from memory only.
- `check_sonar.js`, which SONAR_COSINE line 108 refers to. It was outside the permitted reading set.
- `SIDON_BOUND_PROOF.md`, the source that COMMON_CAPACITY says it copies. It was not read; COMMON_CAPACITY was reviewed as a standalone proof.
- Any Lean or kernel formalisation. None exists for this result.
- Optimality of the vertical certificate (a_y b_y = 8/9). No proof was available in the reviewed files.
