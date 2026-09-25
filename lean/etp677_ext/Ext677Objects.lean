import Ext677Window
import Mathlib.Tactic

/-!
# Two explicit order-217 E677 magmas

The operations are presented directly on `ZMod 7 × ZMod 31`. The large
universal identities are certified by native evaluation. All named point
computations use kernel reduction and explicit witnesses for left division.
-/

namespace Ext677

open Function

/-- The underlying set of both order-217 examples. -/
abbrev Obj217 := ZMod 7 × ZMod 31

/-- The fibre operation used as a control in the two examples. -/
def F31 (s t : ZMod 31) : ZMod 31 := 5 * s - 4 * t + 1

/-- The order-217 window example `M217ε`. -/
def M217ε : Obj217 → Obj217 → Obj217
  | (q, s), (r, t) =>
      (4 * q + r, 5 * s - 4 * t + if q = 0 ∧ r = 0 then 1 else 0)

/-- The order-217 example `R217`. -/
def R217 : Obj217 → Obj217 → Obj217
  | (q, s), (r, t) =>
      (4 * q + 3 * r, 5 * s - 4 * t + if q = 0 ∧ r = 0 then 1 else 0)

/-! ## Global finite certificates -/

theorem M217ε_E677 : E677 M217ε := by
  unfold E677
  native_decide
set_option maxRecDepth 10000 in
theorem M217ε_E255 : E255 M217ε := by
  unfold E255 E255At
  decide
set_option maxRecDepth 10000 in
theorem M217ε_no_idempotent : ∀ x, M217ε x x ≠ x := by decide

theorem M217ε_left_bijective (x : Obj217) : Function.Bijective (M217ε x) :=
  L1_left_bij M217ε M217ε_E677 x

theorem R217_E677 : E677 R217 := by
  unfold E677
  native_decide
set_option maxRecDepth 10000 in
theorem R217_E255 : E255 R217 := by
  unfold E255 E255At
  decide
set_option maxRecDepth 10000 in
theorem R217_no_idempotent : ∀ x, R217 x x ≠ x := by decide

theorem R217_left_bijective (x : Obj217) : Function.Bijective (R217 x) :=
  L1_left_bij R217 R217_E677 x

/-! ## The window in `M217ε` -/

def M217εa : Obj217 := (1, 0)

private theorem M217ε_div₁ :
    ldiv M217ε M217ε_E677 M217εa M217εa = (4, 0) := by
  symm
  apply ldiv_unique M217ε M217ε_E677
  decide

private theorem M217ε_div₂ :
    ldiv M217ε M217ε_E677 M217εa (4, 0) = (0, 0) := by
  symm
  apply ldiv_unique M217ε M217ε_E677
  decide

private theorem M217ε_div₃ :
    ldiv M217ε M217ε_E677 M217εa (0, 0) = (3, 0) := by
  symm
  apply ldiv_unique M217ε M217ε_E677
  decide

private theorem M217ε_div₄ :
    ldiv M217ε M217ε_E677 M217εa (3, 0) = (6, 0) := by
  symm
  apply ldiv_unique M217ε M217ε_E677
  decide

/-- Explicit kernel-checked coordinates of the seven requested `M217ε` terms. -/
theorem M217ε_window_coordinates :
    L13W M217ε M217εa = (4, 0) ∧
    L13U M217ε M217εa = (0, 0) ∧
    L13P M217ε M217ε_E677 M217εa = (3, 0) ∧
    L13B M217ε M217ε_E677 M217εa = (6, 0) ∧
    L13D M217ε M217ε_E677 M217εa = (2, 0) ∧
    M217ε M217εa M217εa = (5, 0) := by
  have hu : L13U M217ε M217εa = (0, 0) := by decide
  have hp : L13P M217ε M217ε_E677 M217εa = (3, 0) := by
    simp only [L13P, hu, M217ε_div₃]
  have hb : L13B M217ε M217ε_E677 M217εa = (6, 0) := by
    simp only [L13B, hp, M217ε_div₄]
  refine ⟨by decide, hu, hp, hb, ?_, by decide⟩
  simp only [L13D, hb]
  decide

/-- In the window notation, `b = F(a)` has the advertised coordinate. -/
theorem M217ε_F_coordinate : L12F M217ε M217ε_E677 M217εa = (6, 0) := by
  rw [← X3_b_eq_F M217ε M217ε_E677 M217εa]
  exact M217ε_window_coordinates.2.2.2.1

/-- At `(1,0)`, `M217ε` is a window and is not idempotent. -/
theorem M217ε_window :
    WindowPred M217ε M217ε_E677 M217εa ∧
      M217ε M217εa M217εa ≠ M217εa := by
  rcases M217ε_window_coordinates with ⟨hw, hu, hp, hb, hd, haa⟩
  have hv : L13V M217ε M217ε_E677 M217εa = (0, 0) := by
    simp only [L13V, hd, hb]
    decide
  have hc : L13C M217ε M217ε_E677 M217εa = (3, 0) := by
    simp only [L13C, hb, hv]
    decide
  exact ⟨⟨hv.trans hu.symm, hc.trans hp.symm⟩, by rw [haa]; decide⟩

/-- The seven requested `M217ε` elements are pairwise distinct. -/
theorem M217ε_seven_nodup :
    List.Nodup
      [M217εa, L13W M217ε M217εa, L13U M217ε M217εa,
        L13P M217ε M217ε_E677 M217εa,
        L13B M217ε M217ε_E677 M217εa,
        L13D M217ε M217ε_E677 M217εa,
        M217ε M217εa M217εa] := by
  rcases M217ε_window_coordinates with ⟨hw, hu, hp, hb, hd, haa⟩
  simp only [hw, hu, hp, hb, hd, haa]
  decide

/-! ## The two requested points in `R217` -/

theorem R217_U_bijective : Function.Bijective (X6U R217) := by native_decide

def R217a : Obj217 := (1, 0)

private theorem R217a_div₁ :
    ldiv R217 R217_E677 R217a R217a = (6, 0) := by
  symm
  apply ldiv_unique R217 R217_E677
  decide

private theorem R217a_div₂ :
    ldiv R217 R217_E677 R217a (6, 0) = (3, 0) := by
  symm
  apply ldiv_unique R217 R217_E677
  decide

private theorem R217a_div₃ :
    ldiv R217 R217_E677 R217a (3, 0) = (2, 0) := by
  symm
  apply ldiv_unique R217 R217_E677
  decide

private theorem R217a_div₄ :
    ldiv R217 R217_E677 R217a (2, 0) = (4, 0) := by
  symm
  apply ldiv_unique R217 R217_E677
  decide

/-- At `(1,0)` in `R217`, `c=u`, while the point is not idempotent. -/
theorem R217_collision_at_one :
    L13C R217 R217_E677 R217a = L13U R217 R217a ∧
      R217 R217a R217a ≠ R217a := by
  have hu : L13U R217 R217a = (3, 0) := by decide
  have hp : L13P R217 R217_E677 R217a = (2, 0) := by
    simp only [L13P, hu, R217a_div₃]
  have hb : L13B R217 R217_E677 R217a = (4, 0) := by
    simp only [L13B, hp, R217a_div₄]
  have hd : L13D R217 R217_E677 R217a = (0, 0) := by
    simp only [L13D, hb]
    decide
  have hv : L13V R217 R217_E677 R217a = (5, 0) := by
    simp only [L13V, hd, hb]
    decide
  have hc : L13C R217 R217_E677 R217a = (3, 0) := by
    simp only [L13C, hb, hv]
    decide
  exact ⟨hc.trans hu.symm, by decide⟩

/-- The same collision written exactly as `W(F(a)) = U(a)`. -/
theorem R217_WF_eq_U_at_one :
    X6W R217 (L12F R217 R217_E677 R217a) = X6U R217 R217a := by
  rw [← X3_b_eq_F R217 R217_E677 R217a,
    ← X3_c_eq_W_b R217 R217_E677 R217a,
    ← X3_u_eq_U R217 R217a]
  exact R217_collision_at_one.1

def R217zero : Obj217 := (0, 0)

private theorem R217zero_div₁ :
    ldiv R217 R217_E677 R217zero R217zero = (0, 8) := by
  symm
  apply ldiv_unique R217 R217_E677
  decide

private theorem R217zero_div₂ :
    ldiv R217 R217_E677 R217zero (0, 8) = (0, 6) := by
  symm
  apply ldiv_unique R217 R217_E677
  decide

private theorem R217zero_div₃ :
    ldiv R217 R217_E677 R217zero (0, 6) = (0, 22) := by
  symm
  apply ldiv_unique R217 R217_E677
  decide

private theorem R217zero_div₄ :
    ldiv R217 R217_E677 R217zero (0, 22) = (0, 18) := by
  symm
  apply ldiv_unique R217 R217_E677
  decide

/-- The six `X_6` disequalities hold at `(0,0)` in `R217`. -/
theorem R217_X6_at_zero : L14X6 R217 R217_E677 R217zero := by
  have hu : L13U R217 R217zero = (0, 6) := by decide
  have hw : L13W R217 R217zero = (0, 8) := by decide
  have hp : L13P R217 R217_E677 R217zero = (0, 22) := by
    simp only [L13P, hu, R217zero_div₃]
  have hb : L13B R217 R217_E677 R217zero = (0, 18) := by
    simp only [L13B, hp, R217zero_div₄]
  have hd : L13D R217 R217_E677 R217zero = (0, 19) := by
    simp only [L13D, hb]
    decide
  have hv : L13V R217 R217_E677 R217zero = (0, 24) := by
    simp only [L13V, hd, hb]
    decide
  have hc : L13C R217 R217_E677 R217zero = (0, 26) := by
    simp only [L13C, hb, hv]
    decide
  unfold L14X6
  rw [hv, hw, hu, hc, hp]
  decide

#print axioms M217ε_E677
#print axioms M217ε_E255
#print axioms M217ε_no_idempotent
#print axioms M217ε_left_bijective
#print axioms M217ε_window
#print axioms M217ε_F_coordinate
#print axioms M217ε_seven_nodup
#print axioms R217_E677
#print axioms R217_E255
#print axioms R217_no_idempotent
#print axioms R217_left_bijective
#print axioms R217_U_bijective
#print axioms R217_collision_at_one
#print axioms R217_WF_eq_U_at_one
#print axioms R217_X6_at_zero

end Ext677
