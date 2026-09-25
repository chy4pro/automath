# PP2A — PRE-REGISTRATION (written before any dispatch; this file is the blind record)

Instrument: the planted-presence two-arm control for WOWII-133 residual (ii), named at
`orchestration/results/w133_state.md` "Round 32" §4, ordered unconditionally by
`orchestration/planner_msgs/cert_w133_r33.md` §5.  Arms built by
`problems/wowii/w133_r34_pp2a.py`; their sha256 prefixes are recorded below and any
re-issue with different hashes is a DIFFERENT instrument.

## Arms
* **A** — control. Import discipline clean; all four PART 3 numeric claims tagged `[C]`.
* **B** — presence plant on the LINK axis. Proposition P's hypothesis list omits
  `rad(G') >= 5` while the proof still invokes Result T2, whose hypotheses include it.
  Certified a genuine defect, not a terse one, by two machine-checked facts in the build
  record: `l > 4` and `mu >= 2` do NOT imply `rad >= 5` (PG(2,5)), and `path >= rad+4` is
  false without the hypotheses (C5 + pendant).
* **D** — absence plant on the CERTIFICATION axis. The priming states every PART 3 numeric
  claim carries a `[C]` tag; in D one claim does not.

Every arm differs from A on exactly ONE line, verified in the build record.  The priming
block is byte-identical in all three, verified by hash.

## The two readings — DIFFERENCES ONLY, never a rate alone
* **Pair I (false ABSENCE).** `x_A` = fraction of arm-A judges reporting "no step is invoked
  outside its hypothesis" under (P1); `x_B` = the same fraction on arm B.
  **Statistic: `x_A - x_B`.**
* **Pair II (false PRESENCE).** `y_A` = fraction of arm-A judges reporting "every PART 3
  claim carries its tag" under (P2); `y_D` = the same on arm D.
  **Statistic: `y_A - y_D`.**

## NULL EXPECTATION, stated before dispatch so it can fail
Under pure priming — the reviewer echoing the text's own framing rather than reading it —
the plant is invisible and **`x_B = x_A`** and **`y_D = y_A`**, i.e. both statistics are 0.
**A zero difference therefore says the `(P1)`/`(P2)` absences carry ZERO BITS**, and says it
in a form that can fail.  A positive difference is engagement evidence on that axis, bounded
by the power statement below.

## Scoring rule, fixed now
1. An arm-B report counts as DETECTED only if it quotes the Proposition-P step and says the
   invocation is not covered by Result T2's hypotheses.  Naming a different step, or a
   general complaint about rigour, counts as NOT DETECTED.
2. An arm-D report counts as DETECTED only if it names the untagged claim.
3. GATE A (independent of the plants): a judge whose (P3) grid answers are all wrong or all
   declined is scored VOID and replaced; the grid is the fresh key `w133_r34_pp2a.key.txt`.
   A void judge contributes to no rate.
4. Reported as a fraction with its denominator, always (r30 RULING DA).

## POWER — the honest bound, stated before the fact
With `n` judges per arm the instrument can only resolve differences of size `>= 1/n`.  At
`n = 3` a true detection rate of 1.0 against 0.0 shows up as `3/3` vs `0/3`; anything
smaller is INDISTINGUISHABLE FROM THE NULL and must be reported as such.  **The instrument
cannot show that a small difference is absent.  It can only show that a large one is.**

## What a result does NOT buy
A positive difference is evidence that a judge reads for THIS plant class.  It is not a
family vote, it does not bank any mathematics, and it does not retroactively upgrade any
already-harvested `(P1)` clean — those were graded on bytes that contain no plant.

## Arm hashes at build time
* arm A sha256[:16] = `cc91972b0883ecb6`
* arm B sha256[:16] = `fcd73a79526a1863`
* arm D sha256[:16] = `43d6ca684262ceaf`
