DONE — PASS-WITH-REPAIRS; headline bound KNOWN/subsumed. Recommend a corrected repository note only.

# Erdős #1: adversarial referee and bounded G2 check

Date: 2026-10-03 UTC. Task 046. Input: PROBE_DSS_CLAUDE_20261003.md. This is an informed review: one reused worker rederived the specified proofs, and the root independently checked their main chains and current primary literature. The reviewers are the same vendor as each other, but different from the Claude probe. No kernel formalization, external certificate replay, publication, or push occurred.

## Decision by statement

Write M=a_n, beta(m)=binom(m,floor(m/2)), rho=sum_i a_i^2/(nM^2), U=sum_i(1-a_i/M), and J(t)=integral_{-1}^1 (1-|s|)cos(pi s/2)^t ds.

| Statement | Correctness | Novelty decision |
|---|---|---|
| Theorem 1: M >= 2 beta(n-1), n>=2 | PASS | KNOWN: explicitly subsumed by Costa–Della Fiore's stronger bandwidth theorem |
| Additional +1 when M and sum_i a_i have equal parity | PASS | PARTIALLY KNOWN: elementary lattice refinement; the located stronger bound covers it for n>=4, while n=2,3 can be checked directly |
| Odd-n factor (n+1)/n over beta(n) | PASS | KNOWN: appears inside the exact odd formula of the stronger theorem |
| Corollary 1, including coefficient -1/(4n) | PASS | KNOWN/subsumed as a bound; the proof is a valid elementary derivation |
| Lemma F: M >= 2^(n-1)J(rho n) | PASS | PARTIALLY KNOWN: classical Fourier/variance ingredients; exact triangular-kernel formulation not located in bounded search |
| Lemma F's uniform relative O(n^-1/2) error | FAIL as written | Replace with an error in t=rho n, or assume rho is bounded below |
| Theorem 3(i): M >= (beta(n)-1)/U | PASS | PARTIALLY KNOWN: elementary middle-layer packing; exact formulation not located |
| Theorem 3(ii): M >= 2^(n-1)J(n-U) | PASS | PARTIALLY KNOWN: follows from Lemma F and exponent comparison |
| Theorem 3(ii)'s uniform relative O(n^-1/2) error | FAIL as written | Replace with an error in t=n-U |
| Two-regime consequence for fixed epsilon in (0,1) | PASS-WITH-REPAIRS | Compare to a fixed multiple of n before taking asymptotics |

The exact integral inequalities survive unchanged. “Exact formulation not located” is not a positive novelty certification. Theorem 2 and every ancillary obstruction in the probe are outside this specific audit; they have not received a blanket PASS.

## Correctness and repaired proofs

**Theorem 1.** Signed sums X=sum epsilon_i a_i are distinct, nonzero, symmetric, and lie in the single lattice coset s+2Z, where s=sum a_i mod 2. Delete M and write Y=sum_{i<n} epsilon_i a_i. Exact folding gives
\[
 \#\{|X|<M\}=2\#\{-2M<Y<0\}.
\]
Indeed X=Y+M belongs to the window exactly when -2M<Y<0, and X=Y-M belongs exactly when 0<Y<2M. Antipodality equates the two counts.

The negative halfspace of Y has 2^(n-2) vertices. An inner-boundary vertex has Y in (-2a_{n-1},0), and Harper's half-cube boundary bound gives at least beta(n-1) such vertices. Finally,
\[
 \#((s+2\mathbb Z)\cap(-M,M))
 =M-\mathbf1_{\{M\equiv s\pmod2\}}.
\]
This proves the stated bound and parity refinement, with strict endpoints preserved.

The half-cube consequence of Harper is valid in both parities. In dimension 2k, take all levels below k and then the k-sets containing a fixed coordinate; the external boundary has 2 binom(2k-1,k)=binom(2k,k) vertices. Inner boundary follows by complementation.

The adjacent binomial identities are
\[
 2\beta(n-1)=\begin{cases}\beta(n)&2\mid n,\\
 (1+1/n)\beta(n)&2\nmid n.\end{cases}
\]
Corollary 1's Stirling step can be made explicit. For n=2k put x=1/(8k), y=1/(2880k^3), z=x+y<1. The stated Stirling remainder yields a factor exceeding exp(-z). Since y<=x^2/3,
\[
 e^{-z}\ge1-z+z^2/2-z^3/6\ge1-x.
\]
For odd n=2k+1 the probe's squared comparison has excess (32k^2-14k+1)/(128k^3)>0. These are proofs, not extrapolations from a finite table.

**Lemma F.** With Fourier transform integral K(x)e^(-2pi i x xi)dx, the kernel is
\[
 K(x)=\frac1{4M}\left(\frac{\sin(\pi x/(4M))}{\pi x/(4M)}\right)^2,\qquad
 \widehat K(\xi)=(1-4M|\xi|)_+.
\]
Its lattice periodization is exactly sum_j K(s+2j)=1/2: all nonzero Fourier coefficients of the periodization vanish. Decay O(x^-2) justifies the periodization. Injectivity and K>=0 imply sum_epsilon K(X(epsilon))<=1/2.

For phi(x)=-log cos(sqrt(x)), on 0<=x<(pi/2)^2,
\[
 \phi''(x)=\frac{u\sec^2u-\tan u}{4u^3}\ge0,\quad u=\sqrt x,
\]
because u-sin(u)cos(u)>=0. Convexity and phi(0)=0 yield, throughout the kernel support,
\[
 \prod_i\cos(2\pi\xi a_i)\ge
 \cos(2\pi\xi M)^{\sum_i a_i^2/M^2}.
\]
Fourier inversion and s=4M xi now give M>=2^(n-1)J(rho n).

**Uniform replacement.** For every real t>=1,
\[
 \max\{0,\sqrt{8/(\pi(t+2))}-8/(\pi^2t)\}
 \le J(t)\le\sqrt{8/(\pi t)}.
\]
Consequently J(t)=sqrt(8/(pi t))(1-delta_t), where
\[
 0\le\delta_t\le\min\{1,2/\sqrt t\}.
\]
To prove this, set I_t=integral_{-1}^1 cos(pi s/2)^t ds. Integration by parts gives I_{m+2}=(m+1)I_m/(m+2), I_0=2, I_1=4/pi, and I_m I_{m+1}=8/(pi(m+1)). Monotonicity and m=ceil(t) give I_t>=sqrt(8/(pi(t+2))). The inequality cos u<=exp(-u^2/2) bounds I_t above by sqrt(8/(pi t)), and bounds the subtracted |s|-weighted integral above by 8/(pi^2t). Finally (1+2/t)^(-1/2)>=1-1/t gives the displayed relative error.

Thus the correct asymptotic parameter is rho n in Lemma F, and n-U in Theorem 3. Either may stay bounded while n grows.

**Theorem 3.** Since n>=2 and the positive integers are distinct, U>0. On a middle signed layer, sum epsilon_i is fixed, while
\[
 X=M\sum_i\epsilon_i-\sum_i\epsilon_i(M-a_i).
\]
The beta(n) distinct values have spacing at least two and lie in an interval of length 2MU. Hence MU>=beta(n)-1. Also sum_i(a_i/M)^2<=sum_i a_i/M=n-U; since J decreases, Lemma F implies (ii).

The powers-of-two family is a counterexample to both original uniform error claims. For M=2^(n-1),
\[
 \rho n=(4M^2-1)/(3M^2)\to4/3,\qquad n-U=2-1/M\to2.
\]
The advertised asymptotic bounds would respectively imply M>=(1-o(1))sqrt(6/pi)M and M>=(1-o(1))(2/sqrt(pi))M, both impossible.

For U>=epsilon n, monotonicity first gives J(n-U)>=J((1-epsilon)n). When (1-epsilon)n>=1 the explicit valid replacement is
\[
 M\ge\sqrt{2/\pi}\frac{2^n}{\sqrt n}(1-\epsilon)^{-1/2}
 \left(1-\frac2{\sqrt{(1-\epsilon)n}}\right).
\]
The U<=1-epsilon consequence follows directly from (i). The asserted hard window survives in this fixed-epsilon sense.

## Bounded novelty and freshness audit

**Decisive source:** Costa–Della Fiore, [A bandwidth refinement of the Erdős distinct subset sums bound, v1](https://arxiv.org/html/2609.27941v1), Theorem 1.1 and Lemma 3.1. It proves
\[
 M\ge H_n:=\sum_{j=0}^{n-1}\beta(j).
\]
Putting Gamma_r=sum_{j=1}^{r-1} binom(2j,j)/(j+1), its exact formulas are
\[
 H_{2r}=\binom{2r}r+\Gamma_r,\qquad
 H_{2r+1}=2\binom{2r}r+\Gamma_r.
\]
Thus H_n>=2beta(n-1), strictly for n>=4. This directly settles the requested headline novelty question. The source-displayed date is 22 August 2026, despite the identifier beginning 2609; do not infer its date from the identifier.

The root independently checked the transfer: ordering all integer subset sums makes every cube-edge rank gap at most its weight a_i, hence at most M. The classical cube-bandwidth formula supplies H_n. Telescoping adjacent central-binomial terms verifies the two formulas above. This checks the short application, not a kernel proof of the classical bandwidth theorem.

[Dubroff–Fox–Xu, v2](https://arxiv.org/html/2006.12988v2) was read, including both proofs and the final isoperimetric paragraph. The located finite conclusion is beta(n); no odd-case footnote was found. [Steinerberger, v2, §§2–3](https://arxiv.org/html/2208.12182v2) develops Fourier/variance and Gaussian arguments. It supplies closely related analytic context, but the exact J(rho n) formulation was not located there. Consequently the probe cannot claim the Fourier method, the variance perspective, or the leading constant as new.

The [live page and complete comment thread](https://www.erdosproblems.com/forum/discuss/1) were freshly read. The page now labels the original conjecture DISPROVED (LEAN), an external status change; this session did not verify that construction or replay its formalization. The lower-bound paragraph still gives the older central-binomial expression. Do not use that stale paragraph to override the newer primary paper. The [day report](https://erdosproblemaday.com/report/1) is SKIPPED, based on an earlier OPEN/collision snapshot, and contains no relevant proof.

Bounded MathOverflow checks included [sumset-distinct numbers](https://mathoverflow.net/questions/442361/sumset-distinct-numbers) and [minimum real subset-sum difference](https://mathoverflow.net/questions/355046/minimum-real-number-for-subset-sum-difference). No additional exact triangular-kernel statement was located. This is a bounded search, not an exhaustive priority certificate.

## Actual finite verification

One worker ran a dependency-free Node process, with a 512 MiB V8 heap cap, no files or dependencies, measured wall time 56.411 s, and final RSS 96,464,896 bytes. These are execution measurements, not billing or peak-memory measurements.

All 15,399 DSS subsets of [1,24] of cardinality at least two were checked: counts by size 2 through 6 were 276, 1892, 6972, 6258, 1. The audit independently reconstructed subset sums, signed sums, cube neighbors, the exact folding count, parity occupancy, and Theorem 3(i)'s layer range. All 6647 cases satisfying the stronger parity condition passed. Exact exponent comparisons for (ii) passed.

| Size | Search maximum | DSS sets | Minimum maximum |
|---|---:|---:|---:|
| 3 | 6 | 14 | 4 |
| 4 | 9 | 21 | 7 |
| 5 | 15 | 31 | 13 |
| 6 | 26 | 53 | 24 |
| 7 | 46 | 9 | 44 |
| 8 | 85 | 7 | 84 |

The DFS appends a when (subset_sum_bitset << a) has no intersection with the current bitset. Fixed-size pruning used only cardinality and total-sum packing. Independent signed-sum reconstruction checked the retained sets. Also checked: 10,000 exact Taylor/odd-polynomial pairs, 999 binomial identities, and 39 powers-of-two parameter pairs. No numerical quadrature was used as proof.

## Recommendation

Keep the repaired proof and the failure of uniform asymptotics in the repository research record. Do not issue a standalone Zenodo record-improvement note: the headline is already subsumed, while the parameterized observations have neither a proved new headline gain nor completed priority clearance. The original conjecture is not claimed solved by this probe or this review.

