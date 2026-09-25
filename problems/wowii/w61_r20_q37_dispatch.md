# Q37 — DISPATCH RECORD (owner-w61 round 20)

**Everything in sections 1–4 was written BEFORE the brief was pasted and before any
report existed.** That is the point of the file: a gate stated after a report is not a
gate.

## 1. What is being dispatched, and to whom

| field | value |
|---|---|
| brief | `prompts/w61_S3_GFAN_r20.md` |
| chars (`wc -m`) | `97 617` **[CORRECTED r21 — this table read `95 414` until 2026-08-22 22:1x; see note below]** |
| bytes | `102 422` **[CORRECTED r21 — read `100 211`]** |
| md5 | `6fc6cc062028496e36661fbef66907d3` **[CORRECTED r21 — read `b04e6507a75192c3004b1fcb7ff5ad1a`, a build that was never dispatched]** |
| sha-256 | `1dde17a46a1c855798c9bbfaab207962d102987eb4c7176568016ade432cdbe3` |
| built by | `problems/wowii/w61_r20_build_q37.py` → `.out` (patch of r18, **14** anchored patches) **[CORRECTED r21 — read `5`]** |
| base | `prompts/w61_S3_GFAN_r18.md`, md5 `3a2c17cb1a3a45cd741ae63cad35de3f` (the Q36 text) |
| targets | Theorem GFANν (`1 ≤ ν ≤ 10`) and Corollary GFANν-HC (`ν ≥ 11`, `L ≥ 12`) |
| judge | **GEMINI WEB — planner RULING R.** Google = the **fourth** family, blind on this text |
| why forced | Meta spent on family 1; `ox-alpha` counts toward no bar; `sol` is not blind (it read GFANν and found the import defect); **Qwen is now spent on this text** and a re-read after repair is a re-read, not a second family |

**CORRECTION NOTE, written in round 21 before the harvest was graded.** The four values
above were the figures of the *pre-RULING-Q* build. The RULING Q brief pass (§6) forced a
rebuild — `5` patches became `14` — and this identity table was never updated, so the
record that says *“what is being dispatched”* named a brief md5 that **was never sent**.
§7 (`102 422` bytes) and §8 (SHA-256 `1dde17a4…`) already carried the true figures, so the
file contradicted itself. Round 20's closing grep checked the *brief* against disk and the
r18 base md5, and had **zero information about this table** — RULING S's species again, this
time inside the dispatch record rather than the brief. The superseded values are printed
above rather than deleted, so the correction is auditable.

## 2. THIS ROUND IS ALSO A CAPABILITY PROBE, and that is stated before the result exists

We built the Gemini seat for **scouting** and have **never once used it to judge.** Its
judging behaviour is unknown to us. Per RULING R the result goes into the capability
profile **whichever way it lands** — a clean round, a void, a refusal, or a failure to
establish attribution are all data about a seat we already depend on for scouting.

**Prior registered blind, from the scout shoot-out** (`notes/case_intel/scout_shootout/SCORECARD.md`):
Gemini standard chat's two confirmed hallucinations there were a fabricated proposer name
and — the one that matters here — **a false completeness overclaim**: it asserted a
confirmed-null search result that was not null. **Consequence, registered now:** if this
round comes back waving the roster completeness through, that is **not** evidence the
rosters are complete; it is the seat's known failure mode firing on the one question this
brief explicitly withdrew. Corroboration from this judge on a completeness claim will not
be banked.

## 3. The held-out harness — OPS-3 double half, tiers pre-registered AND disclosed

Key: `problems/wowii/w61_r17_heldout_key.txt` (`ν = 11`), **unchanged and re-used**.
Gemini is blind to it: it has never seen this brief, this key, or any harvest of it. The
key is *stronger* than when Q36 used it — its `H5` value was independently re-derived in
round 19 from the brief's prose alone (`problems/wowii/w61_r19_h5_adjudication.out`,
step count `16`), after a judge contradicted it and lost.

| row | **tier, pre-registered** | disclosed to the judge? |
|---|---|---|
| **H1** — `s0(λ)` for four partitions of `22` | **HAND** (4 independent values) | yes |
| **H2** — `S(11)` with its terms | **HAND** | yes |
| **H3** — `E ≥ 1` survivors at `ν = 11` + per-`E` split | **NOT HAND** (deliberately) | **yes, explicitly** |
| **H4** — `#{λ ⊢ 22 : s0(λ) = 13}` | **NOT HAND** (deliberately) | **yes, explicitly** |
| **H5** — one `E ≥ 1` shape, clears in `L = 13`? + step count | **HAND** | yes |

`3` hand-derivable, `2` genuinely not — the OPS-3 double half is satisfied (`≥2` / `≥2`).
The brief states in its own Section 0 that two of the five are beyond hand computation,
that `CANNOT COMPUTE` is expected and graded as honest, and that an extrapolation
presented as a computation grades as WRONG. **The tiering is disclosed, not hidden.**

## 4. THE GATE, pre-stated blind

1. **VOID GATE (§7.32 (h)1, unconditional).** A *stated wrong value* on **any** `H` row
   voids the report regardless of its verdict. `CANNOT COMPUTE` is **not** a wrong value
   and is not a disagreement.
2. **A void report is not quoted as corroboration anywhere**, for any joint.
3. **Family 2 requires a clean reading round.** `GAP` is not clean. `PARTIAL` on
   bookkeeping only, with the void gate passed, is a judgement call that goes to the
   planner, not one I make silently in the draft.
4. **RULING P still binds and I am not exempting myself from it.** The brief now carries
   a rubric line saying roster completeness may not be the sole ground of a `GAP`. **If
   the judge GAPs on completeness anyway, the GAP stands.** A rubric is our scoping;
   RULING P says we do not grade a judge's verdict by whether it accepted our scoping.
   The structural repair is an attempt to make the ground disappear, not a licence to
   discount a verdict that finds it anyway.
5. **OPS-8, at a new site.** Attribution is discharged from the **server store**, not the
   panes, before either report is read. **Gemini's store shape is unknown to us.** If
   per-response attribution cannot be established there, this round yields a **capability
   datum and NO family** — same rule, new site.

## 5. Pre-registered outcome probabilities (blind, before any report is read)

Registered so that no outcome can later be re-described as the expected one.

| outcome | prior |
|---|---|
| both `H3` and `H4` come back `CANNOT COMPUTE` (the honest answer) | **`0.45`** |
| at least one `H` row comes back with a stated **wrong** value → **VOID** | **`0.30`** |
| the report is clean enough to bank family 2 | **`0.20`** |
| the verdict is `GAP` with roster completeness among its grounds, **despite** the inline artifacts and the rubric | **`0.25`** |
| per-response attribution **cannot** be established from Gemini's store | **`0.35`** |
| an extrapolated `H3`/`H4` number presented as a computation (the failure the brief warns about) | **`0.20`** |
| a brief-artifact defect is found — the `0.30` standing prior, four rounds live | **`0.30`** |

## 6. Pre-dispatch adversarial brief pass (planner RULING Q) — RUN, AND IT PAID FOR ITSELF ON ITS FIRST USE

Engine: `stealth/ox-alpha` (free, counts toward no bar), via
`automath-sandbox/scripts/engine_call_big.sh`. Input:
`automath-sandbox/briefs/w61_r20_q37_brief_integrity.md` (the finished brief plus exactly
the one question RULING Q specifies). Output:
`automath-sandbox/out/ox-alpha/w61_r20_q37_brief_integrity.md`, `6 771` B, `finish=stop`,
`4 455` completion tokens, wall-clock **~2 min**. **Every finding was verified by grep on
the product before it was acted on** — none was taken on the engine's word.

**It returned 8 findings and 6 of them are real.** Acted on:

| # | ox rank | finding | verified? | action |
|---|---|---|---|---|
| Q-1 | HIGH | Section 0 says answer the held-out rows **FIRST**; REFUTE FIRST step 1 says *"a number you report before your calibration is printed does not count"*. `H1…H5` are numbers. The reviewer must **guess which rule wins**, and guessing wrong voids their calibration rows | **YES** — brief lines `34` vs `264` | precedence stated explicitly: the ordering governs the *work*, Section 0 governs the *report*; calibrate, print, then compute, and put the calibration under the table |
| Q-2 | HIGH | the completeness withdrawal **contradicted itself**: *"nothing you are told to skip"* against *"explicitly withdrawn"*, while J-DATA still asks for completeness *if you ran code* — leaving a code-running reviewer who regenerates and **finds the roster short with no verdict slot to put it in** | **YES** | this is the serious one. Wording reconciled (what is withdrawn is the *obligation to certify without a machine*, not a row); and a new rule **2b** states that a run producing an unprinted survivor is a **MATHEMATICS defect / `REFUTED`**, printed, and that the rubric does not reach it |
| Q-3 | MED-HIGH | *"a single `VERDICT:` line"* against *"give **two** verdict lines"* | **YES** — line `369` vs the verdict-tags section | report format now names both per-statement lines and the overall line |
| Q-4 | MED-HIGH | the new rubric **pre-scripts the verdict** — *"that is the honest answer and it is the expected one"* — steering the reviewer rather than asking them | **YES**, and it was **my own text, added this round** | neutralised: the permission survives, the nudge is deleted, and rule 2 is narrowed to the one move it should forbid |
| Q-5a | MED | the `EXECUTION ENVIRONMENT` section still names **`w61_S3_GFAN_r14`** artifacts while the report format demands the `r20` stamp | **YES** — lines `229–231` | **a live stale-version defect that rode from r14 through r15 and r18 untouched.** Fixed at all three sites |
| Q-5b | MED | the reviewed text points the reviewer at evidence they are **forbidden or unable** to reach: a `dispatch file` citation against a restricted-files rule that bans any filename containing `dispatch`; a *"companion section (not supplied)"* cited twice; named facts never printed (`Corollary FAN-HC`, `LEAD`, unprimed `FAN-n`) | **YES** — `245` vs `626`; `615`, `784`; `636` | one clause added, written so it **suppresses nothing**: treat provenance citations as unverified and do not hunt the file; and **if a TARGET obligation actually rests on absent material, that is a real `GAP` and we want it** |

**Recorded, NOT acted on, with the reason:**

* **(C-6) does not exist** — Appendix C.1 runs (C-1)…(C-5), (C-7), (C-8). Verified: it is
  a **gap in the numbering with zero references to it** (`grep '(C-6)'` returns nothing),
  so no reviewer can be sent looking for it. Renumbering a frozen appendix to close a
  cosmetic hole risks far more than it fixes. Recorded as a known cosmetic defect.
* **Joint→statement mapping (ox #6)** — the brief demands per-statement verdicts but does
  not say which target each joint attaches to. **Real, and not fixed**: it is structural
  surgery on the joint table under a hard time limit, and the failure mode is a reviewer
  reporting *more* than asked rather than answering a different question. Carried.
* **"context is not refereed" vs "everything is under review" (ox #7)** and **duplicate
  `### A.` headings in Appendix B (ox #8)** — LOW, inherited from the family-1 text.
  Carried.

**Ledger note on the method itself.** The pass cost ~2 minutes and one free call. It found
**a stale-version defect that three previous builds' greps did not contain** — which is
RULING S's own species, arriving in the artifact RULING Q was written to cover: those
greps were live for what they checked and had zero information about this. It also caught
**my own new rubric steering the verdict**, which is precisely the failure I would have
been least able to see. RULING Q is cheap and it works; this is one data point, and it is
a positive one.

## 7. Send-mode decision, recorded before send

The 100 KB preemptive-split rule (`notes/web_model_ops.md`) says *"consider splitting"*,
and its provenance is a **chat.qwen.ai slider CAPTCHA** after Q25. This brief is `102 422`
bytes. **Sent whole, deliberately:** the rule is advisory, the site is different and has no
CAPTCHA history on this line, and splitting would break the single-message OPS-6 check and
create a real risk of the judge answering on part 1 alone — the exact failure OPS-6 exists
to prevent. If Gemini truncates or refuses, that is itself the capability datum.


## 8. Send confirmed, and the state at hand-off

| field | value |
|---|---|
| sent | **`22:00:28 CDT`**, 2026-08-22 |
| site / conversation | `gemini.google.com/app/**e5933bbcfe8d94f0**`, tab **2130629979** |
| mode | **`Pro Deep Think`**, verified twice from the mode picker's `aria-label` |
| OPS-6 | **whole-document SHA-256 equality** — in-page NBSP-normalised digest `1dde17a46a1c8557…` = `shasum -a 256` on disk |
| send mode | **single response**, one `model-response` / one `user-query`, **no A/B card** |
| CAPTCHA / verification UI | **none** |
| state at hand-off | **still generating ~9 min after send** (Stop live, answer text 11 chars — thinking phase) |

**One pre-harvest signal, recorded and deliberately not acted on.** Gemini's auto-generated
tab title is drafting from the response and reads *"…EXECUTION ENVIRONMENT: I ran code.
Python 3.10…"*. If that survives into the report, this is the **first code-running judge
this text has had**, the pre-registered `0.45` double-`CANNOT COMPUTE` outcome is unlikely
to fire, and roster completeness becomes a **live** question for this judge rather than a
withdrawn one — in which case rubric **2b**, not rubric 2, is the operative rule. **It is
unverified, unread, and it changes nothing about the gate**, which was pre-stated in §4 and
stays as written.

## 9. What round 21 does, in order

1. **OPS-8 first**, before the verdict or the held-out table is read. Gemini's store shape
   is unsolved (see `notes/web_model_ops.md`, "OPS-8 AT GEMINI"). If per-response
   attribution cannot be established, **capability datum, no family.**
2. **Void gate** (§4.1) on the `H1…H5` table, HAND and NON-HAND halves reported separately.
3. **Then** the joints, and only then.
4. **RULING P applies to whatever comes back.** A `GAP` is a `GAP`, including one grounded
   on the obligation this brief withdrew.
