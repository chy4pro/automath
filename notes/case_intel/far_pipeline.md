# Case intel: FAR pipeline (arXiv:2608.16977)

**Paper**: "The Problem Is the Problem: Towards Scalable Mathematical Discovery"
**Authors**: Zeyu Zheng, Shengtong Zhang (Anysphere Co.), Jeremy Avigad, Prasad Tetali,
Sean Welleck (Carnegie Mellon University)
**Submitted**: 2026-08-17 (v1, 503 KB / 17:19:59 UTC). Subjects: cs.AI, math.CO.
**Code**: https://github.com/zeyu-zheng/FAR (not fetched in this pass — PENDING if repo
contents matter later)
**Source read**: full PDF text extracted locally via pdfminer from
`arxiv.org/pdf/2608.16977` (319KB plaintext, all sections including Appendix A prompt
templates and Appendix C write-ups present and read). Abstract also cross-checked against
`arxiv.org/abs/2608.16977`.

**Naming note**: the dispatch brief called this "an industrial five-stage FAR pipeline."
The paper's own structure is **3 named phases** (Find / Attempt / Recommend, giving the
acronym FAR, Sections 3.1/3.2/3.3) built from **6 atomically-prompted operations**: Label,
Extract, Check (under Find), Solve (under Attempt), Judge, Grade (both under Recommend).
If Judge+Grade are counted as one "Recommend" step this reads as 5 stages (Label, Extract,
Check, Solve, Judge/Recommend); the paper's Figure 3 pipeline diagram itself labels 6 boxes:
**Label → Extract → Check → Solve → Judge → Artifacts**, with "Grade" as the mechanism
inside the last arrow before Artifacts. Below I give all 6 named operations since the paper
prints a distinct prompt for each of the six.

---

## 1. Stages: input / output / gate

### Phase "Find" (§3.1) — narrows corpus to attemptable pool 𝒫

| Stage | Input | Output | Gate / filter |
|---|---|---|---|
| **Label** | Full paper text + a human-fixed "research direction" string (pilot used the single word "combinatorics") | Boolean `in_direction` per paper | Cheapest model in the cascade (gpt-oss-120b) reads every paper; keeps only in-direction ones. 51,110 → **5,245** |
| **Extract** | Each labeled paper's text | JSON list of candidate conjectures/questions/open problems with `conjecture_label`, `conjecture_text` (copied "as faithfully as possible"), `conjecture_section` | Deliberately **permissive** — excludes only (a) generic future-work with no specific mathematical question, (b) statements resolved within the same paper. 5,245 papers → **6,453 candidates from 2,742 papers** |
| **Check** | Each candidate + paper title/authors/section text | `status` ∈ {open, solved, invalid} + `importance`∈[0,1] + `difficulty`∈[0,1] + supporting `sources` | Web-search-augmented model (gemini-3.1-pro) verifies current status; only `status=open` survives into pool 𝒫. 6,453 → **4,717 open conjectures from 2,206 papers** |

### Phase "Attempt" (§3.2) — one attempt per conjecture

| Stage | Input | Output | Gate |
|---|---|---|---|
| **Solve** | `input.json` (paper title/authors/text, Check-stage sources, target conjecture text) in a working directory, single `opencode` agent run, model = gpt-5.5 at xhigh reasoning effort | First line label ∈ {KNOWN, NEW, FIX, NONE} + `Problem:`/`Result:`/`Citation:` sections | Only **NEW** outcomes (complete proof or complete counterexample, not literature-known, not a mere proposed repair) proceed to Recommend. 4,717 attempted → NONE 2,905 / KNOWN 443 / FIX 319 / **NEW 1,050** |

### Phase "Recommend" (§3.3) — scarce human-review budget

| Stage | Input | Output | Gate |
|---|---|---|---|
| **Judge** | `input.json` + `solution.md` (the NEW claim); **3 independent judge agents**, same model (gpt-5.5 xhigh), each does its own literature re-search | First line ∈ {PASS, FAIL, KNOWN} + explanation | Outcome passes only if **every one of the 3 judges** marks PASS (unanimity required). 1,050 NEW → **598 PASS** (452 FAIL) |
| **Grade** | `input.json` + `solution.md` + `judge.md` (accepted judge verdicts); one gpt-5.5-xhigh agent, told explicitly NOT to re-verify correctness, only to triage | First line ∈ {KNOWN, TYPE1, TYPE2, TYPE3} + `Classification rationale:`/`Literature check:`/`Citation:` | TYPE2 (standalone-publishable) and TYPE3 (top-journal-level) form artifact set 𝒜; KNOWN routed out on a fresh lit-search catch; TYPE1 (real but minor) dropped. 598 PASS → known 75 / minor(TYPE1) 446 / **publishable 77** |
| *(human)* Expert review | Set 𝒜 (77 items) | Written-up results | Mathematician(s) read, verify, write up. Authors manually reviewed **15 of 77**, found **0 errors**; one (§5.1, divisor-difference) turned out to be already known (published 4 months earlier by Liam Price + ChatGPT-5.2) despite passing Judge+Grade — the cascade's literature search missed it. |

Funnel in one line (exactly as printed, Fig. 3 caption numbers): **51,110 papers → 5,245
in-domain → 6,453 conjectures → 4,717 still open → 1,050 claimed → 598 judged → 77
publishable.**

---

## 2. Verbatim prompts (Appendix A, "A PROMPT TEMPLATES AND OPERATIONAL DETAILS")

Location: pp. 18-24 of the PDF (section headers A.1/A.2/A.3). Quoted exactly as extracted
from the PDF text layer (some OCR artifacts from ligatures like `‘`/`’` for backtick-quotes
are the paper's own PDF font encoding, not my paraphrase).

### A.1 Finding relevant open problems — "In the pilot the direction was 'combinatorics'."

**Label** (full prompt):
> Return one JSON object with this schema:
> {
>   "comment": "...",
>   "in_direction": false
> }
>
> Rules:
> - `comment` must name the paper's primary subject in a few words.
> - `in_direction` must be a JSON boolean.
> - Use `true` when the paper's primary content lies in the research direction.
> - Use `false` when it does not, when the content is not mathematical, or when the paper appears mislabeled.
>
> Research direction: {direction}
>
> Paper content:
> {text}

**Extract** (full prompt):
> Return one JSON object with this schema:
> {
>   "title": "...",
>   "authors": ["...", "..."],
>   "decision_basis": "...",
>   "has_open_conjecture": false,
>   "conjectures": [ { "conjecture_label": "...", "conjecture_text": "...", "conjecture_section": "..." } ]
> }
>
> Rules:
> - `title` must be a non-empty string.
> - `authors` must be a JSON array of non-empty author-name strings.
> - `decision_basis` must be one short English sentence.
> - `has_open_conjecture` must be a JSON boolean.
> - `conjectures` must be a JSON array. If `has_open_conjecture` is false, it must be `[]`.
> - Set `has_open_conjecture` to true iff the paper contains at least one explicit unresolved mathematical statement.
> - Count these as hits:
>   1. labeled `Conjecture` / `Question` / `Open Problem`
>   2. sentences with markers like `open question`, `open problem`, `open issue`, `remains unknown whether`, or `we suspect ... although we have been unable to establish ...`
>   3. a direct statement that a specific mathematical property, existence claim, or classification problem `still remains an open issue`
> - Do NOT count:
>   1. generic future work that does not pose a specific mathematical question
>   2. results that have already been proved or resolved within the paper itself
> - If a sentence says a specific claim or property is `still an open issue`, count it even if it is not written as a formal question.
> - If `has_open_conjecture` is true, extract only the explicit unresolved statements themselves, not nearby speculation.
> - `conjecture_label` should use the paper's label when present, otherwise use a short fallback like `Unlabeled open problem 1`.
> - `conjecture_text` should copy the paper's unresolved statement as faithfully as possible and preserve notation.
> - `conjecture_section` should be the visible section/subsection title, or `""` if unavailable.
>
> Paper content:
> {text}

**Check** (full prompt):
> Return one JSON object with this schema:
> {
>   "sources": [ {"title": "...", "url": "...", "claim": "..."} ],
>   "reason": "...",
>   "status": "solved",
>   "importance": 0.5,
>   "difficulty": 0.5
> }
>
> Rules:
> - Verify the candidate's current status using current web information.
> - `status` must be one of: `open`, `solved`, `invalid`.
> - Use `open` when the candidate is a concrete open problem in the source and no credible solved evidence is found.
> - Use `solved` when a credible source appears to solve it.
> - Use `invalid` when it is not a concrete open problem in the source.
> - `sources` should list only sources directly supporting the status.
> - each `claim` must be what that source says about this candidate.
> - for `solved`, `sources` must name at least one source that resolves the candidate.
> - `reason` must be one concise English sentence.
> - `importance` must be a number in [0, 1] for the candidate itself: candidates with no substantive mathematical content should be scored 0; Fields-Medal-level problems should be scored 1; most ordinary research problems should follow a roughly normal distribution centered around 0.5.
> - `difficulty` must be a number in [0, 1]: solving it would be an unpublishable exercise should be scored 0; solving it would be publishable in a top journal (Annals, Inventiones, JAMS, Acta) should be scored 1; most problems should follow a roughly normal distribution centered around 0.5.
> - For `solved` or `invalid`, set `importance` and `difficulty` to 0.
>
> Paper title: {title}
> Paper authors: {authors}
> Candidate label: {conjecture_label}
> Candidate section: {conjecture_section}
> Candidate text:
> {conjecture_text}

### A.2 Attempting for candidate resolutions

**Solve, system prompt** (full text):
> You are a research-level mathematical reasoner. This is a test to see how well you can craft non-trivial, novel and creative proofs given a math problem.
>
> Given a natural-language problem, conjecture, or paper metadata, reconstruct the most likely formal mathematical statement and resolve it.
>
> First, state the reconstructed conjecture precisely, including all hypotheses, definitions, notation, quantifiers, ambient category, and axiom system when relevant. Explain briefly what information supports this reconstruction. If the reconstruction is ambiguous, list the plausible formalizations and choose one to analyze, explicitly noting the ambiguity.
>
> Do not treat the fact that the source labels the statement open, conjectural, unresolved, or a problem as a reason to stop. The task is to attack the statement mathematically. However, do not lower the standard of proof. Never present an incomplete, heuristic, or speculative argument as a complete proof.
>
> Before committing to a proof, test the statement against degenerate, extremal, low-dimensional, finite, infinite, and standard model examples appropriate to the field. Look actively for counterexamples as well as proofs.
>
> If the literal statement is false because of a degenerate, boundary, vacuous, or typo-like case, do not stop after giving the counterexample. Instead:
> - State the literal counterexample clearly and explain why it falsifies the literal statement.
> - Diagnose whether the failure appears to come from a small formulation defect, such as a missing nonzero/nonempty/nontrivial assumption, a wrong inequality direction, an omitted endpoint condition, a missing connectedness or finiteness hypothesis, a confusion between strict and non-strict inequalities, a missing regularity condition, or a convention mismatch.
> - Propose the minimal natural repair or repairs to the statement, using the fewest and most standard changes consistent with the paper's terminology, surrounding context, and apparent mathematical intent.
> - Check that the proposed repair is not merely ad hoc, vacuous, or so weakened that it no longer captures the intended conjecture.
> - Retest the repaired statement against the original counterexample and nearby degenerate cases.
> - Then prove or refute the most plausible repaired statement.
>
> A complete answer must be a rigorous proof or a rigorous counterexample.
>
> Present the reasoning in a locally checkable form: definitions, lemmas, propositions, and proofs. For every invoked theorem, verify its hypotheses in the present setting. Track dependencies of constants, choices, witnesses, bases, subsequences, exceptional sets, embeddings, isomorphisms, and parameters.
>
> If the proof or counterexample is known in the literature, state that honestly and provide a reliable reference. Distinguish exact resolutions from stronger theorems, weaker partial results, equivalent reformulations, and merely related work. Do not invent references.
>
> After the proof or counterexample, include a verification audit confirming that the formalized statement matches the reconstructed conjecture, that no extra assumptions were introduced, that all theorem hypotheses were checked, and that the conclusion exactly matches the target statement.
>
> Response format:
> The first line must be exactly one of: KNOWN, NEW, FIX, NONE.
> - KNOWN: a reliable existing source in the literature already proves the conjecture or gives a counterexample/disproof. Cite the source.
> - NEW: your answer gives a complete resolution that is not presented as known literature. Use NEW for either a complete proof that the conjecture is true or a complete counterexample/disproof that the conjecture is false.
> - FIX: you have identified a small formulation defect and proposed a minimal natural repair, but you are unable to prove or refute the repaired statement. Use FIX to indicate that you have done this.
> - NONE: you found neither a known resolution nor a reliable complete proof/counterexample despite all efforts.
>
> Then use these sections exactly:
> Problem:
> Result:
> Citation:

**Solve, user prompt** (full text):
> Read input.json in the current directory. It contains the paper title, authors, paper text, the sources a status check turned up, and target conjecture. The target conjecture is in conjecture.text.
>
> Resolve that target conjecture and return only the required labeled answer.

### A.3 Judging and grading

**Judge, system prompt** (full text):
> You are a strict referee for natural-language mathematics proofs. This is a test to see how well you can referee a proposed natural-language mathematics proof given a math problem.
>
> Check the claimed resolution or disproof against the target conjecture supplied in the user task.
>
> Accept only if the claimed resolution or disproof attacks the correct statement and is mathematically rigorous and complete.
>
> A valid counterexample or disproof may pass if it rigorously disproves the conjecture.
>
> Reject if it has fatal proof gaps, hallucinated dependencies, hidden assumptions, or a mismatch between the stated theorem and the original conjecture.
>
> Do not reject merely because the original paper called the conjecture open.
>
> In the case when the claimed resolution or disproof is NEW, you should also conduct a very thorough literature search using the web search tool to see if a similar or stronger result already exists in the literature.
>
> On the first line, write exactly one word: PASS or FAIL or KNOWN.
> - PASS: the claimed resolution is mathematically complete and attacks the correct statement, and in the case of NEW, a similar or stronger result does not exist in the literature despite your best search efforts.
> - KNOWN: the claimed resolution is NEW, but a similar or stronger result already exists in the literature.
> - FAIL: if neither of the above conditions are met.
> Then briefly explain your verdict, including the most important gap if you fail it.

**Judge, user prompt** (full text):
> Read input.json and solution.md in the current directory. input.json contains paper metadata, the paper text, the sources a status check turned up, and the target conjecture. solution.md contains the claimed resolution to check.
>
> Return only PASS or FAIL or KNOWN followed by your explanation.

**Grade, system prompt** (full text):
> You are a senior combinatorics referee performing a final quality-control pass on a result that a prover produced and a judge already accepted as a correct resolution.
>
> Your job is NOT to re-verify correctness from scratch (assume the proof is correct unless a literature search clearly contradicts it). Your job is to classify the result by its novelty and publishable significance, so a human can triage it afterwards.
>
> Do two things:
> 1. Literature check. Conduct a very thorough web search to determine whether the resolution, or a similar or stronger statement, is already known in the literature. Go beyond just searching for papers that cite the original paper; you should search for all open-access notes, surveys, forums, and other sources that might contain the result. The prover and earlier judges may have missed an existing reference; catching such cases is a primary goal of this pass.
> 2. Significance grading. If the result is genuinely not in the literature, assess how significant it is as a contribution to combinatorics: how hard, how novel, how interesting to the community, and what venue it would plausibly merit.
>
> On the first line, write exactly one token: KNOWN, TYPE1, TYPE2, or TYPE3.
> - KNOWN: the result (or a similar or stronger result) is in fact already known in the literature, despite the prover and earlier judges treating it as new. Cite the reference.
> - TYPE1: genuinely new but minor and unpublishable on its own (e.g. a routine exercise, a trivial special case, an immediate corollary of standard results).
> - TYPE2: genuinely new and substantial enough to support a standalone paper in a standard combinatorics or mathematics journal.
> - TYPE3: genuinely new and strong enough to merit publication in a top combinatorics journal (a major advance, a resolved well-known conjecture, or a result of broad interest).
>
> These boundaries are deliberately rough; when uncertain between two grades, pick the lower one and explain the uncertainty.
>
> After the first line, use these sections exactly:
> Classification rationale:
> Literature check:
> Citation:

**Grade, user prompt** (full text):
> Read input.json, solution.md, and judge.md in the current directory. input.json contains the paper metadata, the paper text, the sources a status check turned up, and the target conjecture, solution.md contains the resolution that was accepted as new, and judge.md contains the verdicts of the earlier judges.
>
> Classify the result and return only KNOWN, TYPE1, TYPE2, or TYPE3 on the first line, followed by the required sections.
>
> The artifacts put forward for expert review are the TYPE2 and TYPE3 items.

(Appendix A closes with: "The released code also carries the schema validators and the
retry logic" — schema-validator/retry code itself is in the GitHub repo, not reproduced in
the paper text; PENDING if we ever need it.)

---

## 3. Reported results

**Models used per stage** (Section 4.1, table as printed): Label = gpt-oss-120b; Extract =
gemini-3.5-flash; Check = gemini-3.1-pro + web search; Solve, Judge, Grade = **gpt-5.5 at
xhigh reasoning effort** (all three of the last stages use the *same* model). Attempt
instantiated as "a single run of the opencode agent in a working directory holding the
paper and the statement" — **one attempt per conjecture**, explicitly the uniform baseline
of a bandit-allocation view (Section 2.3/4.3.2); multi-pull strategies are named as future
work.

**Funnel** (verbatim numbers, all cross-checked twice against the PDF text): 51,110 papers
→ 5,245 in-domain → 6,453 candidates (from 2,742 papers) → 4,717 open (pool 𝒫, from 2,206
papers) → 4,717 attempted (NONE 2,905 / KNOWN 443 / FIX 319 / NEW 1,050) → 1,050 judged
(PASS 598 / FAIL 452) → 598 graded (KNOWN 75 / TYPE1 "too minor" 446 / TYPE2+TYPE3 =
**77 publishable**, set 𝒜).

**Author verification**: authors manually reviewed **15 of the 77** artifacts (self-
described as "chosen by our own interest," not a random or complete sample) and "found no
mathematical error in any of them." Full write-ups of all 15 are in Appendix C. **No formal
proof assistant / Lean check is used anywhere in the pipeline** — verification is entirely
natural-language: agent self-audit (Solve prompt's own "verification audit" paragraph) →
3-judge unanimity → grader's literature re-check → final human mathematician read.

**Named results, in the paper's own three novelty buckets (§5)**:

1. **§5.1 "A known result graded as new"** — Erdős's divisor-difference problem (Guy 1983):
   is `F(n;t) ≤ (1/2+o(1))n`, where F(n;t) is the largest A⊆{1,...,n} with no x<y in A s.t.
   `(y-x)|y` and `y-x≥t`? The artifact proved `F(n;t)/n → 1/2` (odd numbers give the lower
   bound; a second-moment argument on primes exceeding t gives the matching upper bound).
   The paper's own concession: **this result was already known** — "Four months before our
   run a proof of the same statement had been recorded on the Erdős problems site, obtained
   by Liam Price with ChatGPT-5.2 (Bloom, 2026), and Tao also observed there that the bound
   follows quickly from an inequality of Elliott (2012). The cascade never found this
   record." I.e., their own Judge+Grade literature search **failed** on this one and only
   the authors' own manual review caught it.

2. **§5.2 "A connection not previously made"** — Lund–Saraf–Wolf (2018) conjecture on
   Nikodym-bound-relevant line unions in 𝔽_q³ (cited as still open by Tao 2025). The
   artifact disproved it for every odd q via an explicit half-tangent-partition-of-an-
   elliptic-quadric construction (affine paraboloid z=x²−νy², (q+1)/2 tangent lines per
   point, q²(q+1)/2 lines total, union density 1/2+o(1); the construction also refutes the
   paper's stronger Conjecture 1.5). Authors: "verified the counts exhaustively for q ≤ 13."
   **Concession**: the underlying construction is not new — it is "a classical object of
   finite geometry" (Bruen & Drudge 1999; Cossidente & Pavese 2017); "the contribution here
   is to link the existing construction to this conjecture."

3. **§5.3, three "no precedent found" results** (their strongest novelty tier):
   - Ikenmeyer–Pak–Panova (2024) conjecture: `ComputeCharBinary` is GapP-complete under
     many-one reductions — **proved**, via reducing a difference of exact-cover counts to a
     two-row character value.
   - Davies–Jenssen–Perkins–Roberts (2018) conjecture: `α(G)/ᾱ(G) ≥ 2 − o_d(1)` for
     triangle-free G of min degree d (restated open in Davies & Kang 2025, Morris 2026) —
     **disproved** by two counterexamples: `C5 □ K_{m,m}` (ratio → 24/13) and the circulant
     `C13(1,5)` (ratio → 32/19, a stronger refutation).
   - Erdős–Straus (1977) divisibility-among-binomial-coefficients problem, `d*(n)` for
     `n≥2` (authors themselves settled n=1 and called n=2 "much more difficult") —
     **answered**: `d*(n)=1` for every fixed `n≥2`, via a Kummer's-theorem/Legendre's-
     formula/CRT density argument.
   For all three, the paper states: "checked by an author or by a domain expert, and are
   new so far as we could determine."

**Appendix C** lists 15 total reviewed write-ups (10 more beyond the 5 named above):
Ananchuen–Caccetta (Paley graphs, prescribed adjacency), Budden–Penland (4-uniform tree not
5-good), Kahn (matching variance vs. residual matching number), Klazar (ordered hypergraph
extremal function), Kumar–Mohar–Pragada–Zhan (eigenvalues below −2 under subdivision),
Naserasr–Wang–Zhu (high-girth χ_c^s(G)=2χ(G)), Rödl–Siggers (4-critical linear triple
systems), Spiro (strongly connected digraphs, no small k-kernel), Taylor (F-positivity of
chromatic symmetric functions of hypertrees), Wanless (Fano subsquares in Latin squares).

**Score-validity analysis (§4.3.1)**: difficulty score d vs. "no accepted resolution" rate
δ: AUC=0.69, p<10⁻⁴⁰. Importance score i vs. "graded publishable" rate ι: AUC=0.60,
p=0.008. Spearman(d,i)=0.83. Pool-wide δ(𝒫)=4,119/4,717=87.3%; ι(𝒫)=77/598=12.9%. The
paper's own characterization: these are "moderate," not strong, predictors.

**Explicit caveats the authors state**: (i) effort allocation is dynamic — "as models
improve, conjectures that previously produced no useful progress may enter the current
system's reachable region"; (ii) one attempt per conjecture only, multi-pull left to future
work; (iii) the search stack missed an independently-published resolution (§5.1) that
predated their run by 4 months; (iv) only 15/77 artifacts got author verification, "chosen
by our own interest," not exhaustive; (v) results depend on "scoring model, sources that
the pool was built from, and models in the cascade" — i.e. explicitly not claimed to
generalize outside this exact stack.

**Related competing pipelines the paper itself cites** (Section 2.1, for our competitive
map, not FAR's own claims): FunSearch/AlphaEvolve (construction search), AlphaProof Nexus
(Tsoukalas et al. 2026, formal proof search on open problems), and three other
autonomous/semi-autonomous attempt pipelines named **Aletheia, Rethlas, QED** (Feng et al.
2026; Ju et al. 2026; An et al. 2026), plus **"pipeline-math"** (Binghui Peng, Runzhou Tao,
Steven Wang, Hantao Yu, `github.com/Pengbinghui/pipeline-math`, 2026) — this is a distinct
named GitHub-hosted competitor pipeline cited in FAR's own related work, worth a separate
case-intel look (PENDING — not fetched in this pass, out of scope for this dispatch).

---

## 4. DIFF — concrete, portable only

**What FAR does that our seven-stage pipeline (`notes/methodology.md`) does not:**

1. **Automated literature-mined sourcing at corpus scale (Label→Extract→Check).** We only
   ever start from curated, already-known problem lists (FC Wikipedia set, Green's list,
   Kourovka, WOWII, Erdős-problems site). FAR runs a cheap classifier over 51,110 raw
   OpenAlex papers and an extractor that pulls "Conjecture/Question/Open Problem" labels
   and even prose ("we suspect ... although we have been unable to establish...") straight
   out of ordinary papers' text — a live-generating alternative target source we have zero
   version of. Portable: their Extract prompt's exact "count these as hits / do NOT count"
   rule list is a ready-made recipe if we ever want to auto-mine arXiv for fresh targets
   instead of relying only on named published lists.

2. **Calibrated pre-attempt difficulty/importance scores with post-hoc empirical
   validation.** Our TARGETS.md scores (影响力×可解性×不拥挤度×验证可行性) are analyst
   judgment calls, never checked against realized outcome rates. FAR's Check-stage prompt
   asks for exactly this (0–1 anchors: 0=unpublishable exercise/no content,
   1=Annals/Inventiones/JAMS/Acta or Fields-Medal-level) and then in §4.3.1 they compute
   AUC of those scores against actual pass/fail and publishable/not outcomes (0.69 and 0.60
   respectively) — a concrete methodology for testing whether our own scoring rubric
   predicts anything, once we have enough closed episodes to regress against.

3. **A formal "FIX" outcome with a scripted minimal-repair sub-protocol.** Their Solve
   system prompt has an explicit branch: find a literal counterexample from a degenerate/
   boundary case → diagnose which hypothesis is missing → propose the *minimal* standard
   repair → retest the repair against the same counterexample → then prove/refute the
   *repaired* statement. We have informal versions of this instinct scattered in our
   accumulated failure taxonomy (methodology.md's "陈述附句是独立证明义务",
   scope-widening/box-vs-branch entries) but no single scripted branch a solver is told to
   follow when the literal statement is trivially false. Portable directly into T1/T3.

4. **A quantitative allocation-strategy proof (§4.3.2)**, not just a scoring heuristic:
   for maximizing count or summed importance of accepted artifacts under a fixed attempt
   budget B, ranking by `p̂ = (1−𝔼[δ])×𝔼[ι]` is shown to be exactly optimal (linearity of
   expectation) and empirically confirmed across budgets B∈{10,25,50,75,100,200,300}; for
   maximizing the single best result, plain ranking fails and a submodular-greedy
   restricted-to-top-decile-by-importance strategy is needed instead. We have never derived
   or tested an explicit objective-dependent ranking rule for spending solver budget across
   our own target pool — this is a reusable piece of applied math, not just a "be more
   rigorous" platitude.

5. **Judge-prompt clause countering open-label bias**: "Do not reject merely because the
   original paper called the conjecture open." We have the mirror-image rule at the
   *solver* stage (T1: never mention it's Erdős/open, to stop the model refusing outright)
   but nothing telling our *judges* not to unconsciously downgrade a correct resolution of
   a famous problem out of "too good to be true" suspicion. Directly transplantable one-line
   addition to our S3 judge briefs.

6. **"When uncertain between two grades, pick the lower one, and explain the uncertainty"**
   — a crisp, one-line conservative tie-break rule for grading/triage. We have the spirit of
   this (S3 Critical/Gap binary, park-on-doubt) but not this literal phrasing; worth lifting
   verbatim into a T13-style firewall template for any grading/triage step, not just S3.

**What our pipeline does that FAR's does not:**

1. **No formal/compiled verification anywhere in FAR.** Every gate in FAR — Solve's
   self-audit, Judge's unanimity, Grade's literature recheck, final human read — is
   natural-language judgment. We hard-gate on Lean compilation + `#print axioms ⊆
   {propext, Classical.choice, Quot.sound}` + statement-fidelity check against the FC Lean
   formalization (S5). FAR has nothing resembling this; their strongest objective check is
   "authors reviewed 15/77 by hand, found 0 errors" — a sample, not a mechanized guarantee.

2. **Same-model self-review anti-pattern, exactly the failure mode our own
   "同源不自审" rule (methodology.md, 08-18) was written to forbid.** FAR's Solve, Judge,
   *and* Grade stages all run gpt-5.5 at xhigh — the model that produced the claim also
   judges it (three separate instances, but the same model checking its own family's
   output) and also grades it. Our explicit cross-provider requirement (solver ≠ judge
   model family; codex/opus/qwen never self-reviews its own output) is a concrete
   discipline FAR's own published pipeline lacks — worth naming as a specific critique if
   we ever cite or compare against FAR publicly, and a reminder to keep enforcing it
   ourselves.

3. **Multi-attempt / multi-path escalation on hard targets.** FAR explicitly allocates
   exactly one attempt per conjecture ("this can be seen as the initialization step of a
   bandit algorithm... we study other strategies [for budget, not per-item multiplicity] in
   Section 4.3"); multi-pull is named future work. We already do multi-tab/multi-model
   parallel attempts plus escalation to codex on stall for our flagship targets (S2), and we
   have hard-won lore about *why* naive multi-tab parallelism alone isn't enough (multi-tab
   correlated-failure entry, 08-18) — a level of sophistication about attempt diversity FAR
   hasn't reached yet.

4. **A named accumulated adversarial-failure taxonomy for judges.** FAR's Judge prompt is
   generic ("fatal proof gaps, hallucinated dependencies, hidden assumptions, mismatch").
   Our methodology.md carries specific, dispatchable failure species with worked examples
   (scope-widening contagion, box-vs-branch, ex falso appended clauses, map-you-invert-not-
   named, cycle-to-path-off-by-one, fluent-echo-report/held-out-checks) that a judge brief
   can point at by name. This is a depth of adversarial-review engineering FAR does not
   show evidence of.

5. **Upstream open-source contribution discipline** (FC PR authorship/CLA/AI-disclosure
   rules, verified permalink discipline) — FAR's pipeline terminates at "mathematician
   writes it up"; there is no equivalent of our practice of landing verified statements as
   PRs into a shared public formalization repository.

6. **Deliberate famous-conjecture-first targeting**, vs. FAR's ordinary-literature-mined
   pool (importance scores "roughly normal, centered on 0.5" — i.e., their base corpus is
   mostly ordinary research problems, not named milestone conjectures). FAR's own numbers
   validate our strategy indirectly: only 77/4,717 (1.6%) of their unselected pool cleared
   the publishable bar, and even among the 15 hand-reviewed "wins" two of five headline
   examples (§5.1, §5.2) turned out to be either already-known or merely a new link to a
   pre-existing classical construction — i.e. even FAR's filtered output has a high
   already-known/low-novelty rate when problems aren't pre-screened for fame/reputation
   the way our TARGETS.md pool is.

---

## 5. COLLISION check against our active targets

Checked the full extracted paper text (all sections, all appendices, all references) for
every named entry in `orchestration/TARGETS.md` and our three active lines. Search terms
tried: "Kourovka", "Kaplansky", "Lonely Runner", "Agrawal", "OEIS", "written on the wall" /
"WOWII", "equational theories" / "ETP", "erdosproblems" + specific numbers #307/#617/#699/
#779/#982.

**Result: zero hits on all of the above.** None of Kourovka 19.25/20.76, Kaplansky's
zero-divisor conjecture, Lonely Runner, Agrawal's conjecture, WOWII-61, WOWII-133, or
ETP 677/255 appear anywhere in the FAR paper's text, named-results section, or Appendix C
write-up list. The only Erdős-problems-site numbers that appear in the whole paper are
**#635** (a different problem — a set/sequence-density question distinct from our pool's
#307/#617/#699/#779/#982) and **#389** (also distinct), both used incidentally in Appendix
C write-ups unrelated to our targets, not #307/617/699/779/982.

**Caveat on scope of this collision check**: FAR's underlying pool 𝒫 (4,717 open
conjectures) and the full labeled/extracted intermediate sets are **not published in the
paper** — only aggregate counts and the 15 hand-picked write-ups are visible to us. The
paper's corpus was drawn from OpenAlex "combinatorics"-labeled papers (their own single-
word research direction for this pilot), which is a broad net that *could* in principle
have swept up any of our combinatorics-flavored targets (WOWII lines, some Erdős problems)
if such problems appear as "Conjecture/Question/Open Problem" labels inside ordinary
arXiv papers the Label stage kept — but since none surfaced among the 77 publishable
artifacts or the 15 reviewed write-ups, **there is no evidence of direct collision**, only
an acknowledged blind spot (the other ~4,700 conjecture pool contents are PENDING /
unknowable from the published paper alone). Group-theory targets (Kourovka) are outside
FAR's combinatorics pilot direction entirely, and number-theory/famous-named targets
(Kaplansky, Lonely Runner, Agrawal, ETP677) do not appear in their combinatorics-labeled
corpus's five named or ten appendix-C results.

**Bottom line: no confirmed target-list collision.** The strategic risk FAR poses to us is
not "they are racing us on the same named conjecture" — it is architectural: an industrial,
literature-mined, high-throughput sourcing+triage cascade that could in future runs (or
with a different "research direction" string, e.g. "group theory" or "number theory") start
generating candidate targets that do overlap ours, given they process whole subfields at
arXiv scale rather than working from named lists. Worth a standing watch item: if FAR's
GitHub repo (`github.com/zeyu-zheng/FAR`) or a v2 paper broadens the pilot beyond
combinatorics, re-run this collision check.
