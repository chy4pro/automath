/-
A common nonnegative part of all renewal transition rows gives an explicit
three-quarter contraction of enclosing intervals.
-/
import Sidon30.RenewalBlockMatrix

namespace Sidon30

open scoped BigOperators

/-- The elementary Bernoulli bound needed for the lower matrix entries. -/
theorem renewalBlock_pow_lower (T j : ℕ) :
    1 + (j : ℝ) * (1 / (T : ℝ)) ≤ (1 + 1 / (T : ℝ)) ^ j := by
  have hq : (0 : ℝ) ≤ 1 / (T : ℝ) := by positivity
  induction j with
  | zero => simp
  | succ j ih =>
    rw [pow_succ]
    have hmul := mul_le_mul_of_nonneg_right ih
      (show (0 : ℝ) ≤ 1 + 1 / (T : ℝ) by positivity)
    have hquadratic : 0 ≤ (j : ℝ) * (1 / (T : ℝ)) ^ 2 := by positivity
    push_cast
    nlinarith

/-- Every column in the last ceiling-half has a uniform lower bound. -/
theorem renewalBlockKernel_half_lower {T i j : ℕ} (hT : 1 ≤ T)
    (hjhalf : (T + 1) / 2 ≤ j) :
    1 / (2 * (T : ℝ)) ≤ renewalBlockKernel T i j := by
  have hTpos : (0 : ℝ) < T := by exact_mod_cast (show 0 < T by omega)
  have hTne : (T : ℝ) ≠ 0 := ne_of_gt hTpos
  have hq : (0 : ℝ) ≤ 1 / (T : ℝ) := by positivity
  have hbase : (1 : ℝ) ≤ 1 + 1 / (T : ℝ) := by linarith
  have hcoeff : (1 : ℝ) / (2 * (T : ℝ)) = (1 / (T : ℝ)) * (1 / 2) := by
    field_simp [hTne] <;> ring
  by_cases hij : i ≤ j
  · rw [renewalBlockKernel, if_pos hij, hcoeff]
    apply mul_le_mul_of_nonneg_left _ hq
    have hp : (1 : ℝ) ≤ (1 + 1 / (T : ℝ)) ^ (i - 1) := one_le_pow₀ hbase
    linarith
  · have hjNat : T ≤ 2 * j := by omega
    have hjReal : (T : ℝ) ≤ 2 * (j : ℝ) := by exact_mod_cast hjNat
    have hhalf : (1 / 2 : ℝ) ≤ (j : ℝ) / (T : ℝ) := by
      apply (le_div_iff₀ hTpos).2
      linarith
    have hbern := renewalBlock_pow_lower T j
    have hr : (1 / 2 : ℝ) ≤ (1 + 1 / (T : ℝ)) ^ j - 1 := by
      simp only [div_eq_mul_inv, one_mul] at hhalf hbern ⊢
      linarith
    have hp : (1 : ℝ) ≤ (1 + 1 / (T : ℝ)) ^ (i - j - 1) := one_le_pow₀ hbase
    have hprod : (1 / 2 : ℝ) ≤
        (1 + 1 / (T : ℝ)) ^ (i - j - 1) * ((1 + 1 / (T : ℝ)) ^ j - 1) := by
      simpa only [one_mul] using mul_le_mul hp hr (by norm_num) (by positivity)
    rw [renewalBlockKernel, if_neg hij, hcoeff]
    calc
      (1 / (T : ℝ)) * (1 / 2) ≤ (1 / (T : ℝ)) *
          ((1 + 1 / (T : ℝ)) ^ (i - j - 1) * ((1 + 1 / (T : ℝ)) ^ j - 1)) :=
        mul_le_mul_of_nonneg_left hprod hq
      _ = _ := by ring

/-- A common part of every transition row, supported on the last ceiling-half. -/
noncomputable def renewalBlockMinorant (T j : ℕ) : ℝ :=
  if (T + 1) / 2 ≤ j then 1 / (2 * (T : ℝ)) else 0

/-- Total common mass of the transition rows. -/
noncomputable def renewalBlockCommonMass (T : ℕ) : ℝ :=
  ∑ j ∈ Finset.Icc 1 T, renewalBlockMinorant T j

/-- The part of the next block shared by every row. -/
noncomputable def renewalBlockCenter (T : ℕ) (v : ℕ → ℝ) : ℝ :=
  ∑ j ∈ Finset.Icc 1 T, renewalBlockMinorant T j * v j

theorem renewalBlockMinorant_nonneg (T j : ℕ) : 0 ≤ renewalBlockMinorant T j := by
  unfold renewalBlockMinorant
  split_ifs <;> positivity

/-- The common part is dominated entrywise by every matrix row. -/
theorem renewalBlockMinorant_le_kernel {T : ℕ} (hT : 1 ≤ T) (i j : ℕ) :
    renewalBlockMinorant T j ≤ renewalBlockKernel T i j := by
  unfold renewalBlockMinorant
  split_ifs with hj
  · exact renewalBlockKernel_half_lower hT hj
  · exact renewalBlockKernel_nonneg T i j

/-- Exact finite counting formula for the common mass. -/
theorem renewalBlockCommonMass_eq {T : ℕ} (hT : 1 ≤ T) :
    renewalBlockCommonMass T =
      ((T + 1 - (T + 1) / 2 : ℕ) : ℝ) / (2 * (T : ℝ)) := by
  have hceil : 1 ≤ (T + 1) / 2 := by omega
  have hset : (Finset.Icc 1 T).filter (fun j => (T + 1) / 2 ≤ j) =
      Finset.Icc ((T + 1) / 2) T := by
    ext j
    simp only [Finset.mem_filter, Finset.mem_Icc]
    omega
  unfold renewalBlockCommonMass renewalBlockMinorant
  rw [← Finset.sum_filter, hset]
  simp only [Finset.sum_const, Nat.card_Icc, nsmul_eq_mul]
  ring

/-- At least one quarter of every row is common, and the common mass is at most one. -/
theorem renewalBlockCommonMass_bounds {T : ℕ} (hT : 1 ≤ T) :
    (1 / 4 : ℝ) ≤ renewalBlockCommonMass T ∧ renewalBlockCommonMass T ≤ 1 := by
  have hTpos : (0 : ℝ) < T := by exact_mod_cast (show 0 < T by omega)
  have hden : (0 : ℝ) < 2 * (T : ℝ) := by positivity
  have hloNat : T ≤ 2 * (T + 1 - (T + 1) / 2) := by omega
  have hhiNat : T + 1 - (T + 1) / 2 ≤ T := by omega
  have hlo : (T : ℝ) ≤ 2 * ((T + 1 - (T + 1) / 2 : ℕ) : ℝ) := by
    exact_mod_cast hloNat
  have hhi : ((T + 1 - (T + 1) / 2 : ℕ) : ℝ) ≤ (T : ℝ) := by
    exact_mod_cast hhiNat
  rw [renewalBlockCommonMass_eq hT]
  constructor
  · apply (le_div_iff₀ hden).2
    nlinarith
  · apply (div_le_iff₀ hden).2
    nlinarith

/-- All row images lie in one explicitly specified smaller interval. -/
theorem renewalBlock_interval {T : ℕ} (hT : 1 ≤ T) (v : ℕ → ℝ) (l u : ℝ)
    (hv : ∀ j : ℕ, 1 ≤ j → j ≤ T → l ≤ v j ∧ v j ≤ u)
    (i : ℕ) (hi : 1 ≤ i) (hiT : i ≤ T) :
    renewalBlockCenter T v + (1 - renewalBlockCommonMass T) * l ≤
      (∑ j ∈ Finset.Icc 1 T, renewalBlockKernel T i j * v j) ∧
    (∑ j ∈ Finset.Icc 1 T, renewalBlockKernel T i j * v j) ≤
      renewalBlockCenter T v + (1 - renewalBlockCommonMass T) * u := by
  have hres (j : ℕ) : 0 ≤ renewalBlockKernel T i j - renewalBlockMinorant T j :=
    sub_nonneg.mpr (renewalBlockMinorant_le_kernel hT i j)
  have hmass :
      (∑ j ∈ Finset.Icc 1 T, renewalBlockKernel T i j - renewalBlockMinorant T j) =
        1 - renewalBlockCommonMass T := by
    change (∑ j ∈ Finset.Icc 1 T, renewalBlockKernel T i j - renewalBlockMinorant T j) =
      1 - ∑ j ∈ Finset.Icc 1 T, renewalBlockMinorant T j
    rw [Finset.sum_sub_distrib, sum_renewalBlockKernel hT i hi hiT]
  have hdecomp :
      (∑ j ∈ Finset.Icc 1 T, renewalBlockKernel T i j * v j) =
        renewalBlockCenter T v +
          ∑ j ∈ Finset.Icc 1 T, (renewalBlockKernel T i j - renewalBlockMinorant T j) * v j := by
    unfold renewalBlockCenter
    rw [← Finset.sum_add_distrib]
    apply Finset.sum_congr rfl
    intro j _hj
    ring
  have hlower : (1 - renewalBlockCommonMass T) * l ≤
      ∑ j ∈ Finset.Icc 1 T, (renewalBlockKernel T i j - renewalBlockMinorant T j) * v j := by
    calc
      (1 - renewalBlockCommonMass T) * l =
          (∑ j ∈ Finset.Icc 1 T, renewalBlockKernel T i j - renewalBlockMinorant T j) * l := by
        rw [hmass]
      _ = ∑ j ∈ Finset.Icc 1 T,
          (renewalBlockKernel T i j - renewalBlockMinorant T j) * l := by rw [Finset.sum_mul]
      _ ≤ _ := by
        apply Finset.sum_le_sum
        intro j hj
        exact mul_le_mul_of_nonneg_left
          (hv j (Finset.mem_Icc.mp hj).1 (Finset.mem_Icc.mp hj).2).1 (hres j)
  have hupper :
      (∑ j ∈ Finset.Icc 1 T, (renewalBlockKernel T i j - renewalBlockMinorant T j) * v j) ≤
        (1 - renewalBlockCommonMass T) * u := by
    calc
      (∑ j ∈ Finset.Icc 1 T, (renewalBlockKernel T i j - renewalBlockMinorant T j) * v j) ≤
          ∑ j ∈ Finset.Icc 1 T, (renewalBlockKernel T i j - renewalBlockMinorant T j) * u := by
        apply Finset.sum_le_sum
        intro j hj
        exact mul_le_mul_of_nonneg_left
          (hv j (Finset.mem_Icc.mp hj).1 (Finset.mem_Icc.mp hj).2).2 (hres j)
      _ = (1 - renewalBlockCommonMass T) * u := by rw [← Finset.sum_mul, hmass]
  rw [hdecomp]
  constructor <;> linarith

/-- The two explicit enclosing endpoints remain in increasing order. -/
theorem renewalBlock_interval_order {T : ℕ} (hT : 1 ≤ T)
    (v : ℕ → ℝ) {l u : ℝ} (hlu : l ≤ u) :
    renewalBlockCenter T v + (1 - renewalBlockCommonMass T) * l ≤
      renewalBlockCenter T v + (1 - renewalBlockCommonMass T) * u := by
  have hcoef : 0 ≤ 1 - renewalBlockCommonMass T :=
    sub_nonneg.mpr (renewalBlockCommonMass_bounds hT).2
  exact add_le_add_left (mul_le_mul_of_nonneg_left hlu hcoef) _

/-- The width contracts by at least the factor three quarters. -/
theorem renewalBlock_interval_width {T : ℕ} (hT : 1 ≤ T)
    (v : ℕ → ℝ) {l u : ℝ} (hlu : l ≤ u) :
    (renewalBlockCenter T v + (1 - renewalBlockCommonMass T) * u) -
        (renewalBlockCenter T v + (1 - renewalBlockCommonMass T) * l) ≤
      (3 / 4 : ℝ) * (u - l) := by
  have hcoef : 1 - renewalBlockCommonMass T ≤ (3 / 4 : ℝ) := by
    have := (renewalBlockCommonMass_bounds hT).1
    linarith
  have hmul := mul_le_mul_of_nonneg_right hcoef (sub_nonneg.mpr hlu)
  nlinarith

/-- The explicit contracted interval contains every entry of the next renewal block. -/
theorem renewal_block_interval {T : ℕ} (hT : 1 ≤ T) (b : ℕ) (l u : ℝ)
    (hv : ∀ j : ℕ, 1 ≤ j → j ≤ T →
      l ≤ renewal T (b * T + j) ∧ renewal T (b * T + j) ≤ u)
    (i : ℕ) (hi : 1 ≤ i) (hiT : i ≤ T) :
    renewalBlockCenter T (fun j => renewal T (b * T + j)) +
        (1 - renewalBlockCommonMass T) * l ≤ renewal T ((b + 1) * T + i) ∧
    renewal T ((b + 1) * T + i) ≤
      renewalBlockCenter T (fun j => renewal T (b * T + j)) +
        (1 - renewalBlockCommonMass T) * u := by
  rw [renewal_block_matrix hT b i hi hiT]
  exact renewalBlock_interval hT (fun j => renewal T (b * T + j)) l u hv i hi hiT

end Sidon30
