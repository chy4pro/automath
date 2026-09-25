# CODEX TICKET — item 3 instrument: CP-SAT encoder for "K perfect rows + delta == 0"
# on the projective plane of order q (q = 2 controls, q = 3 probe). ENGINEERING + LOCAL
# CONTROLS ONLY. The heavy q=3 runs go to the cloud later via a committed runner script.
# Repo: $HOME/workspace/claudecode/automath. Write code in ENGLISH only.

## Goal
A single Python 3 script `problems/etp677/cloud_r45/item3/rowcap_cpsat.py` (OR-tools CP-SAT,
installed in an isolated venv `engine/venv_item3/` — never system/global pip) that decides:

  "does a BRANCH OBJECT at order q exist whose perfect-row set CONTAINS a prescribed set P
   and whose delta vector is identically zero?"

and, on SAT, dumps the object as JSON {"table","lines","nu"} that the EXISTING verifier
`problems/etp677/R45_verify_any.py` accepts (you must run it on every SAT model).

## Definitions (exact; encode these, nothing else)
n = q^2+q+1. Points/rows/columns/values are all {0..n-1}. A branch object is an n x n
integer array T (entry a*t = T[a][t]) with:
 (B1) every row is a permutation;
 (B2) for every column c there is a value nu(c) attained exactly q+1 times, on the set
      ell_c; every other value at most once (so exactly q values are absent);
 (B3) the sets ell_c form a projective plane of order q on the points;
 (B4) nu is a bijection (may be imposed; it is a theorem).
WLOG (all planes of order 2 and 3 are unique): FIX the line set L0 = translates of a
difference set — q=2: {0,1,3} in Z_7; q=3: {0,4,10,12} in Z_13 — and let the column->line
assignment asg: columns -> L0 be a FREE bijection variable, and nu a FREE bijection variable.
So: T[a][c] == nu[c]  iff  a in L0[asg(c)]; off those cells T[a][c] != nu[c] and the
off-block values in a column are pairwise distinct.
Left division: lam[a] = inverse permutation of row a (lam[a][T[a][w]] = w; use AddInverse).
Xi[t][x] = lam[x][ lam[t][x] ]   (nested element constraint; index lam[t][x] is a variable).
E[t][v] = #{x : Xi[t][x] == v};   N[t][v] = #{a : T[a][t] == v}   (both via booleans + sums).
delta[v] = sum_t E[t][v] - n.    Row r is PERFECT iff E[r][v] == N[r][v] for all v.
Constraints of a run: for every r in P: row r perfect; if --delta0: delta[v] == 0 for all v.
P is given as row indices; because asg and nu are free and Aut(L0) is transitive on each
configuration type, P can be fixed to ONE representative per type:
  q=2, |P|=2: {0,1}.  q=2, |P|=3: line {0,1,3} and triangle {0,1,2}.
  q=3, |P|=3: collinear {0,4,10} and triangle {0,1,2}.
  q=3, |P|=4: line {0,4,10,12}, near-pencil {0,4,10,1} (3 on a line + 1 off),
              quadrangle {0,1,2,5} (check: no 3 collinear in L0; if not, pick one that is).
Include a `--fix-json FILE` option that additionally pins T to a given object's table (for
the "must be feasible" control) and a `--hint-json FILE` option that only hints it.

## CLI and output
`rowcap_cpsat.py --q 3 --P 0,1,2,5 --delta0 --timeout 600 --workers 8 --out res.json`
Result JSON: {"q","P","delta0","status": "SAT"|"UNSAT"|"UNKNOWN", "wall_s", "object": {...}
or null, "verifier": <verbatim R45_verify_any.py verdict line> or null}. Every run has an
INTERNAL hard timeout (CP-SAT max_time_in_seconds AND an outer wall guard); never wait
unbounded. Log progress lines to stdout with flush.

## MANDATORY LOCAL CONTROLS (run all; report the table below verbatim; q=2 runs are
## seconds; cap every q=3 run at 300 s and report UNKNOWN honestly if it hits the cap)
 C1  q=2 P={0,1}     --delta0      expected SAT   (witness exists; verifier must say OK, |P|>=2, mass 0)
 C2a q=2 P={0,1,3}   --delta0      expected UNSAT (theorem, exhaustive: no 3 perfect rows with delta==0 at q=2)
 C2b q=2 P={0,1,2}   --delta0      expected UNSAT (same theorem)
 C3  q=2 P={0,1,2}   (no --delta0) expected SAT   (3-perfect tables exist; verifier |P|>=3)
 C4  q=3 P={0,1,2}   --delta0 --fix-json problems/etp677/R45_L02_q3_3perf_delta0.json
                                   expected SAT immediately (that object IS a solution up to relabeling —
                                   NOTE: its perfect rows are {4,6,10}, a triangle, with lines = the same L0 and
                                   nu = id; so use --P 4,6,10 for this control, not 0,1,2)
 C5  q=3 P={4,6,10}  --delta0 --hint-json (same file), no fix   expected SAT (may need the hint)
 C6  q=3 P={0,4,10}  --delta0      collinear triple, 300 s cap: report SAT/UNSAT/UNKNOWN (unknown territory)
If C1, C3, C4 or C5 come back UNSAT the ENCODER IS WRONG — fix it before reporting.
If C2a/C2b come back SAT the encoder is under-constrained — the verifier will reject the
model; fix it. Do not tune away a control; report what happened.

## Deliverables
1. `problems/etp677/cloud_r45/item3/rowcap_cpsat.py` (+ `requirements.txt`: ortools pinned).
2. `problems/etp677/cloud_r45/item3/controls.out` — the C1..C6 table with wall times.
3. `engine/out/codex/etp677_item3_cpsat_report.md` — what was built, the control table,
   encoding size (vars/constraints), any deviations, ending with the line DONE-ITEM3ENC.
Minimum runtime: do NOT self-limit below the caps stated above (earlier tickets stopped at
60 s of a 15-min budget; that is a defect). No cloud actions from this ticket.
