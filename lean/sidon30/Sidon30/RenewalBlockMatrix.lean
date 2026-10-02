/-
The explicit finite matrix carrying one positive renewal block to the next.
-/
import Sidon30.RenewalRecurrence

namespace Sidon30

open scoped BigOperators

/-- A window form of the renewal recurrence. -/
theorem renewal_eq_window {T n : ℕ} (hn : 0 < n) :
    renewal T n = (1 / (T : ℝ)) *
      ∑ k ∈ Finset.Ico (n - T) n, renewal T k := by
  have hset : (Finset.range n).filter (fun k => n - k ≤ T) =
      Finset.Ico (n - T) n := by
    ext k
    simp only [Finset.mem_filter, Finset.mem_range, Finset.mem_Ico]
    omega
  rw [renewal_eq_prefix_of_pos T n hn, ← Finset.sum_filter, hset]

/-- Moving a full renewal window removes its left endpoint and adds its right endpoint. -/
theorem renewal_window_step {T n : ℕ} (hT : 1 ≤ T) (hnT : T ≤ n) :
    renewal T (n + 1) = (1 + 1 / (T : ℝ)) * renewal T n -
      (1 / (T : ℝ)) * renewal T (n - T) := by
  have hlow : n + 1 - T = (n - T) + 1 := by omega
  have hsum :
      (∑ k ∈ Finset.Ico (n + 1 - T) (n + 1), renewal T k) =
        (∑ k ∈ Finset.Ico (n - T) n, renewal T k) +
          renewal T n - renewal T (n - T) := by
    rw [hlow, Finset.sum_Ico_eq_sub (renewal T) (by omega),
      Finset.sum_Ico_eq_sub (renewal T) (by omega),
      Finset.sum_range_succ, Finset.sum_range_succ]
    ring
  rw [renewal_eq_window (T := T) (n := n + 1) (by omega), hsum,
    mul_sub, mul_add, ← renewal_eq_window (T := T) (n := n) (by omega)]
  ring

/-- The first entry of the next block is the mean of the preceding block. -/
theorem renewal_block_first {T : ℕ} (hT : 1 ≤ T) (b : ℕ) :
    renewal T ((b + 1) * T + 1) = (1 / (T : ℝ)) *
      ∑ j ∈ Finset.Icc 1 T, renewal T (b * T + j) := by
  have hmul : (b + 1) * T = b * T + T := by ring
  rw [renewal_eq_window (T := T) (n := (b + 1) * T + 1) (by omega), hmul]
  congr 1
  refine Finset.sum_bij (fun k _ => k - b * T) ?_ ?_ ?_ ?_
  · intro k hk
    rcases Finset.mem_Ico.mp hk with ⟨hlo, hhi⟩
    exact Finset.mem_Icc.mpr ⟨by omega, by omega⟩
  · intro a ha c hc hac
    rcases Finset.mem_Ico.mp ha with ⟨ha0, ha1⟩
    rcases Finset.mem_Ico.mp hc with ⟨hc0, hc1⟩
    omega
  · intro j hj
    rcases Finset.mem_Icc.mp hj with ⟨hj1, hjT⟩
    refine ⟨b * T + j, Finset.mem_Ico.mpr ⟨by omega, by omega⟩, by omega⟩
  · intro k hk
    rcases Finset.mem_Ico.mp hk with ⟨hk0, hk1⟩
    have hback : b * T + (k - b * T) = k := by omega
    rw [hback]

/-- The scalar recurrence within a block. -/
theorem renewal_block_step {T : ℕ} (hT : 1 ≤ T) (b i : ℕ) :
    renewal T ((b + 1) * T + (i + 1)) =
      (1 + 1 / (T : ℝ)) * renewal T ((b + 1) * T + i) -
        (1 / (T : ℝ)) * renewal T (b * T + i) := by
  have hnT : T ≤ (b + 1) * T + i := by
    rw [add_mul, one_mul]
    omega
  have hnext : (b + 1) * T + i + 1 = (b + 1) * T + (i + 1) := by omega
  have hback : (b + 1) * T + i - T = b * T + i := by
    rw [add_mul, one_mul]
    omega
  simpa only [hnext, hback] using renewal_window_step hT hnT

/-- The explicit transition kernel on the indices 1 through T. -/
noncomputable def renewalBlockKernel (T i j : ℕ) : ℝ :=
  if i ≤ j then (1 / (T : ℝ)) * (1 + 1 / (T : ℝ)) ^ (i - 1)
  else (1 / (T : ℝ)) * (1 + 1 / (T : ℝ)) ^ (i - j - 1) *
    ((1 + 1 / (T : ℝ)) ^ j - 1)

/-- The first matrix row is uniform. -/
theorem renewalBlockKernel_first (T : ℕ) {j : ℕ} (hj : 1 ≤ j) :
    renewalBlockKernel T 1 j = 1 / (T : ℝ) := by
  simp [renewalBlockKernel, hj]

/-- Every matrix entry is nonnegative. -/
theorem renewalBlockKernel_nonneg (T i j : ℕ) : 0 ≤ renewalBlockKernel T i j := by
  have hbase : (1 : ℝ) ≤ 1 + 1 / (T : ℝ) := by
    have h : (0 : ℝ) ≤ 1 / (T : ℝ) := by positivity
    linarith
  unfold renewalBlockKernel
  split_ifs
  · positivity
  · exact mul_nonneg (by positivity) (sub_nonneg.mpr (one_le_pow₀ hbase))

/-- Successive matrix rows satisfy the same scalar update as a renewal block. -/
theorem renewalBlockKernel_step (T : ℕ) {i j : ℕ} (hi : 1 ≤ i) (hj : 1 ≤ j) :
    renewalBlockKernel T (i + 1) j =
      (1 + 1 / (T : ℝ)) * renewalBlockKernel T i j -
        (if j = i then 1 / (T : ℝ) else 0) := by
  have hexp : i - 1 + 1 = i := by omega
  have hpow : (1 + 1 / (T : ℝ)) ^ i =
      (1 + 1 / (T : ℝ)) ^ (i - 1) * (1 + 1 / (T : ℝ)) := by
    simpa only [hexp] using (pow_succ (1 + 1 / (T : ℝ)) (i - 1))
  rcases lt_trichotomy i j with hij | hij | hji
  · simp only [renewalBlockKernel,
      if_pos (show i + 1 ≤ j by omega), if_pos (show i ≤ j by omega),
      if_neg (show j ≠ i by omega), Nat.add_sub_cancel]
    rw [hpow]
    ring
  · subst j
    simp only [renewalBlockKernel,
      if_neg (show ¬ i + 1 ≤ i by omega), if_pos (le_refl i),
      if_pos (show i = i from rfl), ite_true,
      show i + 1 - i - 1 = 0 by omega, pow_zero, mul_one]
    rw [hpow]
    ring
  · have hsub : i + 1 - j - 1 = (i - j - 1) + 1 := by omega
    simp only [renewalBlockKernel,
      if_neg (show ¬ i + 1 ≤ j by omega), if_neg (show ¬ i ≤ j by omega),
      if_neg (show j ≠ i by omega)]
    rw [hsub, pow_succ]
    ring

/-- A matrix row update after application to any real vector. -/
theorem renewalBlockKernel_action_step (T : ℕ) {i : ℕ}
    (hi : 1 ≤ i) (hiT : i ≤ T) (v : ℕ → ℝ) :
    (∑ j ∈ Finset.Icc 1 T, renewalBlockKernel T (i + 1) j * v j) =
      (1 + 1 / (T : ℝ)) *
        (∑ j ∈ Finset.Icc 1 T, renewalBlockKernel T i j * v j) -
          (1 / (T : ℝ)) * v i := by
  have hsingle :
      (∑ j ∈ Finset.Icc 1 T, if j = i then (1 / (T : ℝ)) * v j else 0) =
        (1 / (T : ℝ)) * v i := by
    rw [Finset.sum_eq_single i]
    · simp
    · intro j _hj hji
      simp [hji]
    · intro hnot
      exact (hnot (Finset.mem_Icc.mpr ⟨hi, hiT⟩)).elim
  calc
    (∑ j ∈ Finset.Icc 1 T, renewalBlockKernel T (i + 1) j * v j) =
        ∑ j ∈ Finset.Icc 1 T,
          ((1 + 1 / (T : ℝ)) * (renewalBlockKernel T i j * v j) -
            (if j = i then (1 / (T : ℝ)) * v j else 0)) := by
      apply Finset.sum_congr rfl
      intro j hj
      rw [renewalBlockKernel_step T hi (Finset.mem_Icc.mp hj).1]
      by_cases hji : j = i
      · simp only [if_pos hji] <;> ring
      · simp only [if_neg hji] <;> ring
    _ = _ := by rw [Finset.sum_sub_distrib, ← Finset.mul_sum, hsingle]

/-- Each relevant row has total mass one. -/
theorem sum_renewalBlockKernel {T : ℕ} (hT : 1 ≤ T) (i : ℕ) :
    1 ≤ i → i ≤ T → (∑ j ∈ Finset.Icc 1 T, renewalBlockKernel T i j) = 1 := by
  have hTne : (T : ℝ) ≠ 0 := by
    have : (0 : ℝ) < T := by exact_mod_cast (show 0 < T by omega)
    exact ne_of_gt this
  induction i with
  | zero => intro hi; omega
  | succ i ih =>
    intro hi hiT
    by_cases hi0 : i = 0
    · subst i
      have hcard : (Finset.Icc 1 T).card = T := by simp [Nat.card_Icc]
      calc
        (∑ j ∈ Finset.Icc 1 T, renewalBlockKernel T (0 + 1) j) =
            ∑ j ∈ Finset.Icc 1 T, (1 / (T : ℝ)) := by
          apply Finset.sum_congr rfl
          intro j hj
          exact renewalBlockKernel_first T (Finset.mem_Icc.mp hj).1
        _ = 1 := by
          simp only [Finset.sum_const, hcard, nsmul_eq_mul]
          field_simp [hTne]
    · calc
        (∑ j ∈ Finset.Icc 1 T, renewalBlockKernel T (i + 1) j) =
            (1 + 1 / (T : ℝ)) *
              (∑ j ∈ Finset.Icc 1 T, renewalBlockKernel T i j) - 1 / (T : ℝ) := by
          simpa only [mul_one] using
            renewalBlockKernel_action_step T (by omega : 1 ≤ i) (by omega : i ≤ T)
              (fun _ => (1 : ℝ))
        _ = 1 := by rw [ih (by omega) (by omega)]; ring

/-- The next renewal block is the image of the preceding block under the explicit matrix. -/
theorem renewal_block_matrix {T : ℕ} (hT : 1 ≤ T) (b i : ℕ) :
    1 ≤ i → i ≤ T →
      renewal T ((b + 1) * T + i) =
        ∑ j ∈ Finset.Icc 1 T, renewalBlockKernel T i j * renewal T (b * T + j) := by
  induction i with
  | zero => intro hi; omega
  | succ i ih =>
    intro hi hiT
    by_cases hi0 : i = 0
    · subst i
      rw [renewal_block_first hT b, Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro j hj
      rw [renewalBlockKernel_first T (Finset.mem_Icc.mp hj).1]
    · rw [renewal_block_step hT b i, ih (by omega) (by omega)]
      exact (renewalBlockKernel_action_step T (by omega) (by omega)
        (fun j => renewal T (b * T + j))).symm

end Sidon30
