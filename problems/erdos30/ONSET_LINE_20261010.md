# Erdős #30 — onset lowering line (Paperclip AUT-71), coordinator record

Target: the published theorem (SIDON_BOUND_PROOF.md; Zenodo 10.5281/zenodo.23103980; Lean lean/sidon30) with onset
N0 = 120^4 = 207,360,000 replaced by N1 = 4,600,000 (ratio 45.08), same coefficient 2√2/3, same additive constant 1.
Expected grade: small result (same theorem, wider effective range; Zenodo version + GitHub only, no X, no site claim).
Gates: two cross-vendor referees, finite checks (verifier), Lean (formalizer, CI only), board approval before any version.

## Step 1 — scout card (AUT-72, DONE 2026-10-09 18:3x)
notes/selection/onset30_card_20261010.md. Accepted. Findings: N0 enters only in section 6 via (6.3); sections 2–5 hold for
N ≥ 4; the Lean route uses the finite certificate k² ≤ (N + (2/3)(T−1) + 29T(3/4)^⌊(N−1)/T⌋)(1 + a_T(k−1)), T = ⌈√2x³⌉,
with 120 threaded through Statement/FinalReduction/IntegerScaleAndTail/SecondOrderFinal and GThinSidonBridge depending on
the original proposition. G2: no external theorem with the same (γ, +1) and a smaller onset found; Ruzsa 2026-09 survey
and two forum PDFs unread; no novelty clearance (none needed for an effectivity extension, but outward wording must stay
qualified). session: fresh (issue_assigned AUT-72).

## Step 2 — clean room CR-9 (AUT-73, attacker-1 / Astra, DONE 18:42) and VER (AUT-74, verifier, DONE 18:35)
- CR-9: problems/erdos30/CR9_ASTRA_ONSET_20261010.md — PROVED (coordinator judgement: consistent, sent to referees).
  Route A: P_ε(y) > (4/1089)x² for every real x ≥ 463/10 using only Lemma 7 (5.1); α > 719/2500, √2 < 99/70, βu > 941/100,
  e^{941/100} > 12100, F(x) = ε(4y/3+√2x³)/x² strictly decreasing on [u,∞), F(u) < 134/121 < 10/9. Route B: r ≥ 32,
  x < √2(r+2), η/x² < 29·69·(3/4)^32 < 667/3300 < 1/2; scalar lemma for every x ≥ 1 by exact subtraction (11/18)x² + …
  Clean room: brief = proof sections 1/5/6 verbatim + finite-certificate chain; no referee reports, no literature.
  The attacker corrected a numerical typo in the brief (x1 bracket); proof unaffected. session: fresh (issue_assigned AUT-73).
- VER: notes/review/VER_onset30_20261010.md — CONFIRMED. Referee B's 4,540,589 / 3,630,447 reproduced exactly; margin
  M(x1) = 0.0301 (CR-9's 4/1089 is a lossy lower bound, consistent); M not monotone (CR-9 does not use it); discrete (B3)
  holds exactly for all N ∈ [2,829,212, 1.2e7], worst η/(x²/2) = 0.3845 (consistent with 2·667/3300 = 0.404 bound);
  existing coarse Lean tail lemmas reach only N ≥ 1.67e7 → formalizer must follow CR-9's chain. session: fresh (AUT-74).
- Coordinator lesson: the brief carried an unverified decimal bracket (46.29 < x1 < 46.30; true 46.3116). Same class as
  SELECTION rule 6 — no coordinator numerics in briefs unless verified.

## Steps 3–5 — dispatched in parallel 2026-10-09 18:5x (owner full-speed instruction)
- AUT-76 REF (referee-1, Claude) and AUT-77 REF (referee-2, Claude): independent cross-vendor review of CR-9 (the new
  section is Astra-written, so Claude referees are the cross-vendor pair); reports to notes/review/REF_CR9_referee{1,2}_20261010.md.
- AUT-78 LEAN (formalizer, Astra): lean/sidon30 onset 120^4 → 4,600,000 via Route B; keep transfer bridges compiling; CI only.
- AUT-79 VER part 2 (verifier): check_sidon_bound_v2.py replaying every CR-9 certificate exactly + integer (B3) scan.
Referee repairs, if any, go to the formalizer as comments (mathematics only).

## Pending
- Owner doctrine decision on the AUT-62 question card (option A includes this line); the owner may cancel the line there.
- After PASS + green CI: transplant CR-9 (i) as section 6 of SIDON_BOUND_PROOF.md v2 (status line updated), then
  request_board_approval (grade small result) before any Zenodo version.

## Steps 3–5 — results (2026-10-09 19:0x–19:2x) and coordinator verdict
- AUT-76 referee-1 (Claude): PASS, 41 comparisons recomputed true, no repair (3 cosmetic remarks on §(ii) wording;
  note that r ≥ 32 comes from N−1 > 32T, not from the floor bound alone). session: resumed after a provider quota cut; all
  checks re-run in the second session. notes/review/REF_CR9_referee1_20261010.md
- AUT-77 referee-2 (Claude): PASS, 48 checks (40 numeric + 8 symbolic), no mathematical repair (E1 wording; E2/E3
  formaliser notes — moot, the formaliser used (B4.2) and the hypothesis 463/10 ≤ x). session: resumed after a quota
  cut; computation in the second session. notes/review/REF_CR9_referee2_20261010.md
- AUT-78 formalizer (Astra): DONE. `sidon_second_order' : SidonSecondOrderBound'` (N ≥ 4600000) kernel-checked; CI
  37978411704 (commit fd880ad) build 8759 jobs + 39 exact axiom guards; documentation run 37979173140 (commit ff9a9e4).
  Old theorem is a corollary; transfer statements unchanged; no mathematical change to Route B. One failed CI (unfold).
- AUT-79 verifier: check_sidon_bound_v2.py exit 0 (2.3 s): 67 CR-9 certificates, 30 identities, 62-point sanity grid,
  exact (B3) for every N in [4.6e6, 5.6e6] + block starts to 1.2e7, old small-N enumeration.
- Verdict: ALL GATES PASSED (two cross-vendor referees, finite checks, Lean, G2 card). SIDON_BOUND_PROOF.md updated to
  version 2 (Section 6 = CR-9 (i) verbatim as refereed; statement, status line, §8 record, §9 checker note; version
  history remark). Grade: SMALL RESULT — same theorem, same coefficient and constant, onset 120^4 → 4,600,000 (×45);
  no new bound, no novelty claim. Outward action proposed to the owner: one Zenodo version (v2) of the existing record
  + GitHub (already pushed). No X, no site claim, no e-mail.
- Cost of the line (runs): scout 1, attacker-1 1, verifier 2, referee-1 1 (+1 quota-cut), referee-2 1 (+1 quota-cut),
  formalizer 1 (3 CI runs), coordinator 5. Engine time not metered here.

## Step 6 — publication (2026-10-10 03:2x, coordinator on Opus 5.5)
- Board approval 04b27a03 (this line, one new Zenodo version) APPROVED 2026-10-10 02:56Z; 7c4457ab (AUT-75 related work, timing A1 = fold into this version) APPROVED 02:55Z. Decision: ONE version carries both (A1's own wording; one Zenodo version per problem per day).
- Corrections to the approval text (no change of scope): the record already has Zenodo v1 (10.5281/zenodo.23103980) and v2 (10.5281/zenodo.23105891, optimality), so this is Zenodo version 3; the record's artefact is the LaTeX paper (publish/automath-papers/erdos30/main.pdf), with proof text, checkers, CR-9, referee/verifier reports and Lean linked on GitHub from the description, as for v1/v2.
- Paper v3 prepared (papers-repo commit 192fbf3, local): Section 6 = SIDON_BOUND_PROOF.md §6 (v2) in LaTeX (normalized error renamed Φ(x) because F(N) is the Sidon function); Theorem 2.1 onset 4,600,000; abstract, table, footnote, Remark 9.1, §9.3 and provenance updated; Lean sidon_second_order' (run 37978411704); new §8.6 (Akwei) + table row + bib from PRIORITY_ADDENDUM §4. README and zenodo_description.html updated.
- Gate before upload: AUT-96 VER transcription/consistency check (verifier) → notes/review/VER_paper30_v3_20261010.md. On PASS: push the papers repo, then `tools/zenodo_newversion.py 23105891 main.pdf --version 3 --description zenodo_description.html --publish`, record the DOI here and in the README.
- 2026-10-10 03:3x — AUT-96 (verifier) PASS-WITH-REPAIRS: no mathematical or numerical discrepancy; four optional wording repairs, all applied (notes/review/VER_paper30_v3_20261010.md). Papers repo pushed (034b6c7; DOI in README 4fe0bb4).
- **PUBLISHED: Zenodo version 3 = 10.5281/zenodo.23273526** (concept 10.5281/zenodo.23103979), main.pdf 18 pp., carrying both approvals (04b27a03 onset + 7c4457ab A related work). Grade: small result. No X, no site-claim edit, no e-mail. LINE CLOSED.
