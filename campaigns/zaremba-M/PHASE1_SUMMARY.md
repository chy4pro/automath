DONE — Phase 1 closed at K2; no improved fixed digit cap certified.

# Zaremba explicit-M campaign: Phase 1 close-out

2026-10-02. Task 024. **K2: agree with stopping the designed routes.** The campaign has not certified an improved fixed digit cap, a complete numerical prime onset, or the original conjecture. The stopping decision concerns the present methods and their checked obstructions; it is not a global impossibility claim. The targets \(c=1/120\) and \(c=1/468\) for general noncentral flattening remain open under the appropriate hypotheses.

The useful outputs are explicit restricted theorems, quantitative counterexamples to particular reductions, two source audits of the displayed numerical chain, and conditional dependency calculations. None currently meets the campaign's announce threshold \(\log_2 M\le500\) with a proved new input and the remaining certification gates closed. The latest source sweep found no new numerical Zaremba constant in its inspected scope; that is not a priority certificate. [Task and K2 instruction](/work/inbox/to_codex/024_zaremba_phase1_summary.md); [campaign ledger](ledger.md); [October 2 source sweep, §1](/work/inbox/from_codex/FRESHNESS_20261002.md).

This summary supersedes shorthand in the historical coordinator ledger where qualified below. It does not modify that ledger or STATUS. The reports linked below contain the full proofs and their primary-source records. This close-out reads those reports; it is not another independent literature search or proof referee.

## 1. Conventions and exact proved results

Throughout the group results, \(G=\mathrm{SL}_2(\mathbb F_p)\), \(D=p(p^2-1)\), \(Z=\{\pm I\}\), counting-measure convolution is used, and
\[
t(\mu)=\|\mu-D^{-1}\|_2^2=\|\mu\|_2^2-D^{-1}.
\]
Set energy counts ordered quadruples, including diagonal ones:
\[
E(A)=\#\{(a,b,c,d)\in A^4:ab^{-1}=cd^{-1}\},\qquad
\alpha(A)=\max_{x,H<G}|A\cap xH|/|A|.
\]
A full proper-coset cap includes the trivial subgroup and the center. For an actual correlation \((\nu*\widetilde\nu)^{*m}\), \(m\) counts pairs, hence \(2m\) source factors. Ordinary powers of the full-grid measure in task020 are a different length convention.

### Central E1: complete restricted theorem, standard Fourier corollary

For every central probability \(\mu\), \(p\ge5\), without a symmetry assumption,
\[
t(\mu*\mu)\le[\mu(Z)+5p^{-1/2}]^2t(\mu).
\]
If \(\mu(Z)\le p^{-a}\), \(0<c<\min(a,1/2)\), then coefficient-one contraction \(t(\mu*\mu)\le p^{-2c}t(\mu)\) holds for
\[
p\ge\max\{5,\ 2^{1/(a-c)},\ 10^{1/(1/2-c)}\}.
\]
There is no energy cutoff. At \(a\ge1/30,\ c=1/120\), \(p\ge2^{40}\) suffices. This is a genuine squared-mass gain \(p^{-1/60}\), not a same-numeral \(K_*^{-c}\) gain. It is not a Zaremba prime onset.

The proof is the standard central-Schur Fourier identity, character-column orthogonality, noncentral centralizers of size at most \(2p\), and nontrivial degree at least \((p-1)/2\). Task019 located the printed central Fourier identities and their immediate SL2 specialization. It did not identify a new general flattening principle.

Review: two isolated same-model referees, one proof/source check and one finite/adversarial check, followed by root comparison. The latter tested **787 exact rational central measures**, including 304 nonsymmetric samples, at \(p=3,5,7,11,13,17,31\). All passed the bracket comparison; all 684 center-capped samples with \(p\ge5\) passed the power target. All sampled primes were below the theorem's onset, and \(p=3\) was outside its domain; its \(Q_8\) power-target failure is not a theorem counterexample. These are finite checks, not cross-vendor review or kernel formalization. [E1 proof](phase1/R2_E1.md); [normalization, §1](phase1/E1_normalization_certified_M.md); [referees and G2, §§1–4](phase1/REFEREE_E1.md).

### General set energy: weaker theorem and exact limits of its transfer

For nonempty symmetric \(A\), the proved fallback is
\[
\frac{E(A)}{|A|^3}\le C_{\rm weak}
\left[|A|^{-1/1611}+\alpha(A)^{1/11}+\frac{|A|}{D}\right].
\]
This deduction uses BSG and symmetric growth. Its coefficient is explicit as a formula, but not numerically extracted. Namely, with
\[
u=2^{-26},\quad v=2^{188},\quad w=2^{162},
\]
\[
C_0=\max\left\{(s_0/u)^{1/11},u^{-1/11},
\left(\frac{v^{20}}{\gamma^{20}u}\right)^{1/1611},
w^{1/69}\right\},\qquad
C_{\rm weak}=\max\{(1+2^{1/69})C_0,4\}.
\]
Here \(\gamma>0,s_0\ge1\) are the unextracted constants in the symmetric generating-set growth theorem: for \(|S|\ge s_0\), either \(S^3=G\) or \(|S^3|/|S|\ge\gamma|S|^{1/20}\).

For symmetric probabilities with full cap \(p^{-a}\), the proved weighted transfer allows
\[
0<c<\min\{h/3224,\ a/23,\ 1/8\},
\qquad p^{-2-4c}\le t(\mu)\le p^{-h},
\]
and gives \(t(\mu*\mu)\le p^{-2c}t(\mu)\) for all sufficiently large primes. The lower cutoff is essential: stopping at \(p^{-2+2c}\) alone does not cross the strict Frobenius threshold.

Thus \(c=1/32241\) is a valid concrete choice **at \(h=1/10\)** and \(a=1/24\) or \(1/30\), with unextracted growth constants/onset. The campaign has not certified that initial entropy for the actual walk. This number is not a universal best exponent or a barrier to a stronger theorem. At the cap-only entropy \(h=a=1/30\), the report instead uses \(c=1/96721\).

The desired estimate with exponents \((1/20,1)\) remains unproved and unrefuted for arbitrary symmetric \(A\). If it held, the same transfer would allow \(c<1/420\) at \(h=1/10\), subject to the other constraints. [Weak theorem and coefficient, R2_E1b §§A1–A3](phase1/R2_E1b.md); [updated ledgers, normalization §7](phase1/E1_normalization_certified_M.md).

### Restricted cases of the stronger set-energy target

Task017 supplied complete ordinary proofs, with root checking after three fresh same-model attempts:

| Domain | Exact proved result |
|---|---|
| Every nonempty \(A\), odd \(p\) | \(E(A)/n^3\le n/D+\frac{2p(p+1)}n(1-n/D)^2\) |
| \(n\ge p^{40/19}\) | Desired \((1/20,1)\) estimate with \(C=8/3\), or convenient \(C=3\) |
| Central sets, \(p\ge37\) | Desired estimate with \(C=1\) |
| Sets in any affine hyperplane of \(\mathrm{Mat}_2(\mathbb F_p)\), odd \(p\) | \(E(A)/n^3\le2(\alpha+n^{-1/2})\); symmetry unnecessary; trace-zero and rank-one cases included |
| \(A_X=\{g:gX\cap X\ne\varnothing\}\), nonempty \(X\subseteq\mathbb P^1(\mathbb F_p)\), \(p\ge5\) | \(E(A_X)/|A_X|^3\le16(\alpha(A_X)+|A_X|/D)\) |

A partition into \(k\) affine-hyperplane pieces gives only \(2k^2(\alpha+n^{-1/2})\). That loss prevents summing the restricted result into an unrestricted theorem with an absolute linear coefficient of \(\alpha\). [Complete proofs and review scope](phase1/CLEANROOM_SE.md).

### General-measure obstruction and a constant-contraction theorem

Task009's symbol \(\tau\) denotes the coset exponent itself, unlike \(\tau/6\) elsewhere. For \(0<\tau<1/2\), \(\tau/2<c<(1-\tau)/2\), and every nonempty original energy range \(0<h\le2-2c\), it constructs symmetric probabilities with
\[
\mu(xH)\le p^{-\tau},\quad
t(\mu)=p^{-2+2c},\quad
\frac{t(\mu*\mu)}{t(\mu)}\ge\frac{p^{-\tau}}{4096}>p^{-2c}
\]
for
\[
p>\max\{32,\ 64^{1/(1-\tau-2c)},\
4096^{1/(2c-\tau)}\}.
\]
In particular \(c=1/40\) is refuted at coset exponent \(\tau=1/24\), with sufficient onset \(p>2^{1440}\). This does not refute \(1/120\) or \(1/468\).

Separately, in any finite group, a symmetric probability with every proper-coset mass at most \(s=\sqrt{2/3}\) and \(\|\mu\|_2^2>1/(sD)\) satisfies
\[
t(\mu*\mu)\le\frac{7+2\sqrt6}{12}\,t(\mu)
<0.991582\,t(\mu).
\]
This constant contraction is not a fixed positive power of \(p\). The counterexamples and theorem were checked by root after fresh attempts; no kernel formalization is claimed. [Task009, §§2–6](phase1/CLEANROOM_R2.md).

### Tensor-envelope and other valid transfer criteria

For any probability, define its least central pointwise-envelope mass
\[
B(\mu)=\sum_{\text{classes }C}|C|\max_C\mu.
\]
It is exactly the least \(B\) for which \(\mu\le B\sigma\) with \(\sigma\) a central probability. Task018 proves, for \(p\ge5\),
\[
s(\mu)^2\le\mu(Z)+5B(\mu)/\sqrt p,\qquad
t(\mu*\mu)\le[\mu(Z)+5B(\mu)/\sqrt p]t(\mu),
\]
where \(s\) is the maximum nontrivial Fourier operator norm. No symmetry, PSD hypothesis or energy cutoff is required. Unlike the older transfer
\[
t(\mu*\mu)\le[\mu(Z)+5B(\mu)/\sqrt p]^2t(\mu)
+(B(\mu)^2-1)/D,
\]
this tensor argument has no additive uniform-mass floor. Its invariant contribution is \(B/d_\rho\); it does not discard that component.

If \(\mu(Z)\le p^{-1/30}\), \(B(\mu)\le Cp^{9/20}\), \(C\ge1\), then
\[
s(\mu)\le p^{-1/120}
\quad\text{for}\quad
p\ge\max\{5,2^{60},(10C)^{30}\}.
\]
One useful envelope stage therefore suffices for a direct spectral bound. Task018's tensor proof was checked by a second agent; task021 checked its use in the ledger. No useful actual stage has been certified.

Other complete conditional interfaces are retained in the report: PSD spectral spread \(L(\mu)=\max d_\rho\|\widehat\mu(\rho)\|_{\rm op}/\operatorname{tr}\widehat\mu(\rho)\), and the relative-centrality estimate with \(\Delta=\|\mu-P\mu\|_2\), \(q=\mu(Z)+5/\sqrt p\),
\[
t(\mu*\mu)\le q^2t(\mu)+(1+2q+2q^2)\Delta^2
\quad(\mu\ \text{symmetric}).
\]
Neither interface's required actual-walk hypothesis is proved. [Task018, §§2–5](phase1/E1_EXTENSION.md); [older exact transfer, R2_E1b §B3](phase1/R2_E1b.md).

### Envelope obstruction: retained cancellation mass, not just total support

For the task020 full-grid law
\[
\mu=N^{-2}\sum_{a,b=1}^N\delta_{U(-b)WU(a)},\quad
W=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\]
with \(p\) odd and \(2\le N\le p\), all ordinary powers satisfy
\[
B(\mu^{*r})\le\frac{(2N-1)p(p+1)}{N^2}.
\]
The complementary lower bounds are
\[
B(\mu^{*2k})\ge\frac{p^2-1}{4kN^{k+1}}\quad(k\ge1),
\qquad
B(\mu^{*(2k+1)})\ge\frac{p^2-1}{2N^{k+1}}\quad(k\ge0).
\]
They retain rare positive cancellation events in the word law: mass \(N^{-k}\) remains on a unipotent distribution, or its one-step translate. The classwise maximum detects this mass even if most of the complete support has spread. **The \(r\le59\) obstruction is not merely a total-support count.**

At \(N=\lfloor p^{1/20}\rfloor\), every fixed ordinary \(r\le59\) is incompatible, for sufficiently large \(p\), with \(B\le Cp^{9/20}\) for any fixed \(C\); it also fails \(Cp^{1/2-\delta}\) for fixed \(\delta>0\). \(r\ge60\) is necessary, not sufficient. At two steps, if \(M=\lfloor N/2\rfloor\) and \(M^2<p\),
\[
B(\mu^{*2})\ge\frac{p^2-1}{72NH_M},
\qquad H_M=\sum_{j=1}^M1/j.
\]
Three fresh same-model attempts independently obtained the cancellation obstruction; root checked them. [Task020, §§1–5](phase1/CLEANROOM_ENVELOPE.md).

Task021 extends the even-stage obstruction to actual subset correlations: for \(S\subseteq[N]^2\), \(n=|S|>N\), \(g\in\mathrm{GL}_2(\mathbb F_p)\), \(g_{21}\ne0\), \(\nu\) uniform on \(U(-b)gU(a)\), \(\lambda=\nu*\widetilde\nu\), and \(q=\sum_a|S_a|^2/n^2\),
\[
B(\lambda^{*k})\ge
\frac{(p^2-1)q^{k-1}(q-1/n)}{4k(N-1)}
\ge\frac{(p^2-1)(n-N)}{4kn(N-1)N^k}.
\]
For \(n\ge2N\), this is at least \((p^2-1)/(8kN^{k+1})\): at \(N=\lfloor p^{1/20}\rfloor\), every fixed pair count \(k\le29\) fails; at \(N=\lfloor p^{1/90}\rfloor\), every \(k\le138\) fails. The full-grid W identity is \(\lambda^{*k}=\delta_{(-I)^k}*\mu^{*2k}\). These formulas do not equate odd ordinary powers with correlation stages.

The same report proves the full-grid exact correlation norm, for any such \(g\) and \(2N-1\le p\),
\[
\|\lambda\|_2^2=\frac4{3N^3}-\frac1{N^4}+\frac2{3N^5}.
\]
Trace-2 mass is at most \((2N-1)/n\), and any other trace mass at most \((N-1)/n\). These do not imply spread within a conjugacy class. Indeed a symmetric probability supported on one inverse pair for each trace other than \(\pm2\) has trace masses \(1/(p-2)\), zero center mass, and \(B\ge(p^2-1)/4\). It is a counterexample to that inference, not asserted to be an actual capped walk. [Task021, §§1–2](phase1/ENVELOPE_ROUTE.md).

A distinct actual Lemma14 family already excludes a universal four-doubling shortcut: for \(N=\lfloor p^{1/25}\rfloor\), seed \(m_0=1\), \(s_j=V(2j)U(-2j)\), \(\mu_r=(\nu*\widetilde\nu)^{*r}\),
\[
B(\mu_{16})\ge(3/400)p^{19/25}.
\]
The full proper-coset cap \(p^{-1/30}\) holds for \(p\ge240^{150}\), using the source-checked subgroup classification and at most \(120/N\) mass per coset. Thus \(B(\mu_{16})\le Cp^{9/20}\) fails when additionally \(p>(400C/3)^{100/31}\). This refutes the earlier illustrative uniform \(d=4\) premise, not every later stage. [Task018, §3](phase1/E1_EXTENSION.md).

### A prime-independent stage exists, but is far too costly

The weak-SE theorem proves that every symmetric probability satisfying the full cap \(p^{-1/30}\) obeys
\[
\boxed{B(f^{*2^{98353}})<2}
\]
for \(p\ge\max\{P_{\rm weak},5,3^{120000}\}\). Here \(P_{\rm weak}\) remains numerically unextracted. The arithmetic is \(h=a=1/30,\ c=1/100000\), then \(j=98335\), residual exponent \(v=1/30000\), followed by 18 quadratic-bootstrap doublings using \(t_{\rm next}\le2p(p+1)t^2\). It is a symbolic theorem, not an executed long walk.

The class-mass reviewer checked the weak-transfer margins, delay, and ledger. The result is conditional on the supplied weak-growth input, whose absolute coefficient exists but is not numerically extracted. For actual walks it also requires proving the stated cap at the actual seed length. Thus “no useful stage certified” must not be shortened to “no fixed stage known.” [Task021, §§4–6](phase1/ENVELOPE_ROUTE.md).

### Other reusable positive results

The G0 audit repairs the Lemma14-to-Corollary16 interface. If Lemma14 has coefficient \(C_{14}\) and exponent \(0<\kappa_{14}\le1/2\), simultaneous shifts give, for disjoint length-\(N\) interval unions and \(N\ge4\),
\[
\left|\#\{(a,b)\in A\times B:ab=1\}-|A||B|/p\right|
\le(2^{\kappa_{14}}C_{14}+4)\sqrt{|A||B|}\,N^{-\kappa_{14}/2}.
\]
Thus \(\kappa_C=\kappa_{14}/2\) is justified without a quantitative Lemma15. This repairs an interface, not the missing original spectral exponent. [G0, §6](phase1/G0_gate_audit.md).

R3 proves an exact Fourier-tail bridge:
\[
|D(A,B)|\le\sqrt{|A||B|}
\left[\rho_p(X)+2\sqrt{p/(NX)+2/N}\right]+1,
\quad
K_p(\xi,\zeta)=\frac{S(-\xi,\zeta;p)+1}{p}.
\]
The zero correction and the tail matter. From the checked Blomer–Pascadi input, for \(5/12<\theta<1\), \(N=p^{\theta+o(1)}\), any
\[
0<\gamma<\min\{(4\theta-1)/40,\ (5\theta-2)/26,\ (12\theta-5)/42\}
\]
gives \(D(A,B)\ll_{\theta,\gamma}\sqrt{|A||B|}p^{-\gamma}+1\). Its coefficient/onset is not fully extracted, and this range does not reach the campaign's \(\theta=1/90\) or \(1/9\). [R3, §§2–5](phase1/R3.md).

The fresh from-scratch attempts prove an unconditional cap \(\lceil2\log p\rceil\) for every prime, with natural logarithm; a sharper supply bound \(|V_2(X)|\ge(X/9)^{41/40}\) for canonical two-digit fractions, \(X>9\); and exact lifting from \(xy=-1\bmod p\) at height \(<\sqrt p\) to denominator exactly \(p\). No requisite signed character-correlation estimate was proved. Conditional \(M=2\) and \(M<2^{150}\) statements in that report retain strong unproved premises. [Task010, §§A–C](phase1/CLEANROOM_ZAREMBA.md).

## 2. Negative list: reductions to retire unless their missing input changes

Each line concerns a particular inference, not every possible method in that area.

1. **Reannounce the roughly 1673-bit ledger:** it is conditional bookkeeping and depends on the unresolved printed-proof inputs. [G0](phase1/G0_gate_audit.md).
2. **Improve only the printed growth exponent or overheads:** the old fixed-BSG sensitivity floor and small overhead savings do not meet the intended route goal; these were conditional ledger ceilings, not universal mathematical lower bounds. [Phase0 synthesis, negative list](phase0/SUMMARY.md).
3. **Rename asymmetric BSG as BSG removal:** the checked theorem retains inverse losses and \(2^J\)-dependent parameters, with unextracted constants. [R2 E2, §3](phase1/R2_E2.md).
4. **Apply a planar incidence estimate directly to the dense centered target:** the derived error terms and wrong main-term coefficient overwhelm the needed saving. [R2 E2, §4](phase1/R2_E2.md).
5. **Infer full-group flattening from a projective-action norm:** the projective representation does not see every group Fourier block. [R2 E2, §1](phase1/R2_E2.md).
6. **Use the unchanged central E1 bracket for all capped correlations:** a uniform/unipotent mixture satisfies the full cap and PSD correlation condition but violates that bracket; it does not refute the smaller desired power gain. [Task018, §2](phase1/E1_EXTENSION.md).
7. **Wait for exact centrality:** the actual positive correlation powers remain noncentral in the stated ranges; PSD roots preserve the obstruction. [R2_E1b, §B2](phase1/R2_E1b.md).
8. **Infer relative centrality from a cap after many powers:** for the capped unipotent-mixture example, \(\|\mu^{*r}-P\mu^{*r}\|_2^2/t(\mu^{*r})=(p-1)^2/(p^2-2)\) for every \(r\ge1\). [Task018, §4](phase1/E1_EXTENSION.md).
9. **Improve PSD spectral spread merely by powering:** \(d\|M^r\|/\operatorname{tr}(M^r)\) is nondecreasing in \(r\). [Task018, §2](phase1/E1_EXTENSION.md).
10. **Use a small early envelope or assume four doublings suffice:** retained cancellation mass and the actual capped Lemma14 family give explicit contradictions. [Tasks020](phase1/CLEANROOM_ENVELOPE.md) and [018, §3](phase1/E1_EXTENSION.md).
11. **Replace within-class spread by trace-mass bounds:** trace masses of order \(1/p\) coexist with \(B\) of order \(p^2\). [Task021, §2](phase1/ENVELOPE_ROUTE.md).
12. **Tensor-square the one-copy R3 estimate:** diagonal averaging \(\sum f(g)\rho(g)\otimes\overline{\rho(g)}\) is not two independent averages; sum-frequency strips, invariant components, zero frequencies, and infinity sectors require their own estimate. [Task021, §3](phase1/ENVELOPE_ROUTE.md).
13. **Insert short-sum/completion estimates at the physical interval length:** the dual blocks are long, at least \(p/N\), and smoothing makes them longer; the checked bounds give no numerical target saving. [R3, §§3–6](phase1/R3.md).
14. **Use a one-sided upper discrepancy or ignore density loss:** the application needs a lower bound/two-sided centered error; conversion to a relative error loses \(\eta/\theta\). [R3, §1](phase1/R3.md).
15. **Substitute Selberg/Kim–Sarnak numbers directly for a walk gap:** a uniform weighted word-distribution or genuine positive-operator comparison is missing; pointwise majorants retain an additive centered error. [R4, §§3–6](phase1/R4.md).
16. **Kill R4 using the old finite-word thinness proxy:** that proxy is not a critical-exponent upper bound; the actual two-parameter support generates the determinant-\(\pm1\) integer lattice, and the comparison measure is still the problem. [R4, §1](phase1/R4.md).
17. **Use support counts, identity returns, or a numerical free-model match as weighted mixing:** multiplicities and the complete centered trace are needed; the grid supplies no uniform spectral upper certificate. [R4, §4](phase1/R4.md); [N8](phase0/N8_numerics.md).
18. **Stop flattening above \(p^{-2}\), or use a one-shot Frobenius step from low entropy:** the quasirandom estimate becomes useful below the required threshold; a lower-cutoff extension is necessary. [Task009, §5](phase1/CLEANROOM_R2.md); [R2_E1b, §A2](phase1/R2_E1b.md).
19. **Infer an exact prime denominator from modular expansion alone:** a multiple of \(p\) can have arbitrary height; the lifting step needs a real height bound and unresolved arithmetic correlation. [Task010](phase1/CLEANROOM_ZAREMBA.md).

## 3. What the two printed-proof audits establish

G0 (task001) and the isolated second audit (task012) agree that **the displayed argument does not establish its printed numerical \(M=2^{2000}\) claim with the checked inputs**. Task012 did not read G0 or the R2 reports. Both are source audits within the same model/vendor; isolation is not cross-vendor review.

The specific issues are:

- Survey (60) contracts squared excess by \(K_*^{-c_K}\), with \(K_*=p^{\tau/6}\). The squared-mass \(p\)-gain is \(g=\tau c_K/6\), so the compatible count is \(\lceil(2-h_0)/g\rceil+1\). The numerical substitution \(c_K=1/1640,\ k=1641\) does not follow by renaming that exponent.
- The cited \(1/20\) growth theorem requires a symmetric set. The BSG output is not asserted symmetric. The checked standard repair triples the tripling exponent, changing the quantitative calculation.
- The cited statements do not establish the pair \((C_1,C_2)=(9,32)\); commented TeX arithmetic is not the missing noncommutative inclusion proof. The pair is **unverified**, not shown false.
- Even granting the optimistic count, the displayed extraction gives \(\kappa_{14}^{-1}=9840\,2^{1645}\), hence \(\log_2\kappa_{14}^{-1}=1658.264442600\ldots\); the printed lower bound \(2^{-1656}\) does not follow.
- A complete numerical digit bound also needs the assembly's coefficients, admissible finite parameters, seed length/cap, and prime onset. The F5 Lemma14/Lemma15 interface has the elementary repair above; it does not resolve the other gaps.

These are verdicts on the argument inspected, **not disproofs of the bound, the large-prime existence theorem, or another possible proof**. The final IMRN text was not fully inspected in these audits; indexed primary survey excerpts and accessible arXiv/book sources have the exact access qualifications recorded in each report. No replacement numerical theorem follows from the pessimistic bookkeeping rows. The private note to the author remains a draft; this close-out does not authorize sending it. [G0, §§1–3,5–9](phase1/G0_gate_audit.md); [F1 second audit, scope and Q1–Q4](phase1/F1_second_audit.md); [private draft](phase1/NOTE_TO_AUTHOR_DRAFT.md).

## 4. Conditional structure and \(\log_2 M\) ledger

All entries below are implications with unproved or unextracted premises. None is an unconditional new Zaremba cap.

The common limiting overhead is \(O_B=705672/25\), with the limit \(\varepsilon\uparrow1/18\); those real thresholds are not attained certificates. Concrete admissible arithmetic uses \(R=40,\ \varepsilon=1/20\), overhead \(31680\), and the strict rule
\[
M_0>198/\kappa_{14},\qquad M=160M_0
\]
in the inverse-gap-dominated range. Every row still requires the actual seed and downstream assembly.

For an actual seed pair length \(m_0\le b\log_Np\), a delay of \(d\) doublings means \(m=2^dm_0\): charge \(d\) once. The MMS convention \(b=1/20\) and appendix convention \(b=1/4\) have different source hypotheses. They are not interchangeable choices for the same unverified seed.

| Single missing analytic input, with stated accompanying hypotheses | Conditional outcome |
|---|---|
| One actual stage with \(B\le Cp^{9/20}\), center mass \(\le p^{-1/30}\), after delay \(d\) | No further flattening: \(\kappa_{14}=1/(240b2^d)\). For \(b=1/20\), limiting \(\log_2 M=18.369744553+d\), concrete \(M=380160\,2^d+160<2^{19+d}\). For \(b=1/4\), limiting \(20.691672647+d\), concrete \(M=1900800\,2^d+160<2^{21+d}\). |
| Relative-centrality criterion at every required stage, yielding \(p^{-1/60}\) gain down to \(p^{-2-1/30}\), with \(h_0=a=1/30\) | 119 further doublings. Limiting \(\log_2 M=137.369744553+d\) for \(b=1/20\), or \(139.691672647+d\) for \(b=1/4\); concrete caps \(<2^{138+d}\) and \(<2^{140+d}\), respectively. |
| Native E1-strength transfer with \(h_0=a=1/24,\ b=1/4\), on the required extended range | \(k=119,\ v=1/40\); limiting direct ledger \(139.106710147+d\), concrete cap \(<2^{140+d}\). The central theorem itself does not supply this noncentral premise. |
| Strong set-energy estimate \((\eta,\theta)=(1/20,1)\), actual \(h_0=1/10\), cap \(a=1/24\) or \(1/30\), \(b=1/4\) | Taking \(c=1/421\): \(j=401\), limiting direct \(\log_2 M=423.432069147\). At \(c=1/468\): \(j=446\), direct \(468.169719944\). The default mechanical B rows are instead \(452.087420976\), \(499.240109272\). |
| Proved weaker SE, but actual \(h_0=1/10,\ b=1/4\) and assembly still to certify | \(c=1/32241,\ j=30630,\ v=21/322410\), limiting direct \(\log_2 M=30658.691001595\). The often-quoted \(32278.346353424\) is the different mechanical default B ledger. Both have unextracted onset. |
| Same weak SE with cap-only \(h_0=a=1/30,\ b=1/4\) | \(c=1/96721,\ j=95110,\ v=61/2901630\); limiting direct \(\log_2 M=95140.322476850\). |
| Only the proved coarse envelope, applied to an actual capped seed | \(d=98353\); concrete conditional caps \(<2^{98372}\) for \(b=1/20\), \(<2^{98374}\) for \(b=1/4\). No improvement; \(P_{\rm weak}\) still unextracted. |
| A new direct Corollary16 estimate with explicit \(\kappa_C\), coefficients and valid interval range | Limiting \(\log_2 M=\log_2(352836/(25\kappa_C))\); e.g. \(\kappa_C=1/100\) gives approximately \(20.43\). R3 and R4 did not prove such a numerical input at the target scale. |

The direct constant-gain formula underlying the table is
\[
j=\left\lceil\frac{2-h_0}{2c}\right\rceil+1,\quad
v=h_0+2cj-2,\quad
F_{\rm direct}=j+d+\log_2(4bO_B/v).
\]
It retains the absolute spectral coefficient rather than silently absorbing it into an exponent. A different conservative convention halves that exponent and adds one bit. The printed-prefactor formula is instead \(F_{\rm print}=k+d+\log_2(96O_B/c_{\rm pref})\).

For comparison only, at \(\tau=1/4,\ h_0=1/24\), mechanically treating E1's numeral \(1/120\) as \(c_K\) gives \(k=5641,\ F_{\rm print}=5669.276635148\); this deliberately weakens the genuine E1 gain by a factor 48 in its exponent. The printed \(c_K=1/1640\) gives \(k=77081,\ F_{\rm print}=77113.049224652\), assuming that general flattening input and its prefactor. Neither is a certified replacement theorem. [All normalization and integer rules](phase1/E1_normalization_certified_M.md); [weak-SE table](phase1/R2_E1b.md); [one-stage improvement](phase1/E1_EXTENSION.md); [coarse ledger](phase1/ENVELOPE_ROUTE.md); [direct Corollary16 sensitivity](phase0/SUMMARY.md).

The complete onset would be the maximum of seed validity, the new estimate's onset, the transfer threshold, and every assembly threshold. A displayed numerical exponent with a missing leading coefficient or onset is not a fully effective theorem. The central value \(2^{40}\) cannot be substituted for that maximum.

## 5. Reopening gates

Do a current primary-source/G2 check before any new substantial campaign. The October 2 sweep is a dated scoped record, not a perpetual clearance. Then require a written estimate that changes one of these interfaces:

1. **A useful actual-walk envelope or direct tensor bound.** State the exact generator family, subset hypotheses, pair length, fixed delay, coefficient and onset. A full-grid W result alone does not cover the actual Lemma14 family or arbitrary Lemma15 subsets. For the diagonal tensor operator, task021 proves
   \[
   \|\widehat f(\rho)\|_{\rm op}^2\le d_\rho^{-1}
   +(1-d_\rho^{-1})\|T_f|_{\Omega^\perp}\|.
   \]
   A power saving for that complementary operator could bypass a pointwise envelope; the checked one-copy R3 bounds do not imply it. [Task021, §3](phase1/ENVELOPE_ROUTE.md).
2. **A stronger noncentral energy input.** Prove the unrestricted \((1/20,1)\) set estimate, or a genuinely useful direct weighted estimate on the actual measures, including the lower cutoff and coefficient. Stronger seed entropy must be independently established. Repeating the central-Schur proof, the restricted hyperplane proof without controlling its partition loss, or the same BSG extraction does not close this gate. [R2_E1b](phase1/R2_E1b.md); [CLEANROOM_SE](phase1/CLEANROOM_SE.md).
3. **A direct incidence/automorphic replacement.** For R3, control the properly smoothed long dual block or the more restricted indicator-derived coefficients, with a two-sided centered error and the density loss. For R4, first supply the uniform weighted centered-trace theorem or a valid positive-operator comparison; only then spend effort improving lattice constants. [R3](phase1/R3.md); [R4, §4](phase1/R4.md).
4. **Repair certification independently of exploration.** Before claiming a digit cap, resolve the displayed-proof gaps or replace those inputs, certify actual seed floors and coset coefficients, propagate incidence and finite-alphabet constants, and extract the full prime onset. Obtain review beyond the present same-model checks when the result warrants it. The private author draft has no sending authorization.

A smaller refinement of the 98,353-stage fallback, a larger finite spectral grid, or another formal ledger with a presumed delay is not, by itself, a reopening trigger. No global lower bound on the best achievable flattening exponent or digit cap has been proved.

## 6. Recorded work and costs

The authoritative numbered task timestamps are in [inbox STATUS](/work/inbox/STATUS.md); Phase0 dates and K2 are in the [campaign ledger](ledger.md). Through task023, STATUS records **23 completed numbered inbox tasks**, not 23 Zaremba proof campaigns:

| Scope | Completed task IDs |
|---|---|
| Zaremba mathematics, source audit, or numerical work: 17 tasks | 001–007, 009–012, 015, 017–021 |
| Private author-note draft: 1 task | 016 |
| Dashboard source updates: 2 tasks | 014, 023 |
| Cross-portfolio source freshness: 1 task | 022 |
| Other problem work, excluded from Zaremba research counts: 2 tasks | 008, 013 |

Task024 is this additional close-out. Task025 is separate selection work and is not charged as a completed Zaremba task. Phase0's earlier workflow is outside the numbered inbox count; its synthesis records completed and failed components rather than a fully completed planned work package.

The following are **enclosing elapsed wall-clock windows**, not sums of parallel agent durations and not exclusive CPU or active reasoning time:

| Recorded window | UTC endpoints | Elapsed |
|---|---|---:|
| Phase0 dispatch to partial completion | September 26, 04:23:33–07:43:27 | 3 h 19 m 54 s |
| First numbered execution batch through task018 completion | September 26, 16:01:13.306–17:36:01.648 | 1 h 34 m 48.342 s |
| Resumed execution through task021 completion | October 2, 08:38:22.887–09:30:33.916 | 52 m 11.029 s |
| Sum of the latter two nonoverlapping recorded windows | — | 2 h 26 m 59.371 s |

The two latter windows contain concurrent work, including the separately listed administrative/other-problem tasks. They exclude earlier coordination, the long owner pause, and this close-out; they are not a complete billed-time total. STATUS records the owner pause at September 26 17:37:05.384 and resumption on October 2. Calendar time between those dates is not research execution time. No sum of agent durations is presented as wall time.

Measured computational costs and checks are separately recorded:

- **Task007:** 40 corrected operator-grid points and eight independent floating-point dense-SVD comparisons; accounted CPU interval \(3229.419846\)–\(3239.419846\) seconds; maximum recorded RSS 252.34 MiB. The invalid padded rerun is excluded from results but included in cost. The power estimates are lower estimates, not certified top-singular-value upper bounds. [N8, §§2,5–6](phase0/N8_numerics.md).
- **Task019:** one exact finite process, 0.286768 CPU seconds, 0.247 internally reported wall seconds, 81,268 KiB peak RSS. Those timings belong to the finite checker, not the entire referee/source task. [REFEREE_E1, numerical verdict](phase1/REFEREE_E1.md).
- **Task021:** six W norm cases, 234 selected subset/matrix retained-submeasure cases, and 18 full-grid general-\(g\) norm cases passed bounded exact integer checks. The two commands each reported wall time below 0.01 seconds; no CPU/RSS measurement was claimed. These verify small signs and multiplicities, not the asymptotic theorem. [ENVELOPE_ROUTE, §6](phase1/ENVELOPE_ROUTE.md).

Other reports contain bounded arithmetic or finite checks, but there is no complete campaign-wide CPU/RSS ledger to sum. The DESIGN's 27.5-million-token allocation was a **plan**, not measured usage. No complete actual token or dollar total is available here. No such total is inferred from task counts, planned budgets, model self-reports, or parallel durations.

This close-out used read-only report inspection and wrote only this file. It ran no new numerical experiment, solver, dependency installation, git operation, publication or external message. Global-memory recall was unavailable in the exposed tool catalog; no notice was invented and no preset was changed.
