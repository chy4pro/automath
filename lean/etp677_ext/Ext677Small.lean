import Ext677Quot
import Mathlib.Tactic

/-!
# Small-order exclusions and the idempotent-free quotient corollary
-/

namespace Ext677

universe u v

/-- There is no E677 operation on a two-element type. -/
theorem no_E677_Fin2 : ∀ op : Fin 2 → Fin 2 → Fin 2, ¬ E677 op := by
  change ∀ op : Fin 2 → Fin 2 → Fin 2,
    ¬ ∀ x y, x = op y (op x (op (op y x) y))
  decide

/-- There is no E677 operation on a three-element type. -/
theorem no_E677_Fin3 : ∀ op : Fin 3 → Fin 3 → Fin 3, ¬ E677 op := by
  change ∀ op : Fin 3 → Fin 3 → Fin 3,
    ¬ ∀ x y, x = op y (op x (op (op y x) y))
  -- `native_decide` is used for the 3^9 operation tables; see the axiom audit.
  native_decide

/-- L11(b). If all fibres of a finite surjective E677 homomorphism have common
cardinality two or three, then the quotient/base has no idempotents. -/
theorem L11_base_idempotent_free_of_fibre_card_two_or_three
    {N : Type u} {B : Type v} [Finite N] [Finite B]
    (opN : N → N → N) (opB : B → B → B) (hN : E677 opN)
    (f : N → B) (hf : Function.Surjective f) (hhom : IsMagmaHom opN opB f)
    (m : ℕ) (hm : m = 2 ∨ m = 3)
    (hfibre : ∀ b : B, Nat.card {x : N // f x = b} = m) :
    ∀ a, opB a a ≠ a := by
  classical
  let hB : E677 opB := L7a_E677_of_surjective_hom opN opB hN f hf hhom
  obtain ⟨Fib, hFibFinite, _, c, hFibCard, _, _, _, hEq4⟩ :=
    L7_coordinatization opN opB hN f hf hhom m hfibre
  let _ : Finite Fib := hFibFinite
  intro a ha
  have hFib677 : E677 (c a a) :=
    (L6_idempotent_level opB hB c a ha).1.mp (hEq4 a a)
  let eFib : Fib ≃ Fin m := Finite.equivFinOfCardEq hFibCard
  let opFin : Fin m → Fin m → Fin m := transportOpEquiv eFib (c a a)
  have hFin677 : E677 opFin := E677_transportOpEquiv eFib (c a a) hFib677
  rcases hm with rfl | rfl
  · exact no_E677_Fin2 opFin hFin677
  · exact no_E677_Fin3 opFin hFin677

/-- L11(c). A congruence quotient whose classes all have cardinality two or three
is idempotent-free. -/
theorem L11_quotient_idempotent_free_of_class_card_two_or_three
    {N : Type u} [Finite N] [Nonempty N] (opN : N → N → N) (hN : E677 opN)
    (θ : MagmaCongruence opN)
    (hsmall : ∀ q : MagmaQuotient θ,
      Nat.card {x : N // quotientMap θ x = q} = 2 ∨
        Nat.card {x : N // quotientMap θ x = q} = 3) :
    ∀ q, quotientOp θ q q ≠ q := by
  classical
  let qmap : N → MagmaQuotient θ := quotientMap θ
  let q₀ : MagmaQuotient θ := qmap (Classical.choice inferInstance)
  let m := Nat.card {x : N // qmap x = q₀}
  have hm : m = 2 ∨ m = 3 := hsmall q₀
  have hfibres : ∀ q : MagmaQuotient θ,
      Nat.card {x : N // qmap x = q} = m := by
    intro q
    exact L2_quotient_fibres opN (quotientOp θ) hN
      (L7a_E677_of_surjective_hom opN (quotientOp θ) hN qmap
        (quotientMap_surjective_hom θ).1 (quotientMap_surjective_hom θ).2)
      qmap (quotientMap_surjective_hom θ).1 (quotientMap_surjective_hom θ).2 q q₀
  exact L11_base_idempotent_free_of_fibre_card_two_or_three
    opN (quotientOp θ) hN qmap (quotientMap_surjective_hom θ).1
      (quotientMap_surjective_hom θ).2 m hm hfibres

#print axioms no_E677_Fin2
#print axioms no_E677_Fin3
#print axioms L11_base_idempotent_free_of_fibre_card_two_or_three
#print axioms L11_quotient_idempotent_free_of_class_card_two_or_three

end Ext677
