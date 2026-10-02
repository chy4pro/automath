import Mathlib

/-!
Exactly normalized finite ramp weights.  Every subtraction and division in a
weight is performed in the reals.  The polynomial sums below are proved by
induction, independently of any analytic summation or integration result.
-/

noncomputable section

open scoped BigOperators

namespace Sidon30

/-- The probability ramp on the natural indices `0, ..., T - 1`. -/
def rampWeight (T j : ℕ) : ℝ :=
  if j < T then
    2 * ((T : ℝ) - (j : ℝ)) / ((T : ℝ) * ((T : ℝ) + 1))
  else 0

/-- The diagonal value of the autocorrelation of the normalized ramp. -/
def rampDiagonal (T : ℕ) : ℝ :=
  2 * (2 * (T : ℝ) + 1) / (3 * (T : ℝ) * ((T : ℝ) + 1))

/-- Extension of the ramp to integer indices, with zero at negative indices. -/
def rampWeightInt (T : ℕ) (j : ℤ) : ℝ :=
  if 0 ≤ j then rampWeight T j.toNat else 0

theorem rampWeight_of_lt {T j : ℕ} (hj : j < T) :
    rampWeight T j =
      2 * ((T : ℝ) - (j : ℝ)) / ((T : ℝ) * ((T : ℝ) + 1)) := by
  simp only [rampWeight, if_pos hj]

theorem rampWeight_eq_zero_of_le {T j : ℕ} (hj : T ≤ j) :
    rampWeight T j = 0 := by
  simp only [rampWeight, if_neg (not_lt.mpr hj)]

theorem rampWeight_nonneg (T j : ℕ) : 0 ≤ rampWeight T j := by
  unfold rampWeight
  split_ifs with hj
  · have hj' : (j : ℝ) ≤ (T : ℝ) := by
      exact_mod_cast Nat.le_of_lt hj
    exact div_nonneg
      (mul_nonneg (by norm_num) (sub_nonneg.mpr hj')) (by positivity)
  · exact le_rfl

theorem rampWeight_eq_coeff_mul {T j : ℕ} (hj : j < T) :
    rampWeight T j =
      (2 / ((T : ℝ) * ((T : ℝ) + 1))) * ((T : ℝ) - (j : ℝ)) := by
  rw [rampWeight_of_lt hj]
  ring

private theorem sum_range_cast_real (n : ℕ) :
    (∑ j ∈ Finset.range n, (j : ℝ)) = (n : ℝ) * ((n : ℝ) - 1) / 2 := by
  induction n with
  | zero => norm_num
  | succ n ih =>
      rw [Finset.sum_range_succ, ih]
      push_cast
      ring

private theorem sum_range_sq_cast_real (n : ℕ) :
    (∑ j ∈ Finset.range n, (j : ℝ) ^ 2) =
      (n : ℝ) * ((n : ℝ) - 1) * (2 * (n : ℝ) - 1) / 6 := by
  induction n with
  | zero => norm_num
  | succ n ih =>
      rw [Finset.sum_range_succ, ih]
      push_cast
      ring

private theorem sum_range_ramp_numerator (T : ℕ) :
    (∑ j ∈ Finset.range T, ((T : ℝ) - (j : ℝ))) =
      (T : ℝ) * ((T : ℝ) + 1) / 2 := by
  simp only [Finset.sum_sub_distrib, Finset.sum_const, Finset.card_range,
    nsmul_eq_mul, sum_range_cast_real]
  ring

private theorem sum_range_sq_ramp_numerator (T : ℕ) :
    (∑ j ∈ Finset.range T, ((T : ℝ) - (j : ℝ)) ^ 2) =
      (T : ℝ) * ((T : ℝ) + 1) * (2 * (T : ℝ) + 1) / 6 := by
  calc
    (∑ j ∈ Finset.range T, ((T : ℝ) - (j : ℝ)) ^ 2) =
        ∑ j ∈ Finset.range T,
          ((T : ℝ) ^ 2 - (2 * (T : ℝ)) * (j : ℝ) + (j : ℝ) ^ 2) := by
      apply Finset.sum_congr rfl
      intro j _hj
      ring
    _ = (T : ℝ) * ((T : ℝ) + 1) * (2 * (T : ℝ) + 1) / 6 := by
      simp only [Finset.sum_add_distrib, Finset.sum_sub_distrib,
        ← Finset.mul_sum, Finset.sum_const, Finset.card_range, nsmul_eq_mul,
        sum_range_cast_real, sum_range_sq_cast_real]
      ring

private theorem sum_range_mul_ramp_numerator (T : ℕ) :
    (∑ j ∈ Finset.range T, (j : ℝ) * ((T : ℝ) - (j : ℝ))) =
      (T : ℝ) * ((T : ℝ) - 1) * ((T : ℝ) + 1) / 6 := by
  calc
    (∑ j ∈ Finset.range T, (j : ℝ) * ((T : ℝ) - (j : ℝ))) =
        ∑ j ∈ Finset.range T, ((T : ℝ) * (j : ℝ) - (j : ℝ) ^ 2) := by
      apply Finset.sum_congr rfl
      intro j _hj
      ring
    _ = (T : ℝ) * ((T : ℝ) - 1) * ((T : ℝ) + 1) / 6 := by
      simp only [Finset.sum_sub_distrib, ← Finset.mul_sum,
        sum_range_cast_real, sum_range_sq_cast_real]
      ring

/-- The chosen denominator gives total mass exactly one. -/
theorem sum_rampWeight {T : ℕ} (hT : 1 ≤ T) :
    (∑ j ∈ Finset.range T, rampWeight T j) = 1 := by
  have hTpos : (0 : ℝ) < (T : ℝ) := by
    exact_mod_cast (show 0 < T by omega)
  have hTne : (T : ℝ) ≠ 0 := ne_of_gt hTpos
  have hT1ne : (T : ℝ) + 1 ≠ 0 := by positivity
  calc
    (∑ j ∈ Finset.range T, rampWeight T j) =
        (2 / ((T : ℝ) * ((T : ℝ) + 1))) *
          (∑ j ∈ Finset.range T, ((T : ℝ) - (j : ℝ))) := by
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro j hj
      exact rampWeight_eq_coeff_mul (Finset.mem_range.mp hj)
    _ = 1 := by
      rw [sum_range_ramp_numerator]
      field_simp [hTne, hT1ne] <;> ring

/-- Exact sum of squares, which is the correlation's diagonal cost. -/
theorem sum_sq_rampWeight {T : ℕ} (hT : 1 ≤ T) :
    (∑ j ∈ Finset.range T, (rampWeight T j) ^ 2) = rampDiagonal T := by
  have hTpos : (0 : ℝ) < (T : ℝ) := by
    exact_mod_cast (show 0 < T by omega)
  have hTne : (T : ℝ) ≠ 0 := ne_of_gt hTpos
  have hT1ne : (T : ℝ) + 1 ≠ 0 := by positivity
  calc
    (∑ j ∈ Finset.range T, (rampWeight T j) ^ 2) =
        (2 / ((T : ℝ) * ((T : ℝ) + 1))) ^ 2 *
          (∑ j ∈ Finset.range T, ((T : ℝ) - (j : ℝ)) ^ 2) := by
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro j hj
      rw [rampWeight_eq_coeff_mul (Finset.mem_range.mp hj)]
      ring
    _ = rampDiagonal T := by
      rw [sum_range_sq_ramp_numerator]
      unfold rampDiagonal
      field_simp [hTne, hT1ne] <;> ring

theorem rampDiagonal_nonneg (T : ℕ) : 0 ≤ rampDiagonal T := by
  unfold rampDiagonal
  positivity

/-- The discrete diagonal does not exceed the continuous ramp's scaled cost. -/
theorem rampDiagonal_le {T : ℕ} (hT : 1 ≤ T) :
    rampDiagonal T ≤ 4 / (3 * (T : ℝ)) := by
  have hTpos : (0 : ℝ) < (T : ℝ) := by
    exact_mod_cast (show 0 < T by omega)
  unfold rampDiagonal
  apply (div_le_div_iff₀ (by positivity : 0 < 3 * (T : ℝ) * ((T : ℝ) + 1))
    (by positivity : 0 < 3 * (T : ℝ))).2
  nlinarith

/-- The exact first moment supplies the one-sided boundary correction. -/
theorem sum_mul_rampWeight {T : ℕ} (hT : 1 ≤ T) :
    (∑ j ∈ Finset.range T, (j : ℝ) * rampWeight T j) = ((T : ℝ) - 1) / 3 := by
  have hTpos : (0 : ℝ) < (T : ℝ) := by
    exact_mod_cast (show 0 < T by omega)
  have hTne : (T : ℝ) ≠ 0 := ne_of_gt hTpos
  have hT1ne : (T : ℝ) + 1 ≠ 0 := by positivity
  calc
    (∑ j ∈ Finset.range T, (j : ℝ) * rampWeight T j) =
        (2 / ((T : ℝ) * ((T : ℝ) + 1))) *
          (∑ j ∈ Finset.range T, (j : ℝ) * ((T : ℝ) - (j : ℝ))) := by
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro j hj
      rw [rampWeight_eq_coeff_mul (Finset.mem_range.mp hj)]
      ring
    _ = ((T : ℝ) - 1) / 3 := by
      rw [sum_range_mul_ramp_numerator]
      field_simp [hTne, hT1ne] <;> ring

theorem rampWeight_zero {T : ℕ} (hT : 1 ≤ T) :
    rampWeight T 0 = 2 / ((T : ℝ) + 1) := by
  have hTpos : (0 : ℝ) < (T : ℝ) := by
    exact_mod_cast (show 0 < T by omega)
  have hTne : (T : ℝ) ≠ 0 := ne_of_gt hTpos
  have hT1ne : (T : ℝ) + 1 ≠ 0 := by positivity
  rw [rampWeight_of_lt (show 0 < T by omega)]
  push_cast
  field_simp [hTne, hT1ne] <;> ring

@[simp]
theorem rampWeightInt_natCast (T j : ℕ) :
    rampWeightInt T (j : ℤ) = rampWeight T j := by
  simp [rampWeightInt]

theorem rampWeightInt_nonneg (T : ℕ) (j : ℤ) : 0 ≤ rampWeightInt T j := by
  unfold rampWeightInt
  split_ifs
  · exact rampWeight_nonneg T j.toNat
  · exact le_rfl

theorem rampWeightInt_eq_zero_of_neg {T : ℕ} {j : ℤ} (hj : j < 0) :
    rampWeightInt T j = 0 := by
  simp only [rampWeightInt, if_neg (not_le.mpr hj)]

theorem rampWeightInt_eq_zero_of_le {T : ℕ} {j : ℤ} (hj : (T : ℤ) ≤ j) :
    rampWeightInt T j = 0 := by
  unfold rampWeightInt
  split_ifs with hj0
  · apply rampWeight_eq_zero_of_le
    omega
  · rfl

theorem rampWeightInt_of_mem {T : ℕ} {j : ℤ}
    (hj0 : 0 ≤ j) (hjT : j < (T : ℤ)) :
    rampWeightInt T j =
      2 * ((T : ℝ) - (j : ℝ)) / ((T : ℝ) * ((T : ℝ) + 1)) := by
  have hjNat : j.toNat < T := by omega
  have hjCastInt : (j.toNat : ℤ) = j := by omega
  have hjCastReal : (j.toNat : ℝ) = (j : ℝ) := by
    exact_mod_cast hjCastInt
  simp only [rampWeightInt, if_pos hj0, rampWeight, if_pos hjNat, hjCastReal]

end Sidon30

end
