import Ext677
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic

/-!
# Switching constructions over `ZMod 7`
-/

namespace Ext677

universe u

/-- The switching product with base operation `4q+r`. -/
def switchOp {X : Type u} (star circ : X → X → X) :
    ZMod 7 × X → ZMod 7 × X → ZMod 7 × X
  | (q, s), (r, t) =>
      (4 * q + r, if q = 0 ∧ r = 0 then circ s t else star s t)

/-- The rotating switching product with base operation `4q+3r`. -/
def rotatingSwitchOp {X : Type u} (star circ : X → X → X) :
    ZMod 7 × X → ZMod 7 × X → ZMod 7 × X
  | (q, s), (r, t) =>
      (4 * q + 3 * r, if q = 0 ∧ r = 0 then circ s t else star s t)

/-- In a non-hub E677 instance for `4q+r`, none of its four products uses the hub block. -/
theorem switch_isolation : ∀ q r : ZMod 7, ¬ (q = 0 ∧ r = 0) →
    ¬ (r = 0 ∧ q = 0) ∧
    ¬ (4 * r + q = 0 ∧ r = 0) ∧
    ¬ (q = 0 ∧ 4 * (4 * r + q) + r = 0) ∧
    ¬ (r = 0 ∧ 4 * q + (4 * (4 * r + q) + r) = 0) := by
  decide

/-- In a non-hub E677 instance for `4q+3r`, none of its four products uses the hub block. -/
theorem rotating_switch_isolation : ∀ q r : ZMod 7, ¬ (q = 0 ∧ r = 0) →
    ¬ (r = 0 ∧ q = 0) ∧
    ¬ (4 * r + 3 * q = 0 ∧ r = 0) ∧
    ¬ (q = 0 ∧ 4 * (4 * r + 3 * q) + 3 * r = 0) ∧
    ¬ (r = 0 ∧ 4 * q + 3 * (4 * (4 * r + 3 * q) + 3 * r) = 0) := by
  decide

/-- The diagonal base equality for the `4q+r` base has only the hub solution. -/
theorem switch_base_idempotent_iff (q : ZMod 7) : 4 * q + q = q ↔ q = 0 := by
  revert q
  decide

/-- The diagonal base equality for the `4q+3r` base has only the hub solution. -/
theorem rotating_switch_base_idempotent_iff (q : ZMod 7) :
    4 * q + 3 * q = q ↔ q = 0 := by
  revert q
  decide

/-- The `4q+r` base operation satisfies E677 (a 49-case finite certificate). -/
theorem switch_base_E677_eval : ∀ q r : ZMod 7,
    q = 4 * r + (4 * q + (4 * (4 * r + q) + r)) := by
  decide

/-- The `4q+r` base operation satisfies E255. -/
theorem switch_base_E255_eval : ∀ q : ZMod 7,
    q = 4 * (4 * (4 * q + q) + q) + q := by
  decide

/-- The `4q+3r` base operation satisfies E677 (a 49-case finite certificate). -/
theorem rotating_switch_base_E677_eval : ∀ q r : ZMod 7,
    q = 4 * r + 3 * (4 * q + 3 * (4 * (4 * r + 3 * q) + 3 * r)) := by
  decide

/-- The `4q+3r` base operation satisfies E255. -/
theorem rotating_switch_base_E255_eval : ∀ q : ZMod 7,
    q = 4 * (4 * (4 * q + 3 * q) + 3 * q) + 3 * q := by
  decide

/-- S1: switching two E677 operations over the base `4q+r` preserves E677. -/
theorem switch_E677 {X : Type u} (star circ : X → X → X)
    (hstar : E677 star) (hcirc : E677 circ) : E677 (switchOp star circ) := by
  rintro ⟨q, s⟩ ⟨r, t⟩
  by_cases hzero : q = 0 ∧ r = 0
  · rcases hzero with ⟨rfl, rfl⟩
    apply Prod.ext
    · norm_num [switchOp]
    · simpa [switchOp] using hcirc s t
  · rcases switch_isolation q r hzero with ⟨h₁, h₂, h₃, h₄⟩
    apply Prod.ext
    · simp only [switchOp]
      exact switch_base_E677_eval q r
    · simpa only [switchOp, h₁, h₂, h₃, h₄, ite_false] using hstar s t

/-- S2: switching two E255 operations over the base `4q+r` preserves E255. -/
theorem switch_E255 {X : Type u} (star circ : X → X → X)
    (hstar : E255 star) (hcirc : E255 circ) : E255 (switchOp star circ) := by
  rintro ⟨q, s⟩
  by_cases hq : q = 0
  · subst q
    apply Prod.ext
    · norm_num [E255At, switchOp]
    · simpa [E255At, switchOp] using hcirc s
  · apply Prod.ext
    · simp only [switchOp]
      simpa only using switch_base_E255_eval q
    · simpa [E255At, switchOp, hq] using hstar s

/-- S3: idempotents of the switched product lie exactly in the hub fibre. -/
theorem switch_idempotent_iff {X : Type u} (star circ : X → X → X)
    (q : ZMod 7) (s : X) :
    switchOp star circ (q, s) (q, s) = (q, s) ↔ q = 0 ∧ circ s s = s := by
  constructor
  · intro h
    have hq : q = 0 := (switch_base_idempotent_iff q).1 (congrArg Prod.fst h)
    refine ⟨hq, ?_⟩
    subst q
    simpa [switchOp] using congrArg Prod.snd h
  · rintro ⟨rfl, hs⟩
    apply Prod.ext
    · norm_num [switchOp]
    · simpa [switchOp] using hs

/-- S4.1: rotating switching preserves E677. -/
theorem rotating_switch_E677 {X : Type u} (star circ : X → X → X)
    (hstar : E677 star) (hcirc : E677 circ) : E677 (rotatingSwitchOp star circ) := by
  rintro ⟨q, s⟩ ⟨r, t⟩
  by_cases hzero : q = 0 ∧ r = 0
  · rcases hzero with ⟨rfl, rfl⟩
    apply Prod.ext
    · norm_num [rotatingSwitchOp]
    · simpa [rotatingSwitchOp] using hcirc s t
  · rcases rotating_switch_isolation q r hzero with ⟨h₁, h₂, h₃, h₄⟩
    apply Prod.ext
    · simp only [rotatingSwitchOp]
      exact rotating_switch_base_E677_eval q r
    · simpa only [rotatingSwitchOp, h₁, h₂, h₃, h₄, ite_false] using hstar s t

/-- S4.2: rotating switching preserves E255. -/
theorem rotating_switch_E255 {X : Type u} (star circ : X → X → X)
    (hstar : E255 star) (hcirc : E255 circ) : E255 (rotatingSwitchOp star circ) := by
  rintro ⟨q, s⟩
  by_cases hq : q = 0
  · subst q
    apply Prod.ext
    · norm_num [E255At, rotatingSwitchOp]
    · simpa [E255At, rotatingSwitchOp] using hcirc s
  · apply Prod.ext
    · simp only [rotatingSwitchOp]
      simpa only using rotating_switch_base_E255_eval q
    · simpa [E255At, rotatingSwitchOp, hq] using hstar s

/-- S4.3: idempotents of the rotating switched product also lie exactly in the hub fibre. -/
theorem rotating_switch_idempotent_iff {X : Type u} (star circ : X → X → X)
    (q : ZMod 7) (s : X) :
    rotatingSwitchOp star circ (q, s) (q, s) = (q, s) ↔
      q = 0 ∧ circ s s = s := by
  constructor
  · intro h
    have hq : q = 0 :=
      (rotating_switch_base_idempotent_iff q).1 (congrArg Prod.fst h)
    refine ⟨hq, ?_⟩
    subst q
    simpa [rotatingSwitchOp] using congrArg Prod.snd h
  · rintro ⟨rfl, hs⟩
    apply Prod.ext
    · norm_num [rotatingSwitchOp]
    · simpa [rotatingSwitchOp] using hs

#print axioms switch_isolation
#print axioms rotating_switch_isolation
#print axioms switch_base_idempotent_iff
#print axioms rotating_switch_base_idempotent_iff
#print axioms switch_base_E677_eval
#print axioms switch_base_E255_eval
#print axioms rotating_switch_base_E677_eval
#print axioms rotating_switch_base_E255_eval
#print axioms switch_E677
#print axioms switch_E255
#print axioms switch_idempotent_iff
#print axioms rotating_switch_E677
#print axioms rotating_switch_E255
#print axioms rotating_switch_idempotent_iff

end Ext677
