# CODEX TICKET (sol tier, Lean 4 + Mathlib) — certify the collision-structure lemmas of the
# (S) attack (rounds 1–2) as Lean theorems. Repo: $HOME/workspace/claudecode/automath;
# project lean/etp677_ext/ (reuse Ext677.lean: E677, ldiv, L1). English. lake build only.
# Time box 3 h. Sources of the informal proofs: problems/etp677/S_attack_codex/notes.md and
# problems/etp677/S_attack_codex/round2/notes.md (read them; formalize, do not re-invent).

## Definitions (finite carrier M, op with E677; use `Finset`/`Fintype` as convenient)
- collision relation: `Rho a b := ∃ t, op a t = op b t` (reflexive, symmetric);
- `F a b := {t | op a t = op b t}` (Finset), `N t v := #{a | op a t = v}`;
- `RhoStar := Relation.TransGen Rho` (or `EqvGen`); (B) := RhoStar is a congruence:
  `RhoStar a b → RhoStar (op c a) (op c b) ∧ RhoStar (op a c) (op b c)`.

## Theorems
C1 (Collision Second-Moment Lemma) `Σ_{t,v} (N t v)^2 = n^2 + 2 * Σ_{a<b} |F a b|`, with
   `n = Fintype.card M` (formulate with an ordered double sum `Σ_{a ≠ b}|F a b|` to avoid the
   `<`; state the unordered form as a corollary if a linear order is available).
   Corollary: if `∀ a b, a ≠ b → Rho a b` (universal ϱ) then `Σ_{t,v} (N t v)^2 ≥ 2n^2 − n`,
   with equality iff every `|F a b| = 1` for `a ≠ b`.
C2 (Generator Transport Criterion) (B) ↔ [∀ a b c, Rho a b → RhoStar (op c a) (op c b) ∧
   RhoStar (op a c) (op b c)]. (Proof: induction on the transitive chain.)
C3 (Connectedness) `(∀ a b, RhoStar a b)` ↔ the collision graph is connected — if you
   formalize RhoStar as TransGen of the symmetric Rho this is definitional; then state the
   useful contrapositive: `(∃ a b, ¬ RhoStar a b)` ↔ there is a proper non-empty subset S
   closed under Rho.
C4 (KEY Certificate Bijection) with `Xi t x := ldiv x (ldiv t x)` and E677 (hence KEY:
   `op (op y x) y = ldiv x (ldiv y x)`, already `key_identity` in Ext677.lean):
   the map `(a, b, t) ↦ (ldiv t a, ldiv t b, t)` is a bijection from
   `{(a,b,t) | a ≠ b ∧ op a t = op b t}` onto `{(x,y,t) | x ≠ y ∧ Xi t x = Xi t y}`, with
   inverse `(x,y,t) ↦ (op t x, op t y, t)`.
   Corollary (Common-Certificate Double Count): `Σ_{t,v} (E t v)^2 = n^2 + Σ_{x ≠ y} C x y`
   where `E t v := #{x | Xi t x = v}` and `C x y := #{t | Xi t x = Xi t y}`; and under (N)
   [`∀ t v, N t v = E t v`] the two second moments coincide.
C5 (N is a theorem of E677 — toolkit (R9-E/N-is-B3)): `∀ t v, N t v = #{x | op t (op x v) = x}`
   — prove it in Lean (proof in the toolkit: a ↦ t\a bijection + KEY). If time is short,
   deliver C1–C4 first.

## Deliverables
`lean/etp677_ext/Ext677Collision.lean` (library root added to lakefile), `lake build` clean,
`#print axioms` for every theorem appended to AXIOMS.txt (only propext / Classical.choice /
Quot.sound), and `engine/out/codex/etp677_lean_collision_report.md` with exact statements,
deviations, build tail, ending with DONE-LEANCOLL.
