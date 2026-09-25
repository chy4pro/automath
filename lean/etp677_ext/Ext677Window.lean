import Ext677X6
import Mathlib.Tactic

/-!
# R46 window and quotient-lifting lemmas
-/

namespace Ext677

open Function

universe u v

/-- The extra window point `e = W(p)`. -/
noncomputable def WindowE {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (a : M) : M :=
  X6W op (L13P op h677 a)

/-- The R46 window hypothesis `v = u ∧ c = p`. -/
def WindowPred {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (a : M) : Prop :=
  L13V op h677 a = L13U op a ∧
  L13C op h677 a = L13P op h677 a

/-- L-A: a left unit at `x` is `U(x)`, and its right product is `W(x)`. -/
theorem window_left_unit {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) {u x : M} (hux : op u x = x) :
    op x u = X6W op x ∧ X6U op x = u := by
  have he := h677 x u
  have hinner : op x (op x u) = x := by
    apply (L1_left_bij op h677 u).1
    rw [hux] at he
    exact he.symm.trans hux.symm
  have hxu : op x u = X6W op x := by
    apply (L1_left_bij op h677 x).1
    exact hinner.trans (X1_W_right_unit op h677 x).symm
  refine ⟨hxu, ?_⟩
  have hu : u = ldiv op h677 x (X6W op x) :=
    ldiv_unique op h677 hxu
  rw [hu, X1_W_iterate op h677 x, X1_U_iterate op h677 x]

/-- E255 states that `U(x)` is a left unit at `x`. -/
theorem window_U_mul {M : Type u} [Finite M] (op : M → M → M)
    (_h677 : E677 op) (h255 : E255 op) (x : M) :
    op (X6U op x) x = x :=
  (h255 x).symm

/-- Under E255, the fixed points of `L_u` are exactly the fibre `U⁻¹(u)`. -/
theorem window_fixed_iff_U {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (h255 : E255 op) (u x : M) :
    op u x = x ↔ X6U op x = u := by
  constructor
  · exact fun h => (window_left_unit op h677 h).2
  · intro h
    rw [← h]
    exact window_U_mul op h677 h255 x

/-- The right-hand companion of E255: `x*U(x)=W(x)`. -/
theorem window_mul_U {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (h255 : E255 op) (x : M) :
    op x (X6U op x) = X6W op x :=
  (window_left_unit op h677 (window_U_mul op h677 h255 x)).1

/-- The useful general identity `W(x)*(x*x)=U(x)`. -/
theorem window_W_mul_square {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (x : M) :
    op (X6W op x) (op x x) = X6U op x := by
  have he := h677 (X6W op x) x
  rw [X1_W_right_unit op h677 x] at he
  apply (L1_left_bij op h677 x).1
  exact he.symm.trans (by rfl)

/-- A right unit `r` for `x` transports the square of `x` to `U(x)`. -/
theorem window_right_unit_mul_square {M : Type u} [Finite M]
    (op : M → M → M) (h677 : E677 op) {x r : M} (hxr : op x r = x) :
    op r (op x x) = X6U op x := by
  have hr : r = X6W op x := by
    apply (L1_left_bij op h677 x).1
    exact hxr.trans (X1_W_right_unit op h677 x).symm
  rw [hr]
  exact window_W_mul_square op h677 x

/-- The collision `c=p` is equivalent to `p*p=a`. -/
theorem window_c_eq_p_iff_p_square {M : Type u} [Finite M]
    (op : M → M → M) (h677 : E677 op) (h255 : E255 op) (a : M) :
    L13C op h677 a = L13P op h677 a ↔
      op (L13P op h677 a) (L13P op h677 a) = a := by
  let p := L13P op h677 a
  let b := L13B op h677 a
  have hpa : op p a = b := L13_p_mul_a op h677 h255 a
  have hab : op a b = p := op_ldiv op h677 a p
  constructor
  · intro hcp
    have hbp : op b p = b := by
      simpa [p, b, hcp] using L13_b_mul_c op h677 h255 a
    have he := h677 a p
    rw [hpa, hbp, hab] at he
    exact he.symm
  · intro hpp
    have he := h677 a p
    change a = op p (op a (op (op p a) p)) at he
    rw [hpa] at he
    have hmid : p = op a (op b p) := by
      apply (L1_left_bij op h677 p).1
      exact hpp.trans he
    have hbp : op b p = b := by
      apply (L1_left_bij op h677 a).1
      exact hmid.symm.trans hab.symm
    apply (L1_left_bij op h677 b).1
    exact (L13_b_mul_c op h677 h255 a).trans hbp.symm

/-- A surjective homomorphism of finite E677 magmas commutes with left division. -/
theorem window_map_ldiv {M : Type u} {B : Type v} [Finite M] [Finite B]
    (opM : M → M → M) (opB : B → B → B)
    (hM : E677 opM) (hB : E677 opB) (φ : M → B)
    (_hφ : Function.Surjective φ) (hhom : IsMagmaHom opM opB φ)
    (x z : M) :
    φ (ldiv opM hM x z) = ldiv opB hB (φ x) (φ z) := by
  apply ldiv_unique opB hB
  calc
    opB (φ x) (φ (ldiv opM hM x z)) = φ (opM x (ldiv opM hM x z)) :=
      (hhom x (ldiv opM hM x z)).symm
    _ = φ z := congrArg φ (op_ldiv opM hM x z)

/-- A surjective homomorphism commutes with `W,U,P,F`. -/
theorem window_map_WUPF {M : Type u} {B : Type v} [Finite M] [Finite B]
    (opM : M → M → M) (opB : B → B → B)
    (hM : E677 opM) (hB : E677 opB) (φ : M → B)
    (hφ : Function.Surjective φ) (hhom : IsMagmaHom opM opB φ) (x : M) :
    φ (X6W opM x) = X6W opB (φ x) ∧
    φ (X6U opM x) = X6U opB (φ x) ∧
    φ (X6P opM hM x) = X6P opB hB (φ x) ∧
    φ (L12F opM hM x) = L12F opB hB (φ x) := by
  have hU : φ (X6U opM x) = X6U opB (φ x) := by
    unfold X6U
    rw [hhom, hhom]
  have hW : φ (X6W opM x) = X6W opB (φ x) := by
    unfold X6W
    rw [hhom, hU]
  have hP : φ (X6P opM hM x) = X6P opB hB (φ x) := by
    simp only [X6P, window_map_ldiv opM opB hM hB φ hφ hhom, hU]
  have hF : φ (L12F opM hM x) = L12F opB hB (φ x) := by
    simp only [L12F, window_map_ldiv opM opB hM hB φ hφ hhom]
  exact ⟨hW, hU, hP, hF⟩

/-- A surjective homomorphism commutes with all six pattern coordinates. -/
theorem window_map_pattern {M : Type u} {B : Type v} [Finite M] [Finite B]
    (opM : M → M → M) (opB : B → B → B)
    (hM : E677 opM) (hB : E677 opB) (φ : M → B)
    (hφ : Function.Surjective φ) (hhom : IsMagmaHom opM opB φ) (a : M) :
    φ (L13U opM a) = L13U opB (φ a) ∧
    φ (L13P opM hM a) = L13P opB hB (φ a) ∧
    φ (L13B opM hM a) = L13B opB hB (φ a) ∧
    φ (L13V opM hM a) = L13V opB hB (φ a) ∧
    φ (L13C opM hM a) = L13C opB hB (φ a) ∧
    φ (L13W opM a) = L13W opB (φ a) := by
  have hU : φ (L13U opM a) = L13U opB (φ a) := by
    unfold L13U
    rw [hhom, hhom]
  have hP : φ (L13P opM hM a) = L13P opB hB (φ a) := by
    simp only [L13P, window_map_ldiv opM opB hM hB φ hφ hhom, hU]
  have hB' : φ (L13B opM hM a) = L13B opB hB (φ a) := by
    simp only [L13B, window_map_ldiv opM opB hM hB φ hφ hhom, hP]
  have hV : φ (L13V opM hM a) = L13V opB hB (φ a) := by
    unfold L13V L13D
    rw [hhom, hhom, hB']
  have hC : φ (L13C opM hM a) = L13C opB hB (φ a) := by
    unfold L13C
    rw [hhom, hB', hV]
  have hW : φ (L13W opM a) = L13W opB (φ a) := by
    unfold L13W
    rw [hhom, hU]
  exact ⟨hU, hP, hB', hV, hC, hW⟩

/-- `L14X6` lifts from a quotient point `U(x)` to `U(x̃)` for every lift `x̃`. -/
theorem window_lift_X6 {M : Type u} {B : Type v} [Finite M] [Finite B]
    (opM : M → M → M) (opB : B → B → B)
    (hM : E677 opM) (hB : E677 opB) (φ : M → B)
    (hφ : Function.Surjective φ) (hhom : IsMagmaHom opM opB φ)
    (x : B) (xLift : M) (hxLift : φ xLift = x)
    (hx6 : L14X6 opB hB (X6U opB x)) :
    L14X6 opM hM (X6U opM xLift) := by
  let aM := X6U opM xLift
  let aB := X6U opB x
  have ha : φ aM = aB := by
    rw [(window_map_WUPF opM opB hM hB φ hφ hhom xLift).2.1, hxLift]
  have hp := window_map_pattern opM opB hM hB φ hφ hhom aM
  rcases hp with ⟨hU, hP, hB', hV, hC, hW⟩
  rw [ha] at hU hP hB' hV hC hW
  rcases hx6 with ⟨hvw, hvu, hca, hcw, hcu, hcp⟩
  unfold L14X6
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩
  · intro h; apply hvw; rw [← hV, ← hW]; exact congrArg φ h
  · intro h; apply hvu; rw [← hV, ← hU]; exact congrArg φ h
  · intro h
    apply hca
    calc
      L13C opB hB aB = φ (L13C opM hM aM) := hC.symm
      _ = φ aM := congrArg φ h
      _ = aB := ha
  · intro h; apply hcw; rw [← hC, ← hW]; exact congrArg φ h
  · intro h; apply hcu; rw [← hC, ← hU]; exact congrArg φ h
  · intro h; apply hcp; rw [← hC, ← hP]; exact congrArg φ h

/-- The twenty certified products in an R46 window. -/
def WindowEntries20 {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (a : M) : Prop :=
  op a (L13W op a) = a ∧
  op a (L13U op a) = L13W op a ∧
  op a (L13P op h677 a) = L13U op a ∧
  op a (L13B op h677 a) = L13P op h677 a ∧
  op a (L13D op h677 a) = L13B op h677 a ∧
  op (L13U op a) a = a ∧
  op (L13U op a) (L13B op h677 a) = L13B op h677 a ∧
  op (L13U op a) (L13P op h677 a) = L13P op h677 a ∧
  op (L13P op h677 a) a = L13B op h677 a ∧
  op (L13P op h677 a) (L13P op h677 a) = a ∧
  op (L13P op h677 a) (L13D op h677 a) = L13U op a ∧
  op (L13P op h677 a) (WindowE op h677 a) = L13P op h677 a ∧
  op (L13P op h677 a) (L13U op a) = WindowE op h677 a ∧
  op (L13B op h677 a) (L13B op h677 a) = L13D op h677 a ∧
  op (L13B op h677 a) (L13P op h677 a) = L13B op h677 a ∧
  op (L13B op h677 a) (L13U op a) = L13P op h677 a ∧
  op (L13D op h677 a) (L13B op h677 a) = L13U op a ∧
  op (WindowE op h677 a) a = L13U op a ∧
  op (L13W op a) a = L13P op h677 a ∧
  op (L13D op h677 a) (L13U op a) = a

/-- All twenty window entries follow from E677, E255, and `v=u ∧ c=p`. -/
theorem window_entries20 {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (h255 : E255 op) (a : M)
    (hwin : WindowPred op h677 a) : WindowEntries20 op h677 a := by
  rcases hwin with ⟨hvu, hcp⟩
  have haw : op a (L13W op a) = a := X1_W_right_unit op h677 a
  have hau : op a (L13U op a) = L13W op a := rfl
  have hap : op a (L13P op h677 a) = L13U op a := op_ldiv op h677 _ _
  have hab : op a (L13B op h677 a) = L13P op h677 a := op_ldiv op h677 _ _
  have had := L13_a_mul_d op h677 h255 a
  have hua := L13_u_mul_a op h677 h255 a
  have hub : op (L13U op a) (L13B op h677 a) = L13B op h677 a := by
    simpa only [hvu] using L13_v_mul_b op h677 h255 a
  have hpa := L13_p_mul_a op h677 h255 a
  have hpp := (window_c_eq_p_iff_p_square op h677 h255 a).1 hcp
  have hbp : op (L13B op h677 a) (L13P op h677 a) = L13B op h677 a := by
    simpa only [hcp] using L13_b_mul_c op h677 h255 a
  have hbu : op (L13B op h677 a) (L13U op a) = L13P op h677 a := by
    rw [← hvu, ← hcp]
    rfl
  have hdb : op (L13D op h677 a) (L13B op h677 a) = L13U op a := by
    change L13V op h677 a = L13U op a
    exact hvu
  have hdu : op (L13D op h677 a) (L13U op a) = a := by
    simpa only [hvu] using L13_d_mul_v op h677 h255 a
  have hUp : X6U op (L13P op h677 a) = L13U op a := by
    simp only [X6U, hpp, hap]
  have hup : op (L13U op a) (L13P op h677 a) = L13P op h677 a := by
    rw [← hUp]
    exact window_U_mul op h677 h255 _
  have hpu : op (L13P op h677 a) (L13U op a) = WindowE op h677 a := by
    rw [← hUp]
    rfl
  have hpe : op (L13P op h677 a) (WindowE op h677 a) = L13P op h677 a :=
    X1_W_right_unit op h677 _
  have hea : op (WindowE op h677 a) a = L13U op a := by
    change op (X6W op (L13P op h677 a)) a = L13U op a
    calc
      op (X6W op (L13P op h677 a)) a =
          op (X6W op (L13P op h677 a))
            (op (L13P op h677 a) (L13P op h677 a)) := congrArg _ hpp.symm
      _ = X6U op (L13P op h677 a) := window_W_mul_square op h677 _
      _ = L13U op a := hUp
  have hpd : op (L13P op h677 a) (L13D op h677 a) = L13U op a := by
    have ht := window_right_unit_mul_square op h677 hbp
    change op (L13P op h677 a) (L13D op h677 a) = L13U op a
    rw [← hvu]
    exact ht
  have hwa : op (L13W op a) a = L13P op h677 a := by
    have hk := key_identity op h677 (L13U op a) a
    have hda : ldiv op h677 a (L13U op a) = L13P op h677 a := rfl
    have hdu' : ldiv op h677 (L13U op a) (L13P op h677 a) =
        L13P op h677 a := (ldiv_unique op h677 hup).symm
    rw [hda, hdu'] at hk
    exact hk
  unfold WindowEntries20
  exact ⟨haw, hau, hap, hab, had, hua, hub, hup, hpa, hpp, hpd,
    hpe, hpu, rfl, hbp, hbu, hdb, hea, hwa, hdu⟩

#print axioms window_left_unit
#print axioms window_U_mul
#print axioms window_fixed_iff_U
#print axioms window_mul_U
#print axioms window_W_mul_square
#print axioms window_right_unit_mul_square
#print axioms window_c_eq_p_iff_p_square
#print axioms window_map_ldiv
#print axioms window_map_WUPF
#print axioms window_map_pattern
#print axioms window_lift_X6
#print axioms window_entries20

end Ext677
