# Erdős #859 lower-bound chain: referee report (Claude, cross-vendor), 2026-09-25

## Executive verdict

1. Scope: this report covers the effective chain d_t >= A^2/B, B <= S, S << (log t)^theta, A >> (log t)^(-101/100), and the qualitative Weingartner route. I found **no mathematical error** in any of the load-bearing steps. All logs are natural.
2. (i) B <= S: **CORRECT**. B(t) <= S(t) for every real t > 0 (uses only g*A_g <= 1 and phi(g) <= g).
3. (ii) B bound: **CORRECT**. S(t) <= 19,200,096,768 (log t)^theta for every real t >= 2, with theta = 1+log(3349/4000)/log 5 = 0.8896306804161379...; so the stated 2*10^10 also holds. theta < 1 is proved (q < 1 is certified), not assumed. No pair-overlap estimate is used.
4. (iii) A bound: **A(t) >= c_1/log t is NOT PROVED anywhere**, so there is no c_1 to test. What is proved, **CORRECT**: A(t) >= 2^(-4*10^9) (log t)^(-101/100) for every real t >= 1024. It passes the acceptance test trivially: A*log t >= 2^(-4*10^9)(log t)^(-1/100), far below the smallest measured value, 0.7765 at t = 4000.
5. (iv) Combination: **CORRECT**, and **fully effective** (explicit coefficient AND explicit range): d_t >= [2^(-8*10^9)/19,200,096,768] (log t)^(-(101/50+theta)) for every integer t >= 1024, where 101/50+theta = 2.9096306804161379.... The coefficient-free form d_t > (log t)^(-73/25) for integer t >= exp(2^(10^12)) is **CORRECT** and fully effective. Its onset is valid but not tight; log2 log t > 7.72*10^11 suffices.
6. (v) Qualitative route: **CORRECT, not effective**. d_t >= (c^2 log 2/nu + o(1)) (log t)^(-2-delta_W), where delta_W = 0.7136125.... Here c and nu are Weingartner's constants, which have no numerical values, and the onset is unspecified. I checked both quoted theorems against the arXiv LaTeX sources.
7. Verification levels. Finite numerical checks: mine, in Perl because python3 is absent, plus earlier Python reruns. Same-vendor review: the Astra verifyB report and Codex reruns. Cross-vendor review: this report. Kernel formalization: **none exists**.
8. Residual trust points that I did not re-derive: the Rosser–Schoenfeld (1962) and Fan explicit prime and rough-number inputs, which I did not re-read at source, and Stewart's criterion, which is classical. I re-checked both machine certificates in IEEE double precision, not with directed rounding.
9. Description errors, not mathematical errors: the brief's measured list is wrong in 5 of 6 entries (§3.3); the phrase "A(t) >= c_1/log t explicit" misdescribes the result; and LOWER_BOUND.md §4c, lines 217–219, contains obsolete "first proof" language.
10. Status: this is not a solution of Erdős (33), and it gives no priority or novelty claim. G2 has not been done. The effective bound beats the trivial d_t >= 1/(2t) only when log t > 5.55*10^9.

---

## 0. Method, provenance and what I actually ran

- Global-memory `recall_presets` was not exposed as a tool in this session, so no preset or user notice was retrieved.
- Files reviewed (SHA-256 prefixes): LOWER_BOUND.md `17d6e353…`, QUALITATIVE_LOWER_BOUND.md `0011880e…`,
  lemmaBprime_astra.md `b47dcf98…`, verifyB_astra.md `ddf14e24…`, explicitA_astra.md `6fd2ad29…`,
  explicitA_weights.json `9d1ef668…`. The last three match the hashes recorded in the Codex takeover review.
- `command -v python3` gives nothing, so python3 is absent. I did **not** run any of the project's Python scripts, and I installed nothing.
  I wrote independent Perl checks, core modules only, in the session scratchpad; they are not in /work. Their outputs are quoted below.
  Total machine time was under 30 s.
- Sources: I downloaded the arXiv e-print LaTeX for 1405.2585 and 2104.07137 and quoted the theorem statements below from it.
  I did not re-read Rosser–Schoenfeld 1962 or Fan–Pomerance arXiv:2306.03339 at source. There is a local scan of Rosser–Schoenfeld, but it cannot be text-extracted here.

## 1. Setup: d_t >= A^2/B — CORRECT

P(t) = {practical m : t < m <= 2t}, f(n) = #{m in P(t) : m | n}, and U = union of the sets m*Z over P(t).
Then sum_{n<=N} f = N*A + O(|P|) and sum_{n<=N} f^2 = sum_{m,m'} floor(N/lcm) = N*B + O(|P|^2). Cauchy–Schwarz gives
|U ∩ [1,N]| >= (sum f)^2/(sum f^2), and U is periodic, so dens U >= A^2/B.
U ⊆ A_t: since m > t >= 1 and m is practical, t <= m is a sum of distinct divisors of m, hence of n.
This needs only the definition of practical numbers. The sigma(m) >= t extension in L1 is not needed. Also
1/lcm(m,m') = sum_{g | gcd} phi(g)/(m m'), so B = sum_g phi(g) A_g^2, with ordered pairs and the diagonal included.

## 2. Item (i): B <= S — CORRECT

For y > 0 the integers in (y,2y] number floor(2y)-floor(y) <= floor(y)+1, and each is >= floor(y)+1, so the sum of their reciprocals is <= 1.
Hence g*A_g = sum over k in (t/g,2t/g] with gk practical of 1/k, which is <= 1. Then phi(g)A_g^2 <= g*A_g*A_g <= A_g, and sum_g A_g = sum_m tau(m)/m = S.
This holds for any set of integers in (t,2t] and any real t > 0. Finite check (Perl sieve, below): B <= S at all six t, and
max_g g*A_g = 1.0000, attained at g = m.

## 3. Item (ii): S(t) <= 19,200,096,768 (log t)^theta for real t >= 2 — CORRECT

### 3.1 Where q = 3349/4000 and the base 5 come from
Base 5 is the block dilation Y -> Y^5 (R = 5). The optimize script chose R = 5 and beta = 43/200 by grid search; that choice is exploratory and not a proof input.
q is a rational ceiling on the certified supremum of the majorant F(r) in (4.9). The true sup is about 0.83723424 at r about 2.3489.
Then c = -log q/log 5 = 0.1103693195838621 and theta = 1 - c.

### 3.2 Line-by-line checks
- **Model (§4.2).** Pr(V_p=e) = (e+1)(1-1/p)^2 p^(-e) sums to 1, and Pr(a_y = a) = tau(a)/(a Z(y)). So
  sum over practical y-smooth a of (tau(a)/a) e^(beta log a/log y) = Z(y) E[e^(beta R_y) 1_{E_y}] is an identity. E_{y'} ⊆ E_y holds because a_y is the prime prefix of a_{y'}.
- **(4.5).** For each p, log E p^(V beta/(5s)) = 2 sum_k (x^k-1)/(k p^k). The k=1 main term is 2I(h/5) after substituting x = Y^(5u).
  The partial-summation error is <= 2f(T)/s^2 = 2(e^beta-1)/s^2 <= 4.8e-7. The k>=2 terms are >= 0 and <= 4e^(2beta)/(Y-1).
  Both directions of (4.5) follow with eps = 1e-5.
- **(4.6).** Sum over Y<p<=Y^h of 1/p is log h with error <= 1/s^2 (RS (3.17)/(3.18), both at x >= 286), plus a k>=2 tail <= 2/(Y-1).
  So |log G(h) + 2 log h| < 3e-6, and e^(-3e-6) > 0.99999.
- **(4.7).** The convexity bound p^alpha - 1 <= (log p/log y)(e^beta - 1) together with RS (3.24) gives the k=1 part <= 2(e^beta-1) = 0.4796.
  The k>=2 part is <= 18 alpha. The total is < 1, so the moment is < e < 4. This is over all smooth a, so it is unconditional.
- **Killing event (4.8).** sigma(a)/a <= H_a <= 1+log a, and 2+5s <= e^(s/100) for s >= 1000 (5002 < e^10 = 22026).
  So when h < 5, sigma(a)+1 <= Y^h. If every exponent in (Y,Y^h] is 0 and some exponent in (Y^h,Y^5] is positive, the first new prime p* has
  prefix exactly a and p* > sigma(a)+1, which violates Stewart. Its weighted mass is exactly
  e^(beta r/5)(G(h) E e^(beta X_h) - G(5)); the G(5) term removes the all-zero path. Every inequality direction in F is correct.
  At h = 1 (r <= 0.99) every new prime kills, so F(0) = 0.0400437.
- **Contraction (4.10).** For practical a, E[... | a_Y=a] <= F(r) e^(beta r) <= q e^(beta r); for non-practical a it is 0. Integrating gives (4.10).
- **Iteration (4.11)–(4.12).** q^J = (log Y_*/log y)^c <= 5000^c (log y)^(-c), and Z(y) < (2 log y)^2 (RS product bound; e^0.58(1+1/2e6) = 1.786 < 2).
  So 16*5000^c = 40.96 <= 128. (4.12) follows because the weight is >= 1 on a > D.
- **Rough counts (4.13)–(4.15).** These are used only with y in {y_0, y_(j+1)}, all with log y >= 1000. Partial summation keeps the 1-1/y term for the integer 1.
  The hyperbola step needs X/a >= sqrt X >= y, which holds because X >= y^2. The dyadic bound is 2(log(2t/d)+2)/(log y)^2 <= 3L/(log y)^2.
  The unrestricted bound is 2(1+log(2t/d)) <= 3L.
- **Transfer (§4.6): every practical m is covered.** Read the prime factors with repetition, take the first prefix d > t^(1/4), and let p be the last prime of d and a = d/p <= t^(1/4).
  Every prefix is practical, including partial prime powers, because Stewart's conditions for a prefix are a subset of those for m.
  The three ranges p > y_0; y_(j+1) < p <= y_j for 0 <= j < J; and p <= y_J are disjoint and exhaustive, with the J = 0 case included.
  - Case 1 correctly switches to the predecessor a: all primes of a are <= a <= y_0, and m/a is y_0-rough.
  - In Cases 2 and 3, d <= t^(1/4)*p <= sqrt t, so the residual is >= sqrt t and never trivial.
  - The crossing prime may be the largest prime of m. Then the residual is a power of p, which is harmless because Case 2 uses the strictly smaller threshold y_(j+1) and Case 3 has no roughness condition.
  - tau(dk) <= tau(d) tau(k) holds without coprimality. The map m -> (d, m/d) is injective, so enlarging to all pairs only adds nonnegative terms.
  - (4.15) is applied pointwise for d <= sqrt t before the d-sum is enlarged to the smooth tail. That order is correct.
- **Constants.** Case 1: 48/L * 128(L/4)^(2-c) = 384*4^c L^(1-c). Case 2: s_j^(2-c)/s_(j+1)^2 = 25 s_j^(-c), which gives
  384*25*4^c 5^(cj) e^(-beta 5^j). Case 3: L*s_J^(2-c) = 4^c L^(1-c) s_J^2 u^c with u = 5^J, s_J < 5000, and u^c e^(-beta u) <= 1 because c < beta.
  sum_j 5^(cj)e^(-beta 5^j) = 1.2208 < 5, and 4^c = 1.1653 < 2. So 3*128*2*(1+125+5000^2) = **19,200,096,768** (recomputed).
- **Range 2 <= t < e^4000.** S <= (1/t) sum_{m<=2t} tau(m) <= 2(1+log 2t) <= 8L, since 6L >= 2+2 log 2 once L >= 0.564. Then 8L <= 8*4000^c L^theta = 19.98 L^theta.
  So one coefficient, 19,200,096,768, covers every real t >= 2.
- **Pair overlap.** None is used. §4 bounds only S, and the pass to B is item (i). The admission in the file's own §6 is consistent with this.

### 3.3 Checks I ran (Perl, double precision)
- I(1/5): series 0.183664725997988, and Simpson quadrature gives the same value to 15 digits. K = 1.443887966588899, matching the certificate's interval.
- Cell bound at the certificate's mesh 1e-4 (left-endpoint exponential times right-endpoint bracket): max **0.8372486443514 at cell 23488**.
  This reproduces the certificate's printed value and index exactly. The tail r >= 4.99 gives 0.6120504605412.
- Finer cell bound at mesh 1e-5: max 0.837235683846, margin 1.43e-5 below q. Pointwise max 0.837234243802 at r = 2.34891, consistent with the
  derivative-sign certificate in verifyB (0.8372342452 at r in [2.34890671, 2.34890672]).
- The bracket is positive and nondecreasing on a grid of 4001 points in h ∈ [1,5]. This is needed for the cell argument and also follows analytically.
- Exact big-integer checks: 5*3349^5 > 4000^5 (so c < 1/5), 5000 < 6^5, 5^11*3349^100 < 4000^100 (so theta < 89/100), and 2*10^10 < 2^35.
- Caveat: my certificate recheck is floating point, not directed rounding. Its margins (>= 1.4e-5) exceed plausible rounding error (~1e-15) by about 10 orders of magnitude.
  The directed-rounding Python certificates were run by OpenAI seats and not by me.
- Finite structural diagnostic: I checked 99,359 practical m in (t,2t] for t = 1000*2^k, k = 0..9. Every first crossing had a practical d and a practical a,
  a <= t^(1/4) < d, residual least prime >= p, d <= sqrt t when p <= t^(1/4), and tau(m) <= tau(d)tau(m/d). The crossing prime was the largest prime 94 times. **0 failures.**
  Stewart's criterion matched the subset-sum definition for all n <= 300.

### 3.4 Verdict (ii)
**CORRECT, fully effective:** B(t) <= S(t) <= 19,200,096,768 (log t)^0.8896306804161379... for all real t >= 2.
This rests on RS 1962 Theorem 5 and (3.24) plus the Mertens-product bound, used at x >= e^1000 or x >= 286; on Fan's Phi(X,y) < X/log y, used only for y >= e^1000; and on the q-certificate.
I did not re-read the external inputs at source. In the ranges used they are standard, and they are the only unverified-by-me dependencies.

## 4. Item (iii): lower bound for A(t)

### 4.1 What is and is not proved
- **Not proved:** A(t) >= c_1/log t for any explicit c_1 > 0. None of the files claims it. explicitA §9–10 and LOWER_BOUND §4f say so explicitly.
  The asymptotic A ~ c*log 2/log t (c = 1.33607 per LOWER_BOUND §3) is qualitative (§6) and has no explicit error term.
- **Proved (CORRECT):** A(t) >= H_400(t) >= 2^(-4,000,000,000) (log t)^(-101/100) for every real t >= 1024.

### 4.2 Line-by-line checks of explicitA §3–6
- The class C (2^e times odd primes each <= the product of the preceding prime powers) lies inside the practical numbers by Stewart's criterion, since that product is <= sigma. The closure mp ∈ C holds for P+(m) < p <= m.
- For each adjunction n = mp with m in H_j(u_k) and p in (t/m, 2t/m], I re-derived all five conditions:
  - u_k >= 4t^(1-q_i) gives p < t^(q_i)/2;
  - q_i <= 1/2 gives p < sqrt t/2 < u_k < m;
  - the block end v_k+h <= d_j L - 2h gives (1+q_j)v_k < L-h, hence u_k^(q_j) < t/(2u_k) < p, so p > P+(m).
  No overcounting: p = P+(n) has exponent 1, so m = n/P+(n) is unique. The m-ranges (v_k, v_k+h] are disjoint within each j. Across j they lie inside (d_(j+1)L, d_j L), because b_ij >= d_(j+1).
- **Prime sum (3.3).** Use RS (3.17) at 2X (valid for x > 1) and (3.18) at X >= 286, with log(1+z) >= z - z^2/2 and h/2+1/h = 1.79 < 3.
  This gives a factor >= 1-36/L. Also log(t/m) > L/11, and 1/log(t/m) > 1/(L - v_k) because m > u_k.
- **Riemann sum (§5).** |d log f/dv| <= 2.02/L + 11/L < 14/L on [L/2, 10L/11]. The full blocks cover [bL+2h, dL-3h], which contains
  L[b+2/L_0, d-3/L_0] because h < 1 <= L/L_0. The substitution s = v/L and then r = (1-s)/s gives (1+r)^(1/100)/r, and r_low >= q_j.
- **Induction (§6).** On the base range 1024 <= t <= e^(10^9), a power of 2 in (t,2t] gives H_i >= 1/(2t) > 2^(-4e9), because t^(q_i) >= 1024^(1/10) = 2.
  On t in (X_k, X_(k+1)] with X_k = exp(10^9*1.1^k), every u_k lies in [4 sqrt t, t^(10/11)] ⊆ [1024, X_k]. The induction is well founded over all real t.
- **Matrix certificate (5.5):** 0.999999 * sum_j K^-_ij w_j >= 1.001 w_i in all 401 rows. I recomputed it in Perl doubles from the JSON weights, using the (5.4) lower entries:
  the minimum over i is 1.001439601435, a margin of **4.40e-4** over 1.001. All weights satisfy 0 < w <= 1 and are monotone, and w_0 = 5.032e-10.
  The a=1 untrimmed negative control for row q=1/2 gives **0.997600889208**, matching the report.
  The argmin row is q = 0.104 for me versus q = 1/4 in the report; all rows agree to about 1e-12 because w is a near-eigenvector, so this is immaterial.
- The §9 obstruction (no positive v with M_1 v >= v on this fixed grid) is correct in its stated scope. It is not load-bearing.
  It says nothing about exponent 1 for other methods.

### 4.3 Acceptance test
My Perl sieve of practical numbers up to 1,024,000 reproduces A(t) to 12 digits. The measured A*log t values are
**0.783626798, 0.776472822, 0.807560743, 0.834791454, 0.836129970, 0.838108010** at t = 10^3, 4*10^3, 1.6*10^4, 6.4*10^4, 2.56*10^5, 5.12*10^5.
The brief's list (0.7772, 0.8091, 0.8330, 0.8344, 0.8375) is off by about 0.001–0.002 in entries 2–6; the error is in the multiplication, not the sieve.
Whichever list is used, the proved quantity A*log t >= 2^(-4e9)(log t)^(-1/100), which is about 10^(-1.2*10^9), lies below every entry. **Test passed.**
It passes because the bound is extremely weak, not because it is strong. t = 1000 is outside the theorem's range t >= 1024.

## 5. Item (iv): the combination

I re-derived it from the stated constants, with A >= c_A L^(-a), c_A = 2^(-4*10^9), a = 101/100, t >= 1024, and B <= C_B L^theta, t >= 2:

    d_t >= A^2/B >= (c_A^2/C_B) L^(-(2a+theta)),   2a+theta = 101/50 + 0.8896306804161379 = 2.9096306804161379...

Using C_B = 19,200,096,768 gives coefficient 2^(-8*10^9)/19,200,096,768, about 10^(-2.408240*10^9).
Using C_B = 2*10^10 gives the file's coefficient, which is also valid. Range: every integer t >= 1024.
**Kind: fully effective theorem** (explicit exponent, explicit coefficient, explicit onset).

Coefficient-free form: theta < 89/100 (exact integer check), so 2a+theta < 291/100 = 73/25 - 1/100. Since L > 1,
d_t >= (c_A^2/C_B) L^(1/100) L^(-73/25). Also 1/(c_A^2/C_B) < 2^(8,000,000,035) (2*10^10 < 2^35), while at log t >= 2^(10^12),
L^(1/100) >= 2^(10^10) > 2^(8,000,000,035). So **d_t > (log t)^(-73/25) for every integer t >= exp(2^(10^12)) — CORRECT, fully effective.**
Using the true gap 2.92 - 2.90963 = 0.010369, log2 log t > 7.715*10^11 already suffices; the file's onset is valid with room to spare.
Practical content: the effective bound exceeds the trivial d_t >= 1/(2t) (a power of 2 in (t,2t]) only when log t > 5.545*10^9.

## 6. Item (v): the qualitative route (QUALITATIVE_LOWER_BOUND.md) — CORRECT, not effective

- **Sources, checked against the arXiv LaTeX.**
  - arXiv:1405.2585, Theorem 1: "There is a positive constant c such that for x >= 3, P(x) = (c x/log x){1 + O(log log x/log x)}." The same paper notes that theta(n) = sigma(n)+1 gives B(x) = P(x).
  - arXiv:2104.07137v2, Theorem 3 (label thmgen): "Assume max(2,n) <= theta(n) << n exp((log n)^a) for n >= 1, where a is any constant with
    a < (1-delta)/(2-delta) = 0.2226... Then T(x) := sum_{n in B(x)} tau(n) = nu_theta x (log x)^delta + O(x), where delta = 0.7136125..."
  - Lines 227–228 of the same source identify theta(n) = sigma(n)+1 with the practical numbers.
  - The hypothesis holds: sigma(n)+1 >= n+1 >= max(2,n), and sigma(n)+1 <= n(2+log n) << n exp((log n)^(1/5)) with 1/5 < 0.2226.
  - Minor: the file says "a = 1/5 is permitted" but does not quote the constraint a < 0.2226. It should.
- **Partial summation (1).** sum_{t<n<=2t} a_n/n = F(2t)/(2t) - F(t)/t + ∫_t^{2t} F(u)/u^2 du is exact for Stieltjes integration with t excluded and 2t included. Correct.
- **A.** The endpoint terms give c(1/(L+h) - 1/L) + O(log L/L^2) = O(log L/L^2). The integral gives c log(1+h/L) + O(log L/L^2) = c h/L + O(log L/L^2).
  So A = c log 2/L + O(log L/L^2). Correct.
- **S.** The endpoint terms give nu((L+h)^delta - L^delta) + O(1) = O(1). The integral gives nu ∫_L^{L+h} v^delta dv + O(h) = nu h L^delta + O(1).
  So S = nu log 2 (log t)^delta + O(1). Correct. The **dyadic coefficient is nu*log 2**, not nu, and the file's warning on this point is right.
  Finite diagnostic: S/L^delta falls from 0.570 to 0.526 over t = 10^3..5.12*10^5, above 0.54*log 2 = 0.374. That is compatible with the O(1)/L^delta correction (L^delta = 6.28 at t = 5.12*10^5) and proves nothing either way.
- **Conclusion (4).** d_t >= A^2/S = (c^2 h^2/L^2)/(nu h L^delta) * (1+o(1)) = (c^2 log 2/nu + o(1)) L^(-2-delta). Correct.
  For every fixed beta > 2+delta_W = 2.7136125..., d_t > (log t)^(-beta) for t >= t_1(beta), with t_1 **unspecified**.
  Neither Weingartner theorem gives numerical error constants.
- **Kind:** explicit exponent with an unspecified coefficient and unspecified onset. It is not a fully effective theorem.
  It has the better exponent (2.7136 versus 2.9096) but no named constants. The two routes are complementary, and neither implies the other.
- G2 (prior literature and priority) has **not** been done for this route. The combination is a routine application of published results,
  and this review supports no first-proof claim.

## 7. Errors found, by category

- Mathematical errors in the load-bearing chain: **none found**.
- Description and record errors:
  1. The "measured" A*log t list in the brief is inaccurate in 5 of its 6 entries (§4.3). The A(t) values themselves are right.
  2. "A(t) >= c_1/log t explicit" is not a result of this chain. The effective A result is at exponent 101/100, and the exponent-1 target is open.
  3. LOWER_BOUND.md lines 217–219 (§4c, historical) say that B << log log t would give "an explicit c_2, and the first proof of Erdős's assertion".
     The premise was refuted in §4d, and the priority language breaks project rules. Do not reuse it.
  4. QUALITATIVE_LOWER_BOUND.md should state Theorem 3's constraint a < (1-delta)/(2-delta) (§6).
- Presentation nits with no effect on validity: lemmaBprime (4.7) bounds 2(e^beta - 1) by 2(e^0.4 - 1), which is looser but true.
  The small-range coefficient "48" could be 20.

## 8. Separation of evidence

| Level | What exists |
|---|---|
| Finite numerical checks | Python by OpenAI seats: both certificates with directed rounding, verifiers, 509-t B<=S checks. Perl by me: both certificates in doubles, the sieve of A, S, B at 6 t, 99,359 crossing decompositions, big-integer inequalities. |
| Same-vendor review | Astra verifyB (six CORRECT, coefficient 19,200,096,768); Codex rerun of the A verifier and the B checker; Codex local reading of the qualitative route. |
| Cross-vendor review | This report: line-by-line re-derivation of (i)–(v). No mathematical error found. External explicit inputs (RS 1962, Fan) not re-read at source. |
| Kernel formalization | None. |

## 9. What a Lean formalization would need

1. **Definitions and density.** Practical numbers; A_t; periodicity of the union of the sets mZ; dens U >= A^2/B through a finite-N Cauchy–Schwarz inequality and a limit, or a lower density.
2. **Stewart's criterion.** Sufficiency, for C ⊆ practical and for L1. Necessity, for prefix-closure and for the killing event p > sigma(a)+1 ⟹ not practical.
   Mathlib has no practical numbers, so both directions need proofs. Sufficiency is an easy induction; necessity is short but combinatorial.
3. **Arithmetic identities.** sum_{g|n} phi(g) = n (in Mathlib: `Nat.sum_totient`); B = sum_g phi(g)A_g^2; the reciprocal sum over (y,2y] is <= 1; tau(dk) <= tau(d)tau(k);
   sum_{n<=X} tau(n) <= X(1+log X); sigma(a)/a <= 1+log a.
4. **Explicit analytic inputs.** Rosser–Schoenfeld (3.17), (3.18), (3.24) and the Mertens-product bound at x >= 286 or x >= e^1000; Fan's Phi(X,y) < X/log y for y >= e^1000.
   None is in Mathlib. They would enter as named axioms or hypotheses unless proved, which is a large project.
   With axioms, the result is "formalized relative to RS and Fan", not a kernel-complete proof.
5. **Euler-product and weighted-moment layer.** The probability model can be replaced by weighted sums over y-smooth integers, which are finite products of geometric series.
   This needs lemmas about exchanging sums and products, partial summation against M(x), and the block independence written as a factorization.
6. **The q-certificate.** A proof of sup_{r>=0} F(r) <= 3349/4000. The derivative-sign route in verifyB needs only a few rational evaluations of exp and I with Taylor remainders, which is much lighter than 49,900 cells.
   Mathlib's `Real.exp_bound` and `Real.add_one_le_exp` suffice for the enclosures.
7. **The A-matrix certificate.** 401x401 rational log lower bounds (`Real.log` bounds through atanh series or `Real.log_le_sub_one_of_pos` variants) and 401 linear inequalities.
   This is feasible with `norm_num`/`decide` only if the entries are pre-rounded rationals. `native_decide` would not count as kernel-checked.
8. **The two inductions.** Iterating the contraction over 5^J blocks, and the real-variable induction on t over [1024, X_k] (well-founded via k).
9. **Final arithmetic.** theta < 89/100 through 5^11*3349^100 < 4000^100, and the onset exp(2^(10^12)). The onset needs only log-monotonicity and integer comparisons; `norm_num` handles the big integers.
10. The qualitative route (v) is **not** formalizable in the near term except by taking Weingartner's Theorems 1 and 3 as axioms.
