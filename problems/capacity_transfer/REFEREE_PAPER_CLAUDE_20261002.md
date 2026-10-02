# Whole-paper referee report: capacity-transfer note (main.tex)

Referee: Claude (Anthropic), adversarial whole-paper review, 2026-10-02.
Object: `publish/automath-papers/capacity-transfer/main.tex` (1461 lines, read completely, every line;
compiled copy = 16 pages, no LaTeX warnings, no undefined references or citations).
No other repository file and no web source was read. The proofs in the paper were checked as written,
step by step; every displayed identity was re-derived by hand and/or symbolically, and every final
explicit bound was evaluated at and above its onset.

Relation to the authors: the paper's proofs were written by GPT-6 Astra (OpenAI), so this review is
cross-vendor relative to the proofs. The original scout derivations were Claude's (Section 6 of
the paper says so), so it is not vendor-independent of those. It is a model review, not a human
referee report.

## Overall verdict: PASS-WITH-REPAIRS

I found no mathematical error in any theorem, proposition, or lemma, and no false constant, exponent
or onset. In particular, the all-N square bound (1.10) is correct as stated. Its elementary window
argument, quadratic-root step, polynomial identity and splice at N = 120^3 all check, both
analytically and numerically for every integer N < 120^3.
The required repairs are transcription and notation defects (an unstated scale identification,
undefined symbols, an inconsistent sub-count in a variation estimate). There are also wording
problems in the source comparisons and the verification-status text. None of these changes a
stated result.

## Per-theorem verdicts

| Item (numbering as compiled) | Verdict | Notes |
|---|---|---|
| Lemma 2.1 (ramp autocorrelation, f(0)=4/3, mass 1, energy representation, signed C-S) | PASS | f formula re-derived symbolically |
| Lemma 2.2 (h*g_+ = 1 on [0,inf), f*g_+ = 1 on x>=0) | PASS | telescoping identity h/2 = H - U*H checked incl. t=0, t=1 |
| Representative values (2.6), Lemma 2.3 (u -> 2 at rate (3/4)^floor t) | PASS | kernel K_x >= 0, mass 1, K_x >= 1/2 on [1/2,1]; numerics consistent |
| Lemma 2.4 (TV <= 9/2, tail <= 6e^{-aL}, q(R) = 1/3) | PASS | Laplace limit (s-2phi)/(2s phi) -> 1/3 checked |
| Lemma 2.5 (capacity: E(mu,mu) >= k^2/(L+2/3+200e^{-aL}), L>=1) | PASS | V_L = 1 on closed [0,L] incl. endpoints; |V_L-1| <= 14; 14*12 = 168 <= 200 |
| Thm 1.1 (1.1) ramp/triangle sonar, n >= 48^3 | PASS (repairs R1, R3, R4) | Lambda formula, completion, B, q, polynomial identity all exact |
| Thm 1.1 (1.2) cosine sonar, n >= 160^3 | PASS (R3, R4) | u, B_c and the expansion of Y(1-u)-B_c verified symbolically (difference 0) |
| Prop 3.1 (pi^2/32 optimal for nonnegative unit-mass factors; equality case) | PASS | C-S equality + ODE on {0<F<1} (locally Lipschitz there) gives the sine density |
| Prop 3.2 (full-class lower bound 1/4 + 1/(18 pi^2)) | PASS | B^(3/2) = -2/(3 pi); eta >= 1/(3 pi); each strip >= eta^2/4 |
| Prop 3.3 (perturbation admissible, value (pi^2/32)R) | PASS | g_theta >= 0, mass 1, transform formula, ratio bound 4210704, R algebra exact |
| (3.14) perturbed sonar consequence, n >= 160^3 | PASS (repair R6) | all constants re-derived; margin 472 at onset |
| Lemma 4.1 (real-parameter scalar step) | PASS | P_0(y) = 10x^2/9 + gamma x/9 + 1/9 exact |
| Thm 1.2 weak Sidon, N >= 90^4 | PASS | structural lemma (r(d) <= 2, distinct middles, not extreme) correct; certificate integers match exactly |
| Thm 1.3 bounded multiplicity (+ diameter version) | PASS (comparison wording R7) | |
| Thm 1.4 difference triangles (both forms), k >= 20365 | PASS | z^4 identity and expansion exact; threshold integers correct |
| Thm 1.5 Manhattan, real r >= 160^3 | PASS | |Dx|+|Dy| = max(|Du|,|Dv|), S_e, S_o bounds, c-identity (2c/3 + c/3), 18529/2160 exact |
| Thm 1.6 (1.9) integer boxes, x >= max(120,4d) | PASS | S(T) closed form verified; w, z, v, binomial and Taylor steps; c_d and exponents correct |
| Thm 1.6 (1.10) all-N square (no earlier review) | PASS (repairs R8, R12) | see dedicated section below |

### The all-N square statement (1.10): detailed check

* Window identities: sum r = kT^2 and sum r^2 = kT^2 + sum_{a!=b} (T-|a1-b1|)_+ (T-|a2-b2|)_+ are exact.
  sum_j (T-|j|)_+ = T^2, so the nonzero-vector budget is T^4 - T^2, and only uniqueness of nonzero ordered
  differences is used. Cauchy–Schwarz on M^2 = (N+T-1)^2 cells gives k^2 <= M^2[1+(k-1)/T^2]. Correct. The
  empty set is covered.
* With x = N^{1/3}, T = ceil(x^2): x^3 <= M <= x^3 + x^2 and A_0 <= (x+1)^2 hold (checked for every
  integer N < 120^3, with exact integer ceilings). Dropping -A_0 and applying (5.3) with A = A_0, B = M^2
  is legitimate. The expansion to x^3 + 3x^2/2 + 9x/8 + 1 + 3/(4x) + 1/(2x^2) + 1/(8x^3) is exact.
* Polynomial identity: 19x^4 - 8x^3 - 6x^2 - 4x - 1 = (x-1)(19x^3+11x^2+5x+1) holds, so the elementary
  bound k <= x^3 + 1.5x^2 + 3.5x holds for every real x >= 1.
* Below the splice: 83^3 = 571787 < 576000 = (8/3)*60^3, so c > 83/60 and (3/2 - c)x^2 < (7/60)x^2 < 14x
  for all real x < 120 (not only integer x). The bound is then < x^3 + cx^2 + 17.5x. The elementary
  bound stays under the target until x ~ 128.0, so the splice at 120 leaves room.
* At and above the splice: x = 120 meets x >= max(120, 4d) = 120 for d = 2. Also x_box = N^{2/6} = x,
  c_2 = (3/2)(8/9)^{2/3} = (8/3)^{1/3} (numerically identical to 15 digits), and 2d^2 = 8. So (1.9)
  gives k <= x^3 + cx^2 + 8x at x >= 120, and the capacity bound really applies at N = 120^3 with
  the stated constants. Exact root of (5.5) at N = 120^3: 1748084.88, against
  x^3 + cx^2 + 8x = 1748928.80.

## Required repairs

R1. Line 680, triangle subsection. The horizontal scale T is never identified with V, but (3.3)
    uses Lambda = mV - (V^2-1)/3, which needs T = V. Replace
    "Take $g(t)=(1-|t|)_+$ and an integer $1\le V\le m$."
    with "Take $g(t)=(1-|t|)_+$ and $T=V$ for an integer $1\le V\le m$."

R2. Lines 809–812. $a_y$ and $b_y$ are undefined. Replace $b_yU$ by $bU$, $aa_y n^2/(TU)$ by
    $aa_2n^2/(TU)$, $(a_yb_y)$ by $(a_2b)$, and "$a_yb_y=8/9$" by "$a_2b=8/9$". Alternatively, define
    "$a_y=f(0)=a_2$, $b_y=b$ for the vertical ramp". Also say what "leading expression" means:
    "After solving (3.8) for $m$, the excess over $n$ is $MT+bU+aa_2n^2/(TU)$ plus lower-order terms."

R3. Line 671. $h_g$ is undefined. Add: "where $g=h_g*\widetilde h_g$; here $h_g=\ind_{[0,1]}$ for the
    triangle and $h_g=h_c$ for the cosine kernel."

R4. Lines 654–664 (also used in (4.2), Section 4.2, (5.1)). $E_G$ and $E_f$ are used but only $E$
    (for $f$) is defined in Lemma 2.1. Before (3.1), insert: "For a bounded kernel $K$ on $\R^j$ and
    finite signed measures write $E_K(\mu,\nu)=\iint K(x-y)\,d\mu(x)\,d\nu(y)$; thus $E_f=E$ of
    Lemma 2.1."

R5. Abstract, lines 41–42. Two problems. The symbol $f$ is the fixed ramp autocorrelation everywhere
    else. And without unit mass the infimum of the stated functional over autocorrelations of
    nonnegative factors is 0, because the functional scales with the factor's mass. Replace with:
    "For a mass-one kernel $g$, the horizontal functional $g(0)\int|t|g(t)\,dt$ has minimum $\pi^2/32$
    among autocorrelations $g=h*\widetilde h$ of nonnegative $h$ with $\int h=1$."

R6. Lines 925–927. The displayed bound $\operatorname{Var}(|t|g_\theta)\le2+\theta(6+132a_0)$ needs the
    central term $2|t|b_\delta(t)$ to contribute 4: 2 from the two shifted unit masses, 4 central,
    $132a_0$ from the shifted bumps. The text says "the central term has variation at most 2".
    Replace with "and the central term $2|t|b_\delta(t)$ has variation at most $4$, twice the
    variation of $|s|g(s)$." The final bound is unaffected; the numerical value is about 1.002.

R7. Lines 95, 110–113, 170. Say which coefficient is compared. As written, "coefficient
    $1-\varepsilon_g/2$" for $g=1$ could be read as a leading coefficient below 1 for Sidon sets.
    Singer's construction makes that impossible. The comparison is with the second-order term.
    Changes:
    * Line 95: "best proved coefficient of $N^{1/4}$".
    * Line 111: "prove the second-order coefficient $1$ (of $(gN)^{1/4}$)".
    * Line 112: "a smaller, explicitly $g$-dependent second-order coefficient".
    * Line 170: "the located coefficients of $N^{2/3}$ are".
    (The wording was checked only for internal consistency; the sources were not read.)

R8. Lines 168–176. Add the pointwise disclaimer that the sonar paragraph already has (line 77).
    (1.10) is below the attributed all-N bound $N+1.9N^{2/3}+1.6N^{1/3}+1$ only for $N\ge32433$
    (computed). Suggested sentence: "Bound~\eqref{eq:boxes-all} is smaller than that all-$N$ bound
    only for $N\ge32433$; no pointwise superiority is asserted."

R9. Lines 812–815 (optimality wording). "proves that the best leading coefficient of this particular
    template ... is $3(\pi^2/36)^{1/3}$, when its lattice errors are lower order". What the paper
    actually establishes is the AM–GM minimum of the leading expression. "Template" and "lattice
    errors lower order" are not formalised. Replace with: "shows that, with the vertical ramp fixed,
    no horizontal kernel that is the autocorrelation of a nonnegative unit-mass factor makes the
    AM–GM minimum of this leading expression smaller than $3(\pi^2/36)^{1/3}n^{2/3}$."

R10. Line 1322 (verification-status overclaim). "followed by independent OpenAI in-team review" is
    self-contradictory, since a same-vendor in-team review is not independent. Replace with
    "followed by a separate same-vendor (OpenAI) review in the same workflow". At line 1318,
    "independently examined" should be "examined".

R11. Line 22 (\RefereeStatus) and line 1325. The macro is now stale. It says the all-N supplement
    "was not in the Claude referees' reading lists", but this whole-paper review read it. Update it
    to record this report and its verdict (PASS-WITH-REPAIRS, all repairs notational or wording) once
    the repairs are applied. Also state that this referee is Claude: cross-vendor relative to the
    Astra proofs, same vendor as the scout derivations. Do not describe any review as human or
    vendor-independent.

R12. Lines 1276–1277. In Section 5.3, $k$ and the Sidon hypothesis are used without being introduced.
    Replace "For $A\subseteq[N]^2$, take" with "For a strong Sidon $A\subseteq[N]^2$ with $k=|A|$, take".

## Optional editorial suggestions

E1. Symbol reuse is heavy. Each use is locally unambiguous, but the following carry two or more
    meanings: $q$ (correction measure, rational in 3.1, function in Prop 3.2, $1/x$ in 5.2); $U$
    (uniform measure, vertical scale, $k/K$); $g$ (kernel, multiplicity, $g_+$); $\Lambda$ (sum in 3,
    lattice in 5.1); $M$ (moment, $N+T-1$); $R$ (perturbation factor, box side); $D$ (diameter,
    Manhattan, boxes); $c$ (limit in 2.3, two constants in 5); $h$ (ramp factor, generic factor in
    Prop 3.1). Also $m$ is columns, scope and $|A|$ (Manhattan); $k$ is mass, $|A|$ and row length.
    Renaming the generic factor in Prop 3.1 (e.g. $\varphi$) and the lattice in 5.1 (e.g. $\Gamma$)
    would help most.

E2. Line 55. "$a-b=c-d$" uses $d$, which also denotes the dimension in the same sentence; use $a',b'$.

E3. Lines 1024, 1074, 1087 and the sonar section say "the capacity lemma" without a reference; cite
    Lemma~\ref{lem:6}. Theorem 1.1 and 1.6 are never referenced from their proofs.

E4. Line 780. "Finally $3v<2$ ..." has no stated purpose; say "so the coefficient in (1.2) is smaller
    than that in (1.1)".

E5. Section 5.3 proves $|A|\le N+\tfrac32N^{2/3}+\tfrac72N^{1/3}$ for every $N\ge1$. This is Robinson's
    asymptotic coefficient with an explicit all-N remainder. It is smaller than (1.10) for all
    $N<128^3$ approximately, and below the attributed $1.9/1.6$ bound from $N\ge72$. Consider stating
    (1.10) as the minimum of the two bounds, or recording the elementary bound as a separate line.
    No priority claim is implied.

E6. Lines 1194–1195. "In particular an unspecified lower-order error has not been silently deleted."
    reads defensively; delete it.

E7. Lines 188–190. "the present analytic construction and its transfers are not claimed as new
    formalised theorems" can be misread as "formalised but not new". Suggested wording: "Apart from
    that earlier Sidon bound, no statement in this note is claimed to be formalised in Lean."

E8. Lines 1346–1374. The checker table asserts PASS runs, but the paper gives no location for the
    checkers, so a reader cannot rerun them. Add the repository path or soften to "recorded runs".
    The total of 127840 is the correct sum of the six listed energy-case counts.

E9. Line 21. The internal LaTeX comment about the coordinator's workflow will be public in the
    source; consider removing it.

E10. Section 1 lists the cosine sonar bound as the headline. Asymptotically, (3.14) has a marginally
    smaller coefficient (factor $R^{1/3}\approx1-5.4\cdot10^{-7}$) with remainder $8n^{1/3}$. The paper
    already says this; no change is needed beyond keeping (3.14) out of the abstract.

## Claims and tone audit (sentences claiming more than proved, or needing qualification)

* Abstract l.41–42: functional "optimum" lacks the unit-mass normalisation (R5).
* l.812–815: template "best leading coefficient" (R9).
* l.1322: "independent OpenAI in-team review" (R10).
* l.22 macro: stale status (R11).
* l.110–113: ambiguous coefficient comparison (R7).
* l.168–176: no pointwise disclaimer for the box comparisons (R8).
* l.1349: "The recorded executions all returned PASS". I could not verify this, and no location is
  given (E8).

Satisfactory as written:
* No priority claim: lines 83–85, 175–176 and 1393–1394 disclaim priority explicitly.
* "Best" appears only as "best ... located in the bounded source audit" (l.71, 95, 148).
* No optimality of onsets or constants is claimed (l.1394–1395).
* The original Sidon conjecture is explicitly not claimed (l.181–182).
* Lean: the abstract (l.45–46), line 1 and Section 6 (l.1329–1344) state that only the earlier ordinary
  Sidon bound is formalised. This matches the requirement.
* "Barrier" does not occur.
* The privacy scan found no local paths, e-mail addresses or chat links in main.tex.

## Numerical tests actually run

Python 3 with numpy, mpmath (50 digits), sympy and scipy; at most 2 threads; no SAT or ILP. The scripts
were run in a scratch directory and are not committed. All tests below PASSED unless stated.

1. Symbolic (sympy), all with difference exactly 0:
   * Lemma 2.1 autocorrelation and its moments (int f = 1, f(0) = ||h||^2 = 4/3).
   * Sonar triangle step: B, q and 36x^3{Y(1-q)-B} = 14x^4-184x^3-81x^2-96x-72, together with its
     t = x-16 expansion 14t^4+712t^3+12591t^2+85376t+141496.
   * Cosine kernel: closed form, mass 1, M = 1/4 and g'.
   * Cosine sonar: u and B_c derived from (3.8), and the full expansion of Y(1-u)-B_c.
   * Perturbation: R = 1-(129/8)theta-508theta^2 and M = 1/4+(127/32)theta.
   * Weak Sidon P_0(y) and Lemma 4.1 P_0(y).
   * DTS z^4 identity.
   * Manhattan identity bt/sqrt2 + a^2/(2t^2) = c.
   * Box lattice closed form of S(T) against direct summation.
   * All-N factorisation.
2. Exact rationals and integers:
   * Weak-Sidon certificate: (1957/720)^10 * sum = 36120.98 > 36000. Both 45-digit integers in the paper
     match exactly. 1957/720 = sum_{j<=6} 1/j!.
   * Threshold and constant checks: 20364·20365/2 = 207356430 < 120^4 < 207376795;
     200·48^2 = 460800 < 9^6; 200·160^4 < 2^40; (3/4)^8 < 1/9; 83^3 < (8/3)·60^3; 18529/2160 < 9;
     8024/6075 > 13/10; 465/512; 16(1+2/delta^2)^2 = 4210704.
3. Capacity certificate, built numerically by solving the delay equation for u on a 1/2000 grid:
   * |u-2| stays below the Lemma 2.3 envelope; the true decay is much faster.
   * q(R) = 0.333331, close to 1/3; ||q||_TV ≈ 0.79, under the 9/2 bound.
   * V_L = 1 on [0,L] to grid accuracy (about 3e-4) for L = 1, 2, 4, 8, 16.
   * E(nu_L,nu_L) - (L+2/3) was 8e-3, -2e-4, -9e-6, -5e-7 and -1e-6, far inside 200e^{-aL}.
4. Final bounds evaluated exactly from each proof's own unrelaxed intermediate inequality, at the onset
   and on dense or geometric scans from the onset up to 1e15 (2e6 dense plus 2e6 geometric points
   each). Minimum margins:

   | Bound | Minimum margin | Notes |
   |---|---|---|
   | Sonar ramp | 14.95 at n = 48^3 | the inequality would fail only below x = 36 |
   | Cosine sonar | 68.04 at 160^3 | fails only below x = 35 |
   | Perturbed sonar | 472 at 160^3 | |
   | Weak Sidon | 0.0834 at 90^4 | tight but positive; fails at x = 88 |
   | Lemma 4.1 | 0.554 | |
   | Manhattan | 1107 | |
   | Boxes, d = 2..12, 20, 30, 31, 40, 60 at x = max(120,4d), and d = 2..5 densely | at least 0.879 · 2d^2 N^{d(d-1)/(2d+2)} | |
   | All-N, every integer N < 120^3 | target minus elementary bound ≥ 14.39 | every link of the chain verified per N |
   | All-N, N ≥ 120^3 (2000 consecutive N plus powers of 10 to 1e18) | (claim - root)/x ≥ 7.03 | |

5. Perturbed kernel:
   * min g_theta ≥ -3e-17 (rounding only); mass 1.
   * aM by quadrature minus (pi^2/32)R = 4e-11.
   * Var g_theta and Var |t|g_theta are within the stated bounds.
   * The ratio 16 sin^2(pi xi)(1-4xi^2)^2 g^(delta xi) is at most 1.98e6 on [0,2000], under 4210704.
   * The transform formula for h_c^ was checked against quadrature at 5 points (error < 1e-16).
   * |h_c^| ≤ min(1, 1/(2xi^2)) holds on the grid.
6. Lattice estimates:
   * |sum g(d/T) - T| ≤ 0.234 and |sum p(d/T) - TM| ≤ 0.272 for the cosine kernel (claims: ≤ a and ≤ 2).
   * The perturbed analogues are within 3.
   * T(S(T) - T) ≤ 0.373 (claim 7/16).
7. Real objects:
   * Quadratic sonar sequences y_i = i^2 mod p, i = 0..p, for p = 101, 211, 307, 401 and 503. The
     sonar property was verified for p ≤ 211. Tests: 225 checks of the marginal inequality
     Lambda ≤ C(n/U)E_G, 125 of the triangle sandwich and 100 of the cosine sandwich, over several
     (T,U). No violation.
   * Bose Sidon sets for p = 31 to 307: 300 checks of the capacity inequality; the stress ratio
     k^2/(E(L+2/3)) reached 0.93.
   * Greedy weak Sidon sets for N up to 20000. Checked: r(d) ≤ 2, repeated differences are 3-AP edges
     with distinct non-extreme middles, and (4.2) at 6 scales each.
   * Greedy multiplicity-g sets (g = 2, 3, 5), with the energy bound tested.
   * Greedy difference triangle sets, with the summed row energy tested.
   * Greedy Sidon sets in [N]^2 (N up to 60) and [N]^3: window identity and inequality at 6 values of
     T, and the box energy bounds.
   * Greedy Manhattan configurations (r up to 30): energy bound and S_e, S_o bounds.
   * No violation of any tested intermediate inequality.
8. Exhaustive maxima of Sidon sets in [N]^2 by backtracking, with each maximiser independently
   re-verified:

   | N | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
   |---|---|---|---|---|---|---|---|
   | max \|A\| | 1 | 3 | 5 | 6 | 8 | 9 | 11 |
   | window root | 1.00 | 3.96 | 6.30 | 8.00 | 9.86 | 11.61 | 13.30 |
   | (1.10) | 20.4 | 26.9 | 31.8 | 36.1 | 39.8 | 43.3 | 46.5 |

   The window inequality holds for every T in 1..2N+1 on each maximiser. At this size (1.10) is far
   from tight. The elementary bound x^3 + 1.5x^2 + 3.5x is 6.0 to 19.2 over the same range.

## What I could not check

* Every literature statement: ORTU14, EGRT92 (including the "printed proof gives 4" remark), CK96,
  BFR21, CHO25 (including epsilon_g ≥ 0.0062g^{-4}), CC97/Kløve, BEMP10, Rob85, Tru23 and the Caicedo
  thesis. These were outside the permitted reading. R7 and R8 rest only on internal consistency and
  textbook facts (Singer).
* The [Chen26] one-dimensional intercept theorem quoted at lines 818–826. It is not used in any proof
  in this paper.
* The Lean claims (toolchain version, Mathlib commit, axiom list, linked revision), the
  JavaScript-checker counts and PASS records, and the history in \RefereeStatus.
* The equality case of Prop 3.1 and the Fourier positivity of Prop 3.3 were checked analytically by
  hand. For Prop 3.3 the numerical grid covered |xi| ≤ 2000; the analytic bound covers the rest. Lemma
  2.3's essential-range argument was checked by hand, with consistent numerics but no formal proof.
* Exhaustive square maxima only for N ≤ 7; larger N used greedy sets only.
