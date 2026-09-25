# CODEX TICKET (engineering + exact search; any tier) — a BETTER INSTRUMENT for the
# extension-with-defect cells (the tier-1 cells time out at 12 h even on the known-SAT control).
# Repo: $HOME/workspace/claudecode/automath. Read problems/etp677/ext/ext_cnf.py (the
# encoder: pair-indexed extension of a base magma B by a fibre of size m, with an E255 defect
# over a chosen level; bases f7a=4s+3t, f7b=4s+t, m9, f5, f13, f31c; options --no-defect,
# --fix-product, --fix-gauge, --fix-diag, --defect-level), ext_decode_verify.py (independent
# decoder/verifier — keep using it), gen_all.sh / gen_tier1b.sh (which cells exist), and
# registry R46 STEP 31 (problems/etp677/campaign_registry.md, grep "STEP 31") for the 12-h
# outcome incl. the known-SAT control that timed out. Local caps: any single solve ≤ 600 s;
# heavy processes ≤ 2 (≈2.5 GB each). OR-tools CP-SAT: engine/venv_item3/bin/python.
# kissat: tools/kissat/build/kissat; drat-trim: tools/drat-trim/drat-trim.
# NOTE: tools/breakid/build/breakid is BROKEN (reports symmetry group order 1 on every
# input, even (1∨2)(3∨4)); do not rely on it — a separate ticket rebuilds it.
# DONE marker: DONE-EXTCP.

## Goal
Decide the tier-1 cells (ext/in/*.cnf; base × fibre size m ≤ 5, defect over the encoded level)
faster than plain kissat. Deliver an instrument that (i) solves the known-SAT CONTROL cells in
minutes, (ii) reproduces the DRAT-known UNSAT results (F31 m=2, m=3: proofs in ext/out/drat/),
and (iii) then attacks the undecided cells.

## Tasks
1. CP-SAT model `problems/etp677/ext/ext_cpsat.py` equivalent to ext_cnf.py's semantics
   (same inputs/options; same decoded output format so ext_decode_verify.py verifies it):
   IntVar per fibre product, AddAllElement/AddAllDifferent for left-bijectivity in the fibre,
   table constraints for E677 instances (use the base table to fix the first coordinates and
   only branch on fibre maps), the defect constraint, symmetry breaking by fixing the gauge
   (fibre relabelling per base level: the m! × |B| gauge — fix the first row of each level's
   fibre map to the identity where ext_cnf's --fix-gauge does the equivalent; prove your gauge
   fixing is WLOG in a comment). Run with 8 workers, log progress every 60 s.
2. Cube-and-conquer for kissat: split the tier-1 CNFs on the gauge-fixed top variables
   (march_cu in tools/ if built; else a simple splitter on the first k fibre-map variables),
   and a driver that runs cubes with kissat under a per-cube cap, collecting UNSAT cubes' DRAT
   proofs and any SAT cube. Compare with plain kissat on the controls.
3. Calibration table (mandatory, in the report): for each control cell and each DRAT-known
   cell: instrument, wall time, verdict, verification (ext_decode_verify.py output for SAT;
   drat-trim for UNSAT). If the instrument cannot solve the known-SAT control within 600 s
   locally, say so plainly and report the best partial progress (do NOT extrapolate).
4. Package the winning instrument as a cloud runner `problems/etp677/ext/startup_extcp.sh`
   (same conventions as startup_ext.sh: metadata WORKERS/CAP/BKTSUB, inputs from the bucket
   subdir, status every 600 s, per-cell logs uploaded, DONE marker, poweroff). Do not launch.

## Deliverables
ext_cpsat.py, the cube driver, startup_extcp.sh, calibration logs under ext/cp_out/, and
engine/out/codex/etp677_extcp_report.md ending with DONE-EXTCP.
