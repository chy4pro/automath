import Ext677Occ
import Mathlib.Tactic

/-!
# Inverse maps, cycle restrictions, and the automatic pattern identities
-/

namespace Ext677

open Function

universe u

/-- The fourth inverse-left-translation iterate at its own base point. -/
noncomputable def L12F {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (x : M) : M :=
  ldiv op h677 x (ldiv op h677 x (ldiv op h677 x (ldiv op h677 x x)))

/-- The companion term `(x*x)*((x*x)*x)`. -/
def L12H {M : Type u} (op : M → M → M) (x : M) : M :=
  op (op x x) (op (op x x) x)

/-- The master left-division form of E677. -/
theorem e677_master_division {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (u y : M) :
    op (ldiv op h677 y u) (op u y) =
      ldiv op h677 y (ldiv op h677 y u) := by
  have h := h677 (ldiv op h677 y u) y
  have hdiv := ldiv_unique op h677 h.symm
  simpa only [op_ldiv] using hdiv

/-- The witness in `z*z = h\z` is unique and is the fourth inverse iterate. -/
theorem L12_square_eq_div_unique {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (h255 : E255 op) (h z : M)
    (hz : op z z = ldiv op h677 h z) : z = L12F op h677 h := by
  let w := op h z
  have hhw : ldiv op h677 h w = z := by
    exact (ldiv_unique op h677 rfl).symm
  have hwh : op w h = z := by
    rw [right_product_formula op h677 w h, hhw, ← hz]
    exact (ldiv_unique op h677 rfl).symm
  have hvh : op (op h w) h = h := by
    have hm := e677_master_division op h677 (op h w) h
    have hd : ldiv op h677 h (op h w) = w :=
      (ldiv_unique op h677 rfl).symm
    rw [hd, hhw] at hm
    apply (L1_left_bij op h677 w).1
    exact hm.trans hwh.symm
  have hvq : op h w = canonicalLeftUnit op h :=
    left_unit_unique op h677 hvh (canonicalLeftUnit_mul op h255 h)
  have hw : w = ldiv op h677 h (canonicalLeftUnit op h) :=
    ldiv_unique op h677 hvq
  have hq : canonicalLeftUnit op h =
      ldiv op h677 h (ldiv op h677 h h) :=
    diagonal_candidate op h677 h
  calc
    z = ldiv op h677 h w := hhw.symm
    _ = ldiv op h677 h (ldiv op h677 h (canonicalLeftUnit op h)) := by rw [hw]
    _ = L12F op h677 h := by rw [hq]; rfl

/-- Under E255, `F x` satisfies the square/division witness equation. -/
theorem L12F_spec {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (h255 : E255 op) (x : M) :
    op (L12F op h677 x) (L12F op h677 x) =
      ldiv op h677 x (L12F op h677 x) := by
  let q := canonicalLeftUnit op x
  let w := ldiv op h677 x q
  let c := ldiv op h677 x w
  let d := ldiv op h677 x c
  have hqdiv : q = ldiv op h677 x (ldiv op h677 x x) :=
    diagonal_candidate op h677 x
  have hwdiv : ldiv op h677 x q = w := rfl
  have hcdiv : ldiv op h677 x w = c := rfl
  have hqmul : op q x = x := canonicalLeftUnit_mul op h255 x
  have hwmul : op w x = c := by
    have hm := e677_master_division op h677 q x
    rw [hwdiv, hqmul, hcdiv] at hm
    exact hm
  have hright := right_product_formula op h677 w x
  have hwd : op w x = ldiv op h677 c d := by
    simpa only [hwdiv, hcdiv] using hright
  have hc : c = ldiv op h677 c d := hwmul.symm.trans hwd
  have hcc : op c c = d := by
    have := congrArg (op c) hc
    simpa only [op_ldiv] using this
  have hcF : c = L12F op h677 x := by
    rw [L12F, ← hqdiv]
  have hdF : d = ldiv op h677 x (L12F op h677 x) := by
    rw [← hcF]
  calc
    op (L12F op h677 x) (L12F op h677 x) = op c c := by rw [hcF]
    _ = d := hcc
    _ = ldiv op h677 x (L12F op h677 x) := hdF

/-- First half of L12(a): `F (H x) = x`. -/
theorem L12_F_H {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (h255 : E255 op) (x : M) :
    L12F op h677 (L12H op x) = x := by
  let s := op x x
  let q := op s x
  let h := op s q
  have hqx : op q x = x := (h255 x).symm
  have hsx : op s x = q := rfl
  have hhs : op h s = x := by
    have hkey := key_identity op h677 q s
    have hsdiv : ldiv op h677 s q = x :=
      (ldiv_unique op h677 hsx).symm
    have hqdiv : ldiv op h677 q x = x :=
      (ldiv_unique op h677 hqx).symm
    rw [hsdiv, hqdiv] at hkey
    exact hkey
  have hs : s = ldiv op h677 h x := ldiv_unique op h677 hhs
  have hxwitness : op x x = ldiv op h677 h x := by
    change s = ldiv op h677 h x
    exact hs
  have hxF : x = L12F op h677 h :=
    L12_square_eq_div_unique op h677 h255 h x hxwitness
  exact hxF.symm

/-- L12(a): the finite maps `F` and `H` are mutual inverses. -/
theorem L12_H_F {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (h255 : E255 op) (x : M) :
    L12H op (L12F op h677 x) = x := by
  have hleft : Function.LeftInverse (L12F op h677) (L12H op) :=
    fun y => L12_F_H op h677 h255 y
  have hHsurj : Function.Surjective (L12H op) :=
    Finite.injective_iff_surjective.mp hleft.injective
  obtain ⟨y, hy⟩ := hHsurj x
  calc
    L12H op (L12F op h677 x) =
        L12H op (L12F op h677 (L12H op y)) := by rw [hy]
    _ = L12H op y := by rw [hleft y]
    _ = x := hy

/-- The forward orbit of `x` under its own left translation. -/
def Lpow {M : Type u} (op : M → M → M) (x : M) (k : Nat) : M :=
  (op x)^[k] x

/-- `x` has exact forward left-translation period `n`. -/
def ExactLcycle {M : Type u} (op : M → M → M) (x : M) (n : Nat) : Prop :=
  Lpow op x n = x ∧
    ∀ k, k < n → 0 < k → Lpow op x k ≠ x

/-- L12(b): E677 alone excludes exact forward cycles of length two. -/
theorem L12_no_exact_cycle_two {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (x : M) : ¬ ExactLcycle op x 2 := by
  rintro ⟨hx2, hmin⟩
  let x1 := op x x
  have hxx1 : op x x = x1 := rfl
  have hx1x : op x x1 = x := by
    simpa only [Lpow, Function.iterate_succ_apply, Function.iterate_zero_apply] using hx2
  have hd1 : ldiv op h677 x x = x1 :=
    (ldiv_unique op h677 hx1x).symm
  have hd2 : ldiv op h677 x (ldiv op h677 x x) = x := by
    rw [hd1]
    exact (ldiv_unique op h677 hxx1).symm
  have hleft : op x1 x = x := by
    rw [diagonal_candidate op h677 x, hd2]
  have h255x : E255At op x :=
    (e255At_iff_exists_left_unit op h677 x).2 ⟨x1, hleft⟩
  have hfixed : op x x = x := by
    change x = op (op x1 x) x at h255x
    rw [hleft] at h255x
    exact h255x.symm
  exact (hmin 1 (by omega) (by omega)) (by
    simpa only [Lpow, Function.iterate_succ_apply, Function.iterate_zero_apply] using hfixed)

/-- L12(b): E677 alone excludes exact forward cycles of length three. -/
theorem L12_no_exact_cycle_three {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (x : M) : ¬ ExactLcycle op x 3 := by
  rintro ⟨hx3, hmin⟩
  let x1 := op x x
  let x2 := op x x1
  have hxx1 : op x x = x1 := rfl
  have hxx2 : op x x1 = x2 := rfl
  have hx2x : op x x2 = x := by
    simpa only [Lpow, Function.iterate_succ_apply, Function.iterate_zero_apply] using hx3
  have hd1 : ldiv op h677 x x = x2 :=
    (ldiv_unique op h677 hx2x).symm
  have hd2 : ldiv op h677 x (ldiv op h677 x x) = x1 := by
    rw [hd1]
    exact (ldiv_unique op h677 hxx2).symm
  have hx1x : op x1 x = x1 := by
    rw [diagonal_candidate op h677 x, hd2]
  have hx2x1 : op x2 x1 = x1 := by
    have hm := e677_master_division op h677 x x
    rw [hd1, hxx1, (ldiv_unique op h677 hxx2).symm] at hm
    exact hm
  have hx1x2 : op x1 x2 = x := by
    rw [left_unit_right_product op h677 hx2x1]
    exact (ldiv_unique op h677 hx1x).symm
  have hx1fixed : op x1 x1 = x1 := by
    have hk := key_identity op h677 x x1
    have hdx1 : ldiv op h677 x1 x = x2 :=
      (ldiv_unique op h677 hx1x2).symm
    have hdx2 : ldiv op h677 x x2 = x1 :=
      (ldiv_unique op h677 hxx2).symm
    rw [hx1x, hdx1, hdx2] at hk
    exact hk
  have heq : x = x1 := by
    apply (L1_left_bij op h677 x1).1
    exact hx1x.trans hx1fixed.symm
  exact (hmin 1 (by omega) (by omega)) (by
    simpa only [Lpow, Function.iterate_succ_apply, Function.iterate_zero_apply] using heq.symm)

/-- L12(b): E677 together with E255 excludes exact forward cycles of length five. -/
theorem L12_no_exact_cycle_five {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (h255 : E255 op) (x : M) : ¬ ExactLcycle op x 5 := by
  rintro ⟨hx5, hmin⟩
  let x1 := op x x
  let x2 := op x x1
  let x3 := op x x2
  let x4 := op x x3
  have hxx1 : op x x = x1 := rfl
  have hxx2 : op x x1 = x2 := rfl
  have hxx3 : op x x2 = x3 := rfl
  have hxx4 : op x x3 = x4 := rfl
  have hx4x : op x x4 = x := by
    simpa only [Lpow, Function.iterate_succ_apply, Function.iterate_zero_apply] using hx5
  have hd1 : ldiv op h677 x x = x4 :=
    (ldiv_unique op h677 hx4x).symm
  have hd2 : ldiv op h677 x x4 = x3 :=
    (ldiv_unique op h677 hxx4).symm
  have hd3 : ldiv op h677 x x3 = x2 :=
    (ldiv_unique op h677 hxx3).symm
  have hd4 : ldiv op h677 x x2 = x1 :=
    (ldiv_unique op h677 hxx2).symm
  have hF : L12F op h677 x = x1 := by
    rw [L12F, hd1, hd2, hd3, hd4]
  have hdivF : ldiv op h677 x (L12F op h677 x) = x := by
    rw [hF]
    exact (ldiv_unique op h677 hxx1).symm
  have hx1square : op x1 x1 = x := by
    have hs := L12F_spec op h677 h255 x
    have hdivx1 : ldiv op h677 x x1 = x :=
      (ldiv_unique op h677 hxx1).symm
    rw [hF, hdivx1] at hs
    exact hs
  have hx3eq : x3 = x := by
    have hinv := L12_H_F op h677 h255 x
    rw [hF] at hinv
    change op (op x1 x1) (op (op x1 x1) x1) = x at hinv
    rw [hx1square, hxx2] at hinv
    exact hinv
  exact (hmin 3 (by omega) (by omega)) (by
    simpa only [Lpow, Function.iterate_succ_apply, Function.iterate_zero_apply] using hx3eq)

/-! ## L13 automatic pattern -/

/-- `u = (a*a)*a`. -/
def L13U {M : Type u} (op : M → M → M) (a : M) : M :=
  op (op a a) a

/-- `p = a\u`. -/
noncomputable def L13P {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (a : M) : M :=
  ldiv op h677 a (L13U op a)

/-- `b = a\p`. -/
noncomputable def L13B {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (a : M) : M :=
  ldiv op h677 a (L13P op h677 a)

/-- `d = b*b`. -/
noncomputable def L13D {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (a : M) : M :=
  op (L13B op h677 a) (L13B op h677 a)

/-- `v = d*b`. -/
noncomputable def L13V {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (a : M) : M :=
  op (L13D op h677 a) (L13B op h677 a)

/-- `c = b*v`. -/
noncomputable def L13C {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (a : M) : M :=
  op (L13B op h677 a) (L13V op h677 a)

/-- `w = a*u`. -/
def L13W {M : Type u} (op : M → M → M) (a : M) : M :=
  op a (L13U op a)

/-- L13: `u*a = a`. -/
theorem L13_u_mul_a {M : Type u} [Finite M] (op : M → M → M)
    (_h677 : E677 op) (h255 : E255 op) (a : M) :
    op (L13U op a) a = a := by
  exact (h255 a).symm

/-- L13: `v*b = b`. -/
theorem L13_v_mul_b {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (h255 : E255 op) (a : M) :
    op (L13V op h677 a) (L13B op h677 a) = L13B op h677 a := by
  exact (h255 (L13B op h677 a)).symm

/-- L13: `p*a = b`. -/
theorem L13_p_mul_a {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (h255 : E255 op) (a : M) :
    op (L13P op h677 a) a = L13B op h677 a := by
  have hap : op a (L13P op h677 a) = L13U op a := by
    exact op_ldiv op h677 a (L13U op a)
  have hk := key_identity op h677 (L13P op h677 a) a
  have hab : ldiv op h677 a (L13P op h677 a) = L13B op h677 a := rfl
  rw [hap, L13_u_mul_a op h677 h255 a, hab] at hk
  have hp := congrArg (op (L13P op h677 a)) hk
  simpa only [op_ldiv] using hp

/-- L13: `a*d = b`. -/
theorem L13_a_mul_d {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (h255 : E255 op) (a : M) :
    op a (L13D op h677 a) = L13B op h677 a := by
  have hab : op a (L13B op h677 a) = L13P op h677 a := by
    exact op_ldiv op h677 a (L13P op h677 a)
  have he := h677 (L13B op h677 a) a
  rw [hab, L13_p_mul_a op h677 h255 a] at he
  change L13B op h677 a = op a (L13D op h677 a) at he
  exact he.symm

/-- L13: `b*c = b`. -/
theorem L13_b_mul_c {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (h255 : E255 op) (a : M) :
    op (L13B op h677 a) (L13C op h677 a) = L13B op h677 a := by
  have hvb := L13_v_mul_b op h677 h255 a
  have he := h677 (L13B op h677 a) (L13V op h677 a)
  rw [hvb] at he
  change L13B op h677 a =
    op (L13V op h677 a) (op (L13B op h677 a) (L13C op h677 a)) at he
  apply (L1_left_bij op h677 (L13V op h677 a)).1
  calc
    op (L13V op h677 a) (op (L13B op h677 a) (L13C op h677 a)) =
        L13B op h677 a := he.symm
    _ = op (L13V op h677 a) (L13B op h677 a) := hvb.symm

/-- L13: `d*v = a`. -/
theorem L13_d_mul_v {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (h255 : E255 op) (a : M) :
    op (L13D op h677 a) (L13V op h677 a) = a := by
  have hu : L13U op a = ldiv op h677 a (ldiv op h677 a a) :=
    diagonal_candidate op h677 a
  have hbF : L13B op h677 a = L12F op h677 a := by
    change ldiv op h677 a (ldiv op h677 a (L13U op a)) = L12F op h677 a
    rw [hu]
    rfl
  calc
    op (L13D op h677 a) (L13V op h677 a) =
        L12H op (L13B op h677 a) := rfl
    _ = L12H op (L12F op h677 a) := by rw [hbF]
    _ = a := L12_H_F op h677 h255 a

#print axioms e677_master_division
#print axioms L12_square_eq_div_unique
#print axioms L12F_spec
#print axioms L12_F_H
#print axioms L12_H_F
#print axioms L12_no_exact_cycle_two
#print axioms L12_no_exact_cycle_three
#print axioms L12_no_exact_cycle_five
#print axioms L13_u_mul_a
#print axioms L13_v_mul_b
#print axioms L13_p_mul_a
#print axioms L13_a_mul_d
#print axioms L13_b_mul_c
#print axioms L13_d_mul_v

end Ext677
