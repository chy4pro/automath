import Sidon30.RenewalRecurrence

/-!
The signed renewal correction and its finite prefixes.  The integer extension
is zero at negative indices; no infinite sum or convergence assertion is used.
-/

noncomputable section

open scoped BigOperators

namespace Sidon30

/-- The correction to the constant density on the nonnegative integers. -/
def renewalCorrection (T n : ℕ) : ℝ := renewal T n - 1

/-- Zero extension of the correction; its value at zero is retained. -/
def renewalCorrectionInt (T : ℕ) (n : ℤ) : ℝ :=
  if 0 ≤ n then renewalCorrection T n.toNat else 0

/-- The signed mass of a finite prefix, including index zero. -/
def correctionPrefixMass (T M : ℕ) : ℝ :=
  ∑ n ∈ Finset.range (M + 1), renewalCorrection T n

@[simp]
theorem renewalCorrection_zero (T : ℕ) :
    renewalCorrection T 0 = ((T : ℝ) - 1) / 2 := by
  unfold renewalCorrection
  rw [renewal_zero]
  ring

@[simp]
theorem renewalCorrectionInt_natCast (T n : ℕ) :
    renewalCorrectionInt T (n : ℤ) = renewalCorrection T n := by
  simp [renewalCorrectionInt]

@[simp]
theorem renewalCorrectionInt_of_neg (T : ℕ) {n : ℤ} (hn : n < 0) :
    renewalCorrectionInt T n = 0 := by
  simp only [renewalCorrectionInt, if_neg (not_le.mpr hn)]

/-- The integer correction subtracts the half-line indicator, not the full constant array. -/
theorem renewalCorrectionInt_eq (T : ℕ) (n : ℤ) :
    renewalCorrectionInt T n = renewalInt T n - (if 0 ≤ n then 1 else 0) := by
  by_cases hn : 0 ≤ n
  · have hn' : ¬ n < 0 := by omega
    simp only [renewalCorrectionInt, if_pos hn, renewalInt, if_neg hn',
      renewalCorrection]
  · have hn' : n < 0 := by omega
    simp only [renewalCorrectionInt, if_neg hn, renewalInt, if_pos hn', sub_self]

@[simp]
theorem correctionPrefixMass_zero (T : ℕ) :
    correctionPrefixMass T 0 = renewalCorrection T 0 := by
  simp only [correctionPrefixMass, zero_add, Finset.sum_range_one]

theorem correctionPrefixMass_succ (T M : ℕ) :
    correctionPrefixMass T (M + 1) =
      correctionPrefixMass T M + renewalCorrection T (M + 1) := by
  unfold correctionPrefixMass
  rw [Finset.sum_range_succ]

/-- A finite translated prefix of the zero extension is an ordinary shorter prefix. -/
theorem sum_renewalCorrectionInt_sub (T M j : ℕ) (hjM : j ≤ M) :
    (∑ n ∈ Finset.range (M + 1),
      renewalCorrectionInt T ((n : ℤ) - (j : ℤ))) =
      correctionPrefixMass T (M - j) := by
  classical
  calc
    (∑ n ∈ Finset.range (M + 1),
        renewalCorrectionInt T ((n : ℤ) - (j : ℤ))) =
        ∑ n ∈ Finset.Icc j M, renewalCorrection T (n - j) := by
      apply Finset.sum_congr_of_eq_on_inter
      · intro n hn hnnot
        have hnM : n < M + 1 := Finset.mem_range.mp hn
        have hnj : n < j := by
          by_contra h
          apply hnnot
          exact Finset.mem_Icc.mpr ⟨by omega, by omega⟩
        apply renewalCorrectionInt_of_neg
        omega
      · intro n hn hnnot
        have hnM : n ≤ M := (Finset.mem_Icc.mp hn).2
        exact False.elim (hnnot (Finset.mem_range.mpr (by omega)))
      · intro n _hn hnI
        have hjn : j ≤ n := (Finset.mem_Icc.mp hnI).1
        have hcast : (n : ℤ) - (j : ℤ) = ((n - j : ℕ) : ℤ) := by omega
        rw [hcast, renewalCorrectionInt_natCast]
    _ = correctionPrefixMass T (M - j) := by
      unfold correctionPrefixMass
      refine Finset.sum_bij (fun n _hn => n - j) ?_ ?_ ?_ ?_
      · intro n hn
        have hn' := Finset.mem_Icc.mp hn
        apply Finset.mem_range.mpr
        omega
      · intro a ha b hb hab
        have ha' := Finset.mem_Icc.mp ha
        have hb' := Finset.mem_Icc.mp hb
        omega
      · intro n hn
        have hn' : n < M - j + 1 := Finset.mem_range.mp hn
        refine ⟨n + j, ?_, by omega⟩
        apply Finset.mem_Icc.mpr
        constructor <;> omega
      · intro n _hn
        rfl

/-- A finite interval is the difference of two inclusive prefix masses. -/
theorem sum_Icc_renewalCorrection (T M L : ℕ) (hLM : L ≤ M) :
    (∑ n ∈ Finset.Icc (L + 1) M, renewalCorrection T n) =
      correctionPrefixMass T M - correctionPrefixMass T L := by
  have hinterval : Finset.Ico (L + 1) (M + 1) = Finset.Icc (L + 1) M := by
    ext n
    simp only [Finset.mem_Ico, Finset.mem_Icc]
    omega
  have hs := Finset.sum_Ico_eq_sub (renewalCorrection T)
    (m := L + 1) (n := M + 1) (by omega)
  simpa only [hinterval, correctionPrefixMass] using hs

end Sidon30

end
