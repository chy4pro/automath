DONE — Task025 selection complete: nine candidates, eighteen fresh probes and adversarial review. SID-B is the sole precise target improvement; it has same-vendor review, while cross-vendor/kernel verification and novelty clearance remain outstanding.

# Probe-based selection, 2026-10-02

Task025 started at 09:38:23 UTC. This file is an internal working report, not a publication or priority claim. The current task overrides older exclusions based merely on active competition. The nine candidate families are Sidon second-order bounds, diagonal Ramsey upper bounds, real sum-product lower exponents, restricted sums-differences upper exponents, almost-primes between squares, primes between consecutive powers, Linnik's exponent, Hadwiger–Nelson, and four MOLS of order22. The last two broaden the pool beyond the v3 shortlist; MOLS also occurs on the construction board.

Final checkpoint: all18 fresh probes and their adversarial reviews are complete. SID-B proves, in the internal reviewed sense, F(N)≤√N+(2√2/3)N^(1/4)+1 for every integer N≥207360000. This is below the located .943006169985179 live claim, whose certificate was not replayed. Recommend a bounded SID validation/consolidation campaign; the other eight targets remain open. The original Erdős30 conjecture remains open. Earlier provisional sections are chronological records superseded by the ranking and final verdicts.

## Method and provenance

- Read the protocol, current operating entry, selection strategyv3, selectionv3 including its skeptic corrections, construction board, and today's freshness report. Older proposed methods and ratings are not passed to probe agents.
- Status scouts have ordinary informed contexts. Every mathematical probe must start in a fresh context (`fork_turns:none`) containing only operational isolation instructions, definitions, exact frontier and target. No files, web, papers, previous probe outputs or coordinator methods are supplied. Existing informed seats may review results but do not count as clean-room probes.
- At most three worker agents can run alongside the root. Fresh-thread creation failures, actual attempt durations and partial results will be recorded; no solver or additional dependency is authorized here.
- Global-memory recall and its skill are unavailable in the exposed tool/skill catalog; no notice was returned and no preset was changed.
- Status is a bounded source search as of October2, not a proof that no unindexed work exists. A preprint or repository claim is labelled separately from independent verification. A changed number must clear mathematical review and subsequent novelty comparison before it can justify a campaign.

## Status-only source checks

### Additional candidate HN: Hadwiger–Nelson / Erdős508

For the graph on all of the Euclidean plane whose edges join points at distance exactly1, the current recorded interval is `5 ≤ χ(R²) ≤ 7`. The lower bound is de Grey2018 ([primary preprint](https://arxiv.org/abs/1804.02385), v3 May30,2018); the upper bound is classical. On October2 the [problem page](https://www.erdosproblems.com/508) still said OPEN, displayed these bounds, and showed one comment and zero proof claims. The [formal-conjectures statement](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/508.lean) also records the interval and marks the exact question open; its `sorry` statements are not kernel proofs of the two bounds.

The exact lower-bound probe target is a finite set of points with exact coordinates whose unit-distance graph has chromatic number at least6, together with a proof of non-5-colourability; an alternative exact general proof of `χ(R²)≥6` qualifies. A proof only for measurable or polygonal colour classes does not meet this target. [Sokolov–Voronov2025](https://arxiv.org/abs/2502.01958), still v1 February4, proves a seven-colour obstruction for a restricted class of map colourings, and therefore does not subsume this target. Today's bounded later-result search found no exact-target replacement. No claim is made that the open exact value cannot be resolved by finding a finite witness.

### Additional candidate M22: four MOLS of order22

`N(22)≥3` is the current located constructive lower bound; the target is `N(22)≥4`. A Latin square is a function `[22]²→[22]` whose restriction to each row or column is a bijection. Squares are mutually orthogonal when for every pair of distinct squares the ordered pair of entries takes each value in `[22]²` exactly once. The output must be four explicit squares, or an exact construction with a complete verification, with no relaxation to partial, quantum or anti-Latin squares.

The [Miller–Abel–Valkov–Fraser published paper](https://eprints.gla.ac.uk/343648/1/343648.pdf), December18,2024, Table1 row20 column2, gives3 and explicitly identifies four at22 as unresolved. The [institutional bibliographic record](https://eprints.gla.ac.uk/343648/) confirms the publication date and refereed status. MDPI direct page/PDF access failed or returned a challenge; the author's institutional published-version copy was accessible. October2 exact-phrase searches found no later four-square construction. The1978 origin date in the old board has not yet been independently re-established, so the defensible dated checkpoint here is the2024 table. Active researchers on this problem are not grounds for exclusion.

## Probe ledger

| Probe | Fresh seat | Dispatch / completion UTC | Actual output |
|---|---|---|---|
| HN-A | `/root/probe_hn_a`, no history | 09:49:38–10:07:31 reasoning; writeup received before2026-10-02T10:14:25.584Z | OPEN; number-field4-colouring and other restricted-route obstructions |
| M22-A | `/root/probe_m22_a`, no history | 09:50:38–10:06:02 reasoning; writeup received before2026-10-02T10:10:28.645Z | OPEN; three construction obstructions, exact44-row symmetry-restricted reduction |
| SID-A | `/root/probe_sidon_a`, no history | 09:55:40–10:12:07 reasoning; writeup received before2026-10-02T10:15:30.749Z | OPEN; exact omitted-difference inequality, weaker sqrt(15)/4 coefficient, boundary-relaxation obstruction |
| RAM-A | `/root/probe_ram_a`, no history | 10:09:28–10:24:30 reasoning; writeup received before10:27:58 | OPEN; conditional spectral criterion, recurrence countermodel, restricted local-step obstruction |
| SQ-A | `/root/probe_sq_a`, no history | 10:14:09–10:31:45 reasoning; writeup received before10:35:07 | OPEN; exact weighted-sieve sufficient inequality, failed-detector counterexample, n≤20 hand witnesses |
| SP-A | `/root/probe_sp_a`, no history | 10:27:56–10:42:54 reasoning; writeup received before10:46:13 | OPEN; conditional exponent258/193, missing rich-fibre energy estimate |
| SD-A | `/root/probe_sd_a`, no history | 10:34:25–10:49:32 reasoning; writeup received before10:51:34 | OPEN; exact entropy deficit, pointwise strictness, failed-shortcut counterexamples |
| POW-A | `/root/probe_pow_a`, no history | 10:46:42–11:01:41 reasoning; received before11:04:03 | OPEN; known-input finite coverage k85,n≤7.98billion; missing explicit bridge |
| LIN-A | `/root/probe_lin_a`, no history | 10:47:06–11:02:17 reasoning; received before11:06:01 | OPEN; explicit prime-power tail lemma, unproved uniform zero criterion |
| M22-B | `/root/probe_m22_b`, no history | 11:03:33–11:21:03 reasoning; received before11:29:35 | OPEN; independently recovers affine-projection obstruction, PBD obstruction and44-orbit reduction |
| HN-B | `/root/probe_hn_b`, no history | 11:05:56–11:21:20 reasoning; received before11:29:35 | OPEN; fractional-colouring barrier, rational-angle3-colouring, minimum14-vertex obstruction |
| SID-B | `/root/probe_sid_b`, no history | 11:22:07–11:38:35 reasoning; full output received before11:42:52 | PROVED after same-vendor review: coefficient2sqrt(2)/3,+1,N≥207360000; external/kernel gates pending |
| RAM-B | `/root/probe_ram_b`, no history | 11:30:01–11:47:41 reasoning; received before11:53 | OPEN;11/3 density-drop reduction and recurrence countermodel with exact fixed-width data |
| SP-B | `/root/probe_sp_b`, no history | 11:30:17–11:45:33 reasoning; received before11:49 | OPEN; exact collision criterion, conditional exponent401/300, arithmetic-progression obstructions |
| SQ-B | `/root/probe_sq_b`, no history | 11:48:27–12:03:31 reasoning; received before12:06 | OPEN; prime-union reduction/disjointness and fixed-polynomial CRT obstruction |
| SD-B | `/root/probe_sd_b`, no history | 11:50:58–12:07:43 reasoning; received before12:11 | OPEN; exact integer/cardinality reduction, independent3/2, sharp≤3-atom constants, nonrecord lower example |
| POW-B | `/root/probe_pow_b`, no history | 11:57:50–12:13:19 reasoning | OPEN; self-contained k85 coverage through465 |
| LIN-B | `/root/probe_lin_b`, no history | 12:05:36–12:20:43 reasoning | OPEN; uniform prime-power removal, sharp support criteria and exceptional-zero reduction |

The first fresh-probe request was rejected while three status/close-out workers were active. The retry succeeded after the analytic status scout completed. No informed context was relabelled as a clean-room attempt. Requested attempt bounds are approximately15–25 minutes of active reasoning with no artificial idle time; the final reported clock-interval totals appear in the completion section.

### Analytic candidate status (ordinary scout, completed before probes)

| Candidate | Current exact frontier and date | Probe target | Status qualification |
|---|---|---|---|
| SQ: almost-primes between squares | For every integer `n≥1`, some integer `n²<a<(n+1)²` has `Ω(a)≤3`, prime factors counted with multiplicity. Campbell [2603.10356v2](https://arxiv.org/abs/2603.10356v2), May19,2026; v1 March11. | Same universal statement with `Ω≤2`. | The old `Ω≤4` baseline is superseded. Campbell has a [JNT publication record](https://doi.org/10.1016/j.jnt.2026.07.014), volume293,488–508, issue April2027; [Crossref](https://api.crossref.org/works/10.1016/j.jnt.2026.07.014) registered the DOI August20,2026. The future issue date is not the initial result date; exact online publication day unverified. |
| POW: primes between powers | For every integer `n≥1`, a prime lies strictly between `n⁸⁶` and `(n+1)⁸⁶`. Lee [2602.14340v2](https://arxiv.org/abs/2602.14340), March3,2026. | Find a fixed integer `2≤k≤85` with the same all-`n` statement. | [Acta Arithmetica primary publisher record](https://www.impan.pl/pl/wydawnictwa/czasopisma-i-serie-wydawnicze/acta-arithmetica/online/116568/minimal-zero-free-regions-for-results-on-primes-between-consecutive-perfect-k-th-powers) shows online publication October1,2026, DOI10.4064/aa260304-20-7. A70th-power result for a special sequence does not replace the universal86. |
| LIN: Linnik exponent | Naslund [Hexagon2610.00018v1](https://hexagonmath.org/2610.00018), October2,2026, claims a uniform `q₀` such that every integer `q≥q₀` and every reduced residue class `a mod q` has least prime `P(a,q)<q^3.99`. | Prove the same uniform large-`q` statement for some fixed `L<3.99`. | Live preprint claim, not a fully verified theorem here. [Author repository](https://github.com/enaslund/linniks-constant-3.99) says full bound is not formalized or human-refereed. [PR205](https://github.com/teorth/optimizationproblems/pull/205), opened07:17:56UTC today, remained open/unmerged with no comments or reviews at the scout check. An explicit coefficient/onset at3.99 would be a different outcome, not an improved exponent. |

No later exact-target improvement was found in the analytic scout's bounded October2 searches. ScienceDirect full text and UWE direct access returned403; publisher search metadata and Crossref supplied Campbell's publication status, and IMPAN directly supplied Lee's. Hexagon's web-tool access failed but public HTTP GET succeeded. No certificates or proofs were replayed in this status pass.

### Additive/combinatorial candidate status (ordinary scout, completed before probes)

| Candidate | Exact frontier and dated source | Exact probe scope |
|---|---|---|
| SID: Sidon second-order coefficient / Erdős30 | Let `F(N)` be maximal size of `A⊂{0,…,N−1}` with `a−b=c−d≠0 ⇒ (a,b)=(c,d)`. Hou–Zhao [2607.01169v3](https://arxiv.org/abs/2607.01169v3), September4,2026, gives `F(N)≤√N+γ₀N^(1/4)+O(1)`, `γ₀≈.94349`. A stronger live self-published [q2 repository claim](https://github.com/wustep/maths/blob/da2440b68979b78d201182118d30ca418e3c2001/problems/sidon-second-term/compute/q2/README.md), August27,07:16:18UTC, gives `γ≈.943006169985179`. | Seek an explicit coefficient at most`.943` (a rational target safely below the live claim), with a uniform `O(1)` remainder for all sufficiently large integersN. Smaller changes would still require comparison with the exact algebraic live coefficient; decimal rounding alone is not progress. |
| RAM: diagonal Ramsey upper base / Erdős77 | `R(k,k)` is the least n for which every red/blue edge-colouring of `K_n` contains a monochromatic `K_k`. Lu–Wang [2609.14525v1](https://arxiv.org/abs/2609.14525v1), September13,14:02:57UTC, states `R(k,k)≤3.69507^k` for all sufficiently large integersk. | Prove a fixed explicit base `b<3.69507` valid eventually, or a strictly better limiting exponential bound. Any reported tiny gain must be checked against the source's underlying certified value rather than its rounded display. |
| SP: real sum-product lower exponent | For every `ε>0` there is `cε>0` such that all nonempty finite `A⊂R` satisfy `max(|A+A|,|AA|)≥cε|A|^(135/101−ε)`. Zhang–Wang–Zeng [2609.25711v1](https://arxiv.org/abs/2609.25711v1), September22,05:32:35UTC. | Prove the same statement with `135/101+δ−ε` for an explicit `δ>0`. All finite real sets, including mixed signs and zero, remain in scope. |
| SD: restricted sums-differences upper exponents (one family, two permissible targets) | For any finitely supported joint distribution `(X,Y)` on`R²`, `H(X−Y)≤(11/6)max(H(X),H(Y),H(X+Y))`; with `H(X+2Y)` included in the maximum the upper factor is`7/4`. Katz–Tao1999, still the upper records on [C3b](https://github.com/teorth/optimizationproblems/blob/main/constants/3b.md) and [C3c](https://github.com/teorth/optimizationproblems/blob/main/constants/3c.md) on October2. | Prove either universal inequality with an explicit strictly smaller factor. `X,Y` may be dependent, logarithm base is fixed, and `0log0=0`. Both independent probes receive both targets; SD is counted once, not as two completed candidate probes. |

These are frontier improvements, not claims to solve the associated original problems. [Erdős30](https://www.erdosproblems.com/30) and [Erdős77](https://www.erdosproblems.com/77) remain open. Their main-page numerical summaries lag current source claims. The original near-quadratic real sum-product conjecture has a [Bloom–Sawin–Schildkraut–Zhelezov disproof preprint](https://arxiv.org/abs/2605.28781v1), May27,2026; that does not subsume the lower-exponent target chosen here.

The q2 Sidon certificate was not replayed. The older August17 forum claim `.94325` also fails to capture its stronger value. Lu–Wang's linked formalization and interval checkers were not rebuilt. Zhang–Wang–Zeng's paper was not refereed here. The SD lower-side records `1.77898884` and `1.6747338950414058` do not settle either upper target: C3b's `1.77898884` is explicitly unverified/asterisked, and Lin's C3c lower construction ([PR185](https://github.com/teorth/optimizationproblems/pull/185), submitted September9, merged September26) is also asterisked in the repository summary. No lower certificate was replayed.

## First completed probe: M22-A (provisional review, not novelty clearance)

The agent proved an obstruction to any orthogonal pair whose field-valued symbol components have the form `A_i x+B_i y+c_i(a,b)` over an odd prime field, with A_i,B_i fixed across binary quadrants and arbitrary binary symbol components. Its proof handles nonzero quadrant-cocycle by a transversal parity contradiction, dependent field projections by fibre divisibility, and independent projections by parity summation or vanishing finite mixed differences. Root walked these cases and found no gap; independent adversarial review remains pending. This says nothing about quadrant-dependent coefficients or nonlinear field coordinates.

The agent also ruled out a proper-block PBD on22points with all blocks of size≥5, and ordinary independent transversal prolongation of an orthogonal pair. It gave necessary/sufficient44-entry conditions for four squares invariant under simultaneous order11translation. No functions satisfying those conditions, general impossibility theorem, or number improvement was obtained. Its reported clocked reasoning was15m24s; writeup followed. Novelty is not yet checked.

## Ranking and recommendation

**Select SID for a bounded 1–3 day validation/consolidation campaign.** It is the only family in which a fresh probe moved the exact requested frontier number. This recommendation is based on the complete proof and adversarial review below, not on an a priori rating. The other eight families do not currently clear the bar for a new campaign. The ordering below them reflects the specificity of the verified partial output, not a claim about their intrinsic difficulty or eventual chance of success.

Here “PASS” means root examination and an ordinary same-vendor adversarial mathematical check of the stated claims, with the scope repairs recorded later. It does not mean cross-vendor, human, or kernel verification. A conditional implication can pass while its hypothesis remains unproved.

| Rank / candidate | Dated frontier checked October2 | Actual outcomes of both clean-room probes | Verified? | New versus known | Recommended next step |
|---|---|---|---|---|---|
| 1 — SID, Sidon second term | Hou–Zhao v3 September4: coefficient .9434925907…; live q2 August27: .943006169985179, certificate not replayed. Uniform √N+γN^(1/4)+O(1). | A: exact omitted-difference inequalities and weaker sqrt(15)/4 bound. B: **F(N)≤√N+(2√2/3)N^(1/4)+1 for every integer N≥207360000**. | PASS, including B's signed-measure energy argument; specify right-continuous u(1)=e−1. | No matching or stronger coefficient located in the bounded comparison. Neither novelty nor priority is thereby established. B is strictly below the located live coefficient; A's coefficient is weaker. | Cross-vendor referee and focused primary-source comparison, then a concise explicit theorem if both gates pass. No automatic publication. |
| 2 — SD, restricted sums-differences | General joint finite-support real variables: 11/6 with three controlled forms, 7/4 with four; Katz–Tao1999, still the located upper records. | A: exact four-form entropy deficit, pointwise strictness, counterexamples to shortcuts. B: exact integer/cardinality encoding, independent-case3/2, sharp ≤3-atom constants and a nonrecord lower example. | PASS with small-support explanation and precise coupling; **no uniform exponent gain**. | The numerical bounds and conditional-copy framework are known. The particular deficit/strictness formulation has uncleared novelty. The independent3/2 bound follows from Tao. | Retain the exact deficit as a secondary research artifact. A new campaign requires a proved uniform stability mechanism; pointwise strictness does not supply it. |
| 3 — LIN, Linnik exponent | Naslund October2 claim L=3.99, full theorem unaudited/unformalized here; author PR205 still open. | A: fully explicit reciprocal prime-power tail beyond exponent1. B: uniform unweighted removal beyond exponent1, sharp sufficient Fourier-support criteria and exceptional-zero relative-error reduction. | PASS; no L<3.99 and no new effective onset. | Prime-power removal, explicit-formula and exceptional-zero frameworks are established. Exact local tail estimates have uncleared novelty. | Keep the useful reductions. Do not launch without a genuinely stronger uniform zero/error estimate; tail removal alone does not fix the main constraint. |
| 4 — SP, real sum-product | Zhang–Wang–Zeng September22: exponent135/101−ε for all finite real sets. Original near-quadratic conjecture has a separate2026 disproof. | A: conditional258/193 from an unproved rich-fibre energy condition. B: exact overlap criterion yielding conditional401/300 from an unproved small-product collision bound. Both give restricted counterexamples. | PASS as conditional results; neither condition proved. | Ray clustering and the controlling energy mechanism are known from Konyagin–Shkredov. Specific packaging has uncleared novelty. | No campaign until a new collision/energy estimate is supplied. Counterexamples to all-fibre bounds do not refute the actual existential conditions. |
| 5 — M22, four MOLS22 | Published December2024 table gives N(22)≥3 and leaves four open. | A/B independently recover obstructions for fixed affine field projections and simple PBD constructions, plus an exact44-orbit reduction. B shows why the obstruction cannot be broadened to arbitrary mates. | PASS in the odd-prime, fixed-coefficient/common-translation scopes; no four squares. | Classical half-order/q-step obstruction is known; exact affine classification novelty uncleared. Independent rediscovery is corroboration, not progress toward a construction. | Park until a concrete construction escapes these restrictions. Do not run prohibited solvers or fund generic symmetry search. |
| 6 — POW, primes between powers | Lee v2 March3, online publication October1: universal exponent86. | A: analytic k85 coverage through7,980,000,000 using Dusart. B: self-contained analytic coverage through465 and an exact effective bridge. Both rule out a simple interval transfer. | PASS; these are analytic finite-range theorems, not billions of executed prime checks. | A's prime estimate is known; B uses elementary factorial/Chebyshev bounds. Neither moves the universal frontier. | Require an explicit eventual onset that connects to a proved finite range; unspecified asymptotic onsets do not suffice. |
| 7 — HN, Hadwiger–Nelson | Exact plane chromatic number5≤χ≤7; de Grey2018 lower bound; problem page still open October2. | A: four-colouring for a special number field and geometric barriers. B: rational-angle/cyclotomic-integer3-colouring, known fractional-colouring barrier and a14-vertex necessary condition. | PASS with denominator and open-set qualifications; no non-5-colourable witness. | Core field colouring and fractional construction have known precedents. Some exact extensions/obstructions have uncleared novelty. | Retain restrictions for future construction design; no current witness or campaign. |
| 8 — RAM, diagonal Ramsey base | Lu–Wang September13: eventual3.69507^k. | A: conditional spectral base√(27/2) and recurrence/step obstructions. B: explicit11/3 density-drop reduction and a synthetic recurrence model respecting any fixed-width true data. | PASS with full-neighbourhood scope repair; no improved base. | No new numerical bound. Exact auxiliary formulations have uncleared novelty; recurrence countermodels are not graph colourings. | Need a new density-recovery or structural estimate. Recurrence axioms and local density bookkeeping alone are insufficient. |
| 9 — SQ, almost-primes between squares | Campbell v2 May19: Ω≤3 in every strict square interval; JNT DOI registeredAugust20, issueApril2027. | A: exact weighted-sieve sufficient criterion without positivity and20 hand witnesses. B: disjoint prime-union reduction for n≥4 and CRT obstruction to fixed finite polynomial candidate lists. | PASS with real-interval/integer-point distinction; Ω≤2 remains open even eventually here. | Basic sieve/Schur–CRT frameworks are known; exact reformulations have uncleared novelty. | No campaign without a genuine all-interval sieve saving or prime-distribution input. |

### The two best complete probe outputs

The requested full texts are retained verbatim in this same file:

1. [SID-B: explicit improved second-order coefficient](#full-probe-output-retained-sid-b), with the [adversarial verdict and density convention](#adversarial-verdict-sid-b--m22-b--hn-b).
2. [SD-A: exact four-form entropy deficit and its limits](#full-probe-output-retained-sd-a), with [source comparison](#sd-a-assessment-and-post-probe-comparison) and [adversarial scope repairs](#adversarial-verdict-sq-a--sd-a--sp-a).

SD-A is the second choice because it isolates a precise nonnegative deficit in an unrestricted upper bound and rigorously tests plausible shortcuts. This is a useful concrete reduction, **not** a second newly improved record. LIN-A's complete explicit tail proof is also preserved for comparison. In fact all nine A originals and SID-B's original are retained, so the selection can be revisited without reconstructing their arguments.

### Recommended bounded follow-up

Day1 should be a cross-vendor hostile review of the exact SID-B theorem and a focused source/priority check of the renewal half-line correction and finite signed-measure energy argument. The theorem to check includes the ordered nonzero-difference convention, coefficient2√2/3, additive constant1, and onset120^4; none may be replaced by an asymptotic numerical self-claim. The existing same-vendor PASS is sufficient to nominate it, not to describe an external review as completed.

Day2 should consolidate a self-contained proof with the right-continuous density representative, endpoint atoms, signed tails, and every constant retained. An actual error or located subsuming theorem is a stop gate. If the proof survives, decide whether the analytic method and explicit bound justify an announcement under the owner's publication standard. A smaller decimal alone is not a publication decision.

Use a third day only if review exposes a specific fix or a concrete substantial extension with a stated lemma. Do not fill the time by automatic constant optimization, repeat parallel probes, or launching the other eight campaigns. No new campaign, publication, push, community message, or formalization project has been executed by this selection task.

The original Erdős30 conjecture is **not solved**. The change is its N^(1/4) upper-bound coefficient, in the internal reviewed sense stated above.

## Assessment rules fixed before outcomes

A number moved means a proved statement with the full target domain and quantifiers, an exact better constant or exponent, and all coefficient/onset qualifications stated. A proved lemma or exact reduction is partial progress only; its implication gap remains visible. An ansatz obstruction rules out that ansatz, not the whole problem. A familiar theorem re-derived independently is mathematically valid but not new. Conditional or asymptotic-only versions of an all-integer target are recorded separately. No fixed weighting based on subject taste will override actual outputs; tied failures remain tied. The final two strongest outputs will be preserved verbatim as appendices before any editorial correction, followed by referee findings. No publication action is included in this task.

## Bounded arithmetic during the status gate

At10:08UTC root used exact Node BigInt cross-products on the two positive rational metadata values a,b in the [pinned Sidon q2 certificate](https://github.com/wustep/maths/blob/da2440b68979b78d201182118d30ca418e3c2001/problems/sidon-second-term/compute/q2/certs/r11_m48_L6.json). The checks prove `0.943006169985178 < sqrt(ab) < 0.943006169985180` and `943/1000 < sqrt(ab)`. Thus the rational probe target is strictly below the reported algebraic coefficient. This does not validate any inequality encoded by the certificate. One bounded exact command, tool-reported wall0.00005375s; no solver, CPU/RSS or model-cost claim.

RAM-A was dispatched fresh after M22-A completed, before2026-10-02T10:10:28.645Z.

## Full probe output retained: M22-A

The following is the producer's complete final mathematical output, retained before external novelty comparison. Its own assessment of significance is not a referee verdict.

---

OPEN. I did not construct four MOLS of order 22. I proved a substantial obstruction to finite-field doubling, two further obstructions to natural construction routes, and an exact reduced construction problem under an explicit symmetry assumption.

The clocked reasoning interval was **2026-10-02 09:50:38–10:06:02 UTC**, or **15 minutes 24 seconds**. The writeup below followed that final clock reading. I used no files, sources, solvers, computation, or additional agents.

**1. Affine projection doubling cannot produce even an orthogonal pair.**

Here is the strongest result obtained.

**Lemma.** Let \(p\) be an odd prime. Index rows and columns by
\[
(a,x),(b,y)\in\{0,1\}\times\mathbf F_p,
\]
and symbols by \(\{0,1\}\times\mathbf F_p\). Suppose two Latin squares have the form
\[
L_i((a,x),(b,y))
 =\bigl(e_i(a,x,b,y),\,A_i x+B_i y+c_i(a,b)\bigr),
 \qquad i=1,2,
\]
where \(e_i\) is completely arbitrary, \(A_i,B_i\in\mathbf F_p\), and \(c_i\) is an arbitrary function on the four binary pairs. Then \(L_1,L_2\) cannot be orthogonal.

Thus the result permits arbitrary binary outputs and arbitrary additive offsets in the four quadrants. The field coefficients must be fixed across those quadrants.

*Proof.*

Write the field-valued output as \(F_i\). First, the Latin property forces \(A_i,B_i\ne0\). For example, if \(B_i=0\), a fixed row has at most two possible field outputs and therefore at most four full symbols, fewer than \(2p\).

We use a preliminary parity observation. A Latin square whose binary output, after a permutation of its symbols, is \(a+b\pmod2\) has no transversal. Indeed, a transversal would select \(p\) cells in each half of the rows and columns. If it selects \(h\) cells in quadrant \(00\), it selects respectively
\[
h,\quad p-h,\quad p-h,\quad h
\]
cells in quadrants \(00,01,10,11\). It would therefore contain \(2h\) symbols with binary output zero. But exactly \(p\) of its symbols must have binary output zero, impossible because \(p\) is odd. Such a square has no orthogonal mate: a symbol class of an orthogonal mate would be a transversal.

For one of the proposed squares, temporarily omit the subscript and put
\[
\delta=c(0,0)+c(1,1)-c(0,1)-c(1,0).
\]
Within a fixed row, the two cells with a specified field output have opposite binary outputs. The same holds within a fixed column. Consequently
\[
\sigma=e+a+b\pmod2
\]
is unchanged when passing between those two cells.

Starting in quadrant \(00\), successively switch the column half, row half, column half, and row half, always retaining the field output. On returning to quadrant \(00\), the field coordinates have changed by
\[
(x,y)\longmapsto
\left(x-\frac{\delta}{A},\,y+\frac{\delta}{B}\right).
\]
If \(\delta\ne0\), this translation visits all \(p\) points on each line \(Ax+By+c(0,0)=f\). Therefore \(\sigma\) depends only on \(f\), throughout all four quadrants:
\[
e=a+b+g(F).
\]
Relabel the binary component of symbol \((e,f)\) as \(e+g(f)\). The preceding parity observation then excludes every orthogonal mate.

It remains only to consider \(\delta_1=\delta_2=0\). Subtracting a constant from each field output, write
\[
F_i=A_i(x+\alpha_i a)+B_i(y+\beta_i b),
\]
where
\[
\alpha_i=\frac{c_i(1,0)-c_i(0,0)}{A_i},
\qquad
\beta_i=\frac{c_i(0,1)-c_i(0,0)}{B_i}.
\]
The same row and column switches now show that the complete freedom in the binary output is precisely
\[
e_i=a+b+\psi_i(X_i,Y_i),\qquad
X_i=x+\alpha_i a,\quad Y_i=y+\beta_i b,
\]
for some arbitrary function
\(\psi_i:\mathbf F_p^2\to\mathbf F_2\).

Let
\[
D=A_1B_2-A_2B_1.
\]
If \(D=0\), within each fixed quadrant every nonempty fibre of the pair \((F_1,F_2)\) has size \(p\). Across four quadrants each fibre consequently has size divisible by \(p\). Orthogonality requires every field-output pair to have exactly four preimages, one for each pair of binary outputs. Since \(p\nmid4\), this is impossible.

Assume \(D\ne0\). For every prescribed \((F_1,F_2)=(f,g)\), there is exactly one cell in each quadrant. Orthogonality requires the four binary-output pairs at these cells to be all four elements of \(\mathbf F_2^2\).

Suppose first that \(\alpha_1=\alpha_2\). For fixed \(f,g,b\), changing \(a\) leaves both normalized coordinate pairs \((X_i,Y_i)\) unchanged and complements both binary outputs. Therefore the two quadrants with \(b=0\) produce one complementary pair of binary-output pairs, and the two with \(b=1\) must produce the other complementary pair. Equivalently,
\[
\psi_1(z_{1,00})+\psi_2(z_{2,00})
+\psi_1(z_{1,01})+\psi_2(z_{2,01})=1
\quad\text{in }\mathbf F_2,
\]
where \(z_{i,ab}\) denotes the normalized coordinate pair at the unique cell in quadrant \(ab\) with field outputs \(f,g\).

Sum this identity over all \(p^2\) choices of \(f,g\). For each fixed quadrant and each \(i\), the map
\[
(f,g)\longmapsto z_{i,ab}
\]
is an affine bijection of \(\mathbf F_p^2\), because \(D\ne0\). Thus each \(\psi_i\) is summed over its whole domain twice, and the left side totals zero in \(\mathbf F_2\). The right side totals \(p^2=1\) in \(\mathbf F_2\), a contradiction. The case \(\beta_1=\beta_2\) is identical with the two binary indices interchanged.

Finally suppose
\[
\alpha_1\ne\alpha_2,\qquad \beta_1\ne\beta_2.
\]
Fix \(F_1=f\). In the normalized coordinates of square 1, the four cells with outputs \(F_1=f,F_2=g\) lie on the line
\[
A_1X+B_1Y=f.
\]
Choose a coordinate \(t\in\mathbf F_p\) on this line. As \(g\) varies, their coordinates have the form
\[
t,\quad t+P,\quad t+Q,\quad t+P+Q,
\]
with \(P,Q\ne0\). Nonvanishing follows from \(A_2,B_2,D\ne0\) and the two inequalities between \(\alpha\)'s and \(\beta\)'s.

Put
\[
h(t)=(-1)^{\psi_1(X(t),Y(t))}.
\]
For square 1’s binary output to be balanced on these four cells, it is necessary that
\[
h(t)-h(t+P)-h(t+Q)+h(t+P+Q)=0
\]
for every \(t\).

Let \(k(t)=h(t)-h(t+Q)\). The equation says \(k(t)=k(t+P)\). Since \(P\ne0\) and \(p\) is prime, \(k\) is constant. Also \(\sum_t k(t)=0\), so \(k=0\). Thus \(h(t)=h(t+Q)\); because \(Q\ne0\), \(h\) is constant.

This holds on every line \(F_1=f\). Hence again
\[
e_1=a+b+g_1(F_1),
\]
which has no orthogonal mate by the parity observation. This completes the proof. \(\square\)

For order 22, this excludes a broad tempting approach: doubling field-11 Latin squares while retaining one common linear field formula in each square and trying to repair orthogonality entirely through binary labels.

The lemma does **not** cover coefficients that vary between quadrants, nonlinear field outputs, or general Latin squares.

**2. A proper-block PBD construction on 22 points is unavailable.**

**Lemma.** There is no pairwise balanced design on 22 points in which every block is proper and every block has size at least five.

*Proof.* Choose any block \(B\), with \(|B|=b\), and a point \(x\notin B\). The blocks containing the pairs \(\{x,y\}\), \(y\in B\), are distinct: otherwise a block would share two points with \(B\), contradicting unique pair coverage. These \(b\) blocks intersect one another only at \(x\). Each contributes at least four other points, so
\[
21\ge4b.
\]
Consequently every block has size five. At each point, however, the other 21 points would then be partitioned into sets of size four, impossible. \(\square\)

This excludes the usual strategy of assembling order 22 from smaller proper blocks all large enough to support four MOLS.

I also caught and rejected a stronger-looking but invalid intermediate idea: “Use the projective plane of order four, whose lines have size five, and put four field-5 MOLS on each line.” The required simultaneous idempotence is impossible. More generally, \(t\) mutually orthogonal idempotent Latin squares of order \(n\) satisfy \(t\le n-2\). At an off-diagonal cell \((r,c)\), their values avoid both \(r,c\), and are pairwise distinct because an equal value \(v\) in two squares would duplicate the pair \((v,v)\) already present at \((v,v)\). Thus order five supports at most three such idempotent squares.

**3. Ordinary transversal prolongation cannot preserve an orthogonal pair.**

**Lemma.** Start with two orthogonal Latin squares \(L,M\) of order \(n\). In each square, use the ordinary prolongation operation: choose a transversal, replace its entries by a new symbol \(\infty\), move its displaced entries into the appended row and column, and place \(\infty\) in the new corner. The two prolonged squares cannot be orthogonal.

*Proof.* Let their chosen transversals be \(T_L,T_M\). They must be disjoint, since an intersection would give an additional \((\infty,\infty)\) pair besides the new corner.

For the pairs \((\infty,s)\) to occur without repetition, \(T_L\) must also be a transversal in \(M\). Similarly \(T_M\) must be a transversal in \(L\).

Write \(c_L(r),c_M(r)\) for their selected columns in row \(r\). The new-column cell in row \(r\) contains the ordinary-symbol pair
\[
P_r=\bigl(L(r,c_L(r)),\,M(r,c_M(r))\bigr).
\]
This cannot equal an original pair on \(T_L\): the first coordinate determines its row uniquely on that transversal, forcing row \(r\), where the second coordinate differs because \(c_L(r)\ne c_M(r)\). It likewise cannot equal an original pair on \(T_M\), using the second coordinate.

Because the original squares were orthogonal, \(P_r\) occurred at a unique original cell. That cell lies outside \(T_L\cup T_M\), so its pair remains unchanged. The new-column occurrence duplicates it. \(\square\)

This excludes a simple “construct at order 21 and prolong” approach, while leaving more extensive trades or replacements open.

**4. An exact 44-row construction problem under order-11 translation symmetry.**

This is a restricted construction route, **not** a claim that every solution has this symmetry.

For each \(i=1,2,3,4\), seek functions
\[
s_i:\mathbf F_2^2\times\mathbf F_{11}\to\mathbf F_2,
\qquad
f_i:\mathbf F_2^2\times\mathbf F_{11}\to\mathbf F_{11}.
\]
Define
\[
L_i((a,x),(b,y))
 =
\left(
s_i(a,b,y-x),\
x+f_i(a,b,y-x)
\right).
\]
The following conditions are necessary and sufficient for these formulas to give four MOLS of order 22:

1. For each \(i\) and each fixed \(a\),
   \[
   (b,d)\longmapsto \bigl(s_i(a,b,d),f_i(a,b,d)\bigr)
   \]
   is a bijection of the 22-element sets involved.

2. For each \(i\) and each fixed \(b\),
   \[
   (a,d)\longmapsto \bigl(s_i(a,b,d),f_i(a,b,d)-d\bigr)
   \]
   is a bijection.

3. For every \(i<j\),
   \[
   (a,b,d)\longmapsto
   \bigl(s_i(a,b,d),s_j(a,b,d),f_j(a,b,d)-f_i(a,b,d)\bigr)
   \]
   is a bijection onto
   \(\mathbf F_2^2\times\mathbf F_{11}\).

*Verification.* In a fixed row, \(x\) is constant, so condition 1 is exactly the Latin row condition. In a fixed column, \(x=y-d\), so condition 2 is exactly the Latin column condition.

For orthogonality, prescribe two full output symbols \((u,z),(v,w)\). Condition 3 determines the unique triple \((a,b,d)\) satisfying
\[
s_i=u,\qquad s_j=v,\qquad f_j-f_i=w-z.
\]
Then
\[
x=z-f_i(a,b,d),\qquad y=x+d
\]
determines the unique cell. This proves sufficiency; reversing the argument proves necessity. \(\square\)

The outstanding input is therefore explicit: **four pairs of 44-entry functions satisfying these 16 bijections on 22 elements and six bijections on 44 elements**. I did not find them.

Lemma 1 further proves that at most one of the four functions \(f_i\) can have the form
\[
f_i(a,b,d)=\lambda_i d+c_i(a,b)
\]
with a slope independent of \(a,b\). Thus an attempted solution of this reduced problem must depart substantially from globally affine field-11 doubling.

No finite search or verification was performed. These are proved restrictions and a verified construction equivalence within a specified symmetry class; the requested four-square construction remains **OPEN**.

---

## Completed probe HN-A: provisional summary

No6-chromatic witness or general lower6proof. Proved claim: the unit-distance graph on `Q(sqrt(-3),sqrt(-11))` is exactly4-chromatic, via a2-adic residue colouring and a7-point spindle lower witness. The proof needs adversarial checking and novelty comparison; it is not a statement about all algebraic coordinates. Further results: direct Mycielski amplification violates the two-common-unit-neighbour property; diamond equality forcing vanishes at4colours; the explicit periodic open-disc independent set gives fractional chromatic number≤`8sqrt(3)/pi<5`; the annulus with radii`.9,1.1` is exactly3-colourable, preventing a small monochromatic cluster alone from giving the target contradiction; critical witness size≥12 and stress-count conditions are only weak necessary conditions. No restrictions on hypothetical colour-class measurability were introduced. Clocked reasoning17m53s plus writeup. SQ-A dispatched fresh after completion, before2026-10-02T10:14:25.584Z.

## Completed probe SID-A: provisional summary

No target number moved. The producer gives an exact inequality retaining short-index and omitted long-index Sidon differences, an exact nonnegative-weight certificate family, and a fully effective but weaker `F(N)≤sqrt(N)+(sqrt(15)/4)N^(1/4)+40` for`N≥257`. It exhibits a formal endpoint profile whose associated family of relaxed necessary inequalities permits coefficient`5/(3sqrt(3))≈.9622504486`, thus obstructing that specific relaxation from reaching`.943`. This is not a Sidon-set construction or a universal barrier to stronger use of the exact inequality. Reasoning clock09:55:40–10:12:07=16m27s, writeup after. Mathematical review/novelty pending.

After SID-A completed, ordinary informed reviewer `/root/ref_e1_b` began adversarial checking of ALL M22-A claims. That seat is not counted as a clean-room probe. RAM-A and SQ-A continue independently.

## Full probe output retained: SID-A

The following is the complete producer output, before novelty comparison or independent adversarial review.

---

**OPEN.** I did not obtain \(\gamma\le 0.943\). I obtained an exact inequality retaining previously discarded differences, a fully effective but weaker bound
\[
F(N)\le \sqrt N+\frac{\sqrt{15}}4N^{1/4}+40
\qquad(N\ge257),
\]
and an explicit obstruction to reaching the target using a particular boundary-only relaxation.

Tracked reasoning interval: **2026-10-02 09:55:40–10:12:07 UTC**. No sources, computation, solvers, files, or other agents’ results were used.

### 1. Exact inequality including omitted differences

Write
\[
A=\{a_1<\cdots<a_m\}\subseteq\{0,\ldots,n\},
\qquad n=N-1.
\]
For \(1\le k<m\), put
\[
D_k=km-\frac{k(k+1)}2,
\]
\[
E_k=\sum_{j=1}^k(k+1-j)(a_j+n-a_{m+1-j}),
\]
and
\[
U_k=\{a_j-a_i:j-i>k\}.
\]
All positive differences are distinct under the stated ordered-difference convention. Then
\[
\boxed{\;
D_k(D_k+1)+2E_k+
2\sum_{d\in U_k}(D_k+1-d)_+
\le k(k+1)n .
\;} \tag{1}
\]

Here \(x_+=\max(x,0)\).

**Proof.** The \(D_k\) differences with index gap at most \(k\) form a set \(S_k\), disjoint from \(U_k\). For any set \(S\) of \(D\) distinct positive integers, disjoint from a set \(U\),
\[
\sum_{s\in S}s
\ge \frac{D(D+1)}2+\sum_{u\in U}(D+1-u)_+.
\]
Indeed, for \(1\le t\le D\),
\[
\#\{s\in S:s>t\}\ge D-t+\#\{u\in U:u\le t\};
\]
sum these inequalities, using the tail-sum formula for \(\sum s\).

On the other hand, telescoping gives
\[
\sum_{s\in S_k}s
=\sum_{r=1}^k\sum_{i=1}^{m-r}(a_{i+r}-a_i)
=\frac{k(k+1)n}{2}-E_k.
\]
Combining proves (1). ∎

This retains all omitted positive differences, including those from the middle of \(A\).

### 2. An exact finite certificate obtained from (1)

Fix \(v\le m/2\), and let \(\lambda_1,\ldots,\lambda_v\ge0\). Define, for \(1\le j\le v\),
\[
\Phi_j(x)=\sum_{k=1}^v\lambda_k\left[
(k+1-j)_+x+
(j-k-1)_+(D_k+1-x)_+
\right].
\]
Then
\[
\boxed{\;
\sum_{k=1}^v\lambda_kD_k(D_k+1)
+4\sum_{j=1}^v\min_{x\ge0}\Phi_j(x)
\le n\sum_{k=1}^v\lambda_k k(k+1).
\;} \tag{2}
\]

**Proof.** For each \(j\le v\), there are \((j-k-1)_+\) omitted differences \(a_j-a_i\) within the first \(v\) points. Since \(a_i\ge0\), their contribution in (1) is at least
\[
(j-k-1)_+(D_k+1-a_j)_+.
\]
The last \(v\) points give the corresponding expression with \(n-a_{m+1-j}\). Their pairs are disjoint because \(2v\le m\), and their differences are distinct by the Sidon assumption. Add the weighted inequalities (1), then minimize separately over these \(2v\) endpoint coordinates. ∎

Thus (2) is a finite, exact necessary condition involving only \(m,n,v,\lambda_k\); no asymptotic hypotheses enter it.

### 3. Explicit consequence: coefficient \(\sqrt{15}/4\)

Here is a proof including a numerical constant and onset.

Put \(q=n^{1/4}\). The standard shift-counting argument first gives
\[
m<q^2+q+1. \tag{3}
\]
For completeness, choose \(t=\lceil q^3\rceil\) and count representations of \(x=a+s\), where \(a\in A\), \(0\le s<t\). Their total is \(mt\), their support has \(n+t\) positions, and their squared sum is at most \(mt+t(t-1)\). Hence
\[
m^2\le(n+t)\left(1+\frac{m-1}{t}\right)
\le q^4+q^3+(q+1)m-q.
\]
Substitution of \(q^2+q+1\) into the resulting quadratic gives the positive value \(q^2+q\), proving (3).

Assume \(q\ge4\) and \(m\ge q^2\); otherwise the desired conclusion is immediate. Set
\[
b=\sqrt{12/5},\qquad v=\lfloor bq\rfloor.
\]
Then \(2v\le m\). Apply (2) with every \(\lambda_k=1\).

We need the following elementary estimate:
\[
\sum_{j=1}^v\min_{x\ge0}\Phi_j(x)
\ge q^2\left(\frac{v^4}{96}-6v^3\right). \tag{4}
\]

To verify it, put
\[
\delta=\frac{v(v+1)}{2q^2}\le2.
\]
Since \(D_k+1\ge q^2(k-\delta)\), substitute \(h=j-1\) and \(Y=x/q^2+\delta\). The relevant discrete expression is bounded below by
\[
q^2\left[
\min_{Y\ge0}\sum_{k=1}^v
\big((k-h)_+Y+(h-k)_+(k-Y)_+\big)
-\delta\sum_{k=1}^v(k-h)_+
\right].
\]
The minimum can be restricted to \(0\le Y\le v\). As a function of \(k\), the summand is \(2v\)-Lipschitz. Replacing its sum by its integral loses at most \(2v^2\). That integral is
\[
\frac{(v-h)^2Y}{2}+\frac{(h-Y)_+^3}{6}.
\]
Its minimum, denoted \(g(h)\), is
\[
g(h)=
\begin{cases}
h^3/6,&0\le h\le v/2,\\[2mm]
(v-h)^2(5h-2v)/6,&v/2\le h\le v.
\end{cases}
\]
It is \(2v^2\)-Lipschitz, and direct integration gives
\[
\int_0^v g(h)\,dh=\frac{v^4}{96}.
\]
The second sum-to-integral replacement loses at most \(2v^3\). Finally,
\[
\delta\sum_{h=0}^{v-1}\sum_{k=1}^v(k-h)_+
=\delta\frac{v(v+1)(v+2)}6\le2v^3.
\]
These three losses prove (4).

Write \(S_r=\sum_{k=1}^v k^r\). From (2), (4), and
\[
\sum_kD_k(D_k+1)\ge m^2S_2-m(S_3+S_2),
\]
we obtain
\[
(m^2-q^4)S_2
\le q^4S_1+m(S_3+S_2)-\frac{q^2v^4}{24}+24q^2v^3.
\]
Use \(m\le q^2+3q\), from (3), and
\(m^2-q^4\ge2q^2(m-q^2)\). The standard power-sum formulas give
\[
m-q^2
\le \frac{3q^2}{4v}+\frac{5v}{16}
+\frac12+\frac9{32}+3+36.
\]
For clarity, the estimates used here are
\[
\frac{S_3}{2S_2}-\frac{v^4}{48S_2}
\le\frac{5v}{16}+\frac9{32},\quad
\frac{3(S_3+S_2)}{2qS_2}<3,\quad
\frac{12v^3}{S_2}\le36.
\]
The function \(3q^2/(4v)+5v/16\) is minimized at \(v=bq\). Rounding down adds at most \(5/(16v)\le5/96\). Consequently
\[
m\le q^2+\frac{\sqrt{15}}4q+40.
\]
Replacing \(n=N-1\) by \(N\) proves the announced bound for \(N\ge257\).

This is weaker than the supplied coefficient \(0.943006169985179\); it is not an improvement on that result.

### 4. A concrete limitation of the boundary-only relaxation

The preceding approach naturally suggests keeping all omitted differences inside the first and last \(O(q)\) points and passing to rank profiles. That particular relaxation cannot establish the target.

For a nondecreasing profile \(f:[0,\infty)\to[0,\infty)\), define
\[
E_\alpha(f)=\int_0^\alpha(\alpha-x)f(x)\,dx,
\]
\[
S_\alpha(f)=
\int_{\substack{0\le x<y\\y-x>\alpha}}
\big(\alpha-f(y)+f(x)\big)_+\,dx\,dy.
\]
When both endpoint profiles equal \(f\), the leading-order inequalities coming from (1), retaining only these endpoint pairs, are
\[
\gamma\le C_\alpha(f):=
\frac{\alpha+\alpha^{-1}}2
-\frac{2(E_\alpha(f)+S_\alpha(f))}{\alpha^2},
\qquad\alpha>0. \tag{5}
\]

Consider the explicit profile
\[
c=\frac{2\sqrt3}{5},
\qquad
f(x)=\frac32(x-c)_+.
\]
Direct integration gives
\[
C_\alpha(f)=
\begin{cases}
\displaystyle
\frac{1/2-c^2}{\alpha}+\frac{4c}{3}+\frac{\alpha}{54},
&0<\alpha\le3c,\\[3mm]
\displaystyle
\frac{3c}{2}+\frac{1-3c^2}{2\alpha}
+\frac{c^3}{2\alpha^2},
&\alpha\ge3c.
\end{cases} \tag{6}
\]

Here is a way to check that integration. Pairs entirely above \(c\) contribute nothing to \(S_\alpha\), since their image gap is \(3/2\) times their rank gap. Thus
\[
S_\alpha=
\frac{\alpha(c-\alpha)_+^2}{2}
+\int_{\max(c,\alpha)}^{c+2\alpha/3}
(y-\alpha)\big(\alpha-\tfrac32(y-c)\big)\,dy,
\]
with the integral zero when its upper endpoint is smaller. Also
\(E_\alpha=(\alpha-c)_+^3/4\). Substitution gives (6).

Since \(c^2=12/25\), the first branch has minimum
\[
\frac{4c}{3}
+2\sqrt{\frac{1/2-c^2}{54}}
=\frac5{3\sqrt3}
\approx0.9622504486,
\]
attained at \(\alpha=3\sqrt3/5\). The second branch is increasing on \([3c,\infty)\), and its initial value is larger. Therefore
\[
\boxed{\quad
C_\alpha(f)\ge\frac5{3\sqrt3}>0.943
\quad\text{for every }\alpha>0.
\quad}
\]

Thus even imposing every inequality (5) leaves a formal profile permitting \(\gamma=5/(3\sqrt3)\). This is a counterexample to the sufficiency of **that relaxation**, not a construction of Sidon sets or a counterexample to the requested theorem.

### Remaining gap

The exact inequality (1) is stronger than the relaxation just disproved. To approach \(0.943\), one needs additional restrictions linking the endpoint profiles to the middle of \(A\), or a quantitative contribution from omitted differences outside the two endpoint regions. I proved no such estimate strong enough to bridge the gap. The original target therefore remains **OPEN in this probe**.

---

## Adversarial verdict M22-A

Ordinary same-model reviewer `/root/ref_e1_b` independently rederived all four main claims and returned PASS: affine projection obstruction, PBD22 obstruction, common-indexing ordinary transversal prolongation obstruction, and the44-row equivalence. This was a proof review, not literature clearance or a finite solver check. The auxiliary general inequality for idempotent MOLS needs `n≥2`; its order5use is unaffected. The affine theorem uses an odd prime, not an arbitrary odd prime power. The symmetry in the44-row reduction is exactly simultaneous translation `(x,y,z)→(x+t,y+t,z+t)` with binary labels fixed, not every conceivable order11automorphism. Separate row/column rearrangements after prolongation and additional trades are outside the no-go result. The retained producer text above is unchanged; these qualifications govern its interpretation. Root also checked the proof cases. No four-MOLS construction follows.

## Adversarial verdict SID-A

Ordinary same-model reviewer `/root/ref_e1_b` independently checked the exact difference inequality, weighted certificate, all discretization and power-sum bounds, the floor choice, and the displayed boundary-profile calculation: PASS for all main claims. Its additive error total is`239/6<40`, so the stated numerical constant and onset are safe. Necessary wording qualifications: the generic auxiliary omitted set`U` must consist of positive integers (the actual`U_k` does); the relaxation obstruction says only that additional information beyond(5)is necessary, not that middle-region information is the only possible remedy. The baseline shift argument is used only in the stated`N≥257`regime, with its positive shift length. Root separately walked the discrete inequality and profile integration. No current record is improved, and novelty has not been checked.

---

## Full probe output retained: HN-A

**OPEN. I did not prove \(\chi(\mathbb R^2)\ge6\), and I found no finite non-5-colourable unit-distance graph.**

The clock-measured reasoning interval was **2026-10-02 09:49:38–10:07:31 UTC: 17 minutes 53 seconds**, followed by writing this report. I used only the clock tool: no files, sources, solvers, computation, or other agents. The results below are independently derived mathematical limitations of several attempted approaches, with no novelty claim.

## 1. A complete arithmetic obstruction: one natural construction field is exactly four-colourable

Identify \(\mathbb R^2\) with \(\mathbb C\). Set
\[
\zeta=\frac{1+i\sqrt3}{2},\qquad
\rho=\frac{5+i\sqrt{11}}6,\qquad
K=\mathbb Q(\zeta,\rho)=\mathbb Q(\sqrt{-3},\sqrt{-11}).
\]
Thus \(K\), viewed as a point set, consists of
\[
a+b\sqrt{33}+i(c\sqrt3+d\sqrt{11}),\qquad a,b,c,d\in\mathbb Q.
\]

**Proposition. The unit-distance graph on the entire point set \(K\) has chromatic number exactly \(4\).**

This rules out obtaining even a five-chromatic graph while remaining inside this particular field.

### Proof of the four-colour upper bound

Let
\[
B=\{a/b\in\mathbb Q:b\text{ is odd}\},\qquad R=B[\zeta,\rho].
\]
The relations
\[
\zeta^2-\zeta+1=0,\qquad
\rho^2-\frac53\rho+1=0
\]
show that \(R\) is spanned over \(B\) by \(1,\zeta,\rho,\zeta\rho\). These four elements are linearly independent over \(\mathbb Q\): the distinct quadratic fields \(\mathbb Q(\sqrt{-3})\) and \(\mathbb Q(\sqrt{-11})\) have compositum of degree four. Consequently, they form a \(B\)-basis of \(R\).

In
\[
A=R/2R
\]
write \(X,Y\) for the images of \(\zeta,\rho\). Then
\[
A=\mathbb F_2[X,Y]/(X^2+X+1,\;Y^2+Y+1).
\]
Complex conjugation preserves \(R\), since
\[
\bar\zeta=1-\zeta,\qquad \bar\rho=\frac53-\rho.
\]
Modulo \(2R\), it therefore satisfies
\[
\bar X=X+1=X^2,\qquad \bar Y=Y+1=Y^2.
\]
For every \(a\in A\), this gives
\[
\bar a=a^2.
\]
Furthermore, \(X^4=X\) and \(Y^4=Y\); the characteristic-two Frobenius identity therefore gives
\[
a^4=a\qquad(a\in A).
\]
In particular,
\[
a\bar a=0\implies a^3=0\implies a^4=0\implies a=0. \tag{1}
\]

Now suppose \(z\in K\) and \(|z|=1\). Choose the smallest integer \(k\ge0\) such that
\[
a=2^kz\in R.
\]
Such a \(k\) exists by clearing the powers of two in the four rational coefficients of \(z\).

If \(k>0\), then \(a\notin2R\), but
\[
a\bar a=2^{2k}
\]
reduces to zero modulo \(2R\). By (1), \(a\) reduces to zero, contradicting \(a\notin2R\). Hence
\[
|z|=1,\ z\in K\quad\Longrightarrow\quad z\in R. \tag{2}
\]

Let
\[
\mathbb F_4=\mathbb F_2[\omega]/(\omega^2+\omega+1).
\]
There is a ring homomorphism
\[
\phi:A\longrightarrow\mathbb F_4,\qquad X\mapsto\omega,\quad Y\mapsto\omega.
\]
For a unit-length \(z\in K\), (2) permits its reduction to \(A\), and
\[
\phi(z)^3=\phi(z\bar z)=1.
\]
Thus
\[
|z|=1\quad\Longrightarrow\quad \phi(z)\ne0. \tag{3}
\]

Choose one representative \(s_C\) for each additive coset \(C\in K/R\), and colour \(v\in C\) by
\[
c(v)=\phi(v-s_C)\in\mathbb F_4,
\]
where reduction modulo \(2R\) is implicit.

If \(|v-w|=1\), then \(v-w\in R\) by (2), so \(v,w\) belong to the same coset. Consequently,
\[
c(v)-c(w)=\phi(v-w)\ne0
\]
by (3). This is a proper four-colouring.

### Proof that four colours are necessary

Consider the seven points
\[
0,\quad 1,\quad\zeta,\quad1+\zeta,\quad
\rho,\quad\rho\zeta,\quad\rho(1+\zeta).
\]
They are distinct. Indeed, their moduli split them into groups of sizes \(1,4,2\), with moduli \(0,1,\sqrt3\), respectively. Writing \(\rho=e^{i\theta}\), we have \(0<\theta<\pi/3\), which distinguishes the arguments within each nontrivial group.

The points \(0,1,\zeta\) form a unit equilateral triangle. Both \(1\) and \(\zeta\) are unit distance from \(1+\zeta\). Therefore, in a three-colouring,
\[
c(1+\zeta)=c(0).
\]
Multiplication by \(\rho\) preserves distances, so the rotated diamond likewise forces
\[
c(\rho(1+\zeta))=c(0).
\]
But these two forced-equal vertices are joined:
\[
\left|\rho(1+\zeta)-(1+\zeta)\right|^2
=|\rho-1|^2|1+\zeta|^2
=\frac13\cdot3=1.
\]
This contradicts three-colourability. The upper bound already proved gives equality \(\chi(K)=4\). ∎

**Exact limitation.** Field operations on these directions and points remain in \(K\), so they cannot produce the target. New circle intersections can introduce algebraic extensions outside \(K\); the proposition gives no bound for those extensions or for arbitrary real coordinates.

## 2. Two geometric amplification routes fail

### Common neighbours and neighbourhood structure

**Lemma. Two distinct plane points have at most two common unit neighbours.**

If \(x\) is a common unit neighbour of \(a\ne b\), subtracting
\[
|x-a|^2=1,\qquad |x-b|^2=1
\]
places \(x\) on a line. That line intersects the unit circle about \(a\) in at most two points. ∎

Thus an injectively realised unit-distance graph cannot contain \(K_{2,3}\), even as a non-induced subgraph.

There is also a stronger description of each individual neighbourhood.

**Lemma. The unit-distance graph induced on the neighbours of one point is a disjoint union of induced subgraphs of six-cycles.**

Translate the point to zero. Its neighbours have the form \(e^{i\theta}\). Two of them are unit distance apart precisely when
\[
2-2\cos(\theta-\varphi)=1,
\]
or
\[
\theta-\varphi\equiv\pm\pi/3\pmod{2\pi}.
\]
Each orbit under addition of \(\pi/3\) contains six points, with precisely the six-cycle edges. Distinct orbits have no edges between them. ∎

In particular, every neighbourhood is bipartite.

### Mycielski amplification cannot raise a five-chromatic unit graph to six

For a graph \(G\) with vertices \(v_i\), its Mycielski construction has original vertices \(v_i\), clones \(u_i\), and an apex \(w\). It preserves original edges, joins \(u_i\) to \(v_j\) whenever \(v_iv_j\) is an edge, and joins \(w\) to every clone.

For completeness, this construction raises chromatic number by one. A \(k\)-colouring of \(G\) extends by giving each clone its original’s colour and giving the apex a new colour. Conversely, in a hypothetical \(k\)-colouring of the construction, call the apex’s colour \(k\). No clone has colour \(k\). Replace the colour of each original vertex coloured \(k\) by its clone’s colour. Adjacent original vertices cannot both originally have colour \(k\); the clone-original edges ensure the replacements give a proper \((k-1)\)-colouring of \(G\).

However, if \(v_j\) has at least three neighbours in \(G\), then \(v_j\) and \(w\) have at least three common clone neighbours. The common-neighbour lemma forbids a unit-distance realisation.

Every five-chromatic graph has a vertex of degree at least four, since maximum degree at most three permits greedy four-colouring. Therefore:

\[
\boxed{\text{The Mycielski construction of a five-chromatic graph cannot be a plane unit-distance graph.}}
\]

This eliminates that direct combinatorial amplification.

### Diamond equality disappears with a fourth colour

A diamond consists of terminals \(a,b\), two adjacent internal vertices \(x,y\), and all four terminal-internal edges.

With three colours, \(x,y\) use two colours and force \(a,b\) to share the third. With any \(q\ge4\), **every assignment of colours to \(a,b\) extends**: select two distinct colours outside \(\{c(a),c(b)\}\) for \(x,y\).

A concrete counterexample to five-colour equality forcing is
\[
c(a)=1,\quad c(b)=2,\quad c(x)=3,\quad c(y)=4.
\]

Consequently, attaching any number of diamonds with fresh, mutually unconnected internal vertices places no further restriction on an existing \(q\)-colouring for \(q\ge4\). An actual point construction may introduce additional unit edges; those additional edges would have to supply the missing constraint.

## 3. Every finite unit-distance graph has fractional chromatic number below five

This blocks an entire class of weighted independence arguments.

**Proposition. Every finite plane unit-distance graph \(G\) satisfies**
\[
\chi_f(G)\le \frac{8\sqrt3}{\pi}<5.
\]

### Proof

Let
\[
L=\{m(2,0)+n(1,\sqrt3):m,n\in\mathbb Z\},
\]
and let \(I\) be the union of the **open** discs of radius \(1/2\) centred at points of \(L\).

Nonzero lattice vectors have squared lengths
\[
4(m^2+mn+n^2)\ge4.
\]
Thus distinct disc centres are at least two apart.

Two points in one disc are at distance strictly less than one. Points in different discs are at distance strictly greater than one, by the triangle inequality and openness of the discs. Therefore \(I\) contains no unit-distance pair.

A fundamental parallelogram of \(L\) has area \(2\sqrt3\). Hence \(I\) has periodic density
\[
\delta=\frac{\pi/4}{2\sqrt3}=\frac{\pi}{8\sqrt3}.
\]

Let \(P\) be any finite point set, with nonnegative vertex weights \(w_p\). Translate \(I\) by a uniformly distributed vector \(t\) in one fundamental parallelogram. Each fixed point belongs to \(I+t\) with probability \(\delta\). Consequently,
\[
\mathbb E_t\!\left[\sum_{p\in P\cap(I+t)}w_p\right]
=\delta\sum_{p\in P}w_p.
\]
Some translate therefore gives an independent set of weight at least
\[
\delta\sum_{p\in P}w_p. \tag{4}
\]

To obtain the fractional colouring directly, for every subset \(S\subseteq P\), let \(p_S\) be the probability that
\[
P\cap(I+t)=S.
\]
Only independent subsets can have positive probability. Moreover,
\[
\sum_Sp_S=1,\qquad
\sum_{S\ni v}p_S=\delta
\]
for every vertex \(v\). Assign fractional weight \(p_S/\delta\) to each such independent set. Every vertex receives coverage one, and total weight is \(1/\delta\).

Finally, \(\pi>3\) and \(8\sqrt3<15\) imply
\[
\frac{8\sqrt3}{\pi}<5.
\]
∎

No measurability of hypothetical colour classes was used. The measurable sets here were explicitly constructed independent sets.

**Exact limitation.** From (4), every lower bound of the form
\[
\frac{\text{total nonnegative vertex weight}}
{\text{maximum independent-set weight}}
\]
is less than five. Rounding such a bound up to an integer can establish at most five colours. Thus the ordinary weighted independent-set relaxation cannot prove the six-colour target.

This does not give a five-colouring: fractional and ordinary chromatic numbers are different.

## 4. Arbitrarily small monochromatic clusters do not create a five-chromatic neighbourhood

A possible route was to exploit the existence of very close same-colour points, then forbid their colour on all their unit neighbours. The relevant neighbourhood has a strong independent upper bound.

**Proposition. The annulus**
\[
A=\{p\in\mathbb R^2:9/10\le |p|\le11/10\}
\]
**has unit-distance chromatic number exactly three.**

### Three-colour upper bound

Partition the angular coordinate into nine half-open sectors of width \(2\pi/9\). Give sector \(j\) colour \(j\bmod3\).

For points of radii \(r,s\), whose smaller angular separation is \(\theta\),
\[
|p-q|^2=(r-s)^2+4rs\sin^2(\theta/2). \tag{5}
\]

If two equally coloured points lie in the same sector, \(\theta\le2\pi/9\). Using
\[
\sin^2(\pi/9)<\sin^2(\pi/8)=\frac{2-\sqrt2}{4},
\qquad \sqrt2>\frac75,
\]
equation (5) gives
\[
|p-q|^2
<\frac1{25}+\frac{121}{100}(2-\sqrt2)
<\frac{383}{500}<1.
\]

If they lie in different sectors of the same colour, their smaller angular separation is at least \(4\pi/9\). Concavity of sine on \([0,\pi/3]\) yields
\[
\sin(2\pi/9)\ge\frac23\sin(\pi/3)=\frac1{\sqrt3}.
\]
Thus
\[
|p-q|^2
\ge4\left(\frac9{10}\right)^2\sin^2(2\pi/9)
\ge\frac{27}{25}>1.
\]
Neither case allows a unit edge within a colour.

### Three colours are necessary

Let
\[
q=6m+1,\qquad
r_m=\frac1{2\sin(\pi m/(6m+1))}.
\]
As \(m\to\infty\), \(r_m\to1\), so sufficiently large \(m\) gives \(r_m\in[9/10,11/10]\).

Place \(q\) equally spaced points on the circle of radius \(r_m\). Joining indices differing by \(m\) produces unit edges. Since
\[
\gcd(m,6m+1)=1,
\]
these edges form a cycle of odd length \(q\). Hence the annulus is not bipartite. ∎

Now let an arbitrary set \(C\) lie inside a radius-\(1/10\) disc about \(o\). Every point at unit distance from some member of \(C\) satisfies
\[
9/10\le |p-o|\le11/10.
\]
Therefore the union of all unit neighbourhoods of \(C\) is three-colourable.

**Exact limitation.** Making the cluster monochromatic forbids one colour on this union, but four colours remain available in a proposed five-colouring. The cluster alone supplies no contradiction; interactions with further points are essential.

## 5. Elementary necessary conditions for a finite witness

These are weak, but they give exact checks that a candidate must pass.

### At least twelve vertices

Suppose \(H\) is vertex-minimal among finite unit-distance graphs that are not five-colourable. Every vertex has degree at least five: otherwise a five-colouring of \(H-v\) extends to \(v\).

Writing \(n=|V(H)|\), count pairs of neighbours:
\[
\sum_v\binom{d(v)}2\le2\binom n2=n(n-1),
\]
because each pair of vertices has at most two common neighbours. Since \(d(v)\ge5\),
\[
10n\le n(n-1),
\]
so \(n\ge11\).

For \(n=11\), equality forces every degree to equal five. Their sum would be \(55\), contradicting the handshake lemma. Hence
\[
n\ge12.
\]

### Many equilibrium stresses

Let \(m=|E(H)|\), and form the usual rigidity matrix of the realised point configuration. Its kernel contains two independent translations and a rotation, so its rank is at most \(2n-3\). Because
\[
m\ge\left\lceil\frac{5n}{2}\right\rceil,
\]
its left kernel has dimension at least
\[
m-(2n-3)\ge\left\lceil\frac n2\right\rceil+3.
\]
Thus any such witness has at least that many independent equilibrium stresses.

Explicitly, a stress satisfies
\[
\sum_{j:ij\in E(H)}\omega_{ij}(p_i-p_j)=0
\]
at every vertex. Taking scalar products with \(p_i\) and summing over vertices gives
\[
0=\sum_{ij\in E(H)}\omega_{ij}|p_i-p_j|^2
=\sum_{ij\in E(H)}\omega_{ij}.
\]
Therefore every nonzero real stress has both positive and negative coefficients.

These dependencies are permitted; they do not furnish a contradiction.

## Remaining gap

The probe produced no mechanism forcing five neighbours of a point to receive all five colours, no alternative global obstruction to five-colourability, and no explicit finite certificate.

The routes examined fail for different proved reasons:

- Diamond equality is restricted to three colours.
- Direct Mycielski amplification violates the two-common-neighbour constraint.
- The specified spindle-generated field admits a four-colouring.
- Weighted independent-set bounds remain below five.
- A small monochromatic cluster has a three-colourable unit neighbourhood.
- Criticality and rigidity supply necessary conditions but no impossibility proof.

**The requested inequality \(\chi(\mathbb R^2)\ge6\) remains OPEN in this attempt.**

---

---

## Full probe output retained: RAM-A

**OPEN. I obtained no unconditional improvement on \(3.69507\).**

Measured active reasoning: **10:09:28–10:24:30 UTC, 15 minutes 2 seconds**. I used only the clock and standard mathematics, with no external material, computation, files, or other agents.

The strongest partial result is a fully proved spectral condition under which the smaller base
\[
b_*=\sqrt{27/2}=3.6742346\ldots
\]
suffices. The unproved gap is controlling the spectrum of an arbitrary Ramsey counterexample.

1. **A conditional bound below the target, proved completely.**

For a red/blue colouring of \(K_n\), define its real symmetric matrix \(S\) by
\[
S_{ii}=0,\qquad
S_{ij}=
\begin{cases}
1,&ij\text{ is red},\\
-1,&ij\text{ is blue}.
\end{cases}
\]

**Lemma.** Let \(k\ge4\), \(t=\lfloor k/2\rfloor\), and \(n\ge b_*^k\). If the colouring contains no monochromatic \(K_k\), then
\[
\lambda_{\max}(S)>\frac{n}{2^{t+1}},
\qquad
\lambda_{\min}(S)<-\frac{n}{2^{t+1}}.
\]
Consequently, either one of the inequalities
\[
\lambda_{\min}(S)\ge-\frac{n}{2^{t+1}},
\qquad
\lambda_{\max}(S)\le\frac{n}{2^{t+1}}
\]
is sufficient to force a monochromatic \(K_k\).

**Proof.** First, the elementary Ramsey recurrence gives
\[
R(a,b)\le \binom{a+b-2}{a-1}.
\]
Indeed, \(R(1,b)=R(a,1)=1\), and, at a vertex of a complete graph on
\(R(a-1,b)+R(a,b-1)\) vertices, either its red neighbourhood has at least \(R(a-1,b)\) vertices or its blue neighbourhood has at least \(R(a,b-1)\) vertices. Induction and Pascal’s identity prove the displayed bound.

Put
\[
B=\binom{2k-t-2}{k-t-1},\qquad z=\frac n{2^t}.
\]
I claim that
\[
B\le z/3,\qquad z\ge6.
\]

For \(k=2m\), the binomial theorem at probabilities \(1/3,2/3\) gives
\[
\binom{3m}{m}\le(27/4)^m.
\]
Therefore
\[
B=\binom{3m-2}{m-1}
=\frac{2m}{3(3m-1)}\binom{3m}{m}
\le\frac13(27/4)^m
\le z/3.
\]
For \(k=2m+1\),
\[
B=\binom{3m}{m}\le(27/4)^m,
\qquad
z\ge b_*(27/4)^m>3(27/4)^m.
\]
The claim follows; \(z\ge6\) is immediate for \(k\ge4\).

Now set \(L=-\lambda_{\min}(S)\), and suppose \(L\le z/2\). For any vertex subset \(X\) of size \(u>0\), the Rayleigh inequality gives
\[
\mathbf1_X^{T}S\mathbf1_X\ge-Lu.
\]
Hence the average red degree inside \(X\) is at least
\[
\frac{u-1}{2}+\frac{\mathbf1_X^{T}S\mathbf1_X}{2u}
\ge\frac{u-1-L}{2}.
\]

Greedily choose a vertex of at least this red degree and replace the current set by its red neighbourhood. After \(i\) choices, the chosen vertices form a red clique and the remaining set is their common red neighbourhood. Its size \(u_i\) satisfies
\[
u_{i+1}\ge\frac{u_i-1-L}{2},
\]
and thus
\[
u_i\ge 2^{-i}(n+L+1)-(L+1).
\]
In particular,
\[
u_t\ge z-(L+1)\ge z/2-1\ge z/3\ge B.
\]
The lower bounds are positive at all preceding stages, so the choices exist.

The remaining graph therefore contains either a red \(K_{k-t}\), which extends the selected red \(K_t\), or a blue \(K_k\). This proves a monochromatic \(K_k\), contradicting the hypothesis. Thus \(L>z/2\).

Interchanging red and blue replaces \(S\) by \(-S\), proving the other spectral inequality. ∎

**Precise limitation.** This proves the smaller base only for colourings satisfying the stated spectral condition. I found no argument forcing that condition in an arbitrary colouring without a monochromatic \(K_k\).

Both spectral extremes can be linear in \(n\) in ordinary colourings. For example, take three equal parts of size \(m\), colour everything red except the edges between the first two parts, and colour those blue. The resulting matrix has eigenvalues \(2m-1\) and \(-m-1\): corresponding vectors, constant on the parts, are \((1,-1,0)\) and \((1,1,-1)\). This example contains large red cliques; it refutes universal spectral control, not the desired Ramsey bound.

2. **The supplied diagonal bound cannot improve itself through the elementary recurrence and monotonicity alone.**

Here is a rigorous countermodel to that attempted inference.

Fix \(2<c<4\), put \(q=c/4\), and define
\[
U(a,b)=\left\lceil
q^{(a+b-2)/2}\binom{a+b-2}{a-1}
\right\rceil,
\]
\[
V(a,b)=\max_{\substack{1\le i\le a\\1\le j\le b}}U(i,j),
\qquad
F(a,b)=\max\{V(a,b),(a-1)(b-1)+1\}.
\]

Then \(F\) is symmetric, integer valued, and nondecreasing in each argument. It satisfies
\[
F(1,b)=1,\qquad F(2,b)=b,
\]
and
\[
F(a,b)\le F(a-1,b)+F(a,b-1)\quad(a,b\ge2).
\]
Nevertheless,
\[
F(k,k)\le c^k\quad\text{for all sufficiently large }k,
\qquad
\lim_{k\to\infty}F(k,k)^{1/k}=c.
\]

**Proof.** Write \(A(a,b)\) for the expression inside the ceiling defining \(U\). Pascal’s identity gives
\[
A(a-1,b)+A(a,b-1)=q^{-1/2}A(a,b)\ge A(a,b).
\]
Taking ceilings proves the recurrence inequality for \(U\). Also \(U(1,b)=1\).

For the recurrence for \(V\), consider a maximizing pair \((i,j)\). If \(i<a\), its value is already bounded by \(V(a-1,b)\). If \(j<b\), it is bounded by \(V(a,b-1)\). Otherwise use the recurrence for \(U(a,b)\).

The polynomial
\[
W(a,b)=(a-1)(b-1)+1
\]
has the same boundary values and satisfies
\[
W(a-1,b)+W(a,b-1)-W(a,b)=(a-2)(b-2)\ge0.
\]
The maximum of two functions satisfying this recurrence inequality also satisfies it. This proves the asserted recurrence for \(F\).

For \(i\le2\), \(j\le b\), one has \(U(i,j)\le j\), because
\[
U(2,j)=\lceil j q^{j/2}\rceil\le j.
\]
Consequently \(F(2,b)=b\).

For the diagonal upper bound, the binomial theorem yields
\[
A(i,j)\le q^{(i+j-2)/2}2^{i+j-2}
=c^{(i+j-2)/2}\le c^{k-1}
\]
whenever \(i,j\le k\). Hence
\[
F(k,k)\le
\max\{\lceil c^{k-1}\rceil,(k-1)^2+1\},
\]
which is at most \(c^k\) for all sufficiently large \(k\).

Finally, the central binomial coefficient is the largest coefficient in its row, so
\[
F(k,k)\ge
q^{k-1}\binom{2k-2}{k-1}
\ge \frac{c^{k-1}}{2k-1}.
\]
Taking \(k\)-th roots proves the limit. ∎

In particular, taking \(c=3.69507\) shows that symmetry, monotonicity, integrality, the usual boundary values, the elementary Ramsey recurrence, and the supplied diagonal estimate do **not**, by themselves, imply a smaller limiting base. Additional graph structure is necessary.

3. **A proposed density-preserving book algorithm fails on an explicit configuration.**

I investigated maintaining two disjoint sets \(X,Y\) with red density \(1/2\), taking red steps that restrict both sets to red neighbours, and blue steps that restrict only \(X\).

The tempting local assertion was that one could always either:

- take a red step retaining at least half of \(X\) while preserving red density at least \(1/2\) between the new sets; or
- take a blue step retaining at least half of \(X\), leaving \(Y\) unchanged.

This assertion is false.

**Counterexample.** Divide \(X\) into four equal groups \(X_1,\ldots,X_4\), each of size \(m\ge2\). Colour edges inside each group blue and between distinct groups red.

Divide \(Y\) into six equal groups \(Y_{ij}\), indexed by the unordered pairs from \(\{1,2,3,4\}\). Colour an edge from \(X_i\) to \(Y_{ab}\) red exactly when \(i\in\{a,b\}\).

Every vertex of \(X\) has red degree exactly \(|Y|/2\) into \(Y\). But for any \(v\in X_i\):

- Its red neighbourhood in \(X\) consists of the other three groups.
- Its red neighbourhood in \(Y\) consists of the three groups \(Y_{ij}\) with \(j\ne i\).
- Between those two new sets, the red density is exactly \(1/3\): each remaining \(X_j\) connects red to just one of the three remaining \(Y\)-groups.
- Its blue neighbourhood in \(X\) has size \(m-1<|X|/4\).

Thus the red step loses density, while the blue step loses more than three quarters of \(X\). Every possible pivot has this behaviour.

Large versions of this example already have large blue cliques inside the groups. Therefore this refutes the proposed **local lemma**, not a more sophisticated algorithm that detects and uses such blue cliques. I did not obtain the quantitative replacement needed to complete that approach.

4. **A counting approach gives a valid book lemma, but the available estimate loses too much.**

A monochromatic \(t\)-book means a monochromatic \(K_t\) together with vertices joined to every spine vertex in that same colour.

**Lemma.** Let \(t\ge2\), \(r=R(t+1,t+1)\), and \(n\ge r\). Every colouring of \(K_n\) contains a monochromatic \(t\)-book with at least
\[
\frac{n-t}{\binom r{t+1}}
\]
pages.

**Proof.** Let \(T_s\) count monochromatic \(K_s\)'s. Every \(r\)-subset contains a monochromatic \(K_{t+1}\). Double counting gives
\[
T_{t+1}\binom{n-t-1}{r-t-1}\ge\binom nr,
\]
or
\[
T_{t+1}\ge
\frac{\binom n{t+1}}{\binom r{t+1}}.
\]
Each monochromatic \(K_{t+1}\) contributes \(t+1\) incidences of a monochromatic \(K_t\) and one same-colour page. Since \(T_t\le\binom nt\), some spine has at least
\[
\frac{(t+1)T_{t+1}}{T_t}
\ge\frac{n-t}{\binom r{t+1}}
\]
pages. ∎

Substituting only an exponential upper bound \(r\le c^{t+1}\) gives the weaker guarantee
\[
(n-t)(t+1)!\,c^{-(t+1)^2}.
\]
For \(t\) proportional to \(k\) and \(n\) exponential in \(k\), this expression becomes negligible because of the negative quadratic exponent in \(k\). Thus this particular counting estimate does not supply the linear-length books needed for the target.

**Status:** the general problem remains **OPEN** in this probe. The explicit \(3.6742346\ldots\) constant above belongs solely to the proved spectral conditional result; it is not an improved bound for \(R(k,k)\).

---

## Completed probe RAM-A: provisional summary

Target OPEN. Clocked reasoning10:09:28–10:24:30=15m02s, followed by writeup. It proves: for`k≥4,t=floor(k/2),n≥(sqrt(27/2))^k`, every colouring with no monochromatic`K_k` must have both spectral extremes of its signed adjacency matrix beyond`±n/2^(t+1)`. Thus`3.6742346…`is solely a conditional base, not a new general Ramsey bound. It also constructs an integer monotone symmetric recurrence countermodel retaining arbitrary diagonal exponential base`c∈(2,4)`, gives a counterexample to an unqualified density-preserving local book step, and proves a weak book-count lemma whose loss is quadratic in the spine length exponent. The counterexamples do not satisfy every property of a large Ramsey counterexample and are only obstructions to their specified inferences. Root checked the main algebra; ordinary adversarial reviewer now has the complete HN-A and RAM-A outputs.

SP-A was dispatched fresh after RAM-A completed (before10:27:58UTC). HN-A and RAM-A then separately appended their own completed outputs verbatim, reading no existing report content; those mechanical archive tasks are not additional probes. Report append ownership was serialized. As of2026-10-02T10:33:16.402Z, completed clean-room attempts=4/18; SQ-A and SP-A active, one ordinary referee active. SD, POW and LIN have not yet started, and all nine B attempts remain outstanding.

## Completed probe SQ-A: provisional summary

OPEN both for alln and eventualn. Clocked reasoning10:14:09–10:31:45=17m36s, writeup afterward. It gives the exact counting identity for prime/semiprime witnesses, an explicit logarithmically weighted sieve sufficient inequality with elementary inclusion–exclusion error, and no positivity proof. It refutes a proposed truncated-Mobius positivity detector even on squarefree integers: n291,m85085=5·7·11·13·17 lies in the square interval but has positive detector value`3log(85264/85085)`. It supplies hand witnesses for n1…20 only. The generic weighted sieve is not claimed new; the pointwise all-interval positivity requirement remains completely open. Root checked the main exact identities and counterexample arithmetic; independent adversarial review remains pending. SD-A was dispatched fresh after SQ-A completed, before2026-10-02T10:35:07.626Z.

## Preliminary post-probe literature comparison (October2; not fed back to fresh probes)

For M22-A, the binary block-parity obstruction is classical: the step-type no-transversal theorem attributed to Maillet1894 is stated in the primary research paper [Latin squares with no transversals (2017)](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v24i2p45/pdf/), Section1/Lemma2. Its application to two odd-size binary blocks matches the parity step of the probe. This alone does not subsume the complete affine-projection classification: the step proving that an orthogonal pair would force that block form still requires its own comparison. A bounded exact-topic search did not settle the novelty of that full classification, so it remains UNCLEARED. The44-row quotient formulation is an elementary equivalence for a prescribed group action, not an existence theorem. [Evans2014](https://cmuc.karlin.mff.cuni.cz/pdf/cmuc1403/evans.pdf) studies other prolongation classes and their mate restrictions; it is relevant context, not proof that the probe has excluded all prolongation methods. No four-square construction results.

For SID-A, [Hou–Zhao v3](https://arxiv.org/html/2607.01169v3) already supplies a strictly smaller asymptotic coefficient`.9434925907135450…`, before even using the stronger live repository claim. Therefore the probe’s`.9682458…`does not advance that frontier. The source uses finite kernel/boundary covering inequalities and presents a reusable exact certificate framework; this does not by itself establish equivalence with the probe’s omitted-index-difference inequality. Exact-number and omitted-difference searches did not establish that the specific inequality or formal profile is new; label their novelty UNCLEARED. The explicit`+40,N≥257`was not matched against fully numerical constants/onsets in the literature, so the entire effective statement is not asserted subsumed merely from an asymptotic coefficient comparison. The reported ceiling concerns only the displayed relaxation; existing stronger coefficients rule out reading it as a general boundary-method ceiling.

These checks concern completed outputs only. Future B probes retain fresh contexts containing the same definitions and target numbers, with no literature methods or A-output findings. No final recommendation has been made from this partial comparison.

## Timing qualification

Probe reasoning intervals above are the producers' reported clock-call intervals, not independently measured CPU time or a model-token meter. Root separately records dispatch/receipt bounds in STATUS. Writeup/archive time is not silently included in a claimed active-reasoning duration. The requested15–25minute budget is not treated as evidence of time actually spent. No dollar or token total is available.

## Adversarial HN-A / RAM-A verdict and scope repair

The ordinary reviewer reports HN-A mathematics valid, with the stress bound applying to a vertex-minimal/minimum-degree5witness, and induced neighbourhoods meaning that all geometric unit edges are included. For RAM-A, the spectral conditional theorem, recurrence countermodel and book count check. Its local-density counterexample requires FULL-neighbourhood updates and a pivot inX. It does not disprove a step allowing arbitrary further trimming ofY: for pivot in`X_i`, choose`X′=X_j∪X_k`, `Y′=Y_ij`; then`|X′|=|X|/2`and density`1/2`. The producer text is retained, but its negative conclusion is restricted accordingly.

The final ordinary adversarial verdict was PASS for HN-A's number-field, geometric, fractional, annulus and necessary-condition arguments, with injective point locations, positive total weight in weighted ratios, and the minimum-degree hypothesis retained. RAM-A's spectral criterion, recurrence countermodel and book count passed; the local counterexample passes only after the preceding restriction. This is same-vendor mathematical review, not kernel formalization or a frontier improvement.

## HN-A post-probe source comparison

[David Speyer's April25,2018 Polymath16 comments](https://dustingmixon.wordpress.com/2018/04/22/polymath16-second-thread-what-does-it-take-to-be-5-chromatic/) explicitly use the same field `Q(sqrt(-3),sqrt(-11))`, its relevant localized ring, the quotient `F4 × F4`, and projection to a four-colour palette. The discussion also corrects an initial description of the unit vectors. Thus the residue-ring colouring core is known. The inspected passage states the ring colouring, not HN-A's entire-field extension with arbitrary denominators and additive cosets; the exact novelty of that extension is UNCLEARED, not established by the absence of an exact search hit. No improvement of the plane's lower bound follows.

## Completed probe SP-A: conditional output, review pending

UTC clock interval10:27:56–10:42:54 (14m58s), writeup received before10:46:13. Target OPEN. For a positive n-point set let `s=|A+A|`, `p=|AA|`, `L=1+floor(log2 n)`, and `X_lambda={x in A:lambda*x in A}`. A dyadic class with `tau≤|X_lambda|<2tau` and m slopes has `m*tau²≥n⁴/(4pL)`. The adjacent-ray argument proves only `s²p≥n⁴/(8L)`.

The conditional advance is explicit: if at least half the slopes in such a class satisfy `E+(X_lambda)≤C*tau^(3-kappa)` for fixed `C≥1`, `0<kappa≤1`, then

`max(s,p) ≥ c(C,kappa) n^((4+kappa/2)/(3+kappa/4)) / L^((1+kappa/4)/(3+kappa/4))`.

At `kappa=1/16` this exponent is `258/193 = 135/101 + 3/19493`, with log power `65/193`. The fibre hypothesis is unproved; this is not an unconditional numerical improvement. Mixed signs and zero are handled by a positive or negated negative subset of size at least N/3 for N≥3, with small sets absorbed into constants.

Proof mechanism retained for review: for two distinct unordered ray pairs, eliminate one coordinate from a collision. Their overlap is at most `|X_c|^(1/2) E+(alpha X_a,beta X_b)^(1/2) ≤ sqrt(2C)*tau^(2-kappa/2)`, with both coefficients nonzero. Group ordered slopes into consecutive blocks of size comparable to `min(m,tau^(kappa/4))`; pairwise-intersection subtraction and disjoint slope sectors yield `s²≥c_C*m*tau²*min(m,tau^(kappa/4))`. Apply this to the good half. With `R=n²/(8pL)`, both good-slope count and tau are at least R, giving the claimed exponent when R≥1; when R<1 the large product set already suffices.

Self-tests: intervals have cubic additive energy in their ray fibres. For A={1,...,6t}, t a power of two, slopes4,5,6 are in the same size-tau=t class, and the ray-pair sums for(4,5) and(4,6) overlap in at least t²/2 points via `(x,4x)+(2z,10z)=(x+z,4x+4z)+(z,6z)`. This refutes a saving asserted for every fibre or every pair. Editorial caution: exhibiting these three slopes alone does NOT refute the more precise existence of an energy-significant class with at least half good slopes; that stronger negative statement requires its own quantifier check. The elementary aggregate bound `sum_lambda E+(X_lambda)≤n⁴` leaves the key simultaneous-small-sum-and-product regime unresolved.

POW-A and LIN-A were dispatched in fresh contexts after SP-A completed and SQ-A's mechanical archival ended. SD-A continues independently. All B probes remain pending; no ranking is final.

Post-probe comparison for SP-A: [Konyagin–Shkredov2016](https://arxiv.org/pdf/1602.03473), Lemma17, already converts control of three-fibre linear equations into an improved sumset lower bound using rich rays; its stated estimate is proportional to `tau³*|S|/sqrt(sigma)` in its parameter range. Substituting an overlap scale `sigma≈tau^(2-kappa/2)` has the same `tau^(2+kappa/4)` dependence as SP-A's packing argument. The underlying ray-cluster mechanism is therefore known. This comparison does not certify exact equivalence of all small-parameter cases or establish the missing energy hypothesis. No new unconditional exponent or novelty clearance results.

---

## Full probe output retained: SQ-A

**OPEN.** I did not prove the requested statement for every \(n\), or an eventual version. The clocked reasoning window was **10:14:09–10:31:45 UTC, 17 minutes 36 seconds**, with no deliberate waiting. I used no files, web, papers, computation tools, solvers, or other agents’ results.

I obtained an explicit finite sufficient inequality, checked several failed approaches, and hand-certified \(1\le n\le20\). None of the reductions below is claimed to be new mathematics.

1. **Exact structure and counting identity.**

Put
\[
L=n^2,\qquad R=n^2+2n,\qquad y=n+1,\qquad H=2n.
\]
The integers in the requested open interval are precisely \(L+1,\ldots,R\).

A prime square cannot occur: \(n^2<p^2<(n+1)^2\) would imply \(n<p<n+1\). Consequently every qualifying composite is a product of **distinct** primes
\[
pq,\qquad p\le n<q.
\]
Indeed, ordering \(p\le q\), the upper endpoint gives \(p<n+1\), while \(q\le n\) would give \(pq\le n^2\). This representation is unique.

Therefore, with \(\pi(t)\) counting primes at most the real number \(t\), the exact number \(N_n\) of qualifying integers is
\[
N_n=\pi(R)-\pi(L)
+\sum_{\substack{p\le n\\p\ {\rm prime}}}
 \left(\pi(R/p)-\pi(L/p)\right).
\]
The remaining difficulty is a **pointwise** positive lower bound for this expression for every \(n\).

2. **An explicit weighted sufficient inequality, with proof.**

Choose any real \(z\) with \(2\le z\le y\), and define
\[
P(z)=\prod_{p<z}p,\qquad
\rho(z)=\prod_{p<z}(1-1/p),\qquad
b(z)=\#\{p<z:p\text{ prime}\}.
\]
For primes \(z\le p<y\), put
\[
w_p=1-\frac{\log p}{\log y},\qquad
K_p=\left\lfloor\frac{\log R}{\log p}\right\rfloor.
\]
All these weights are positive.

For an integer \(m\in[L+1,R]\) coprime to \(P(z)\), set
\[
w(m)=1-\sum_{z\le p<y}v_p(m)w_p.
\]
If \(\Omega(m)\ge3\), then
\[
\sum_{z\le p<y}v_p(m)w_p
\ \ge\
\sum_{p\mid m}v_p(m)\left(1-\frac{\log p}{\log y}\right)
=\Omega(m)-\frac{\log m}{\log y}>1.
\]
The inequality holds because omitted primes satisfy \(p\ge y\) and contribute nonpositive terms. The final strict inequality uses \(m<y^2\). Thus **\(w(m)<0\) for every unwanted integer**.

A prime in the interval has weight \(1\). A surviving qualifying composite \(pq\), with \(p\le n<q\), has weight
\[
w(pq)=\frac{\log p}{\log y}\in(0,1).
\]
It follows that
\[
N_n\ge W_n(z):=
\sum_{\substack{L<m\le R\\(m,P(z))=1}}w(m).
\tag{1}
\]

Everything in \(W_n(z)\) can be expressed using primes at most \(n\) and explicit floor differences. Define
\[
M_t=\left\lfloor\frac R t\right\rfloor
    -\left\lfloor\frac L t\right\rfloor.
\]
Inclusion–exclusion gives the exact identity
\[
W_n(z)=
\sum_{d\mid P(z)}\mu(d)M_d
-\sum_{z\le p<y}w_p
 \sum_{k=1}^{K_p}\sum_{d\mid P(z)}\mu(d)M_{dp^k}.
\tag{2}
\]
Here \((d,p)=1\), as required.

Since \(|M_t-H/t|<1\), each inner inclusion–exclusion sum differs from its density main term by less than \(2^{b(z)}\). Also
\(\sum_{k=1}^{K_p}p^{-k}\le1/(p-1)\). Combining these facts with (1)–(2) proves the fully explicit inequality
\[
\boxed{
N_n\ge
H\rho(z)\left(1-\sum_{z\le p<y}\frac{w_p}{p-1}\right)
-
2^{b(z)}
\left(1+\sum_{z\le p<y}w_pK_p\right).
}
\tag{3}
\]

A positive right-hand side is therefore a rigorous certificate for that \(n\), with no asymptotic or unspecified constant.

**Exact gap:** I did not establish positivity of (3) for every \(n\), or obtain a sufficiently strong replacement for its inclusion–exclusion error. The crude error becomes prohibitive when many primes are sieved. Moreover, \(W_n(z)>0\) is sufficient, not necessary; a negative value does not supply a counterexample.

3. **A tempting truncated Möbius argument fails, including on squarefree integers.**

Consider
\[
F_n(m)=\sum_{\substack{d\mid m\\d\le n}}
\mu(d)\log\frac{n+1}{d}.
\]
For primes in the interval this equals \(\log(n+1)>0\); for a qualifying semiprime \(pq\), it equals \(\log p>0\).

It also has a useful exact first-moment estimate. Put
\[
A_n=\sum_{d\le n}\frac{\mu(d)}d\log\frac{n+1}{d}.
\]
Then
\[
\sum_{m=L+1}^{R}F_n(m)=2nA_n+E_n,\qquad |E_n|<n.
\tag{4}
\]
To prove the error bound, use \(|M_d-H/d|<1\) and
\[
\begin{aligned}
\sum_{d\le n}|\mu(d)|\log\frac{n+1}{d}
&\le n\log(n+1)-\log(n!)\\
&\le n\log(1+1/n)+n-1<n.
\end{aligned}
\]
The second inequality follows from
\(\log(n!)\ge\int_1^n\log t\,dt\).
Thus \(A_n\ge1/2\), whenever established, would imply a positive total in (4).

However, **positive \(F_n(m)\) does not certify \(\Omega(m)\le2\)**. Already \(m=8,n=2\) gives \(F_2(8)=\log2>0\), despite \(\Omega(8)=3\).

Removing nonsquarefree integers does not repair this. Take
\[
m=5\cdot7\cdot11\cdot13\cdot17=85085,\qquad n=291.
\]
Then
\[
291^2=84681<85085<85264=292^2.
\]
Every product of two of these primes is at most \(13\cdot17=221<291\), while every product of three is at least \(5\cdot7\cdot11=385>291\). Hence precisely the empty product, five single primes, and ten pair products occur in \(F_{291}\). Therefore
\[
F_{291}(85085)
=6\log292-3\log85085
=3\log\frac{85264}{85085}>0,
\]
although this integer is squarefree with \(\Omega=5\).

This is a concrete obstruction to turning the attractive first-moment estimate (4) directly into the desired theorem.

4. **Other approaches attacked and rejected.**

- **Balanced prime products.** Products
  \[
  (n+1-d)(n+1+d)=(n+1)^2-d^2
  \]
  work when both factors are prime and \(0<d^2<2n+1\). This family cannot cover every \(n\): at \(n=10\), the prime pairs summing to \(22\) give \(3\cdot19=57\), \(5\cdot17=85\), and \(11^2=121\), none in \((100,121)\). Nevertheless \(111=3\cdot37\) qualifies.
- **A prime between \(n\) and \(2n\).** Existence of such a prime does not ensure that one of its multiples in the square interval has prime cofactor. At \(n=10,p=13\), the only multiples are \(104=2^3\cdot13\) and \(117=3^2\cdot13\).
- **Direct rough-number sieve.** An integer in the interval with no prime factor below \((n+1)^{2/3}\) necessarily has \(\Omega\le2\). But I obtained no positive lower bound for this sifted set in every interval. This condition also discards many valid semiprimes.
- **Descent using the supplied \(P_3\) theorem.** Multiplying a smaller complete square interval by a prime enlarges its length too much to fit inside the target interval at the corresponding location. Conversely, finding a \(P_3\) integer in a dilated interval supplies no divisibility by the chosen prime. I found no valid descent.

5. **Finite range actually covered by hand.**

The following witnesses certify every \(1\le n\le20\), in order:
\[
\begin{array}{c|rrrrrrrrrr}
n&1&2&3&4&5&6&7&8&9&10\\ \hline
a&2&6&10&21&26&39&51&65&85&111\\
\text{factorization}&2&2\cdot3&2\cdot5&3\cdot7&2\cdot13&
3\cdot13&3\cdot17&5\cdot13&5\cdot17&3\cdot37
\end{array}
\]
\[
\begin{array}{c|rrrrrrrrrr}
n&11&12&13&14&15&16&17&18&19&20\\ \hline
a&123&145&177&201&226&259&291&327&365&403\\
\text{factorization}&3\cdot41&5\cdot29&3\cdot59&3\cdot67&
2\cdot113&7\cdot37&3\cdot97&3\cdot109&5\cdot73&13\cdot31
\end{array}
\]
All inequalities are strict. All listed factors are prime; trial division by primes at most \(7\), where relevant, suffices because the largest is \(113<11^2\). This is only a small finite certificate.

The unresolved requirement remains a rigorous positive lower bound for qualifying integers **in each individual square interval**, with every exceptional or initial case covered. No such bound was established here.

---


---

## Full probe output retained: SD-A

**OPEN. Neither requested universal constant was improved.**

Tracked active reasoning: **10:34:25–10:49:32 UTC, 15m07s**. I used no files, web, papers, solvers, computation tools, or additional agents; only the clock and a progress message to the parent.

The substantive result is an exact conditional-copy entropy identity recovering the four-form \(7/4\) bound, with a complete decomposition of its deficit. It also proves pointwise strictness for every nonconstant finite distribution, but **does not provide a uniformly smaller constant**. Two tempting stronger inequalities were refuted.

### 1. Exact four-form identity

Write
\[
S=X+Y,\qquad T=X+2Y,\qquad D=X-Y,
\]
and abbreviate \(h=H(X,Y)\), \(H_X=H(X)\), etc.

Construct an actual coupling as follows.

1. Let \(V=(A,B,C)\), where \(A\) has the law of \(X\), and, conditional on \(A\), \(B,C\) are independent with the conditional law of \(Y\mid X=A\).
2. Put \(F=(A+B,A+C)\).
3. Let \(V'=(A',B',C')\) be a conditionally independent copy of \(V\) given \(F\).

Consequently,
\[
A+B=A'+B',\qquad A+C=A'+C'.
\]
Every pair \((A,B),(A,C),(A',B'),(A',C')\) has the original joint law of \((X,Y)\).

Define
\[
Q=(V,V'),\quad Z=(C,B',A'+2C'),\quad W=(A,B),\quad D_0=A-B.
\]
Set
\[
\begin{aligned}
R&=H(X,Y\mid D),\\
J&=I(A+B;A+C),\\
K&=H(C)+H(B')+H(A'+2C')-H(Z),\\
L&=I(W;Z\mid D_0).
\end{aligned}
\]
All four quantities are nonnegative. Then the following is an **exact identity**:
\[
\boxed{
4H_D+3R+J+K+L
=2H_X+2H_Y+2H_S+H_T.
}
\tag{1}
\]

**Proof.** Conditional independence gives
\[
H(V)=2h-H_X,\qquad H(F)=2H_S-J,
\]
hence
\[
H(Q)=2H(V)-H(F)=4h-2H_X-2H_S+J.
\tag{2}
\]

The two matching-sum constraints imply
\[
A'=A+B-B',\qquad C'=C-B+B',
\]
so
\[
A'+2C'=A-B+2C+B'.
\]
Therefore
\[
D_0=Z_3-2Z_1-Z_2
\]
is determined by \(Z\).

Moreover, \(Q\) and \((Z,W)\) determine each other: from \(Z,W\), recover \(C,B'\), then use the displayed formulas for \(A',C'\). Thus
\[
\begin{aligned}
H(Q)
&=H(Z)+H(W\mid Z)\\
&=2H_Y+H_T-K+H(W\mid D_0)-I(W;Z\mid D_0)\\
&=2H_Y+H_T-K+h-H_D-L.
\end{aligned}
\tag{3}
\]
Equating (2) and (3), and using \(h=H_D+R\), proves (1). No uncoupled independence identity is used.

In particular,
\[
H_D+3H(X,Y)\le 2H_X+2H_Y+2H_S+H_T,
\]
and
\[
4H_D\le 2H_X+2H_Y+2H_S+H_T.
\tag{4}
\]
Equation (4) recovers the supplied \(7/4\) constant.

### 2. Pointwise strictness, and why it is insufficient

Let
\[
M=\max(H_X,H_Y,H_S,H_T).
\]
If \(M>0\), then
\[
\boxed{H_D<\tfrac74 M.}
\tag{5}
\]

**Proof.** Suppose equality held. In (1), the right side is at most \(7M\), while \(4H_D=7M\). Hence
\[
H_X=H_Y=H_S=H_T=M,\qquad R=J=K=L=0.
\]
In particular \(h=H_D=7M/4\).

But \(J=0\) forces \(S\) independent of \(X\). To see this directly, let
\[
p_s(a)=\Pr(A+B=s\mid A=a).
\]
Because \(A+B,A+C\) are conditionally iid given \(A\), their independence gives
\[
\mathbb E[p_s(A)^2]=\mathbb E[p_s(A)]^2.
\]
Thus \(p_s(A)\) is constant almost surely for every \(s\), proving \(S\perp X\). Consequently
\[
h=H(X,S)=H_X+H_S=2M,
\]
contradicting \(h=7M/4\).

This is **not** the requested improvement: strictness separately for every distribution does not bound the supremum away from \(7/4\).

More precisely, (1) gives the exact deficit decomposition
\[
\boxed{
\begin{aligned}
7M-4H_D={}&2(M-H_X)+2(M-H_Y)+2(M-H_S)+(M-H_T)\\
&+3R+J+K+L.
\end{aligned}}
\tag{6}
\]
The remaining gap is a distribution-independent positive lower bound on the right side divided by \(M\). I did not prove one.

### 3. A uniform conditional-copy stability shortcut fails

One cannot infer a substantial \(J\) solely from substantial \(I(X;S)\), even when \(H(X)=H(S)\) and \(H(X,S)=7H(X)/4\).

Here is an exact finite-channel example. It is **not a counterexample to either target**, because it does not control the required ordinary-real additive forms.

Let \(q\) be a prime power. Let
\[
U=(U_0,U_1,U_2,U_3)
\]
be uniform on \(\mathbb F_q^4\). Independently choose \(I=(i_1,i_2,i_3)\) uniformly on \(\mathbb F_q^3\), and set
\[
V=(I,U_0+i_1U_1+i_2U_2+i_3U_3).
\]
Then
\[
H(U)=H(V)=4\log q,\quad H(U,V)=7\log q,\quad I(U;V)=\log q.
\]

For conditionally independent copies \(V_1,V_2\) given \(U\),
\[
I(V_1;V_2)=q^{-3}\log q.
\]
Indeed, the indices are independent. Given distinct indices, the two displayed linear functionals are independent uniform field elements; given equal indices, they are identical uniform elements. Thus
\[
H(V_1,V_2)=6\log q+(2-q^{-3})\log q.
\]

Therefore \(J/H(U)\to0\), while \(I(U;V)/H(U)=1/4\). A quantitative improvement from (6) must use the additional real-additive restrictions, especially the bounds on \(Y\) and \(T\); generic conditional-copy stability alone does not supply it.

### 4. Two proposed stronger entropy inequalities are false

I tested stronger linear inequalities that would have improved the three-form constant. Both failed.

**First false candidate**
\[
H_D+3h\le 2H_X+2H_Y+3H_S.
\tag{7}
\]
Since \(h\ge H_D\), this would imply the three-form constant \(7/4\).

Take binary \(X,Y\) with
\[
P(0,0)=P(1,1)=\varepsilon/2,\qquad
P(0,1)=P(1,0)=(1-\varepsilon)/2.
\]
Write \(\ell=\log2\), and let \(b(\varepsilon)\) be binary entropy. Direct calculation gives
\[
\begin{aligned}
H_X=H_Y&=\ell,\\
h&=\ell+b(\varepsilon),\\
H_S&=b(\varepsilon)+\varepsilon\ell,\\
H_D&=b(\varepsilon)+(1-\varepsilon)\ell.
\end{aligned}
\]
The right side of (7) minus its left side is
\[
4\varepsilon\ell-b(\varepsilon).
\]
For \(\varepsilon=1/16\),
\[
b(1/16)>\tfrac1{16}\log16=\tfrac14\ell,
\]
so (7) fails. This is an explicit rational-probability, four-point counterexample.

**Second false candidate**
\[
H_D+4h\le 3(H_X+H_Y+H_S).
\tag{8}
\]
This would imply the improved three-form constant \(9/5\).

Here is an explicit finite-support family violating (8) for all sufficiently large integers \(n\). Let
\[
A\sim\operatorname{Bin}(n,\tfrac12),\quad
B\sim\operatorname{Bin}(5n,\tfrac12),\quad
E\sim\operatorname{Bern}(\tfrac12)
\]
be independent, and set
\[
X=A+B,\qquad Y=A-B+E.
\]
Denote \(b_m=H(\operatorname{Bin}(m,\tfrac12))\). Then
\[
\begin{aligned}
H_X&=b_{6n},&
H_Y&=b_{6n+1},\\
H_S&=b_n+\ell,&
H_D&=b_{5n}+\ell,\\
h&=b_n+b_{5n}+\ell.
\end{aligned}
\]
The last three assertions follow from the injective encodings \(2A+E\), \(2B-E\), and the fact that \((X,Y)\) determines \(E\) by parity, then \(A,B\).

Hence the right side of (8) minus its left side equals
\[
F_n=3b_{6n}+3b_{6n+1}-b_n-5b_{5n}-2\ell.
\]
Using
\[
b_m=\tfrac12\log(\pi e m/2)+o(1),
\]
we obtain
\[
F_n\longrightarrow
3\log6-\tfrac52\log5-2\log2
=\log\!\left(\frac{54}{25\sqrt5}\right)<0,
\]
because \(54^2=2916<3125=(25\sqrt5)^2\).

For completeness, that entropy asymptotic follows directly from Stirling and concentration. For \(K\sim\operatorname{Bin}(m,1/2)\), uniformly on
\[
|K-m/2|\le m^{3/5},
\]
Stirling and Taylor expansion give
\[
-\log P(K)
=\tfrac12\log(\pi m/2)+\frac{2(K-m/2)^2}{m}+o(1).
\]
The complementary probability is at most \(2e^{-2m^{1/5}}\), by the exponential-moment bound \(\cosh(t/2)^m\le e^{mt^2/8}\). Since \(-\log P(K)\le m\log2\), tails contribute \(o(1)\). Taking expectations and using \(\operatorname{Var}(K)=m/4\) proves the asymptotic.

I did **not** determine or claim a checked finite threshold \(n\). The negative limit rigorously establishes finite counterexamples throughout a terminal portion of this explicitly defined family.

### 5. Exact lower bound for the three-form target

Let \((X,Y)\) be uniform on
\[
\{(0,0),(1,0),(0,1)\}.
\]
Then \(D\) has three distinct equiprobable values, while each of \(X,Y,S\) has binary entropy \(b(1/3)\). Thus every valid three-form constant satisfies
\[
\boxed{
c\ge
\frac{\log3}{b(1/3)}
=
\frac{\log3}{\log3-\frac23\log2}
\approx1.726.
}
\]
This example does not give the same obstruction for the four-form target: \(T\) already has three distinct equiprobable values.

### 6. Reduction to difference-injective finite sets

I also verified that the universal entropy exponent is exactly equivalent to the corresponding cardinality exponent for finite real point sets whose difference projection is injective.

Let the controlled forms be either \((X,Y,S)\) or \((X,Y,S,T)\).

* An entropy inequality with constant \(c\), applied to the uniform distribution on a difference-injective finite set \(G\), gives
  \[
  |G|\le \bigl(\max_i|\pi_i(G)|\bigr)^c.
  \]

* Conversely, suppose this cardinality inequality holds for every such finite real \(G\). For an arbitrary finite joint distribution, take \(n\) independent copies and retain tuples on which all controlled forms and \(D\) have self-information within \(n\varepsilon\) of their respective entropies. This event \(E_n\) has probability tending to one.

  Each controlled projection then takes at most
  \[
  \exp(n(H_i+\varepsilon))
  \]
  values. Since each retained difference string has probability at most
  \[
  \exp(-n(H_D-\varepsilon)),
  \]
  at least
  \[
  P(E_n)\exp(n(H_D-\varepsilon))
  \]
  distinct difference strings occur. Select one joint tuple for each such string.

  To put this finite vector configuration back in \(\mathbb R^2\), choose a linear functional \(\lambda:\mathbb R^n\to\mathbb R\) injective on every relevant finite projection set. Such a choice exists outside finitely many proper hyperplanes. The map
  \[
  (x^n,y^n)\mapsto(\lambda(x^n),\lambda(y^n))
  \]
  commutes with all specified linear forms and preserves the needed cardinalities and difference injectivity.

  Applying the cardinality inequality, dividing logarithms by \(n\), and letting \(n\to\infty\), then \(\varepsilon\to0\), gives
  \[
  H_D\le c\max_i H_i.
  \]

Thus neither arbitrary dependence nor nonuniform probabilities can simply be discarded, but both can be handled by a rigorous reduction. This reduction itself gives no improved exponent.

**Final status:** both requested improvements remain **OPEN in this probe**. The strongest established output is identity (1), its exact deficit formula (6), and pointwise strictness without a uniform improvement.

---

---

## Full probe output retained: SP-A

**OPEN.** I did not prove an unconditional improvement over \(135/101\). I obtained a self-contained conditional improvement to
\[
\frac{258}{193}
=\frac{135}{101}+\frac{3}{19493},
\]
and isolated the missing estimate. The condition concerns additive energies of rich multiplicative fibers; it is not established and is false without an additional hypothesis.

Measured UTC interval: **2026-10-02 10:27:56–10:42:54**, approximately 15 minutes of active reasoning. I used no files, sources, computation, other outputs, or agents; only the clock.

1. **Reduction from arbitrary real sets to positive sets**

Let \(A\subset\mathbb R\) be finite, \(|A|=N\ge3\). At least one of its strictly positive and strictly negative parts has cardinality at least
\[
(N-1)/2\ge N/3.
\]
Take this part, negating it if necessary, to obtain \(B\subset\mathbb R_{>0}\), \(|B|\ge N/3\). Then
\[
|B+B|\le |A+A|,\qquad |BB|\le |AA|.
\]
Thus a universal positive-set lower bound with any fixed exponent transfers to all real sets by changing its constant. Sets of size one or two can be absorbed into that constant. This handles zero and mixed signs without changing the exponent.

Henceforth \(A\subset\mathbb R_{>0}\), with
\[
n=|A|,\quad s=|A+A|,\quad p=|AA|,
\quad L=1+\lfloor\log_2 n\rfloor .
\]

2. **Elementary energy reduction and the \(4/3\) bound**

For \(\lambda\in A/A\), define
\[
X_\lambda=\{x\in A:\lambda x\in A\},\qquad
P_\lambda=\{(x,\lambda x):x\in X_\lambda\}.
\]
Write \(r_\lambda=|X_\lambda|\). Multiplicative energy satisfies
\[
E^\times(A)=\sum_\lambda r_\lambda^2
=\#\{(a,b,c,d)\in A^4:ab=cd\}
\ge \frac{n^4}{p}.
\]
The equality follows by rewriting a product equality as a ratio equality; the inequality is Cauchy–Schwarz applied to the \(n^2\) ordered products.

Also,
\[
\sum_\lambda r_\lambda=n^2.
\]

Some dyadic class
\[
\Lambda=\{\lambda:\tau\le r_\lambda<2\tau\},
\qquad \tau=2^j,\qquad m=|\Lambda|,
\]
satisfies
\[
m\tau^2\ge \frac{n^4}{4pL}. \tag{1}
\]
Consequently,
\[
\tau\ge \frac{n^2}{4pL},
\qquad
m\ge \frac{n^2}{4pL}. \tag{2}
\]
Indeed, \(m\tau\le n^2\) gives the first assertion, while \(\tau\le n\) gives the second.

Order the slopes in \(\Lambda\). For two distinct slopes, vector addition
\[
P_\lambda\times P_\mu\longrightarrow P_\lambda+P_\mu
\]
is injective because the two direction vectors are linearly independent. Thus each adjacent pair supplies at least \(\tau^2\) points of \((A+A)^2\). Positivity puts their slopes strictly between the two input slopes, so the sectors from adjacent pairs are disjoint. Therefore
\[
(m-1)\tau^2\le s^2.
\]
When \(m=1\), \(\tau^2\le n^2\le s^2\). Hence \(m\tau^2\le2s^2\) always. Together with (1),
\[
s^2p\ge \frac{n^4}{8L}. \tag{3}
\]
This only gives \(4/3\), below \(135/101\).

3. **An overlap lemma with a full proof**

For a finite real set \(X\), let
\[
E^+(X)=\#\{(x_1,x_2,x_3,x_4)\in X^4:
x_1+x_2=x_3+x_4\}.
\]

Suppose distinct positive slopes \(\lambda_1,\ldots,\lambda_m\) have fibers \(X_i\) satisfying
\[
\tau\le |X_i|<2\tau,
\qquad E^+(X_i)\le C\tau^{3-\kappa}, \tag{4}
\]
where \(C\ge1\) and \(0<\kappa\le1\). Put
\[
Q_{ij}=P_{\lambda_i}+P_{\lambda_j}\quad(i<j).
\]
For any two different unordered index pairs,
\[
|Q_{ab}\cap Q_{cd}|
\le \sqrt{2C}\,\tau^{2-\kappa/2}. \tag{5}
\]

To prove this, relabel \(c,d\) so that \(d\notin\{a,b\}\), which is possible because the index pairs differ. A collision satisfies
\[
u+v=w+z,\qquad
\lambda_a u+\lambda_b v=\lambda_c w+\lambda_d z.
\]
Eliminating \(z\),
\[
w=\alpha u+\beta v,
\quad
\alpha=\frac{\lambda_a-\lambda_d}{\lambda_c-\lambda_d},
\quad
\beta=\frac{\lambda_b-\lambda_d}{\lambda_c-\lambda_d}.
\]
Both coefficients are nonzero. A point in either \(Q\) has a unique representation using its two rays, so the overlap is at most
\[
\#\{(u,v,w)\in X_a\times X_b\times X_c:
\alpha u+\beta v=w\}.
\]
Cauchy–Schwarz bounds this by
\[
|X_c|^{1/2}E^+(\alpha X_a,\beta X_b)^{1/2}.
\]
Here the mixed energy counts equal sums from the two indicated sets. Expressing it through differences and applying Cauchy–Schwarz again gives
\[
E^+(\alpha X_a,\beta X_b)
\le \sqrt{E^+(X_a)E^+(X_b)}.
\]
Scaling by a nonzero real number preserves additive energy. Substitution of (4) now proves (5).

4. **Packing blocks of rays**

Under (4), there is a constant \(c_C>0\) such that
\[
s^2\ge c_C\,m\tau^2
       \min\{m,\tau^{\kappa/4}\}. \tag{6}
\]

Here is the packing argument, including the small-block issue. Write
\[
T=\tau^{\kappa/4},\qquad B=\sqrt{2C}.
\]
Choose a sufficiently small positive constant \(a=a(C)\). If \(aT\ge2\), partition the ordered slopes into complete consecutive blocks of size
\[
k=\min\{m,\lfloor aT\rfloor\},
\]
handling \(m=1\) separately.

Inside a block there are \(q=\binom{k}{2}\) sets \(Q_{ij}\), each of cardinality at least \(\tau^2\). By the elementary union bound with pairwise intersections and (5),
\[
\left|\bigcup Q_{ij}\right|
\ge q\tau^2-\binom q2 B\tau^{2-\kappa/2}.
\]
Since \(k\le aT\), choosing \(a\) small makes the second term at most half the first. Thus a block contributes at least \(k^2\tau^2/8\) points.

All these points lie strictly between the smallest and largest slopes of their block. Different complete blocks consequently contribute disjoint sets. There are at least \(m/(2k)\) complete blocks, so
\[
s^2\ge \frac{mk\tau^2}{16}.
\]
Moreover, \(k\) is bounded below by a constant times \(\min(m,T)\).

If \(aT<2\), then \(T\) is bounded in terms of \(C\), and the adjacent-ray argument proves (6) after reducing its constant. For \(m=1\), use \(s^2\ge\tau^2\). This completes the proof.

5. **Conditional exponent \(258/193\)**

Assume the energy-significant dyadic class in (1) has at least half its slopes satisfying (4). Then
\[
\max(s,p)\ge
c_{C,\kappa}\,
\frac{n^{(4+\kappa/2)/(3+\kappa/4)}}
     {L^{(1+\kappa/4)/(3+\kappa/4)}}. \tag{7}
\]

Indeed, let \(m_g\ge m/2\) be the number of these slopes and set
\[
R=\frac{n^2}{8pL}.
\]
Then
\[
m_g\tau^2\ge n^2R.
\]
Since \(m_g\tau\le n^2\) and \(\tau\le n\), both \(m_g\ge R\) and \(\tau\ge R\).

If \(R\ge1\), (6) gives
\[
s^2\ge c\,n^2R^{1+\kappa/4},
\]
because \(0<\kappa/4\le1\). Therefore
\[
s^2p^{1+\kappa/4}
\ge c\,\frac{n^{4+\kappa/2}}{L^{1+\kappa/4}},
\]
which implies (7).

If \(R<1\), then \(p>n^2/(8L)\), which already implies (7): writing its two exponents as \(\beta,\gamma\), one has
\[
\frac{n^2/L}{n^\beta/L^\gamma}
=(n/L)^{2/(3+\kappa/4)}\ge1.
\]

In particular, take \(\kappa=1/16\). The sufficient fiber hypothesis is
\[
E^+(X_\lambda)\le C\tau^{47/16}
\quad\text{for at least half the slopes in an energy-significant class}. \tag{8}
\]
It yields
\[
\max(s,p)\ge c_C\,\frac{n^{258/193}}{L^{65/193}}. \tag{9}
\]
The logarithm can be absorbed into \(n^\varepsilon\). Thus **if (8) were available universally in the required regime**, the requested statement would follow with
\[
\delta=\frac{3}{19493}.
\]
I have not established that hypothesis.

6. **Self-refutations and the precise remaining obstruction**

A uniform multiplicative-energy saving such as
\[
E^\times(A)\ll s^2n^{-\eta}\qquad(\eta>0)
\]
is false. For \(A=\{1,\ldots,n\}\), the diagonal quotient fiber already gives \(E^\times(A)\ge n^2\), whereas \(s=2n-1\).

The fiber condition (8), and a corresponding unconditional overlap saving, are also false in general. This failure occurs even for three slopes in the same dyadic class.

Take \(A=\{1,\ldots,6t\}\), where \(t\ge2\) is a power of two. The fibers for slopes \(4,5,6\) have sizes
\[
3t/2,\quad \lfloor6t/5\rfloor,\quad t,
\]
all in \([t,2t)\). Their coordinate sets are intervals. For an interval \(I_q=\{1,\ldots,q\}\),
\[
E^+(I_q)
=q^2+2\sum_{j=1}^{q-1}j^2
=\frac{2q^3+q}{3}.
\]
Consequently these fibers have cubic additive energy, violating (8) for every fixed \(C\) as \(t\to\infty\).

There are also at least \(t^2/2\) overlaps between \(Q_{4,5}\) and \(Q_{4,6}\). For
\[
1\le x\le t,\qquad 1\le z\le t/2,
\]
the equality
\[
(x,4x)+(2z,10z)
=(x+z,4x+4z)+(z,6z)
\]
uses legitimate points from the indicated rays. Different \((x,z)\) give different sum points, since
\[
(x,z)\mapsto(x+2z,4x+10z)
\]
has nonzero determinant. Thus no universal bound \(O(\tau^{2-\eta})\) for these overlaps can hold.

Finally, the elementary aggregate estimate I could prove is only
\[
\sum_{\lambda\in A/A}E^+(X_\lambda)\le n^4. \tag{10}
\]
To see this, first choose an additive quadruple \((a,b,c,d)\in A^4\). There are at most \(n^3\) such quadruples, since three entries determine the fourth. For each quadruple, at most \(n\) positive numbers \(\lambda\) can put all four entries in \(X_\lambda\), because \(\lambda a\in A\) determines \(\lambda\) from one of \(n\) possibilities. This proves (10).

Estimate (10) is too weak. Near the proposed exponent, the bad-fiber alternative only forces an aggregate of approximately \(n^{3.285}\), up to logarithms, entirely compatible with \(n^4\).

The remaining gap is therefore concrete: **one must control the numerous high-additive-energy multiplicative fibers, or directly obtain sufficient averaged savings in the ray-pair overlaps, using the simultaneous smallness of \(s\) and \(p\).** None of the proved inequalities above supplies that control. The unconditional target remains **OPEN**.

---

## SD-A assessment and post-probe comparison

Both upper targets remain OPEN. The exact identity is `4H(D)+3H(X,Y|D)+J+K+L=2H(X)+2H(Y)+2H(X+Y)+H(X+2Y)`, with all deficit terms nonnegative and their actual coupling specified in the full output. For each nonconstant finite distribution the7/4 bound is strict, but no normalized uniform gap was proved. The finite-channel counterexample defeats a generic conditional-copy stability shortcut only; it is not an additive real counterexample to the target. The two proposed stronger linear inequalities are refuted, one by four rational-probability atoms and one by an explicit binomial family with a rigorous negative asymptotic limit but no checked finite threshold. The lower bound near1.726 is weaker than the current lower record and does not move a frontier.

[Katz–Tao, Section4](https://arxiv.org/pdf/math/9906097) already gives the7/4 cardinality bound by a two-copy configuration and injectivity. The numerical upper bound recovered by SD-A is known. [Lau–Nair](https://chandra.ie.cuhk.edu.hk/pub/papers/HC/InfInqAddComb.pdf), Lemma1 and Theorem2, explicitly develops conditional-copy entropy identities and cites the Ruzsa cardinality/entropy equivalence. SD-A independently re-derived this established framework. Exact novelty of its particular deficit decomposition, pointwise strictness proof and failed-shortcut counterexamples remains UNCLEARED; no source comparison here establishes new progress toward a uniform smaller constant.

As of 2026-10-02T10:56:30.158Z, seven of18fresh probes are complete. SQ-A, SD-A and SP-A full originals have been retained; ordinary reviewer `/root/ref_e1_b` now audits all three. POW-A and LIN-A are still producing; all B attempts remain outstanding.

---

## Full probe output retained: POW-A

**OPEN.** I did not prove any universal exponent \(2\le k\le85\).

UTC start: **10:46:42**. End: **11:01:41**, approximately **15 minutes of active reasoning**. I used only clock calls; no files, browsing, computations/solvers, other agents’ outputs, or subagents.

I obtained the following rigorous reductions and finite coverage. The two quoted analytic theorems below are recalled from memory, not source-checked during this probe.

**1. An explicit finite range for \(k=85\).**

The standard Dusart bound I recall is:

> For every real \(x\ge396738\), there is a prime \(p\) such that
> \[
> x<p\le x\left(1+\frac1{25(\log x)^2}\right).
> \]

I am confident about this statement, but its exact threshold and coefficient should be source-checked before publication. Using it as stated gives
\[
\boxed{\text{For every integer }1\le n\le7\,980\,000\,000,\quad
n^{85}<p<(n+1)^{85}\text{ for some prime }p.}
\]

Here is the complete numerical argument, requiring no individual prime checks.

Put
\[
C=25\cdot85^3=15\,353\,125,\qquad N=7\,980\,000\,000.
\]
I first show
\[
n<C(\log n)^2\qquad(2\le n\le N).
\]

For \(2\le n\le7\), use \(\log2>2/3\):
\[
\frac n{(\log n)^2}<\frac{63}{4}<C.
\]
For \(n\ge8\), the function \(t/(\log t)^2\) is increasing, since its derivative is
\[
\frac{\log t-2}{(\log t)^3}>0.
\]
Thus it suffices to check \(N\).

The elementary logarithm series
\[
\log\frac{1+z}{1-z}
=2\sum_{j\ge0}\frac{z^{2j+1}}{2j+1}
\]
gives, by retaining five terms at \(z=1/3\) and three at \(z=1/9\),
\[
\log2>0.693146,\qquad \log(5/4)>0.223143,
\]
and hence \(\log10>2.30258\). Also
\(\log(1-u)>-u/(1-u)\) for \(0<u<1\). Therefore
\[
\begin{aligned}
\log N
&=3\log2+9\log10+\log(399/400)\\
&>3(0.69314)+9(2.30258)-1/399\\
&>22.8.
\end{aligned}
\]
Consequently,
\[
C(\log N)^2>C(22.8)^2
=7\,981\,168\,500>N.
\]
This proves the required inequality throughout the stated range.

Now \(x=n^{85}\ge2^{85}>396738\), so Dusart supplies
\[
\begin{aligned}
n^{85}<p
&\le n^{85}\left(1+\frac1{25\cdot85^2(\log n)^2}\right)\\
&<n^{85}\left(1+\frac{85}{n}\right)\\
&=n^{85}+85n^{84}\\
&<(n+1)^{85}.
\end{aligned}
\]
The last inequality follows from the remaining positive binomial terms. For \(n=1\), use \(p=2\).

This is analytic finite coverage, not a new universal exponent.

**2. A precise connection between an eventual interval theorem and the remaining range.**

Suppose an unconditional theorem gives, for every real \(x\ge X_0\), a prime in
\[
[x-x^\theta,x],\qquad \theta\le1-\frac1k,\quad k\ge2.
\]
Then the desired open interval statement holds for every integer \(n\ge1\) satisfying
\[
(n+1)^k\ge X_0.
\]

Indeed,
\[
\begin{aligned}
(n+1)^k-n^k-(n+1)^{k-1}
&=n\big((n+1)^{k-1}-n^{k-1}\big)>0.
\end{aligned}
\]
With \(x=(n+1)^k\), this gives
\[
x-n^k>x^{1-1/k}\ge x^\theta.
\]
Thus the prime supplied lies strictly above \(n^k\). It lies strictly below \(x\), because \(x=(n+1)^k\) is composite.

The standard Baker–Harman–Pintz statement I recall gives the above interval for \(\theta=21/40=0.525\) and all sufficiently large \(x\). It therefore supplies eventual coverage for every \(k\ge3\). It supplies **no numerical bridge here**, because I have not established a usable explicit \(X_0\).

Combining the preceding finite result with this lemma would prove universal \(k=85\) if one could justify
\[
X_0\le (N+2)^{85}.
\]
Otherwise the exact unresolved portion is
\[
\boxed{n>N\quad\text{and}\quad(n+1)^{85}<X_0.}
\]
An unspecified onset cannot certify this portion.

**3. Why the given universal \(86\) statement does not directly transfer.**

For \(r=85/86<1\), concavity gives
\[
(n+1)^r-n^r<1\qquad(n\ge1).
\]
Consequently, no interval
\[
(m^{86},(m+1)^{86})
\]
can be contained in
\[
(n^{85},(n+1)^{85}).
\]
Containment would require
\[
m\ge n^r,\qquad m+1\le(n+1)^r,
\]
contradicting the displayed length bound. Thus direct interval containment fails for every \(n\).

A stronger diagnostic makes the missing information explicit. Fix any integer \(n\ge170\), write \(a=n^{85}\), \(b=(n+1)^{85}\), and consider the artificial set
\[
S=\{2,3,4,\ldots\}\setminus(a,b).
\]
This is **not a set of primes and not a counterexample to the target**. Nevertheless:

- \(S\) meets every consecutive \(K\)-th-power interval for every \(K\ge86\). The same concavity argument rules out containment in the deleted interval; integer endpoints then provide a surviving integer.
- \(S\) satisfies the integer version of Bertrand’s interval property. Indeed,
  \[
  b/a=(1+1/n)^{85}<e^{85/n}\le e^{1/2}<2.
  \]
  If every integer \(m+1,\ldots,2m-1\) lay in the deleted interval, integrality would imply \(a\le m\) and \(b\ge2m\), contradicting \(b<2a\).
- Beyond \(b\), \(S\) contains every integer, so it satisfies arbitrarily strong eventual short-interval existence statements.
- It has no element in the selected \(85\)-th-power interval.

The example explains why combining only the stated \(86\) property, Bertrand, and a qualitative eventual theorem leaves a genuine logical gap. Quantitative information linking the ranges is essential.

**4. An exact prime-gap reformulation.**

For a fixed \(k\ge2\), the universal target is equivalent to
\[
\left\lfloor p_{j+1}^{1/k}\right\rfloor
-\left\lfloor p_j^{1/k}\right\rfloor\le1
\]
for every pair of consecutive primes \(p_j<p_{j+1}\).

A prime is never a perfect \(k\)-th power, so it lies in the desired interval indexed by precisely \(\lfloor p^{1/k}\rfloor\). These indices start at \(1\), increase without bound, and hit every positive integer exactly when they never jump by \(2\) or more. The given \(86\) result controls these jumps for \(86\)-th roots; it does not control them for \(85\)-th roots.

I also tested binomial-product/Sylvester arguments, induction from a hypothetical least counterexample, and interpolation of the \(86\)-th-power grid. None supplied the missing local prime information. In particular, a large prime factor of an integer in the target interval need not itself lie in that interval.

**Remaining gap:** establish an explicit short-interval theorem covering the range after the finite bound above, or find a different argument proving prime existence there. The universal target remains **OPEN** in this probe.

---

---

## Full probe output retained: LIN-A

**OPEN.** I did not prove any unconditional exponent \(L<3.99\).

Recorded UTC start: **2026-10-02 10:47:06**. Recorded end of active reasoning: **11:02:17** — **15 minutes 11 seconds**. I used no files, web, papers, computations, solvers, or other agents’ results.

The proved progress is an elementary, uniform prime-power removal lemma with an effective coefficient, followed by a precise smooth explicit-formula reduction. The unresolved part is controlling the zeros uniformly, particularly the contribution remaining after a possible exceptional real zero. No novelty or priority claim is intended.

### 1. Elementary prime-power lemma

For \(q\ge2\), \((a,q)=1\), and \(Y>1\), define
\[
T(q,a;Y)=
 \sum_{\substack{p\ {\rm prime},\ k\ge2\\p^k\ge Y\\p^k\equiv a\pmod q}}
 \frac{\log p}{p^k}.
\]

**Lemma.** For every fixed real \(u>1\),
\[
\frac{\varphi(q)}{\log q}\,T(q,a;q^u)
 \ll_u q^{-\eta},
\qquad
\eta=\min\!\left(\frac{u-1}{2},\frac12\right),
\]
uniformly over all integers \(q\) and all coprime residues \(a\).

Here is one fully effective version. Put
\[
\epsilon=\frac{u-1}{2},\qquad
K=\left\lceil\frac{2u}{u-1}\right\rceil,\qquad
M=\left\lceil K^{1/\epsilon}\right\rceil.
\]
For every integer \(q\ge 2^{K/u}\),
\[
\boxed{\quad
\frac{\varphi(q)}{\log q}T(q,a;q^u)
 \le
4(u+2)(K^{M+1}+1)\,q^{-\eta}.
\quad}
\]
The coefficient is deliberately crude.

**Proof.** For fixed \(k\), let \(R_k(a,q)\) be the number of unit roots of
\(b^k\equiv a\pmod q\). The cyclic structure of the units modulo odd prime powers, and
\[
(\mathbb Z/2^e\mathbb Z)^\times\simeq C_2\times C_{2^{e-2}}
\quad(e\ge3),
\]
give
\[
R_k(a,q)\le 2k^{\omega(q)}.
\]
For \(2\le k<K\), split the prime divisors of \(q\) at \(K^{1/\epsilon}\). There are at most \(M\) smaller prime divisors; each larger prime divisor \(r\) satisfies \(K\le r^\epsilon\). Consequently
\[
R_k(a,q)\le 2K^M q^\epsilon.
\]

If \(Z\ge2\), the function \(g(t)=\log t/t^k\) is decreasing, so for each residue \(b\pmod q\),
\[
\sum_{\substack{m\ge Z\\m\equiv b\pmod q}}\frac{\log m}{m^k}
\le
\frac{\log Z}{Z^k}
+\frac1q\int_Z^\infty\frac{\log t}{t^k}\,dt.
\]
The integral equals
\[
Z^{1-k}\left(\frac{\log Z}{k-1}+\frac1{(k-1)^2}\right).
\]
Taking \(Z=Y^{1/k}\), replacing primes by integers, and summing the unit roots proves, for \(Y\ge2^K\),
\[
\sum_{2\le k<K}
\sum_{\substack{p^k\ge Y\\p^k\equiv a\pmod q}}
\frac{\log p}{p^k}
\le
2K^{M+1}q^\epsilon(\log Y+1)
\left(Y^{-1}+q^{-1}Y^{-1/2}\right). \tag{1}
\]

For \(k\ge K\), discard the congruence condition. Put \(Z=Y^{1/K}\). For each prime \(p\le Z\), start the geometric series at the first exponent \(k\ge K\) satisfying \(p^k\ge Y\). Its contribution is at most \(2\log p/Y\). Summing these primes gives at most
\[
2Y^{-1}Z\log Z.
\]
For \(p>Z\), summing all exponents \(k\ge K\) gives at most \(2\log p/p^K\). Replacing primes by integers and using the preceding integral estimate proves
\[
\sum_{\substack{p,\ k\ge K\\p^k\ge Y}}\frac{\log p}{p^k}
\le4(\log Y+1)Y^{-1+1/K}. \tag{2}
\]
The constant \(4\) is sufficient for \(K\ge3\), \(Z\ge2\).

Combine (1) and (2), put \(Y=q^u\), and use \(\varphi(q)\le q\). The resulting three powers of \(q\) are
\[
q^{1+\epsilon-u}=q^{-(u-1)/2},\qquad
q^{\epsilon-u/2}=q^{-1/2},\qquad
q^{1-u+u/K}\le q^{-(u-1)/2}.
\]
Finally,
\[
\frac{\log Y+1}{\log q}=u+\frac1{\log q}<u+2.
\]
This proves the boxed assertion. ∎

More flexibly, the proof gives, for fixed \(K\ge3\) and \(\epsilon>0\),
\[
\frac{\varphi(q)}{\log q}T(q,a;q^u)
\ll_{u,K,\epsilon}
q^{1-u+\epsilon}+q^{-u/2+\epsilon}+q^{1-u+u/K}. \tag{3}
\]
This sharper form is useful if the eventual zero estimate has a shrinking margin.

**The threshold \(u>1\) is sharp for uniform negligibility of this tail.** Fix \(0<u\le1\). For arbitrarily large odd primes \(p\), take
\[
q=2^{\lfloor (2/u)\log_2p\rfloor},\qquad a\equiv p^2\pmod q.
\]
Then \(a\) is coprime to \(q\), and
\[
q^u\le p^2<2^uq^u.
\]
The single square \(p^2\) therefore yields
\[
\frac{\varphi(q)}{\log q}T(q,a;q^u)
\ge
\frac{q}{2\log q}\frac{\log p}{p^2}
\ge u\,2^{-u-2}q^{1-u}.
\]
At \(u=1\) this is at least \(1/8\); for \(u<1\) it grows. Thus an unrestricted assertion of uniform negligibility at \(u=1\) would be false.

This improves the *naive removal argument*, which uses all prime powers globally and requires a lower support exponent greater than \(2\). It does not itself improve a least-prime exponent.

### 2. A precise zero criterion for an exponent below \(3.99\)

Fix
\[
1<u<v<3.99
\]
and a nonzero nonnegative real function \(f\in C_c^\infty((u,v))\). Define its Laplace transform
\[
F(z)=\int_{\mathbb R}f(t)e^{-zt}\,dt.
\]
For each character \(\chi\bmod q\), let \(\chi^*\) be its inducing primitive character. For every nontrivial zero \(\rho=\beta+i\gamma\) of \(L(s,\chi^*)\), counted with multiplicity, put
\[
z_\rho=(1-\rho)\log q.
\]
Define the absolutely convergent sum
\[
Z_f(q,a)=
\sum_{\chi\bmod q}\overline{\chi(a)}
\sum_{\rho\ {\rm of}\ L(s,\chi^*)}F(z_\rho).
\]

Then, uniformly in coprime \(a\),
\[
\boxed{\quad
\frac{\varphi(q)}{\log q}
 \sum_{\substack{p\ {\rm prime}\\p\equiv a\pmod q}}
 \frac{\log p}{p}f\!\left(\frac{\log p}{\log q}\right)
 =
F(0)-Z_f(q,a)+O_{f,u}(q^{-\eta}),
\quad} \tag{4}
\]
where \(\eta=\min((u-1)/2,1/2)\). The quantity \(Z_f(q,a)\) is real, by conjugate pairing.

In particular, a fixed \(\delta>0\) and a bound
\[
Z_f(q,a)\le F(0)-\delta
\]
for **every sufficiently large \(q\)** and **every coprime \(a\)** would prove
\[
P(a,q)<q^v
\]
uniformly, and hence solve the requested target.

**Standard analytic facts used from memory.** I used the usual analytic continuation and functional equation for primitive Dirichlet \(L\)-functions; nonvanishing on \(\Re s=1\); the zero count
\[
N_\chi(T)\ll (T+1)\log(d(T+2))
\]
for primitive conductor \(d\); and the standard contour-shift estimates for their logarithmic derivatives away from zeros. These are standard foundational facts, not remembered numerical zero-density or zero-free-region constants. I have no uncertainty about the forms needed here.

**Derivation of (4).** Set
\[
g_q(x)=x^{-1}f\!\left(\frac{\log x}{\log q}\right).
\]
Its Mellin transform is
\[
H_q(s)=(\log q)F((1-s)\log q).
\]
Mellin inversion on \(\Re s=c>1\) gives
\[
\sum_n\Lambda(n)\chi^*(n)g_q(n)
=
\frac1{2\pi i}\int_{(c)}
-\frac{L'}{L}(s,\chi^*)H_q(s)\,ds.
\]
Shift to \(\Re s=-1/2\). The pole at \(1\), when \(\chi^*\) is principal, contributes \((\log q)F(0)\). The nontrivial zeros contribute
\[
-(\log q)\sum_\rho F(z_\rho).
\]
The only possible trivial zero crossed is at \(0\), of order at most one, and its contribution has absolute value at most
\[
(\log q)q^{-u}\|f\|_1.
\]

The functional equation and the absolutely convergent logarithmic derivative at \(\Re s=3/2\) give
\[
\left|\frac{L'}{L}(-1/2+it,\chi^*)\right|
\ll\log(d(|t|+2)).
\]
Twice integrating the transform by parts gives
\[
|H_q(-1/2+it)|
\le
\frac{\|f''\|_1q^{-3u/2}}
{\log q\,((3/2)^2+t^2)}.
\]
Thus the new vertical integral is \(O_f(q^{-3u/2})\), uniformly for \(d\le q\). Rapid transform decay, together with the zero count, justifies absolute convergence of the zero sum and the usual limiting contour shift.

Passing from \(\chi^*\) to \(\chi\) removes only powers of primes dividing \(q\). Their total absolute contribution is at most
\[
2\|f\|_\infty q^{-u}\sum_{p\mid q}\log p
\le 2\|f\|_\infty q^{-u}\log q.
\]
Character orthogonality consequently gives
\[
\frac{\varphi(q)}{\log q}
\sum_{\substack{n\equiv a\pmod q}}
\frac{\Lambda(n)}n f\!\left(\frac{\log n}{\log q}\right)
=
F(0)-Z_f(q,a)+O_f(q^{1-u}).
\]
The prime-power lemma removes \(n=p^k\), \(k\ge2\), with error \(O_{f,u}(q^{-\eta})\). This proves (4). ∎

### 3. Why the attempted analytic shortcuts do not finish the target

**A density exponent alone does not make the error tend to zero.** Write
\[
\lambda=(1-\beta)\log q,\qquad \mu=\gamma\log q.
\]
For a zero with fixed \(\lambda\), its contribution at \(x=q^L\) has size on the scale
\[
x^{\beta-1}=e^{-L\lambda}.
\]
Increasing the onset \(q_0\) does not make that quantity smaller. Thus the inference “a density exponent \(A<L\) implies an \(o(1)\) zero error” is invalid without quantitative control of the low zeros and the associated constants.

Here is a precise sufficient estimate, showing what is missing. Fix an integer \(m\ge2\), and define the weighted counting function
\[
M_q(t)=
\sum_{\chi\bmod q}
\sum_{\substack{\rho\\(1-\beta)\log q\le t}}
(1+|\gamma|\log q)^{-m}.
\]
Suppose all included zeros have \(\lambda\ge b\), and
\[
M_q(t)\le C e^{At}
\]
with uniform explicit constants. Integration by parts in \(F\) gives
\[
|F(\lambda-i\mu)|
\le K_{f,m}e^{-u\lambda}(1+|\mu|)^{-m},
\quad
K_{f,m}=2^m\max(\|f\|_1,\|f^{(m)}\|_1).
\]
For \(u>A\), Stieltjes integration therefore proves
\[
\sum_{\chi,\rho}|F(z_\rho)|
\le
K_{f,m}\frac{Cu}{u-A}e^{-(u-A)b}. \tag{5}
\]
Indeed, writing the weighted zero measure as \(dM_q(t)\),
\[
\int e^{-ut}\,dM_q(t)
=u\int_b^\infty e^{-ut}M_q(t)\,dt
\le\frac{Cu}{u-A}e^{-(u-A)b}.
\]

I did **not** establish constants \(A,C,b\) making (5) smaller than \(F(0)\) for any \(u<v<3.99\). No claimed numerical density theorem has been silently imported.

**An exceptional real zero leaves a shrinking margin.** Suppose a real character has a real zero
\[
\beta_e=1-\lambda_e/\log q.
\]
Its term is \(\chi_e(a)F(\lambda_e)\). For \(a=1\), its sign is always \(+1\), so the principal term minus this zero is
\[
F(0)-F(\lambda_e).
\]
Since \(f\ge0\) and its support lies in \([u,v]\),
\[
(1-e^{-u\lambda_e})F(0)
\le F(0)-F(\lambda_e)
\le v\lambda_e F(0). \tag{6}
\]
For \(u\lambda_e\le1\), the lower bound is at least
\[
\frac{u\lambda_e}{2}F(0).
\]
Thus a fixed absolute error bound for the remaining zeros is insufficient when \(\lambda_e\) is very small. Their contribution, and the arithmetic error in (4), must be controlled relative to this shrinking margin.

For example, if a repulsion bound supplied
\[
b\ge B\log(1/\lambda_e)-D
\]
for the other zeros, (5) would bound their contribution by
\[
K_{f,m}\frac{Cu}{u-A}e^{(u-A)D}
\lambda_e^{B(u-A)}.
\]
It is \(o(\lambda_e)\) if \(B(u-A)>1\). This is a proved conditional reduction, **not** a proved repulsion estimate with constants sufficient for the target. The arithmetic error must also be \(o(\lambda_e)\); formula (3) permits a sharper removal error when needed.

**Positive smoothing cannot arbitrarily suppress near-real zeros.** For \(\lambda\ge0\),
\[
F(\lambda)\ge e^{-v\lambda}F(0).
\]
More generally, if \(|\mu|(v-u)\le\pi\), rotating the integral by the phase at the midpoint of \([u,v]\) gives
\[
|F(\lambda-i\mu)|
\ge
\cos\!\left(\frac{|\mu|(v-u)}2\right)
e^{-v\lambda}F(0). \tag{7}
\]
This follows by taking the real part of
\[
e^{-i\mu(u+v)/2}
\int f(t)e^{-\lambda t}e^{i\mu t}\,dt.
\]
Consequently, an absolute-sum method needs real information excluding or repelling troublesome low-zero configurations; choosing a positive smoothing function alone cannot remove them.

### 4. Other routes checked

I also checked two tempting reductions and found no route through them:

- Bounds for character nonresidues can show that small primes **generate** the unit group. Generation does not ensure a prime in each individual residue. Already in an abstract cyclic group, a singleton generator generates every element while containing only one element.
- A mean-square statement must be much stronger than a “most residues” statement to exclude one missing residue. Precisely, if \(F:G\to\mathbb R_{\ge0}\) on a group of order \(h>1\) has total mass \(M\), and \(F(a_0)=0\), then
  \[
  \sum_{a\in G}(F(a)-M/h)^2\ge\frac{M^2}{h(h-1)}.
  \]
  Proof: the deviation at \(a_0\) is \(-M/h\), and the other deviations sum to \(M/h\); apply Cauchy–Schwarz to those \(h-1\) deviations. Equality occurs when all other entries equal \(M/(h-1)\). By Parseval, excluding every empty residue requires
  \[
  \sum_{\chi\ne1}|\widehat F(\chi)|^2<\frac{M^2}{h-1}.
  \]
  I did not obtain such a prime-distribution estimate.

**Exact remaining gap:** prove a uniform bound on \(Z_f(q,a)\), with adequate margin after a possible exceptional zero, for some fixed nonnegative \(f\) supported in an interval \((u,v)\) with \(1<u<v<3.99\). The elementary removal and contour arguments above do not supply that bound. No uniform least-prime exponent below \(3.99\), restricted substitute presented as uniform, or effective onset at the frontier has been proved.

---

## Adversarial verdict SQ-A / SD-A / SP-A

Ordinary reviewer /root/ref_e1_b passed all substantive positive derivations, subject to the following precise scope. This is same-vendor mathematical review only, not source validation, numerical solver verification or formalization.

- SQ-A: exact prime/semiprime count, weighted-sieve identity and explicit lower bound, Mobius first-moment error, both false positives, all twenty hand witnesses, balanced-product/multiple/roughness tests PASS. Its scaling statement concerns WHOLE REAL intervals only. It cannot exclude fitting their integer points: 5*{2,3}={10,15} lies in(9,16). No valid general descent was obtained.
- SD-A: actual conditional-copy construction, exact identity/deficit, pointwise strictness for M>0, finite-channel example, four-atom and asymptotic binomial counterexamples, three-point lower bound and entropy/cardinality equivalence all PASS. The binomial counterexample has a rigorous negative limiting deficit and hence eventual finite counterexamples, but no checked/effective numerical onset. Generic finite-channel laws do not supply the necessary real-additive restrictions. Strictness for each distribution does not imply a smaller universal constant.
- SP-A: sign reduction, ordered-energy/dyadic/adjacent-ray estimates, shared-ray overlap lemma, every block-size case, conditional exponent258/193 and log power65/193, interval overlap examples and aggregate energy bound PASS. For a general real set, the fibre hypothesis must apply to the selected positive or negated-negative subset. A fixed admissible packing constant is c_C=(2C)^(-1/4)/32. An explicit coefficient in the conditional bound is min(1/8,[(2C)^(-1/4)/(32*8^(1+kappa/4))]^(1/(3+kappa/4))). The interval examples refute an all-fibre/all-overlap saving only. They DO NOT refute the precise existential energy-significant class with half good slopes; both raw assertions to that effect are withdrawn. The preserved original is not silently rewritten.

## Completed first probes POW-A and LIN-A: assessment pending adversarial audit

POW-A: UTC10:46:42–11:01:41,14m59s. Universal target OPEN. It derives analytic finite coverage for k85 and all integers1≤n≤7,980,000,000 from a recalled Dusart bound, gives the exact missing-onset interval, rules out direct containment of an86th-power interval in an85th-power interval, supplies an artificial-integer-set nonimplication example and an equivalent consecutive-prime root-floor criterion. Root checked its logarithm-series estimates and exact product C*(22.8)^2=7,981,168,500. These are paper arithmetic checks, not a sweep through7.98billion integers or prime tables.

Post-probe source check confirms [Dusart2010, Proposition6.8](https://arxiv.org/pdf/1002.0442): for x>396738 there is x<p≤x(1+1/(25log²x)). The probe's endpoint x≥396738 is immaterial to its application x=n85 with n≥2. Thus its finite result is a direct corollary of known input, not a new prime-distribution estimate. [Baker–Harman–Pintz2001, Theorem1](https://www.cs.umd.edu/~gasarch/BLOGPAPERS/BakerHarmanPintz.pdf) confirms the recalled backward interval[x−x^.525,x] for x>x0, with no numericalx0 in the statement. One may enlarge an existence threshold to use the probe's generic closed-onset formulation, but may not claim a numerical bridge from the source. The abstract's forward-interval wording is not substituted for this exact theorem. The artificial Bertrand property is understood for integersm≥2.

LIN-A: UTC10:47:06–11:02:17,15m11s. Target OPEN. For every fixedu>1 it proves uniform negligible reciprocal prime-power tails in each coprime residue, with eta=min((u−1)/2,1/2), explicit coefficient4(u+2)(K^(M+1)+1), K=ceil(2u/(u−1)), M=ceil(K^(2/(u−1))), for q≥2^(K/u). It proves sharpness of this particular tail-negligibility cutoff at u=1, not a barrier for all smoothed weights or Linnik methods. It derives a smooth explicit-formula criterion supported on1<u<v<3.99, but obtains no zero bound making its main term positive uniformly. Its zero-counting, exceptional-zero, positive-smoothing and Parseval analyses locate missing estimates rather than supplying them.

A post-probe primary-source comparison finds the reciprocal smoothed prime sum, primitive-character replacement, Laplace zero sum and shift to Re(s)=−1/2 already in [Heath-Brown, Section13](https://www.researchgate.net/publication/248493012_Zero-Free_Regions_for_Dirichlet_L-Functions_and_the_Least_Prime_in_an_Arithmetic_Progression), author-uploaded full text. The framework is known. That passage uses a global prime-power error; it does not establish the exact congruence-sensitive tail lemma in LIN-A. Its novelty remains UNCLEARED. In the inspected Lemma13.2, the support lower endpoint already exceeds3; root's inference is that lowering the auxiliary prime-power cutoff from2to1 alone does not relax that lemma's dominant condition. This is a comparison with the specified older argument, not a claim about every contemporary proof.

Full originals for all nine A probes are now retained. All nine universal numerical targets remain OPEN in those probes. Ordinary reviewer now audits POW-A and LIN-A; fresh M22-B and HN-B are active. Seven B probes have not yet started.

## Adversarial verdict POW-A / LIN-A

Ordinary reviewer /root/ref_e1_b passed the main mathematical claims, with the repairs below. Root also walked the finite-range arithmetic and prime-power/contour estimates. This is same-vendor review, not kernel verification or a new numerical frontier.

POW-A's finite coverage, generic eventual-interval implication, failed containment, artificial-set model and consecutive-prime floor-jump equivalence PASS. Dusart's strict threshold is satisfied in every application. To use BHP at its boundary, add this argument: take real x_j↓x0; all supplied primes lie in a common bounded neighborhood, hence one recurs on a subsequence, and passage to the limit places it in[x0−x0^.525,x0]. This extends the closed-interval existence statement to x=x0. With that addition, the probe's non-strict bridge x0≤(N+2)^85 and strict uncovered cutoff are valid. Without it, direct source substitution requires x0<(N+2)^85 and retains equality in the uncovered range. No numericalx0 was extracted. The artificial set's Bertrand property is for integersm≥2, and its eventual interval properties are feasible families such as fixed positive-power widths x^theta, theta>0; it cannot fill arbitrary subunit intervals for all realx.

LIN-A's local root count, low/high-exponent estimates, explicit coefficient/onset, flexible three-power error and tail sharpness PASS. In the high-k estimate, with Z=Y^(1/K), the total is bounded by 2Z^(1−K)*[(1+1/Z+1/(K−1))*logZ+1/(K−1)^2], below the stated4(logY+1)Y^(−1+1/K). The smooth explicit formula, primitive-character correction, contour/trivial-zero terms, absolute convergence, uniformity in a, conditional zero criterion, weighted zero bound, exceptional-zero inequalities, phase-rotation inequality and variance estimate also PASS.

Two LIN-A wording repairs are necessary. First, global removal does NOT requireu>2 merely for negligibility: Chebyshev bounds give sum_{p≥q}(logp)/p²≪q^(−1); with the K=3 tail, the normalized global error atu=2 is O(1/logq+q^(−1/3))=o(1). The crude integer majorant requiresu>2 for its displayed power saving. The congruence-sensitiveu>1lemma itself is unaffected. Second, on a finite ABELIAN group, with unnormalized Fourier transform hatF(chi)=sum_a F(a)conj(chi(a)), the strict Parseval threshold is SUFFICIENT, not necessary, for every entry to be positive. On C3, F=(8,1,1) is positive everywhere but its nontrivial Fourier square sum is98>100/2. For a general nonabelian group the matrix-transform version needs dimension weights. The threshold remains sharp as a sufficient second-moment certificate. When isolating an exceptional zero, count one occurrence or a simple zero, leaving any further multiplicity in the remaining sum.

All nine A probes now have completed adversarial mathematical review. Every precise target remains OPEN. Three fresh B probes are active: M22-B, HN-B and SID-B; six B probes are not yet dispatched.

## Completed second probes M22-B and HN-B (adversarial audit pending)

M22-B independently recovered M22-A's same odd-prime affine-projection obstruction, with a complete proof using the nonzero quadrant defect, fibre divisibility, mixed finite differences and parity summation. Its exact scope is two squares with common row/column labels and fixed field coefficients across all four binary quadrants. It also recovered the proper-block PBD obstruction. A square containing an11-by11 Latin subsquare cannot have a transversal: the Latin property forces alternating11-symbol sets in the four quadrants, and a transversal takes an even number from the first set. Thus group tables of order22 and their isotopes are excluded. These are construction-family obstructions, not N(22)≤3.

Its explicit scope counterexample is L((a,x),(b,y))=(a+b+1_{y=x+1},x+y) over F2×F11. This square is Latin and HAS a transversal: cells ((0,x),(0,x)) and ((1,x),(1,x+1)), x∈F11, give respectively (0,2x) and (1,2x+1). Therefore the zero-defect affine family does not universally lack transversals; the main lemma excludes two affine projections together.

M22-B's exact symmetry reduction uses44 representatives v_s=((b_sj,d_sj))_{j=1}^6 with b_sj∈F2,d_sj∈F11. For every coordinate pair j<k, the44 triples (b_sj,b_sk,d_sk−d_sj) must enumerate F2²×F11 exactly once. Develop each representative by common translations d_sj→d_sj+t. This yields484 rows of an OA(484,6,22,2), hence four MOLS, and conversely every such OA with this common translation action gives44 free orbits with exactly these conditions. The binary projection alone is an OA with index11 and is insufficient. No44 representatives were found. This is equivalent in scope to A's common-translation reduction, not a more general construction. No new target number moved. Reported reasoning11:03:33–11:21:03,17m30s.

HN-B reported reasoning11:05:56–11:21:20,15m24s, and three partial results. None proves χ≥6.

1. For every finite plane unit-distance graph, χ_f≤C=(3+6√2+6√3+2√6)/(π+3)<5. Set θ=π/12,a=cosθ/2,L=1+2a; let K be the OPEN radius1/2 disk intersected with |x·n_j|<a for unit normals at angles0,π/3,2π/3. Translate K by the triangular lattice generated by L n_0,L n_1. Within a copy, distances are<1; between nearest copies normal projections are> L−2a=1; other center separations are≥√3 L>2. Six disjoint removed caps each have areaπ/48−1/16, so |K|=(π+3)/8 and densityδ=(π+3)/(4√3 L²)=1/C. Uniform random translation on the lattice torus includes each fixed vertex with probabilityδ, giving a fractional colouring and an independent subset of at leastδ of any nonnegative vertex weight. This rules out proving6 by a weighted independence bound alone, not by ordinary-colouring obstructions.

2. Every finite unit-distance configuration whose edge directions differ by rational multiples ofπ is3-colourable. For a prime power p^a,h=p^{a−1}, choose p signs b_j∈{±1}⊂F3 with sum0. The integral basis ζ^{s+jh},0≤s<h,0≤j<p−1, maps additively to b_j; the cyclotomic relation gives b_{p−1} on the missing block. Thus every p^a-th root has nonzero image. For N=∏p_i^{a_i}, multiplication identifies the tensor product of these free integral modules with Z[ζ_N]: it is surjective and the ranks equalφ(N). The product of the prime-power additive maps defines an additive map f_N:Z[ζ_N]→F3 nonzero on each N-th root. After a common rotation, all finitely many oriented unit-edge vectors are such roots. Componentwise displacement from a base vertex is in Z[ζ_N]; apply f_N to colour. For N=1 one uses the empty tensor convention, equivalently integer reduction mod3.

The same conclusion holds when, after a common rigid motion, all coordinates are cyclotomic algebraic INTEGERS: every unit difference u satisfies u conjugate(u)=1, all embeddings of its cyclotomic field commute with conjugation, and hence all conjugates have modulus1. The minimal polynomials of all powers of u have bounded degree and bounded integer coefficients, so there are finitely many powers and u is a root of unity. This does not apply to arbitrary cyclotomic field elements with denominators.

3. A finite plane unit-distance graph with minimum degree≥5 has at least14 vertices. Distinct points have at most two common unit neighbours; every neighbourhood graph is a subgraph of disjoint6-cycles. For a vertex of degree d and e_v neighbourhood edges, counting length-two walks gives 4d≤Σ_{w∈N(v)}(deg(w)−1)≤2e_v+2(n−1−d). Choose a uniquely extreme point for a generic linear functional. Its neighbours lie in a strict open semicircle, so neighbourhood path components have at most3 vertices and e_v≤floor(2d/3). Thus n≥3d−floor(2d/3)+1≥13.

For n=13, e_v≤d forces every degree≤6. Degrees cannot all be5 by parity, so some vertex has degree6. All the preceding counting inequalities there are equalities: its neighbours form a regular unit hexagon, all have degree5, and every remaining vertex has exactly two neighbours in the hexagon. Write its vertices a_j=e^(ijπ/3) with center0. Besides0, the common neighbour of a_i,a_j is a_i+a_j when distinct. Two-step pairs give an existing hexagon vertex; opposite pairs have only0. Therefore the six outside vertices must be the six points a_j+a_{j+1}. They have radius√3, no unit edges among themselves, no edge to0, and exactly two inner-hexagon neighbours, contradicting minimum degree5. A vertex-minimal non-5-colourable graph has minimum degree5, giving the claimed necessary14-vertex bound. For non-induced unit-distance subgraphs one can first add all geometric unit edges; minimum degree only increases. No existence at14 or general5-colouring follows.

HN-B novelty comparison after its completion: the rounded-disk/hexagon packing and its fractional-colouring implication are KNOWN, with a stronger optimized parameter already covered by [Grytczuk et al., Theorem3 and its proof](https://arxiv.org/pdf/1506.01887), which develops the Hochberg–O'Donnell construction. HN-B uses a convenient exact angle rather than the optimum; it is not a new fractional record. A bounded search did not settle prior status of the exact rational-direction colouring proof or14-vertex lemma; both remain novelty-UNCLEARED. The Polymath2018 discussion distinguishes cyclotomic fields from integer modules; it is not evidence that HN-B settled an open unrestricted plane-colouring question.


## Full probe output retained: SID-B

I obtain a **candidate complete proof** of the requested target:

\[
\boxed{F(N)\le \sqrt N+\frac{2\sqrt2}{3}N^{1/4}+1
\qquad(N\ge120^4=207\,360\,000).}
\]

Here \(2\sqrt2/3=0.942809\ldots<0.943\), and both \(K=1\) and \(N_0=207\,360\,000\) are numerical. The argument below has no knowingly unresolved dependency. Because this improves the supplied records, it needs independent auditing before being treated as a verified project result.

UTC reasoning interval: **11:22:07–11:38:35**, approximately 16½ minutes. I used no files, external sources, computations, solvers, or other agents.

The central construction is a cubic positive definite kernel with an elementary renewal-theoretic boundary correction.

### 1. The kernel

Put
\[
h(t)=2(1-t)\mathbf1_{[0,1]}(t),\qquad
\widetilde h(t)=h(-t),\qquad f=h*\widetilde h.
\]
Direct integration gives
\[
f(x)=
\begin{cases}
\displaystyle\frac43-2|x|+\frac23|x|^3,& |x|\le1,\\
0,&|x|>1.
\end{cases}
\]
Consequently:

- \(f\ge0\);
- \(f\) is nonincreasing on \([0,\infty)\);
- \(f(0)=4/3\);
- \(\int_{\mathbb R}f=1\);
- \(f\) is positive definite.

For finite signed real measures \(\mu,\nu\), define
\[
E(\mu,\nu)=\iint f(x-y)\,d\mu(x)\,d\nu(y).
\]
Since \(f=h*\widetilde h\),
\[
E(\mu,\nu)=\int_{\mathbb R}(h*\mu)(t)(h*\nu)(t)\,dt.
\]
Thus
\[
|E(\mu,\nu)|^2\le E(\mu,\mu)E(\nu,\nu).
\tag{1}
\]
All these integrals exist: \(h\in L^2\), and convolution with a finite measure maps \(h\) into \(L^2\).

### 2. An exact half-line potential

Let \(U\) be the probability measure uniform on \([0,1]\), and set
\[
g_+=\frac12\sum_{n=0}^{\infty}U^{*n},
\qquad U^{*0}=\delta_0.
\]
This is locally finite. Indeed, the density of \(U^{*n}\), for \(n\ge1\), is at most \(t^{n-1}/(n-1)!\) at \(t\ge0\).

We have the exact convolution identity
\[
h*g_+=\mathbf1_{[0,\infty)}.
\tag{2}
\]
Here and below single-point choices for functions do not affect the subsequent integrals.

To prove (2), let \(X_1,X_2,\ldots\) be independent uniform random variables on \([0,1]\), and \(S_n=X_1+\cdots+X_n\), with \(S_0=0\). Since
\[
h(t)=2\Pr(X_1>t)\quad(t\ge0),
\]
\[
\frac12(h*U^{*n})(t)
=\Pr(S_n\le t<S_{n+1}).
\]
Almost surely \(S_n\to\infty\), so summing these disjoint events gives (2).

It follows by Tonelli and associativity that, for every \(x\ge0\),
\[
(f*g_+)(x)
=(\widetilde h*(h*g_+))(x)
=\int_{-1}^0\widetilde h(y)\,dy
=1.
\tag{3}
\]

### 3. A proved exponential remainder

Write
\[
g_+=\frac12\delta_0+\frac12u(t)\,dt
\]
on the nonnegative half-line. The renewal density \(u\) satisfies
\[
u(t)=e^t\quad(0<t<1)
\]
and
\[
u(t)=\int_{t-1}^{t}u(s)\,ds\quad(t>1).
\tag{4}
\]

Here is an elementary quantitative convergence proof, so no renewal theorem is being assumed.

For every integer \(n\ge1\) and \(0\le x\le1\), differentiating (4) almost everywhere and solving the resulting linear equation gives
\[
u(n+x)=e^xu(n)-\int_0^x e^{x-y}u(n-1+y)\,dy.
\]
Using \(u(n)=\int_0^1u(n-1+y)\,dy\), this becomes
\[
u(n+x)=\int_0^1 K_x(y)u(n-1+y)\,dy,
\]
where
\[
K_x(y)=e^x-\mathbf1_{\{y\le x\}}e^{x-y}.
\]
These kernels satisfy
\[
K_x(y)\ge0,\qquad \int_0^1K_x(y)\,dy=1.
\]
Furthermore, for every \(x\in[0,1]\) and \(y\in[1/2,1]\),
\[
K_x(y)\ge\frac12.
\]
For \(y>x\) this follows from \(K_x(y)=e^x\ge1\). For \(y\le x\),
\[
K_x(y)=e^{x-y}(e^y-1)\ge e^{1/2}-1>\frac12.
\]

Therefore all these averaging kernels contain the common measure
\[
\frac12\mathbf1_{[1/2,1]}(y)\,dy,
\]
whose mass is \(1/4\). The essential range on each successive unit interval lies inside the preceding range, and its width is at most \(3/4\) of the preceding width. Thus \(u(t)\) converges exponentially to a constant \(c\), with
\[
|u(t)-c|\le(e-1)(3/4)^{\lfloor t\rfloor}
<2(3/4)^{\lfloor t\rfloor}
\tag{5}
\]
almost everywhere.

For \(t>1\), equation (2) says
\[
1=\frac12\int_0^1 h(s)u(t-s)\,ds.
\]
Letting \(t\to\infty\), and using \(\int h=1\), shows \(c=2\).

Define the finite signed measure
\[
q=g_+-\mathbf1_{[0,\infty)}(t)\,dt
=\frac12\delta_0+r(t)\,dt,\qquad r(t)=\frac12u(t)-1.
\]
By (5),
\[
|r(t)|\le(3/4)^{\lfloor t\rfloor}.
\tag{6}
\]
In particular,
\[
\|q\|_{\mathrm{TV}}\le\frac12+\sum_{n=0}^{\infty}(3/4)^n
=\frac92.
\tag{7}
\]
Put \(\alpha=\log(4/3)\). For \(L\ge1\),
\[
\|q\|_{\mathrm{TV},(L,\infty)}
\le4(3/4)^{\lfloor L\rfloor}
\le\frac{16}{3}e^{-\alpha L}
\le6e^{-\alpha L}.
\tag{8}
\]

Finally,
\[
q(\mathbb R)=\frac13.
\tag{9}
\]
To verify this exact constant, for \(s>0\) the Laplace transform is
\[
\int e^{-st}\,dg_+(t)
=\frac{1}{2\left(1-\frac{1-e^{-s}}s\right)}
=\frac1s+\frac13+O(s).
\]
Subtracting the Laplace transform \(1/s\) of half-line Lebesgue measure and using the finite total variation of \(q\) proves (9) by dominated convergence.

### 4. A finite-interval energy bound

For \(L\ge1\), let \(q_L\) be the reflection of \(q\) under \(t\mapsto L-t\), and define the finite signed measure
\[
\nu_L=\mathbf1_{[0,L]}(t)\,dt+q+q_L.
\]
Its total mass is
\[
\nu_L(\mathbb R)=L+\frac23.
\tag{10}
\]

The potential is exactly constant on the desired interval:
\[
(f*\nu_L)(x)=1\qquad(0\le x\le L).
\tag{11}
\]
Indeed, as locally finite measures,
\[
\nu_L=g_++g_-^L-dt,
\]
where \(g_-^L\) is the reflection of \(g_+\) about \(L/2\). Equation (3) gives potential \(1\) for the first term when \(x\ge0\), and for the second when \(x\le L\). Full-line Lebesgue measure has potential \(\int f=1\). All convolutions here are well-defined locally because \(f\) has compact support.

Write \(V_L=f*\nu_L\). Since \(\|f\|_\infty=4/3\), equations (7) and \(\int f=1\) give
\[
|V_L(x)|\le1+2\cdot\frac43\cdot\frac92=13.
\tag{12}
\]
Outside \([0,L]\), the measure \(\nu_L\) consists of the two reflected tails appearing in (8). Combining (10)–(12),
\[
\begin{aligned}
\left|E(\nu_L,\nu_L)-\left(L+\frac23\right)\right|
&=\left|\int_{\mathbb R\setminus[0,L]}(V_L-1)\,d\nu_L\right|\\
&\le14\cdot12e^{-\alpha L}\\
&\le200e^{-\alpha L}.
\end{aligned}
\tag{13}
\]

If \(\mu\) is any finite positive measure supported on \([0,L]\), of total mass \(k\), then (11) implies
\[
E(\mu,\nu_L)=k.
\]
Cauchy–Schwarz (1) and (13) therefore give
\[
\boxed{
E(\mu,\mu)\ge
\frac{k^2}{L+\frac23+200e^{-\alpha L}}.
}
\tag{14}
\]
No positivity of the auxiliary measure \(\nu_L\) is required.

### 5. Apply uniqueness of ordered differences

Let \(A\subset\{0,\ldots,N-1\}\) satisfy the question’s hypothesis, and write \(k=|A|\).

For any real \(T>0\), put
\[
\mu=\sum_{a\in A}\delta_{a/T},\qquad L=\frac NT.
\]
Its support lies in \([0,L]\). The actual endpoint \((N-1)/T\) is smaller than \(L\); no replacement of interval length by endpoint is being made.

Every positive integer difference occurs at most once. Hence
\[
E(\mu,\mu)
=\frac43k+2\sum_{d\in D_+(A)}f(d/T)
\le\frac43k+2\sum_{d=1}^{\infty}f(d/T).
\]
Because \(f\) is nonnegative and nonincreasing on the positive half-line,
\[
\sum_{d=1}^{\infty}f(d/T)
\le T\int_0^\infty f(x)\,dx=\frac T2.
\]
Thus
\[
E(\mu,\mu)\le T+\frac43k.
\tag{15}
\]
The diagonal contribution is exactly \(kf(0)=4k/3\).

Combining (14) and (15), whenever \(N/T\ge1\),
\[
k^2\le
\left(\frac NT+\frac23+200e^{-\alpha N/T}\right)
\left(T+\frac43k\right).
\tag{16}
\]

### 6. Explicit coefficient, constant, and onset

Set
\[
x=N^{1/4},\quad T=\sqrt2\,x^3,\quad
\gamma=\frac{2\sqrt2}{3},\quad
\varepsilon=200e^{-\alpha x/\sqrt2}.
\]
Then (16) becomes
\[
P_\varepsilon(k)\le0,
\]
where
\[
P_\varepsilon(z)=
z^2-\left(\gamma x+\frac89+\frac43\varepsilon\right)z
-x^4-\gamma x^3-\sqrt2\,\varepsilon x^3.
\]

We show \(P_\varepsilon(x^2+\gamma x+1)>0\) for \(x\ge120\).

First,
\[
\alpha=\log(4/3)\ge\frac14,\qquad \sqrt2\le\frac32,
\]
so \(\alpha/\sqrt2\ge1/6\). As \(x e^{-x/6}\) decreases for \(x\ge6\),
\[
\varepsilon x\le24000e^{-20}
<\frac{24000}{2^{20}}<\frac1{32}
\qquad(x\ge120).
\tag{17}
\]

Let \(y=x^2+\gamma x+1\). Exact expansion gives
\[
P_0(y)=\frac{10}{9}x^2+\frac{\gamma}{9}x+\frac19\ge x^2.
\tag{18}
\]
Since \(\gamma<1\), we have \(y\le3x^2\) for \(x\ge1\). Using (17),
\[
\begin{aligned}
\varepsilon\left(\frac43y+\sqrt2\,x^3\right)
&\le\frac{1}{32x}\left(4x^2+\frac32x^3\right)\\
&=\frac{x}{8}+\frac{3x^2}{64}
\le\frac{11x^2}{64}.
\end{aligned}
\]
Together with (18), this proves \(P_\varepsilon(y)>0\).

The quadratic \(P_\varepsilon\) has negative constant term and positive leading coefficient, hence exactly one positive root. Since \(P_\varepsilon(k)\le0\) and \(k\ge0\), it follows that \(k<y\), proving the stated bound.

Finally,
\[
\left(\frac{943}{1000}\right)^2-\left(\frac{2\sqrt2}{3}\right)^2
=\frac{3241}{9\,000\,000}>0.
\]
Thus the coefficient is strictly below \(0.943\).

### Attempts rejected and remaining status

The initial uniform-window energy bound gives coefficient \(1\). Attempts to improve it by assuming approximately uniform endpoint density are invalid: the hypothesis does not prevent substantial endpoint concentration on the relevant scale. I discarded those assumptions.

The successful construction instead allows the boundary correction explicitly, using an exact half-line potential and a signed finite-interval auxiliary measure. The signed measure causes no gap because the required inequality is Hilbert-space Cauchy–Schwarz, not a positivity comparison.

I found no remaining mathematical gap in the argument above. **External checking, source/priority comparison, and kernel formalization remain undone.**


## SID-B assessment and post-probe source comparison (provisional referee pass)

The complete clean-room proof above claims the fully effective theorem F(N)≤√N+(2√2/3)N^(1/4)+1 for every integer N≥207360000, with exactly the ordered-difference convention fixed at the status gate. Root independently walked the kernel, half-line identity, elementary contraction, finite signed-measure gluing, Cauchy inequality and final quadratic calculation without finding a gap. A fresh ordinary adversarial referee, ref_probe_b1, returned an immediate mathematical PASS, subject to setting u(1)=e−1 as the right-hand value in the interval recurrence; its detailed verdict and other two audits are pending. This is same-vendor model review, not human, cross-vendor or kernel verification.

The exact comparison is 8/9 < (943/1000)^2, with difference3241/9000000. The candidate coefficient is therefore strictly below the pinned q2 coefficient, whose square comparison with .943 was independently checked earlier. No replay of q2's covering certificate is implied.

After the frozen probe completed, root reopened [Hou–Zhao v3](https://arxiv.org/pdf/2607.01169v3) and the [q2 README at its pinned commit](https://raw.githubusercontent.com/wustep/maths/da2440b68979b78d201182118d30ca418e3c2001/problems/sidon-second-term/compute/q2/README.md). Their stated numerical bounds remain above SID-B's. The former uses finite symmetric kernel vectors and boundary weights; q2 uses the same framework. No exact renewal-boundary formula or coefficient2√2/3 was located in these texts or the bounded exact-coefficient/method searches. This establishes comparison with located records, not a global priority claim. The Hou–Zhao source is a public preprint; peer-reviewed publication status is not established here.

At11:43UTC, public GitHub GETs confirmed that the newest commit affecting wustep/maths/problems/sidon-second-term is still da2440b68979b78d201182118d30ca418e3c2001, August27,07:16:18UTC. The current-main q2 README matches the pinned numerical claim. [Linnik PR205](https://github.com/teorth/optimizationproblems/pull/205) was still open/unmerged, last updated07:17:56UTC, with zero comments and review comments. A fresh Erdős30 page/forum fetch returned403; that failed fetch supplies no new status. No private credentials or remote mutations were used.

Even if SID-B passes all remaining gates, the original Erdős30 conjecture of a remainder O_epsilon(N^epsilon) remains OPEN. The improvement concerns only the N^(1/4) coefficient. Recommendation waits for the remaining requested probes.

## Completed second probe SP-B (adversarial audit pending)

Target OPEN. Reported reasoning11:30:17–11:45:33,15m16s. No external sources, computations or files were used. The following preserves all claimed mathematical progress and its gaps.

For any nonempty finite real A of size n≥2, the larger strictly positive/negative portion, reflected if needed, yields B⊂R_{>0} of size N≥ceil((n−1)/2)≥n/3, with |B+B|≤|A+A| and |BB|≤|AA|. Treat n=1 separately. Put S=|B+B|,P=|BB|,X_lambda={x∈B:lambda x∈B},r_lambda=|X_lambda|,V_lambda={(x,lambda x):x∈X_lambda}, and E=Σr_lambda², counting ordered multiplicative-energy quadruples. Cauchy gives EP≥N⁴.

Let L=1+floor(log2N). In a dyadic class tau≤r_lambda<2tau with q slopes, adjacent-ray sumsets have disjoint strict angular supports and cardinalities at least tau². Thus S²≥(q−1)tau² for q≥2, while its class energy is≤4q tau²≤8S². A singleton class has energy≤N²≤S². Summing gives E≤8LS² and S²P≥N⁴/(8L). The transferred explicit all-real baseline is max(|A+A|,|AA|)≥n^(4/3)/[2*3^(4/3)*(1+log2n)^(1/3)], also valid for n=1. This is weaker than the frontier.

Choose a class with E_j≥E/L, and integer2≤k≤q/2. Partition the first k floor(q/k) slopes into consecutive k-blocks I. Define F_I(z)=Σ_{lambda<mu in I}1_{V_lambda+V_mu}(z), W=Σ_{I,z}F_I(z), C=Σ_{I,z}F_I(z)², D=C/W≥1. Different blocks have disjoint angular supports. Within each block W_I≥binom(k,2)tau², so W≥qk tau²/8≥kE_j/32≥kE/(32L). Cauchy gives W²≤S²C. Hence the exact unconditional reduction
S²P≥kN⁴/(32LD).
Defining D is not a bound on D.

The missing sufficient hypothesis (H) is: absolute C0,N0 exist such that every positive B with N≥N0 and P≤N^(401/300) has an energy-rich class E_j≥E/L whose blocks, for k=floor(N^(1/50)), satisfy D≤C0 N^(1/100). In this regime qN²≥E/L≥N⁴/(LP), so q≥N^(199/300)/L and q≥2k holds eventually. Under (H), k≥N^(1/50)/2 gives S²P≥N^(4+1/100)/(64C0L), hence max(S,P)≥(64C0L)^(-1/3)N^(401/300). The complementary large-P case is immediate. Absorbing logs, finite small N, and the sign reduction yields the universal target with delta=401/300−135/101=1/30300. Hypothesis(H) is UNPROVED.

Positivity/richness alone cannot supply this D bound. For B={1,...,N}, N a power of2, reduced slope a/b has r=floor(N/max(a,b)). For a power of2 K|N, tau=N/K, its class is exactly K/2<max(a,b)≤K. There are at least K²/18 reduced ordered pairs in this band: at most K²Σ_{d≥2}d^(−2)≤25K²/36 pairs are noncoprime, and subtracting the inner K²/4 square leaves K²/18. The displayed zeta tail follows from 1/4+1/9+∫_3^∞x^(−2)dx=25/36. Thus q tau²≥N²/18, and whenever q≥2k, W≥kN²/144. As S²=(2N−1)²<4N², Cauchy forces D≥W/S²≥k/576. Taking N a power of4,K=√N,k=floor(N^(1/50)) contradicts a UNIVERSAL D≤C0N^(1/100). It does NOT refute(H): counting reduced pairs by max denominator gives E≤Σ_{d≤N}2d(N/d)²≤2N²(1+logN), hence P≥N²/[2(1+logN)]>N^(401/300) eventually.

For four rays, a collision x(1,lambda1)+y(1,lambda2)=u(1,lambda3)+v(1,lambda4), with lambda1≠lambda2 and lambda3≠lambda4, has
u=[(lambda1−lambda4)x+(lambda2−lambda4)y]/(lambda3−lambda4),
v=[(lambda3−lambda1)x+(lambda3−lambda2)y]/(lambda3−lambda4).
The intersection size exactly counts pairs (x,y)∈X_lambda1×X_lambda2 for which these linear forms lie in X_lambda3,X_lambda4. With B={1,...,8m}, power-of2 m≥8, ray pairs(5,8),(6,7) all have cardinalities in[m,2m). Every integer x,y∈[m/2,5m/8] yields u=2x−y,v=2y−x∈[3m/8,3m/4], a valid collision. Injectivity of the first ray pair gives intersection≥(m/8+1)²≥m²/64. No uniform O(tau^(2−eta)) estimate follows merely from distinct positive rays of comparable richness.

Finally the formal exponent assignment S=P=N^alpha,q=N^alpha,tau=N^(2−alpha),E=N^(4−alpha) satisfies the baseline exponent inequalities for alpha≥4/3. This is an algebraic relaxation, not actual sets. At alpha=135/101 it leaves ray-packing slack N^(1/101). Per-fibre products are already bounded trivially by tau²=N^(134/101), smaller than the proposed global P=N^(135/101), so those inequalities alone cannot close the gap. No collective collision gain was proved.


## Completed second probe RAM-B (adversarial audit pending)

Target OPEN. Reported reasoning11:30:01–11:47:41,17m40s, with no files, external sources, experiments or other agents.

**Density-drop certificate.** Let c=11/3,q=3/8,n=floor(c^k),m=floor(n/2),a*=ceil(5k/6). For k≥1152, every colouring of K_n with no monochromatic K_k, after possibly exchanging colour names, admits disjoint A,B,X,Y with a=|A|<a*,b=|B|<k: A is a red clique, B a blue clique, all A–(X∪Y) edges red and all B–X edges blue,
|X|≥(m+1)2^(−a−b)−1, |Y|≥m q^a,
but red density d_R(X,Y)<3/8. It arises from a process starting at disjoint m-sets X0,Y0 with red cross-density≥1/2.

Whenever d_R(X,Y)≥q, averaging supplies v∈X with red Y-degree≥q|Y|. One internal colour has degree≥(|X|−1)/2. A red move appends v to A and restricts both X,Y to its red neighbours; a blue move appends v to B and restricts X to its blue neighbours, leaving Y unchanged. Either internal majority can be chosen in a tie. Invariants and the displayed size estimates follow from |X_new|+1≥(|X_old|+1)/2 and red-step Y losses≤q.

Reaching b=k gives a blue clique. Reaching a* gives a monochromatic K_k inside A∪Y: put r=k−a*=floor(k/6), beta=7^(7/6)/6. The elementary Ramsey and binomial entropy bounds give R(r,k)≤binom(r+k−2,r−1)≤binom(r+k,r)≤beta^k, since (1+x)log(1+x)−xlogx increases for x>0 and r/k≤1/6. For k≥2, m≥c^k/3, while a*≤5k/6+1, so m q^a*≥(c q^(5/6))^k/8. With rho=c q^(5/6)/beta,
rho^6=11^6*3^5/(2^9*7^7)=430489323/421654016>65/64.
For k≥1152, rho^k>(65/64)^192>8 by (1+1/64)^64>2. Hence |Y|>R(r,k). A red K_r combines with A, and a blue K_k already suffices.

Before either front threshold, t=a+b≤T=a*+k−2≤11k/6−1. Put kappa=c/2^(11/6); then (m+1)2^(−T)≥(2/3)kappa^k. As kappa^6=1771561/1492992>9/8, for k≥96 its k-th power is>(9/8)^16>4. Thus X cannot empty. The process must stop at density<q in a K_k-free colouring. A suitable density-preservation/recovery theorem would imply the target base11/3, but none is supplied.

Initial density and majority alone cannot preserve density: split X=X1∪X2,Y=Y1∪Y2 into four equal-sized classes. Colour X1X2,X1Y1,X2Y2 red, every other relevant internal-X or X–Y edge blue. The initial cross-density is1/2, every pivot has red Y-degree|Y|/2, and its unique internal majority is red. A red move leaves (X2,Y1) or (X1,Y2), with red density0. This example may contain large monochromatic cliques; it does NOT refute a preservation statement using their absence.

**Recurrence-only obstruction with exact fixed-width data.** Let C=3.69507. For every fixed integer M≥2 there exists a symmetric coordinatewise nondecreasing positive integer array F(s,t), s,t≥1, with F(1,t)=F(s,1)=1, F(s,t)≤F(s−1,t)+F(s,t−1) for s,t≥2, and F(s,t)=R(s,t) whenever min(s,t)≤M, but eventually F(k,k)≤C^k and lim F(k,k)^(1/k)=C. This is a synthetic array, not colourings.

Proof: a=√C,theta=π/12,lambda=2cos(theta)=√(2+√3), so1<a<lambda<2. Let h_d=cos(dtheta) for |d|≤5 and0 otherwise. Then0≤h_d≤1,h0=1 and h_{d−1}+h_{d+1}≥lambda h_d (cosine identity on support, zero RHS outside). Set epsilon=a^(−2M−5),H(s,t)=epsilon a^(s+t)h_{s−t}. For s,t≥2, the sum of its two predecessors is≥(lambda/a)H(s,t)≥H(s,t).

Take J(s,t)=max({1}∪{H(u,v):1≤u≤s,1≤v≤t}). It is symmetric/monotone and equals1 on min(s,t)≤M: a nonzero term there has u+v≤2M+5. J obeys the recurrence: if its maximum is>1, a maximizing pair has u,v≥2, and apply the H recurrence then bound each predecessor by the corresponding J predecessor; the case J=1 is immediate.

Define Q(s,t)=max(R(min(s,M),t),R(s,min(t,M))). On the fixed-width strip it equals R, and both predecessors stay in the strip, so obeys the genuine Ramsey recurrence. Outside, Q(s,t)=R(M,max(s,t)); decreasing a smaller coordinate leaves it unchanged, so one predecessor already equals Q. It is symmetric/monotone. Let F=max(Q,ceil J). Ceilings preserve the subadditive recurrence, and so does the pointwise maximum. It agrees with R on the strip. On the diagonal J(k,k)=max(1,epsilon C^k), while Q(k,k)=R(M,k)≤binom(M+k−2,M−1) is polynomial. Eventually F(k,k)=ceil(epsilon C^k), proving both the eventual bound and exact limiting rate. Any strict improvement must use something outside these numerical recurrence properties; actual-graph constraints may do so.


## Adversarial verdict SID-B / M22-B / HN-B

Fresh ordinary referee ref_probe_b1 independently audited all three and returned detailed PASS verdicts. Root separately checked the calculations. These checks are same-vendor mathematical reviews; there is no kernel, independent human or cross-vendor verification.

**SID-B: PROVED in the internal reviewed sense, with one representative convention made explicit.** Define the renewal density at t=1 by u(1)=e−1, its right-hand limit; the left limit is e. Use right-continuous representatives in the unit-interval recurrence. Nested CLOSED essential ranges then justify the contraction exactly as written; all downstream assertions are unchanged. The autocorrelation formula and integral, local finiteness, event-partition identity, averaging-kernel common mass, limiting density2, TV/tail bounds and Laplace excess mass1/3 pass. The signed auxiliary measure is valid in L² Cauchy. The exact gluing includes both tails and endpoint atoms, with potential1 throughout[0,L]; its energy error is actually bounded by168 exp(−alpha L), below the chosen200. Ordered differences and diagonal4k/3 are correctly counted. All quadratic expansions and explicit numerical bounds pass, including N0=120^4=207360000 and the exact strict comparison with .943. Thus the precise task target is met:
F(N)≤√N+(2√2/3)N^(1/4)+1 for every integer N≥207360000.
Source/priority limitations remain as recorded above, and Erdős30's original conjecture remains open.

**M22-B:** all construction-family obstructions and exact equivalences pass. The fixed-affine theorem genuinely needs an odd PRIME field in the translation-generation step; it is not justified for arbitrary prime powers. The square with binary twist1_{y=x+1} has the displayed full transversal, preventing an overstatement that all affine projections lack mates of every kind. Half-order subsquare and group-table obstructions, proper-block PBD counting, and the44-orbit equivalence all pass. The44-row representative binary array has index11; its484-row developed binary array has index121. With the first field coordinate normalized to0, B's orbit conditions recover A's common-translation ansatz. The unrestricted four-MOLS target stays open.

**HN-B:** all three partial results pass. The packing uses OPEN caps, preserving the strict cross-copy inequalities. Finite translated subsets give an actual fractional colouring, and no ordinary5-colouring follows. The prime-power additive maps work at p=2 and3; tensor multiplication is an isomorphism by surjectivity and equal free ranks, and the product maps are Z-multilinear. For N=1 use Z→F3. Edge-path displacement is the actual complex difference, so there is no path choice ambiguity. The cyclotomic-integer corollary excludes denominators. Length-two counts, the extreme-vertex semicircle restriction, parity at13 and the regular-hexagon equality classification all pass, including arbitrary unit-distance subgraphs. There is no six-chromatic witness or unrestricted plane-colouring improvement.


## Adversarial verdict SP-B / RAM-B

Referee ref_probe_b1 completed both additional audits, with root checking their algebra separately. This finishes mathematical review of the first14 completed clean-room probes.

SP-B's positive-set reduction, dyadic8L baseline, exact W/C collision inequality, conditional401/300 exponent, progression band count and explicit four-ray collision count PASS. The factor32 follows from W≥qk tau²/8 and E_j≤4q tau²; all subsequent powers and logarithmic losses check. Two scope clarifications: the K=√N progression class is not proved to satisfy the EXACT threshold E_j≥E/L, so it refutes only the unrestricted comparable-richness collision claim, not a statement with that additional threshold. The small-product hypothesis(H) remains unproved and is not refuted by the example. Restrict the formal exponent consistency model to4/3≤alpha≤2 when including the elementary S,P,q≤N² and r≥1 constraints; alpha=135/101 lies in this range. No universal frontier gain follows.

RAM-B's density-drop certificate, all explicit ratio arithmetic and onset1152, and its equal-part counterexample PASS. The process's absence of monochromatic cliques is essential to termination in a density drop; the counterexample appropriately does not impose that absence. The truncated cosine construction, monotone envelope J, fixed-width true-Ramsey extension Q, ceiling/maximum operations and eventual diagonal value ceil(epsilon C^k) all PASS. In particular, the cosine support boundary uses cos(6theta)=0, and reducing a smaller coordinate outside Q's fixed-width strip leaves its value unchanged. The array is synthetic and does not constrain all graph-specific arguments. Neither density recovery nor an improved Ramsey base is proved.

No additional novelty clearance is assigned to these two outputs. SP-B's angular clustering and collision-count structure is in the same established family as the Konyagin–Shkredov mechanism compared for SP-A. Its explicit hypothesis is a reduction, not a new unconditional theorem at exponent401/300. RAM-B's exact auxiliary formulations were not located in the bounded comparison, but their novelty remains uncleared and no new record follows.


## Completed second probe SQ-B (adversarial audit pending)

Target and eventual version OPEN; no new finite range. Reported reasoning11:48:27–12:03:31,15m04s, no external sources, files or computations.

Put N=n²+2n, I_n={n²+1,...,N}. The exact count of members with Ω≤2 is
C(n)=π(N)−π(n²)+Σ_{p≤n prime}[π(N/p)−π(n²/p)].
An interval member cannot be a square. Every semiprime therefore has distinct prime factors p≤n<q; its smaller prime is unique. This proves the formula, identical to A's count. Distinct-prime counting alone is insufficient:32 lies in(25,36) but has Ω=5.

Let J1=(n²,N],J_p=(n²/p,N/p] for primes p≤n, and U_n their union. The target is exactly the existence of a prime in U_n for every n. For n≥4 these real half-open intervals are pairwise disjoint: for p<r, N/r≤n²/p iff2p≤n(r−p). Except(2,3), prime gaps are≥2 and n(r−p)≥2n>2p; the exceptional pair needs n≥4. Also N/2≤n² for n≥2 separates J1. Thus C(n) counts distinct primes in U_n and the total real length is2n(1+Σ_{p≤n prime}1/p). Distinct semiprime witnesses then have distinct larger factors; n=3 is an exception because10 and15 share5. The Ω≤3 frontier is equivalent to U_n containing an INTEGER of Ω≤2: divide a composite interval witness by its smallest prime p≤n, or retain a prime witness in J1; conversely multiply a witness in J_p by p. Neither union length nor this translation proves that U_n contains a prime.

A balanced sufficient condition is: integerd≥1,d²≤2n, with both n+1−d and n+1+d prime. Their product=(n+1)²−d² is strictly in the interval and has Ω=2. Conversely this characterizes the semiprime witnesses with factor sum2n+2: the two distinct primes must both be odd and d=(q−p)/2 is integral. This restricted condition fails at n=6: d=1,2,3 give(6,8),(5,9),(4,10), whereas38=2*19 is a valid unrestricted witness.

For any fixed finite family of nonconstant integer polynomials f_j and integerK≥1, there is an arithmetic progression of positive n on which every nonzero f_j(n) has at leastK DISTINCT prime factors. Elementary proof: given any polynomialF and finite forbidden prime setS, choose a with A=F(a)≠0 and M=product(S). Then H(t)=F(a+AMt)/A is a nonconstant integer polynomial congruent to1 moduloM. Take |H(t)|>1; any prime divisor lies outsideS and divides a nonzero value ofF. Repeating this suppliesK prime divisors for eachf_j, all distinct across indices, and corresponding roots modulo those primes. CRT imposes all these root congruences simultaneously. Only finitely many integer zeros need removal. This rules out any fixed finite polynomial witness list at K=3, not all n-dependent constructions.

The integer polynomials lying strictly between n² and(n+1)² for all sufficiently largen are exactly f(n)=n²+bn+c with either b=0,c≥1; b=1,c arbitraryinteger; or b=2,c≤0. Indeed0<f(n)−n²<2n+1 forces degree≤1, then0≤b≤2 and the endpoint restrictions; each listed case fits eventually. In particular, for every FIXED H there are arbitrarily largen on which all n²+j and(n+1)²−j,1≤j≤H, have Ω≥3. H is fixed before the progression is chosen; this is not a counterexample for the entire interval of growing length2n.


## Completed second probe SD-B (adversarial audit pending)

Both universal upper targets OPEN. Reported reasoning11:50:58–12:07:43,16m45s. Natural logarithms below; ratios are base-independent. No files, sources, computations or other agents.

**Exact integer reduction.** Every finite-support real joint pair has an integer-valued counterpart preserving the entropies of X,Y,X+Y,X+2Y,X−Y exactly. Take the finite-dimensional Q-span of all coordinate values and a rational basis. Let F contain every value of the five forms. An integer vector outside the finitely many proper rational hyperplanes determined by differences u−v, u≠v inF, defines a Q-linear functional injective onF. Clear denominators. Applying it to X,Y preserves each linear formula and every projection's probability multiset. This is finite-support encoding, not a globally injective R→Z map.

For either controlled family L3={x,y,x+y} or L4={x,y,x+y,x+2y}, and D=x−y, the universal entropy inequality HD≤c max_L HL is equivalent to |G|≤(max_L|L(G)|)^c for finite G⊂Z² on which D is injective. Uniform G proves entropy⇒cardinality (in the intended nonnegative-c range). Conversely encode supports into integers, choose rational joint types q_n→p with denominatorn, and let T_n be the joint type class. Projection L(T_n) has at most exp(n H_qn(L)) elements. Every sequence of the induced D-type lifts to T_n by assigning the required joint-atom counts within each difference class, so |D(T_n)|≥(n+1)^(−|suppD|)exp(nH_qn(D)). Choose one element per D-sequence. Encode vectors by Σv_j B^(j−1), where integerB>2M+1 and M bounds all absolute coordinate/projection values. Signed-digit uniqueness makes this injective on all relevant finite vector sets, and it commutes with integer forms. The resulting planar integer set has injectiveD. Apply the cardinality inequality, take logs/n and letn→∞. A global multiplicative constant in the cardinality bound contributes onlyO(1/n). The producer stated equivalence for every fixed realc; outside c≥1 both universal statements fail using a nontrivial X with Y=0, so that case can be settled separately without multiplying inequalities by a negative number.

**Independent-pair upper bound.** For independent X,Y, HD≤(3/2)H(X+Y). Proof: if Z is independent of(A,C), put U=A−Z,V=Z−C,W=A−C=U+V. Conditional onW, A andZ remain independent; hence H(U|W)≥H(U|A,W)=HZ. Thus H(A−C)≤H(A−Z)+H(Z−C)−HZ. For independent A,B,C, data processing C→B+C→A+B+C gives H(A+B+C)+HB≤H(A+B)+H(B+C). Now take Y' an independent copy ofY, also independent ofX, and a=HX,b=HY,s=H(X+Y),d=H(X−Y). The first inequality with Z=−Y' gives d≤s+H(Y+Y')−b. The second and entropy monotonicity under independent addition give H(Y+Y')≤H(X+Y+Y')≤2s−a. Therefore d≤3s−a−b, while d≤a+b; adding yields2d≤3s. This is not the arbitrary dependent-pair target.

**Exact ≤3-atom constants.** For the three controlled projections, restricting the JOINT support to at most3 gives optimalc=log3/h2(1/3)=log27/log(27/4). The uniform support{(0,0),(1,0),(0,1)} attains it. For the upper bound, an injective controlled projection dominatesHD. Otherwise each projection has a2+1 partition and their collision pairs must differ because any two forms determine a point. Their entropies are h2(p1),h2(p2),h2(p3). If pmax≤1/2, the maximum is≥h2(1/3) and joint entropy≤log3. If pmax≥1/2, the maximum equals h2(pmax), and Hjoint≤h2(pmax)+(1−pmax)log2≤(3/2)h2(pmax), using h2(t)≥2(1−t)log2 on[1/2,1]. Smaller supports are covered by the injective-projection case. For four distinct controlled forms and≤3 atoms, at least one is injective, since there are only3 pairs and two forms cannot share a collision pair. The optimal constant is1; attainment follows from nonconstantX,Y=0.

**Five-atom four-projection lower obstruction.** Assign7/32 each to(0,2),(2,0),(0,1),(2,1), and1/8 to(1,1). Differences are distinct. Write
a=(31/8)log2−(7/8)log7,
b=(71/16)log2−(7/16)log7−(9/8)log3,
d=(19/4)log2−(7/8)log7.
Then HX=H(X+2Y)=a,HY=H(X+Y)=b,HD=d. Direct probability multisets give these formulas. Also b−a=(1/16)log(2^9*7^7/3^18)>0 because421654016>387420489, and5d−8b=(1/8)log(3^72/(2^94*7^7))>0. For the latter,3^12>(9/4)*2^15*7; raise to the sixth power and use(9/4)^6>112. Thus the unrestricted four-projection constant must exceed8/5. This is weaker than the located current lower claim1.6747338950414058 and is not a new record. The three-point lower ratio≈1.726 is likewise below the located three-projection lower claim1.77898884. Those stronger live lower claims remain unreplayed, as stated at the status gate.


SD-B post-probe source comparison: the independent-pair inequality is a known corollary of [Tao, Shannon-entropy sumset theory, equation(23)](https://arxiv.org/pdf/0906.4387): replace Y by−Y in the stated sum-difference inequality and combine with H(X−Y)≤H(X)+H(Y). The arithmetic finite-support encoding is also consistent with that paper's Freiman-isomorphism discussion. This does not supply an improvement for dependent pairs. No novelty clearance is assigned to the exact small-support optimizations; their lower examples do not exceed the located records.


## Adversarial verdict SQ-B / SD-B

The ordinary adversarial reviewer ref_probe_b1 independently checked both complete derivations and returned **PASS**. This is same-vendor mathematical review, not cross-vendor review, executed large finite verification, or kernel formalization.

For SQ-B, the exact prime-count identity, half-open interval disjointness for n≥4, equivalence with an Ω≤2 integer in the prime union, balanced-factor characterization, simultaneous Schur–CRT argument, and classification of eventually admissible fixed integer polynomials all pass. At n=4 two intervals may touch at an excluded/included endpoint without sharing an integer. The CRT result concerns fixed finite polynomial lists; it does not obstruct searching the whole growing interval.

For SD-B, exact integer encoding of the five forms, the entropy/cardinality equivalence (including the trivial c<1 case), independent-pair 3/2 bound, constants on at most three joint atoms, and five-atom ratio greater than 8/5 all pass. One explanatory addition to the small-support argument: if a controlled projection is constant, another linearly independent controlled projection is injective on the joint support. The independent-pair bound is a known corollary of Tao's sum-difference entropy inequality, as recorded above. Neither probe improves its unrestricted target.

## Completed second probe POW-B (adversarial audit pending)

**OPEN** for every all-n target k≤85. Fresh producer probe_pow_b reports active reasoning/checking from 11:57:50 to 12:13:19 UTC, 15m29s, with no files, sources, shell, solvers or external computations. The finite range below is an analytic theorem, not an executed prime search.

### Self-contained prime-interval lemma

For every real x≥2^80, there is a prime x<p≤ρx, where ρ=4801/4000.

Write L(x)=log(floor(x)!), ψ(x)=Σ_{p^r≤x}log p, θ(x)=Σ_{p≤x}log p, and F(x)=x log x−x with F(0)=0. Integral comparison gives
|L(x)−F(x)|≤1+log_+x for every x≥0:
for integers m≥1, F(m)+1≤log(m!)≤F(m)+1+log m; for m≤x<m+1, 0≤F(x)−F(m)≤log x; for 0<x<1, |F(x)|≤1.

Set
g(t)=floor t−floor(t/2)−floor(t/3)−floor(t/5)+floor(t/30).
It is 30-periodic and takes value 1 on unit intervals with integer part modulo30 in
{1,2,3,4,5,7,8,9,11,13,14,17,19,23,29}, and 0 on the others. This follows from
g(j)−g(j−1)=1−1_{2|j}−1_{3|j}−1_{5|j}+1_{30|j}.
Thus 0≤g≤1, with g=1 on [1,6). For
Φ(x)=L(x)−L(x/2)−L(x/3)−L(x/5)+L(x/30)
prime factorization gives
Φ(x)=Σ_{p^r≤x}g(x/p^r)log p,
hence ψ(x)−ψ(x/6)≤Φ(x)≤ψ(x).

Put
a=(log2)/2+(log3)/3+(log5)/5−(log30)/30
=(7/15)log2+(3/10)log3+(1/6)log5
>(11/10)log2>1/2.
Cancellation in F gives |Φ(x)−ax|≤5(1+log x), x≥1.
Iteration until x/6^J<1 uses J=floor(log x/log6)+1≤1+log x and proves
ax−5(1+log x)≤ψ(x)≤(6/5)ax+5(1+log x)^2.
Also 0≤ψ(x)−θ(x)≤sqrt(x)log x, because each prime p≤sqrt(x) contributes at most log x through its powers of exponent≥2.

For y=ρx and H=log x, it follows that
θ(y)−θ(x)≥ax/4000−5(1+log y)−sqrt(y)log y−5(1+H)^2.
For x≥2^80, H≥1, log y<H+1, sqrt(y)<2sqrt(x), so the error is less than
15H+4sqrt(x)H+20H^2.
For x≥2^16, log x≤x^(1/4), by checking the boundary with log2<1 and then the derivative. The error is therefore at most 39x^(3/4). Thus
θ(y)−θ(x)>x/8000−39x^(3/4)>0,
since x^(1/4)≥2^20>312000. This proves the lemma, including its explicit real onset.

### Exact finite range for the target k=85

For every integer 1≤n≤465 there is a prime n^85<p<(n+1)^85. For n=1 take 2. For 2≤n≤465, x=n^85≥2^85, and monotonicity plus the first four binomial terms give
(1+1/n)^85≥(1+1/465)^85
>1+85/465+3570/465^2+98770/465^3>4801/4000.
The final rational inequality is certified by the exact identity
4000(85·465^2+3570·465+98770)−801·465^3=15535375>0.
The lemma's prime is therefore strictly within the required power interval.

### Exact completion bridge

If a forward short-interval theorem is supplied with explicit A>0, X≥1, θ<84/85 and
∀x≥X ∃ prime p: x<p≤x+Ax^θ,
then putting δ=84−85θ>0 and
N=ceil(max{1,X^(1/85),(A/85)^(1/δ)})
proves the k=85 target for all integers n≥N, because
An^(85θ)≤85n^84<(n+1)^85−n^85.
Together with the proved segment, this completes the target if N≤466; otherwise precisely the finite gap 466≤n<N remains. At θ=84/85 the same implication holds if A≤85; A>85 cannot be substituted without further work because the normalized gap tends to85. A backward interval with length85y^(84/85), evaluated at y=(n+1)^85, is longer than the target interval, so does not give that containment.

No such sufficiently effective input is established in this probe. Without it, the target is unresolved for n≥466.

### Interval-transfer obstructions

No integer m≥1 has
n^85≤m^86<(m+1)^86≤(n+1)^85,
since this would imply 1≤(n+1)^(85/86)−n^(85/86)<1 by the mean value theorem.

The abstract integer set
S={j∈Z:j≥2 and j∉(A,B)}, A=1000^85, B=1001^85,
misses one k=85 interval while meeting every k≥86 interval and every Bertrand interval (m,2m), m≥2.
For the first assertion, if both interior endpoint integers m^k+1 and (m+1)^k−1 were in the hole, integrality would give A≤m^k and (m+1)^k≤B, contradicting concavity with exponent85/k<1. For the second, B<2A follows from 85log(1001/1000)<.085<.5<log2. If m<A or m≥B choose m+1; if A≤m<B choose B. This concerns the logical information in interval coverage, not a counterexample involving actual primes.

### Root assessment

The self-contained finite proof and containment obstruction appear correct, pending the adversarial verdict. The finite coverage is weaker than POW-A's independently checked 7,980,000,000 range using Dusart's primary-source theorem; POW-B's additional value is that its proof needs no quoted prime-distribution estimate. Its elementary factorial argument is not asserted new. No all-n numerical frontier is moved.


## Completed second probe LIN-B (adversarial audit pending)

**OPEN**: no fixed unconditional L<3.99. Fresh producer probe_lin_b reports active reasoning12:05:36–12:20:43 UTC (15m07s), clock/coordinator messaging only, no files, web, experiments, solvers, other agents or dependencies. It treated the supplied October2 frontier as an unverified premise. The following retains all substantive proof content.

### Uniform removal of prime powers above exponent one

Let ψ(x;q,a)=Σ_{n≤x,n≡a(q)}Λ(n), θ(x;q,a)=Σ_{p≤x,p≡a(q)}log p, and R=ψ−θ. For each fixed δ>0, let η=min(δ,1)/4. There is effectively computable Cδ such that, for all sufficiently large q, all reduced a mod q and all real x≥q^(1+δ),
R(x;q,a)≤Cδ(x/q)q^(−η)(log q)^2.
In particular R=oδ(x/q) uniformly over this entire range.

Here is an elementary proof, retaining explicit estimates used by the producer. If r_k(a;q) counts roots u^k≡a mod q, then
r_k(a;q)≤k^(ω(q)+2).
For p^e||q put s=v_p(k). There are at most k roots mod p. If e≤2s+1 they have at most kp^(2s) lifts. If e>2s+1, split roots by their residues modulo p^(s+1), at most kp^s groups. Two roots in a group have t=v_p(v−u)≥s+1. Unless identical mod p^e, the binomial expansion has linear valuation s+t, with every subsequent term at least2t>s+t, so e≤s+t. A group therefore contains at most p^s roots modulo p^e. CRT gives
r_k≤k^ω(q)∏_{p|q}p^(2v_p(k))≤k^(ω(q)+2).
For every fixed ε>0,
k^ω(q)≤k^floor(k^(1/ε))q^ε,
by splitting prime divisors at k^(1/ε).

Choose K=max(2,ceil(2/δ)). For 2≤k≤K, counting integers in each root class and bounding their weights by log x yields
R_≤K≪δ q^η log x (sqrt(x)/q+1).
Discarding the congruence and primality at k>K gives
R_>K≤(log x)^2 x^(1/(K+1))/log2.
After multiplying by q/x, the functions of x decrease for sufficiently large q on x≥q^(1+δ). Evaluation at the endpoint gives
(q/x)R≪δ(log q)^2[
q^(η−(1+δ)/2)+q^(η−δ)+q^(−(δK−1)/(K+1))].
All three exponents are at most−η. For the third when δ≤1,
(δK−1)/(K+1)≥1/(K+1)≥δ/(2+2δ)≥δ/4;
when δ≥1, K=2 and the exponent's positive magnitude is at least1/3.
This proves the bound.

Consequently, at x=q^L for fixed L>1, any uniform lower bound
ψ(x;q,a)≥c(x/q)q^(−ρ),
with 0≤ρ<min(L−1,1)/4, ensures a prime for all large q. Removing prime powers does not itself impose exponent2.

### Elementary principal mass

The central binomial coefficient satisfies binom(2n,n)≥4^n/(2n+1). Its p-adic valuation is
Σ_j[floor(2n/p^j)−2floor(n/p^j)]≤floor(log(2n)/log p).
Thus log binom(2n,n)≤ψ(2n). Taking n=floor(x/2) yields
ψ(x)≥(x−2)log2−log(x+1).
As ψ−θ≤sqrt(x)log x,
θ(x)≥(x−2)log2−log(x+1)−sqrt(x)log x.
Removing primes dividing q loses at most log q. Hence at x=q^L, fixed L>1, both the principal prime mass and principal von Mangoldt mass over units are at least x/2 for sufficiently large q.

### Sharp finite Fourier support criterion

For G=(Z/qZ)^×, N=φ(q), q≥3, let nonnegative weights t_a have Fourier coefficients
Tχ=Σ_a t_aχ(a), M=Tχ0>0, E=Σ_χ≠χ0 |Tχ|².
If B classes have zero weight, then
B≤NE/(M²+E).
Indeed Parseval gives Σ_a t_a²=(M²+E)/N and Cauchy on the N−B occupied classes gives M²≤(N−B)(M²+E)/N.
Either
Σ_χ≠χ0 |Tχ|<M
or E<M²/(N−1)
therefore ensures full support; the first follows directly from Fourier inversion at a missing class.
These universal sufficient thresholds are sharp: assign zero at a0 and M/(N−1) elsewhere, giving
Tχ=−Mχ(a0)/(N−1)
for nonprincipal χ. This is an abstract weight example, not an assertion about primes.

For Ψχ(x)=Σ_n≤x Λ(n)χ(n), M=Ψχ0, Eψ=Σ_χ≠χ0 |Ψχ|², Rmax=max_a R(x;q,a), a prime-free class and M>NRmax imply
Eψ≥(M−NRmax)²/(N−1)
by Fourier inversion and Cauchy. At x=q^L, L>1, the preceding results show that
Eψ=o(x²/q)
is sufficient for primes in every reduced class. An estimate
Eψ(q,x)≤Cq^α x^β(log(qx))^B, β<2,
would give this whenever L>(α+1)/(2−β). Such an estimate at a fixed
max(1,(α+1)/(2−β))<L<3.99
would settle the target. No such estimate is proved. The sufficient second-moment condition may be much stronger than prime existence, especially in the exceptional-real-character case.

### Exceptional real character reduction

Fix 1<L<3.99 and x=q^L. Either of the following alternatives, if proved uniformly for every sufficiently large q, would suffice.

Regular alternative:
|Ψχ0(x)−x|+Σ_χ≠χ0 |Ψχ(x)|≤x/2.

Exceptional alternative: there exist a real nonprincipal χ* and β∈[1/2,1) such that, putting D=x−x^β/β,
|Ψχ0(x)−x|+|Ψχ*(x)+x^β/β|+
Σ_χ∉{χ0,χ*}|Ψχ(x)|≤D/2,
and for every ρ>0, 1−β≥cρq^(−ρ), cρ>0 independent of q.

If β is an actual exceptional real Dirichlet zero, the last input is the recalled, ineffective Siegel lower bound. This is the sole non-elementary recalled dependency in this reduction; no effective constants or onset are supplied. A conductor bound for d|q implies the stated q-bound.

In the regular case, inversion gives ψ(x;q,a)≥x/(2N), from which the prime-power lemma removes R. In the exceptional case χ*(a)∈{−1,1} gives
Nψ(x;q,a)≥x−χ*(a)x^β/β−D/2≥D/2.
For h=1−β∈(0,1/2], −log(1−h)≤2h. If log x≥4, then
x^β/(βx)≤exp(−h(log x−2))≤exp(−h log x/2).
Using 1−e^(−t/2)≥(1/4)min(t,1), t≥0, gives
D≥(x/4)min((1−β)log x,1).
Take δ=L−1, η=min(δ,1)/4 and ρ=η/2. For large q, cρq^(−ρ)log x≤1, so
D≥(cρ/4)xq^(−ρ)log x,
ψ(x;q,a)≥(cρ/8)(x/q)q^(−ρ)log x.
The prime-power error is smaller by O_L(q^(−(η−ρ))log q)=o(1). Thus every reduced class contains a prime. The resulting onset may be ineffective. The conclusion P(a,q)≤q^L gives the strict requested inequality after a fixed arbitrarily small exponent increase remaining below3.99.

No proof of the regular/exceptional alternatives at any L<3.99 is supplied. An o(x) error alone is insufficient in the exceptional case when D=o(x).

### Abstract density/repulsion bookkeeping

Suppose a positive weighted multiset (λ_j,w_j) satisfies λ_j≥R and
N(t)=Σ_λj≤t w_j≤Be^(At).
Assume B>0 and L>max(A,0). Tonelli yields
Σ_j w_j e^(−Lλ_j)
=L∫_R^∞e^(−Lt)N(t)dt
≤[BL/(L−A)]e^(−(L−A)R).
If c>0, u>0 and R≥c log(1/u)−d, this is at most
[BL/(L−A)]e^((L−A)d)u^(c(L−A)).
It is o(u) as u→0 when c(L−A)>1, giving the model threshold A+1/c. No valid Dirichlet zero-density/repulsion parameters or required explicit-formula errors are proved here, so this is conditional bookkeeping only.

### Two shortcut obstructions

No uniform linear bound P(a,q)≤Cq is possible. Fix m and choose distinct primes ℓ1,…,ℓm>m. CRT gives arbitrarily large q with
q≡−k^(−1) mod ℓk, 1≤k≤m.
For q>maxℓk, each 1+kq is a proper multiple of ℓk, hence P(1,q)>1+mq. Taking m>C proves the claim. This is no obstruction near3.99.

Finally, writing M(q)=max_(a,q)=1 P(a,q), the target is equivalent to
limsup_(q→∞) log M(q)/log q<3.99.
The supplied frontier gives only a non-strict upper bound3.99. Abstract functions q^3.99/log q illustrate the missing margin, not a counterexample concerning actual primes.

### Root assessment

No exponent was improved. The uniform unweighted prime-power removal independently complements LIN-A's reciprocal-weighted removal, while the exceptional-zero reduction states the real relative-error requirement. Its overall framework is standard Linnik theory, not a claimed new proof. Exact local estimates have uncleared novelty. Full claims await the ordinary adversarial review.


## Adversarial verdict POW-B / LIN-B

Ordinary reviewer ref_probe_b1 returned detailed **PASS** verdicts after independent mathematical checks. These are same-vendor reviews; no external mathematical or kernel certification is claimed.

**POW-B:** the real-x factorial error, all15 residues of g, half-open [1,6) interval, geometric ψ iteration, prime-power remainder, and numerical margins all pass. The lemma holds for every real x≥2^80. The exact binomial numerator15535375 is correct, and the finite target coverage is strictly within both endpoints. The effective bridge, its boundary coefficient case, backward-interval warning, concavity and abstract set are correct. No mathematical repair was needed. This is an analytic proof through465, not an all-n improvement or an executed prime search.

**LIN-B:** local prime-power lifting, the bound k^(ω(q)+2), low/high-power counts and all exponent comparisons pass, including uniformity throughout the unbounded real range x≥q^(1+δ). The Fourier criteria are sharp universal sufficient criteria and are not necessary criteria for prime existence. Exceptional inversion, the relative deficit bound, Siegel conductor-to-modulus transfer and prime-power error comparison pass. The implied onset can be ineffective, as stated.

Two explanatory qualifications are applied. First, removing primes dividing q from θ loses at most log q; the principal Ψ lower bound follows by domination of this unit-prime mass, not by claiming that removing every prime power dividing q also costs only log q. Second, the abstract Laplace calculation requires L>max(A,0), B>0 and c>0, with u→0+. These are now explicit in its statement. They hold in the intended positive-exponent application. The CRT linear-bound obstruction and limsup equivalence pass. No numerical exponent improvement follows without the missing analytic estimate.

## Final freshness checkpoint, 2026-10-02 12:29 UTC

The [current Hou–Zhao arXiv entry](https://arxiv.org/abs/2607.01169) still identifies v3, revised September4, as the latest version. Public read-only retrieval of the [q2 README](https://raw.githubusercontent.com/wustep/maths/main/problems/sidon-second-term/compute/q2/README.md) and [its path-specific commit history](https://api.github.com/repos/wustep/maths/commits?path=problems/sidon-second-term/compute/q2/README.md&per_page=1) still gives .943006169985179 at commit da2440b68979b78d201182118d30ca418e3c2001, August27 07:16:18UTC. This rechecks the record metadata, not its certificate.

[Linnik PR205](https://github.com/teorth/optimizationproblems/pull/205), checked through its public API at12:29:18UTC, remains open/unmerged, last updated07:17:56UTC, with zero comments and zero review comments. This is metadata about review status, not evidence that the theorem is true or false. Other candidate baselines have the dated October2 primary-source checks recorded above. Repeated broad Sidon keyword searches produced irrelevant hits and did not expand the novelty clearance; the substantive comparison remains the located primary paper/repository and the bounded searches already documented.

## Completion, measured scope and cost

All18 required fresh mathematical probes completed, two for each of nine families. Each positive claim and obstruction was subsequently checked by an ordinary adversarial reviewer; final assessments include every scope repair, not merely the producers' self-evaluations. The task's ranking, two best complete originals, source comparison and bounded campaign recommendation are provided above.

The reported clock intervals sum to142m37s for the nine A probes and144m43s for the nine B probes, total **287m20s (4h47m20s)**. The intervals are producer-reported clock-call intervals, not independently measured active CPU time. They range from14m58s to17m53s, consistent with the requested approximately15–25minute attempts. Writeup, archival, status scouting, root work and refereeing are not included in that sum. Peak capacity was three worker agents plus root. No dollar total or token total is available, so none is estimated.

No SAT solver, prime enumeration, new dependency, paid cloud job, Git commit/push, publication, or external message was performed. The tiny exact BigInt record comparison and metadata/timing arithmetic are distinguished from mathematical certificates; the external q2 certificate was not replayed. No unattended scheduler was recreated or tested. The inbox task is complete; the authorized inbox-polling workflow continues until STOP or a newer owner instruction.
