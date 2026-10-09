DONE — two exact, unproved lemma cards admitted; no proof attempt and no candidate test executed. There is no admissible third card in this bounded screen.

# Lemma shortlist — selection round 2026-10-09

**READ / scope.** This dossier supplies two falsifiable hypotheses, for the leading constant in the sum-of-two-squares covering bound and the second-order constant for finite Sidon sets. Each names a discarded piece of arithmetic or realizability information, an exact conditional improvement, and an independently executable integer test. The first targets an old elementary frontier; the second must go beyond the fixed-kernel scalar relaxation. Neither hypothesis is a theorem or an experimentally supported conjecture. Current-source checks found an additional Sidon competitor dated 5 October and confirmed the existing repository Sidon bound's Lean verification. **UNVERIFIED:** completeness of the literature search and worldwide novelty; a bounded search is not a priority claim. Cutoff: 2026-10-09 UTC.

**Labels used throughout.** READ means the cited primary text, code, or live page was inspected; it does not mean its mathematics was independently verified. SECONDARY means a catalogue/database or another author's account, and also carries UNVERIFIED where the underlying primary evidence was not inspected. NOT ACCESSIBLE records a failed access, never a negative literature result. LIVE CLAIM marks an unrefereed mathematical assertion without established full formalization. Proposed lemmas, test-design choices, conditional substitutions and ranking judgments are marked UNVERIFIED. A label on a paragraph or table cell governs its contents. No source claims either proposed lemma below.

## Ranking and disposition

**UNVERIFIED / editorial assessment, not calibrated probabilities.** Rank by the requested product of improvement value and likelihood of surviving the *specified finite test*, not by likelihood of being provable in a week:

1. **Card 1, #222:** highest value; a reduction from \(2\sqrt2\) to \(14/5\) in an old uniform leading constant, with an exact exhaustive test of 15,736,833 small instances and additional adversarial families. Survival is plausible but wholly untested; the growing search neighborhood is the substantive, difficult hypothesis.
2. **Card 2, #30:** important second-order gain from \(2\sqrt2/3\) to \(\sqrt{197}/15\), and an existing verified theorem supplies the surrounding argument. The construction-family test is likely less discriminating: survival on those sets would provide little evidence about hypothetical extremizers. Current competing work also lowers its selection value.

**READ / next action.** The coordinator can rank these two cards; the verifier can run either test using only its card. There is no third card to test. **UNVERIFIED:** no recommendation to start a proof campaign before finite results and a separate assessment of tractability. A universal quantified hypothesis is a concrete gate, not evidence that its proof is within reach.

## Considered and excluded

**READ / internal decision evidence.** All required catalogues were read before drafting: [targets](targets_20261003.md), [old records](old_records_20261003.md), [release sweep](G2_OPENAI_RELEASE_20261009.md), [transfer targets](transfer_targets_20261002.md), [construction board](construction_board_20260925.md), [famous watch](famous_watch.md), [negative list](/work/SELECTION.md), [round 3](selection_probe_20261002.md), and [round 4](astra_probes_round4_20261009.md). The exclusions below describe those records and this screen; historical frontier claims not refreshed from primary sources here remain SECONDARY / UNVERIFIED.

| Considered candidate or route | Reason excluded |
|---|---|
| #156 minimal maximal Sidon: independent thinning, cubic curve, height lift | READ round-4 T1: the first two routes fail at the required coverage scale; the lift still lacks a specified correlated design with the required hole count. No new exact design lemma supplied. |
| #30: kernel retuning, triangular-window integrality/cubic moments, end-cluster counts alone | READ round-4 T6 and its referee: these relaxations are saturated or realize only sparse cluster counts. Card 2 instead constrains differences of the entire actual dense set. |
| #1082: pair/class counting, local kite or good-base proportions | READ round-4 T2: abstract metric models saturate the counting constraints; local planar configurations and polygon examples defeat the proposed simplistic upgrades. No quantitative global planar constraint was identified. |
| #86: degree histogram, entropy, one-face relaxation | READ round-4 T3: already saturated; a new compatible overlap inequality for different faces was not writable exactly. |
| #241: one-point moments, weighted-hole smoothing | READ rounds 3–4: moments are rigid; the advertised weighted-hole improvement repackages the target smoothed energy and the rounded-frontier gain is inadequate. No distinct new lemma. |
| #1066: degree-six rigidity or degree-only independence bound | READ round-4 T5: dense degree-five triangle-square strips survive those constraints. SECONDARY / UNVERIFIED current coefficient claim not inspected sufficiently for a new proof-loss card. |
| #304; Jacobsthal quadratic target; Kaplansky; affine cancellation; circulant Hadamard; planar unit-distance \(4/3\) coefficient; six-colour Hadwiger–Nelson; Brennan; strong sensitivity; De Giorgi dimension eight | READ negative list/release sweep: closed-by-claim at the specified scopes, respectively families 025, 021, 196, 047, 179, 167, 158, 072, 132, 375. Excluded even though unformalized claims are not established theorems. |
| Refereeing unformalized OpenAI release families | READ negative list: a separate owner decision, not a lemma-selection output. |
| Union-closed constant; minimum overlap #36; \(B_2[6]\); sequence discrepancy | READ target cards/round 3: scalar entropy/product, moment/PSD, mixed-norm or admissible-function improvements do not supply a new exact compatibility lemma. SECONDARY / UNVERIFIED record details not refreshed here. |
| Caccetta–Häggkvist; diagonal Ramsey; restricted sum–difference | READ target cards/round 3: missing certificate-level gain, density recovery, or realizable conditional-copy inequality; the tested scalar/general entropy replacements fail. |
| Linnik; sum–product; primes plus powers of two; semiprime patterns | READ target cards/round 3: no exact uniform new input with a credible finite falsifier and inspected proof-loss passage at the current frontier. Prime-power/special-pattern results do not meet the original quantifiers. |
| #509, #1033, #1093, #790, #789; Zaremba #336 | SECONDARY / UNVERIFIED old-record catalogue: original record proof or the necessary exact lossy passage was not accessible/inspected. Exclude rather than reconstruct it from summaries. |
| #1182; #1181; #902; #187; #17; #33; #1109 | READ catalogue screening: respectively a sharp/subsumed elementary core, lower-order factorial savings, unchanged leading tournament logarithm, onset-only dependence refinement, no factorial-to-frontier gain, no leading repetition gain, or an unspecified analytic input. No qualifying new lemma. |
| #887; MOLS(22); further capacity transfers | READ catalogue screening: unresolved source/scope mismatch; no exact compatible construction lemma; or already recorded transfer scope without a new record-moving gate. |

## Card 1 — Erdős #222, sums of two squares (leading constant \(2\sqrt2\))

### (a) Exact located record and status

**READ / refereed.** Define
\[
g(n)=\min\{d\in\mathbb Z_{\ge0}:n+d=a^2+b^2, a,b\in\mathbb Z_{\ge0}\}.
\]
Peter Shiu, *On a Result of Bambah and Chowla*, **Integers 19 (2019), A48, Theorem 2(i), p. 5**, gives, for every integer \(n\ge1\), with \(u=\lfloor\sqrt n\rfloor\), \(v=\lceil\sqrt{n-u^2}\rceil\),
\[
\min\{u^2+v^2-n,(u+1)^2-n\}<2\sqrt2\,n^{1/4}-2.
\tag{SQ-record}
\]
Thus \(g(n)\) satisfies the same strict upper bound, with explicit onset 1. [Primary journal PDF](https://math.colgate.edu/~integers/t48/t48.pdf).

**READ / bibliographic attribution; SECONDARY / UNVERIFIED original proof.** Shiu attributes the additive \(-2\) improvement to G. J. O. Jameson, *More on the gaps between sums of two squares*, **Mathematical Gazette 103(558) (2019), Note 103.32, 499–503**, DOI [10.1017/mag.2019.114](https://doi.org/10.1017/mag.2019.114); the [journal index](https://homepage.univie.ac.at/hans.humenberger/Aufsaetze/2019c.pdf) verifies the citation. Jameson's original full text was not accessed. The earlier source is R. P. Bambah and S. Chowla, *On numbers which can be expressed as a sum of two squares*, **Proc. Nat. Inst. Sci. India 13 (1947), 101–103**; its original text was not inspected. The primary proof used here is Shiu's reproduction and refinement, not an invented theorem number for 1947.

**READ / bounded status.** The live [#222 page](https://www.erdosproblems.com/222) still records the \(1/4\) upper exponent; no inspected source reduces this uniform leading constant. The problem is not solved or subsumed by the inspected recent results. **UNVERIFIED:** global bestness beyond the stated search coverage.

### (b) Quoted loss

**READ.** Shiu, p. 1 immediately after equation (1), uses
\[
n-u^2\le v^2<n-u^2+2\sqrt{n-u^2}+1.
\tag{SQ-loss}
\]
This replaces the exact upward-rounding error by its worst possible value. For the sharpened record, p. 5, proof of Theorem 2(i), the second branch is explicitly “we consider the lattice point \((u+1,0)\)”. The two branches do not use rounding errors at abscissae \(u-j\). Theorem 2(ii) gives infinitely many inputs on which those two choices alone cannot supply even additive \(-3\). [Same primary PDF](https://math.colgate.edu/~integers/t48/t48.pdf).

### (c) One exact candidate lemma and conditional output

**UNVERIFIED / proposed lemma SQ-L; not a literature claim.** For every integer \(u\ge1024\) and every integer \(r\) with \(0\le r\le2u\), let \(J\) be the smallest positive integer satisfying \(J^4\ge u\). For \(j=0,\ldots,J\), define
\[
x_j=r+2uj-j^2,\qquad q_j=\lceil\sqrt{x_j}\rceil,\qquad e_j=q_j^2-x_j,
\]
and
\[
e_*(u,r)=\min\bigl(2u+1-r,e_0,e_1,\ldots,e_J\bigr).
\]
All these are nonnegative integers. The proposed assertion is exactly
\[
\boxed{25e_*(u,r)^2\le196u.}\tag{SQ-L}
\]
The neighborhood grows as \(\lceil u^{1/4}\rceil\); it is not a fixed number of alternate points and is not Shiu's Hypothesis H.

**UNVERIFIED / conditional substitution, no proof of SQ-L.** If SQ-L holds, replace the two candidates in (SQ-record) by \((u+1,0)\) and \((u-j,q_j)\). For \(n=u^2+r\), this supplies
\[
\boxed{g(n)\le\frac{14}{5}n^{1/4}\quad\text{for every integer }n\ge1,048,576.}
\tag{SQ-output}
\]
This moves the leading coefficient from \(2\sqrt2\) to \(2.8\); it does not reduce the exponent. For successive representable integers \(s<t\), its exact consequence is \(t-s\le1+(14/5)(s+1)^{1/4}\) when \(s+1\ge1,048,576\). This states explicitly the difference between a covering bound at arbitrary \(n\) and a consecutive-gap bound.

### (d) Information absent from the saturated relaxations

**READ / source comparison; UNVERIFIED / assessment of SQ-L.** The two-point saturation above and the round-3 fixed-pattern arithmetic obstructions do not assert anything about the entire growing list \((q_j^2-x_j)_{0\le j\le J}\). SQ-L uses **exact integer-square arithmetic and the dependence between rounding errors sharing the same \(u,r\)**. It cannot be evaluated from independent rounding errors, marginal moments, or a fixed list of residue patterns. The six round-4 relaxations concern different objects; none models this list. This is a concrete scope distinction, not evidence SQ-L is true or easy. A false SQ-L could coexist with a better unrestricted bound for \(g\).

### (e) Exact finite falsification test — standalone specification

**UNVERIFIED / test design; not executed.** Use Python 3 standard-library arbitrary-precision integers, `math.isqrt`, and `time.process_time`. No floating-point root, solver, or primality test is needed. For a nonnegative integer \(x\), compute \(s=\operatorname{isqrt}(x)\) and \(\operatorname{ceilroot}(x)=s+\mathbf1_{s^2<x}\). Compute \(J\) by integer binary search, or start at `isqrt(isqrt(u))` and increment until \(J^4\ge u\).

For each \((u,r)\) below, initialize \(e=2u+1-r\). If \(25e^2\le196u\), the instance passes. Otherwise visit \(j=0,1,\ldots,J\) in order, compute \(x_j,q_j,e_j\), replace \(e\) by \(\min(e,e_j)\), and stop this instance as soon as \(25e^2\le196u\). If the list ends with \(25e^2>196u\), report **FALSIFIED** with \(u,r,n=u^2+r,J\), every \(e_j\), the boundary candidate and the two integer sides. Recompute that witness without early exit before reporting.

Run these three batches, in this order:

1. **Exhaustive rectangle:** every \(u=1024,1025,\ldots,4096\), and every \(r=0,1,\ldots,2u\), lexicographic order. This is exactly **15,736,833** instances; \(J\le8\).
2. **Two-choice hard family:** every even \(m=2,4,\ldots,100000\), set \(u=m(m+2)/2\), \(r=m^2+1\), and retain only \(u\ge1024\) and \(r\le2u\). This includes \(m=2862\), \(u=4098384\), \(n=16796759602501\), an input discussed in Shiu §5. The primary text reports an alternate point at displacement 40 with excess 2059; this is a useful regression fixture, not survival evidence for SQ-L.
3. **Larger near-square remainders:** for every \(b=10,\ldots,40\) and \(t=0,\ldots,31\), set \(u=2^b+t\). Let \(M=\operatorname{isqrt}(2u)\). Test the distinct remainders in \(\{0,u,2u\}\cup\{m^2+1:\max(0,M-16)\le m\le M,\ m^2+1\le2u\}\), in increasing order. All integer values, including \(n\), must remain arbitrary precision.

**UNVERIFIED / resource estimate.** The fixed batches require fewer than 200 million candidate-square evaluations even without early exit; anticipated runtime is comfortably below one CPU-hour, but it has not been benchmarked here. Stop at **3300 CPU-seconds**, checking the clock at least every 1000 instances. If stopped, report **PARTIAL**, the completed batch/prefix and instance count, not full survival. Memory can be constant apart from one failure witness.

**UNVERIFIED / interpretation.** **SURVIVED** means zero violations in *all three completed batches*, with counts reported separately. It says nothing universal about \(u>4096\), about untested remainders in batch 3, or about the asymptotic behavior. Do not change 1024, 196/25, or the neighborhood after a failure; that would be a different lemma requiring a new card.

**READ database / SECONDARY, UNVERIFIED independent certification.** [OEIS A001481 b-file](https://oeis.org/A001481/b001481.txt) begins \(0,1,2,4,5,8,9,10,13,16,17,18,20,25,26,29\). These are representable integers, not values of the restricted \(e_*\). They can check a small unrestricted reference implementation; no completeness computation was rerun here.

### (f) G2, dates, activity and access limitations

| Source/check | Qualified finding as of 2026-10-09 |
|---|---|
| [#222 forum](https://www.erdosproblems.com/forum/thread/222) | READ live page: 0 comments, 0 proof claims, no accounts listed as currently working or formalizing. This does not mean nobody is working privately. |
| OpenAI release sweep | READ internal primary audit: no family matched this upper-gap coefficient or closed #222. UNVERIFIED completeness beyond that title/statement sweep. |
| Artūras Dubickas, *Gaps in a sumset of a polynomial with itself*, Math. Reports 25(75)(2) (2023), 313–318, [DOI 10.59277/mrar.2023.25.75.2.313](https://imar.ro/journals/Mathematical_Reports/Pdfs/2023/2/10.pdf) | READ Theorem 1.1 and pp. 314, 317: general polynomial sumsets; its upper bound has a polynomial-dependent constant, not a smaller explicit coefficient here. |
| Siddharth Iyer, *Gaps between quadratic forms*, [arXiv:2505.23428](https://arxiv.org/abs/2505.23428), submitted 2025-05-29; Bull. Aust. Math. Soc. (2026), DOI 10.1017/S0004972726101191 | READ abstract and journal metadata: counts simultaneous values of two forms in longer short intervals. It does not state the uniform coefficient improvement in this card. |
| Yanqiu Guo and Michael Ilyin, *Sparse distribution of lattice points in annular regions*, J. Number Theory, [DOI 10.1016/j.jnt.2024.05.009](https://doi.org/10.1016/j.jnt.2024.05.009), [author PDF](https://faculty.fiu.edu/~yanguo/sparse.pdf) | READ primary PDF: related annular sparsity; not a replacement for the uniform covering record. |
| arXiv last-12-month query | READ API: exact phrase `"sums of two squares"`, submitted dates 2025-10-09 through 2026-10-09, returned 24 records. Titles screened; inspected relevant abstracts include Iyer's cubic-polynomial paper (2510.25492), Fan–Lott's difference-avoidance paper (2606.29185), and Sun–Zhao's almost-all three-square paper (2609.13894). None of those abstracts claims SQ-output. UNVERIFIED: full-text exclusion of all 24 records, and coverage of synonyms. |
| [OpenAlex W3013127143](https://openalex.org/W3013127143) and `works?filter=cites:W3013127143` | SECONDARY / UNVERIFIED completeness: database returned one citing work, Dubickas 2023; that paper was then read as above. Citation counts are not a completeness certificate. |
| [Erdős Problem a Day attempted report](https://erdosproblemaday.com/report/222) | NOT ACCESSIBLE: HTTP 404 at this path. No claim that the site has no differently routed report. |
| MathOverflow, Zulip, Mathlib | READ search results: related [Iyer discussion](https://mathoverflow.net/questions/409857/representing-x3-2-as-a-sum-of-two-squares), answer 2025-10-30/edited 2026-01-23, concerns polynomial values, not uniform gaps. Public Mathlib open-PR API query `Bambah` returned 0. UNVERIFIED: exhaustive formalization/community activity; no relevant indexed Zulip hit was located. This is not a Mathlib task. |

### (g) Product if proved

**UNVERIFIED / assessment: announce-worthy quantitative result**, because it would lower the old uniform leading constant by \(2\sqrt2-14/5\), about 1.0%, with an explicit onset. It would not solve the full gap-growth problem or change the \(1/4\) exponent.

## Card 2 — Erdős #30, finite Sidon sets (second-order constant \(2\sqrt2/3\))

### (a) Exact located record and status

**READ / formalized upper-bound result; paper not human-refereed.** A strong Sidon set has distinct unordered sums \(a+b\) with \(a\le b\), **including doubled terms**. Let \(F(N)\) be its maximum cardinality in \(\{0,\ldots,N-1\}\). Haoyu Chen, *An explicit second-order bound for Sidon sets and the limit of the fixed-kernel energy method*, **2026, v2, Theorem 2.1, equation (2.1)**, states
\[
\boxed{F(N)\le\sqrt N+\frac{2\sqrt2}{3}N^{1/4}+1\quad(N\in\mathbb Z,\ N\ge120^4=207360000).}
\tag{SID-record}
\]
Sources: [v2 paper source](/work/publish/automath-papers/erdos30/main.tex), [local v2 PDF](/work/publish/automath-papers/erdos30/main.pdf), Zenodo [v2 DOI 10.5281/zenodo.23105891](https://doi.org/10.5281/zenodo.23105891), v1 DOI 10.5281/zenodo.23103980. The standalone [proof text](/work/problems/erdos30/SIDON_BOUND_PROOF.md) has the same statement as an **unnumbered Theorem in §1, (1.1)**; do not interchange its section numbers with the typeset version.

**READ / formalization evidence.** The pinned [Statement.lean](https://github.com/chy4pro/automath/blob/f8e97665f26ea40ec867d8d054d352b5fc5ec56c/lean/sidon30/Sidon30/Statement.lean) matches the quantifiers, diagonal convention, coefficient and onset. [Main.lean](/work/lean/sidon30/Sidon30/Main.lean) supplies `sidon_second_order`; [FinalCheck.lean](https://github.com/chy4pro/automath/blob/f8e97665f26ea40ec867d8d054d352b5fc5ec56c/lean/sidon30/Sidon30/FinalCheck.lean) requires exactly `propext, Classical.choice, Quot.sound`. GitHub API confirmed [CI run 37060176909](https://github.com/chy4pro/automath/actions/runs/37060176909), commit `f8e97665f26ea40ec867d8d054d352b5fc5ec56c`, completed successfully on **2026-10-02**, including Build and Axioms steps. No new build or proof audit was performed. The older standalone header saying “no Lean” is stale. The **kernel-optimality theorem is still a LIVE CLAIM**, distinct from the formalized upper bound.

**READ / comparison.** The inspected refereed comparator is Daniel Carter, Zach Hunter and Kevin O'Bryant, *On the Diameter of Finite Sidon Sets*, **Acta Math. Hungar. 175(1) (2025), 108–126**, [arXiv:2310.20032](https://arxiv.org/abs/2310.20032), with coefficient 0.98183 and unspecified \(O(1)\). Jianfeng Hou and Hongbin Zhao, *An Improved Upper Bound for Finite Sidon Sets via Vector-Valued Smoothing*, **arXiv:2607.01169v3, Theorem 1.2, 2026-09-04**, is a **LIVE CLAIM** with coefficient \(0.9434925907\ldots\) and unspecified \(O(1)\). Those are weaker located coefficients; neither supplies a numerical onset for its remainder in the inspected statement. [Hou–Zhao primary text](https://arxiv.org/html/2607.01169v3).

**READ / bounded status.** The original Erdős conjecture with error \(O_\varepsilon(N^\varepsilon)\) remains open in the inspected sources. SID-record is the strongest same-scope coefficient located, not a worldwide priority finding. **UNVERIFIED:** search completeness.

### (b) Quoted loss

**READ.** In the typeset paper **§5, equation (5.2)**, also standalone §5 equation (5.2), let \(\mu=\sum_{a\in A}\delta_{a/T}\) and \(D_+(A)=\{a-b:a,b\in A,a>b\}\). The exact step is
\[
E(\mu,\mu)=\frac43|A|+2\sum_{d\in D_+(A)}f(d/T)
\ \le\ \frac43|A|+2\sum_{d=1}^{\infty}f(d/T),
\tag{SID-loss}
\]
where
\[
f(x)=\begin{cases}\frac43-2|x|+\frac23|x|^3,&|x|\le1,\\0,&|x|>1.\end{cases}
\]
The replacement fills every missing positive difference, discarding the fact that all occupied differences come from one common indicator set. [Primary source](/work/publish/automath-papers/erdos30/main.tex).

### (c) One exact candidate lemma and conditional output

**UNVERIFIED / proposed lemma SID-L; not a literature claim.** For every integer \(N\ge4096\) and every strong Sidon set \(A\subseteq\{0,\ldots,N-1\}\), put \(k=|A|\). Assume \(k^2\ge N\). Define \(T=T(N)\) to be the smallest positive integer such that
\[
10000T^4\ge38809N^3.
\]
With exactly the kernel and difference convention above, assert
\[
\boxed{\sum_{\substack{1\le d<T\\d\notin D_+(A)}}f(d/T)\ge\frac{k}{100}.}
\tag{SID-L}
\]
The quantifiers concern actual sets, not free difference multiplicities or relaxed window arrays; \(T=\lceil(\sqrt{197}/10)N^{3/4}\rceil\) is fixed, not optimized after seeing \(A\).

**UNVERIFIED / conditional substitution, no proof of SID-L.** Retaining this missing mass in (SID-loss) changes the source energy upper estimate to \(T+(197/150)k\). Keep its capacity intercept \(b=2/3\) and exponential remainder. The coefficient substitution in the source's scalar formula (standalone **§7, (7.3)**; typeset **§7, (7.3)**) then gives
\[
\boxed{\limsup_{N\to\infty}\frac{F(N)-\sqrt N}{N^{1/4}}
\le\frac{\sqrt{197}}{15}<\frac{2\sqrt2}{3}.}
\tag{SID-output}
\]
Equivalently: for every real \(\varepsilon>0\), there exists an integer \(N_\varepsilon\) such that every integer \(N\ge N_\varepsilon\) satisfies \(F(N)\le\sqrt N+(\sqrt{197}/15+\varepsilon)N^{1/4}\). Sets with \(k^2<N\) require no estimate from SID-L. **No numerical \(N_\varepsilon\), additive \(+1\), or effective all-\(N\) version of the improved coefficient is claimed.** The proposed lemma has an explicit onset; this conditional asymptotic output does not.

### (d) Information absent from the saturated relaxations

**READ.** Round-4 T6 and [referee 2](/work/notes/review/REF_referee-2_erdos30_20261009.md) distinguish: (i) triangular-window second/third scalar moments plus integrality and span capacities; (ii) realizable end-cluster counts with only \(O(N^{1/4})\) points, no dense bulk; and (iii) the stronger optimal-kernel argument. The referee explicitly declines to infer a no-go for the full realizable dense profile. The source fixed-kernel barrier concerns scalar capacity together with the **full** difference sum.

**UNVERIFIED / assessment of SID-L.** The new input is **joint positional realizability by a single 0/1 set with \(k^2\ge N\)**. It charges differences that this entire set fails to realize at a prescribed scale. Free pair arrays can fill the relevant distances while respecting their isolated multiplicity bounds; scalar window moments and sparse end clusters do not certify realizability of that filled array with the dense bulk. SID-L forbids precisely that behavior. It is therefore outside the stated relaxations, but there is no claim here that this missing information enforces a positive constant: that is the entire unproved gate. Retuning a kernel or invoking a third-moment upper bound does not establish it.

### (e) Exact finite falsification test — standalone specification

**UNVERIFIED / test design; not executed.** Use Python 3 arbitrary-precision integers, sets, `math.gcd`, and `time.process_time`. Generate the following finite family; the verifier must check each actual set's Sidon property rather than rely on a construction theorem.

1. For each prime \(p\) in the fixed list **67, 71, 79, 97, 127, 191, 257**, put \(M=p^2-1\). Let \(\delta\) be the least integer \(2\le\delta<p\) with `pow(delta,(p-1)//2,p)==p-1`.
2. Work with pairs \((a,b)\in\{0,\ldots,p-1\}^2\), identity \((1,0)\), and multiplication
   \[
   (a,b)(c,d)=((ac+\delta bd)\bmod p,(ad+bc)\bmod p).
   \]
   Factor the ordinary integer \(M\) by trial division. Among nonzero pairs in lexicographic order, choose the first \(z\) such that \(z^{M/\ell}\ne(1,0)\) for every distinct prime factor \(\ell\) of \(M\), using binary exponentiation with the displayed multiplication. Assert \(z^M=(1,0)\). Enumerate \(z^i\), \(0\le i<M\), and set \(B=\{i:\text{second coordinate of }z^i=1\}\). Assert \(|B|=p\) and that the enumerated powers are distinct. A failed assertion is a generator error, not a counterexample to SID-L.
3. For each \(s\in\{1,-1,2,3,5,7\}\) with \(\gcd(s,M)=1\), use every \(c=0,\ldots,M-1\) when \(p=67\); otherwise use \(c=\lfloor jM/32\rfloor\), \(j=0,\ldots,31\). Set \(A_0=\{(sb+c)\bmod M:b\in B\}\), with residues in \([0,M-1]\). Test **both** \((N,A)=(M,A_0)\) and \((\max A_0-\min A_0+1,A_0-\min A_0)\). Duplicates may be retained; never claim the two families are independent samples.
4. Sort each \(A\). Generate every positive difference from pairs of distinct elements. Check that their number is \(k(k-1)/2\) and that no value repeats; this independently checks the strong Sidon convention. Reject a generator failure with its full object. Skip only those instances with \(N<4096\) or \(k^2<N\), and count skips. For eligible sets compute \(T\) by integer binary search of \(10000T^4\ge38809N^3\); assert \(T\le N\).
5. Form the integer
   \[
   S=\sum_{\substack{1\le d<T\\d\notin D_+(A)}}(4T^3-6dT^2+2d^3).
   \]
   The **exact counterexample condition is \(100S<3kT^3\)**. Equality passes. Recompute any failure by a second direct loop through the missing distances; output \(p,z,s,c,N,A,k,T,S\), both integer sides and the list of missing \(d<T\). No floating tolerance is permitted.

**UNVERIFIED / resource estimate.** The fixed family has fewer than 30,000 generated sets before testing the two interval conventions, each with at most 257 points; streaming avoids large memory. The workload is expected below one CPU-hour but unbenchmarked here. Stop at **3300 CPU-seconds**, checking at least once per generated set. A timeout is **PARTIAL**, with the last completed \((p,s,c)\), eligible counts and skips. It is not full survival. No SAT/ILP or optimization solver is part of the test.

**UNVERIFIED / interpretation.** **SURVIVED** means all eligible objects in exactly this family passed the integer inequality, with generator checks completed. It does not cover all Sidon sets at even the smallest tested \(N\), much less near-extremal dense profiles for arbitrary large \(N\). These algebraic sets are deliberately a cheap falsifier, not a substitute for the lemma. The cost of exhaustive enumeration of dense Sidon sets at the lemma's onset is not hidden inside this specification.

**READ database / SECONDARY, UNVERIFIED independent certification.** [OEIS A143824 b-file](https://oeis.org/A143824/b143824.txt) gives \(F(N)=1,2,2,3,3,3\) for \(N=1,\ldots,6\), then 4 for \(7\le N\le11\), 5 for \(12\le N\le17\), and 6 for \(18\le N\le25\). The round-4 referee independently reports agreement through 24. These small values check conventions; none lies in SID-L's domain, and none is a test of SID-L.

### (f) G2, dates, activity and access limitations

| Source/check | Qualified finding as of 2026-10-09 |
|---|---|
| [#30 forum](https://www.erdosproblems.com/forum/thread/30) | READ: 9 comments; page lists Emmanuel_Audigé_Y., Rynaldos, TerenceTao and KMendoza as currently working. These are self-reports. The main page's 0.98183 entry, last edited 2026-04-06, lags later claims. |
| New competitor, johnakwei, **2026-10-05 15:04**, same thread | READ author post / LIVE CLAIM: coefficient \(<0.942809522\), advertised safely as 0.9428096; an asymmetric/two-sided smoothing limit \(2\sqrt2/3\); a pair-level semidefinite relaxation retaining variance and difference slack with the same limit. This is weaker numerically than SID-record and does not purport to constrain all realizable indicator sets. NOT ACCESSIBLE: linked [companion PDF](https://github.com/johnakwei/Science/blob/main/The_limit_of_vector-valued_smoothing_for_Sidon_sets.pdf) failed web text extraction; GitHub API confirms the file exists. UNVERIFIED: its proof and exact relaxation scope. Do not treat that barrier claim as a theorem. |
| [#30 proof-claims tab](https://www.erdosproblems.com/forum/thread/30/proof-claims) | READ: one claim by chenhaoyu, submitted **2026-10-02 19:06:21**, states SID-record and links the Lean theorem. It is our existing result, not a new independent competitor or a resolution of the original conjecture. |
| Hou–Zhao | READ primary arXiv: v1 2026-07-01, v3 2026-09-04, [Theorem 1.2](https://arxiv.org/html/2607.01169v3); LIVE CLAIM as qualified in (a). |
| Josh Madeiros and wustep | READ author forum post **2026-08-17** / LIVE CLAIM: approximately 0.94324445, with a claimed Lean check of covering inequalities, not the whole theorem. READ [wustep q2 README](https://github.com/wustep/maths/blob/da2440b68979b78d201182118d30ca418e3c2001/problems/sidon-second-term/compute/q2/README.md) / LIVE CLAIM: safe coefficient 0.94301. SECONDARY / UNVERIFIED here: the internal 2 October audit dates its last relevant commit/PR 69 to **2026-08-27**; no certificates were replayed. |
| Tao collaboration | READ own forum post **2026-02-17**: reports work with Carter, Georgiev, Gómez-Serrano, Hunter, O'Bryant and Wagner; 0.97633 and tentative approximately 0.947. LIVE CLAIM, neither current best nor evidence about SID-L. |
| arXiv refresh since the prior sweep | READ API query `(all:Sidon OR all:Golomb)` updated **2026-10-02–09** returned two papers: Dev Ranjan Pandey, [*Partition regular linear equations over Sidon sets*, 2610.11840](https://arxiv.org/abs/2610.11840), **October 8**, and Katalin Gyarmati, [*Translation-invariant equations in finite fields and groups*, 2610.09887](https://arxiv.org/abs/2610.09887), **October 7**. READ abstracts: uniformity/linear equations and finite-group avoidance respectively, not a new second-order upper coefficient. UNVERIFIED full-text exclusion. The earlier 2015–2026 chronology is in [G2_SIDON_20261002.md](/work/problems/erdos30/G2_SIDON_20261002.md); its unrefreshed details remain SECONDARY / UNVERIFIED. |
| OpenAI release | READ [release sweep](G2_OPENAI_RELEASE_20261009.md): no matching family for this Sidon frontier; no family-number closure to apply. |
| [Erdős Problem a Day #30](https://www.erdosproblemaday.com/report/30) | READ report: **SKIPPED**, citing the listed workers and a **2026-07-26** access date. It is a collision report, not a proof. |
| [OpenAlex W7167055292](https://openalex.org/W7167055292); Semantic Scholar | SECONDARY / UNVERIFIED completeness: OpenAlex's Hou–Zhao entry reports 0 citations. NOT ACCESSIBLE: Semantic Scholar paper/citations endpoint returned HTTP 429. Neither supports a priority claim. |
| Mathlib / Zulip | READ: public GitHub search of open `leanprover-community/mathlib4` PRs for `Sidon` returned 0. The existing bound is in the independent repository above. UNVERIFIED: comprehensive open-PR/Zulip coverage; indexed Zulip search found no relevant current hit. No formalization of SID-L is asserted. |

### (g) Product if proved

**UNVERIFIED / assessment: important milestone**, a coefficient reduction of \((10\sqrt2-\sqrt{197})/15\), approximately 0.00710 (0.75%), beyond the full-difference scalar method's claimed barrier. It leaves exponent \(1/4\) and the original Erdős conjecture unchanged; the output stated here is asymptotic, not a new effective onset theorem.

## Search boundaries and handoff

**READ.** Primary statements and proof-loss passages were inspected for both admitted cards; catalogue-only candidates were excluded when those prerequisites were missing. Searches combined the mandated local catalogues, live problem/forum pages, journal PDFs, arXiv pages/API, public GitHub code/CI/PR metadata, OEIS, OpenAlex and attempted Semantic Scholar access. No forum posts, email, community PRs, publication, commit, proof search, or finite lemma test was performed. Local global-memory tooling was not available in the callable tool inventory; the on-disk catalogues supplied the continuation evidence.

**UNVERIFIED / limitations.** Search-engine indexing, exact-keyword API queries and citation databases can miss new work. The #30 competitor's full proof and #222 original historical articles have the access limits stated above. The finite tests deliberately cover much less than the quantified hypotheses. The proposed constants and onsets are frozen test targets, not empirically fitted discoveries. SURVIVED must not be reworded as PROVED, likely true, or a record improvement.

**READ / next action for AUT-51.** Rank these two cards, send the selected finite specification to the verifier, and use its exact failure witness or explicitly bounded survival result before allocating a research slot. If both fail or offer insufficient tractability, retain the exclusions and request a different structural lemma; do not relaunch the saturated relaxations.

**Cost:** approximately 18 minutes wall time, 2026-10-09 15:43–16:01 UTC; 11 batched web-tool calls plus direct public HTTP/API fetches (at least 50 attempted URLs/requests in total; exact total not instrumented). Token usage unavailable. No paid compute; no solver or finite-test CPU used. File structure and whitespace were checked; the candidate tests are reserved for the verifier.
