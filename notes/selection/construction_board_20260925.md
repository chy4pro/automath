# Construction Board — 2026-09-25

## 1. Method

Six scouts each searched a channel (C1–C5 plus a mixed sweep) for open, finite-object,
checker-decidable construction targets and reported record/value/year/method,
object size, search shape, checker and acceptance path, plus a list of sources
they could not reach. A rater scored each pick (fit: high/medium/low) with a
pilot plan and kill criterion. A skeptic then attempted to refute each rated
pick (prior art, competition, blocking rules, hardness), producing an adjusted
fit and confidence, and a short verdict write-up per pick.

## 2. Board

| id | channel | statement (short) | record (value, year, method) | object size | search shape | acceptance path | rater fit | skeptic refuted? | adjusted fit | confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| OEIS A000789/A267295/A267296 a(13) | C4 | Max order triangle-free circulant with no independent set of size n (+related RC numbers) | a(12)=48 / A267296(12)=49; 2003, Harborth–Krause exhaustive search | S ⊆ Z_m, ~30 residues, m~50–67 | exact-SAT/ILP | OEIS edit | high | yes | none | high |
| LJCR C(28,13,3) + siblings | C1/mixed | Covering design C(v,k,3) small-b cells | C(28,13,3)=19; 1998, induced construction | 18×28 vars, ~59k aux | exact-SAT/ILP | LJCR / coveringrepository.com | high | yes | low | medium |
| OEIS A283438 a(5) | C4 | Largest 3-AP-free (restricted differences {0,1}^n) set in F_3^n | 102 ≤ a(5) ≤ 108; 2017, R. Israel | 243 vars, ~7.5k triples | exact-SAT/ILP | OEIS edit | high | yes | low | medium |
| OEIS A275672 a(7) | C4 | Largest distinct-pairwise-distance subset of n×n×n lattice | 10 ≤ a(7) ≤ 12; 2016, unstated (Israel ILP/tabu per Math.SE) | 343 pts, choose 11 | exact-SAT/ILP | OEIS edit | high | yes | low | high |
| erdos617 r=5 | C5 | Erdős–Gyárfás balanced-colouring conjecture, smallest open case r=5 | proved r=3,4; r=5 open Jul 2026 | 325 edges×5 colours, ~1.15M clauses | exact-SAT/ILP | erdosproblems.com proof claim | medium | yes | none | high |
| erdos1056-k15 (OEIS A060427(15)) | C4/C5 | Prime with 16 equal factorial-mod-p residues | k=14, p=10428007; 2007, Andersen, plain search | scan primes to ~4.5e7–8e7 | search/scan | OEIS edit | medium | yes | low | high |
| LJCR C(27,12,5) / C(16,10,8) | C1/mixed | Covering design local-search cells | 208 (2006, DP covering) / 448 (1997, Nurmela–Östergård SA) | ~8008 candidate blocks | local search / ILP | LJCR / coveringrepository.com | medium | yes | low | medium |
| Ramsey R(5,15) lower bound (circulant) | C3 | Classical Ramsey number lower bound via circulant graph | 275 (2026, DS1 rev 18, gluing ineq. 2.3.h, not a direct search) | Z_n, n~276–300, connection set | exact-SAT/ILP + local search | DS1 (Radziszowski) revision | medium | **no** | medium | medium |
| MOLS 4-MOLS(22) / OA(6,22) | C3 | Existence of 4 mutually orthogonal Latin squares of order 22 | N(22)≥3; 1978 (per 2014 source), still open 2024 | 484×6 OA, ~23 base rows under group | mixed | Abel/Colbourn–Dinitz MOLS table | medium | yes | low | high |
| erdos867 consecutive-sum-free density | C2 | Density constant for consecutive-sum-free sets | 13/24·N−O(1) lower bound; 1996, Coppersmith–Phillips hand construction | small-N exact search + family construction | mixed (LLM-proposed family + proof) | erdosproblems.com comment/note | medium | **no** | medium | medium |
| TxGraffiti Conj 4: Z(G) ≤ α(G)+1 subcubic G≠K4 | C5 | Automated-conjecture zero-forcing vs independence bound | evidence only up to n=16/n=8 census; open per TxGraffiti | small graphs | exact search + local search | arXiv note / authors | medium | yes | none | high |
| OEIS A271906 a(12) | C4 | Largest right-isosceles-triangle-free subset of n×n grid | a(12)≥29; 2016, R. Israel | 144 vars, ~8544 triples | exact-SAT/ILP | OEIS edit | medium | yes | low | high |

## 3. Survivor sections

### Ramsey R(5,15) lower bound (circulant) — adjusted fit: medium, confidence: medium

**Full cell (as rated):**
- statement: DS1 lists R(5,15) ≥ 275, sourced to the generic gluing inequality 2.3.h, not a direct search. DS1 note 2.2(i) says such Table IIa bounds "should not be that hard to improve." (Skeptic correction: this cell is actually in Table Ia, not IIa — see findings.)
- object: A symmetric connection set for a circulant graph on Z_n, n ≥ 276, K5-free with independence number ≤ 14.
- record: R(5,15) ≥ 275, from DS1 revision #18 (24 April 2026), via 2.3.h: R(5,14)+R(5,2)+3−k type gluing = 267+5+3.
- record_year / method: 2026 DS1 listing; the 275 bound itself is not from a direct circulant search but from gluing R(5,14)=267.
- object_size: one connection set (line-sized witness) on n~276–300 vertices.
- checker: circulant is K5-free (look for K4 in N(0)) plus independence number ≤ 14 certified via exact clique/branch-and-bound on the complement (~180 vertices at density ~0.6–0.65).
- search_shape: simulated annealing / local search for candidates, exact clique solver for certification.
- acceptance_path: DS1 (Radziszowski) revision, arXiv note + GitHub witness/checker, email to maintainer.
- url: https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS1 ; Kuznetsov arXiv 1505.07186

**Pilot plan (as rated):** Write a circulant search on Z_n for n=276..280: simulated annealing over symmetric K5-free connection sets, scored by a fast/greedy independence-number bound, confirmed with an exact clique solver on the complement (fix vertex 0 in the independent set via vertex-transitivity). Validate first by reproducing Kuznetsov-type circulants for R(5,14) ≥ 267 on 267 vertices. Use 4 cores for 2 h.

**Kill criterion (as rated):** Stop if the R(5,14) circulant is not reproduced in 1 CPU-h, or if no candidate with exact α ≤ 14 appears after 3 CPU-h at n ≥ 276.

**Skeptic's findings:**
- Record confirmed at DS1 revision #18 (24 April 2026, cached scratchpad/r515/ds1.txt): row 5 = 43 59 80 101 133 149 183 203 233 267 275, sources Ex4 Ex25 CaET HaKr1 Kuz ExT Kuz Kuz Kuz Kuz 2.3.h. 275 = R(5,14) 267 + R(5,2) 5 + 3 — a gluing placeholder, not a direct search result. No newer improvement found in two searches. Neighboring 2026 papers (DeepMind arXiv 2603.09172; Coniglio et al. 2608.18769; Yu 2608.18169) do not touch R(5,15).
- Rater error 1: R(5,15) sits in Table Ia (k≤10, l≤15), not Table IIa. DS1 note 2.2(i)'s "should not be hard to improve" comment is about Table IIa/IIb, arguing against this specific cell — but the conclusion (this entry is a gluing placeholder, not a search result) survives anyway.
- No known object under another name found. Kuznetsov (arXiv 1505.07186) lists circulants only up to (5,14)=266 vertices; does not treat (5,15). His method reportedly loses connectivity beyond order ~300.
- Plausibility guess (unverified): Kuznetsov's circulant orders grow by steps of +30/+34 for l=12..14 (202→232→266); extrapolating, a (5,15) circulant might exist around n=290–300, above the target of 276 — favorable but unconfirmed. A leftover local probe script (scratchpad/r515/probe.py) exists but its output was never saved.
- Compute/rule blocker: the pilot as written (SA + exact clique solving on 4 local cores, 2 h) violates the current owner rule (commit c4b72f6, 09-25): "no local solvers — solvers only for important results and only on GitHub Actions, otherwise wait for the owner." Must move to GitHub Actions or get owner sign-off.
- Checker is not as cheap as claimed for the certification side: proving α ≤ 14 needs branch-and-bound on ~180 vertices at density ~0.6–0.65 (random graphs that size/density have clique number ~17–18), so real work, though feasible in minutes–hours with a coloring-bound MCS.
- Acceptance path is real but slow: DS1 revisions are not "roughly yearly" (rater error 2) — actual dates 2014-01, 2017-03, 2021-01, 2024-06, 2026-04, so next listing likely ~2027–28. Practical path: arXiv note + GitHub witness, plus email to maintainer.
- Value is modest: a classical Table Ia entry, less impressive than beating a searched record; borderline "small" under the owner's no-X/no-site-claim rule for small results. Worth more if the result lands well above 276 or if the method improves several related cells (R(5,15), R(6,14), R(6,15), other 2.3.h/2.3.i entries) at once.

### erdos867 consecutive-sum-free density — adjusted fit: medium, confidence: medium

**Full cell (as rated):**
- statement: erdosproblems.com #867. The lower bound 13/24 is Coppersmith–Phillips 1996, a hand construction; site lists nothing newer.
- object: exact max|A| for consecutive-sum-free sets up to N (small-N search), or a periodic/scaled family construction with proven density above 13/24, plus a proof.
- record: current best bounds 13/24·N − O(1) ≤ |A| ≤ (2/3 − 1/512)N + log N, due to Coppersmith and Phillips [CoPh96]. Freud gives 19/36 [Fr93]; Adenwalla gives (2/3+o(1))N.
- record_year / method: 1996, hand construction.
- object_size: small-N branch-and-bound (N up to ~70–90), or a scaled-interval family S ⊂ (0,1] with A = N·S ∩ ℕ.
- checker: sort A, scan each start forward summing consecutive elements until exceeding N; O(|A|·run length), seconds even at N=1e5.
- search_shape: mixed (LLM-proposed family + exact small-N branch-and-bound + proof).
- acceptance_path: erdosproblems.com forum comment / proof claim, since the page names "current best bounds" and comments are active (2025–2026).
- url: https://www.erdosproblems.com/867 ; https://www.erdosproblems.com/forum/thread/867

**Pilot plan (as rated):** Step 1 (1 CPU-h): compute exact max|A| for N ≤ 70–90 by branch-and-bound (numba), prefix-sum incremental check, tabulate max|A|/N and extremal sets. Step 2: implement/extend the Coppersmith–Phillips family, have an LLM propose periodic/scaled patterns, measure density on N up to 1e5 with the checker (~0.5 CPU-h).

**Kill criterion (as rated, superseded by skeptic — see findings):** Stop if exact small-N maxima sit at or below 13/24·N+O(1) with no structure beyond Coppersmith–Phillips, and 3 LLM-proposed family rounds all fail the checker or give density ≤ 13/24.

**Skeptic's findings:**
- Record verified at https://www.erdosproblems.com/867 (fetched today): "current best bounds are due to Coppersmith and Phillips [CoPh96]," 13/24·N−O(1) ≤ |A| ≤ (2/3−1/512)N+log N; Freud 19/36 [Fr93]; Adenwalla (2/3+o(1))N. Forum thread has 3 comments (Weisenberg 2025-08-12: only an O(1) gain; Alexeev 2025-09-02: points to CoPh96; Monticone 2026-04-07: Aristotle autoformalization); none improves 13/24. No post-1996 improvement to the lower constant found.
- Caveat: the underlying Erdős problem is already marked "disproved (Lean)" on the site and in the local mirror. Raising 13/24 improves a side constant on a closed problem, not the open Erdős question itself — value is modest, comparable to a "small result."
- No other name/OEIS entry found for this object (site OEIS field says "possible" — not fully ruled out, few searches done). Unverified guess: possibly overlaps AlphaEvolve/Tao-style Erdős-constant problem lists — flagged for further G2, not checked.
- Compute measured locally (naive Python DFS, scratchpad csf.py): exact max|A| for N=1..55, e.g. N=20:12, 30:17, 40:24, 50:30, 55:33 (64s at N=55, roughly doubling every 3 steps of N). numba + better pruning should reach N≈80–90 within 1 CPU-h — fits the box, not a compute race.
- Pilot logic problem: small-N maxima already sit well ABOVE 13N/24 (33 vs 29.8 at N=55, slope ≈0.64 from N=30→55), but the upper bound has a +log N term so O(1)/log effects dominate at N≤90 — exact small-N data cannot separate 1/2, 13/24, or 0.6 asymptotically. The stated kill/progress criteria are therefore untestable as written and should be replaced.
- Framing correction: the binding structure is likely scale-invariant/dyadic (pairs in (N/2,N] are automatically fine; Adenwalla's bound counts across [x,2x]), not periodic-residue. Candidate families should be A = N·S ∩ ℕ for S a finite union of intervals in (0,1] (Coppersmith–Phillips-type), checkable exactly via rational interval arithmetic, with an O(1)-loss argument for behavior near 0. This gives the LLM-first route (construct family → compute exact density → prove) a real path; a checker run to N=1e5 alone is only supporting evidence, not a proof.
- Checker confirmed simple and correct as described; writable from the Lean definition (ConsecutiveSumFree) in minutes.
- Acceptance path is real and active (site comments 2025–2026). A side product: the exact-max sequence 1,2,2,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,12,… appears to have no OEIS entry (site says "possible") — a small C4 side item, unverified (OEIS not directly searched).
- Value: small circle of interest — a 1996 constant on an already-disproved problem; an improvement would be a short note/site comment, not an X-level milestone. Gap [0.5417, 0.6647] has not moved in 30 years; small-N local slope (~0.6) is encouraging but payoff stays modest.

## 4. Refuted sections (short)

**OEIS A000789/A267295/A267296 a(13)** — REFUTED. arXiv 2608.18769 (Coniglio et al., submitted 2026-08-19) already gives R_C(3,n) for n=13..20 via IP, matching OEIS for n≤12 and extending it (Table 8: 58, 64, 73, 79, 92, 98, 106, 111 for n=13..20), same object as A267295/A000789 but not yet posted to OEIS. Only the untouched sibling A267296 (RC_1, ascending-sweep variant) might remain open, as a minor unclaimed extension of someone else's 2026 result — not a record of our own.

**LJCR C(28,13,3) + siblings** — REFUTED. "Never searched" is unsupported (LJCR logs only improvements, not failed attempts); the same v=28 region has been actively swept by contributors (Atzeni, Milshtein, Jurcovich, Bluskov–Sidorenko) through 2024–2026 with no change to this cell, suggesting it may already be near-optimal. The claimed UNSAT path (raising the lower bound by 3) is out of reach for plain cadical without a structural/counting argument (cf. arXiv 2607.23766's method for a similar 1-gap cell); checker is trivial but doesn't help since a routine SAT improvement is low value (thousands logged yearly) and coveringrepository.com (the current successor site) could not be checked (Cloudflare 403).

**OEIS A283438 a(5)** — REFUTED (blocked, not falsified). Record and gap confirmed genuine and possibly beatable (product bound only gives 84; 102 looks improvable), but the required method (local CP-SAT/cadical/tabu search) is barred by the standing owner rule "no local solvers — solvers only for important results and only on GitHub Actions." An OEIS lower-bound bump is explicitly a "small result" under the 09-25 owner ruling (no X, no site claim), so it doesn't qualify for GitHub Actions either. Parked.

**OEIS A275672 a(7)** — REFUTED. Scout's "~100 possible squared distances" is wrong (actual: 66 distinct values in {0..6}^3, so an 11-point set needs 55/66 = 83% coverage); the original record-setter (R. Israel, via Math.SE, ILP+tabu search) already tried and failed to find an 11-point set, making "no witness exists" the more likely outcome — the expensive direction. Pilot also breaks the no-local-solvers owner rule, and value is low (only Math.SE/Wolfram Demonstration citations, no papers depend on small values).

**erdos617 r=5** — REFUTED, decisively. r=5 has already been claimed as SETTLED (conjecture holds) via an open, unmerged Lean 4 PR (conjectures-io/conjectures-contribution#129, opened 2026-09-19, 3651-line script.lean, no sorry/admit/axiom beyond propext/Classical.choice/Quot.sound) using a minimal-core structural argument (the case range 4≤a≤r−2 is empty at r=5, closed by omega) — not a SAT search. The object is also identifiable as the Chung–Liu 1978 "weakened Ramsey number" R̄_r(r+1), tight at affine-plane orders, making a counterexample very unlikely. 7 hidden proof claims already exist on the erdosproblems.com page.

**erdos1056-k15 (OEIS A060427(15))** — REFUTED (blocked + low value). Record confirmed unextended, but a competing AI-assisted user (KentaKitamura, active on the same forum thread) is well-positioned to take k=15 next, and the sibling sequence A230315 shows the same community does exactly this kind of scan routinely. Measured cost (~80–270 core-hours) is exactly the "heavy local compute for a small result" the owner rule bars from local execution; would need ~12 GitHub Actions jobs, of doubtful "importance." Rater's "Wilson reflection halves the work" claim was checked and found wrong. Value: routine OEIS extension, no structural insight, already below the #889 "small result" bar.

**LJCR C(27,12,5) / C(16,10,8)** — REFUTED. Records confirmed but the rater got two facts wrong: the C(16,10,8) lower bound is 360 not 352 (Krug, arXiv 2607.23766), and the 448 record is itself a "symmetric covering" (prescribed-automorphism-group SA) — the same method the pilot proposes, meaning the obvious idea already produced this exact 29-year-old record. The C(27,12,5) region has been actively swept through Sept 2026 with neighboring cells improving while this one held — suggesting resilience, not neglect. Pilot also breaks the no-local-solvers owner rule; value is low (routine table improvement among ~98,583 logged since 1996).

**MOLS 4-MOLS(22) / OA(6,22)** — REFUTED (fit downgraded, facts hold). Record verified genuine and still open as of a 2024 source (Miller–Abel–Valkov–Fraser, Symmetry 2024), explicitly named the "flagship gap" of the MOLS table (last N(n)≥4 case unresolved) — but that also means it is a famous problem under expert, ongoing attack (Abel, Todorov) using exactly the proposed methods (difference matrices/QDMs, group-invariant search) for decades, so a naive symmetric-ansatz SAT pilot is very unlikely to find anything new; UNSAT on a single ansatz is not publishable. High value if solved, but low odds — downgrade to a gacha-ticket-scale side task only.

**TxGraffiti Conj 4: Z(G) ≤ α(G)+1 subcubic G≠K4** — REFUTED, dead. Already disproved: arXiv 2607.23664 (Fischer, 2026-07-26) gives explicit counterexamples (24-vertex subcubic graph, Z=α+2; 36-vertex cubic graph, Z=α+2), found "with the assistance of Claude Opus 5," with a companion paper already claiming the "smallest counterexample" and "repaired conjecture" follow-ups. The pilot's exhaustive sweep (n≤13/20) would never have reached the actual 24-vertex structured counterexample anyway — compute was never the real bottleneck, a structural idea was.

**OEIS A271906 a(12)** — REFUTED (blocked + hardness risk). Record confirmed open, but a new 2026 competitor (Karolyi–Solymosi, arXiv 2607.22828, with DeepMind/AlphaEvolve acknowledgment) is actively working this exact problem family (asymptotic side, no small-n values given). The proposed local cadical/CP-SAT pilot breaks the no-local-solvers owner rule; hardness at n=12 (144 vars, density ~0.2, UNSAT likely needed since the +3 pattern suggests a(12)=29 exactly) is plausibly large, unlike the rater's optimistic framing. Value is low (obscure sequence, ignored even by the two 2026 papers on the same underlying combinatorial family).

## 5. Rater's dropped summary

I checked a few claims myself today (WebSearch/WebFetch, 2026-09-25). Scout claims are otherwise taken as given.

Duplicates: erdos213 and erdos213-integral-8pts merged; the cage cells cage(3,13), cage(8,5) and 'Cages n(k,g)' merged; the Hadamard 668 cell is closed.

C1 dropped:
- erdos203. At least three groups ran a 2-D covering search and published negative outcomes in September 2026: github.com/veljjanoski/erdos203, github.com/Neo7672/erdos-203-covering-search (LNS plateaus at 17–21% uncovered and concludes 'structural design needed, not more search') and an issue in the-omega-institute/trureturing. It is crowded and raw search has already failed. Revisit only with a new nested-covering idea (a proof-line task).
- erdos273: needs huge L, the density margin is thin and prior searches died. Big-compute regime.
- erdos213 (8 points): Kurz-style exhaustive methods already cover this, bounty hunters are active, and a raw search has low odds.
- erdos686 N=4, erdos849 t=5, erdos850: the expected answer is 'no witness', and each has been searched heavily (GPU past 1.4e12 for #850; 1e62 for #849).
- erdos276: not a finite object. Separately flag the possible FC mis-statement for a skeptic.
- erdos289: 2 proof claims already on the page.
- erdos931 variant: unread at source; the heuristic says very rare. Keep in reserve.

C4 dropped or held in reserve:
- A375071, A375077, A005113: very recent (2026) compute races with active amateurs; they do not settle anything.
- A036236 table: the list of unknown entries was not seen, so it cannot be rated.
- Reserve if slots free up: A110214 a(6) (quick set-cover ILP, low value), A234349 a(22), A248866 a(14), A271520 a(10) (scout's sphere bound a(10) >= 47 already rules out A122408; exact value likely hard), A157616/A157617 (recreational, harder path encodings).
- A063551: needs the order-type database, too heavy.

C2 dropped:
- erdos302: wide gap but recent, simple bounds; others are likely on it.
- erdos857 and erdos20: the record is 3 weeks old (arXiv 2609.06175) and the authors are active.
- erdos188: interesting, but no finite checker (needs a geometric covering proof). Note a pitfall for any lattice-disc ansatz: red pieces must have diameter < 1, and lattice arrangements leave empty strips along lattice directions, which give infinite blue APs. Hand to the proof line (slot 1) rather than to constructions.
- erdos503 (R^9): the d=9 record is unknown; reserve after G2 on 2-distance sets.
- erdos1097 and erdos36: C6/AlphaEvolve territory.
- erdos170: the construction side is believed optimal.

C3 dropped:
- Hadamard 668: closed (Claude-assisted team, Aug 2026).
- Costas 32/33, Golomb OGR-28/29, ex(n;{C3,C4}), cages: compute-dominated or reworked in 2025–26 by well-equipped groups.
- Degree/diameter: kept as a method source only. It validates the LLM-proposed Cayley ansatz, but expect copycats.
- R(4,4,4), Schur S(6), R(5,18): famous or SAT-expert cells. R(5,18) is superseded by the smaller R(5,15) pick.
- W(6,3): plausible (a 2012 cyclic-zipper record that Heule did not certify) but the acceptance path is weak. Reserve.
- Maruta n_3(6,19), n_5(5,18), codetables [15,8]_7: expert competition, nonexistence is likely, and codetables small-k upper bounds are known to be stale. Reserve for when an ILP-with-group toolchain exists.
- S(2,6,v): the Banakh et al. group is actively clearing the list (Jul 2025, Nov 2025, May 2026). Also my own arithmetic: most listed v (231, 256, 261, 286, ...) are not ≡ 1 mod 30, so there is no plain regular difference family; they need 1-rotational or non-regular actions, which is their specialty. Search today confirms 231/256/261 are still open. Reserve.
- Skew-Hadamard 356: still listed unknown (SageMath docs, search today). But 89 is prime, so small cyclotomic orbit spaces were surely exhausted by Djoković, and the Claude-assisted Hadamard team may move to it. Reserve after G2.
- HDS 576/400/784, the smallest open abelian difference sets, cyclic RDS: likely nonexistence (proof/UNSAT targets) or lottery tickets. Idle-CPU gacha only.
- CW(n,k): fits certified UNSAT, but the cells survived Gordon's orbit-exhaustive searches. Reserve with a quotient-image ansatz.

C5 dropped:
- erdos97: crowded, prior leans toward non-existence.
- erdos64: two arXiv papers in 5 weeks; better as a slot-2 exact race.
- erdos993: unimodality survived tens of thousands of ML examples.
- erdos647: the expected answer is no.
- erdos488: AI groups are present and the forum is unread.
- Babai VT: probably already checked via the census.
- Negami: low prior, open ply.
- WoWII: DeepMind is actively mining it.
- erdos1082(a): cheap, reasonable reserve C5 pilot. First compute total distinct distances of the Harborth 8-set and the Xichuan 42-set.
- The 'shape' cell is a reference, not a target.

Scheduling note, since the user asked that this not slow progress: run every pilot at nice 19 on 4–6 cores at most, with about 2 GB RAM each, proof logging off in pilots, and DRAT written only in capped re-runs (after the 36 GB crash). #624 checkpoint 2 keeps priority.

Tooling to add first (user-level): pip install ortools and python-sat into ~/.venv-automath, and build nauty/geng. `which` did not find cadical or cake_lpr on PATH, so confirm their install paths.

## 6. All unreachable sources

**Scout 1 (C4/mixed):**
- WebSearch: session budget exhausted (200/200) at first call, so no general web/literature search was possible; G2 for #203, #213 and #273 prior art rests only on arXiv API queries and site pages
- erdosproblems.com pages not fetched because of the 10-page cap: /850, /849, /931, /389, /396, /479, /1055, /197, /124 and the forum threads for 203, 213, 276, 289
- erdosproblems.com/273: the content of the one listed proof claim was not visible in the fetched pages
- arXiv PDF 0804.1303 (Kreisel–Kurz): binary PDF saved but not text-extractable (no pdftotext/pypdf installed; no new dependencies added), so the 8-point search range is unverified
- Havermann–Hobson 2^n mod n tables (unknown entries for k<=10000): linked from OEIS A036236 but not fetched
- Remaining 17 of the 30 listed problems (197, 376, 1209, 41, 51, 261, 282, 396-extra, 602, 680, 681, 727, 786, 1059, 1108, 1199, 124): Lean docstrings read locally; they were triaged out as not settleable by a finite witness (infinite objects, 'infinitely many' or 'sufficiently large' quantifiers), or, for 1209, already disproved in FC

**Scout 2 (C1/C5-adjacent):**
- https://dl.acm.org/doi/abs/10.1007/s00373-014-1504-3 (HTTP 403; Wu–Sun–Radziszowski R(C4,K1,n) values)
- https://www.researchgate.net/publication/280809879_A_remark_on_star-C4_and_wheel-C4_Ramsey_numbers (HTTP 403)
- https://arxiv.org/pdf/2310.16701 (PDF not parsed; the HTML version was used instead)
- erdosproblems.com/213 and /508 were not fetched because of the 10-page cap (10 used: 170, 302, 36, 1097, 20, 857, 188, 503, 867, 552); the local FC docstrings and other sources were used instead
- Coppersmith–Phillips 1996 paper not read (construction structure for #867 unverified)
- Deuber–Erdős–Gunderson–Kostochka–Meyer 1997 paper not read (the 1.551 amplification mechanism is unverified)

**Scout 3 (C1/C3 covering & Ramsey/cage designs):**
- https://ljcr.dmgordon.org/cover.html (NXDOMAIN). Per https://dmgordon.org/ljcr/, the covering database froze after 2026-03-01 and its AWS servers shut down in Aug 2026. I used the GitHub JSON mirror dmgordo/LJCR/coverings/coverdata.json instead.
- https://coveringrepository.com (Giovanni Acerbi's successor site, which carries post-freeze improvements): Cloudflare 403 block. Post-2026-03 covering records are therefore NOT checked.
- https://users.encs.concordia.ca/~ta_ahmed/vdw.html (Ahmed's vdW table): HTTP 404. Wayback has a 2010-11-24 snapshot, but the Wayback availability API returned 429, so I did not read it.
- http://ginger.indstate.edu/ge/CAGES (connection refused). I used the mirror http://isu.indstate.edu/ge/CAGES/index.html, which lists Exoo's own record graphs only.
- WebSearch: the session budget was exhausted (200/200), so I found no post-2013 cage literature and no post-2017 vdW/Schur literature beyond the pages fetched.
- Text extraction lost the DS1 reference list (font encoding), so the years for the HiIr, FreSw and Chu1 records are from memory and marked as guesses.
- Global-memory recall_presets (required by AGENTS.md) was not available in this session and was not called.

**Scout 4 (C3 design theory / MOLS / BIBD / Turán):**
- https://combinatoricswiki.org (HTTPS certificate error in WebFetch; the pages were fetched over plain http with curl, but the wiki pages are dated 2019-01-03 and stale)
- https://www.mdpi.com/2073-8994/16/12/1678 (Miller–Abel–Valkov–Fraser 2024 'Implementing the MOLS table for n up to 500': HTTP 403, so the current small-n MOLS table was not read)
- https://onlinelibrary.wiley.com/doi/abs/10.1002/jcd.21298 (Todorov 2012, 4 MOLS(14): HTTP 403)
- https://dl.acm.org/doi/10.1016/j.disc.2009.03.035 (Markström, 4-uniform K5 Turán numbers for n<=16: HTTP 403). No verified table of small open hypergraph Turán cells was found, so no hypergraph Turán cell is reported
- https://sites.google.com/site/dmgordo/diffset (old La Jolla DS page renders empty; the GitHub datasets dmgordo/* were used instead)
- Colbourn–Dinitz Handbook MOLS table itself (not online); the only N(n) table read is the Colbourn–Dinitz 'N(n) and ν(n)' PDF, whose references end in 1996
- BIBD/Steiner t-design tables beyond S(2,6,v): no current online table of open (v,k,λ) BIBD or small t-design cells was found (the ScienceDirect r<=41 table was not fetched)
- distributed.net OGR-28 blog: facts taken from search snippets, page not opened

**Scout 5 (C4 OEIS sweep):**
- https://oeis.org/history/view?seq=...&v=N (individual OEIS revision views need a login, so last-term dates come from the %E/extensions field, the public history list page, and the entry's created/time stamps)
- erdosproblems.com (not fetched: 0 of the 10-page budget used; the local mirror /work/problems/erdosproblems/data/problems.yaml was grepped only for Heilbronn #507)
- arXiv 2511.02864 (AlphaEvolve-scale 'Mathematical exploration and discovery at scale') and arXiv 2606.26399 (Geometry-Aware MCTS): seen in search results only, not read
- No ILP/CP solver (ortools, highspy) in ~/.venv-automath, so no pilot runs were made; all feasibility estimates are guesses

**Scout 6 (C5 conjecture datasets):**
- http://cms.uhd.edu/faculty/delavinae/research/wowII/all.html (ECONNREFUSED on 443 and via curl; used Wayback snapshot 2026-07-23 instead)
- AIM Pólya–Schur–Lax (Borcea–Brändén) problem list: guessed URL aimath.org/pastworkshops/polyaschurlaxproblems.pdf returned an HTML page, list not read
- House of Graphs conjectures/counterexample pages: only search snippets, not fetched
- 'Conjectures in graph theory' wiki: not fetched
- erdosproblems.com 10-page budget used on pages 64, 993, 617, 23, 647, 1082, 97, 488 and forum threads 617 and 97. Pages 982, 114, 583, 743, 128 and forum threads 488 and 993 were not read.
- Local problems.yaml has no statement text, only status and tags, so the 'probably false' grep ran only on the FC Lean docstrings (few hits)
- Wolfram MathWorld page did not state how far Hamiltonicity checks of the VT census extend
