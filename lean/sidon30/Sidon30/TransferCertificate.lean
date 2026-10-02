import Sidon30.SidonRampEnergy
import Sidon30.FiniteBoundaryPotential
import Sidon30.DiscreteSidonCertificate
import Sidon30.FiniteBoundaryCost
import Sidon30.RenewalErrorBound

/-!
Assembly of the actual finite signed boundary certificate.

The boundary cost and exact unit potential are supplied by the existing
proved certificate. Difference-counting estimates may be inserted separately.
-/

noncomputable section

open scoped BigOperators

namespace Sidon30

/-- The finite ramp capacity inequality for an arbitrary finite set.
No difference-multiplicity assumption is imposed here. -/
theorem ramp_card_sq_le_certificate (N T : ℕ) (A : Finset ℕ)
    (hN : 1 ≤ N) (hT : 1 ≤ T) (hAN : A ⊆ Finset.range N) :
    (A.card : ℝ) ^ 2 ≤
      ((N : ℝ) + (2 : ℝ) / 3 * ((T : ℝ) - 1) +
        29 * (T : ℝ) * ((3 : ℝ) / 4) ^ ((N - 1) / T)) *
      orderedPairEnergy A (rampCorrelation T) := by
  let V : Finset ℤ := Finset.Icc (1 - (T : ℤ)) ((N : ℤ) + (T : ℤ) - 2)
  let Z : Finset ℤ := Finset.Icc (1 - (T : ℤ)) ((N : ℤ) + 2 * (T : ℤ) - 3)
  let U : ℝ := orderedPairEnergy A (rampCorrelation T)
  let C : ℝ := (N : ℝ) + (2 : ℝ) / 3 * ((T : ℝ) - 1) +
    29 * (T : ℝ) * ((3 : ℝ) / 4) ^ ((N - 1) / T)
  have hAV : liftedSidonSet A ⊆ V := by
    intro x hx
    obtain ⟨hx0, hxN⟩ := liftedSidonSet_mem_window hAN hx
    apply Finset.mem_Icc.mpr
    constructor <;> omega
  have hZV : ∀ x ∈ V, ∀ j ∈ Finset.range T, x + (j : ℤ) ∈ Z := by
    intro x hx j hj
    obtain ⟨hxlo, hxhi⟩ := Finset.mem_Icc.mp hx
    have hjT : j < T := Finset.mem_range.mp hj
    apply Finset.mem_Icc.mpr
    constructor <;> omega
  have hZA : ∀ x ∈ liftedSidonSet A, ∀ j ∈ Finset.range T,
      x + (j : ℤ) ∈ Z := by
    intro x hx j hj
    exact hZV x (hAV hx) j hj
  have hsupport : ∀ y : ℤ, y ∉ V → boundaryCertificate N T y = 0 := by
    intro y hy
    exact boundaryCertificate_eq_zero_of_not_mem hN hT hy
  have hpotential : ∀ x ∈ liftedSidonSet A,
      (∑ y ∈ V, boundaryCertificate N T y *
        finiteGramKernel Z (fun z u : ℤ => rampWeightInt T (z - u)) x y) = 1 := by
    intro x hx
    obtain ⟨hx0, hxN⟩ := liftedSidonSet_mem_window hAN hx
    calc
      (∑ y ∈ V, boundaryCertificate N T y *
          finiteGramKernel Z (fun z u : ℤ => rampWeightInt T (z - u)) x y) =
          ∑ y ∈ V, boundaryCertificate N T y * rampCorrelation T (x - y) := by
        apply Finset.sum_congr rfl
        intro y _hy
        rw [rampGramKernel_eq T Z x y (hZA x hx)]
      _ = rampDoublePotential T (boundaryCertificate N T) x :=
        rampCorrelation_sum_eq_doublePotential_of_support T V
          (boundaryCertificate N T) x hsupport
      _ = 1 := boundaryCertificate_potential hN hT hx0 hxN
  have hU :
      finiteGramEnergy Z (liftedSidonSet A) (liftedSidonSet A)
          (fun z x : ℤ => rampWeightInt T (z - x)) (fun _ => 1) (fun _ => 1) ≤ U := by
    rw [rampGramEnergy_eq T Z (liftedSidonSet A) (liftedSidonSet A)
      (fun _ => 1) (fun _ => 1) hZA]
    simp only [one_mul]
    rw [liftedSidonSet_pairEnergy]
    exact le_rfl
  have hC :
      finiteGramEnergy Z V V (fun z x : ℤ => rampWeightInt T (z - x))
          (boundaryCertificate N T) (boundaryCertificate N T) ≤ C := by
    rw [rampGramEnergy_eq T Z V V
      (boundaryCertificate N T) (boundaryCertificate N T) hZV]
    simpa only [boundaryEnergy, boundarySupport, C, V] using
      (boundaryCertificate_energy_le (N := N) (T := T) hN hT
        (fun n hn => renewalCorrection_bound hT hn))
  have hbound := finiteGram_card_sq_le Z (liftedSidonSet A) V
    (fun z x : ℤ => rampWeightInt T (z - x)) (boundaryCertificate N T)
    U C hpotential hU hC
  simpa only [liftedSidonSet_card, U, C] using hbound

end Sidon30

end
