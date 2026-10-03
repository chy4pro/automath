DONE — analytic core PASS-WITH-REPAIRS; hand improvement PASS. The 0.83 certificate and explicit onset are CONDITIONAL / not independently replayed. Novelty PARTIALLY KNOWN; a quantitative note is a candidate after the remaining gates.

# Erdős #156: referee, certificate audit, and bounded G2 check

Date: 2026-10-03 UTC. Task 046a, appended to task 046. Input: PROBE_MAXSIDON_CLAUDE_20261003.md and its code directory. This third report path is inferred from the two specified sibling report paths.

The root and three informed reused workers divided analysis, source comparison, and static code/finite checking. These reviewers are the same vendor as each other and different from the Claude probe. Python, NumPy, SciPy and mpmath are unavailable in this worker environment; no dependencies were installed. The large branch-and-bound runs were not repeated. A source statement or model's run tally is not an independently verified certificate.

## Decision table

Here s(N) is the smallest size of an inclusion-maximal strong Sidon subset of [1,N]. Pair sums include diagonal pairs and are indexed by unordered multisets. This is neither maximum Sidon cardinality nor the weak finite-field convention.

| Statement | Correctness verdict | Novelty / delivery decision |
|---|---|---|
| Lemma 1, all but O(k^2) points have >=2 ordered b+c-a representations | PASS | KNOWN blocking framework; the explicit exceptional-set formulation is elementary |
| Weak-limit reduction liminf s(N)^3/N >=2/lambda_* | PASS-WITH-REPAIRS to the last regularity step | PARTIALLY KNOWN compactness/covering method; precise cubic formulation not located |
| Hand lambda_*<=0.954 | PASS, with exact proof below | PARTIALLY KNOWN machinery; specific numerical improvement not located in bounded search |
| Lemma 3, all three PSD constraints and monotonicity | PASS | KNOWN moment/localizer machinery; cubic application only partly overlaps located prior work |
| Proposition 4, infeasibility at lambda=0.83 | PASS-WITH-REPAIRS as a conditional certificate argument; computational premise OPEN in this review | No encoding error found; no retained leaf artifact or independent replay |
| Theorem 5, constant (2/0.83)^(1/3) | PASS as an implication of Proposition 4; CONDITIONAL as a delivered theorem | PARTIALLY KNOWN machinery; specific constant not located or independently proved |
| Corollary 6, onset N>=3*10^11 | PASS-WITH-REPAIRS, CONDITIONAL on repaired certificate verification | Exact vector norms must be checked; explain the combined rounding slack or use the simpler bounds below |
| Lemma 7, diameter about 2.062 times covered interval | PASS-WITH-REPAIRS to a sign case; sharper exact output 33/16 | KNOWN/subsumed by classical >2.4344 difference-basis consequences |
| Exact table N<=67 | PASS as agreement with known published data; partial independent replay only | KNOWN; public data now extend through 183 |
| Numerical lambda_* about 0.71792 | OPEN / numerical candidate only | No rigorous optimum or method ceiling proved |
| Original #156 upper-bound question | OPEN | No removal of the logarithm |

“Not located” is a bounded search outcome, not a NEW priority certificate. The project has an unconditional hand lower bound available from this review,
\[
 \liminf_{N\to\infty}\frac{s(N)}{N^{1/3}}
 \ge (1000/477)^{1/3}=1.2798543247\ldots,
\]
but no explicit onset is supplied for that compactness corollary here.

## Covering and continuous transfer

Let A be maximal strong Sidon, |A|=k, and f(x)=#{(b,c,a) in A^3:b+c-a=x}, with b,c ordered. Take
\[
 E=A\cup\{2b-a:a,b\in A\}\cup
 \{x\in\mathbb Z:2x=b+c,\ b,c\in A,\ b\ne c\}.
\]
Then |E|<=k+k^2+k(k-1)/2; the probe's looser 1.5k^2+k is safe.

For x outside E, a nontrivial pair-sum equality after adjoining x cannot contain x on both sides, cannot contain it twice on one side, and cannot use b=c. Thus x+a=b+c with b!=c, giving the two distinct ordered representations. This proves k^3>=2N-3k^2-2k. The sharper classical total-block count N<=(k^3+k)/2 is also available; the looser displayed inequality is sufficient for the transfer.

Define nu_mu=mu*mu*tilde(mu), and define lambda-covering by measure domination
\[
 \nu_\mu\ge\lambda\,{\rm Leb}|_{[0,1]}.
\]
This is well-defined even if nu_mu has atoms or singular parts. An “essential infimum of the density” must refer to the density of its absolutely continuous part; a density of the whole convolution need not exist.

To reprove the transfer from an upper bound lambda_*<=lambda_0, with lambda_0>0, suppose along a sequence k^3/N is bounded above by a fixed constant smaller than 2/lambda_0. For the empirical measures mu_N=k^(-1)sum_{a in A}delta_{a/N}, pass to a weakly convergent subsequence on [0,1]. Then nu_mu_N converges weakly as well. For every nonnegative continuous test function phi on [-1,2],
\[
 \int\phi\,d\nu_{\mu_N}
 \ge\frac2{k^3}\sum_{x\in[1,N]\setminus E}\phi(x/N).
\]
The omitted mass is O(k^2/k^3)=o(1), and the Riemann sum converges. Since 2N/k^3 stays above a fixed lambda'>lambda_0, the limit dominates lambda' Leb on [0,1], a contradiction. This avoids the probe's insufficient invocation of Lebesgue outer regularity alone. Alternatively use outer regularity of nu when extending the interval inequality.

The same asymptotic transfer works for arbitrary A_N with [1,N]\(A_N+A_N-A_N) of size o(N). On a subsequence where k=O(N^(1/3)), the at most k^2 diagonal-representation values 2A-A are negligible; outside them any representation has b!=c and therefore comes in two orders. The factor two does not itself require Sidon. Maximal strong Sidon supplies the almost-covering condition. This extension must be stated with these asymptotic quantifiers.

## Exact hand proof of lambda_*<=0.954

Let chi(t)=integral e^(-2pi i tx)dmu(x). If mu is lambda-covering, write nu=lambda Leb|_[0,1]+rho, where rho>=0 has total mass 1-lambda. Since nu-hat(t)=chi(t)|chi(t)|^2,
\[
 |\chi(1)|^3\le1-\lambda,\qquad
 |\chi(1/2)|^3\ge(1+2/\pi)\lambda-1=:R.
\]
Every unit-modulus random variable Z satisfies
\[
 |EZ^2|\ge2|EZ|^2-1.
\]
Rotate Z so its mean is nonnegative real, use Re(EZ^2)=2E(Re Z)^2-1, and apply Jensen. Therefore
\[
 (1-\lambda)^{1/3}\ge2R^{2/3}-1
\]
whenever R>=0.

Set lambda=477/500. Using pi<22/7,
\[
 R>1543/2750,\quad
 (1543/2750)^2-(17/25)^3=2957/7562500>0.
\]
Hence 2R^(2/3)-1>9/25. But (1-lambda)^(1/3)=(23/500)^(1/3)<9/25. Contradiction. Monotonicity excludes every larger lambda as well.

The probe's nearby 0.9535 cutoff can also be certified rationally: pi<355/113, lambda=1907/2000, R>397967/710000, and
\[
 (899/2500)^3-93/2000=10199/15625000000>0,
\]
\[
 (397967/710000)^2-(3399/5000)^3
 =15472828091/630125000000000>0.
\]
These give (1-lambda)^(1/3)<899/2500<2R^(2/3)-1. The weaker 0.954 headline above suffices to answer the requested hand-bound audit; the strengthened hand consequence is (4000/1907)^(1/3)=1.2800779973....

## Fourier certificate: valid framework, incomplete delivered verification

For c_j=chi(jh), c_-j=conj(c_j), and ell_j=integral_0^1 exp(-2pi i jhx)dx, the Toeplitz matrices formed from c_j and c_j|c_j|^2-lambda ell_j are PSD, as Fourier moments of mu and rho. The third sequence is the Fourier transform of
\[
 [\cos(2\pi h(x-1/2))-\cos(\pi h)]\,\mu.
\]
This multiplier is nonnegative on [0,1] for 0<h<=1. Its coefficients are exactly
\[
 g_j=\tfrac12e^{-i\pi h}c_{j-1}
 +\tfrac12e^{i\pi h}c_{j+1}-\cos(\pi h)c_j.
\]
The matrix sizes and available indices in the code agree with this formula. Feasibility at a larger lambda implies feasibility at every smaller lambda, by adding the PSD Lebesgue Toeplitz matrix.

The static review found the signs, conjugations, affine localizer coefficients, and cubic interval expressions consistent. A leaf with a rigorously negative upper bound for v*Tv excludes its box for any nonzero v; normalization is unnecessary for asymptotic infeasibility.

However:

- code/verify.py:13 regenerates leaves with bnb.run rather than reading a retained certificate. No leaf archive or run log was present in the supplied directory. The claimed 1,084,724 leaves and zero failures are probe-reported, not replayed measurements here.
- verify.py:16–24 encloses the decimal lambda and uses h as its exact binary64 value. This is a legitimate parameter choice; it must be recorded with the artifact.
- verify.py:29–36 converts eigenvector coordinates exactly and computes their quadratic correlations. This does not make the vector exactly unit length.
- verify.py:62–72 checks the raw inequality v*T2v<-delta. Corollary 6 instead uses a margin for a unit vector. The checker must certify v*T2v<-delta||v||^2, or separately certify a sufficient norm bound, such as ||v||^2<=1.01 with the adjusted perturbation budget below.
- verify.py:48–56 checks exact dyadic volumes and disk leaves. Midpoint subdivision and exhaustion of the search stack supply the tiling argument. A volume sum alone would not prove coverage for an arbitrary externally supplied list with overlaps; a retained artifact needs its subdivision tree or an independent nonoverlap/coverage check.
- The printed minimum margin is rounded to a float for display; the validity check uses the interval bound. A publication artifact should retain exact/directed bounds, not just that printed decimal.
- A feasible-center return or maximum-box exit cannot be mistaken for success: verify.py rejects every return other than INFEASIBLE. No unsound inference was found in that control flow.
- verify.py:92 prints NOT_VERIFIED without a nonzero process exit status. Automation must check the actual verification result. test_bnb.py only prints its discrepancy diagnostic; verify_sanity.py's enlarged boxes also change total volume, so its overall rejection alone is a weak negative control. None of these diagnostics was replayed here.

The smaller 0.853 and 0.843 certificates have the same replay qualification. This review supplies no numerical infeasibility PASS for any of them.

## Repair of the explicit onset

Assume a verified certificate at lambda_0=0.85, n=3, h equal to binary64 0.65, with normalized T2 margin delta=0.003. The finite empirical measure makes T1,T3 exactly PSD and makes
\[
 T_2'=T_2(\lambda_N)+\lambda_N\Delta
\]
PSD, where lambda_N=2N/k^3 and
\[
 \sum_{j=-3}^3|\Delta_j|
 \le 7|E|/N+24\pi h/N.
\]
The individual coefficients 9.3 and 49 are below their separate estimates, approximately 9.3104 and 49.0088. This does not make the combined bound false: slack in the leading coefficient 18.6 can absorb both discrepancies. The written derivation should explain that compensation. A simpler termwise safe replacement is
\[
 \sum|\Delta_j|
 \le18.7N^{-1/3}+9.4N^{-2/3}+50/N.
\]
Indeed k<=(2N/0.85)^(1/3)<(4/3)N^(1/3), h<21/32, and pi<22/7 give this with rational slack.

For completeness the original combined estimate also checks exactly: putting r=(40/17)^(1/3)<13301/10000 gives (21/2)r^2<18.577 and 7r<9.311; pi<355/113 and h<6500001/10^7 give 24pi h<49.009. For x=N^(-1/3)<=1, the two excess terms are at most (0.011+0.009)x, absorbed by 18.6-18.577.

For N>=3*10^11, the counting bound forces k>=8000 under the relevant contradiction hypothesis, so lambda_N<=1+3/k+2/k^2<1.04. Also N^(1/3)>6600. Consequently the fully conservative rational upper bound is
\[
 1.04\cdot1.01\left(18.7/6600+9.4/6600^2+50/(3\cdot10^{11})\right)
 <0.002977<0.003.
\]
Thus even a separately certified norm bound ||v||^2<=1.01 would suffice for raw margins 0.003. The onset survives these repairs in principle. It is not yet independently certified without checking the actual leaves and their norms.

The exact target is s(N)>(40/17)^(1/3)N^(1/3), whose coefficient is 1.3300573168.... The rounded weaker statement s(N)>1.33N^(1/3) follows. An equality sign between the irrational coefficient and 1.3300 should be replaced by an approximation.

## Difference-cover lemma and ancillary scope

The end-piece argument in Lemma 7 is sound once beta=L/D<=1/3 is handled separately. For beta>1/3 the lower bound on both end-piece sizes is positive, and the resulting inequality is
\[
 \tfrac12\ge\beta+
 \left(\sqrt{2\beta}-\sqrt{(1+\beta)/2}\right)^2-o(1).
\]
It simplifies to beta<=16/33+o(1), or D>=(33/16-o(1))L. This sharpens the rounding in the probe, but is not a useful new bound.

The classical difference-basis constant
\[
 \gamma=2-2\inf_{t\ne0}\sin(t)/t=2.4344\ldots
\]
gives |C|^2>=(gamma-o(1))L for arbitrary integer difference bases C. Combined with the Sidon bound |C|^2<=D+O(D^(3/4)), it yields D>=(gamma-o(1))L. If D/L is unbounded the conclusion is immediate; otherwise the error is o(L). [Bernshteyn–Tait, Theorems 1.2–1.3](https://arxiv.org/pdf/1901.09411) records this and a further strictly positive improvement. Thus the probe's 2.062 lemma is subsumed.

The lifting lemma is valid, but its hypotheses force m=3L+1 and diam(A)=L: integer triple sums lie in an interval of at most 3L+1 integers and must cover all m residue classes, while m>=3L+1. A strictly smaller containing arc is impossible. A support ratio 1/3 pertains to the longest target interval, not all its shorter subintervals.

The estimated optimizer 0.71792 and the proposed two-scale profile remain numerical. Finite-grid local optima neither prove the continuous optimum nor establish a ceiling for the method. Assertions that every coarse profile is realizable by Sidon sets, or every random-like construction must pay a logarithm, need separate proofs and must remain heuristic. The upper-bound targets remain open.

The sixth-moment observation needs a substantive correction. The full sum_x f(x)^2 is ordered three-sum energy; trivial permutations contribute 6k^3-9k^2+4k, not approximately 2k^3. For strong Sidon A, f(a)=2k-1 for every a in A. After removing x in A, the remaining trivial contribution is 2k^3-5k^2+3k. Restrict the statement accordingly, and do not promote a heuristic saturation observation to a general barrier. Likewise, covering without triple collisions is an extra construction ansatz, not a consequence of Sidon.

## Current sources and publication gate

[Ruzsa 1998](https://doi.org/10.1023/A:1009757824153), read in its primary [author DVI](https://www.renyi.hu/~ruzsa/cikkek/sidmax.dvi) during dossier045 and in a scanned article during this audit, already uses the two blocking equations m=a+b-c and 2m=a+b. Do not present the basic almost-covering framework as new.

[Bernshteyn–Tait 2019](https://arxiv.org/pdf/1901.09411), Lemma 2.1, Lemma 3.2 and §3, is close methodological prior: Fourier Toeplitz positivity, uniform covered mass plus a positive residual, and higher-frequency PSD contradictions. Its convolution is mu*tilde(mu), not the cubic convolution here. The specific cubic numerical constants were not located in the bounded search.

[Redman–Rose–Walker](https://arxiv.org/pdf/2109.00292) treats a weak convention in characteristic two; its theorem does not transfer to strong integer Sidon sets. The [day report](https://erdosproblemaday.com/day/156-maximal-sidon-log-factor) discusses related coverings and finite data without the located constant improvement. The [fresh live page and entire thread](https://www.erdosproblems.com/forum/discuss/156), read at about 02:31 UTC, still show OPEN and one September 16 cyclic-data comment. An empty proof-claims page is not priority evidence.

The table through 67 agrees with [OEIS A382397's b-file](https://oeis.org/A382397/b382397.txt). The current source-reported table extends through 183; [Huber's eight-mark threshold paper](https://oeis.org/A399118/a399118.pdf) gives 144. Those larger computations were not replayed here. Cyclic thresholds are different quantities.

Recommendation: unlike the other two probes, this is a plausible short quantitative-note candidate, because a strictly improved hand constant is proved and no matching constant was located. A publishable note must choose its actual headline: the hand theorem can stand without B&B; the 1.3406558 / effective 1.3300573 headlines require the repaired retained certificate and independent replay. Cite the known covering and PSD machinery, remove novelty packaging around the diameter lemma, and complete a final targeted priority check. Do not publish a mere referee/version update. No external posting or publication was performed or authorized by this report.

## Actual independent checks and artifact identification

Analytic worker: one dependency-free Node process, measured 0.833 s, final RSS 59,338,752 bytes. It exhaustively enumerated 106,721 nonempty strong Sidon subsets of [1,30], checked 121,910 maximal ambient-set pairs, 1,083,092 covering-multiplicity cases, and 1,154,339 endpoint cross-pair cases. It reproduced the full minimum table through N=30 and verified all five displayed witnesses. Rational Jensen and onset arithmetic passed.

Code worker: a separate Node process, reported 131 ms. It checked 108 exact BigInt/rational Toeplitz/localizer identity cases for n=2,3,4; all 131,070 subsets across N=1..16; 87,240 blocked-point/direct-Sidon legality comparisons; and 30,113 nested-set pruning comparisons at N=16. It reproduced the small table through 16 and verified witnesses for N=22,42,43,66,67. That worker did not establish the exclusion ranges 17..67 independently; across both workers, minimum claims beyond 30 were not replayed.

The exact search uses the blocking bound B(k)=(k^3+k)/2. The pruning difference B(k)-B(i) is valid because every newly blocked point is generated by a new formal blocker expression containing a newly added element; an increment in the number of such expressions bounds the increment in blocked points. Monotonicity of s(N) was not assumed.

Source SHA256 at review:
- probe: ea3ab2eb92ccc3a893255d9ca05390f6230ba6bd25750be7510352e0fbe6462a
- code/bnb.py: a82f52b27a872c3b4f934513f17a913281bdcf7b9fc9bacbda1372ec20b3093d
- code/verify.py: a3113313bff35642352d387d92088307a2dca93e18689d6c7d0fd32a8b16326e

No files in the probe/code directory were modified. No Python certificate, external finite-data certificate, or kernel proof was replayed. Peak memory and billing were not measured.
