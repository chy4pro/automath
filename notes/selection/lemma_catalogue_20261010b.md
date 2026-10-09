DONE — 14 new records across five areas; zero admissible lemma cards. This bounded screen did not establish worldwide priority or certify every current-record claim.

# Literature catalogue — widening pass 2, round 2026-10-10

**READ / scope.** Checked on 2026-10-09 UTC for AUT-69. The companion [shortlist](lemma_shortlist_20261010b.md) records every exclusion and the bite-regime gate. No proof, falsification experiment, certificate replay, solver run, posting, or contact was performed.

**READ / labels.** READ means the identified primary passage was inspected, not independently verified. SECONDARY means an attribution or database account rather than its underlying proof. NOT ACCESSIBLE identifies an unsuccessful primary-text access. LIVE CLAIM identifies an unrefereed mathematical assertion, or an explicitly marked Scout selection assessment. Multiple labels distinguish access from verification. Publication metadata does not certify a computation. An unspecified onset remains unspecified.

**READ / exclusions enforced.** The screen used [SELECTION.md](/work/SELECTION.md), [targets](targets_20261003.md), [old records](old_records_20261003.md), the [9 October shortlist and exclusion table](lemma_shortlist_20261009.md), [pass 1 C1–C8](lemma_catalogue_20261010.md), and [release audit section A](G2_OPENAI_RELEASE_20261009.md). Real sum–product and distinct subset sums were already screened, despite appearing among this task's suggestions. They were not reconsidered. The five new areas below are distinct-modulus coverings, finite-group zero-sum constants, integer sums of dilates, finite order-two additive bases, and bounded-denominator unit-fraction subsets. The latter does not reconsider #304 short representations, #295 lower-bounded denominators, or practical-number divisor representations.

**LIVE CLAIM / interpretation of “record”.** Each entry gives the strongest relevant statement located, an exact sharp result, or an explicitly identified baseline whose bestness could not be established. B4 and B6 contain recent unrefereed claims. B7's optimal additive constant and B9's disputed improvement remain unresolved in this dossier. These are exclusions, not certified current frontiers handed to a prover.

## Distinct-modulus covering systems

### B1 — minimum modulus

**READ.** Balister–Bollobás–Morris–Sahasrabudhe–Tiba, [*On the Erdős covering problem: the density of the uncovered set*, Theorem 8.1](https://arxiv.org/html/1811.03547v1), preprint 2018, refereed [Inventiones 228 (2022), 377–414](https://doi.org/10.1007/s00222-021-01087-5): a finite family of arithmetic progressions with distinct moduli all at least **616000** cannot cover Z. Thus a covering has minimum modulus **<616000**, equivalently at most 615999. No asymptotic onset. The qualitative boundedness question is solved; the optimal cutoff is not determined here. Proof sections 3, 6, 8 inspected.

**SECONDARY.** The [#2 page](https://www.erdosproblems.com/2) reports Owens's minimum-modulus-42 construction. Its original certificate was not inspected. Attention: the [thread](https://www.erdosproblems.com/forum/thread/2) contains three 14 October 2025 comments correcting Hough's historical bound to 10^16; this is discussion, not a new improvement.

### B2 — explicit uncovered-density coefficient

**READ.** Same paper, **Theorem 1.1**: for every ε>0 there exists M=M(ε) such that, for distinct moduli d_i≥M, the uncovered density is at least **(1/2)exp(−4C)**, where C=Σ_i μ(d_i)/d_i and μ is multiplicative with μ(p^j)=1+(log p)^(3+ε)/p for every prime p and j≥1. μ is a weight, not the Möbius function. **No numerical M is supplied.** Statement and proof ingredients inspected; a fully effective finite-cutoff record was not obtained. Same publication and attention trail as B1.

### B3 — squarefree moduli

**READ.** Cummings–Filaseta–Trifonov, [*An upper bound on the minimum modulus in a covering system with squarefree moduli*, Theorem 1.1 and §4.1](https://arxiv.org/html/2211.08548v1), 2022 preprint: every finite distinct squarefree covering has minimum modulus **≤118**. All finite systems; no onset. **SECONDARY publication metadata:** [Acta Mathematica Hungarica 175 (2025), 1–25](https://doi.org/10.1007/s10474-024-01496-x), refereed.

**READ / proof loss.** Lemma 3.1 and §4 bound the sum of distorted masses. The reported computed total is 0.999385061449…<1; §4's tail estimate says it “ignored negative quantities.” The Maple computation and rounding were not replayed. A smaller numerical total alone supplies no new realizability lemma. Attention: 2025 publication and the covering citation trail below. No inspected squarefree construction near 118 was found; Owens's general construction must not silently be treated as squarefree.

### B14 — a gap above reciprocal sum one

**READ.** Filaseta–Kalogirou, [*Covering systems with the sum of the reciprocals of the moduli close to 1*, Theorem 1](https://arxiv.org/html/2407.15280v1), 2024 preprint: every finite distinct covering with minimum modulus **>4** satisfies

\[
\sum_m 1/m\ge 1+\exp(-3.363054\cdot10^{21}).
\]

**SECONDARY publication metadata:** [Transactions AMS, DOI 10.1090/tran/9670](https://doi.org/10.1090/tran/9670), 2026. This resolves the stated Davenport/Erdős–Selfridge positive-gap question, not the optimal numerical gap. No size onset.

**READ / proof loss and attention.** Sections 2–3 inspected. Equation (6)→(7): “allowing m_j to range over all p_{i−1} smooth numbers” drops actual divisor restrictions in a fourth-moment bound. Lemma 1 gives a tail estimate for prime indices N≥10^9; Lemmas 3–4 select much larger cutoffs. Improving that estimate while retaining realizability and producing a certified replacement for the displayed exponential constant was not specified. The named historical proposers and 2024/2026 paper are the attention evidence; no independent current numerical competitor was identified.

## Zero-sum constants

**READ / conventions.** In the sources below, D(G) forces a nonempty zero-sum subsequence of a sequence over G; repetitions are allowed. s(G) forces a zero-sum subsequence of exactly exp(G) terms. D_k(G), forcing k disjoint zero-sum subsequences, is a different invariant. C_n^r is the direct sum of r cyclic groups of order n.

### B4 — D(C_n³), including a 2026 claim

**READ + LIVE CLAIM.** Max Grinsztajn's [author README, pinned 848b081e40ecd769017a6199ebcb4e31fe125483](https://github.com/maaxgrin/davenport-cn3-bound/tree/848b081e40ecd769017a6199ebcb4e31fe125483), latest commit located 27 May 2026, asserts for every n≥2

\[
D(C_n^3)\le4n-P(n)-2,
\]

where P(n) is the largest prime-power divisor of n. It records the input D_k(C_p³)≤pk+p² for k≥3p−2. **NOT ACCESSIBLE:** the paper PDF could not be retrieved through the attempted GitHub/raw routes; no theorem number or proof loss was recovered. **READ:** the Lean development expressly retains cited inputs as axioms; it is conditional, not an end-to-end verification. No replay.

**READ / older comparator.** Zakarczemny, [*Note on the Davenport's constant for finite abelian groups with rank three*, Corollary 3.11](https://arxiv.org/html/1910.10984v1), 2019 preprint, gives for n≥2
3(n−1)+1≤D(C_n³)≤min{20369,3^ω(n)}(n−1)+1, with ω counting distinct prime divisors. **SECONDARY attention:** [Tao's optimization page](https://teorth.github.io/optimizationproblems/constants/53a.html) links the 2026 claim. The exact general value is not settled by either bound.

### B5 — s(C_n³), explicit Alon–Dubiner coefficient

**READ.** Zakarczemny, same primary text, **Lemma 3.8**: for every integer n≥2, **s(C_n³)≤20370(n−1)+1**. The statement, Remark 3.5, prime split, and lifting Theorem 3.7 were inspected. The optimized recurrence gives c(3)<20233.005; the proof combines the elementary small-prime estimate p³+p−1 for p≤139 with the larger-prime estimate for p≥149. The resulting all-n coefficient is explicit, not an asymptotic hidden constant. Publication was not independently checked here; the inspected version is the 2019 preprint.

**LIVE CLAIM / selection assessment.** This is the strongest explicit general s(C_n³) coefficient located, not an exhaustive current-best certification. No new estimate uniform in prime p was found. The 2026 D and D_k activity in the ledger does not automatically improve s; substituting a different invariant would be invalid.

### B6 — D(C_n⁴), a very recent universal-group bound

**READ + LIVE CLAIM.** Guoqing Wang, [*Disproof of a Conjectured Upper Bound for the Davenport Constant*, v3, 5 October 2026](https://arxiv.org/html/2609.29878v3), **Theorem 6.2**: D(G)≤(16/5)r exp(G) for every nontrivial finite abelian group of rank r. **Remark 6.9** sharpens this to

\[
D(G)\le\lfloor3.158464724\,r\exp(G)\rfloor-r.
\]

**READ / exact specialization.** For G=C_n⁴, n≥2, the latter is **floor(12.633858896n)−4**. The decimal is exact, not rounded: Lemma 6.8 states this convention. The lemma, remark, and portions of §6 were inspected; the full argument and numerical certificate were not independently audited. No refereed publication established.

**READ / scope.** The proof uses probabilistic group algebra and scalar prime-power estimates. Its separate counterexample theorem is not a determination of D(C_n⁴). **SECONDARY:** prime-power homocyclic cases have the stronger classical exact value 4n−3. This entry is a universal linear bound, not the best pointwise bound for each n. No precise structural replacement for its scalar estimates was obtained.

## Integer sums of dilates

### B7 — a uniform additive error for pA+qA

**READ.** Balog–Shakan, [*On the sum of dilations of a set*, Theorem 1.1](https://arxiv.org/pdf/1311.0422), preprint 2013, Acta Arithmetica 164 (2014), 153–162: for coprime integers 1≤p<q and every finite A⊂Z,

\[
|p\cdot A+q\cdot A|\ge(p+q)|A|-(pq)^{(p+q-3)(p+q)+1}.
\]

**READ / baseline limitation.** The authors do not optimize the additive error and give stronger special-case estimates. This displayed general bound is **not certified as the optimal/current smallest C_(p,q)**. Theorem and residue-class argument inspected. Their digit-block obstruction rules out a polynomial-in-q uniform error in the p=1 problem. No quantified new compatibility estimate was found.

### B8 — the sharp dilation-three inequality

**READ.** Same paper, **Theorem 2.2**: every finite A⊂Z has **|A+3·A|≥4|A|−4**; proof inspected. For n≥3, X={i+3x: i∈{0,1}, 0≤x<n} attains equality, as do integer affine images with nonzero scale. Thus the unrestricted constant cannot improve. The paper attributes the original result to Cilleruelo–Silva–Vinuesa. No asymptotic onset.

**READ / attention for B7–B8.** Ruzsa is the named proposer acknowledged by Balog–Shakan. [Conlon–Lim, 2024](https://arxiv.org/html/2409.17112v1) studies dilates in prime fields; its abstract and main theorem were inspected. This is recent neighboring activity, not a new unrestricted integer additive-error record. Shakan's [*Sum of many dilates*](https://doi.org/10.1017/S0963548315000164), 2015 online/2016 volume, concerns the multi-dilate extension. **SECONDARY** publication/scope metadata for that paper; its proof was not read.

## Finite additive bases of order two

**READ / convention.** Following the nonnegative finite-basis literature, let R(k) be the largest n for which some A⊂Z_≥0, |A|=k, satisfies [0,n]⊂A+A. Repeated summands are allowed; 0 must be in A. This differs from difference bases and infinite asymptotic bases. Define g(n) as the least size of such a basis for [0,n]. No existence of a limit R(k)/k² is assumed.

### B9 — the upper range coefficient / lower size coefficient

**SECONDARY.** Gang Yu, [*A new upper bound for finite additive h-bases*, JNT 156 (2015), 95–104](https://doi.org/10.1016/j.jnt.2015.04.007), refereed: **limsup R(k)/k²≤0.4585**. Located in Kohonen's primary introduction and the [#791 page](https://www.erdosproblems.com/791). **NOT ACCESSIBLE:** Yu's original proof; theorem number and proof-loss passage not recovered. No numerical finite-k onset obtained.

**READ + LIVE CLAIM / disputed stronger source.** Sultan Alzahrani's [2016 thesis, Theorem 1.1 and §6](https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=kent1479595346428957&disposition=inline) prints **0.45504** in the theorem but **0.4550452314** at the final Maple evaluation. These are different literal bounds. The relevant statements and final calculation were inspected; no rounding/error certificate was checked. The thesis improvement is **not adopted as a verified replacement**. This unresolved baseline alone blocks a record-improvement card. Neither coefficient comes with a numerical onset.

### B10 — an explicit construction coefficient

**READ.** Jukka Kohonen, [*An improved lower bound for finite additive 2-bases*, Theorem 1](https://arxiv.org/html/1606.04770v2), preprint 2016; [JNT 174 (2017), 518–524](https://doi.org/10.1016/j.jnt.2016.11.011), refereed: **liminf R(k)/k²≥85/294**. The construction and coverage proof were inspected. For each integer t≥2 its 42-component placement supplies |A|≤42t+8 and R(A)≥510t²−1; this is an explicit finite family.

**READ / loss.** Before Fact 1, contributions from two components of the same type are discarded because their sizes are O(t). The leading coefficient is determined by the finite placement. No improved placement or exact overlap lemma yielding a larger coefficient was specified.

**READ / attention for B9–B10.** The [#791 thread](https://www.erdosproblems.com/forum/thread/791) has two 24 September 2025 comments about references. [Weltge–Zyhalko, May 2026, Theorem 1.1](https://arxiv.org/html/2605.19449v2) gives a positive-proportion counting result for finite bases; its primary statement was read. It does not improve the minimal-cardinality coefficient. **LIVE CLAIM:** the [27 July 2026 Problem a Day report](https://www.erdosproblemaday.com/report/791) reports exact calculations through n=65 and discusses the thesis discrepancy; these computations were not replayed.

## Bounded-denominator unit-fraction subsets

### B11 — number of distinct achievable rational sums

**READ.** Put E_N={Σ_(j=1)^N ε_j/j: ε_j∈{0,1}}, including 0; ln_j denotes j-fold iterated natural logarithm. Bettin–Grenié–Molteni–Sanna, [*A lower bound for the number of Egyptian fractions*, Theorem 1](https://arxiv.org/html/2509.10030v1), September 2025, gives

\[
\log_2|E_N|\ge\frac{2N}{\ln N}
\begin{cases}
1,&\ln_2N\ge1,\\
\ln_3N,&\ln_3N\ge1,\\
(1-3/(2\ln_kN))\prod_{j=3}^k\ln_jN,&k\ge4,\ \ln_kN\ge3/2.
\end{cases}
\]

**READ / publication metadata:** [institutional record](https://iris.polito.it/handle/11583/3006694), Mathematics of Computation 2026, [DOI 10.1090/mcom/4190](https://doi.org/10.1090/mcom/4190). Proof Lemmas 1–2, 7–8 inspected. Lemma 2 retains only exact-doubling denominators. Lemma 8 explicitly discards an additive 2.2; recovering that already disclosed scalar gain is not a new structural lemma. **READ / reported exact values:** Table 2 gives |E_0|,…,|E_4|=1,2,4,8,16. Larger computations were not replayed. This counts rational values, not representations of one fixed rational.

### B12 — fixed-rational representation count: leading constant solved

**READ.** Conlon–Fox–He–Mubayi–Pham–Suk–Verstraëte, [*A question of Erdős and Graham on Egyptian fractions*, Theorem 1](https://arxiv.org/html/2404.16016v1), April 2024; refereed [Discrete Analysis 2025:28](https://discreteanalysisjournal.com/article/154329-a-question-of-erdos-and-graham-on-egyptian-fractions): for every fixed x∈Q_>0, the number of A⊂[n] with Σ_(a∈A)1/a=x is **2^(c_x n+o(n))**, where

\[
c_x=\int_0^1 h\left(\frac1{1+e^{\lambda/y}}\right)dy,
\qquad \int_0^1\frac{dy}{y(1+e^{\lambda/y})}=x,
\]

and h is binary entropy, λ the unique positive solution. c_1≈0.91117 is an approximation; the integral defines the exact constant. No numerical onset. Main statement, entropy argument, and absorption outline inspected, not every proof detail. The leading constant is matched from both sides; a leading-constant improvement is unavailable. **READ / attention:** Liu–Sawhney's simultaneous [Theorem 1.2](https://arxiv.org/html/2404.07113v1) obtains the same exponential rate for x=1, expressed with base e. The decimal coefficients in different bases must not be compared directly.

### B13 — reciprocal-mass threshold forcing a sum of one

**READ; LIVE CLAIM publication status.** Liu–Sawhney, [*On further questions regarding unit fractions*, Theorem 1.1](https://arxiv.org/html/2404.07113v1), April 2024 preprint: for every ε>0 there exists N_0(ε) such that every N≥N_0 and every A⊂[1,N] with **Σ_(a∈A)1/a≥(log N)^(4/5+ε)** contains a subset summing to one. **No numerical N_0.** Refereed publication was not established here. §6, including Lemma 6.1 and the application of Proposition 5.2, inspected.

**READ / loss and adjacent solved case.** Localization reduces available reciprocal mass before the Fourier argument. No exact uniform replacement was specified. The same paper's Theorem 1.3 proves the sharp ordinary-density coefficient **1−1/e**, with an ε margin and unspecified onset; tail intervals supply its obstruction. That sharp coefficient is not an alternative improvement target. These refine earlier Bloom/Croot work; a short-expansion theorem for one rational is a different statement.

## Small exact values and test provenance

**READ + LIVE CLAIM.** [Yiu, September 2026](https://arxiv.org/html/2609.04950v1) asserts **D_k(C_5³)=5k+10 for every k≥2**, including D_4=30, using exhaustive computations; statement and computational description read, certificates not replayed. These are multiwise constants, not D(C_n^r) with r=k. They provide recent activity, not an admissible new card.

**SECONDARY.** The classical prime-power formula D(C_(p^a)^r)=r(p^a−1)+1, restated by the inspected zero-sum sources, gives D(C_2³)=4, D(C_3³)=7 and D(C_2⁴)=5. The original classical proof was not inspected.

**READ / convention translation.** Güntürk–Nathanson's [2006 primary introduction](https://www.theoryofnumbers.com/melnathanson/pdfs/nath2006-112.pdf) lists interval *lengths* 1,3,5 for one-, two-, and three-element bases. In this dossier's endpoint convention these are R(1),R(2),R(3)=0,2,4. **SECONDARY:** Kohonen cites R(25)=212 from earlier computation. No new optimality computation was performed. Allowing negative basis elements changes the problem; that variant's OEIS values were not imported.

## Freshness, attention, and G2 ledger

**READ / search boundary.** Exact searches were made for the five areas and the named sources. An arXiv API title query for `covering systems`, `Davenport constant`, `Ginzburg-Ziv`, `sums of dilates`, `finite additive`, or `Egyptian fractions`, with submitted dates **2025-10-09 through 2026-10-09**, returned **24 records**, all title-screened. Relevant abstracts/full texts were opened selectively. The earlier broad all-field query failed/truncated and contained Ginzburg physics; it is not credited as complete coverage. Neither query covers all synonyms or updates of older papers.

**READ / recent primary scope checks.** The title scan found Wang and Yiu above, [minimum modulus 7 with constrained LCM (July 2026)](https://arxiv.org/abs/2607.19029), [coverings using primes 2,3,5 (May 2026)](https://arxiv.org/abs/2605.18644), and the finite-basis counting paper. The covering abstracts do not assert an improvement to B1. [Geroldinger–Wang–Yang, September 2026](https://arxiv.org/abs/2609.17127) concerns a different invariant ν(G); its abstract is not a homocyclic-D exact-value theorem. These are scope checks, not full-proof audits.

**READ / API responses; SECONDARY bibliographic evidence.** [OpenAlex BBMST record W3211924274](https://openalex.org/W3211924274) yielded ten citing works, including the squarefree and reciprocal-gap papers; [Kohonen W2428137983](https://openalex.org/W2428137983) yielded four, missing the known 2026 counting paper; [Yu W964999425](https://openalex.org/W964999425) yielded three. The [Semantic Scholar citation endpoint for arXiv:1910.10984](https://api.semanticscholar.org/graph/v1/paper/ARXIV:1910.10984/citations?fields=title,year,externalIds&limit=100) returned an empty list. These responses are incomplete evidence, not absence-of-work certificates.

**READ / public discussion access.** Both Erdős forum threads above were read by direct HTTP after inconsistent browser-tool access. The #2 page lists self-reported working/formalizing users: **LIVE CLAIM**, not a theorem audit. The [Problem a Day #2 URL](https://www.erdosproblemaday.com/report/2) returned **NOT ACCESSIBLE (404)**. The #791 report was read. A #311 report concerns approximation error, a different unit-fraction quantity, and was not used to establish B11–B13.

**READ / code-search results.** Public open Mathlib PR searches for `Davenport`, `"covering system"`, and `"unit fraction"` returned respectively two unrelated polynomial PRs (#41339/#41348), zero hits, and an unrelated S-unit PR (#40791). Indexed Zulip searches did not produce a matching thread. This is not an exhaustive repository, Zulip, or open-PR audit. B4's external Lean project remains conditional on its stated axioms. No formalization of a new lemma is claimed.

**READ / release-audit scope; LIVE CLAIM / G2 assessment.** The local release audit records short Egyptian expansions and neighboring fixed-length/prescribed-denominator statements in family 025. Those quantifiers do not themselves establish B11's number of distinct values, B12's all-length count with maximum denominator n, or B13's assertion about every supplied A. B12 is already solved by the independent 2024/2025 literature. No matching closure of B1–B11/B13–B14 was identified in the inspected audit, but there is **no priority clearance** for a nonexistent candidate lemma. No outward-facing action was taken.

**READ / next action.** The screen is complete. The coordinator should use the companion shortlist's fewer-than-three result under SELECTION.md rule 5. No proof or verifier assignment follows from this catalogue.
