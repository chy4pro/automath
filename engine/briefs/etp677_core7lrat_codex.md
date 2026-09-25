# CODEX TICKET (Lean 4 + SAT certificates; sol tier) — KERNEL-CHECKED fibre-3 exclusion via a
# verified LRAT proof of the gauge-free Core-7 instance (registry R46 STEP 49).
# Repo: $HOME/workspace/claudecode/automath. Encoder: problems/etp677/simple/fibre_core/
# core7_free.py (read its docstring: 8 symbols, 12 products, 7 instances, 14 pairs, σ as
# permutation matrices; m = 3 is UNSAT, DRAT in out/core7_m3.drat). Lean project lean/etp677_ext
# (Lean 4.34.0-rc1 + Mathlib; `Std.Tactic.BVDecide` / the LRAT checker `Std.Tactic.BVDecide.LRAT`
# is available in this toolchain — check `lake env lean` for `Std.Tactic.BVDecide.Frontend` and
# the `bv_decide` tactic; CaDiCaL is bundled with the toolchain). 0 sorry; #print axioms in
# AXIOMS.txt (a `Lean.ofReduceBool` axiom from the LRAT reflection is acceptable and must be
# named). Heavy ≤ 2. DONE marker: DONE-CORE7LRAT.

## Goal
A Lean theorem, kernel-checked, stating: "there is no assignment σ : Pair → Fin 3 → Equiv.Perm
(Fin 3) satisfying the seven lifted E677 chains (†)", where Pair is the 14-element type of
ordered base pairs used by the pattern, together with a Lean proof that this finite statement
implies: for finite E677 magmas M, B with B ⊨ E255, a surjective hom φ : M → B, and a : B with
Nat.card (fibre a) = 3 — False. (The second part is the "transport + lifting" argument: fibres
over the eight terms have size 3; choose bijections with Fin 3; the induced maps are the σ's;
the seven E677 instances of M give (†).)

## Route (in order; deliver what you get)
1. Encode the finite statement as a Bool-valued decision on the 14×3 permutation choices —
   6^42 cases is far too many for `decide`; instead express it as a propositional formula over
   the same Boolean variables as core7_free.py (permutation matrices + chain aux variables) and
   prove it with `bv_decide` (which calls CaDiCaL and checks the LRAT proof in the kernel via
   `ofReduceBool`), or directly with the `Std` LRAT checker on an LRAT file produced by
   `drat-trim -L` / CaDiCaL --lrat from out/core7_m3.cnf. Deliver the theorem
   `core7_free_three_unsat` and its axiom list.
2. Bridge lemma: a solution of the semantic statement (σ's satisfying (†) as functions) gives
   a satisfying assignment of the Boolean formula (straightforward: the permutation-matrix
   variables are `decide (σ p s t = v)`, the aux R-variables the intermediate values). So
   `¬ ∃ σ, (†)`.
3. Transport + lifting (reuse Ext677Window.lean / Ext677Fibre2's F1 fibre transport if
   LEANF2 has landed; otherwise prove: for φ a surjective hom of finite E677 magmas, left
   multiplication by m maps fibre(y) bijectively onto fibre(φ m * y); hence card fibre(a) =
   card fibre(W a) = card fibre(U a) = … for all eight terms) and the twelve product identities
   (all in the library: L13_u_mul_a, X1_W_right_unit, window_mul_U, ldiv defs, L13_a_mul_d,
   L13_p_mul_a, L13_v_mul_b, L13_b_mul_c?, window_W_mul_square, L13_d_mul_v …; add any missing
   one). Conclude `fibre3_exclusion`.
4. State the corollary with STEP 48 (LEANF2) if available: a finite E677 magma with a surjective
   hom onto an E255 quotient has no fibre of size 2 or 3.

## Deliverables
lean/etp677_ext/Ext677Core7Free.lean (+ any LRAT file under lean/etp677_ext/certs/), AXIOMS.txt
updated, engine/out/codex/etp677_core7lrat_report.md (which parts are kernel-checked, which
axioms, timings) ending with DONE-CORE7LRAT.
