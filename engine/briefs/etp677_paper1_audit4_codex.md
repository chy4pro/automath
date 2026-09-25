# CODEX TICKET (sol) — G1 AUDIT v4, SCOPED, of the FROZEN v3 set (problems/etp677/pub/FREEZE_INVENTORY.sha256, see FREEZE.md v3).
Scope: (a) every file whose hash changed between FREEZE v2 (inventory sha c7919c7f...) and v3 — list them from the two inventories (the v2 list
is in git history or engine/out/codex/etp677_patch2_report.md); re-check each changed file's content for correctness and for leaks/package escapes;
(b) copy problems/etp677/pub/github and problems/etp677/pub/bundle to a FRESH temp directory OUTSIDE the repo (mktemp -d) and run from there:
github: scripts/check_manifest.py, handproof/check_handproof.py, witness/replay_witness.py (or the shipped witness checker);
bundle: scripts/run_standalone_checks.py, scripts/finalize_manifest.py --validate-only, scripts/check_m5_witness.py. Paste transcripts.
(c) grep over both packages: leak list (dialogue|codex|luna|chatgpt|qwen|registry R46|engine/harvest|$HOME|gmail|gs://|automath-compute;
whitelist github/scripts/check_manifest.py:29) and PACKAGE-ESCAPE (\.\./\.\./\.\., parents\[[3-9]\], problems/etp677/, \.venv/, /diag/) — zero hits.
Do NOT redo the full statement/Lean audit (audit3 passed it); do not edit anything; no lake build; no solver runs.
Report engine/out/codex/etp677_paper1_audit4.md with READY / NOT READY, ending DONE-PAPERAUDIT4.
