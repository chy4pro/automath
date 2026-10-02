OPEN — useful-stage envelope and improved M unproved. Three strategy checks completed; general-subset/full-grid obstructions and a coarse fixed-delay deduction are proved, with unextracted numerical onset.

# Envelope route for the actual correlation laws

Task021, 2026-10-02. Ordinary source-informed work. Read E1_EXTENSION, R3, E1_normalization_certified_M and R2_E1b. The task's N4N5N6 path is a typo: the source audit is in phase0, not phase1. Freshness task022 was completed first; its source/version checks are recorded in [FRESHNESS_20261002](/work/inbox/from_codex/FRESHNESS_20261002.md). No new core arXiv versions supplying the missing numerical estimate were found. No paid computation, dependencies, solver or external communication was used.

Three distinct strategy agents completed their checks: direct matrix counting; class-mass/spread and coarse-delay arithmetic; and tensor-Fourier transfer. New-thread creation was limited, but after the direct-count check completed, two existing ordinary seats accepted follow-up assignments concurrently. These were informed reviews of the draft, not clean-room independent discoveries or cross-vendor review. Task020's three fresh isolated attempts were completed before this route material was supplied to any reviewer.

## 1. Exact laws and a general-subset obstruction

Let p≥5 be prime, 2≤N<p, S⊆[N]² of size n>N, and g∈GL2(F_p) have g21≠0. Put

\[
h_{a,b}=U(-b)gU(a),\quad
\nu=n^{-1}\sum_{(a,b)\in S}\delta_{h_{a,b}},\quad
\lambda=\nu*\widetilde\nu,\quad\lambda_k=\lambda^{*k}.
\]

The generators have one fixed nonzero determinant; λ and its powers are probabilities on SL2. When defining ν's Fourier singular norms later, first right-multiply all generators by one fixed matrix of determinant (det g)^-1. This places ν on SL2 and leaves every correlation hh'^{-1}, hence λ, unchanged. The endpoint map is injective because g21≠0. These are the Lemma15 correlation conventions; k counts **pairs**, not individual generators. The least central-envelope constant is

\[
\mathcal B(f)=\sum_C|C|\max_C f,
\]

as proved in E1_EXTENSION and independently in task020. Noncentral classes have size at least (p²−1)/2.

For each a define the row S_a={b:(a,b)∈S}, d_a=|S_a|, and

\[
q=\frac{\sum_a d_a^2}{n^2}\ge\frac1N.
\]

**Proposition.** For every integer k≥1,

\[
\boxed{\mathcal B(\lambda_k)\ge
 \frac{(p^2-1)q^{k-1}(q-1/n)}{4k(N-1)}
 \ge\frac{(p^2-1)(n-N)}{4kn(N-1)N^k}.}
\tag{1}
\]

In particular if n≥2N,

\[
\mathcal B(\lambda_k)\ge\frac{p^2-1}{8kN^{k+1}}.
\tag{2}
\]

**Proof.** Retain the generator pairs with equal a. For such a pair,

\[
h_{a,b}h_{a,b'}^{-1}=U(b'-b),
\]

independently of g. Their subprobability φ≤λ on the upper-unipotent subgroup has mass q, atom φ(I)=1/n, and every atom at most 1/n: for each (a,b)∈S a specified difference determines at most one b'. Hence λ_k≥φ^{*k}; this subprobability has mass q^k and its identity atom is at most q^{k-1}/n by Young's inequality. Its nonidentity mass is at least q^{k-1}(q−1/n).

The upper-unipotent parameters are sums of k differences in [1−N,N−1]. They occupy at most 2k(N−1) nonzero residues, even after modular wrapping. At least one nonzero atom has mass at least the preceding nonidentity mass divided by 2k(N−1). Multiply by its noncentral class size (p²−1)/2. This proves the first inequality. Substitute q≥1/N and q−1/n≥(n−N)/(nN) for the second. For n≥2N use (n−N)/n≥1/2 and N−1≤N. QED.

Thus for N=floor(p^{1/20}) and n≥2N, **each fixed k≤29 fails** every bound Cp^{9/20} and every Cp^{1/2−δ}, δ>0. At k=29 the lower exponent is exactly 1/2. More generally a necessary condition is (k+1)θ≥2−β for an envelope Cp^β. If n≥N^{1+ε} for fixed ε>0, the size condition n≥2N holds once N^ε≥2. These are uniform obstructions for arbitrary g and dense-enough S, not merely the full grid or an integer-lift range. They do not prove feasibility at k=30.

For comparison, at N=floor(p^{1/90}), (2) requires k≥139 for exponent9/20; each fixed k≤138 fails. This is still only a necessary stage condition, not a sufficient one or a claim that all these laws have the application's coset cap.

## 2. Full-grid counts, trace masses and the within-class problem

For the special full-grid W law μ in task020,

\[
h_{a,b}^{-1}=-h_{b,a},\qquad
\widetilde\mu=\delta_{-I}*\mu,\qquad
\lambda_k=\delta_{(-I)^k}*\mu^{*2k}.
\tag{3}
\]

In particular μ is a normal convolution measure, and central translation preserves 𝓑. The clean-room ordinary-power obstruction therefore agrees with (1) on even lengths. Odd ordinary powers are not Lemma15 correlation stages.

Assume 2N−1≤p. Set d=a1−b2, b=b1, a=a2. Then

\[
h_{a1,b}h_{a,b2}=
\begin{pmatrix}-1-bd&b-a-abd\\d&ad-1\end{pmatrix}.
\tag{4}
\]

If d≠0, the output determines d,b,a uniquely, and its mass is (N−|d|)/N⁴ when admissible. If d=0, the output is −U(a−b), with mass (N−|a−b|)/N³. Thus the largest atom is 1/N² at −I, while nonzero-lower-left atoms are at most 1/N³.

Writing T=∑_{d=1−N}^{N−1}(N−|d|)²=(2N³+N)/3, the exact squared L2 mass is

\[
\|\mu^{*2}\|_2^2=\|\lambda\|_2^2
 =\frac{2T-N^2}{N^6}
 =\frac4{3N^3}-\frac1{N^4}+\frac2{3N^5}.
\tag{5}
\]

To check the count: the d=0 outputs contribute T/N⁶; nonzero d contribute (T−N²)/N⁶, because for each d there are N² choices of distinct endpoint outputs. This exact formula includes the identity atom and all ordered pairs.

The direct-count strategy reviewer proves that the same formula for ||λ||₂² holds for **every full-grid g with g21≠0**, not only W. Set γ=g21²/det(g) and d=a−a'. The correlation output is U(-b)gU(d)g^-1U(b'), with lower-left entry −γd. For d≠0 that entry recovers d; upper-left and lower-right then recover b,b'. Its mass is (N−|d|)/N⁴. For d=0 it is U(b'−b), with mass (N−|b'−b|)/N³. The same disjoint count proves (5), with λ's maximum at I. The no-wrap condition 2N−1≤p is retained for this exact formula.

For general g and S the single-pair trace is

\[
\operatorname{tr}(h_{a,b}h_{a',b'}^{-1})
 =2-\frac{g_{21}^2}{\det g}(a-a')(b'-b).
\tag{6}
\]

At trace 2, either a=a' or b=b'. Row/column degree bounds give trace-2 mass at most (2N−1)/n; full grid gives exactly 2/N−1/N². At any other fixed trace, fix (a,b)∈S, then choose a'≠a among at most N−1 possibilities; the trace equation determines at most one b'. This gives mass at most (N−1)/n, hence <1/N on the full grid. In particular n≥N^{1+ε} gives O(N^-ε) mass per trace. These elementary class-mass bounds do **not** give the desired pointwise envelope: (1) already records the concentration within large unipotent classes.

For full-grid data with any g21≠0, the two outer endpoints remain independent uniforms after conditioning on the middle matrix of a correlation word. The same elementary argument as task020 consequently gives

\[
\mathcal B(\lambda_k)\le\frac{(2N-1)p(p+1)}{N^2}
\quad(k\ge1).
\tag{7}
\]

For arbitrary S those endpoint variables are generally conditionally biased; (7) is not asserted without additional work. Trivially any probability on G has 𝓑≤p(p+1).

At k=1, **every full-grid g with g21≠0** and M=floor(N/2) with M²<p satisfy the stronger lower bound

\[
\mathcal B(\lambda)\ge\frac{p^2-1}{72N H_M}.
\tag{8}
\]

For the general-g proof, choose d=a−a' and s=b'−b in [M], with b=1,b'=1+s. The N−d choices of (a,a') give a noncentral atom of mass at least 1/(2N³), of trace 2−γds. Distinct integer products ds≤M²<p give distinct traces. The ordered multiplicative energy of [M] is at most 2M²H_M, by the coprime-factor parametrisation in task020, so there are at least M²/(2H_M) distinct products. Multiplying by minimum class size and using M≥N/3 yields (8). Modular collisions in other representations can only increase these selected atom masses; no additional no-wrap assumption is needed for this lower bound.

This matches (7) in powers of p,N up to a logarithm. Controlling trace masses while discarding the pointwise peaks cannot yield exponent9/20 at this stage.

Strategy(ii) supplies a general warning with a complete example. For each τ∈F_p\{±2}, let gτ=[[0,−1],[1,τ]] and assign mass1/[2(p−2)] to gτ and gτ^-1. The resulting probability is symmetric, has zero central mass, and each occupied trace has mass exactly1/(p−2). Yet choosing a class containing gτ for each trace gives 𝓑≥(p²−1)/4, since these classes are distinct and each contains an atom of the specified size. Thus even trace masses of order1/p do not control the required envelope. This example is not asserted to be an actual walk or to satisfy the full proper-coset cap; it rules out the inference from trace-mass bounds alone.

## 3. Why the R3 reduction cannot simply be tensor-squared

The source-audited R3 reduction uses inversion extended by 0↦0, with unitary Fourier kernel

\[
K_p(\xi,\zeta)=\frac{S(-\xi,\zeta;p)+1}{p}.
\]

For the projector P_X to 0<|ξ|_p≤X, R3 proves

\[
\rho_p(X)=\|P_XK_pP_X\|\le
\min\{1,2\lfloor X\rfloor(2\sqrt p+1)/p\}.
\tag{9}
\]

For disjoint unions A,B of length-N intervals its centered discrepancy is bounded by

\[
\sqrt{|A||B|}\left[\rho_p(X)+2\sqrt{p/(NX)+2/N}\right]+1.
\tag{10}
\]

Thus the physical scale N=p^θ needs a dual block X=p^{1−θ+u}, u>0, to make the indicator tails small. The currently checked [Blomer–Pascadi Theorem1.1](https://arxiv.org/html/2607.24311v1) gives

\[
\rho_p(X)\ll p^{o(1)}
 [X^{1/8}p^{-3/32}+X^{5/16}p^{-3/16}
   +X^{2/3}p^{-7/18}]+2X/p.
\tag{11}
\]

At the already optimistic X=p^{1−θ}, its three exponent savings would be

\[
(4\theta-1)/32,\quad(5\theta-2)/16,
\quad(12\theta-5)/18.
\]

For θ=1/20 all three are negative. The reduction supplies positive savings only in its much larger-interval range θ>5/12, with the tail loss retained. Repeating the same numerical substitution for θ=1/9 or 1/90 does not help. This is a limitation of these checked bounds, not a proof that the true norms have no saving.

More fundamentally, the operator needed by E1_EXTENSION's envelope theorem is the **diagonal group action**

\[
T_f=\sum_g f(g)\,\rho(g)\otimes\overline{\rho(g)}.
\tag{12}
\]

It is not \(\widehat f(\rho)\otimes\overline{\widehat f(\rho)}\), whose expansion averages two independent group elements. For example, for uniform f on G and a nontrivial irreducible ρ, the latter is zero by averaging; (12) is the nonzero projection onto the invariant vector D_ρ^{-1/2}∑e_i⊗ē_i. This gives a direct counterexample to replacing (12) by the tensor square of a one-copy average.

In the projective-line permutation model, simultaneous translations act on pairs (x,y). In additive Fourier coordinates, interval averaging multiplies by a factor at the **sum frequency** ξ+η, rather than independent factors at ξ and η. Thus low sum frequency includes an entire anti-diagonal band of high individual frequencies. A one-copy low-frequency block bound does not cover that coefficient geometry. Further, the projective-line representation alone does not supply every irreducible block needed for a central majorant on G.

Tensor-square centralisation in E1_EXTENSION works because the pointwise majorant F is *already central*, making every irreducible constituent scalar, with its invariant line explicitly accounted for. Reversing that argument to construct F from a one-copy discrepancy estimate is a new step, not a consequence of the existing R3 theorem.

### Representation and boundary checks from strategy (iii)

The tensor reviewer confirmed the foregoing distinction and identified qualifications that must be retained:

- The full projective permutation representation is 1⊕St. Its tensor square has two invariant dimensions, from diagonal/off-diagonal ordered pairs. The one-dimensional invariant statement above concerns an irreducible ρ, including St, not the full permutation representation.
- Every ρ⊗ρ̄ is trivial on the center. It sees f_+(g)=[f(g)+f(−g)]/2. Positivity gives f≤2f_+, hence 𝓑(f)≤2𝓑(f_+); center blindness costs a factor2 if an envelope for f_+ is established, and is not by itself an impossibility result.
- R3's artificial affine inversion fixes0; projective inversion exchanges0 and∞. Its tensor application must treat the infinity-coordinate sectors explicitly. Small rank alone does not bound their operator norm.

With ordinary Fourier labels in both affine coordinates, Q_X projects to |ξ+η|_p≤X and inversion has matrix K_p⊗K_p. With conjugate labels in the second coordinate the strip uses |ξ−η|_p≤X and the kernel is K_p⊗K̄_p; these descriptions agree after relabelling. The strip rank is p(2floor(X)+1), and includes high individual frequencies. Within fixed total input/output frequencies, one encounters correlated products of two Kloosterman kernels, with the relative frequencies ranging over the entire field. The second kernel depends jointly on input/output indices and is not a separate input/output coefficient in the checked one-kernel bilinear theorem.

**Zero-frequency repair.** The initial tensor-review output applied an entrywise Weil estimate to the full strip. Root identified K_p(0,0)=1, and the reviewer confirmed the correction: K_p(0,ζ)=K_p(ξ,0)=0 for nonzero ξ,ζ, while |K_p(ξ,ζ)|≤(2sqrt(p)+1)/p applies on the individually nonzero block. Thus only for

\[
Q_X^\circ=(P_{\ne0}\otimes P_{\ne0})Q_X
\]

does the stated elementary strip estimate follow:

\[
\|Q_X^\circ(K_p\otimes K_p)Q_X^\circ\|
\le\min\left\{1,
 \frac{(2\lfloor X\rfloor+1)(2\sqrt p+1)^2}{p}\right\}.
\tag{T0}
\]

It is still vacuous: the second term has order X. It is not asserted for full Q_X, whose constant pair is present. At θ=1/20 even the easier independent-coordinate BP bound (11) has positive exponents 1/40,7/64,11/45 before smoothing enlargement. Squaring the resulting unitary bound1 cannot improve it.

### A correct direct tensor criterion

For irreducible nontrivial ρ of dimension dρ put

\[
q_\rho(f)=\|T_f|_{\Omega^\perp}\|.
\]

Then for any probability f,

\[
\boxed{\|\widehat f(\rho)\|_{\rm op}^2
 \le\frac1{d_\rho}+(1-1/d_\rho)q_\rho(f).}
\tag{T1}
\]

Indeed Jensen bounds a squared matrix coefficient by the T_f coefficient between v⊗v̄ and w⊗w̄. Each has invariant component dρ^-1/2Ω and perpendicular norm sqrt(1−1/dρ). T_f fixes Ω and preserves its complement; Cauchy–Schwarz gives (T1).

For correlations the exact identities are T_λ=T_ν T_ν*, and T_{λ^{*r}}=(T_ν T_ν*)^r. Hence

\[
\|\widehat{\lambda^{*r}}(\rho)\|_{\rm op}^2
 \le\frac1{d_\rho}+(1-1/d_\rho)q_\rho(\nu)^{2r}.
\tag{T2}
\]

A new uniform input qρ(ν)≤Cp^-δ, C≥1, would therefore give s(λ^{*r})≤p^-c whenever 0<c<1/2 and rδ>c. Using 1/dρ≤3/p for p≥3, a sufficient explicit onset is

\[
p\ge\max\{5,6^{1/(1-2c)},
 (2C^{2r})^{1/(2r\delta-2c)}\}.
\tag{T3}
\]

This supplies a precise possible **spectral** replacement for the envelope goal. The checked R3 estimates do not prove its premise; a constant qρ≤q<1 would require r growing like log p for a p-power saving. Neither (T1) nor (T2) reconstructs a pointwise central envelope. No useful new stage or alphabet improvement follows from the tensor audit.

## 4. A coarse fixed-delay envelope from the existing weak estimate

This subsection records what existing machinery does prove, to avoid confusing “no useful stage” with “no prime-independent stage known”. It is **not a clean-room/direct-counting result and not a new strong flattening lemma**.

Use the proved weaker set estimate and weighted transfer from R2_E1b §A: for symmetric probabilities with full proper-coset cap p^-a and excess squared mass t=||f−1/D||₂²,

\[
t(f*f)\le p^{-2c}t(f)
\]

when p^{-2−4c}≤t(f)≤p^{-h}, provided

\[
0<c<\min\{h/3224,a/23,1/8\}
\tag{13}
\]

and p exceeds an absolute threshold depending on the source's unextracted coefficient. Its source exponents are 1/1611 and 1/11; the 1/20 symmetric-growth theorem was rechecked in task022. The coefficient depends on numerically unextracted growth constants γ and s0. No numerical value of the threshold P_weak is claimed.

**Coarse theorem.** Let f be any symmetric probability on SL2(F_p) satisfying f(xH)≤p^{-1/30} for every proper subgroup H and every coset xH. Then for all sufficiently large p,

\[
\boxed{\mathcal B(f^{*2^{98353}})<2.}
\tag{14}
\]

A sufficient onset is p≥max{P_weak,5,3^{120000}}, where P_weak is the unextracted onset in (13) at h=a=1/30,c=1/100000. Both the constant2 and the delay98353 are explicit; the total numerical prime onset is not. This is a deduction from the previously proved weak-SE theorem, not a replacement for its coefficient extraction.

**Proof.** The trivial subgroup gives ||f||∞≤p^-a and t(f)≤p^-a. The full coset cap persists through convolution on either side, because translated right cosets may be rewritten as left cosets of conjugate subgroups. Set c=1/100000. It satisfies (13), since 1/100000<1/96720=h/3224. After

\[
j=98335=\left\lceil\frac{2-1/30}{2/100000}\right\rceil+1
\]

doublings,

\[
t_j\le p^{-2-v},\qquad
v=1/30+2j/100000-2=1/30000<4c.
\tag{15}
\]

If an earlier iterate crosses the lower cutoff p^{-2−4c}, Young contraction preserves an even stronger estimate; otherwise apply (13) at each step.

For any probability, the quasirandom Fourier estimate in E1_EXTENSION gives t_next≤A t², A=2p(p+1). Let Q=A t. Then Q_next≤Q². At (15), Q≤3p^-v for p≥2; the displayed onset gives Q≤p^{-3v/4}. After 18 further doublings,

\[
Q\le p^{-(3v/4)2^{18}}=p^{-4096/625}\le p^{-4},
\qquad t\le\tfrac12p^{-6}.
\]

Finally ||f−1/D||∞≤sqrt(t) and hence

\[
\mathcal B(f)\le1+D\sqrt t<1+1/\sqrt2<2.
\]

This proves (14). The 98,353 doublings are symbolic, not an executed computation. QED.

The class-mass reviewer checked the weak-transfer bookkeeping as well as the delay. For clarity, write η=1/1611, θ_SE=1/11 and L=ceil(log₂(32p³))+2. Once the elementary range prerequisites in R2_E1b hold, a sufficient condition for its dyadic contradiction is

\[
C_{\rm weak}\left[
2^\eta(512L^4)^{1+\eta}p^{-\epsilon_1}
 +(512L^4)^{1+\theta_{\rm SE}/2}p^{-\epsilon_2}
 +2(512L^4)^2p^{-\epsilon_3}\right]\le1,
\]

where at the displayed a,h,c,

\[
\epsilon_1=h\eta-2c(1+\eta)=\frac{41}{60412500},\quad
\epsilon_2=a\theta_{\rm SE}-c(2+\theta_{\rm SE})
 =\frac{9931}{3300000},\quad
\epsilon_3=1-8c=\frac{12499}{12500}.
\]

All are positive, so an absolute eventual P_weak exists. The first is very small. The numerical C_weak, hence a numerical P_weak, has not been supplied; writing this condition is not a numerical onset certification.

For the actual correlations, the theorem applies **once an actual seed with the full cap p^-1/30 is proved**. A seed f=(ν*ν̃)^{*m0} then reaches (14) at pair length m0·2^98353. The theorem is an implication from the stated cap, not an assertion that every arbitrary subset S already satisfies it.

## 5. Spectral/alphabet ledger and remaining gates

The tensor-envelope theorem, already independently checked in task018, gives

\[
s(f)^2\le f(Z)+5\mathcal B(f)/\sqrt p.
\tag{16}
\]

If f(Z)≤p^-1/30 and 𝓑(f)≤Cp^{9/20}, then s(f)≤p^-1/120 for

\[
p\ge\max\{5,2^{60},(10C)^{30}\}.
\tag{17}
\]

At an actual pair length m=2^d m0≤b2^d log_N p, Fourier positivity gives s(f)=s(ν)^{2m}. Thus

\[
\kappa_{14}=\frac1{240b2^d},
\tag{18}
\]

with no further flattening stages needed after the envelope. The limiting ledger overhead is O_B=705672/25; the concrete R=40, ε=1/20 overhead is 31680, and the strict integer rule is M0>198/κ14, M=160M0.

| Actual seed convention, if certified | Envelope delay d | Conditional concrete alphabet |
|---|---:|---|
| b=1/20 | any proved useful d | M=380160·2^d+160<2^{19+d} |
| b=1/4 | any proved useful d | M=1900800·2^d+160<2^{21+d} |
| b=1/20, using only coarse (14) | 98353 | M<2^{98372} |
| b=1/4, using only coarse (14) | 98353 | M<2^{98374} |

The coarse theorem's B<2 allows C=2 in (17). Its enormous delay is worse than the campaign baseline and does not justify another campaign merely to refine this bookkeeping. The center bound required in (16) for actual correlations is preserved as f(Z)≤1/n (no opposite generator pairs); it must be checked against p^-1/30 for the chosen actual seed. Alternatively a full coset cap bounds center mass directly since Z is a proper subgroup.

The two b conventions have different source seed hypotheses. A full-grid W result alone cannot replace the actual Lemma14 family s_j=V(2j)U(-2j), or all subsets S in Lemma15. Task018 already gives an actual capped Lemma14 family ruling out a uniform d=4 envelope. Equations (1)–(2) now give a direct complementary obstruction for the Lemma15 subset families. Neither furnishes a sufficient small d.

No number in this table is a certified new Zaremba theorem: actual seed length/cap, leading coefficients, downstream assembly and total prime onset remain explicit gates. In particular P_weak is unspecified numerically. A theorem with a numerical exponent but missing coefficient/onset is not a fully effective result.

## 6. Review status

Root derived the subset obstruction, W counts, tensor-action distinction and coarse-delay implication. The three requested strategy checks completed as follows:

| Strategy | Check and contribution | Scope |
|---|---|---|
| Direct counts | Checked (1)–(6); extended (5),(8) to arbitrary full-grid g | No useful upper envelope obtained |
| Class mass/spread | Checked weak-transfer margins, 98,353 delay and alphabet arithmetic; supplied flat-trace/high-envelope example | Prior weak-SE/growth theorem treated as supplied proved input; no new source or kernel replay |
| Tensor Fourier | Checked the correlated-action distinction; supplied representation/boundary qualifications and (T1)–(T2) | Initial full-strip Weil application corrected after root identified zero-frequency exception; final bound restricted to Q_X° |

The tensor review correction is incorporated explicitly above; it did not affect (T1)–(T2), the counting results or the coarse-delay proof. None of the reviewers established a useful stage or certified a new M. Source novelty and independent kernel formalisation are not claimed.

Root also ran bounded dependency-free exact integer counts in Node (Python is unavailable): six W ordinary two-step norm cases; 234 selected subset/matrix cases checking pointwise retained-submeasure domination and its mass/identity bounds at pair powers1,2; and 18 full-grid general-g correlation norm cases. Primes were5,7,11, N=2,3, with g=W, [[0,1],[1,0]], [[1,2],[1,3]]. Subset masks were those divisible by17 and the full mask, restricted to n>N. All checks passed. Counts stay within exact integer range; these finite cases check signs/multiplicities, not the asymptotic theorem or kernel formalisation. The two commands reported wall times below0.01 seconds each; no CPU/RSS or dollar-cost estimate is asserted.
