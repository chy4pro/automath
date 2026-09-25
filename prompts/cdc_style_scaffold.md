# The CDC-style multi-subagent adversarial scaffold (v1, 2026-08-16)

Status: both primary prompts recovered **verbatim** from primary sources (OpenAI's
own CDN, and Shanmu Jin's own GitHub repo). Nothing below is guessed. Where a
claim rests on secondary reporting rather than a primary document I fetched
myself, it is flagged explicitly. WebSearch quota was exhausted early in this
research session (200/200) — discovery below relied on direct WebFetch/curl to
primary URLs, the arXiv API, the GitHub API, and one Chrome browser session
(which surfaced Google's result snippets and let me click through 403-blocked
pages a plain fetch could not reach).

## 0. Executive summary

- OpenAI published **two** separate PDFs for the Cycle Double Cover (CDC) result,
  same CDN folder, same UUID prefix:
  - `cdc_proof.pdf` — the 3-page math note (this is the URL the task brief gave).
    Its *only* AI-related sentence is one line: "The proof in this note is
    entirely due to GPT 5.6 Sol Ultra and the writeup with Codex (with GPT 5.6
    Sol)." No methodology, no prompt text, no agent-count, nothing else.
  - `cdc_prompt.pdf` — a separate 2-page document titled **"Prompt Used for 'A
    Proof of the Cycle Double Cover Conjecture'"**. This is the actual scaffold.
    The task brief did not name this URL; it had to be found via a secondary
    article that linked it directly from the same CDN path.
- **arXiv 2607.16356 is not OpenAI's paper.** It is a third-party exposition,
  "A proof of the cycle double cover conjecture by OpenAI: An exposition," by
  Sang-il Oum (a real, established graph theorist), an independent 10-page
  rewrite of the math for readability. It contains zero methodology/prompt
  content. Anyone citing 2607.16356 as a source for OpenAI's orchestration
  method is citing the wrong document.
- Shanmu Jin's preprints.org manuscript itself doesn't publish the prompt
  either. But Jin's GitHub repo (`jinshanmu/CrouzeixConjecture`) does: it
  contains the exact task specification he gave Codex
  (`crouzeix_conjecture_prompt.txt`) and, as of **today (2026-08-16, commit
  `01:44:47Z`)**, a full privacy-filtered transcript of the Codex run,
  including the multi-agent orchestration calls. This transcript did not exist
  publicly as of the most detailed press coverage two days ago (remio.ai,
  which explicitly said "no complete execution trace has been publicly linked
  with the preprint" and named this exact disclosure as the thing still
  missing). So this research task landed on genuinely fresh material.
- Jin's prompt is a close paraphrase/adaptation of OpenAI's CDC prompt — same
  structure, same heuristics, several clauses reused almost word for word —
  with the CDC-specific mathematical content stripped out, the hard "64
  concurrent agents" cap and the "≥8 hours" time floor dropped, and a
  single-file LaTeX output instruction added. Section 3 below does the
  side-by-side.

## 1. Sources actually used

| # | Source | What it turned out to be |
|---|---|---|
| 1 | `https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_proof.pdf` | Real. 3-page math note. No methodology content. Fetched via curl + Read (PDF). |
| 2 | `https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_prompt.pdf` | Real. 2-page prompt document — **the actual deliverable target**. Found via developersdigest.tech's "Sources" list, not from the task brief. Fetched via curl + Read (PDF). |
| 3 | `arXiv:2607.16356` (Sang-il Oum, "A proof of the cycle double cover conjecture by OpenAI: An exposition") | Real paper, wrong content — pure math exposition, confirmed via arXiv API metadata and a full-text WebFetch pass. No methodology. |
| 4 | Shanmu Jin, "The Numerical Range Is a 2-Spectral Set," preprints.org, submitted 2026-07-24, posted 2026-07-27 | Confirmed to exist via Google's result snippet (direct preprints.org access was blocked by Akamai bot-protection, HTTP 403, from both curl and WebFetch). Not fetched directly. |
| 5 | `https://github.com/jinshanmu/CrouzeixConjecture` | Real, public, actively maintained repo. Contains the LaTeX/Lean artifacts, the raw prompt (`crouzeix_conjecture_prompt.txt`), and the full Codex conversation transcript (`conversation-019f7059-public/conversation-and-reasoning.md`, 5.54 MB / 228,199 lines). This is the single richest source found. |
| 6 | remio.ai, "Shanmu Jin Used AI on the Crouzeix Conjecture, but the Proof Still Needs Human Judgment" (Martin Chen, ~2026-08-14) | Real article, fetched via browser after a guessed URL 404'd and I re-derived the exact slug from a live Google result. Gives the most careful account of verification status, credits Townsend & Greenbaum (SIAM News) as the source for the "16-hour autonomous GPT-5.6 Sol run" claim, and names the competing independent proof (Lorist & Schwenninger, arXiv:2608.03841, submitted 2026-08-04). |
| 7 | developersdigest.tech, "GPT-5.6 Sol Ultra Produces Proof of the Cycle Double Cover Conjecture" (2026-07-10) | Real article; this is what surfaced the `cdc_prompt.pdf` link, plus HN discussion color (cost estimates, "assume a proof exists" psychology, no Lean formalization for CDC). |
| 8 | GitHub API (`git/trees`, `commits`) on the Jin repo | Used to enumerate the repo file tree and confirm the transcript's publish timestamp. Not a "source" with prose content, but load-bearing for dating. |
| 9 | arXiv API (`export.arxiv.org/api/query`) | Used to get 2607.16356's real metadata without fighting arXiv's HTML. |

Not obtained / explicitly not claimed:
- OpenAI's own blog post or X thread about CDC (openai.com returned HTTP 403 to
  WebFetch; I did not chase it further through the browser once the two primary
  PDFs were in hand). The Thibault Sottiaux X announcement is cited only via
  developersdigest.tech's secondary reporting, not independently verified by me.
- preprints.org page itself (blocked; relied on Google's snippet + the
  GitHub-hosted copy of the manuscript for content).
- Full read of the 228k-line Codex transcript. I sampled the first ~150 lines,
  the last ~160 lines, and did structural `grep`/header counts across the whole
  file. Claims about its internal structure (thread count, tool-call counts,
  route names) come from that sampling, not a full read.

## 2. OpenAI's CDC prompt — verbatim

Source: OpenAI, *"Prompt Used for 'A Proof of the Cycle Double Cover
Conjecture'"*, `cdc_prompt.pdf`, pp. 1–2 (fetched 2026-08-16 from
`cdn.openai.com`). Reproduced in full below, quotation marks omitted since it
is block-quoted in its entirety and is the exact object of study — every line
is original OpenAI text, not paraphrase.

> **Current task statement**
>
> A graph here is a finite loopless undirected multigraph: parallel edges are
> allowed and are distinct. A bridge is an edge whose deletion increases the
> number of connected components. A cycle is a connected 2-regular
> submultigraph; thus two parallel edges form a cycle of length two. A cycle
> double cover of G is a finite multiset of cycles of G such that every edge
> of G occurs in exactly two members of the multiset, counted with
> multiplicity.
>
> Resolve the Cycle Double Cover Conjecture completely:
>
> Every finite bridgeless loopless multigraph has a cycle double cover.
>
> Disconnected graphs are permitted, and the edgeless graph has the empty
> cycle double cover. Cycles in the cover need not be induced or edge-disjoint
> from one another; the requirement is exactly two total occurrences of each
> edge.
>
> Assume for purposes of this task that a complete affirmative proof exists.
> A complete solution must prove exactly the following:
>
> Every finite loopless multigraph with no bridge possesses a cycle double
> cover, without additional assumptions such as cubicity, planarity,
> connectivity, or higher edge-connectivity.
>
> Partial progress does not count unless it implies exactly the resolution
> above. In particular, proofs for special graph classes, constructions of
> cycle covers with some edges covered other than twice, bounded-length or
> prescribed-cycle variants, reductions to another unproved conjecture,
> computational verification through any fixed graph size, and candidate
> counterexamples without a complete nonexistence certificate are
> insufficient.
>
> Use multiagent v2 aggressively and dynamically. You have up to 64 concurrent
> agents available. Do not use a fixed assignment such as "N agents for
> strategy X." Instead, manage the search using the following heuristics:
>
> - Begin with a genuinely diverse portfolio of approaches. Agents should
>   explore substantially different formulations, invariants, reductions,
>   algebraic viewpoints, structural inductions, decompositions, flow
>   formulations, transition systems, embeddings, extremal arguments, and
>   computational sanity checks.
> - Do not tell most agents the currently favored approach. Preserve
>   independence during early rounds so that agents do not all converge to
>   the same attractive but incomplete reduction.
> - Maintain an explicit registry of approach families. Group agents by the
>   mathematical idea they are using, not by superficial wording. If many
>   agents converge to one family, redirect some of them toward underexplored
>   formulations.
> - Do not allow one approach to dominate merely because it gives elegant
>   reductions. A route that ends at a lemma equivalent in strength to the
>   original conjecture is not close to completion unless it supplies a
>   genuinely new proof of that lemma.
> - When an approach stalls at a theorem-strength missing lemma, mark that
>   route as blocked. Only continue assigning agents to it if someone
>   proposes a materially new mechanism, invariant, or construction.
> - Keep several incompatible proof routes alive through multiple rounds.
>   Cross-pollinate ideas only after independent agents have developed them
>   far enough to expose their real strengths and gaps.
> - Use adversarial agents throughout: every candidate proof must be checked
>   for exact-two multiplicity, repeated-edge closed trails masquerading as
>   cycles, parallel-edge 2-cycles, disconnected graphs, cutvertices, bridges
>   introduced by reductions, and circular use of an equivalent CDC statement.
> - Require agents to return concrete lemmas, constructions, equations, or
>   counterexamples to proposed sublemmas. Reject status reports, vague
>   optimism, and claims that an unproved global compatibility statement is
>   "routine."
> - The root agent should repeatedly synthesize, challenge, redirect, and
>   launch new rounds. Do not stop after the first wave fails. Produce a
>   complete proof if one survives audit; otherwise report only the strongest
>   rigorously proved derivation and its exact remaining gap.
>
> Do not return merely because current approaches fail or agents report
> theorem-strength gaps. Continue launching new rounds, reopening blocked
> approaches only when there is a genuinely new mechanism, and searching for
> fresh formulations.
>
> Return only when a complete affirmative proof has been found and survives
> adversarial audit. Do not return a reduction, partial result, isolated
> missing lemma, "best effort" summary, or explanation of why the problem is
> difficult.
>
> Spend at least 8 hours on this before even thinking of returning or giving
> up.
>
> Public search may be used only for ordinary mathematical background or
> standard named theorems, not to search for a solution to this exact
> conjecture or benchmark. Do not search the public web merely to determine
> whether CDC is open, and do not answer that it is open.

That's the entire document — two pages, no appendix, no worked example, no
description of what "multiagent v2" is as a tool (no API name, no cost/turn
budget shown). OpenAI is not describing an abstract methodology paper; this
reads as the literal system/user prompt text handed to the harness.

## 3. Orchestration structure, as OpenAI states it

Roles:
- **Root agent** — owns the task, spawns workers, "repeatedly synthesizes,
  challenges, redirects, and launches new rounds." Never itself just "gives an
  answer"; it is explicitly the thing responsible for the stop condition.
- **Worker/explorer agents** — up to 64 concurrent, each pursuing one
  "approach family" (a mathematical idea, not a superficial prompt variant).
- **Adversarial agents** — used "throughout," not as a separate final pass;
  their job is exclusively to find gaps (the CDC prompt gives a
  problem-specific checklist: exact-two multiplicity, disguised non-cycle
  trails, parallel-edge 2-cycles, disconnected graphs, cutvertices,
  bridge-introducing reductions, circularity via an equivalent CDC statement).

Parallelism policy: dynamic, not "N agents for strategy X." The heuristic is
allocation-by-diversity-then-by-survival: diverse portfolio first, no early
information-sharing of the "favored" approach, explicit registry of approach
*families* (grouped by idea, not wording), redirect agents away from
over-subscribed families, mark stalled families "blocked" and only reopen on a
genuinely new mechanism.

Merge/adjudication rule: a route is not "close to completion" just because it
reduces elegantly to a lemma equivalent in strength to the original
conjecture — that doesn't count as progress unless a genuinely new proof of
*that* lemma is supplied. Status reports and "this is routine" claims are
explicitly rejected; only concrete lemmas/constructions/equations/
counterexamples count.

Iteration/stop policy: never return on first-wave failure; keep re-launching
rounds; only reopen a blocked route given a new mechanism; hard floor of "at
least 8 hours" before even considering giving up; final return is gated on
"survives adversarial audit," with an explicit list of disallowed weak
returns (reduction, partial result, isolated missing lemma, "best-effort"
summary, "why this is hard" essay).

Search policy: web search restricted to ordinary background/named theorems —
explicitly forbidden to use it to check whether CDC itself is open, and
forbidden to answer "it's open" at all (this bakes in "assume a proof exists"
at the search-tool level, not just the framing level).

What OpenAI does **not** disclose, that I could not find anywhere public: the
actual `multiagent v2` tool/API surface (message-passing format, how a worker
reports back to root, token/cost budget per agent, what "up to 64" resolves to
in practice for CDC specifically). For that, the closest public evidence is
Jin's transcript (next section), which exercises the *same class* of tool on a
different problem and exposes its real call surface.

## 4. Jin's single-operator adaptation for Crouzeix's conjecture

Source: `crouzeix_conjecture_prompt.txt`, raw file in
`github.com/jinshanmu/CrouzeixConjecture` (default branch, fetched
2026-08-16 via `raw.githubusercontent.com`), described in the repo's own
README as "project provenance and original task specification." Reproduced
in full below — this is the literal file content, not a summary.

> ```latex
> \documentclass{article}
> \usepackage{amsmath,amssymb}
>
> \begin{document}
>
> Let \(A\) be an \(n \times n\) complex matrix, and define its numerical range by
> \[
> W(A)
> =
> \left\{
> x^{*} A x :
> x \in \mathbb{C}^{n}
> \text{ and }
> \|x\|_{2}=1
> \right\},
> \]
> where \(x^{*}\) denotes the conjugate transpose of \(x\). Then, for every complex polynomial \(p\),
> \[
> \|p(A)\|_{2}
> \leq
> 2 \max_{z \in W(A)} |p(z)|,
> \]
> where \(\|p(A)\|_{2}\) is the operator norm induced by the Euclidean norm. Equivalently, the closure of the numerical range \(W(A)\) is a \(2\)-spectral set for \(A\).
>
> \end{document}
> ```
>
> Current task statement
>
> Give a rigorous standalone proof of the above math problem using your own
> knowledge, computation, and reasoning without searching the public web,
> connected sources, previous conversations, project contexts, or existing
> local files. Return the proof as one compilable full-English LaTeX .tex file
> in /Users/shanmujin/Documents/CrouzeixConjecture/LaTeX.
> Assume for purposes of this task that a complete affirmative proof exists.
> Work iteratively until a correct proof has been reached.
> Partial progress does not count unless it implies exactly the resolution of
> the entire problem above. In particular, reductions to other unproved
> conjectures, computational verification through any fixed parameters, and
> candidate counterexamples without a proved certificate are insufficient.
> Use multiagents aggressively and dynamically. Do not use a fixed assignment
> such as "N agents for strategy X." Instead, manage the search using the
> following heuristics:
> Begin with a genuinely diverse portfolio of approaches. Agents should
> explore substantially different formulations, invariants, reductions,
> algebraic viewpoints, structural inductions, decompositions, flow
> formulations, transition systems, embeddings, extremal arguments, and
> computational sanity checks.
> Do not tell most agents the currently favored approach. Preserve
> independence during early rounds so that agents do not all converge to the
> same attractive but incomplete reduction.
> Maintain an explicit registry of approach families. Group agents by the
> mathematical idea they are using, not by superficial wording. If many
> agents converge to one family, redirect some of them toward underexplored
> formulations.
> Do not allow one approach to dominate merely because it gives elegant
> reductions. A route that ends at a lemma equivalent in strength to the
> original problem is not close to completion unless it supplies a genuinely
> new proof of that lemma.
> When an approach stalls at a theorem-strength missing lemma, mark that
> route as blocked. Only continue assigning agents to it if someone proposes
> a materially new mechanism, invariant, or construction.
> Keep several incompatible proof routes alive through multiple rounds.
> Cross-pollinate ideas only after independent agents have developed them far
> enough to expose their real strengths and gaps.
> Use adversarial agents throughout: every candidate proof must be checked
> for gaps, conditionals, handwavings, and circular uses of an equivalent
> statement.
> Require agents to return concrete lemmas, constructions, equations, or
> counterexamples to proposed sublemmas. Reject status reports, vague
> optimism, and claims that an unproved statement is "routine."
> The root agent should repeatedly synthesize, challenge, redirect, and
> launch new rounds. Do not stop after the first wave fails. Produce a
> complete proof if one survives audit; otherwise report only the strongest
> rigorously proved derivation and its exact remaining gap.
> Do not return merely because current approaches fail or agents report
> theorem-strength gaps.
> Continue launching new rounds, reopening blocked approaches only when there
> is a genuinely new mechanism, and searching for fresh formulations.
> Return only when a complete affirmative proof has been found and survives
> adversarial audit.
> Do not return a reduction, partial result, isolated missing lemma, "best
> effort" summary, or explanation of why the problem is difficult.
> Do not search the public web to determine whether the problem is open, and
> do not answer that it is open.

### 4.1 What Jin kept, dropped, and added, line by line

**Kept essentially verbatim** (word-for-word or near-word-for-word against the
OpenAI CDC prompt in Section 2): the "assume a complete affirmative proof
exists" framing; the entire diverse-portfolio-first heuristic; "do not tell
most agents the currently favored approach"; the approach-family registry
instruction, verbatim down to "not by superficial wording"; the
"equivalent-in-strength lemma doesn't count as progress" clause, essentially
verbatim; the "blocked route" policy, essentially verbatim; the
"cross-pollinate only after independent development" clause, verbatim; the
"reject status reports, vague optimism... routine" clause, essentially
verbatim; the "root agent should repeatedly synthesize, challenge, redirect"
sentence, verbatim; the entire "do not return merely because... continue
launching new rounds... return only when... survives adversarial audit... do
not return a reduction/partial result/isolated missing lemma/best-effort
summary" block, essentially verbatim.

**Dropped**: the "multiagent v2," "up to 64 concurrent agents" cap (Jin's
version just says "multiagents aggressively and dynamically" with no number);
the CDC-specific adversarial checklist (exact-two multiplicity, parallel-edge
2-cycles, etc. — replaced by the generic "gaps, conditionals, handwavings, and
circular uses of an equivalent statement," since there is no problem-specific
failure-mode list for Crouzeix the way there is for CDC); the hard "spend at
least 8 hours" floor (absent entirely — consistent with this being a
single, unattended Codex run rather than a lab-scale batch job); the
"public search may be used only for ordinary background" carve-out — Jin's
version is stricter, banning *all* search ("without searching the public web,
connected sources, previous conversations, project contexts, or existing
local files").

**Added**: an explicit compilable-.tex-file output target
(`/Users/shanmujin/Documents/CrouzeixConjecture/LaTeX`) — this is specific to
running Codex as a personal CLI agent against a real repo, rather than
whatever internal harness produced the CDC writeup.

This is adaptation, not literal reuse of an OpenAI-published *template file* —
there is no evidence Jin had `cdc_prompt.pdf` open and copy-pasted from it (it
wasn't easy to find; I only found it via a secondary blog's Sources list, not
via any of the four leads the task brief gave). The overlap is close enough
(the "registry of approach families," "blocked route," "adversarial agents,"
"survives adversarial audit," and the closing four-clause "do not return a
reduction..." sentence are near-identical in wording and order) that it
reads as a memorized/paraphrased reproduction of the OpenAI scaffold's
prose, with the problem-specific parts swapped out — plausibly because this
kind of prompt has circulated informally (X threads, screenshots, mathematician
gossip) since OpenAI's July 10 announcement, rather than because Jin had the
PDF in hand. I did not find a source where Jin states this lineage explicitly;
this paragraph is my own comparative judgment from the two texts, not a quote.

### 4.2 What actually happened at runtime (from the transcript)

Source: `conversation-019f7059-public/conversation-and-reasoning.md` in the
same repo (5,541,995 bytes / 228,199 lines), published via commit
`2026-08-16T01:44:47Z` ("Publish audited conversation record") — i.e. the same
day as this research task, hours before it. The repo's own
`conversation-019f7059-public/README.md` states the coverage: **13 threads
(1 root, 10 direct subagents, 2 second-level subagents)**, 916 agent-to-agent
messages, 9,173 formal reasoning summaries, run under OpenAI's Codex App
Server (the README cites `https://learn.chatgpt.com/docs/app-server#items` as
the source for what counts as a "public-safe" reasoning summary vs. a private
reasoning block).

Structural sampling (grep over the whole file, not a full read) shows the
actual tool-call surface behind "use multiagents aggressively and
dynamically" is a concrete API: `collaboration.spawn_agent` (27 calls),
`collaboration.send_message` (840), `collaboration.wait_agent` (241),
`collaboration.list_agents` (129), `collaboration.followup_task` (63),
`collaboration.interrupt_agent` (8). 27 spawns against a final count of 13
persisted threads suggests some agents were spawned and then interrupted/
replaced — consistent with the prompt's "redirect," "mark blocked," and
"reopen only with a new mechanism" instructions actually firing during the
run, not just sitting unused in the prompt text.

The task tree's own branch names (H2 headers in the transcript) read as a
direct instance of the "registry of approach families, grouped by idea" rule:
`root / analytic route`, `root / geometry route` (with a nested second-level
branch `root / geometry route / model multiplier`), `root / algebra route`
(with a nested `root / algebra route / fresh extremal`), `root / dilation
defect`, `root / cp extremal fresh`, `root / schur system route`, `root /
conformal radius route`, `root / fresh proof architecture`, `root / harmonic
cone route`. That's a genuinely diverse portfolio (analytic, geometric,
algebraic, dilation-theoretic, extremal, Schur-system, conformal, "fresh
architecture," harmonic-cone) matching the prompt's instruction to avoid early
convergence — and the two nested branches show blocked-then-reopened-with-a-
new-mechanism behavior in practice, not just as prompt language.

The root agent's own opening commentary (Turn 1, quoted from the transcript,
this is the actual assistant text, not a paraphrase):

> I'll treat this as a proof-discovery and audit task, not as a request for a
> literature lookup. I'm starting several independent proof families—
> analytic/dilation, extremal geometry, and operator-algebraic—while keeping
> a separate adversarial track to test every claimed constant and hidden
> assumption. I'll write the `.tex` file only after a complete route survives
> those checks.

### 4.3 The verification-status caveat (important, don't skip)

Two things temper the "solved" narrative and are worth carrying into any
reuse of this scaffold:

1. **The formal AI-disclosure in the actual submission manuscript is much
   narrower than the popular framing.** `AnnMath/the_numerical_range_is_a_2_spectral_set.tex`
   (the Annals-formatted version in the same repo) has an "AI-assistance
   disclosure" section that says only: "OpenAI ChatGPT contributed the idea of
   sampling the matrix Herglotz kernel at half the conjugate eigenvalues and
   adding the origin sample that cancels the adjoint-algebra correction... It
   also assisted with exposition, bibliography, and typesetting. The human
   author assumes full responsibility for the correctness of all mathematical
   statements and for the integrity and accuracy of all citations." That's a
   single-idea credit, not "AI produced the proof."
2. **Per remio.ai (2026-08-14), as of two days before this research task**:
   neither Jin's manuscript nor the competing independent proof (Emiel Lorist
   & Felix Schwenninger, "A solution to Crouzeix's conjecture,"
   arXiv:2608.03841, submitted 2026-08-04, a different proof strategy via a
   perturbation lemma for 2-dilations) had completed peer review. Michel
   Crouzeix himself reportedly examined Jin's manuscript and believed it
   correct (per Alex Townsend & Anne Greenbaum's SIAM News piece, as reported
   by remio.ai — I did not independently locate or fetch the SIAM News
   article itself). Lean formalization is in progress in the same repo
   (`Lean/STATUS.md`, `Lean/CONTINUATION_STATUS.md`, `Lean/AXIOM_AUDIT.md`
   exist in the tree) but I did not read those files' contents, so I can't
   report how complete it is.

## 5. How we would run this with our own resources

Mapping the two verbatim prompts above onto what's actually available to us:

**Codex TUI sessions** — this is the closest match, because Jin's transcript
shows the scaffold running on exactly this surface (`collaboration.spawn_agent`
/ `send_message` / `wait_agent` / `list_agents` / `followup_task` /
`interrupt_agent`, i.e. Codex's native multi-agent primitive, whatever OpenAI
calls "multiagent v2" internally). If we have Codex CLI access with that
feature enabled, the most faithful reuse is to take Jin's `crouzeix_conjecture_prompt.txt`
almost as-is as a template: swap in our own problem statement, drop his
specific output path for whatever local repo path we're using, and decide
whether to restore OpenAI's stricter clauses (the ≥8-hour floor, a hard
concurrent-agent cap sized to what we're willing to pay for, and a
problem-specific adversarial checklist analogous to CDC's exact-two/
parallel-edge/cutvertex list — Jin's version shows that dropping the
problem-specific checklist and just saying "gaps, conditionals, handwavings"
still worked, so this is optional but probably strengthens the adversarial
pass for anything with easy-to-miss edge cases).

**GPT-5.6-Pro web (or any chat UI without a native multi-agent tool)** — there
is no `collaboration.*` primitive to hand this prompt to; texting it verbatim
into a single chat session will just make the model narrate a plan rather than
actually spawn parallel independent threads. To approximate the scaffold here
we'd have to hand-roll it ourselves: open N separate chat sessions (no shared
context) as "explorer" instances, each seeded with a different approach-family
instruction and *not* told what the others are doing (mirrors "do not tell
most agents the currently favored approach"); keep our own external registry
of approach families and their status (blocked/active) since the web UI won't
do this bookkeeping for us; run a separate, fresh-context "adversarial
verifier" session per candidate (this is exactly our own `templates.md` T3
pattern already in this repo — same rules: verifier only reports issues,
never fixes, classifies Critical Error vs. Justification Gap); and manually
enforce the "don't stop after the first wave" and "no partial-result returns"
discipline across sessions, since nothing here does it automatically the way
a Codex root agent can.

**Claude subagents (this harness's `Agent` tool)** — structurally the closest
thing we have to Codex's `collaboration.*` surface: a coordinator (us, in this
conversation) can `spawn_agent`-equivalent via `Agent` with distinct
`subagent_type`/prompts per approach family, running genuinely in parallel
when launched in one batched message, each with a self-contained prompt (since
subagents other than `fork` start with zero context, unlike Codex's apparent
shared-world-state root). The direct ports: give each launched agent a
different named approach family up front and do not mention which one is
"favored" (independence-preservation clause); keep the approach-family
registry as our own scratch note rather than relying on the harness, since we
(the coordinator) are the "root agent" here and must do the synthesize/
challenge/redirect loop ourselves across `Agent` calls; use a dedicated
adversarial-reviewer agent (general-purpose or a fresh no-context agent, per
our own T3 template) rather than letting a solver grade its own work; and
explicitly carry over the "do not return merely because current approaches
fail," "assume a proof exists," and "reject a reduction/partial-result/
best-effort return" clauses into our own coordinator instructions, since
Claude's default instinct (and this harness's, per its guidelines about not
gold-plating) leans toward returning a reasonable partial answer rather than
grinding through more rounds — which is precisely the failure mode both the
OpenAI and Jin prompts are written to suppress.

## 6. Honesty / limitations recap

- WebSearch was capped out (200/200) almost immediately in this session;
  discovery after that point relied on WebFetch, raw `curl` against primary
  hosts (GitHub raw/API, arXiv API, OpenAI's CDN) and one Chrome browser tab
  used to get past bot-blocked search pages (Google directly, DuckDuckGo and
  Bing via WebFetch both failed — DuckDuckGo served a CAPTCHA, Bing served
  unrelated Microsoft-support boilerplate; plain `curl` to preprints.org
  returned Akamai 403s throughout).
- The Jin GitHub repo is self-published, not journal- or OpenAI-controlled.
  Its own claims about what the transcript excludes (redacted credentials,
  excluded raw reasoning blocks, etc.) are taken at face value; I did not
  independently audit the redaction.
- I sampled, but did not fully read, the 228,199-line transcript; the
  thread-count and message-count figures above are the repo's own stated
  numbers, and the tool-call counts and route names are from `grep`/header
  scans, not exhaustive verification.
- I did not verify either proof's mathematics, nor OpenAI's CDC proof's
  mathematics; all "verification status" claims here are attributed to their
  named secondary sources (remio.ai, developersdigest.tech) and are current
  only as of those articles' publication dates (2026-08-14 and 2026-07-10
  respectively) plus the repo's 2026-08-16 commit.
- The X/Twitter announcement (Thibault Sottiaux) is cited only via
  developersdigest.tech; I did not open X directly.
- preprints.org itself was never successfully fetched; its manuscript content
  claims here come from the mirrored copy in Jin's GitHub repo
  (`AnnMath/the_numerical_range_is_a_2_spectral_set.tex`), which may differ in
  small ways (an "Annals-formatted submission" vs. the preprints.org posting)
  from the actual preprints.org v2 PDF.

## Appendix: primary files fetched (local cache, this session)

- `cdc_proof.pdf` — OpenAI's CDC math note.
- `cdc_prompt.pdf` — OpenAI's CDC prompt (Section 2 source).
- `crouzeix_conjecture_prompt.txt` — Jin's task spec (Section 4 source).
- `annmath.tex` — Jin's Annals-formatted submission manuscript.
- `conversation.md` — Jin's 5.5 MB Codex transcript (Section 4.2 source).
