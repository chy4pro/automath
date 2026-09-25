import Ext677Pattern
import Mathlib.Tactic

/-!
# Pattern-pair subscripts and distinctness consequences
-/

namespace Ext677

open Function

universe u

/-! ## L15: the seven equation-(4) subscript quadruples -/

/-- L15, pair `(p,a)`. -/
theorem L15_pair_p_a {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (h255 : E255 op) (a : M) :
    L10P1 op h677 (L13P op h677 a, a) = (a, L13B op h677 a) ∧
    L10P2 op (L13P op h677 a, a) = (L13P op h677 a, a) ∧
    L10P3 (L13P op h677 a, a) = (a, L13P op h677 a) ∧
    L10P4 op (L13P op h677 a, a) = (L13U op a, a) := by
  have hap : op a (L13P op h677 a) = L13U op a :=
    op_ldiv op h677 a (L13U op a)
  have hdiv : ldiv op h677 a (L13P op h677 a) = L13B op h677 a := rfl
  have hua := L13_u_mul_a op h677 h255 a
  refine ⟨?_, ?_, rfl, ?_⟩
  · exact Prod.ext rfl hdiv
  · simp only [L10P2, hap, hua]
  · exact Prod.ext hap rfl

/-- L15, pair `(v,d)`. -/
theorem L15_pair_v_d {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (h255 : E255 op) (a : M) :
    L10P1 op h677 (L13V op h677 a, L13D op h677 a) =
      (L13D op h677 a, L13B op h677 a) ∧
    L10P2 op (L13V op h677 a, L13D op h677 a) =
      (L13V op h677 a, L13B op h677 a) ∧
    L10P3 (L13V op h677 a, L13D op h677 a) =
      (L13D op h677 a, L13V op h677 a) ∧
    L10P4 op (L13V op h677 a, L13D op h677 a) =
      (a, L13D op h677 a) := by
  have hdb : op (L13D op h677 a) (L13B op h677 a) = L13V op h677 a := rfl
  have hdiv : ldiv op h677 (L13D op h677 a) (L13V op h677 a) =
      L13B op h677 a := (ldiv_unique op h677 hdb).symm
  have hdv := L13_d_mul_v op h677 h255 a
  have had := L13_a_mul_d op h677 h255 a
  refine ⟨?_, ?_, rfl, ?_⟩
  · exact Prod.ext rfl hdiv
  · simp only [L10P2, hdv, had]
  · exact Prod.ext hdv rfl

/-- L15, pair `(c,b)`. -/
theorem L15_pair_c_b {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (h255 : E255 op) (a : M) :
    L10P1 op h677 (L13C op h677 a, L13B op h677 a) =
      (L13B op h677 a, L13V op h677 a) ∧
    L10P2 op (L13C op h677 a, L13B op h677 a) =
      (L13C op h677 a, L13D op h677 a) ∧
    L10P3 (L13C op h677 a, L13B op h677 a) =
      (L13B op h677 a, L13C op h677 a) ∧
    L10P4 op (L13C op h677 a, L13B op h677 a) =
      (L13B op h677 a, L13B op h677 a) := by
  have hbv : op (L13B op h677 a) (L13V op h677 a) = L13C op h677 a := rfl
  have hdiv : ldiv op h677 (L13B op h677 a) (L13C op h677 a) =
      L13V op h677 a := (ldiv_unique op h677 hbv).symm
  have hbc := L13_b_mul_c op h677 h255 a
  refine ⟨?_, ?_, rfl, ?_⟩
  · exact Prod.ext rfl hdiv
  · simp only [L10P2, hbc]
    rfl
  · exact Prod.ext hbc rfl

/-- L15, pair `(a,u)`. -/
theorem L15_pair_a_u {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (h255 : E255 op) (a : M) :
    L10P1 op h677 (a, L13U op a) = (L13U op a, a) ∧
    L10P2 op (a, L13U op a) = (a, L13W op a) ∧
    L10P3 (a, L13U op a) = (L13U op a, a) ∧
    L10P4 op (a, L13U op a) = (a, L13U op a) := by
  have hua := L13_u_mul_a op h677 h255 a
  have hdiv : ldiv op h677 (L13U op a) a = a :=
    (ldiv_unique op h677 hua).symm
  refine ⟨?_, ?_, rfl, ?_⟩
  · exact Prod.ext rfl hdiv
  · simp only [L10P2, hua]
    rfl
  · exact Prod.ext hua rfl

/-- L15, pair `(b,v)`. -/
theorem L15_pair_b_v {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (h255 : E255 op) (a : M) :
    L10P1 op h677 (L13B op h677 a, L13V op h677 a) =
      (L13V op h677 a, L13B op h677 a) ∧
    L10P2 op (L13B op h677 a, L13V op h677 a) =
      (L13B op h677 a, L13C op h677 a) ∧
    L10P3 (L13B op h677 a, L13V op h677 a) =
      (L13V op h677 a, L13B op h677 a) ∧
    L10P4 op (L13B op h677 a, L13V op h677 a) =
      (L13B op h677 a, L13V op h677 a) := by
  have hvb := L13_v_mul_b op h677 h255 a
  have hdiv : ldiv op h677 (L13V op h677 a) (L13B op h677 a) =
      L13B op h677 a := (ldiv_unique op h677 hvb).symm
  refine ⟨?_, ?_, rfl, ?_⟩
  · exact Prod.ext rfl hdiv
  · simp only [L10P2, hvb]
    rfl
  · exact Prod.ext hvb rfl

/-- L15, pair `(b,a)`. -/
theorem L15_pair_b_a {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (h255 : E255 op) (a : M) :
    L10P1 op h677 (L13B op h677 a, a) = (a, L13D op h677 a) ∧
    L10P2 op (L13B op h677 a, a) =
      (L13B op h677 a, L13B op h677 a) ∧
    L10P3 (L13B op h677 a, a) = (a, L13B op h677 a) ∧
    L10P4 op (L13B op h677 a, a) = (L13P op h677 a, a) := by
  have hab : op a (L13B op h677 a) = L13P op h677 a :=
    op_ldiv op h677 a (L13P op h677 a)
  have hdiv : ldiv op h677 a (L13B op h677 a) = L13D op h677 a :=
    (ldiv_unique op h677 (L13_a_mul_d op h677 h255 a)).symm
  have hpa := L13_p_mul_a op h677 h255 a
  refine ⟨?_, ?_, rfl, ?_⟩
  · exact Prod.ext rfl hdiv
  · simp only [L10P2, hab, hpa]
  · exact Prod.ext hab rfl

/-- L15, pair `(b,b)`. -/
theorem L15_pair_b_b {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (h255 : E255 op) (a : M) :
    L10P1 op h677 (L13B op h677 a, L13B op h677 a) =
      (L13B op h677 a, L13C op h677 a) ∧
    L10P2 op (L13B op h677 a, L13B op h677 a) =
      (L13B op h677 a, L13V op h677 a) ∧
    L10P3 (L13B op h677 a, L13B op h677 a) =
      (L13B op h677 a, L13B op h677 a) ∧
    L10P4 op (L13B op h677 a, L13B op h677 a) =
      (L13D op h677 a, L13B op h677 a) := by
  have hbc := L13_b_mul_c op h677 h255 a
  have hdiv : ldiv op h677 (L13B op h677 a) (L13B op h677 a) =
      L13C op h677 a := (ldiv_unique op h677 hbc).symm
  refine ⟨?_, ?_, rfl, ?_⟩
  · exact Prod.ext rfl hdiv
  · exact Prod.ext rfl rfl
  · exact Prod.ext rfl rfl

/-! ## L14: short cycles and orbit windows -/

/-- E255 excludes an exact forward cycle of length four. -/
theorem L12_no_exact_cycle_four {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (h255 : E255 op) (x : M) : ¬ ExactLcycle op x 4 := by
  rintro ⟨hx4, hmin⟩
  let x1 := op x x
  let x2 := op x x1
  let x3 := op x x2
  have hxx1 : op x x = x1 := rfl
  have hxx2 : op x x1 = x2 := rfl
  have hxx3 : op x x2 = x3 := rfl
  have hx3x : op x x3 = x := by
    simpa only [Lpow, Function.iterate_succ_apply, Function.iterate_zero_apply] using hx4
  have hd1 : ldiv op h677 x x = x3 :=
    (ldiv_unique op h677 hx3x).symm
  have hd2 : ldiv op h677 x x3 = x2 :=
    (ldiv_unique op h677 hxx3).symm
  have hd3 : ldiv op h677 x x2 = x1 :=
    (ldiv_unique op h677 hxx2).symm
  have hd4 : ldiv op h677 x x1 = x :=
    (ldiv_unique op h677 hxx1).symm
  have hcanonical : op x1 x = x2 := by
    rw [diagonal_candidate op h677 x, hd1, hd2]
  have hx2x : op x2 x = x := by
    have h := h255 x
    change x = op (op x1 x) x at h
    rw [hcanonical] at h
    exact h.symm
  have hx1x : op x1 x = x := by
    have hm := e677_master_division op h677 x2 x
    rw [hd3, hx2x, hd4] at hm
    exact hm
  have hx12 : x1 = x2 :=
    left_unit_unique op h677 hx1x hx2x
  have hfixed : x = x1 := by
    apply (L1_left_bij op h677 x).1
    exact hxx1.trans (hx12.trans hxx2.symm)
  exact (hmin 1 (by omega) (by omega)) (by
    simpa only [Lpow, Function.iterate_succ_apply, Function.iterate_zero_apply] using hfixed.symm)

/-- The inverse orbit under the left translation by `x`. -/
noncomputable def LinvPow {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (x : M) (k : Nat) : M :=
  (ldiv op h677 x)^[k] x

/-- Idempotent-freeness and the cycle lemmas exclude every return in steps one through five. -/
theorem L14_Lpow_ne_of_pos_le_five {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (h255 : E255 op) (hfree : ∀ y, op y y ≠ y)
    (x : M) {k : Nat} (hkpos : 0 < k) (hkle : k ≤ 5) : Lpow op x k ≠ x := by
  induction k using Nat.strong_induction_on with
  | h k ih =>
      intro hkfix
      have hexact : ExactLcycle op x k := by
        refine ⟨hkfix, ?_⟩
        intro j hj hjpos
        exact ih j hj hjpos (by omega)
      interval_cases k
      · apply hfree x
        simpa only [Lpow, Function.iterate_succ_apply, Function.iterate_zero_apply] using hkfix
      · exact L12_no_exact_cycle_two op h677 x hexact
      · exact L12_no_exact_cycle_three op h677 x hexact
      · exact L12_no_exact_cycle_four op h677 h255 x hexact
      · exact L12_no_exact_cycle_five op h677 h255 x hexact

/-- A short inverse-orbit return would give the corresponding forward-orbit return. -/
theorem L14_LinvPow_ne_of_pos_le_five {M : Type u} [Finite M]
    (op : M → M → M) (h677 : E677 op) (h255 : E255 op)
    (hfree : ∀ y, op y y ≠ y) (x : M) {k : Nat}
    (hkpos : 0 < k) (hkle : k ≤ 5) : LinvPow op h677 x k ≠ x := by
  intro hinv
  change (ldiv op h677 x)^[k] x = x at hinv
  have hright : Function.RightInverse (ldiv op h677 x) (op x) :=
    fun y => op_ldiv op h677 x y
  have hforward : Lpow op x k = x := by
    change (op x)^[k] x = x
    calc
      (op x)^[k] x = (op x)^[k] ((ldiv op h677 x)^[k] x) := by rw [hinv]
      _ = x := hright.iterate k x
  exact L14_Lpow_ne_of_pos_le_five op h677 h255 hfree x hkpos hkle hforward

/-- Distinct positions in the first six entries of an inverse orbit are unequal. -/
theorem L14_LinvPow_pair_ne {M : Type u} [Finite M]
    (op : M → M → M) (h677 : E677 op) (h255 : E255 op)
    (hfree : ∀ y, op y y ≠ y) (x : M) {i j : Nat}
    (hij : i < j) (hjle : j ≤ 5) :
    LinvPow op h677 x i ≠ LinvPow op h677 x j := by
  intro heq
  let g := ldiv op h677 x
  have hright : Function.RightInverse g (op x) := fun y => op_ldiv op h677 x y
  have hginj : Function.Injective g := hright.injective
  have hadd : g^[j - i + i] x = g^[i] x := by
    rw [Nat.sub_add_cancel (Nat.le_of_lt hij)]
    exact heq.symm
  have hperiod : g^[j - i] x = x :=
    (Function.iterate_add_eq_iterate (m := j - i) (n := i) (a := x) hginj).mp hadd
  apply L14_LinvPow_ne_of_pos_le_five op h677 h255 hfree x
    (Nat.sub_pos_of_lt hij) (le_trans (Nat.sub_le j i) hjle)
  exact hperiod

/-- The first pattern window is the first six inverse iterates of `L_a`. -/
theorem L14_first_window_coordinates {M : Type u} [Finite M]
    (op : M → M → M) (h677 : E677 op) (h255 : E255 op) (a : M) :
    L13W op a = LinvPow op h677 a 1 ∧
    L13U op a = LinvPow op h677 a 2 ∧
    L13P op h677 a = LinvPow op h677 a 3 ∧
    L13B op h677 a = LinvPow op h677 a 4 ∧
    L13D op h677 a = LinvPow op h677 a 5 := by
  have hu : L13U op a = ldiv op h677 a (ldiv op h677 a a) :=
    diagonal_candidate op h677 a
  have haw : op a (L13W op a) = a := by
    change op a (op a (L13U op a)) = a
    rw [hu, op_ldiv op h677 a (ldiv op h677 a a), op_ldiv op h677 a a]
  have hw : L13W op a = ldiv op h677 a a :=
    ldiv_unique op h677 haw
  have hbF : L13B op h677 a = L12F op h677 a := by
    change ldiv op h677 a (ldiv op h677 a (L13U op a)) = L12F op h677 a
    rw [hu]
    rfl
  have hd : L13D op h677 a = ldiv op h677 a (L13B op h677 a) := by
    simpa only [L13D, hbF] using L12F_spec op h677 h255 a
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · simpa only [LinvPow, Function.iterate_succ_apply, Function.iterate_zero_apply] using hw
  · simpa only [LinvPow, Function.iterate_succ_apply, Function.iterate_zero_apply] using hu
  · rw [L13P]
    simpa only [LinvPow, Function.iterate_succ_apply, Function.iterate_zero_apply] using
      congrArg (ldiv op h677 a) hu
  · rw [L13B, L13P]
    simpa only [LinvPow, Function.iterate_succ_apply, Function.iterate_zero_apply] using
      congrArg (fun z => ldiv op h677 a (ldiv op h677 a z)) hu
  · rw [hd, L13B, L13P, hu]
    rfl

/-- The terms `c,v` are the first two inverse iterates of `L_b`. -/
theorem L14_second_window_coordinates {M : Type u} [Finite M]
    (op : M → M → M) (h677 : E677 op) (h255 : E255 op) (a : M) :
    L13C op h677 a = LinvPow op h677 (L13B op h677 a) 1 ∧
    L13V op h677 a = LinvPow op h677 (L13B op h677 a) 2 := by
  have hbc := L13_b_mul_c op h677 h255 a
  have hc : L13C op h677 a =
      ldiv op h677 (L13B op h677 a) (L13B op h677 a) :=
    ldiv_unique op h677 hbc
  have hv : L13V op h677 a =
      ldiv op h677 (L13B op h677 a) (L13C op h677 a) :=
    ldiv_unique op h677 rfl
  constructor
  · simpa only [LinvPow, Function.iterate_succ_apply, Function.iterate_zero_apply] using hc
  · rw [hv, hc]
    rfl

section L14Inequalities

variable {M : Type u} [Finite M]
variable (op : M → M → M) (h677 : E677 op) (h255 : E255 op)
variable (hfree : ∀ y, op y y ≠ y) (a : M)

include h677 h255 hfree

/-- Automatic inequality `a ≠ w`. -/
theorem L14_a_ne_w : a ≠ L13W op a := by
  have hc := L14_first_window_coordinates op h677 h255 a
  rw [hc.1]
  simpa only [LinvPow, Function.iterate_zero_apply] using
    (L14_LinvPow_pair_ne op h677 h255 hfree a (i := 0) (j := 1) (by omega) (by omega))

/-- Automatic inequality `a ≠ u`. -/
theorem L14_a_ne_u : a ≠ L13U op a := by
  have hc := L14_first_window_coordinates op h677 h255 a
  rw [hc.2.1]
  simpa only [LinvPow, Function.iterate_zero_apply] using
    (L14_LinvPow_pair_ne op h677 h255 hfree a (i := 0) (j := 2) (by omega) (by omega))

/-- Automatic inequality `a ≠ p`. -/
theorem L14_a_ne_p : a ≠ L13P op h677 a := by
  have hc := L14_first_window_coordinates op h677 h255 a
  rw [hc.2.2.1]
  simpa only [LinvPow, Function.iterate_zero_apply] using
    (L14_LinvPow_pair_ne op h677 h255 hfree a (i := 0) (j := 3) (by omega) (by omega))

/-- Automatic inequality `a ≠ b`. -/
theorem L14_a_ne_b : a ≠ L13B op h677 a := by
  have hc := L14_first_window_coordinates op h677 h255 a
  rw [hc.2.2.2.1]
  simpa only [LinvPow, Function.iterate_zero_apply] using
    (L14_LinvPow_pair_ne op h677 h255 hfree a (i := 0) (j := 4) (by omega) (by omega))

/-- Automatic inequality `a ≠ d`. -/
theorem L14_a_ne_d : a ≠ L13D op h677 a := by
  have hc := L14_first_window_coordinates op h677 h255 a
  rw [hc.2.2.2.2]
  simpa only [LinvPow, Function.iterate_zero_apply] using
    (L14_LinvPow_pair_ne op h677 h255 hfree a (i := 0) (j := 5) (by omega) (by omega))

/-- Automatic inequality `w ≠ u`. -/
theorem L14_w_ne_u : L13W op a ≠ L13U op a := by
  have hc := L14_first_window_coordinates op h677 h255 a
  rw [hc.1, hc.2.1]
  exact L14_LinvPow_pair_ne op h677 h255 hfree a (by omega) (by omega)

/-- Automatic inequality `w ≠ p`. -/
theorem L14_w_ne_p : L13W op a ≠ L13P op h677 a := by
  have hc := L14_first_window_coordinates op h677 h255 a
  rw [hc.1, hc.2.2.1]
  exact L14_LinvPow_pair_ne op h677 h255 hfree a (by omega) (by omega)

/-- Automatic inequality `w ≠ b`. -/
theorem L14_w_ne_b : L13W op a ≠ L13B op h677 a := by
  have hc := L14_first_window_coordinates op h677 h255 a
  rw [hc.1, hc.2.2.2.1]
  exact L14_LinvPow_pair_ne op h677 h255 hfree a (by omega) (by omega)

/-- Automatic inequality `w ≠ d`. -/
theorem L14_w_ne_d : L13W op a ≠ L13D op h677 a := by
  have hc := L14_first_window_coordinates op h677 h255 a
  rw [hc.1, hc.2.2.2.2]
  exact L14_LinvPow_pair_ne op h677 h255 hfree a (by omega) (by omega)

/-- Automatic inequality `u ≠ p`. -/
theorem L14_u_ne_p : L13U op a ≠ L13P op h677 a := by
  have hc := L14_first_window_coordinates op h677 h255 a
  rw [hc.2.1, hc.2.2.1]
  exact L14_LinvPow_pair_ne op h677 h255 hfree a (by omega) (by omega)

/-- Automatic inequality `u ≠ b`. -/
theorem L14_u_ne_b : L13U op a ≠ L13B op h677 a := by
  have hc := L14_first_window_coordinates op h677 h255 a
  rw [hc.2.1, hc.2.2.2.1]
  exact L14_LinvPow_pair_ne op h677 h255 hfree a (by omega) (by omega)

/-- Automatic inequality `u ≠ d`. -/
theorem L14_u_ne_d : L13U op a ≠ L13D op h677 a := by
  have hc := L14_first_window_coordinates op h677 h255 a
  rw [hc.2.1, hc.2.2.2.2]
  exact L14_LinvPow_pair_ne op h677 h255 hfree a (by omega) (by omega)

/-- Automatic inequality `p ≠ b`. -/
theorem L14_p_ne_b : L13P op h677 a ≠ L13B op h677 a := by
  have hc := L14_first_window_coordinates op h677 h255 a
  rw [hc.2.2.1, hc.2.2.2.1]
  exact L14_LinvPow_pair_ne op h677 h255 hfree a (by omega) (by omega)

/-- Automatic inequality `p ≠ d`. -/
theorem L14_p_ne_d : L13P op h677 a ≠ L13D op h677 a := by
  have hc := L14_first_window_coordinates op h677 h255 a
  rw [hc.2.2.1, hc.2.2.2.2]
  exact L14_LinvPow_pair_ne op h677 h255 hfree a (by omega) (by omega)

/-- Automatic inequality `b ≠ d`. -/
theorem L14_b_ne_d : L13B op h677 a ≠ L13D op h677 a := by
  have _h255b : E255At op (L13B op h677 a) := h255 (L13B op h677 a)
  change L13B op h677 a ≠ op (L13B op h677 a) (L13B op h677 a)
  exact (hfree (L13B op h677 a)).symm

/-- Automatic inequality `b ≠ c`. -/
theorem L14_b_ne_c : L13B op h677 a ≠ L13C op h677 a := by
  have hc := L14_second_window_coordinates op h677 h255 a
  rw [hc.1]
  simpa only [LinvPow, Function.iterate_zero_apply] using
    (L14_LinvPow_pair_ne op h677 h255 hfree (L13B op h677 a)
      (i := 0) (j := 1) (by omega) (by omega))

/-- Automatic inequality `b ≠ v`. -/
theorem L14_b_ne_v : L13B op h677 a ≠ L13V op h677 a := by
  have hc := L14_second_window_coordinates op h677 h255 a
  rw [hc.2]
  simpa only [LinvPow, Function.iterate_zero_apply] using
    (L14_LinvPow_pair_ne op h677 h255 hfree (L13B op h677 a)
      (i := 0) (j := 2) (by omega) (by omega))

/-- Automatic inequality `c ≠ v`. -/
theorem L14_c_ne_v : L13C op h677 a ≠ L13V op h677 a := by
  have hc := L14_second_window_coordinates op h677 h255 a
  rw [hc.1, hc.2]
  exact L14_LinvPow_pair_ne op h677 h255 hfree (L13B op h677 a) (by omega) (by omega)

/-- Automatic inequality `d ≠ c`. -/
theorem L14_d_ne_c : L13D op h677 a ≠ L13C op h677 a := by
  intro hdc
  have hreturn : Lpow op (L13B op h677 a) 2 = L13B op h677 a := by
    change op (L13B op h677 a) (op (L13B op h677 a) (L13B op h677 a)) =
      L13B op h677 a
    rw [show op (L13B op h677 a) (L13B op h677 a) = L13D op h677 a from rfl,
      hdc, L13_b_mul_c op h677 h255 a]
  exact L14_Lpow_ne_of_pos_le_five op h677 h255 hfree (L13B op h677 a)
    (by omega) (by omega) hreturn

/-- Automatic inequality `d ≠ v`. -/
theorem L14_d_ne_v : L13D op h677 a ≠ L13V op h677 a := by
  intro hdv
  have hreturn : Lpow op (L13B op h677 a) 3 = L13B op h677 a := by
    change op (L13B op h677 a)
      (op (L13B op h677 a) (op (L13B op h677 a) (L13B op h677 a))) =
      L13B op h677 a
    rw [show op (L13B op h677 a) (L13B op h677 a) = L13D op h677 a from rfl,
      hdv, show op (L13B op h677 a) (L13V op h677 a) = L13C op h677 a from rfl,
      L13_b_mul_c op h677 h255 a]
  exact L14_Lpow_ne_of_pos_le_five op h677 h255 hfree (L13B op h677 a)
    (by omega) (by omega) hreturn

/-- Automatic cross-window inequality `v ≠ a`. -/
theorem L14_v_ne_a : L13V op h677 a ≠ a := by
  intro hva
  have hvb := L13_v_mul_b op h677 h255 a
  have hab : op a (L13B op h677 a) = L13P op h677 a :=
    op_ldiv op h677 a (L13P op h677 a)
  rw [hva, hab] at hvb
  exact L14_p_ne_b op h677 h255 hfree a hvb

/-- Automatic cross-window inequality `v ≠ p`. -/
theorem L14_v_ne_p : L13V op h677 a ≠ L13P op h677 a := by
  intro hvp
  have hvb := L13_v_mul_b op h677 h255 a
  rw [hvp] at hvb
  have hpa := L13_p_mul_a op h677 h255 a
  have hab : a = L13B op h677 a := by
    apply (L1_left_bij op h677 (L13P op h677 a)).1
    exact hpa.trans hvb.symm
  exact L14_a_ne_b op h677 h255 hfree a hab

/-- The six explicitly retained cross-window disequalities from the ticket. -/
def L14X6 : Prop :=
  L13V op h677 a ≠ L13W op a ∧
  L13V op h677 a ≠ L13U op a ∧
  L13C op h677 a ≠ a ∧
  L13C op h677 a ≠ L13W op a ∧
  L13C op h677 a ≠ L13U op a ∧
  L13C op h677 a ≠ L13P op h677 a

/-- Explicit pairwise-distinctness predicate for `(a,u,p,b,v,c,d,w)`. -/
def L14PairwiseTerms : Prop :=
  a ≠ L13U op a ∧ a ≠ L13P op h677 a ∧
  a ≠ L13B op h677 a ∧ a ≠ L13V op h677 a ∧
  a ≠ L13C op h677 a ∧ a ≠ L13D op h677 a ∧ a ≠ L13W op a ∧
  L13U op a ≠ L13P op h677 a ∧ L13U op a ≠ L13B op h677 a ∧
  L13U op a ≠ L13V op h677 a ∧ L13U op a ≠ L13C op h677 a ∧
  L13U op a ≠ L13D op h677 a ∧ L13U op a ≠ L13W op a ∧
  L13P op h677 a ≠ L13B op h677 a ∧ L13P op h677 a ≠ L13V op h677 a ∧
  L13P op h677 a ≠ L13C op h677 a ∧ L13P op h677 a ≠ L13D op h677 a ∧
  L13P op h677 a ≠ L13W op a ∧
  L13B op h677 a ≠ L13V op h677 a ∧ L13B op h677 a ≠ L13C op h677 a ∧
  L13B op h677 a ≠ L13D op h677 a ∧ L13B op h677 a ≠ L13W op a ∧
  L13V op h677 a ≠ L13C op h677 a ∧ L13V op h677 a ≠ L13D op h677 a ∧
  L13V op h677 a ≠ L13W op a ∧
  L13C op h677 a ≠ L13D op h677 a ∧ L13C op h677 a ≠ L13W op a ∧
  L13D op h677 a ≠ L13W op a

/-- L14 package: `X6` plus the 22 automatic inequalities gives all 28 pairs. -/
theorem L14_X6_implies_pairwise :
    L14X6 op h677 a → L14PairwiseTerms op h677 a := by
  intro hx6
  rcases hx6 with ⟨hvw, hvu, hca, hcw, hcu, hcp⟩
  have haw := L14_a_ne_w op h677 h255 hfree a
  have hau := L14_a_ne_u op h677 h255 hfree a
  have hap := L14_a_ne_p op h677 h255 hfree a
  have hab := L14_a_ne_b op h677 h255 hfree a
  have had := L14_a_ne_d op h677 h255 hfree a
  have hwu := L14_w_ne_u op h677 h255 hfree a
  have hwp := L14_w_ne_p op h677 h255 hfree a
  have hwb := L14_w_ne_b op h677 h255 hfree a
  have hwd := L14_w_ne_d op h677 h255 hfree a
  have hup := L14_u_ne_p op h677 h255 hfree a
  have hub := L14_u_ne_b op h677 h255 hfree a
  have hud := L14_u_ne_d op h677 h255 hfree a
  have hpb := L14_p_ne_b op h677 h255 hfree a
  have hpd := L14_p_ne_d op h677 h255 hfree a
  have hbd := L14_b_ne_d op h677 h255 hfree a
  have hbc := L14_b_ne_c op h677 h255 hfree a
  have hbv := L14_b_ne_v op h677 h255 hfree a
  have hcv := L14_c_ne_v op h677 h255 hfree a
  have hdc := L14_d_ne_c op h677 h255 hfree a
  have hdv := L14_d_ne_v op h677 h255 hfree a
  have hva := L14_v_ne_a op h677 h255 hfree a
  have hvp := L14_v_ne_p op h677 h255 hfree a
  unfold L14PairwiseTerms
  exact ⟨hau, hap, hab, hva.symm, hca.symm, had, haw,
    hup, hub, hvu.symm, hcu.symm, hud, hwu.symm,
    hpb, hvp.symm, hcp.symm, hpd, hwp.symm,
    hbv, hbc, hbd, hwb.symm,
    hcv.symm, hdv.symm, hvw,
    hdc.symm, hcw, hwd.symm⟩

end L14Inequalities

#print axioms L15_pair_p_a
#print axioms L15_pair_v_d
#print axioms L15_pair_c_b
#print axioms L15_pair_a_u
#print axioms L15_pair_b_v
#print axioms L15_pair_b_a
#print axioms L15_pair_b_b
#print axioms L12_no_exact_cycle_four
#print axioms L14_Lpow_ne_of_pos_le_five
#print axioms L14_LinvPow_ne_of_pos_le_five
#print axioms L14_LinvPow_pair_ne
#print axioms L14_first_window_coordinates
#print axioms L14_second_window_coordinates
#print axioms L14_a_ne_w
#print axioms L14_a_ne_u
#print axioms L14_a_ne_p
#print axioms L14_a_ne_b
#print axioms L14_a_ne_d
#print axioms L14_w_ne_u
#print axioms L14_w_ne_p
#print axioms L14_w_ne_b
#print axioms L14_w_ne_d
#print axioms L14_u_ne_p
#print axioms L14_u_ne_b
#print axioms L14_u_ne_d
#print axioms L14_p_ne_b
#print axioms L14_p_ne_d
#print axioms L14_b_ne_d
#print axioms L14_b_ne_c
#print axioms L14_b_ne_v
#print axioms L14_c_ne_v
#print axioms L14_d_ne_c
#print axioms L14_d_ne_v
#print axioms L14_v_ne_a
#print axioms L14_v_ne_p
#print axioms L14_X6_implies_pairwise

end Ext677
