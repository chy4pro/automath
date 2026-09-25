# CODEX TICKET (engineering; any tier incl. luna) — cloud runner variant that keeps kissat's
# DRAT proof and verifies it on the VM, so long UNSAT verdicts are bankable without local
# reproduction. Repo: $HOME/workspace/claudecode/automath. Read
# problems/etp677/ext/startup_ext.sh (metadata WORKERS/CAP/BKTSUB; inputs from
# gs://[gcp-project]/$BKTSUB/in/ incl. kissat-src.tgz; per-cell logs uploaded;
# status every 600 s; DONE marker; poweroff) and problems/etp677/ext/watch_ext.sh (the Monitor
# that parses VERDICT lines). Do NOT launch anything. DONE marker: DONE-STARTUPPROOF.

## Tasks
1. `problems/etp677/ext/startup_ext_proof.sh`: same conventions as startup_ext.sh plus:
   - build drat-trim from a tarball in the bucket subdir (drat-trim-src.tgz; add it to the
     inputs contract, and put a copy of tools/drat-trim sources as
     problems/etp677/ext/drat-trim-src.tgz if none exists in the bucket) — or vendor the
     single-file drat-trim.c;
   - run each cell as `kissat --time=$CAP in/X.cnf out/X.drat` (binary DRAT is fine for
     drat-trim; use `--no-binary` only if drat-trim needs it), then on UNSAT run
     `drat-trim in/X.cnf out/X.drat` with a time cap (metadata DTCAP, default 24 h), append the
     verdict line `X: s UNSATISFIABLE drat-trim=s VERIFIED proof_bytes=N` (or NOT VERIFIED /
     DT-TIMEOUT) to out/X.log, upload out/X.log and, if the proof is < 2 GB (metadata
     PROOFMAX), out/X.drat.gz; delete the local proof afterwards to protect the disk;
   - on SAT upload the log (contains the `v` lines) as before;
   - keep the status/DONE/poweroff behaviour; keep `ls -S -r` ordering; WORKERS parallel;
   - the watch script must still match: extend watch_ext.sh minimally (a VERDICT line already
     prints the whole `s …` line; make sure the added `drat-trim=…` text is included in the
     event line) — keep it backward compatible.
2. Local dry run (no cloud): simulate the runner with a fake metadata server or a
   `LOCAL_TEST=1` mode that reads inputs from a local dir and writes outputs locally, on two
   tiny cells (problems/etp677/simple/fibre_core/out/core7_m2.cnf and core7_m3.cnf: both
   UNSAT, seconds) and one SAT cell (out/core7_m4.cnf); show the log lines produced and that
   drat-trim verified the UNSAT proofs. Also test the disk guard (a fake 3 GB proof must be
   skipped for upload but still verified).
3. Document the metadata contract at the top of the script and in
   problems/etp677/ext/README_runners.md (startup_ext.sh vs startup_ext_proof.sh; when to use
   which; cost note: drat-trim time can exceed the solve time).

## Deliverables
startup_ext_proof.sh, watch_ext.sh (compatible), README_runners.md, the dry-run log, and
engine/out/codex/etp677_startup_proof_report.md ending with DONE-STARTUPPROOF.
