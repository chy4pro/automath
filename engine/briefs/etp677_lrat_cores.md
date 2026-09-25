# TICKET (codex4, engineering only; no cloud launch — line-677 launches; no deletion of anything)
# R46 publication: LRAT cores + independent checks for the nine archived big proofs (owner rule:
# publish trimmed, independently checkable cores + logs + hashes; raw DRATs are deleted by the
# owner line ONLY after every core is verified and uploaded).

## Inputs (all already in the bucket or the public package)
- Raw proofs: `ext12/out/jdef_m4.drat.gz`, `ext13/out/dlgdef_m4_def.drat.gz`,
  `ext15/out/c8def_m4.drat.gz`, `ext14/out/cube_{05,14,26,29,36}.drat.gz`,
  `ext16/out/core7nh_m4.drat.gz` — raw/gz sha256 + sizes are the 9 rows of
  `problems/etp677/pub/big_proof_hashes.txt` (authoritative; verify every download against it).
- CNF identity: the recorded CNF sha256 per proof in `problems/etp677/pub/github/sat/big/certificates.json`
  (+ `sat/a5/cover_table.json` for the cubes). The runner REGENERATES each CNF on the VM from the
  packaged encoders (`github/sat/encoders/`: core_joint.py / the independent dlgdef encoder /
  a5.py + a5_cubes.py + diag_cnf.py) using the exact generation commands documented in
  `github/REPRODUCE.md` / the certificates' generation fields, and MUST hash-compare before use
  (mismatch ⇒ status line `CNF-HASH-MISMATCH`, skip). Never download a CNF as a substitute.
- Tools: `drat-trim-src.tgz` (tested, `problems/etp677/ext/`), which also contains `lrat-check.c`;
  stage `cake_lpr` only as a pinned prebuilt release binary placed in the bucket `in/` by you with
  its sha256 in SHA256SUMS (no runtime downloads from arbitrary URLs). If no trustworthy prebuilt
  exists, lrat-check alone is the mandatory checker and say so.

## Runner `problems/etp677/ext/startup_lrat_cores.sh` (path-launched; model on startup_a5_proof.sh v2)
Metadata: `PROOFS` (comma list of the 9 names above, default all), `BKTSUB` (default ext20),
`DTCAP` (drat-trim seconds per proof, default 43200), `WORKERS` (default 1 — memory!),
`LOCAL_TEST=1` mode as before. Phase markers to `phase.txt` at every stage; rolling status.txt and
job.log every 600 s.
Per proof, sequentially:
1. download `.drat.gz`, check gz sha256 + bytes against big_proof_hashes.txt (staged as input),
   gunzip, check raw sha256 + bytes;
2. regenerate the CNF, hash-compare (mandatory);
3. `drat-trim <cnf> <drat> -l <name>.core.lrat -o <name>.core.drat -t $DTCAP` → keep the log;
   require `s VERIFIED`;
4. `lrat-check <cnf> <name>.core.lrat` (build from the tarball) → require its success line; if
   cake_lpr was staged, run it too and keep its log;
5. record: sizes and sha256 of raw DRAT, core.lrat, core.drat, core.lrat.gz; wall times of steps
   3–4; the exact commands; gzip the LRAT (and the trimmed DRAT), upload
   `<name>.core.lrat.gz`, `<name>.core.drat.gz`, `<name>.dt.log`, `<name>.lratcheck.log`
   (+ `<name>.cakelpr.log`), and one status line
   `<name>: CORE-OK raw_bytes=… lrat_bytes=… lrat_sha256=… lrat_gz_sha256=… lrat_gz_bytes=… drat_core_bytes=… checker=lrat-check[,cake_lpr]`;
6. delete the local raw DRAT and CNF (disk), never anything in the bucket.
Disk: 300 GB pd-balanced; the largest raw DRAT is 5.7 GB and LRAT files can exceed the DRAT
(hints) — report the observed ratio per proof. Memory: one proof at a time on e2-highmem-8 (64 GB)
unless the local test proves less suffices.

## Deliverables
- The runner + `startup_lrat_cores_local_test.sh` (tiny UNSAT formula: drat-trim -l, lrat-check
  pass, ordered phase assertion, one kissat at most, `timeout 60`).
- A second mode/metadata `PROOFS=a5:<ids>` that does the same for the 39 A5 cubes being produced
  in `ext19/out` (input = `cube_XX.drat.gz` + the runner-emitted status line hashes) — same
  pipeline, so the A5 rows also ship cores.
- Launch card (e2-highmem-8, bucket sub ext20; a separate ext21 card for the A5 batch).
- Report `engine/out/codex/etp677_lrat_cores_report.md` ending `DONE-LRATCORES`: no claims, no
  deletions, frozen trees untouched. Sizes/hash tables are filled ONLY from real runs (PENDING
  otherwise).

# ADDENDUM (owner line STEP 80, 12:3x) — ROOT CAUSE of the silent A5 VMs: instances created without --scopes=storage-rw get the default
# read-only storage scope; every gsutil upload fails "403 Provided scope(s) are not authorized" while downloads work. MANDATORY for this runner:
#  (1) every launch card carries --scopes=storage-rw (and says so in a comment);
#  (2) the runner starts with an UPLOAD-PROBE phase: write a tiny object to <prefix>/out/probe.txt and read it back; on failure write a
#      BUILD-FAILED marker to local disk, echo it to the serial console, and poweroff — never continue silently;
#  (3) LOCAL_TEST must exercise the probe path (simulated failure → marker + exit).

# INTERPRETATION NOTE (owner line STEP 82, 12:5x): "no runtime downloads of unpinned binaries" does NOT forbid distro packages —
# `apt-get install gcc make gzip coreutils python3` from the image's own repositories is REQUIRED before the tool check (the stock
# image ships no compiler; v1 died at BUILD-FAILED "missing preinstalled tool gcc"). Keep the apt line in every runner; the rule
# targets unpinned third-party binaries fetched over the network (those must be staged with sha256).
