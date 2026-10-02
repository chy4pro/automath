import Sidon30.RampWeights

/-! Exact integer scales and a finite geometric tail for the triangle sonar
bound. The horizontal scale is twice the square of the cube-root parameter. -/

noncomputable section

namespace Sidon30

def sonarHorizontalScale (x : ℝ) : ℕ := Nat.ceil (2 * x ^ 2)

def sonarVerticalScale (x : ℝ) : ℕ := Nat.ceil (x ^ 2)

theorem sonarHorizontalScale_lower (x : ℝ) :
    2 * x ^ 2 ≤ (sonarHorizontalScale x : ℝ) := by
  exact Nat.le_ceil _

theorem sonarVerticalScale_lower (x : ℝ) :
    x ^ 2 ≤ (sonarVerticalScale x : ℝ) := by
  exact Nat.le_ceil _

theorem sonarHorizontalScale_upper (x : ℝ) :
    (sonarHorizontalScale x : ℝ) ≤ 2 * x ^ 2 + 1 := by
  exact (Nat.ceil_lt_add_one (by positivity : (0 : ℝ) ≤ 2 * x ^ 2)).le

theorem sonarVerticalScale_upper (x : ℝ) :
    (sonarVerticalScale x : ℝ) ≤ x ^ 2 + 1 := by
  exact (Nat.ceil_lt_add_one (sq_nonneg x)).le

theorem sonarHorizontalScale_pos {x : ℝ} (hx : 0 < x) :
    1 ≤ sonarHorizontalScale x := by
  exact Nat.one_le_ceil_iff.mpr (by positivity)

theorem sonarVerticalScale_pos {x : ℝ} (hx : 0 < x) :
    1 ≤ sonarVerticalScale x := by
  exact Nat.one_le_ceil_iff.mpr (by positivity)

theorem sonarVerticalScale_diagonal_le {x : ℝ} (hx : 0 < x) :
    rampDiagonal (sonarVerticalScale x) ≤ 4 / (3 * x ^ 2) := by
  have hV := sonarVerticalScale_pos hx
  have hVpos : (0 : ℝ) < (sonarVerticalScale x : ℝ) := by
    exact_mod_cast (show 0 < sonarVerticalScale x by omega)
  have hx2pos : 0 < x ^ 2 := pow_pos hx 2
  calc
    rampDiagonal (sonarVerticalScale x) ≤
        4 / (3 * (sonarVerticalScale x : ℝ)) := rampDiagonal_le hV
    _ ≤ 4 / (3 * x ^ 2) := by
      apply (div_le_div_iff₀ (by positivity : 0 < 3 * (sonarVerticalScale x : ℝ))
        (by positivity : 0 < 3 * x ^ 2)).mpr
      have h := sonarVerticalScale_lower x
      nlinarith

theorem sonarVerticalScale_boundary_le {n : ℕ} {x : ℝ}
    (hn : x ^ 3 = (n : ℝ)) :
    (n : ℝ) + (2 : ℝ) / 3 * ((sonarVerticalScale x : ℝ) - 1) ≤
      x ^ 3 + (2 : ℝ) / 3 * x ^ 2 := by
  have h := sonarVerticalScale_upper x
  nlinarith

theorem sonarVerticalScale_quotient_bound {n : ℕ} {x : ℝ}
    (hx : 48 ≤ x) (hn : x ^ 3 = (n : ℝ)) :
    x ≤ (((n - 1) / sonarVerticalScale x : ℕ) : ℝ) + 2 := by
  have hxpos : 0 < x := by linarith
  have hnposR : (0 : ℝ) < (n : ℝ) := by
    rw [← hn]
    exact pow_pos hxpos 3
  have hnpos : 0 < n := by exact_mod_cast hnposR
  have hnOne : 1 ≤ n := by omega
  have hV := sonarVerticalScale_pos hxpos
  have hVpos : 0 < sonarVerticalScale x := by omega
  have hdiv : n - 1 <
      sonarVerticalScale x * ((n - 1) / sonarVerticalScale x + 1) := by
    have hrem := Nat.mod_lt (n - 1) hVpos
    have hid := Nat.mod_add_div (n - 1) (sonarVerticalScale x)
    nlinarith
  have hdivR : ((n - 1 : ℕ) : ℝ) <
      (sonarVerticalScale x : ℝ) *
        ((((n - 1) / sonarVerticalScale x : ℕ) : ℝ) + 1) := by
    exact_mod_cast hdiv
  have hpred : ((n - 1 : ℕ) : ℝ) = x ^ 3 - 1 := by
    rw [Nat.cast_sub hnOne, Nat.cast_one, ← hn]
  rw [hpred] at hdivR
  have hupper := mul_le_mul_of_nonneg_right (sonarVerticalScale_upper x)
    (by positivity :
      (0 : ℝ) ≤ (((n - 1) / sonarVerticalScale x : ℕ) : ℝ) + 1)
  by_contra h
  have hbad : (((n - 1) / sonarVerticalScale x : ℕ) : ℝ) + 1 < x - 1 := by
    have hh := lt_of_not_ge h
    linarith
  have hmul := mul_lt_mul_of_pos_left hbad
    (by positivity : (0 : ℝ) < x ^ 2 + 1)
  have hxx := mul_nonneg hxpos.le (by linarith : 0 ≤ x - 1)
  nlinarith

theorem sonarVerticalScale_quotient_ge {n : ℕ} {x : ℝ}
    (hx : 48 ≤ x) (hn : x ^ 3 = (n : ℝ)) :
    46 ≤ (n - 1) / sonarVerticalScale x := by
  have h := sonarVerticalScale_quotient_bound hx hn
  have hr : (46 : ℝ) ≤ (((n - 1) / sonarVerticalScale x : ℕ) : ℝ) := by
    linarith
  exact_mod_cast hr

def sonarTailEnvelope (r : ℕ) : ℝ :=
  29 * (((r : ℝ) + 2) ^ 2 + 1) * ((3 : ℝ) / 4) ^ r

theorem sonarTailEnvelope_succ_le {r : ℕ} (hr : 5 ≤ r) :
    sonarTailEnvelope (r + 1) ≤ sonarTailEnvelope r := by
  have hrR : (5 : ℝ) ≤ (r : ℝ) := by exact_mod_cast hr
  have hc : 29 * (((r : ℝ) + 1 + 2) ^ 2 + 1) * ((3 : ℝ) / 4) ≤
      29 * (((r : ℝ) + 2) ^ 2 + 1) := by
    nlinarith [sq_nonneg ((r : ℝ) - 5)]
  have hp : 0 ≤ ((3 : ℝ) / 4) ^ r := by positivity
  have hm := mul_le_mul_of_nonneg_right hc hp
  simp only [sonarTailEnvelope, Nat.cast_add, Nat.cast_one, pow_succ]
  nlinarith

theorem sonarTailEnvelope_le_base {r : ℕ} (hr : 46 ≤ r) :
    sonarTailEnvelope r ≤ sonarTailEnvelope 46 := by
  induction r, hr using Nat.le_induction with
  | base => exact le_rfl
  | succ r hr ih =>
      exact (sonarTailEnvelope_succ_le (by omega)).trans ih

theorem sonarTailEnvelope_base_lt : sonarTailEnvelope 46 < 1 := by
  norm_num [sonarTailEnvelope]

theorem sonarTailEnvelope_lt {r : ℕ} (hr : 46 ≤ r) :
    sonarTailEnvelope r < 1 :=
  lt_of_le_of_lt (sonarTailEnvelope_le_base hr) sonarTailEnvelope_base_lt

theorem sonarVerticalScale_tail_nonneg (n : ℕ) (x : ℝ) :
    0 ≤ 29 * (sonarVerticalScale x : ℝ) *
      ((3 : ℝ) / 4) ^ ((n - 1) / sonarVerticalScale x) := by
  positivity

theorem sonarVerticalScale_tail_lt_one {n : ℕ} {x : ℝ}
    (hx : 48 ≤ x) (hn : x ^ 3 = (n : ℝ)) :
    29 * (sonarVerticalScale x : ℝ) *
      ((3 : ℝ) / 4) ^ ((n - 1) / sonarVerticalScale x) < 1 := by
  have hxnonneg : 0 ≤ x := by linarith
  have hbound := sonarVerticalScale_quotient_bound hx hn
  have hsq := mul_le_mul hbound hbound hxnonneg
    (by positivity : (0 : ℝ) ≤ (((n - 1) / sonarVerticalScale x : ℕ) : ℝ) + 2)
  have hV : (sonarVerticalScale x : ℝ) ≤
      ((((n - 1) / sonarVerticalScale x : ℕ) : ℝ) + 2) ^ 2 + 1 := by
    have hv := sonarVerticalScale_upper x
    nlinarith
  have hm := mul_le_mul_of_nonneg_right hV
    (by positivity : (0 : ℝ) ≤ 29 *
      ((3 : ℝ) / 4) ^ ((n - 1) / sonarVerticalScale x))
  have henv := sonarTailEnvelope_lt (sonarVerticalScale_quotient_ge hx hn)
  unfold sonarTailEnvelope at henv
  nlinarith only [hm, henv]

/-- Parameter matching the real powers in the frozen transfer statement. -/
def sonarCubeRoot (n : ℕ) : ℝ := Real.rpow (n : ℝ) ((1 : ℝ) / 3)

theorem sonarCubeRoot_nonneg (n : ℕ) : 0 ≤ sonarCubeRoot n := by
  exact Real.rpow_nonneg (by positivity : (0 : ℝ) ≤ (n : ℝ)) _

theorem sonarCubeRoot_cube (n : ℕ) : sonarCubeRoot n ^ 3 = (n : ℝ) := by
  have h := (Real.rpow_mul (by positivity : (0 : ℝ) ≤ (n : ℝ))
    ((1 : ℝ) / 3) (3 : ℝ)).symm
  norm_num at h
  simpa only [sonarCubeRoot, Real.rpow_eq_pow] using h

theorem sonarCubeRoot_sq (n : ℕ) :
    sonarCubeRoot n ^ 2 = Real.rpow (n : ℝ) ((2 : ℝ) / 3) := by
  have h := (Real.rpow_mul (by positivity : (0 : ℝ) ≤ (n : ℝ))
    ((1 : ℝ) / 3) (2 : ℝ)).symm
  norm_num at h
  simpa only [sonarCubeRoot, Real.rpow_eq_pow] using h

theorem sonarCubeRoot_ge {n : ℕ} (hn : 48 ^ 3 ≤ n) : 48 ≤ sonarCubeRoot n := by
  have hx0 := sonarCubeRoot_nonneg n
  have hx3 := sonarCubeRoot_cube n
  have hnR : (48 : ℝ) ^ 3 ≤ (n : ℝ) := by exact_mod_cast hn
  by_contra h
  have hxlt : sonarCubeRoot n < 48 := lt_of_not_ge h
  have hprod : 0 < (48 - sonarCubeRoot n) *
      ((48 : ℝ) ^ 2 + 48 * sonarCubeRoot n + sonarCubeRoot n ^ 2) := by
    apply mul_pos (sub_pos.mpr hxlt)
    positivity
  nlinarith

end Sidon30

end
