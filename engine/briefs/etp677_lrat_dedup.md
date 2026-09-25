# TICKET (codex4, engineering only) — lrat-check rejects drat-trim's LRAT for cube_14
# (ext20 run of startup_lrat_cores.sh). Fix the pipeline so every core gets an independently
# checkable LRAT; do not touch the frozen publication tree; no cloud launch (line-677 launches).

## Observed (ext20/out, 2026-08-30 18:25Z)
cube_36: CORE-OK (raw 666,747,106 B → LRAT 456,097,152 B; lrat-check c VERIFIED).
cube_14: drat-trim `s VERIFIED` (1457 s; "98301 of 2237059 lemmas in core", "1351 RAT lemmas in
core") but lrat-check: `c FAILED: multiple literals unassigned in hint 14245375: -431942 -431942`
→ `c NOT VERIFIED` after 47 s. I.e. an LRAT lemma/clause carries a DUPLICATED literal
(-431942 twice); lrat-check treats it as two unassigned literals. cube_36 had (probably) no RAT
lemmas; the failure correlates with RAT lemmas in the core.

## Tasks
1. Reproduce locally on a SMALL instance that has RAT lemmas (e.g. problems/etp677/pub/small_certs
   a4_e677.cnf + .drat, or the core7 m=3 pair from the bundle): run the staged drat-trim with -L,
   then lrat-check; if it passes, construct/locate a small DRAT with a duplicated literal in a
   RAT lemma (kissat can emit such lemmas; or craft one by hand) and confirm the same failure.
2. Fix options, in order of preference; implement the first that works and keep the others as
   fallbacks selectable by metadata:
   (a) LRAT post-normaliser `lrat_dedup.py` (stream; no full load): for each lemma line, remove
       duplicate literals within the literal list (semantically safe: a clause with a repeated
       literal is the same clause), leave hints untouched, preserve deletion lines; then
       lrat-check the normalised file. Verify on the reproduction that lrat-check accepts it.
   (b) `lrat-trim` (Biere, https://github.com/arminbiere/lrat-trim — pin a commit, stage the
       source tarball with sha256 in SHA256SUMS): `lrat-trim core.lrat core.trimmed.lrat` and
       then lrat-check / cake_lpr on the trimmed file.
   (c) Latest drat-trim master (pin the commit; stage its tarball) for the -L export, if its
       LRAT writer fixed duplicate-pivot hints.
   (d) Fallback artefact if no LRAT checks: publish core.drat (trimmed DRAT) + an INDEPENDENT
       second drat-trim run of core.drat against the regenerated CNF (log kept) and state
       "LRAT export rejected by lrat-check (duplicate literal); trimmed DRAT re-verified".
3. Update problems/etp677/ext/startup_lrat_cores.sh: after drat-trim -L, run the normaliser
   before lrat-check; on lrat-check failure fall back to (b) if staged, then (d); status line
   must say which artefact was certified and by which checker; ALWAYS upload the trimmed
   core.drat.gz + both logs even when the LRAT fails. Keep UPLOAD-PROBE, apt line, phases.
4. For NEW solving runs (Core-12, E17260): evaluate CaDiCaL's native `--lrat` (CaDiCaL ≥ 1.7)
   as the future default proof format — pinned source tarball + sha256; do not switch running
   jobs. Report only.
5. LOCAL_TEST: extend with the duplicate-literal reproduction (must PASS after normalisation).

## Report
engine/out/codex/etp677_lrat_dedup_report.md ending DONE-LRATDEDUP: the reproduction, which
option was implemented, the diff summary, LOCAL_TEST transcript, and a relaunch card for the
remaining proofs (PROOFS list = whatever ext20 did not certify) into a fresh bucket sub.

# NOTE FOR THE RECORD (owner line STEP 90): DIMACS headers must be plain decimal — NO fixed-width zero padding ("p cnf 00000000000000003822 ..."
# broke drat-trim, whose %i parser reads leading zeros as octal and stops at the first 8/9, so proofs were checked against a wrong formula).
# Apply to every encoder/template you touch (the E17260 encoder was patched by the owner line).
