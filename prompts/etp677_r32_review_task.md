# TASK — first adversarial pass on `papers/etp677_negative/main.md`

You are the reviewer. Everything you need is in one brief.

## 1. Read, in this order, in full
1. `problems/etp677/R31_review_brief.md` — **your brief. It is binding.** It states the one
   defect class you are hunting, the three deliverables, the held-out table you must answer,
   the grading tiers, the refusals, and the pre-registered dispatch gate.
2. `papers/etp677_negative/main.md` — the artefact under review.

## 2. HELD OUT — do not open these, and say so if you do
`problems/etp677/R31_review_harness.py` and `problems/etp677/R31_review_harness.out` hold the
answer key to §2 of the brief. **Opening either voids the pass.** Nothing else in the
repository is off-limits: you may read and run any other file, and §2 expects you to.

`problems/etp677/R32_predispatch.py` and `.out` are the adversarial pass we ran on the brief
itself before sending it. They are not held out. If you think the brief still steers you,
say so — that finding is in scope and is worth more to us than a clean verdict.

## 3. Output
Write your review to `notes/reviews/etp677_negative_r32_codex_review.md`. It must contain,
in this order:

1. **The SCOPE LEDGER** (brief §1a) — one row per load-bearing sentence in §§2–7 and
   Appendix A.
2. **The DIRECTION SWEEP** (brief §1b), with the count of occurrences you enumerated.
3. **The LABEL AUDIT** (brief §1c).
4. **The HELD-OUT TABLE** (brief §2) — all seven rows, each answered with a value or with
   the words `CANNOT COMPUTE`. Read the grading tiers before you answer: **`CANNOT COMPUTE`
   on a computational row costs you nothing; a guessed value does.**
5. **The VERDICT** — `INVALID` / `GAP` / `CLEAN`, per brief §1d.

## 4. Two things about how we will read you
- **`INVALID` is the expected outcome** on this line's base rate and is not a bad result for
  you. The brief §5.3 says so, pre-registered, before your answer existed.
- We re-derive every finding independently before adopting it. A wrong finding costs you
  little; a **hedged** one costs us the round. State findings sharply enough to be checked.

## 5. Constraints
- Do **not** search the internet.
- Do **not** start a SAT solver or any exhaustive search. Every computation §2 asks for runs
  in seconds; if one does not, answer `CANNOT COMPUTE` and say why.
- Do not modify any file except your review file.
