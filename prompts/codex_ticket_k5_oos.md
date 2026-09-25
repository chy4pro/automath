# TICKET K5OOS — out-of-sample and independent re-verification of the K5-GFQ construction (Kourovka 16.95, R5)

Self-contained. Do NOT modify existing files. New files only under `problems/k1695/k5_oos/`; report at
`engine/out/codex/k1695_k5_oos_report.md` ending with the literal line `DONE-K5OOS`. Every number must come
from a command you ran, with logs under `problems/k1695/k5_oos/logs/`. Compute budget: 90 minutes wall.

## Inputs
- `engine/harvest/k1695_r5_gfq/k5_gfq.py` (SHA-256 d04f15c03e80458effaeec466b6fa05822cd49ec419e570d3ae7a9736fff3592 — verify
  before use) and `engine/harvest/k1695_r5_gfq/K5-GFQ_submission.md` (its own statement of the construction,
  the profile criterion gcd(P_T, P_T^vee, C_m) = 1, the k=2 corrected criterion, the {a,a,b,b}@n=4 obstruction, and a
  5866-cell table for q in {3,4,5,7,8,9}, n <= 30 claiming 5689 FOUND / 177 NONE). Read the prose definitions
  (clean placement, residue profile, capacity partition) and re-implement them yourself for T2.

## Tasks
T1 (exact reproduction). Run `python3 k5_gfq.py --table --csv k5_gfq_table.csv --nmax 30 --qs 3,4,5,7,8,9` from a copy in
your directory; print SHA-256 of the produced full CSV and of the NONE-cells CSV and compare with the values
claimed in the submission (full CSV b9e4bde9...5195c, NONE CSV bc94363f...19b1 — the full hashes are in the
submission text; report MATCH / MISMATCH with the exact strings). Record counts FOUND/NONE per family.
T2 (independent checker). Write `indep_check.py` FROM SCRATCH (do not import k5_gfq.py): given q, n, coefficient
multiset u and positions s, decide cleanliness directly from the definition in the submission (build the
polynomial, test the forbidden-root condition over the splitting field or via the gcd criterion computed with
your own polynomial arithmetic over GF(q)). Validate it on the submission's own worked examples and controls
(V-a)-(V-c). Then re-check (i) a seeded random sample of >= 500 FOUND witnesses from T1's CSV and (ii) EVERY NONE cell
by your own exhaustive enumeration. Any disagreement is a FINDING with a reproducer.
T3 (out-of-sample). Extend the table to n in 31..40 for q in {3,4,5,7,8,9} (all three families), and, if the
script's field builder supports it (check how GF(4)/GF(8)/GF(9) are built and add the analogous modulus), to
q in {11,13,16} for n <= 30. Report FOUND/NONE counts and list every NONE cell. Test the claimed NONE pattern
out of sample: "every NONE is in the all-ones family; k = n with m > 1; additionally in odd characteristic
n in {4,8,16}, k in {2, n-2}" — say exactly which new cells confirm or break it.
T4 (verdict). Does the construction + criterion survive independent re-implementation and out-of-sample
extension? List FINDINGS (possibly none — say so).

## Report
T1-T4 with tables, exact commands, SHA-256 of every CSV, then `DONE-K5OOS`.
