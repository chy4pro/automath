# PP2A — DISPATCH ADDENDUM (round 36). WRITTEN BEFORE ANY ARM WAS SENT.

This file completes parameters that `problems/wowii/w133_r34_prereg.md` left unspecified.
It is written **before the first API call** and **before any arm output exists on disk**.
It does not change any statistic, any null, or any scoring rule already pre-registered.

## 0. Instrument identity — VERIFIED, not assumed
`shasum -a 256 | cut 16` on the three arm files, this round, on disk:

| arm | hash now | hash in `w133_r34_prereg.md` | match |
|---|---|---|---|
| A | `cc91972b0883ecb6` | `cc91972b0883ecb6` | YES |
| B | `fcd73a79526a1863` | `fcd73a79526a1863` | YES |
| D | `43d6ca684262ceaf` | `43d6ca684262ceaf` | YES |

`diff A B` = exactly one changed line (line 59, Proposition P's hypothesis list loses
`rad(G') >= 5`). `diff A D` = exactly one changed line (line 73, `H3` radius claim loses `[C]`).
**This is the same instrument r34 built. A re-issue with different hashes would be a different
instrument and this file would not apply to it.**

*Correction to the r34 narration, found here:* r34 and `cert_w133_r35` both say "exactly 1
differing line **of 91**". `wc -l` on all three arms is **90** (files end in a newline, so 90 is
the true line count). The "exactly one differing line" claim is confirmed by `diff`; only the
total is off by one. Nothing depends on the total.

## 1. WHICH CHANNEL, and why this one
**Target: the free engine channel — OpenRouter `stealth/ox-alpha`**, the endpoint the project's
`ENGINE_BACKLOG.md` dispatches first-pass review to (`automath-sandbox/scripts/engine_batch.sh`).
Per `cert_w133_r35` §6 and `tasks/w133_r36.md` §1: PROTOCOL v4 §3 made engine first-pass review
load-bearing, so **the judge being measured must be the judge that is actually doing the
filtering.** Not Claude, not codex, not a scarce seat.

`automath-sandbox/README.md` §4 notes ox-alpha does not count toward **cross-family** gates while
its lab identity is unknown. **That is irrelevant here and is not being evaded:** PP2A is not a
family vote and banks no mathematics. It measures one channel's detection rate on one defect
class. The channel it measures is the channel v4 §3 relies on.

## 2. n = 5 PER ARM (15 slots), as approved
`cert_w133_r35` §6. n = 3 resolves only blind spots larger than 1/3, which are visible without an
instrument.

## 3. THE ONE PARAMETER r34 LEFT UNSPECIFIED — SAMPLING TEMPERATURE
The shared dispatcher `engine_call_big.sh` hard-codes `temperature: 0`. **Five calls at
temperature 0 with a byte-identical brief are not five judges; they are one judge replicated,
and the pre-registered power bound `>= 1/n` would be a fiction** — the realised n would be 1
regardless of how many slots were spent.

**Therefore this dispatch uses `temperature: 1.0`, five independent draws per arm.** This is a
completion of an unspecified parameter, not a change to a registered one, and it is recorded
here before any output exists.

**Declared deviation, stated against my own interest:** production first-pass review on this
channel runs at temperature 0. **A rate measured at temperature 1.0 is therefore an estimate of
the channel's detection rate under sampling, not a measurement of the exact production
configuration.** The alternative — five identical draws — measures the production configuration
exactly and has n = 1 of power. I take the estimate with real n over the exact measurement with
no power, and I flag the gap rather than hide it.

## 4. THE NULL, restated BEFORE the outcome (task book §1, cert §6)
> Under pure priming — the reviewer echoing the text's own framing rather than reading it —
> the plant is invisible, so **`x_B = x_A`** and **`y_D = y_A`**: both statistics are **0**.
> A zero difference says the `(P1)`/`(P2)` absences carry **ZERO BITS** on this channel.

## 5. THE POWER BOUND, restated BEFORE the outcome
> With n = 5 judges per arm the instrument resolves only differences **>= 1/5 = 0.20**.
> A difference below 0.20 is **INDISTINGUISHABLE FROM THE NULL** and must be reported as such.
> **The instrument can show a large difference is present. It can never show a small one is
> absent.** With n = 5 the finest non-zero difference expressible is 1/5, and no confidence
> statement beyond "present / indistinguishable" is claimed.

## 6. Scoring — unchanged from `w133_r34_prereg.md` §"Scoring rule, fixed now"
1. Arm B counts DETECTED only if the report quotes the Proposition-P step and says the
   invocation is not covered by Result T2's hypotheses. A different step, or a general
   complaint about rigour, is NOT DETECTED.
2. Arm D counts DETECTED only if the report names the untagged claim (the `H3` radius claim).
3. GATE A: a judge whose (P3) grid answers are all wrong or all declined is VOID and replaced;
   graded against the held-out key `w133_r34_pp2a.key.txt`. A VOID judge contributes to no rate.
4. Every fraction ships with its denominator.

**`x_A`** = fraction of arm-A judges reporting "no step is invoked outside its hypotheses" under
(P1). **`x_B`** = same on arm B — note the direction: on arm B, a judge that *finds* the plant
does **not** report clean, so `x_A - x_B` is the pre-registered statistic and is expected
POSITIVE if the channel reads.
**`y_A`** = fraction of arm-A judges reporting every PART 3 claim carries its tag. **`y_D`** =
same on arm D. Statistic `y_A - y_D`.

## 7. What a result does NOT buy — carried forward verbatim in force
A positive difference is evidence that this channel reads for THIS plant class in a ~5 KB
extract. It is **not** a family vote, it banks **no** mathematics, and it does **not**
retroactively upgrade any already-harvested `(P1)` clean.

## 8. Burn accounting, acknowledged before the fact
Dispatch spends hosts `H1`/`H2`/`H3` and the 6-row key permanently. After this round they are
public to the channel and may not be reused as held-out material.
