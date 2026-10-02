import Sidon30.TransferStatement
import Sidon30.IndexedRampCertificate

/-! Exact column marginal via all sliding windows, including both boundary
ramps. The finite sets count columns even when row coordinates repeat. -/

open scoped BigOperators
namespace Sidon30

/-- A length-U window with right endpoint k, intersected with m columns. -/
def sonarWindow (m U k : ℕ) : Finset ℕ :=
  (Finset.range m).filter (fun i => i < k ∧ k ≤ i + U)

theorem sonarWindow_eq_Ico (m U k : ℕ) :
    sonarWindow m U k = Finset.Ico (k - U) (min k m) := by
  ext i
  simp only [sonarWindow, Finset.mem_filter, Finset.mem_range, Finset.mem_Ico]
  omega

theorem sonarWindow_card (m U k : ℕ) :
    (sonarWindow m U k).card = min k m - (k - U) := by
  rw [sonarWindow_eq_Ico, Nat.card_Ico]

theorem sonarWindow_card_left {m U k : ℕ} (hU : U ≤ m) (hk : k ≤ U) :
    (sonarWindow m U k).card = k := by
  rw [sonarWindow_card]
  omega

theorem sonarWindow_card_middle {m U k : ℕ} (hkU : U ≤ k) (hkm : k ≤ m) :
    (sonarWindow m U k).card = U := by
  rw [sonarWindow_card]
  omega

theorem sonarWindow_card_right {m U k : ℕ} (hU : U ≤ m)
    (hmk : m ≤ k) (hk : k ≤ m + U) :
    (sonarWindow m U k).card = m + U - k := by
  rw [sonarWindow_card]
  omega

theorem sum_range_sq_real (U : ℕ) :
    (∑ k ∈ Finset.range U, (k : ℝ) ^ 2) =
      (U : ℝ) * ((U : ℝ) - 1) * (2 * (U : ℝ) - 1) / 6 := by
  induction U with
  | zero => norm_num
  | succ U ih =>
      rw [Finset.sum_range_succ, ih]
      push_cast
      ring

/-- Every column is present in exactly U windows. -/
theorem sonarWindow_index_support {m U i : ℕ} (hi : i < m) :
    (Finset.range (m + U)).filter (fun k => i ∈ sonarWindow m U k) =
      Finset.Ico (i + 1) (i + U + 1) := by
  ext k
  simp only [Finset.mem_filter, Finset.mem_range, sonarWindow]
  simp only [Finset.mem_filter, Finset.mem_range, Finset.mem_Ico]
  omega

/-- The common windows of two columns depend only on their displacement. -/
theorem sonarWindow_pair_support {m U i j : ℕ} (hi : i < m) (hj : j < m) :
    (Finset.range (m + U)).filter
      (fun k => i ∈ sonarWindow m U k ∧ j ∈ sonarWindow m U k) =
      Finset.Ico (max i j + 1) (min i j + U + 1) := by
  ext k
  simp only [Finset.mem_filter, Finset.mem_range, sonarWindow]
  simp only [Finset.mem_filter, Finset.mem_range, Finset.mem_Ico]
  omega

theorem sonarWindow_pair_count {m U i j : ℕ} (hi : i < m) (hj : j < m) :
    ((Finset.range (m + U)).filter
      (fun k => i ∈ sonarWindow m U k ∧ j ∈ sonarWindow m U k)).card =
      U - (max i j - min i j) := by
  rw [sonarWindow_pair_support hi hj, Nat.card_Ico]
  omega

end Sidon30
