# CODEX TICKET (Lean 4; sol tier) — formalise the (R46/AMPLIFY) reduction.
# Repo: $HOME/workspace/claudecode/automath; project lean/etp677_ext (conventions as
# in Ext677.lean; Mathlib available). 0 sorry; `#print axioms` lines appended to AXIOMS.txt.
# Heavy processes ≤ 2 (lake build). DONE marker: DONE-LEANAMP.

## Statements (registry R46 STEP 33, §I.3 — banked, re-derived)
For a magma (M, op) define E255At (x : M) := op (op (op x x) x) x = x and the E255 set
E(M) := {x | E255At x}. For magmas M, N with the product operation on M × N
(op (a,b) (c,d) = (op a c, op b d)):
A1  E255At (x, y) ↔ E255At x ∧ E255At y  (pointwise; no E677 needed).
A2  E677 for M and N implies E677 for M × N (coordinatewise); same for E255.
A3  (finite M, N) the E255 density δ(M) := |E(M)| / |M| is multiplicative:
    δ(M × N) = δ(M) · δ(N)  (as rationals; Fintype.card of the set E(M) via a decidable
    predicate — assume DecidableEq M, N).
A4  Corollary (finite E677 magma A with δ(A) = r < 1): for every k, the product A^k
    (Fin k → A, or iterated product) is a finite E677 magma with δ(A^k) = r^k, hence for
    every ε > 0 there is a finite E677 magma with δ < ε. State as: ∀ ε > 0, ∃ finite E677
    magma M, δ(M) < ε — derived from the existence of one A with δ(A) < 1.
A5  Contrapositive, the usable form: if there is a function f : ℕ → ℚ with
    ∀ finite E677 magma M, δ(M) ≥ f |M| and ∀ α > 0, eventually f n ≥ n^(−α)  (i.e. f is
    n^(−o(1))), then every finite E677 magma satisfies E255 everywhere. (Prove: a
    counterexample A with δ(A) = r < 1 gives δ(A^k) = r^k = |A^k|^(−α₀) with
    α₀ = −log r / log |A| > 0, contradicting f eventually; you may formalise with the weaker,
    cleaner hypothesis "∃ c > 0, ∀ M, δ(M) ≥ c" first (A5'), then A5 if time permits, using
    Real.log / rpow from Mathlib.)

## Deliverables
lean/etp677_ext/Ext677Amplify.lean (A1–A4 and A5' mandatory; A5 optional), AXIOMS.txt appended,
engine/out/codex/etp677_lean_amplify_report.md ending with DONE-LEANAMP.
