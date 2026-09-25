# CODEX TICKET (Lean 4; sol tier) — the HEADLINE COROLLARY in minimal-counterexample form.
# Repo: $HOME/workspace/claudecode/automath; project lean/etp677_ext (use Ext677Fibre2.lean:
# fibre2_exclusion / fibre2_quotient_class_ne_two, Ext677Core7Free.lean: fibre3_exclusion /
# fibre_two_or_three_exclusion, Ext677Quot.lean: quotient constructions, and the equal-fibre
# lemma L2_quotient_fibres). 0 sorry; own #print axioms appended to AXIOMS.txt (the bv_decide
# certificate axiom inherited from fibre3_exclusion is expected and must be listed).
# Heavy ≤ 2 (lake build). DONE marker: DONE-LEANMIN.

## Statements to formalise
Fix a universe u. For a finite magma (M, op) write `IsE677 op`, `IsE255 op`.
D1 `IsCounterexample op := E677 op ∧ ¬ E255 op` (finite M implicit).
D2 `IsMinimalCounterexample op := IsCounterexample op ∧ ∀ (B : Type u) [Finite B] (opB) (φ : M → B),
    Function.Surjective φ → IsMagmaHom op opB φ → (∃ x y, φ x = φ y ∧ x ≠ y) →
    (∃ b, ∀ m, φ m = b) ∨ E255 opB`
    — i.e. every proper non-trivial quotient satisfies E255. (Justify in a docstring that a
    counterexample of minimum cardinality satisfies D2: a non-trivial proper quotient is a
    strictly smaller E677 magma, hence E255 by minimality — you may ALSO prove that lemma:
    `minimal_of_min_card`: if op is a counterexample and no counterexample exists on a type of
    smaller Nat.card, then IsMinimalCounterexample op; use Nat.card and Fintype.card_le_of_surjective.)
T1 `equal_fibres`: for finite E677 magmas and a surjective hom φ, all fibres have equal
    cardinality (reuse L2_quotient_fibres if it says exactly this; else prove via
    w = y*(w*((y*w)*y)) and the fibre-transport bijection).
T2 `minimal_counterexample_no_class_two_or_three`: IsMinimalCounterexample op → for every
    surjective hom φ : M → B onto a finite E677 magma that is neither trivial (constant) nor
    injective, every fibre has Nat.card ≥ 4. (From D2 the quotient satisfies E255; fibres ≠ 2
    by fibre2_exclusion, ≠ 3 by fibre3_exclusion, ≠ 1 since non-injective + equal fibres,
    ≠ 0 by surjectivity.)
T3 Corollary in congruence language if the library has `MagmaCongruence` (Ext677Fibre2 has
    fibre2_quotient_class_ne_two with `quotientOp θ`): every non-trivial proper congruence
    class of a minimal counterexample has ≥ 4 elements; and `Nat.card M ≥ 4 * Nat.card B` for
    any such quotient, hence a minimal counterexample that is non-simple has order ≥ 4·|B| ≥
    4·5 = 20 if you can cite that no E677 magma has order 2, 3, 4 (no_E677_Fin2/Fin3 exist in
    Ext677Small.lean; order 4 may need a new decide — optional).

## Deliverables
lean/etp677_ext/Ext677Minimal.lean, AXIOMS.txt appended, engine/out/codex/etp677_lean_minimal_report.md
ending with DONE-LEANMIN.
