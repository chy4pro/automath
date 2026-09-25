# CODEX TICKET (sol tier, Lean 4 + Mathlib) — L14 distinctness package, L15 the seven pattern
# pairs' subscripts. Repo: $HOME/workspace/claudecode/automath; project
# lean/etp677_ext/ (reuse Ext677Pattern.lean: L12F/L12H, L13U/P/B/D/V/C/W, L13_* identities,
# cycle lemmas; Ext677.lean: ldiv, key_identity; Ext677Occ.lean: subscript maps). English.
# lake build only. Time box 2.5 h. Informal source: engine/out/codex/
# etp677_pattern_existence_report.md + problems/etp677/ext/fibre3/pattern/notes.md.

## L15 (equational; do this FIRST — it is the load-bearing link)
For a finite E677+E255 magma and a : M, with u,p,b,d,v,c,w as in L13, prove that the
eq.(4) subscript quadruples (P1,P2,P3,P4) = ((y, y\x), (x, (y*x)*y), (y,x), (y*x, y)) at the
seven base pairs are EXACTLY:
  (p,a) ↦ ((a,b),(p,a),(a,p),(u,a));   (v,d) ↦ ((d,b),(v,b),(d,v),(a,d));
  (c,b) ↦ ((b,v),(c,d),(b,c),(b,b));   (a,u) ↦ ((u,a),(a,w),(u,a),(a,u));
  (b,v) ↦ ((v,b),(b,c),(v,b),(b,v));   (b,a) ↦ ((a,d),(b,b),(a,b),(p,a));
  (b,b) ↦ ((b,c),(b,v),(b,b),(d,b)).
(Each entry is an equation between terms, e.g. at (p,a): P1 = (a, a\p) = (a,b) by definition
of b; P2 = (p, (a*p)*a) and (a*p)*a = a by KEY … — derive each from the L13 identities and
KEY; state one theorem per pair, or one theorem with 28 conjuncts.)

## L14 (distinctness; idempotent-free hypothesis `∀ x, op x x ≠ x`)
Prove the AUTOMATIC inequalities among the eight terms (a,u,p,b,v,c,d,w) under E677 + E255 +
idempotent-free: the report states that all distinctness relations other than the six
X_6(a) := [v≠w, v≠u, c≠a, c≠w, c≠u, c≠p] are automatic, using the cycle facts (no exact
L-cycle of length 1 (idempotent-free), 2, 3, 4, 5 — note length 4 is in the toolkit as (Cyc)
but NOT yet in Lean: prove `L12_no_exact_cycle_four` too, from E677 (toolkit (Cyc): m = 4
forces E255 to fail at y, so under E255 it is excluded — prove that version) — and left
cancellation. Deliver as many of the 22 inequalities as you can prove, each a separate
theorem `L14_<x>_ne_<y>`; list the ones you could not prove. Then the package theorem:
`X6 a → (the eight terms are pairwise distinct)` for the proved subset.

## Deliverables
`lean/etp677_ext/Ext677PatternPairs.lean` (root), `lake build` clean, `#print axioms` appended
to AXIOMS.txt (propext / Classical.choice / Quot.sound only), and
`engine/out/codex/etp677_lean_L14L15_report.md` ending with DONE-LEANPAIRS.
