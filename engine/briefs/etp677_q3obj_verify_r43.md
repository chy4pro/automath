# VERIFICATION TICKET (codex): three order-13 left-quasigroup tables

Implement everything YOURSELF from the definitions below. Do NOT search this machine
for related code or files; do not read any other project directory. Work in your own
scratch space. Output: create the single file
  ~/workspace/claudecode/automath-sandbox/out/codex/etp677_q3obj_verify_r43.md
containing your script (one fenced python block) and the printed report.

## Definitions
A table T is a 13x13 array over {0..12}; row a is the list T[a][0..12]. Write
a*t := T[a][t]. All rows must be permutations. Left division: a\v is the unique w
with a*w = v.
- N(t,v) := #{a : a*t = v}  (multiplicity of value v in COLUMN t).
- Xi_t(x) := x\(t\x);  E(t,v) := #{x : Xi_t(x) = v}.
- E'(t,v) := #{x : t*(x*v) = x}.   [check E' == E cellwise; report any mismatch]
- delta(v) := (Σ_t E(t,v)) − 13.
- A row r is PERFECT iff E(r,v) = N(r,v) for every v.
- Column structure: for each column t report the value profile of N(t,·) as a sorted
  multiset, the set ell_t := {a : a*t = v_t} where v_t is the (unique, if any) value
  with N(t,v_t) = 4, and D_t := {v : N(t,v) = 0}.
- Plane check: do the 13 sets ell_t (if each has size 4) cover every unordered pair
  of points {0..12} exactly once? Report yes/no and the exception count.
- TI check: is T[(a+1) mod 13][(t+1) mod 13] == (T[a][t]+1) mod 13 for all a,t?

## For EACH of the three tables below report
rows-all-permutations (yes/no); E'==E (mismatch count); the full delta vector;
the list of perfect rows; plane check; TI check; nu vector (v_t per column);
per-column |D_t|.

## Tables

### TABLE 0
[[10, 4, 12, 6, 11, 2, 1, 3, 8, 7, 0, 9, 5], [10, 9, 4, 3, 0, 7, 8, 2, 11, 1, 5, 6, 12], [11, 9, 8, 0, 4, 12, 2, 6, 7, 10, 1, 3, 5], [10, 5, 8, 1, 7, 0, 9, 4, 2, 6, 12, 11, 3], [4, 9, 2, 1, 11, 6, 7, 0, 3, 5, 10, 12, 8], [5, 2, 8, 9, 11, 7, 4, 10, 1, 12, 3, 0, 6], [9, 3, 6, 1, 12, 7, 2, 5, 10, 4, 0, 8, 11], [0, 12, 1, 7, 11, 8, 2, 4, 5, 3, 9, 6, 10], [1, 10, 9, 11, 6, 7, 12, 4, 3, 0, 8, 2, 5], [10, 1, 5, 4, 8, 9, 2, 11, 3, 12, 6, 7, 0], [3, 9, 7, 8, 2, 5, 11, 4, 6, 12, 0, 10, 1], [12, 11, 8, 5, 1, 4, 10, 7, 3, 9, 0, 6, 2], [7, 0, 10, 1, 9, 11, 3, 8, 4, 12, 2, 6, 5]]

### TABLE 1
[[11, 4, 5, 3, 10, 7, 0, 1, 9, 12, 2, 6, 8], [0, 12, 8, 3, 9, 2, 5, 7, 4, 11, 1, 10, 6], [6, 1, 5, 4, 12, 2, 3, 10, 7, 8, 9, 0, 11], [7, 11, 9, 3, 5, 8, 12, 10, 1, 2, 6, 4, 0], [1, 8, 6, 10, 7, 2, 0, 3, 12, 5, 11, 4, 9], [9, 12, 4, 5, 1, 3, 0, 10, 11, 6, 8, 7, 2], [3, 12, 10, 7, 11, 5, 6, 2, 9, 8, 0, 4, 1], [7, 10, 11, 1, 2, 4, 0, 5, 3, 8, 12, 9, 6], [7, 12, 5, 2, 6, 9, 10, 0, 8, 4, 11, 1, 3], [5, 7, 0, 3, 1, 10, 9, 6, 2, 8, 11, 12, 4], [7, 6, 12, 0, 1, 2, 4, 8, 9, 3, 10, 11, 5], [4, 5, 7, 12, 3, 0, 8, 10, 9, 1, 11, 2, 6], [12, 2, 5, 8, 1, 11, 7, 9, 10, 0, 3, 4, 6]]

### TABLE 2
[[5, 3, 9, 2, 12, 7, 10, 11, 0, 1, 8, 6, 4], [5, 6, 0, 11, 7, 1, 12, 8, 4, 3, 9, 2, 10], [11, 6, 10, 8, 2, 9, 7, 1, 12, 5, 3, 0, 4], [5, 12, 10, 0, 4, 6, 9, 3, 2, 7, 11, 1, 8], [10, 6, 7, 0, 12, 8, 1, 2, 9, 4, 5, 11, 3], [4, 8, 10, 9, 12, 1, 5, 0, 3, 11, 2, 7, 6], [3, 9, 11, 0, 6, 1, 7, 12, 5, 10, 8, 4, 2], [9, 10, 1, 4, 12, 0, 7, 3, 11, 8, 6, 2, 5], [6, 0, 12, 5, 8, 1, 11, 3, 9, 2, 7, 10, 4], [5, 4, 8, 1, 0, 2, 7, 6, 9, 11, 10, 3, 12], [7, 6, 4, 10, 9, 5, 2, 3, 1, 11, 8, 12, 0], [0, 5, 10, 7, 11, 12, 3, 4, 9, 6, 8, 2, 1], [12, 7, 5, 0, 3, 10, 6, 9, 8, 11, 1, 2, 4]]

## Rules
- Print exact counts; no prose beyond a LIMITS section.
- python3 stdlib only; the script must run in under 60 seconds.
- When done, print DONE-E-VERIFY as the last line of the report file.
