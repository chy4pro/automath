# WOWII-61 · S3 adversarial review round 1 — dispatch record

owner-w61, round 3. Written **before** dispatch (2026-08-18, `date` = 08:09 CDT
at the time of writing; timestamps in this file are `date` output, never
estimated — planner v3 timestamps-discipline reminder, 08:13), per
`prompts/templates.md` §T13 ("declare the error prior + the two most likely
failure modes before dispatching a verification").

## Judge protocol in force (three hardening clauses, task book w61_r3 §1)

1. **Named joints, assigned by the dispatcher.** Joint *positions* are fixed here
   and in the briefs; joint *content* is whatever `notes/proofs/wowii61_draft.md`
   says at that position (PROTOCOL v3 authoritative-source rule — the briefs
   deliberately do not restate the mathematics).
   * Theorem T3 (planner-assigned): J1 = the (F-b) available-pair exhaustiveness
     argument inside the proofs of C2 and C3 (§7.3.1); J2 = the closing forcing
     step of case k=3 (§7.3.3); J3 = Lemma U's hypotheses and each application
     site (§7.3.2 + §7.3.3); J4 = the counting steps of the three k=2 sub-cases
     (§7.3.3). Added by owner: J5 = global exhaustiveness / hypothesis hygiene.
   * Theorem N (owner-assigned, 5 named assertions, all citing §7.2 B):
     N-J1 = proof of Lemma H; N-J2 = the "K = B" step plus the identity
     sum_i h_i = e_B; N-J3 = the endgame (Lemma H at i = tau, contradiction with
     hypothesis (iii)); N-J4 = the three tools Lemma S / F3 / T; N-J5 = global
     scope, non-vacuity, Corollaries N1/N2.
2. **Judge independence, no cross-reading.** One codex TUI session exists, so the
   two reviews run **serially with `/new` between them**, and each brief carries
   an explicit isolation rule forbidding the judge to open the other brief, the
   other report, or `notes/reviews/*` (this file included).
3. **Pre-written attack plan per joint** — in the briefs, as lettered (a)-(g)
   probes naming the *mechanism* to test, never the expected answer. Plus §T12
   control cases: four known-FALSE / known-TIGHT neighbours (CTRL-1..4) that the
   accepted machinery must not also prove, with a mandatory report section.

Channel: codex **Spark** (`gpt-5.3-codex-spark`), weekly quota 100% at dispatch;
codex **sol** untouched (8% left, planner-rationed, off-limits to this round).
Lease registered in `orchestration/RESOURCES.md`.

## Error prior, declared before dispatch

Honesty note: I read both proofs closely before writing the briefs, so this prior
is already conditioned on my own reading; two of the four failure modes below are
defects I believe I found myself. They are recorded here **so that the judges'
reports can be scored** (did they find these, and what else), not as hints — none
of them appears in either brief.

**Theorem N — P(material defect that breaks the theorem) ≈ 0.15;
P(a repairable exposition gap) ≈ 0.35.**
* Failure mode N-a (most likely): Lemma H's step *"the head is not among the D_j
  decremented entries, hence those entries all have value >= its value"* is
  tie-sensitive in principle — Havel–Hakimi's order among equal entries is not
  canonical, so both the definition of J and the count "tau − j − 1 later heads"
  could shift under adversarial tie-breaking. My reading says the inequality
  survives ties (a sorted-descending prefix dominates anything outside it
  regardless of how ties are broken), but this is the joint most likely to hide
  an off-by-one.
* Failure mode N-b: near-vacuity. (i) all B-degrees >= tau+1 and (iii)
  min_B deg >= 2 e_B + 3 may co-occur too rarely to matter — `w61_lemH.out`
  reports only 153 hypothesis hits in 116 873 graphs. Outcome would be "true but
  thin", which is a strategic defect, not a mathematical one.

**Theorem T3 — P(material defect that breaks the theorem) ≈ 0.20;
P(at least one repairable exposition gap) ≈ 0.75.**
* Failure mode T-a (I believe I already found this): in case **k=3** the sentence
  "于是 z 在第 2 步**未被减**" is asserted, not proved. For Z >= 5 it follows
  (no other L^1 entry can reach Z−1), but at **Z = 4** the value Z−1 = 3 ties
  with the degree-3 A-entries and the step-2 tie-break decides. I expect this to
  be **repairable without changing the conclusion**: pick any entry w attaining
  max(L^2) = D_3 = Z−1 and split on whether w was decremented at step 2 — the
  "decremented" branch dies because no entry of L^1 other than the step-2 head
  has value >= Z, and the "not decremented" branch reproduces the draft's count
  of >= Y >= 4 entries that are >= 2 after step 2, contradicting Lemma T.
* Failure mode T-b (I believe I already found this): in case **k=1, e_B=0** the
  clause "p >= 3 给 deg(y) >= p+… > 3" does not hold as written at **p = 3**
  (take p = 3 with n_y = mu[{x,y}] = mu[{y,z}] = 0, giving deg(y) = 3 exactly).
  I expect p = 3 is still excluded, but by (F-b) rather than by a degree count:
  with two B-vertices of degree exactly 3 the only occurring types are the
  universal one and possibly one singleton, which admits no disjoint pair. Same
  repairable-gap classification.
* Residual worry T-c (lower probability, no candidate found): the k=2, e_B=0 and
  k=2, e_B=1 branches both run the argument "some value-3 entry escaped step 1,
  hence #{entries >= 3} > X". The escaping entry must in fact survive step 2 as
  well; the draft only argues step 1. I currently believe the weaker (step-1
  only) statement is a valid *necessary* condition and therefore enough, but this
  is the third place I would bet on.

## Scoring rule for the returned reports

* Judge finds T-a and T-b independently → protocol working; treat the rest of its
  findings at face value.
* Judge returns CLEAN on T3 without addressing the tie-breaking mechanism in k=3
  → judge under-powered; do NOT count the round as a clean review; escalate to
  the cross-model second round (Qwen, once Chrome frees) with the joints
  re-pointed at T-a/T-b explicitly.
* Any REFUTED verdict → stop, verify numerically myself before touching the
  draft, and message planner immediately (T3 is currently provisional-approved).

---

## OUTCOME — round 1, judge 1 (Theorem T3, codex Spark xhigh, `date` 08:2x CDT)

Report: `problems/wowii/w61_S3_T3_spark.md`. Verdict line: **`CLEAN`**, all of
J1–J5 scored OK, all four controls addressed, one concrete τ=3 hard-core instance
(e_B=2, k=2) pushed through the case analysis with correct L¹/L² traces.

**Scored against the pre-declared rule: judge UNDER-POWERED; this does NOT count
as a clean first round.** Reasons:

* It returned OK on J2 (the k=3 closing step) with the sentence "no admissible
  tie-ordering in the relevant hard-core subcases changes the required head-value
  relations" — i.e. it *ran* the tie-breaking probe but did not notice that the
  draft's sentence "于是 z 在第 2 步**未被减**" (§7.3.3, k=3) is **asserted, not
  derived**, and that at Z = 4 the value Z−1 = 3 ties with the degree-3 A-entries
  so the step-2 tie-break decides. This is failure mode **T-a**, declared above
  before dispatch.
* It did not flag failure mode **T-b** (§7.3.3, k=1 & e_B=0: the clause
  "p ≥ 3 给 deg(y) ≥ p+… > 3" fails at p = 3), which falls under J3/J5.
* Its J1 verdict asserts the (F-b) pair list is exactly right — which agrees with
  my own independent re-enumeration, so that joint is genuinely corroborated.

Net: **one joint corroborated (J1), one joint corroborated with a caveat (J4 —
its independent HH trace of the e_B=2 family matches mine), two joints (J2, J3)
returned OK where I hold a pre-declared, pre-registered objection.** Both
objections are *repairable* (repairs applied to the draft, §7.3.6), so T3's
conclusion stands; its exposition did not survive review.

**Actions taken:** repairs written into draft §7.3 "5bis" (not silently edited
into the original text — the original lines are quoted and then repaired, so the
planner can audit exactly what changed). Round 2 (Qwen, queue item Q1) proceeds
as the real cross-model round, with T-a/T-b NOT disclosed to it — if Qwen finds
them independently that is a strong signal about relative judge power for this
problem class, and it goes into `notes/case_intel/qwen_capability_profile.md`.

## OUTCOME — round 1, judge 2 (Theorem N, codex Spark xhigh, `date` 08:24 CDT)

Report: `problems/wowii/w61_S3_N_spark.md`. Verdict line: **`CLEAN`**, N-J1…N-J5
all OK, no GAP, all four controls addressed.

**Scored: genuine corroboration, with one caveat.** Unlike the T3 report, this one
does not merely assert — it *reconstructs* Lemma H's chain independently (the
|J| = i−1−h_i count, the block-dominance step, the F3 elimination of survivors,
the D_j ≤ τ−j−1 contradiction against head monotonicity) and reaches the same
conclusion I do; and it answers N-J5's non-vacuity question concretely with
Family I(τ=3, c=4). Neither of my two pre-declared failure modes for Theorem N
(N-a tie-sensitivity, N-b near-vacuity) turned into a defect: N-a is genuinely
tie-safe, and N-b is real but strategic rather than mathematical.

Caveat: the judge explicitly declined to run any computation ("I did not run
additional computational checks beyond the file-internal reported numerics"),
although an independent labelled-HH implementation with adversarial tie-breaking
was the single highest-value check requested. So this is a *reading-only* review.

**Independent third confirmation (owner, same round).** Draft §7.4's Lemma DEC
re-derives Lemma H's payload `D_i ≤ τ − i + 2 + hs` from block occupancy, by an
argument that never mentions the per-head bookkeeping `h_i` — and it is verified
computationally on 116 189 graphs (36 664 with residue = α) under the canonical
sort plus three randomised adversarial tie-breaks per graph, 0 failures. That is
the computational check judge 2 skipped, done independently.

## ADJUDICATION — S3 round 2 (Qwen3.8-Max) vs round 1 (Spark), `date` 09:00 CDT

Round-2 reports: `problems/wowii/w61_S3_N_qwen.md` (PARTIAL, 1 GAP),
`problems/wowii/w61_S3_T3_qwen.md` (PARTIAL, 3 GAPs). I reproduced **every**
numeric claim in both from scratch — script `problems/wowii/w61_adjudicate.py`,
output `w61_adjudicate.out`. **All six confirmed; none refuted.**

| # | Claim | Reviewer | My verdict | Impact |
|---|---|---|---|---|
| 1 | Corollary N2 is false unqualified; K_{2,3} is a counterexample | Qwen (N) | **UPHELD** — K_{2,3}: α=3, τ=2, e_B=0, B-degs 3=τ+1 so (i) holds, Δ=3, bound=5 < m=6; and s=3≠τ=2 so the reductio fails there | Exposition only. N2 is unused by Lemma H / Theorem N. Draft patched: reductio hypothesis now explicit + contrapositive form added |
| 2 | "k ≤ 1 … Lemma U 可用" omits Lemma U's 2nd hypothesis and is false on the proof's own control instance | Qwen (T3) | **UPHELD** — [3,3,3,3,3,2,1]: Δ=3 < #{3s in R}=4; misapplied it gives m≤7 vs m=9, exactly the forbidden slack-2 | The sentence is a **false statement in the draft**, but no application site misuses it: k=0 never calls Lemma U, and both k=1 sites satisfy p+2 ≤ X. Conclusion unaffected. Draft patched in place |
| 3 | Both real Lemma U sites do satisfy the 2nd hypothesis | Qwen (T3) | **UPHELD** — #3s in R = 2+p, and the draft's own "p ≤ X−2" is exactly p+2 ≤ X | Confirms #2 is exposition, not error |
| 4 | k=3's "z 在第 2 步未被减" is unjustified, incl. under ties; and the step-2 head may be an A-entry | Qwen (T3) T-J2 | **UPHELD, and it beats my own pre-declared T-a** | My round-3 first repair assumed y is the step-2 head — wrong when Y=4 (ties with A-3s). Replaced by a complete tie-free repair (draft §7.3 5bis), which also collapses the draft's Z≥5 / Z=4 split into one line |
| 5 | "p ≥ 3 ⟹ deg(y) > 3" is false at p=3; witness degrees [4,3,3,3,3,3,1] | Qwen (T3) T-J5 | **UPHELD** — independently identical to my pre-declared T-b, same repair via (F-b) | Exposition only |
| 6 | The reductio silently needs f ≥ α+1 | Qwen (T3) T-J5 | **UPHELD** — but source is **Lemma 3** (§4.1), not Corollary B1 as Qwen wrote (B1 also works at d=4) | Missing citation only; draft patched |
| 7 | Theorem N's hypotheses are non-vacuous, e.g. K_{3,4} | Qwen (N) | **UPHELD** — K_{3,4}: (i) 4≥4, (ii) 0≤1, (iii) 4≥3, and residue=2 ≤ α−1=3 as Theorem N predicts | Answers the one question my own numerics left open (only 137–153 hypothesis hits) |

**Reviewer scorecard for the dispatch matrix.**
* **Theorem T3**: Spark CLEAN (0/4 defects found) vs Qwen PARTIAL (4/4 found,
  one of them — the Lemma U blanket sentence — not found by *me* either, and one
  — the k=3 tie-break — found *more completely* than by me). Qwen decisively
  better on this target.
* **Theorem N**: Spark CLEAN with a genuine independent reconstruction of Lemma H
  (its N-J1 walkthrough is correct and detailed); Qwen also OK on N-J1…N-J5 with
  the same reconstruction, plus it caught the N2 qualifier that Spark missed.
  Qwen better, but Spark was substantive here rather than empty.
* **Why Spark's mandatory control-instance probe missed #2**: the brief required
  running [3,3,3,3,3,2,1] through "every counting step you accept". Spark's report
  did run it — but only through the k=0 branch (where the draft handles it
  correctly by direct HH) and reported slack 1. It never asked the counterfactual
  "what would Lemma U give here, and is Lemma U claimed to be available here?".
  Qwen did exactly that. **Lesson for the judge protocol**: the control-instance
  clause must say "for each lemma the text claims is *available* in the branch the
  control lands in, verify the lemma's hypotheses on the control — not only the
  steps the text actually executes". I have not yet edited `prompts/templates.md`
  (§T12) — flagged to planner as a protocol amendment for the whole project.

**Net: no REFUTED verdict on either theorem. Theorem T3's and Theorem N's
conclusions stand; four exposition defects in T3 and one in N are repaired.**

## Net verdict on S3 round 1

* **Theorem N**: first round CLEAN and substantively corroborated (judge
  reconstruction + owner's independent re-derivation + adversarial-tie numerics).
  Still needs the cross-model round (Q1) before the ≥2-round bar is met.
* **Theorem T3**: first round does NOT count — judge under-powered against a
  pre-registered objection. Two repairable exposition gaps found by the owner and
  repaired in draft §7.3 "5bis"; conclusion unaffected. Needs Q1 plus, ideally, a
  judge better than Spark on this joint.

---

## S3 CLOSURE ROUNDS (owner-w61 round 4, `date` = 09:16 CDT) — target decision + dispatch

### Target-statement decision (required by task w61_r4 before round A)

**Decision: the N-side S3 target is the post-K consolidated chain, not legacy
Theorem N.** Concretely the gated object is

> `Lemma Z⁺ → Lemma DICH → Theorem K → Corollary K1` (draft §7.5),

with `Lemma S / T / F3` (§7.2 B) and `Lemma BO / Z / DEC / Corollary CNT /
Theorem N′ / Lemma C*` (§7.4) supplied as the supporting toolkit and explicitly
scoped by a named joint (K-J5: "state which of these the chain actually needs").

*Reasons.* (1) §7.5 **absorbs** Theorem N and Theorem N′: Corollary K1 deletes
both of Theorem N's auxiliary hypotheses (ii) and (iii), and Lemma DICH subsumes
Lemma H (low heads get Lemma H's conclusion with no hypothesis, high heads get an
equality). Gating legacy N would spend a scarce clean round on text that §7.5
already replaces. (2) Legacy N has in fact already had two substantive rounds
(Spark CLEAN with an independent reconstruction of Lemma H; Qwen OK on
N-J1…N-J5) — what remained open there was exactly the **Corollary N2 patch**,
which was written after both rounds and has therefore never been reviewed.
(3) The planner's gate rule "**N** closes when the patched-N2 re-read comes back
clean" is honoured by carrying that re-read as its **own named joint with its own
verdict line** — **K-J6** — inside the K-CHAIN brief, rather than as a footnote.

*Consequence for the gate.* Theorem N's S3 closes on K-J6 coming back clean.
Corollary K1's S3 needs both clean rounds (A and B) on K-J1…K-J5. Theorem T3's
S3 needs both clean rounds on T-J1…T-J5 of the **repaired** text.

### Round A (Qwen, fresh sessions) — dispatched to the queue

Brief `prompts/w61_S3_R2A.md`, queue row **Q5**, status READY (the Chrome-lease
holder is the driver; owner-w61 does not hold the lease this round). Two fresh
conversations, one per target, appendix trimmed per the driver table. The amended
**T12 counterfactual-availability clause** is baked into probe 4 verbatim
("for every lemma the text claims is *available* in the branch the control lands
in, verify that lemma's hypotheses ON the control — not only the steps the text
actually executes"), together with a new probe 5 requiring the judge to actually
run Havel–Hakimi trajectories (round 1's Spark judge declined to compute, which
is the caveat recorded above).

Same-source note: conversation 1 re-reviews text that Qwen helped repair in Q1.
That is compliant — Qwen is judging *Claude's repair*, not its own output — and
the brief tells the judge so, and tells it not to treat its own earlier findings
as settled. The same-source firewall is round B.

### Round B (opus judges, owner-run, in parallel) — dispatched

Judged in parallel rather than after round A: the repaired text has been stable
since the round-3 adjudication and the planner approved it in full, so serialising
would only cost wall-clock. Two independent opus helpers, one per target, each
under an explicit **isolation rule** forbidding `notes/reviews/` (this file),
`problems/wowii/w61_S3_*`, `prompts/w61_S3_*` and `orchestration/` — i.e. they
cannot see the other judge, the round-1/round-2 reports, or the pre-declared
failure modes below. Reports land at `problems/wowii/w61_S3_T3_opusB.md` and
`problems/wowii/w61_S3_K_opusB.md`.

### Error prior for the closure rounds, declared before dispatch (§T13)

**T3-REPAIRED — P(material defect breaking Theorem T3) ≈ 0.07;
P(a further repairable exposition gap) ≈ 0.45.**
* Failure mode R-a (most likely): the *repair* of gap T-a is itself new,
  unreviewed text. Its branch (ii-b) asserts "u was not decremented at step 2 —
  otherwise u's L¹ value is D_3+1 = Z ≥ 4, and no entry of L¹∖{H₂} has value ≥ 4".
  That needs `Z ≥ 4` (true, k=3) *and* that H₂ is the only L¹ entry that could
  have been ≥ 4; I believe this is right because A-entries are ≤ 3 and w's value
  is Z−1, but it is the same shape of argument that failed the first time.
* Failure mode R-b: the p = 3 repair of gap T-b concludes "the only occurring
  types are {x,y,z} and possibly {x}" — I have not re-checked whether a type
  {x,y} could occur there without contradicting deg_A(y) = 3.

**K-CHAIN — P(material defect breaking Theorem K / Corollary K1) ≈ 0.10;
P(a repairable gap) ≈ 0.40.**
* Failure mode K-a (most likely): **Corollary K1's quantifier over A.** The
  statement says "if *some* maximum independent set A has min_{b∈B} deg(b) ≥ τ+1";
  but τ = n − α does not depend on the choice of A, whereas B = V∖A does, and
  Lemma S's "every vertex of degree ≥ τ+1 is a head" is A-free. I believe the
  proof is fine (the whole chain only ever uses |B| = τ and Lemma S), but the
  mixed quantifiers are exactly where a reviewer should push.
* Failure mode K-b: Lemma DICH(c) at the boundary — the parenthetical
  "(for i = 1, D_1 = g ≤ s)" is a special case handled in a parenthesis, and the
  case j₀ = i is not separated out explicitly.
* Failure mode K-c (K-J6): the patched Corollary N2 is now stated under the
  reductio standpoint, but its *contrapositive* form is asserted to be
  "equivalent" — the equivalence needs the standpoint to be the only hypothesis
  in play, which I have not re-derived.

These are recorded so the returned reports can be **scored**, not as hints; none
of them appears in any brief.

### Scoring rule for the closure rounds

* Round A or B returns CLEAN on a target **and** its control-case section shows
  the counterfactual availability check actually being performed (naming at least
  one lemma the text claims is available but never executes) → counts as a clean
  round for that target.
* CLEAN **without** the counterfactual availability section, or without the probe-5
  trajectories → judge under-powered, does NOT count as a clean round (this is the
  round-1 Spark failure, now made an explicit scoring criterion).
* Any REFUTED → stop, reproduce numerically myself before touching the draft, and
  message planner immediately.

## ADJUDICATION — S3 round A (Qwen, fresh sessions), `date` 11:24 CDT

Reports: `problems/wowii/w61_S3_T3R_qwenA.md` (GAP), `w61_S3_KCHAIN_qwenA.md`
(PARTIAL). Reproduced from scratch with my own HH implementation:
`problems/wowii/w61_adjudicate_r4.py` → `.out`. **Both findings UPHELD; neither
refutes a conclusion.** Full write-up and the repairs are in draft **§7.7**.

* **R1 (T-J2)** — §7.3 5bis branch (ii-b)'s parenthetical "L¹∖{H₂} 中值 ≥4 的项
  不存在" is false for `Z ≥ 5`. Reproduced: `[5,5,5,3,3,3,2]` is graphical with
  `L¹ = [4,4,2,2,2,2]`. Repaired by excluding "value **= Z**" instead; verified on
  70 017 `k=3`-shaped graphical sequences, 0 violations.
* **R2 (K-J1, K-J5)** — Lemma Z⁺/DICH are stated for general `s` but cite Lemma F3,
  which §7.2 B states only under `s = τ`. Reproduced: `K_{2,3}` has `α=3, τ=2, s=3`.
  Repaired by **proving F3 for general `s` (Lemma F3′)** rather than narrowing Z⁺'s
  scope; verified on 19 324 trajectories of which **14 784 have `s ≠ τ`** — F3′ 0
  failures, Z⁺ itself 0 failures (the statement was always true; only the citation
  was out of scope). **Theorem K unaffected** — it runs wholly inside the reductio.

**Scorecard.** Round A found, on T3, a defect *inside the repair of a defect found
in the previous round* — the pre-registered "repairs are the most likely place for a
new defect" prior was correct, and this is now stated in the re-run brief. Both
round-A conversations performed the counterfactual-availability check and both
computed trajectories, so they meet the probe-4/probe-5 criteria; they fail the
clean-round criterion only because they found real gaps.

**Gate status.** Neither target has a clean round yet. Re-run dispatched as queue
row **Q6** on the re-repaired text (brief `prompts/w61_S3_R2A2.md`). Round-B opus
judges must record which text version they reviewed: the K-CHAIN and §7.6 judges
were launched **before** §7.7 existed (pre-R2 text); the T3 judge is being
re-launched **after** R1 landed (post-R1 text).

## ROUND-4 (rebuild) — staleness check on the Q6 brief + round-B relaunch, `date` 12:27 CDT

### CRITICAL staleness check — **PASSED, no re-dispatch needed**

The dead round left an open question: the Q6 re-run brief `prompts/w61_S3_R2A2.md`
was written at 11:27, and the draft was patched afterwards (mtime 11:32). Were the
Q6 judges sent a stale version of the target sections?

Checked mechanically, not by eye: every appendix section of the brief was diffed
line-by-line (heading levels and blank lines normalised) against the corresponding
range of the **current** draft. Result:

| appendix | draft section | diff |
|---|---|---|
| C | §7.2 B | identical; brief truncates before §7.2 C (deliberate trim) |
| D | §7.4 | identical (brief omits the trailing `---`) |
| E | §7.3 | identical; brief truncates before §7.3 "5. 现状与下一步" (trim) |
| F | §7.5 | identical (brief omits the trailing `---`) |
| G | §7.7 | identical up to "Gate consequence" (brief's END-OF-PASTE marker) |

**Every difference is a deliberate tail truncation; not one line of reviewed text
differs.** The 11:32 patch was the *append* of "§7.6 G — numerical backing" at the
end of §7.7 — new material after the brief's cut point, altering nothing the judges
were asked to referee. **Q6 is judging the current text; the A2 verdicts are valid
as returned.** (Script: scratch diff, not kept; the check is reproducible by
re-running the same section ranges.)

### Round B (opus judges) — RELAUNCHED after the 5xx storm killed the first set

The first round-B judges died producing nothing (no `w61_S3_*_opusB.md` on disk).
Three relaunched in parallel at 12:26 CDT, each with a "on 5xx wait 30s and retry
(≤5×)" reliability clause and the same **isolation rule** (may read
`notes/proofs/wowii61_draft.md` and non-`w61_S3_*` files in `problems/wowii/`;
forbidden: `notes/reviews/`, `problems/wowii/w61_S3_*`, `prompts/`,
`orchestration/` — so no judge can see another judge, the round-A reports, or the
pre-declared failure modes above). All three read the draft **directly** rather
than a brief, so all three review the **post-R1/post-R2 text** (draft mtime 11:32),
and each must record its text version in section (0) of its report.

| judge | target | joints | report file |
|---|---|---|---|
| B-T3 | Theorem T3 as repaired twice | T-J1…T-J5 (T-J2 covers Repair R1) | `problems/wowii/w61_S3_T3_opusB.md` |
| B-K | Z⁺ → DICH → K → K1 + patched N2 | K-J1…K-J6 (K-J1/J2/J5 cover Repair R2 / F3′) | `problems/wowii/w61_S3_K_opusB.md` |
| B-76 | **draft §7.6 in full** — first referee this text has ever had | L-J1…L-J7 (new joint set, below) | `problems/wowii/w61_S3_76_opusB.md` |

New joint set for §7.6 (pre-registered here before any verdict returns):
* **L-J1** Lemma HI + the position-sum collapse in Theorem LOW (incl. position
  independence, and (LOW2)/(LOW3) with the crossing-term cancellation);
* **L-J2** Proposition L1 + Corollary L1′;
* **L-J3** **Theorem SL**, Steps 1–6 individually (Step 3's prefix claim and Step 5's
  `s_j ≤ 2` are the load-bearing ones);
* **L-J4** Corollary SL-HC + Corollary L1-short;
* **L-J5** **Theorem MB** — the degree count and the substitution into (LOW3)-of-SL;
* **L-J6** Proposition L2 + Corollary MB1, incl. the tightness claim (e);
* **L-J7** hypothesis hygiene across §7.6 (reductio vs general `s`; hard core vs
  arbitrary G; legitimacy of every DICH dependency now that DICH runs on F3′).

All three carry the full probe set (tie-breaking, boundaries, hidden hypotheses,
the T12 counterfactual-availability control section, and mandatory computation);
B-76 additionally must build its **own** HH/residue implementation from scratch and
must not reuse any script in `problems/wowii/`. The round-1 under-powered-judge
scoring rule applies unchanged.

### Error prior for B-76, declared before its verdict returns (§T13)

**§7.6 — P(material defect breaking Theorem SL or Theorem MB) ≈ 0.15;
P(a repairable gap somewhere in §7.6) ≈ 0.55.** §7.6 is the least-reviewed and
fastest-written part of the document, and Theorem SL's Step 3 is the kind of
"block is a prefix, so every block entry has value ≥ v_j" argument that has already
failed once in this document under tie-breaking.
* Failure mode L-a (most likely): **Theorem SL Step 4**, `λ_j ≤ ℓ_j − 1`. It counts
  low later heads in `block_j` by excluding `x` — but it does not argue that the
  remaining low later heads *are* in the block, only bounds them; the identity
  `D_j = (τ−j−ℓ_j) + λ_j + s_j` is an **equality** written with `λ_j` defined as the
  actual count, so the subsequent substitution of the *bound* must be sign-correct.
* Failure mode L-b: **Step 5**'s disjointness — survivors in `block_j` and high
  heads after `i₀` are asserted disjoint inside `block_{i₀}`; a survivor is never a
  head, so this looks right, but "all `τ − i₀` of them lie in `block_{i₀}`" uses
  DICH(b) at position `i₀` for heads deleted *later*, which is the direction Z⁺
  supplies, not DICH(b) directly.
* Failure mode L-c: **Theorem MB**'s "every `b ∈ T₁∪T₂` lies in `B_lo⁺`" — `T₁,T₂`
  are types, and the claim silently needs the other type to be non-empty **and**
  disjoint from `b`'s neighbourhood in B, which is (F-b); fine if (F-b) is stated
  for the occurring types, but the quantifier deserves a push.
* Failure mode L-d: Proposition L2(c) "re-running its degree count … forces
  `Σ deg_A = 2`" — a tightness argument, and tightness arguments need the
  inequality chain to be tight at *every* link, which is not spelled out.

These are recorded so the returned report can be **scored**; none of them appears
in any judge's prompt.

## ROUND-4 (rebuild, seventh start) — A2 adjudication + Fan adjudication, `date` 13:0x CDT

Full write-up: draft **§7.8**. Scripts (owner's own, no reuse):
`problems/wowii/w61_r4_fanL.py`, `w61_r4_fanmech.py`, `w61_r4_a2check.py` (+ `.out`).

**K-CHAIN round A2 = CLEAN and it COUNTS.** Scoring rule satisfied: the control
section performs the counterfactual-availability check and names lemmas claimed
available that never execute (Theorem K/K1 unavailable on control (a); DEC/CNT
available but deliberately weak; reductio-only family absent on (b)/(d)), and
seven trajectories are computed (probe-5). I re-derived K-J1 and K-J2 (the joint
both prior defects touched) by hand — both correct — and re-checked F3′/Z⁺/DICH
at **general `s`** on 94 419 labelled runs (17 660 reductio + 9 815 non-reductio
canonical runs among `n ≤ 6` exhaustive, plus 4 000 random `n = 8…13`, three
tie-breaks each): **0 failures** on F3′, Z⁺, DICH(b), DICH(c) and both boundaries
the judge names. → **K-CHAIN: 1 clean round. Still needs round-B opus.**

**T3-REPAIRED round A2 = PARTIAL, T-J4 UPHELD** (terminal-shape count in the
k=2/e_B=2 branch miscounts under either reading; verified wrong in 726/726
parameter instances, with the parenthetical sum argument `Σ_{i≤3}D_i = m−1 < m`
correct in 726/726). Repair **R3** landed in §7.8 B: delete the count clause.
→ **T3: still 0 clean rounds**, and R3 is new text, so it needs a clean round on
the R3 version **plus** round-B opus.

**Fan(τ,L≥2) (Qwen tab B):** conclusion reproduced — 63 239 strict / 99 619
superset Fan degree sequences, **0** with `residue = α`, and the failure is
uniform (`α − residue = 1` always). Mechanism reproduced — 64 911 labelled runs
with adversarial tie-breaks: tab B's Lemma 1 (no escape) and Lemma 2 (residual
`1,1`) hold with 0 failures, the step-`p+1` multiset is **exactly** `[L]^{L+1},1,1`
in every run. Owner-proved: Lemma FAN-1 (high phase first, via tie-break
invariance), FAN-2 (no escape for `j ≤ min(p,L+1)`), FAN-3 (the endgame — the
`[L]^{L+1},1,1` suffix forces `s = τ+1`). **Not certified:** tab B's Lemma 1 for
`L+1 < j ≤ p` and its Lemma 2; the full derivation of its `r + 2L ≤ 2` is only in
the Qwen transcript, not in the harvest, so it could not be checked line by line.
**Not a milestone yet** — a conditionally-proved elimination. Named handle for the
residual: an `A′` vertex excess at step `j` must have escaped `≥ L+1` of the first
`j−1` blocks.

### Fan line — status upgrade, `date` 13:2x CDT (same round)

After the adjudication above I closed most of the Fan gap myself (draft §7.8 D/E).
New owner-proved lemmas: **FAN-4** (the `A′` residue after the high phase sums to
exactly 2 — a pure decrement count), **FAN-6** (that residue is `1+1` and never a
single `2`, by a backward induction on the block-prefix property; the `2` case
would force `max(A′ degrees) = p+2 > p`), **FAN-7** (the escape budget `E ≤ 2`,
and `E = 2` is non-graphical). With FAN-1/2/3 this leaves a **complete four-row
case list** of which three rows are closed; the residual is the single case
`E = 1` (exactly one `C`-escape, `A′` residue `[1]`, list `[L+1],[L]^L,1`, which
does clear in `L` steps). Structural hypotheses re-verified on **508 239**
high-phase runs with adversarial tie-breaks, 0 failures
(`problems/wowii/w61_r4_fanE.py` → `.out`).

Q9 brief (`prompts/w61_FANRES_qwen.md`) rewritten to target `E = 1` only, with
P1–P7 supplied as usable facts so the tabs cannot burn effort on solved parts.

### MILESTONE — Theorem FAN, `date` 13:3x CDT

The `E = 1` residual fell to a three-line argument (**Lemma FAN-8**): at an escape
step `t`, `block_t` necessarily contains an `A′` entry `x` with `v_t(x) ≥ τ−t+1`,
but the `A′` mass at step `p+1` is `2−E ≤ 1` and `x` is not deleted in steps
`t…p`, so `v_t(x) ≤ p−t+2`; together these force `L ≤ 1`. Hence `E = 0`, and with
FAN-4 + FAN-6 + FAN-3 the whole family dies.

* **Theorem FAN** — no `Fan(τ,L≥2)` graph has `residue = α`; every such graph has
  `residue = α−1` with `s = τ+1` exactly. **PROVED** (draft §7.8 F).
* **Corollary FAN-HC** — the hard core has `L ≥ 3` (via Proposition L2's rigidity
  at `L = 2`). Residual hard core: `τ ≥ 4`, `L ≥ 3`.
* **No Qwen step survives in the proof**: tab B's Lemma 1 is superseded by FAN-8
  (different, shorter) and its Lemma 2 by FAN-4 + FAN-6. Tab B is credited with
  *locating* the target, not with any adopted step.
* Numerics agree exactly, off-by-one included: `α − residue = 1` for 1 098 141 /
  1 098 141 strict and 1 700 094 / 1 700 094 superset Fan sequences; `E = 0` and
  residue partition `(1,1)` in 508 239 / 508 239 labelled runs.
* **S3**: §7.8 is brand-new and unreviewed. Its adversarial round must go to a
  **non-Qwen** judge (Qwen is the same source that raised the Fan target).
* **Q9 is now partly obsolete**: Problem D is proved. The row should be re-pointed
  at the genuinely open successor — a rigidity theorem for `L ≥ 3` (an analogue of
  Proposition L2), which is what would let Theorem FAN close more of the hard core.

### Planner ruling on Theorem FAN, `date` 13:3x CDT (corroboration: `orchestration/tasks/w61_r4.md`)

**Spot-check PASSED**; registry status **PROVED-provisional pending S3**. The
non-Qwen-judge call for §7.8 is APPROVED **and required**. Per the ruling, the S3
dispatch for §7.8 must list the dependence chain explicitly:

> **§7.8 dependence chain (to be stated verbatim in the §7.8 S3 brief).**
> Theorem FAN ← Lemmas FAN-1, FAN-3, FAN-4, FAN-6, FAN-7, FAN-8 ← **Lemma 1**
> (HH basics: terminal zeros, `Σ D_i = m`), **Lemma S** (`deg ≥ τ+1 ⟹ head`),
> **Lemma DICH** (a)(b)(c), **Lemma F3′** (survivor decay, general `s`).
> Corollary FAN-HC additionally ← **Theorem K**, **Corollary L1-short**,
> **Theorem SL**, **Proposition L2**, **Observation R1**, **Lemma 4**, **Lemma C\***.
> Named joints to pre-register: FAN-1's tie-break-invariance step; FAN-4's
> decrement bookkeeping (are the three recipient classes exhaustive?); FAN-6's
> backward induction (does the "`v−1` absent" invariant really propagate?);
> FAN-7's non-graphicality step; FAN-8's `v_{p+1}(x) ≥ v_t(x) − (p−t+1)` step
> (does `x` really survive steps `t…p`?); FAN-HC's use of Proposition L2 as a
> *rigidity* statement (does L2 supply every clause of the `Fan` definition?).

Next structural target APPROVED: an `L ≥ 3` rigidity analogue of Proposition L2,
with Qwen pre-chewing candidate-configuration enumeration under TIGHT while the
owner holds the decisive-step role.

### IN FLIGHT at round end (13:3x CDT) — K-CHAIN round-B opus judge

One opus judge was spawned at 13:11 CDT (independence enforced: it reads ONLY
`prompts/w61_S3_R2A2.md`, TARGET = K-CHAIN, appendix A/B/C/D/F/G; it is forbidden
the draft, the dispatch file and every `w61_S3_*.md`, so it has not seen round A/A2
or my own §7.8 C verification). It writes to
**`problems/wowii/w61_S3_KCHAIN_opusB.md`** and was still running at round end.
A successor should: (1) read that file when it lands; (2) if CLEAN with a real
counterfactual-availability section, **K-CHAIN's S3 gate closes** (round A2 already
counts); (3) if it finds a defect, reproduce numerically before touching the draft
and message planner. **Do not edit `prompts/w61_S3_R2A2.md` while it is running.**
Still owed after that: a T3 round on the Repair-R3 text (needs a new brief, since
R2A2's appendix G predates R3), the T3 round-B opus judge, and a **non-Qwen** S3
round on §7.8 with the dependence chain and joints pre-registered above.

### ADJUDICATION — S3 round B (opus, K-CHAIN), `date` 13:4x CDT

Report `problems/wowii/w61_S3_KCHAIN_opusB.md`: **CLEAN**, all six joints OK,
conclusion intact. Independence held (read only the brief; own labelled-HH
implementation from the Lean spec; 5 842 009 trajectories under **exhaustive**
tie-break enumeration over 28 163 graphs + a 34 265-graph sweep, 0 failures; the
two known-false controls failed exactly as required). Both mandatory sections
present — the availability check names **Lemma Z⁺** as available-but-never-firing
on all four controls, and full trajectories are computed. **Counts as a clean
round.**

Five sub-gap defects D1–D5, **all UPHELD by me**, all repaired in draft **§7.9**:
D1 (survivor defined as "其余 α 个条目", wrong off the reductio — the residue of the
R2 repair, one clause), D2 (K1's "Otherwise" needs Fact 2, terse-but-correct),
D3 (Lemma C\* declared inside §7.4's reductio but never uses it — corroborated by my
own `w61_r4_mb.out`: 0 failures on 1 064 hard-core instances computed *without* the
reductio), D4 ("O(1) vertices" should be "constant bound"), D5 (two overstated
equivalences; one is a **strengthening** — Theorem N's (iii) / N′'s (iii′) are
outright redundant given Theorem K + Fact 2).

**GATE — K-CHAIN: two clean rounds (Qwen A2 + opus B), different model families,
same text version, no shared information → S3 CLOSES**, subject to the planner's
confirmation, since D1–D5 land after both rounds (my reading: sub-gap findings do
not re-open the gate under the pre-registered rule, which targets GAP-level
findings; round B explicitly certifies no false statement and no failing
inference). **T3: still 0 clean rounds** — needs a round on the Repair-R3 text
(new brief required; R2A2's appendix G predates R3) plus its round-B opus judge.

Acted on the judge's one caveat (§7.6 not in its appendix, so R2's blanket "all of
§7.6 assumes the reductio" was unverifiable): I audited §7.6 **and** §7.8 for the
D1/D3 species — none found; recorded in §7.9. That audit is owner-only and unS3'd.

### Planner gate ruling actioned — `date` 13:5x CDT

**K-CHAIN S3 = CLOSED-CONDITIONAL** (planner, corroboration `tasks/w61_r4.md` gate
section). The required condition — a **diff-scoped confirmation pass on the §7.9
D1–D5 repair text only** — is now dispatched, riding along as **Part 2 (D-DIFF)**
of the §7.8 judge below, exactly as the ruling permits. When that returns clean,
K-CHAIN (Z⁺/DICH/Theorem K/K1, Theorem N as corollary) is fully S3-closed.

**Dispatched 13:4x CDT — §7.8 FAN chain, round A, opus (non-Qwen as required).**
Brief `prompts/w61_S3_FAN_A.md` (self-contained, 1 661 lines: header + verbatim
appendix A–H of the draft plus §7.9 as section J). Independence enforced: reads
only that file; forbidden the draft, this dispatch file, every `w61_S3_*.md` and
every `.py`/`.out` in `problems/wowii/` (its numbers must be its own). Joints
pre-registered **F-J1…F-J7** (FAN-1 tie-break invariance; FAN-4 bookkeeping;
FAN-6 backward induction; FAN-7 non-graphicality; FAN-8's two sub-points incl.
"does `x` survive steps `t…p`"; FAN-HC's use of L2 as rigidity; and **F-J7 = an
independent re-run of my §7.6/§7.8 scope audit**, per the planner's instruction to
fold that verification into this round rather than a separate pass). Plus
**D-DIFF**: separate verdicts D1…D5 and whether any repair creates a new
inconsistency. Writes `problems/wowii/w61_S3_FAN_opusA.md`.

**T3: brief written and queued.** `prompts/w61_S3_T3R3.md` (self-contained, 734
lines) supersedes `w61_S3_R2A2.md` for TARGET = T3-REPAIRED, because R2A2's
appendix G predates Repair R3. Joints **T-J1…T-J6**, with T-J6 asking specifically
whether R3 leaves any sentence dangling. Queue row **Q11 READY**. Round B for T3
must be a non-Qwen judge, dispatched once round A returns.

**D5's strengthening adopted** (planner-accepted): Theorem N's (iii) and
Theorem N′'s (iii′) are redundant given Theorem K + Fact 2; the incompatibility
holds for every `τ ≥ 1`, not just `τ ≥ 3`. Recorded as **Amendment N-iii** in the
draft, with provenance (round-B judge D5 → owner-verified → planner-accepted).

**Queue state:** Q9 SUPERSEDED, **Q10 READY** (`L ≥ 3` rigidity pre-chew),
**Q11 READY** (T3-R3). Judges in flight: one (§7.8 + D-DIFF, opus).

### Handover for the in-flight §7.8 + D-DIFF judge

Writes **`problems/wowii/w61_S3_FAN_opusA.md`**. A successor should: (1) read it
when it lands; (2) **D-DIFF part** — if D1–D5 come back clean, the planner's
condition is met and **K-CHAIN is fully S3-closed**; report to planner for
confirmation and move the registry rows to PROVED-S3. (3) **FAN part** — if CLEAN
with both mandatory sections, §7.8 has 1 clean round and needs a second from a
different model family (Qwen is eligible here **only** if it never sees this
report; note Qwen raised the Fan target originally, so prefer a third family or a
fresh opus). (4) If anything is REFUTED, stop, reproduce numerically first, and
message planner immediately. **Do not edit `prompts/w61_S3_FAN_A.md` while it
runs.** Also still open: dispatch Q11 (T3-R3 round A) and Q10 (`L ≥ 3` rigidity
pre-chew) via the Chrome/Qwen driver.

### ADJUDICATION — S3 round A for §7.8 + D-DIFF (opus), `date` 14:0x CDT

Report `problems/wowii/w61_S3_FAN_opusA.md`. Independence held (read only the
brief; own labelled-HH implementation; 3.34 M self-computed runs; **refutation
search found nothing**). Both mandatory sections present — availability check names
**DICH(c) at its FAN-1 call site** as never executing (in 0 of 18 831 runs does any
non-`B_hi` entry even tie the maximum during the high phase), plus Lemma Z's
`β_j = 0` and FAN-7's `E=2`/`E=1` rows; control `Fan(4,2)+uv` (`B = K_4`) gives
`residue = α` exactly, so the test is not vacuously negative; six trajectories,
three of them `Fan(τ,L≥2)`.

**D-DIFF (the planner's required condition): D1, D2, D3, D4, D5 all CONFIRMED, and
"does any repair create a new inconsistency elsewhere" = NO.** → **the condition on
the K-CHAIN CLOSED-CONDITIONAL ruling is MET; K-CHAIN is fully S3-closed**, subject
to the planner's confirmation, and its registry rows move to PROVED-S3.

**FAN chain: PARTIAL.** F-J1…F-J6 CORRECT; **F-J7 DEFECT**. Five findings, **all
UPHELD by me**, repaired in draft **§7.10**:

* **F1 (real, in a statement marked PROVED).** Theorem FAN's second sentence
  ("*equivalently* `residue = α−1`, exactly `τ+1` steps") is not equivalent
  (`residue ≠ α` + Fact 2 gives only `≤ α−1`) and its justification is **ex falso**
  — the step-`p+1` multiset was derived under `s = τ`, which the theorem refutes. I
  reproduced the minimal witness: `Fan(4,2)`, `deg = [5,5,4,4,4,2,1,1]`, `s = 5`,
  `residue = 3 = α−1`, where every `B_hi` degree is `τ+1 = s`, so **Lemma S and
  DICH(b) both fire zero times**. Repaired by weakening to `residue ≤ α−1` and
  demoting the exact value to **Observation FAN-E** (numerical lead, 2.8 M
  sequences, not proved).
* **F2** FAN-2 lacks its reductio marker. **F3** "hard core" expanded three
  inequivalent ways — repaired by fixing two canonical terms (**hard-core frame**
  = no reductio; **hard core** = frame + `residue = α` + `τ ≥ 4`). **F4** FAN-6's
  parenthetical misdiagnoses its own failure mode (uniqueness of the maximum, not
  the presence of `v−1`). **F5** §7.9's audit sentence.

**F5 is mine and worth stating plainly: my §7.6/§7.8 scope audit was WRONG** — it
declared no recurrence of the D1/D3 species and the judge found three, one of them a
real defect in a PROVED statement. Owner self-review did not substitute for an
independent round here. The planner's instruction to fold the audit into this round
rather than accept it is exactly what caught it; recorded as such.

**Conclusion survives in full**: Theorem FAN's first sentence and **Corollary
FAN-HC (hard core has `L ≥ 3`)** are untouched, and every lemma FAN-1…FAN-8 was
certified CORRECT joint by joint.

**Gate accounting.** K-CHAIN: **CLOSED** (2 clean + condition met). §7.8: **0 clean
rounds** — a round with a confirmed defect cannot count clean, so §7.8 needs a fresh
round on the F1–F5 text (brief to be rebuilt; `prompts/w61_S3_FAN_A.md` is now
stale). T3: 0 clean rounds, Q11 READY.

---

## ROUND 5 (owner-w61) — REGISTRY MOVE: K-CHAIN → PROVED-S3, `date` = 14:35 CDT

Planner ruling 14:2x (`orchestration/tasks/w61_r5.md`): **K-CHAIN CONFIRMED
PROVED-S3**. Registry written to draft **§7.11** (rows R-1…R-7: Lemma Z⁺, Lemma
DICH, Theorem K, Corollary K1, Lemma F3′, Theorem N/N′ as corollaries with
Amendment N-iii, patched Corollary N2). Evidence cited in the registry:

| artifact | round | verdict | why it counts |
|---|---|---|---|
| `problems/wowii/w61_S3_KCHAIN_qwenA2.md` | A2, Qwen3.8-Max fresh session | **CLEAN** | T12 availability check performed (Theorem K/K1 unavailable on control (a)); 7 trajectories |
| `problems/wowii/w61_S3_KCHAIN_opusB.md` | B, independent opus | **CLEAN** | availability check names Lemma Z⁺ as available-but-never-firing on all 4 controls; 5 842 009 exhaustive-tie-break trajectories, 0 failures |
| `problems/wowii/w61_S3_FAN_opusA.md` Part 2 | **D-DIFF** (the planner's condition) | **D1–D5 all CONFIRMED**, no new inconsistency | diff-scoped pass on the §7.9 repair text; D1's 2nd witness upgraded to a graph witness |

Also carried into §7.11: the D-DIFF judge's out-of-scope sibling flag — **Lemma T's
second sentence has the D2 shape** (needs Fact 2 to reach `residue ≤ α−1`); repair
recorded in §7.11, sub-gap, does not re-open the gate.

**Gate ledger after this move.** K-CHAIN **CLOSED / PROVED-S3**. §7.8 (FAN):
0 clean rounds, fresh round on the F1–F5 text dispatched below. T3: 0 clean rounds,
Q11 in flight. §7.6: 0 clean rounds (B-76 judge never returned a report).

### §7.8 round A2 — brief REBUILT on the F1–F5 text, judge dispatched, `date` = 14:38 CDT

`prompts/w61_S3_FAN_A2.md` (1 749 lines) **supersedes `prompts/w61_S3_FAN_A.md`**,
which is stale (pre-F1 text, plus a D-DIFF part now discharged). Structure:

* new header — **refute-first protocol** put ahead of everything (search for a
  `Fan(τ,L≥2)` graph with `residue = α` first; then a separate counterexample hunt
  per lemma FAN-1/4/6/7/8; only then read for validity), plus the standing
  "**a repair is the most likely place for a new defect**" prior aimed explicitly
  at appendix K;
* appendix A–H = the same verbatim draft text as round A (definitions, §7.2 B
  toolkit, §7.4, §7.5, §7.6, §7.7 context, §7.8 as originally written);
* **section J = context only** — §7.9's D1–D5, kept solely because they define the
  defect species F-J7 hunts and because F5 repairs a sentence living there; the
  K-chain is declared out of scope (it is PROVED-S3 as of §7.11), and the gate
  reasoning + verdict paragraphs of §7.9 were stripped so no prior verdict leaks;
* **section K = the operative text** — the F1–F5 amendments, rewritten free of any
  provenance ("the author's own audit was wrong" rather than "a judge found"), and
  declared to **supersede section H wherever they conflict**.

Joints **F-J1…F-J7 unchanged**, plus the new joint required by the round shape:

> **F-J8 — the F1 repair itself and the FAN / FAN-E demarcation.** (i) Is the
> repaired statement ("no `Fan(τ,L≥2)` graph has `residue = α`; consequently, by
> Fact 2, `residue ≤ α−1`") correctly derived, and is Fact 2 genuinely available?
> (ii) Is the demarcation in the right place — is everything left inside Theorem FAN
> provable with no consequence of the refuted `s = τ`, and is everything moved into
> **Observation FAN-E** genuinely unavailable off the reductio (test against the
> `[5,5,4,4,4,2,1,1]` witness, and find your own)? (iii) **Orphan sweep**: does any
> other statement still lean on the deleted "`residue = α−1` / `s = τ+1` exactly",
> directly or through a chain — name every site checked, not only the failures?
> (iv) Does repair F3's canonical pair (**hard-core frame** vs **hard core**)
> actually scope §7.6/§7.8 correctly — Lemma C\*, Observation R1, Prop L1/L2,
> Theorem MB, Cor SL-HC, Cor FAN-HC, one by one?

**Dispatched 14:38 CDT** — fresh opus judge, writes
`problems/wowii/w61_S3_FAN_opusA2.md`. Independence enforced in its prompt: it may
read **only** `prompts/w61_S3_FAN_A2.md`; forbidden the draft, all of `notes/`,
every `problems/wowii/w61_S3_*`, every `.py`/`.out` under `problems/wowii/`,
`orchestration/`, and every other file in `prompts/` — so it cannot see round A's
report, this file, or the pre-declared failure modes. Own labelled-HH
implementation, calibrated on `residue(K₂)` and `residue(Cₙ)`, and **no number from
the brief may be reused**. Reliability clause carried: on 5xx/overloaded, wait 30 s
and retry the same step, ≤5 attempts, never silently truncate.
**Do not edit `prompts/w61_S3_FAN_A2.md` while it runs.**

### Error prior for §7.8 round A2, declared before the verdict returns (§T13)

**P(a defect that breaks Theorem FAN's first sentence or Corollary FAN-HC) ≈ 0.06**
(round A hunted refutations over 3.34 M runs and found none, and certified
FAN-1…FAN-8 joint by joint); **P(at least one further repairable gap) ≈ 0.55** —
concentrated in the F1–F5 text itself, which no judge has ever seen.
* Failure mode A2-a (most likely): **F-J8(iii), the orphan sweep.** §7.8 E's case
  table ("clears in `L+1`" / "clears in `L`" columns) and §7.8 G's `GFan` LEAD both
  reason with exact step counts. The table is inside the reductio and so is safe,
  but the LEAD's "which shapes clear in exactly `L` steps" enumeration is the kind
  of statement that could be quietly consuming the withdrawn exact-value claim.
* Failure mode A2-b: **F3's frame assignment is too coarse.** Theorem LOW is
  assigned to the hard core, but §7.6's own preamble derives it under the reductio
  *and* uses `f = α+1` only through Observation R1 — a judge may find a statement
  that needs neither frame exactly as drawn, i.e. the pair of terms may be right
  but the assignment of individual results to them wrong.
* Failure mode A2-c: F1's replacement sentence cites **Fact 2** — the same citation
  species as defect D2, and Fact 2's own scope (it is stated in §7.2 B's convention
  block) is not restated in §7.8.

Recorded so the returned report can be **scored**; none of them appears in the brief.

### OWNER RESULT — Theorem RIG (the decisive `L ≥ 3` rigidity step), `date` = 14:4x CDT

Full write-up: draft **§7.12**. Own script `problems/wowii/w61_r5_rig.py` → `.out`
(fresh this round, imports/reads no earlier `w61_*` code).

**Lemma CAP.** For `b ∈ B_lo` with `n_b` non-neighbours in `B`:
`1 ≤ deg_A(b) ≤ n_b + 1`. (Upper: `deg_B(b) = τ−1−n_b` and `deg(b) ≤ τ`. Lower:
`A` maximum.) **Corollary CAP1:** a B-universal low vertex has `deg_A(b) = 1`.
Hypotheses: `A` a maximum independent set — nothing else.

**Theorem RIG.** In the hard-core **frame**, if `B_lo ≠ ∅` and every low vertex is
B-universal, then `deg_A ≡ 1` on `B_lo`, the A-neighbours coincide in one `a₀`,
`a₀` is adjacent to **all** of `B`, every non-edge of `B` lies inside `B_hi`
(`ν = m̄ ≥ 1`), and no `a ∈ A∖{a₀}` touches `B_lo` — i.e. `G` is **exactly**
`GFan(τ,L,ν)`. Under the reductio, additionally `ν ≤ L−1` (Corollary MB1).

Why it matters, in order of weight:
1. **Corollary RIG-2** — that layer collapses to `GFan(τ,L,ν)` with `2 ≤ ν ≤ L−1`,
   because `ν = 1` is `Fan(τ,L)` and **Theorem FAN kills it for every `L ≥ 2`**.
   At **`L = 3` the whole B-universal layer is the single configuration
   `GFan(τ,3,2)`** — a named finite target, not a search.
2. **Corollary RIG-1** — Proposition L2(c) no longer needs its tightness re-run;
   `deg_A = 1` falls out of the degree cap. That retires **pre-declared failure
   mode L-d** of the §7.6 error prior (12:27 entry) before any judge sees §7.6.
3. **Lemma CAP is a new handle on the other layer**: it converts every A-degree
   lower bound into a non-edge count, so Lemma C\* now reads "every low vertex of
   `T₁ ∪ T₂` has ≥ 2 non-neighbours in `B`".

**Honest negative recorded (§7.12 D):** the `L = 2` argument that forced
`B_lo⁺ = ∅` does **not** generalize — at `L = 3` the budget admits `k = 1` with
`(c,m̄) = (0,1)` and with `(1,0)`, and the (F-b) contradiction needed both `c = 0`
and `m̄ = 0`. So the residual hard core at `L ≥ 3` splits as
**[B-universal layer: `GFan(τ,L,2…L−1)`] ∪ [`B_lo⁺ ≠ ∅`]**, and the second layer is
open. Successors must not re-derive "`B_lo⁺ = ∅` always" — it is false-by-budget.

**Numerics (own corpora).** 1 926 B-universal low vertices over exhaustive `n ≤ 7`
(2 931 `(graph, MIS)` pairs), random `n = 8…12` (6 119 pairs) and 622 targeted
frame instances: `deg_A = 1` in **1 926/1 926**. Theorem RIG's package (i)–(vi):
**33/33** hypothesis instances, **0 failures**. Scope demarcation **measured**: two
frame instances have `(L,ν) = (1,3)`, i.e. `ν > L−1` — the `ν ≤ L−1` clause really
does need the reductio and is not a frame fact.

**Next decisive step, named:** prove the `GFan(τ,L,2)` elimination — i.e. write out
the two generalized identities of §7.8 G's LEAD (`A′` total `= 2ν − E` from FAN-4;
`L ≤ 2ν − E` from FAN-8) and the step-count enumeration that leaves only the
single-part residues `[4]` (`E=0`) and `[3]` (`E=1`), both killed by FAN-6's
backward induction. That closes `L = 3`'s B-universal layer outright.

### ADJUDICATION — Q11 (T3-R3 round A) and Q10 (`L ≥ 3` rigidity pre-chew), `date` = 14:48 CDT

**Q11 — `problems/wowii/w61_S3_T3R3_qwenA.md`: CLEAN, and it COUNTS.** Scoring rule
satisfied: the report carries a full counterfactual-availability section (lemma
tables for controls C1–C4, naming **Lemma U as claimed-available in the `k = 0`
branch where its second hypothesis in fact fails**, i.e. the exact probe-4 species
round 1's Spark judge missed), and it computes HH trajectories (probe 5), including
a from-scratch re-derivation of the R3 sum contradiction
`Σ_{i≤3} D_i = X + Y = m − 1 < m` for general `a₀,b₀,c₀ ≥ 1` with the boundary
`a₀ = b₀ = c₀ = 1` checked explicitly. T-J1…T-J6 all PASS; T-J6 confirms R3 leaves
no sentence dangling. It also ran a refutation search (no `τ = 3` hard-core graph
found). → **T3-REPAIRED: 1 clean round on the R3 text.**

**Round B dispatched 14:47 CDT** — opus, non-Qwen as the same-source rule requires,
reads **only** `prompts/w61_S3_T3R3.md` (same text version as round A, no shared
information), forbidden the draft, `notes/`, every `w61_S3_*`, every `.py`/`.out`
under `problems/wowii/`, `orchestration/` and every other `prompts/` file. Own
calibrated HH implementation, no brief number reusable, refute-first, 5xx→30 s
retry ≤5×. Writes `problems/wowii/w61_S3_T3R3_opusB.md`. **Clean ⟹ T3's S3 gate
closes** (two clean rounds, different families, same text version).

*Error prior for T3 round B (§T13, declared before the verdict):* P(defect breaking
Theorem T3) ≈ 0.05; P(a further repairable gap) ≈ 0.40, concentrated in **R3
itself** — R3 deletes a clause and leans the whole `k=2 / e_B=2` branch on the sum
identity, so the failure mode I would bet on is that the sum identity's derivation
quietly reuses the deleted terminal-shape reading somewhere upstream in the same
branch.

**Q10 — both tabs adjudicated. Verdict: STRONG CONVERGENCE on the universal layer,
NOTHING ADOPTED, and the residual is confirmed to be where I independently placed it.**

* **Tab B (`w61_L3RIG_qwen_B.md`) proves exactly Theorem RIG** — "if every vertex of
  `B_lo` is B-universal then `p = 0`, `ν(B_lo) = 0`, `c = 0`, `ν = m̄ ≤ L−1`, every
  `b ∈ B_lo` has `deg_A(b) = 1`, all these unique A-neighbours coincide in one `a₀`,
  and `a₀` is adjacent to every vertex of `B`" — by a different route (its Lemma 1
  "pair-cycle neighbourhood" + Lemma 2 degree bounds, six steps) from mine (Lemma
  CAP, one line, plus Lemma 4). **Independence is genuine and checkable from
  timestamps**: draft §7.12 was written and flushed at **14:45:46** and the harvest
  files were first opened at **14:47** — the two derivations did not see each other.
  Two independent proofs of the same statement is the strongest corroboration this
  project has had on a new structural theorem.
* **What §7.12 has that tab B does not**: clause (e) (no `a ∈ A∖{a₀}` touches
  `B_lo`), which is what upgrades the conclusion from a degree/neighbour description
  to the **exact `GFan(τ,L,ν)` identification**; and **Corollary RIG-2** (`ν = 1` is
  `Fan(τ,L)`, killed by Theorem FAN ⟹ the layer is `GFan(τ,L,2…L−1)`, a single
  configuration at `L = 3`). Tab B explicitly reports no rigidity beyond `ν ≤ L−1`.
* **Tab A corroborates §7.12 D's honest negative, row for row.** Its skeleton row
  `(ν(B_lo), |B_lo⁺|, c, m̄) = (0,1,0,1)` — "leaves the nonuniversal low vertex free
  to have any number of cross-nonedges without violating the local inequalities" —
  **is my §7.12 D first sub-case**, reached independently. So "`B_lo⁺ = ∅` always"
  is now doubly refuted-by-budget and must never be re-derived as a theorem.
* **Both tabs converge on the same strategic obstruction**: the local toolkit
  (MB/SL/F-b/C\*) cannot control **`f = α+1` globally** — ruling out induced forests
  on `α+2` vertices is a condition on A-neighbourhood overlaps that no local
  inequality sees. **This is the round's strategic finding and it validates the
  target choice**: the way to close `L = 3` is the **HH-side** `GFan(τ,L,2)`
  elimination (§7.12 C), not more local budgeting.
* **NOT ADOPTED, registered as unverified**: both tabs' `G1/G2/G3` witnesses, the
  Problem-T explicit `L = 3` graph, both skeleton tables, and tab A's Lemmas 2.1/2.2.
  The harvests are summaries, not transcripts — no edge list is present, so
  byte-exact verification is impossible from the artifact (same ruling as w133's
  Q3). **The existence claim they carry is independently established by my own
  code anyway**: `w61_r5_rig.out` contains 4 hard-core-**frame** instances with
  `(L,ν) = (3,1)` and `B_lo⁺ = ∅`, generated and checked by
  `problems/wowii/w61_r5_rig.py`. (None has `residue = α`, as it must be — a
  hard-core instance would refute WOWII-61 outright.)
* **Same-source note**: nothing from either tab enters the draft, so §7.12 remains
  Qwen-free and a Qwen judge stays eligible for it. Q10 is **HARVESTED / ADJUDICATED,
  0 adoptions**; its value was corroboration + the `f = α+1` obstruction finding.

### OWNER RESULT — Theorem GFAN2 (the `L = 3` B-universal layer is empty), `date` = 14:54 CDT

Full write-up: draft **§7.13**. Scripts (own, this round): `w61_r5_gfan2.py` → `.out`
and the explicit shape table `w61_r5_gfan2_L3.out`.

Three generalized lemmas, all proved: **FAN-4′** (the `A′` residue at step `p+1`
totals `2ν − E`, `C`-part `= {L + e_c}`), **FAN-8′** (`E ≥ 1 ⟹ L ≤ 2ν − E`), and
**FAN-6′** — Lemma FAN-6 restated in the form its proof actually uses: *no `A′`
residue with a unique maximum `w ≥ 1` whose second-largest entry is `≤ w−2`*. That
restatement is worth more than the generalization: it kills `[3,1]`, `[4,1]`,
`[5,1]`, … as well as every single part, and it makes explicit why `[1,1]`, `[2,1]`,
`[2,2]` escape (Repair F4's point).

> **Theorem GFAN2.** For every `τ` and every `L ≥ 3`, no `GFan(τ,L,2)` graph has
> `residue = α`.

Proof shape: FAN-8′ leaves `E = 0` for `L ≥ 4` and `E ≤ 1` for `L = 3`; FAN-6′ kills
every single-part residue and `[3,1]`; the remaining residues (`[2,2]`, `[2,1,1]`,
`[1,1,1,1]`, and at `L = 3` also `[2,1]`, `[1,1,1]`) are killed by an explicit
uniform trajectory — while the common `C`-value is `≥ 3` the block is exactly the
other `C`-entries, so after `L−2` steps the list is `[2]^3` plus the untouched
residue, and the three tails then take 3, 3, 4 further steps, i.e. `L+1`, `L+1`,
`L+2` ≠ `L`. `L = 3` is an eight-row table, displayed in full in §7.13 B.

**Consequences.**
* **Corollary GFAN2-HC** — in the hard core, a B-universal low layer forces
  **`ν ≥ 3` and `L ≥ 4`** (`ν = 1` dies by Theorem FAN, `ν = 2` by GFAN2, and
  `ν ≤ L−1`).
* **Corollary GFAN2-L3** — **the whole `L = 3` layer of the hard core has
  `B_lo⁺ ≠ ∅`**: with Theorem RIG this empties the B-universal layer at `L = 3`
  outright. `L = 3` now lives entirely in the residual regime mapped in §7.12 D.

**§7.8 G's LEAD is corrected on the record.** It named `L = 4`, `E = 2`,
`C = [6,4,4,4,4]`, `A′ = [3,1]` as "the first genuine obstruction" at `ν = 3`. It is
not an obstruction — FAN-6′ kills `[3,1]`. Classifying all 20 measured `ν = 3`
survivors: every one with `L ≥ 4` is killed by FAN-6′, and the ones it misses are at
`L = 3`, where `ν = 3` cannot occur (`ν ≤ L−1`). So **`ν = 3` is measured-dead for
`4 ≤ L ≤ 11`** — *measured, not proved*: the general-`L` argument needs Step 2's
trajectory re-run for the partitions of `6`. Named as the next target; if it goes
through, the B-universal layer needs `ν ≥ 4` and `L ≥ 5`.

**S3 debt this creates.** §7.12 and §7.13 are new, unreviewed text; both are queued
for the next S3 dispatch (and both are **Qwen-free**, so a Qwen judge is eligible).

### OWNER RESULT — Lemma TAIL and Theorem GFANν (`ν ≤ 6`), `date` = 14:58 CDT

Draft **§7.13 D**. Script functions `tail_check` / `escape_check` / `complete_check`
in `problems/wowii/w61_r5_gfan2.py`; output `w61_r5_gfan2_complete.out`.

**Lemma TAIL** (hand-proved): for `E = 0` the step-`p+1` list is `[L]^{L+1} ∪ λ`,
and while the common `C`-value exceeds `λ₁` the block is exactly the other
`C`-entries, so for `L ≥ λ₁` the remaining step count is `(L − λ₁) + s₀(λ)` with
`s₀(λ) := steps([λ₁]^{λ₁+1} ∪ λ)`. **Survival is therefore a condition on `λ`
alone — `L` drops out.** Cross-checked against direct simulation on 1 817 `(λ,L)`
pairs, 0 mismatches.

That plus FAN-4′ (residue total `2ν − E`), FAN-8′ (`E ≥ 1 ⟹ L ≤ 2ν − E`) and
Corollary MB1 (`L ≥ ν+1`) makes `GFan(τ,L,ν)` a **finite** check for each fixed `ν`.
Running it:

> **Theorem GFANν.** For every `τ`, every `ν ≤ 6` and every `L ≥ ν+1`, no
> `GFan(τ,L,ν)` graph has `residue = α`. (`ν = 1` = Theorem FAN and `ν = 2` =
> Theorem GFAN2 have complete hand proofs; `ν = 3…6` are **computer-assisted** —
> declared as such in the draft — with the finiteness of the case list itself
> hand-proved.) At `E = 0` the only residue clearing in exactly `L` steps is the
> single part `[2ν]`, and FAN-6′ kills it; every `E ≥ 1` survivor is likewise
> FAN-6′-killed. Shapes tested at `E ≥ 1`: 0 / 3 / 24 / 110 / 397 / 1 211 for
> `ν = 1…6`; rows FAN-6′ misses: **none, at every `ν`**.

> **Corollary GFANν-HC.** In the hard core, a B-universal low layer forces
> **`ν ≥ 7` and `L ≥ 8`** (was `ν ≥ 3`, `L ≥ 4` an hour ago).

**Conjecture stated as a conjecture** (not proved): (C1) for every `ν`, no partition
`λ` of `2ν` other than `[2ν]` has `s₀(λ) = λ₁`; (C2) every `E ≥ 1` survivor's `λ`
has a unique maximum with second-largest `≤ λ₁ − 2`. If both hold for all `ν`, **the
entire B-universal layer of the hard core is empty at every `L`**, and the whole
hard core reduces to the `B_lo⁺ ≠ ∅` regime of §7.12 D. That is the standing next
target on this line.

### HANDOVER at round-5 end (`date` = 14:59 CDT)

**Two judges in flight, neither report on disk yet.**

| judge | dispatched | target | report file | what to do when it lands |
|---|---|---|---|---|
| FAN round A2 (opus) | 14:38 | §7.8 on the F1–F5 text, joints F-J1…F-J8 | `problems/wowii/w61_S3_FAN_opusA2.md` | CLEAN with both mandatory sections ⟹ §7.8 has **1** clean round and needs a second from a different family (Qwen eligible only if it never sees this report); PARTIAL/GAP ⟹ reproduce numerically, repair in a new draft section, brief rebuilt again |
| T3 round B (opus) | 14:47 | T3-REPAIRED on the R3 text, T-J1…T-J6 | `problems/wowii/w61_S3_T3R3_opusB.md` | CLEAN ⟹ **T3's S3 gate CLOSES** (Q11 round A already counts); report to planner for confirmation and move the registry rows in §7.11 |

**Do not edit `prompts/w61_S3_FAN_A2.md` or `prompts/w61_S3_T3R3.md` while they run.**

**S3 debt opened this round**: draft **§7.12** (Lemma CAP, Theorem RIG) and **§7.13**
(FAN-4′/6′/8′, Lemma TAIL, Theorems GFAN2 and GFANν) are new, unreviewed text. Both
are **Qwen-free**, so a Qwen judge is eligible; the natural dispatch is one brief
covering both, with joints on: CAP's degree count; RIG's (b)/(c) Lemma-4 chain and
the frame/hard-core scope split; FAN-4′'s bookkeeping at general `ν`; FAN-6′'s
restated hypothesis (does the backward induction really need only "unique max with a
gap of 2"?); FAN-8′; **Lemma TAIL's "block is exactly the other `C`-entries" step**
(a prefix/tie-break claim of exactly the species that has failed twice in this
document); and the declared computer-assisted status of GFANν at `ν = 3…6`.

**Queue**: Q10 ADJUDICATED (0 adoptions), Q11 ADJUDICATED (clean, round B dispatched).
No new Qwen row is needed for the `L ≥ 3` line right now — the open targets are
(C1)/(C2) of §7.13 D and the `B_lo⁺ ≠ ∅` regime of §7.12 D; the latter is the better
Qwen row, since both Q10 tabs already converged on its obstruction (`f = α+1` is not
locally controllable).

### ADJUDICATION — S3 round A2 for §7.8 (opus, F1–F5 text), `date` = 15:17 CDT

Report `problems/wowii/w61_S3_FAN_opusA2.md`: **PARTIAL**. F-J1…F-J6 SOUND, F-J7
PARTIAL, F-J8 (i) SOUND / (ii) sound-with-wrong-reason / (iii) **DEFECT** / (iv)
sound-with-stale-labels. Independence held; both mandatory sections present (T12
names **Theorem K / Corollary K1** — hypothesis holds in 0 of 13 139 Fan graphs —
and **Lemma FAN-2** as available-but-never-executing). Refutation effort is the
largest in the project's history: **22 027 441** exhaustively enumerated
`Fan(τ,L≥2)` sequences plus a 1.8 M second box, 233 149 random extreme instances to
`τ = 40`, `GFan` sweeps at `ν = 2,3` — **0 survivors**; 52 556 labelled runs under
two *malicious* tie-break policies — FAN-1/4/6/7/8 never broken; 193 491 reductio
instances from a 111 742-graph corpus — 0 failures of S/F3′/Z⁺/DICH/(LOW1)/SL/K.
**All findings UPHELD**, each reproduced first with my own code
(`problems/wowii/w61_r5_a2check.py` → `.out`). Repairs **G1–G5** in draft **§7.14**.

* **G1 (the real one).** §7.8 F's "Numerical agreement" still says "Theorem FAN
  predicts `residue = α−1` for *every* Fan sequence" — after F1 the theorem yields
  only `≤ α−1`. The withdrawn sentence is re-attributed to the repaired theorem
  **inside the repair's own target section**. Reproduced: `Fan(4,2)`,
  `A′ = [2,2]` → `deg = [5,5,4,4,4,2,2]`, `α = 3` (A verified maximum), `τ = 4`,
  `residue = 2 = α−1`, `s = 5`; the brief's witness `[5,5,4,4,4,2,1,1]` rebuilt and
  confirmed too. Repaired by splitting the sentence between Theorem FAN (`≤ α−1`)
  and **Observation FAN-E** (the exact value).
* **G2.** Lemma FAN-3's proof still ends "which is precisely the measured
  `α − residue = 1`" — the identical ex-falso identification F1(ii) forbids. Clause
  deleted. Factually correct (judge: 52 556/52 556), so audit-trail, not error.
* **G3.** Lemma FAN-2's proof is **tie-unsafe exactly at `j = L+1`**, where
  `p = τ−j+1` lets an `A′` entry tie with a `C` entry and "none is strictly above"
  stops working; the proof carries one unit of slack, so it covers `q ≤ 1` only.
  Never realized — my own count: `q = 0` in **837/837** instances whose high phase
  reaches that step (judge: 8 884, also all 0). Repair: FAN-2 restated as
  tie-incomplete **and struck from §7.8 E's PROVED list**. Zero impact (FAN-8 is
  unconditional and FAN-2 is unused).
* **G4 — a gain, not just a fix.** F1's "Lemma S does not fire (it needs `s = τ`)"
  misdiagnoses: Lemma S's *proof* is general-`s`; what fails is that its threshold
  moves to `s+1 = τ+2` while the `B_hi` degrees sit at `τ+1 = s`. Recorded as
  **Lemma S′** (every survivor has degree `≤ s`; `deg ≥ s+1 ⟹ head`). **Same
  species as R2's `F3 → F3′`** — two of §7.2 B's four tools have now proved to be
  general-`s`, and the rest should be re-read with that question before the next
  round.
* **G5 (cosmetic).** Two labels left stale by F3: §7.4 D / §7.6 C call their corpora
  "the hard core" when F3 makes them the **frame**; Corollary SL-HC's "`τ ≥ 3`" is
  stale under `τ ≥ 4`.

**Prior calibration, on the record.** My pre-declared **A2-a** ("the orphan sweep is
where a defect will be") named the right species but the wrong addresses — I pointed
at §7.8 E's case table and §7.8 G's LEAD; both orphans were nearer, one of them
inside the very section F1 repaired. A2-b and A2-c did not materialize as defects
(A2-c's shape did appear, as G4's Fact-2/Lemma-S citation species).

**Gate accounting.** **§7.8: still 0 clean rounds** — a round with confirmed defects
cannot count clean, and G1–G5 are new text; a fresh round on the G-text is required.
Worth stating plainly for the next brief: **this is the second consecutive round
whose every finding sat in repair/bookkeeping text rather than in the mathematics.**
The FAN chain's proofs have now been attacked by three independent judges (Qwen tab
B's original, opus round A, opus round A2) and every lemma has survived each time;
what keeps breaking is the prose around them. The next §7.8 brief should say so and
point the judge at the bookkeeping first.

### PLANNER RULING actioned — §7.8 loop-breaking procedure + general-`s` sweep, `date` = 15:2x CDT

Ruling received (corroboration `orchestration/tasks/w61_r6.md` item 1): G1–G5 accepted,
FAN-2 struck, Lemma S′ registered, gate arithmetic confirmed at **0 clean**. Three
standing instructions, recorded here as the procedure for the next §7.8 round:

1. **FREEZE after the repairs land.** Once G1–G5 are in, §7.8 (with §7.10/§7.14) is
   frozen: **no edits between dispatch and verdict**. Any bookkeeping fix found in
   the interim queues as an *annotation* for the following round instead of being
   written into the reviewed text. This is what breaks the "repair breeds a defect
   in the repair" loop that has now run three times.
2. **Next brief points at bookkeeping FIRST**, math joints second — attribution of
   claims to the right statement, orphan sweeps, status lines, labels, citation
   scope — since that is where every finding of the last two rounds has been.
3. **Saturation precedent (planner, going forward):** if the next round returns a
   **bookkeeping-only PARTIAL with all math joints sound again**, the planner will
   treat the FAN mathematics as **review-saturated** and close the gate via a
   **diff-scoped confirmation pass** on the residual text fixes — the K-CHAIN
   pattern — rather than demanding further full rounds. The pre-registered
   "confirmed defect ≠ clean" rule stays intact **for math findings**.

**Pre-dispatch action completed (planner-directed): the general-`s` species is now
EXHAUSTED in §7.2 B.** Write-up: draft **§7.14 addendum**; script
`problems/wowii/w61_r5_generalS.py` → `.out`.

* **Lemma T′** — Lemma T's first sentence is general-`s` verbatim ("the run has
  exactly `k` steps iff the list at the start of step `k` is `[D_k, 1^{D_k}, 0^…]`");
  `τ` plays no role. Its second sentence is the Fact-2 item already carried in §7.11.
* **Lemma H′** — general-`s` by replacing `τ` with `s` in its two `τ`-dependent
  places (the later-head count and the F3 citation, now F3′) — **but no new lemma is
  needed: H′ is already subsumed by Lemma DICH**, which is general-`s` and
  PROVED-S3. Recorded so no successor re-derives it.
* **Net: all four §7.2 B tools are known general-`s`** — F3′, S′, T′, and H via DICH.
  No tool there is stated more narrowly than its proof, so the D1/R2/G4 species
  cannot recur in that section.
* **Numerics, deliberately off the reductio**: exhaustive `n ≤ 7` + 700 random
  `n = 8…11`, canonical sort + two adversarial tie-breaks — **3 087 runs with
  `s ≠ τ`**; Lemma T′ **0 failures / 5 085** terminal steps; Lemma H′ **0 failures /
  13 274** `(head, step)` pairs.

### §7.8 round B — bookkeeping-first brief built and DISPATCHED, `date` = 15:23 CDT

Planner directive (r6 task book item 1): dispatch now, do not serialize behind T3-B.

**Brief `prompts/w61_S3_FAN_B.md`** (1 907 lines) supersedes `w61_S3_FAN_A2.md`.
Reviewed text = the **frozen** G-text (draft §7.8 + §7.10 + §7.14 as of 15:20).
Structure: appendix A–H (definitions + §7.8 as originally written), J (context),
**K = F1–F5**, **L = G1–G5 + the general-`s` addendum**, with an explicit precedence
rule — **L supersedes K supersedes H**.

Shape, per the recorded procedure:

* **Bookkeeping joints first, six of them**, each with its own verdict — **B-J1**
  attribution sweep (every measured/predicted claim: is it attributed to Theorem FAN
  (`≤ α−1`) or to Observation FAN-E (`= α−1`)? is G1 the *only* such site?);
  **B-J2** orphan sweep for anything still leaning on the withdrawn exact value,
  with §7.8 E's case table and §7.8 G's LEAD named as mandatory checks;
  **B-J3** status-line audit (verify G3's FAN-2 diagnosis independently; is any other
  lemma listed at the wrong status?); **B-J4** scope labels (F3's frame/hard-core
  pair, G5's fixes, and *which frame each proof actually needs*); **B-J5**
  citation-scope audit (Lemma S/S′, F3′, DICH, T/T′, Fact 2 — is the *form cited*
  available at that site?); **B-J6** the repairs and the three new lemmas themselves,
  including an independent re-derivation of the closure claim "no §7.2 B tool is
  stated more narrowly than its proof".
* **Mathematics joints second**, M-J1…M-J6 = the former F-J1…F-J6 unchanged.
* **Every defect must be classified BOOKKEEPING or MATHEMATICS**, and the judge must
  say which drives its verdict line. That is what makes the planner's saturation
  precedent applicable without further argument.
* The brief tells the judge honestly that the refutation effort already spent is
  very large and came back empty, so its marginal value is in the bookkeeping — and
  asks it to report the box it actually searched rather than out-enumerating.

**Dispatched 15:23 CDT — fresh opus judge**, reads only the brief, forbidden the
draft, `notes/`, every `w61_S3_*`, every `.py`/`.out` under `problems/wowii/`,
`orchestration/`, every other `prompts/` file. Own calibrated HH implementation, no
brief number reusable, 5xx→30 s retry ≤5×. Writes
`problems/wowii/w61_S3_FAN_opusB.md`.

**Cross-family row queued in parallel: `qwen_queue.md` Q14 READY**, same brief,
harvest to `problems/wowii/w61_S3_FAN_qwenB.md`. Same-source reasoning stated on the
row for planner override: Qwen's Q7 tab B *located* the Fan target but **no Qwen step
survives in the proof** (tab B's Lemma 1 superseded by FAN-8, its Lemma 2 by
FAN-4+FAN-6 — draft §7.8 F), so Qwen judges Claude's proof, not its own output, the
same call already accepted for Q5. If the planner disagrees, the row re-points at
codex Spark. Running both in parallel is what lets §7.8 reach two clean rounds from
**different families** without another serial cycle.

**FREEZE IN FORCE**: no edits to draft §7.8/§7.10/§7.14 or to
`prompts/w61_S3_FAN_B.md` until both verdicts are in. Interim bookkeeping findings
queue as annotations for the round after.

### Error prior for §7.8 round B, declared before any verdict (§T13)

**P(a MATHEMATICS defect) ≈ 0.04** — the FAN lemmas have now been attacked
independently three times, joint by joint, with a combined refutation effort in the
tens of millions of sequences and adversarial tie-break runs, and nothing has moved.
**P(at least one BOOKKEEPING defect) ≈ 0.5**, concentrated in section L, which no
judge has seen.
* Failure mode B-a (most likely): **B-J6 on the closure claim.** "No tool of §7.2 B
  is stated more narrowly than its proof" is a universal statement about a section I
  audited myself — and my last self-audit of a universal scope claim (F5) was wrong.
  The likeliest hole is that §7.2 B has a *fifth* item I am not counting as a "tool"
  (Fact 2, or Lemma 1's clauses), or that Lemma T′'s "only if" direction needs a word.
* Failure mode B-b: **B-J1's completeness.** G1 fixed one attribution sentence; §7.8
  E's numerical-status paragraph and §7.8 F's "Numerical agreement" are not the only
  places the exact value is quoted, and I have not swept §7.8 D's measured-status
  paragraph with the same care.
* Failure mode B-c: G3 strikes FAN-2 from one status line; a second list naming
  FAN-2 may survive elsewhere in H.

### ADJUDICATION — S3 round B for Theorem T3 (opus, R3 text), `date` = 15:30 CDT

Report `problems/wowii/w61_S3_T3R3_opusB.md`: **PARTIAL**. **T-J1…T-J4 CLEAN**
(the four joints that carry the mathematics), **T-J5 / T-J6 PARTIAL**. Both findings
UPHELD, each reproduced first with my own code (`w61_r5_t3check.py` → `.out`).
Repairs **J1–J2** in draft **§7.15**, written as annotations — no frozen text
touched.

**Refutation effort, the most complete this problem has had**: every `τ = 3` graph on
`n ≤ 37` (89.8 M tuples), a `μ ≤ 10` box (77.9 M, `n ≤ 73`), 7.7 M huge-multiplicity
instances (`n` up to ~10⁶), and an independent `2²¹` brute force at `n = 7` that
reproduces exactly the five hard-core degree sequences its own parameterisation
predicts. **No counterexample.** Plus **24 013 near-misses** that satisfy everything
except `f = α+1` — so **Theorem T3 is tight, not vacuous**, which settles the
near-vacuity worry (failure mode N-b) that has been open on this family since round 1.

* **J1 (the real one).** The `k = 0` bullet reaches the `p ≥ 3` exclusion by "同上",
  pointing at the `k = 1, e_B = 0` sentence that §7.3 5bis **itself declares false**
  at `p = 3` — while 5bis's replacement argument is written for `k = 1` only. A live
  branch of the exhaustive split therefore rested on a retracted sentence. *Repair:*
  widen to "`k ≤ 1` 要求 B 中至少两点度 ≤3（`k = 0` 时三点全部度 ≤3，更强）"; the rest of
  the paragraph stands verbatim, since the argument only ever used `k = 1` to get
  "at least two vertices of `B` have degree `≤ 3`", which is *weaker* at `k = 0`.
  **My own check**: enumerating that branch from the type-multiplicity
  parameterisation gives **10** configurations — **1 with `k = 0`**, 9 with `k = 1` —
  and `diam = 4` in **0** of them. The branch is real (the judge's `K_{3,3}` witness
  `d = [3,3,3,3,3,3]` lives in it) and the widened repair disposes of it.
* **J2.** §7.7's bullet scores the `k=2/e_B=2` terminal-count clause "*terse but
  correct*" with the diagnosis "undercounts the terminal shape" — but §7.8 B's
  **Repair R3 UPHELD and deleted that clause**, so the document both keeps and
  removes the same sentence; and §7.7's diagnosis is **itself wrong** (at `D_3 = 1`
  the shape `[1,1,0^…]` does have exactly one `1` after the head; the real defect is
  R3's mixed-reading one). *Repair:* withdraw both the score and the diagnosis and
  point at R3 as the operative treatment.
* **Corroboration kept**: the judge independently confirms **R3 itself is correct**
  (32 800/32 800 on `m`, `L¹`, `L²`, `D = (X,Y−1,1)`, `Σ_{i≤3}D_i = m−1`) and finds
  that **Lemma T never executes in that branch** (fires 0/32 800) — the structural
  reason the deleted clause could never have worked. The branch's Lemma T citation is
  decorative.

**Gate accounting — T3: 1 clean round, does NOT close.** Round A (Qwen, R3 text) was
CLEAN and counts; round B is PARTIAL, and confirmed defects cannot count clean; J1
and J2 are new text.

**For the planner (my call is only to flag it, not to make it).** Both findings are
**BOOKKEEPING-class** — a scope word (`k=1` vs `k ≤ 1`) and a stale score contradicting
a later repair — with **zero mathematics findings**, all four math joints CLEAN, and a
refutation search of ~175 M configurations behind them. **That is the same shape the
saturation precedent was written for**, but the precedent was declared for §7.8, and
T3 is a different target; whether it extends is the planner's ruling. If it does, the
natural instrument is a **diff-scoped confirmation pass on J1/J2 only**, riding along
with whichever judge dispatches next — the K-CHAIN pattern.

**Own numerical sanity** (`w61_r5_t3check.out`): 12 288 `τ = 3` graphs over all `e_B`
and all type multiplicities `≤ 2`, `A` verified maximum — **0 hard-core instances**.

### PLANNER RULING actioned — T3 J-pass dispatched, tightness registered, `date` = 15:34 CDT

Ruling (r6 task book item 1): the saturation precedent **extends to T3** as a
principle about evidence state; but **J1 is reclassified as MATHEMATICS** — a live
branch of an exhaustive split resting on a retracted sentence is a justification gap,
and the widening to `k ≤ 1` is new proof text no judge has seen. J2 stays
bookkeeping. Instrument: a diff-scoped pass with J1 as a named math joint. Clean on
J1 ⟹ T3 closes, on planner confirmation.

**Vehicle chosen: a dedicated standalone opus pass, dispatched 15:33 CDT.** The
planner offered two vehicles (ride with Q14's Qwen judge, or with the FAN-opusB
follow-up); I took neither, for two reasons worth recording. (1) Q14 is a **§7.8 FAN**
brief awaiting a Chrome-lease driver — bolting a `τ = 3` case-analysis part onto it
would both inflate an already ~1 900-line paste and mix targets in one conversation,
and it would leave the T3 gate blocked on driver availability. (2) The FAN-opusB
follow-up does not exist yet and its timing is unknown; the J-text is two short
amendments and does not need to wait. A standalone pass is cheaper than either and
blocks on nothing. Family note: T3 round A was Qwen and round B opus, so the two
**counting** rounds are already cross-family; the confirmation pass being opus
matches the K-CHAIN precedent exactly (there, D-DIFF rode an opus judge while one
counting round was also opus).

**Brief `prompts/w61_S3_T3_JPASS.md`** (791 lines) = new header + the verbatim
appendix of `w61_S3_T3R3.md` (definitions, the `τ = 3` parameterisation, the case
split, and the earlier repairs the amendments sit inside) + **section Z** = J1 and J2
in quote-then-repair form. The header states plainly that the body of T3 is **out of
scope** and that anything noticed there goes in a labelled non-scoring section.

Joints as the planner specified:
* **J-M1 (MATHEMATICS)** — four sub-questions, each answered separately: (a) does
  `k ≤ 1` really deliver "two vertices of `B` of degree `≤ 3`", and is that the only
  use of `k` — does no later step silently need `k = 1`? (b) at `p = 3`, does
  `deg_A(y) ≥ 3` with `deg(y) ≤ 3` force the multiplicities to vanish **including
  when `e_B ≠ 0`**, and is `e_B = 0` actually available wherever the argument is
  reached? (c) is the type list complete and does (F-b) genuinely fail on it?
  (d) **is the disposal exhaustive** — re-derive the 10-configuration enumeration
  independently and judge whether the parameterisation itself is complete for the
  branch.
* **J-B1 (BOOKKEEPING)** — J2's withdrawal of the stale score and wrong diagnosis,
  plus a sweep for any other sentence still asserting either.
* Most-valuable-outcome instruction: **find a `k ≤ 1, e_B = 0, p = 3` configuration
  with `diam = 4`** — that breaks J1 and re-opens a branch. Second: a step that needs
  `k = 1` and fails at `k = 0`.
* Own calibrated HH implementation, own enumeration, no brief number reusable, T12
  section mandatory, 5xx→30 s retry ≤5×. Writes
  `problems/wowii/w61_S3_T3_JPASS_opus.md`.

**Error prior for the J-pass, declared before the verdict (§T13).** P(J1's widening is
unsound) ≈ 0.05 — it removes a hypothesis rather than adding one, and the removed
hypothesis is used for a single weaker consequence. **P(the enumeration is incomplete)
≈ 0.2** — that is the sub-question I would bet on: my box capped the six non-universal
type multiplicities at 3, and while `p = 3` plus `deg_A(y) = 3` forces most of them to
zero, "the parameterisation cannot express configuration X" is exactly the kind of
completeness claim I have got wrong before (F5). P(J2 faulted) ≈ 0.03.

**Tightness registered as its own row** — draft §7.11, **registry addendum R-8**:
Theorem T3 is **tight, not vacuous**, on the strength of the round-B judge's **24 013
near-misses** (everything except `f = α+1`) against ~175 M configurations with no
counterexample. This settles failure mode **N-b**, declared in the very first error
prior of round 1 ("true but thin ... a strategic defect") and open across four
subsequent rounds. Corroborated in my own box: 12 288 `τ = 3` graphs, 0 hard-core.

### Gate-report requirement for the T3 J-pass (planner, 15:3x CDT) — recorded before the verdict

Planner confirmed the standalone opus J-pass as the vehicle (no override), accepted
R-8, and added one **reporting** requirement that must not be lost between now and
the verdict:

> **If the judge confirms the enumeration's completeness independently, the gate
> report must say so EXPLICITLY** — not fold it into a general "CLEAN".

Why this matters and how it will be reported. My declared bet was
`P(enumeration incomplete) ≈ 0.2`, the **F5 species** (a completeness claim I made
about my own audit and got wrong). So the gate report on T3 closure must state, as
separate lines:

1. whether the judge **re-derived the branch enumeration with its own code**, and
   what it returned (does it get the same configuration set, and the same `k = 0` /
   `k = 1` split?);
2. whether it judged the **parameterisation itself complete** for the branch — i.e.
   whether any configuration exists that the type-multiplicity parameterisation
   cannot express — and on what grounds;
3. **explicitly**: whether my `P ≈ 0.2` bet resolved for or against me. If the judge
   confirms completeness, the report says the bet lost and the completeness claim is
   now independently supported rather than owner-only. If the judge cannot confirm
   it, that is a **PARTIAL on J-M1(d)** and T3 does **not** close, whatever the other
   sub-answers say.

**T3 closure remains planner-confirmed, not self-declared.** No registry row moves
until the planner rules on the returned verdict.

### ADJUDICATION — T3 J-pass (opus, diff-scoped), `date` = 15:51 CDT

Report `problems/wowii/w61_S3_T3_JPASS_opus.md`: **PARTIAL**. J-M1 (a)(b)(c) SOUND;
**J-M1(d) exhaustive but my count claim wrong**; J-B1 withdrawal correct but
incomplete. Three defects, all UPHELD, reproduced with my own code
(`w61_r5_jcheck.py` → `.out`). Repairs **K1–K3** in draft **§7.16**.

* **K1 — the real one, and it is mine at one remove.** J1 widened the `p = 3`
  paragraph to `k ≤ 1`; the sentence **immediately after** it ("后续 `p ≤ 2 ≤ X−2 ⟹
  Lemma U ⟹ m ≤ X+4 与 m=X+6 矛盾` 原样有效") was written for `k = 1` and stayed
  behind, so the widening silently extended it to `k = 0`, **where it is false** —
  the `k = 0` branch never uses Lemma U (it ends with its own direct HH computation),
  and applying Lemma U there resurrects the blanket "`k ≤ 1 ⟹ Lemma U 可用`" the
  document retracted in round 2. Reproduced: the `k=0` branch's unique graph is
  `deg = [3,3,3,3,3,2,1]`, `n = 7`, `m = 9`, `α = 4`, `diam = 4`, own ending correct
  (`Σ_{i≤3} D_i = 8 = m−1 < m`); misapplied Lemma U gives `m ≤ X+4 = 7` against
  `m = 9` — **the forbidden slack-2 on the document's own control instance**.
  *(Honesty: my reading of `R` gives `#{3s} = 2`, not §7.7's `4`; I did not re-derive
  which reading is the draft's. The defect is independent of it — `m = 9 > 7` is
  reproduced directly.)* **Methodology datum recorded: widening a paragraph's scope
  silently widens every sentence that continues it.**
* **K2 — my "exactly 10 configurations" was a box artifact.** The branch is an
  **infinite family**: `K_{3,3}` plus `t ≥ 0` pendants at one `B`-vertex (`t = 0` →
  `diam 2`, `k = 0`; `t ≥ 1` → `diam 3`, `k = 1`). Repair: **delete the enumeration
  claim** and replace it with the judge's closed-form disposal, which is strictly
  stronger — every occurring type contains `x`, so every `A`-vertex is adjacent to
  `x`, giving `dist(a,a') = 2`, `dist(a,b) ≤ 3`, `dist(b,b') = 2`, hence **`diam ≤ 3`
  for the whole branch, unconditionally**, no box and no reductio.
* **K3 — J2 left its parent heading** ("Two wording fixes adopted (neither is a
  defect)") contradicting the bullet it introduces. Retitled.

**GATE — T3 does NOT close, and takes no shortcut.** The planner's ruling was
pre-committed: *"If the pass faults J1's repair, T3 needs a full round, no
shortcut."* The pass faulted the J-text twice — a false adjacent sentence activated
by J1 (K1) and a false claim inside J1 (K2). **T3 needs a full round on the K-text.**
I am not arguing the other way; K1 is a live false sentence inside a proof chain,
which is precisely what the rule exists for. T3 remains at **1 clean round**.

**Completeness bet, reported explicitly as pre-committed (planner requirement).**
1. **Did the judge re-derive the enumeration with its own code?** Yes — and at the
   same box size it reproduced my configuration set and my `k = 0` / `k = 1` split
   exactly (1 and 9).
2. **Is the parameterisation itself complete?** **Yes, independently confirmed** — it
   can express every configuration in the branch; the judge found nothing it cannot
   reach, and closed the branch in closed form instead.
3. **Did my `P ≈ 0.2` bet resolve for or against me?** **Against my text, in favour of
   the worry.** The F5 species recurred, in a new disguise: not "a configuration the
   parameterisation cannot express" but "**a claim quantified over a box presented as
   quantified over the branch**". The completeness of the parameterisation is now
   independently supported; my count claim is withdrawn and replaced by K2.

**Next**: T3 needs a full round on the K-text (brief not yet written — awaiting the
planner's word on sequencing, since §7.8's round B is still out and Q14 is still
READY). Judges outstanding: §7.8 FAN round B (opus). Queue: Q14 READY.

### PLANNER RULING actioned — K-text FROZEN, T3 K-round HELD, `date` = 15:5x CDT

Ruling (r6 task book): adjudication accepted; the judge's closed-form branch disposal
**adopted as operative text**; **sequencing = HOLD the T3 K-round**.

**FREEZE, effective now.** Draft **§7.16** (repairs K1–K3) is frozen under the same
discipline as §7.8/§7.10/§7.14: **no edits until the K-round verdict**. Any further
bookkeeping finding on the K-text queues as an *annotation* for the round after,
never as an edit to the reviewed text. Current frozen set:
**§7.8 + §7.10 + §7.14** (FAN, since 15:20) and **§7.16** (T3 K-text, since now).

**Operative-text marker.** Within K2 the **closed-form disposal is the operative
argument** and the enumeration is demoted to a spot check — i.e. the branch
`k ≤ 1, e_B = 0, p = 3` is disposed of by "*every occurring type contains `x`, so
every `A`-vertex is adjacent to `x`, whence `dist(a,a') = 2`, `dist(a,b) ≤ 3`,
`dist(b,b') = 2`, so `diam ≤ 3` unconditionally*". **No box, no enumeration and no
reductio appears in the operative chain.** The `t = 0…5` numbers are illustration
only and carry no weight; the K-round brief must present them that way, or it will
re-import the very defect K2 removed.

**Sequencing decision, recorded with its reasons** (planner's, not mine): the T3
K-round brief is written **only after both FAN verdicts (opus round B + Qwen Q14)
land and are adjudicated**. Reasons on the record: (1) **quota** — batch the
adjudications, THROTTLED is one meter-reading away; (2) the FAN loop's lesson that
rushed repair→review cycles breed defects; (3) any new bookkeeping species surfaced
by the FAN verdicts then folds into **one** K-round brief instead of two serial
rounds. **Family choice (Qwen free vs fresh opus) is deferred to dispatch time, with
the meter in view.**

**Two methodology entries landed by the planner from this verdict** — both are mine,
and the K-round brief must carry them as named probes:
1. **Scope-widening contagion (K1).** Widening a paragraph's hypothesis silently
   widens every sentence that continues it. Probe: after any scope widening, re-read
   the *following* sentences and check each independently at the new boundary.
2. **Box-vs-branch quantification artifact (K2) — the F5 species' third disguise.**
   A claim quantified over a finite computational box, presented as quantified over
   the mathematical branch. Probe: for every count reported about a family, ask
   whether the family is finite, and if not, whether a closed-form argument replaces
   the count.

**State at hold.** T3: **1 clean round**, K-text frozen, K-round pending. §7.8: **0
clean rounds**, opus round B out, Q14 READY. Nothing else is in flight from me.

### ADJUDICATION — §7.8 round B (opus, bookkeeping-first), `date` = 16:00 CDT

Report `problems/wowii/w61_S3_FAN_opusB.md`: **PARTIAL**, self-classified
**BOOKKEEPING-driven**. **M-J1…M-J6 all CLEAN** — the third independent judge to
certify the FAN chain joint by joint. Bookkeeping: B-J2, B-J5 CLEAN; B-J1, B-J3, B-J4
PARTIAL; **B-J6 GAP**. Six defects, all UPHELD, reproduced with my own code
(`w61_r5_bcheck.py` → `.out`). Repairs **V1–V5** in draft **§7.17**, written as
annotations — no frozen text edited. Refutation again empty: 332 044 Gale–Ryser
sequences, 1 328 176 labelled runs with adversarial tie-breaks, `α − residue = 1`,
`s = τ+1`, `E = 0`, `q = 0` at `j = L+1` in every instance.

**The pre-declared prior B-a hit, and on my own text.** I wrote before dispatch that
the likeliest hole was "Lemma T′'s 'only if' direction needs a word". That is V1.

* **V1 — MATHEMATICS, and mine.** Lemma T′ was stated as an **iff**; the "only if"
  direction is false under `residueAux`'s **ℕ-truncation**. Witness reproduced:
  `[4,1,1,0,0,0]` terminates in exactly 1 step without the terminal shape, and is
  **not graphical** — which is the hypothesis the proof used silently. Repaired by
  adding graphicality (equivalently Lemma 1(2)); T′ then holds on **1 245/1 245**
  graphical atlas sequences. **Cited by nothing** — T′ came from the general-`s`
  completeness sweep and the FAN chain never uses it.
* **V2 — Repair F3 re-commits the D3 species it was written to cure.** It files
  **Theorem LOW and Theorem SL** under "the hard core", but both are proved under the
  **reductio alone**. Witness reproduced: `C₅` has `residue = α` (reductio TRUE) while
  `diam = 2` and `f = 4 ≠ α+1` (frame FALSE). Repaired by replacing F3's two tiers
  with **three**: *reductio only* (S/S′, T/T′, F3′, DICH, Z⁺, LOW, SL) / *frame*
  (Lemma 4, C\*, R1, (F-b)) / *hard core* (MB, L1/L2, SL-HC, L1-short, FAN-HC, all FAN
  lemmas).
* **V3 — the sharpest.** Every FAN lemma stands on the reductio, but **Theorem FAN
  proves no `Fan` graph satisfies it** — real `Fan` runs have `s = τ+1` (reproduced:
  `Fan(4,2)`, `τ = 4`, `s = 5`). So §7.8's `M1–M4` / `H1–H5` blocks are measured where
  the lemmas' standing hypothesis is **false**. §7.6 G carries exactly this firewall;
  §7.8 carried none, and G1 fixed only the residue-*value* sentence — so B-J1's "is G1
  the only such site?" is **no**. Repaired by inserting the firewall: those runs are
  **mechanism checks off the reductio**, not instances of the lemmas.
* **V4** — G3's status sweep fixed §7.8 E's PROVED list but not §7.8 A's twin, which
  still lists FAN-2. Struck there too. *Same species, one round later.*
* **V5 — an upgrade, not a demotion.** Observation FAN-5 was listed PROVED with its
  second half only simulated (`L = 2…8`). **Lemma TAIL (§7.13 D) proves it in
  general**: `λ = [2]`, `s₀ = 2 = λ₁`, total `= L` for every `L ≥ 2`; verified against
  direct simulation at `L = 2…9`. FAN-5 becomes a corollary of TAIL.

**Kept as the round's best structural observation** (not a defect): the judge's
counterfactual check finds **DICH(b) — the chain's main engine — fires on 0 heads in
all five controls**, because inside the `Fan` family it can only execute under
`s = τ`, which Theorem FAN proves never happens. That is the sharpest available
statement of why this chain is a reductio and why its numerics can only ever be
mechanism checks; it is what V3 now says in the text.

**GATE — §7.8: still 0 clean rounds.** Six confirmed defects, and **V1 is a
mathematics defect**, so the pre-registered rule bites on its own terms — I am not
claiming the saturation precedent here.

**For the planner's weighing, stated precisely and without advocacy.** The precedent
was declared for "a bookkeeping-only PARTIAL with all math joints sound again". This
round is *almost* that and not quite: **all six math joints of the FAN chain are
CLEAN for the third consecutive independent judge**, the refutation searches now total
tens of millions of sequences across four judges with nothing found, and the single
mathematics defect is **not in the FAN chain at all** — it is in a toolkit lemma
introduced by the previous repair round, used by nothing. Whether that counts as
"bookkeeping-only" for gate purposes is the planner's ruling; my own reading is that
the rule as written says no, and I would rather be told I was too strict than close a
gate I talked myself into.

**Next**: both FAN verdicts are now in (opus round B here; **Q14's Qwen round is still
READY/undispatched**), so the planner's hold on the T3 K-round is the live question —
its condition was "both FAN verdicts land and are adjudicated".

### CORRECTION (owner-w61, `date` = 16:01 CDT) — my "Q14 READY" was STALE

**My error, flagged by the planner and corrected here rather than left standing.**
Several entries above (the round-B dispatch record, the J-pass record, the round-B
adjudication and my accompanying reports) describe **Q14 as "READY / undispatched"**.
That was true when I wrote the first of them and **false by the time I repeated it**:
re-reading `orchestration/qwen_queue.md`, row Q14 reads

> **DISPATCHED (08-18 15:5x, owner-intel qwen_queue driver round 9)**,
> conversation `https://chat.qwen.ai/c/b5a9411f-2783-48b1-99c1-429d55272671`,
> model-confirmed Qwen3.8-Max, harvest target `problems/wowii/w61_S3_FAN_qwenB.md`.

The driver took the Chrome lease and pasted the brief while I was adjudicating the
opus round; I carried my own earlier snapshot forward instead of re-reading the row.
**Root cause: I treated a queue status I had written myself as still current.** The
queue is driver-owned, not owner-owned — its rows change under me. *Standing
correction to my own practice: re-read `qwen_queue.md` immediately before reporting
any queue state, never quote a remembered status.*

Consequence for the record: the planner's **hold on the T3 K-round continues on its
original condition** (both FAN verdicts landed and adjudicated) — Q14 is the second
of the two and is generating now, not waiting on a driver.

*(Also logged from the Q14 row, for `notes/web_model_ops.md`: on this Qwen build the
model-selector option row **silently no-ops on coordinate clicks even when batched**;
a `computer left_click` using the `ref` from `read_page`/`find` worked first try.
That is the second independent sighting of this failure mode.)*

### PLANNER FORWARD PLAN recorded (r6 task book) — the §7.8 close is now conditional and pre-specified

Gate ruling on round B: **0 clean, no saturation claim — my reading stands.** V1 is
mathematics and the rule bites on its own terms; the planner declines the other-side
argument **for now** but records its substance: the math defect sits **outside** the
FAN chain (an uncited toolkit lemma added by a repair round), and three consecutive
judges have certified all six FAN math joints with tens of millions of refutation
sequences empty.

**Pre-specified forward plan** (so the next dispatch is mechanical, not a fresh
decision):

* **If Q14's mathematics joints are also clean** — a fourth independent read,
  cross-family, on the same frozen text — the planner closes §7.8 via **ONE
  diff-scoped pass on the V-text**, *regardless of any further bookkeeping-class
  findings in Q14*. That pass must carry:
  1. **V1's graphicality repair as a named MATHEMATICS joint**;
  2. the **three repair-species probes** from methodology — *(a)* statement riders
     are separate proof obligations, *(b)* **scope-widening contagion** (K1), *(c)*
     **box-vs-branch quantification artifact** (K2, the F5 species' third disguise);
  3. the **J/K-text riders** (T3's K1–K3, which supersede J1–J2) as a second named
     part sharing the same dispatch.
* **If Q14 faults a FAN mathematics joint** — full round, no shortcut.

**Accepted this round**: V2's three-tier scope fix, V3's firewall (and the
DICH(b)-fires-on-zero-heads structural clarity), V5's TAIL upgrade.

**Prep done, dispatch withheld.** The stable half of that brief — its header, joint
structure and scoring rules — is written to `prompts/w61_S3_VPASS_prep.md` and marked
**DO NOT DISPATCH**. Its appendix is deliberately **not** assembled yet: if Q14
returns bookkeeping findings they become repairs, and those repairs belong inside the
same single pass. Assembling now would guarantee a stale appendix — the exact defect
species (box/scope/rider staleness) this whole sequence has been about.

### ADJUDICATION — §7.8 round B, cross-family (Qwen3.8-Max, Q14), `date` = 16:1x CDT

Report `problems/wowii/w61_S3_FAN_qwenB.md`: **PARTIAL**, self-classified
**BOOKKEEPING-driven** — *"all defects found are BOOKKEEPING, none MATHEMATICS."*
**All six FAN mathematics joints CLEAN** (M-J1…M-J6), plus B-J1/B-J2/B-J4/B-J5 clean.
**Fourth independent judge, second model family**, to certify the chain joint by
joint. Its refutation box (τ ≤ 6, `L ∈ {2,3}`, `E = 1` escapes, arbitrary tie-breaks)
was empty; its own HH implementation was calibrated on `K₂`/`C₅` first; its T12
section independently names **DICH(b)** as claimed-available-but-never-executing —
the same structural fact V3's firewall states, arrived at from a different family.

Full adjudication in draft **§7.18**. Three bookkeeping defects, each reproduced with
my own code first (`problems/wowii/w61_r6_q14check.py` → `.out`; calibrated
`residue(K₂)=1`, `residue(Cₙ)=⌈n/3⌉`, `n = 3…9`):

* **D1 (stale FAN-2 PROVED line in §7.8 A) — UPHELD, DUPLICATE of Repair V4.**
  Reproduced at draft line 1725, character-for-character the site V4 struck one round
  earlier. No new repair; what it buys is that **two families independently found the
  same stale twin-list**, so V4 is confirmed rather than one judge's reading.
* **D2 (Observation FAN-5 PROVED on a simulated half) — UPHELD, DUPLICATE of V5, and
  Qwen supplies a second independent proof.** Reproduced at draft line 1940. V5 proved
  the second half via Lemma TAIL; Qwen, not having TAIL, proved it by the one-step
  induction `[L]^{L+1},2 → [L−1]^L,2` with base `[2,2,2,2]`. **I verified Qwen's route
  myself: induction step and direct simulation both hold 39/39 for `L = 2…40`**, and
  the sort is stable because `2 ≤ L−1` at `L ≥ 3`. FAN-5's second half now has **two
  independent proofs from two families**. No further repair.
* **D3 (the "Lemma T's second sentence needs Fact 2" note is an overstatement) — NOT
  UPHELD as stated; new repair V6.** Qwen is right that under the *literal* in-scope
  reading the implication needs nothing — but only because it is then **vacuous**:
  Lemma T's first sentence makes its antecedent impossible under the standing reductio.
  Under the only contentful reading (off the reductio) Fact 2 is needed **twice** —
  to make "after step `τ−1`" well-formed, and to pass `s ≠ τ ⟹ s ≥ τ+1 ⟹ residue ≤ α−1`.
  **Measured over all 1 893 731 connected graphs on `n ≤ 7`**: antecedent-true with
  `s = τ` — **0** instances (vacuous, as Qwen says); antecedent-true with `s > τ` —
  **139 066**; Fact 2 violations — **0**; `s < τ` — **0**. So the note is right and the
  objection is right, about different readings, and **the real defect is that the text
  never says which reading it means**. **Repair V6 (BOOKKEEPING)**: state the sentence
  off the reductio with its Fact 2 citation, and record that in-scope it is vacuous.
  Same species as V2 — a statement filed under a hypothesis its proof does not use —
  recurring one round later on the sentence next door.

**Nothing in Q14 touches the mathematics**, and it missed V1/V2 (it worked from the
§7.8+§7.10+§7.14 text; Lemma T′ lives in the §7.14 addendum and is cited by nothing).
Frozen text untouched: everything above is annotation in §7.18.

### DISPATCHED — the V-PASS, one diff-scoped closing pass, `date` = 16:2x CDT

**The planner's pre-committed forward plan fired on its own terms** — Q14's
mathematics joints are clean, so §7.8 closes via ONE diff-scoped pass on the V-text
regardless of its further bookkeeping findings (which are the two duplicates and V6
above). Brief assembled to `prompts/w61_S3_VPASS.md` per the recorded recipe:
header + `w61_S3_FAN_A2.md` appendix A–H/J/K (byte-identical to what rounds A2 and B
already reviewed — verified by diff) + section **L** (G1–G5, from the round-B brief)
+ section **M** (V1–V5, neutralised) + section **N** (V6, neutralised) + section **P**
(T3's K1–K3, neutralised) + the T3 context appendix. 2 609 lines / 158 KB.

Deltas from the recipe, both deliberate:
1. **A V-B4 joint was added** to carry V6 — and it asks for more than V6: sweep every
   call site of Lemma T's second sentence, and ask the same scope question of **Lemma
   T′'s** second sentence and **Lemma S′'s** head-forcing clause. If the species is
   still live it should surface there.
2. **Q14's inductive proof of FAN-5 was kept OUT of section M.** It is a Qwen-authored
   step, and putting it in the reviewed text would have handed Qwen its own output to
   review — the exact firewall the Q5/Q14 precedent depends on. It stays on the record
   in §7.18 only. *(V6 itself is clean on this test: it is my derivation, and it
   **rejects** Qwen's claim rather than adopting it.)*

**Family = Qwen, queued READY as row Q18** (not dispatched by me: I do not hold the
Chrome lease). Reasons on the record: the firewall check above is clean, so Qwen is
eligible under the Q5/Q14 precedent; cross-family coverage for §7.8 is already met by
Q14; the meter is **THROTTLED** and a new opus long-run is discouraged, while Qwen is
free. I judge cross-family unnecessary here — the V-text is a repair layer authored by
opus judges and by me, so a Qwen read *is* the cross-family read.

**Paste-size guard**: 158 KB is ~36 % larger than the biggest brief this queue has
successfully pasted (`w61_S3_FAN_B.md`, 116 KB). Pre-built fallback splits
`prompts/w61_S3_VPASS_p1.md` (Part 1, 123 KB) and `_p2.md` (Part 2, 34 KB), each
self-contained and each edited to stand alone; the brief itself declares Part 2
independent of Part 1, so splitting changes no mathematics. The driver does not have
to make that call under pressure.

### GATE ARITHMETIC as it stands — NOTHING CLOSED, both await the planner

* **§7.8 — 0 clean rounds.** Rounds so far: A (PARTIAL, F1–F5), A2 (PARTIAL, G1–G5),
  B/opus (PARTIAL, V1–V5, V1 a MATHEMATICS defect), B/Qwen = Q14 (PARTIAL, V6 + two
  duplicates). Four judges, **two families**, **all six FAN mathematics joints CLEAN
  in the last three**, refutation searches empty at tens of millions of sequences. The
  pre-registered rule ("a round with a confirmed defect is not clean") still gives
  **0**, and I am not claiming saturation. The planner's ruling replaced the *route*,
  not the count: **§7.8 closes iff the V-pass returns with no MATHEMATICS defect in
  Part 1.** If it does, §7.8 goes to 1 clean round *and the planner has pre-committed
  that this one pass suffices*; if it faults a mathematics joint, the shortcut is void.
* **T3 — 1 clean round** (round B/opus on the R3 text). J-pass PARTIAL → K1–K3;
  K-text §7.16 frozen since 15:5x. The planner's hold on the K-round was conditioned on
  "both FAN verdicts landed and adjudicated" — opus B at 15:5x (§7.17), Q14 now
  (§7.18) — so **the hold is discharged**, and per the same forward plan the K-text
  rides this dispatch as Part 2 instead of taking its own round. **T3 closes iff the
  V-pass returns with no MATHEMATICS defect in Part 2**, which would make 2 clean
  rounds against the pre-registered bar of 2.
* **Neither gate is marked closed here.** The verdict returns to the planner for
  confirmation, per the standing gate-report requirement.

**In flight at round end**: Q18 (V-pass) READY in `qwen_queue.md`, awaiting whoever
takes the Chrome lease. Nothing else is out from me. Frozen set unchanged:
**§7.8 + §7.10 + §7.14** (FAN) and **§7.16** (T3 K-text); §7.17 and §7.18 are the
annotation layers and are now themselves under review as sections M and N.

---
## ROUND 8 (owner-w61) — **BOTH GATES CLOSED, REGISTRY MOVE EXECUTED**, `date` = Tue Aug 18 17:5x CDT 2026

Planner confirmation 17:48 CDT (`orchestration/tasks/w61_r6.md`, appended note):
**§7.8 CLOSED** (pre-committed condition met: Q14 mathematics joints clean ⟹ one
diff-scoped V-pass with **V-M1 clean**; Q18 delivered it, scored GENUINE in §7.19(a)).
**T3 CLOSED** (the §7.16 "full round, no shortcut" clause ruled to require genuine
independent mathematical review, delivered in substance by Q18 **Part 2**'s independent
re-derivation of K-M1 and K-M2; T3 = round A clean + round B math-clean + K-text
re-derived clean).

**Executed in one step** (draft §7.20 is the execution record; §7.11 carries the rows):

* **§7.11 rows R-9…R-13 → PROVED-S3**: Lemmas FAN-1/3/4/6/7/8 (R-9); **Theorem FAN**
  (R-10); **Lemma T′**, graphicality-repaired, zero call sites (R-11); **Lemma S′** +
  H′-via-DICH + the §7.2 B general-`s` closure (R-12); **Theorem T3** with repairs
  J1–J2, K1–K3 (R-13). Evidence chains cited per row: opusA / opusA2 / opusB / Q14 /
  Q18 V-pass; T3 = round A (`w61_S3_T3R3_opusB.md`) + Q18 Part 2.
* **V1–V6 folded from annotation into operative text in the same step** (V1 → §7.14,
  V2 → §7.10 F3 three-tier, V3 → §7.8 A firewall, V4 → §7.8 A status, V5 → §7.8 D/E,
  V6 → §7.2 B), plus **W1/W2/W3**, plus **J1/J2/K1/K2/K3** landed at their §7.3/§7.7
  sites (R-13 must not point at defect-carrying text).
* **Do-not-overreach constraints honoured**: **Observation FAN-5 did not move** (rests
  on Lemma TAIL, 0 S3 rounds — Q18's D2, recorded as W2); **Corollary FAN-HC did not
  move** (rests on the §7.6 chain, 0 clean rounds); **Lemma FAN-2 stays superseded**;
  §7.12/§7.13 held out entirely.
* **Freezes LIFTED**: §7.8 + §7.10 + §7.14 (FAN) and §7.16 (T3 K-text). Annotation
  layers §7.15/§7.16/§7.17/§7.18 keep their text verbatim as audit trail, each banner-
  marked LANDED with its operative sites; superseded gate bullets inside them are
  marked superseded, not deleted. **Frozen set is now empty.**

**Remaining S3 debt (next round's docket seed — NOT started this round):**
1. **§7.6 chain under Corollary FAN-HC** — Theorem MB, Corollary L1-short, Corollary
   MB1, Proposition L2: PROVED, **0 clean rounds** (B-76 judge never returned). This is
   the largest debt: it is the only one gating a statement the FAN work would otherwise
   have finished.
2. **Lemma TAIL** (§7.13 D): **0 rounds** — and with it FAN-5's second half and the
   `ν ≤ 6` elimination.
3. **§7.12/§7.13 GFAN family** — Theorem RIG, Theorem GFAN2, Theorem GFANν (incl. the
   `ν = 3…6` computer-assisted demarcation): **0 rounds**, no row queued.
4. **Theorem LOW / Theorem SL / Corollary SL-HC** (§7.6): 0 clean rounds, and V2's
   re-tiering gives them new scope text nobody has reviewed.

**Addendum (same step, 17:5x CDT):** the fold had to reach one round further back —
**F1–F5 and G1–G5 were also annotation-only** against the frozen §7.8, so R-9/R-10
would have certified text still carrying their defects. All landed: F1 (Theorem FAN
restated `residue ≤ α−1`, justification deleted, Observation FAN-E split out), F2/G3
(Lemma FAN-2 header), G2 (FAN-3 ex-falso clause deleted), F4 (FAN-6 parenthetical),
F5 (§7.9 audit sentence struck), G1 (§7.8 F "Numerical agreement"), G5 (§7.4 D corpus
label, Corollary SL-HC `τ ≥ 4`). Every annotation section keeps its text verbatim as
audit trail with a LANDED banner naming the operative sites.

---

## ROUND 9 (owner-w61) — **the whole remaining S3 debt is now brief-written and queued**, `date` = Tue Aug 18 18:0x CDT 2026

Short brief-writing slice under THROTTLED. **No mathematics was written this round.**
Three self-contained Qwen briefs were built out of the §7.20 debt table and queued as
**READY** rows. **I did not dispatch anything** — the driver holds the Chrome lease
and dispatches.

### Debt → brief mapping (complete: every row of the §7.20 table is covered)

| §7.20 debt | objects | brief | queue row | named joints |
|---|---|---|---|---|
| **S3-D1** (largest — FAN-HC's sole gate) | Theorem MB, Corollary L1-short, Corollary MB1, Proposition L2 | `prompts/w61_S3_76_qwen.md` (80 KB) | **Q23**, P1-highest | **J-MB, J-L1s, J-MB1, J-L2**, plus **J-LOW / J-SL** because MB is derived from the (LOW3) form of Theorem SL and neither has ever been refereed |
| **S3-D2** | Lemma TAIL (+ Observation FAN-5's second half, + the `ν ≤ 6` elimination's leg) | `prompts/w61_S3_TAIL_qwen.md` (41 KB) | **Q24** | J-TAIL-BLOCK, J-TAIL-IND, J-TAIL-EQUIV, J-TAIL-DEF, **J-FAN5** (`λ = [2]`), J-SCOPE |
| **S3-D3** | Theorem RIG, Theorem GFAN2, Theorem GFANν incl. the `ν = 3…6` computer-assisted demarcation | `prompts/w61_S3_GFAN_qwen.md` (138 KB) | **Q25** | J-CAP, J-RIG, J-RIG-NU, J-RIG12, J-FAN4P, J-FAN8P, J-FAN6P, J-GFAN2, **J-GFANNU**, J-CORHC, J-SCOPE |
| **S3-D4** (smallest — rider, as planned) | Theorem LOW, Theorem SL, Corollary SL-HC under **V2's new, never-reviewed scope text** | rides Q23 | **J-SCOPE** (tier-by-tier audit of all ten §7.6 statements, mismatches reported in *both* directions) and **J-SLHC** (incl. the `τ ≥ 4` parenthetical from Repair G5(ii)) |

**Why TAIL stands alone rather than riding Q23.** It gates a *different* statement
(Observation FAN-5, on the §7.8 line) from the §7.6 chain, so a single mixed verdict
would couple two independent gates in one report — the coupling the V-PASS had to
work around with an explicit "say which part the defect is in" clause. It is also
small enough to run beside the two large briefs on the free channel, and its appendix
overlaps §7.13, not §7.6, so riding Q23 would have duplicated more text than standing
alone. Its consumer inside Theorem GFANν is refereed in Q25 (J-GFANNU), not here, so
no statement is refereed twice.

### The computer-assisted demarcation is a named joint, as instructed

**J-GFANNU** asks two questions and requires them answered separately:
1. **Is the finiteness argument hand-proved?** The case list is finite because of
   FAN-4′, FAN-8′, Corollary MB1 and Lemma TAIL. The judge must check the case split
   is exhaustive — `E = 0` with `L ≥ λ₁` (TAIL), `E = 0` with `ν+1 ≤ L < λ₁ ≤ 2ν`
   ("checked directly"), `E ≥ 1` (bounded by FAN-8′) — and that `λ₁ ≤ 2ν` is justified.
2. **Is the enumeration reproducible?** The judge does not have the script. It must
   reconstruct the enumeration from the text alone and print **its own** table,
   reusing none of the printed counts (0 / 3 / 24 / 110 / 397 / 1 211). The brief
   states in terms that **a computer-assisted proof that cannot be reconstructed from
   its own description is itself a reportable defect.**

### Same-source check, stated per brief (this was an explicit requirement)

* **Q23 / §7.6** — Claude-authored throughout (owner-w61 round 4; Theorem LOW was
  re-derived by the owner *before* the round-3 Claude-`fable` helper's probe script
  was opened, which is why it was adopted). **Qwen eligible.** The one Qwen-authored
  input is **Lemma 4** (§7.1, root-verified line by line on adoption); the brief puts
  Lemma 4's *proof* out of scope by the same-source rule while explicitly keeping *how
  §7.6 uses it* in scope.
* **Q24 / Lemma TAIL** — Claude-authored (owner-w61 round 5, 14:58 CDT). **Qwen
  eligible.** Firewall honoured: Q14's Qwen-authored second proof of FAN-5's same half
  was kept out of the draft at the time and is **not** in this appendix.
* **Q25 / §7.12+§7.13** — Claude-authored; the earlier Qwen pre-chew (Q10) was
  adjudicated with **0 adoptions** and the section was recorded Qwen-free at 14:5x.
  **Qwen eligible.** Corollary MB1 and Lemma TAIL are imported while under review in
  Q23/Q24; the brief refereess the *import*, not those proofs.

All three briefs carry: refute-first ordering (refutation log before any verification
narrative), the **three T12 amendments** (counterfactual availability; witness
validated against every defining constraint, most basic first; delivered/repaired
statements must ship an instance satisfying all their own hypotheses or be marked
possibly vacuous), the **three repair-species probes** by name (statement riders /
scope-widening contagion / box-vs-branch quantification artifact), a
**statement-hypothesis audit** against the three-tier scope text (quoted verbatim as
appendix section T, and itself under review), own-implementation + calibration
(`residue(K₂) = 1`, `residue(Cₙ) = ⌈n/3⌉`, `n = 3…9`) with "reuse no number printed in
this brief", explicit boundary lists, and the deliverable format with a MATHEMATICS /
BOOKKEEPING label on every defect.

### Error priors, declared BEFORE dispatch (§T13) — not in any judge's prompt

**Q23 / §7.6 chain.** P(material defect breaking Theorem SL or Theorem MB) ≈ **0.15**;
P(a repairable gap somewhere in the chain) ≈ **0.60** (up from the 0.55 declared for
the B-76 judge in round 4, because V2's re-tiering added never-reviewed scope text).
* Failure mode **9-a** (most likely, carried over from the round-4 prior): Theorem SL
  **Step 4**, `λ_j ≤ ℓ_j − 1` — an equality is written with `λ_j` the actual count and
  a *bound* is then substituted; the substitution must be sign-correct.
* Failure mode **9-b**: Proposition **L2(c)**'s tightness re-run — tightness needs
  every link of MB → SL(LOW3) → LOW tight simultaneously, which is not spelled out.
  (Note §7.12's Corollary RIG-1 claims to remove exactly this step; if the judge
  faults L2(c), RIG-1 is the standing repair and the conclusion likely survives.)
* Failure mode **9-c** (new): the V2 tier line "Theorem LOW / Theorem SL are
  reductio-only" — a silent use of `f = α+1` or `diam = 4` inside SL Steps 1–6 would
  make it false, and nobody has re-read those six steps against the new tier.

**Q24 / Lemma TAIL.** P(material defect) ≈ **0.10** (short multiset argument,
cross-checked against direct simulation on 1 817 `(λ,L)` pairs); P(a rider/boundary
defect) ≈ **0.50**.
* Failure mode **9-d** (most likely): the **"consequently"** sentence drops the
  standing `L ≥ λ₁` hypothesis while asserting `L`-independence — the statement-rider
  species, which is what this document produces most often.
* Failure mode **9-e**: an off-by-one in "steps" at the terminal list (the spec stops
  when the head is `0` and returns the remaining length), which would move every count
  by one and, at `λ = [2]`, break Observation FAN-5's second half rather than TAIL.

**Q25 / GFAN family.** P(material defect in FAN-4′ / FAN-8′ / FAN-6′ / GFAN2) ≈
**0.25**; P(the `ν = 3…6` enumeration is *not* reconstructible from the text as
written) ≈ **0.50**.
* Failure mode **9-f** (most likely): **FAN-6′'s restated hypothesis** is weaker than
  its induction needs — specifically `a_j ≥ 1 + e_j ≥ 1` at `j = 1`, and the claim
  that the decremented `A′` entries are the largest ones under ties.
* Failure mode **9-g**: the **boundary rows** `ν+1 ≤ L < λ₁ ≤ 2ν` of Theorem GFANν
  ("checked directly") are not exhaustive, or `λ₁ ≤ 2ν` is unjustified — this is the
  seam between the hand proof and the machine, i.e. exactly what J-GFANNU targets.
* Failure mode **9-h**: Theorem RIG's "**Consequently** `G` carries **exactly** the
  configuration `GFan(τ,L,ν)`" proves one direction and asserts both.

### Dispatch discipline for the driver

* **Three fresh conversations, one per brief.** No judge may be shown another judge's
  report, this dispatch file, or the error priors above.
* Harvest to `problems/wowii/w61_S3_76_qwen.md`, `…_TAIL_qwen.md`, `…_GFAN_qwen.md`.
* Scoring rule unchanged: a round with a confirmed defect **cannot** count clean; a
  CLEAN counts only if both mandatory sections (T12 + own computation with the
  calibration output) are actually present.
* Gate arithmetic if the verdicts come back clean: §7.6 chain → 1 clean round (the
  two-family bar still open, so **Corollary FAN-HC does not promote on Q23 alone**);
  Lemma TAIL → 1 clean round, and Repair W2's citation caveat on Observation FAN-5
  becomes liftable; §7.12/§7.13 → 1 clean round. **Nothing closes this round.**

---

## ROUND 10 (owner-w61) — **Q23/Q24 adjudicated, seven repairs landed, both second-family rounds written and queued**, `date` = Tue Aug 18 19:1x–19:3x CDT 2026

Short adjudication slice under THROTTLED. **No new mathematics.** Full adjudication
record with quotes and repairs: draft **§7.21**. Reproduction script:
`problems/wowii/w61_r10_adjudicate.py` → `.out` (own `residueAux`, calibrated on
`residue(K₂) = 1` and `residue(Cₙ) = ⌈n/3⌉` before any adjudication number; no number
from either report reused as input).

### Verdicts and what they cost

Both rounds: **PARTIAL, zero MATHEMATICS defects, both mandatory sections present and
substantive.** Q23 raised 4 bookkeeping defects, Q24 raised 3 boundary defects. **All
seven reproduced, none refuted, all repaired** (X1–X4 in §7.6/§7.10, Y1–Y3 in §7.13 D).
Under the planner's pre-registered rule a PARTIAL with zero mathematics defects does
**not** count clean as it stands, so neither round moved a gate; each converted a
0-round statement into a 1-round-repairs-landed statement whose second family is queued.

One judge claim did not survive intact: Q24 calls `λ = [4], L = 2` the *smallest*
failure of the equivalence rider. It is a genuine failure and reproduces exactly, but
`λ = [2], L = 0` (⟹ direction) and `λ = [3], L = 1` (⟸ direction) are smaller. The
defect stands; only the superlative was wrong.

### Error priors of ROUND 9, scored

| prior | outcome |
|---|---|
| **9-a** Theorem SL Step 4 sign-correctness (declared most likely for Q23) | **MISS** — Steps 1–6 verified individually by the judge, and `λ_j` enters with coefficient `+1`, so the substitution is sign-correct |
| **9-b** Proposition L2(c) tightness not spelled out | **DIRECT HIT** — Q23 Defect 1, predicted statement, predicted reason |
| **9-c** V2's reductio-only tier line false via silent `f = α+1` / `diam = 4` | **HALF** — J-SCOPE did come back PARTIAL, but the widening is sound; the real defect is omission + *over*-hypothesising, the opposite direction |
| **9-d** TAIL's "consequently" drops `L ≥ λ₁` (declared most likely for Q24) | **DIRECT HIT** — Q24 Defect 3, down to the species |
| **9-e** off-by-one in `steps` breaking FAN-5 at `λ = [2]` | **MISS** — `steps([2,2,2,2]) = 2` recomputed twice independently |

**2 hits / 1 half / 2 misses of 5 scoreable** (9-f/g/h unscored — Q25 never ran). Both
hits are the **statement-rider** species (a conclusion restated without the hypothesis
it was proved under), now 3-for-3 in this document; neither miss belongs to it.
**Methodological consequence, recorded for future rounds: declare priors by species
first and by site second** — the site-level "most likely" call was wrong in one of two
cases while the species-level call was right in both. Probability declarations
themselves were well calibrated (0.15/0.60 and 0.10/0.50 against 0 material + 4, and 0
material + 3).

### The two second-family briefs (written this round, both READY, neither dispatched)

Both are built from the round-9 briefs by script — `problems/wowii/w61_r10_build_sol_brief.py`
and `…_build_spark_brief.py` — so they are regenerable and the transformation is auditable.
Construction rules, identical in both:

1. **The appendix carries the REPAIRED text**, taken live from the draft.
2. **Repair provenance is rewritten into the author's voice.** The draft keeps every
   〔Repair X…/Y… LANDED, from Q23/Q24 Defect n〕 annotation as the audit trail; the briefs
   carry the corrected mathematics with the provenance stripped. A second-family judge that
   is shown what the first family found is not an independent family. Leak probes are part
   of the build output (`Repair X`: 0, `Q23`: 0 in the sol brief; `Repair Y`: 0, `Q24`: 0 in
   the spark brief).
3. **The two joint rows that quoted pre-repair wording were re-aimed** at the text as it now
   stands (J-MB's inclusion claim, J-L2(c)'s squeeze) — which also keeps them from
   signposting the edits. All other joints are unchanged, as instructed: same names, same
   count, same order.
4. **A hard read restriction**, new and necessary because these judges run with filesystem
   access inside the repository: the draft, `notes/reviews/`, `problems/wowii/w61_S3_*`,
   `prompts/w61_S3_*`, `orchestration/`, and anything named `dispatch`/`adjudicate`/
   `harvest`/`qwen` are off limits; a joint that cannot be done without one is to be marked
   UNRESOLVED, not read around.
5. Each brief says the text has had **one** round from another family and that the judge is
   the second — the fact, never the content — and that two passages have been edited since,
   unmarked, to be found the ordinary way.
6. Both now say plainly: you have a filesystem and a Python interpreter, use them, keep the
   scripts; and both name the file the report must be written to.

| row | brief | model | size | gate |
|---|---|---|---|---|
| **Q26** | `prompts/w61_S3_76_sol.md` | codex `gpt-5.6-sol` | 84 KB | **TIME GATE 22:49 CDT** (weekly quota reset; planner pre-authorised this single dispatch) |
| **Q27** | `prompts/w61_S3_TAIL_spark.md` | codex `gpt-5.3-codex-spark` | 44 KB | none — independent weekly quota; must not delay Q26 if the TUI holds one session |

**Why Spark for TAIL and not a rider on the Q25 re-dispatch** (the alternative that was
on the table): Q25 is Qwen, and TAIL's first round was Qwen — riding it would buy a
second round of the *same* family and satisfy no bar. Q25's brief is also the 138 KB
paste that drew the CAPTCHA; enlarging it is exactly the wrong move. And the target
suits Spark specifically: Lemma TAIL is a pure multiset/Havel–Hakimi statement,
falsifiable by direct simulation, which is the mechanical work this family does well,
as opposed to the graph-theoretic case analysis it has measured badly on (4/4 vs 0/4).
Sequencing bonus: Q27 landing before the Q25 re-dispatch means Q25's J-GFANNU imports a
two-family Lemma TAIL instead of a one-family one.

### Dispatch discipline for the driver (unchanged except where noted)

* codex TUI, screen session `codex`, **file + one-line instruction** (`Read <brief> and
  execute the task in it.`) — never paste a brief into the TUI, long `stuff` strings
  truncate silently. Confirm "Working" on a `hardcopy`; answer `a` to any approval box.
  **Register the TUI lease before use.**
* Q26 not before 22:49 CDT. Q27 may run earlier on its own quota.
* Harvest to `problems/wowii/w61_S3_76_sol.md` and `problems/wowii/w61_S3_TAIL_spark.md`
  (each brief tells its judge to write there itself).
* Scoring rule unchanged: a round with a confirmed defect cannot count clean; CLEAN
  counts only with both mandatory sections actually present.

### Gate arithmetic if the two come back clean

* **§7.6 chain**: 1 (Q23, repairs landed) + 1 clean second family (Q26) ⟹ two families on
  the current text ⟹ **Corollary FAN-HC's last dependency clears** and it may be proposed
  for PROVED-S3 — planner confirmation required, as always; the owner does not self-mark.
* **Lemma TAIL**: same shape with Q27 ⟹ Repair W2's citation caveat on Observation FAN-5
  becomes liftable and FAN-5 can move.
* **§7.12/§7.13**: still 0 rounds; Q25's re-dispatch is the only path, and nothing else
  in the line is blocked on it.

---

## ROUND 11 (owner-w61) — **Q27 (Spark, Lemma TAIL) adjudicated: CLEAN and it COUNTS**, `date` = Tue Aug 18 20:37 CDT 2026

Short adjudication slice. **No new mathematics.** Report audited for shallowness FIRST
(Q18 precedent; the run initially false-completed at 85 s with no output before the
planner nudge; the 20:04 landing is the real one).

### Shallowness audit — PASSES, this is not a skim

* The judge's script + 24 KB output exist on disk (`problems/wowii/
  w61_S3_TAIL_spark_check.py` / `.out`, both 20:04) and the script is a genuine fresh
  `residueAux` implementation matching the appendix-A spec (ℕ-truncated decrement,
  0-head terminal, step not counted).
* All six joints (J-TAIL-BLOCK/IND/EQUIV/DEF, J-FAN5, J-SCOPE) carry substantive,
  *correct* rationales, not restatements: strict `t > λ₁` in the block claim, loop
  bounds `t = L … λ₁+1`, the equivalence checked in both directions **under** the
  retained `L ≥ λ₁` (i.e. the round-10 Y-repair verified as its own obligation),
  `steps([2,2,2,2]) = 2` recomputed from spec.
* Its numbers are internally consistent (3125 + 1211 = 4336 = 271 × 16; 272 = Σ p(n),
  n = 0…12) and were **not** copied from the brief (the brief's cross-check count is
  1 817 pairs; the judge's box is 4 336).
* All mandatory sections present: refutation log + calibration, joint table, three
  repair-species probes by name, T12 section, "could NOT check", out-of-scope.
  **One weak-form execution flagged for the planner**: the T12
  counterfactual-availability clause is satisfied in a thinner form than the K-chain
  exemplars — it names FAN-5's first half / Theorem GFANν as visible-but-not-executed
  and supplies the `L < λ₁` mismatch inventory (462 witnesses) as the control content,
  rather than a lemma-available-on-control-that-never-fires. For a pure multiset
  target I judge this meets the bar; planner to confirm.

### Adjudication — every checkable claim reproduced, none refuted

Own fresh implementation (no reuse of the judge's code or any prior script's numbers),
calibrated on `residue(K₂) = 1` and `residue(Cₙ) = ⌈n/3⌉` before any adjudication
number: `problems/wowii/w61_r11_adjudicate.py` → `.out`. **ALL REPRODUCED**:

* calibration table including `steps(Cₙ)` values — exact match;
* box `Σλ ≤ 12`, `L ≤ 15`: 272 partitions, **3 125 in-hypothesis pairs, 0 mismatches**
  against `(L−λ₁) + s₀(λ)`; 1 211 out-of-hypothesis pairs, **462 mismatches** — exact;
* FAN-5 second half: `s₀([2]) = 2 = λ₁`, `[L]^{L+1} ∪ [2]` clears in exactly `L` for
  all `L = 2…15`;
* boundary rows (`[1,1]` at `L=1`; `[2ν]`, `ν = 1…6`, all `s₀ = 2ν`; four
  repeated-maxima samples) — exact;
* the judge's superlative "smallest outside-hypothesis counterexample is `λ=[2], L=0`"
  — **correct under both orderings tried** (total content and multiset length), unlike
  Q24's round-10 superlative;
* **adjudicator's extra, closing the one hole in a canonical-sort-only simulation**:
  adversarial tie-breaks at the block boundary, 377 in-hypothesis multisets × 3
  randomised runs — **0 tie-dependent step counts** (consistent with the value-multiset
  tie-invariance argument already used by FAN-1).

### Gate arithmetic for Lemma TAIL — proposed to planner, not self-marked

* Round 1 = Qwen (Q24): PARTIAL, **0 MATHEMATICS defects**, 3 boundary defects Y1–Y3
  all repaired in §7.13 D → 1 round, repairs landed.
* Round 2 = Spark (Q27) on the **repaired** text: **CLEAN**, 0 defects of any class,
  both mandatory sections present, real simulation, all claims reproduced by owner.
  Under the pre-registered scoring rule this **counts as a clean round**.
* ⟹ **Lemma TAIL meets the two-family bar** (Qwen + codex-Spark, same text version),
  subject to planner confirmation of the T12 weak-form caveat above. If confirmed:
  1. **Repair W2 releases** — the citation caveat on Observation FAN-5 becomes
     liftable; FAN-5's second half now rests on a two-family TAIL and **FAN-5 can
     move** (first half = FAN-3, already certified).
  2. **Theorem GFANν's finite-case import** of TAIL is discharged at two-family
     strength (GFANν itself is refereed separately and still has 0 rounds).
  3. **Q25's re-dispatch ordering condition is satisfied** — Q27 landed first, so
     Q25's J-GFANNU imports a two-family Lemma TAIL, as ROUND 10 intended.
* Not counted, stated for the record: the judge did not name the edited-since-round-1
  passage explicitly, but its J-TAIL-EQUIV and Probe R1 verify exactly the edited
  rider under its retained hypothesis, which is what the check was for.

## PLANNER CORRECTION (22:54 CDT) — Q26 time gate
My ROUND-10 pre-authorization asserted sol "resets tonight 22:49" — WRONG: /status ground truth reads "0% left, resets 22:49 on 19 Aug" (RESOURCES.md had the correct date all along; planner misread it while scheduling — the same manual-transcription-without-verification species this project keeps legislating against, now caught in planner hands; date-gate assertions must be re-verified against the recorded source at scheduling time). **Corrected gate: Q26 dispatches no earlier than 22:49 CDT Aug 19.** Substitution considered and REJECTED: Spark would technically satisfy the two-family bar (TAIL precedent) but is measurably weak on case-analysis proofs (T3: 0/4 vs Qwen 4/4) and a weak CLEAN would not survive our own scoring rules — quality argues for waiting for sol. FAN-HC promotion simply waits; nothing else is blocked.

---
# ROUND 12 (owner-w61, 2026-08-22 00:1x–00:4x CDT) — Q25 adjudicated, GFANν text rebuilt, FAN-5/TAIL registry move executed, Q26 adjudicated

## Q25 — GFAN family (Qwen3.8-Max, `w61_S3_GFAN_qwen.md`), verdict **GAP**

**Scored per statement, not per report** (§7.22 (a)). Ten of eleven joints CLEAN or
bookkeeping-PARTIAL, with genuine independent work: own `residueAux` calibrated on
`residue(K₂)=1` / `residue(Cₙ)=⌈n/3⌉` before use, FAN-4′'s mass identity `2ν−E` and
FAN-8′'s bound `L ≤ 2ν−E` re-derived from scratch, all three GFAN2 `L≥4` trajectories
and all eight `L=3` rows re-simulated, T12 counterfactual control run
(`[5,5,4,4,4,2,1,1]`, `τ=4,L=2,ν=1`, residue `3=α−1`), explicit "could NOT check"
section. **⟹ 1 clean round** for Lemma CAP/CAP1, Theorem RIG, RIG-1, RIG-2, Lemmas
FAN-4′/8′/6′, Theorem GFAN2, Corollaries GFAN2-HC/GFAN2-L3.

**J-GFANNU = GAP, and the cause was a BRIEFING defect of mine**: the `ν=3…6`
enumeration was cited by filename and never pasted, so the judge could not reproduce
the decisive "FAN-6′ misses = none" column. It nevertheless certified the *hand-proved
skeleton* (case split disjoint + exhaustive, `λ₁ ≤ 2ν`, MB1/TAIL imports legitimate)
and re-derived the `E≥1` shape counts `0/3/24/110/397/1211` from its **own** partition
formula. Theorem GFANν stays at **0 rounds**.

**Defects 4/4 UPHELD** — D1 (FAN-6′'s `[w] for every w≥1` is false at `w=1` under the
zero-carrying convention) → **Z1**; D2 (reproducibility) → **Z2**; D3 (no tier assigned
to any §7.12/§7.13 statement) → **Z3**; D4 (Theorem RIG's converse sentence) → **Z4**.
All landed in operative text. No mathematical falsity claimed anywhere in Q25.

## Repair Z2 — the enumeration is now text-complete (draft §7.22 (c))

New artifacts `problems/wowii/w61_r12_gfannu_embed.py` / `.out`. Embedded in the draft:
the shape-generation spec (unlabelled multisets; zero-inertness **verified**, 480 lists
× 6 paddings, 0 padding-dependent counts; no graphicality filter, by an explicit
superset argument; abort conventions; parameter ranges), the full `E=0` `s₀`-column for
all **159** partitions of `2ν` (`ν≤6`) with `[2ν]` the unique survivor at every `ν`,
all **51** `E=0` boundary pairs with their **9** survivors, the closed form
`S(ν)=Σ_{E=1}^{ν−1}(ν−E)·p(E)·p(2ν−E)` reproducing `0/3/24/110/397/1211` and its
per-`E` split, and the complete roster of all **72** surviving `E≥1` rows with FAN-6′
certificates. The demarcation line moves from *the whole enumeration* to *one
completeness claim about an explicitly specified finite set*. Planner independently
re-ran the script 00:2x: byte-identical to the committed `.out`, all headline counts
confirmed against both `.out` and the §7.22 (c) text.

## Registry move EXECUTED (draft §7.22 (d))

**R-14 Observation FAN-5 → PROVED-S3** (both halves) and **R-15 Lemma TAIL →
PROVED-S3**, on the planner's 20:38 two-family confirmation (Q24 Qwen + Q27 Spark CLEAN
on repaired text). **Repair W2 LIFTED** at the §7.8 D site. **Debt S3-D2 CLOSED.**
Three constraints ride: FAN-HC does not move on this, GFANν does not move, RIG/GFAN2
do not move on one round. Planner confirmed the move 00:2x.

## Q26 — §7.6 chain (codex `gpt-5.6-sol`, `w61_S3_76_sol.md`), verdict **PARTIAL, 0 MATHEMATICS defects**

Second family on the **repaired** text (X1–X4), doubling as the repair-confirmation
pass exactly as pre-registered in draft §7.21 (e).

**Shallowness audit — `sol` is a new family, so it was calibrated: GENUINE, 8/8**
(draft §7.23 (a)). Highlights: calibration printed before use; T12 control is a
*separating pair* (Control R = `C₅`, reductio-yes/frame-no; Control F =
`E={02,13,24,25,34,35}`, `A={0,1,4,5}`, frame-yes/reductio-no); names an
available-but-non-executing lemma; **refuses to launder vacuity** — 8 frame graphs and
0 frame+reductio graphs in its box, said twice, ingredients attacked instead;
20 682 labelled trajectories under 6 tie orders with maximum (not maximal) `A`.

**Owner reproduction** (`problems/wowii/w61_r12_adjudicate.py` / `.out`, own
transcription, no number reused from the report): the 8 calibration residues, the 12
class predicates of both controls, the SL boundary instance `E={03,12,13,23}`,
`A={0,1}`, and D1's replacement fact — **all reproduce exactly**.

**Defects 2/2 UPHELD, both BOOKKEEPING.** D1: SL-HC's "(note `τ ≥ 4`)" cites Theorem
T3 for a rider the proof never consumes and which was not supplied to the judge →
**AA1 landed**, replaced by the local `diam = 4 ⟹ τ ≥ 2` (27 stars, `n = 2…7`, 0 with
`τ≤1` and `diam>2`). D2: independent second-family reproduction of X3(ii), **extended
by one statement** (SL-HC) → **AA2 landed**, six → seven.

### Gate arithmetic for the §7.6 chain — proposed to planner, NOT self-marked

* Round 1 = Q23 (Qwen): PARTIAL, 0 mathematics defects, X1–X4 landed.
* Round 2 = Q26 (codex `sol`) **on the repaired text**: PARTIAL, 0 mathematics
  defects, AA1–AA2 landed; faulted none of X1–X4, so repair-confirmation is discharged.
* ⟹ **the §7.21 (e) pre-registered condition — "FAN-HC promotes only if Q26 comes back
  clean on the mathematics" — is MET.** Ready to move to PROVED-S3 on confirmation:
  Theorem MB, Corollary L1-short, Corollary MB1, Proposition L1, Corollary L1′,
  Proposition L2, Theorem LOW, Theorem SL, Corollary SL-HC, **and Corollary FAN-HC**.
  Registry move prepared, not applied.

## Dispatched this round

**Q30 — READY** (`orchestration/qwen_queue.md`): Theorem GFANν re-round on the rebuilt
text. Brief `prompts/w61_S3_GFANNU_qwen.md`, **31 KB** (one fifth of the 138 KB Q25
paste that drew the CAPTCHA twice), regenerable via
`problems/wowii/w61_r12_build_gfannu_brief.py`, which runs a **leak check** so no
pointer to the review record survives into the brief. Ten joints: J-FIN, J-SPEC, J-E0,
J-BND, J-COUNT, J-SURV, J-KILL, J-FAN6P, J-IMPORT, J-HC. **Family note for the ledger:
Q30 is family 1 for Theorem GFANν and does NOT supply the second family for the
11-statement Q25 group — that needs a non-Qwen family on the repaired text.**

## ROUND 12, part 2 (00:4x CDT) — **PLANNER CONFIRMED; the §7.6 chain and Corollary FAN-HC are PROVED-S3**

Planner confirmation 2026-08-22 00:4x CDT, with five personal checks recorded in draft
§7.24 (including an independent re-run of **Q26's own checker** — every number agrees,
`FAILURE_COUNT = 0` — and personal certification of Repair AA1's replacement argument).

**EXECUTED — registry rows R-16…R-19** (draft §7.24): Theorem LOW, Theorem SL (R-16);
Theorem MB, Corollary L1-short, Corollary MB1, Proposition L1, Corollary L1′,
Proposition L2 (R-17); Corollary SL-HC + Repair AA1 (R-18); **Corollary FAN-HC**
(R-19, released by the first three). Repairs AA1/AA2 landed in the same step.

**S3-D1 and S3-D4 are CLOSED.** With S3-D2 closed earlier in this round, the entire
remaining S3 surface of WOWII-61 is the GFAN family: **S3-D3a** (11 statements at 1
clean round, needing a **non-Qwen** second family on the repaired text) and **S3-D3b**
(Theorem GFANν at 0 rounds, Q30 queued).

**Two hygiene items from the same confirmation, both done:**
* `problems/wowii/w61_S3_76_sol_check.out` was a hand-formatted summary, not the
  script's raw stdout — same reproducibility species as the permalink rule.
  **Regenerated as raw stdout** (1 201 lines, `FAILURE_COUNT=0`); the judge's original
  summary is preserved as `w61_S3_76_sol_check_summary.md`.
* Round-12 repair annotations (Z1–Z4, AA1, AA2) were written with the Chinese marker
  「LANDED」 inherited from earlier rounds. **All six rewritten to `LANDED`** per the
  English-only rule for internal artifacts.

## ROUND 12, part 3 (00:4x–00:5x CDT) — dispatch authoring and own attack

**Q33 authored and queued READY** (renumbered from Q31 after a collision with w133's
allocation): `prompts/w61_S3_GFAN_sol.md`, 43 KB, codex `gpt-5.6-sol`, planner-approved
as the **widened** brief covering **both** open GFAN debts in one dispatch — Part 1 the
11-statement group (non-Qwen second family, on the repaired text, doubling as the
repair-confirmation pass) and Part 2 Theorem GFANν (family 1 or 2 depending on Q30's
landing order). 14 named joints. Modelled on Q26's disciplines, with two additions
written in from this round's lessons: an explicit **vacuity-honesty clause** (the GFan
frame has no small witness — Q25 failed to construct one — so a family that launders
vacuity would produce a worthless CLEAN) and a **raw-stdout requirement** (the Q26
hygiene defect, legislated so it cannot recur). Builder
`problems/wowii/w61_r12_build_sol_gfan_brief.py`, leak check clean. **Owner did not
drive the TUI**; dispatch is the planner's.

**Own attack (draft §7.25).** Three statements proved by hand: **Lemma C1-A**
(`s₀([2ν]) = 2ν` for every `ν`, by a two-step parity induction — this removes the
`E = 0` single-part row from the machine-checked interior for **all** `ν`, not just
`ν ≤ 6`); **Proposition C1-B** (`s₀(λ) = λ₁ ⟺ residue([λ₁]^{λ₁+1} ∪ λ) = k+1`);
**Corollary C1-C** (C1 follows from exhibiting a realization with `α ≤ k`, via
Favaron–Mahéo–Saclé). C1 verified over all 10 268 terminating cases with `n ≤ 28`,
zero violations, bound attained 196 times. **C1 and C2 remain CONJECTURES.**

**The enumeration extends clean to `ν ≤ 10`** (`w61_r12_gfannu_ext.py` / `.out`):
`E ≥ 1` shapes `3 340 / 8 457 / 20 126 / 45 450`, survivors `75 / 137 / 251 / 447`,
**FAN-6′ misses = none** at every `ν`, and the §7.22 (c-4) closed form predicts all
four counts — J-COUNT re-verified four steps outside its range. **Deliberately NOT
folded into Theorem GFANν's statement**: Q30 and Q33 are holding the `ν ≤ 6` text, and
desynchronising a theorem from a brief a judge is reviewing would void the round. The
upgrade (Corollary GFANν-HC from `ν ≥ 7, L ≥ 8` to `ν ≥ 11, L ≥ 12`) is a one-line
edit once those rounds land.

**Own attack, late addition (00:4x CDT):** **Conjecture C1 is PROVED for `k ≤ 2`** —
**Lemma C1-A′** (`steps([c]^{c+3}) = c+1`, by a self-reproducing shape
`[t]^2 ∪ [t−1]^t`) and **Theorem C1-2** (`s₀((w,c)) = λ₁ + 1` exactly, and the list is
a step sequence iff `w+c` is even — which is automatic for `λ ⊢ 2ν`). Numerical
backing `problems/wowii/w61_r12_c1k2.py` / `.out`: 1 830 pairs `c ≤ w ≤ 60` and
`V(c)`, `c = 1…79`, **0 mismatches**. What remains of C1 is `k ≥ 3` only; recorded at
the site that the excess is *not* `λ₁ + (k−1)` (`λ = (2,1,1)` has excess 1,
`λ = (2,2,2)` has excess 2), so the mechanism to generalise is the self-reproducing
shape, not the arithmetic.
