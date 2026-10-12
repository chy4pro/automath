# AUT-148 — capacity-transfer formalisation status reconciliation (2026-10-12)

Status: DONE. README patch pushed 2026-10-12 after board approval 3685dd22 (automath-papers commit 34a9860, README only). PDF p.3 erratum deferred.

## Record check
Recorded Lean scope (inbox/STATUS.md 2026-10-02T23:17Z/23:23Z; lean/sidon30/README.md; lean/sidon30/PLAN_TRANSFER.md;
problems/capacity_transfer/README.md; ledger 10-03 00:3x): CI 37076247531, commit 2f981a7, 26 axiom guards, axioms
propext / Classical.choice / Quot.sound only. Kernel-checked: g_thin_second_order (Thm 1.3), weakSidon_second_order
(Thm 1.2), sonar_triangle_bound (Thm 1.1 coefficient-2 bound), difference_triangle_scope_bound and
difference_triangle_expanded_bound (Thm 1.4); plus the earlier ordinary Sidon bound. Not formalised: cosine sonar,
Manhattan, boxes, all-N square supplement, kernel functional results, analytic capacity argument.
The records agree with each other; no rebuild needed.

## Public statements
| Location | Statement | Consistent with record |
| --- | --- | --- |
| README publication line | four bounds kernel-checked, CI/commit | yes |
| README "Review and formalisation status", last paragraph | only ordinary Sidon checked, no transfer formalised | NO (stale, pre-Lean) |
| README top "Repairs applied (task 040b)" and closing line | pre-publication task prose | obsolete, not false as history |
| zenodo_description.html | four bounds + theorem names + run/commit; non-formalised list | yes |
| main.tex / PDF abstract (p.1) | four bounds kernel-checked | yes |
| main.tex / PDF final section (p.15) | four bounds, Lean/Mathlib versions, run/commit, axioms | yes |
| main.tex / PDF end of §2 intro (p.3, tex l.193–195) | "Apart from that earlier Sidon bound, no statement in this note is claimed to be formalised in Lean." | NO (stale; found in this check, not in the AUT-147 dossier) |
| main.tex line 1 (TeX comment, not in PDF) | "Only the earlier ordinary Sidon bound is Lean-checked." | NO, source-only |

## Repair
- README: patch notes/selection/AUT148_capacity_transfer_readme.patch (prose only; applies cleanly to
  publish/automath-papers with `git apply`; privacy grep clean). Replaces the stale paragraph with the recorded scope,
  adds an erratum line for PDF p.3, marks the 040b sections historical. Not applied to the publish tree, not pushed.
- Manuscript p.3 and the TeX comment: NOT changed now (a source edit without a new PDF would desync the published
  version; the issue forbids a new paper version for this alone). Fold into the next capacity-transfer version if one
  is ever made: replace tex l.193–195 by "The ordinary Sidon consequence of that paper has been checked in Lean; four of
  the bounds in this note are kernel-checked as described in Section~\ref{...final section...}." and update line 1.
- Outward step: pushing the README patch to automath-papers = board approval request (grading: small documentation
  correction, not a result).
