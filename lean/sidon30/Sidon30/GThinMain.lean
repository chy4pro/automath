import Sidon30.GThinEnergy
import Sidon30.GThinScale
import Sidon30.TransferCertificate
import Sidon30.SecondOrderFinal

/-! The bounded-difference-multiplicity theorem, with the original coefficient,
additive constant, and onset. The old Sidon theorem is not changed. -/

noncomputable section

namespace Sidon30

theorem gThin_second_order_proof : GThinSecondOrderBound := by
  intro g N A hg hN hGN hAN hA
  let B := shiftWindow A
  have hB : IsGThin g B := isGThin_shiftWindow hA hAN
  have hBN : B ⊆ Finset.range N := shiftWindow_subset_range hAN
  have hcard : B.card = A.card := shiftWindow_card hAN
  have hgpos : (0 : ℝ) < (g : ℝ) := by exact_mod_cast (show 0 < g by omega)
  have hgR : (1 : ℝ) ≤ (g : ℝ) := by exact_mod_cast hg
  by_cases hlarge : N ≤ g
  · have hcardN : B.card ≤ N := by
      simpa only [Finset.card_range] using Finset.card_le_card hBN
    have hcardNR : (A.card : ℝ) ≤ (N : ℝ) := by
      rw [hcard] at hcardN
      exact_mod_cast hcardN
    have hNg : (N : ℝ) ≤ (g : ℝ) := by exact_mod_cast hlarge
    have hsqrt : (N : ℝ) ≤ Real.sqrt ((g : ℝ) * (N : ℝ)) := by
      apply Real.le_sqrt_of_sq_le
      have hm := mul_le_mul_of_nonneg_right hNg (show (0 : ℝ) ≤ (N : ℝ) by positivity)
      nlinarith only [hm]
    have hterm : 0 ≤ (2 * Real.sqrt 2 / 3) *
        Real.sqrt (Real.sqrt ((g : ℝ) * (N : ℝ))) := by positivity
    linarith
  · let x := Real.sqrt (Real.sqrt ((g : ℝ) * (N : ℝ)))
    have hxnonneg : 0 ≤ x := Real.sqrt_nonneg _
    have hx2 : x ^ 2 = Real.sqrt ((g : ℝ) * (N : ℝ)) :=
      Real.sq_sqrt (Real.sqrt_nonneg _)
    have hx4 : x ^ 4 = (g : ℝ) * (N : ℝ) := by
      calc
        x ^ 4 = (x ^ 2) ^ 2 := by ring
        _ = (g : ℝ) * (N : ℝ) := by rw [hx2, Real.sq_sqrt (by positivity)]
    have hx : 120 ≤ x := by
      change (120 : ℝ) ≤ Real.sqrt (Real.sqrt ((g : ℝ) * (N : ℝ)))
      apply Real.le_sqrt_of_sq_le
      apply Real.le_sqrt_of_sq_le
      have hGNr : (120 : ℝ) ^ 4 ≤ (g : ℝ) * (N : ℝ) := by exact_mod_cast hGN
      nlinarith
    have hxpos : 0 < x := by linarith
    have hgN : (g : ℝ) ≤ (N : ℝ) := by
      exact_mod_cast (show g ≤ N by omega)
    have hgx : (g : ℝ) ≤ x ^ 2 := by
      rw [hx2]
      apply Real.le_sqrt_of_sq_le
      have hm := mul_le_mul_of_nonneg_left hgN hgpos.le
      nlinarith only [hm]
    by_cases hkzero : B.card = 0
    · have hAzero : A.card = 0 := hcard.symm.trans hkzero
      rw [hAzero]
      norm_num only [Nat.cast_zero]
      positivity
    · have hkone : (1 : ℝ) ≤ (B.card : ℝ) := by
        exact_mod_cast (show 1 ≤ B.card by omega)
      have hkpred : 0 ≤ (B.card : ℝ) - 1 := sub_nonneg.mpr hkone
      let T := gThinIntegerScale g x
      let η := 29 * (g : ℝ) * (T : ℝ) * ((3 : ℝ) / 4) ^ ((N - 1) / T)
      let C := (N : ℝ) + (2 : ℝ) / 3 * ((T : ℝ) - 1) +
        29 * (T : ℝ) * ((3 : ℝ) / 4) ^ ((N - 1) / T)
      let U := 1 + (rampDiagonal T / (g : ℝ)) * ((B.card : ℝ) - 1)
      have hT : 1 ≤ T := gThinIntegerScale_pos hg hxpos
      have hTpred : 0 ≤ (T : ℝ) - 1 := by
        have hTreal : (1 : ℝ) ≤ (T : ℝ) := by exact_mod_cast hT
        linarith
      have hCnonneg : 0 ≤ C := by dsimp [C]; positivity
      have hηnonneg : 0 ≤ η := by dsimp [η]; positivity
      have hη : η < x ^ 2 / 2 := gThinIntegerScale_tail_lt_half hg hN hx hx4 hgx
      have hcost : (g : ℝ) * C ≤ x ^ 4 + sidonGamma * x ^ 3 + η := by
        have hb := gThinIntegerScale_boundary_le hg hxnonneg hx4
        dsimp [C, η, T]
        nlinarith only [hb]
      have hUeq : (g : ℝ) * U =
          (g : ℝ) + rampDiagonal T * ((B.card : ℝ) - 1) := by
        dsimp [U]
        field_simp [ne_of_gt hgpos]
        <;> ring
      have henergy : orderedPairEnergy B (rampCorrelation T) ≤ (g : ℝ) * U := by
        have he := isGThin_rampEnergy_le hB hT
        have ha := rampDiagonal_nonneg T
        have hm := mul_nonneg ha (sub_nonneg.mpr hgR)
        rw [hUeq]
        nlinarith only [he, hm]
      have hupper : U ≤ 1 + (sidonGamma / x ^ 3) * ((B.card : ℝ) - 1) := by
        have hm := mul_le_mul_of_nonneg_right (gThinIntegerScale_diagonal_le hg hxpos) hkpred
        dsimp [U, T]
        linarith
      have hUnonneg : 0 ≤ U := by
        have ha := rampDiagonal_nonneg T
        dsimp [U]
        positivity
      have hDnonneg : 0 ≤ x ^ 4 + sidonGamma * x ^ 3 + η := by
        have hgamm := sidonGamma_pos
        positivity
      have hraw := ramp_card_sq_le_certificate N T B hN hT hBN
      have hnorm : (B.card : ℝ) ^ 2 ≤ ((g : ℝ) * C) * U := by
        calc
          (B.card : ℝ) ^ 2 ≤ C * orderedPairEnergy B (rampCorrelation T) := hraw
          _ ≤ C * ((g : ℝ) * U) := mul_le_mul_of_nonneg_left henergy hCnonneg
          _ = _ := by ring
      have hscaled : (B.card : ℝ) ^ 2 ≤
          (x ^ 4 + sidonGamma * x ^ 3 + η) *
            (1 + (sidonGamma / x ^ 3) * ((B.card : ℝ) - 1)) :=
        hnorm.trans (mul_le_mul hcost hupper hUnonneg hDnonneg)
      have hfinal := secondOrder_of_scaled_certificate hx sidonGamma_pos
        sidonGamma_lt_one sidonGamma_sq hηnonneg hη hscaled
      rw [hcard, hx2] at hfinal
      simpa only [x, sidonGamma] using hfinal

end Sidon30

/-- The g-thin transfer, with g and N both quantified and no restriction g ≤ N. -/
theorem g_thin_second_order : GThinSecondOrderBound :=
  Sidon30.gThin_second_order_proof

end
