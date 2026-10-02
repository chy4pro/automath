import Sidon30.RampWeights

/-!
Exact natural scale and finite geometric tail for the weak Sidon transfer.
No asymptotic estimates or numerical approximation enter these lemmas.
-/

noncomputable section

namespace Sidon30

def weakSidonBeta : ℝ := 2 * Real.sqrt 6 / 3

def weakSidonIntegerScale (x : ℝ) : ℕ := Nat.ceil (Real.sqrt 6 * x ^ 3)

theorem weakSidonBeta_pos : 0 < weakSidonBeta := by
  unfold weakSidonBeta
  positivity

theorem weakSidonBeta_sq : weakSidonBeta ^ 2 = (8 : ℝ) / 3 := by
  have hs : (Real.sqrt 6) ^ 2 = (6 : ℝ) := Real.sq_sqrt (by norm_num)
  unfold weakSidonBeta
  nlinarith

theorem weakSidonBeta_lt_two : weakSidonBeta < 2 := by
  have hs := weakSidonBeta_sq
  have hp := weakSidonBeta_pos
  nlinarith

theorem weakSidonBeta_eq_sqrt : weakSidonBeta = Real.sqrt ((8 : ℝ) / 3) := by
  have hs : (Real.sqrt ((8 : ℝ) / 3)) ^ 2 = (8 : ℝ) / 3 :=
    Real.sq_sqrt (by norm_num)
  have hp := weakSidonBeta_pos
  have hnonneg := Real.sqrt_nonneg ((8 : ℝ) / 3)
  have hprod :
      (weakSidonBeta - Real.sqrt ((8 : ℝ) / 3)) *
        (weakSidonBeta + Real.sqrt ((8 : ℝ) / 3)) = 0 := by
    nlinarith [weakSidonBeta_sq]
  rcases mul_eq_zero.mp hprod with h | h
  · linarith
  · linarith

theorem weakSidonIntegerScale_lower (x : ℝ) :
    Real.sqrt 6 * x ^ 3 ≤ (weakSidonIntegerScale x : ℝ) := by
  exact Nat.le_ceil _

theorem weakSidonIntegerScale_lt {x : ℝ} (hx : 0 ≤ x) :
    (weakSidonIntegerScale x : ℝ) < Real.sqrt 6 * x ^ 3 + 1 := by
  exact Nat.ceil_lt_add_one (mul_nonneg (Real.sqrt_nonneg 6) (pow_nonneg hx 3))

theorem weakSidonIntegerScale_pos {x : ℝ} (hx : 0 < x) :
    1 ≤ weakSidonIntegerScale x := by
  have hscale : 0 < Real.sqrt 6 * x ^ 3 := by positivity
  exact Nat.one_le_ceil_iff.mpr hscale

theorem weakSidonIntegerScale_sub_one_le {x : ℝ} (hx : 0 ≤ x) :
    (weakSidonIntegerScale x : ℝ) - 1 ≤ Real.sqrt 6 * x ^ 3 := by
  have h := weakSidonIntegerScale_lt hx
  linarith

theorem weakSidonIntegerScale_upper {x : ℝ} (hx : 90 ≤ x) :
    (weakSidonIntegerScale x : ℝ) ≤ (5 : ℝ) / 2 * x ^ 3 := by
  have hxpos : 0 < x := by linarith
  have hxone : 1 ≤ x := by linarith
  have hx2one : 1 ≤ x ^ 2 := one_le_pow₀ hxone
  have hx3large : (20 : ℝ) ≤ x ^ 3 := by
    have h := mul_le_mul_of_nonneg_left hx2one hxpos.le
    nlinarith
  have hs : Real.sqrt 6 ≤ (49 : ℝ) / 20 := by
    apply (Real.sqrt_le_left (by norm_num : (0 : ℝ) ≤ 49 / 20)).mpr
    norm_num
  have hmul := mul_le_mul_of_nonneg_right hs (pow_nonneg hxpos.le 3)
  have hceil := weakSidonIntegerScale_lt hxpos.le
  linarith

/-- The weak Sidon energy contains three times the ramp diagonal. -/
theorem weakSidonIntegerScale_diagonal_le {x : ℝ} (hx : 0 < x) :
    3 * rampDiagonal (weakSidonIntegerScale x) ≤ weakSidonBeta / x ^ 3 := by
  have hT := weakSidonIntegerScale_pos hx
  have hTpos : (0 : ℝ) < (weakSidonIntegerScale x : ℝ) := by
    exact_mod_cast (show 0 < weakSidonIntegerScale x by omega)
  have hx3pos : 0 < x ^ 3 := pow_pos hx 3
  have hs : (Real.sqrt 6) ^ 2 = (6 : ℝ) := Real.sq_sqrt (by norm_num)
  have hprod : 4 * x ^ 3 ≤ weakSidonBeta * (weakSidonIntegerScale x : ℝ) := by
    calc
      4 * x ^ 3 = (2 / 3 : ℝ) * (Real.sqrt 6) ^ 2 * x ^ 3 := by
        rw [hs]
        ring
      _ = weakSidonBeta * (Real.sqrt 6 * x ^ 3) := by
        unfold weakSidonBeta
        ring
      _ ≤ weakSidonBeta * (weakSidonIntegerScale x : ℝ) :=
        mul_le_mul_of_nonneg_left (weakSidonIntegerScale_lower x)
          weakSidonBeta_pos.le
  calc
    3 * rampDiagonal (weakSidonIntegerScale x) ≤
        3 * (4 / (3 * (weakSidonIntegerScale x : ℝ))) :=
      mul_le_mul_of_nonneg_left (rampDiagonal_le hT) (by norm_num)
    _ = 4 / (weakSidonIntegerScale x : ℝ) := by
      field_simp [ne_of_gt hTpos]
    _ ≤ weakSidonBeta / x ^ 3 :=
      (div_le_div_iff₀ hTpos hx3pos).mpr hprod

theorem weakSidonIntegerScale_boundary_le {N : ℕ} {x : ℝ}
    (hx : 0 ≤ x) (hN : x ^ 4 = (N : ℝ)) :
    (N : ℝ) + (2 : ℝ) / 3 * ((weakSidonIntegerScale x : ℝ) - 1) ≤
      x ^ 4 + weakSidonBeta * x ^ 3 := by
  have h := weakSidonIntegerScale_sub_one_le hx
  unfold weakSidonBeta
  nlinarith

/-- Natural division gives the needed envelope without real floors. -/
theorem weakSidonIntegerQuotient_scale_bound {N T : ℕ} {x : ℝ}
    (hx : 90 ≤ x) (hN : x ^ 4 = (N : ℝ)) (hT : 1 ≤ T)
    (hTupper : (T : ℝ) ≤ (5 : ℝ) / 2 * x ^ 3) :
    x ≤ (5 : ℝ) / 2 * ((((N - 1) / T : ℕ) : ℝ) + 2) := by
  have hxpos : 0 < x := by linarith
  have hxone : 1 ≤ x := by linarith
  have hx3pos : 0 < x ^ 3 := pow_pos hxpos 3
  have hx3one : 1 ≤ x ^ 3 := one_le_pow₀ hxone
  have hNposR : (0 : ℝ) < (N : ℝ) := by
    rw [← hN]
    exact pow_pos hxpos 4
  have hNpos : 0 < N := by exact_mod_cast hNposR
  have hNOne : 1 ≤ N := by omega
  have hTpos : 0 < T := by omega
  have hdiv : N - 1 < T * ((N - 1) / T + 1) := by
    have hrem := Nat.mod_lt (N - 1) hTpos
    have hid := Nat.mod_add_div (N - 1) T
    nlinarith
  have hdivR : ((N - 1 : ℕ) : ℝ) <
      (T : ℝ) * ((((N - 1) / T : ℕ) : ℝ) + 1) := by
    exact_mod_cast hdiv
  have hpred : ((N - 1 : ℕ) : ℝ) = x ^ 4 - 1 := by
    rw [Nat.cast_sub hNOne, Nat.cast_one, ← hN]
  rw [hpred] at hdivR
  have hupper := mul_le_mul_of_nonneg_right hTupper
    (by positivity : (0 : ℝ) ≤ (((N - 1) / T : ℕ) : ℝ) + 1)
  by_contra h
  have hbad : (5 : ℝ) / 2 * ((((N - 1) / T : ℕ) : ℝ) + 2) < x :=
    lt_of_not_ge h
  have hmul := mul_lt_mul_of_pos_right hbad hx3pos
  nlinarith

theorem weakSidonIntegerScale_quotient_bound {N : ℕ} {x : ℝ}
    (hx : 90 ≤ x) (hN : x ^ 4 = (N : ℝ)) :
    x ≤ (5 : ℝ) / 2 *
      ((((N - 1) / weakSidonIntegerScale x : ℕ) : ℝ) + 2) := by
  have hxpos : 0 < x := by linarith
  exact weakSidonIntegerQuotient_scale_bound hx hN
    (weakSidonIntegerScale_pos hxpos) (weakSidonIntegerScale_upper hx)

theorem weakSidonIntegerScale_quotient_ge {N : ℕ} {x : ℝ}
    (hx : 90 ≤ x) (hN : x ^ 4 = (N : ℝ)) :
    34 ≤ (N - 1) / weakSidonIntegerScale x := by
  have h := weakSidonIntegerScale_quotient_bound hx hN
  have hr : (34 : ℝ) ≤ (((N - 1) / weakSidonIntegerScale x : ℕ) : ℝ) := by
    linarith
  exact_mod_cast hr

def weakSidonTailEnvelope (r : ℕ) : ℝ :=
  (5 : ℝ) / 2 * ((r : ℝ) + 2) * ((3 : ℝ) / 4) ^ r

theorem weakSidonTailEnvelope_succ_le {r : ℕ} (hr : 1 ≤ r) :
    weakSidonTailEnvelope (r + 1) ≤ weakSidonTailEnvelope r := by
  have hrR : (1 : ℝ) ≤ (r : ℝ) := by exact_mod_cast hr
  have hc : (5 : ℝ) / 2 * ((r : ℝ) + 1 + 2) * ((3 : ℝ) / 4) ≤
      (5 : ℝ) / 2 * ((r : ℝ) + 2) := by linarith
  have hp : 0 ≤ ((3 : ℝ) / 4) ^ r := by positivity
  have hm := mul_le_mul_of_nonneg_right hc hp
  simp only [weakSidonTailEnvelope, Nat.cast_add, Nat.cast_one, pow_succ]
  nlinarith

theorem weakSidonTailEnvelope_le_base {r : ℕ} (hr : 34 ≤ r) :
    weakSidonTailEnvelope r ≤ weakSidonTailEnvelope 34 := by
  induction r, hr using Nat.le_induction with
  | base => exact le_rfl
  | succ r hr ih =>
      exact (weakSidonTailEnvelope_succ_le (by omega)).trans ih

theorem weakSidonTailEnvelope_base_lt :
    weakSidonTailEnvelope 34 < (1 : ℝ) / 150 := by
  norm_num [weakSidonTailEnvelope]

theorem weakSidonTailEnvelope_lt {r : ℕ} (hr : 34 ≤ r) :
    weakSidonTailEnvelope r < (1 : ℝ) / 150 :=
  lt_of_le_of_lt (weakSidonTailEnvelope_le_base hr) weakSidonTailEnvelope_base_lt

theorem weakSidonIntegerScale_geometric_tail_lt {N : ℕ} {x : ℝ}
    (hx : 90 ≤ x) (hN : x ^ 4 = (N : ℝ)) :
    x * ((3 : ℝ) / 4) ^ ((N - 1) / weakSidonIntegerScale x) <
      (1 : ℝ) / 150 := by
  have hbound := weakSidonIntegerScale_quotient_bound hx hN
  have hr := weakSidonIntegerScale_quotient_ge hx hN
  calc
    x * ((3 : ℝ) / 4) ^ ((N - 1) / weakSidonIntegerScale x) ≤
        weakSidonTailEnvelope ((N - 1) / weakSidonIntegerScale x) :=
      mul_le_mul_of_nonneg_right hbound (by positivity)
    _ < (1 : ℝ) / 150 := weakSidonTailEnvelope_lt hr

theorem weakSidonIntegerScale_tail_nonneg (N : ℕ) (x : ℝ) :
    0 ≤ 29 * (weakSidonIntegerScale x : ℝ) *
      ((3 : ℝ) / 4) ^ ((N - 1) / weakSidonIntegerScale x) := by
  positivity

theorem weakSidonIntegerScale_tail_lt {N : ℕ} {x : ℝ}
    (hx : 90 ≤ x) (hN : x ^ 4 = (N : ℝ)) :
    29 * (weakSidonIntegerScale x : ℝ) *
        ((3 : ℝ) / 4) ^ ((N - 1) / weakSidonIntegerScale x) <
      (29 : ℝ) / 60 * x ^ 2 := by
  have hxpos : 0 < x := by linarith
  have hx2pos : 0 < x ^ 2 := pow_pos hxpos 2
  have hsmall := weakSidonIntegerScale_geometric_tail_lt hx hN
  have hT := weakSidonIntegerScale_upper hx
  have hp : 0 ≤ ((3 : ℝ) / 4) ^ ((N - 1) / weakSidonIntegerScale x) := by
    positivity
  have hupper := mul_le_mul_of_nonneg_right hT
    (mul_nonneg (by norm_num : (0 : ℝ) ≤ 29) hp)
  have hmul := mul_lt_mul_of_pos_left hsmall
    (by positivity : (0 : ℝ) < ((145 : ℝ) / 2) * x ^ 2)
  nlinarith only [hupper, hmul]

theorem weakSidonIntegerScale_tail_lt_half {N : ℕ} {x : ℝ}
    (hx : 90 ≤ x) (hN : x ^ 4 = (N : ℝ)) :
    29 * (weakSidonIntegerScale x : ℝ) *
        ((3 : ℝ) / 4) ^ ((N - 1) / weakSidonIntegerScale x) < x ^ 2 / 2 := by
  have hxpos : 0 < x := by linarith
  have hx2pos : 0 < x ^ 2 := pow_pos hxpos 2
  calc
    29 * (weakSidonIntegerScale x : ℝ) *
          ((3 : ℝ) / 4) ^ ((N - 1) / weakSidonIntegerScale x) <
        (29 : ℝ) / 60 * x ^ 2 := weakSidonIntegerScale_tail_lt hx hN
    _ < x ^ 2 / 2 := by nlinarith

end Sidon30

end

