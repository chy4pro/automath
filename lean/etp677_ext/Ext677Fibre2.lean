import Ext677Window
import Ext677Quot
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic

/-!
# Exclusion of two-element fibres

This file formalizes registry R46, Step 48.  The proof first transports fibres
by left translations, then normalizes every permutation of a two-element fibre
to an affine map over `ZMod 2`.  The fibre coordinates of E677 force two
coefficient identities, whose four specializations under E255 contradict one
another.
-/

namespace Ext677

open Function

universe u v

/-! ## F1: transport of fibres -/

/-- Left multiplication by `m` is an equivalence from the fibre over `y` to
the fibre over `φ(m) * y`. -/
noncomputable def fibreLeftEquiv
    {M : Type u} {B : Type v} [Finite M] [Finite B]
    (opM : M → M → M) (opB : B → B → B)
    (hM : E677 opM) (hB : E677 opB)
    (φ : M → B) (hhom : IsMagmaHom opM opB φ)
    (m : M) (y : B) :
    {z : M // φ z = y} ≃ {z : M // φ z = opB (φ m) y} where
  toFun z := ⟨opM m z, by rw [hhom, z.2]⟩
  invFun z := ⟨ldiv opM hM m z, by
    apply (L1_left_bij opB hB (φ m)).1
    calc
      opB (φ m) (φ (ldiv opM hM m z)) =
          φ (opM m (ldiv opM hM m z)) := (hhom _ _).symm
      _ = φ z := congrArg φ (op_ldiv opM hM m z)
      _ = opB (φ m) y := z.2⟩
  left_inv z := by
    apply Subtype.ext
    exact (ldiv_unique opM hM rfl).symm
  right_inv z := by
    apply Subtype.ext
    exact op_ldiv opM hM m z

/-- Fibre cardinality is preserved by a single left translation. -/
theorem fibre_card_mul_left
    {M : Type u} {B : Type v} [Finite M] [Finite B]
    (opM : M → M → M) (opB : B → B → B)
    (hM : E677 opM) (hB : E677 opB)
    (φ : M → B) (hhom : IsMagmaHom opM opB φ)
    (m : M) (y : B) :
    Nat.card {z : M // φ z = y} =
      Nat.card {z : M // φ z = opB (φ m) y} :=
  Nat.card_congr (fibreLeftEquiv opM opB hM hB φ hhom m y)

/-- In particular, a two-element fibre transports to the six base points used
in the Step-48 window.  The existing `L2_quotient_fibres` proves the stronger
fact that all fibres of a finite surjective E677 homomorphism have equal size. -/
theorem fibre_cards_WUPFS_eq_two
    {M : Type u} {B : Type v} [Finite M] [Finite B]
    (opM : M → M → M) (opB : B → B → B)
    (hM : E677 opM) (hB : E677 opB)
    (φ : M → B) (hφ : Function.Surjective φ)
    (hhom : IsMagmaHom opM opB φ) (x : B)
    (hx : Nat.card {m : M // φ m = x} = 2) :
    Nat.card {m : M // φ m = X6W opB x} = 2 ∧
    Nat.card {m : M // φ m = X6U opB x} = 2 ∧
    Nat.card {m : M // φ m = X6P opB hB x} = 2 ∧
    Nat.card {m : M // φ m = L12F opB hB x} = 2 ∧
    Nat.card {m : M // φ m = opB x x} = 2 := by
  have hall (y : B) : Nat.card {m : M // φ m = y} = 2 :=
    (L2_quotient_fibres opM opB hM hB φ hφ hhom y x).trans hx
  exact ⟨hall _, hall _, hall _, hall _, hall _⟩

/-! ## F2: affine coordinates on a two-element fibre -/

abbrev Fibre2 := ZMod 2

/-- Every function on `ZMod 2` is affine. -/
theorem fibre2_function_affine (g : Fibre2 → Fibre2) (t : Fibre2) :
    g t = g 0 + (g 1 - g 0) * t := by
  revert g t
  decide

/-- Every permutation of `ZMod 2` is translation by its value at zero. -/
theorem fibre2_injective_eq_add_const (g : Fibre2 → Fibre2)
    (hg : Function.Injective g) (t : Fibre2) :
    g t = t + g 0 := by
  revert g t
  decide

/-- The affine pair-indexed operation on two-element fibres. -/
def fibre2AffineOp {B : Type u} (opB : B → B → B)
    (A D : B → B → Fibre2) :
    B × Fibre2 → B × Fibre2 → B × Fibre2
  | (x, s), (y, t) => (opB x y, t + A x y * s + D x y)

/-- Constant coefficient of an arbitrary pair-indexed two-point fibre law. -/
def fibre2Const {B : Type u}
    (c : B → B → Fibre2 → Fibre2 → Fibre2) (x y : B) : Fibre2 :=
  c x y 0 0

/-- Linear coefficient of an arbitrary pair-indexed two-point fibre law. -/
def fibre2Slope {B : Type u}
    (c : B → B → Fibre2 → Fibre2 → Fibre2) (x y : B) : Fibre2 :=
  c x y 1 0 - c x y 0 0

/-- Permutation rows on a two-element fibre have the advertised affine form. -/
theorem fibre2_row_affine {B : Type u}
    (c : B → B → Fibre2 → Fibre2 → Fibre2)
    (hinj : ∀ x y s, Function.Injective (c x y s))
    (x y : B) (s t : Fibre2) :
    c x y s t =
      t + fibre2Slope c x y * s + fibre2Const c x y := by
  calc
    c x y s t = t + c x y s 0 :=
      fibre2_injective_eq_add_const (c x y s) (hinj x y s) t
    _ = t + (c x y 0 0 + (c x y 1 0 - c x y 0 0) * s) := by
      rw [fibre2_function_affine (fun z ↦ c x y z 0) s]
    _ = t + fibre2Slope c x y * s + fibre2Const c x y := by
      simp only [fibre2Slope, fibre2Const]
      ring

/-! ## F3: coefficient identities forced by E677 -/

theorem fibre2_extract_s (z a b : Fibre2)
    (h0 : 0 = z) (h1 : 1 = z + a + b) : a + b = 1 := by
  revert z a b
  decide

theorem fibre2_extract_t (z a b : Fibre2)
    (h0 : 0 = z) (h1 : 0 = 1 + z + a + b) : b + a = 1 := by
  revert z a b
  decide

/-- The two linear coefficient identities obtained from E677 at `(r,s),(q,t)`.
They are Step 48's equations (I) and (II). -/
theorem fibre2_coefficients {B : Type u}
    (opB : B → B → B) (A D : B → B → Fibre2)
    (hprod : E677 (fibre2AffineOp opB A D)) (r q : B) :
    A (opB q r) q + A r (opB (opB q r) q) = 1 ∧
    A q (opB r (opB (opB q r) q)) + A (opB q r) q * A q r = 1 := by
  have h00 := congrArg Prod.snd (hprod (r, 0) (q, 0))
  have h10 := congrArg Prod.snd (hprod (r, 1) (q, 0))
  have h01 := congrArg Prod.snd (hprod (r, 0) (q, 1))
  simp only [fibre2AffineOp] at h00 h10 h01
  let k : Fibre2 :=
    A (opB q r) q * D q r + D (opB q r) q +
      D r (opB (opB q r) q) + D q (opB r (opB (opB q r) q))
  have hk0 : (0 : Fibre2) = k := by
    dsimp only [k]
    linear_combination h00
  have hk10 : (1 : Fibre2) =
      k + A (opB q r) q + A r (opB (opB q r) q) := by
    dsimp only [k]
    linear_combination h10
  have hk01 : (0 : Fibre2) =
      1 + k + A (opB q r) q * A q r +
        A q (opB r (opB (opB q r) q)) := by
    dsimp only [k]
    linear_combination h01
  constructor
  · exact fibre2_extract_s k _ _ hk0 hk10
  · exact fibre2_extract_t k _ _ hk0 hk01

theorem fibre2_factor_eq_one (a b : Fibre2)
    (h : a + b * a = 1) : a = 1 ∧ b = 0 := by
  revert a b
  decide

/-! ## F4: the four E255 specializations -/

/-- For every base point, the diagonal linear coefficient is zero. -/
theorem fibre2_diagonal_slope_zero
    {B : Type u} [Finite B]
    (opB : B → B → B) (hB : E677 opB) (h255 : E255 opB)
    (A D : B → B → Fibre2)
    (hprod : E677 (fibre2AffineOp opB A D)) (z : B) :
    A z z = 0 := by
  let u := X6U opB z
  let w := X6W opB z
  have huz : opB u z = z := window_U_mul opB hB h255 z
  have hzu : opB z u = w := window_mul_U opB hB h255 z
  have hzw : opB z w = z := X1_W_right_unit opB hB z
  rcases fibre2_coefficients opB A D hprod z u with ⟨hIzu, hIIzu⟩
  rw [huz, hzu] at hIzu hIIzu
  rw [hzw] at hIIzu
  obtain ⟨hAuz, hAzu⟩ := fibre2_factor_eq_one (A u z) (A z u) hIIzu
  have hAzw : A z w = 1 := by simpa [hAzu] using hIzu
  rcases fibre2_coefficients opB A D hprod z z with ⟨hIzz, hIIzz⟩
  have hszu : opB (opB z z) z = u := rfl
  rw [hszu, hAzu] at hIzz
  have hAsz : A (opB z z) z = 1 := by simpa using hIzz
  rw [hszu, hzu, hAzw, hAsz] at hIIzz
  simpa using hIIzz

/-- The pair-indexed affine FIBRE-2 exclusion theorem. -/
theorem fibre2_affine_exclusion
    {B : Type u} [Finite B]
    (opB : B → B → B) (hB : E677 opB) (h255 : E255 opB)
    (A D : B → B → Fibre2)
    (hprod : E677 (fibre2AffineOp opB A D)) (x : B) : False := by
  let u := X6U opB x
  let w := X6W opB x
  let p := X6P opB hB x
  let f := L12F opB hB x
  have hux : opB u x = x := window_U_mul opB hB h255 x
  have hxu : opB x u = w := window_mul_U opB hB h255 x
  have hxw : opB x w = x := X1_W_right_unit opB hB x
  have hxp : opB x p = u := op_ldiv opB hB x u
  have hxf : opB x f = p := by
    rw [show f = ldiv opB hB x p from X1_F_iterate opB hB x]
    exact op_ldiv opB hB x p
  have hpx : opB p x = f := by
    have hk := key_identity opB hB p x
    rw [hxp, hux, show ldiv opB hB x p = f from (X1_F_iterate opB hB x).symm] at hk
    calc
      opB p x = opB p (ldiv opB hB p f) := congrArg (opB p) hk
      _ = f := op_ldiv opB hB p f
  rcases fibre2_coefficients opB A D hprod x u with ⟨hIxu, hIIxu⟩
  rw [hux, hxu] at hIxu hIIxu
  rw [hxw] at hIIxu
  obtain ⟨hAux, hAxu⟩ := fibre2_factor_eq_one (A u x) (A x u) hIIxu
  rcases fibre2_coefficients opB A D hprod p x with ⟨hIpx, _⟩
  rw [hxp, hux, hAux] at hIpx
  have hApx : A p x = 0 := by simpa using hIpx
  have hAff : A f f = 0 := fibre2_diagonal_slope_zero opB hB h255 A D hprod f
  rcases fibre2_coefficients opB A D hprod f x with ⟨hIfx, _⟩
  rw [hxf, hpx, hApx, hAff] at hIfx
  exact zero_ne_one hIfx

/-- Pair-indexed form without an affine hypothesis: permutation rows are
automatically normalized by `fibre2_row_affine`. -/
theorem fibre2_pair_indexed_exclusion
    {B : Type u} [Finite B]
    (opB : B → B → B) (hB : E677 opB) (h255 : E255 opB)
    (c : B → B → Fibre2 → Fibre2 → Fibre2)
    (hinj : ∀ x y s, Function.Injective (c x y s))
    (hprod : E677 (productOp opB c)) (x : B) : False := by
  let A := fibre2Slope c
  let D := fibre2Const c
  have hop : productOp opB c = fibre2AffineOp opB A D := by
    funext p q
    rcases p with ⟨r, s⟩
    rcases q with ⟨z, t⟩
    apply Prod.ext
    · rfl
    · exact fibre2_row_affine c hinj r z s t
  apply fibre2_affine_exclusion opB hB h255 A D (hop ▸ hprod) x

/-! ## Assembly: the original fibre theorem -/

/-- FIBRE-2 EXCLUSION THEOREM (registry R46, Step 48).

No finite surjective homomorphism from an E677 magma to an E677+E255 magma
can have a fibre of cardinality two. -/
theorem fibre2_exclusion
    {M : Type u} {B : Type v} [Finite M] [Finite B]
    (opM : M → M → M) (opB : B → B → B)
    (hM : E677 opM) (hB : E677 opB) (h255 : E255 opB)
    (φ : M → B) (hφ : Function.Surjective φ)
    (hhom : IsMagmaHom opM opB φ) (x : B)
    (hx : Nat.card {m : M // φ m = x} = 2) : False := by
  classical
  have hfibres (y : B) : Nat.card {m : M // φ m = y} = 2 :=
    (L2_quotient_fibres opM opB hM hB φ hφ hhom y x).trans hx
  obtain ⟨Fib, hFibFinite, _e, c, hFibCard, _hefst, _heop, hinj, hEq4⟩ :=
    L7_coordinatization opM opB hM φ hφ hhom 2 hfibres
  let _ : Finite Fib := hFibFinite
  let eFin : Fib ≃ Fin 2 := Finite.equivFinOfCardEq hFibCard
  let e2 : Fib ≃ Fibre2 := eFin.trans (ZMod.finEquiv 2).toEquiv
  let c2 : B → B → Fibre2 → Fibre2 → Fibre2 := fun r q s t ↦
    e2 (c r q (e2.symm s) (e2.symm t))
  have hinj2 : ∀ r q s, Function.Injective (c2 r q s) := by
    intro r q s t₁ t₂ ht
    apply e2.symm.injective
    apply hinj r q (e2.symm s)
    exact e2.injective ht
  have hprod : E677 (productOp opB c) :=
    (L3_eq4_iff opB hB c).2 hEq4
  let E : B × Fib ≃ B × Fibre2 := Equiv.prodCongr (Equiv.refl B) e2
  have htransport : transportOpEquiv E (productOp opB c) = productOp opB c2 := by
    funext p q
    rcases p with ⟨r, s⟩
    rcases q with ⟨z, t⟩
    apply Prod.ext
    · rfl
    · simp [transportOpEquiv, productOp, E, c2]
  have hprod2 : E677 (productOp opB c2) := by
    rw [← htransport]
    exact E677_transportOpEquiv E (productOp opB c) hprod
  exact fibre2_pair_indexed_exclusion opB hB h255 c2 hinj2 hprod2 x

/-- Quotient/congruence corollary: no class of a finite E677 magma can have
cardinality two when the induced quotient satisfies E255. -/
theorem fibre2_quotient_class_ne_two
    {M : Type u} [Finite M]
    (opM : M → M → M) (hM : E677 opM)
    (θ : MagmaCongruence opM) (h255 : E255 (quotientOp θ))
    (x : MagmaQuotient θ) :
    Nat.card {m : M // quotientMap θ m = x} ≠ 2 := by
  intro hx
  exact fibre2_exclusion opM (quotientOp θ) hM
    (L7a_E677_of_surjective_hom opM (quotientOp θ) hM
      (quotientMap θ) (quotientMap_surjective_hom θ).1
      (quotientMap_surjective_hom θ).2)
    h255 (quotientMap θ) (quotientMap_surjective_hom θ).1
    (quotientMap_surjective_hom θ).2 x hx

#print axioms fibreLeftEquiv
#print axioms fibre_card_mul_left
#print axioms fibre_cards_WUPFS_eq_two
#print axioms fibre2_function_affine
#print axioms fibre2_injective_eq_add_const
#print axioms fibre2_row_affine
#print axioms fibre2_extract_s
#print axioms fibre2_extract_t
#print axioms fibre2_coefficients
#print axioms fibre2_factor_eq_one
#print axioms fibre2_diagonal_slope_zero
#print axioms fibre2_affine_exclusion
#print axioms fibre2_pair_indexed_exclusion
#print axioms fibre2_exclusion
#print axioms fibre2_quotient_class_ne_two

end Ext677
