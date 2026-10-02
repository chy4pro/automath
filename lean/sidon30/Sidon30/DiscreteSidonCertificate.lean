import Sidon30.FiniteEnergyCS

/-!
Generic finite Gram-certificate inequalities.

These lemmas consume an exact finite potential and explicit self-energy bounds.
They do not construct the ramp boundary certificate, prove its cost, or assert
the concrete DiscreteSidonCertificateBound proposition from FinalReduction.
The certificate and coefficient arrays may both have signed real entries.
-/

noncomputable section

open scoped BigOperators

namespace Sidon30

variable {α ζ : Type*}

/-- An exact unit potential on `S` evaluates cross energy as the total mass
of the coefficient array on `S`, even when that array is signed. -/
theorem finiteGramEnergy_eq_mass_of_potential (Z : Finset ζ) (S V : Finset α)
    (H : ζ → α → ℝ) (μ ν : α → ℝ)
    (hpotential : ∀ x ∈ S, ∑ y ∈ V, ν y * finiteGramKernel Z H x y = 1) :
    finiteGramEnergy Z S V H μ ν = ∑ x ∈ S, μ x := by
  rw [finiteGramEnergy_eq_kernel_sum]
  apply Finset.sum_congr rfl
  intro x hx
  calc
    (∑ y ∈ V, μ x * ν y * finiteGramKernel Z H x y) =
        μ x * (∑ y ∈ V, ν y * finiteGramKernel Z H x y) := by
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro y _hy
      ring
    _ = μ x := by rw [hpotential x hx, mul_one]

/-- Counting measure has cross energy equal to its cardinality. -/
theorem finiteGramEnergy_eq_card_of_potential (Z : Finset ζ) (S V : Finset α)
    (H : ζ → α → ℝ) (ν : α → ℝ)
    (hpotential : ∀ x ∈ S, ∑ y ∈ V, ν y * finiteGramKernel Z H x y = 1) :
    finiteGramEnergy Z S V H (fun _ => 1) ν = (S.card : ℝ) := by
  simpa only [Finset.sum_const, nsmul_eq_mul, mul_one] using
    (finiteGramEnergy_eq_mass_of_potential Z S V H (fun _ => 1) ν hpotential)

/-- A genuine finite Gram certificate inequality. Nonnegativity of both
self energies supplies the sign conditions when their upper bounds are multiplied. -/
theorem finiteGram_certificate_bound (Z : Finset ζ) (S V : Finset α)
    (H : ζ → α → ℝ) (μ ν : α → ℝ) (U C : ℝ)
    (hpotential : ∀ x ∈ S, ∑ y ∈ V, ν y * finiteGramKernel Z H x y = 1)
    (hU : finiteGramEnergy Z S S H μ μ ≤ U)
    (hC : finiteGramEnergy Z V V H ν ν ≤ C) :
    (∑ x ∈ S, μ x) ^ 2 ≤ C * U := by
  have hmass := finiteGramEnergy_eq_mass_of_potential Z S V H μ ν hpotential
  have hμ := finiteGramEnergy_self_nonneg Z S H μ
  have hν := finiteGramEnergy_self_nonneg Z V H ν
  calc
    (∑ x ∈ S, μ x) ^ 2 = (finiteGramEnergy Z S V H μ ν) ^ 2 := by rw [hmass]
    _ ≤ finiteGramEnergy Z S S H μ μ * finiteGramEnergy Z V V H ν ν :=
      finiteGramEnergy_cauchySchwarz Z S V H μ ν
    _ ≤ U * C := mul_le_mul hU hC hν (hμ.trans hU)
    _ = C * U := mul_comm _ _

/-- Cardinality specialization. The unit-potential and both energy bounds
remain explicit hypotheses, to be proved for the actual Sidon certificate. -/
theorem finiteGram_card_sq_le (Z : Finset ζ) (S V : Finset α)
    (H : ζ → α → ℝ) (ν : α → ℝ) (U C : ℝ)
    (hpotential : ∀ x ∈ S, ∑ y ∈ V, ν y * finiteGramKernel Z H x y = 1)
    (hU : finiteGramEnergy Z S S H (fun _ => 1) (fun _ => 1) ≤ U)
    (hC : finiteGramEnergy Z V V H ν ν ≤ C) :
    (S.card : ℝ) ^ 2 ≤ C * U := by
  simpa only [Finset.sum_const, nsmul_eq_mul, mul_one] using
    (finiteGram_certificate_bound Z S V H (fun _ => 1) ν U C hpotential hU hC)

end Sidon30

end
