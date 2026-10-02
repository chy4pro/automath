import Sidon30.RenewalRecurrence

/-!
The first renewal block, including its exact closed form.
The elementary numerical bound is obtained from existing Mathlib exponential
inequalities; no measure, infinite convolution, or renewal limit is introduced.
-/

open scoped BigOperators

namespace Sidon30

/-- In the first block, the recurrence includes the entire earlier prefix. -/
theorem renewal_eq_full_prefix {T n : ℕ} (hn : 0 < n) (hnT : n ≤ T) :
    renewal T n = (1 / (T : ℝ)) * ∑ k ∈ Finset.range n, renewal T k := by
  rw [renewal_eq_prefix_of_pos T n hn]
  congr 1
  apply Finset.sum_congr rfl
  intro k _hk
  rw [if_pos (le_trans (Nat.sub_le n k) hnT)]

/-- Consecutive positive entries in the first block have a fixed ratio. -/
theorem renewal_firstBlock_step {T n : ℕ} (hn : 0 < n) (hnT : n + 1 ≤ T) :
    renewal T (n + 1) = (1 + 1 / (T : ℝ)) * renewal T n := by
  have hnT' : n ≤ T := by omega
  calc
    renewal T (n + 1) =
        (1 / (T : ℝ)) * ((∑ k ∈ Finset.range n, renewal T k) + renewal T n) := by
      rw [renewal_eq_full_prefix (by omega) hnT, Finset.sum_range_succ]
    _ = renewal T n + (1 / (T : ℝ)) * renewal T n := by
      rw [mul_add, ← renewal_eq_full_prefix hn hnT']
    _ = (1 + 1 / (T : ℝ)) * renewal T n := by ring

/-- The exact first-block formula; the exceptional initial mass is at index zero. -/
theorem renewal_firstBlock {T : ℕ} (hT : 1 ≤ T) (n : ℕ) :
    1 ≤ n → n ≤ T →
      renewal T n = (1 / 2 : ℝ) * (1 + 1 / (T : ℝ)) ^ n := by
  have hTpos : (0 : ℝ) < T := by exact_mod_cast (show 0 < T by omega)
  have hTne : (T : ℝ) ≠ 0 := ne_of_gt hTpos
  induction n with
  | zero =>
      intro hn _hnT
      omega
  | succ n ih =>
      intro _hn hnT
      by_cases hn : n = 0
      · subst n
        rw [renewal_eq_full_prefix (by omega) hnT]
        simp only [Finset.sum_range_one, renewal_zero, pow_one]
        field_simp [hTne]
        <;> ring
      · have hnpos : 0 < n := Nat.pos_of_ne_zero hn
        rw [renewal_firstBlock_step hnpos hnT,
          ih (by omega) (by omega), pow_succ]
        ring

/-- A library-proved exact upper bound for the finite binomial expression.
The two exponential inequalities here are used only to certify the number 3. -/
theorem firstBlock_base_pow_le_three (T : ℕ) :
    (1 + 1 / (T : ℝ)) ^ T ≤ 3 := by
  have hpow : (1 + 1 / (T : ℝ)) ^ T ≤ Real.exp 1 := by
    simpa only [one_div] using (Real.one_add_inv_pow_le_exp (n := T))
  have he : Real.exp (1 : ℝ) < 3 := by
    have h := Real.exp_lt_two_add_div_two_sub
      (by norm_num : (0 : ℝ) < 1) (by norm_num : (1 : ℝ) < 2)
    norm_num at h
    exact h
  exact hpow.trans he.le

/-- The initial block lies in an interval of width one. -/
theorem renewal_firstBlock_bounds {T n : ℕ} (hT : 1 ≤ T)
    (hn : 1 ≤ n) (hnT : n ≤ T) :
    (1 / 2 : ℝ) ≤ renewal T n ∧ renewal T n ≤ (3 / 2 : ℝ) := by
  rw [renewal_firstBlock hT n hn hnT]
  have hbase : (1 : ℝ) ≤ 1 + 1 / (T : ℝ) := by
    have hinv : (0 : ℝ) ≤ 1 / (T : ℝ) := by positivity
    linarith
  have hlower : (1 : ℝ) ≤ (1 + 1 / (T : ℝ)) ^ n := one_le_pow₀ hbase
  have hmono : (1 + 1 / (T : ℝ)) ^ n ≤ (1 + 1 / (T : ℝ)) ^ T := by
    gcongr
  have hupper := hmono.trans (firstBlock_base_pow_le_three T)
  constructor <;> linarith

end Sidon30
