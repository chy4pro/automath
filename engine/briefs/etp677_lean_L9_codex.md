# CODEX TICKET (sol tier, Lean 4 + Mathlib) — L9 glue: the last human link of the extension
# reduction. Repo: $HOME/workspace/claudecode/automath; project lean/etp677_ext/
# (Ext677.lean L1–L6, Ext677Quot.lean L7/L7a/L8 exist — reuse). English. lake build only.
# Time box 2 h.

## Statement to prove (L9)
Let opN on finite N be a counterexample of minimal cardinality (as in L8's hypotheses) that
is NOT simple. Then there exist: a finite E677+E255 magma opB on B with 1 < |B| < |N|; a
fibre type Fib with 1 < |Fib| < |N|; a family c : B → B → Fib → Fib → Fib with permutation
rows satisfying Eq4 opB c; an equivalence e : N ≃ B × Fib transporting opN to productOp
opB c; and a level a : B and σ : Fib such that
   (i)  ¬ ∃ s, c x_a a s σ = σ   where x_a := opB (opB a a) a   (E255 fails at (a,σ)), and
   (ii) opB a a ≠ a   (the defect level is NOT idempotent).
Proof sketch: L8 gives θ, the quotient B := N/θ with E677 ∧ E255 and uniform fibre size m;
L7 gives Fib, e, c with Eq4 (and E677 on the product by L3 transported along e);
¬E255 opN gives a point failing E255, transported by e to some (a,σ) and by L4 to (i);
for (ii): if opB a a = a then by L6 the operation c a a satisfies E677 on Fib and E255 fails
for c a a at σ, so (Fib, c a a) is a counterexample of cardinality m < |N| — contradicting
minimality (transport it to Fin m to match L8's hypothesis form).

## Deliverables
`lean/etp677_ext/Ext677Glue.lean` (library root), `lake build` clean, `#print axioms` appended
to AXIOMS.txt (only propext / Classical.choice / Quot.sound), and
`engine/out/codex/etp677_lean_L9_report.md` with the exact statement, deviations, build
tail, ending with DONE-LEANGLUE. If (ii) resists, deliver (i) and say so.
