import Sidon30.RampWeights

/-!
The exact integer scale and a rational geometric tail estimate.
All division defining the block number is natural division. No logarithm,
real floor, asymptotic estimate, or numerical approximation is used.
-/

noncomputable section

namespace Sidon30

/-- The second-order coefficient in the target theorem. -/
def sidonGamma : ℝ := 2 * Real.sqrt 2 / 3

/-- Integer scale chosen by rounding the optimal real scale upward. -/
def sidonIntegerScale (x : ℝ) : ℕ := Nat.ceil (Real.sqrt 2 * x ^ 3)

theorem sidonGamma_pos : 0 < sidonGamma := by
  unfold sidonGamma
  positivity

theorem sidonGamma_sq : sidonGamma ^ 2 = (8 : ℝ) / 9 := by
  have hs : (Real.sqrt 2) ^ 2 = (2 : ℝ) := Real.sq_sqrt (by norm_num)
  unfold sidonGamma
  nlinarith

theorem sidonGamma_lt_one : sidonGamma < 1 := by
  have hs := sidonGamma_sq
  have hp := sidonGamma_pos
  nlinarith

theorem sidonIntegerScale_lower (x : ℝ) :
    Real.sqrt 2 * x ^ 3 ≤ (sidonIntegerScale x : ℝ) := by
  exact Nat.le_ceil _

theorem sidonIntegerScale_lt {x : ℝ} (hx : 0 ≤ x) :
    (sidonIntegerScale x : ℝ) < Real.sqrt 2 * x ^ 3 + 1 := by
  exact Nat.ceil_lt_add_one (mul_nonneg (Real.sqrt_nonneg 2) (pow_nonneg hx 3))

theorem sidonIntegerScale_pos {x : ℝ} (hx : 0 < x) :
    1 ≤ sidonIntegerScale x := by
  have hscale : 0 < Real.sqrt 2 * x ^ 3 := by positivity
  exact Nat.one_le_ceil_iff.mpr hscale

theorem sidonIntegerScale_sub_one_le {x : ℝ} (hx : 0 ≤ x) :
    (sidonIntegerScale x : ℝ) - 1 ≤ Real.sqrt 2 * x ^ 3 := by
  have h := sidonIntegerScale_lt hx
  linarith

/-- The rounding error fits inside the gap between sqrt(2) and 3/2. -/
theorem sidonIntegerScale_upper {x : ℝ} (hx : 120 ≤ x) :
    (sidonIntegerScale x : ℝ) ≤ (3 : ℝ) / 2 * x ^ 3 := by
  have hxpos : 0 < x := by linarith
  have hxone : 1 ≤ x := by linarith
  have hx2one : 1 ≤ x ^ 2 := one_le_pow₀ hxone
  have hx3large : (12 : ℝ) ≤ x ^ 3 := by
    have h := mul_le_mul_of_nonneg_left hx2one hxpos.le
    nlinarith
  have hs : Real.sqrt 2 ≤ (17 : ℝ) / 12 := by
    apply (Real.sqrt_le_left (by norm_num : (0 : ℝ) ≤ 17 / 12)).mpr
    norm_num
  have hmul := mul_le_mul_of_nonneg_right hs (pow_nonneg hxpos.le 3)
  have hceil := sidonIntegerScale_lt hxpos.le
  linarith

/-- The diagonal bound at this integer scale has exactly the target coefficient. -/
theorem sidonIntegerScale_diagonal_le {x : ℝ} (hx : 0 < x) :
    rampDiagonal (sidonIntegerScale x) ≤ sidonGamma / x ^ 3 := by
  have hT := sidonIntegerScale_pos hx
  have hTpos : (0 : ℝ) < (sidonIntegerScale x : ℝ) := by
    exact_mod_cast (show 0 < sidonIntegerScale x by omega)
  have hx3pos : 0 < x ^ 3 := pow_pos hx 3
  have hs : (Real.sqrt 2) ^ 2 = (2 : ℝ) := Real.sq_sqrt (by norm_num)
  have hprod : 4 * x ^ 3 ≤ 2 * Real.sqrt 2 * (sidonIntegerScale x : ℝ) := by
    calc
      4 * x ^ 3 = (2 * Real.sqrt 2) * (Real.sqrt 2 * x ^ 3) := by
        calc
          _ = 2 * (Real.sqrt 2) ^ 2 * x ^ 3 := by rw [hs]; ring
          _ = _ := by ring
      _ ≤ (2 * Real.sqrt 2) * (sidonIntegerScale x : ℝ) :=
        mul_le_mul_of_nonneg_left (sidonIntegerScale_lower x) (by positivity)
  calc
    rampDiagonal (sidonIntegerScale x) ≤ 4 / (3 * (sidonIntegerScale x : ℝ)) :=
      rampDiagonal_le hT
    _ ≤ sidonGamma / x ^ 3 := by
      apply (div_le_div_iff₀ (by positivity : 0 < 3 * (sidonIntegerScale x : ℝ))
        hx3pos).mpr
      unfold sidonGamma
      nlinarith [hprod]

/-- Keeping `T - 1` avoids an extra rounding loss in the boundary mass. -/
theorem sidonIntegerScale_boundary_le {N : ℕ} {x : ℝ}
    (hx : 0 ≤ x) (hN : x ^ 4 = (N : ℝ)) :
    (N : ℝ) + (2 : ℝ) / 3 * ((sidonIntegerScale x : ℝ) - 1) ≤
      x ^ 4 + sidonGamma * x ^ 3 := by
  have h := sidonIntegerScale_sub_one_le hx
  unfold sidonGamma
  nlinarith

/-- A natural quotient bound, stated independently of how the scale was chosen. -/
theorem integerQuotient_scale_bound {N T : ℕ} {x : ℝ}
    (hx : 120 ≤ x) (hN : x ^ 4 = (N : ℝ)) (hT : 1 ≤ T)
    (hTupper : (T : ℝ) ≤ 2 * x ^ 3) :
    x ≤ 2 * ((((N - 1) / T : ℕ) : ℝ) + 2) := by
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
  have hbad : 2 * ((((N - 1) / T : ℕ) : ℝ) + 2) < x := lt_of_not_ge h
  have hmul := mul_lt_mul_of_pos_right hbad hx3pos
  nlinarith

theorem sidonIntegerScale_quotient_bound {N : ℕ} {x : ℝ}
    (hx : 120 ≤ x) (hN : x ^ 4 = (N : ℝ)) :
    x ≤ 2 * ((((N - 1) / sidonIntegerScale x : ℕ) : ℝ) + 2) := by
  have hxpos : 0 < x := by linarith
  apply integerQuotient_scale_bound hx hN (sidonIntegerScale_pos hxpos)
  have h := sidonIntegerScale_upper hx
  have hx3 := pow_nonneg hxpos.le 3
  linarith

theorem sidonIntegerScale_quotient_ge {N : ℕ} {x : ℝ}
    (hx : 120 ≤ x) (hN : x ^ 4 = (N : ℝ)) :
    58 ≤ (N - 1) / sidonIntegerScale x := by
  have h := sidonIntegerScale_quotient_bound hx hN
  have hr : (58 : ℝ) ≤ (((N - 1) / sidonIntegerScale x : ℕ) : ℝ) := by
    linarith
  exact_mod_cast hr

/-- The geometric envelope used to absorb the finite boundary error. -/
def sidonTailEnvelope (r : ℕ) : ℝ :=
  2 * ((r : ℝ) + 2) * ((3 : ℝ) / 4) ^ r

theorem sidonTailEnvelope_succ_le {r : ℕ} (hr : 1 ≤ r) :
    sidonTailEnvelope (r + 1) ≤ sidonTailEnvelope r := by
  have hrR : (1 : ℝ) ≤ (r : ℝ) := by exact_mod_cast hr
  have hc : 2 * ((r : ℝ) + 1 + 2) * ((3 : ℝ) / 4) ≤
      2 * ((r : ℝ) + 2) := by linarith
  have hp : 0 ≤ ((3 : ℝ) / 4) ^ r := by positivity
  have hm := mul_le_mul_of_nonneg_right hc hp
  simp only [sidonTailEnvelope, Nat.cast_add, Nat.cast_one, pow_succ]
  nlinarith

theorem sidonTailEnvelope_le_base {r : ℕ} (hr : 58 ≤ r) :
    sidonTailEnvelope r ≤ sidonTailEnvelope 58 := by
  induction r, hr using Nat.le_induction with
  | base => exact le_rfl
  | succ r hr ih =>
      exact (sidonTailEnvelope_succ_le (by omega)).trans ih

/-- The only large numerical endpoint is checked by exact rational arithmetic. -/
theorem sidonTailEnvelope_base_lt : sidonTailEnvelope 58 < (1 : ℝ) / 100 := by
  norm_num [sidonTailEnvelope]

theorem sidonTailEnvelope_lt {r : ℕ} (hr : 58 ≤ r) :
    sidonTailEnvelope r < (1 : ℝ) / 100 :=
  lt_of_le_of_lt (sidonTailEnvelope_le_base hr) sidonTailEnvelope_base_lt

theorem sidonIntegerScale_geometric_tail_lt {N : ℕ} {x : ℝ}
    (hx : 120 ≤ x) (hN : x ^ 4 = (N : ℝ)) :
    x * ((3 : ℝ) / 4) ^ ((N - 1) / sidonIntegerScale x) < (1 : ℝ) / 100 := by
  have hbound := sidonIntegerScale_quotient_bound hx hN
  have hr := sidonIntegerScale_quotient_ge hx hN
  calc
    x * ((3 : ℝ) / 4) ^ ((N - 1) / sidonIntegerScale x) ≤
        sidonTailEnvelope ((N - 1) / sidonIntegerScale x) :=
      mul_le_mul_of_nonneg_right hbound (by positivity)
    _ < (1 : ℝ) / 100 := sidonTailEnvelope_lt hr

theorem sidonIntegerScale_tail_nonneg (N : ℕ) (x : ℝ) :
    0 ≤ 29 * (sidonIntegerScale x : ℝ) *
      ((3 : ℝ) / 4) ^ ((N - 1) / sidonIntegerScale x) := by
  positivity

/-- Explicit error constant before the simpler `x²/2` comparison. -/
theorem sidonIntegerScale_tail_lt {N : ℕ} {x : ℝ}
    (hx : 120 ≤ x) (hN : x ^ 4 = (N : ℝ)) :
    29 * (sidonIntegerScale x : ℝ) *
        ((3 : ℝ) / 4) ^ ((N - 1) / sidonIntegerScale x) <
      (87 : ℝ) / 200 * x ^ 2 := by
  have hxpos : 0 < x := by linarith
  have hx2pos : 0 < x ^ 2 := pow_pos hxpos 2
  have hsmall := sidonIntegerScale_geometric_tail_lt hx hN
  have hT := sidonIntegerScale_upper hx
  have hp : 0 ≤ ((3 : ℝ) / 4) ^ ((N - 1) / sidonIntegerScale x) := by positivity
  have hupper := mul_le_mul_of_nonneg_right hT
    (mul_nonneg (by norm_num : (0 : ℝ) ≤ 29) hp)
  have hmul := mul_lt_mul_of_pos_left hsmall
    (by positivity : (0 : ℝ) < ((87 : ℝ) / 2) * x ^ 2)
  nlinarith only [hupper, hmul]

theorem sidonIntegerScale_tail_lt_half {N : ℕ} {x : ℝ}
    (hx : 120 ≤ x) (hN : x ^ 4 = (N : ℝ)) :
    29 * (sidonIntegerScale x : ℝ) *
        ((3 : ℝ) / 4) ^ ((N - 1) / sidonIntegerScale x) < x ^ 2 / 2 := by
  have hxpos : 0 < x := by linarith
  have hx2pos : 0 < x ^ 2 := pow_pos hxpos 2
  calc
    29 * (sidonIntegerScale x : ℝ) *
          ((3 : ℝ) / 4) ^ ((N - 1) / sidonIntegerScale x) <
        (87 : ℝ) / 200 * x ^ 2 := sidonIntegerScale_tail_lt hx hN
    _ < x ^ 2 / 2 := by nlinarith

end Sidon30

end
