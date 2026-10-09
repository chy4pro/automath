# Selection round 2026-10-09 — lemma-gated (coordinator record)

Status: IN PROGRESS (step 1, scout shortlist AUT-52 running). Ranking and verdict are appended when steps 2–3 close.

## Method — coordinator decision (2026-10-09, after the owner's authority instruction relayed on AUT-51)

The owner (10-09) made the Paperclip coordinator the sole research decision maker; the step list in the AUT-51
description came from the chat session and is a suggestion. The method below is the coordinator's own choice,
with reasons; hard constraints kept: owner rules (AGENTS.md, OPERATIONS.md, OWNER_RULES.md) and "a campaign needs
owner approval".

1. **Select by lemma, not by problem.** Reason: round 4 (astra_probes_round4_20261009.md) spent six clean-room probes
   and twelve referee reports on problem-level targets and produced zero target progress; every probe re-derived a
   relaxation already known to be saturated (round 3, selection_probe_20261002.md). A candidate is admissible only
   with an exactly stated lemma L, the quoted lossy step it would repair, and a concrete reason L uses information
   the saturated relaxations discard. Vague candidates are excluded, not ranked low.
2. **Step 1 (scout, AUT-52, running — not interrupted).** <=8 cards. Catalogues: targets_20261003, old_records_20261003,
   G2_OPENAI_RELEASE_20261009 B–C, transfer_targets_20261002, construction_board_20260925, famous_watch, SELECTION
   negative list, the round-3/4 verdict files.
3. **Step 2 (verifier): finite falsification tests, at most 3 lemmas, <=1 CPU-hour each.** Ranking key for choosing
   the three: product grade if proved × strength of the non-refutation argument (d) × sharpness of the test (e).
   Outcomes: FALSIFIED (witness) / SURVIVED (range) / NOT TESTABLE AS STATED. Cap 3 is a cost choice, not a rule;
   a fourth is run only if two top cards are falsified and the fourth has an exact test.
4. **Step 2b (coordinator addition): one clean-room probe on the best surviving lemma before any campaign request.**
   Reason: a finite test only fails to refute; the owner's approval request should carry evidence that L is
   attackable, and one probe is the cheapest such evidence. Engine: attacker-1 (Astra), single run, brief = statement
   of L, definitions, exact target, route seeds, standard of proof — no literature, no campaign files. If the probe
   returns PROVED, two Claude referees review before anything else happens. If it returns OPEN with the same obstruction
   as a saturated relaxation, L is parked. This is a probe under coordinator authority (as in rounds 3–4), not a
   campaign; it is skipped if no lemma survives step 2.
5. **Step 3: ranking + campaign proposal.** Written here (English) and in the AUT-51 closing comment (Chinese): routes,
   referee plan (cross-vendor), budget in Astra/Claude runs, kill criteria, expected product grade. Submitted as
   request_board_approval with the grading first. Nothing starts before the board decision.
6. **If nothing survives:** park with the exact reason per lemma; the next round widens the catalogue (scout sweep on a
   new family list) instead of re-probing the same targets.

Cost ledger for this round is kept in lines/DIALOGUE_STATE_0829.md (AUT-51 entries).
