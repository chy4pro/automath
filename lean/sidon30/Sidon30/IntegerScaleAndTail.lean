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

/-- Route B's sharper quotient estimate, including both rounding operations. -/
theorem sidonIntegerScale_quotient_bound_sharp {N : ℕ} {x : ℝ}
    (hx : 1 < x) (hN : x ^ 4 = (N : ℝ)) :
    x < Real.sqrt 2 * ((((N - 1) / sidonIntegerScale x : ℕ) : ℝ) + 2) := by
  have hxpos : 0 < x := by linarith
  have hspos : 0 < Real.sqrt 2 := by positivity
  have hs : (Real.sqrt 2) ^ 2 = (2 : ℝ) := Real.sq_sqrt (by norm_num)
  have hx2 : 1 ≤ x ^ 2 := one_le_pow₀ hx.le
  have hx3 : x ≤ x ^ 3 := by
    have hm := mul_le_mul_of_nonneg_left hx2 hxpos.le
    nlinarith only [hm]
  have hNposR : (0 : ℝ) < (N : ℝ) := by rw [← hN]; positivity
  have hNOne : 1 ≤ N := by
    have : 0 < N := by exact_mod_cast hNposR
    omega
  let T := sidonIntegerScale x
  let r := (N - 1) / T
  have hT : 1 ≤ T := sidonIntegerScale_pos hxpos
  have hdiv : N - 1 < T * (r + 1) := by
    have hrem := Nat.mod_lt (N - 1) (show 0 < T by omega)
    have hid := Nat.mod_add_div (N - 1) T
    dsimp [r]
    nlinarith
  have hdivR : ((N - 1 : ℕ) : ℝ) < (T : ℝ) * ((r : ℝ) + 1) := by
    exact_mod_cast hdiv
  rw [Nat.cast_sub hNOne, Nat.cast_one, ← hN] at hdivR
  have hupper := mul_le_mul_of_nonneg_right (sidonIntegerScale_lt hxpos.le).le
    (show (0 : ℝ) ≤ (r : ℝ) + 1 by positivity)
  have hscaled : Real.sqrt 2 * (x ^ 4 - 1) <
      (Real.sqrt 2 * x ^ 3 + 1) * (Real.sqrt 2 * ((r : ℝ) + 1)) := by
    have hm := mul_lt_mul_of_pos_left (hdivR.trans_le hupper) hspos
    nlinarith only [hm]
  have hsx : (Real.sqrt 2) ^ 2 * x ^ 3 = 2 * x ^ 3 := by rw [hs]
  have hcompare : (Real.sqrt 2 * x ^ 3 + 1) * (x - Real.sqrt 2) <
      Real.sqrt 2 * (x ^ 4 - 1) := by
    nlinarith only [hsx, hx3, hxpos]
  change x < Real.sqrt 2 * ((r : ℝ) + 2)
  by_contra h
  have hbad : Real.sqrt 2 * ((r : ℝ) + 1) ≤ x - Real.sqrt 2 := by
    have := le_of_not_gt h
    linarith
  have hm := mul_le_mul_of_nonneg_left hbad
    (show 0 ≤ Real.sqrt 2 * x ^ 3 + 1 by positivity)
  linarith

/-- The rational onset gives at least 32 complete blocks. -/
theorem sidonIntegerScale_quotient_ge_thirtytwo {N : ℕ} {x : ℝ}
    (hx : (463 : ℝ) / 10 ≤ x) (hN : x ^ 4 = (N : ℝ)) :
    32 ≤ (N - 1) / sidonIntegerScale x := by
  have hxpos : 0 < x := by linarith
  have hsnonneg := Real.sqrt_nonneg (2 : ℝ)
  have hs : (Real.sqrt 2) ^ 2 = (2 : ℝ) := Real.sq_sqrt (by norm_num)
  have hsupper : Real.sqrt 2 < (99 : ℝ) / 70 := by nlinarith
  have hgap : 1 < x - 32 * Real.sqrt 2 := by linarith
  have hx2 : 1 ≤ x ^ 2 := one_le_pow₀ (show 1 ≤ x by linarith)
  have hx3large : (33 : ℝ) < x ^ 3 := by
    have hm := mul_le_mul_of_nonneg_left hx2 hxpos.le
    nlinarith only [hm, hx]
  have hmul := mul_lt_mul_of_pos_left hgap (pow_pos hxpos 3)
  have hceil := sidonIntegerScale_lt hxpos.le
  have h32R : 32 * (sidonIntegerScale x : ℝ) < x ^ 4 - 1 := by
    nlinarith only [hmul, hx3large, hceil]
  have hNposR : (0 : ℝ) < (N : ℝ) := by rw [← hN]; positivity
  have hNpos : 0 < N := by exact_mod_cast hNposR
  have hpred : ((N - 1 : ℕ) : ℝ) = x ^ 4 - 1 := by
    rw [Nat.cast_sub (show 1 ≤ N by omega), Nat.cast_one, ← hN]
  rw [← hpred] at h32R
  have h32 : 32 * sidonIntegerScale x ≤ N - 1 := by exact_mod_cast h32R.le
  have hT := sidonIntegerScale_pos hxpos
  have hdiv : N - 1 < sidonIntegerScale x * ((N - 1) / sidonIntegerScale x + 1) := by
    have hrem := Nat.mod_lt (N - 1) (show 0 < sidonIntegerScale x by omega)
    have hid := Nat.mod_add_div (N - 1) (sidonIntegerScale x)
    nlinarith
  by_contra h
  have hr : (N - 1) / sidonIntegerScale x + 1 ≤ 32 := by omega
  have hm := Nat.mul_le_mul_left (sidonIntegerScale x) hr
  nlinarith only [h32, hdiv, hm]

/-- The sharper envelope retains the exact ceiling error. -/
def sidonTailEnvelopeSharp (r : ℕ) : ℝ :=
  (2 * (r : ℝ) + 5) * ((3 : ℝ) / 4) ^ r

theorem sidonTailEnvelopeSharp_succ_le {r : ℕ} (hr : 32 ≤ r) :
    sidonTailEnvelopeSharp (r + 1) ≤ sidonTailEnvelopeSharp r := by
  have hrR : (32 : ℝ) ≤ (r : ℝ) := by exact_mod_cast hr
  have hc : (2 * ((r : ℝ) + 1) + 5) * ((3 : ℝ) / 4) ≤
      2 * (r : ℝ) + 5 := by linarith
  have hm := mul_le_mul_of_nonneg_right hc
    (show 0 ≤ ((3 : ℝ) / 4) ^ r by positivity)
  simp only [sidonTailEnvelopeSharp, Nat.cast_add, Nat.cast_one, pow_succ]
  nlinarith only [hm]

theorem sidonTailEnvelopeSharp_le_base {r : ℕ} (hr : 32 ≤ r) :
    sidonTailEnvelopeSharp r ≤ sidonTailEnvelopeSharp 32 := by
  induction r, hr using Nat.le_induction with
  | base => exact le_rfl
  | succ r hr ih => exact (sidonTailEnvelopeSharp_succ_le hr).trans ih

/-- Exact integer comparison: 9900 * 3^32 < 4^32. -/
theorem sidonTail_power_thirtytwo_lt : ((3 : ℝ) / 4) ^ 32 < (1 : ℝ) / 9900 := by
  norm_num

/-- The Route B envelope, uniformly in the natural block number. -/
theorem sidonTailEnvelopeSharp_lt {r : ℕ} (hr : 32 ≤ r) :
    29 * sidonTailEnvelopeSharp r < (667 : ℝ) / 3300 := by
  have hbase := sidonTailEnvelopeSharp_le_base hr
  have hpower := sidonTail_power_thirtytwo_lt
  norm_num only [sidonTailEnvelopeSharp, Nat.cast_ofNat] at hbase
  nlinarith only [hbase, hpower]

/-- CR-9's exact normalized tail constant, at the rational fourth-root onset. -/
theorem sidonIntegerScale_tail_lt_sharp {N : ℕ} {x : ℝ}
    (hx : (463 : ℝ) / 10 ≤ x) (hN : x ^ 4 = (N : ℝ)) :
    29 * (sidonIntegerScale x : ℝ) *
        ((3 : ℝ) / 4) ^ ((N - 1) / sidonIntegerScale x) <
      (667 : ℝ) / 3300 * x ^ 2 := by
  have hxone : 1 < x := by linarith
  have hxpos : 0 < x := by linarith
  have hx2pos : 0 < x ^ 2 := pow_pos hxpos 2
  have hx2one : 1 < x ^ 2 := by nlinarith
  let r := (N - 1) / sidonIntegerScale x
  have hbound := sidonIntegerScale_quotient_bound_sharp hxone hN
  have hr := sidonIntegerScale_quotient_ge_thirtytwo hx hN
  have hs : (Real.sqrt 2) ^ 2 = (2 : ℝ) := Real.sq_sqrt (by norm_num)
  have hsbound : Real.sqrt 2 * x < 2 * (r : ℝ) + 4 := by
    have hm := mul_lt_mul_of_pos_left hbound (show 0 < Real.sqrt 2 by positivity)
    have hid : Real.sqrt 2 * (Real.sqrt 2 * ((r : ℝ) + 2)) =
        2 * (r : ℝ) + 4 := by
      calc
        _ = (Real.sqrt 2) ^ 2 * ((r : ℝ) + 2) := by ring
        _ = _ := by rw [hs]; ring
    change Real.sqrt 2 * x < Real.sqrt 2 * (Real.sqrt 2 * ((r : ℝ) + 2)) at hm
    rw [hid] at hm
    exact hm
  have hTbound : (sidonIntegerScale x : ℝ) < (2 * (r : ℝ) + 5) * x ^ 2 := by
    have hm := mul_lt_mul_of_pos_right hsbound hx2pos
    have hceil := sidonIntegerScale_lt hxpos.le
    nlinarith only [hm, hceil, hx2one]
  have htail := mul_lt_mul_of_pos_right hTbound
    (show 0 < 29 * ((3 : ℝ) / 4) ^ r by positivity)
  have henv := mul_lt_mul_of_pos_right (sidonTailEnvelopeSharp_lt hr) hx2pos
  change 29 * (sidonIntegerScale x : ℝ) * ((3 : ℝ) / 4) ^ r < _
  change 29 * ((2 * (r : ℝ) + 5) * ((3 : ℝ) / 4) ^ r) * x ^ 2 < _ at henv
  nlinarith only [htail, henv]

theorem sidonIntegerScale_tail_lt_half_sharp {N : ℕ} {x : ℝ}
    (hx : (463 : ℝ) / 10 ≤ x) (hN : x ^ 4 = (N : ℝ)) :
    29 * (sidonIntegerScale x : ℝ) *
        ((3 : ℝ) / 4) ^ ((N - 1) / sidonIntegerScale x) < x ^ 2 / 2 := by
  have htail := sidonIntegerScale_tail_lt_sharp hx hN
  have hx2pos : 0 < x ^ 2 := pow_pos (by linarith) 2
  nlinarith only [htail, hx2pos]

end Sidon30

end
