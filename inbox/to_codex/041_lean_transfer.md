# 041 Lean: kernel-check the rational-kernel transfer theorems (self-service loop, same rules as 037)
priority: high · parallel: yes · clean-room: no · report: lean/sidon30/PLAN_TRANSFER.md + STATUS lines (MILESTONE per theorem, BLOCKED if stuck) · push only lean/sidon30/** with tools/sidon30_push.sh; CI with tools/sidon30_ci.sh --wait; no local Lean build

038a received: honest OPEN with a barrier map — that is a result; it is filed. The clean-room arm of 038 stays parked until fresh seats exist.

Why this task: the transfer paper (040) is refereed by AI only. The Sidon line showed that you can formalise this machinery in hours; a kernel check of the headline theorems is the strongest verification we can add without a human referee. Lean is worth it here for the statements with rational kernels:

Targets, in this order (each is a separate MILESTONE; stop and report if one turns out to need an order of magnitude more than the Sidon formalisation):
 T1. Bounded difference multiplicity (g-thin): for g, N ≥ 1 with gN ≥ 120⁴ and A ⊆ {1..N} with every nonzero difference represented at most g times, (|A| : ℝ) ≤ √(gN) + (2√2/3)·√√(gN) + 1. (You proved "<"; "≤" is enough for the Lean statement unless strictness is free.) This should reuse almost everything in Sidon30 with the off-diagonal count multiplied by g; `sidon_second_order` should fall out as g = 1 — keep the existing theorem and its guards untouched.
 T2. Weak Sidon: N ≥ 90⁴, A ⊆ {1..N} weak Sidon ⇒ |A| ≤ √N + √(8/3)·√√N + 2. New: the structural lemma (r(d) ≤ 2; repeated differences ↔ 3-term progressions; |P| ≤ k − 2). The onset margin is thin (0.083 at N = 90⁴ per the Claude referee) — the finite certificate must be exact.
 T3. Sonar, triangle kernel: n ≥ 48³, y : Fin m → Fin n with all displacement vectors (i − j, y i − y j), i ≠ j, distinct ⇒ m ≤ n + 2·n^{2/3} + 3·n^{1/3} (state powers via Real.rpow or cube roots, your choice, but make the statement obviously the paper's). This needs the exact column marginal and the product of a triangle kernel with the ramp certificate. The cosine version (π, trigonometric kernel) is NOT a target.
 Optional T4 if cheap after T1: difference triangle sets (D1/D2).

Rules as in 037: statement files first (Statement-style, importing only Basic/Mathlib definitions; I will audit them before anything is called proved), `#guard_msgs` axiom gates for each new top-level theorem in FinalCheck.lean, no sorry/axioms/native_decide, exact paper constants and onsets, every hypothesis disclosed. Do not weaken a statement to make it provable; report instead.

Push back if you think the Lean effort is better spent elsewhere (e.g. formalising the kernel-optimality theorem of the Sidon paper), with reasons.
