/-
The finite convolution of the normalized ramp with the renewal array is the
nonnegative half-line indicator.  The proof uses a finite difference and finite sums.
-/
import Sidon30.RampWeights
import Sidon30.RenewalRecurrence

namespace Sidon30

open scoped BigOperators

/-- The ramp's finite difference, including its last nonzero entry. -/
theorem rampWeight_successor (T j : ℕ) :
    rampWeight T (j + 1) = rampWeight T j -
      (if j < T then 2 / ((T : ℝ) * ((T : ℝ) + 1)) else 0) := by
  by_cases hj : j < T
  · rw [if_pos hj, rampWeight_of_lt hj]
    by_cases hs : j + 1 < T
    · rw [rampWeight_of_lt hs]
      push_cast
      ring
    · rw [rampWeight_eq_zero_of_le (show T ≤ j + 1 by omega)]
      have hTj : (T : ℝ) = (j : ℝ) + 1 := by
        exact_mod_cast (show T = j + 1 by omega)
      rw [hTj]
      ring
  · rw [if_neg hj,
      rampWeight_eq_zero_of_le (show T ≤ j by omega),
      rampWeight_eq_zero_of_le (show T ≤ j + 1 by omega)] <;> ring

/-- The convolution equals one at each natural index, written as a finite prefix. -/
theorem sum_rampWeight_mul_renewal {T : ℕ} (hT : 1 ≤ T) (n : ℕ) :
    (∑ k ∈ Finset.range (n + 1), rampWeight T (n - k) * renewal T k) = 1 := by
  have hTpos : (0 : ℝ) < (T : ℝ) := by
    exact_mod_cast (show 0 < T by omega)
  have hTne : (T : ℝ) ≠ 0 := ne_of_gt hTpos
  have hT1ne : (T : ℝ) + 1 ≠ 0 := by positivity
  induction n with
  | zero =>
    change (∑ k ∈ Finset.range 1, rampWeight T (0 - k) * renewal T k) = 1
    rw [Finset.sum_range_one]
    change rampWeight T 0 * renewal T 0 = 1
    rw [rampWeight_zero hT, renewal_zero]
    field_simp [hT1ne] <;> ring
  | succ n ih =>
    have hsum :
        (∑ k ∈ Finset.range (n + 1), rampWeight T (n + 1 - k) * renewal T k) =
          1 - (2 / ((T : ℝ) * ((T : ℝ) + 1))) *
            (∑ k ∈ Finset.range (n + 1),
              if n + 1 - k ≤ T then renewal T k else 0) := by
      calc
        (∑ k ∈ Finset.range (n + 1), rampWeight T (n + 1 - k) * renewal T k) =
            ∑ k ∈ Finset.range (n + 1),
              (rampWeight T (n - k) * renewal T k -
                (2 / ((T : ℝ) * ((T : ℝ) + 1))) *
                  (if n + 1 - k ≤ T then renewal T k else 0)) := by
          apply Finset.sum_congr rfl
          intro k hk
          have hkn : k ≤ n := by
            have := Finset.mem_range.mp hk
            omega
          have hstep : n + 1 - k = (n - k) + 1 := by omega
          rw [hstep, rampWeight_successor]
          by_cases hlt : n - k < T
          · have hle : (n - k) + 1 ≤ T := by omega
            rw [if_pos hlt, if_pos hle]
            ring
          · have hle : ¬ (n - k) + 1 ≤ T := by omega
            rw [if_neg hlt, if_neg hle]
            ring
        _ = 1 - (2 / ((T : ℝ) * ((T : ℝ) + 1))) *
              (∑ k ∈ Finset.range (n + 1),
                if n + 1 - k ≤ T then renewal T k else 0) := by
          rw [Finset.sum_sub_distrib, ← Finset.mul_sum, ih]
    rw [Finset.sum_range_succ]
    simp only [Nat.sub_self]
    rw [hsum, rampWeight_zero hT, renewal_succ_prefix]
    field_simp [hTne, hT1ne] <;> ring

/-- At a natural index one can sum over the fixed ramp support instead of the prefix. -/
theorem sum_rampWeight_mul_renewalInt_nat {T : ℕ} (hT : 1 ≤ T) (n : ℕ) :
    (∑ j ∈ Finset.range T,
      rampWeight T j * renewalInt T ((n : ℤ) - (j : ℤ))) = 1 := by
  calc
    (∑ j ∈ Finset.range T,
        rampWeight T j * renewalInt T ((n : ℤ) - (j : ℤ))) =
        ∑ j ∈ Finset.range (n + 1), rampWeight T j * renewal T (n - j) := by
      apply Finset.sum_congr_of_eq_on_inter
      · intro j _ hj
        have hnj : n < j := by
          have hnot : ¬ j < n + 1 := fun h => hj (Finset.mem_range.mpr h)
          omega
        have hneg : (n : ℤ) - (j : ℤ) < 0 := by omega
        rw [renewalInt_of_neg T hneg, mul_zero]
      · intro j _ hj
        have hTj : T ≤ j := by
          have hnot : ¬ j < T := fun h => hj (Finset.mem_range.mpr h)
          omega
        rw [rampWeight_eq_zero_of_le hTj, zero_mul]
      · intro j _ hj
        have hjn : j ≤ n := by
          have := Finset.mem_range.mp hj
          omega
        have hcast : (n : ℤ) - (j : ℤ) = ((n - j : ℕ) : ℤ) := by omega
        rw [hcast, renewalInt_natCast]
    _ = ∑ k ∈ Finset.range (n + 1), rampWeight T (n - k) * renewal T k := by
      refine Finset.sum_bij (fun j _ => n - j) ?_ ?_ ?_ ?_
      · intro j hj
        exact Finset.mem_range.mpr (by omega)
      · intro a ha b hb hab
        have han : a < n + 1 := Finset.mem_range.mp ha
        have hbn : b < n + 1 := Finset.mem_range.mp hb
        omega
      · intro k hk
        have hkn : k < n + 1 := Finset.mem_range.mp hk
        refine ⟨n - k, Finset.mem_range.mpr (by omega), by omega⟩
      · intro j hj
        have hjn : j < n + 1 := Finset.mem_range.mp hj
        have hback : n - (n - j) = j := by omega
        rw [hback]
    _ = 1 := sum_rampWeight_mul_renewal hT n

/-- The finite ramp-renewal convolution is exactly the nonnegative half-line indicator. -/
theorem renewal_ramp_identity {T : ℕ} (hT : 1 ≤ T) (n : ℤ) :
    (∑ j ∈ Finset.range T, rampWeight T j * renewalInt T (n - (j : ℤ))) =
      if 0 ≤ n then 1 else 0 := by
  by_cases hn : 0 ≤ n
  · rw [if_pos hn]
    have hcast : (n.toNat : ℤ) = n := by omega
    simpa only [hcast] using sum_rampWeight_mul_renewalInt_nat hT n.toNat
  · rw [if_neg hn]
    apply Finset.sum_eq_zero
    intro j _hj
    have hneg : n - (j : ℤ) < 0 := by omega
    rw [renewalInt_of_neg T hneg, mul_zero]

/-- The same convolution identity with both arrays written on the integer line. -/
theorem renewal_ramp_identity_int {T : ℕ} (hT : 1 ≤ T) (n : ℤ) :
    (∑ j ∈ Finset.range T,
      rampWeightInt T (j : ℤ) * renewalInt T (n - (j : ℤ))) =
      if 0 ≤ n then 1 else 0 := by
  simpa only [rampWeightInt_natCast] using renewal_ramp_identity hT n

end Sidon30
