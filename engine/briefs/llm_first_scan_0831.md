# LLM-FIRST CANDIDATE SCAN (2026-08-31) — replaces all prior scan briefs' fit criteria
Mission: find 15-25 OPEN problems where LLM REASONING is the primary attack surface —
constructing proofs, counterexamples, or new arguments. EXCLUDE problems whose natural
attack is large-scale SAT/CP exhaustion or big algebraic certificate sweeps (those tools
are now verifiers only, never the main engine).
Hard verification gate (unchanged red line): every claimed proof must be Lean-formalizable
(Mathlib pinned) or reduce to independently checkable explicit objects. Prose-only proofs
are worth nothing.
Source rule (owner 08-31): being pre-stated in Lean is a CONVENIENCE, NOT a criterion —
do not let it become a hidden filter. Many recently AI-solved problems were never stated
in Lean. Informal-statement sources get EQUAL weight; for those, formalizing the statement
ourselves is part of the deliverable (and guards against proving the wrong statement).
Priority sources:
 (a) google-deepmind/formal-conjectures (LOCAL CLONE problems/formal-conjectures):
     open conjectures already STATED in Lean — proving one = instant kernel-checked,
     publishable, upstream-PR-able. Enumerate tractable-looking items first.
 (b) erdosproblems.com open items with elementary statements (LLM-solved precedents exist
     since 2025 — the genre is proven); note any prize/named items.
 (c) MathOverflow / recent arXiv "we were unable to prove ..." lemmas.
 (d) OEIS conjectured identities/relations.
Score each candidate on FIVE axes: impact | PRACTICALITY (owner rule: wider application =
higher priority) | LLM-attack-surface (why a reasoning model plausibly cracks it) |
verification path (Lean target? explicit object?) | time budget.
Deliverables: ranked slot-2 list (plausibly provable in days, high certainty) and a
slot-1 reserve list (famous/hard, low probability, high ceiling). Flag every item with
solved-after-cutoff risk for G2.
