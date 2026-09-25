# CODEX TICKET (sol tier, Lean 4 + Mathlib) — close the two uncertified links of the
# extension-reduction chain: L7 quotient coordinatization, L8 minimal-counterexample dichotomy.
# Repo: $HOME/workspace/claudecode/automath; project lean/etp677_ext/ (Lean
# v4.34.0-rc1, local Mathlib path dependency; existing Ext677.lean has L1–L6 — reuse its
# definitions E677, E255At, productOp, Eq4, ldiv, IsMagmaHom). English. Local compute:
# lake build only. Time box 3 h.

## Why
The R46 audit (engine/out/codex/etp677_r46_audit_report.md, A5) found that the chain
"UNSAT(GC_{B,m}) ⟹ no counterexample to 677→255 has quotient B with fibre size m" uses two
human-proved links that are not in Lean: (i) a surjective hom with equal fibres lets us
present N as a pair-indexed product B × M with SOME family c satisfying Eq4 (the
coordinatization), and (ii) a counterexample of minimal order is either simple (no proper
non-trivial congruence) or admits a proper quotient B with 1 < |B| < |N| that satisfies
E677 and E255 (minimality) and has fibres of a common size 1 < m < |N|.

## Theorems to prove (statements may be adjusted if a cleaner equivalent is used — say so)
L7 (coordinatization). Let `opM` on a finite `M` satisfy E677, `f : M → B` a surjective
   magma hom onto `opB` (E677 on B follows from surjectivity — prove that too, `L7a`),
   and suppose all fibres have the same cardinality `m` (from L2). Then there exist a type
   `Fib` with `Nat.card Fib = m`, an equivalence `e : M ≃ B × Fib` with `(e x).1 = f x`,
   and a family `c : B → B → Fib → Fib → Fib` such that `e` transports `opM` to
   `productOp opB c` (i.e. `e (opM x y) = productOp opB c (e x) (e y)`), each `c x y s`
   is injective (permutation rows), and `Eq4 opB hB c` holds (via L3). Existential
   statement is fine (`∃ Fib e c, …`); use `Fib := Fin m` if convenient.
L8 (minimality dichotomy). Define `IsCounterexample op := E677 op ∧ ¬ E255 op` on a finite
   carrier. Prove: if `opN` on `N` is a counterexample and no counterexample exists on any
   finite type of smaller cardinality (state this as a hypothesis quantified over
   `Fin k`, `k < Nat.card N`, with an arbitrary operation), then EITHER every congruence
   of `opN` is trivial or total (simple), OR there is a congruence `θ` with
   `1 < Nat.card (Quotient θ) < Nat.card N` such that the quotient operation satisfies E677
   and E255, and (by L2 applied to the quotient map) all θ-classes have the same size `m`
   with `1 < m < Nat.card N`. You will need: a congruence gives a quotient magma and a
   surjective hom (Mathlib `Quotient` / `Setoid` machinery); quotient of an E677 magma is
   E677 (L7a); the size bound from `Nat.card N = Nat.card (Quotient θ) * m`.
L9 (optional, if time permits) glue: from L8's second case and L7 conclude the existence
   of `(B, m, c)` with `Eq4` and, using L4 + the hypothesis that some point fails E255,
   the existence of a level `a` and `σ` with `¬ ∃ s, c x_a a s σ = σ`; and using L6, that
   `a` is not idempotent (because the fibre magma `c a a` would be a smaller
   counterexample — this uses the minimality hypothesis again).

## Deliverables
`lean/etp677_ext/Ext677Quot.lean` (imports Ext677), `lake build` clean, `#print axioms` for
every new theorem appended to `lean/etp677_ext/AXIOMS.txt` (only propext / Classical.choice /
Quot.sound acceptable), and `engine/out/codex/etp677_lean_L7L8_report.md` with the exact
statements, deviations, build-log tail, ending with DONE-LEANQUOT. If a lemma resists,
deliver the rest and state the obstruction.
