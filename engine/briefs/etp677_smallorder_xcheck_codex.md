# CODEX TICKET (engineering, sol OK) — cross-family check of the small-order E677 encoders
# and an independent classification of E677 magmas of order ≤ 9.
# Repo: $HOME/workspace/claudecode/automath. English. Write under
# problems/etp677/simple/xcheck/. Do NOT read problems/etp677/simple/simple_cnf.py or
# simple/noidem/noidem_cnf.py before writing your own encoder (independence); you may read
# them afterwards for the comparison step. Local compute: pure Python + kissat
# (tools/kissat/build/kissat) runs ≤ 300 s each, one at a time, total ≤ 60 min.

## Why
Two new DRAT-certified theorems ("no idempotent-free finite E677 magma of order 5 or 7") and
the earlier "no non-Latin E677 magma of order 5 or 7" / "no rho = nabla E677 magma of order
7" rest on ONE encoder (simple_cnf.py and its noidem copy). A DRAT proof certifies
"this CNF is UNSAT", not "this CNF says what we think". We need a second, independent
encoder and a third, solver-free method.

## Tasks
1. YOUR OWN encoder `x_cnf.py` for: E677 magma of order n (X[a][b][v] one-hot, rows
   permutations, E677 via your own aux scheme), with optional extra constraints
   `--noidem` (x*x ≠ x for all x), `--nonlatin` (some column has a repeated value),
   `--rhonabla` (every pair a ≠ b collides in some column). Include your own decoder and
   an independent checker.
2. Controls: order 5 plain → SAT, decode, check E677 + Latin; order 3, 4, 6 plain → UNSAT;
   order 5 with F_5 (2x−y) fixed by units + --noidem → UNSAT; order 31 with the F_31
   (5x−4y+1) table fixed + --noidem → SAT (propagation).
3. Verdict comparison with the existing CNFs (you may now read them): for n ∈ {5, 7}:
   plain, --noidem, --nonlatin; n = 7 --rhonabla — solve YOUR CNFs (300 s cap each) and
   report verdict + DRAT verification; compare with the existing calibration tables
   (simple/calibration.out, simple/noidem/calibration.out). Any disagreement is a finding.
4. SOLVER-FREE METHOD: a backtracking enumerator of all E677 magmas of order n ≤ 7
   (rows permutations, E677 propagation, canonical-form or plain labeled count). Report
   labeled counts for n = 1..7 and isomorphism classes with automorphism-group orders
   (expected from the eq677 db: one class at 5, two at 7; the round-3 (S) census reports
   labeled counts 1,0,0,0,6,0,1680 — confirm or refute), whether each class is Latin, has
   an idempotent, satisfies E255. Then n = 9 if it finishes within 20 minutes (report
   progress honestly otherwise).
5. From (4): state which of the small-order theorems are now established by THREE
   independent methods (two encoders + enumeration) and which by fewer.

## Deliverables
`problems/etp677/simple/xcheck/{x_cnf.py, x_check.py, enum677.py, results.out}` and
`engine/out/codex/etp677_smallorder_xcheck_report.md` ending with DONE-XCHECK.
