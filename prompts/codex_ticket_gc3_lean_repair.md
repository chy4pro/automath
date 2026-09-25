# CODEX TICKET — K6-GC3-LEAN: make GoodCount3.lean compile (Lean 4 + Mathlib, no sorry) — DONE marker: DONE-GC3LEAN
Engine: codex on gpt-5.6-sol. Heavy processes: ≤ 1 (lake build only). No internet needed. No cloud.

## Goal
Turn engine/harvest/k1695_r6_gclean3_GoodCount3.lean (531 lines; the best of four Qwen rounds; last compile = 22 errors after
two Mathlib renames, see engine/briefs/k1695_r6_gclean4/BRIEF.md for the exact error log and per-error diagnosis) into a file
that compiles cleanly under the project's existing Lean/Mathlib toolchain (find it: `ls lean/ lean/proofenv/ ; cat lean/*/lakefile*`;
line-k1695 builds with `lake env lean` inside lean/proofenv — use the same). Target statements (keep them, do not weaken):
  * Delta-lemma: for x1 x2 x3 : K × K over a field K with at least one nonzero pairwise bracket br x y = x.1*y.2 - x.2*y.1,
    at least two of the six values Δ(i;j,k) = (x_i).1 * br x_i x_j + (x_i).2 * br x_i x_k are nonzero.
  * goodCount3: for A : Matrix (Fin 3) (Fin 3) K with IsUnit A.det there exist two DISTINCT σ τ : Equiv.Perm (Fin 3) such that
    e₁ is Krylov-cyclic for A * σ.permMatrix K and for A * τ.permMatrix K (det ![e₁, B e₁, B² e₁] ≠ 0). Either permMatrix
    convention is acceptable if stated.
You MAY restructure proofs freely (replace let-bound abbreviations by explicit terms, split lemmas, use `decide`-free tactics,
`linear_combination`, `field_simp`, `ring`, `Matrix.det_fin_three`), but NOT: sorry, admit, native_decide, new axioms,
`set_option maxHeartbeats` above 400000, or weakening the statements. Check `#print axioms goodCount3` at the end.

## Deliverables
1. lean/proofenv/K1695/GoodCount3.lean (or the analogous path next to StratumBAssembly.lean) compiling with 0 errors, plus the
   exact build command and its full output → engine/out/codex/k1695_gc3_lean_report.md (include `#print axioms` output).
2. If you cannot reach 0 errors: stop at ≤ 5 errors, list each remaining error with the goal state and your best diagnosis.
3. Run time and heartbeat count. Print the marker DONE-GC3LEAN on its own line in the report and in your final message.
Rules: never claim "compiles" without pasting the build output; distinguish PROVED (kernel-checked) from "compiles with sorry"
(forbidden anyway). Do not touch other files in lean/ except adding an import line to a lakefile/Main if needed.
