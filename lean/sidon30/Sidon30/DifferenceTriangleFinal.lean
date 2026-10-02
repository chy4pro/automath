import Sidon30.IntegerScaleAndTail

/-!
Strict scalar comparison and inversion for difference triangle sets.
These real lemmas are independent of the within-row combinatorial certificate.
-/

noncomputable section

namespace Sidon30

theorem dts_quadratic_comparison {K y C b : ℝ}
    (hC : 0 < C) (hy : 0 < y)
    (hgap : C * (1 + b * y) < y ^ 2)
    (hK : K ^ 2 ≤ C * (1 + b * K)) : K < y := by
  have hyb : b * C < y := by
    by_contra h
    have hle : y ≤ b * C := le_of_not_gt h
    have hmul := mul_le_mul_of_nonneg_right hle hy.le
    nlinarith
  by_contra h
  have hyK : y ≤ K := le_of_not_gt h
  have hprod : 0 ≤ (K - y) * (K + y - b * C) := by
    apply mul_nonneg (sub_nonneg.mpr hyK)
    linarith
  nlinarith

theorem dts_margin_identity {x γ : ℝ} (hx : x ≠ 0)
    (hγ : γ ^ 2 = (8 : ℝ) / 9) :
    (x ^ 2 + γ * x + 1) ^ 2 -
        (x ^ 4 + γ * x ^ 3) * (1 + (γ / x ^ 3) * (x ^ 2 + γ * x + 1)) =
      (10 : ℝ) / 9 * x ^ 2 + (γ / 9) * x + (1 : ℝ) / 9 := by
  have hcube : γ ^ 3 = ((8 : ℝ) / 9) * γ := by
    calc
      γ ^ 3 = γ ^ 2 * γ := by ring
      _ = ((8 : ℝ) / 9) * γ := by rw [hγ]
  have hraw :
      (x ^ 2 + γ * x + 1) ^ 2 -
          (x ^ 4 + γ * x ^ 3) * (1 + (γ / x ^ 3) * (x ^ 2 + γ * x + 1)) =
        (2 - γ ^ 2) * x ^ 2 + (γ - γ ^ 3) * x + 1 - γ ^ 2 := by
    field_simp [hx]
    <;> ring
  rw [hraw, hγ, hcube]
  ring

theorem dts_of_scaled_certificate {x γ K η : ℝ}
    (hx : 120 ≤ x) (hγpos : 0 < γ) (hγlt : γ < 1)
    (hγsq : γ ^ 2 = (8 : ℝ) / 9)
    (hηnonneg : 0 ≤ η) (hη : η < x ^ 2 / 2)
    (hK : K ^ 2 ≤ (x ^ 4 + γ * x ^ 3 + η) * (1 + (γ / x ^ 3) * K)) :
    K < x ^ 2 + γ * x + 1 := by
  have hxpos : 0 < x := by linarith
  have hxne : x ≠ 0 := ne_of_gt hxpos
  have hx2 : 0 < x ^ 2 := pow_pos hxpos 2
  have hx3 : 0 < x ^ 3 := pow_pos hxpos 3
  have hx4 : 0 < x ^ 4 := pow_pos hxpos 4
  have hxone : 1 ≤ x := by linarith
  have hx2one : 1 ≤ x ^ 2 := one_le_pow₀ hxone
  have hx3large : (120 : ℝ) ≤ x ^ 3 := by
    have hm := mul_le_mul_of_nonneg_left hx2one hxpos.le
    nlinarith
  have hC : 0 < x ^ 4 + γ * x ^ 3 + η := by
    have := mul_pos hγpos hx3
    linarith
  have hy : 0 < x ^ 2 + γ * x + 1 := by
    have := mul_pos hγpos hxpos
    linarith
  have hfrac1 : γ / x < (1 : ℝ) / 3 := by
    apply (div_lt_iff₀ hxpos).mpr
    linarith
  have hfrac2 : γ ^ 2 / x ^ 2 < (1 : ℝ) / 3 := by
    apply (div_lt_iff₀ hx2).mpr
    nlinarith [sq_nonneg (x - 120)]
  have hfrac3 : γ / x ^ 3 < (1 : ℝ) / 3 := by
    apply (div_lt_iff₀ hx3).mpr
    linarith
  have hfactor_eq :
      1 + (γ / x ^ 3) * (x ^ 2 + γ * x + 1) =
        1 + γ / x + γ ^ 2 / x ^ 2 + γ / x ^ 3 := by
    field_simp [hxne]
    <;> ring
  have hfactor_lt : 1 + (γ / x ^ 3) * (x ^ 2 + γ * x + 1) < 2 := by
    rw [hfactor_eq]
    linarith
  have herror : η * (1 + (γ / x ^ 3) * (x ^ 2 + γ * x + 1)) < x ^ 2 := by
    have hmul := mul_le_mul_of_nonneg_left hfactor_lt.le hηnonneg
    nlinarith
  have hmargin := dts_margin_identity hxne hγsq
  have hgap :
      (x ^ 4 + γ * x ^ 3 + η) * (1 + (γ / x ^ 3) * (x ^ 2 + γ * x + 1)) <
        (x ^ 2 + γ * x + 1) ^ 2 := by
    have hγx : 0 < γ * x := mul_pos hγpos hxpos
    nlinarith
  exact dts_quadratic_comparison hC hy hgap hK

def dtsInverse (k : ℝ) : ℝ :=
  (Real.sqrt (4 * k + (8 : ℝ) / 9) - sidonGamma) / 2

theorem dtsInverse_nonneg {k : ℝ} (hk : 0 ≤ k) : 0 ≤ dtsInverse k := by
  have hle : sidonGamma ≤ Real.sqrt (4 * k + (8 : ℝ) / 9) := by
    apply Real.le_sqrt_of_sq_le
    nlinarith [sidonGamma_sq]
  unfold dtsInverse
  linarith

theorem dtsInverse_quadratic {k : ℝ} (hk : 0 ≤ k) :
    dtsInverse k ^ 2 + sidonGamma * dtsInverse k = k := by
  have harg : 0 ≤ 4 * k + (8 : ℝ) / 9 := by linarith
  have hs := Real.sq_sqrt harg
  have hg := sidonGamma_sq
  unfold dtsInverse
  nlinarith

/-- Strict inversion, using the actual real scope relation x^4 n = m. -/
theorem dts_scope_inversion {k n m x : ℝ}
    (hn : 0 < n) (hk : 1 ≤ k) (hx : 0 ≤ x)
    (hrel : x ^ 4 * n = m) (hbound : k < x ^ 2 + sidonGamma * x) :
    n * ((Real.sqrt (4 * k + (8 : ℝ) / 9) - sidonGamma) / 2) ^ 4 < m := by
  have hk0 : 0 ≤ k := by linarith
  have hz0 := dtsInverse_nonneg hk0
  have hzquad := dtsInverse_quadratic hk0
  have hγ := sidonGamma_pos
  have hzlt : dtsInverse k < x := by
    by_contra h
    have hxz : x ≤ dtsInverse k := le_of_not_gt h
    have hprod : 0 ≤ (dtsInverse k - x) * (dtsInverse k + x + sidonGamma) := by
      apply mul_nonneg (sub_nonneg.mpr hxz)
      linarith
    nlinarith
  have hxpos : 0 < x := lt_of_le_of_lt hz0 hzlt
  have hprod1 : 0 < (x - dtsInverse k) * (x + dtsInverse k) := by
    apply mul_pos (sub_pos.mpr hzlt)
    linarith
  have hsq : dtsInverse k ^ 2 < x ^ 2 := by nlinarith
  have hprod2 : 0 < (x ^ 2 - dtsInverse k ^ 2) * (x ^ 2 + dtsInverse k ^ 2) := by
    apply mul_pos (sub_pos.mpr hsq)
    positivity
  have hfourth : dtsInverse k ^ 4 < x ^ 4 := by nlinarith
  change n * dtsInverse k ^ 4 < m
  calc
    n * dtsInverse k ^ 4 < n * x ^ 4 := mul_lt_mul_of_pos_left hfourth hn
    _ = m := by nlinarith [hrel]

/-- A division-free form of the explicit square-root remainder estimate.
Only k ≥ 1 is needed for this algebraic comparison. -/
theorem dts_fourth_lower_of_quadratic {k γ z : ℝ}
    (hk : 1 ≤ k) (hγpos : 0 < γ) (hγlt : γ < 1)
    (hγsq : γ ^ 2 = (8 : ℝ) / 9) (hquad : z ^ 2 + γ * z = k) :
    k ^ 2 - 2 * γ * (k * Real.sqrt k) + (16 : ℝ) / 9 * k -
      2 * Real.sqrt k ≤ z ^ 4 := by
  have hkpos : 0 < k := by linarith
  let s := Real.sqrt k
  have hs0 : 0 ≤ s := Real.sqrt_nonneg _
  have hspos : 0 < s := Real.sqrt_pos.2 hkpos
  have hs2 : s ^ 2 = k := Real.sq_sqrt hkpos.le
  let e := z + γ / 2 - s
  have heq : 4 * e ^ 2 + 8 * s * e = γ ^ 2 := by
    dsimp [e]
    nlinarith [hquad, hs2]
  have heupper : 8 * s * e ≤ 1 := by
    nlinarith [sq_nonneg e]
  have hcoef0 : 0 ≤ γ * (2 * k + γ ^ 2) := by positivity
  have hcoef : γ * (2 * k + γ ^ 2) ≤ 2 * k + 1 := by
    have hm := mul_le_mul_of_nonneg_right hγlt.le
      (by positivity : (0 : ℝ) ≤ 2 * k + γ ^ 2)
    nlinarith
  have hrem : 8 * (γ * (2 * k + γ ^ 2) * e) ≤ 3 * s := by
    by_cases he : 0 ≤ e
    · have hleft := mul_le_mul_of_nonneg_right hcoef he
      have hmid := mul_le_mul_of_nonneg_right (by linarith : 2 * k + 1 ≤ 3 * k) he
      have hke : 24 * k * e ≤ 3 * s := by
        calc
          24 * k * e = (3 * s) * (8 * s * e) := by rw [← hs2]; ring
          _ ≤ (3 * s) * 1 :=
            mul_le_mul_of_nonneg_left heupper (by positivity)
          _ = 3 * s := by ring
      nlinarith only [hleft, hmid, hke]
    · have he' : e ≤ 0 := (lt_of_not_ge he).le
      have hr := mul_nonpos_of_nonneg_of_nonpos hcoef0 he'
      linarith
  have hcube : γ ^ 3 ≤ 1 := by
    have hm := mul_le_mul_of_nonneg_right hγlt.le (sq_nonneg γ)
    nlinarith
  have hcubes := mul_le_mul_of_nonneg_right hcube hs0
  have hfourth : 0 ≤ γ ^ 4 := pow_nonneg hγpos.le 4
  have hzero : (z ^ 2 + γ * z - k) * (z ^ 2 - γ * z + k + γ ^ 2) = 0 := by
    rw [show z ^ 2 + γ * z - k = 0 by linarith]
    ring
  have hquartic : z ^ 4 = k ^ 2 + γ ^ 2 * k - γ * (2 * k + γ ^ 2) * z := by
    nlinarith only [hzero]
  have hexpansion :
      z ^ 4 = k ^ 2 - 2 * γ * k * s + 2 * γ ^ 2 * k -
        γ ^ 3 * s + γ ^ 4 / 2 - γ * (2 * k + γ ^ 2) * e := by
    rw [hquartic]
    dsimp [e]
    ring
  have h2γ : 2 * γ ^ 2 * k = (16 : ℝ) / 9 * k := by
    rw [hγsq]
    ring
  change k ^ 2 - 2 * γ * (k * s) + (16 : ℝ) / 9 * k - 2 * s ≤ z ^ 4
  nlinarith only [hexpansion, hrem, hcubes, hfourth, h2γ, hs0]

theorem dts_inverse_fourth_lower {k : ℝ} (hk : 1 ≤ k) :
    k ^ 2 - 2 * sidonGamma * (k * Real.sqrt k) + (16 : ℝ) / 9 * k -
        2 * Real.sqrt k ≤
      ((Real.sqrt (4 * k + (8 : ℝ) / 9) - sidonGamma) / 2) ^ 4 := by
  have hk0 : 0 ≤ k := by linarith
  exact dts_fourth_lower_of_quadratic hk sidonGamma_pos sidonGamma_lt_one
    sidonGamma_sq (dtsInverse_quadratic hk0)

end Sidon30

end

