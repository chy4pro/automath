# TEMPLATE v2.3 — ATTACK BRIEF (campaign structure, after Jin/Crouzeix; use for EVERY proof attack from 09-01; v2.3 09-04)
# ENGINE FIT: the multiagent clauses assume an engine that really runs long-horizon multi-agent loops
# (ChatGPT Pro/Work). On single-shot chat engines (Qwen) keep every ambition clause but the
# 'strongest derivation + exact gap' line is what prevents an empty return — never remove it.
# Fill <PROBLEM>, <PRECISE STATEMENT>, <KNOWN GIVENS>. Delete nothing from the campaign clauses.
# Do NOT: state that the problem is open; grant any fallback; narrow the scope; ask for a report.

## The problem
<PRECISE STATEMENT — self-contained, notation defined, no commentary on difficulty or status>

<KNOWN GIVENS — only results we have PROVED and the model may use freely; each labelled PROVED with a one-line reason.
 Omit anything speculative. If there are none, delete this block.>

## Current task statement
Give a rigorous standalone proof of the above using your own knowledge, computation, and reasoning,
without searching the public web, connected sources, previous conversations, or project contexts.
Assume for purposes of this task that a complete affirmative proof exists. Work iteratively until a
correct proof has been reached.

Partial progress does not count unless it implies exactly the resolution of the entire problem above.
In particular, reductions to other unproved conjectures, computational verification through any fixed
parameters, and candidate counterexamples without a proved certificate are insufficient.

Use multiagents aggressively and dynamically. Do not use a fixed assignment such as "N agents for
strategy X." Instead:
- Begin with a genuinely diverse portfolio of approaches: substantially different formulations,
  invariants, reductions, algebraic viewpoints, structural inductions, decompositions, embeddings,
  extremal arguments, and computational sanity checks.
- Do not tell most agents the currently favored approach; preserve independence in early rounds so
  agents do not converge on the same attractive but incomplete reduction.
- Maintain an explicit registry of approach families, grouped by mathematical idea, not wording. If
  many agents converge on one family, redirect some toward underexplored formulations.
- A route ending at a lemma equivalent in strength to the original problem is NOT close to completion.
  When a route stalls at a theorem-strength missing lemma, mark it blocked; reopen only on a genuinely
  new mechanism, invariant, or construction.
- Keep several incompatible routes alive across rounds; cross-pollinate only after independent agents
  have exposed each route's real strengths and gaps.
- Use adversarial agents throughout: every candidate proof is checked for gaps, hidden conditionals,
  handwaving, and circular use of an equivalent statement. Reject status reports, vague optimism, and
  any claim that an unproved statement is "routine."
- Require concrete lemmas, constructions, equations, or counterexamples to proposed sublemmas.
- The root agent repeatedly synthesizes, challenges, redirects, and launches new rounds. Do not stop
  after the first wave fails. Do not return because approaches fail or agents report theorem-strength gaps.
  Produce a complete proof if one survives audit; otherwise report only the strongest rigorously proved
  derivation and its exact remaining gap. (VERBATIM from the Crouzeix prompt — do NOT drop this line:
  without it a single-shot engine that fails simply returns NOTHING. Cost of learning this: Q11, 09-01.)

Return only when a complete proof has been found and survives adversarial audit. Do not return a
reduction, partial result, isolated missing lemma, "best effort" summary, or an explanation of why the
problem is difficult. Do not search the web to determine whether the problem is open, and do not answer
that it is open.

## Output contract (ours, applied AFTER the audit passes)
Deliver the proof as numbered lemmas, each step elementary and independently checkable, plus:
(1) the verification path — what a Lean formalisation needs, or the explicit finite object a checker
    can verify; (2) every finite computation you relied on, stated so it can be re-run.
A check that cannot fail counts as no check.

## ENGINE-CONDITIONAL BLOCK (added 09-01 after the Q11/Q12 A/B — read before dispatching)
If the target engine runs long-horizon multi-agent loops (ChatGPT Pro / Work mode): use the template
above verbatim, prohibitions included.
If the target engine is a SINGLE-SHOT chat model (Qwen and similar): keep every ambition clause above,
but REPLACE the paragraph beginning "Return only when..." with this one:

  Return a complete proof if one survives adversarial audit. If none does, return instead: (1) the
  strongest rigorously proved derivation you reached, as numbered lemmas; (2) the exact remaining gap,
  stated as a precise open statement; (3) every machine-checkable artefact you built (explicit objects,
  tables, congruences, counts) so it can be re-run and reused. Do not return an empty answer, a bare
  statement of failure, a status report, or an explanation of why the problem is hard.

Evidence: with the prohibitions and no valve the engine returned NOTHING (Q11); with the valve but the
prohibitions intact it returned a single sentence (Q12); the older brief with an explicit fallback
produced a full, machine-verifiable partial certificate (Q9). See engine/harvest/erdos203_v2_qwen.md.


## INEQUALITY-TYPE BLOCK (v2.3, added 09-04 after the #708 six-round archaeology — read before dispatching)
Classify the target first. CONSTRUCTIVE targets (exhibit a set/bound/algorithm; we can machine-verify the output) use the
template above as is: the four #708 theorem rounds (26–90 min) all had this shape. INEQUALITY / ANALYTIC targets (prove a
statement for ALL m, x, weights; no finite object certifies success) produced only reductions in four rounds of 2.4–4 h, and
every intermediate target the engines endorsed was FALSE at scales 10^4–10^6 that neither random tests nor the engine's
sandbox reach. For such targets apply ALL of the following changes:
1. Prove-or-refute at equal rank. Keep "do not answer that it is open", but list "explicit counterexample (we re-check it)"
   as a top-tier target, not the fourth, and add this rule verbatim: "No intermediate statement may be used as a lemma or
   proposed as a target until an adversarial agent has tried to break it on the provided large-scale instances; report the
   attempt and its outcome next to the statement."
2. Supply the tools, not their names. Paste into the brief: the instance generator that produced our refutations (CRT dense
   windows: class 0 mod p for p ≤ √L, least-populated class for larger p; the objective-driven greedy), the explicit
   certificates (or their compact description), and the analytic inputs WITH constants (e.g. Montgomery–Vaughan large sieve,
   Brun–Titchmarsh) as PROVED givens. An engine cannot build 10^6-scale windows or produce explicit sieve constants on its own.
3. Make the dead-route list executable: each D-item comes with the one-line check that kills it (an inequality on the
   provided window), so the adversarial agents can run it instead of reading it.
4. Output contract: every numbered lemma carries a status tag PROVED / CONDITIONAL (on what) / CONJECTURED, and the
   answer ends with a dependency list "final claim ← lemmas ← unproved items". Mixed lists cost hours at harvest (P20, P21).
5. Cadence: cap inequality-type Pro runs at about 2 h and interleave with the dialogue's machine tests (the 4 h budget note
   stays only for constructive targets). Reason: P21's mid-run candidate was refuted by the dialogue within an hour but could
   not be fed back; the run spent 2.5 more hours on it.
6. Single-shot engines (Qwen) get exact micro-lemmas the Pro run needs (a specific bound with its constant, a specific finite
   identity), never a shrunken copy of the Pro brief (Q24–Q26 returned restatements or trivialities).
7. The dialogue seat's pre-dispatch duty: run the objective-driven adversary on EVERY route the brief suggests, at the largest
   scale affordable, before sending; random tests at m ≤ 600 are not evidence for statements about all intervals.
