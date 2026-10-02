import Sidon30.CorrectionBasic

/-!
Finite absolute-prefix bounds for the renewal correction.
The geometric pointwise estimate is an explicit hypothesis, to be supplied
by the renewal contraction card. No infinite series or unproved axiom is used.
-/

noncomputable section

open scoped BigOperators

namespace Sidon30

/-- A finite geometric sum, with its remainder retained exactly. -/
theorem sum_three_quarters_eq (B : ℕ) :
    (∑ b ∈ Finset.range B, ((3 : ℝ) / 4) ^ b) =
      4 * (1 - ((3 : ℝ) / 4) ^ B) := by
  induction B with
  | zero => simp
  | succ B ih =>
      rw [Finset.sum_range_succ, ih, pow_succ]
      ring

theorem sum_three_quarters_le_four (B : ℕ) :
    (∑ b ∈ Finset.range B, ((3 : ℝ) / 4) ^ b) ≤ 4 := by
  rw [sum_three_quarters_eq]
  have hpow : 0 ≤ ((3 : ℝ) / 4) ^ B := by positivity
  linarith

/-- Exact grouping of an integer-quotient weight into full blocks of length `T`. -/
theorem sum_three_quarters_full_blocks (T B : ℕ) :
    (∑ n ∈ Finset.range (B * T), ((3 : ℝ) / 4) ^ (n / T)) =
      (T : ℝ) * ∑ b ∈ Finset.range B, ((3 : ℝ) / 4) ^ b := by
  induction B with
  | zero => simp
  | succ B ih =>
      have hblock :
          (∑ i ∈ Finset.range T, ((3 : ℝ) / 4) ^ ((B * T + i) / T)) =
            (T : ℝ) * ((3 : ℝ) / 4) ^ B := by
        calc
          _ = ∑ _i ∈ Finset.range T, ((3 : ℝ) / 4) ^ B := by
            apply Finset.sum_congr rfl
            intro i hi
            have hiT : i < T := Finset.mem_range.mp hi
            have hdiv : (B * T + i) / T = B := by
              apply Nat.div_eq_of_lt_le
              · omega
              · simpa only [Nat.add_mul, Nat.one_mul] using
                  Nat.add_lt_add_left hiT (B * T)
            rw [hdiv]
          _ = _ := by
            simp only [Finset.sum_const, Finset.card_range, nsmul_eq_mul]
      have hlen : (B + 1) * T = B * T + T := by ring
      rw [hlen, Finset.sum_range_add, ih, hblock, Finset.sum_range_succ]
      ring

/-- Every finite prefix of the quotient weight has total mass at most `4T`. -/
theorem sum_three_quarters_div_le {T : ℕ} (hT : 1 ≤ T) (M : ℕ) :
    (∑ n ∈ Finset.range M, ((3 : ℝ) / 4) ^ (n / T)) ≤ 4 * (T : ℝ) := by
  have hlarge : M + 1 ≤ (M + 1) * T := by
    simpa only [Nat.mul_one] using Nat.mul_le_mul_left (M + 1) hT
  have hM : M ≤ (M + 1) * T := le_trans (Nat.le_succ M) hlarge
  have hsubset : Finset.range M ⊆ Finset.range ((M + 1) * T) := by
    intro n hn
    exact Finset.mem_range.mpr (lt_of_lt_of_le (Finset.mem_range.mp hn) hM)
  calc
    (∑ n ∈ Finset.range M, ((3 : ℝ) / 4) ^ (n / T)) ≤
        ∑ n ∈ Finset.range ((M + 1) * T), ((3 : ℝ) / 4) ^ (n / T) :=
      Finset.sum_le_sum_of_subset_of_nonneg hsubset (fun _ _ _ => by positivity)
    _ = (T : ℝ) * ∑ b ∈ Finset.range (M + 1), ((3 : ℝ) / 4) ^ b :=
      sum_three_quarters_full_blocks T (M + 1)
    _ ≤ (T : ℝ) * 4 :=
      mul_le_mul_of_nonneg_left (sum_three_quarters_le_four (M + 1)) (by positivity)
    _ = 4 * (T : ℝ) := by ring

/-- The sharp elementary finite-prefix bound, conditional on the pointwise
renewal error estimate. Index zero is retained separately. -/
theorem sum_abs_renewalCorrection_le {T : ℕ} (hT : 1 ≤ T)
    (hq : ∀ n : ℕ, 1 ≤ n →
      |renewalCorrection T n| ≤ ((3 : ℝ) / 4) ^ ((n - 1) / T)) (M : ℕ) :
    (∑ n ∈ Finset.range (M + 1), |renewalCorrection T n|) ≤
      ((T : ℝ) - 1) / 2 + 4 * (T : ℝ) := by
  have hTreal : (1 : ℝ) ≤ (T : ℝ) := by exact_mod_cast hT
  have hzero : |renewalCorrection T 0| = ((T : ℝ) - 1) / 2 := by
    rw [renewalCorrection_zero, abs_of_nonneg (by linarith)]
  have htail : (∑ n ∈ Finset.range M, |renewalCorrection T (n + 1)|) ≤
      4 * (T : ℝ) := by
    calc
      _ ≤ ∑ n ∈ Finset.range M, ((3 : ℝ) / 4) ^ (n / T) := by
        apply Finset.sum_le_sum
        intro n _hn
        simpa only [Nat.add_sub_cancel] using hq (n + 1) (by omega)
      _ ≤ 4 * (T : ℝ) := sum_three_quarters_div_le hT M
  rw [Finset.sum_range_succ' (fun n => |renewalCorrection T n|) M, hzero]
  linarith

/-- The coarser `9T/2` bound used in the boundary-potential estimate. -/
theorem sum_abs_renewalCorrection_le_nine_halves {T : ℕ} (hT : 1 ≤ T)
    (hq : ∀ n : ℕ, 1 ≤ n →
      |renewalCorrection T n| ≤ ((3 : ℝ) / 4) ^ ((n - 1) / T)) (M : ℕ) :
    (∑ n ∈ Finset.range (M + 1), |renewalCorrection T n|) ≤
      (9 : ℝ) / 2 * (T : ℝ) := by
  have h := sum_abs_renewalCorrection_le hT hq M
  linarith

end Sidon30

end
