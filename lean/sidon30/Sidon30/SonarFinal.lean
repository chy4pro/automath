import Sidon30.SonarScale

/-!
Final real algebra for the triangle sonar bound. The last theorem explicitly
requires the finite-window sandwich; it does not assume a sonar theorem.
-/

noncomputable section

namespace Sidon30

def sonarRatio (x : ℝ) : ℝ :=
  2 / (3 * x) + 4 / (9 * x ^ 2) + 2 / (3 * x ^ 4)

theorem sonarRatio_nonneg {x : ℝ} (hx : 0 < x) : 0 ≤ sonarRatio x := by
  unfold sonarRatio
  positivity

theorem sonarRatio_lt_half {x : ℝ} (hx : 48 ≤ x) : sonarRatio x < 1 / 2 := by
  have hxpos : 0 < x := by linarith
  have hxone : 1 ≤ x := by linarith
  have hx2one : 1 ≤ x ^ 2 := one_le_pow₀ hxone
  have hx2large : (48 : ℝ) ≤ x ^ 2 := by
    have hm := mul_le_mul_of_nonneg_left hxone hxpos.le
    nlinarith
  have hx4large : (48 : ℝ) ≤ x ^ 4 := by
    have hm := mul_le_mul_of_nonneg_left hx2one (sq_nonneg x)
    nlinarith
  have h1 : 2 / (3 * x) < (1 : ℝ) / 6 := by
    apply (div_lt_iff₀ (by positivity : (0 : ℝ) < 3 * x)).mpr
    linarith
  have h2 : 4 / (9 * x ^ 2) < (1 : ℝ) / 6 := by
    apply (div_lt_iff₀ (by positivity : (0 : ℝ) < 9 * x ^ 2)).mpr
    linarith
  have h3 : 2 / (3 * x ^ 4) < (1 : ℝ) / 6 := by
    apply (div_lt_iff₀ (by positivity : (0 : ℝ) < 3 * x ^ 4)).mpr
    linarith
  unfold sonarRatio
  linarith

theorem sonarRatio_mul_scale {x : ℝ} (hx : x ≠ 0) :
    sonarRatio x * (2 * x ^ 2) =
      (x ^ 3 + (2 : ℝ) / 3 * x ^ 2 + 1) * (4 / (3 * x ^ 2)) := by
  unfold sonarRatio
  field_simp [hx]
  <;> ring

theorem sonarRatio_margin_identity {x : ℝ} (hx : x ≠ 0) :
    (x ^ 3 + 2 * x ^ 2 + 3 * x) * (1 - sonarRatio x) -
        (x ^ 3 + (4 : ℝ) / 3 * x ^ 2 + (4 : ℝ) / 3) =
      (11 : ℝ) / 9 * x - (38 : ℝ) / 9 -
        2 / x - 4 / (3 * x ^ 2) - 2 / x ^ 3 := by
  unfold sonarRatio
  field_simp [hx]
  <;> ring

theorem sonarRatio_margin_pos {x : ℝ} (hx : 48 ≤ x) :
    x ^ 3 + (4 : ℝ) / 3 * x ^ 2 + (4 : ℝ) / 3 <
      (x ^ 3 + 2 * x ^ 2 + 3 * x) * (1 - sonarRatio x) := by
  have hxpos : 0 < x := by linarith
  have hxone : 1 ≤ x := by linarith
  have hx2one : 1 ≤ x ^ 2 := one_le_pow₀ hxone
  have hx3one : 1 ≤ x ^ 3 := one_le_pow₀ hxone
  have h1 : 2 / x ≤ (2 : ℝ) := by
    apply (div_le_iff₀ hxpos).mpr
    linarith
  have h2 : 4 / (3 * x ^ 2) ≤ (4 : ℝ) / 3 := by
    apply (div_le_iff₀ (by positivity : (0 : ℝ) < 3 * x ^ 2)).mpr
    linarith
  have h3 : 2 / x ^ 3 ≤ (2 : ℝ) := by
    apply (div_le_iff₀ (by positivity : (0 : ℝ) < x ^ 3)).mpr
    linarith
  have hid := sonarRatio_margin_identity (ne_of_gt hxpos)
  linarith

/-- Pure real algebra after the exact finite-window sandwich. -/
theorem sonar_of_scaled_sandwich {x m U a C : ℝ}
    (hx : 48 ≤ x) (hm : 0 ≤ m)
    (hUlower : 2 * x ^ 2 ≤ U) (hUupper : U ≤ 2 * x ^ 2 + 1)
    (hanonneg : 0 ≤ a) (haupper : a ≤ 4 / (3 * x ^ 2))
    (hCnonneg : 0 ≤ C) (hCupper : C ≤ x ^ 3 + (2 : ℝ) / 3 * x ^ 2 + 1)
    (hsandwich : m * U - (U ^ 2 - 1) / 3 ≤ C * (m * a + U - 1)) :
    m ≤ x ^ 3 + 2 * x ^ 2 + 3 * x := by
  have hxpos : 0 < x := by linarith
  have hx2pos : 0 < x ^ 2 := pow_pos hxpos 2
  have hUpos : 0 < U := by linarith
  have hqnonneg := sonarRatio_nonneg hxpos
  have hqsmall := sonarRatio_lt_half hx
  have hdenpos : 0 < 1 - sonarRatio x := by linarith
  have hC0nonneg : 0 ≤ x ^ 3 + (2 : ℝ) / 3 * x ^ 2 + 1 := by positivity
  have hratio : C * a ≤ sonarRatio x * U := by
    calc
      C * a ≤ (x ^ 3 + (2 : ℝ) / 3 * x ^ 2 + 1) * (4 / (3 * x ^ 2)) :=
        mul_le_mul hCupper haupper hanonneg hC0nonneg
      _ = sonarRatio x * (2 * x ^ 2) :=
        (sonarRatio_mul_scale (ne_of_gt hxpos)).symm
      _ ≤ sonarRatio x * U := mul_le_mul_of_nonneg_left hUlower hqnonneg
  have hraw : m * (U - C * a) ≤ U * (U / 3 + C) := by
    nlinarith
  have hbase : U / 3 + C ≤ x ^ 3 + (4 : ℝ) / 3 * x ^ 2 + (4 : ℝ) / 3 := by
    linarith
  have hmratio := mul_le_mul_of_nonneg_left hratio hm
  have hUbase := mul_le_mul_of_nonneg_left hbase hUpos.le
  have hscaled :
      m * (1 - sonarRatio x) ≤ x ^ 3 + (4 : ℝ) / 3 * x ^ 2 + (4 : ℝ) / 3 := by
    apply (mul_le_mul_right hUpos).mp
    nlinarith only [hraw, hmratio, hUbase]
  have hcomparison :
      m * (1 - sonarRatio x) <
        (x ^ 3 + 2 * x ^ 2 + 3 * x) * (1 - sonarRatio x) :=
    hscaled.trans_lt (sonarRatio_margin_pos hx)
  exact ((mul_lt_mul_right hdenpos).mp hcomparison).le

/-- The finite cost and diagonal supplied by the existing ramp certificate
give the target polynomial as soon as the stated window sandwich is proved. -/
theorem sonar_of_finite_sandwich {n : ℕ} {x m : ℝ}
    (hx : 48 ≤ x) (hn : x ^ 3 = (n : ℝ)) (hm : 0 ≤ m)
    (hsandwich :
      m * (sonarHorizontalScale x : ℝ) -
          ((sonarHorizontalScale x : ℝ) ^ 2 - 1) / 3 ≤
        ((n : ℝ) + (2 : ℝ) / 3 * ((sonarVerticalScale x : ℝ) - 1) +
          29 * (sonarVerticalScale x : ℝ) *
            ((3 : ℝ) / 4) ^ ((n - 1) / sonarVerticalScale x)) *
          (m * rampDiagonal (sonarVerticalScale x) +
            (sonarHorizontalScale x : ℝ) - 1)) :
    m ≤ x ^ 3 + 2 * x ^ 2 + 3 * x := by
  have hxpos : 0 < x := by linarith
  have hV := sonarVerticalScale_pos hxpos
  have hVreal : (1 : ℝ) ≤ (sonarVerticalScale x : ℝ) := by exact_mod_cast hV
  have htailnonneg := sonarVerticalScale_tail_nonneg n x
  have htail := sonarVerticalScale_tail_lt_one hx hn
  have hboundary := sonarVerticalScale_boundary_le hn
  have hCnonneg :
      0 ≤ (n : ℝ) + (2 : ℝ) / 3 * ((sonarVerticalScale x : ℝ) - 1) +
        29 * (sonarVerticalScale x : ℝ) *
          ((3 : ℝ) / 4) ^ ((n - 1) / sonarVerticalScale x) := by
    have hb := mul_nonneg (by norm_num : (0 : ℝ) ≤ 2 / 3)
      (sub_nonneg.mpr hVreal)
    have hnnonneg : (0 : ℝ) ≤ (n : ℝ) := by positivity
    linarith
  have hCupper :
      (n : ℝ) + (2 : ℝ) / 3 * ((sonarVerticalScale x : ℝ) - 1) +
        29 * (sonarVerticalScale x : ℝ) *
          ((3 : ℝ) / 4) ^ ((n - 1) / sonarVerticalScale x) ≤
        x ^ 3 + (2 : ℝ) / 3 * x ^ 2 + 1 := by
    linarith
  exact sonar_of_scaled_sandwich hx hm (sonarHorizontalScale_lower x)
    (sonarHorizontalScale_upper x) (rampDiagonal_nonneg _)
    (sonarVerticalScale_diagonal_le hxpos) hCnonneg hCupper hsandwich

end Sidon30

end

