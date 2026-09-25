import Ext677PatternPairs
import Mathlib.Tactic

/-!
# X6 equalizer reductions
-/

namespace Ext677

open Function

universe u

/-! ## X1: iterate forms -/

/-- `U(x) = (x*x)*x`. -/
def X6U {M : Type u} (op : M → M → M) (x : M) : M :=
  op (op x x) x

/-- `W(x) = x*U(x)`. -/
def X6W {M : Type u} (op : M → M → M) (x : M) : M :=
  op x (X6U op x)

/-- `P(x) = x\U(x)`. -/
noncomputable def X6P {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (x : M) : M :=
  ldiv op h677 x (X6U op x)

/-- X1: `U(x)` is the second inverse iterate. -/
theorem X1_U_iterate {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (x : M) :
    X6U op x = ldiv op h677 x (ldiv op h677 x x) :=
  diagonal_candidate op h677 x

/-- X1: `W(x)` is a right unit for `x`. -/
theorem X1_W_right_unit {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (x : M) : op x (X6W op x) = x := by
  change op x (op x (X6U op x)) = x
  rw [X1_U_iterate op h677 x,
    op_ldiv op h677 x (ldiv op h677 x x), op_ldiv op h677 x x]

/-- X1: `W(x)` is the first inverse iterate. -/
theorem X1_W_iterate {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (x : M) : X6W op x = ldiv op h677 x x :=
  ldiv_unique op h677 (X1_W_right_unit op h677 x)

/-- X1: `P(x)` is the third inverse iterate. -/
theorem X1_P_iterate {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (x : M) :
    X6P op h677 x =
      ldiv op h677 x (ldiv op h677 x (ldiv op h677 x x)) := by
  rw [X6P, X1_U_iterate op h677 x]

/-- X1: `F(x) = x\P(x)`, hence is the fourth inverse iterate. -/
theorem X1_F_iterate {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (x : M) :
    L12F op h677 x = ldiv op h677 x (X6P op h677 x) := by
  rw [X6P, X1_U_iterate op h677 x]
  rfl

/-! ## X2: fixed points of F -/

/-- X2: `F(x)` fixes exactly the idempotent elements. -/
theorem X2_F_fixed_iff_idempotent {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (h255 : E255 op) (x : M) :
    L12F op h677 x = x ↔ op x x = x := by
  constructor
  · intro hF
    have hinv : (ldiv op h677 x)^[4] x = x := by
      simpa only [L12F, Function.iterate_succ_apply, Function.iterate_zero_apply] using hF
    have hright : Function.RightInverse (ldiv op h677 x) (op x) :=
      fun y => op_ldiv op h677 x y
    have hfour : Lpow op x 4 = x := by
      change (op x)^[4] x = x
      calc
        (op x)^[4] x = (op x)^[4] ((ldiv op h677 x)^[4] x) := by rw [hinv]
        _ = x := hright.iterate 4 x
    by_contra hnonidem
    have hone : Lpow op x 1 ≠ x := by
      simpa only [Lpow, Function.iterate_succ_apply, Function.iterate_zero_apply]
        using hnonidem
    have htwo : Lpow op x 2 ≠ x := by
      intro htwoFix
      apply L12_no_exact_cycle_two op h677 x
      refine ⟨htwoFix, ?_⟩
      intro k hk hkpos
      interval_cases k
      exact hone
    have hthree : Lpow op x 3 ≠ x := by
      intro hthreeFix
      apply L12_no_exact_cycle_three op h677 x
      refine ⟨hthreeFix, ?_⟩
      intro k hk hkpos
      interval_cases k <;> assumption
    apply L12_no_exact_cycle_four op h677 h255 x
    refine ⟨hfour, ?_⟩
    intro k hk hkpos
    interval_cases k <;> assumption
  · intro hxx
    have hd : ldiv op h677 x x = x := (ldiv_unique op h677 hxx).symm
    simp only [L12F, hd]

/-! ## X3: pattern coordinates and equalizers -/

/-- X3: `b = F(a)`. -/
theorem X3_b_eq_F {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (a : M) : L13B op h677 a = L12F op h677 a := by
  change ldiv op h677 a (ldiv op h677 a (L13U op a)) = L12F op h677 a
  rw [show L13U op a = X6U op a from rfl, X1_U_iterate op h677 a]
  rfl

/-- X3: `v = U(b)`. -/
theorem X3_v_eq_U_b {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (a : M) :
    L13V op h677 a = X6U op (L13B op h677 a) := rfl

/-- X3: `c = W(b)`. -/
theorem X3_c_eq_W_b {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (a : M) :
    L13C op h677 a = X6W op (L13B op h677 a) := rfl

/-- X3: `u = U(a)`. -/
theorem X3_u_eq_U {M : Type u} (op : M → M → M) (a : M) :
    L13U op a = X6U op a := rfl

/-- X3: `w = W(a)`. -/
theorem X3_w_eq_W {M : Type u} (op : M → M → M) (a : M) :
    L13W op a = X6W op a := rfl

/-- X3: `p = P(a)`. -/
theorem X3_p_eq_P {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (a : M) : L13P op h677 a = X6P op h677 a := rfl

/-- X3: `d = b*b`. -/
theorem X3_d_eq_b_square {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (a : M) :
    L13D op h677 a = op (L13B op h677 a) (L13B op h677 a) := rfl

/-- X3 equalizer: `v ≠ w`. -/
theorem X3_v_ne_w_iff {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (a : M) :
    L13V op h677 a ≠ L13W op a ↔
      X6U op (L12F op h677 a) ≠ X6W op a := by
  rw [X3_v_eq_U_b op h677 a, X3_b_eq_F op h677 a, X3_w_eq_W op a]

/-- X3 equalizer: `v ≠ u`. -/
theorem X3_v_ne_u_iff {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (a : M) :
    L13V op h677 a ≠ L13U op a ↔
      X6U op (L12F op h677 a) ≠ X6U op a := by
  rw [X3_v_eq_U_b op h677 a, X3_b_eq_F op h677 a, X3_u_eq_U op a]

/-- X3 equalizer: `c ≠ a`. -/
theorem X3_c_ne_a_iff {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (a : M) :
    L13C op h677 a ≠ a ↔ X6W op (L12F op h677 a) ≠ a := by
  rw [X3_c_eq_W_b op h677 a, X3_b_eq_F op h677 a]

/-- X3 equalizer: `c ≠ w`. -/
theorem X3_c_ne_w_iff {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (a : M) :
    L13C op h677 a ≠ L13W op a ↔
      X6W op (L12F op h677 a) ≠ X6W op a := by
  rw [X3_c_eq_W_b op h677 a, X3_b_eq_F op h677 a, X3_w_eq_W op a]

/-- X3 equalizer: `c ≠ u`. -/
theorem X3_c_ne_u_iff {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (a : M) :
    L13C op h677 a ≠ L13U op a ↔
      X6W op (L12F op h677 a) ≠ X6U op a := by
  rw [X3_c_eq_W_b op h677 a, X3_b_eq_F op h677 a, X3_u_eq_U op a]

/-- X3 equalizer: `c ≠ p`. -/
theorem X3_c_ne_p_iff {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (a : M) :
    L13C op h677 a ≠ L13P op h677 a ↔
      X6W op (L12F op h677 a) ≠ X6P op h677 a := by
  rw [X3_c_eq_W_b op h677 a, X3_b_eq_F op h677 a, X3_p_eq_P op h677 a]

/-! ## X4: conditional commutation closures -/

/-- X4: commutation of `F` with `U` rules out `U(F a) = U(a)` in an
idempotent-free magma. -/
theorem X4_UF_ne_U_of_commute {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (h255 : E255 op) (hfree : ∀ x, op x x ≠ x)
    (hFU : ∀ x, L12F op h677 (X6U op x) = X6U op (L12F op h677 x))
    (a : M) : X6U op (L12F op h677 a) ≠ X6U op a := by
  intro heq
  apply hfree (X6U op a)
  apply (X2_F_fixed_iff_idempotent op h677 h255 (X6U op a)).mp
  exact (hFU a).trans heq

/-- X4: commutation of `F` with `W` rules out `W(F a) = W(a)` in an
idempotent-free magma. -/
theorem X4_WF_ne_W_of_commute {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (h255 : E255 op) (hfree : ∀ x, op x x ≠ x)
    (hFW : ∀ x, L12F op h677 (X6W op x) = X6W op (L12F op h677 x))
    (a : M) : X6W op (L12F op h677 a) ≠ X6W op a := by
  intro heq
  apply hfree (X6W op a)
  apply (X2_F_fixed_iff_idempotent op h677 h255 (X6W op a)).mp
  exact (hFW a).trans heq

/-! ## X5: the automatic `c ≠ a` reduction -/

/-- Identity (J): both sides reduce by KEY to `(y*x)\x`. -/
theorem X5_identity_J {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (x y : M) :
    op x (op (op (op y x) x) (op y x)) =
      op (op y (op y x)) y := by
  let t := op y x
  have hyt : ldiv op h677 y t = x :=
    (ldiv_unique op h677 rfl).symm
  have hleft := key_identity op h677 x t
  have hright := key_identity op h677 t y
  rw [hyt] at hright
  change op x (op (op t x) t) = op (op y t) y
  calc
    op x (op (op t x) t) = op x (ldiv op h677 x (ldiv op h677 t x)) := by rw [hleft]
    _ = ldiv op h677 t x := op_ldiv op h677 x (ldiv op h677 t x)
    _ = op (op y t) y := hright.symm

/-- X5: the collision `c = a` forces `b` to be idempotent. -/
theorem X5_c_eq_a_implies_b_idempotent {M : Type u} [Finite M]
    (op : M → M → M) (h677 : E677 op) (h255 : E255 op) (a : M)
    (hca : L13C op h677 a = a) :
    op (L13B op h677 a) (L13B op h677 a) = L13B op h677 a := by
  have hbc := L13_b_mul_c op h677 h255 a
  rw [hca] at hbc
  have hJ := X5_identity_J op h677 a (L13B op h677 a)
  rw [hbc, hbc] at hJ
  change op a (L13D op h677 a) = L13V op h677 a at hJ
  rw [L13_a_mul_d op h677 h255 a] at hJ
  change L13B op h677 a = L13V op h677 a at hJ
  have hvb := L13_v_mul_b op h677 h255 a
  rw [← hJ] at hvb
  exact hvb

/-- Equalizer form of X5: `W(F a) = a` forces `F(a)` to be idempotent. -/
theorem X5_W_F_eq_implies_F_idempotent {M : Type u} [Finite M]
    (op : M → M → M) (h677 : E677 op) (h255 : E255 op) (a : M)
    (hWFa : X6W op (L12F op h677 a) = a) :
    op (L12F op h677 a) (L12F op h677 a) = L12F op h677 a := by
  have hca : L13C op h677 a = a := by
    rw [X3_c_eq_W_b op h677 a, X3_b_eq_F op h677 a]
    exact hWFa
  simpa only [X3_b_eq_F op h677 a] using
    X5_c_eq_a_implies_b_idempotent op h677 h255 a hca

/-- X5: idempotent-freeness automatically excludes `c = a`. -/
theorem X5_c_ne_a {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (h255 : E255 op) (hfree : ∀ x, op x x ≠ x) (a : M) :
    L13C op h677 a ≠ a := by
  intro hca
  exact hfree (L13B op h677 a)
    (X5_c_eq_a_implies_b_idempotent op h677 h255 a hca)

/-- The five genuinely remaining collision inequalities after automatic `c ≠ a`. -/
def X6Reduced5 {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (a : M) : Prop :=
  L13V op h677 a ≠ L13W op a ∧
  L13V op h677 a ≠ L13U op a ∧
  L13C op h677 a ≠ L13W op a ∧
  L13C op h677 a ≠ L13U op a ∧
  L13C op h677 a ≠ L13P op h677 a

/-- Under idempotent-freeness, the ticket's `X6` is exactly the reduced `X5`. -/
theorem X5_X6_iff {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (h255 : E255 op) (hfree : ∀ x, op x x ≠ x) (a : M) :
    L14X6 op h677 a ↔ X6Reduced5 op h677 a := by
  have hca := X5_c_ne_a op h677 h255 hfree a
  unfold L14X6 X6Reduced5
  aesop

#print axioms X1_U_iterate
#print axioms X1_W_right_unit
#print axioms X1_W_iterate
#print axioms X1_P_iterate
#print axioms X1_F_iterate
#print axioms X2_F_fixed_iff_idempotent
#print axioms X3_b_eq_F
#print axioms X3_v_eq_U_b
#print axioms X3_c_eq_W_b
#print axioms X3_u_eq_U
#print axioms X3_w_eq_W
#print axioms X3_p_eq_P
#print axioms X3_d_eq_b_square
#print axioms X3_v_ne_w_iff
#print axioms X3_v_ne_u_iff
#print axioms X3_c_ne_a_iff
#print axioms X3_c_ne_w_iff
#print axioms X3_c_ne_u_iff
#print axioms X3_c_ne_p_iff
#print axioms X4_UF_ne_U_of_commute
#print axioms X4_WF_ne_W_of_commute
#print axioms X5_identity_J
#print axioms X5_c_eq_a_implies_b_idempotent
#print axioms X5_W_F_eq_implies_F_idempotent
#print axioms X5_c_ne_a
#print axioms X5_X6_iff

end Ext677
