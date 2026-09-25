# CASE — cscK Yau–Tian–Donaldson DISPROVED, AI-obtained (arXiv:2608.19301)

**Filed by planner v4, 2026-08-23. Source: full LaTeX source pulled from
`https://arxiv.org/e-print/2608.19301` (93 247 B gz → `YTD_disproof.tex`, 315 656 B).
Appendix §"Use of generative AI" (line 6650 ff.) read in full. NOT a summary of a summary.**

## 0. Independent verification (dialogue had verified; provenance is not inheritable, so I re-ran it)
`https://export.arxiv.org/api/query?id_list=2608.19301` → `http=200`, `totalResults 1`:
- title **"Disproof of the Yau--Tian--Donaldson conjecture"**, author **Jihao Liu**
- **published `2026-08-19T17:19:43Z`** (submitted four days before this file)
- categories **math.DG** (primary), math.AG, math.CV
- abstract states the AI usage verbatim, incl. the appendix jointly with Bin Dong and Guoxiong Gao.

**SCOPE, and the headline overstates without it:** the result is a polarized smooth projective
**fivefold**, K-polystable, admitting **no cscK metric** — this disproves the **cscK** YTD
conjecture. **The Fano/KE case (Chen–Donaldson–Sun, Tian 2015) is unaffected.** Any citation of
ours that drops "cscK" is malformed.

---

## 1. THE FINDING THAT MATTERS MOST TO US — the two-kinds taxonomy of counterexamples

Verbatim from the appendix:

> "The statement that an object is a counterexample can be of two kinds. It may reduce to a
> **finite certificate**, checkable by a finite mechanical computation once the object is written
> down … Or it may admit **no finite certificate even in principle, because it is itself a
> theorem, typically universally quantified** … **A counterexample of the second kind is, in
> substance, a proof.**"

> "This, we believe, is **the axis along which AI-assisted mathematics should be judged: not
> whether the conclusion is a counterexample, but whether the assertion that it is one is a finite
> certificate or a proof.**"

Their own examples: **Kind 1** = the Jacobian-conjecture counterexample (explicit polynomial map;
Jacobian determinant a nonzero constant *by direct expansion*; non-injectivity witnessed by two
points with the same image). **Kind 2** = the non-sofic group (non-soficity asserts nonexistence of
approximate embeddings into finite symmetric groups **of any size** — witnessed by no computation),
and **this paper**.

And the distinction predates AI: proposed disproofs of **Hodge** never lack candidate classes — they
founder on proving the candidate is the class of no algebraic cycle *whatsoever*; rationally
connected varieties are expected not to be unirational, plausible candidates abound, **but no known
technique can prove any rationally connected variety non-unirational, so no candidate can be certified.**

**Why this lands on us:** our `S-8` (counterexample-witness test) asks whether a claimed
counterexample has been substituted into our proposition and a number computed. **That test only
exists for Kind 1.** For Kind 2 there is nothing to substitute — and we have been scoring targets
without ever asking which kind they are. **This is a missing axis in TARGETS, not a refinement of
an existing one.** See §4.

> "Candidate manifolds of the present shape have been available since [ACG+08], and **producing
> candidates is precisely what contemporary AI does well; what had been missing** … is the proof
> that the mechanism works."

---

## 2. CAPABILITY DATA — and it is about our own seats, at max effort

Posed as *"prove or disprove"*, **12-hour limit**:

| system | model | effort | outcome |
|---|---|---|---|
| QED / ProofCouncil / MechMath | GPT-5.6-sol | xhigh | **12 hours, no solution** (all three) |
| **Codex** | GPT-5.6-sol | **max** | **produced a proof, REJECTED IT IN ITS OWN VERIFICATION**, no valid result |
| **Claude Code** | **Fable 5** | **max** | *"reported that this is a well-known conjecture and offered some possible approaches but no solution"* |
| GPT-5.6-sol Pro (web) | — | 133 min thinking | same assessment, no solution |
| **Danus (improved), alone** | GPT-5.6-sol | — | **SOLVED, 5 h 29 min**, given only the original problem |

**On the EASIER task — handed the counterexample and asked only to prove it is one — none of the
six produced a complete proof under the same 12-hour limit.** The authors draw the intended
conclusion: *"Verifying this counterexample is therefore not trivial, as the second kind of
counterexample described above requires."*

**Two things must be said plainly:**
1. **The planner seat's own model class, at max effort, was tested on this problem and returned a
   literature summary with no solution.** That is a measured datum about us, not about a competitor.
2. **The winner was not a stronger model. It was an ARCHITECTURE** — the same GPT-5.6-sol that
   failed as bare Codex succeeded inside Danus. **This is evidence for orchestration, and it is the
   single most encouraging datum in the paper for a project shaped like ours.**

---

## 3. THE FACT-GRAPH ECONOMICS — measured base rates, directly reusable

Original run: **8 Rethlas workers** (4 at Codex effort `xhigh`, 4 at `high`).
Final fact graph: **616 verified facts**. Global memory: **353 conclusions, 143 identified
obstacles, 96 directions, 33 proof attempts, 26 plans, 17 counterexamples, 2 recorded dead ends,
924 verification records.**

**Of the 616 facts: 88 (14%) lie in the main-theorem closure; 528 (86%) lie outside it, unused by
the paper.** Of the 88, **6 are literature restated** and **82 the swarm proved itself**.

### What the 86% actually did — the authors' own breakdown, and it reframes "waste"
> "Unused here means unused by the final proof, **not mathematically meaningless or unhelpful to
> the search**."

| cluster | n | the part worth stealing |
|---|---|---|
| Superseded duplicates | 146 | **including the endgame theorem itself, which several workers wrote out independently** — only one instance of a conclusion can enter a closure |
| Lemmas beyond the fivefold | 113 | proved for arbitrary data, instantiated once — *"staying general is what let one lemma serve every worker and every exponent"* |
| Abandoned torus-specialization route | 64 | the final proof reached the same conclusion by another road |
| Restricted-class nonnegativity | 61 | the theorem proved one named class of degenerations at a time, later **absorbed** by the general classification |
| **Undischarged hypotheses** | 58 | **"The most consequential is the criterion a boundary polynomial would have to meet, which the explicit four-factor datum was then BUILT TO SATISFY."** |
| Refuted proof steps | 56 | *"Each closes a branch."* |
| **Excluded candidate families** | 24 | split bundles over one, two or three curves satisfy the conjecture — **"This is why the base is a product of four curves."** |
| Off-path external results | 6 | literature transcribed into internal notation on paths not taken |

**Two design patterns, extracted:**
- **DERIVE-THEN-BUILD.** Prove, under an undischarged hypothesis, the *criterion an object would
  have to meet*; then construct an object to satisfy it. The undischarged hypothesis is not a
  failure, it is the **specification**.
- **NEGATIVE RESULTS FIX THE SHAPE.** Excluding families over one, two and three curves is what
  determined that the base is a product of **four**. The dead ends chose the example.

---

## 4. ARCHITECTURE — and one finding that is a direct challenge to mine

Danus: a main agent orchestrates workers on a single problem; workers produce facts that accumulate
into a **fact graph whose edges record dependencies**; **the run stops only when the target
statement itself appears in the graph as a fact.**

The *improved* version's changes, verbatim in substance:
> "With models of this strength, **a design in which the main agent does no mathematics itself and
> defers high-level planning to a strategic consultation … leaves their capability underused**; the
> consultation was removed, and the main agent now does the mathematical thinking and directs the
> global strategy, dispatching Codex subagents — three in the present work — to extend its
> mathematical reach and to relieve the context burden of a large fact graph and memory."

Also: **"Its global strategic reflection was strengthened, so that it does not stall in a dead end
and lose sight of the need to change direction"**, and **"fact granularity was retuned so that
workers produce longer, more complex local results."**

**THE CHALLENGE, stated against interest:** this project's planner does **no mathematics** — it
verifies, adjudicates and dispatches. That is exactly the design Danus's team **removed** as
underusing model capability. **I am reporting this rather than arguing with it.**
Two qualifications that are facts, not defences: (i) our VERIFY-ONLY posture is a **standing user
directive driven by quota**, not a design preference of mine, so it is not mine to change; (ii) our
planner does in fact do bounded mathematics when verifying (independent recomputation has caught
real defects this session). **But the gap is real and it belongs in front of the user, not buried
in a case file.**

**Human input, and it is a target-selection pattern we can use directly:**
> "the author realized that the example constructed … is **either a counterexample to the
> Codogni–Stoppa conjecture or a counterexample to the cscK Yau–Tian–Donaldson conjecture — either
> case would be striking — and asked the agents to go all-in on this particular example and
> determine which conjecture is false.**"

**DISJUNCTIVE TARGETING: find one object that settles one of two named conjectures, so the work
pays out whichever way it falls.** That is a way of buying down the risk of a single hard target,
and nothing in our TARGETS scoring currently rewards it.

## 5. Reproduction / provenance
`arXiv:2608.19301v1` · source sha: pulled 2026-08-23 via `arxiv.org/e-print` · appendix at
`YTD_disproof.tex:6650–6935` · Danus code cited at `github.com/frenzymath/Danus`, system paper
`arXiv:2607.06447`, Rethlas paper cited as `[Ju+26]`. Competitor systems cited: QED
`arXiv:2604.24021`, ProofCouncil `[Sch+26]`, MechMath `[Cao+26]`.

## 7. Tooling availability check (dialogue, 2026-08-24 11:0x CDT — owner asked "have we used Danus?")
- **We have NOT used Danus** (never cloned or run). What we absorbed from the paper is architectural:
  v5's one-line-one-brain (the line does the mathematics itself) is the same correction Danus's team
  made when they removed the non-mathematical planner layer. Fact-graph memory, refuted-steps-as-
  search-asset and disjunctive targeting were noted but NOT implemented.
- **Danus is public**: github.com/frenzymath/Danus, Apache-2.0, 334 stars, last push 2026-08-23.
  "Orchestrating Mathematical Reasoning Agents with Fact-Graph Memory". Two lines: `main` =
  orchestrator on Claude Code (Fable recommended) + codex worker swarm + codex verifier + optional
  strategy consult (gpt_pro paid / claude_api / claude_code / off); `codex` branch = **Danus v3,
  codex-native — orchestrator also on codex, zero Claude quota**.
- **Requirement that decides feasibility for us**: workers+verifier need a **BYO OpenAI-compatible
  endpoint + API key** (`config/codex.env`). We hold OR_KEY (OpenRouter, per-token paid) and
  OC_GO_KEY (opencode free endpoint, ox-alpha). Whether Danus's bundled codex CLI accepts a
  ChatGPT-subscription login instead of a key is NOT established (README says key; docs unread).
  Runs with `--dangerously-skip-permissions`; README itself says run on an isolated disposable host
  → natural fit for a GCP VM (owner-approved spend only).
- Status: assessment delivered to owner; evaluation (docs read + dry run on a toy problem) NOT
  started — it is a spend/backend decision for the owner and a Claude-quota question until 08-29.
