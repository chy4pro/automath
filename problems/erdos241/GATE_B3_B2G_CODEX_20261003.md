DONE — Task 043 bounded INFORMED gate; four compatibility families audited. NO-GO for a full campaign; no improved leading constant or new record claimed.

# Compatibility gate: B3 and B2[g]

Started 2026-10-03 00:18:58 UTC. This is the informed arm. No `PROBE_*` file has been read. Source reading is restricted to the four works cited below and Costa's version metadata. Independent derivations and dependency-free small numerical experiments are separated from source computational claims.

## Exact questions and the two different relaxations

For B3, equality of three-term sums, including repeated elements, must identify the two multisets. Write `R3(N)` for the maximum size of such a subset of `{1,...,N}`. For B2[g], every integer has at most g unordered sum representations `a+b`, `a<=b`, including diagonals; g is fixed and `Lambda_g=limsup R2[g](N)/sqrt(N)`. These are sum conditions, not the already-completed difference-g-thin condition.

Ordinary convolution is denoted by `*`; `~f(x)=f(-x)`. Green uses a different correlation convention. We define the signed-triple quantities directly, so no odd-convolution sign is inferred from an extracted formula. All continuous norms are on the real line unless a periodic Fourier polynomial is explicitly specified.

### B3: the scalar energy program

White's admissible class is

`F+ = {f in L1(R): f>=0, supp(f) subset [-1/2,1/2], integral f=1}`,

and its objective is `E(f)=||f*f||_2^2`. There is no triple-peak constraint in this scalar minimization. Green's finite representation argument, combined with White's transfer, gives a leading coefficient at most `(2/K)^(1/3)` from a valid energy lower certificate K. The safely rounded rational supplied by Rechnitzer's theorem is

`K=5746396071515195/10^16`, hence `(2/K)^(1/3)=1.51546116978632...`.

Rechnitzer's lower certificate also applies to real signed unit-mass functions. We do not identify the signed and nonnegative infima merely from that fact. Its reported 128-digit computation was not replayed. The finite smoothing proof below independently explains the nonnegative-profile transfer and the information it loses.

Sources READ: [Green, §2 and Lemma 16](https://www.impan.pl/shop/publication/transaction/download/product/82571); [White, Corollary 1.2 and §5, online 2023-07-05](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8D109D51F271CC78EBDA2C99FB35612D/S0008439523000565a.pdf/an_optimal_l2_autoconvolution_inequality.pdf); [Rechnitzer, Theorem 1, 2026-02-07 v1](https://arxiv.org/html/2602.07292v1). READ means inspected statements/relevant arguments, not a full proof or certificate audit.

### B2[g]: exact continuous problem, then a finite SDP below it

Put `G={f>=0: integral f=1, supp(f) subset [-1/4,1/4]}` and

`Cmix_g=inf_G max(||f*f||_infinity, alpha_g ||f*f||_2^2)`, `alpha_g=2g/(2g-1)`.

Costa's Proposition 2.4 gives `Lambda_g^2<=4g/Cmix_g`. Its finite program is only a lower relaxation of Cmix; it is not an equivalent definition of the continuous problem. For g=6,d=9, the author claims a rational lower certificate

`h_6,9 >= 3129912493639957/2400000000000000 = 1.304130205683315...`,

giving `Lambda_6<4.289880000`. This remains a LIVE CLAIM with its computational certificate unreplayed here.

Here is the complete constraint set of Costa (35), in our notation. For k=1,...,d let `mu_k=a_k-i b_k`, `mu_0=1`, `mu_-k=conj(mu_k)`, `w_k=1-k/(d+1)`, and `nu_j=(mu_(j-1)+mu_(j+1))/2`. Set

`Tf=(mu_(i-j))_(0<=i,j<=d)`, `Tnu=(nu_(i-j))_(0<=i,j<d)`, `y=(1,a_1,...,a_d,b_1,...,b_d)`.

The variables are real T, Omega, a, b, real symmetric M of size 2d+1, real eta_k, and Hermitian Q of size d+1. Minimize T subject to

```
M >=PSD 0, M00=1, M0k=a_k, M0,d+k=b_k;
s_k=Mkk+M_d+k,d+k, [[eta_k,s_k],[s_k,1]] >=PSD 0;
Tf >=PSD 0, Tnu >=PSD 0, Q >=PSD 0;
tr Q=Omega-1;
sum_(i=0)^(d-k) Q_i,i+k
  =-w_k(Mkk-M_d+k,d+k)+2i w_k M_k,d+k;
Omega>=12937/10000, T>=Omega;
T>=alpha_g(1+2 sum_k eta_k).
```

The g=5,d=7 program (33) takes Omega=T and omits the numerical floor. A genuine density supplies `M=yy^T`, `eta_k=|mu_k|^4`. The finite program drops rank one, the positive quartic tail beyond d, and replaces the actual convolution peak by its Fejer-smoothed peak.

Source READ: [Costa, Propositions 2.2–2.4 and §4, equations (33),(35)](https://www.researchgate.net/publication/414188555_IMPROVED_BOUNDS_FOR_GENERALIZED_SIDON_SETS). [Figshare metadata](https://api.figshare.com/v2/articles/33549037) identifies v1, published 2026-09-10 15:46:29 UTC. No later source is imported into this gate.

For clarity, the integer-to-continuous step keeps two constraints simultaneously. For fixed g, take a sequence `N -> infinity` with `m_N^2/N -> A>0`. The empirical probability measures on [0,1] have a subsequential limit mu. The ordered-sum bound `r(s)<=2g` gives a density of `mu*mu` bounded by `2g/A`. The identity `sum r^2=sum d^2` and removal of the zero-difference contribution m^2 give `||mu*~mu||_2^2 <=(2g-1)/A`. One can prove the latter using step densities of height `N d(t)/m^2` on cells of width 1/N, omitting t=0; the omitted mass is 1/m. Weak L2 compactness and Plancherel identify the two energies.

No density for mu itself is assumed. Translate, mollify by a probability kernel on [-epsilon,epsilon], then compress the support from length `L=1+2epsilon` to length 1/2. Both the convolution infinity norm and squared L2 norm multiply by `2L`. Letting epsilon tend to zero proves `A<=4g/Cmix_g`. This subsequence argument gives no explicit finite onset.

## Candidate 1: retain the entire B3 signed-triple cap

Let `a=1_A`, `k=|A|`, `r=a*~a`, `t=a*a*~a`, `q=r*r`. For every nonempty B3 set,

`t(x)=2k-1` for x in A, and `t(x)<=2` for x outside A.

Proof: B3 implies B2 by adding a fixed element. If x is in A, the B2 equality `a+b=c+x` forces the same unordered pair, giving 2k-1 orders. If x is outside A, two signed representations imply `a+b+c'=a'+b'+c`. Multiset uniqueness and `c notin {a,b}` force c=c', then equality of the positive pair. There are at most its two orders. Thus

`t<=2+(2k-3)1_A`, and `q(d)<=2k+(2k-3)r(d)`.

If `N_j -> infinity`, `k_j^3/N_j -> beta>0`, and the empirical measures converge to mu on [0,1], then

**`mu*mu*~mu <= (2/beta) dx`.**

Indeed, the exceptional signed-triple atoms on A have total mass `(2k-1)/k^2 ->0`. Every remaining lattice atom has mass at most `2/k^3`; its evaluation against a nonnegative continuous compactly supported test function is bounded by a Riemann sum tending to `(2/beta) integral phi`. Compact support permits passage through convolution. This is a measure inequality, with no density assumption on mu.

Finite quantitative transfer: let integer u>=1, epsilon=u/N, `psi=epsilon^(-1)1_[-epsilon/2,epsilon/2]`, and `f=mu_A*psi`. For k>=2,

```
||f*f*~f||_infinity <= 2N/k^3 + 3(2k-3)/(4k^2 epsilon),
E(f)                <= 2N/k^3 + 2(2k-3)/(3k^2 epsilon).
```

Proof: for j>=2, `sum_z psi^{*j}(x-z/N)=N`; first tile with the box, then convolve with probability kernels. Also `||psi^{*3}||infinity=3/(4epsilon)` and `||psi^{*4}||infinity=2/(3epsilon)`. Apply the finite t and q inequalities and use `sum r=k^2`. The smoothed support has length at most 1+epsilon.

Define `tau=inf_{f>=0, integral f=1, supp f subset [0,1]} ||f*f*~f||infinity`. Compress the smoothed support; choose `u=ceil(N^(5/6))`. On any relevant subsequence `k asymp N^(1/3)`, the support and spike errors are O(N^(-1/6)), hence

`limsup R3(N)/N^(1/3) <= (2/tau)^(1/3)`.

The pointwise finite observation was already in Green. Its full content is omitted from the scalar energy optimization. Nonimplication is explicit: the uniform density on [0,1] has E=2/3 but triple peak 3/4; at beta=3 it satisfies the scalar cap but fails the triple cap. This proves strict inclusion of feasible sets somewhere, not a strict gap at their minima.

Since `E(f)=integral f(x)(f*f*~f)(x) dx`, one has `tau>=inf_F+ E>=K`. A coefficient 1.51 would require `tau>=2/1.51^3=0.580897027...`; 1.50 would require `tau>=16/27`. These are conditional sensitivities, not established improvements. Numerical comparison is recorded below.

A useful redundancy check: for arbitrary complex weights on a B3 set, multiset counting gives

`integral_0^1 |sum_a w_a exp(2pi i a theta)|^6 dtheta = 6S2^3-9S2 S4+4S6`,

where `Sj=sum_a |w_a|^j`. The multiplicity patterns 1+1+1, 2+1, 3 contribute respectively 36,9,1 times their monomials, proving the identity. Its macroscopic weighted inequality has constant 6/beta. The triple cap already gives the same family with constant 2/beta: push forward `mu^3` by x+y-z, apply Cauchy–Schwarz to the weight `w(x)w(y)conj(w(z))`, and use the density cap, L2 duality and Plancherel. Therefore these weighted sixth moments add no information after Candidate 1.

Likewise, `q(0)=2k^2-k` and `q(d)=4k-4` for nonzero differences in A-A. To prove the latter, write d=u-v and match the multisets in `a+b+v=c+e+u`; the two pairs must be {u,w} and {v,w}, giving four orders except two at w=u,v. Directly substituting these refinements in the smoothed energy changes only O(1/(k^2 epsilon)) terms, not the leading numerator 2.

## Candidate 2: retain B2[g] diagonal parity defects

Write u(s) for unordered representations and r(s) for ordered ones. Exactly

`r(s)=2u(s)-1_(s in 2A)`, `sum_s r(s)=m^2`.

Thus `E(A)=2g m^2-sum_s r(s)(2g-r(s))`. At each of the m distinct diagonal sums, r(s) is odd between 1 and 2g-1, so its defect is at least 2g-1. All other defects are nonnegative. Consequently

```
E(A) <= 2g m^2-(2g-1)m,
sum_(t!=0) d_A(t)^2 <= (2g-1)m^2-(2g-1)m.
```

This is a genuine integer correction to Costa's aggregate bound. After division by m^2 it vanishes. Its isolated effect on the leading Lambda_g constant is exactly zero. A finite-size correction must not be reported as a new leading bound.

## Candidate 3: enforce rank-one realizability in the finite lift

For every actual empirical profile or density, `M=yy^T` by definition; all its 2-by-2 minors vanish. This is automatic in the exact continuous Cmix problem and is omitted only in the finite SDP.

The following exact elimination makes small comparisons possible without an external SDP package. Define

`c_k=Mkk-M_d+k,d+k-2i M_k,d+k`, `sigma_k=|mu_k|^2+|c_k-mu_k^2|`.

For the original program the objective is equivalently

```
max(12937/10000,
    sup_theta [1+2 Re sum_(k=1)^d w_k c_k exp(i k theta)],
    alpha_g [1+2 sum_(k=1)^d sigma_k^2]).
```

The moment vector still must satisfy the two original moment matrices. Proof: `S=M-yy^T>=PSD0`. The k-th harmonic block has trace at least `|Delta_k|`, where `Delta_k=c_k-mu_k^2`; equality is attained by

`(1/2)[[|Delta|+Re Delta, -Im Delta],[-Im Delta, |Delta|-Re Delta]]`.

These blocks may be assembled independently because the original constraints never use cross-frequency entries of M. Minimize the quartic epigraph at `sigma_k^2`; Fejer–Riesz is exactly the displayed all-angle peak condition. This elimination was independently checked by two workers. It is convex: `sigma(mu,c)=sup_|z|=1 [|mu|^2-Re(z mu^2)+Re(z c)]`, a supremum of convex quadratics. The rank restriction `c_k=mu_k^2` is nonconvex.

Exact zero-gain control, g=6,d=2: take equal point masses at 0, +/-1/4, so `y=(1,1/3,-1/3,0,0)`. At `T=Omega=cKP=12937/10000`, the rank-one M, epigraph `(1/81,1/81)`, and Q with diagonal 979/10000 and every off-diagonal -1/27 satisfy all constraints. Q has least eigenvalue `979/10000-2/27>0`; the energy term is `340/297<cKP`.

A non-rank-one solution at the same objective is `M=yy^T+(1/9)e_b1 e_b1^T`, epigraph `(4/81,1/81)`. Take the same Q diagonal, only Q02=Q20=-1/27 nonzero off-diagonal. Its energy is `364/297<cKP`. This violates rank one. Since the original hard floor is cKP and a rank-one witness attains it, both d=2 optima are **exactly cKP**. Nonrealizable feasible points alone demonstrate no optimum gap.

## Candidate 4: couple the relaxed lift to positive profile moments

Let theta=2pi x, r=floor(d/2), and let z consist of cos(k theta), sin(k theta), k=1,...,r. For an actual profile put `H=E[zz^T]`, `m=E[z]`. The required principal block of M is `m m^T`, and

`H-M_J >=PSD0`.

For a finite empirical profile this follows from the exact identity

`H-m m^T=(1/(2n^2)) sum_(a,b) (z_a-z_b)(z_a-z_b)^T`.

For probability measures use the same double-integral identity. Product-to-sum expresses H through existing moments up to 2r: `H_cos i,cos j=(a_(i-j)+a_(i+j))/2`, `H_sin i,sin j=(a_(i-j)-a_(i+j))/2`, `H_cos i,sin j=(b_(i+j)+b_(j-i))/2`. Thus this is a convex finite cut, valid for every admissible integer set after rescaling. It is not new arithmetic specific to B2[g].

Nonimplication witness at d=2: retain the preceding y and take `M=yy^T+(1/3)e_a1 e_a1^T`, epigraph `(16/81,1/81)`, T=Omega=5/3, and

`Q=(1/27)[[5,-4,-1],[-4,8,-4],[-1,-4,5]]`.

Q is a graph Laplacian, its Fourier diagonal sums match the constraints, and its energy is `460/297<5/3`. But M_a1,a1=4/9 whereas H_cos1,cos1=1/3. The d=2 optimum nevertheless stays cKP by the rank-one control above.

There is a stronger obstruction to using only individual-frequency cuts. At g=6, every such 2-by-2 Jensen cut is already implied throughout

**`T <= 28703/21384 = 1.342265245...`.**

Proof: let t=|mu_(2k)|<=1. The feature second-moment block has least eigenvalue (1-t)/2. If its Jensen inequality fails, `s_k>(1-t)/2`, while `s_(2k)>=t^2` follows from the original Schur constraint. Therefore `sum_j s_j^2>(1-t)^2/4+t^4`. The exact identity

```
(1-t)^2/4+t^4
 = (t-5/12)^2 (t^2+5t/6+25/48)
   +(1/4)(t-91/216)^2+5375/46656
```

gives the threshold after multiplication by 12/11. The first quadratic is positive. Since Tnu implies `(1+a_2)/2<=a_1`, this also rules out a gain from the scalar cut `M_a1,a1<=a_1` in the relevant sublevel. It says nothing comparable about multiple frequencies together.

A second elementary positivity condition is `TC=(c_(i-j))>=PSD0`, c0=1. For a real profile `c_k=mu_k^2`, so TC is the entrywise product Tf o Tf, equivalently the moment Gram matrix of the convolution probability measure. It is omitted from the lifted program: at d=2 set `M=yy^T+(19/9)e_b2 e_b2^T`, epigraph `(1/81,400/81)`, T=Omega=12. Take Q diagonal 11/3, Q01=Q12=-1/27 and Q02=2/3, symmetrically. Diagonal dominance proves Q PSD; energy is `3532/297<12`. Here c=(1/9,-2), and TC has quadratic form -2 at (1,0,1). Again this is a high-objective omission witness. The numerical near-record lift has a strictly positive TC eigenvalue and is not excluded by this cut.

### A concrete four-frequency consequence

For the first four sine coordinates define the rational vector and diagonal matrix

`v=(1/2,-17/25,1/2,-93/500)`, `W=diag(-32,1/8,-1/10,-1/5)`, `Z=v v^T`.

Then Z-W is positive definite. The relevant Schur-complement comparison is exactly

`184960/1472317 - 1/8 = 7363/11778536 >0`.

If `S=M_sine-b b^T` and `Cov=H_sine-b b^T`, the full Jensen condition gives `0<=PSD S<=PSD Cov`. Consequently `tr(W S)<=tr(Z S)<=tr(Z Cov)`, or

**`sum_(i=1)^4 W_i (s_i-Re c_i)/2 + b^T(Z-W)b <= v^T H_sine v`.**

This is convex and uses only moments through frequency eight. Every genuine lift satisfies it. The numerical trial below violates it within the sublevel where one-frequency cuts are automatic; this is a heuristic feasibility diagnostic, not a certified low-sublevel omission witness. In testing it, s must be allowed to exceed sigma: negative W entries permit added covariance to restore feasibility, at an energy cost. Excluding a particular minimal-trace lift is not by itself evidence of an optimum gap.

## Numerical comparison, verification and decision

All decimal optimization results below are **HEURISTIC diagnostics**. An objective at a trial point is an upper value for an infimum over that trial class; it is not a certified lower bound and cannot be inserted into a combinatorial upper-bound theorem as though it were one.

### B3 profile comparison

Equal-bin nonnegative densities were optimized on the simplex using dependency-free floating-point projected gradient/FISTA with backtracking. For m bins, probabilities p and q=p*p, the exact piecewise-linear convolution formula is

`E(f)=(m/3)[2 sum_k q_k^2+sum_k q_k q_(k+1)]`.

The triple peak was evaluated from every quadratic cell's endpoints and interior maximum. A separate peak search used a smoothed sampled maximum, then reevaluated the actual cell maxima. Sampled peaks were not reported as global peaks.

| Bins m | Energy-minimization trial E | Actual triple peak at that energy trial | Best actual peak in the separate search |
|---|---:|---:|---:|
| 16 | .5850738170 | .6034127953 | .5932210411 |
| 32 | .5798406682 | .5926730221 | .5840812581 |
| 64 | .5772359117 | .5862617409 | .5795228046 |
| 128 | .5759366768 | .5823018968 | .5772112353 |

The energy-trial gradient spreads were below 8e-12; this checks a finite-grid stationary point, not a continuum optimum. Peak minimization was local and more delicate; a later variant did not improve these trials and was discarded. Refinement makes the apparent excess over K smaller. No positive lower gap `tau-K` was established.

Rounding the last profile to rational probabilities allowed the **exact** function certificate in the next section: tau<=.57722. Hence the possible coefficient gain from Candidate 1 alone is at most `1.51546116978632-1.513199567163226 ~= .002261603`, and even a positive gain inside that small range is unproved. The 1.51 and 1.50 targets are excluded for this relaxation alone.

Candidate 2 needs no optimizer: its contribution to the normalized B2[g] energy cap is exactly `(2g-1)/m`, tending to zero. At g=6 and m=100,1000,10000 the deficits are .11,.011,.0011, respectively, and the limiting leading-coefficient change is zero.

### Costa finite-grid comparisons

The exact elimination above was used. Moment measures were restricted to n equally spaced points on the half-circle, with simplex probabilities. The Fejer polynomial used 1024 angles during the matched runs, then 32768 angles for checking. These are two different approximations: the location grid restricts moments, while angle sampling relaxes the continuous peak. Neither was silently identified with the source SDP. The source moment constraints were always satisfied by the grid measures.

At d=2 the original and rank-restricted minima are exactly 1.2937, by the rational witnesses above; the small floating-point run reached that value as well. Thus the measured and proved change there is zero.

At d=9, three 65-point rank-one local searches, checked on the dense angle grid, gave approximately 1.340272,1.333003,1.333008; a 33-point run reached 1.331408. These are local feasible values of a nonconvex problem. The apparent gap of about .027 from the relaxed trials is **not a lower gap**. If a future lower certificate reached 1.331, the formula would suggest a Lambda6 improvement of order .04; this gate supplies no justification for expecting that certificate.

Single-frequency Jensen cuts have exactly zero effect throughout the rigorously identified low sublevel. The extra convolution moment matrix TC at the earlier relaxed 65-point trial had minimum eigenvalue about .4310, so it did not cut that point. No global redundancy of TC is claimed.

The four-frequency rational cut did exclude the chosen minimal-trace relaxed trial. To compare optima, the implementation allowed the traces s to increase. For fixed moments and c, write `ell_k=|mu_k|^2+|c_k-mu_k^2|`, `w=(-16,1/16,-1/20,-1/10,0,...)`, and

`B=v^T Hsin v-b^T(Z-W)b+sum_i w_i Re c_i`.

One minimizes `sum s_k^2` subject to `s_k>=ell_k`, `w.s<=B`. A scalar multiplier gives `s_k=max(ell_k,-lambda*w_k/2)`. A first implementation stalled at this nonsmooth transition; its apparent ~.0014 increase is excluded from the evidence. The matched runs instead used a logarithmic barrier and checked its analytic gradients by central differences (maximum absolute discrepancy 9.84e-9 at the tested point).

For barrier parameter eta, minimize `sum[s_k^2-eta log(s_k-ell_k)]`; the scalar solution is

`s_k=(2ell_k-lambda*w_k+sqrt((2ell_k+lambda*w_k)^2+8eta))/4`.

Choose lambda>=0 by bisection if the cut binds. This keeps the full convex comparison and permits the otherwise-missing covariance. The final schedule used softmax temperatures .001,.0002,.00004,.000008,.0000016, eta=.003*temperature, and 6000 projected/backtracking steps per stage. Norms were also smoothed during optimization; the displayed energy was reevaluated without that smoothing or the barrier term.

| Arc points | Constraint | Actual trial objective | Smooth-objective tangent diagnostic gap |
|---|---|---:|---:|
| 65 | Original lifted constraints | 1.3045897315 | 1.753e-4 |
| 65 | With rational four-frequency cut | 1.3046054714 | 1.880e-3 |
| 129 | Original lifted constraints | 1.3045445598 | 1.450e-4 |
| 129 | With rational four-frequency cut | 1.3045684155 | 7.457e-3 |

The diagnostic gap uses a supporting affine function over the simplex and the box `|Re c_k|,|Im c_k|<=.4`; the box contains every original solution with T<=1.4 since `|c_k|<=s_k` and the energy bounds s_k. It diagnoses convergence of the regularized grid problem, not a rigorous interval certificate. These gaps are larger than the observed differences.

The matched differences are about 1.57e-5 and 2.39e-5. The latter would correspond to a Lambda6 change of about 3.92e-5 **if it were a genuine certified denominator increase**. It is smaller than unresolved optimization and location-grid effects, so no positive optimum movement is established. The dense-angle peaks were below the displayed energies; a second-derivative interpolation estimate was below 3.2e-8 in these trials. Angle sampling is therefore not the dominant uncertainty.

### Decision and actual verification

**NO-GO for a full proof campaign on present evidence.** No candidate meets all three requested gates simultaneously: universal validity, omission from the relevant relaxation, and a demonstrated useful optimum change.

| Candidate | Valid for all admissible sets/profiles? | Omitted information | Gain established by this gate |
|---|---|---|---|
| B3 triple cap | Yes, with a finite smoothing proof | Pointwise cap omitted by scalar energy optimization; finite observation already known | No positive gap. Exact tau upper certificate excludes coefficients below 1.513199567 from this route alone. |
| B2[g] parity defect | Yes, exact finite count | O(m) defect dropped in aggregate energy | Leading gain exactly zero. |
| Rank-one lift | Yes, by construction | Removed in finite SDP; automatic in exact Cmix | d=2 gain exactly zero; d=9 nonconvex local trials do not certify a gap. |
| Coupled positive moments | Yes, covariance/Gram proofs | Genuine finite-lift omissions | Individual-frequency cuts provably inactive; one coupled cut has an unresolved ~2e-5 trial difference. |

A further bounded certificate audit could retain the explicit four-frequency cut, but a large search is not justified by a difference smaller than its numerical uncertainty. A useful next gate would need a rational dual lower certificate beyond the current baseline, with the original source certificate and continuum reduction checked. Merely increasing d or retuning the same scalar problem is not recommended. This is not a proof that every possible higher-order compatibility condition is redundant.

Checks performed: the B3 worker tested 814 nonempty B3 subsets encountered for interval lengths 1 through 12, covering 33186 pointwise representation checks and 1628 BigInt weighted identities. Root checked the B2[g] parity inequality on 8178 nonempty subsets and 38336 admissible (set,g) cases, g=1,...,6, with exact energy identities. These finite checks support transcription; the universal results rest on the proofs above.

Root also checked the rational Q/eigenvalue margins, the four-frequency Schur-complement margin, and the 780 inequalities of the explicit B3 function certificate using BigInt. Two workers independently verified the SDP elimination; the coupled cut received a separate exact audit. These are same-vendor reviews. No external source certificate or complete source theorem was replayed, no kernel formalization was performed, and no original conjecture or new leading bound is claimed.

Closed 2026-10-03T00:48:01.346Z, after 29.1 minutes wall time. Three existing informed worker seats were used in parallel. Their final integration reviews passed after adding explicit N-to-infinity quantifiers and qualifying the low-sublevel four-frequency violation as numerical. The B3 function checker was independently extracted from this report and rerun by a second seat; both embedded JavaScript programs were syntax-checked. No PROBE file was read, source computational certificate replayed, local Lean/SAT build run, dependency installed, cloud compute purchased, external message posted or publication made. Only this report and inbox ledgers were written. Global-memory tools/skill were unavailable in the exposed environment; no notice was invented and no preset changed. Token/billing data were unavailable, so no monetary cost is inferred.

## Reproducible exact B3 profile certificate

This is a new finite **function** certificate produced in this gate; it does not certify that any integer B3 sequence has this profile. The 128 bin probabilities are the following 64 integers followed by their reversal, divided by `10^12`. The density on bin i is `128*p_i`.

For `R=n*n*reverse(n)`, on `t=(j+u)/128-1`, `0<=u<=1`, the signed triple density is

`128/(2D^3) [A u^2+B u+C]`,

where `A=R_j-2R_(j-1)+R_(j-2)`, `B=2(R_(j-1)-R_(j-2))`, and `C=R_(j-1)+R_(j-2)`; missing entries are zero. This follows by convolving three unit boxes: their quadratic pieces are `u^2/2`, `(-2u^2+2u+1)/2`, and `(1-u)^2/2`.

The checker compares both endpoints and every interior concave vertex with U=57722/100000 using integers only. At a vertex it multiplies the inequality by the positive number -4A; no square root or floating-point comparison is used.

```javascript
// node: dependency-free exact verification of a feasible triple-peak profile.
const D = 1000000000000n, m = 128n;
const half = [
  51876802493n, 21770963072n, 19296227297n, 15566902210n, 13803974677n, 12439747009n, 11460277253n, 10688107070n,
  10071111061n, 9558072751n, 9126064226n, 8755018678n, 8432825598n, 8149730235n, 7898864935n, 7674768302n,
  7473277418n, 7291049952n, 7125412216n, 6974182024n, 6835563118n, 6708059951n, 6590417203n, 6481572515n,
  6380619875n, 6286781423n, 6199385481n, 6117848781n, 6041662095n, 5970378710n, 5903605154n, 5840993513n,
  5782234984n, 5727054496n, 5675206277n, 5626470151n, 5580648379n, 5537562933n, 5497053176n, 5458973876n,
  5423193539n, 5389592946n, 5358063880n, 5328508003n, 5300835887n, 5274966172n, 5250824841n, 5228344580n,
  5207464208n, 5188128170n, 5170286088n, 5153892376n, 5138905905n, 5125289703n, 5113010699n, 5102039487n,
  5092350127n, 5083919960n, 5076729466n, 5070762136n, 5066004366n, 5062445380n, 5060077152n, 5058894361n,
];
const p = half.concat(half.slice().reverse());
if (p.length !== 128 || p.some(x => x < 0n) ||
    p.reduce((a,b) => a+b, 0n) !== D) throw Error('probabilities');
function conv(a,b) {
  const c = Array(a.length+b.length-1).fill(0n);
  for (let i=0;i<a.length;i++)
    for (let j=0;j<b.length;j++) c[i+j] += a[i]*b[j];
  return c;
}
const R = conv(conv(p,p), p.slice().reverse());
const U=57722n, V=100000n, den=D**3n;
let endpoints=0, vertices=0;
for (let j=0;j<=R.length+1;j++) {
  const A=(R[j]||0n)-2n*(R[j-1]||0n)+(R[j-2]||0n);
  const B=2n*((R[j-1]||0n)-(R[j-2]||0n));
  const C=(R[j-1]||0n)+(R[j-2]||0n);
  for (const value of [C,A+B+C]) {
    endpoints++;
    if (m*V*value > 2n*den*U) throw Error('endpoint '+j);
  }
  if (A<0n && B>0n && B< -2n*A) {
    vertices++;
    if (m*V*((-4n*A)*C+B*B) > (-4n*A)*2n*den*U)
      throw Error('vertex '+j);
  }
}
console.log({endpoints,vertices}); // { endpoints: 768, vertices: 12 }
```

All 780 inequalities passed. Therefore **`tau<=0.57722` exactly**. The best coefficient obtainable solely by the relaxation `(2/tau)^(1/3)` cannot be below

`(2/0.57722)^(1/3)=1.513199567163226...`.

This is a scoped obstruction to that relaxation, not a lower bound on R3(N), not optimality of tau, and not a barrier to other integer compatibility conditions. In particular, this route alone cannot reach 1.51 or 1.50.

## Reproduction of the matched floating-point diagnostics

The following Node program reproduces the four matched grid runs. It has no external dependency. It is a diagnostic optimizer, **not a proof checker**: the returned tangent quantity concerns the regularized grid problem and is not an interval certificate. Only the four calls shown here are part of this experiment. The initial vector is a previously obtained feasible grid trial, with masses placed at matching points upon refinement.

```javascript
const INIT=[0.17488626090434878,0,0,0,0,0,0,0,0,0,0.10882898986549554,0.024628971452121107,0,0,0,0,0,0,0,0,0,0.06296228262011355,0.06475802389276544,0,0,0,0,0,0,0,0,0,0.12787105711153562,0,0,0,0,0,0,0,0,0,0.06475885110459152,0.06296168275455007,0,0,0,0,0,0,0,0,0,0.024627369074492016,0.1088304179585023,0,0,0,0,0,0,0,0,0,0.1748860932614841,0.228511936224974,-0.042157976097865174,-0.06606771922481562,0.058461541990616914,-0.03626493164952156,0.044836268693391,-0.044763917747777306,0.01535264874444571,0.020862518876667596,-1.921967604911225e-7,3.3746406496907697e-8,-3.5743039949359544e-8,1.3889227919689556e-7,1.1238857977220104e-7,-2.777481468654403e-7,8.252460041672086e-8,-1.4244319373979885e-7,3.0321635667315937e-7];

function project(v,n){const u=Array.from(v.slice(0,n)).sort((a,b)=>b-a);let s=0,t=0;for(let j=0;j<n;j++){s+=u[j];let q=(s-1)/(j+1);if(j===n-1||u[j+1]<=q){t=q;break}}let out=v.slice();for(let i=0;i<n;i++)out[i]=Math.max(0,v[i]-t);return out}
function run(n,d,rank=false,seed=0,cut=false){
const grid=1024, ag=12/11, cos=Array.from({length:d},()=>new Float64Array(n)),sin=Array.from({length:d},()=>new Float64Array(n)),pc=Array.from({length:d},()=>new Float64Array(grid)),ps=Array.from({length:d},()=>new Float64Array(grid));
for(let k=0;k<d;k++){for(let j=0;j<n;j++){let th=-Math.PI/2+Math.PI*j/(n-1);cos[k][j]=Math.cos((k+1)*th);sin[k][j]=Math.sin((k+1)*th)}for(let j=0;j<grid;j++){let th=2*Math.PI*j/grid;pc[k][j]=2*(1-(k+1)/(d+1))*Math.cos((k+1)*th);ps[k][j]=2*(1-(k+1)/(d+1))*Math.sin((k+1)*th)}}
const size=n+(rank?0:2*d);
function calc(x,tau,eps,gradient=true){
let a=new Float64Array(d),b=new Float64Array(d),u=new Float64Array(d),v=new Float64Array(d),ss=new Float64Array(d),dx=new Float64Array(d),dy=new Float64Array(d),rho=new Float64Array(d),E=ag;
for(let k=0;k<d;k++){for(let j=0;j<n;j++){a[k]+=x[j]*cos[k][j];b[k]+=x[j]*sin[k][j]}let re=a[k]*a[k]-b[k]*b[k],im=2*a[k]*b[k];u[k]=rank?re:x[n+k];v[k]=rank?im:x[n+d+k];dx[k]=u[k]-re;dy[k]=v[k]-im;rho[k]=Math.sqrt(dx[k]*dx[k]+dy[k]*dy[k]+eps*eps);ss[k]=a[k]*a[k]+b[k]*b[k]+(rank?0:rho[k]);E+=2*ag*ss[k]*ss[k]}


const lower=ss.slice(),ww=[-16,1/16,-1/20,-1/10],vv=[1/2,-17/25,1/2,-93/500],eta=tau*.003;
let lambda=0,Budget=Infinity,dBudgetP=new Float64Array(n),bproj=0;
if(cut){
for(let k=0;k<4;k++)bproj+=vv[k]*b[k];Budget=-bproj*bproj;
for(let k=0;k<4;k++)Budget+=2*ww[k]*b[k]*b[k]+ww[k]*u[k];
for(let j=0;j<n;j++){let h=0;for(let k=0;k<4;k++)h+=vv[k]*sin[k][j];Budget+=x[j]*h*h;let de=h*h;for(let k=0;k<4;k++)de-=2*(vv[k]*bproj-2*ww[k]*b[k])*sin[k][j];dBudgetP[j]=de;}
}
function barrierS(k,l){let w=cut?(ww[k]||0):0;return (2*lower[k]-l*w+Math.hypot(2*lower[k]+l*w,Math.sqrt(8*eta)))/4;}
function ff(l){let z=-Budget;for(let k=0;k<4;k++)z+=ww[k]*barrierS(k,l);return z}
if(cut&&ff(0)>0){let hi=1;while(ff(hi)>0)hi*=2;let lo=0;for(let j=0;j<55;j++){let mid=(lo+hi)/2;if(ff(mid)>0)lo=mid;else hi=mid}lambda=hi;}
for(let k=0;k<d;k++)ss[k]=barrierS(k,lambda);
let ETrue=ag*(1+2*ss.reduce((s,z)=>s+z*z,0));
E=ag*(1+2*ss.reduce((s,z,k)=>s+z*z-eta*Math.log(Math.max(1e-300,z-lower[k])),0));
let vals=new Float64Array(grid+2);vals[0]=1.2937;vals[1]=E;let mx=Math.max(vals[0],E);
for(let j=0;j<grid;j++){let z=1;for(let k=0;k<d;k++)z+=pc[k][j]*u[k]+ps[k][j]*v[k];vals[j+2]=z;mx=Math.max(mx,z)}
if(!gradient)return {T:mx,E,a:Array.from(a),b:Array.from(b),u:Array.from(u),v:Array.from(v),s:Array.from(ss),lower:Array.from(lower),lambda,Budget,ETrue,eta};
let weights=Float64Array.from(vals,z=>Math.exp((z-mx)/tau)),sum=weights.reduce((a,b)=>a+b,0);for(let j=0;j<weights.length;j++)weights[j]/=sum;
let grad=new Float64Array(size),F=mx+tau*Math.log(sum);
for(let k=0;k<d;k++){
let gu=0,gv=0;for(let j=0;j<grid;j++){gu+=weights[j+2]*pc[k][j];gv+=weights[j+2]*ps[k][j]}
let factor=weights[1]*2*ag*(2*ss[k]+lambda*(cut?(ww[k]||0):0)),ga,gb;
if(rank){ga=factor*2*a[k]+gu*2*a[k]+gv*2*b[k];gb=factor*2*b[k]-gu*2*b[k]+gv*2*a[k]}
else{ga=factor*(2*a[k]+(-2*a[k]*dx[k]-2*b[k]*dy[k])/rho[k]);gb=factor*(2*b[k]+(2*b[k]*dx[k]-2*a[k]*dy[k])/rho[k]);grad[n+k]=gu+factor*dx[k]/rho[k]-weights[1]*2*ag*lambda*(ww[k]||0);grad[n+d+k]=gv+factor*dy[k]/rho[k]}
for(let j=0;j<n;j++)grad[j]+=ga*cos[k][j]+gb*sin[k][j];
}
if(cut)for(let j=0;j<n;j++)grad[j]-=weights[1]*2*ag*lambda*dBudgetP[j];return {F,grad,T:mx,E};
}
let x=new Float64Array(size);for(let j=0;j<n;j++)x[j]=seed?(.5+((Math.sin((j+1)*(seed*12.9898+78.233))*43758.5453)%1+1)%1):1;let initSum=x.slice(0,n).reduce((a,b)=>a+b,0);for(let j=0;j<n;j++)x[j]/=initSum;if(!rank){let q=calc(x,.01,.001,false);for(let k=0;k<d;k++){x[n+k]=q.a[k]**2-q.b[k]**2;x[n+d+k]=2*q.a[k]*q.b[k]}}
x=new Float64Array(size);for(let j=0;j<65;j++)x[Math.round(j*(n-1)/64)]=INIT[j];for(let k=0;k<2*d;k++)x[n+k]=INIT[65+k];let phases=[],L=100,iterations=0;
for(let tau of [.001,.0002,.00004,.000008,.0000016]){
let eps=tau*.05,y=x.slice(),tt=1,last=Infinity;
for(let iter=0;iter<6000;iter++){let r=calc(y,tau,eps),z,rz;for(;;){z=project(Float64Array.from(y,(w,i)=>w-r.grad[i]/L),n);rz=calc(z,tau,eps);let dot=0,norm=0;for(let j=0;j<size;j++){let dd=z[j]-y[j];dot+=r.grad[j]*dd;norm+=dd*dd}if(rz.F<=r.F+dot+L*norm/2+1e-12)break;L*=2;if(L>1e14)throw Error('L')}
let tn=(1+Math.sqrt(1+4*tt*tt))/2;
if(rank&&rz.F>last){y=x.slice();tt=1;continue}
y=Float64Array.from(z,(w,j)=>w+(tt-1)/tn*(w-x[j]));x=z;tt=tn;last=rz.F;iterations++;if(iter%80===0)L*=.8;
}phases.push({tau,...calc(x,tau,eps,false)});
}
let rr=calc(x,.0000016,.0000016*.05),dot=rr.grad.reduce((s,g,i)=>s+g*x[i],0),mn=Math.min(...rr.grad.slice(0,n)),cabs=rr.grad.slice(n).reduce((s,g)=>s+Math.abs(g),0);let tangentLower=rr.F-dot+mn-.4*cabs;return {n,d,rank,seed,cut,iterations,phases,x:Array.from(x),smoothObjective:rr.F,tangentLower,gradientCMax:Math.max(...rr.grad.slice(n).map(Math.abs)),final:calc(x,.0000016,0,false)};
}

console.log(JSON.stringify([run(65,9,false,0,false),run(65,9,false,0,true),run(129,9,false,0,false),run(129,9,false,0,true)]));
```
