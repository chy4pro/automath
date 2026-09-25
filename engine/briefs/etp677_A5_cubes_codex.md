# CODEX TICKET (exact search engineering; any tier — verified verdicts only) — the A5 two-sided
# group-action family, cubed on the 44 identity-row orbits, run LOCALLY under caps.
# Repo: $HOME/workspace/claudecode/automath. Read problems/etp677/diag/ (a5.py,
# diag_cnf.py — NOTE it writes a zero-padded DIMACS header "p cnf 000…"; normalise it —,
# diag_cpsat.py, check.py; controls.out; the D1 report engine/out/codex/etp677_D1_diag_report.md)
# and registry STEP 45/48 (§4/§7 of the ULTIMATE Pro harvest: S3, D8, Q8, A4, S4, F21 admit NO
# E677 magma of the form x*y = a_x y b_x⁻¹; A4 is DRAT-certified in diag/recheck/; A5 open;
# under the S5-conjugation automorphisms the 3600 possible identity rows fall into 44 orbits).
# Local caps: ≤ 600 s per cube, ≤ 2 concurrent solvers, total ≈ 3 h. DONE marker: DONE-A5CUBES.

## Tasks
1. Reproduce the 44 orbits: the row at the identity is (a_1, b_1) ∈ A5 × A5 acting by
   z ↦ a_1 z b_1⁻¹; S5 acts by simultaneous conjugation (a,b) ↦ (g a g⁻¹, g b g⁻¹) (prove in a
   comment that this is the full symmetry fixing the identity point: relabelling by φ_{c,d}
   with c = d = g); count orbits, print one representative per orbit with its size (sizes
   must sum to 3600).
2. Cube-and-conquer: for each orbit representative, fix (a_1, b_1) and solve the E677-ONLY
   instance (no E255, no defect) with kissat on diag_cnf.py's encoding (and CP-SAT as a second
   engine where kissat is slow) under the cap; verify every UNSAT cube by drat-trim on the
   CNF + unit clauses; report the cover table (orbit → size → verdict → time → proof). If all
   44 are UNSAT-verified: THEOREM "no E677 magma on 60 points has rows x*y = a_x y b_x⁻¹ over
   A5" (state exactly so; it closes the A5 diagonal template, and with §4 the non-abelian
   two-sided route for all groups tried). Any SAT cube: decode with check.py, verify E677 on
   all 3600 pairs, report E255 status at every point (an E255 failure = a counterexample to
   677 ⟹ 255 — verify twice, do not interpret further).
3. Package the unfinished cubes for the cloud (CNF per cube with units appended, SHA256SUMS,
   runner in the startup_ext.sh style; do not launch).
## Deliverables
problems/etp677/diag/cubes/ (orbits.json, per-cube CNF/logs/proofs, cover table md+json),
engine/out/codex/etp677_A5_cubes_report.md ending with DONE-A5CUBES.
