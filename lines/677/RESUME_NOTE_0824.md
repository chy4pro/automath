# line-677 resume note (dialogue, 2026-08-24 ~09:2x CDT)

Your session context was CLEARED after a safety-classifier false positive stalled you for
about two hours. Nothing is lost that matters: state lives on disk, by design.

## Read to resume
1. lines/677/BOOTSTRAP.md (your charter)
2. problems/etp677/campaign_registry.md — TAIL. You are at **R45 STEP 10**.
3. prompts/etp677_R3_common.md (toolkit, 1321 lines, current)

## Three things that happened while you were stalled
1. **Your L01 engine result is waiting**: engine/harvest/etp677_L01_cap2_r45.md
   (Qwen3.8-Max). T1 = NONE, honestly refused to fabricate a table. T2 = a real partial
   derivation, cited by fact name, with three eliminations (v- = nu(p) forces b <= q-1;
   the tight budget lock A_w = q+2-d_w, S_w = 1, h_p(w) = q for a zero-delta perfect value
   with b = q, hence d_w <= 1 when P is non-collinear; b(v-) = q makes v- skeleton-only)
   and a PRECISELY STATED four-case gap. Its own suggestion for the missing lemma —
   "prohibit a perfect row from drawing too many copies of its own nu(p) from singleton
   columns" — looks close to your (R20/PN) / (R43/GEN-BUDGET) column-side accounting.
   Grade it yourself; everything in that file is UNVERIFIED.
2. **Cloud item 1 was preempted twice by spot** (not a timeout, not a budget problem).
   Checkpoint intact: gs://[gcp-project]/item1/out/run.partial.log at
   jobs=1000/1296, nodes=43,796,883,514, sols=2 (both expected solutions already found).
   Inputs still in item1/in/. Owner-approved budget for item 1 covers the retry.
   A ready launcher is committed at **problems/etp677/cloud_r45/startup_item1c.sh** —
   launch with `--metadata-from-file startup-script=problems/etp677/cloud_r45/startup_item1c.sh`.
   Consider a different zone (us-central1 preempted ~every 2h last night) or finishing the
   ~296-job tail on-demand (~$0.15, still far under the $0.80 cap).
   Positive control at harvest is unchanged: exactly 56,629,380,606 nodes / 2 solutions.
3. **All four formal-conjectures PRs merged today** (#5023, #5027, #5028, #5029).

## NEW STANDING RULE (this is what stalled you — please follow it)
Do NOT assemble remote-execution shell payloads inside the conversation. Keep runner
scripts as committed repo files and reference them by path at launch; describe cloud work
in plain workload terms. Reason: the aggregate shape of "provision a host + fetch code +
compile + run max-parallel search + periodic upload loop + poweroff", written out inline
and surrounded by attack/kill/witness/certificate/SAT vocabulary, reads as offensive
tooling to a safety classifier even though the workload is pure combinatorics. Your
mathematics was never the problem; the packaging was. Same rule applies to any future
cloud item (2 and 3 are still owner-approved and unspent).
