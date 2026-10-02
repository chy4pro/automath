import Sidon30.SidonRampEnergy
import Sidon30.FiniteBoundaryPotential
import Sidon30.DiscreteSidonCertificate
import Sidon30.FinalReduction

/-!
Assembly of the actual finite signed boundary certificate.

The only remaining hypothesis is the displayed double-sum cost of that
specific certificate. Its support, exact unit potential, and the Sidon energy
upper bound are proved by the imported cards and discharged here.
-/

noncomputable section

open scoped BigOperators

namespace Sidon30

/-- The actual boundary-cost theorem supplies the complete finite Sidon
certificate. This is a conditional assembly, not an assertion of that cost. -/
theorem discreteSidonCertificate_of_boundaryCost
    (hcost : ∀ (N T : ℕ), 1 ≤ N → 1 ≤ T →
      (∑ x ∈ Finset.Icc (1 - (T : ℤ)) ((N : ℤ) + (T : ℤ) - 2),
        ∑ y ∈ Finset.Icc (1 - (T : ℤ)) ((N : ℤ) + (T : ℤ) - 2),
          boundaryCertificate N T x * boundaryCertificate N T y *
            rampCorrelation T (x - y)) ≤
        (N : ℝ) + (2 : ℝ) / 3 * ((T : ℝ) - 1) +
          29 * (T : ℝ) * ((3 : ℝ) / 4) ^ ((N - 1) / T)) :
    DiscreteSidonCertificateBound := by
  intro N T A hN hT hAN hA
  let V : Finset ℤ := Finset.Icc (1 - (T : ℤ)) ((N : ℤ) + (T : ℤ) - 2)
  let Z : Finset ℤ := Finset.Icc (1 - (T : ℤ)) ((N : ℤ) + 2 * (T : ℤ) - 3)
  let U : ℝ := 1 + rampDiagonal T * ((A.card : ℝ) - 1)
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
          (fun z x : ℤ => rampWeightInt T (z - x)) (fun _ => 1) (fun _ => 1) ≤ U :=
    rampGramEnergy_liftedSidon_le hA hT Z hZA
  have hC :
      finiteGramEnergy Z V V (fun z x : ℤ => rampWeightInt T (z - x))
          (boundaryCertificate N T) (boundaryCertificate N T) ≤ C := by
    rw [rampGramEnergy_eq T Z V V
      (boundaryCertificate N T) (boundaryCertificate N T) hZV]
    exact hcost N T hN hT
  have hbound := finiteGram_card_sq_le Z (liftedSidonSet A) V
    (fun z x : ℤ => rampWeightInt T (z - x)) (boundaryCertificate N T)
    U C hpotential hU hC
  simpa only [liftedSidonSet_card, U, C] using hbound

end Sidon30

end
