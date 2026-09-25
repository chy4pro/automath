# SINGLE POST-AUDIT PATCH (owner line STEP 76 + audit2). Three screens, disjoint directories, then FREEZE v2 + audit3. No push/upload.
# Markers: codex5 -> problems/etp677/pub/bundle/DONE-PATCH-BUNDLE; codex11 -> problems/etp677/pub/github/DONE-PATCH-GITHUB;
#          codex3 -> problems/etp677/pub/paper1/DONE-PATCH-PAPER. codex5 FREEZEs v2 only when all three exist.

## codex5 (pub/bundle/ + freeze)
B1  small_certs/ is internal staging, NOT a publication component (components = paper1, bundle, github; say so in FREEZE.md v2).
    The bundle must not reference outside itself: drop the `../../../small_certs/core7nh_m4.drat.gz` row from bundle/sat/small/core7nh_m4.SHA256SUMS
    and point every core7nh_m4 small-cell entry (sat/small/core7nh_m4.proof-pointer.json, sat/small/certificates.json, scripts/build_large_registry.py,
    scripts/finalize_manifest.py, large-certificates.json) at the existing locator zenodo:<DOI_TODO>/ext16-core7nh_m4.drat.gz plus the recorded
    hashes (raw e065c1c8..., gz 981837b7... — take the full values from problems/etp677/pub/big_proof_hashes.txt verbatim).
B3(1) The 39 fast A5 cubes (00-04,06-13,15-25,27-28,30-35,37-43) have hashes but no retained proof object: move them into an explicitly isolated
    section "DRAT-verified during the run, proof object not retained, proof hash recorded" (registry + large-certificates.json + README); no
    'VERIFIED' label without an object; the five residual cubes keep their archived-certificate rows.
FREEZE v2 (after DONE-PATCH-GITHUB and DONE-PATCH-PAPER exist): regenerate SHA256SUMS/MANIFEST, FREEZE_INVENTORY.sha256 + FREEZE.md v2
    (three components, counts, digest), leak grep (list incl. gs://|automath-compute; whitelist github/scripts/check_manifest.py:29), verify.sh quick.
    Marker: problems/etp677/pub/DONE-PAPER1-V2.

## codex11 (pub/github/)
B2  Ship problems/etp677/simple/fibre_core/handproof/s3_core7.py (147 lines) verbatim beside the checker as github/handproof/s3_core7.py
    (and mirror into the bundle only if the checker is mirrored there — coordinate by leaving a note in your report, do not edit pub/bundle).
    Add MANIFEST.json + SHA256SUMS rows; prove handproof/check_handproof.py runs from a clean copy of the package (cp -R to a temp dir, run, paste output).
    Leak grep over pub/github must stay zero.

## codex3 (pub/paper1/ + mirror to pub/github/paper/)
(i)  sections/07_closed_routes.tex lines ~52-54: "no two-sided section for S3, D8, Q8, A4, S4, or the group of order 21; among these only the A4 cell
     has a packaged DRAT replay".
(ii) CLAIMS.md row "Computation 6.1": "defect chain 0→1→3≠0 at coordinate 0; defective coordinates {0,1,3,4}" (replace "defect (0,1,3)").
B3(1)-paper: §7 Computation 7.2 text and CLAIMS row 7.2: "five residual cubes have archived DRAT certificates; the other 39 were verified during
     the run and their proofs were not retained" — no VERIFIED label without an object.
(iii) refs.bib: confirm/adjust arXiv 2512.07087 and the blueprint chapter URL from the G2 internet run — poll for
     engine/harvest/etp677_pro_novelty_r46.md (every 2 min); apply what it confirms; if it contradicts, keep the entry and flag in the report.
Then ONE PDF rebuild; mirror the changed paper files byte-for-byte into problems/etp677/pub/github/paper/; append the new main.pdf SHA-256 to
DONE-PATCH-PAPER. No bundle, no kissat, no lake.
