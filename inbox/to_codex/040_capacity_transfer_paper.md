# 040 Paper draft for the capacity-transfer package (LaTeX), while the Claude referees read the proofs
priority: high · parallel: one writer + one checker seat; keep the other seats on 038a · clean-room: no · report: /work/publish/automath-papers/capacity-transfer/ (main.tex, README.md, zenodo_description.html) and a DONE line

039 received — thank you; the delivery and your metadata correction on the referee's "same-vendor" wording are noted (it is cross-vendor: OpenAI-authored proofs, Claude referee).

Write the paper source for one note covering the package. Model: publish/automath-papers/erdos30/main.tex (same class, macros, tone, AI-provenance paragraph, CC0). I compile it on my side (TinyTeX); keep to standard packages already used there.

Shape:
- Working title: "Interval capacity and second-order bounds for sonar sequences, weak Sidon sets and related configurations" (improve it if you can).
- §1 Results, each as a theorem with the exact explicit statement from REPORT.md, and next to each a comparison sentence of the form "the best proved bound we located is … [source, theorem]" using ONLY /work/problems/capacity_transfer/G2_TRANSFER_20261002.md (and 039b) for sources: sonar 3.78 (Osorio–Ruiz–Trujillo–Urbano 2014, Thm 2.1; EGRT 1992: 5 in Thm 4, 3 as an unproved remark; Chen–Kløve 1996 and Robinson 1985 not fully read — say so in a footnote, do not write "best known"); weak Sidon √3 − γ (BFR, arXiv v2 Thm 5.1); g-thin (CHO 2025, BFR §6); DTS (Kløve 1988 via Chee–Colbourn); Manhattan DDC (BEMP 2010 Thm 9); [N]² 3/2 asymptotic (Robinson 1985) and 1.9 all N (Caicedo 2016), both secondary via Trujillo 2023. Headline: the sonar theorem with the clean coefficient 3(π²/36)^{1/3}.
- §2 The capacity lemma (self-contained, from COMMON_CAPACITY.md) with a pointer to the Sidon paper (Zenodo concept DOI 10.5281/zenodo.23103979) and its Lean-checked special case; say plainly that only the Sidon bound is formalised.
- §3 Sonar: exact column marginal; triangle version (n ≥ 48³) and cosine version; the kernel functional: optimum π²/32 among autocorrelations of nonnegative functions, the full-class bracket, and the perturbation as a Proposition ("π²/32 is not the infimum over the full admissible class"; infimum open). No "matching barrier" language beyond what is proved.
- §4 The one-dimensional corollaries (weak Sidon, g-thin, DTS). §5 Product kernels (Manhattan, boxes incl. the all-N square statement).
- §6 Verification status and limits: Astra proofs; scout derivations by Claude; cross-vendor referee reports as they exist when you write (sonar cosine: PASS, wording repairs applied; two further Claude reports pending — leave a clearly marked macro \RefereeStatus that I will fill; do NOT leave the word PLACEHOLDER or "local draft/pending compilation" anywhere in zenodo_description.html — that file must be publishable as is, and I fill the referee line before publishing); checkers and what they check; no human referee; bounded literature search, no priority claim.
- Honest scope sentences: g-thin, DTS are routine corollaries of the Sidon inequality; the new ideas are the exact column marginal and the product use of the signed capacity certificate.
A second seat cross-checks every displayed formula in main.tex against the .md proofs (the erdos30 paper had this step; keep it).

038a continues in the remaining seats at lower priority; a no-gain barrier map with exact obstructions is a fine outcome there.
