DONE — 1 admissible, unproved lemma card; 8 new catalogue records. Fewer than three cards: the screened pool, not the selection method, is the bottleneck. No proof attempt or finite falsification test was run.

# Lemma shortlist — widened round 2026-10-10

**UNVERIFIED / ranking.** Rank 1 (the only card): **B4-L**, an important specialist milestone if proved. Product grade × discarded-information argument × test sharpness: moderate × moderate (a concrete scope distinction, no new mechanism established) × moderate. The test is exact and covers whole finite construction orbits, but the available structured sets are not known to approximate an upper-bound extremizer. Admission means a precisely falsifiable hypothesis with a conditional record improvement; it does not mean experimental support, likely truth, or tractability.

**READ / scope and labels.** Sources were checked on 2026-10-09 UTC. Definitions and freshness limits are in [the catalogue](lemma_catalogue_20261010.md). READ means primary text inspected; SECONDARY means another account; LIVE CLAIM means an unrefereed assertion without our certificate replay; UNVERIFIED applies to our proposed lemma, implications, ranking and runtime estimate. NOT ACCESSIBLE denotes an unsuccessful access. A bounded search is not a priority claim. This card is for **finite B4 sets**, not the previously screened B3/g=1 or finite Sidon second-order records.

## Card 1 — B4-L: joint occupation of differences of disjoint pair sums

### (a) Exact record and status

**READ.** Let R₄(N) be the maximum size of A⊆{0,…,N−1} such that equality of two four-term sums implies equality of their multisets, including repeated summands. Let β₄=limsup_N R₄(N)/N^(1/4). [White, Corollary 1.2](https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/an-optimal-l2-autoconvolution-inequality/8D109D51F271CC78EBDA2C99FB35612D), published online 2023 / volume 2024, gives β₄≤(4/0.574636066)^(1/4). Its proof explicitly reuses Green's equation (30), Theorem 15. This is refereed, with no finite-N onset stated.

**READ + LIVE CLAIM; UNVERIFIED conditional substitution.** [Rechnitzer, Theorem 1, February 2026](https://arxiv.org/html/2602.07292v1) supplies the stronger autoconvolution lower endpoint c_low transcribed exactly in catalogue C1. In White's transfer this gives the strongest located coefficient β₄≤(4/c_low)^(1/4). The combined statement is our direct substitution, not a newly numbered theorem in either paper. The numerical certificate was not replayed. This is not a determination of β₄ and not a claim that its defining limit exists.

### (b) Quoted loss in the proof

**READ.** [Green, *The number of squares and Bh[g] sets*, 2001, author copy, Lemma 2 and equation (12), pp. 5–6](https://people.maths.ox.ac.uk/greenbj/papers/number-of-squares-and-Bh%5Bg%5D.pdf): “We remark that the important feature of the above bound is the number 4.” The lemma caps the number of ordered, cross-disjoint representations of a₁+a₂−b₁−b₂=x by 4, separately for each x. Equation (12) sums these individual caps against a triangular weight, producing 4u². It does not keep their simultaneous occupation by pairs drawn from the same A. White improves the subsequent Fourier lower bound; this combinatorial cap remains the input.

**READ / convention.** Green uses a correlation convention in this passage. The definitions below replace the convolution notation by explicit ordered tuples, avoiding any sum-versus-difference ambiguity.

### (c) One exact candidate lemma, and its conditional output

**UNVERIFIED / proposed B4-L.** For every integer N≥256 and every B4 set A⊆{0,…,N−1}, put m=|A| and let u be the smallest positive integer with u^17≥N^13. For each integer x define

\[
T_A(x)=\#\{(a_1,a_2,b_1,b_2)\in A^4:
 a_1+a_2-b_1-b_2=x,\quad
 \{a_1,a_2\}\cap\{b_1,b_2\}=\varnothing\}.
\]

**UNVERIFIED / specification.** Tuples are ordered. Repetitions within either pair are allowed; only sharing between the two pairs is forbidden. Empty A is allowed. Define the integer

\[
D(A,N)=\sum_{1\le |x|<u}(4-T_A(x))(u-|x|).
\]

The proposed assertion, with no density condition or exceptional sets, is

\[
\boxed{100D(A,N)\ \ge\ u(u-1).}\tag{B4-L}
\]

**UNVERIFIED / calibration.** The saving 1/100 and onset 256 are fixed hypotheses chosen for this screen; neither is supported by an experiment. The statement retains the positions and shared summands of one actual 0/1 set. It does not assert a gap for arbitrary arrays satisfying T(x)≤4.

**UNVERIFIED / conditional substitution only.** In Green's equation (12), B4-L changes the leading triangular contribution from 4u² to at most (399/100)u²+O(u); the existing shared-summand term is O(m³u). Use the source's scales u≈N^(13/17), v≈N^(16/17), X≈N^(3/17), and the White–Rechnitzer Fourier lower bound. The conditional target is exactly

\[
\boxed{\beta_4\le\left(\frac{399}{100c_{\rm low}}\right)^{1/4}.}\tag{B4-output}
\]

**UNVERIFIED / quantifiers.** This means ∀ε>0 ∃N₀(ε) ∀N≥N₀(ε), R₄(N)≤((399/(100c_low))^(1/4)+ε)N^(1/4). No numerical N₀ is supplied by the cited asymptotic transfer. The lemma itself has explicit onset 256; it does **not** make the output a fully effective finite-N theorem. The coefficient ratio to the located record is exactly (399/400)^(1/4). There is no proof of B4-L here, and no new argument for the asymptotic transfer is claimed.

### (d) Information missing from the saturated relaxations

**READ / comparison.** [Round 3](selection_probe_20261002.md) and [round 4](astra_probes_round4_20261009.md) concern, among other things, scalar Sidon window moments, independent difference budgets, and B3 one-point moments/weighted holes. Their witnesses do not supply a B4 set whose **cross-disjoint pair-pair difference counts** nearly fill every small integer x. In B4-L the same pair {a,b} participates in many differences; their locations must be compatible with all four-term multiset uniqueness constraints simultaneously. Independent choices of T(x), or the histogram of T alone without which pairs realize x, discard that information.

**UNVERIFIED / exact limitation.** Thus those relaxation-saturation results do not themselves refute B4-L. This is a scope distinction, not a proof of a uniform deficit. The occupation deficit still asks for a new upper bound on a weighted count: merely renaming it supplies no method. The concrete omitted data are the incidence labels (which two pairs produce each x), their common integer coordinates, and four-term multiset uniqueness. The card requires these jointly; it does not propose a gap for independent arrays with T(x)≤4 or reoptimize the scalar autoconvolution constant. No quantitative use of those data has been established. The earlier falsified SQ-L and SID-L remain excluded.

### (e) Exact finite falsification test — specification, not executed

**UNVERIFIED / resource contract.** Implement with compiled integer code and arbitrary-precision integers for u^17 and N^13. Use one CPU, no SAT/ILP and no numerical roots. Stop at **3300 CPU-seconds**. Completion of every mandatory batch is necessary for SURVIVED; timeout means PARTIAL with the exact completed prefix. No change of δ, onset, parameters, or orbit after a failure is permitted.

**UNVERIFIED / predicate.** First verify each distinct candidate set's B4 property by enumerating all index multisets i≤j≤k≤l and rejecting any repeated sum from different multisets. For a valid set, enumerate ordered quadruples with the cross-disjoint condition and tally integer x. Compute D from the finite histogram using the baseline 4u(u−1); subtract T_A(x)(u−|x|) for every 0<|x|<u. Report FALSIFIED if 100D<u(u−1), retaining N,u,sorted A, the entire nonzero T histogram, and both integer sides. Recompute a failure independently without cached values. An invalid construction is a fixture/construction error, not a counterexample to B4-L.

**UNVERIFIED / mandatory batch 1 — whole algebraic orbits.** Use both families in (h) for every q∈{2,3,4,5}, every permitted b, every multiplier a∈(Z/MZ)× and **every** t∈{0,…,M−1}. Lift aD+t to {0,…,M−1}. Include the full set and every nonempty subset of that lift; subtract each subset's minimum, and call its span length s=max−min+1. Test at each distinct

\[
N\in\{\max(256,s),\max(512,s),\max(4096,s)\}.
\]

**UNVERIFIED / exact orbit accounting.** Also cover each reflected set and both ambient conventions {0,…,N−1} and {1,…,N}. For a normalized shape of span s, cover every ordinary translate k=0,…,N−s in the first convention and k=1,…,N−s+1 in the second. A cache may reuse D because a common integer translation leaves every tuple difference unchanged, and reflection exchanges x and −x. Record the translations represented by each cached result. **Do not** replace modular t enumeration by an unexplained representative cut. Enumerate every raw (family,q,b,a,t); exact equality of normalized sorted full sets permits deduplication before generating all their subset masks. Then deduplicate the normalized subsets before tallying quadruples. Record both raw orbit counts and unique full-set/subset counts. This covers the orbit of every subset without sampling masks or cuts. Reflection is already a modular multiplier, but retaining it as a check avoids convention mistakes.

**UNVERIFIED / mandatory batch 2 — dense small and greedy fixtures.** Enumerate every subset of {0,…,31} of cardinality at most four, keep the B4 sets, and test at N=256,512,4096. In addition, use every nonempty prefix of

```
0, 1, 5, 21, 55, 153, 368, 856, 1424, 2603, 4967, 8194
```

and each of its integer dilates dA for d=1,…,16. For each use the same span-dependent three N choices and complete ordinary translation/reflection coverage as in batch 1. These are fixed fixtures, not generated proof candidates. **READ database / SECONDARY optimality:** the displayed terms are from [OEIS A365300](https://oeis.org/A365300/b365300.txt), accessed by direct HTTP. They are greedy terms, not a claim of globally optimal diameters. Validate the B4 property before evaluating the lemma.

**UNVERIFIED / runtime estimate.** The largest modulus is 781 and the largest algebraic set has six points. There are fewer than 800 million raw (b,a,t) tuples under the crude bounds b≤M and φ(M)<M. For fixed b,a there are at most six normalized full-set cut shapes; reuse their stored keys while still enumerating every t for coverage. Deduplicate full shapes globally before expanding their at most 63 nonempty subset masks, and deduplicate again before computing T. This avoids one quadruple tally per raw tuple. A compiled implementation is a plausible sub-hour test; this has **not** been benchmarked. The 3300 CPU-second cap includes construction, validation and orbit work. If it expires, report PARTIAL, never full-orbit survival.

**UNVERIFIED / interpretation.** The whole orbit requirement applies to **every member of the explicitly bounded families q∈{2,3,4,5}**, including all its subsets, not to infinitely many q. Survival would not test larger fields, all B4 sets at N≥256, or near-extremizers at asymptotic density. Small constructions may leave an uninformatively large margin. Report minima by family and N, not just one pooled margin.

### (f) G2 status and activity

**READ / recent primary sources.** O'Bryant's January 2024 construction paper, Rechnitzer's February 2026 numerical refinement, and Woo's September 2026 removal paper establish current activity. These are named authors with public relevant work, not claims about who is presently attacking B4-L. The 94-entry arXiv last-12-month scan is documented in the catalogue. Croot et al.'s June 2026 abstract treats B4[g] inside fourth powers, a different domain. No inspected source supplies B4-L or a better unrestricted finite-B4 coefficient; exhaustive exclusion is UNVERIFIED.

**READ / distinction from forums.** No dedicated finite-B4 leading-constant forum thread was identified. Erdős #41 and its [local formal statement](/work/problems/formal-conjectures/FormalConjectures/ErdosProblems/41.lean) concern an infinite-sequence liminf, not R₄(N). #241 is the excluded B3 record. Do not turn either thread's status into B4 priority clearance. The release audit has no matching claimed closure for this quantitative statement.

**SECONDARY / coverage limits.** The OpenAlex and Semantic Scholar responses in the catalogue are incomplete even for known follow-ups. No relevant indexed Zulip hit was found, and the open Mathlib PR query `Sidon` returned zero. No exhaustive code/PR audit, dedicated Erdős Problem a Day finite-B4 report, or independent certificate replay was obtained. No posting or contact occurred.

### (g) Product grade if proved

**UNVERIFIED / assessment: important milestone**, a strict leading-constant improvement for a classical generalized Sidon problem, with a small coefficient gain. It would not settle β₄=1, prove the existence of its limit, or solve an Erdős conjecture. The effective onset of the lemma should not be advertised as an effective onset for B4-output. Finite survival alone is a selection result, not a publication result.

### (h) Adversary family and complete symmetry specification

**READ.** [O'Bryant, *Constructing Thick Bh-Sets*, JIS 27 (2024), Definitions 1–2, Theorems 3–4, Table 3](https://cs.uwaterloo.ca/journals/JIS/VOL27/OBryant/obry7.pdf) gives generalized Bose–Chowla/Singer families and inequivalent parameters. Table 3 reports five-/six-point Singer spans 71/156 at q=5. Hence q=5 and all subsets are mandatory at onset N=256. The source questions these families' near-optimality for h>2; they are the standard structured adversaries, not proved extremizers.

**READ / family definitions.** Fix a primitive θ in a field F_(q⁴). For every b modulo M=q⁴−1 with θ^b of degree four over F_q, use
\[
B(q,b)=\{a\bmod M:\theta^a=\theta^b+v,\ v\in\mathbb F_q\}.
\]
For Singer, fix primitive θ in F_(q⁵), put M=(q⁵−1)/(q−1), and take every b modulo M with θ^b of degree five over F_q; use the exponents of nonzero uθ^b+v, (u,v)∈F_q²\{(0,0)}, reduced modulo M. Their cardinalities are q and q+1 respectively. The moduli are 15,80,255,624 and 31,121,341,781.

**UNVERIFIED / construction implementation specification.** No external finite-field package is necessary: enumerate monic irreducible polynomials over F_p in lexicographic coefficient order, use the first, and choose the first primitive nonzero element in coefficient order. For q=4 embed F₄ as the elements satisfying z⁴=z in F_(2⁸) or F_(2¹⁰). A complete discrete-log table defines the exponent sets exactly. Check cardinality and cyclic B4 uniqueness before lifting. Enumerating all allowed b and all unit multipliers absorbs the generator choice; do not assume b=1 covers them. Field conjugations induce multipliers already included. The finite orbit to test is exactly {(aD+t) mod M: gcd(a,M)=1, 0≤t<M}, for every specified D, with all interval cuts and both conventions handled in (e).

## Why the other seven records did not become cards

**UNVERIFIED / screen decisions, not alternative lemma proposals.** These rows are exclusions; no unstated “promising lemma” is being handed to a prover.

| Catalogue entry | Exact missing gate |
|---|---|
| C2 | **READ:** Timmons already uses interval occupancy in addition to Fourier caps. No exact additional realizability inequality, onset and conditional numerical output were obtained. |
| C3 | **READ:** The displayed proof sums absolute Fourier coefficients. A different trigonometric polynomial alone would not meet this assignment's requirement to use information discarded by the saturated relaxations. No structural replacement was specified. |
| C4 | **READ:** the unbounded-excess subproblem is already resolved; the quantitative frontier has unspecified c and onset. No exact uniform improvement or suitable finite adversary family was supplied. |
| C5 | **READ:** 536 comes from a finite partition, not a lossy analytic bound. No explicit improved partition or extension lemma was found. |
| C6 | **READ:** the current paper already uses shifts; its §IV reports restricted width-11 searches as UNSAT. Those unaudited searches are not a universal obstruction, but no new admissible template was specified. |
| C7 | **READ:** Berry–Esseen and finite-group lifting are already used; both h and N thresholds need care. No new effective uniform estimate, complete adversary orbit and sub-hour falsifier were jointly available. |
| C8 | **READ:** the current proof already combines logarithmic energy with auxiliary-polynomial constraints. No concrete new arithmetic constraint and improved certificate were provided. |

**READ / next action.** The coordinator may assign B4-L's exact test to the verifier if this specialist-grade target merits the slot. This dossier schedules no proof campaign or follow-up scout run. The requested two-file selection task is complete; the mathematical lemma remains OPEN.

**READ / recovery provenance.** The prior run's delayed shortlist write became visible during recovery and was preserved. Recovery checked its primary B4 and construction locators, narrowed catalogue C3's current-record scope, and expanded the finite test to q=5 and every subset to include the source's best listed small Singer fixtures at the lemma's onset. These are specification repairs, not mathematical test results.
