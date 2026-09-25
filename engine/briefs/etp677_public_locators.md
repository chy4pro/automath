# SHARED SPEC (owner line, 09:0x) — no private bucket names in public content. Applies to codex5 (pub/bundle/, pub/small_certs/, freeze)
# and codex11 (pub/github/). Each screen edits ONLY its own directories.
L1 Replace EVERY `gs://[gcp-project]/...` URI (ext11..ext16, hashes/...) by a public locator of the form
   `zenodo:<DOI_TODO>/<file-name>` (e.g. `zenodo:<DOI_TODO>/ext16-core7nh_m4.drat.gz`), to be filled after deposition exactly like the
   DOI placeholder; the sha256 rows remain the authority for identity. Keep byte sizes. Do this in JSON, MD, sh and py alike.
L2 The 36 MONO3 ext11 cube entries are verdict-only (no certificate): move them into a clearly separate table/array named
   "verdict_only_no_certificate" with NO URI field (or drop them from the public registry) — never list them beside certified rows.
L3 Internal upload helpers (github/scripts/publish_big.sh and any bucket→public upload script) are out of the public repo: delete from
   pub/github and from the manifest; keep a copy under engine/harvest/etp677_internal_tools/ if useful.
L4 Freeze/acceptance grep list gains `gs://` and `automath-compute` (plus the existing: dialogue|codex|luna|chatgpt|qwen|registry R46|
   engine/harvest|$HOME|gmail). Both screens report the grep over their own directories = empty.
L5 (revised 09:0x) The owner file problems/etp677/pub/big_proof_hashes.txt now holds exactly the 9 sha rows (marker already removed by the
   owner line). The bundle mirror and the github copy must be re-mirrored BYTE-FOR-BYTE from it (cmp identical); no independent edits.
Markers: codex11 writes problems/etp677/pub/github/DONE-LOCATORS; codex5 writes problems/etp677/pub/bundle/DONE-LOCATORS and only then FREEZEs
(its inventory must see both markers).
