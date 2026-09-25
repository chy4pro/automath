# VERIFY CHECKLIST (v5, frozen — the 2-page distillation of verification_doctrine.md)
Every rule below was bought by a real failure in this project. Apply mechanically.
The archived doctrine (notes/verification_doctrine.md) is reference only and does not grow.

## A. What it takes to BANK a claim
1. Lean proof (0 sorry, #print axioms clean, statement checked against the original wording)
   OR an executable verifier run fresh with BOTH controls: a positive control (a case that
   must pass) and a negative control (a case that must fail). A check that cannot fail has
   said nothing.
2. Numbers: every narrated number is re-extracted from the artifact at bank time — never
   typed from memory. If a number fails, first ask WHAT it measured (population/counter
   drift, F1b) before calling it fabricated (F1a); the two need opposite fixes.
3. Statement riders are independent proof obligations: the main theorem passing does not
   certify its "moreover" clause. Every delivered theorem must include one worked instance
   satisfying its own hypotheses (no vacuous truths).
4. A census is not a proof: exhaustive checks over a finite window bank as CENSUS with the
   window stated. "Zero hits" is evidence only after excluding: wrong key, wrong axis
   (object vs date vs field), and instrument failure (empty population = ALARM, not a quiet day).
5. Before proving properties of X, verify X exists (search order: existence before structure).
6. Dependencies: state which results a new claim leans on; a downstream defect never
   propagates silently into an upstream bank.

## B. Cross-family review (milestones/publication only)
7. Same-family review banks as "same-family found nothing", never as "verified".
   Family is a property of the CHANNEL (registered endpoint), not of the brief's title.
8. Engines: measured profile — checklist-completeness ~10/10, derivation validity ~2/15.
   USE them to filter, enumerate, and construct; NEVER to adjudicate a derivation.
   Read what they BUILT, not what they JUDGED. Convergent independent reconstruction
   (two channels forced to invent the same undefined object) is strong support, not proof.
9. Judges without execution environments get held-out harnesses (withhold what they must
   verify; publish what they must use). VOID (parroting) never counts as a family.
   Judged-text-is-false rounds do not count as clean rounds.
10. Repairs REPLACE text; never annotate. After any repair, sweep for unswept citations of
    the repaired statement (partial patches miss siblings).

## C. Claims about the world
11. Literature check both directions and both axes: object keys (is X open?) AND date/field
    keys (what closed recently?). Repo-merge-level resolutions are invisible to web search —
    gh/API structured checks are mandatory. "No name found" for self-invented objects is a
    WEAK negative: cite, don't claim novelty.
12. Provenance or silence: an outward factual claim links to a machine-produced artifact or
    it is removed. Verification claims name script+output; citations are opened and read by
    the reviewing model, not just resolved.
13. Empirical gaps must beat a null model before becoming targets (sample-size illusions);
    search plateaus are never obstruction evidence (searcher-blind).

## D. Process hygiene (the ones that kept biting)
14. Prose lessons decay; only mechanical checks persist. When a lesson repeats, convert it
    to a script/gate the same day.
15. Pre-register acceptance conditions before dispatching a review; grade against the
    pre-registration, not against how the answer feels.
16. Findings stand ≠ defects live: any status assertion names the version it describes.
17. Approval in one context does not extend to the next; PREPARED/HOLD markers bind everyone,
    including the orchestrator. Outward writes (publish/edit/PR) need explicit authorization
    per action class.
18. Time-box everything; append state to disk as you go (a crash loses only the current step);
    atomic claim before dispatch (tools/claim.sh) to prevent duplicate runs.

## E. Margin notes (accumulating for the next authorized revision; the checklist above is frozen)
19. **A control must be able to fail FOR THE CHANNEL IT COVERS.** (2026-08-24, cite_lookup:
    the selftest printed PASS with one of two arms 100% dead, because every control happened
    to resolve through the live arm.) Multi-channel tools need PER-CHANNEL controls; a silent
    missing channel is a DEGRADATION, never a pass. Same shape as an internal cap polled too
    coarsely to fire, found the same day on another line — both are "guards that cannot trip".
20. **Divergent counts across corpora corroborate EXISTENCE, not magnitude.** OpenAlex and
    Crossref legitimately disagree on citation counts (different corpora); use agreement as
    evidence the work exists, never quote either as a precise impact figure.
21. **A fresh preprint's zero citations is a MEASUREMENT, not a channel failure.** Never read
    "0 because new" as "0 because unimportant"; score fresh work by the problem's standing.
