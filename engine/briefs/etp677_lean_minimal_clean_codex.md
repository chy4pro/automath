# CODEX TICKET (Lean 4; sol tier; small) — re-point the minimal-counterexample corollary at the
# CLEAN fibre-3 theorem so the whole headline chain has standard axioms only.
# Repo: $HOME/workspace/claudecode/automath; project lean/etp677_ext. 0 sorry; own
# `#print axioms` for every listed theorem appended to AXIOMS.txt; peak memory must stay small
# (no whole-space `decide`; nothing new to decide here). Heavy ≤ 2 (lake build). DONE-LEANMINC.

## Tasks
1. In `Ext677Minimal.lean` (or a new `Ext677MinimalClean.lean` importing Ext677Core7Hand),
   provide clean versions of: `minimal_counterexample_no_class_two_or_three`,
   `minimal_counterexample_card_ge_four_mul`, `minimal_counterexample_congruence_class_ge_four`,
   `minimal_counterexample_congruence_card_ge_four_mul` — identical statements, proofs using
   `fibre3_exclusion_clean` / `fibre_two_or_three_exclusion_clean` instead of the bv_decide
   versions. Keep the old theorems (do not delete); name the new ones with suffix `_clean`.
2. `#print axioms` of all four `_clean` theorems must be exactly
   [propext, Classical.choice, Quot.sound]. Full `lake build` must pass.
3. Update lean/etp677_ext/AXIOMS.txt with a short "HEADLINE STATUS" paragraph listing the
   clean-tier chain: fibre2_exclusion, fibre3_exclusion_clean, fibre_two_or_three_exclusion_clean,
   the four `_clean` corollaries — and noting which theorems still carry the bv_decide certificate
   axiom (the legacy Core7Free versions only).
## Deliverables
The Lean changes, AXIOMS.txt, engine/out/codex/etp677_lean_minimal_clean_report.md ending with
DONE-LEANMINC.
