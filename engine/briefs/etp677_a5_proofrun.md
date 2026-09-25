# TICKET (codex, engineering only — no mathematics, no claims) — R46 / publication track B3(2):
# proof-keeping re-run of the 39 A5 cubes whose DRAT proofs were not retained.

## Why
Audit2 B3: 39 of the 44 A5 orbit cubes (00-04, 06-13, 15-25, 27-28, 30-35, 37-43) carry proof
hashes but no proof object. Bucket ext14/out holds only the five residual cubes (05, 14, 26, 29,
36). Their CNFs are not in the bucket either (ext14/in has only the residual five + tarballs).
The publication patch isolates the 39 as "verified during the run, proof not retained"; this
ticket produces the missing certificates so the rows can be upgraded to Zenodo locators.

## Deliverable 1 — runner `problems/etp677/ext/startup_a5_proof.sh` (committed file; launched by path)
Model it on `problems/etp677/ext/startup_ext_proof.sh` (same metadata contract, same
kissat/drat-trim source builds from `kissat-src.tgz` / `drat-trim-src.tgz`, same gzip+upload+
hash+poweroff discipline). Differences:
1. Inputs (bucket `$BKTSUB/in/`): `a5_cubes.py`, `diag_cnf.py` (copied from
   `problems/etp677/pub/github/sat/encoders/`), `cover_table.json` and `orbits.json`
   (from `problems/etp677/pub/github/sat/a5/`), `CUBES` metadata = comma-separated cube ids.
2. GENERATE on the VM: for each cube id, regenerate the DIMACS with the packaged encoder using
   the generation parameters recorded in `cover_table.json` (derive the exact invocation from
   the encoder's `--help`/source; do not modify the encoder). Compute sha256 of the generated
   CNF and COMPARE with the CNF hash stored in `cover_table.json` for that cube. Mismatch ⇒ write
   `cube_XX: CNF-HASH-MISMATCH expected=… got=…` to status and SKIP the cube (never solve a
   formula whose identity is not confirmed).
3. SOLVE with kissat + DRAT (`--time=$CAP`), then drat-trim ON THE VM (`$DTCAP`); upload
   `cube_XX.drat.gz`, `cube_XX.dt.log`, `cube_XX.log` (kissat stdout tail + verdict line), and
   append one line per cube to `status.txt` in the form used by ext14/out/final.txt:
   `cube_XX: s UNSATISFIABLE drat-trim=s VERIFIED proof_bytes=N cnf_sha256=… proof_sha256=… gz_sha256=… gz_bytes=…`.
   PROOFMAX default 4 GiB. Delete the local .cnf and .drat after upload (disk).
4. WORKERS default = vCPU count − 1 (metadata override). Keep `LOCAL_TEST=1` mode working.
5. Robustness: `set -x`, log to /var/log/job.log, per-cube failures never abort the batch,
   `DONE` marker + `final.txt` at the end, then poweroff.

## Deliverable 2 — local dry test (no solving beyond seconds)
Run the runner with `LOCAL_TEST=1` on ONE tiny formula (any small UNSAT CNF) to prove the
generate→hash-compare→solve→drat-trim→status pipeline end to end; include the transcript in the
report. Do NOT generate the real A5 cubes locally (each is ~1 GB; the box is loaded): the
hash-compare path is tested by a deliberately mismatching expected hash on the tiny formula.

## Deliverable 3 — launch card (for line-677 to execute; do not launch yourself)
Exact `gcloud compute instances create` command with `--metadata-from-file startup-script=
<repo path>`, `--metadata CUBES=…,BKTSUB=ext18,CAP=…,DTCAP=…`, machine type e2-highcpu-8
(or -4), 200 GB pd-balanced boot disk, plus the `gsutil cp` lines that stage the inputs into
`gs://<bucket>/ext18/in/`. Estimated wall time from the ext14 logs if available.

## Report
`engine/out/codex/etp677_a5_proofrun_report.md` ending with `DONE-A5PROOFRUN`. No claims about
mathematics; do not touch `problems/etp677/pub/` (frozen).
