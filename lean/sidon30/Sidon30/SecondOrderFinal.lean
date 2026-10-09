import Mathlib

/-!
The final real algebra, conditional on the finite certificate and its tail bound.
This file does not assert the Sidon theorem: the certificate, scale selection,
and square-root substitution must be supplied by the other cards.
-/

namespace Sidon30

/-- An upward quadratic is positive beyond a positive comparison point under
the coefficient conditions used by the finite Sidon certificate. -/
theorem quadratic_certificate_comparison {k y C b : ℝ}
    (hC : 0 < C) (hb : b < 1) (hy : 0 < y)
    (hgap : C * (1 + b * (y - 1)) < y ^ 2)
    (hk : k ^ 2 ≤ C * (1 + b * (k - 1))) : k < y := by
  have hyb : b * C < y := by
    by_contra h
    have hle : y ≤ b * C := le_of_not_gt h
    have hmul := mul_le_mul_of_nonneg_right hle hy.le
    have hpos : 0 < C * (1 - b) := mul_pos hC (sub_pos.mpr hb)
    nlinarith
  by_contra h
  have hyk : y ≤ k := le_of_not_gt h
  have hprod : 0 ≤ (k - y) * (k + y - b * C) := by
    apply mul_nonneg (sub_nonneg.mpr hyk)
    linarith
  nlinarith

/-- The exact polynomial margin responsible for the final additive constant. -/
theorem secondOrder_margin_identity {x γ : ℝ} (hx : x ≠ 0)
    (hγ : γ ^ 2 = (8 : ℝ) / 9) :
    (x ^ 2 + γ * x + 1) ^ 2 -
        (x ^ 4 + γ * x ^ 3) *
          (1 + (γ / x ^ 3) * (x ^ 2 + γ * x + 1 - 1)) =
      (10 : ℝ) / 9 * x ^ 2 + (10 * γ / 9) * x + 1 := by
  have hcube : γ ^ 3 = ((8 : ℝ) / 9) * γ := by
    calc
      γ ^ 3 = γ ^ 2 * γ := by ring
      _ = ((8 : ℝ) / 9) * γ := by rw [hγ]
  have hraw :
      (x ^ 2 + γ * x + 1) ^ 2 -
          (x ^ 4 + γ * x ^ 3) *
            (1 + (γ / x ^ 3) * (x ^ 2 + γ * x + 1 - 1)) =
        (2 - γ ^ 2) * x ^ 2 + (2 * γ - γ ^ 3) * x + 1 := by
    field_simp [hx]
    <;> ring
  rw [hraw, hγ, hcube]
  ring

/-- The original `+1` follows from a certificate with error below `x²/2`.
The inequality in the hypothesis is still a genuine obligation of the
finite boundary construction; it is not assumed by the final Sidon theorem. -/
theorem secondOrder_of_scaled_certificate_one {x γ k η : ℝ}
    (hx : 1 ≤ x) (hγpos : 0 < γ) (hγlt : γ < 1)
    (hγsq : γ ^ 2 = (8 : ℝ) / 9)
    (hηnonneg : 0 ≤ η) (hη : η < x ^ 2 / 2)
    (hk : k ^ 2 ≤ (x ^ 4 + γ * x ^ 3 + η) *
      (1 + (γ / x ^ 3) * (k - 1))) :
    k ≤ x ^ 2 + γ * x + 1 := by
  have hxpos : 0 < x := by linarith
  have hxne : x ≠ 0 := ne_of_gt hxpos
  have hx2 : 0 < x ^ 2 := pow_pos hxpos 2
  have hx3 : 0 < x ^ 3 := pow_pos hxpos 3
  have hx4 : 0 < x ^ 4 := pow_pos hxpos 4
  have hxge1 : 1 ≤ x := by linarith
  have hx3ge1 : 1 ≤ x ^ 3 := one_le_pow₀ hxge1
  have hb : γ / x ^ 3 < 1 := by
    apply (div_lt_iff₀ hx3).mpr
    simpa only [one_mul] using lt_of_lt_of_le hγlt hx3ge1
  have hC : 0 < x ^ 4 + γ * x ^ 3 + η := by
    have := mul_pos hγpos hx3
    linarith
  have hy : 0 < x ^ 2 + γ * x + 1 := by
    have := mul_pos hγpos hxpos
    linarith
  have hfactor_eq :
      1 + (γ / x ^ 3) * (x ^ 2 + γ * x + 1 - 1) =
        1 + γ / x + γ ^ 2 / x ^ 2 := by
    field_simp [hxne]
    <;> ring
  have hfactor_pos :
      0 < 1 + (γ / x ^ 3) * (x ^ 2 + γ * x + 1 - 1) := by
    rw [hfactor_eq]
    positivity
  have hhalf_identity :
      (x ^ 2 / 2) *
          (1 + (γ / x ^ 3) * (x ^ 2 + γ * x + 1 - 1)) =
        x ^ 2 / 2 + γ * x / 2 + (4 : ℝ) / 9 := by
    rw [hfactor_eq]
    have hraw : (x ^ 2 / 2) * (1 + γ / x + γ ^ 2 / x ^ 2) =
        x ^ 2 / 2 + γ * x / 2 + γ ^ 2 / 2 := by
      field_simp [hxne]
      <;> ring
    rw [hraw, hγsq]
    ring
  have herror :
      η * (1 + (γ / x ^ 3) * (x ^ 2 + γ * x + 1 - 1)) <
        x ^ 2 / 2 + γ * x / 2 + (4 : ℝ) / 9 := by
    rw [← hhalf_identity]
    exact mul_lt_mul_of_pos_right hη hfactor_pos
  have hmargin := secondOrder_margin_identity hxne hγsq
  have hremaining : 0 < (11 : ℝ) / 18 * x ^ 2 +
      (11 : ℝ) / 18 * γ * x + (5 : ℝ) / 9 := by positivity
  have hgap :
      (x ^ 4 + γ * x ^ 3 + η) *
          (1 + (γ / x ^ 3) * (x ^ 2 + γ * x + 1 - 1)) <
        (x ^ 2 + γ * x + 1) ^ 2 := by
    nlinarith only [hmargin, herror, hremaining]
  exact (quadratic_certificate_comparison hC hb hy hgap hk).le

/-- Compatibility interface for the transfer proofs at their original onset. -/
theorem secondOrder_of_scaled_certificate {x γ k η : ℝ}
    (hx : 120 ≤ x) (hγpos : 0 < γ) (hγlt : γ < 1)
    (hγsq : γ ^ 2 = (8 : ℝ) / 9)
    (hηnonneg : 0 ≤ η) (hη : η < x ^ 2 / 2)
    (hk : k ^ 2 ≤ (x ^ 4 + γ * x ^ 3 + η) *
      (1 + (γ / x ^ 3) * (k - 1))) :
    k ≤ x ^ 2 + γ * x + 1 :=
  secondOrder_of_scaled_certificate_one (by linarith) hγpos hγlt hγsq hηnonneg hη hk

end Sidon30
