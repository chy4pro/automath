# CODEX TICKET (sol tier, Lean 4 + Mathlib) — L10 occurrence trichotomy, L11 small-order
# nonexistence + idempotent-free quotient corollary. Repo: $HOME/workspace/claudecode/
# automath; project lean/etp677_ext/ (Ext677.lean L1–L6, Ext677Quot.lean, Ext677Glue.lean,
# Ext677Collision.lean exist — reuse). English. lake build only. Time box 2.5 h.

## L10 (R7-B Theorem 0, occurrence trichotomy) — for any finite E677 magma B with E255
For a : B let x_a := (a*a)*a (the unique left unit, `left_unit_unique` exists). Define the
four subscript maps of eq.(4) on base pairs: P1(x,y) = (y, y\x), P2(x,y) = (x, (y*x)*y),
P3(x,y) = (y,x), P4(x,y) = (y*x, y). Prove:
 (a) each Pi is a bijection B×B → B×B (P1, P2, P4 via L1; P3 swap);
 (b) if a*a = a then P1(a,a) = P2(a,a) = P3(a,a) = P4(a,a) = (a,a) (four-fold collapse);
 (c) if a*a ≠ a then the pair (x_a, a) occurs as P1 and as P3 of the SAME instance
     (a, x_a) [P1(a,x_a) = (x_a, x_a\a) = (x_a, a) since x_a*a = a; P3(a,x_a) = (x_a,a)],
     and as P2 of exactly one other instance and as P4 of exactly one other instance,
     these three instances being pairwise distinct; i.e. the multiset of occurrences of
     (x_a,a) over the four positions and all instances has exactly three instances with
     the {1,3} collision. State it as: the set {(x,y,i) | Pi(x,y) = (x_a,a)} has cardinality
     4 and projects onto exactly 3 distinct instances (x,y).

## L11 (small orders + idempotent-free quotient)
 (a) `no_E677_Fin2 : ∀ op : Fin 2 → Fin 2 → Fin 2, ¬ E677 op` and the same for Fin 3, by
     `decide` (finite quantification over all tables: 2^4 and 3^9 tables; if `decide` is
     slow for Fin 3, a `native_decide` fallback is acceptable ONLY if labelled — record axioms).
 (b) Corollary (Prop 0): in the setting of L7 (surjective hom f : N → B of finite E677
     magmas with all fibres of size m ∈ {2,3}), B has no idempotent: for an idempotent a,
     L6 makes `c a a` an E677 operation on Fib with Nat.card Fib = m, contradicting (a)
     after transport to Fin m.
 (c) (optional) With L7/L8 phrasing: if a finite E677 magma N has a congruence all of whose
     classes have cardinality 2 or 3, the quotient is idempotent-free.

## Deliverables
`lean/etp677_ext/Ext677Occ.lean` (L10) and `Ext677Small.lean` (L11), library roots, `lake
build` clean, `#print axioms` appended to AXIOMS.txt (propext / Classical.choice / Quot.sound;
any native_decide use labelled), and `engine/out/codex/etp677_lean_L10L11_report.md` with
exact statements, deviations, build tail, ending with DONE-LEANOCC.
