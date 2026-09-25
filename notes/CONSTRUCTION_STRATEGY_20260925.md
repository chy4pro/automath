# Constructions as a product line — channels and selection method (2026-09-25)

Owner decision 2026-09-25: constructions (explicit objects) are a third product type next to
proofs of bounds (slot 1) and exact finite values (slot 2). This note fixes where such targets
come from and how they are chosen. Rules that stay: G2 before any campaign, one independent
checker per claim, no-hype reporting, publication cadence.

## 1. What a construction claim is

A construction claim is a triple (object, checker, record):
- **object** — a finite explicit thing: a set, graph, colouring, code, design, integer tuple,
  covering system, point configuration;
- **checker** — a program, written independently of the search, that verifies the property in
  seconds to minutes and prints PASS;
- **record** — the public state it improves or settles: a table cell (best known lower bound), an
  OEIS term, an "is there …?" question, or a conjecture (counterexample).

Verification is finite, so the verification gap that kills proof claims (4% acceptance) mostly
does not apply. Priority checking is also easier: the record table *is* the G2.

## 2. Channels (where the open side is a construction)

| # | Channel | What is there | Acceptance path | Competition |
|---|---------|---------------|-----------------|-------------|
| C1 | erdosproblems.com existence questions (`answer(sorry)` variants in formal-conjectures; the 61 "existence-construction" problems in today's pool, 30 with high/medium fit: #124 #197 #203 #213 #389 #849 #850 #931 #1056 #41 #51 #273 #276 #289 #396 #479 #680 #681 #686 #727 #1055 #1059 #1108 …) | one witness settles "does there exist…" or extends a small-case table | site proof claim / comment; FC `answer(True)` | AI groups mine the site, but mostly for proofs |
| C2 | Erdős extremal functions whose best LOWER bound is an old construction (Sidon/B_h sets, sum-free, Ramsey-type, covering systems with constraints, unit-distance, integer-distance point sets) | a better construction = a new bound | site claim; arXiv note | medium |
| C3 | Record tables with mechanical acceptance: La Jolla Covering Repository (C(v,k,t) upper bounds by explicit coverings), codetables.de (bounds on codes, lower bounds by explicit codes), cage tables (smallest (k,g)-graphs), Radziszowski's dynamic Ramsey survey (lower bounds by explicit colourings), van der Waerden / Schur / Rado number lower bounds, MOLS N(n) lower bounds, Costas/Golomb-type (only where compute is not the bottleneck) | thousands of open cells with dated records and known methods | e-mail the maintainer (owner sends), table updates within weeks | heavy on famous cells (Ramsey, Golomb), thin on large-parameter or odd cells |
| C4 | OEIS "hard" sequences with a known next-term gap; sequences whose terms are extremal objects | a new term = exact-value + construction | OEIS submission (owner) | low–medium |
| C5 | Conjectures suspected false: erdosproblems entries with "probably false" remarks, formal-conjectures `answer(sorry)` with weak evidence, Graffiti/House-of-Graphs-style graph conjectures, Kourovka-style algebraic questions | a counterexample closes the question | site claim; arXiv note; FC `answer(False)` | low for obscure ones |
| C6 | AI-construction problem sets (AlphaEvolve appendix, Tao et al. 2025 follow-up, FunSearch cap sets, kissing numbers): continuous/discrete optimisation records | a better object = a new bound, instantly checkable | arXiv; the problem set's own repo | very high (big labs); use only as a method source, not as targets |

Priority order for us: C1 and C5 (single witness, high prestige per unit of work, G2 via the
site), then C3 niches (mechanical acceptance, choose cells where the record is old and was
set by a weak method), then C4. C2 when a slot-1 line needs a lower-bound companion. C6 never
as a target.

## 3. Selection method (replaces "explicit constant" as the fit test for this product)

Features per candidate cell, extracted mechanically where possible:
1. **Checkability** — checker runtime and simplicity (must be writable from the definition in
   an hour; runs in minutes).
2. **Search shape** — exact small case (SAT/ILP/CP), record search (local search, tabu, SA),
   algebraic ansatz (cyclotomic, Cayley, difference sets, lattices), or LLM-guided generator
   search (FunSearch-style: the model proposes structured generators, an evaluator scores).
   Prefer targets where an ansatz or symmetry reduction exists — raw search is where big compute
   wins, and we have 10 cores.
3. **Record age and method** — a record set before 2010 by hand or by a small search is a
   signal; a record set in 2023–2026 by SAT/ML is a warning.
4. **Object size** — the winning object should be describable in the claim (or by a short
   generator); giant unstructured objects are hard to publish and to trust.
5. **Acceptance path** — is there a maintainer or a site that records the new value? (C3 yes,
   C1 yes, C4 yes.)
6. **G2** — the table's current state, the site page, arXiv 2024–26, and for C1/C5 the
   mathematical literature on the object (the #859 lesson applies here too: a construction
   may be known under another name).

Pipeline: channel scouts (parallel, one per channel, each returns ≤ 15 cells with record,
year, method, size, URL) → dedup → feature rating (Opus) → adversarial skeptic per survivor
(is the record really that old? is the object already known? does the search fit our box?) →
**pilot** (1–2 CPU-h per survivor: does the search reach the record quickly? any progress
signal past it?) → campaign with kill criteria (no improvement after X CPU-h or Y model-hours)
→ publication (object + checker + hash on GitHub; Zenodo for a note; maintainer/site by owner).

## 4. Tooling to add (all free, user-level)
- SAT + certified UNSAT: cadical, cake_lpr, lrat-check (installed 09-25).
- ILP/CP: HiGHS (pip), OR-Tools CP-SAT (pip) — for exact small cases and coverings.
- Local search framework: a small Python/numpy harness with restarts and tabu, plus a
  generator-search loop where Sonnet/Opus propose parametrised constructions and the evaluator
  scores them (our version of FunSearch; cheap in tokens, uses idle CPU).
- Checkers are always separate programs, written from the definition, never from the search code.

## 5. Immediate actions
1. Scouting wave (workflow): six scouts (C1–C5 plus a "record tables niche" scout), rating,
   skeptic, report → notes/selection/construction_board_20260925.md.
2. Pick 1–2 targets for slot 2 after #624 checkpoint 2 finishes; pilot before committing.
3. Update the selection rules (memory + STRATEGY) — done in this note.
