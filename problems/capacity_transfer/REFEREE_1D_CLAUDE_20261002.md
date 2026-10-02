# Cross-vendor referee report: weak Sidon, g-thin, difference triangle sets

Date: 2026-10-02. Referee: Claude (Opus 5.5), acting as an adversarial cross-vendor referee
of proofs written by GPT-6 Astra. This is a referee report, not a Lean formalisation and not a
novelty, priority or literature check.

Files reviewed (first 16 hex digits of SHA-256 at review time; all tracked, no local diff):

| file | sha256 prefix |
|---|---|
| `COMMON_CAPACITY.md` | `f787424ba9a1e64d` |
| `WEAK_SIDON.md` | `199822c7dfde70d7` |
| `G_THIN.md` | `6e04f6327a0959b5` |
| `DIFFERENCE_TRIANGLES.md` | `8777d65ae5aefd7c` |
| `check_weak_sidon.js` | `a5633d5280fd7bd6` |
| `check_g_thin.js` | `7158663cc6bcce09` |
| `check_difference_triangles.js` | `04fbd407d081d7da` |

I read no other repository files and did no web search for these results. I did not edit any
file under review.

## Verdict summary

| Theorem | Verdict | Remarks |
|---|---|---|
| Weak Sidon (W1) | **PASS** | Every step re-derived. The onset is tight but proved: the scalar margin at N = 90^4 is only about 0.083 (Section 1.4). Editorial notes E1 and E4 are optional. |
| g-thin (G1, diameter form, G11) | **PASS** | Every step re-derived. The `+O(k)` sentence after G11 has an unspecified constant. I suggest an explicit replacement (E2), which is optional because the file already calls G11 the explicit statement. |
| Difference triangle sets (D1, D2) | **PASS** | Every step re-derived, including the D11 remainder algebra. Editorial note E3 only. |

I found no false line, no missing case and no circular step. All three theorems depend on
Lemma 6 of `COMMON_CAPACITY.md`. I re-derived that lemma independently and checked it numerically
(Section 0). If it failed, all three results would fail together. That shared dependency is the
main structural risk. I found no defect in it.

---

## 0. Shared analytic input (COMMON_CAPACITY, Lemmas 2–6)

### 0.1 Steps re-derived by hand
1. **The kernel.** I computed f = h * h~ for h = 2(1−t) on [0,1]. This gives
   f(x) = 4/3 − 2|x| + (2/3)|x|^3 on [−1,1]. Also f(1) = 0, f'(x) = −2 + 2x^2 ≤ 0 on [0,1],
   f(0) = ||h||_2^2 = 4/3 and ∫f = (∫h)^2 = 1. The identity E(μ,ν) = <h*μ, h*ν>_{L^2} holds
   for finite signed measures, so Cauchy–Schwarz holds for signed certificates.
2. **The half-line identity.** H − U*H equals 1−t on [0,1] and 0 elsewhere, including at t = 0.
   This is h/2, so the series telescopes to h*g_+ = 1_{[0,∞)}. Hence
   f*g_+ = h~*(h*g_+) = ∫h~ = 1 for x ≥ 0. At x = 0 I also checked this in closed form:
   (1/2)f(0) + (1/2)∫_0^1 f(t)e^t dt = 2/3 + 1/3 = 1.
3. **The density u.** u = e^t on [0,1) and u(1) = e − 1 for the right-continuous version. The
   delay equation u(t) = ∫_{t−1}^t u holds for t ≥ 1. The kernel K_x(y) in (3.9) has mass 1, is
   nonnegative, and is at least 1/2 on [1/2,1] (e^{1/2} − 1 > 1/2). So the oscillation contracts by
   3/4 per unit interval. The limit is c = 2 because 1 = (1/2)∫h(s)u(t−s)ds tends to c/2.
4. **The mass of q.** q(R) = 1/3. I checked this independently with the renewal theorem for
   Uniform[0,1] steps: Σ_{n≥0}P(S_n ≤ t) = t/μ + E[X^2]/(2μ^2) + o(1) = 2t + 2/3 + o(1).
   Hence g_+([0,t]) − t → 1/3. This agrees with the Laplace computation in (3.15).
5. **The certificate.** ν_L = 1_{[0,L]}dt + q + q_L = g_+ + g_-^L − dt. Its potential on
   [0,L], including both endpoints, is 1 + 1 − ∫f = 1. Its mass is L + 2/3. The energy satisfies
   E(ν_L,ν_L) − (L+2/3) = ∫_{R∖[0,L]}(V_L − 1)dν_L, with |V_L| ≤ 1 + (4/3)·9 = 13 and
   |ν_L|(R∖[0,L]) ≤ 12e^{−αL}. The constants 9/2, 16/3 ≤ 6 and 168 ≤ 200 all check.
6. **Where L ≥ 1 is used.** It is needed only for the tail estimate (3.13). Every application has
   L much larger than 1: L = x/√6 ≥ 36.7 for weak Sidon and L = x/√2 ≥ 84.8 for g-thin and DTS.

### 0.2 Numerical checks (mpmath, 50 digits; numpy float64)
- **u.** I used the closed form u(t) = Σ_{k≤⌊t⌋}(−1)^k e^{t−k}[(t−k)^k/k! + (t−k)^{k−1}/(k−1)!].
  It agrees with the delay equation at sample points to below 1e−25.
- **Lemma 4.** I tested |u − 2| ≤ (e−1)(3/4)^{⌊t⌋} on t ∈ [0,40] with step 0.02. The largest
  ratio is 0.58, at t = 0. The true decay is much faster: |u(10) − 2| = 1.2e−9.
- **Lemma 3 and (4.5).** h*g_+ = 1 at 8 sample points, and |f*q − (1 − F)| ≤ 1.4e−51 on
  [0,6] with step 0.1. So f*g_+ = 1 on [0,∞) holds numerically.
- **The mass and tails of q.** q([0,40]) − 1/3 = −4.3e−30. Also ||q||_TV = 0.790, against the
  claimed 9/2, and |q|((L,∞)) is far below 6e^{−αL} for L = 1, 2, 5, 10, 20.
- **The energy of ν_L.** For L = 1, 2, 3 I computed V_L ≡ 1 on [0,L] and V_L ≡ 0 beyond L+1.
  The energy correction E(ν_L,ν_L) − (L+2/3) is +0.0082 at L = 1, −0.00020 at L = 2 and
  −0.00012 at L = 3. The proof allows up to 168e^{−αL} (126, 94 and 71). At L = 5, 8, 12 and 20
  the correction is at most 1e−6 in absolute value (see the appendix).
- **Signed capacity of finite point sets.** For any finite P ⊂ [0,L], Lemma 6 implies
  1ᵀF_P^{−1}1 ≤ C(L), because its proof also works for signed μ. I tested 47 lattices
  {j/T} with T from 0.7 to 20 and L from 1 to 80. I also tested uniform grids on [0,L]
  (L ≤ 40, spacing down to 0.01) and 300 random point sets. There were no violations. The
  largest value of s − C(L) was −0.060 on lattices and −0.31 on random sets.
  The grids converge to about L + 2/3 from below; Richardson extrapolation at L = 40 gives
  L + 2/3 − 1e−6. At L = 1 the grid value exceeds L + 2/3 by 0.0078, which agrees with the
  +0.0082 energy correction there. So L + 2/3 is essentially sharp, and the 200e^{−αL} slack is
  very generous.

---

## 1. Weak Sidon (`WEAK_SIDON.md`)

### 1.1 Exact statement and conventions
A ⊂ Z is weak Sidon if the sums a+b over unordered pairs {a,b} with a ≠ b are pairwise
distinct. Diagonal sums 2a are excluded, so 3-term progressions are allowed. The theorem says:
for every integer N ≥ 90^4 = 65 610 000 and every weak Sidon set A ⊆ {1,…,N},
|A| < √N + √(8/3) N^{1/4} + 2.

The interval is {1..N}. After translating by −1 the points lie in [0,(N−1)/T] ⊆ [0,N/T].
The energy counts ordered pairs, including all k diagonal pairs. r(d) counts ordered pairs
with x − y = d > 0, which equals the number of unordered pairs at distance d. I found no
mismatch between the definition in the file and the definition used in the proof. The
attribution to Balogh–Füredi–Roy §5 was not checked (literature).

### 1.2 Steps re-derived before reading the justification
1. **r(d) ≤ 2, and repeats come from 3-term progressions.** Take lower endpoints p < q for the
   same d. Then (p+d) + q = (q+d) + p. The pair {q+d, p} has distinct elements, and q+d exceeds
   both p+d and q, so the two pairs differ. If q ≠ p+d, the pair {p+d, q} also has distinct
   elements, which violates weak Sidon. So q = p+d. A third endpoint r would also need
   r = p+d, which is impossible.
2. **|P| ≤ k−2.** Different d, e ∈ P with the same middle z would give the distinct pairs
   {z−d, z+d} and {z−e, z+e} with the same sum 2z. A middle is never min A or max A. So the map
   from P to middles is injective into the interior of A.
3. **The energy bound (W5).** E = (4/3)k + 2Σ_d r(d)f(d/T), and r(d) ≤ 1 + 1_P(d). With f ≥ 0
   and f ≤ f(0) = 4/3, E ≤ (4/3)k + T + (8/3)(k−2) = T + 4k − 16/3 for k ≥ 2. The cases
   k ≤ 1 are trivial.
4. **The lattice sum.** f(d/T) ≤ T∫_{(d−1)/T}^{d/T} f because f is nonincreasing, so
   2Σ_{d≥1} f(d/T) ≤ 2T·(1/2) = T for every real T > 0. Monotonicity is used here.
   Nonnegativity is used to fill in the differences that do not occur.
5. **The scale.** T = √6 x^3 with x = N^{1/4}. T ≤ N ⟺ x ≥ √6, and L = x/√6 ≥ 36.7.
   T depends only on N, not on k, so no step is circular.
6. **Expansion (W7).** 4/√6 = (2/3)√6 = γ and γ^2 = 8/3. I re-expanded W6 by hand and got W7
   exactly. I also computed P_0(x^2 + γx + c) = (2c − γ^2)x^2 + γ(c − γ^2)x + c^2 − cγ^2. At
   c = 2 this is (4/3)x^2 − (2/3)γx − 4/3, which is W10.
7. **(W8) εx < 1/2 for all real x ≥ 90.**
   - log u ≥ 2(u−1)/(u+1), so α ≥ 2/7.
   - √6 < 49/20, so α/√6 ≥ 40/343.
   - x·e^{−40x/343} is decreasing for x ≥ 8.575.
   - The certificate (1957/720)^10·Q > 36000 was reproduced with Python integers: both printed
     integers match, and their ratio is 1.00336.
8. **(W11), (W12) and the conclusion.**
   - 8024/6075 > 13/10.
   - 49/40 + 1/45 + 1/2430 + 1/182250 = 1.24764 < 5/4.
   - Each bounding function is monotone in x, so the bounds hold for every real x ≥ 90, not
     just on a grid.
   - P_ε is monic with a negative constant term. P_ε(k) ≤ 0 and P_ε(y) > 0 then give k < y.

### 1.3 Numerical tests run
- **Exhaustive enumeration.** I enumerated all weak Sidon subsets of {0,…,40} (5 276 458
  sets), and every interval length N from 3 to 41 (24.4 million (set, N) instances). On each I
  checked:
  - r(d) ≤ 2;
  - each repeated d has exactly two lower endpoints, with q = p+d;
  - different repeated differences have different middles, and every middle is interior
    (6 935 784 repeat instances at N = 41);
  - |P| ≤ k − 2, with equality attained;
  - the exact integer form of E ≤ T + 4k − 16/3 at 12 rational scales T, including
    3/2, 5/2, 7/3, 11/2 and 19/2;
  - the sandwich k^2 ≤ C(N/T)·E.

  There were no violations. On these sets the sharper inequality k^2 ≤ (L + 2/3)E, without the
  exponential term and with L ≥ 2, also held: the minimum slack was 1.72.
- **My count against the author's.** My count of weak Sidon subsets of {0..13} is 2048. This
  matches the checker's number, which only coincides with 2^11.
- **At the real scale.** I used a Ruzsa Sidon set with p = 8101 and N = p(p−1) = 65 618 100,
  just above 90^4, with k = 8100, T = √6N^{3/4} and L = 36.74. Then:
  - E_true = 1 779 882.5 ≤ T + 4k − 16/3 = 1 818 238.0;
  - k^2 = 65 610 000 ≤ C(L)E_true = 66 594 802;
  - k < 8249.47.
- **Many 3-term progressions.** Greedy weak Sidon sets for N = 2·10^4 (k = 87, |P| = 22) and
  N = 2·10^5 (k = 213, |P| = 36) satisfied W5 and the sandwich at 5 scales.
- **Scalar step at high precision (60 digits).**
  - I computed the positive root ρ of P_ε for every integer N in [90^4, 90^4 + 20 000], every
    37th integer up to 90^4 + 2·10^5, and 3001 log-spaced x up to 9·10^16.
  - y − ρ > 0 everywhere. The minimum is 0.0834, at N = 90^4. It rises to 0.46 at x = 100 and
    to about 2/3 as x → ∞.
  - Directly expanding W6 agrees with W7 at sample (N,k).
  - The true value of εx at x = 90 is 0.46209. The proved envelope is 0.49783 < 0.5.

### 1.4 Observations and editorial notes
- **The onset is tight.** It is correct but fragile. With y = x^2 + γx + 2, the scalar step
  P_ε(y) > 0 fails for x ≤ 88.72 (grid scan). At x = 90 the root lies only 0.083 below y, and the
  envelopes in W8 and W12 are within 0.5% and 0.2% of their thresholds. Any edit to constants,
  such as replacing 200 by a larger error constant, must re-run the certificate.
- **E1.** §2 says the kernel is "decreasing on the positive half-line". It should say
  "nonincreasing", since f ≡ 0 on [1,∞). Only nonincreasing is used.
- **E4.** "PROVED" in the header is the author's own label. Under project rules, the status
  should read: proof written; cross-vendor referee PASS (this report); not formalised; no
  novelty check.
- **Comparison sentence.** None. The file explicitly makes no optimality or record claim, so
  there is nothing to check for internal consistency.

**Verdict: PASS.**

---

## 2. g-thin sets (`G_THIN.md`)

### 2.1 Exact statement and conventions
r_A(d) = #{(a,b) ∈ A^2 : a − b = d}, and the hypothesis is r_A(d) ≤ g for every d ≠ 0. For
d ≠ 0, ordered and unordered counting agree, since the sign of d fixes the order. Zero
differences are unrestricted. This is a difference condition (B_2^-[g]), not the sum condition
B_2[g].

The theorem: for integers N, g ≥ 1 with gN ≥ 120^4 and A ⊆ {1..N},
|A| < √(gN) + (2√2/3)(gN)^{1/4} + 1. There is a diameter form with D = max A − min A > 0 in
place of N when gD ≥ 120^4. There is also an inverse form G11 for k ≥ 20366. I found no mismatch
between definition and proof. The attribution to Balogh–Füredi–Roy §6 was not checked.

### 2.2 Steps re-derived
1. **The energy bound (G4).** E = (4/3)k + 2Σ r(d)f(d/T) ≤ (4/3)k + 2gΣ f(d/T) ≤ (4/3)k + gT.
   The diagonal coefficient stays 4/3 and is not multiplied by g. This uses f ≥ 0 and the
   lattice bound.
2. **Change of variables.** S = gT and X = gN, so N/T = X/S and every S ∈ (0,X] is allowed
   (T = S/g ≤ N). For the diameter form, translate by −min A; then the support is [0, D/T].
3. **Expansion (G7).** With S = √2x^3: 4/(3√2) = (2√2/3) = γ and γ^2 = 8/9. I re-expanded G5
   by hand and got G7 exactly. P_0(y) = (2 − γ^2)x^2 + γ(1 − γ^2)x + 1 − γ^2
   = (10/9)x^2 + (γ/9)x + 1/9 ≥ x^2. This matches G9.
4. **The bounds G8 and G10.**
   - α ≥ 1/4 and √2 ≤ 3/2 give εx ≤ 200x·e^{−x/6}, which decreases for x ≥ 6, so
     εx ≤ 24000e^{−20} < 24000/2^{20} < 1/32.
   - y ≤ 3x^2 for x ≥ 1.
   - x/8 + 3x^2/64 ≤ 11x^2/64 for x ≥ 1.
   - Hence P_ε(y) > 53x^2/64. Every step holds for all real x ≥ 120.
5. **The inverse form G11.** The k(k−1)/2 positive differences lie in {1..D}, each with
   multiplicity at most g, so gD ≥ k(k−1)/2. Then 20366·20365/2 = 207 376 795 > 120^4. Solving
   k − 1 < y^2 + γy gives G11.
6. **No circularity.** S depends only on X.

### 2.3 Numerical tests run
- **Exhaustive enumeration.** I enumerated all 2-thin subsets of {0..28} (1 428 120 sets) and
  all 3-thin subsets of {0..24} (1 658 224 sets), over every prefix length N. On each I checked:
  - the exact decomposition E = (4/3)k + 2Σ r(d)f(d/T);
  - G4 in exact integer form at 11 rational scales;
  - the sandwich k^2 ≤ C(L)E for L = N/T and for the diameter scale L = D/T;
  - the inequality actually used, k^2 ≤ C(L)(S + 4k/3);
  - k(k−1)/2 ≤ gD.

  There were no violations.
- **Greedy sets.** Greedy 2-thin (k = 257) and 3-thin (k = 341) sets in [1, 10^5] satisfied
  G4 and the sandwich at 4 scales, including S = √2 X^{3/4}.
- **Scalar lemma at high precision.**
  - I tested 22 000 real X in [120^4, 120^4 + 1.5·10^6], most of them non-integers, plus a log
    grid up to x = 1.2·10^17. y − ρ > 0 everywhere. The minimum is 0.5538, at X = 120^4, and it
    tends to 5/9.
  - εx at x = 120 is 6.0e−7, against the bound 1/32.
  - The step itself already works for x > 46.16, so the onset 120 is very conservative. The file
    makes no minimality claim.

### 2.4 Editorial notes
- **E2.** After G11, the line "gD ≥ k^2 − (4√2/3)k^{3/2} + O(k), with an absolute error
  constant" has an unspecified constant. A fully explicit replacement follows from G11 together
  with the DTS inequality D11 applied with j = k − 1 ≥ 1. For k ≥ 20366,
  gD > (k−1)^2 − (4√2/3)(k−1)^{3/2} + (16/9)(k−1) − 2√(k−1).
  I checked this algebraically: G11 says gD > z(k−1)^4, and D11 bounds z(j)^4 for every j ≥ 1.
  This is optional, since the file already labels G11 as the explicit statement.
- **Comparison sentence.** None. The file explicitly disclaims any record or improvement claim.

**Verdict: PASS.**

---

## 3. Difference triangle sets (`DIFFERENCE_TRIANGLES.md`)

### 3.1 Exact statement and conventions
An (n,k) DTS has n rows, each with K = k+1 marks 0 = a_{i0} < … < a_{ik}. All positive
within-row differences, over all rows, are distinct. Differences between rows are
unconstrained. The scope is m = max_i a_{ik}, and m(n,k) is the minimum scope. With this
convention, m(1,k) is the length of an optimal Golomb ruler with k+1 marks. My enumeration
(3.3) reproduces G(2..6) = 1, 3, 6, 11, 17, which confirms how the convention is implemented. The
attribution to Chee–Colbourn was not checked.

The theorem: for all integers n ≥ 1 and k ≥ 20365,
m(n,k) > n((√(4k + 8/9) − 2√2/3)/2)^4. Corollary D2:
m(n,k) ≥ n(k^2 − (4√2/3)k^{3/2} + (16/9)k − 2√k).

### 3.2 Steps re-derived
1. **Row energies (D4, D5).** Each row is a separate measure of mass K with support in
   [0, m/T]. Lemma 6, applied row by row and summed, gives nK^2 ≤ C(L)ΣE_i. Since
   Σ_i r_i(d) ≤ 1 for every d ≥ 1, ΣE_i ≤ (4/3)nK + 2Σ_d f(d/T) ≤ (4/3)nK + T. There is only
   one lattice budget, and the proof never forms cross-row terms.
2. **Change of variables (D6).** S = T/n and X = m/n, so L = m/T = X/S and T = nS ≤ m ⟺
   S ≤ X. For real X ≥ 120^4 the scalar algebra is the same as in G7–G10, with k replaced by K.
   This yields D9: K < √X + γX^{1/4} + 1. S depends on the configuration's scope, not on K, so
   there is no circularity.
3. **The onset (D10).** There are n·k(k+1)/2 distinct positive differences in {1..m}, so
   X ≥ k(k+1)/2. Then 20365·20366/2 = 207 376 795 ≥ 120^4 > 20364·20365/2. This holds for
   every n.
4. **Inversion.** k < x^2 + γx, and that function is increasing, so x > z. Hence m = nx^4 > nz^4.
5. **The remainder (D11).** I expanded z^4 = k^2 + γ^2k − γ(2k + γ^2)z myself and substituted
   z ≤ √k − γ/2 + γ^2/(8√k), which follows from concavity. The result is
   k^2 − 2γk^{3/2} + 2γ^2k − (5/4)γ^3√k + γ^4/2 − γ^5/(8√k), exactly as written. The final
   simplification to −2√k uses γ < 1 and 1/√k ≤ √k.

### 3.3 Numerical tests run
- **Exhaustive small families.** I enumerated every DTS family with:
  - k = 1, at most 6 rows, scope ≤ 20;
  - k = 2, at most 5 rows, scope ≤ 18;
  - k = 3, at most 3 rows, scope ≤ 22;
  - k = 4, at most 2 rows, scope ≤ 27;
  - k = 5, at most 2 rows, scope ≤ 30 (no 2-row family exists at this scope, so only single
    rows occur).

  That is 576 585 families. On each I checked D10, D5 in exact integers at 10 rational scales,
  D4 and D6. There were no violations. The minimum scopes found were:
  - m(1,1..5) = 1, 3, 6, 11, 17;
  - m(2,2) = 7, m(3,2) = 10, m(4,2) = 12, m(5,2) = 15;
  - m(2,3) = 13, m(3,3) = 19;
  - m(2,4) = 22.
- **Large instances.** I split Ruzsa Sidon sets into n consecutive blocks:
  - p = 20011, n = 1, K = 20010, X = 4.0·10^8;
  - p = 29009, n = 2, K = 14504, X = 2.1·10^8;
  - n = 4 and n = 7 at smaller X.

  D5, D4 and D6 hold at the real scale S = √2X^{3/4}. Where X ≥ 120^4, D9 and D1 also hold:
  for example, m = 421 870 936 > n·z^4 = 4.141·10^8.
- **D11 and D2.** I checked z^4 ≥ RHS(D2) for every integer k from 1 to 200 000 and on a log
  grid up to 10^15. The minimum of (z^4 − RHS)/√k is 0.95. The scalar step behaves as in 2.3,
  including at non-integer X = m/n.

### 3.4 Editorial notes
- **E3.** "PROVED" in the header and the "Stage A" verdict are the author's own labels. Status
  should be recorded as in E4.
- **Comparison sentence.** The only comparison is with the scout's earlier right-hand side,
  which had an extra "−1". It is internally consistent: m > nz^4 trivially implies the weaker
  m > nz^4 − 1. The scout's exact statement is not quoted in the file, so I could only check
  that this follows. No literature comparison is made.

**Verdict: PASS.**

---

## 4. Author checkers
All three ran with exit code 0 and printed exactly the counts recorded in the files:
- weak Sidon: 16 384 subsets, 2048 weak Sidon sets, 16 384 energy checks, 1558 repeats;
- g-thin: 4096 subsets, 7521 admissible (set, g) pairs, 60 168 energy checks, 54 substitutions;
- DTS: 687 families, 210 of them with three rows, 4122 energy checks, 72 substitutions.

The integer certificate W9, the rational margins, and the polynomial identities W10 and G9
(evaluated at 5 points for a degree-4 polynomial over Q[γ]) are correct.

The checkers only test bookkeeping. Two minor weaknesses:
- In `check_weak_sidon.js`, `strongScalarChecks` is defined but never called. This is harmless,
  because it holds the g-thin constants, and the weak Sidon constants are checked inline.
- In `check_g_thin.js`, the counting assertion uses the bound 11 instead of the actual diameter.

Neither checker is evidence for the analytic lemma, and the files say so.

## 5. What is proved and what is only numerically checked
- **Proved.** I re-derived these line by line and found them correct:
  - the combinatorial lemmas (W4, the r(d) ≤ 2 and 3-AP structure, G4, D5, D10);
  - the lattice bound;
  - the Cauchy–Schwarz reduction through Lemma 6;
  - all scalar algebra, with rational and monotone envelopes valid for every real parameter
    above the stated onsets;
  - the integer certificates;
  - the D11 remainder;
  - Lemmas 2–6 of COMMON_CAPACITY.

  This is one referee's re-derivation. It is not machine-checked.
- **Only numerically checked:**
  - the identities of Lemmas 3–5 (at sample points and on grids);
  - the size of E(ν_L,ν_L) for small L;
  - the capacity bound on finite point sets;
  - the finite exhaustive combinatorics;
  - the scalar inequalities on dense grids, as a cross-check of the proofs, which do not rely
    on them.

## 6. What I could not check
- The literature conventions and attributions (BFR §5, BFR §6, Chee–Colbourn), novelty,
  priority, and whether these bounds improve the current records.
- That COMMON_CAPACITY is faithfully copied from the project's Sidon proof. I reviewed it only
  as written here.
- Lean or kernel formalisation.

## Appendix: reproduction notes
The scripts ran in a scratch directory and are not committed. They used Node v22 and Python 3.12
with numpy and mpmath, on at most 2 threads, with no SAT or ILP solvers. Their logic:
- Backtracking enumerators in JavaScript (weak Sidon, g-thin, DTS families) with exact integer
  kernel weights 3p^3 f(dq/p).
- mpmath code for the renewal density u, the potentials f*q, the energy of ν_L, and the scalar
  roots.
- numpy code for 1ᵀF^{−1}1 on point sets and for energies of large explicit sets.

**Energy of ν_L for larger L** (continuing 0.2; V_L ≡ 1 on [0,L] and V_L ≡ 0 beyond L+1 in
every case):

| L | E(ν_L,ν_L) − (L+2/3) | allowed bound 168e^{−αL} |
|---|---|---|
| 5 | +9.5e−7 | 39.9 |
| 8 | −2.8e−9 | 16.8 |
| 12 | +5.1e−13 | 5.32 |
| 20 | −2.8e−20 | 0.533 |

The run for L = 30 reached its 1700 s time limit and was not repeated. The applications use
L ≥ 36.7, and that range is covered by the finite point-set tests at L = 40 and L = 80 in 0.2,
which use C(L) directly.
