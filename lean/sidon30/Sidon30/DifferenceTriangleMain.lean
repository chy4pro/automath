import Sidon30.DifferenceTriangleEnergy
import Sidon30.DifferenceTriangleScale
import Sidon30.DifferenceTriangleFinal

namespace Sidon30

/-- The shared difference count supplies the exact onset for the real
scope-per-row parameter m/n. It is not rounded to an integer. -/
theorem dts_root_data {n k m : ℕ} {X : Fin n → Finset ℕ}
    (hn : 1 ≤ n) (hk : 20365 ≤ k) (hX : IsDifferenceTriangleSet n k m X) :
    let x := Real.sqrt (Real.sqrt ((m : ℝ) / (n : ℝ)))
    120 ≤ x ∧ x ^ 4 * (n : ℝ) = (m : ℝ) := by
  let x := Real.sqrt (Real.sqrt ((m : ℝ) / (n : ℝ)))
  have hnpos : (0 : ℝ) < (n : ℝ) := by exact_mod_cast (show 0 < n by omega)
  have hkR : (20365 : ℝ) ≤ (k : ℝ) := by exact_mod_cast hk
  have hkk : (120 : ℝ) ^ 4 ≤ (k : ℝ) * ((k : ℝ) + 1) / 2 := by
    nlinarith [sq_nonneg ((k : ℝ) - 20365)]
  have hcount := dts_scope_count hX
  have hminimum : (120 : ℝ) ^ 4 ≤ (m : ℝ) / (n : ℝ) := by
    apply (le_div_iff₀ hnpos).mpr
    have hscaled := mul_le_mul_of_nonneg_left hkk hnpos.le
    nlinarith only [hcount, hscaled]
  have hx : 120 ≤ x := by
    apply Real.le_sqrt_of_sq_le
    apply Real.le_sqrt_of_sq_le
    nlinarith only [hminimum]
  have hx2 : x ^ 2 = Real.sqrt ((m : ℝ) / (n : ℝ)) :=
    Real.sq_sqrt (Real.sqrt_nonneg _)
  have hx4 : x ^ 4 = (m : ℝ) / (n : ℝ) := by
    calc
      x ^ 4 = (x ^ 2) ^ 2 := by ring
      _ = (m : ℝ) / (n : ℝ) := by rw [hx2, Real.sq_sqrt (by positivity)]
  refine ⟨hx, ?_⟩
  rw [hx4]
  exact div_mul_cancel₀ _ (ne_of_gt hnpos)

/-- Strict row-cardinality comparison at the real scope-per-row scale. -/
theorem dts_card_comparison {n k m : ℕ} {X : Fin n → Finset ℕ}
    (hn : 1 ≤ n) (hk : 20365 ≤ k) (hX : IsDifferenceTriangleSet n k m X) :
    let x := Real.sqrt (Real.sqrt ((m : ℝ) / (n : ℝ)))
    (k : ℝ) < x ^ 2 + sidonGamma * x := by
  let x := Real.sqrt (Real.sqrt ((m : ℝ) / (n : ℝ)))
  obtain ⟨hx, hx4m⟩ := dts_root_data hn hk hX
  have hxpos : 0 < x := by linarith
  let T := dtsIntegerScale n x
  let η := dtsScaleError n m x
  have hT : 1 ≤ T := dtsIntegerScale_pos hn hxpos
  have hηnonneg : 0 ≤ η := dtsScaleError_nonneg n m x
  have hη : η < x ^ 2 / 2 := dtsScaleError_lt_half hn hx hx4m
  have hcost :
      ((m : ℝ) + 1 + (2 : ℝ) / 3 * ((T : ℝ) - 1) +
        29 * (T : ℝ) * ((3 : ℝ) / 4) ^ (m / T)) / (n : ℝ) ≤
      x ^ 4 + sidonGamma * x ^ 3 + η := by
    simpa only [Nat.cast_add, Nat.cast_one, Nat.add_sub_cancel] using
      (dtsIntegerScale_cost_le hn hxpos.le hx4m)
  have hupper : 1 + (n : ℝ) * rampDiagonal T * ((k : ℝ) + 1) ≤
      1 + (sidonGamma / x ^ 3) * ((k : ℝ) + 1) := by
    have hmul := mul_le_mul_of_nonneg_right
      (dtsIntegerScale_diagonal_le hn hxpos) (by positivity : (0 : ℝ) ≤ (k : ℝ) + 1)
    linarith
  have hUnonneg : 0 ≤ 1 + (n : ℝ) * rampDiagonal T * ((k : ℝ) + 1) := by
    have ha := rampDiagonal_nonneg T
    positivity
  have hDnonneg : 0 ≤ x ^ 4 + sidonGamma * x ^ 3 + η := by
    have hγ := sidonGamma_pos
    positivity
  have hraw : ((k : ℝ) + 1) ^ 2 ≤
      (((m : ℝ) + 1 + (2 : ℝ) / 3 * ((T : ℝ) - 1) +
        29 * (T : ℝ) * ((3 : ℝ) / 4) ^ (m / T)) / (n : ℝ)) *
      (1 + (n : ℝ) * rampDiagonal T * ((k : ℝ) + 1)) := by
    simpa only [Nat.cast_add, Nat.cast_one, Nat.add_sub_cancel] using
      (dts_finite_certificate hn hT hX)
  have hscaled : ((k : ℝ) + 1) ^ 2 ≤
      (x ^ 4 + sidonGamma * x ^ 3 + η) *
        (1 + (sidonGamma / x ^ 3) * ((k : ℝ) + 1)) :=
    hraw.trans (mul_le_mul hcost hupper hUnonneg hDnonneg)
  have hfinal := dts_of_scaled_certificate hx sidonGamma_pos sidonGamma_lt_one
    sidonGamma_sq hηnonneg hη hscaled
  linarith

end Sidon30

/-- Every normalized difference triangle configuration satisfies the strict
scope bound, with the exact coefficient and k >= 20365 onset. -/
theorem difference_triangle_scope_bound : DifferenceTriangleScopeBound := by
  intro n k m X hn hk hX
  let x := Real.sqrt (Real.sqrt ((m : ℝ) / (n : ℝ)))
  obtain ⟨hx, hx4m⟩ := Sidon30.dts_root_data hn hk hX
  have hnpos : (0 : ℝ) < (n : ℝ) := by exact_mod_cast (show 0 < n by omega)
  have hkone : (1 : ℝ) ≤ (k : ℝ) := by exact_mod_cast (show 1 ≤ k by omega)
  have hbound := Sidon30.dts_card_comparison hn hk hX
  have hfinal := Sidon30.dts_scope_inversion hnpos hkone
    (show 0 ≤ x by positivity) hx4m hbound
  simpa only [Sidon30.sidonGamma] using hfinal

/-- The expanded scope bound with the explicit -2 sqrt(k) remainder. -/
theorem difference_triangle_expanded_bound : DifferenceTriangleExpandedBound := by
  intro n k m X hn hk hX
  have hstrict := difference_triangle_scope_bound n k m X hn hk hX
  have hkone : (1 : ℝ) ≤ (k : ℝ) := by exact_mod_cast (show 1 ≤ k by omega)
  have hfourth := Sidon30.dts_inverse_fourth_lower hkone
  have hmult := mul_le_mul_of_nonneg_left hfourth
    (by positivity : (0 : ℝ) ≤ (n : ℝ))
  have hscaled :
      (n : ℝ) * ((k : ℝ) ^ 2 - 2 * Sidon30.sidonGamma *
        ((k : ℝ) * Real.sqrt (k : ℝ)) + (16 : ℝ) / 9 * (k : ℝ) -
        2 * Real.sqrt (k : ℝ)) ≤ (m : ℝ) := by
    apply le_trans hmult
    simpa only [Sidon30.sidonGamma] using hstrict.le
  convert hscaled using 1 <;> unfold Sidon30.sidonGamma <;> ring
