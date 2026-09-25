# CODEX TICKET (writing + packaging; sol) — apply the G1 audit fixes to Paper 1 and its bundle,
# then FREEZE. Inputs: engine/out/codex/etp677_paper1_audit.md (B1–B4, M1–M2, N1–N2),
# problems/etp677/pub/paper1/, problems/etp677/pub/bundle/, problems/etp677/pub/github/,
# problems/etp677/pub/small_certs/ (line-677's regenerated core7nh_m4 CNF+DRAT and the A4
# CNF+DRAT with logs and SHA256SUMS — use them verbatim, do NOT re-solve; note the bundle's own
# rebuild blew up to 46 GB RSS: any kissat run you launch must use `--time=600` and a memory
# cap via `ulimit -v 8000000`), problems/etp677/pub/checkers/parity_halves.py and
# dropone_core7.py (line-677's standalone checkers; run them with KISSAT=tools/kissat/build/kissat,
# save outputs next to them, hash them). DONE marker: DONE-PAPER1FIX.

## Fixes (apply exactly)
B2 Lemma 4.2: status → "written proof + exhaustive computation; partial Lean corroboration";
   cite the public checker (bundle path of handproof/check_handproof.py or its copy) and its saved
   output for the 252 solutions / five orbits / sizes 36,36,36,36,108; describe hand_f_normalize,
   hand_k_normalize, hand_rep*_check_true as the formalised normalisation/representative checks
   only. Same change in CLAIMS.md.
B3 Lemma 5.1: keep the general statement as a WRITTEN proof; state that
   `Ext677.fibre4_symbolic_nh` formalises the Fin 4 / marked coordinate 0 specialisation used by
   Theorem 5.5. Same in CLAIMS.md (status "written; Lean: specialisation").
B4 Bundle: add sat/small/core7nh_m4.{cnf,drat} + logs and sat/small/a4_e677.{cnf,drat} + logs
   from pub/small_certs/ (hashes verbatim), generate sat/small/certificates.json and per-cell
   SHA256SUMS; change finalize_manifest.py to FAIL (non-zero) if any expected cell, its
   `s VERIFIED` drat-trim log, or its checksum is missing; rerun it. Regenerate the axiom table
   with a single isolated `lake build` (no other lake process running — coordinate via the
   dialogue) and fresh `#print axioms`.
M1 Replace the projection sentence in sections/04_fibre3.tex with: "There are 23,328 surviving
   enumerated assignments, yielding 1,944 distinct projected triples with constant L; none
   violates (4.8)." (numbers from parity_halves.py output — confirm they match; if your run gives
   different numbers, STOP and report.)
M2 Add two rows to CLAIMS.md: "Parity route (Sec. 4.x): exhaustive computation — checkers/
   parity_halves.py + output + sha256" and "Drop-one minimality of Core-7: computation —
   checkers/dropone_core7.py + output (seven SAT models re-checked) + sha256"; include both
   scripts and outputs in the bundle and the GitHub package (sat/checkers/).
N1 Replace the first two header lines of the public witness file (pub/github/witness/m5_witness.md
   and its bundle copy) with a neutral description ("Five-point local witness for the relaxed
   Core-10 + defect system; 21 pair-operations × 5 rows; replay with replay_witness.py") — no
   product names, no URLs; keep the table byte-identical.
N2 Keep the disclosure clause; it becomes true after this round.
B1 FREEZE: rebuild main.pdf; write problems/etp677/pub/paper1/FREEZE_INVENTORY.txt with sha256 of
   main.tex, every sections/*.tex, refs.bib, CLAIMS.md, main.pdf, and of every bundle file;
   create the marker file problems/etp677/pub/paper1/DONE-PAPER1 containing the inventory's own
   sha256 and the UTC time. No further edits after the marker without a new inventory.
## Deliverables
The edited paper/bundle/package, FREEZE_INVENTORY.txt, DONE-PAPER1, and
engine/out/codex/etp677_paper1_fixes_report.md ending with DONE-PAPER1FIX.
