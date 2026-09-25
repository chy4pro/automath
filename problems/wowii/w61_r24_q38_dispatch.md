# Q38 DISPATCH RECORD — Corollary GFANν-HC, family 2, codex `gpt-5.6-sol`
owner-w61 round 24 · 2026-08-23 02:1x CDT · authority: `orchestration/planner_msgs/cert_w61_r23.md` RULING BC (one round)

Full narrative: `notes/proofs/wowii61_draft.md` §7.39. This file is the operational record.

## What was sent
| | |
|---|---|
| round | **Q38** |
| target | **Corollary GFANν-HC** (`ν ≥ 11`, `L ≥ 12`), §7.13 D — ONE statement, family 2 |
| judge | codex `gpt-5.6-sol high`, screen session `codex` |
| brief | `prompts/w61_S3_GFAN_r24.md` — `108 368` chars, md5 `45b79f35f9cd42dd29ddecb31dfacdde` |
| base | `prompts/w61_S3_GFAN_r20.md` — md5 `6fc6cc062028496e36661fbef66907d3`, `97 617` chars (`+10 751`) |
| builder | `problems/wowii/w61_r24_build_q38.py` — 27 anchored patches, 12 product asserts |
| gates | `problems/wowii/w61_r24_gate.py` → `.out` |
| key | `problems/wowii/w61_r17_heldout_key.txt` — **not pasted**, `ν = 11`, untouched since r17 |
| expected | `problems/wowii/w61_S3_GFAN_r24.md`, `_check.py`, `_check.out` |

## TUI discipline, in order
1. `hardcopy -h` before touching anything → session idle, Q34 closed with `Worked for 19m 18s`, model already `gpt-5.6-sol high`, cwd `~/workspace/claudecode/automath`.
2. `/new` — **required**, to keep sol's Q34 transcript out of the window. First attempt stuffed a literal `\n` (recorded, not hidden); cleared with `^U` and re-sent with `\r`. Full-screen hardcopy confirms a fresh session banner, `gpt-5.6-sol high`, empty composer.
3. One short line into the TUI pointing at the brief file and naming the three output paths. Task book is the brief; the TUI never carries the task.
4. Full-screen `hardcopy` → **`Working`**. Re-checked at `2m 06s`, still Working.
5. No approval box appeared; lease registered in `orchestration/RESOURCES.md`.

## Gates, all passed before the send
| gate | result |
|---|---|
| **brieflint** (`w61_r22_brieflint.py`, first use as a BUILD GATE; rules exec'd from the source file, not re-typed) | `0` findings on r24 · **`4` on the r20 base** — the gate can still fail |
| **RULING AX derivability** (per-row, not per-substring; `BODY` = brief minus Section 0) | clear. H2 asserted **deliberately** derivable — its closed form is printed on purpose |
| **B6 by role-of-object** (RULING AU) | disclosure `5/5`; every held-out row lives at `ν = 11` / partitions of `22`, which have no mathematical role in the target |

**Calibration failure, reported (RULING BA).** Gate 2 v1 ran unscoped and returned four LEAKs — all four its own Section 0 question text — plus a read of `(C-4)`'s "the count is a closed form, and every survivor is printed" as a survivor-count formula when it is a shape-count formula. Noisy-and-safe, not silent-and-favourable; recorded in the script.

## Pre-registered blind, before any report exists
* **Tiers** (RULING A): `H1/H2/H5` **HAND** — a stated wrong value **VOIDS**. `H3/H4` **COMPUTATIONAL** — `CANNOT COMPUTE` costs nothing; a wrong value is a **traced** downgrade; **both** wrong with the hatch unused **VOIDS**. Written into the frozen brief and disclosed to the judge.
* **The r20 structural withdrawal is UNTESTED and this round is its test.** Outcomes named now: (1) sol attacks the withdrawal's evidence → it worked; (2) sol GAPs on completeness alone → the rubric line does not bind; (3) sol neither attacks nor invokes it → **still untested**, recorded as such and not as a pass.

## sol's strength, stated honestly
Q33 — five import GAPs. Q34 — **read Theorem GFANν and found its import defect** (D1, the Corollary MB1 mismatch, UPHELD, repaired AC1), plus D2 and D3; machine-verified the `E ≥ 1` roster both directions. **It has never judged Corollary GFANν-HC**, and has never seen the r18/r20/r24 text. Per-statement bar ⟹ the family counts; a reader must also see that sol is **not naive** about the surrounding text.

## Riding the round
The four AD1/AE1 sentences (Corollary MB1; Corollary GFAN2-HC; Corollary GFANν-HC; Theorem RIG's scope) are landed verbatim and quoted back to the judge as **TARGET joint J-NEWTEXT** — true? needed? does it supply what it claims? Blindness cost of marking them is paid deliberately and stated in §7.39 (c).

## RULING AZ, first brief written with it known
Guards for all three of the target's imports are supplied **at the import site**, with the non-consumed hypothesis (`τ ≥ 4`) named too, under **TARGET joint J-AZGUARD**. The three obligations that **cannot** move on-site — the `Fan→GFan` configuration licence, the canonical meaning of "the hard core", roster completeness — get a named block telling the judge they exist and are carried elsewhere.

## Limits that ride wherever the 11-clear sweep verdict is cited
Numeric/non-emptiness guards only (`L ≥ n`, `ν ≥ n`, `τ ≥ n`, `B_lo ≠ ∅`). **Symbolic, configuration and tier guard classes remain unswept.** The §7.13 preamble licence was found **by hand**, not by the tool.

## Harvest
Next round. Void gate first, blind. Then J-NEWTEXT and J-AZGUARD before anything else, then the withdrawal outcome as 1/2/3.
