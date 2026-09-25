import Ext677Core7Hand
import Mathlib.Tactic

/-!
# Minimal-counterexample fibre bounds

`IsCounterexample`, defined in `Ext677Quot`, is the conjunction `E677 op ∧ ¬ E255 op`.
The definition below records the quotient property needed by the headline argument.

A counterexample of minimum finite cardinality satisfies this definition: every surjective,
noninjective homomorphic image is strictly smaller, while a nonconstant image is nontrivial;
E677 descends along the surjection, so cardinal minimality forces E255 on the image.
-/

namespace Ext677

open Function

universe u

/-- Every proper nontrivial quotient of the counterexample satisfies E255. -/
def IsMinimalCounterexample {M : Type u} [Finite M] (op : M → M → M) : Prop :=
  IsCounterexample op ∧
    ∀ (B : Type u) [Finite B] (opB : B → B → B) (φ : M → B),
      Function.Surjective φ → IsMagmaHom op opB φ →
      (∃ x y, φ x = φ y ∧ x ≠ y) →
      (∃ b, ∀ m, φ m = b) ∨ E255 opB

/-- Cardinal-minimal counterexamples have the quotient property in
`IsMinimalCounterexample`. -/
theorem minimal_of_min_card {M : Type u} [Finite M] (op : M → M → M)
    (hcounter : IsCounterexample op)
    (hminimal : ∀ (B : Type u) [Finite B], Nat.card B < Nat.card M →
      ∀ opB : B → B → B, ¬ IsCounterexample opB) :
    IsMinimalCounterexample op := by
  refine ⟨hcounter, ?_⟩
  intro B _ opB φ hφ hhom hcollision
  by_cases hconst : ∃ b, ∀ m, φ m = b
  · exact Or.inl hconst
  · right
    have hnotinj : ¬ Function.Injective φ := by
      rintro hinj
      obtain ⟨x, y, hxy, hne⟩ := hcollision
      exact hne (hinj hxy)
    letI : Fintype M := Fintype.ofFinite M
    letI : Fintype B := Fintype.ofFinite B
    have hcard : Nat.card B < Nat.card M := by
      simpa only [Nat.card_eq_fintype_card] using
        Fintype.card_lt_of_surjective_not_injective φ hφ hnotinj
    have hB677 : E677 opB :=
      L7a_E677_of_surjective_hom op opB hcounter.1 φ hφ hhom
    by_contra hB255
    exact hminimal B hcard opB ⟨hB677, hB255⟩

/-- All fibres of a finite surjective E677 homomorphism have equal cardinality. -/
theorem equal_fibres {M B : Type u} [Finite M] [Finite B]
    (opM : M → M → M) (opB : B → B → B)
    (hM : E677 opM) (hB : E677 opB)
    (φ : M → B) (hφ : Function.Surjective φ)
    (hhom : IsMagmaHom opM opB φ) (x y : B) :
    Nat.card {m : M // φ m = x} = Nat.card {m : M // φ m = y} :=
  L2_quotient_fibres opM opB hM hB φ hφ hhom x y

/-- A proper nontrivial quotient of a minimal counterexample has no fibre of
size zero through three; equivalently every fibre has at least four elements. -/
theorem minimal_counterexample_no_class_two_or_three
    {M B : Type u} [Finite M] [Finite B]
    (opM : M → M → M) (opB : B → B → B)
    (hmin : IsMinimalCounterexample opM)
    (hB : E677 opB) (φ : M → B) (hφ : Function.Surjective φ)
    (hhom : IsMagmaHom opM opB φ)
    (hnotconst : ¬ ∃ b, ∀ m, φ m = b)
    (hnotinj : ¬ Function.Injective φ) (b : B) :
    4 ≤ Nat.card {m : M // φ m = b} := by
  have hcollision : ∃ x y, φ x = φ y ∧ x ≠ y := by
    rw [Function.Injective] at hnotinj
    push Not at hnotinj
    exact hnotinj
  have h255 : E255 opB := by
    rcases hmin.2 B opB φ hφ hhom hcollision with hconst | h255
    · exact (hnotconst hconst).elim
    · exact h255
  obtain ⟨x, y, hxy, hne⟩ := hcollision
  let bx : B := φ x
  let fx : {m : M // φ m = bx} := ⟨x, rfl⟩
  let fy : {m : M // φ m = bx} := ⟨y, hxy.symm⟩
  have hfxy : fx ≠ fy := by
    intro h
    exact hne (congrArg Subtype.val h)
  have htwo : 1 < Nat.card {m : M // φ m = bx} :=
    Finite.one_lt_card_iff_nontrivial.mpr ⟨⟨fx, fy, hfxy⟩⟩
  have hcard : Nat.card {m : M // φ m = b} = Nat.card {m : M // φ m = bx} :=
    equal_fibres opM opB hmin.1.1 hB φ hφ hhom b bx
  have hone : 1 < Nat.card {m : M // φ m = b} := by
    rw [hcard]
    exact htwo
  have hne2 : Nat.card {m : M // φ m = b} ≠ 2 := by
    intro hb
    exact fibre2_exclusion opM opB hmin.1.1 hB h255 φ hφ hhom b hb
  have hne3 : Nat.card {m : M // φ m = b} ≠ 3 := by
    intro hb
    exact fibre3_exclusion opM opB hmin.1.1 hB h255 φ hφ hhom b hb
  omega

/-- Consequently the total cardinality is at least four times that of every
proper nontrivial quotient. -/
theorem minimal_counterexample_card_ge_four_mul
    {M B : Type u} [Finite M] [Finite B]
    (opM : M → M → M) (opB : B → B → B)
    (hmin : IsMinimalCounterexample opM)
    (hB : E677 opB) (φ : M → B) (hφ : Function.Surjective φ)
    (hhom : IsMagmaHom opM opB φ)
    (hnotconst : ¬ ∃ b, ∀ m, φ m = b)
    (hnotinj : ¬ Function.Injective φ) :
    4 * Nat.card B ≤ Nat.card M := by
  have hcollision : ∃ x y, φ x = φ y ∧ x ≠ y := by
    rw [Function.Injective] at hnotinj
    push Not at hnotinj
    exact hnotinj
  obtain ⟨x, y, hxy, hne⟩ := hcollision
  let b : B := φ x
  let m := Nat.card {z : M // φ z = b}
  have hfibres (q : B) : Nat.card {z : M // φ z = q} = m :=
    equal_fibres opM opB hmin.1.1 hB φ hφ hhom q b
  have hm : 4 ≤ m :=
    minimal_counterexample_no_class_two_or_three opM opB hmin hB φ hφ hhom
      hnotconst hnotinj b
  obtain ⟨Fib, _, e, _, hFib, _, _, _, _⟩ :=
    L7_coordinatization opM opB hmin.1.1 φ hφ hhom m hfibres
  have hfactor : Nat.card M = Nat.card B * m := by
    calc
      Nat.card M = Nat.card (B × Fib) := Nat.card_congr e
      _ = Nat.card B * Nat.card Fib := by simp
      _ = Nat.card B * m := by rw [hFib]
  rw [hfactor, Nat.mul_comm 4 (Nat.card B)]
  exact Nat.mul_le_mul_left (Nat.card B) hm

/-- Every class of a proper nontrivial congruence of a minimal counterexample
has at least four elements. -/
theorem minimal_counterexample_congruence_class_ge_four
    {M : Type u} [Finite M] (op : M → M → M)
    (hmin : IsMinimalCounterexample op) (θ : MagmaCongruence op)
    (hnotTrivial : ¬ θ.IsTrivial) (hnotTotal : ¬ θ.IsTotal)
    (q : MagmaQuotient θ) :
    4 ≤ Nat.card {m : M // quotientMap θ m = q} := by
  have hB : E677 (quotientOp θ) :=
    L7a_E677_of_surjective_hom op (quotientOp θ) hmin.1.1
      (quotientMap θ) (quotientMap_surjective_hom θ).1
      (quotientMap_surjective_hom θ).2
  have hnotinj : ¬ Function.Injective (quotientMap θ) := by
    intro hinj
    apply hnotTrivial
    intro x y hxy
    exact hinj (Quotient.sound hxy)
  have hnotconst : ¬ ∃ q, ∀ m, quotientMap θ m = q := by
    rintro ⟨q, hq⟩
    apply hnotTotal
    intro x y
    exact Quotient.exact ((hq x).trans (hq y).symm)
  exact minimal_counterexample_no_class_two_or_three op (quotientOp θ) hmin hB
    (quotientMap θ) (quotientMap_surjective_hom θ).1
    (quotientMap_surjective_hom θ).2 hnotconst hnotinj q

/-- The corresponding quotient cardinality bound in congruence language. -/
theorem minimal_counterexample_congruence_card_ge_four_mul
    {M : Type u} [Finite M] (op : M → M → M)
    (hmin : IsMinimalCounterexample op) (θ : MagmaCongruence op)
    (hnotTrivial : ¬ θ.IsTrivial) (hnotTotal : ¬ θ.IsTotal) :
    4 * Nat.card (MagmaQuotient θ) ≤ Nat.card M := by
  have hB : E677 (quotientOp θ) :=
    L7a_E677_of_surjective_hom op (quotientOp θ) hmin.1.1
      (quotientMap θ) (quotientMap_surjective_hom θ).1
      (quotientMap_surjective_hom θ).2
  have hnotinj : ¬ Function.Injective (quotientMap θ) := by
    intro hinj
    apply hnotTrivial
    intro x y hxy
    exact hinj (Quotient.sound hxy)
  have hnotconst : ¬ ∃ q, ∀ m, quotientMap θ m = q := by
    rintro ⟨q, hq⟩
    apply hnotTotal
    intro x y
    exact Quotient.exact ((hq x).trans (hq y).symm)
  exact minimal_counterexample_card_ge_four_mul op (quotientOp θ) hmin hB
    (quotientMap θ) (quotientMap_surjective_hom θ).1
    (quotientMap_surjective_hom θ).2 hnotconst hnotinj

/-! ## Clean headline corollaries

These variants follow the hand-checked Core-7 exclusion from `Ext677Core7Hand`,
while the legacy declarations above remain available for compatibility.
-/

/-- Clean version of `minimal_counterexample_no_class_two_or_three`. -/
theorem minimal_counterexample_no_class_two_or_three_clean
    {M B : Type u} [Finite M] [Finite B]
    (opM : M → M → M) (opB : B → B → B)
    (hmin : IsMinimalCounterexample opM)
    (hB : E677 opB) (φ : M → B) (hφ : Function.Surjective φ)
    (hhom : IsMagmaHom opM opB φ)
    (hnotconst : ¬ ∃ b, ∀ m, φ m = b)
    (hnotinj : ¬ Function.Injective φ) (b : B) :
    4 ≤ Nat.card {m : M // φ m = b} := by
  have hcollision : ∃ x y, φ x = φ y ∧ x ≠ y := by
    rw [Function.Injective] at hnotinj
    push Not at hnotinj
    exact hnotinj
  have h255 : E255 opB := by
    rcases hmin.2 B opB φ hφ hhom hcollision with hconst | h255
    · exact (hnotconst hconst).elim
    · exact h255
  obtain ⟨x, y, hxy, hne⟩ := hcollision
  let bx : B := φ x
  let fx : {m : M // φ m = bx} := ⟨x, rfl⟩
  let fy : {m : M // φ m = bx} := ⟨y, hxy.symm⟩
  have hfxy : fx ≠ fy := by
    intro h
    exact hne (congrArg Subtype.val h)
  have htwo : 1 < Nat.card {m : M // φ m = bx} :=
    Finite.one_lt_card_iff_nontrivial.mpr ⟨⟨fx, fy, hfxy⟩⟩
  have hcard : Nat.card {m : M // φ m = b} = Nat.card {m : M // φ m = bx} :=
    equal_fibres opM opB hmin.1.1 hB φ hφ hhom b bx
  have hone : 1 < Nat.card {m : M // φ m = b} := by
    rw [hcard]
    exact htwo
  have hne23 : ¬ (Nat.card {m : M // φ m = b} = 2 ∨
      Nat.card {m : M // φ m = b} = 3) := by
    intro hb
    exact fibre_two_or_three_exclusion_clean opM opB hmin.1.1 hB h255
      φ hφ hhom b hb
  omega

/-- Clean version of `minimal_counterexample_card_ge_four_mul`. -/
theorem minimal_counterexample_card_ge_four_mul_clean
    {M B : Type u} [Finite M] [Finite B]
    (opM : M → M → M) (opB : B → B → B)
    (hmin : IsMinimalCounterexample opM)
    (hB : E677 opB) (φ : M → B) (hφ : Function.Surjective φ)
    (hhom : IsMagmaHom opM opB φ)
    (hnotconst : ¬ ∃ b, ∀ m, φ m = b)
    (hnotinj : ¬ Function.Injective φ) :
    4 * Nat.card B ≤ Nat.card M := by
  have hcollision : ∃ x y, φ x = φ y ∧ x ≠ y := by
    rw [Function.Injective] at hnotinj
    push Not at hnotinj
    exact hnotinj
  obtain ⟨x, _, _, _⟩ := hcollision
  let b : B := φ x
  let m := Nat.card {z : M // φ z = b}
  have hfibres (q : B) : Nat.card {z : M // φ z = q} = m :=
    equal_fibres opM opB hmin.1.1 hB φ hφ hhom q b
  have hm : 4 ≤ m :=
    minimal_counterexample_no_class_two_or_three_clean opM opB hmin hB φ hφ hhom
      hnotconst hnotinj b
  obtain ⟨Fib, _, e, _, hFib, _, _, _, _⟩ :=
    L7_coordinatization opM opB hmin.1.1 φ hφ hhom m hfibres
  have hfactor : Nat.card M = Nat.card B * m := by
    calc
      Nat.card M = Nat.card (B × Fib) := Nat.card_congr e
      _ = Nat.card B * Nat.card Fib := by simp
      _ = Nat.card B * m := by rw [hFib]
  rw [hfactor, Nat.mul_comm 4 (Nat.card B)]
  exact Nat.mul_le_mul_left (Nat.card B) hm

/-- Clean version of `minimal_counterexample_congruence_class_ge_four`. -/
theorem minimal_counterexample_congruence_class_ge_four_clean
    {M : Type u} [Finite M] (op : M → M → M)
    (hmin : IsMinimalCounterexample op) (θ : MagmaCongruence op)
    (hnotTrivial : ¬ θ.IsTrivial) (hnotTotal : ¬ θ.IsTotal)
    (q : MagmaQuotient θ) :
    4 ≤ Nat.card {m : M // quotientMap θ m = q} := by
  have hB : E677 (quotientOp θ) :=
    L7a_E677_of_surjective_hom op (quotientOp θ) hmin.1.1
      (quotientMap θ) (quotientMap_surjective_hom θ).1
      (quotientMap_surjective_hom θ).2
  have hnotinj : ¬ Function.Injective (quotientMap θ) := by
    intro hinj
    apply hnotTrivial
    intro x y hxy
    exact hinj (Quotient.sound hxy)
  have hnotconst : ¬ ∃ q, ∀ m, quotientMap θ m = q := by
    rintro ⟨q, hq⟩
    apply hnotTotal
    intro x y
    exact Quotient.exact ((hq x).trans (hq y).symm)
  exact minimal_counterexample_no_class_two_or_three_clean op (quotientOp θ) hmin hB
    (quotientMap θ) (quotientMap_surjective_hom θ).1
    (quotientMap_surjective_hom θ).2 hnotconst hnotinj q

/-- Clean version of `minimal_counterexample_congruence_card_ge_four_mul`. -/
theorem minimal_counterexample_congruence_card_ge_four_mul_clean
    {M : Type u} [Finite M] (op : M → M → M)
    (hmin : IsMinimalCounterexample op) (θ : MagmaCongruence op)
    (hnotTrivial : ¬ θ.IsTrivial) (hnotTotal : ¬ θ.IsTotal) :
    4 * Nat.card (MagmaQuotient θ) ≤ Nat.card M := by
  have hB : E677 (quotientOp θ) :=
    L7a_E677_of_surjective_hom op (quotientOp θ) hmin.1.1
      (quotientMap θ) (quotientMap_surjective_hom θ).1
      (quotientMap_surjective_hom θ).2
  have hnotinj : ¬ Function.Injective (quotientMap θ) := by
    intro hinj
    apply hnotTrivial
    intro x y hxy
    exact hinj (Quotient.sound hxy)
  have hnotconst : ¬ ∃ q, ∀ m, quotientMap θ m = q := by
    rintro ⟨q, hq⟩
    apply hnotTotal
    intro x y
    exact Quotient.exact ((hq x).trans (hq y).symm)
  exact minimal_counterexample_card_ge_four_mul_clean op (quotientOp θ) hmin hB
    (quotientMap θ) (quotientMap_surjective_hom θ).1
    (quotientMap_surjective_hom θ).2 hnotconst hnotinj

#print axioms minimal_of_min_card
#print axioms equal_fibres
#print axioms minimal_counterexample_no_class_two_or_three
#print axioms minimal_counterexample_card_ge_four_mul
#print axioms minimal_counterexample_congruence_class_ge_four
#print axioms minimal_counterexample_congruence_card_ge_four_mul
#print axioms minimal_counterexample_no_class_two_or_three_clean
#print axioms minimal_counterexample_card_ge_four_mul_clean
#print axioms minimal_counterexample_congruence_class_ge_four_clean
#print axioms minimal_counterexample_congruence_card_ge_four_mul_clean

end Ext677
