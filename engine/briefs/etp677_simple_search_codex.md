# CODEX TICKET — exact instruments for the SIMPLE case of ETP 677→255 (R46, two questions)
# ENGINEERING + LOCAL CALIBRATION ONLY (caps below). No cloud action. Code in ENGLISH only.
# Repo: $HOME/workspace/claudecode/automath. Put code under problems/etp677/simple/.
# Tools available: tools/kissat/build/kissat (4.0.4), tools/drat-trim/drat-trim, python-sat
# in engine/venv_item3 (CardEnc). BreakID may be under tools/breakid if another ticket built it.

## Background (one paragraph; do not restate mathematics beyond this)
A finite magma (M,*) satisfies E677: x = y*(x*((y*x)*y)); then every L_y: z -> y*z is a
permutation. E255: x = ((x*x)*x)*x, equivalently "column x contains x" (some a with a*x = x).
The campaign's proof skeleton needs (Prop_exists): some pair a != b NEVER collides in a column
(a*t != b*t for all t). Its negation, rho = nabla ("every pair a != b collides in some
column t: a*t = b*t"), has never been decided at any order. All known finite 677-magmas of
order <= 13 are Latin squares (every column a permutation), where rho = Delta trivially.

## Q1 — smallest NON-LATIN finite 677-magma
CNF(n): a 677-magma of order n with at least one column collision (exists t, a != b with
a*t = b*t). Encoding: X[a][b][v] = [a*b = v] one-hot; rows permutations; E677 via aux
one-hots for the inner terms (y*x = z; z*y = w; x*w = u; y*u must be x) with implication
clauses; collision via selector variables. Symmetry: relabellings of M act; break with
BreakID if available, else fix the L_0 cycle type WLOG? (NOT WLOG in general — do not claim
it; if you fix anything, prove it is WLOG or run without.)
## Q2 — rho = nabla at order n
CNF'(n): a 677-magma of order n in which EVERY pair a != b collides in some column. Encoding:
e[a][b][t] -> (X[a][t][v] -> X[b][t][v]) for all v, and OR_t e[a][b][t] for every pair.

## MANDATORY CALIBRATION (pre-registered; report the table verbatim)
 C1  order 3, 4, 6 (no 677-magma exists): plain E677 CNF -> UNSAT + DRAT verified, each < 60 s.
 C2  order 5 and 7: plain E677 CNF -> SAT; decode; verify E677 on the table with an
     INDEPENDENT checker (your own, brute force); check the table is Latin.
 C3  order 5, 7, 9: Q1 CNF (non-Latin) -> expected UNSAT (all known models Latin); report
     UNSAT + DRAT or TIMEOUT honestly; local cap 300 s each.
 C4  order 11, 13: Q1 CNF -> run with a 600 s cap each; report verdict/TIMEOUT.
 C5  order 7: Q2 CNF -> expected UNSAT (Latin ⟹ rho = Delta); cap 300 s.
 C6  order 13, 16, 19, 21, 25: Q2 CNF -> 600 s cap each; report verdict/TIMEOUT; if SAT,
     decode and verify with the independent checker: E677 on all pairs, rho = nabla
     directly, E255 status of every element (an E255 failure would be a counterexample to
     the ETP implication — report it VERBATIM with the table, nothing else, and stop).
 Sizes: print variables/clauses for every CNF. Do NOT exceed the caps; the long runs are a
 separate cloud item. Total local budget: 90 minutes wall, one solver process at a time.

## Deliverables
1. `problems/etp677/simple/{simple_cnf.py, simple_check.py, run_calib.sh}`; CNFs for the
   C6 orders written to `problems/etp677/simple/in/` (they will be shipped to the cloud).
2. `problems/etp677/simple/calibration.out` — the C1..C6 table with times and verdicts.
3. `engine/out/codex/etp677_simple_search_report.md` — what was built, the table, any
   deviation, ending with the line DONE-SIMPLESEARCH.
