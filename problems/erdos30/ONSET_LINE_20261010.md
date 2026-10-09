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
