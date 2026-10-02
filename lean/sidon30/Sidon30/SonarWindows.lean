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

theorem sum_range_id_real (U : ℕ) :
    (∑ k ∈ Finset.range U, (k : ℝ)) = (U : ℝ) * ((U : ℝ) - 1) / 2 := by
  induction U with
  | zero => norm_num
  | succ U ih =>
      rw [Finset.sum_range_succ, ih]
      push_cast
      ring

theorem sum_range_sub_sq_real (U : ℕ) :
    (∑ k ∈ Finset.range U, ((U : ℝ) - (k : ℝ)) ^ 2) =
      (U : ℝ) * ((U : ℝ) + 1) * (2 * (U : ℝ) + 1) / 6 := by
  simp only [sub_sq, Finset.sum_add_distrib, Finset.sum_sub_distrib,
    ← Finset.mul_sum, Finset.sum_const, nsmul_eq_mul, Finset.card_range]
  rw [sum_range_id_real, sum_range_sq_real]
  ring

/-- Exact column marginal, with the two truncated boundary ramps retained. -/
theorem sonarWindow_card_sq_sum {m U : ℕ} (hU : U ≤ m) :
    (∑ k ∈ Finset.range (m + U), ((sonarWindow m U k).card : ℝ) ^ 2) =
      (m : ℝ) * (U : ℝ) ^ 2 - ((U : ℝ) ^ 3 - (U : ℝ)) / 3 := by
  have hm : m = U + (m - U) := by omega
  have hleft : (∑ k ∈ Finset.range U, ((sonarWindow m U k).card : ℝ) ^ 2) =
      ∑ k ∈ Finset.range U, (k : ℝ) ^ 2 := by
    apply Finset.sum_congr rfl
    intro k hk
    rw [sonarWindow_card_left hU (by have := Finset.mem_range.mp hk; omega)]
  have hmiddle :
      (∑ k ∈ Finset.range (m - U), ((sonarWindow m U (U + k)).card : ℝ) ^ 2) =
      ((m : ℝ) - (U : ℝ)) * (U : ℝ) ^ 2 := by
    calc
      _ = ∑ _k ∈ Finset.range (m - U), (U : ℝ) ^ 2 := by
        apply Finset.sum_congr rfl
        intro k hk
        rw [sonarWindow_card_middle (by omega) (by have := Finset.mem_range.mp hk; omega)]
      _ = _ := by simp [Nat.cast_sub hU]
  have hright :
      (∑ k ∈ Finset.range U, ((sonarWindow m U (m + k)).card : ℝ) ^ 2) =
      ∑ k ∈ Finset.range U, ((U : ℝ) - (k : ℝ)) ^ 2 := by
    apply Finset.sum_congr rfl
    intro k hk
    have hkU : k ≤ U := by have := Finset.mem_range.mp hk; omega
    rw [sonarWindow_card_right hU (by omega) (by omega)]
    have heq : m + U - (m + k) = U - k := by omega
    rw [heq, Nat.cast_sub hkU]
  calc
    _ = (∑ k ∈ Finset.range U, ((sonarWindow m U k).card : ℝ) ^ 2) +
        (∑ k ∈ Finset.range (m - U), ((sonarWindow m U (U + k)).card : ℝ) ^ 2) +
        (∑ k ∈ Finset.range U, ((sonarWindow m U (m + k)).card : ℝ) ^ 2) := by
      rw [Finset.sum_range_add]
      congr 1
      conv_lhs => rw [hm]
      rw [Finset.sum_range_add]
    _ = _ := by
      rw [hleft, hmiddle, hright, sum_range_sq_real, sum_range_sub_sq_real]
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

def sonarFinWindow (m U k : ℕ) : Finset (Fin m) :=
  Finset.univ.filter (fun i => i.val < k ∧ k ≤ i.val + U)

theorem sonarFinWindow_card (m U k : ℕ) :
    (sonarFinWindow m U k).card = (sonarWindow m U k).card := by
  have himage : (sonarFinWindow m U k).image Fin.val = sonarWindow m U k := by
    ext i
    constructor
    · intro hi
      obtain ⟨j, hj, rfl⟩ := Finset.mem_image.mp hi
      have hwindow := (Finset.mem_filter.mp hj).2
      exact Finset.mem_filter.mpr ⟨Finset.mem_range.mpr j.isLt, hwindow⟩
    · intro hi
      obtain ⟨him, hwindow⟩ := Finset.mem_filter.mp hi
      refine Finset.mem_image.mpr ⟨⟨i, Finset.mem_range.mp him⟩, ?_, rfl⟩
      exact Finset.mem_filter.mpr ⟨Finset.mem_univ _, hwindow⟩
  rw [← himage, Finset.card_image_of_injOn]
  intro i _hi j _hj hij
  exact Fin.ext hij

theorem sonarFinWindow_card_sq_sum {m U : ℕ} (hU : U ≤ m) :
    (∑ k ∈ Finset.range (m + U), ((sonarFinWindow m U k).card : ℝ) ^ 2) =
      (m : ℝ) * (U : ℝ) ^ 2 - ((U : ℝ) ^ 3 - (U : ℝ)) / 3 := by
  simp_rw [sonarFinWindow_card]
  exact sonarWindow_card_sq_sum hU

theorem sonarFinWindow_pair_count {m U : ℕ} (i j : Fin m) :
    ((Finset.range (m + U)).filter
      (fun k => i ∈ sonarFinWindow m U k ∧ j ∈ sonarFinWindow m U k)).card =
      U - (max i.val j.val - min i.val j.val) := by
  have hfin : ∀ k (i : Fin m),
      i ∈ sonarFinWindow m U k ↔ i.val ∈ sonarWindow m U k := by
    intro k i
    simp only [sonarFinWindow, sonarWindow, Finset.mem_filter, Finset.mem_univ,
      Finset.mem_range, i.isLt, true_and]
  simp_rw [hfin]
  exact sonarWindow_pair_count i.isLt j.isLt

/-- Summing local row energies produces the exact discrete triangle weight. -/
theorem sonarFinWindow_sum_energy {m U : ℕ} (F : Fin m → Fin m → ℝ) :
    (∑ k ∈ Finset.range (m + U),
      ∑ i ∈ sonarFinWindow m U k, ∑ j ∈ sonarFinWindow m U k, F i j) =
    ∑ i : Fin m, ∑ j : Fin m,
      ((U - (max i.val j.val - min i.val j.val) : ℕ) : ℝ) * F i j := by
  simp only [sonarFinWindow, Finset.sum_filter]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro i _hi
  have hinner : ∀ k,
      (if i.val < k ∧ k ≤ i.val + U then
        ∑ j : Fin m, if j.val < k ∧ k ≤ j.val + U then F i j else 0 else 0) =
      ∑ j : Fin m, if (i.val < k ∧ k ≤ i.val + U) ∧
          (j.val < k ∧ k ≤ j.val + U) then F i j else 0 := by
    intro k
    by_cases h : i.val < k ∧ k ≤ i.val + U <;> simp [h]
  simp_rw [hinner]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro j _hj
  rw [← Finset.sum_filter]
  have hcount := sonarFinWindow_pair_count (U := U) i j
  simp only [sonarFinWindow, Finset.mem_filter, Finset.mem_univ, true_and] at hcount
  simp only [Finset.sum_const, nsmul_eq_mul, hcount]

end Sidon30
