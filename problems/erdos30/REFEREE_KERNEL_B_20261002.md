# Cross-vendor referee B (Claude Opus), independent reconstruction and numerical attack — kernel optimality

Date: 2026-10-02. Object under review: `problems/erdos30/KERNEL_OPTIMALITY.md`
(author: GPT-6 Astra; Theorems 1 and 2, and the barrier statement in §7).
Isolation: I did not open any `REFEREE_*` file, `KERNEL_SCAN_20261002.md`, or
`numerics/` (the author's optimiser and log). I read §1 of the document only,
reconstructed a proof, ran the numerics below, and only then read §§2–10.
Vendor: Anthropic (Claude Opus 5.5); the author is OpenAI, so this is a
cross-vendor review. It is not a human or a Lean check.

## Verdict

**PASS.** I verified Theorem 1 (universal lower bound ab >= 8/9) and Theorem 2 (ramp
attainment with the explicit two-sided remainder) as stated, by an
independent reconstruction followed by a line-by-line check of §§2–6. No
counterexample was found. No grid-converged numerical value
falls below 8/9. Three non-blocking remarks follow (R1–R3). None of them is
needed for correctness. R1 is a strengthening that I recommend stating.

Three most important findings:

1. **My independent reconstruction found the same certificate.** Before
   reading §§2–10 I derived that every positive half-line boundary correction rho
   gives a bound that is *linear in f*:
   liminf(C_f(L) − L) >= ∫ f dW_rho, with
   W_rho = (|t| + 2 rho([0,|t|))) dt − 2 rho*rho~.
   If W_rho >= alpha·dt − beta·delta_0, then dilation gives ab >= alpha²/(4 beta).
   Atoms alone give only 1/2. Atom plus gap reaches about 0.880 on the ramp, which is not enough.
   For decreasing h, the signed half-line equilibrium h^{-1}*H_+ equals
   (1/h(0)) times the renewal measure of q = −h'/h(0), which is automatically
   nonnegative. For the ramp this is v = U_{Unif[0,1]}/2, the
   document's trial. I computed W for it numerically. On (−1,1) the density is 4/3 to within
   1.3e-7. At |t| = 1 it jumps by +1/2, and beyond that it is 4/3 + R(|t|−1)/2. There is an atom −1/2 at 0.
   This gives alpha = 4/3 and beta = 1/2, so ab >= 8/9. It is exactly the document's Lemma (4.2),
   because B = 4m·dt − W with m = 1/3.
2. **The numerical attack found no kernel below 8/9.** I computed the positive capacity with a
   grid QP, which gives a rigorous lower bound on C_f(L). For PD kernels I also computed a Cauchy–Schwarz
   upper bound from the optimal grid measure. Of the named kernels tested (about 30, including signed h and
   heavy tails), every in-class value of ab is >= 8/9. Equality holds only for the ramp. The next-best values are
   (1−t)^p-type factors at 0.900, and the Gaussian, sech and smooth-bump kernels at 0.94–0.99.
   An evolution-strategy minimiser ran over four 24–36-parameter families (signed
   piecewise-constant h on [0,1] with 24 and 32 cells, the same on [0,3] with 36 cells, and positive
   mixtures of 24 triangles) from 20 starts, 16 of them feasible. The lowest value was
   a·b = 0.889078. Every run converged to a ramp-shaped kernel. For these piecewise-linear
   kernels on node-aligned grids, the lower bound C_lo and the upper bound C_hi agree to 6 digits under 2×–8× grid
   refinement and L up to 30, so these values are certified two-sided. Their excess over 8/9 is the cell-resolution
   effect 2/(9M²) of a piecewise-constant ramp, which is exact (see §3.3). On the exact (smooth-cubic) ramp,
   the raw grid deficit is a·(C_lo − L) − 8/9 ≈ −1.1e-4 at L = 10, δ = 0.005, and it scales as L·δ².
3. **The hypothesis "C_f(L) = L + b + o(1)" fails for many natural nonnegative
   kernels, but the proof does not need it (R1).** Every nonnegative non-PD kernel
   has capacity slope > 1, so C − L grows linearly. Examples are the box, the Epanechnikov kernel, and 500/500 random nonnegative
   piecewise-linear even f. Kernels with m_1 = ∞ (Cauchy, Fejér sinc²) have C − L ≥ M_1(L) → ∞.
   The triangle converges only at rate O(1/L): C(L) = L + 1 − 1/(4L+4) at
   half-integers. The proof of §5 never uses existence of the limit. It shows
   liminf_{L→∞}(C_f(L) − L) >= 8/(9 f(0)) for **every** even nonnegative
   f ∈ C_0 ∩ L¹ with ∫f = 1 and f(0) > 0, with value +∞ when m_1 = ∞. The Sidon application
   needs limsup ≥ liminf, so the barrier in §7 holds for all fixed nonnegative
   kernels, not only those with a finite intercept.

## 1. Independent reconstruction (done before reading §§2–10)

Notation: G(x) = ∫_x^∞ f, so m_1 = ∫|t| f = 2∫_0^∞ G. Two-ended trial
mu_L = lambda_[0,L] + rho + (reflection of rho), with rho a decaying measure on [0,∞) and
lambda_+ + rho >= 0. Expanding 2M − E (equivalently M²/E) gives

    C_f(L) >= L + m_1 + 4<G,rho> − 2E_f(rho,rho) + o(1) = L + ∫ f dW_rho + o(1),

with W_rho as in finding 1 (Fubini: 4<G,rho> = 2∫ f(t) rho([0,|t|)) dt). Dilation of
rho by ell maps ∫ f dW to ell·∫ f_ell dW. Therefore W_rho >= alpha dt − beta delta_0 implies
b >= sup_ell ell(alpha − beta ell a) = alpha²/(4 beta a). Each family below was checked:

| trial family | alpha²/(4beta) or value on the ramp | sufficient? |
|---|---|---|
| atom beta δ_0 only | 1/2 (ab >= a·m_1 + 1/2, = 77/90 on the ramp) | no |
| atom + gap [0,c) | best ≈ 0.880 on the ramp (c ≈ 0.227) | no |
| renewal v = U_{Unif[0,1]}/2 (ramp equilibrium) | 4/3 squared over 4·(1/2) = **8/9** | **yes** |

The numerical evaluation of D(t) = density of W_rho for the renewal trial used
U computed in 45-digit arithmetic from the closed form
U([0,x]) = Σ_k (−1)^k (x−k)^k e^{x−k}/k!. Double precision is catastrophically unstable for x ≳ 10.
The autocorrelation was computed by FFT with h = 1e-3. Results:
max_{[0,1)}|D − 4/3| = 1.3e-7. D(1+) − 4/3 = 0.5000000. D(t) − 4/3 equals R(t−1)/2 at all
sampled t in (1,8] (e.g. 0.82436 at 1.5, 1.82866 at 2.5). ∫k² = 1/12 to 7e-8, and
κ(R) = 1/3 to 1e-16. So W >= (4/3)dt − (1/2)δ_0 for all t, with equality exactly on (−1,1).
Since f >= 0, this is all the proof needs. Positive definiteness is not used.

## 2. Check of the document against the reconstruction

* §2 (2.1)–(2.2): correct. 2M − E maximised over scalings gives 1/E. E(λ_L,λ_L) = L − M_1(L),
  hence m_1 <= b.
* §3: I checked h_0/2 = H_+ − W*H_+ and the telescoping in (3.1) by hand. I checked (3.2) numerically:
  the error is 6e-17 at 20 points (n = 1,2,3,5). The quantities u >= 1 (min 1.0005 on the h = 1e-3 grid), |u−2|/(2(3/4)^⌊t⌋) <= 0.4998 < 1,
  TV(κ) = 0.790 <= 9/2, and |κ|((L,∞)) (4.4e-2 at L = 1, 2.8e-10 at L = 10) all hold. The
  bounds are valid but loose: the true decay rate is about 2.09, from the roots of s = 1 − e^{−s},
  against alpha = log(4/3) ≈ 0.288. The Doeblin contraction argument (kernel ≥ ½ on [½,1], mass ¼) is correct.
* §4: the operator identities Av = ½δ'_0, AH_+ = δ_0 − W and Aκ = W − δ_0 + ½δ'_0 were checked by hand.
  The ODE step on (0,1) is correct: g = D_0(t) − D_0(1−t) has g' = 0 and is odd about ½.
  The delay-equation uniqueness on (1,∞) is correct, and so is the matching of asymptotic constants (d + 2/3 = 2m ⇒ d = 0).
  The final identity (4.2) agrees with my independent numerics above.
* §5: I re-derived all four energy terms of (5.1), including the dominated-convergence steps (f bounded, |κ| finite,
  f ∈ C_0 for the cross term), the positivity of ν_L (density u(x)/2 + u(L−x)/2 − 1 ≥ 0 because u ≥ 1), and the
  scaling C_{f_ℓ}(L) = C_f(ℓL)/ℓ. I also checked (5.1)/(5.3) directly at finite L. I built ν_L with
  ℓ = 4/(3a), computed 2M − E − L with exact cell-averaged kernels, and obtained the following:

  | kernel | L=12 | L=20 | predicted (5.3) incl. tail term | 8/(9a) |
  |---|---|---|---|---|
  | ramp f_0 | 0.66667 | 0.66667 | 0.66667 | 0.66667 |
  | Gaussian e^{−πt²} | 0.88949 | 0.88945 | 0.88949 | 0.88889 |
  | triangle | 0.88889 | 0.88887 | 0.88889 | 0.88889 |
  | e^{−\|t\|}/2 | 1.92010 | 1.92008 | 1.92008 | 1.77778 |
  | sech²(t)/2 | 1.79349 | 1.79356 | 1.79354 | 1.77778 |

* §6 (Theorem 2): checked line by line. η_L = v + v_L − λ_R, V_L = 1 on the closed [0,L], |V_L| ≤ 13,
  ‖τ_L‖ ≤ 12q_L, the error term 168 q_L = 14·12 q_L, the exact identity 2M(σ) − E(σ,σ) = E(η,η) − E(τ,τ), and 192 q_L² = (4/3)·144 q_L².
  The numerics are well inside the bound (Richardson-extrapolated grid QP, upper-bound certificate in brackets):

  | L | C(L) − L − 2/3 | document bound 360e^{−αL} |
  |---|---|---|
  | 1 | +7.83e-3 | 270 |
  | 2 | −2.05e-4 | 203 |
  | 3 | −1.24e-4 | 152 |
  | 4 | −9.2e-6 | 114 |
  | 5 | +9.5e-7 | 85 |

  The sign oscillates and the deviation decays at roughly e^{−2.1L}. The stated remainder is correct but
  becomes nontrivial (< 1) only for L > 20.5 (R3). b(f_0) = 2/3: Richardson extrapolation at L = 12 gives
  0.66666666, and the upper certificate converges to it from above (at L = 12: 0.67195, 0.66800, 0.66700 for δ = 0.02, 0.01, 0.005).
* §7: the sampling bound for monotone f_0, the TV variant, the Sidon energy ≤ ak + T + O(1)
  (which uses f ≥ 0 and r(d) ≤ 1), k² ≤ C(N/T)(ak+T+O(1)), the root x² + (bt + a/t)x/2 + o(x) and the optimum √(ab)
  are all correct. The scope statements are accurate.
* §8: the (1+s)^{-2} example is correct (1/(sH) − 1/s = 2 + s). Signed-capacity comparison is used only as a
  Cauchy–Schwarz certificate, which is correct.

## 3. Numerical attack

Method: atoms on a uniform grid of [0,L]. Maximise 2Σw − wᵀKw over w ≥ 0, with K_ij = f(x_i − x_j),
using block principal pivoting and an L-BFGS-B fallback for ill-conditioned K.
Every feasible w is a genuine nonnegative measure, so **C_lo = 2Σw − wᵀKw ≤ C_f(L)
rigorously**, up to floating point. For PD f, **C_hi = E(w)/(min_{[0,L]} f*w)²**, with the minimum
over a 4–8× finer continuum grid, is an upper bound by Cauchy–Schwarz. For kinked f the bulk
grid error of C_lo is ∝ L·δ². It is removed by the discrete slope 1/(δΣ_k f(kδ)), shown as
"b_est". For piecewise-linear f on node-aligned grids that slope is exactly 1.

### 3.1 Named kernels (a = f(0); values of a·b)

| kernel | a | a·(C_lo−L) | a·(C_hi−L) | a·b_est / exact | in class? |
|---|---|---|---|---|---|
| ramp autocorrelation f_0 (L=10, δ=.005) | 4/3 | 0.88878 | 0.88927 | 0.88889 (=8/9) | yes |
| triangle (1−\|t\|)_+ (L=10,20) | 1 | 1.00000 | 1.00000 | 1 | yes |
| e^{−\|t\|}/2 (L=30) | 1/2 | 0.99922 | 1.00172 | 1.00000 | yes |
| Gaussian e^{−πt²} (L=12) | 1 | 0.95708 | 0.95885 | ≈0.957–0.959 | yes |
| sech(t)/π | 1/π | 0.94126 | 0.94138 | 0.9413 | yes |
| sech²(t)/2 | 1/2 | 0.94101 | 0.94110 | 0.9410 | yes |
| Jackson 1.5·sinc⁴ | 3/2 | 0.98386 | 0.98831 | ≈0.984–0.988 | yes |
| auto(half-sine) | 1.2337 | 0.98174 | 0.98197 | 0.9817 | yes |
| auto(6t(1−t)) (L=12; at L=8 the bracket is 0.97876–0.97890) | 1.2 | 0.98237 | 0.98296 | ≈0.98, slow in L | yes |
| auto((1−t)^{1/2}) | 1.125 | 0.89994 | 0.90154 | 0.90000 (exact 9/10) | yes |
| auto((1−t)²) | 1.8 | 0.89961 | 0.90091 | 0.90001 (exact 9/10) | yes |
| auto((1−t)³) | 2.2857 | 0.91339 | 0.91625 | 0.91430 (exact 32/35) | yes |
| auto(1−t²) | 1.2 | 0.89994 | 0.90033 | 0.90000 | yes |
| auto(e^{−3t} on [0,1]) | 1.6572 | 0.93076 | 0.93193 | 0.93114 | yes |
| auto(1−√t) | 1.5 | 0.89967 | 0.90370 | 0.90000 | yes |
| non-monotone h ≥ 0: auto(2(1−t)+0.3cos 2πt) | 1.3783 | 0.91875 | 0.91932 | 0.91889 | yes |
| non-monotone h ≥ 0: auto((1−t)(1−1.5t)+0.2) | 1.4733 | 0.92742 | 0.92813 | 0.92760 | yes |
| **signed** h = e^{−t}(1+1.2 sin 20t) on [0,12] (min h = −0.149, f ≥ 0) | 0.8706 | 1.63700 | 1.65673 | ≈1.638 | yes |
| signed h: 2(1−t)−¼P₂, 1−1.4t, 1−1.6t, e^{−t}(1+1.3cos12t), 2(1−t)(1+1.3 sin30t), (1−t)(1+1.25cos25t) | — | — | — | f takes negative values (min f from −4e-7 to −1.9) | no (excluded) |
| (1+t²)^{-3/2}/2 (heavy tail, m_1=1) | 1/2 | 1.0525 (L=160) | 1.0569 | ≈1.05, still rising with L | yes |
| (2/π)(1+t²)^{-2} | 0.6366 | 0.97548 | 0.97676 | 0.9755 | yes |
| Cauchy 1/(π(1+t²)) | 1/π | C−L = 4.02, 4.77, 5.60 at L = 10, 40, 160 | | ∞ (m_1 = ∞) | no |
| Fejér sinc² | 1 | C−L = 1.29, 1.43, 1.57 at L = 10, 40, 160 | | ∞ (m_1 = ∞) | no |
| box 1_[−½,½] | 1 | C/L ≥ 1.35 (L=20) | | slope > 1 | no |
| Epanechnikov ¾(1−t²)_+ | 3/4 | C/L ≥ 1.20 (L=20) | | slope > 1 | no |

For decreasing nonnegative h, the values agree with the closed form ab = 2∫th·∫h² (signed and
positive capacities coincide via the renewal construction). For example, (p+1)(1−t)^p gives
2(p+1)²/((2p+1)(p+2)), with its minimum 8/9 at p = 1.

### 3.2 Random kernels

All 500 random nonnegative piecewise-linear even f (12 iid U(0,1) nodes on [0,1]) have f̂ < 0
somewhere (exact transform on ξ ∈ (0,40]; median min f̂/f̂(0) = −0.25). By finding 3 they are outside the class, with
slope > 1. Random PD in-class kernels came from the optimiser's random starts (h ~ U(0,1) on 24–36 cells): the initial a·b were
1.10–1.26.

### 3.3 Optimiser (≥ 20 parameters)

(μ,λ)-evolution strategy with step adaptation. Objective a·(C_lo − L) on node-aligned grids, which is a rigorous lower bound
for the represented kernel, so the search was biased *toward* finding values below 8/9.

Families: f = h*h~ with h piecewise constant (signed allowed, f ≥ 0 enforced on nodes,
infeasible = penalty), and f = Σ c_k (1−|t|/w_k)_+/w_k with c_k = e^{p_k}, w_k = k/24.

| family (params) | grid, L | starts → best a·b per start | best |
|---|---|---|---|
| H: 24 cells on [0,1] | cell/3, L=6 | ramp 0.889275→0.889260; near-flat 0.930→0.889282; rand 1.119→0.889320; rand 1.145→0.889264; (1−t)³ 0.915→0.904868 | 0.889260 |
| T: 24 triangle weights | cell/3, L=6 | equal 1.193→0.889590; rand 1.260→0.892045; rand 0.911→0.890464; narrow 1.133→0.896180 | 0.889590 |
| H: 32 cells on [0,1] | cell/2, L=6 | rand 1.105→0.889150; rand 1.096→0.889115; ramp+noise (infeasible)→0.889102; 2 signed starts stuck infeasible | 0.889102 |
| HL: 36 cells on [0,3] | cell/2, L=15 | rand 1.130→0.889178; rand 1.104→0.889078; peak+shoulder 1.471→1.183498; two-scale 1.252→0.897450; 2 signed starts stuck infeasible | **0.889078** |

Each best kernel is a ramp-like autocorrelation. The HL optimum uses the whole length-3 support. The size of the excess
is explained exactly: for the piecewise-constant ramp h_i = 2(1 − (i+½)/M), a decreasing nonnegative h,
ab = 2∫th·∫h² = 2(1/3 + 1/(6M²))(4/3 − 1/(3M²)) = 8/9 + 2/(9M²) + O(M⁻⁴). This is 0.889275 for M = 24, which is the
"ramp" start above, and 0.889106 for M = 32. The optimiser improves on it only by about 1e-5. Nothing approached
8/9 from below.

### 3.4 Discretisation error, quantified

*Exact ramp, a·(C − L) at L = 10* (exact value 8/9 = 0.888889):

| δ | a·(C_lo−L) | a·(C_hi−L) | slope-corrected |
|---|---|---|---|
| 0.02 | 0.88720 | 0.89486 | 0.88898 |
| 0.01 | 0.88847 | 0.89039 | 0.88891 |
| 0.005 | 0.88878 | 0.88927 | 0.88889 |

C_lo has error ∝ L·δ² (the bulk kink of f_0 at 0). Richardson extrapolation at L = 12 gives b = 0.66666666. C_hi converges at O(δ).

*Optimiser optima (piecewise-linear f, node-aligned grid):* C_lo = C_hi to 6 decimals for grid = cell/2, cell/4 and cell/8,
and for L = 6, 10 (support 1) or L = 18, 30 (support 3). For example, HL36 gives 0.889079 / 0.889078 and H32 gives 0.889102 at every
refinement. These numbers are therefore certified brackets for C(L) − L, up to floating point. The convergence in L is
exponential: the change from L = 6 to L = 10 is ≤ 1e-6.

So the smallest value found, 0.889078, exceeds 8/9 by 1.9e-4. That is the M⁻² cell effect and not a discretisation
artefact. No observed value is below 8/9 by more than the documented grid error on the exact ramp.

## 4. Can "C_f(L) = L + b + o(1)" fail for admissible-looking kernels?

Yes, in three ways. The theorem treats all three correctly by excluding them, and R1 shows they need not be excluded.

1. **f ≥ 0 but not positive definite.** If f̂(ξ_0) < 0, the trial (1 + cos 2πξ_0x)dx
   gives C_f(L) ≥ L/(1 + f̂(ξ_0)/2) + o(L). So the slope exceeds 1 and no finite intercept exists.
   I confirmed this numerically for the box (predicted slope 1.122, trial 1.126, local QP ≥ 1.35) and
   Epanechnikov (1.045 / 1.051 / ≥ 1.197). Consequence: **the "larger class" of Theorem 1
   consists automatically of positive-definite kernels** (f̂ ≥ 0, f continuous ⇒ PD ⇒ |f| ≤ a). The proof
   does not use PD, as the document says, but the class is not larger than PD (R2).
2. **m_1 = ∞** (Cauchy, Fejér sinc²): C − L ≥ M_1(L) → ∞, as §2 already notes.
3. **Slow but genuine convergence** (triangle: 1 − 1/(4L+4) at half-integers. Here C_lo = C_hi exactly,
   grid-independent, so the value is certified. The heavy tail (1+t²)^{-3/2} drifts by +5.7e-3, then +3.0e-3, per doubling of L, roughly ∝ 1/L.)
   These satisfy the hypothesis, but they show that the o(1) is not uniform and may be only O(1/L).
   §7 already says this.
   I found no PD kernel with m_1 < ∞ for which C − L fails to converge. I did not prove that
   none exists.

## 5. Remarks (non-blocking)

* **R1 (recommended strengthening).** The proof gives, with no intercept hypothesis,
  liminf_{L→∞}(C_f(L) − L) ≥ 8/(9 f(0)) for every even nonnegative f ∈ C_0 ∩ L¹ with ∫f = 1 and f(0) > 0. If m_1 = ∞,
  this follows from C ≥ L + M_1(L). Otherwise (5.1)–(5.3) hold verbatim, with lim replaced by liminf.
  Stating it this way makes the §7 barrier cover every fixed nonnegative kernel. A Sidon bound needs an upper bound,
  that is the limsup along L = N/T. This includes kernels whose intercept does not exist.
* **R2.** In §1, "Autocorrelation and positive definiteness are not needed" is true of the proof.
  However, the finite-intercept hypothesis itself forces f̂ ≥ 0 (item 4.1). Suggested wording: "...are not
  *used*; the hypothesis forces f̂ ≥ 0".
* **R3.** Theorem 2's remainder 360e^{−αL} with α = log(4/3) is correct but very loose. The observed rate is
  about 2.1, and the bound is vacuous for L < 20.5. This matters only if someone wants explicit
  Sidon onsets from it. The document does not claim any.

## 6. What I did not verify

* The weak-derivative computation AB = … in §4 symbolically, term by term. I checked the operator
  identities and the ODE/uniqueness steps by hand, and the resulting identity (4.2) numerically to
  1e-7 on [0,8]. Beyond 8 the identity rests on the proof.
* Any claim of uniqueness of the extremal (the document makes none) or of global optimality outside the
  fixed-kernel scalar capacity method.
* §9 (process claims about the author's workers) and §10 (literature/priority). I did no G2 or
  literature search.
* The numerics are floating-point, without interval arithmetic. The optimiser is a heuristic local
  search over finite families. It supports the theorem but proves nothing.
* No Lean formalisation. No human review.

Cost: one agent session. Python CPU time was about 25 CPU-minutes, an estimate summed from process times,
with at most 2 concurrent processes and peak RSS under 0.2 GB. Scripts are in the session scratchpad and not committed.
They are qp.py, kernels.py, suite*.py, opt*.py, refine.py, weightD*.py, trialcheck.py, nonpd2.py and ramp_small.py.
No paid or cloud resources were used, and nothing was installed.
