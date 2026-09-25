import Ext677Quot

/-!
# The final glue lemma for the E677 extension reduction

This file combines L7/L8 with the pointwise defect lemmas L4/L6. A nonsimple
cardinal-minimal counterexample is coordinatized over a proper E255 quotient, and its
defect must occur over a non-idempotent base level.
-/

namespace Ext677

open Function

universe u

/-- L9. A nonsimple cardinal-minimal counterexample admits proper base/fibre product
coordinates whose E255 defect lies over a non-idempotent base level. -/
theorem L9_nonsimple_minimal_counterexample_glue {N : Type u} [Finite N]
    (opN : N → N → N) (hcounter : IsCounterexample opN)
    (hminimal : ∀ k, k < Nat.card N → ∀ op : Fin k → Fin k → Fin k,
      ¬ IsCounterexample op)
    (hnotsimple : ¬ IsSimple opN) :
    ∃ (B : Type u) (_ : Finite B) (Fib : Type) (_ : Finite Fib)
      (opB : B → B → B) (hB677 : E677 opB) (_hB255 : E255 opB)
      (c : B → B → Fib → Fib → Fib) (e : N ≃ B × Fib) (a : B) (σ : Fib),
      1 < Nat.card B ∧ Nat.card B < Nat.card N ∧
      1 < Nat.card Fib ∧ Nat.card Fib < Nat.card N ∧
      (∀ x y s, Function.Bijective (c x y s)) ∧
      Eq4 opB hB677 c ∧
      (∀ x y, e (opN x y) = productOp opB c (e x) (e y)) ∧
      (¬ ∃ s, c (opB (opB a a) a) a s σ = σ) ∧
      opB a a ≠ a := by
  classical
  rcases L8_minimal_counterexample_dichotomy opN hcounter hminimal with
    hsimple | ⟨θ, _, _, hBcard, hBproper, hB677, hB255,
      m, hmcard, hmproper, hfibres, _⟩
  · exact (hnotsimple hsimple).elim
  · obtain ⟨Fib, hFibFinite, e, c, hFibCard, _, he_op, hc_injective, hEq4⟩ :=
      L7_coordinatization opN (quotientOp θ) hcounter.1
        (quotientMap θ) (quotientMap_surjective_hom θ).1
        (quotientMap_surjective_hom θ).2 m hfibres
    let _ : Finite Fib := hFibFinite
    have hFibCardOne : 1 < Nat.card Fib := by
      rw [hFibCard]
      exact hmcard
    have hFibCardProper : Nat.card Fib < Nat.card N := by
      rw [hFibCard]
      exact hmproper
    have hc_bijective : ∀ x y s, Function.Bijective (c x y s) := by
      intro x y s
      have hinj := hc_injective x y s
      exact ⟨hinj, Finite.injective_iff_surjective.mp hinj⟩
    have hProduct677 : E677 (productOp (quotientOp θ) c) :=
      (L3_eq4_iff (quotientOp θ) hB677 c).mpr hEq4
    obtain ⟨z, hz⟩ : ∃ z, ¬ E255At opN z := by
      by_contra h
      apply hcounter.2
      intro z
      by_contra hz
      exact h ⟨z, hz⟩
    have hProductFail : ¬ E255At (productOp (quotientOp θ) c) (e z) := by
      intro hp
      apply hz
      unfold E255At at hp ⊢
      apply e.injective
      simpa only [he_op] using hp
    rcases hpair : e z with ⟨a, σ⟩
    have hPairFail : ¬ E255At (productOp (quotientOp θ) c) (a, σ) := by
      simpa only [hpair] using hProductFail
    have hMissing :
        ¬ ∃ s, c (quotientOp θ (quotientOp θ a a) a) a s σ = σ :=
      (L4_defect_iff (quotientOp θ) hB677 hB255 c hProduct677 a σ).mp hPairFail
    have hNonidempotent : quotientOp θ a a ≠ a := by
      intro haa
      have hLevel := L6_idempotent_level (quotientOp θ) hB677 c a haa
      have hFib677 : E677 (c a a) := hLevel.1.mp (hEq4 a a)
      have hFibFailAt : ¬ E255At (c a a) σ := by
        intro h255
        exact hPairFail ((hLevel.2 σ).mpr h255)
      have hFibNot255 : ¬ E255 (c a a) := by
        intro h255
        exact hFibFailAt (h255 σ)
      let f : Fib ≃ Fin (Nat.card Fib) := Finite.equivFin Fib
      let opFin : Fin (Nat.card Fib) → Fin (Nat.card Fib) → Fin (Nat.card Fib) :=
        transportOpEquiv f (c a a)
      have hFinCounter : IsCounterexample opFin := by
        constructor
        · exact E677_transportOpEquiv f (c a a) hFib677
        · intro hFin255
          exact hFibNot255 ((E255_transportOpEquiv_iff f (c a a)).mp hFin255)
      exact hminimal (Nat.card Fib) hFibCardProper opFin hFinCounter
    exact ⟨MagmaQuotient θ, inferInstance, Fib, inferInstance,
      quotientOp θ, hB677, hB255, c, e, a, σ,
      hBcard, hBproper, hFibCardOne, hFibCardProper,
      hc_bijective, hEq4, he_op, hMissing, hNonidempotent⟩

#print axioms L9_nonsimple_minimal_counterexample_glue

end Ext677
