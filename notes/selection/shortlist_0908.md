# Slot-2 selection pass — 2026-09-08 (Opus 5)

Context: #708 is at rest. Four Pro runs and one Astra run produced refereed structure but no uniform improvement; the hinge/LP route is capped at 4n and the incidence route gives 3n on the obstruction family; the only queued milestone is the Section 18 formalisation, waiting on the Astra pool reset (14 Sep 21:38). So slot 2 needs a different problem.

## The filter I actually applied
Our demonstrated edge is **certificate design plus exact verification plus formalisation**: on #708 we moved an explicit constant 81 → 12 by redesigning rounding schemes and certificates, verifying every constant in exact rational arithmetic, and kernel-checking the chain. Our demonstrated NON-edge is **raw compute**: we cannot out-SDP or out-search an established group. So the filter is:
1. statement pinned to the primary source; 2. importance (named, priced, or a quantified frontier); 3. **G2 first**; 4. the bottleneck must be certificate/structure design, NOT compute; 5. partial results publishable as explicit constants or new sufficient conditions; 6. Lean-formalisable; 7. not crowded.

G2 tools run: `tools/vm_g2.py` against the refreshed VibeMathed dataset (701 problems, 2026-09-08) and `tools/sfm_g2.py` against Star Fleet — **zero hits for every candidate below**; erdosproblems pages read for comment and proof-claim counts; targeted web search for the current record.

## Candidates

### 1. Erdős #375 — Grimm's conjecture  ✗ DISPATCHED AND DROPPED THE SAME DAY (see the post-mortem at the end)
**Statement** (erdosproblems.com/375, FALSIFIABLE): for any n, k ≥ 1, if n+1, …, n+k are all composite, are there distinct primes p_1, …, p_k with p_i | n+i?
**Importance**: Grimm 1969; Guy B32; implies p_{n+1} − p_n < p_n^{1/2−c}, hence Legendre's conjecture — so the full statement is out of reach and only explicit partial results are on the table, which is exactly our shape.
**Known**: trivial for k ≤ 2; Grimm k ≪ log n/log log n; Erdős–Selfridge k ≤ (1+o(1))log n; Ramachandra–Shorey–Tijdeman 1975 k ≪ (log n/log log n)³ via Baker's theory; Laishram–Shorey 2006 verified all k for n ≤ 1.9·10^10; Laishram–Murty 2012 via smooth numbers.
**G2**: VibeMathed 0, Star Fleet 0, 6 comments and 0 proof claims on the site; the last substantial advance is 1975 with refinements in 2008–2013. **Quiet.**
**Why our machinery fits**: Grimm is a system of distinct representatives on the bipartite graph of the interval's integers against their prime divisors — the same object as the incidence graph we proved theorems about this week. Hall's deficiency is exactly what our cycle-rank estimate d = s − ν ≤ max(0, β−1) controls, with β = Σ_i ω(n+i) − |P| + c. A publishable partial result is a new **explicit, checkable sufficient condition** for the interval, or an explicit non-asymptotic form of RST, neither of which needs Baker's theory or heavy compute.
**Lean**: the statement is elementary and finite for fixed n, k; a sufficient condition would formalise.
**Cost**: one Pro run plus one referee; the machinery is already written down.

### 2. Erdős #167 — Tuza's conjecture  ★ RUNNER-UP, held
**Statement** (erdosproblems.com/167, FALSIFIABLE): if G has at most k edge-disjoint triangles, can it be made triangle-free by deleting at most 2k edges?
**Importance**: Tuza 1981; K_4 and K_5 show 2k is optimal.
**Known**: trivial 3k; Haxell 1999 (3 − 3/23 + o(1))k = (66/23)k ≈ 2.8696k; Kahn–Park for random graphs. **G2 CAUGHT A STALE PAGE**: the site (last edited 13 Oct 2025) still quotes Haxell, but arXiv 2608.23010 (2026) improves this to (63/22)ν ≈ 2.8636 via 2-colourable triangle families. Any brief must target 63/22, not 66/23.
**Fit**: excellent in kind — τ ≤ cν is an LP relaxation plus rounding, our core competence this week, and a rational certificate is exactly verifiable.
**Why held**: the area is ACTIVE (a 2026 improvement), so collision risk is real and beating a fresh result in one run is unlikely. #708 succeeded partly because nobody else was there. Reconsider if a structural idea appears.

### 3. Erdős #128 — Erdős–Rousseau sparse halves, $250
**Statement**: if every induced subgraph on ≥ ⌊n/2⌋ vertices has more than n²/50 edges, must G contain a triangle? The constant 50 is optimal (C_5 blow-up, Petersen).
**Known**: true with 50 replaced by 16 (Erdős–Faudree–Rousseau–Schelp); Krivelevich with n/2 → 3n/5 and 50 → 25; Keevash–Sudakov under extra hypotheses.
**G2**: VibeMathed 0, Star Fleet 0; 6 comments, 0 claims.
**Why not first**: the modern attack is flag algebras and SDP, i.e. compute-bound, which is our weakness. Only worth it if we first find a certificate formulation that avoids a large SDP.

### 4. Erdős #23 — Erdős–Faudree–Pach–Spencer
**Statement**: can every triangle-free graph on 5n vertices be made bipartite by deleting at most n² edges? The C_5 blow-up shows n² is optimal.
**Known**: Balogh–Clemen–Lidický 2021 give 1.064n².
**G2**: VibeMathed 0, Star Fleet 0; 3 comments, 0 claims.
**Why not first**: same flag-algebra/SDP bottleneck as #128.

### 5. Erdős #779 — Deaconescu  ✗ REJECTED
P the product of the first n primes; is there always a prime p with p_n < p < P and P + p prime? Verified n ≤ 1000; the heuristic failure probability is exp(−n^{cn}). There is no partial result anyone can prove short of major analytic input, and extending the verification is pure compute. Rejected on fit.

### 6. Erdős #458 — lcm inequality  ✗ REJECTED
Is [1,…,p_{k+1}−1] < p_k[1,…,p_k] for all k? Erdős and Graham call it "almost certainly true, but the proof is beyond our ability", and it needs Legendre-strength input on prime gaps. Rejected on fit.

## Decision
Dispatch **#375 Grimm** to the web GPT-6 Pro seat, with the target delimited as a new explicit sufficient condition or an explicit non-asymptotic bound — NOT the full conjecture, which provably implies Legendre. Hold #167 Tuza as the runner-up pending a structural idea that avoids competing on SDP size. Revisit #128 and #23 only if a non-SDP formulation appears.


## Post-mortem, 2026-09-08 17:1x — Grimm dropped, and the filter is now sharper
The G1 run proved, correctly and honestly, that n ≥ lcm(1,…,k−1) suffices, i.e. k ≤ 2 + log n/log 4 ≈ 0.72 log n, by an elementary anchored-prime-power argument; I verified its two lemmas and its sufficient condition myself. It is nevertheless **weaker than Erdős–Selfridge (1962) and far weaker than Ramachandra–Shorey–Tijdeman (1975) in every regime**, and its only advantage — explicitness — is neutralised because Laishram–Shorey verified every k for n ≤ 1.9·10^10 computationally. Nothing publishable.
**The mistake was mine, and it is a filter defect, not a bad run.** I checked that our machinery APPLIES to Grimm (incidence graph, Hall deficiency, cycle rank — all genuinely relevant) but not that it applies AT THE FRONTIER. The frontier of Grimm is Gelfond–Baker theory; our tools reproduce the 1969-level range and stop. That is the same failure mode for which I had already rejected #779 and #458.
**Added to the filter as step 4b: identify what the CURRENT RECORD's proof actually uses, and reject the problem unless our machinery can plausibly operate on that, not merely on the problem's statement.**
Consequence for the ranking: #167 Tuza rises to first, because its record genuinely comes from fractional relaxation plus rounding plus local structure, which is our machinery. But it must not be dispatched until the 2026 improvement to 63/22 (arXiv 2608.23010, "An improved upper bound for Tuza's conjecture via 2-colorable triangle families") has been read, so that the brief targets the real frontier and the real method. Dispatching against an unknown frontier is exactly what went wrong here.


## Tuza frontier read, 2026-09-08 17:5x — DISPATCHED
Applying the new step 4b before dispatching, I read arXiv 2608.23010. Current record τ ≤ (63/22)ν, improving Haxell's 66/23. Method: Haxell fixes a maximum independent family of triangles, classifies by type, and proves four lemmas bounding τ against ν and the sizes of certain subfamilies; the 2026 note adds one ingredient, that a "2-colourable" family (each triangle with one edge outside E(B') and two inside) satisfies τ(F) ≤ (1+√3)ν(F), obtained from combining τ ≤ 3ν − |B_1| with τ ≤ 2ν + τ(F_R). **The paper contains no case enumeration, no flag algebras and no semidefinite program — it is purely analytical**, and the final constant comes from a linear combination of the four lemmas with coefficients (5/2, 1, 11/2, 2) which the paper does not justify as optimal.
That is our machinery exactly, and there are three visible sources of slack: the combination is a small LP that can be solved exactly in rationals with a dual certificate; the substitution uses the rational approximation 11/4 = 2.75 where the proved constant is 1+√3 = 2.73205…; and the 2-colourable recurrence itself has only two inputs. There is also a stated ceiling for the whole route, 54/19 ≈ 2.8421, because K_4 is 2-colourable with τ = 2ν — a barrier of exactly the kind we proved for #708 and equally publishable.
**Dispatched as T1**, with the brief warning that my description of Haxell's framework is second-hand and must be re-derived before anything is built on it — the day's other lesson — and requiring exact rational certificates with written-out dual multipliers so that no solver is needed to verify.


## Tuza post-mortem, 2026-09-08 18:4x — dropped, and the G2 step is amended again
T1 reconstructed Haxell's framework, solved the combination LP exactly with primal and dual certificates, and derived f(c) = (12c+30)/(4c+11) — which reproduces 66/23 at c = 3, 63/22 at c = 11/4, 54/19 at c = 2, and (162+4√3)/59 at c = 1+√3. I verified every one of those in exact arithmetic. The mathematics is right and the certificates are complete.
**It is nevertheless worthless, because arXiv 2608.23010 already contains the sentence "In fact, directly applying the constant 1+√3 in Theorem 1 yields the sharper bound τ(G)≤(162+4√3)/59·ν(G), at the cost of elegance."** Confirmed by two independent targeted fetches. The slack I identified had already been taken by the authors, one paragraph after the theorem I read.
**Amendment to the filter, step 4c:** when the plan is to exploit slack in a published proof, read the paper's own remarks before dispatching — the "in fact", "one can do better", "at the cost of" sentences and any concluding section — because that is exactly where a sharper-but-uglier constant is recorded. And never base a dispatch on a summary of a paper when the dispatch depends on what the paper does or does not contain.
**Status of slot 2:** both candidates dispatched today are dropped. #128 and #23 remain held on the SDP-fit objection. The next dispatch waits until the amended process has been run end to end on a candidate, including reading the current record's actual text.


## Amended process run end to end on #128 and #23 — BOTH REJECTED, 2026-09-08 19:4x
This is the first use of steps 4b and 4c before a dispatch rather than after.

**#128 (Erdős–Rousseau sparse halves, $250) — REJECTED on three independent grounds.**
Current record read from the primary page, not a summary: Razborov [Ra22] proved the statement with 1/50 replaced by **27/1024 ≈ 0.0263672**. Razborov is the inventor of flag algebras and this is a flag-algebra result, so the frontier is exactly our non-edge (step 4b). Worse for us, the page shows **one proof claim already lodged**: a partial claim by Amir Sarid, produced with GPT-5.6 Sol and Claude Fable 5, asserting **0.0262 n²** — an improvement on Razborov obtained by a flag-algebra argument in the dense case plus a perturbation argument in the sparse case. Two further users (Sam_Petkov, Aurelien_Col) are marked "currently working on" and "working on formalising". So the problem is simultaneously at an SDP frontier, already under AI-assisted attack by another team, and crowded. Nothing about our machinery beats a flag-algebra pipeline here.

**#23 (Erdős–Faudree–Pach–Spencer) — REJECTED on the frontier ground.** The record 1.064n² is Balogh–Clemen–Lidický 2021, a flag-algebra group using the same machinery. Same objection as #128; no dispatch.

**Conclusion: the whole "famous explicit-constant graph problem" class is closed to us**, because in graph theory the explicit-constant frontier is held by flag algebras and semidefinite programming, which is compute, and we cannot outspend the incumbents. That is a class-level verdict, not a verdict on two problems.

## The class we should target instead, with the reasoning
The one line that worked, #708, had a property none of today's candidates has: **before we started, the literature contained no bound depending only on n at all.** The thin literature is what left 81n → 12n on the table in two days. Every famous prize problem has the opposite property.
So the search should be for **thin-literature problems with an explicit constant**, not for famous ones. Concretely, the screen for the next selection task is:
1. open, and neither in the VibeMathed dataset nor claimed on Star Fleet;
2. **zero proof claims and nobody marked "currently working on"** — the #128 lesson, and it is visible on the page;
3. a short reference list on the problem page, i.e. the problem has attracted few papers;
4. the page contains an explicit bound or constant, so partial progress is publishable;
5. the current record's proof, read in its own text, is combinatorial or certificate-shaped rather than flag-algebra, SDP, analytic or brute-force;
6. the statement is finite or elementary enough to formalise.
The local database (problems/erdosproblems/data/problems.yaml, 1217 problems) supports criteria 1 and 6 offline: **591 open, of which 323 are already marked formalisable**, with tags dominated by number theory (309), graph theory (114), Ramsey theory (60), geometry (54), additive combinatorics (49). Criteria 2, 3 and 5 need the problem pages themselves, which is the next selection task's work — and it must be done BEFORE any dispatch, which is the whole lesson of today.
