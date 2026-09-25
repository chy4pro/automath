import Ext677
import Mathlib.Data.Fintype.EquivFin
import Mathlib.Tactic

/-!
# Occurrence maps for equation (4)

Three of the four subscript maps are bijections in every finite E677 magma. The
second map is bijective exactly when all right translations are bijective; consequently
that part of the proposed unconditional L10 statement requires an extra hypothesis.
-/

namespace Ext677

open Function

universe u

/-- The canonical left unit attached to a point in an E255 magma. -/
def canonicalLeftUnit {B : Type u} (op : B → B → B) (a : B) : B :=
  op (op a a) a

/-- First base-pair subscript in equation (4). -/
noncomputable def L10P1 {B : Type u} [Finite B] (op : B → B → B)
    (h677 : E677 op) : B × B → B × B :=
  fun p => (p.2, ldiv op h677 p.2 p.1)

/-- Second base-pair subscript in equation (4). -/
def L10P2 {B : Type u} (op : B → B → B) : B × B → B × B :=
  fun p => (p.1, op (op p.2 p.1) p.2)

/-- Third base-pair subscript in equation (4). -/
def L10P3 {B : Type u} : B × B → B × B :=
  fun p => (p.2, p.1)

/-- Fourth base-pair subscript in equation (4). -/
def L10P4 {B : Type u} (op : B → B → B) : B × B → B × B :=
  fun p => (op p.2 p.1, p.2)

/-- The first subscript map as an explicit equivalence. -/
noncomputable def L10P1Equiv {B : Type u} [Finite B] (op : B → B → B)
    (h677 : E677 op) : B × B ≃ B × B where
  toFun := L10P1 op h677
  invFun := fun p => (op p.1 p.2, p.1)
  left_inv := by
    rintro ⟨x, y⟩
    apply Prod.ext
    · exact op_ldiv op h677 y x
    · rfl
  right_inv := by
    rintro ⟨x, y⟩
    apply Prod.ext
    · rfl
    · exact (ldiv_unique op h677 rfl).symm

/-- The swap subscript map as an explicit equivalence. -/
def L10P3Equiv (B : Type u) : B × B ≃ B × B :=
  Equiv.prodComm B B

/-- The fourth subscript map as an explicit equivalence. -/
noncomputable def L10P4Equiv {B : Type u} [Finite B] (op : B → B → B)
    (h677 : E677 op) : B × B ≃ B × B where
  toFun := L10P4 op
  invFun := fun p => (ldiv op h677 p.2 p.1, p.2)
  left_inv := by
    rintro ⟨x, y⟩
    apply Prod.ext
    · exact (ldiv_unique op h677 rfl).symm
    · rfl
  right_inv := by
    rintro ⟨x, y⟩
    simp [L10P4, op_ldiv]

theorem L10_P1_bijective {B : Type u} [Finite B] (op : B → B → B)
    (h677 : E677 op) : Function.Bijective (L10P1 op h677) :=
  (L10P1Equiv op h677).bijective

theorem L10_P3_bijective {B : Type u} : Function.Bijective (L10P3 : B × B → B × B) :=
  (L10P3Equiv B).bijective

theorem L10_P4_bijective {B : Type u} [Finite B] (op : B → B → B)
    (h677 : E677 op) : Function.Bijective (L10P4 op) :=
  (L10P4Equiv op h677).bijective

/-- Exact obstruction to the proposed P2 claim: P2 is bijective precisely when every
right translation is bijective. E255 is not needed for this equivalence. -/
theorem L10_P2_bijective_iff_right_bijective {B : Type u} [Finite B]
    (op : B → B → B) (h677 : E677 op) :
    Function.Bijective (L10P2 op) ↔
      ∀ w, Function.Bijective (fun y => op y w) := by
  constructor
  · intro hP2 w
    have hsurj : Function.Surjective (fun y => op y w) := by
      intro x'
      let z' := ldiv op h677 x' w
      obtain ⟨p', hp'⟩ := hP2.2 (x', z')
      rcases p' with ⟨u, y'⟩
      have hu : u = x' := congrArg Prod.fst hp'
      subst u
      have hr' : op (op y' x') y' = z' := congrArg Prod.snd hp'
      refine ⟨y', ?_⟩
      have hxz' : op x' z' = w := by simp [z', op_ldiv]
      calc
        op y' w = op y' (op x' z') := by rw [hxz']
        _ = op y' (op x' (op (op y' x') y')) := by rw [hr']
        _ = x' := (h677 x' y').symm
    exact ⟨Finite.injective_iff_surjective.mpr hsurj, hsurj⟩
  · intro hright
    have hsurj : Function.Surjective (L10P2 op) := by
      rintro ⟨x, z⟩
      obtain ⟨y, hy⟩ := (hright (op x z)).2 x
      refine ⟨(x, y), ?_⟩
      apply Prod.ext
      · rfl
      · change op (op y x) y = z
        apply (L1_left_bij op h677 x).1
        apply (L1_left_bij op h677 y).1
        exact (hy.trans (h677 x y)).symm
    exact ⟨Finite.injective_iff_surjective.mpr hsurj, hsurj⟩

/-- The four positions in the equation-(4) occurrence calculation. -/
inductive OccurrencePosition
  | first | second | third | fourth
  deriving DecidableEq

instance : Fintype OccurrencePosition where
  elems := {.first, .second, .third, .fourth}
  complete := by
    intro i
    cases i <;> simp

/-- Select one of the four equation-(4) subscript maps. -/
noncomputable def occurrenceMap {B : Type u} [Finite B] (op : B → B → B)
    (h677 : E677 op) : OccurrencePosition → B × B → B × B
  | .first => L10P1 op h677
  | .second => L10P2 op
  | .third => L10P3
  | .fourth => L10P4 op

/-- Occurrences of a target base pair, retaining the equation-(4) position. -/
def OccurrenceCertificates {B : Type u} [Finite B] (op : B → B → B)
    (h677 : E677 op) (target : B × B) :=
  Σ i : OccurrencePosition, {p : B × B // occurrenceMap op h677 i p = target}

/-- The distinct equation-(4) instances in which a target pair occurs. -/
noncomputable def occurrenceInstanceSet {B : Type u} [Fintype B] [DecidableEq B]
    (op : B → B → B) (h677 : E677 op) (target : B × B) : Finset (B × B) :=
  Finset.univ.filter fun p => ∃ i, occurrenceMap op h677 i p = target

/-- L10(b): at an idempotent level all four subscripts of `(a,a)` collapse to
`(a,a)`. -/
theorem L10_fourfold_collapse {B : Type u} [Finite B] (op : B → B → B)
    (h677 : E677 op) (a : B) (ha : op a a = a) :
    ∀ i, occurrenceMap op h677 i (a, a) = (a, a) := by
  have hdiv : ldiv op h677 a a = a := (ldiv_unique op h677 ha).symm
  intro i
  cases i <;> simp [occurrenceMap, L10P1, L10P2, L10P3, L10P4, ha, hdiv]

/-- E255 makes the canonical element `(a*a)*a` the unique left unit of `a`. -/
theorem canonicalLeftUnit_mul {B : Type u} (op : B → B → B) (h255 : E255 op)
    (a : B) : op (canonicalLeftUnit op a) a = a :=
  (h255 a).symm

theorem canonicalLeftUnit_ne_of_not_idempotent {B : Type u} (op : B → B → B)
    (h255 : E255 op) (a : B) (ha : op a a ≠ a) : canonicalLeftUnit op a ≠ a := by
  intro h
  apply ha
  have h255a := h255 a
  change a = op (canonicalLeftUnit op a) a at h255a
  rw [h] at h255a
  exact h255a.symm

/-- The unavoidable `{1,3}` collision at the instance `(a,x_a)`. -/
theorem L10_first_third_collision {B : Type u} [Finite B] (op : B → B → B)
    (h677 : E677 op) (h255 : E255 op) (a : B) :
    let x_a := canonicalLeftUnit op a
    occurrenceMap op h677 .first (a, x_a) = (x_a, a) ∧
      occurrenceMap op h677 .third (a, x_a) = (x_a, a) := by
  dsimp only
  constructor
  · apply Prod.ext
    · rfl
    · exact (ldiv_unique op h677 (canonicalLeftUnit_mul op h255 a)).symm
  · rfl

/-- A non-idempotent point and its canonical left unit cannot be mutual left units. -/
theorem canonicalLeftUnit_not_reverse {B : Type u} [Finite B] (op : B → B → B)
    (h677 : E677 op) (h255 : E255 op) (a : B) (ha : op a a ≠ a) :
    op a (canonicalLeftUnit op a) ≠ canonicalLeftUnit op a := by
  let x_a := canonicalLeftUnit op a
  have hxa : op x_a a = a := canonicalLeftUnit_mul op h255 a
  have hne : x_a ≠ a := canonicalLeftUnit_ne_of_not_idempotent op h255 a ha
  intro hax
  change op a x_a = x_a at hax
  have hxx : op x_a x_a = a := by
    have h := h677 a x_a
    rw [hxa, hax, hax] at h
    exact h.symm
  apply hne
  have h := h255 x_a
  change x_a = op (op (op x_a x_a) x_a) x_a at h
  simpa only [hxx, hax] using h

/-- Corrected L10(c). Under the necessary P2-bijectivity hypothesis, the target
`(x_a,a)` has four position-labelled occurrences and exactly three distinct source
instances, with the first and third positions colliding at `(a,x_a)`. -/
theorem L10_occurrence_trichotomy_of_P2_bijective
    {B : Type u} [Fintype B] [DecidableEq B]
    (op : B → B → B) (h677 : E677 op) (h255 : E255 op)
    (a : B) (ha : op a a ≠ a) (hP2 : Function.Bijective (L10P2 op)) :
    let x_a := canonicalLeftUnit op a
    Nat.card (OccurrenceCertificates op h677 (x_a, a)) = 4 ∧
      (occurrenceInstanceSet op h677 (x_a, a)).card = 3 ∧
      occurrenceMap op h677 .first (a, x_a) = (x_a, a) ∧
      occurrenceMap op h677 .third (a, x_a) = (x_a, a) := by
  classical
  dsimp only
  let x_a := canonicalLeftUnit op a
  let target : B × B := (x_a, a)
  let shared : B × B := (a, x_a)
  let e2 : B × B ≃ B × B := Equiv.ofBijective (L10P2 op) hP2
  let e4 : B × B ≃ B × B := L10P4Equiv op h677
  let q2 : B × B := e2.symm target
  let q4 : B × B := e4.symm target
  have hq2 : occurrenceMap op h677 .second q2 = target := by
    exact e2.apply_symm_apply target
  have hq4 : occurrenceMap op h677 .fourth q4 = target := by
    exact e4.apply_symm_apply target
  have h13 := L10_first_third_collision op h677 h255 a
  have hfirst : occurrenceMap op h677 .first shared = target := h13.1
  have hthird : occurrenceMap op h677 .third shared = target := h13.2
  have hAll : ∀ i, Function.Bijective (occurrenceMap op h677 i) := by
    intro i
    cases i
    · exact L10_P1_bijective op h677
    · exact hP2
    · exact L10_P3_bijective
    · exact L10_P4_bijective op h677
  have hFiber : ∀ i, Nat.card
      {p : B × B // occurrenceMap op h677 i p = target} = 1 := by
    intro i
    apply Nat.card_eq_one_iff_exists.mpr
    obtain ⟨q, hq⟩ := (hAll i).2 target
    refine ⟨⟨q, hq⟩, ?_⟩
    rintro ⟨p, hp⟩
    apply Subtype.ext
    exact (hAll i).1 (hp.trans hq.symm)
  have hcert : Nat.card (OccurrenceCertificates op h677 target) = 4 := by
    change Nat.card (Σ i : OccurrencePosition,
      {p : B × B // occurrenceMap op h677 i p = target}) = 4
    rw [Nat.card_sigma]
    simp_rw [hFiber]
    decide
  have hocc (p : B × B) :
      (∃ i, occurrenceMap op h677 i p = target) ↔
        p = shared ∨ p = q2 ∨ p = q4 := by
    constructor
    · rintro ⟨i, hi⟩
      cases i
      · exact Or.inl ((L10_P1_bijective op h677).1 (hi.trans hfirst.symm))
      · exact Or.inr (Or.inl (e2.injective (hi.trans hq2.symm)))
      · exact Or.inl (L10_P3_bijective.1 (hi.trans hthird.symm))
      · exact Or.inr (Or.inr (e4.injective (hi.trans hq4.symm)))
    · rintro (rfl | rfl | rfl)
      · exact ⟨.first, hfirst⟩
      · exact ⟨.second, hq2⟩
      · exact ⟨.fourth, hq4⟩
  have hxne : x_a ≠ a := canonicalLeftUnit_ne_of_not_idempotent op h255 a ha
  have hq2fst : q2.1 = x_a := congrArg Prod.fst hq2
  have hq4snd : q4.2 = a := congrArg Prod.snd hq4
  have hsharedq2 : shared ≠ q2 := by
    intro h
    apply hxne
    calc
      x_a = q2.1 := hq2fst.symm
      _ = shared.1 := congrArg Prod.fst h.symm
      _ = a := rfl
  have hsharedq4 : shared ≠ q4 := by
    intro h
    apply hxne
    calc
      x_a = shared.2 := rfl
      _ = q4.2 := congrArg Prod.snd h
      _ = a := hq4snd
  have hq2q4 : q2 ≠ q4 := by
    intro h
    have hq4fstArg : q4.1 = x_a := by
      rw [← h]
      exact hq2fst
    have hq4fst : op q4.2 q4.1 = x_a := congrArg Prod.fst hq4
    have hreverse : op a x_a = x_a := by
      simpa only [hq4snd, hq4fstArg] using hq4fst
    exact canonicalLeftUnit_not_reverse op h677 h255 a ha hreverse
  have hset : occurrenceInstanceSet op h677 target = {shared, q2, q4} := by
    ext p
    simp only [occurrenceInstanceSet, Finset.mem_filter, Finset.mem_univ, true_and,
      Finset.mem_insert, Finset.mem_singleton]
    exact hocc p
  have hinstances : (occurrenceInstanceSet op h677 target).card = 3 := by
    rw [hset]
    simp [hsharedq2, hsharedq4, hq2q4]
  exact ⟨hcert, hinstances, hfirst, hthird⟩

#print axioms L10_P1_bijective
#print axioms L10_P3_bijective
#print axioms L10_P4_bijective
#print axioms L10_P2_bijective_iff_right_bijective
#print axioms L10_fourfold_collapse
#print axioms canonicalLeftUnit_mul
#print axioms canonicalLeftUnit_ne_of_not_idempotent
#print axioms L10_first_third_collision
#print axioms canonicalLeftUnit_not_reverse
#print axioms L10_occurrence_trichotomy_of_P2_bijective

end Ext677
