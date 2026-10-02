import Sidon30.CorrectionBasic
import Sidon30.RenewalRampIdentity

/-!
An exact finite mass identity for the renewal correction.  This file does not
define an infinite total mass and does not assume a tail or convergence bound.
-/

noncomputable section

open scoped BigOperators

namespace Sidon30

/-- The correction's convolution is precisely the missing initial ramp mass. -/
theorem correction_ramp_identity {T : ℕ} (hT : 1 ≤ T) (n : ℕ) :
    (∑ j ∈ Finset.range T,
      rampWeight T j * renewalCorrectionInt T ((n : ℤ) - (j : ℤ))) =
      ∑ j ∈ Finset.range T, if n < j then rampWeight T j else 0 := by
  have hn : (0 : ℤ) ≤ (n : ℤ) := by omega
  have hconv := renewal_ramp_identity hT (n : ℤ)
  rw [if_pos hn] at hconv
  calc
    (∑ j ∈ Finset.range T,
        rampWeight T j * renewalCorrectionInt T ((n : ℤ) - (j : ℤ))) =
        (∑ j ∈ Finset.range T,
          rampWeight T j * renewalInt T ((n : ℤ) - (j : ℤ))) -
        (∑ j ∈ Finset.range T,
          rampWeight T j * (if 0 ≤ (n : ℤ) - (j : ℤ) then 1 else 0)) := by
      simp_rw [renewalCorrectionInt_eq, mul_sub]
      rw [Finset.sum_sub_distrib]
    _ = (∑ j ∈ Finset.range T, rampWeight T j) -
        (∑ j ∈ Finset.range T,
          rampWeight T j * (if 0 ≤ (n : ℤ) - (j : ℤ) then 1 else 0)) := by
      rw [hconv, sum_rampWeight hT]
    _ = ∑ j ∈ Finset.range T, if n < j then rampWeight T j else 0 := by
      rw [← Finset.sum_sub_distrib]
      apply Finset.sum_congr rfl
      intro j _hj
      by_cases hnj : n < j
      · have hneg : ¬ 0 ≤ (n : ℤ) - (j : ℤ) := by omega
        simp only [if_neg hneg, if_pos hnj, mul_zero, sub_zero]
      · have hnonneg : 0 ≤ (n : ℤ) - (j : ℤ) := by omega
        simp only [if_pos hnonneg, if_neg hnj, mul_one, sub_self]

private theorem sum_range_ite_lt_const (M j : ℕ) (hj : j ≤ M + 1) (c : ℝ) :
    (∑ n ∈ Finset.range (M + 1), if n < j then c else 0) = (j : ℝ) * c := by
  classical
  calc
    (∑ n ∈ Finset.range (M + 1), if n < j then c else 0) =
        ∑ _n ∈ Finset.range j, c := by
      apply Finset.sum_congr_of_eq_on_inter
      · intro n _hn hnnot
        have hnj : ¬ n < j := fun h => hnnot (Finset.mem_range.mpr h)
        simp only [if_neg hnj]
      · intro n hn hnnot
        have hnj : n < j := Finset.mem_range.mp hn
        exact False.elim (hnnot (Finset.mem_range.mpr (by omega)))
      · intro n _hn hnj
        simp only [if_pos (Finset.mem_range.mp hnj)]
    _ = (j : ℝ) * c := by
      simp only [Finset.sum_const, Finset.card_range, nsmul_eq_mul]

/-- Summing the correction identity over a sufficiently long finite prefix gives its moment. -/
theorem correction_weighted_prefix_mass {T M : ℕ} (hT : 1 ≤ T) (hM : T - 1 ≤ M) :
    (∑ j ∈ Finset.range T, rampWeight T j * correctionPrefixMass T (M - j)) =
      ((T : ℝ) - 1) / 3 := by
  calc
    (∑ j ∈ Finset.range T, rampWeight T j * correctionPrefixMass T (M - j)) =
        ∑ j ∈ Finset.range T, ∑ n ∈ Finset.range (M + 1),
          rampWeight T j * renewalCorrectionInt T ((n : ℤ) - (j : ℤ)) := by
      apply Finset.sum_congr rfl
      intro j hj
      have hjT : j < T := Finset.mem_range.mp hj
      have hjM : j ≤ M := by omega
      rw [← sum_renewalCorrectionInt_sub T M j hjM, Finset.mul_sum]
    _ = ∑ n ∈ Finset.range (M + 1), ∑ j ∈ Finset.range T,
          rampWeight T j * renewalCorrectionInt T ((n : ℤ) - (j : ℤ)) :=
      Finset.sum_comm
    _ = ∑ n ∈ Finset.range (M + 1), ∑ j ∈ Finset.range T,
          if n < j then rampWeight T j else 0 := by
      apply Finset.sum_congr rfl
      intro n _hn
      exact correction_ramp_identity hT n
    _ = ∑ j ∈ Finset.range T, ∑ n ∈ Finset.range (M + 1),
          if n < j then rampWeight T j else 0 := Finset.sum_comm
    _ = ∑ j ∈ Finset.range T, (j : ℝ) * rampWeight T j := by
      apply Finset.sum_congr rfl
      intro j hj
      have hjT : j < T := Finset.mem_range.mp hj
      exact sum_range_ite_lt_const M j (by omega) (rampWeight T j)
    _ = ((T : ℝ) - 1) / 3 := sum_mul_rampWeight hT

/-- The finite mass error can be expressed by differences of finite prefixes. -/
theorem correction_finite_mass_prefix {T M : ℕ} (hT : 1 ≤ T) (hM : T - 1 ≤ M) :
    correctionPrefixMass T M - ((T : ℝ) - 1) / 3 =
      ∑ j ∈ Finset.range T,
        rampWeight T j * (correctionPrefixMass T M - correctionPrefixMass T (M - j)) := by
  calc
    correctionPrefixMass T M - ((T : ℝ) - 1) / 3 =
        (∑ j ∈ Finset.range T, rampWeight T j) * correctionPrefixMass T M -
        (∑ j ∈ Finset.range T, rampWeight T j * correctionPrefixMass T (M - j)) := by
      rw [sum_rampWeight hT, correction_weighted_prefix_mass hT hM, one_mul]
    _ = ∑ j ∈ Finset.range T,
          (rampWeight T j * correctionPrefixMass T M -
            rampWeight T j * correctionPrefixMass T (M - j)) := by
      rw [Finset.sum_mul, Finset.sum_sub_distrib]
    _ = ∑ j ∈ Finset.range T,
          rampWeight T j * (correctionPrefixMass T M - correctionPrefixMass T (M - j)) := by
      apply Finset.sum_congr rfl
      intro j _hj
      ring

/-- Exact finite mass formula, with an explicit finite tail for each ramp index. -/
theorem correction_finite_mass {T M : ℕ} (hT : 1 ≤ T) (hM : T - 1 ≤ M) :
    correctionPrefixMass T M - ((T : ℝ) - 1) / 3 =
      ∑ j ∈ Finset.range T,
        rampWeight T j * (∑ n ∈ Finset.Icc (M - j + 1) M, renewalCorrection T n) := by
  rw [correction_finite_mass_prefix hT hM]
  apply Finset.sum_congr rfl
  intro j _hj
  rw [sum_Icc_renewalCorrection T M (M - j) (Nat.sub_le M j)]

end Sidon30

end
