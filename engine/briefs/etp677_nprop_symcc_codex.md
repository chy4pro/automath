# CODEX TICKET — symmetry breaking + cube-and-conquer instrument for the (N)@q=3 CNF
# ENGINEERING + LOCAL CALIBRATION ONLY. No cloud action. Code in ENGLISH only.
# Repo: $HOME/workspace/claudecode/automath
# Context: cloud_r45/item3/nprop_cnf.py emits `in/nprop_q3_all13.cnf` (84,799 vars /
# 242,723 clauses; "all 13 rows perfect" on the q=3 extremal branch, asg and nu free).
# Plain single-thread kissat ran 3.5 h on it with no verdict (and proof logging costs
# ~2.7 GB/h, so a long plain run can never be certified by drat-trim). The instance has
# a large symmetry group (PG(2,3) collineations act on rows/columns/values simultaneously,
# ~5616 elements, plus whatever the encoding adds) that plain CDCL does not exploit.
# We want a CERTIFIED, PARALLEL, RESUMABLE route: symmetry breaking + cube-and-conquer
# with a small DRAT proof per cube.

## Goal
Build and calibrate, self-contained under `tools/` (no global installs; record versions
/ commits), then deliver scripts under `problems/etp677/cloud_r45/item3/`:
1. **Symmetry breaking**: BreakID (Devriendt et al.; github.com/meelgroup/breakid or the
   original) run on the CNF to produce a symmetry-broken CNF. Report the number of
   generators found and the group order / orbit statistics BreakID prints. Write an
   INDEPENDENT checker `symcheck.py` that reads the generators (make BreakID print them)
   and verifies each is a syntactic symmetry: applying the literal permutation to the
   clause set returns the same clause set. Print "generators verified k/k".
2. **Cube generation**: march_cu (Heule; the CnC repository) on the symmetry-broken CNF,
   producing a cube file (`a ... 0` lines). Target 2,000–20,000 cubes; tune the cutoff
   (-d / -n options) and report cube count and depth distribution.
3. **Per-cube solving with certificates**: driver `cnc_run.sh CNF CUBES OUTDIR WORKERS`
   that for each cube i writes `OUTDIR/cube_i.{status,log,drat}`: appends the cube's
   literals as unit clauses (as an incremental CNF file), runs kissat with proof logging,
   runs drat-trim on the result, and records one of UNSAT-VERIFIED / UNSAT-UNVERIFIED /
   SAT (model kept, decoded with nprop_cnf.py's decoder and graded by
   R45_grade_object.py) / TIMEOUT. RESUMABLE: a cube with an existing terminal status
   file is skipped. Parallel via xargs -P or GNU parallel; each cube gets a per-cube
   time cap (argument).
4. **Cover certificate** `cnc_merge.py CNF CUBES OUTDIR`: (a) every cube has a terminal
   status; (b) all are UNSAT-VERIFIED (else report the exceptions); (c) COVER CHECK: write
   CNF' = CNF plus, for every cube c, the clause NOT(c) (the disjunction of the negated
   cube literals), run kissat with proof logging + drat-trim; UNSAT-VERIFIED means every
   model of CNF satisfies some cube, i.e. the cube set is a complete cover. Print a
   one-line verdict: "ALL CUBES UNSAT-VERIFIED (k/k) + COVER VERIFIED => CNF UNSAT".
   Also print the symmetry-breaking caveat line: "UNSAT proved for the symmetry-broken
   CNF; soundness of the reduction rests on symcheck.py (generators verified) and the
   lex-leader argument".
5. **Cloud runner (committed file, NOT executed)**: `cloud_r45/startup_item3cc.sh` for a
   16-vCPU Debian VM: install gcc/make, fetch inputs from
   `gs://[gcp-project]/item3cc/in/` (broken CNF, cube file, tool source
   tarballs, SHA256SUMS), build the tools, run `cnc_run.sh` with 15 workers and a
   per-cube cap given by a metadata value, sync `OUTDIR` status/log files to
   `item3cc/out/` every 10 minutes (resumable across VM restarts: on start, download
   existing out/ status files first), write DONE when all cubes are terminal, poweroff.
   Keep the script plain and commented as a batch job; abort with BUILD-FAILED if any
   binary is missing.

## MANDATORY CALIBRATION (pre-registered; run all; report the table verbatim)
 S1  q=2 all-7 (the (R9-H/q2-theorem) instance, plain kissat UNSAT 32 s): BreakID
     generators found and verified; symmetry-broken CNF + plain kissat -> UNSAT + DRAT
     VERIFIED; wall time vs the plain 32 s.
 S2  q=2 P={0,1} delta0 (K3, plain SAT 84 s): broken CNF must remain SAT (symmetry
     breaking must preserve satisfiability); decode + grade the model VERIFIED.
 S3  q=3 P={0,4,10} delta0 free (K5, plain SAT 71 s): broken CNF must remain SAT; grade.
 S4  q=2 P={0,1,2} delta0 (K2b, plain UNSAT 822 s): cube-and-conquer end to end on the
     broken CNF: cube count, per-cube max/median time, total CPU, wall time, cnc_merge
     verdict including COVER VERIFIED. This is the instrument's main proof-side test.
 S5  q=3 all-13 (the target): BreakID statistics; cube generation; then SAMPLE 20 cubes
     (evenly spaced) with a 300 s cap each, single process, report how many closed and
     the time distribution; extrapolate total CPU for all cubes honestly (a sample that
     mostly times out means the cutoff must be deeper — report that, do not hide it).
     LOCAL BUDGET for S5: at most 30 minutes wall in total. No cloud action.
 If S1 or S4 fails to produce UNSAT + verified certificates, the instrument is NOT
 usable; say so plainly. If S2/S3 become UNSAT after breaking, the breaking is unsound
 for this encoding — report and stop.

## Deliverables
1. `tools/breakid/`, `tools/march_cu/` (source + binaries, versions/commits recorded).
2. `problems/etp677/cloud_r45/item3/{symcheck.py,cnc_run.sh,cnc_merge.py}` +
   `cloud_r45/startup_item3cc.sh`; generated files `item3/in/nprop_q3_all13.sb.cnf`,
   `item3/in/nprop_q3_all13.cubes`, `item3/in/SHA256SUMS.item3cc`.
3. `problems/etp677/cloud_r45/item3/calibration_symcc.out` — S1..S5 table with wall
   times, counts, and the certificate verdict lines verbatim.
4. `engine/out/codex/etp677_nprop_symcc_report.md` — what was built, the table, any
   deviation, ending with the line DONE-NPROPSYMCC.
Minimum runtime: do not self-limit below the stated caps. No cloud actions.
