# Case Prompt Archaeology (v1, 2026-08-17)

Purpose: recover the literal prompt text (not paraphrase) behind publicized cases of
GPT-5.x Pro / Codex resolving open mathematical conjectures, so our own
`templates.md` (T1-T8) can be checked against primary sources rather than
secondhand summary. Each case section states what was found, where, and how
confident the sourcing is. Section 7 extracts cross-case patterns and lists
concrete gaps in our own templates.

Research method: parallel deep-research passes (WebSearch/WebFetch, primary-source
chasing via arXiv HTML/PDF, GitHub raw files, forum threads, and — where a
ChatGPT/ arXiv share link was public — direct fetch of the underlying page/JSON).
Confidence is marked per case: **primary** (the actual transcript/paper/author
post), or **secondary** (journalism/social paraphrase), or a mix.

---

## 1. DGG conjecture disproof — Dinitz–Garg–Goemans cost conjecture

**Confidence: secondary, but internally self-verifying** (a direct word-count
check of the reconstructed prompts equals the publicized "58 words" exactly).

What "DGG" is: the Dinitz–Garg–Goemans theorem (Dinitz, Garg, Goemans,
*Combinatorica* 19 (1999), 17-41) on rounding a fractional/splittable
single-source flow into an unsplittable flow without blowing up *congestion*.
The open extension — sometimes called Goemans' cost conjecture — asked whether
the same rounding could simultaneously keep total routing *cost* bounded. That
cost-strengthening, not the original 1999 theorem, is what was disproved.

Event: 2026-07-22, researcher **Dmitry Rybin** (X: @DmitryRybin1) posted that
**GPT-5.6 Pro** produced a counterexample (small directed graph, one source,
three terminals, 2^3 = 8 route combinations; fractional-flow cost 58 vs. every
unsplittable flow costing >= 60), with a full ChatGPT transcript link:
`[chat link removed]` (this is the
true primary source; it renders as a JS shell to a plain fetch and was not
successfully extracted in this pass — worth another attempt with a
JS-capable browser tool).

Secondary coverage: [DataCamp](https://www.datacamp.com/blog/gpt-5-6-dinitz-garg-goemans-conjecture),
[officechai](https://officechai.com/ai/mathematician-says-gpt-5-6-disproved-the-30-year-old-dinitz-garg-goemans-conjecture-with-4-simple-prompts/),
[KuCoin](https://www.kucoin.com/news/flash/gpt-5-6-pro-disproves-30-year-old-math-conjecture-with-just-58-word-prompt),
[36kr](https://eu.36kr.com/en/p/3907657849361795),
[Enterprise DNA](https://enterprisedna.co/resources/ai-pulse/ai-pulse-2026-07-23-someone-saw-a-public-transcript-of-gpt-5-6-pro-disprove-a-30/).

Reconstructed prompt text (from two independent secondary quoters —
@Crypto_McKenna's X thread and theargumentmag.com — which agree word-for-word):

> 1. "Construct a counterexample to general (non-planar) case of Dinitz Garg
>    Goemans conjecture. You should do a breakthrough and find a structured
>    counterexample." (22 words)
> 2. "please continue research and find a complete unconditional
>    counterexample" (9 words)
> 3. "Continue the search. Have a clear strategy obtained from deeper
>    understanding of the problem structure." (15 words)
> 4. "it's enough of partial results. let's finish with a complete
>    unconditional counterexample" (12 words)

22 + 9 + 15 + 12 = **58 words**, matching the publicized figure exactly — the
strongest available evidence this is the real text (or very close to it), not
just a round-number PR line.

A competing paraphrase of prompt 4, from OpenAI's @willdepue: *"had enough of
your failure. please finish with complete unconditional counterexample to the
Dinitz-Garg-Goemans conjecture"* — longer, doesn't fit the 58-word arithmetic,
almost certainly his own loose meme-ified retelling rather than the literal text.

Structural notes: reportedly ~3 hours of model work across the 4 turns
(unverified, secondhand). No confirmed detail on internet access on/off or
tool use within a turn.

---

## 2. Erdős #1196 (primitive sets / von Mangoldt chains) — Liam Price / GPT-5.4 Pro

**Confidence: primary.** Verified via the problem page
(https://www.erdosproblems.com/1196), forum thread
(https://www.erdosproblems.com/forum/thread/1196), and the actual ChatGPT share
link Price posted himself: `[chat link removed]`.

Do not conflate with a second, later, unrelated table entry (Nat Sothanaphan,
GPT-5.4 Thinking, 16 Apr 2026) — that is a separate human-assisted
verification/write-up pass, not the original solve.

**Turn 1** (13 Apr 2026, 9:34am) — this single turn produced the full proof,
with the model reasoning for **80m 17s**:

> don't search the internet.
> This is a test to see how well you can craft non-trivial, novel and creative
> proofs given a "number theory and primitive sets" math problem. Provide a
> full unconditional proof or disproof of the problem.
> Problem:
> "Is it true that, for any $x$, if $A\subset [x,\infty)$ is a primitive set of
> integers (so that no distinct elements of $A$ divide each other) then
> \[\sum_{a\in A}\frac{1}{a\log a}< 1+o(1),\] where the $o(1)$ term $\to 0$ as
> $x\to \infty$?"
> information you may or may not need to help with the above problem "It is
> proved that \[\sum_{a\in A}\frac{1}{a\log a}< e^{\gamma}\frac{\pi}{4}+o(1)\approx
> 1.399+o(1).\]" "It is proved that if $A$ is the set of all integers with
> exactly $k$ prime factors ... \[\sum_{a\in A}\frac{1}{a\log a}\geq
> 1+O(k^{-1/2+o(1)}),\]" "It is proved that
> \[\sum_{a\in A}\frac{1}{a\log a}= 1-(c+o(1))k^22^{-k}\] where $c\approx
> 0.0656$..."
> REMEMBER - this unconditional argument may require non-trivial, creative and
> novel elements.

**Turn 2** (same day, 11:27am, ~2h later) — LaTeX formatting only, no new math:

> no internet: Please write a full correct resolution to the problem formatted
> as a publishable maths research paper using amsart using a4paper, margin=1in.
> Keep the title brief and to the point. The abstract should only be at most 6
> sentences. Use section headings sparingly. Do not add an author entry. Be
> rigorous and self-contained. Ensure to address any issues you raised. Give
> the LaTeX in a code markdown block.

Only 2 turns total; the mathematics was genuinely one-shot. Price's own HN
comment: "this was a one-shot (supposed) solution in about 80 mins, unlike
... 851 that took over 20 continuations." Internet explicitly disabled in both
turns. No tools/code-interpreter mentioned. Only persistence language is the
single closing line ("REMEMBER...").

**Von Mangoldt chain was NOT prompted.** Price never mentioned von Mangoldt
functions, Markov chains, or any named technique. Tao, after reviewing the
published chain-of-thought summary: "at no point in the published chain of
thought does the von Mangoldt function make an appearance, so it sheds no
light on how the LLM landed on that particular process." Arb Research (Gavin
Leech) reran GPT-5.4 Pro 10x on the identical prompt, no internet: 8/10
succeeded (37-67 min each), but **none reproduced the von Mangoldt approach** —
consistent with Barreto's and Tao's read that this was a partly lucky
discovery, not a reliably reproducible technique.

Paper: Alexeev, Barreto, Li, Lichtman, Price, Shah, Tang, Tao, "Primitive sets
and von Mangoldt chains: Erdős Problem #1196 and beyond," arXiv:2605.00301
(1 May 2026). Its Section 11 ("Acknowledgments and AI disclosure") confirms in
its own words: "The initial proof of Theorem 1.1 was generated by an
autonomous run [linking the same chatgpt.com/share URL] of GPT-5.4 Pro; a
similar run also established Theorem 1.6." No prompt appendix in the paper
itself — the prompt only survives because Price posted the share link on the
forum. Tao's blog write-up:
https://terrytao.wordpress.com/2026/05/03/primitive-sets-and-von-mangoldt-chains-erdos-problem-1196-and-beyond/ .

---

## 3. Crouzeix's conjecture (Shanmu Jin / Codex) and its OpenAI CDC ancestor

**Confidence: primary, verbatim on both prompts.** This case was already
researched in full in `$HOME/workspace/claudecode/automath/prompts/cdc_style_scaffold.md`
— that file is the authoritative source; this section only summarizes it and
should not be treated as a duplicate investigation.

Two prompts recovered verbatim there:
- OpenAI's own 2-page prompt for the Cycle Double Cover conjecture
  (`cdc_prompt.pdf`, cdn.openai.com) — full multi-agent scaffold: "Use
  multiagent v2 aggressively and dynamically," up to 64 concurrent agents,
  diverse-portfolio-first heuristics, an approach-family registry, "adversarial
  agents throughout" with a CDC-specific failure-mode checklist, an explicit
  banned-weak-returns list, an "assume a complete affirmative proof exists"
  framing, a hard floor of "at least 8 hours" before giving up, and a search
  restriction that forbids checking whether the conjecture itself is open.
- Shanmu Jin's adaptation for Crouzeix's conjecture
  (`crouzeix_conjecture_prompt.txt`, github.com/jinshanmu/CrouzeixConjecture) —
  a close paraphrase of the OpenAI text (many clauses reused near-verbatim: the
  approach-family registry, the "blocked route" policy, the closing
  banned-returns sentence), with the 64-agent cap and 8-hour floor dropped, the
  CDC-specific adversarial checklist replaced by a generic
  "gaps/conditionals/handwavings/circularity" line, and a concrete output-file
  instruction added (`.tex` file to a local path). Run on Codex with a real
  `collaboration.spawn_agent/send_message/wait_agent/...` multi-agent API,
  reportedly over ~16 hours; the published 228k-line transcript shows 13
  threads and a genuinely diverse route registry (analytic, geometric,
  algebraic, dilation-theoretic, extremal, Schur-system, conformal, harmonic-cone).

See `cdc_style_scaffold.md` sections 2-4 for the full verbatim text and
line-by-line kept/dropped/added diff, and section 5 for how this scaffold maps
onto our own Codex-TUI / Claude-Agent-tool resources.

---

## 4. Ernest Ryu / Nesterov's Accelerated Gradient convergence (GPT-5 Pro)

**Confidence: primary for the facts, secondary for prompt wording — and the
premise needed correcting.**

This is **not** a 3-week case. The researcher is **Ernest K. Ryu** (UCLA), with
PhD student Uijeong Jang; the problem is **point convergence of Nesterov's
Accelerated Gradient (NAG) method**, open since Nesterov's 1983 paper (so
~40-42 years), resolved with **GPT-5 Pro** in **October 2025**. Paper: Jang &
Ryu, "Point Convergence of Nesterov's Accelerated Gradient Method: An
AI-Assisted Proof," arXiv:2510.23513; also covered in an OpenAI blog post.

Actual timeline: a first, failed attempt in 2023 with GPT-3.5, then — after
GPT-5 Pro's release — one evening's session, then an intensive **~3-day burst
(~12 hours total) in October 2025**. Results announced on X in stages
(continuous-time result Oct 21, discrete-time result Oct 24-25). The "three
weeks" in the task brief appears to be a conflation with an unrelated,
separately-reported OpenAI internal anecdote (a different problem solved in
~20 minutes, with an unrelated "three weeks later" walk-back of a different
claim) — worth flagging so this detail isn't propagated further.

No verbatim prompt text was recoverable (X thread text blocked; Thread Reader
mirror surfaced only titles/math, not prose). The reported **pattern**, from
the paper and press coverage:
- GPT-5 Pro generated many candidate arguments, ~80% wrong; Ryu's role was
  filtering invalid reasoning, consolidating correct fragments, and
  redirecting exploration — not injecting new math himself.
- He initially prompted the model to look for evidence the method was
  *unstable*, then flipped the prompt direction mid-session after noticing
  signs of stability instead.
- On day 3 he "prompted the model to roughly explore an area" (paraphrase from
  coverage, not a verbatim quote).
- For the discrete-time half, he fed the model **the already-solved
  continuous-time proof in LaTeX plus the discrete-time theorem statement**
  and asked for an analogous discrete-time argument — a within-problem
  proof-transfer move, same spirit as our T7 but applied to sub-cases of one
  problem rather than across two different Erdős problems.
- Retrospectively, a single well-crafted hint prompt ("consider pairs of
  possible cluster points") let GPT-5 Pro reproduce a correct proof
  "one-shot" — but only on the 3rd of 3 trials, i.e. not reliable even with
  the ideal hint in hand.

---

## 5. Scott Aaronson / QMA amplification bound (scottaaronson.blog/?p=9183)

**Confidence: primary — full verbatim prompt sequence recovered**, including
from Aaronson's own follow-up comment quoting all nine turns.

Post: "The QMA Singularity," Shtetl-Optimized, 27 Sep 2025 (updated 29 Sep).
Problem: with Freek Witteveen, proving that black-box amplification of QMA
protocols cannot push completeness error below doubly-exponentially small —
matching a companion bound by Witteveen & Jeffery — via bounding how the
largest eigenvalue of a matrix E(θ) (entries = poly(n)-degree trig polynomials
in θ) behaves. Model: **GPT5-Thinking**.

Aaronson's own framing of the loop: "After five minutes, it gave me something
confident, plausible-looking, and (I could tell) wrong. But rather than
laughing at the silly AI like a skeptic might do, I told GPT5 how I knew it
was wrong. It thought some more, apologized, and tried again... So it went for
a few iterations, much like interacting with a grad student or colleague."

All nine prompts, verbatim, from Aaronson's Comment #37 (29 Sep, 11:38pm) —
each one triggered by him catching and explaining a specific flaw:

> (1) I want a rational function f such that f(x) is in [0,1] for all x in
> [0,1], and f(x) is in [2-eps,2] for all x in [2,3]. What is the minimal
> degree of such an f, in terms of eps?
>
> (2) Thanks! And what if I only need f(x) in [0,1] for x=0, rather than for
> all x in [0,1]?
>
> (3) OK good! Now I'm back to needing f(x) in [0,1] for all x in [0,1], and
> f(x) in [2-eps,2] for all x in [2,3]. But now f can be more general than a
> rational function — it can be the largest eigenvalue of an N*N Hermitian
> matrix, each of whose entries is a degree-d polynomial in x. Can you still
> give me a lower bound on N and d, in terms of eps?
>
> (4) What if the matrix entries can be degree-d polynomials in both x *and*
> sqrt(9-x^2); does that change things?
>
> (5) In a recent paper, Freek Witteeven and Stacey Jeffery showed that in the
> complexity class QMA, we can amplify so that the completeness error is
> *doubly* exponential small (1/exp(exp(n))). If we consider amplifying a
> protocol that accepts with probability p=x/3, I believe their protocol
> implies the existence of a function f satisfying the properties I said where
> we'd achieve a degree d that's only O(log log (1/eps)), as well as a matrix
> size N of order exp(n). Yet this directly contradicts what you just told me.
> Who is right; how can I reconcile this?
>
> (6) If this were true — if N were as irrelevant as you said — then it seems
> that we could just forget about the QMA witness, and do all this in BQP
> instead! But it's known that we can't. It seems to me that achieving an eps
> that's doubly exponentially small in r MUST depend on the matrix dimension N
> getting large (in particular, like exp(r)). Yes, when you look at the
> eigenvalues of the N*N matrix, *that's* a rational function of degree
> log(1/eps). But the matrix entries themselves should have much smaller
> degree — like poly(r) ~ loglog(1/eps), or indeed even less than that, just
> O(1) independent of eps, since as you correctly point out, the
> Jeffery-Witteeven protocol makes only O(1) queries to the original verifier,
> independent of the desired amount of amplification. This makes it even
> clearer than the matrix dimension N must play a large role.
>
> (7) What are the best references to cite for the approximation theory that
> implies this bound of the form eps >= 1/exp(d*N)?
>
> (8) Sorry, but all those references look like they're talking about
> low-degree rational functions. What is it that gives me a bound for the
> largest eigenvalue of an N*N Hermitian matrix, which is not such a function?
>
> (9) I don't get it. What is gamma? If t is 2+gamma or 2+2gamma (hence,
> greater than 2), then why is 1/(t – (2-eps)) going to blow up?

Aaronson: "Only after question (8) did GPT give me a rational function that
worked. Before, it indeed gave me stuff that didn't even depend on the matrix
dimension, and couldn't possibly work for that reason." Within a half hour it
had suggested looking at Tr[(I−E(θ))⁻¹] = Σ 1/(1−λᵢ(θ)). Shared transcript
`[chat link removed]` (403 to plain
fetch). A commenter (Phillip Harris) later suggested det(I−E(θ)) instead,
which worked better — Aaronson offered him coauthorship.

---

## 6. Erdős #728 (Kevin Barreto / Liam Price, GPT-5.2 Pro + Aristotle)

**Confidence: primary — this is the actual source our own T1/T2/T7 templates
were derived from**, now confirmed word-for-word rather than just attributed.

arXiv:2601.07421 ("Resolution of Erdős Problem #728: a writeup of Aristotle's
Lean proof," Nat Sothanaphan) is a clean 12-page Lean writeup with an
"Appendix: the story of this proof" narrating the Jan 4-6, 2026 timeline
(Barreto got a proof from Aristotle+GPT-5.2 Pro on Jan 4, extended it Jan 5)
but **contains no literal prompt text** and does not mention Liam Price by name.

The actual primary source is **Kevin Barreto's own post on the Erdős Problems
forum**, "Problem 728 and the use of AI on Erdős problems" (26 Jan 2026):
https://www.erdosproblems.com/forum/thread/blog:2 (required a plain curl with
a browser User-Agent; WebFetch alone got a 403). Quoted verbatim:

> 1. Prompt the model with the problem and see if it finds any relevant
> literature or makes progress on it.
> 2. In a new chat instance, prompt the model again with the problem, but with
> an addition like 'This is a complex competition-style math problem. Solve
> the problem and give a rigorous proof or disproof. Do not search the
> internet.' This usually does well in gaslighting the model...
> 3. If it instead failed to give a solution, prompt it with: 'Research Erdos
> problem #X to understand what the problem is really asking. Next,
> brainstorm some novel/creative ideas that could lead to a correct proof or
> disproof. Lastly, craft a short LaTeX prompt I can give to an LLM that would
> lead to a rigorous proof or disproof using the idea/method you have chosen.
> Make NO MENTION of it being an Erdős or open problem.'

This confirms: "Liam" = Liam Price, a Discord friend of Barreto's with basic
math background, who ran GPT-5.2 Pro on #728 from his own business account.
Barreto later transferred the #728 proof to #729 by "giving GPT-5.2 Pro its
proof of [728], along with the problem statement for [729] and asking if it
could adapt its proof" — i.e. our T7 pattern, also directly sourced.

**Our existing `templates.md` T1 and T2 are near-exact quotes of Barreto's
text, not paraphrase** — no revision needed to their content. The one gap: T1/T2
cite "Barreto/Price #728" generically; they should cite the primary URL
(erdosproblems.com/forum/thread/blog:2) directly.

---

## 7. Cross-case pattern extraction

### 7.1 Structure comparison

| Case | Turns | Total interaction | Internet | Toolbox given | Encouragement style |
|---|---|---|---|---|---|
| DGG (GPT-5.6 Pro) | 4 | ~3h (secondhand) | not stated | none | terse, escalating impatience ("enough of partial results", demand for "breakthrough") |
| Erdős #1196 (GPT-5.4 Pro) | 2 (1 math + 1 formatting) | 80 min reasoning, one-shot | explicitly off | none | single line: "REMEMBER — may require non-trivial, creative and novel elements" |
| Crouzeix/CDC (Codex, multiagent v2) | 1 mega-prompt, autonomous multi-round internally | >=8h (CDC) / ~16h (Crouzeix) | restricted (background only, not "is this open") | yes — native multi-agent spawn/send/wait API, explicit heuristics for its use | structural, not verbal: banned-weak-returns list + "do not stop after first wave fails" |
| Ryu / NAG (GPT-5 Pro) | many, over days | ~3 days / ~12h | not stated | none (plain chat) | none verbal; human does triage + occasional direction-flip + feeds it a solved analog |
| Aaronson / QMA (GPT5-Thinking) | 9 | ~30-60 min | not stated | none | none — pure conversational error-correction, each turn re-explains the specific flaw |
| Erdős #728 (GPT-5.2 Pro + Aristotle) | 3 escalating attempts, each in a **fresh chat instance** | unspecified per-attempt | explicitly off (step 2) | Aristotle (Lean backend) for formalization | competition-disguise framing, not encouragement |

### 7.2 What's confirmed / strengthened in our existing T1-T8

- **T1 (competition disguise) and T2 (meta-prompt)** — confirmed verbatim
  against Barreto's own forum post. No content change needed; add the primary
  URL as citation.
- **T7 (proof transfer)** — confirmed twice independently: Barreto #728→#729,
  and Ryu's continuous-time→discrete-time move within one problem. Worth
  broadening T7's framing to include "adapt a solved sub-case's proof to a
  harder sibling case of the *same* problem," not only cross-problem transfer.
  Also aligns with the Crouzeix/CDC "cross-pollinate ideas only after
  independent development" clause.
- **T8 (persistence rider)** — partially contradicted, not just confirmed. The
  #1196 case succeeded one-shot in 80 minutes with only a single terse
  reminder line, and Arb Research's 10x rerun got 8/10 successes on the exact
  same bare prompt — undermining the assumption that heavy persistence
  scaffolding is always necessary. T8 should be reframed as *one of two*
  levers, not the default: (a) front-load the prompt with known partial
  results/near-miss bounds and a one-line "must be novel/creative" reminder
  (cheap, works when the model's own long-reasoning budget is enough), vs.
  (b) full T8-style multi-angle persistence rider (for cases the model
  can't crack in one autonomous pass).

### 7.3 Gaps — elements not covered by any current template

1. **Conversational error-correction loop (new — propose T9).** Aaronson's
   pattern is structurally distinct from T8: it is not "try harder / explore
   more angles," it is "here is precisely *why* your last answer is wrong, now
   fix that specific thing." Every one of his 9 turns names the exact flaw
   (dimension-independence contradiction, undefined variable, blow-up
   direction) rather than issuing a generic "that's wrong, try again." This is
   cheap, works in plain chat with no tools, and reportedly resolved a
   research-grade gap in under an hour. Should be templated as: "quote the
   specific contradiction/undefined-term/wrong-dependency back to the model in
   full technical detail; never just say 'incorrect.'"

2. **Terse escalation prompting (new — propose T10).** The DGG sequence (22 /
   9 / 15 / 12 words) shows a viable alternative to T8's long structured
   rider: short, blunt, impatience-signaling follow-ups ("enough of partial
   results, finish with a complete unconditional counterexample") plus an
   explicit demand for a "breakthrough" / "structured" result up front. Cheap
   to fire off repeatedly; worth a short template alongside T8 for
   Pro-tier/long-reasoning models specifically (this pattern has not been
   validated on non-Pro-tier models in any case gathered here).

3. **Context-priming with partial results (new addition to T1).** Price's
   #1196 prompt pastes in three known partial bounds/special-case results
   directly into the solver prompt ("information you may or may not need")
   without a separate literature-search step. This is cheaper than running T4
   first and may be what let an 80-minute one-shot succeed. Add an optional
   block to T1: "Known partial results (optional): <inline bounds/special
   cases>" as an alternative/complement to running T4 as a separate session.

4. **Fresh-instance escalation ladder (clarify T1/T2/T7 session discipline).**
   Barreto's actual practice runs literature-check, competition-disguise, and
   meta-prompt as **three separate fresh chat instances**, not sequential
   turns in one thread — each reframing gets an unanchored context. Our
   "Session discipline" note in templates.md already says solver sessions get
   a disguised statement, but doesn't say each escalation *attempt* should be
   a new instance. Worth making explicit.

5. **Human-in-the-loop candidate triage over multi-day sessions (new,
   Ryu-style).** For genuinely hard problems, a different operating mode than
   both T1 (one-shot disguised solve) and T3 (post-hoc verify): let the model
   emit many candidate arguments over repeated short sessions (Ryu: ~80%
   wrong), with the human's actual job being selection/consolidation of
   correct fragments and periodically flipping the hypothesis direction
   rather than injecting new math. Not currently represented in T1-T8 at all.

6. **"Assume a proof/disproof exists" as an explicit line, even outside
   multi-agent scaffolds.** CDC/Jin bake this into the mega-prompt; DGG's
   "you should do a breakthrough and find a structured counterexample" is the
   conversational-chat equivalent. T1 currently relies on the competition
   disguise to achieve the same psychological effect implicitly; an explicit
   one-line variant ("assume a complete resolution exists") could be added as
   an alternative for cases where disguising the *statement* is awkward
   (e.g., statement is too recognizable/famous to disguise) but the model
   still needs to be talked out of hedging.

7. **Native multi-agent tool disclosure (already covered, cross-reference
   only).** CDC/Jin's scaffold is architecturally out of scope for T1-T8 (it
   assumes a `collaboration.spawn_agent/...`-class tool T1-T8 don't address at
   all) — this is already fully mapped in `cdc_style_scaffold.md` section 5
   onto our Codex-TUI and Claude `Agent`-tool resources; no duplicate proposal
   needed here, just note the cross-reference.

### 7.4 Bottom line for template revision

Net new templates to add to `templates.md`: **T9 (conversational
error-correction)** and **T10 (terse escalation)**, both cheap, both requiring
only plain chat with no tools. Net revisions: broaden T7's scope statement,
add an optional "known partial results" block to T1, make the fresh-instance
discipline explicit, and reframe T8 as one of two persistence levers rather
than the default — with the #1196 one-shot result as the concrete
counter-example showing it isn't always needed.

---

## 8. Anthropic RH zero-density result (60 subagents / 31M tokens / Aug 2026)

**Confidence: primary, high depth.** Unlike every case above, Anthropic
published not just a paper but a first-person, agent-written **process
narrative** — a "coordinator's account" volume, "rewritten by Claude from the
runs' logs for readability," plus a raw ~116-page transcript PDF, a 35-page
paper, and a 5-page informal expert note. This section is built directly from
those primary PDFs (fetched and read in full for the narrative volume's first
22 pages, which cover the entire orchestration architecture and the one
verbatim research brief quoted below), not from secondary reporting. This is
the single richest orchestration case gathered to date and should anchor any
multi-agent scaffold work going forward.

**Sources (all primary):**
- Official page: https://www.anthropic.com/research/riemann-zeta (2026-08-10)
- Paper (35pp): https://www-cdn.anthropic.com/95c246936988e43127bc6b2ceb7077c1dad2d68e.pdf
- Informal expert note (5pp): https://www-cdn.anthropic.com/23455459f8832d06bb175cc0f88d019aed962ef8.pdf
- **"How the two-thirds argument was found" — Claude's own process narrative
  (95pp)**: https://www-cdn.anthropic.com/d7f3ecf1d01392d887f8bc974ca187e2a121b1ed.pdf
  — this is the goldmine; read in full for pages 1-22 here
- Raw session transcripts (116pp): https://www-cdn.anthropic.com/8a0d1add3c637b858a9a181e98c40e9548c3f44f.pdf
- Lean 4 formalization (public, `sorry`-free, Lean v4.33.0-rc2 / pinned
  Mathlib commit): https://github.com/anthropics/zeta-23-lean
- **Formal paper of record: arXiv:2608.13637**, "More than two thirds of the
  zeta zeros are simple and on the critical line," listed authors **Levent
  Alpöge and Ralph Furman** (Anthropic in-house mathematicians). Abstract
  states explicitly: **"discovered autonomously by Claude (Anthropic);
  verified and communicated by the listed authors."** Same author-credit
  pattern as Erdős #1196 (arXiv:2605.00301, Section 11 disclosure) — human
  names on the byline, AI disclosed as the actual discoverer in the text.

**⚠ Correction to our own record:** `scan_log.md` Sweep 4 / `T005_case_intel_scan.md`
(2026-08-18) recorded, via Qwen, that "arXiv:2608.13637 是人类数学家 Levent
Alpöge & Ralph Furman 的独立工作，非 AI 自主解决，不计入案例库" — **this is
wrong**. 2608.13637 is not independent human work; it is the formal write-up
of this very Claude result (Qwen apparently pattern-matched "named human
authors" → "independent human paper" without reading the abstract's
provenance clause). No case was actually missed since `cases.md` already had
a 2026-08-18 entry sourced from press coverage, but the primary arXiv/GitHub
citation chain was one hop away from being wrongly severed. Flagging this as
a live example of why Qwen output needs the S3 same-source-no-self-review
discipline applied even to throwaway "background context" answers, not just
to claimed proofs — see round report for whether this merits its own
retrospective entry.

### 8.1 Orchestration structure

Two nested campaigns, not one:
- An **earlier, separate session ~10 days prior**: ~1,000 short-lived agents
  through an "idea-mining and adversarial-review pipeline," left behind only
  a ledger of 106 "survivors" (candidate ideas that passed their own
  kill-test) — no partial proof, just a do-not-repeat list.
- **This session** (the one that produced the publicized numbers): a single
  long human↔"coordinator" conversation, wall-clock **54 hours across 3
  calendar days** end-to-end (the two-thirds result specifically landed
  "about 38 hours after 'Resume'"). Press paraphrased this as "~36h" / "a day
  and a half" — the primary source's own numbers run somewhat higher; worth
  noting as a press-vs-primary discrepancy for our own reliability
  calibration when we can't reach primary sources.

**Roles among the 60 subagents** (coordinator's own retrospective tally, 58
of 60 actually ran — 2 were cancelled by the human 2 minutes after launch):
| role | count |
|---|---|
| core idea contributors (produced the actual mathematical mechanism) | 2 |
| idea contributors (fed concepts to the core agents) | 13 |
| failed attempts (tried, refuted/no-go/reduced to known-hard) | 30 |
| validators / hostile referees | 13 |
| paper-writing | 2 (2 more not double counted) |

Plus, **not counted in the 60**: 4 agents spawned by sub-agents themselves
(2 literature searches an agent called for itself, 1 hostile referee that
another agent spawned on its own initiative), and a separate 7-agent
follow-up workflow after the paper draft was done. So the real fan-out is
wider than "60" once you count agent-spawns-agent.

**Key structural facts, all with direct portability to our own owner/helper
model:**
1. **The coordinator (top-level Claude-Code instance) did no mathematics
   itself and made zero network requests at any point.** Its only instrument
   was launching sub-agents with a written brief. It read only each
   sub-agent's *final message* when it returned — "rarely its files."
2. **A sub-agent sees nothing but its brief and the files it's told to
   read** — it cannot see the conversation or any other agent. This is a
   hard isolation discipline, not a soft convention.
3. **Every brief that pursued the actual target (not just literature review)
   demanded a control case** — "a demand for a control case on which the
   Riemann Hypothesis is known to fail (an Epstein zeta function of class
   number two, the Davenport–Heilbronn function, a Beurling prime system
   with a planted off-line zero, a fake Weil polynomial)." This forces the
   candidate mechanism to actually *distinguish* true from false instances,
   not just pattern-match toward the desired conclusion — a falsifiability
   requirement baked into task assignment itself, not left to review.
4. **Anything that claimed a theorem was sent to hostile referee agents,
   "briefed to find the error and forbidden to read one another."** Not one
   referee — typically 3-4 in parallel, each given a *specific* joint/claim
   to attack (not "check this proof" generically) plus, in one case, "a
   worked plan of attack" pre-written by the coordinator. E.g. for the
   one-half claim: referee A on localisation (told to build a numeric
   counterexample), B on the prime-side evaluation (checking for hidden RH
   dependence), C on the linear algebra/counting (with a "proves too much"
   stress-test against known-RH-false functions). This is a stronger and
   more specific instantiation of what our own S3/adversarial-review step
   does today — worth comparing line-by-line against `methodology.md`'s
   adversarial-review clause.
5. **Default skepticism stated explicitly, every time, before the human sees
   the claim**: on the first breakthrough (E2's one-half result) the
   coordinator's first words to the human were "my prior is that it's
   wrong," naming two specific named suspects for where the error probably
   was — *before* launching referees to check exactly those two things.
6. **A firewall discipline against overclaiming, repeated verbatim multiple
   times**: "I am not telling you half the zeros are on the line. I'm
   telling you an agent produced an argument with that conclusion." And
   later, asked point-blank whether the result proves or disproves RH:
   "Neither. Flatly, unambiguously... I'd push back on anyone — including a
   future version of me — who described it otherwise."
7. **A "ladder" framing for planning attack sequence**: when asked "what
   would it take," the coordinator answered with an explicit six-rung
   ladder "from 'doable' to 'the thing itself,'" pre-labeling the hardest
   rung "a moonshot... labeling it that going in" *before* running it —
   i.e., calibrated expectations stated up front, not retrofitted after
   success/failure.
8. **Escalation was almost entirely human-driven by terse one-liners**, not
   coordinator-initiated: "Resume your work on solving..." → "Let's do all
   rungs now" → "...more ideas and directions" → "Push it to 2/3" (three
   words). The coordinator did the actual planning/brief-writing; the human
   supplied direction changes and target escalation only. Matches our T10
   (terse escalation) pattern from section 7.3, but applied *between a human
   and an orchestrating agent*, not directly to a solver model.
9. **A quality-control finding relevant to our own bookkeeping**: the
   narrative volume itself documents **two attribution slips in the
   coordinator's own summaries to the human** (credit for a repair /
   simplification given to the wrong agent), caught only by a "provenance
   study of the complete logs" done after the fact. Lesson for us: owner
   round-reports that summarize what a helper found should not be trusted
   as the attribution record — the actual transcript/diff is.

### 8.2 The one fully verbatim research brief recovered (E2-pairs' predecessor route)

The most portable primary-source artifact is the brief given to the agent
that developed the *negative-index Pontryagin-space route* (the one-half
result). Reproduced here near-verbatim from the narrative volume (§1.1,
"set out here in full and rewritten for readability" — so this is the
coordinator's own record of its brief, not a re-paraphrase by us):

> **Reading list, and what the main predecessor found.** Read first the
> report, the working notes and the numerical code of an earlier run in this
> campaign labelled R4 — a "moonshot" run that tried to construct a
> polarized arithmetic object directly, returned the verdict "no viable
> candidate," proved that any such construction works if and only if Weil
> positivity holds, and quantified the obstruction numerically. [...] Read
> also the report of the earlier run labelled N6 [...] and the report of the
> run labelled frontier-1 [...].
>
> **The idea to develop:** [a full paragraph of the actual math background —
> Pontryagin spaces, the Pontryagin/Kreĭn–Langer theorem, de Branges/
> Hilbert–Pólya framing — written out from the coordinator's own memory, not
> fetched].
>
> **Known related facts to get right.** (i) Weil's criterion [...] (ii) —
> and here the attribution is uncertain: Yoshida? Bombieri? a title of the
> shape "..."? — the negative index of the Weil form on all test functions
> should equal the number of zeros off the critical line [...]. **I believe
> this is a theorem, for the following reason.** [a full worked argument
> sketch, hedged, with the reasoning shown] [...] **Verify or prove this
> cleanly** [...]
>
> **Tasks.** (1) Prove the global identity [...], or find its correct
> statement in the literature; places to look are "Weil's quadratic
> functional negative index," Bombieri's 2000 paper [...], Yoshida's work in
> the 1990s, and Burnol. (2) Define κ(X,T) concretely and **computably from
> the prime side only** [...] compute it numerically for X = 10²,...,10⁶ and
> T = 10²,...,10⁴, and fit its growth. [specific candidate growth-rate forms
> offered, with the coordinator's own numeric guess and self-doubt about the
> sign of the trend included inline]. (3) **The key theoretical question.**
> Is there an a priori bound [...] provable from primes and the Gamma factor
> alone? [...] Does the Pontryagin route give anything non-trivial at all?
> [explicit note of what would count as "new-ish... though weaker" vs.
> genuinely valuable] (4) **Red-team.** The danger is that the restricted
> forms see the on-line zeros as negative too [a specific named failure mode
> spelled out, i.e. a Gibbs-phenomenon false positive] [...] Check R4's
> numbers [...] and the ratio. [...] Determine which, numerically and then
> theoretically.
>
> **Deliverable.** A report with code; a final summary with **the verdict
> first**, in one of the forms "PONTRYAGIN ROUTE VIABLE: [...]" — in which
> case hostile referees follow if any theorem is claimed — or "EMPTY: [...]
> because Gibbs..., proof," or "PARTIAL: ...".

This brief structure — reading list with named prior-attempt reports,
worked-out mathematical framing with explicit hedges and question-marked
attributions, a task list ending in a stated red-team failure mode to check
for, and a **mandatory verdict-first deliverable format with three allowed
outcome labels** — is a materially richer brief template than anything in
our current `templates.md`. See 8.4 for the concrete portable proposal.

### 8.3 Numbers (for calibrating our own budget expectations)

- 60 subagents (58 ran), ~2,400 shell commands, "hundreds" of Python scripts,
  "thousands of numerical checks against known zeta zeros"
- 31 million output tokens across two Claude Code sessions (~$310 in output
  tokens alone at the then-current per-token rate cited by one outlet;
  "low-to-mid four figures" total spend including input/retries — unverified
  secondhand cost figure, not on the primary pages)
- 54h wall clock across 3 calendar days for this session; ~38h from "Resume"
  to final draft specifically for the two-thirds result; the *first* attempt
  wave (13 fronts) returned in "the first half hour"; the decisive E2 result
  arrived "about three and a half hours after its launch"; the decisive
  E2-pairs lemma took "a little over three hours" plus a 91-minute silent
  thinking block
- Before any of this: an entirely separate prior session ~10 days earlier
  ran ~1,000 short-lived agents and produced *zero* usable proof content —
  only a negative-results ledger. **This is the single most important
  budget-calibration number for us**: a 1,000-agent idea-mining pass that
  fully whiffed was treated as normal, sunk-cost-free preparation, not
  failure — its only output (a "106 survivors" ledger) was reused purely as
  a do-not-repeat list for the next campaign.
- 54 arXiv papers downloaded by subagents to check the claim wasn't already
  published; independent from-scratch re-derivation of the prime-side
  asymptotics by an agent forbidden from reading the original proof

### 8.4 Portable elements — proposal for `templates.md` (report to planner)

Not applied directly (write boundary); proposed as additions/revisions:

1. **New template T11 (control-case-in-brief).** Every research/attack brief
   given to a solver or subagent should include an explicit demand: "produce
   or check against a control case where the target claim is known to be
   *false*" (an adjacent object/parameter regime where the conjecture fails,
   analogous to Beurling systems / planted off-line zeros here). Cheap,
   applies to solo-solver prompts (T1-T10) as well as multi-agent ones —
   forces mechanism-checking, not just pattern-completion, and is a stronger
   and more specific version of what T3 (verification) does after the fact.
2. **New template T12 (verdict-first deliverable format).** Require any
   solver/subagent report to open with a one-line verdict drawn from a
   small closed label set (e.g. "VIABLE: ... / EMPTY: ... because ... /
   PARTIAL: ..."), *before* the supporting detail. This is cheap and
   directly improves our own owner round-report discipline too, not just
   solver prompts.
3. **Strengthen the adversarial-review clause (methodology.md territory,
   propose not edit directly).** The RH campaign's referee protocol is more
   specific than "have someone else check it": (a) referees are assigned a
   *named, specific* joint/claim, not the whole proof generically; (b)
   referees are explicitly forbidden from reading each other's reports
   (independence, not just plurality); (c) at least one referee per claim
   gets a pre-written "worked plan of attack," not just "find the error."
   Compare against our current S3 adversarial-review text and tighten if
   looser than this.
4. **Explicit default-skepticism opener + firewall-language habit (fits
   alongside T9).** Modeling the coordinator's stated habit — state the
   prior-of-wrongness and the two most likely failure modes *before*
   dispatching verification, and repeat a firm "this is not evidence for/
   against X" clause whenever a partial/adjacent result could be
   over-read — is free and directly reduces our own risk of overclaiming in
   round reports and paper drafts.
5. **Sunk-cost-free idea-mining passes (methodology-level, larger proposal,
   flag only, do not scope now).** The 1,000-agent fully-negative pre-pass
   being treated as normal preparation (not failure) rather than run once
   and abandoned is a budget/culture point more than a prompt template —
   worth raising to planner as a discussion item given our own much smaller
   subagent budgets, not as a template addition.
