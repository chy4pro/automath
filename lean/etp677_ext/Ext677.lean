import Mathlib.Data.Finite.Prod
import Mathlib.Data.Fintype.Card
import Mathlib.SetTheory.Cardinal.Finite

/-!
# The E677 pair-indexed extension reduction

This file formalizes the interpretation lemmas used by the finite extension search for
Equation 677 implies Equation 255. No algebraic laws are hidden in type classes: every
magma operation and every identity is an explicit argument.
-/

namespace Ext677

open Function

universe u v

/-- Equation 677: `x = y * (x * ((y * x) * y))`. -/
def E677 {α : Type u} (op : α → α → α) : Prop :=
  ∀ x y, x = op y (op x (op (op y x) y))

/-- Equation 255 at one point: `x = ((x * x) * x) * x`. -/
def E255At {α : Type u} (op : α → α → α) (x : α) : Prop :=
  x = op (op (op x x) x) x

/-- Equation 255 at every point. -/
def E255 {α : Type u} (op : α → α → α) : Prop :=
  ∀ x, E255At op x

/-- L1. Every left translation in a finite E677 magma is bijective. -/
theorem L1_left_bij {M : Type u} [Finite M] (op : M → M → M) (h677 : E677 op) (y : M) :
    Function.Bijective (op y) := by
  have hsurj : Function.Surjective (op y) := by
    intro x
    refine ⟨op x (op (op y x) y), ?_⟩
    exact (h677 x y).symm
  exact ⟨Finite.injective_iff_surjective.mpr hsurj, hsurj⟩

/-- The left translation as an equivalence. -/
noncomputable def leftEquiv {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (y : M) : M ≃ M :=
  Equiv.ofBijective (op y) (L1_left_bij op h677 y)

/-- Left division, defined by the inverse left translation. -/
noncomputable def ldiv {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (y x : M) : M :=
  (leftEquiv op h677 y).symm x

set_option warning.simp.varHead false in
@[simp] theorem op_ldiv {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (y x : M) :
    op y (ldiv op h677 y x) = x :=
  (leftEquiv op h677 y).apply_symm_apply x

theorem ldiv_unique {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) {y x z : M} (hz : op y z = x) :
    z = ldiv op h677 y x := by
  apply (L1_left_bij op h677 y).1
  simpa using hz

/-- A homomorphism between two explicitly presented magmas. -/
def IsMagmaHom {M : Type u} {B : Type v} (opM : M → M → M) (opB : B → B → B)
    (f : M → B) : Prop :=
  ∀ x y, f (opM x y) = opB (f x) (f y)

/-- L2. Fibres of a surjective homomorphism of finite E677 magmas have equal size. -/
theorem L2_quotient_fibres {M : Type u} {B : Type v} [Finite M] [Finite B]
    (opM : M → M → M) (opB : B → B → B)
    (hM : E677 opM) (hB : E677 opB) (f : M → B)
    (hf : Function.Surjective f) (hhom : IsMagmaHom opM opB f) (b₁ b₂ : B) :
    Nat.card {x : M // f x = b₁} = Nat.card {x : M // f x = b₂} := by
  classical
  obtain ⟨xM, hxM⟩ := hf b₁
  obtain ⟨yM, hyM⟩ := hf b₂
  let zM := opM yM xM
  let Hfun : M → M := fun m => opM yM (opM xM (opM zM m))
  let Kfun : B → B := fun b => opB b₂ (opB b₁ (opB (opB b₂ b₁) b))
  have hHbij : Function.Bijective Hfun := by
    exact (L1_left_bij opM hM yM).comp
      ((L1_left_bij opM hM xM).comp (L1_left_bij opM hM zM))
  have hKbij : Function.Bijective Kfun := by
    exact (L1_left_bij opB hB b₂).comp
      ((L1_left_bij opB hB b₁).comp (L1_left_bij opB hB (opB b₂ b₁)))
  have hmap (m : M) : f (Hfun m) = Kfun (f m) := by
    simp only [Hfun, Kfun]
    rw [hhom, hhom, hhom, hhom, hxM, hyM]
  have hKb₂ : Kfun b₂ = b₁ := by
    exact (hB b₁ b₂).symm
  let H : M ≃ M := Equiv.ofBijective Hfun hHbij
  let fibreMap : {x : M // f x = b₂} → {x : M // f x = b₁} := fun x =>
    ⟨H x.1, by
      change f (Hfun x.1) = b₁
      rw [hmap, x.2, hKb₂]⟩
  have hfibreBij : Function.Bijective fibreMap := by
    constructor
    · intro x y hxy
      apply Subtype.ext
      exact H.injective (congrArg Subtype.val hxy)
    · intro y
      let x : M := H.symm y.1
      have hxbase : f x = b₂ := by
        apply hKbij.1
        rw [← hmap x]
        have hxH : Hfun x = y.1 := by
          change H x = y.1
          exact H.apply_symm_apply y.1
        rw [hxH, y.2, hKb₂]
      exact ⟨⟨x, hxbase⟩, by apply Subtype.ext; exact H.apply_symm_apply y.1⟩
  exact (Nat.card_congr (Equiv.ofBijective fibreMap hfibreBij)).symm

/-- The pair-indexed product operation. -/
def productOp {B : Type u} {M : Type v} (opB : B → B → B)
    (c : B → B → M → M → M) : B × M → B × M → B × M
  | (x, s), (y, t) => (opB x y, c x y s t)

/-- One `(x,y)` instance of blueprint equation (4). -/
def Eq4At {B : Type u} {M : Type v} [Finite B] (opB : B → B → B)
    (hB : E677 opB) (c : B → B → M → M → M) (x y : B) : Prop :=
  ∀ s t,
    s = c y (ldiv opB hB y x) t
      (c x (opB (opB y x) y) s (c (opB y x) y (c y x t s) t))

/-- The full pair-indexed equation (4). -/
def Eq4 {B : Type u} {M : Type v} [Finite B] (opB : B → B → B)
    (hB : E677 opB) (c : B → B → M → M → M) : Prop :=
  ∀ x y, Eq4At opB hB c x y

/-- The first inner base coordinate in E677 is exactly `y \ x`. -/
theorem e677_inner_eq_ldiv {B : Type u} [Finite B] (opB : B → B → B)
    (hB : E677 opB) (x y : B) :
    opB x (opB (opB y x) y) = ldiv opB hB y x := by
  apply ldiv_unique opB hB
  exact (hB x y).symm

/-- L3. E677 on the product is equivalent to blueprint equation (4). -/
theorem L3_eq4_iff {B : Type u} {M : Type v} [Finite B]
    (opB : B → B → B) (hB : E677 opB) (c : B → B → M → M → M) :
    E677 (productOp opB c) ↔ Eq4 opB hB c := by
  constructor
  · intro hprod x y s t
    have h := congrArg Prod.snd (hprod (x, s) (y, t))
    simpa [productOp, e677_inner_eq_ldiv opB hB x y] using h
  · intro hc p q
    rcases p with ⟨x, s⟩
    rcases q with ⟨y, t⟩
    apply Prod.ext
    · simpa [productOp] using hB x y
    · have h := hc x y s t
      simpa [productOp, e677_inner_eq_ldiv opB hB x y] using h

/-- The KEY identity in left-division form. -/
theorem key_identity {M : Type u} [Finite M] (op : M → M → M) (h677 : E677 op)
    (x y : M) :
    op (op y x) y = ldiv op h677 x (ldiv op h677 y x) := by
  apply ldiv_unique op h677
  apply ldiv_unique op h677
  exact (h677 x y).symm

/-- A right product is determined by left division. -/
theorem right_product_formula {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (v y : M) :
    op v y = ldiv op h677 (ldiv op h677 y v)
      (ldiv op h677 y (ldiv op h677 y v)) := by
  simpa using key_identity op h677 (ldiv op h677 y v) y

/-- The diagonal candidate is the second inverse-left-translation iterate. -/
theorem diagonal_candidate {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (y : M) :
    op (op y y) y = ldiv op h677 y (ldiv op h677 y y) := by
  apply ldiv_unique op h677
  apply ldiv_unique op h677
  exact (h677 y y).symm

/-- A left unit determines the corresponding right product. -/
theorem left_unit_right_product {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) {w y : M} (hw : op w y = y) :
    op y w = ldiv op h677 y y := by
  rw [right_product_formula op h677 y w]
  have hwy : ldiv op h677 w y = y := by
    symm
    exact ldiv_unique op h677 hw
  rw [hwy, hwy]

/-- In an E677 finite magma, a point has at most one left unit. -/
theorem left_unit_unique {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) {x y z : M} (hy : op y x = x) (hz : op z x = x) : y = z := by
  apply (L1_left_bij op h677 x).1
  rw [left_unit_right_product op h677 hy, left_unit_right_product op h677 hz]

/-- Pointwise form of blueprint Lemma 13.1(ii). -/
theorem e255At_iff_exists_left_unit {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) (x : M) :
    E255At op x ↔ ∃ y, op y x = x := by
  constructor
  · intro h255
    exact ⟨op (op x x) x, h255.symm⟩
  · rintro ⟨y, hy⟩
    have hyright : op x y = ldiv op h677 x x :=
      left_unit_right_product op h677 hy
    have hdiag : op (op x x) x = ldiv op h677 x (ldiv op h677 x x) :=
      diagonal_candidate op h677 x
    have hcandidate : y = op (op x x) x := by
      apply (L1_left_bij op h677 x).1
      rw [hyright, hdiag, op_ldiv op h677 x (ldiv op h677 x x)]
    exact (hcandidate ▸ hy).symm

/-- L4. Product E255 failure is exactly a missing fixed value in the star block. -/
theorem L4_defect_iff {B : Type u} {M : Type v} [Finite B] [Finite M]
    (opB : B → B → B) (hB : E677 opB) (h255B : E255 opB)
    (c : B → B → M → M → M) (hprod : E677 (productOp opB c))
    (a : B) (σ : M) :
    let x_a := opB (opB a a) a
    ¬ E255At (productOp opB c) (a, σ) ↔ ¬ ∃ s, c x_a a s σ = σ := by
  dsimp only
  rw [e255At_iff_exists_left_unit (productOp opB c) hprod]
  constructor
  · intro hleft ⟨s, hs⟩
    apply hleft
    refine ⟨(opB (opB a a) a, s), ?_⟩
    apply Prod.ext
    · exact (h255B a).symm
    · exact hs
  · intro hstar ⟨p, hp⟩
    rcases p with ⟨x, s⟩
    have hx : opB x a = a := congrArg Prod.fst hp
    have hxa : opB (opB (opB a a) a) a = a := (h255B a).symm
    have : x = opB (opB a a) a := left_unit_unique opB hB hx hxa
    apply hstar
    refine ⟨s, ?_⟩
    simpa [productOp, this] using congrArg Prod.snd hp

/-- An automorphism of an explicitly presented magma. -/
structure MagmaAut {B : Type u} (opB : B → B → B) where
  toEquiv : B ≃ B
  map_op : ∀ x y, toEquiv (opB x y) = opB (toEquiv x) (toEquiv y)

instance {B : Type u} {opB : B → B → B} : CoeFun (MagmaAut opB) (fun _ => B → B) :=
  ⟨fun φ => φ.toEquiv⟩

/-- An automorphism commutes with left division. -/
theorem map_ldiv {B : Type u} [Finite B] (opB : B → B → B) (hB : E677 opB)
    (φ : MagmaAut opB) (y x : B) :
    φ (ldiv opB hB y x) = ldiv opB hB (φ y) (φ x) := by
  apply ldiv_unique opB hB
  rw [← φ.map_op, op_ldiv opB hB y x]

/-- Transport a fibre family along a base automorphism. -/
def transport {B : Type u} {M : Type v} {opB : B → B → B}
    (φ : MagmaAut opB) (c : B → B → M → M → M) : B → B → M → M → M :=
  fun x y => c (φ x) (φ y)

/-- L5. Equation (4) and the defect level transport along any base automorphism. -/
theorem L5_transport {B : Type u} {M : Type v} [Finite B]
    (opB : B → B → B) (hB : E677 opB) (c : B → B → M → M → M)
    (φ : MagmaAut opB) (hc : Eq4 opB hB c) :
    Eq4 opB hB (transport φ c) ∧
      ∀ a σ, (¬ E255At (productOp opB (transport φ c)) (a, σ) ↔
        ¬ E255At (productOp opB c) (φ a, σ)) := by
  constructor
  · intro x y s t
    have h := hc (φ x) (φ y) s t
    simpa [Eq4At, transport, map_ldiv opB hB φ, φ.map_op] using h
  · intro a σ
    let Φ : B × M ≃ B × M := φ.toEquiv.prodCongr (Equiv.refl M)
    have hpoint : E255At (productOp opB (transport φ c)) (a, σ) ↔
        E255At (productOp opB c) (φ a, σ) := by
      constructor
      · intro h
        unfold E255At at h ⊢
        have hmapped := congrArg Φ h
        simpa [Φ, productOp, transport, φ.map_op] using hmapped
      · intro h
        unfold E255At at h ⊢
        apply Φ.injective
        simpa [Φ, productOp, transport, φ.map_op] using h
    exact not_congr hpoint

/-- L6. At an idempotent base level, equation (4) and E255 reduce to the fibre operation. -/
theorem L6_idempotent_level {B : Type u} {M : Type v} [Finite B]
    (opB : B → B → B) (hB : E677 opB) (c : B → B → M → M → M)
    (a : B) (ha : opB a a = a) :
    (Eq4At opB hB c a a ↔ E677 (c a a)) ∧
      ∀ σ, (E255At (productOp opB c) (a, σ) ↔ E255At (c a a) σ) := by
  have hdiv : ldiv opB hB a a = a := by
    symm
    exact ldiv_unique opB hB ha
  constructor
  · simp [Eq4At, E677, hdiv, ha]
  · intro σ
    simp [E255At, productOp, ha]

#print axioms L1_left_bij
#print axioms L2_quotient_fibres
#print axioms L3_eq4_iff
#print axioms L4_defect_iff
#print axioms L5_transport
#print axioms L6_idempotent_level

end Ext677
