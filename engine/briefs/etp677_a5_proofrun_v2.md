# TICKET (codex, engineering only) — follow-up to etp677_a5_proofrun.md: phase visibility for
# problems/etp677/ext/startup_a5_proof.sh. Seat ONLY if line-677 says the first run stalled.

## Symptom
ext-a5p (e2-highmem-4, WORKERS=3) showed nothing in ext18/out for > 70 minutes: the runner
uploads its first status_snapshot only after apt + both builds + base-CNF generation + hash check,
so the operator cannot distinguish "generating a 41.6M-clause DIMACS in Python" from "stuck".

## Changes (minimal; keep everything else byte-identical in behaviour)
1. `phase()` helper: writes `$(date -u) PHASE=<name>` to `$OUTDIR/phase.txt` and uploads it to
   `$BKT/out/phase.txt` (cp in LOCAL_TEST). Call it at: INPUTS-OK, KISSAT-BUILT, DRATTRIM-BUILT,
   METADATA-VALID, BASE-GEN-START, BASE-GEN-DONE (with byte size + seconds), BASE-HASH-OK,
   SOLVING (with WORKERS), FINISHED.
2. Start the 600-s status_snapshot loop BEFORE the base generation (right after the builds), so
   `status.txt` (all PENDING) appears within ~10 minutes of boot.
3. Run the encoder with `python3 -u` and tee its stderr into job.log; time it (`/usr/bin/time -v`
   if present) so the report can record generation wall time and peak RSS.
4. Upload job.log every snapshot as well (rolling `job.log`), not only at the end.
5. Add `--metadata BASE_GEN_TIMEOUT` (default 7200 s) around the base generation via `timeout`;
   on expiry → `BUILD-FAILED: base generation timeout` path (status + DONE + poweroff).

## Test
Re-run the existing LOCAL_TEST harness; add an assertion that phase.txt contains the expected
sequence (in LOCAL_TEST mode BASE-* phases are skipped — assert the SOLVING/FINISHED entries).
Also run the packaged encoder ONCE locally under `timeout 900` with output to /dev/null-like
counting (do NOT write a 1 GB file on the box; pipe to `wc -c`) to measure how long base
generation actually takes on the local machine — one process, report the seconds. If it exceeds
900 s locally, say so; that number decides whether the cloud pre-phase was merely slow.

## Report
`engine/out/codex/etp677_a5_proofrun_v2_report.md` ending with `DONE-A5PROOFRUN-V2`, with a
launch card identical to v1 except the added metadata key. No cloud launch; frozen trees untouched.
