# Task: S3 adversarial review of the 677 structure-theory paper (round 1)

You are a VERIFIER, not a co-author: find errors, do not fix or improve.

Target: papers/etp677_structure/main.tex (~2400 lines).
Ground truth sources: problems/etp677/campaign_registry.md (corrected timestamps
authoritative), prompts/etp677_R3_common.md, problems/etp677/*_report.md
(F1/F4/F5/F7, R2, R3A/R3C/R3F, R5C + R5C_scripts/, R5A_codex_report.md),
r5a_search.py, R5C_scripts/m176.json.

Review dimensions, in priority order:
1. MATHEMATICAL CORRECTNESS: every theorem/lemma statement vs its source report.
   Flag any statement that is stronger than what the source proves (especially:
   R5C Thm 5.1 must be scoped to AFFINE fibres; 176 minimality must be scoped to
   its scanned family p in {5,11}, q<=32; order-11 census is 22/87 partial;
   community n<=10 DRAT is unreviewed).
2. VERIFICATION-LABEL HONESTY: [machine-verified] labels must point to scripts
   that actually verify that exact claim; [computational, partial] scopes must
   match reality. Spot-run at least 3 of the cited scripts and compare outputs.
3. INTERNAL CONSISTENCY: notation (L_y, Lambda, Theta_t, N(t,v)), numbering,
   cross-references, the blocked-routes table vs the prose.
4. OMISSIONS that mislead: any place where a partial result reads as complete.

Output: notes/reviews/etp677_structure_review1.md with findings classified as
CRITICAL ERROR (breaks a claim) vs JUSTIFICATION GAP (claim plausible, proof
insufficient as written) vs EDITORIAL. For each: file location (line/section),
the problem, the source-of-truth citation. End with verdict:
VALID / INVALID / VALID-WITH-GAPS. Do not rewrite the paper.
