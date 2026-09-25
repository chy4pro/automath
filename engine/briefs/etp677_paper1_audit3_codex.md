# CODEX TICKET (sol) — G1 AUDIT v3 of the FROZEN v2 publication set (NEW ticket; audit2 is history).
Scope: ONLY the files listed in problems/etp677/pub/FREEZE_INVENTORY.sha256 (see problems/etp677/pub/FREEZE.md; components paper1, bundle,
github; frozen 2026-08-30T18:09:55Z; 243 rows). Do not read anything outside that set except the freeze control files themselves.
Re-verify and report:
 1. every theorem/lemma/proposition/corollary/computation statement vs the Lean sources and the axiom table;
 2. every CLAIMS.md row vs the artifact it names — any CLAIMS-named artifact absent from the package is a BLOCKER (list by name);
 3. the certificate registry: sha256 rows vs files present; the isolated "verdict-only, proof not retained" section for the 39 A5 cubes;
    zenodo:<DOI_TODO> locators consistent between bundle and github; the core7nh_m4 rows (raw + gz hashes); s3_core7.py now shipped;
 4. the leak grep over the frozen set: dialogue|codex|luna|chatgpt|qwen|registry R46|engine/harvest|$HOME|gmail|gs://|automath-compute
    (only github/scripts/check_manifest.py:29 is whitelisted);
 5. the witness checker and the hand-proof checker run from the bundle/package AS SHIPPED (copy to a temp dir first);
 6. the G2 wording: C1/C2 cited as known (Blueprint 13.1/13.4), C3+C4+C5 as the contribution, Issue #1464 cited as public-but-unreviewed;
 7. bundle/README.md:37 reproduction step (`cd ../../../../..` assumes the private layout) — MINOR unless it breaks reproduction.
Rules: no lake build unless fewer than 2 other lake builds are running; no solver runs beyond the small cells (timeout 600, ulimit -v 8000000);
no edits to the frozen set; no push/upload.
Report: engine/out/codex/etp677_paper1_audit3.md with a READY / NOT READY verdict and a BLOCKER/MAJOR/MINOR list, ending with DONE-PAPERAUDIT3.
