# CODEX TICKET (engineering; any tier) — REPRODUCIBILITY BUNDLE for paper 1 (PLAN_0830.md §9, gate G3).
# Repo: $HOME/workspace/claudecode/automath. No cloud launches. DONE marker: DONE-CERTBUNDLE.

## Tasks
1. Lean: from a clean checkout state of lean/etp677_ext, run `lake build` and produce
   `AXIOMS_TABLE.md`: every public theorem of the modules listed in PLAN §9 with its `#print axioms`
   (generated, not copied), grouped CLEAN (exactly propext/Classical.choice/Quot.sound or a subset)
   vs LABELLED (name the generated certificate axiom). Record Lean/Mathlib versions.
2. SAT certificates: regenerate every small CNF from its generator with the exact command
   (core7_free.py m=2,3; core_joint.py --set joint --defect m=3,4 and --set c8 --defect m=4;
   the Core-7 + NH m=4 CNF via the snippet in registry STEP 64 addendum 2 — turn it into
   fibre_core/core_nh.py; diag_cnf.py A4 E677-only), solve with kissat producing DRAT, verify
   with drat-trim, and record sha256 of CNF and proof, sizes, times; for the large cloud
   certificates (jdef_m4 1.95 GB, dlgdef_m4_def 5.7 GB, c8def_m4 2.1 GB, the five A5 cubes
   0.67–2.39 GB, the MONO3 cubes) list the bucket paths, the sha256 recorded in the registry /
   bucket .sha256 files, and the drat-trim logs (download the dt.logs only).
3. A5 orbit cover: a standalone script recomputing the 44 conjugacy orbits and the cover
   (sizes sum 3,600), plus the cube generation parameters (units) from diag/cubes/cover_table.json.
4. The m = 5 witness: a standalone checker (no imports from our encoders) that reads
   engine/harvest/etp677_fibre4_m5witness_pro.md and verifies the 250 chain equations and the
   defect; print its output.
5. Package: problems/etp677/pub/bundle/ with README (how to rebuild everything), the scripts,
   the small CNF/DRAT pairs (< 50 MB each; larger ones by pointer + sha256), SHA256SUMS, and a
   MANIFEST.json; total size < 500 MB.
## Deliverables
problems/etp677/pub/bundle/, AXIOMS_TABLE.md, engine/out/codex/etp677_cert_bundle_report.md
ending with DONE-CERTBUNDLE.
