# CODEX TICKET (engineering + exact search; any tier — verified verdicts only) — MONOGENIC
# LADDER v2 CUBE-AND-CONQUER: decide n = 11, 12, 13 (and as far as possible) locally by
# splitting, and package the cube cover for the cloud.
# Repo: $HOME/workspace/claudecode/automath. Read problems/etp677/simple/mono2/
# (mono_cnf2.py = canonical BFS encoding, in/mono2_n*.cnf, out/ with DRAT-verified UNSAT for
# n = 5..10; n = 11, 12 UNKNOWN at 600 s) and problems/etp677/ext/ext_cube_driver.py (a cube
# driver from the EXTCP ticket: exact 2^k partitions or march_cu cubes, per-cube caps, per-cube
# DRAT checks, aggregate UNSAT only when the whole cover is verified — reuse it). Local caps:
# ≤ 600 s per cube, ≤ 2 concurrent kissat processes, total local budget ≈ 2 h; keep RSS small.
# kissat: tools/kissat/build/kissat; drat-trim: tools/drat-trim/drat-trim; march_cu under tools/
# if built. tools/breakid is BROKEN (no symmetry found) — do not use. DONE marker: DONE-MONO3.

## Splits to try (structural, so each cube is meaningful)
S1 The L_0-cycle length m: with generator 0, the sequence c_0 = 0, c_{i+1} = 0*c_i is a cycle
   of length m ∈ {6, …, n} (no exact cycle of length 2, 3, 4 (E677) or 5 (E677+E255); and for
   the DEFECT instance E255 fails at 0, so m ≠ 1 and the generator is not idempotent). In the
   canonical BFS labelling 0*0 = 1 always; the cycle labels beyond that are determined by the
   scan order — derive which literal pattern "cycle closes at step m" corresponds to, and use
   the m-split as the first level (n − 5 cubes), or if the cycle labels are not fixed by the
   canonical order, split on the value of 0*1 and 0*(0*1) instead.
S2 The defect witness: the defect clause is ∀ s,u: ¬(0*0 = s ∧ s*0 = u ∧ u*0 = 0); split on
   s = 1 (forced) and the value u = 1*0 (n − 1 cubes), combined with S1.
S3 Exact 2^k partitions on the first k primary variables as a baseline (k = 2..6).
For each split: run every cube with the cap, verify each UNSAT cube's DRAT against the CNF +
cube units, record per-cube time; report a cover table (cube → verdict → time → proof). If a
cover is fully UNSAT-verified, that is the theorem "no finite E677 magma of order n has a
generating point failing E255" — state it exactly like that, with the list of proof files.
A SAT cube = decode with mono_canon.py, verify (rows, E677, defect at 0, generation) — do
not interpret beyond "the decoded table verifies / does not verify".

## Deliverables
problems/etp677/simple/mono2/cubes/ (cube files, logs, proofs, cover tables as JSON + md),
a cloud package for the unfinished cubes (cubes as separate CNFs with the cube's unit clauses
appended, SHA256SUMS, a runner startup_mono3.sh in the startup_ext.sh style; do not launch),
and engine/out/codex/etp677_mono3_report.md ending with DONE-MONO3.
