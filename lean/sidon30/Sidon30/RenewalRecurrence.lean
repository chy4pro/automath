/-
A positive renewal array for the normalized discrete ramp.
Only earlier natural indices are used; the integer extension is zero to the left.
-/
import Mathlib

namespace Sidon30

open scoped BigOperators

private noncomputable def renewalStep (T n : ℕ)
    (previous : ∀ k : ℕ, k < n → ℝ) : ℝ :=
  if n = 0 then ((T : ℝ) + 1) / 2
  else (1 / (T : ℝ)) * ∑ k : Finset.range n,
    if n - (k : ℕ) ≤ T then previous k (Finset.mem_range.mp k.property) else 0

/-- The renewal array, constructed by strong recursion on the natural index. -/
noncomputable def renewal (T n : ℕ) : ℝ :=
  Nat.strongRecOn n (renewalStep T)

/-- The recursion equation in forward-prefix form. -/
theorem renewal_eq_prefix (T n : ℕ) :
    renewal T n =
      if n = 0 then ((T : ℝ) + 1) / 2
      else (1 / (T : ℝ)) * ∑ k ∈ Finset.range n,
        if n - k ≤ T then renewal T k else 0 := by
  change Nat.lt_wfRel.wf.fix (renewalStep T) n = _
  rw [WellFounded.fix_eq]
  change
    (if n = 0 then ((T : ℝ) + 1) / 2
     else (1 / (T : ℝ)) * ∑ k : Finset.range n,
       if n - (k : ℕ) ≤ T then renewal T k else 0) = _
  by_cases hn : n = 0
  · simp only [if_pos hn]
  · simp only [if_neg hn]
    exact congrArg (fun x : ℝ => (1 / (T : ℝ)) * x)
      (Finset.sum_coe_sort (Finset.range n)
        (fun k : ℕ => if n - k ≤ T then renewal T k else 0))

@[simp]
theorem renewal_zero (T : ℕ) :
    renewal T 0 = ((T : ℝ) + 1) / 2 := by
  rw [renewal_eq_prefix]
  simp

/-- The positive-index recurrence with forward indices. -/
theorem renewal_eq_prefix_of_pos (T n : ℕ) (hn : 0 < n) :
    renewal T n = (1 / (T : ℝ)) * ∑ k ∈ Finset.range n,
      if n - k ≤ T then renewal T k else 0 := by
  rw [renewal_eq_prefix, if_neg (Nat.ne_of_gt hn)]

/-- A successor version useful in finite-difference calculations. -/
theorem renewal_succ_prefix (T n : ℕ) :
    renewal T (n + 1) = (1 / (T : ℝ)) * ∑ k ∈ Finset.range (n + 1),
      if n + 1 - k ≤ T then renewal T k else 0 := by
  exact renewal_eq_prefix_of_pos T (n + 1) (by omega)

private theorem renewal_prefix_sum (T n : ℕ) :
    (∑ k ∈ Finset.range n, if n - k ≤ T then renewal T k else 0) =
      ∑ i ∈ Finset.Icc 1 (min T n), renewal T (n - i) := by
  rw [← Finset.sum_filter]
  refine Finset.sum_bij (fun k _ => n - k) ?_ ?_ ?_ ?_
  · intro k hk
    rcases Finset.mem_filter.mp hk with ⟨hkn, hkT⟩
    have hkn' : k < n := Finset.mem_range.mp hkn
    exact Finset.mem_Icc.mpr ⟨by omega, le_min hkT (Nat.sub_le n k)⟩
  · intro a ha b hb hab
    have han : a < n := Finset.mem_range.mp (Finset.mem_filter.mp ha).1
    have hbn : b < n := Finset.mem_range.mp (Finset.mem_filter.mp hb).1
    omega
  · intro i hi
    rcases Finset.mem_Icc.mp hi with ⟨hi1, himin⟩
    have hiT : i ≤ T := le_trans himin (min_le_left T n)
    have hin : i ≤ n := le_trans himin (min_le_right T n)
    refine ⟨n - i, ?_, by omega⟩
    exact Finset.mem_filter.mpr ⟨Finset.mem_range.mpr (by omega), by omega⟩
  · intro k hk
    have hkn : k < n := Finset.mem_range.mp (Finset.mem_filter.mp hk).1
    have hback : n - (n - k) = k := by omega
    rw [hback]

/-- The renewal equation in the lag-indexed form of the finite certificate. -/
theorem renewal_eq_of_pos (T n : ℕ) (hn : 0 < n) :
    renewal T n = (1 / (T : ℝ)) *
      ∑ i ∈ Finset.Icc 1 (min T n), renewal T (n - i) := by
  rw [renewal_eq_prefix_of_pos T n hn, renewal_prefix_sum]

/-- Every value of the renewal array is nonnegative, including the harmless T = 0 case. -/
theorem renewal_nonneg (T n : ℕ) : 0 ≤ renewal T n := by
  induction n using Nat.strong_induction_on with
  | h n ih =>
    by_cases hn : n = 0
    · subst n
      rw [renewal_zero]
      positivity
    · rw [renewal_eq_prefix, if_neg hn]
      apply mul_nonneg (by positivity)
      apply Finset.sum_nonneg
      intro k hk
      split_ifs with hkT
      · exact ih k (Finset.mem_range.mp hk)
      · exact le_rfl

/-- The renewal array extended by zero to negative integer indices. -/
noncomputable def renewalInt (T : ℕ) (n : ℤ) : ℝ :=
  if n < 0 then 0 else renewal T n.toNat

@[simp]
theorem renewalInt_of_neg (T : ℕ) {n : ℤ} (hn : n < 0) :
    renewalInt T n = 0 := by
  simp only [renewalInt, if_pos hn]

@[simp]
theorem renewalInt_natCast (T n : ℕ) :
    renewalInt T (n : ℤ) = renewal T n := by
  simp [renewalInt]

/-- Nonnegativity also holds on the whole integer line. -/
theorem renewalInt_nonneg (T : ℕ) (n : ℤ) : 0 ≤ renewalInt T n := by
  unfold renewalInt
  split_ifs
  · exact le_rfl
  · exact renewal_nonneg T n.toNat

end Sidon30
