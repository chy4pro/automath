# POST-AUDIT PATCH LIST (single patch after codex7's re-audit v2; then FREEZE v2 + mechanical checks only). Owner line STEP 75 items:
(i)  sections/07_closed_routes.tex lines 52-54: list must include A4 — "no two-sided section for S3, D8, Q8, A4, S4, or the group of
     order 21; among these only the A4 cell has a packaged DRAT replay".
(ii) CLAIMS.md row "Computation 6.1": replace "defect (0,1,3)" by "defect chain 0→1→3≠0 at coordinate 0; defective coordinates {0,1,3,4}".
(iii) refs.bib: arXiv 2512.07087 and the blueprint chapter URL — confirm/adjust from the G2 internet run (677 novelty) before the patch.
(iv) k1695-independent; no effect here.
+ codex7 audit2 findings (pending) + C5 wording of the k1695 paper is a different package.
Procedure: one codex ticket (sol) applies all items to paper1 (+ mirrored copies in pub/github/paper), rebuilds the PDF once, then codex5
re-freezes (FREEZE v2: inventory, leak grep, verify.sh quick) — nothing else re-run.
# codex7 audit2 (09:56) blockers — packaging only, math PASS:
B1 small_certs/ (11 files) absent from FREEZE_INVENTORY though bundle/sat/small/core7nh_m4.SHA256SUMS references ../../../small_certs/core7nh_m4.drat.gz
   -> codex5: add small_certs payload to the inventory (+ FREEZE.md counts/digest) or remove the references and define the reduced component.
B2 handproof/check_handproof.py (Lemma 4.2, CLAIMS-named) cannot run from the shipped package: dependency s3_core7.py missing
   -> codex11: ship s3_core7.py into handproof/ (verbatim), prove the checker runs from the package, manifest rows.
B3 39/44 A5 rows labelled VERIFIED have proof hashes but no frozen object and no public locator (cubes 00-04,06-13,15-25,27-28,30-35,37-43)
   -> owner-line decision: publish the 39 proofs with zenodo locators, OR move to the isolated verdict-only section + revise paper/CLAIMS status.
Then: codex5 FREEZE v2 (inventory + leak grep + verify.sh quick), codex7 audit3 on the frozen set only.
# STEP 77 note for the NEXT freeze after ext-a5p lands (or v2 if first): the 39 A5 cube rows get NEW proof_sha256 values (new solver run) and
# zenodo locators; CNF hashes must equal cover_table.json exactly; every cube must show drat-trim=s VERIFIED in ext18/out/final.txt.
