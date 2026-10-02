import Sidon30.RampWeights

/-!
Finite autocorrelation of the normalized ramp.  Integer shifts are reduced to
finite selectors, so all changes of summation order concern finite sums.
-/

noncomputable section

open scoped BigOperators

namespace Sidon30

/-- Autocorrelation at an integer displacement, using the zero extension. -/
def rampCorrelation (T : ℕ) (d : ℤ) : ℝ :=
  ∑ j ∈ Finset.range T,
    rampWeight T j * rampWeightInt T ((j : ℤ) + d)

private theorem sum_natCast_selector (T : ℕ) (z : ℤ) (w : ℕ → ℝ) :
    (∑ j ∈ Finset.range T, if (j : ℤ) = z then w j else 0) =
      if 0 ≤ z ∧ z < (T : ℤ) then w z.toNat else 0 := by
  classical
  by_cases hz : 0 ≤ z ∧ z < (T : ℤ)
  · have hzmem : z.toNat ∈ Finset.range T := by
      apply Finset.mem_range.mpr
      omega
    have hzcast : (z.toNat : ℤ) = z := by omega
    rw [if_pos hz]
    have hs := Finset.sum_eq_single_of_mem
      (f := fun j : ℕ => if (j : ℤ) = z then w j else 0) z.toNat hzmem
      (by
        intro j _hj hjne
        have hjz : (j : ℤ) ≠ z := by omega
        simp only [if_neg hjz])
    simpa only [if_pos hzcast] using hs
  · rw [if_neg hz]
    apply Finset.sum_eq_zero
    intro j hj
    have hjlt : j < T := Finset.mem_range.mp hj
    have hjz : (j : ℤ) ≠ z := by
      intro heq
      apply hz
      constructor <;> omega
    simp only [if_neg hjz]

private theorem rampWeightInt_eq_zero_of_not_mem (T : ℕ) (z : ℤ)
    (hz : ¬ (0 ≤ z ∧ z < (T : ℤ))) : rampWeightInt T z = 0 := by
  by_cases hz0 : 0 ≤ z
  · apply rampWeightInt_eq_zero_of_le
    omega
  · apply rampWeightInt_eq_zero_of_neg
    omega

/-- Recover the zero extension by selecting a natural index in the support. -/
theorem rampWeightInt_eq_sum (T : ℕ) (z : ℤ) :
    rampWeightInt T z =
      ∑ j ∈ Finset.range T, if (j : ℤ) = z then rampWeight T j else 0 := by
  rw [sum_natCast_selector]
  by_cases hz : 0 ≤ z ∧ z < (T : ℤ)
  · simp only [if_pos hz, rampWeightInt, if_pos hz.1]
  · rw [if_neg hz, rampWeightInt_eq_zero_of_not_mem T z hz]

private theorem rampWeightInt_sq_eq_sum (T : ℕ) (z : ℤ) :
    (rampWeightInt T z) ^ 2 =
      ∑ j ∈ Finset.range T, if (j : ℤ) = z then (rampWeight T j) ^ 2 else 0 := by
  rw [sum_natCast_selector]
  by_cases hz : 0 ≤ z ∧ z < (T : ℤ)
  · simp only [if_pos hz, rampWeightInt, if_pos hz.1]
  · rw [if_neg hz, rampWeightInt_eq_zero_of_not_mem T z hz]
    norm_num

private theorem sum_natCast_selector_le (T : ℕ) (z : ℤ) (c : ℝ) (hc : 0 ≤ c) :
    (∑ j ∈ Finset.range T, if (j : ℤ) = z then c else 0) ≤ c := by
  rw [sum_natCast_selector]
  split_ifs
  · exact le_rfl
  · exact hc

/-- The same correlation, written as a finite sum over pairs of indices. -/
theorem rampCorrelation_eq_double (T : ℕ) (d : ℤ) :
    rampCorrelation T d =
      ∑ i ∈ Finset.range T, ∑ j ∈ Finset.range T,
        if (j : ℤ) - (i : ℤ) = d then rampWeight T i * rampWeight T j else 0 := by
  unfold rampCorrelation
  apply Finset.sum_congr rfl
  intro i _hi
  rw [rampWeightInt_eq_sum, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro j _hj
  by_cases hdiff : (j : ℤ) - (i : ℤ) = d
  · have heq : (j : ℤ) = (i : ℤ) + d := by omega
    simp only [if_pos hdiff, if_pos heq]
  · have hne : (j : ℤ) ≠ (i : ℤ) + d := by omega
    simp only [if_neg hdiff, if_neg hne, mul_zero]

theorem rampCorrelation_nonneg (T : ℕ) (d : ℤ) : 0 ≤ rampCorrelation T d := by
  unfold rampCorrelation
  apply Finset.sum_nonneg
  intro j _hj
  exact mul_nonneg (rampWeight_nonneg T j)
    (rampWeightInt_nonneg T ((j : ℤ) + d))

@[simp]
theorem rampCorrelation_zero {T : ℕ} (hT : 1 ≤ T) :
    rampCorrelation T 0 = rampDiagonal T := by
  unfold rampCorrelation
  simpa only [add_zero, rampWeightInt_natCast, pow_two] using sum_sq_rampWeight hT

/-- Swapping the two finite indices reverses the displacement. -/
theorem rampCorrelation_neg (T : ℕ) (d : ℤ) :
    rampCorrelation T (-d) = rampCorrelation T d := by
  rw [rampCorrelation_eq_double, rampCorrelation_eq_double]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro i _hi
  apply Finset.sum_congr rfl
  intro j _hj
  have heq : (i : ℤ) - (j : ℤ) = -d ↔ (j : ℤ) - (i : ℤ) = d := by omega
  simp only [heq]
  split_ifs <;> ring

/-- The support is strictly inside the integer interval `[-T, T]`. -/
theorem rampCorrelation_eq_zero_of_abs_le {T : ℕ} {d : ℤ}
    (hd : (T : ℤ) ≤ |d|) : rampCorrelation T d = 0 := by
  unfold rampCorrelation
  apply Finset.sum_eq_zero
  intro j hj
  have hjlt : j < T := Finset.mem_range.mp hj
  have hzero : rampWeightInt T ((j : ℤ) + d) = 0 := by
    by_cases hd0 : 0 ≤ d
    · have hdT : (T : ℤ) ≤ d := by
        simpa only [abs_of_nonneg hd0] using hd
      apply rampWeightInt_eq_zero_of_le
      omega
    · have hdneg : d < 0 := by omega
      have hdT : (T : ℤ) ≤ -d := by
        simpa only [abs_of_neg hdneg] using hd
      apply rampWeightInt_eq_zero_of_neg
      omega
  rw [hzero, mul_zero]

/-- Restricting a translate to the original support cannot increase its square sum. -/
theorem sum_sq_shift_rampWeightInt_le {T : ℕ} (hT : 1 ≤ T) (d : ℤ) :
    (∑ i ∈ Finset.range T, (rampWeightInt T ((i : ℤ) + d)) ^ 2) ≤
      rampDiagonal T := by
  calc
    (∑ i ∈ Finset.range T, (rampWeightInt T ((i : ℤ) + d)) ^ 2) =
        ∑ i ∈ Finset.range T, ∑ j ∈ Finset.range T,
          if (j : ℤ) = (i : ℤ) + d then (rampWeight T j) ^ 2 else 0 := by
      apply Finset.sum_congr rfl
      intro i _hi
      exact rampWeightInt_sq_eq_sum T ((i : ℤ) + d)
    _ = ∑ j ∈ Finset.range T, ∑ i ∈ Finset.range T,
          if (i : ℤ) = (j : ℤ) - d then (rampWeight T j) ^ 2 else 0 := by
      rw [Finset.sum_comm]
      apply Finset.sum_congr rfl
      intro j _hj
      apply Finset.sum_congr rfl
      intro i _hi
      have heq : (j : ℤ) = (i : ℤ) + d ↔ (i : ℤ) = (j : ℤ) - d := by omega
      simp only [heq]
    _ ≤ ∑ j ∈ Finset.range T, (rampWeight T j) ^ 2 := by
      apply Finset.sum_le_sum
      intro j _hj
      exact sum_natCast_selector_le T ((j : ℤ) - d) ((rampWeight T j) ^ 2)
        (sq_nonneg (rampWeight T j))
    _ = rampDiagonal T := sum_sq_rampWeight hT

theorem rampCorrelation_le_diagonal {T : ℕ} (hT : 1 ≤ T) (d : ℤ) :
    rampCorrelation T d ≤ rampDiagonal T := by
  have hcs := Finset.sum_mul_sq_le_sq_mul_sq (Finset.range T)
    (fun j => rampWeight T j) (fun j => rampWeightInt T ((j : ℤ) + d))
  change (rampCorrelation T d) ^ 2 ≤
    (∑ j ∈ Finset.range T, (rampWeight T j) ^ 2) *
      (∑ j ∈ Finset.range T, (rampWeightInt T ((j : ℤ) + d)) ^ 2) at hcs
  rw [sum_sq_rampWeight hT] at hcs
  have hshift := sum_sq_shift_rampWeightInt_le hT d
  have hdiag := rampDiagonal_nonneg T
  have hcorr := rampCorrelation_nonneg T d
  have hprod := mul_le_mul_of_nonneg_left hshift hdiag
  have hsquare : (rampCorrelation T d) ^ 2 ≤ (rampDiagonal T) ^ 2 := by
    nlinarith [hcs, hprod]
  nlinarith

private theorem sum_int_selector {s : Finset ℤ} {z : ℤ} (hz : z ∈ s) (c : ℝ) :
    (∑ d ∈ s, if z = d then c else 0) = c := by
  classical
  have hs := Finset.sum_eq_single_of_mem
    (f := fun d : ℤ => if z = d then c else 0) z hz
    (by
      intro d _hd hdz
      simp only [if_neg (Ne.symm hdz)])
  simpa using hs

/-- Total mass on an explicit finite interval containing the whole support. -/
theorem sum_rampCorrelation {T : ℕ} (hT : 1 ≤ T) :
    (∑ d ∈ Finset.Icc (1 - (T : ℤ)) ((T : ℤ) - 1), rampCorrelation T d) = 1 := by
  classical
  calc
    (∑ d ∈ Finset.Icc (1 - (T : ℤ)) ((T : ℤ) - 1), rampCorrelation T d) =
        ∑ d ∈ Finset.Icc (1 - (T : ℤ)) ((T : ℤ) - 1),
          ∑ i ∈ Finset.range T, ∑ j ∈ Finset.range T,
            if (j : ℤ) - (i : ℤ) = d then rampWeight T i * rampWeight T j else 0 := by
      apply Finset.sum_congr rfl
      intro d _hd
      exact rampCorrelation_eq_double T d
    _ = ∑ i ∈ Finset.range T, ∑ j ∈ Finset.range T,
          ∑ d ∈ Finset.Icc (1 - (T : ℤ)) ((T : ℤ) - 1),
            if (j : ℤ) - (i : ℤ) = d then rampWeight T i * rampWeight T j else 0 := by
      rw [Finset.sum_comm]
      apply Finset.sum_congr rfl
      intro i _hi
      exact Finset.sum_comm
    _ = ∑ i ∈ Finset.range T, ∑ j ∈ Finset.range T,
          rampWeight T i * rampWeight T j := by
      apply Finset.sum_congr rfl
      intro i hi
      apply Finset.sum_congr rfl
      intro j hj
      apply sum_int_selector
      have hi' : i < T := Finset.mem_range.mp hi
      have hj' : j < T := Finset.mem_range.mp hj
      apply Finset.mem_Icc.mpr
      constructor <;> omega
    _ = (∑ i ∈ Finset.range T, rampWeight T i) *
          (∑ j ∈ Finset.range T, rampWeight T j) := by
      rw [Finset.sum_mul_sum]
    _ = 1 := by simp only [sum_rampWeight hT, mul_one]

/-- The nonzero positive displacements carry half the off-diagonal mass. -/
theorem two_mul_sum_pos_rampCorrelation {T : ℕ} (hT : 1 ≤ T) :
    2 * (∑ d ∈ Finset.Icc (1 : ℤ) ((T : ℤ) - 1), rampCorrelation T d) =
      1 - rampDiagonal T := by
  classical
  let P : Finset ℤ := Finset.Icc 1 ((T : ℤ) - 1)
  let M : Finset ℤ := Finset.Icc (1 - (T : ℤ)) (-1)
  have hsplit : Finset.Icc (1 - (T : ℤ)) ((T : ℤ) - 1) = ({0} ∪ P) ∪ M := by
    ext d
    simp only [P, M, Finset.mem_Icc, Finset.mem_union, Finset.mem_singleton]
    omega
  have h0P : Disjoint ({0} : Finset ℤ) P := by
    apply Finset.disjoint_left.mpr
    intro d hd0 hdP
    have hd0' : d = 0 := Finset.mem_singleton.mp hd0
    have hdP' := Finset.mem_Icc.mp hdP
    omega
  have hPM : Disjoint (({0} : Finset ℤ) ∪ P) M := by
    apply Finset.disjoint_left.mpr
    intro d hd hdM
    have hdM' := Finset.mem_Icc.mp hdM
    rcases Finset.mem_union.mp hd with hd0 | hdP
    · have hd0' : d = 0 := Finset.mem_singleton.mp hd0
      omega
    · have hdP' := Finset.mem_Icc.mp hdP
      omega
  have hneg : (∑ d ∈ M, rampCorrelation T d) = ∑ d ∈ P, rampCorrelation T d := by
    refine Finset.sum_bij (fun d _hd => -d) ?_ ?_ ?_ ?_
    · intro d hd
      have hd' := Finset.mem_Icc.mp hd
      apply Finset.mem_Icc.mpr
      constructor <;> omega
    · intro a _ha b _hb hab
      omega
    · intro d hd
      have hd' := Finset.mem_Icc.mp hd
      refine ⟨-d, ?_, ?_⟩
      · apply Finset.mem_Icc.mpr
        constructor <;> omega
      · simp
    · intro d _hd
      exact (rampCorrelation_neg T d).symm
  have hmass := sum_rampCorrelation hT
  rw [hsplit, Finset.sum_union hPM, Finset.sum_union h0P,
    Finset.sum_singleton, rampCorrelation_zero hT, hneg] at hmass
  change 2 * (∑ d ∈ P, rampCorrelation T d) = 1 - rampDiagonal T
  linarith

end Sidon30

end
