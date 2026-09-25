# TICKET L02-REVERIFY (independent re-verification, cross-family)

Inputs:
- engine/harvest/etp677_L02_cap2_r45_pro.md — a claimed q=3 (n=13) BRANCH OBJECT (JSON block:
  "table", "lines", "nu") with the claim: exactly three PERFECT rows (4, 6, 10) and delta(v) == 0
  for every v, and b(v) == 1 for every v.
- engine/briefs/etp677_L02_cap2_r45.md — the definitions (B1)-(B4), Xi_t(x) = x\(t\x), E(t,v),
  N(t,v), delta(v), g(c), b(v), PERFECT row, and the coupling identity (F-fusion) x * Xi_t(x) = t\x.

Rules:
- Do NOT read or reuse engine/scripts/check_L02_object.py or any checker in problems/etp677/.
  Implement every check yourself from the definitions in the brief.
- Check: (B1) rows are permutations; (B2) column structure incl. the missing sets D_t (|D_t| = q)
  and that the value nu(t) is attained exactly on the listed line; (B3) the 13 lines form a
  projective plane of order 3 (every pair of points on exactly one line); (B4) nu is a bijection;
  compute Xi, the E/N frequency vectors, the set of perfect rows, delta(v) for all v, verify
  F-fusion on all 169 cells, and compute b(v).
- Negative control: perturb two cells of the table (swap two entries in one row) and show which
  checks fail, so the checker is demonstrably not vacuous.
- Report: engine/harvest/etp677_L02_codex_reverify.md with your script embedded and its actual
  output pasted; final line must be exactly: DONE-L02REV
