# CODEX TICKET — MUS extraction + DRAT certification for UNSAT extension instances (R46)
# ENGINEERING + LOCAL RUNS under caps. Repo: $HOME/workspace/claudecode/automath.
# Code in ENGLISH only. Read problems/etp677/ext/ext_cnf.py first (do not modify it; write
# under problems/etp677/ext/mus/). Tools: tools/kissat/build/kissat, tools/drat-trim/drat-trim.
# Instances: the list in problems/etp677/ext/mus/TARGETS.txt (filled by line-677 with the
# instances that came back UNSAT on the cloud, with their solve times). Local cap per solver
# call: 120 s; total local budget 2 h; one solver process at a time.

## Goal
For each UNSAT target instance (base B, fibre size m, defect at level 1), find WHICH base
pairs' eq.(4) constraints are needed for the contradiction — a small "instance-level MUS".
The eq.(4) clauses are grouped by base pair (x,y) (nb^2 groups); the structural clauses
(one-hot cells, permutation rows, defect clause, any --fix-diag units) are always kept.
1. `mus_groups.py`: re-emit the target CNF with the eq.(4) clauses tagged by group (x,y)
   (regenerate via ext_cnf.py's logic — import its functions or replicate the numbering
   exactly; verify by checking the re-emitted CNF is clause-for-clause identical to the
   original file, modulo order).
2. `mus_extract.py`: deletion-based MUS over groups: start from all groups, try removing one
   group at a time (kissat, 120 s cap; UNKNOWN counts as "needed"), keep the smallest set that
   stays UNSAT. Use the R7-A structure as the deletion order heuristic: try removing groups
   far from the star pair first. Output the MUS group list, its size, and for each kept group
   its subscripts P1..P4 (so a human can read which operations are coupled).
3. For the final MUS: kissat with proof logging + drat-trim verification of the reduced CNF;
   store proof size and verification time.
4. Also for every target instance itself: kissat with proof logging + drat-trim (proof
   sizes may be large; if a proof exceeds 20 GB or the cap, report so, do not force).

## Report
`engine/out/codex/etp677_ext_mus_report.md`: per instance — MUS size / nb^2, the kept
group list with P1..P4, whether the MUS contains only the three star-instances (R7-A: I1 =
(a,x_a), I2, I3) plus what else, certificate status, timings; end with DONE-EXTMUS.
A MUS of size <= 10 with a verified DRAT is a milestone-grade result (a human proof becomes
plausible); say so plainly if it happens, and say plainly if the MUS is essentially everything.
