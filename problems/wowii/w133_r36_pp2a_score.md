# PP2A — SCORING RECORD, round 36. Free engine channel, n = 5 per arm.

Instrument: `problems/wowii/arms_r34/w133_r34_arm{A,B,D}.md`, hashes verified against
`w133_r34_prereg.md` this round (see `w133_r36_pp2a_dispatch_prereg.md` §0).
Pre-registration: `w133_r34_prereg.md` + the dispatch addendum
`w133_r36_pp2a_dispatch_prereg.md` (both written before any output existed).

## Dispatch record
* **Channel**: OpenRouter `stealth/ox-alpha` — the free engine channel this project uses for
  first-pass review (`ENGINE_BACKLOG.md`). **Not** Claude, **not** codex, **no** Chrome lease.
* **Driver**: `automath-sandbox/scripts/pp2a_batch_r36.sh` -> `pp2a_call.sh`
  (**new files**; the shared `engine_call_big.sh` / `engine_batch.sh` were NOT modified).
* **Slots**: 15 = 5 judges x 3 arms. `temperature = 1.0`, `max_tokens = 32000`,
  `reasoning.effort = medium`, cap 4 concurrent, 5 s stagger.
* **Order: INTERLEAVED** `A1,B1,D1,A2,B2,D2,…` — running one arm to completion first would
  confound ARM with TIME OF DISPATCH.
* **Outcome of the calls themselves**: **15 of 15 returned content; 0 burned; 0 retries**
  (`finish=stop` on all 15, completion tokens 4 370–8 624). Dispatched 10:41 CDT,
  last output 10:51 CDT.
* Briefs: `automath-sandbox/briefs/pp2a_r36/` (each of the 15 hash-verified identical to its
  arm before sending). Outputs: `automath-sandbox/out/ox-alpha/pp2a_r36/` (quarantine zone,
  per `automath-sandbox/README.md` rule 1).

## GATE A — the held-out key, graded first
Key `w133_r34_pp2a.key.txt`, **independently reproduced this round from the printed edge lists
with my own BFS / independence-number code** (system `python3` 3.9.6): W1 = 19, W2 = (5,1),
W3 = (2,2,2,2,2,2,3,3,4,4,4,4), W4 = (38,13), W5 = (2,3,2), W6 = (3,0). **All 6 rows match
r34's key exactly.**

**VOID (all six wrong or all declined): 0 of 15. GATE A discharged; all 15 judges scored.**

Per-row correctness, **as a LOWER BOUND** (the grader is a conservative pattern matcher over
each `W`-section; an unusually phrased correct answer would be counted wrong):

| row | correct |
|---|---|
| W1 H1 edge count | **15 of 15** |
| W2 H1 (max degree, vertex) | **15 of 15** |
| W3 H2 sorted a-vector | 12 of 15 |
| W4 H1 (sum a, n) | **15 of 15** |
| W5 H2 (radius, diameter, #centres) | **3 of 15** |
| W6 H3 (radius, #ecc = rad+1) | 8 of 15 |

*POPULATION: 15 judges x 6 rows = 90 answers; 68 scored correct. The pre-registered use of the
grid is the VOID gate only; the rest is descriptive.*

## THE TWO PRE-REGISTERED STATISTICS

`x` = fraction of an arm's judges reporting under (P1) that **no** step invokes a numbered
result outside its hypotheses. `y` = fraction reporting under (P2) that **every** PART 3 numeric
claim carries its `[C]` tag.

| arm | `x` (P1 reports clean) | `y` (P2 reports all tagged) | plant DETECTED per the scoring rule |
|---|---|---|---|
| **A** control | **5/5 = 1.00** | **5/5 = 1.00** | — |
| **B** false ABSENCE, link axis | **0/5 = 0.00** | 5/5 = 1.00 | **5 of 5** |
| **D** false PRESENCE, certification axis | 5/5 = 1.00 | **0/5 = 0.00** | **5 of 5** |

> ### `x_A − x_B` = **5/5 − 0/5 = 1.00**
> ### `y_A − y_D` = **5/5 − 0/5 = 1.00**

**Both statistics take the maximum value the instrument can express.** The pre-registered null
(`x_B = x_A` and `y_D = y_A`, both differences 0, "these absences carry ZERO BITS") is
**REFUTED on both axes**, and refuted by the largest margin n = 5 admits. The power bound
(resolves only differences `>= 1/5 = 0.20`) is not binding here: 1.00 >> 0.20.

Scoring detail, per the fixed rule (`w133_r34_prereg.md` §"Scoring rule"):
* **Arm B, DETECTED 5/5.** Every one of B_j1…B_j5 quotes the Proposition-P step
  *"By (B1) and Result T2 applied to `G'`…"* and states that Result T2's hypothesis
  `rad(G') >= 5` is not among Proposition P's assumptions and is not derived. None was scored on
  a general complaint about rigour; all five name the step and the missing hypothesis.
  (B_j2 mis-transcribes a *different* T2 hypothesis as `mu(G) >= 5`; it still names
  `rad(G') >= 5` as the uncovered one, so it is DETECTED.)
* **Arm D, DETECTED 5/5.** Every one of D_j1…D_j5 names the untagged claim — *"`H3` has radius
  `3`"* — as the sole PART 3 numeric claim without `[C]`. Three of the five add, unprompted,
  that the *value* is nonetheless correct, i.e. they separate a certification defect from a
  mathematical one.

## AN UNPRE-REGISTERED CONTROL THAT FELL OUT, AND IT IS THE STRONGEST ONE HERE
Each plant depressed **only its own** statistic:

| | `x` | `y` |
|---|---|---|
| A | 1.00 | 1.00 |
| B (link plant) | **0.00** | 1.00 |
| D (tag plant) | 1.00 | **0.00** |

The off-diagonal entries sit **exactly at the control value**. So the effect is not "a judge
handed a defective arm complains about everything": arm B's judges certify the tags clean 5/5,
and arm D's judges certify the link discipline clean 5/5. **This is discriminant validity, and
it was not designed in** — it is a consequence of the one-line-per-arm construction.

## A REAL DEFECT THE CHANNEL FOUND THAT NOBODY PLANTED — AND IT IS MINE (r34's), NOT THE DRAFT'S
`D_j1` and `D_j3` flag the arms' own paraphrase of Result T1:

> *"Then `y` is not adjacent to `u_{d-1}` and, for `i <= d-2`, `y u_i` is excluded by distance…"*

**They are right, and the justification is over-broad at exactly one index.** If `y ~ u_{d−2}`
then `w … u_{d−2} y u_d` has length `d`, which contradicts nothing — the distance argument works
only for `i <= d−3`. The index `i = d−2` is excluded instead by **C4-freeness**: `u_{d−2}` and
`u_d` would then have the two common neighbours `u_{d−1}` and `y`. `D_j1` supplies exactly that
repair; `D_j3` finds the gap but wrongly asserts C4-freeness does not close it.

**The theorem is unharmed and the DRAFT IS CLEAN**: `notes/proofs/wowii133_draft.md` §42.2
proves `(TAIL-1)` with the case split written out (`i <= d−3` by distance, `i = d−2` by C4).
**The defect is in r34's compression of that proof into the arm text**, and it sits in the
priming block that is **byte-identical across all three arms** — so it cannot bias the
difference statistics, only add noise.

**And the reading of the endorsements is the round's sharpest capability finding:**

*(Counted by reading all 15, not by pattern; the three categories partition the 15.)*

| | count | which |
|---|---|---|
| FLAGGED the justification as over-broad / false | **2 of 15** | `D_j1` (and repairs it correctly, via C4-freeness), `D_j3` (finds the gap, wrongly says C4-freeness does not close it) |
| ENDORSED T1's proof as sound | **12 of 15** | `A_j1..A_j5`, `B_j1..B_j5`, `D_j4`, `D_j5` |
| did not address T1's internal proof | **1 of 15** | `D_j2` |

**Of the 12 endorsers, 4 gave a stated reason that is itself invalid**: `A_j1` ("`y` is at
distance `d+1` from `w`" — it need not be), `A_j2` ("`dist(w,y) >= d−1 > i`" — compares a
distance to an index), `B_j3` ("`dist(w,u_d) <= i+2 <= d`, contradicting `= d`" — `≤ d` is not
a contradiction), `B_j4` ("`dist(w,y) <= i+1 <= d−1`, contradicting `dist(w,u_d) = d`" — same
non-contradiction). **Four judges reconstructed a proof of a step that does not follow, and
called it sound.**

> **10 of 10 on a planted hypothesis-LIST defect; 2 of 15 on an unplanted JUSTIFICATION defect.**
> The channel is strong at the **comparison** task (does this invocation's hypothesis list cover
> what the cited result demands?) and weak at the **derivation** task (is the stated reason
> actually a reason?). *POPULATION: the 15 judges of this dispatch. This axis was not
> pre-registered and carries no power statement; it is an observation, not a measurement.*

## WHAT THIS DOES NOT BUY — pre-registration §"What a result does NOT buy", in force
A `1.00` difference is evidence that **this channel reads for these two plant classes in a
~4.8 KB, 90-line extract**. It is **not** a family vote, it banks **no** mathematics, it does
**not** retroactively upgrade any earlier `(P1)` clean, and it says nothing about the same
channel's behaviour on a 146 KB paper.

## BURN
`H1`/`H2`/`H3` and the 6-row key are now **SPENT** — public to this channel. They may not be
reused as held-out material. A further arm needs fresh hosts and a fresh key.
