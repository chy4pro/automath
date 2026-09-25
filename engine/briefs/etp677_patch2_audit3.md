# PATCH 2 after G1 audit3 (owner line GO, 13:5x). Three screens, disjoint directories; then FREEZE v3 + audit4. No push/upload; no edits outside
# your own directory. "Clean copy" = the package copied to a FRESH temp directory OUTSIDE the repo (mktemp -d), so monorepo paths cannot resolve.
# Markers: codex11 -> problems/etp677/pub/github/DONE-PATCH2-GITHUB; codex5 -> problems/etp677/pub/bundle/DONE-PATCH2-BUNDLE, then FREEZE v3
# -> problems/etp677/pub/DONE-PAPER1-V3.

## codex11 (pub/github/ only)
B1  handproof/s3_core7.py inserts the package root in sys.path but the encoder lives at sat/encoders/core7_free.py -> add
    HERE.parent / "sat" / "encoders" (package-relative) to sys.path; regenerate handproof/outputs/* from the clean copy; update MANIFEST.json /
    SHA256SUMS rows; PROVE with a transcript: `cp -R pub/github $(mktemp -d)/pkg && cd .../pkg && python3 handproof/check_handproof.py`
    ends with HANDPROOF CHECK PASS.
PACKAGE-ESCAPE grep (mandatory, zero hits over pub/github, excl. .lake): `\.\./\.\./\.\.`, `parents\[[3-9]\]`, `problems/etp677/`, `\.venv/`, `/diag/`.

## codex5 (pub/bundle/ + freeze)
M1  scripts/run_standalone_checks.py must invoke bundle/check_a5_orbits.py with a BUNDLE-RELATIVE default (no problems/etp677/diag/cubes path);
    scripts/finalize_manifest.py --validate-only must read bundle/big_proof_hashes.txt (the frozen copy), not pub/big_proof_hashes.txt.
N1  README.md:37 — replace the fixed `cd ../../../../..` by a bundle-relative command.
PACKAGE-ESCAPE grep (mandatory, zero hits over pub/bundle): same five patterns as above.
Prove from a clean copy (mktemp -d outside the repo): scripts/run_standalone_checks.py, scripts/finalize_manifest.py --validate-only,
scripts/check_m5_witness.py (or replay_witness.py) all PASS; paste transcripts in the report.
FREEZE v3 (only after DONE-PATCH2-GITHUB exists): regenerate SHA256SUMS/MANIFEST, FREEZE_INVENTORY.sha256 + FREEZE.md v3 (three components,
counts, digest), leak grep (dialogue|codex|luna|chatgpt|qwen|registry R46|engine/harvest|$HOME|gmail|gs://|automath-compute; whitelist
github/scripts/check_manifest.py:29) + the PACKAGE-ESCAPE grep over bundle/ and github/, verify.sh quick; marker DONE-PAPER1-V3.
Report: engine/out/codex/etp677_patch2_report.md (both screens append their section).
