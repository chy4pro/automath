# N9: K0 collision check and G2 literature sweep (Zaremba explicit M)

Written 2026-09-26T07:25Z (UTC, from `date -u`). Agent: N9 (Phase 0, slot 1). The only file this agent writes is this one.

## 0. Verdict for K0: **CLEAR**

As of 2026-09-26, nothing in print or on arXiv gives an explicit M < 2^2000 for Zaremba with prime denominators. It does not matter whether "all sufficiently large primes" or "all primes" is meant. The only explicit value in print for large primes is still Shkredov's own **M = 2^2000**, arXiv:2603.14116**v2**, Appendix eq. (158). I re-extracted it from the v2 PDF today: "We claim that for sufficiently large q = p one can take (158) M = 2^2000."

- **No v3 of 2603.14116 exists.** The abs page, fetched today, lists [v1] Sat 14 Mar 2026 (98 KB) and [v2] Wed 24 Jun 2026 (68 KB) only. The arXiv OAI record has datestamp 2026-07-10. That is a metadata-only change (comments field, report no. "MPIM-Bonn-2025"), not a new version.
- **Zhang arXiv:2605.02518** has [v1] 4 May 2026 and [v2] 8 May 2026 ("Typos in v1 corrected"), and nothing later. Remark 1.3, verbatim from the v2 PDF: "The bound M in Conjecture 1.1 is effectively computable. The methods in [Shk26] and in this paper would produce a large number. Lowering this bound to 5 or any reasonable magnitude requires a new idea." He gives no number. The arXiv listings contain no Zhang follow-up on Zaremba or SL2(Z/qZ) expansion since then (§2.3).
- **No human group or AI lab has announced an explicit M** anywhere I could reach (§3). The one non-refereed "Zaremba proof" artifact I found, a human–AI GitHub repo, is (i) about A = 5 for all d via a different route, (ii) labelled by its own authors "Proof framework (not complete proof) … 4 gaps remain", and (iii) invalid at a checkable step (§3.1). It does not trigger K0.

Caveats on coverage are in §5. General web search was **unavailable**: this session's WebSearch budget was exhausted (200/200) before N9 started. X/Twitter, Reddit and Google Scholar were not reachable. The arXiv sweep is complete at the metadata level (title, abstract, comments). It does not cover full texts.

---

## 1. Method (what was actually queried)

| channel | query / scope | result |
|---|---|---|
| arXiv full search (all fields, all archives), `arxiv.org/search/?query=Zaremba&searchtype=all&order=-announced_date_first` | 391 results total. I inspected the newest 100, which reach back to 2020. | Every Zaremba-*conjecture* item from 2025–26 is listed in §2.1. The other hits are physics authors named Zaremba, the Zaremba boundary problem, the Hlawka–Zaremba identity, and OpenAI system cards (W. Zaremba as author). |
| arXiv OAI-PMH bulk harvest (`oaipmh.arxiv.org`, metadataPrefix=arXiv, datestamp ≥ 2025-01-01) | sets math.NT, CO, GR, DS, CA, RT, SP (complete). Partial: math.NA, PR; cs.AI (to 2026-06), cs.LO, cs.LG (partial). **98,130 records**, last datestamp 2026-09-25. | regex scans for Zaremba, partial quotient, Korobov, continuant, SL2 × {spectral gap, expansion, energy, growth}, Kloosterman × {bilinear, hyperbola}, BSG, incidence × F_p (§4). |
| arXiv abs pages | 2603.14116, 2605.02518, 2212.14646, 2604.19094, 2604.20812, 2609.27023, 2303.17950, 2305.02228, 2609.05652, 1201.1139 | version histories and comments are quoted below |
| PDFs read (pymupdf text) | 2603.14116v2 (Appendix, §5.4), 2605.02518v2 (§1, §4), 2604.19094 (all Zaremba mentions) | quoted |
| Semantic Scholar citations API | citing papers of 2603.14116, 2605.02518, 2212.14646 | §2.2 |
| OpenAlex | title/abstract search for "Zaremba conjecture", "Zaremba continued fraction", "bounded partial quotients", Russian "гипотеза Зарембы", "Заремба цепные дроби"; author works since 2025-06 for Shkredov, Moshchevitin, Kontorovich, Rudnev | §2 |
| Author pages | Kontorovich (Rutgers research page, full publication list scraped); arXiv author list for Shkredov (`arxiv.org/a/shkredov_i_1`) | §2.3 |
| GitHub | repo search "zaremba"; code search "Zaremba language:Lean"; the file tree of google-deepmind/formal-conjectures (1902 paths) | §3 |
| Hacker News (Algolia API) | "Zaremba", "Zaremba conjecture", "Zaremba's conjecture", "Shkredov", "bounded partial quotients" | §3 |
| Quanta Magazine WP JSON API | search=Zaremba | empty |

---

## 2. Zaremba-conjecture literature 2025–2026 (complete arXiv inventory)

### 2.1 Every arXiv item from 2025–26 whose metadata mentions Zaremba's conjecture

| arXiv | dates | authors | what it proves about M | K0 relevance |
|---|---|---|---|---|
| **2603.14116** | v1 2026-03-14, v2 2026-06-24 | I. D. Shkredov | Thm 8: all sufficiently large q (under a mild condition) have a with all partial quotients ≤ an absolute constant. For primes: **M = 2^2000** (App. (158)). Also O(√log q) bounds and the count Ω(q^{1−O(1/M)}). | This is the record. No v3. |
| **2605.02518** | v1 2026-05-04, v2 2026-05-08 | Xin Zhang | Zaremba for **all q**. It uses a growth/expansion theory in SL2(Z/qZ) plugged into Shkredov's Thm 8 framework. M "effectively computable", no number (Rem. 1.3). | Not explicit. |
| 2604.19094 | v1 2026-04-21 | S. H. Chan, S. Heilman, G. Panova | Uses [Shk26] (cited as "36 pp.", i.e. v1) to show that the number of independent sets of graphs with ≤ D\|V\| edges covers all positive integers, with **D := A + 1**, where A is Shkredov's constant. | Not explicit. It depends on the non-explicit all-q constant. |
| 2603.12611 | 2026-03-13 | J. Schleischitz | Disproof of the uniform Littlewood conjecture. Its non-constructive part uses Bourgain–Kontorovich density results. | No M. |
| 2512.11357 | v 2026-04-22 | Jungwon Lee | Asymptotics for ε-thickenings of bounded-type fractal sets: "a remark on Zaremba's conjecture in an averaging sense". | No M. |
| 2411.18782 | v2 2025-06-30 | Chan, Kontorovich, Pak | Spanning-tree counts via continued fractions and thin orbits. Predates Shkredov. | No M. |
| 2401.01860 | v 2025-01-23 (ref. rev. 2025-12-24) | Rickards, Stange | Reciprocity obstructions for semigroup orbits, including continued-fraction semigroups with finite alphabets. | Obstruction-type result, not an M. |
| 2310.11279 | journal update 2026-01-28 (Amer. Math. Monthly) | E. Dubno | Folding-lemma algorithm, explicit families (the strong version for specific sequences). | No M for primes. |
| 2312.11661 | 2026-09-14 | McCormack, Zelinsky | Concerns "Zaremba's *function*" Σ_{d\|n} log d/d. | Unrelated. |

Off-arXiv items from 2026 found through OpenAlex:
- MMS, *IMRN* 2026(6) rnag048, published 2026-03-01. This is the journal version of 2212.14646; arXiv has v1 only. Its result is M = O(log p/log log p), so it cannot contain an absolute M. The full text is **unread** (closed access, OUP returned 403). Agent B also lists it as unread; the appendix of 2603.14116 cites "[43, Page 7/9]" from it.
- E. Dubno, PhD thesis, UZH, 2026-09-24 (doi 10.5167/uzh-436242). I read the abstract only; the ZORA page blocks bots. It contains a folding-lemma construction giving "all powers of 12 and 18", plus results on low-lying geodesics. No M for primes.
- A. Illarionov, *St. Petersburg Math. J.* 2026 (doi 10.1090/spmj/1886), "Probability estimates related to Korobov's quadrature formulas". It cites MMS. Abstract only (MathML), unread. Its title indicates Korobov-type probability estimates, not an absolute M.
- I. D. Shkredov, *Bull. LMS* 2026 (doi 10.1112/blms.70359), "On the exceptional set in Littlewood's discrete conjecture". It cites MMS. Abstract only; no Zaremba M.

### 2.2 Citation sweeps (Semantic Scholar, queried 2026-09-26)

- Papers citing 2603.14116: **2**, namely Zhang 2605.02518 and Chan–Heilman–Panova 2604.19094. OpenAlex cited_by_count = 0 (lagging).
- Papers citing 2605.02518: **0**.
- Papers citing 2212.14646 (MMS): 2111.05751 (Shkredov girth-free BG), 2210.14095, 2307.03156, 2310.09801 (Shulga, radical bound), 2603.14116, 2605.02518, Illarionov (SPMJ 2026), Shkredov (BLMS 2026), and one Moscow Univ. Bull. item. None has an explicit absolute M.

### 2.3 Author and group sweeps (arXiv metadata, created or updated since 2025-06)

- **Shkredov**: 2601.12457 (with Semchankau, set addition with two operations), 2603.14116, and 2609.08056 (Hamming-slice energy, with Biswas–Hwang–Maji–Ye). Journal items: "On a paucity result in incidence geometry" (*Forum Math.* 2026-07), "On common energies and sumsets II" (*Discrete Math.* 2026), "Uncertainty for convolutions of sets" (*PAMS* 2025), "On the BSG theorem for real numbers" (HAL 2026-05). None is about Zaremba constants. "On the BSG theorem for real numbers" is only possibly relevant to N6, and I have **not read** it.
- **Xin Zhang (HKU)**: 2605.02518; 2308.09982 (with Tang, super-approximation for SL2×SL2 and ASL2, revision 2026-05-02). There is no Zaremba follow-up. The other "Xin Zhang" hits are graph-colouring authors with the same name.
- **Kontorovich**: his research page lists #65 "Arithmetic Polyhedra" (2026, arXiv 2609.05349), #64 AMR diamond OA, #63 ICM 2026 plenary "The Shape of Math to Come", and #61–62 with Chan–Pak on continued fractions (2025). Nothing new on Zaremba constants. He co-organised the ICARM workshop "Milestones of Autonomous Mathematics", 13–17 April 2026. I found no Zaremba-related output from it (only its listing on his page; unread otherwise).
- **Moshchevitin**: 10 arXiv items since 2025-06, all Diophantine approximation or lattices. None on Zaremba M.
- **B. Murphy**: no arXiv items since 2025-06 in the harvested sets. His homepage was not checked (**unread**).
- **Rudnev**: 2607.24270 (with Tyrrell, multiplicative subgroups are not sumsets) and the distinct-angles paper. No new explicit SL2 growth exponent.
- **Helfgott**: only Chirre–Helfgott papers on arithmetic-function sums. No SL2 growth.
- **Kowalski**: trace functions, bilinear forms (FKMS 2511.09459). No update of explicit SL2 growth.
- **Breuillard**: Becker–Breuillard 2512.15364 and 2608.00755 (§4.1).
- **Magee**: no new Schottky or congruence explicit-gap paper since Calderón–Magee 2303.17950.
- **Pollicott**: 2606.13958 (validated numerics for the Gauss–Kuzmin–Wirsing constant) and others (§4.4).

---

## 3. AI-lab and non-refereed announcements touching Zaremba

- **Hacker News** (all time): 0 hits for "Zaremba conjecture" or "Zaremba's conjecture". All "Zaremba" hits concern Wojciech Zaremba (OpenAI). "Shkredov" gives only fuzzy-match noise.
- **arXiv cs.\*** (harvested records): no item about Zaremba's conjecture. The cs hits containing "Zaremba" are OpenAI system cards and robotics papers (W. Zaremba as author). The continued-fraction AI items are the Ramanujan-Machine line (2412.12361, 2502.17533, 2412.16818) and a "Continued Fraction Neural Network" (2603.20634). None concerns bounded partial quotients.
- **google-deepmind/formal-conjectures**: no path matching zaremba, continued or partial in the 1902-file main tree.
- **GitHub Lean code**: "Zaremba" appears only in `cahlen/idontknow` (below) and in auto-generated `ZarembaFiveFiniteFront.lean` files in the-omega-institute/trureturing and two forks. The latter are finite-range checks, not relevant.
- **Quanta Magazine**: the WP API search for "Zaremba" returns [] (no article).
- **X/Twitter, Reddit, lab blogs individually (DeepMind, OpenAI, Anthropic, Epoch), Google Scholar: unread.** They were unreachable or not searchable without WebSearch; Reddit's JSON search is bot-blocked.

### 3.1 `github.com/cahlen/idontknow`: human–AI "Zaremba A=5 proof framework". Not a K0 trigger.

Created 2026-03-28, last push 2026-07-22, 0 stars. README: "Human–AI collaborative research … (Claude, GPT-5.2/o3-pro, Gemini, Grok) … Not peer-reviewed." Table row: "**Zaremba Conjecture | Proof framework (not complete proof).** 210B verified, ρ_η ≤ 0.7606 … 4 gaps remain." The paper `paper/zaremba-proof.tex` claims A = 5 for all d. It combines brute force for d ≤ 2.1×10^11 with a claimed individual-denominator asymptotic R(d) = c1 d^{2δ−1} + O(d^{2δ−1−2ε}), δ = 0.837, derived from Magee–Oh–Winter norm-ball counting, and a threshold D0 ≈ 3.4×10^10.

Why it is not a collision:
1. It is not an explicit M for large primes via the Shkredov route, and its authors call it incomplete (gaps (1)–(4), including "MOW matching … pending independent verification" and a brute-force kernel "likely to have clipped Phase B frontiers").
2. The individual-count step is wrong as written. The .tex, lines ~165–196 of its Lemma "Tauberian", takes the error term E(d) of the cumulative count N(d) = #{γ : q(γ) ≤ d}, assumes a Mellin/Laplace representation with integrand decay (1+|t|)^{−A0}, A0 > 2, and concludes by the mean value theorem that |E(d) − E(d−1)| = |E′(ξ)|. But N is a step function with integer jumps and the main term c d^{2δ} is smooth, so E has jump discontinuities and is not C^1. The assumed transform decay would force E ∈ C^1, so the hypothesis is false for this E. The underlying fact is standard: a power-saving asymptotic for a cumulative count gives no asymptotic for individual values R(d). This is the minor-arc problem that Bourgain–Kontorovich and Huang had to solve.

I report this only so that the orchestrator does not treat the repo as prior art. **It has no bearing on the campaign's target.**

---

## 4. G2 sweep of related machinery (2025–2026, arXiv metadata; abstracts read, full texts unread unless stated)

None of the items below gives an explicit M, an explicit c ≥ 1/450 in the Shkredov min{…}, or the R2, R3 or R4 gap statement from DESIGN.md. The items bear on the routes as noted.

### 4.1 Explicit spectral gaps / expansion for SL2(F_p) or SL2(Z/qZ) actions
- **Kowalski, arXiv:1201.1139** "Explicit growth and expansion for SL_2" (v3 2012-07-02; *IMRN* 2013). Pre-2025 baseline. It gives explicit versions of Helfgott's growth theorem and of Bourgain–Gamburd for a fixed Zariski-dense generating set. Its comment reads: "v3, major corrections, including (almost) all numerical constants, and correction of one serious mistake, giving much worse expansion bounds". I did **not read** the constants. N5/N6 should read it because it is the other published explicit Helfgott exponent besides Rudnev–Shkredov.
- **Calderón–Magee, arXiv:2303.17950** (v2 2023-04-19; cited as JEMS 2025 by others, not verified). "Uniform and explicit lower bound of the second eigenvalue … of congruence coverings of Γ\H² provided the limit set of Γ is thick enough", for Schottky Γ < SL(2,Z). Relevant to R4 as an explicit uniform-in-level gap. It is stated for a **fixed** Schottky group, whereas Zaremba/Shkredov needs a q-dependent generating set with \|S\| ≈ q^{2τ}. Zhang's Remark 1.4 makes the same point about Bourgain–Varjú.
- **Soares, arXiv:2305.02228** (*Glasgow Math. J.* 68 (2026) 345–385). Conditional on GRH: an explicit uniform gap on Hecke covers Γ0(p)\H² of arithmetic Schottky surfaces, for almost all p. Relevant to R4 because P¹(F_p) = Γ0(p)\Γ is the quotient the design names. Conditional and "almost all p", so it gives no unconditional input.
- **Becker–Breuillard, arXiv:2512.15364** (uniform spectral gaps for quasi-regular representations; non-abelian Littlewood–Offord) and **arXiv:2608.00755** (2026-08-01): all Cayley graphs of G(p) of bounded rank are uniformly expanding, except for a small exceptional family of primes. This is qualitative, via heights. R2/R4 should note it, but it does not give explicit constants and does not remove the exceptional primes.
- Tang–Zhang 2308.09982 (super-approximation for SL2×SL2 and ASL2), Sarkar 2606.18674 (Selberg 3/16 for geometrically finite thin subgroups of SO(n,1)), and Dougall 2609.05271 (relative (τ) and expanders for expanding maps) are all qualitative.

### 4.2 Growth / energy in SL2(F_p); sum-product and incidence inputs
- No 2025–26 arXiv item improves the explicit Helfgott-type exponent. **Rudnev–Shkredov c_H = 1/20 (arXiv:1812.01671) is still the best explicit value I found.** This cross-checks N5: Kowalski 2012 is older and weaker per its own comment.
- **Lewko, arXiv:2609.27023** (v1 2026-09-22, 16 pp., unrefereed): "m points and n lines in k² determine O((mn)^{2/3} + m + n + mn/p) incidences" for any field of characteristic p, by the polynomial method, and "sharp over prime fields" for m = n. If correct, this is a large change in F_p incidence geometry. It would give full-strength Szemerédi–Trotter over F_p up to the mn/p term. I sanity-checked the obvious counterexample: the subfield grid F_q² in F_{q^k}² with F_q-lines has q³ incidences, and mn/p = q^4/p ≥ q³ for k ≥ 2. The claim survives that check, but I have **not read** the proof. It could feed R3 (point–line or Möbius incidence for Cor. 16) and R2 (sum-product/energy steps inside Larsen–Pink-type arguments). The R2 and R3 explorers should read it first and treat it as unverified until a referee pass.
- Xiyu Hu, arXiv:2609.05652 (2026-09-04) uses "Bourgain's expansion-based incidence theorem in SL2(F_p)" to get value sets ≫ min{M,p}^{1/2+η} with η absolute and **not explicit** per the abstract. There is also a partial Lean 4 formalization.
- Hung–Pham–Slavov, arXiv:2501.01697: subgroups of SL2(F_q) preserving E ⊂ F_q². If \|E\| ≪ q^α and more than q^β elements preserve E with β ≥ 3α/2, then E lies in a line.
- Harrison–Mudgal–Schmidt, arXiv:2603.06483: uniform sum-product for 1-dimensional algebraic groups over **C**, which does not apply to F_p.
- Zhi Yao, arXiv:2608.10355: a quadratic-expansion exponent 17/14 over F_p for \|A\| ≤ p^{2/3}. It is abelian (sum-product type).

### 4.3 Bilinear Kloosterman sums / modular hyperbola (R3)
- **Pascadi, arXiv:2511.08445** (v2 2026-06-21): type-II Kloosterman bilinear forms with composite moduli via Fourier analysis on SL2(Z/cZ) and non-abelian amplification. It saves c^{−1/12} at length √c for products of two equal-size primes and "beyond the Pólya–Vinogradov range for all moduli" when combined with earlier prime-modulus results.
- **Blomer–Pascadi, arXiv:2607.24311** (2026-07-27): saving **c^{−1/32}** at length √c for all moduli, "improving on all previous approaches even for prime moduli".
- **Fouvry–Kowalski–Michel–Sawin, arXiv:2511.09459** (bilinear forms with trace functions) and Kowalski–Michel–Sawin 1802.09849 (updated 2025-12-15).
- A. Mohammadi, arXiv:2608.01203: bilinear Kloosterman sums over boxes in F_{p^n}, nontrivial once \|B1\|\|B2\| > p^{n/2+ε}, i.e. beyond Weil. It also shows exponential Fourier decay for the random walk with steps aXY + b(XY)^{−1}.
- Dong–Robles–Zeindler 2601.00292 (Kloosterman fractions, saving 1/12 in the balanced case), Blomer–Risager–Shparlinski 2411.17823 (discrepancy of modular inverses), T. H. Chan 2506.04087 (close points on xy ≡ c mod p), Wright 2608.27732 (trilinear Kloosterman fractions), Shparlinski–Xiao 2601.10113 (Salié bilinear sums).
- Relevance: these papers target short sums (the √-barrier, length about √c). R3's regime is different: I-invariant sets of density ≥ p^{−η} with interval length N = p^{1/9}, where the task is to beat the square-root barrier using density and I-invariance. None of them states that gap lemma. For R3 they are tools, not collisions.

### 4.4 R5 (overhead) inputs
- Pollicott, arXiv:2606.13958 (2026-06-11): validated numerics for the Gauss–Kuzmin–Wirsing constant.
- J. Brown, arXiv:2604.20812 (math.NA, 2026-04-22): rigorous high-order B-spline estimates of Hausdorff dimensions of continued-fraction IFS limit sets. This bears on rigorous w_M enclosures, as does Pollicott–Vytnova 2012.07083, which is already in DESIGN.

---

## 5. Unread / unreachable (stated plainly)

- **General web search**: unavailable (the session WebSearch budget of 200/200 was exhausted before this task). So no Google/Bing-style sweep was run for blogs, news, lab announcements, conference talks, or slides.
- **arXiv export API** (`export.arxiv.org/api`): HTTP 406 to every client I tried. I used the arXiv web search and OAI-PMH instead.
- **X/Twitter; Reddit** (bot-blocked); **Google Scholar**; the **ZORA thesis page** (Anubis block; abstract taken from OpenAlex).
- **MMS IMRN 2026 rnag048** full text (closed, OUP 403). **Illarionov SPMJ 2026** full text.
- **Math-Net.ru** Shkredov person page (my guessed ID was wrong; not retried). **Murphy** and **Zhang (HKU)** homepages were not fetched.
- Full texts of every §4 paper. Classification is from abstracts only.
- OAI harvest coverage: math.NT/CO/GR/DS/CA/RT/SP are complete from 2025-01-01. math.NA/PR and cs.AI/LO/LG are partial. The arXiv web search for "Zaremba" (all archives) covers the metadata of the rest.
- Metadata sweeps cannot see a paper that mentions an explicit Zaremba M only in its body. Citation sweeps (Semantic Scholar) partly cover this: only 2 papers cite 2603.14116, and both were read.

## 6. Numbers established (with sources)

| number | source |
|---|---|
| M = 2^2000 for all sufficiently large primes | Shkredov arXiv:2603.14116v2, Appendix eq. (158), verbatim from the PDF |
| 2603.14116 versions: v1 2026-03-14 (98 KB), v2 2026-06-24 (68 KB), no v3 as of 2026-09-26 | arXiv abs page, fetched 2026-09-26 |
| 2605.02518 versions: v1 2026-05-04, v2 2026-05-08, no v3 | arXiv abs page |
| Zhang: M "effectively computable", no value | 2605.02518v2, Remark 1.3 |
| Zhang: \|S\| ≈ q^{2τ} generating set, so Bourgain–Varjú's dependence "not good enough" | 2605.02518v2, Remark 1.4 |
| Shkredov Thm 8 bookkeeping parameters quoted by Zhang: H = N^{9/20}, M* ≈ 10M, N* = N^{1/100} | 2605.02518v2, §4 (Zhang's outline). Shkredov's own §5.4 uses N* = N/H² = N^{1/10}, which Agent B's ledger uses. The discrepancy is Zhang's paraphrase and is not load-bearing. |
| Chan–Heilman–Panova D = A + 1 (A = Shkredov's absolute constant, not computed) | 2604.19094, proof of Thm 1.7 |
| Citing papers of 2603.14116: 2; of 2605.02518: 0 | Semantic Scholar API, 2026-09-26 |
| arXiv "Zaremba" all-field hits: 391 total; 2025–26 Zaremba-conjecture items: 9 (table §2.1) | arXiv search page, 2026-09-26 |
| OAI records scanned: 98,130 (datestamps 2025-01-01 → 2026-09-25) | own harvest |
| Best explicit Helfgott-type exponent in print: c_H = 1/20 (no 2025–26 improvement found) | Rudnev–Shkredov 1812.01671 (per DESIGN and Agent B); negative result of the §4.2 sweep |
| Blomer–Pascadi saving c^{−1/32} at length √c; Pascadi c^{−1/12} (two equal primes) | abstracts of 2607.24311, 2511.08445 |
| Lewko incidence bound O((mn)^{2/3} + m + n + mn/p) (unrefereed, 2026-09-22) | abstract of 2609.27023 |
| cahlen repo: claimed D0 ≈ 3.4×10^10, brute force to 2.1×10^11, δ = 0.837 (claims, not verified; see §3.1 for the invalid step) | `paper/zaremba-proof.tex` abstract |

## 7. Recommendations to the orchestrator (for the K0 decision and Phase 1 briefs)

1. **K0 = CLEAR.** No re-scope is needed. Re-run this sweep before any announcement (G2), because Shkredov or Zhang could post a v3 or a new paper at any time. The quick check is the arXiv abs pages of 2603.14116 and 2605.02518, plus `arxiv.org/search/?query=Zaremba&order=-announced_date_first`.
2. Give R2 and R3 explorers **Lewko 2609.27023** (unverified; flag it as needing a referee pass before any use) and **Blomer–Pascadi 2607.24311 / Pascadi 2511.08445** (R3 tools). Give R4 **Calderón–Magee 2303.17950** and **Soares 2305.02228**, and note the fixed-generator versus q-dependent-generator gap.
3. N5/N6 should read Kowalski 1201.1139 for the other explicit Helfgott constant, and Shkredov's HAL 2026 "BSG for real numbers" for possible BSG-exponent changes. I did not read either.
