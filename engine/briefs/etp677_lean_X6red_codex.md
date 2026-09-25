# CODEX TICKET (sol tier, Lean 4 + Mathlib) — certify the X_6 reductions of the second
# attacker (engine/out/codex/etp677_X6_existence2_report.md). Repo:
# $HOME/workspace/claudecode/automath; project lean/etp677_ext/ (reuse
# Ext677Pattern.lean L12F/L12H, cycle lemmas, L13*, Ext677PatternPairs.lean). English.
# lake build only. Time box 2.5 h.

## Theorems (finite E677 magma with E255 unless stated)
 X1 Define `U x := op (op x x) x`, `W x := op x (U x)`, `P x := ldiv x (U x)` and prove the
    iterate forms: `U x = ldiv x (ldiv x x)` (exists as diagonal_candidate), `W x = ldiv x x`
    (W is the unique right unit: op x (W x) = x), `P x = ldiv x (ldiv x (ldiv x x))`,
    `L12F x = ldiv x (P x)` (i.e. F = L^{-4}).
 X2 Fixed-point lemma: `L12F op h677 x = x ↔ op x x = x`. Needs "no exact L-cycle of
    length 4 under E255": prove `L12_no_exact_cycle_four` (toolkit (Cyc): if the L_x-cycle
    through x has exact length 4 then E255 fails at x — derive from E677/KEY; the length-2/3
    proofs in Ext677Pattern.lean show the method). Then: F x = x means L_x^{-4} x = x, so the
    exact period divides 4; periods 2 and 4 excluded, so period 1, i.e. xx = x.
 X3 Definitional relations of the pattern terms (with a, u, p, b, d, v, c, w as in L13):
    `b = L12F a`, `v = U b`, `c = W b`, `u = U a`, `w = W a`, `p = P a`, `d = op b b`.
    Hence the six X_6 disequalities are the equalizer statements
    v ≠ w ⟺ U (F a) ≠ W a, v ≠ u ⟺ U (F a) ≠ U a, c ≠ a ⟺ W (F a) ≠ a,
    c ≠ w ⟺ W (F a) ≠ W a, c ≠ u ⟺ W (F a) ≠ U a, c ≠ p ⟺ W (F a) ≠ P a (state as iff's).
 X4 Conditional closures: assuming `hFU : ∀ x, L12F (U x) = U (L12F x)` prove: idempotent-free
    ⟹ ∀ a, U (F a) ≠ U a (i.e. v ≠ u); assuming `hFW : ∀ x, L12F (W x) = W (L12F x)` prove
    ∀ a, W (F a) ≠ W a (c ≠ w). (Via X2: U(F a) = U a ⟹ F (U a) = U a ⟹ U a idempotent.)
 X5 (from the pattern report, "c = a ⟹ b idempotent" is PROVED by identity (J) — locate it
    in problems/etp677/ext/fibre3/pattern/notes.md and formalize: W (F a) = a ⟹ op b b = b,
    hence under idempotent-freeness c ≠ a.)

## Deliverables
`lean/etp677_ext/Ext677X6.lean` (root), `lake build` clean, `#print axioms` appended to
AXIOMS.txt (propext / Classical.choice / Quot.sound only), and
`engine/out/codex/etp677_lean_X6red_report.md` ending with DONE-LEANX6. Deliver what closes;
list what resists.
