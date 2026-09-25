# CODEX TICKET — CNF encoder + kissat/DRAT harness for "(N) on the extremal branch"
# ENGINEERING + LOCAL CALIBRATION ONLY (q=2 instances are tiny). No cloud action.
# Repo: $HOME/workspace/claudecode/automath. Code in ENGLISH only.
# Context: the CP-SAT encoder (cloud_r45/item3/rowcap_cpsat.py) is SOUND on the SAT side
# but cannot prove UNSAT even for the smallest known theorem (q=2, all 7 rows perfect:
# UNKNOWN after 540 s). We need a proof-side instrument with certificates.

## Goal
`problems/etp677/cloud_r45/item3/nprop_cnf.py`: emit a DIMACS CNF for
  "a BRANCH OBJECT at order q exists with (a) every row in a prescribed set P perfect,
   and optionally (b) delta == 0"  (P = ALL rows is the (N) case; then (b) is implied),
plus `nprop_run.sh` that runs kissat with proof logging, verifies the proof with
drat-trim, decodes a SAT model back to {"table","lines","nu"} JSON and grades it with
`problems/etp677/R45_grade_object.py`. Tools: build **kissat** and **drat-trim** from
source into `tools/` (self-contained, like tools/ladr_build; no global installs; record
versions/commits). Python deps (e.g. python-sat for cardinality encodings) go into the
existing isolated env `engine/venv_item3/` or a new `engine/venv_cnf/`.

## Definitions (encode exactly these)
n = q^2+q+1; rows/columns/values = {0..n-1}. Fixed line set L0 = translates of a
difference set (q=2: {0,1,3} mod 7; q=3: {0,4,10,12} mod 13; q=4: {3,6,7,12,14} mod 21;
q=5: {1,5,11,24,25,27} mod 31). FREE bijection asg: columns -> L0 and FREE bijection nu.
Table T[a][c] with (B1) each row a permutation; (B2) T[a][c] = nu(c) iff a in L0[asg(c)];
off those cells the values are pairwise distinct within the column and != nu(c).
Left division: a\v = w iff T[a][w] = v.  Xi_t(x) = x\(t\x).
E(t,v) = #{x : Xi_t(x) = v};  N(t,v) = #{a : T[a][t] = v};  delta(v) = Sum_t E(t,v) - n.
Row t is PERFECT iff E(t,v) = N(t,v) for all v.
Suggested encoding (you may improve it, but keep it DIRECT and SMALL):
  x[a][c][v]  := [T[a][c] = v]   (one-hot per cell; exactly-one per row-value = B1)
  nu[c][v], asg[c][j] one-hot bijections; inc[a][c] := OR_j (asg[c][j] AND [a in L0[j]])
  x[a][c][v] AND nu[c][v]  <-> inc[a][c]   (block cells carry nu(c), non-block cells do not)
  off-block uniqueness: for each c,v: at most one a with x[a][c][v] AND NOT inc[a][c]
  Xi: z[t][x][v] := [Xi_t(x) = v] = OR_w ( x[t][w][x] AND x[x][v][w] )   (t\x = w and x\w = v)
  perfect row t: for each v: nu[t][v] -> exactly q+1 of {z[t][x][v]}_x;
                 abs[t][v] (v absent from column t) -> none;  else -> exactly one,
                 where abs[t][v] := NOT OR_a x[a][t][v].
  delta == 0 (only when requested): for each v, Sum_{t,x} z[t][x][v] = n.
Use a mature cardinality encoding (totalizer / sequential counter via python-sat's
CardEnc); no hand-rolled counters. Print variable/clause counts.

## MANDATORY CALIBRATION (pre-registered; run all; report the table verbatim)
 K1  q=2, P = all 7 rows            -> expected UNSAT, drat-trim VERIFIED, target < 60 s
     (theorem: (R9-H/q2-theorem), exhaustive; the CP-SAT encoder failed this)
 K2a q=2, P={0,1,3}, delta0         -> expected UNSAT + DRAT VERIFIED (theorem)
 K2b q=2, P={0,1,2}, delta0         -> expected UNSAT + DRAT VERIFIED (theorem)
 K3  q=2, P={0,1},  delta0          -> expected SAT; decoded object must be graded
     VERIFIED by R45_grade_object.py with |P| >= 2 and mass 0
 K4  q=3, P={4,6,10}, delta0, with the assignment fixed to
     problems/etp677/R45_L02_q3_3perf_delta0.json (add unit clauses for that table,
     lines, nu)  -> expected SAT immediately (the encoding must ACCEPT a known object;
     if it does not, the encoding is wrong)
 K5  q=3, P={0,4,10}, delta0, free  -> expected SAT (a known-feasible case); grade the model
 K6  q=3, P = all 13 rows           -> run with a 600 s LOCAL cap only; report
     UNSAT+DRAT / SAT (grade it!) / TIMEOUT honestly. Do NOT exceed the cap locally;
     the long run, if needed, is a separate owner-approved cloud item.
If K1, K2a, K2b are not UNSAT-with-verified-DRAT, the instrument is NOT usable; report
that plainly. If K3/K4/K5 are UNSAT the encoder is over-constrained; fix before reporting.

## Deliverables
1. `problems/etp677/cloud_r45/item3/nprop_cnf.py`, `nprop_run.sh`, `requirements.txt`.
2. `tools/kissat/` and `tools/drat-trim/` builds (source + binary; note commit/version).
3. `problems/etp677/cloud_r45/item3/calibration.out` — K1..K6 table with wall times,
   CNF sizes, and drat-trim outputs.
4. `engine/out/codex/etp677_nprop_cnf_report.md` — what was built, the table, any
   deviation, ending with the line DONE-NPROPCNF.
Minimum runtime: do not self-limit below the stated caps. No cloud actions.
