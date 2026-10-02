import Mathlib

/-!
Finite real Gram energies with explicit supports.

The two coefficient arrays may be signed and may use different finite supports.
The common outer support must contain every feature needed by an application;
identifying that support for an integer convolution is a separate lemma.
No convergence, measure theory, or coefficient positivity is used here.
-/

noncomputable section

open scoped BigOperators

namespace Sidon30

variable {α ζ : Type*}

/-- The finite linear transform of an array supported on `S`. -/
def finiteTransform (S : Finset α) (H : ζ → α → ℝ) (μ : α → ℝ)
    (z : ζ) : ℝ :=
  ∑ x ∈ S, H z x * μ x

/-- The Gram kernel of the features `H`, restricted to the outer support `Z`. -/
def finiteGramKernel (Z : Finset ζ) (H : ζ → α → ℝ) (x y : α) : ℝ :=
  ∑ z ∈ Z, H z x * H z y

/-- Cross energy of two finite, possibly signed, coefficient arrays. -/
def finiteGramEnergy (Z : Finset ζ) (S T : Finset α)
    (H : ζ → α → ℝ) (μ ν : α → ℝ) : ℝ :=
  ∑ z ∈ Z, finiteTransform S H μ z * finiteTransform T H ν z

/-- A real Gram kernel is symmetric. -/
theorem finiteGramKernel_symm (Z : Finset ζ) (H : ζ → α → ℝ)
    (x y : α) :
    finiteGramKernel Z H x y = finiteGramKernel Z H y x := by
  unfold finiteGramKernel
  apply Finset.sum_congr rfl
  intro z _hz
  exact mul_comm _ _

/-- Every diagonal entry of a real Gram kernel is nonnegative. -/
theorem finiteGramKernel_self_nonneg (Z : Finset ζ) (H : ζ → α → ℝ)
    (x : α) :
    0 ≤ finiteGramKernel Z H x x := by
  unfold finiteGramKernel
  exact Finset.sum_nonneg (fun z _hz => mul_self_nonneg (H z x))

/-- Symmetry includes swapping the coefficient supports. -/
theorem finiteGramEnergy_symm (Z : Finset ζ) (S T : Finset α)
    (H : ζ → α → ℝ) (μ ν : α → ℝ) :
    finiteGramEnergy Z S T H μ ν = finiteGramEnergy Z T S H ν μ := by
  unfold finiteGramEnergy
  apply Finset.sum_congr rfl
  intro z _hz
  exact mul_comm _ _

/-- Self energy is a finite sum of squares. -/
theorem finiteGramEnergy_self_eq_sum_sq (Z : Finset ζ) (S : Finset α)
    (H : ζ → α → ℝ) (μ : α → ℝ) :
    finiteGramEnergy Z S S H μ μ =
      ∑ z ∈ Z, (finiteTransform S H μ z) ^ 2 := by
  simp only [finiteGramEnergy, pow_two]

/-- Self energy is nonnegative even for signed coefficients. -/
theorem finiteGramEnergy_self_nonneg (Z : Finset ζ) (S : Finset α)
    (H : ζ → α → ℝ) (μ : α → ℝ) :
    0 ≤ finiteGramEnergy Z S S H μ μ := by
  unfold finiteGramEnergy
  exact Finset.sum_nonneg
    (fun z _hz => mul_self_nonneg (finiteTransform S H μ z))

/-- Finite energy Cauchy--Schwarz, with no sign restriction on either array. -/
theorem finiteGramEnergy_cauchySchwarz (Z : Finset ζ) (S T : Finset α)
    (H : ζ → α → ℝ) (μ ν : α → ℝ) :
    (finiteGramEnergy Z S T H μ ν) ^ 2 ≤
      finiteGramEnergy Z S S H μ μ * finiteGramEnergy Z T T H ν ν := by
  simpa only [finiteGramEnergy, pow_two] using
    (Finset.sum_mul_sq_le_sq_mul_sq Z
      (finiteTransform S H μ) (finiteTransform T H ν))

/-- Expanding the transforms gives the double sum against the Gram kernel. -/
theorem finiteGramEnergy_eq_kernel_sum (Z : Finset ζ) (S T : Finset α)
    (H : ζ → α → ℝ) (μ ν : α → ℝ) :
    finiteGramEnergy Z S T H μ ν =
      ∑ x ∈ S, ∑ y ∈ T, μ x * ν y * finiteGramKernel Z H x y := by
  unfold finiteGramEnergy finiteTransform finiteGramKernel
  calc
    (∑ z ∈ Z, (∑ x ∈ S, H z x * μ x) * (∑ y ∈ T, H z y * ν y)) =
        ∑ z ∈ Z, ∑ x ∈ S, ∑ y ∈ T,
          μ x * ν y * (H z x * H z y) := by
      apply Finset.sum_congr rfl
      intro z _hz
      rw [Finset.sum_mul_sum]
      apply Finset.sum_congr rfl
      intro x _hx
      apply Finset.sum_congr rfl
      intro y _hy
      ring
    _ = ∑ x ∈ S, ∑ y ∈ T, ∑ z ∈ Z,
          μ x * ν y * (H z x * H z y) := by
      rw [Finset.sum_comm]
      apply Finset.sum_congr rfl
      intro x _hx
      rw [Finset.sum_comm]
    _ = ∑ x ∈ S, ∑ y ∈ T, μ x * ν y * (∑ z ∈ Z, H z x * H z y) := by
      apply Finset.sum_congr rfl
      intro x _hx
      apply Finset.sum_congr rfl
      intro y _hy
      rw [Finset.mul_sum]

end Sidon30

end
