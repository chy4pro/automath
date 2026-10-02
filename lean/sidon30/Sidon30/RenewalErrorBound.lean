/-
An explicit enclosing interval for every positive renewal block.
The finite ramp identity locates 1 in that interval and turns contraction into
an error estimate for the actual renewal correction.
-/
import Sidon30.CorrectionBasic
import Sidon30.RenewalFirstBlock
import Sidon30.RenewalBlockContraction
import Sidon30.RenewalRampIdentity

namespace Sidon30

open scoped BigOperators

/-- Explicit lower and upper endpoints enclosing the b-th positive renewal block. -/
noncomputable def renewalBlockInterval (T : ℕ) : ℕ → ℝ × ℝ
  | 0 => (1 / 2, 3 / 2)
  | b + 1 =>
    let previous := renewalBlockInterval T b
    let center := renewalBlockCenter T (fun j => renewal T (b * T + j))
    (center + (1 - renewalBlockCommonMass T) * previous.1,
      center + (1 - renewalBlockCommonMass T) * previous.2)

@[simp]
theorem renewalBlockInterval_zero (T : ℕ) :
    renewalBlockInterval T 0 = ((1 / 2 : ℝ), (3 / 2 : ℝ)) := rfl

/-- Every entry of a block lies between its recursively specified endpoints. -/
theorem renewal_mem_blockInterval {T : ℕ} (hT : 1 ≤ T) (b : ℕ) :
    ∀ i : ℕ, 1 ≤ i → i ≤ T →
      (renewalBlockInterval T b).1 ≤ renewal T (b * T + i) ∧
        renewal T (b * T + i) ≤ (renewalBlockInterval T b).2 := by
  induction b with
  | zero =>
    intro i hi hiT
    simpa only [renewalBlockInterval_zero, zero_mul, zero_add] using
      renewal_firstBlock_bounds hT hi hiT
  | succ b ih =>
    intro i hi hiT
    change
      renewalBlockCenter T (fun j => renewal T (b * T + j)) +
          (1 - renewalBlockCommonMass T) * (renewalBlockInterval T b).1 ≤
            renewal T ((b + 1) * T + i) ∧
        renewal T ((b + 1) * T + i) ≤
          renewalBlockCenter T (fun j => renewal T (b * T + j)) +
            (1 - renewalBlockCommonMass T) * (renewalBlockInterval T b).2
    exact renewal_block_interval hT b
      (renewalBlockInterval T b).1 (renewalBlockInterval T b).2 ih i hi hiT

/-- The lower endpoint never exceeds the upper endpoint. -/
theorem renewalBlockInterval_order {T : ℕ} (hT : 1 ≤ T) (b : ℕ) :
    (renewalBlockInterval T b).1 ≤ (renewalBlockInterval T b).2 := by
  have hmem := renewal_mem_blockInterval hT b 1 (by omega) hT
  exact hmem.1.trans hmem.2

/-- The interval width decays geometrically from its initial width one. -/
theorem renewalBlockInterval_width {T : ℕ} (hT : 1 ≤ T) (b : ℕ) :
    (renewalBlockInterval T b).2 - (renewalBlockInterval T b).1 ≤ (3 / 4 : ℝ) ^ b := by
  induction b with
  | zero => norm_num [renewalBlockInterval_zero]
  | succ b ih =>
    calc
      (renewalBlockInterval T (b + 1)).2 - (renewalBlockInterval T (b + 1)).1 ≤
          (3 / 4 : ℝ) * ((renewalBlockInterval T b).2 - (renewalBlockInterval T b).1) :=
        renewalBlock_interval_width hT (fun j => renewal T (b * T + j))
          (renewalBlockInterval_order hT b)
      _ ≤ (3 / 4 : ℝ) * (3 / 4 : ℝ) ^ b :=
        mul_le_mul_of_nonneg_left ih (by norm_num)
      _ = (3 / 4 : ℝ) ^ (b + 1) := by rw [pow_succ]; ring

/-- At the right endpoint, the ramp averages only entries of the current positive block. -/
theorem renewal_block_convex_identity {T : ℕ} (hT : 1 ≤ T) (b : ℕ) :
    (∑ j ∈ Finset.range T, rampWeight T j * renewal T (b * T + (T - j))) = 1 := by
  have hmul : (b + 1) * T = b * T + T := by ring
  calc
    (∑ j ∈ Finset.range T, rampWeight T j * renewal T (b * T + (T - j))) =
        ∑ j ∈ Finset.range T,
          rampWeight T j * renewalInt T ((((b + 1) * T : ℕ) : ℤ) - (j : ℤ)) := by
      apply Finset.sum_congr rfl
      intro j hj
      have hjT : j < T := Finset.mem_range.mp hj
      have hcast : (((b + 1) * T : ℕ) : ℤ) - (j : ℤ) =
          ((b * T + (T - j) : ℕ) : ℤ) := by
        rw [hmul]
        omega
      rw [hcast, renewalInt_natCast]
    _ = 1 := sum_rampWeight_mul_renewalInt_nat hT ((b + 1) * T)

/-- The exact convolution identity locates the constant 1 inside every block interval. -/
theorem one_mem_renewalBlockInterval {T : ℕ} (hT : 1 ≤ T) (b : ℕ) :
    (renewalBlockInterval T b).1 ≤ 1 ∧ 1 ≤ (renewalBlockInterval T b).2 := by
  have hconv := renewal_block_convex_identity hT b
  have hlower : (renewalBlockInterval T b).1 ≤
      ∑ j ∈ Finset.range T, rampWeight T j * renewal T (b * T + (T - j)) := by
    calc
      (renewalBlockInterval T b).1 =
          (∑ j ∈ Finset.range T, rampWeight T j) * (renewalBlockInterval T b).1 := by
        rw [sum_rampWeight hT, one_mul]
      _ = ∑ j ∈ Finset.range T, rampWeight T j * (renewalBlockInterval T b).1 := by
        rw [Finset.sum_mul]
      _ ≤ _ := by
        apply Finset.sum_le_sum
        intro j hj
        have hjT : j < T := Finset.mem_range.mp hj
        have hmem := renewal_mem_blockInterval hT b (T - j) (by omega) (by omega)
        exact mul_le_mul_of_nonneg_left hmem.1 (rampWeight_nonneg T j)
  have hupper :
      (∑ j ∈ Finset.range T, rampWeight T j * renewal T (b * T + (T - j))) ≤
        (renewalBlockInterval T b).2 := by
    calc
      (∑ j ∈ Finset.range T, rampWeight T j * renewal T (b * T + (T - j))) ≤
          ∑ j ∈ Finset.range T, rampWeight T j * (renewalBlockInterval T b).2 := by
        apply Finset.sum_le_sum
        intro j hj
        have hjT : j < T := Finset.mem_range.mp hj
        have hmem := renewal_mem_blockInterval hT b (T - j) (by omega) (by omega)
        exact mul_le_mul_of_nonneg_left hmem.2 (rampWeight_nonneg T j)
      _ = (∑ j ∈ Finset.range T, rampWeight T j) * (renewalBlockInterval T b).2 := by
        rw [Finset.sum_mul]
      _ = (renewalBlockInterval T b).2 := by rw [sum_rampWeight hT, one_mul]
  rw [hconv] at hlower hupper
  exact ⟨hlower, hupper⟩

/-- Every entry of block b differs from 1 by at most the geometric interval width. -/
theorem renewal_block_abs_bound {T : ℕ} (hT : 1 ≤ T) (b i : ℕ)
    (hi : 1 ≤ i) (hiT : i ≤ T) :
    |renewal T (b * T + i) - 1| ≤ (3 / 4 : ℝ) ^ b := by
  have hmem := renewal_mem_blockInterval hT b i hi hiT
  have hone := one_mem_renewalBlockInterval hT b
  have habs : |renewal T (b * T + i) - 1| ≤
      (renewalBlockInterval T b).2 - (renewalBlockInterval T b).1 := by
    apply abs_le.mpr
    constructor <;> linarith
  exact habs.trans (renewalBlockInterval_width hT b)

/-- The actual signed renewal correction satisfies the required pointwise decay estimate. -/
theorem renewalCorrection_bound {T n : ℕ} (hT : 1 ≤ T) (hn : 1 ≤ n) :
    |renewalCorrection T n| ≤ (3 / 4 : ℝ) ^ ((n - 1) / T) := by
  let b : ℕ := (n - 1) / T
  let i : ℕ := (n - 1) % T + 1
  have hi : 1 ≤ i := by dsimp [i]; omega
  have hiT : i ≤ T := by
    have hmod := Nat.mod_lt (n - 1) (show 0 < T by omega)
    dsimp [i]
    omega
  have hrepr : n = b * T + i := by
    have hdiv := Nat.mod_add_div (n - 1) T
    have hcomm : T * ((n - 1) / T) = ((n - 1) / T) * T := Nat.mul_comm _ _
    dsimp [b, i]
    omega
  have hbound := renewal_block_abs_bound hT b i hi hiT
  rw [← hrepr] at hbound
  unfold renewalCorrection
  exact hbound

end Sidon30
