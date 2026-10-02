DONE — freshness/source audit completed; Zaremba K0 CLEAR within searched scope; #859 artifact and optimization baseline materially CHANGED; no new proof independently certified.

# Freshness sweep, 2026-10-02

All external sources below were accessed on **2026-10-02 UTC**. This is a read-only source/status audit, not a proof referee or kernel replay. The comparison baseline is the 2026-09-26 local campaign/selection record. Dates of events and dates of discovery are distinguished.

## Findings that change the operating picture

| Item | State recorded on 09-26 | State observed today | Consequence |
|---|---|---|---|
| Zaremba explicit prime-denominator constant | Shkredov appendix: M = 2^2000 for sufficiently large primes; Zhang existential general-denominator claim; no certified replacement constant in our work | **CLEAR within the searched scope.** Shkredov remains v2, June 24; Zhang remains v2, May 8. No new numerical M below 2^2000 located. | Continue the explicit-constant gate, preserving its prime/large-denominator scope. This is not an exhaustive novelty certificate. |
| #889 | Lowercase-v1 effective-finiteness note published; level 3 parked; KitaKen1 capital-V1 proof September 22 | **CHANGED administratively:** PR6453 reviewed September 27, documentation response September 28; still open. No newer lowercase-v1 or level-3 result located in inspected sources. | Do not confuse capital V with lowercase v. No basis to resume level 3 or declare a collision absent globally. |
| #708 | Moderator update requested September 25 | **CHANGED/confirmed:** public claim now gives 12n and a Lean link. Main 2n/(2+o(1))n problem remains OPEN. | Requested visibility milestone achieved. No follow-up message needed. |
| #624 | September 25 certified table reply submitted; n=12 unresolved | **Confirmed:** reply publicly visible; no subsequent mathematical reply/new value in the inspected thread. | Keep parked. N_L(4) remains only 11 ≤ N_L(4) ≤ 15 in that thread. No solver run. |
| #859 | Campaign closed as subsumed by Hughes; original asymptotic considered open | **CHANGED knowledge:** September 27 site claim; current conjectures.io artifact claims a *disproof*, certified September 23. Site summary and its linked elementary contribution do not match that claim. Hughes remains v1. | Preserve closure; flag the previously missed artifact and source discrepancy. Do not certify the disproof without separate exact-target/kernel review. |
| AI/optimization landscape | C3b lower 1.77898884; C3c lower 1.67473389502, both attributed to Mosaic | **CHANGED:** C3b explicitly unverified; C3c now 1.6747338950414058, attributed to Lin. New C3a, sunflower and Linnik claims. | Correct the selection baseline; inspect the new claims before launching related work. Neither C3b nor C3c upper bound improved in these records. |

## 1. Zaremba K0 and supporting source versions

- [Shkredov arXiv record](https://arxiv.org/abs/2603.14116): v1 March 14, v2 June 24, 2026; no v3 listed. The [current HTML appendix](https://arxiv.org/html/2603.14116v2), equation (158), still states M = 2^2000. Its large-prime qualification is essential. The [author's arXiv list](https://arxiv.org/a/shkredov_i_1.html) has this as its latest listed article, with the appendix described in the revision comments.
- [Zhang arXiv record](https://arxiv.org/abs/2605.02518): v2 May 8, 2026, no v3 listed. [Theorem 1.2 and Remark 1.3](https://arxiv.org/html/2605.02518v2) claim general Zaremba with an effectively computable but large unspecified bound; they do not supply a numerical constant below our target. An internal HTML date is not evidence of an additional arXiv version. This sweep did not independently audit that proof.
- [Date-filtered arXiv search](https://arxiv.org/search/advanced?advanced=&terms-0-operator=AND&terms-0-term=Zaremba&terms-0-field=all&classification-include_cross_list=include&date-filter_by=date_range&date-from_date=2026-09-20&date-to_date=2026-10-02&date-date_type=submitted_date&abstracts=show&size=50&order=-announced_date_first) returned one item, 2610.01487, on the Zaremba–Jaumann rate in continuum mechanics, unrelated to continued fractions. Separate indexed searches for the paper identifier, new explicit constants, and explicit SL2 spectral gaps did not locate a relevant new result.
- [Google Scholar citing-record query](https://scholar.google.com/scholar?cites=6755870018850554900&as_sdt=5,50&scipsc=1&hl=en) returned two citing items: Zhang and Shkredov's Littlewood exceptional-set paper. Neither is a new September 26–October 2 explicit-Zaremba improvement. Scholar's page contained a generic feature-error banner but did return these results; citation coverage is incomplete by nature.
- [Princeton October 13 seminar announcement](https://www.math.princeton.edu/events/zarembas-conjecture-and-korobovs-optimal-coefficients-2026-10-13t203000) is a future talk, not an additional numerical theorem.
- Supporting sources rechecked: [Blomer–Pascadi 2607.24311](https://arxiv.org/abs/2607.24311), v1 July 27; [Moshchevitin–Murphy–Shkredov 2212.14646](https://arxiv.org/abs/2212.14646), v1 December 30, 2022; [Pascadi 2511.08445](https://arxiv.org/abs/2511.08445), v2 June 21, 2026; [FKMS 2511.09459](https://arxiv.org/abs/2511.09459), v3 March 11, 2026; [1905.00291](https://arxiv.org/abs/1905.00291), v1 May 1, 2019. No later versions shown. Shkredov's [homepage](https://www.math.purdue.edu/~ishkredo/) now lists the MMS paper in IMRN 2026, issue 6; journal publication is not a new numerical bound.
- Source precision: [1812.01671](https://arxiv.org/abs/1812.01671) remains v3 February 26, 2019. Its abstract metadata says exponent 1/21, whereas [the current PDF, Theorem 2](https://arxiv.org/pdf/1812.01671), and HTML give 1/20. This is an existing metadata/text discrepancy, not evidence of a new downgrade. The symmetric-generating-set hypotheses, sufficiently-large-set threshold and implicit coefficient still matter for using that theorem.

**K0 verdict: CLEAR, scoped to these searches and records.** No priority claim follows. No new AI-lab Zaremba theorem has been verified by this sweep.

## 2. Erdős #889: the variant distinction persists

The [main page](https://www.erdosproblems.com/889) remains OPEN, last edited January 2, 2026, with two comments, zero proof claims, and no currently-working/formalising reaction. The [discussion](https://www.erdosproblems.com/forum/discuss/889) still contains Kitamura's September 22 capital-V1 announcement and Luccioli's January 3 reduction. The [proof-claims page](https://www.erdosproblems.com/forum/thread/889/proof-claims) is empty; this establishes only its current contents, not novelty.

[PR6453](https://github.com/google-deepmind/formal-conjectures/pull/6453) was created September 22 03:29:58 UTC and is **open, unmerged**. The [review](https://api.github.com/repos/google-deepmind/formal-conjectures/pulls/6453/reviews) on September 27 12:37:16 requested explanatory documentation and a proof-repository link. The [September 28 02:13:50 response](https://api.github.com/repos/google-deepmind/formal-conjectures/issues/6453/comments) says that documentation was added. This activity is not a new lowercase-v1 theorem or completed proof review. The PR explicitly leaves lowercase-v1 finiteness, the main divergence question and the largest-capital-exception prediction open.

The [capital-V1 proof repository](https://github.com/KitaKen1/erdos-889-capital-v1-finite) remains at commit `44d38dd7f618dbaa0b08fb976c0378b4897021cd` dated September 22 03:15:33 UTC. Its kernel/axiom assertions are the author's verification record; we did not rerun Lean. Both pages of the [public repository inventory](https://api.github.com/users/KitaKen1/repos?per_page=100&sort=pushed) were inspected (100 + 16 repositories); the second page starts June 21. No newly pushed repository identified as lowercase-v1 or level-3 work was located. This does not rule out private work or work under an unrelated name.

The [current formal-conjectures file](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/889.lean) still has open/sorry placeholders for the relevant main and finite-exception statements. Its [latest path commit](https://api.github.com/repos/google-deepmind/formal-conjectures/commits?path=FormalConjectures/ErdosProblems/889.lean&per_page=8) is September 18; KitaKen1's fork main has the same path history. A research-category annotation is not itself a proved theorem.

Exact DOI/name searches located no new citation to our concept DOI. **Zenodo unreachable:** [concept API record](https://zenodo.org/api/records/22962743) returned HTTP403, explicitly citing restricted network traffic; the web reader also failed. Accordingly, current record contents/citation metrics were not verified. Our local v1/v2 publication record is not substituted for a successful remote check.

## 3. Erdős #708: requested update is visible

The [public claim](https://www.erdosproblems.com/forum/thread/708/proof-claims) now states 12n for all n, identifies Lean 4 v4.34.0-rc1 / Mathlib de5ce8a9 and the three standard axioms, and links the [formalisation directory](https://github.com/chy4pro/erdos-708-explicit-upper-bounds/tree/main/lean). It separately labels 11n as unformalised. This verifies that the requested public summary/link is present; it is not a new kernel run.

The claim contains a minor stale-text inconsistency: its main summary names paper v14, but its later concept-DOI note still says “currently v10”. Record this only; no moderator message is authorised or necessary here.

The [main/discussion page](https://www.erdosproblems.com/forum/discuss/708) still marks the original conjecture OPEN, with one comment and one claim. The visible discussion comment is Mazur's May 6 cardinality-wording observation; no new discussion comment was found. No currently-working/formalising reaction is listed; Woett and Jerome remain open to collaboration. Closing our published partial-result work does not close the original conjecture.

## 4. Erdős #624: approved reply, no new value found

The [thread](https://www.erdosproblems.com/forum/discuss/624) publicly shows our September 25 15:12 reply. Its literal all-subsets convention records H_L(9)=H_L(10)=H_L(11)=4, H_L(16)=H_L(17)=5, 11≤N_L(4)≤15, and n=12 undecided. It separately records the original Erdős–Hajnal convention and its different values. The post attributes the checks to programs and describes the certificates; this sweep did not rerun them.

No later response from herong or another participant, and no newer n=12/N_L(4) value, appeared in the retrieved thread. Herong's September 18 expectation N_L(4)=10 remains an older conjectural comment, superseded by the public n=11 witness. Keep the line parked under the no-local-solver instruction.

## 5. Erdős #859: important omitted artifact and conflicting summaries

[Hughes 2609.25446](https://arxiv.org/abs/2609.25446) remains v1 September 21, 2026, with no v2 listed. Its bounds do not by themselves settle the positive-constant asymptotic. The [Erdős page](https://www.erdosproblems.com/859) remains OPEN, zero comments, one proof claim.

The [September 27 13:09:28 claim](https://www.erdosproblems.com/forum/thread/859/proof-claims), posted by Thomas Bloom, describes an affirmative full proof but expressly withholds verification/endorsement. Its formalisation link points to [this contribution](https://github.com/conjectures-io/conjectures-contribution/blob/main/contributions/erdos-859/db9fea06448238039cfd518408bb79ea9b61ccdebadd2d060d3998a8fb30974d/script.lean). Reading its complete 12,383-character source shows a theorem of **positive density for each fixed target**, not the asymptotic conjecture. That link cannot support the forum's full-proof summary.

Separately, the [current conjectures.io problem page](https://conjectures.io/problems/erdos859-erdos-859) reports **Disproved**, linking a different [result and verification record](https://conjectures.io/results/e060355f-a728-4b06-af11-6302b5780d19). The provider dates verification September 18 and certification September 23, credits JenW1N, and reports Lean acceptance with the three standard axioms; its record says a second kernel was not run. Thus this is a previously missed pre-pause artifact, not necessarily a discovery made after September 26. We did not reproduce the provider's build or verification.

The [actual downloadable proof](https://conjectures.io/results/e060355f-a728-4b06-af11-6302b5780d19/solution/download) was accessible: 1,642,075 characters, 36,198 lines. At line 35981 its target is the negation of the named Formal Conjectures proposition, supplied by two density estimates. A text scan found no `sorry`, `axiom`, `native_decide` or `unsafe` tokens; this is **only a static scan, not a transitive-axiom or kernel check**. SHA-256 of the fetched UTF-8 source: `c8011826d105daecca4de0f0a58cc4acd887eafd1a78a9e8c9095c399ca97aea`.

The [September 21 exposition](https://conjectures.io/papers/erdos859.pdf?v=20260921-expanded), attributed to Liam Kruer and Jensen Kohlmeyer, states

\[
\liminf_{t\to\infty}\frac{-\log d_t}{\log\log t}=\delta,
\qquad (\log t)^\delta d_t\longrightarrow0,
\qquad \delta=1-\frac{1+\log\log2}{\log2}.
\]

These two statements would refute every positive-constant logarithmic-power asymptotic: such an asymptotic forces its exponent to equal δ and then forces a positive scaled limit, contradicting zero. **The lower limit must not be silently replaced by a limit.** This sweep checked the target and this implication, not the long estimates. The provider's full artifact, elementary contribution and forum summary have different scopes; a dedicated review would be required before treating the full disproof as independently established.

## 6. Landscape

The parallel agent checked the following primary records independently of the root's items 1–5. These are source checks, not independent proof or certificate reproductions.

| Source/target | Observed change and scope | Implication |
|---|---|---|
| [C3b constant page](https://github.com/teorth/optimizationproblems/blob/main/constants/3b.md) | Upper 11/6 unchanged; lower 1.77898884 remains Mosaic's but now explicitly carries an unverified asterisk. Commit d793db4, September 26 16:58:17 UTC, aligns the page with README. [PR176 discussion](https://github.com/teorth/optimizationproblems/pull/176#issuecomment-5848109776) says no known independent replay of the 13-point certificate; PR closed unmerged. | Carry the unverified qualifier. This is a verification-status change, not a worse numerical bound. |
| [C3c constant page](https://github.com/teorth/optimizationproblems/blob/main/constants/3c.md) | Upper 7/4 unchanged. Lower now **1.6747338950414058**, attributed to **Yongxi Lin**, via [PR185](https://github.com/teorth/optimizationproblems/pull/185), merged September 26 16:51:29 UTC. Original submission September 9; 147 points with rational-weight denominator 10^320. Improvement over Mosaic's value is about 2.06×10^-11. | Update number and attribution. The merge happened during the old session; discovery today does not make the construction new today. |
| Linnik constant | [Naslund preprint 2610.00018v1](https://hexagonmath.org/2610.00018v1) and [PR205](https://github.com/teorth/optimizationproblems/pull/205), opened October 2 07:17:56 UTC, claim P(a,q)<q^3.99 uniformly for coprime a,q and sufficiently large q. PR remains open. | New relevant number-theory claim, not a Zaremba constant. No numerical onset verified. Formal coverage is partial: auxiliary estimates/checker and conditional certificate-to-prime implication, not the entire Linnik theorem. |
| C3a | [Kleinwaks source](https://github.com/kleinwaks/sum-difference) and [PR198](https://github.com/teorth/optimizationproblems/pull/198), September 28, claim C3a≤(13524e−7359)/(9451e−3286)=1.312373302115… and a sum/difference exponent 1.454277448906… for finite subsets of arbitrary abelian groups. Twenty Lean modules, Aristotle/Astra/Sol assistance disclosed; PR open. | Source/formalisation claim not rebuilt here. Not a C3b/C3c upper-bound improvement. |
| Sunflower-free capacity | [Versioned source v1.0](https://github.com/Aspect5/sunflower-free-capacity/tree/v1.0), [PR200](https://github.com/teorth/optimizationproblems/pull/200), September 30: claimed μ3≥1.56178470895053…, 6,127 sets on 20 points plus integer transfer matrix. Open, asterisked; two program checkers claimed, no Lean, review remains same-vendor. | Potential selection input only after certificate/source checks; not cross-vendor or peer-reviewed evidence. |

The [optimization repository commit query](https://api.github.com/repos/teorth/optimizationproblems/commits?since=2026-09-26T00%3A00%3A00Z&per_page=100) returned 19 commits, all September 26, latest `2c1968cd520b60f1cf3cf50749f7285e800e4e15` at 17:07:53 UTC. Newer open PRs must not be read as merged baseline changes.

- **Anthropic:** [October 1 Claude-shaped science](https://www.anthropic.com/research/claude-shaped-science) concerns BootLoops and cross-disciplinary computation, not a Zaremba theorem. The [formal-math repository](https://github.com/anthropics/formal-math) default branch's latest checked commit was September 5 16:38 UTC; September 26 onward query empty. A September 30 repost of an older percolation result is not evidence of new publication.
- **OpenAI/Astra and DeepMind:** bounded searches and the [OpenAI research list](https://openai.com/news/research/) / [DeepMind blog](https://deepmind.google/blog/) yielded no new directly relevant official number-theory/combinatorics announcement in the window. Astra's [Erdős–Sós exposition](https://arxiv.org/abs/2609.32011) was submitted September 25, outside it. No universal absence assertion is made.
- **Star Fleet Math:** the [homepage](https://www.starfleetmath.com/) lists 19 proposed solutions, 13 full and 6 partial, with visible dates July 10–14. No demonstrated September 26–October 2 addition was located. Its Lean assertions were not replayed.
- **VibeMathed:** [dataset](https://vibemathed.com/api/dataset), generated October 2 08:52:38.722 UTC, contained 755 entries. Three precisely dated solveDate entries fall in the window, all September 29 from one Codex/GPT-6-family project: NANUQ full hierarchy labelled unreviewed, and avoidance-population nonuniversality plus ordinal-certificate/pruning results labelled lean-checked/partial. Month-only dates do not support an exact-window count. The aggregator does not itself rebuild proofs or independently check correspondence to informal claims.
- **Tao:** inspected new posts include [September 30 two reports](https://terrytao.wordpress.com/2026/09/30/two-reports/) and the [October 1 arXiv-policy post](https://terrytao.wordpress.com/2026/10/01/arxiv-updates-its-rate-limiting-policy/) (October 2 UTC publication). No new C3b/C3c theorem post was located in that bounded check.

**Decision:** retain the direct Zaremba collision check, correct C3b verification status and C3c attribution/value in future selection decisions, and put Linnik 3.99/C3a on a source-review list before any related campaign. No new campaign is authorised or started by this report.

## Access and operating record

Public Erdős pages initially returned HTTP403 through the web reader but succeeded with ordinary unauthenticated public HTTP GET in Node; no login, credentials or access controls were bypassed. GitHub public APIs, arXiv and the listed conjectures.io pages were reachable. Zenodo remained unreachable as stated above. An IMRN DOI web-reader attempt failed; the author homepage, rather than that failed request, supports the journal-metadata observation.

Global-memory `recall_presets` and its skill were not exposed in the available tools/local skill catalog. No user_notice was returned or invented; no memory preset was changed. Scheduler/worker state was rechecked on resumption and no retired scheduler was restarted. An isolated clean-room producer completed its existing write-up while this priority sweep ran; no further root proof campaign was undertaken during the sweep. A fresh parallel landscape agent was available after that completion; an additional attempted freshness agent was rejected by the platform thread limit.

No external writes/messages, dependency installation, paid cloud, numerical campaign or Lean/SAT execution were performed. API/model monetary costs are not exposed, so no dollar estimate is claimed.
