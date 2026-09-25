# COMPUTE TICKET (codex): bounded q=4 search for small-delta 3-perfect branch objects

Implement from the definitions below YOURSELF (do not read other project files).
Write your program and outputs ONLY to
  $HOME/workspace/claudecode/automath/engine/out/codex/
final report: etp677_q4hunt_r45.md there. HARD COMPUTE BUDGET: 15 minutes total
wall-clock for all runs combined; put an internal time limit in the program itself.

## Definitions
q = 4, n = 21. Points {0..20}. Lines: the cyclic planar difference set D = {3,6,7,12,14}
mod 21: line_j = { (j+d) mod 21 : d in D } for j = 0..20. (Verify: every pair of points
in exactly one line; abort if not.)
A BRANCH TABLE: 21x21 array T, rows are permutations; a bijection nu: columns->values;
column c equals nu(c) exactly on a line ell_c (choose ell_c = line_{sigma(c)} for a
bijection sigma of your choice), and off ell_c the column takes pairwise distinct
values != nu(c) (so exactly q=4 values are absent per column).
Define a\v (row inverse), Xi_t(x) = x\(t\x), E(t,v) = #{x : Xi_t(x)=v},
N(t,v) = #{a : a*t=v}, delta(v) = Sum_t E(t,v) - n.
Row r is PERFECT iff E(r,.) == N(r,.) as vectors.

## Task
Stochastic search (simulated annealing or your choice) over branch tables:
stage 1: reach >= 3 simultaneously perfect rows; stage 2: with those rows protected,
minimize Sum_v |delta(v)|. Report, with exact counts:
- number of restarts, stage-1 successes;
- the MINIMUM delta-mass reached with 3 protected perfect rows, and its delta pattern;
- if mass <= 4 is reached: print the FULL table + lines + nu (JSON) for each such hit
  (they will be independently verified; that is the deliverable that matters).
Print DONE-Q4HUNT at the end of the report. No prose beyond a LIMITS section.
