# CODEX TICKET (sol tier, Lean 4, 3 h) — formalize the shape-only Core-7 theorem: no
# fourteen permutation-row operations on Fin 3 satisfy the seven eq.(4) instances.
# Repo: $HOME/workspace/claudecode/automath; project lean/etp677_ext/ (Mathlib
# available; for finite case analysis prefer `decide` on small enumerations; `native_decide`
# only as a labelled fallback). English. Sources: problems/etp677/ext/fibre3/proof/proof.md
# (the human proof: collision instances force the third op; 252 triples in five orbits;
# bridge eliminations 0,0,6,0,0; the endgame), fibre3/proof/check_*.py (the checkers).

## Statement to prove (self-contained, no base magma needed)
Let Row := Fin 3 → Fin 3 with the predicate "bijective", and an operation be a map
Fin 3 → Row (row s = the permutation t ↦ s <> t). Fourteen operations A B C D E F G H I J K L
M0 N (names as in proof.md). Define
  E(P,Q,R,S) := ∀ s t, P t (Q s (S (R t s) t)) = s
(eq.(1) of proof.md: P_t(Q_s(S_{R_t(s)}(t))) = s). THEOREM core7:
  ¬ ∃ (A … N : Fin 3 → Fin 3 → Fin 3) (all rows bijective),
      E(A,B,C,D) ∧ E(E,F,G,H) ∧ E(I,J,K,L) ∧ E(D,M0,D,N) ∧ E(F,K,F,I) ∧ E(H,L,A,B) ∧ E(K,I,L,E).
Check the seven quadruples against proof.md's list (2) BEFORE proving anything, and record
the check in the report.

## Suggested route (mirror the human proof; each finite step by `decide` over S_3-valued data)
 1. Collision lemma: E(X,Y,X,Z) determines Z from (X,Y): Z (X_t s) t = Y_s^{-1}(X_t^{-1} s).
    Prove as a general lemma over Fin 3 (or over any Fintype with bijective rows).
 2. The 252 valid (X,Y,Z) collision triples and their five fibre-coordinate orbits: rather
    than orbits, let `decide` enumerate: the set of (X,Y) with all rows bijective is
    6^3 × 6^3 = 46,656 pairs — too many for one `decide`? Use the structure: quantify over
    X's rows and Y's rows (each ∈ S_3, represented as Fin 6 via `Equiv.Perm (Fin 3)`), and
    let the kernel check the derived constraints per case; if a single `decide` is too slow,
    split into lemmas by the orbit representative (five cases) with `decide` per case.
 3. Bridge instances: with (D,M0,N) and (F,K,I) forced by the collisions, the instances
    E(A,B,C,D), E(E,F,G,H), E(I,J,K,L) — derive the constraints proof.md states (survivor
    counts 0,0,6,0,0 per type) by `decide` on the relevant rows.
 4. Endgame: E(H,L,A,B) and E(K,I,L,E) → L_s = ℓ, H_s = ℓ^{-1}, B Latin, D_r(t) = t,
    contradiction with the first collision. Follow proof.md sections.
If a full kernel proof is out of reach in 3 h, deliver: the collision lemma (general),
and as much of the chain as closes, with the remaining steps stated as `sorry`-FREE
hypotheses (i.e. theorems conditional on explicit finite facts) plus a `native_decide`
check of those facts, clearly labelled.

## Deliverables
`lean/etp677_ext/Ext677Core7.lean` (root), `lake build` clean, `#print axioms` for every
theorem appended to AXIOMS.txt (native_decide uses labelled), and
`engine/out/codex/etp677_lean_core7_report.md` ending with DONE-LEANCORE7.
