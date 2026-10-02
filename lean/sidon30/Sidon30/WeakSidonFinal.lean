import Sidon30.TransferStatement
import Sidon30.TransferCertificate
import Sidon30.WeakSidonEnergy
import Sidon30.WeakSidonScale
import Sidon30.SecondOrderFinal

/-!
The exact weak Sidon second-order bound. The proof combines the actual finite
ramp certificate and weak Sidon energy inequality with the integer scale.
The auxiliary real comparison is explicitly conditional; the final theorem
has only the hypotheses in WeakSidonSecondOrderBound.
-/

namespace Sidon30

theorem weakSecondOrder_margin_identity {x β : ℝ} (hx : x ≠ 0)
    (hβ : β ^ 2 = (8 : ℝ) / 3) :
    (x ^ 2 + β * x + 2) ^ 2 -
        (x ^ 4 + β * x ^ 3) *
          (1 + (β / x ^ 3) * (x ^ 2 + β * x + 2 - 1)) =
      (4 : ℝ) / 3 * x ^ 2 + (β / 3) * x + (4 : ℝ) / 3 := by
  have hcube : β ^ 3 = ((8 : ℝ) / 3) * β := by
    calc
      β ^ 3 = β ^ 2 * β := by ring
      _ = ((8 : ℝ) / 3) * β := by rw [hβ]
  have hraw :
      (x ^ 2 + β * x + 2) ^ 2 -
          (x ^ 4 + β * x ^ 3) *
            (1 + (β / x ^ 3) * (x ^ 2 + β * x + 2 - 1)) =
        (4 - β ^ 2) * x ^ 2 + (3 * β - β ^ 3) * x + 4 - β ^ 2 := by
    field_simp [hx]
    <;> ring
  rw [hraw, hβ, hcube]
  ring

theorem weakSecondOrder_of_scaled_certificate {x β k η : ℝ}
    (hx : 90 ≤ x) (hβpos : 0 < β) (hβlt : β < 2)
    (hβsq : β ^ 2 = (8 : ℝ) / 3)
    (hηnonneg : 0 ≤ η) (hη : η < x ^ 2 / 2)
    (hk : k ^ 2 ≤ (x ^ 4 + β * x ^ 3 + η) *
      (1 + (β / x ^ 3) * (k - 1))) :
    k ≤ x ^ 2 + β * x + 2 := by
  have hxpos : 0 < x := by linarith
  have hxne : x ≠ 0 := ne_of_gt hxpos
  have hx2 : 0 < x ^ 2 := pow_pos hxpos 2
  have hx3 : 0 < x ^ 3 := pow_pos hxpos 3
  have hx4 : 0 < x ^ 4 := pow_pos hxpos 4
  have hxge1 : 1 ≤ x := by linarith
  have hx2ge1 : 1 ≤ x ^ 2 := one_le_pow₀ hxge1
  have hx3large : (90 : ℝ) ≤ x ^ 3 := by
    have hm := mul_le_mul_of_nonneg_left hx2ge1 hxpos.le
    nlinarith
  have hb : β / x ^ 3 < 1 := by
    apply (div_lt_iff₀ hx3).mpr
    linarith
  have hC : 0 < x ^ 4 + β * x ^ 3 + η := by
    have := mul_pos hβpos hx3
    linarith
  have hy : 0 < x ^ 2 + β * x + 2 := by
    have := mul_pos hβpos hxpos
    linarith
  have hfrac1 : β / x < (1 : ℝ) / 3 := by
    apply (div_lt_iff₀ hxpos).mpr
    linarith
  have hfrac2 : β ^ 2 / x ^ 2 < (1 : ℝ) / 3 := by
    apply (div_lt_iff₀ hx2).mpr
    nlinarith [sq_nonneg (x - 90)]
  have hfrac3 : β / x ^ 3 < (1 : ℝ) / 3 := by
    apply (div_lt_iff₀ hx3).mpr
    linarith
  have hfactor_eq :
      1 + (β / x ^ 3) * (x ^ 2 + β * x + 2 - 1) =
        1 + β / x + β ^ 2 / x ^ 2 + β / x ^ 3 := by
    field_simp [hxne]
    <;> ring
  have hfactor_lt :
      1 + (β / x ^ 3) * (x ^ 2 + β * x + 2 - 1) < 2 := by
    rw [hfactor_eq]
    linarith
  have herror :
      η * (1 + (β / x ^ 3) * (x ^ 2 + β * x + 2 - 1)) < x ^ 2 := by
    have hmul := mul_le_mul_of_nonneg_left hfactor_lt.le hηnonneg
    nlinarith
  have hmargin := weakSecondOrder_margin_identity hxne hβsq
  have hgap :
      (x ^ 4 + β * x ^ 3 + η) *
          (1 + (β / x ^ 3) * (x ^ 2 + β * x + 2 - 1)) <
        (x ^ 2 + β * x + 2) ^ 2 := by
    have hβx : 0 < β * x := mul_pos hβpos hxpos
    nlinarith
  exact (quadratic_certificate_comparison hC hb hy hgap hk).le

/-- The paper's exact weak Sidon coefficient, additive constant and onset. -/
theorem weakSidon_second_order : WeakSidonSecondOrderBound := by
  intro N A hN hAN hA
  let B := shiftWindow A
  have hB : IsWeakSidon B := isWeakSidon_shiftWindow hA hAN
  have hBN : B ⊆ Finset.range N := shiftWindow_subset_range hAN
  have hcard : B.card = A.card := shiftWindow_card hAN
  let x := Real.sqrt (Real.sqrt (N : ℝ))
  have hxnonneg : 0 ≤ x := Real.sqrt_nonneg _
  have hx2 : x ^ 2 = Real.sqrt (N : ℝ) := Real.sq_sqrt (Real.sqrt_nonneg _)
  have hx4 : x ^ 4 = (N : ℝ) := by
    calc
      x ^ 4 = (x ^ 2) ^ 2 := by ring
      _ = (N : ℝ) := by rw [hx2, Real.sq_sqrt (by positivity)]
  have hx : 90 ≤ x := by
    change (90 : ℝ) ≤ Real.sqrt (Real.sqrt (N : ℝ))
    apply Real.le_sqrt_of_sq_le
    apply Real.le_sqrt_of_sq_le
    have hNr : (90 : ℝ) ^ 4 ≤ (N : ℝ) := by exact_mod_cast hN
    nlinarith
  have hxpos : 0 < x := by linarith
  by_cases hkzero : B.card = 0
  · have hAzero : A.card = 0 := hcard.symm.trans hkzero
    rw [hAzero]
    norm_num only [Nat.cast_zero]
    positivity
  · have hkoneNat : 1 ≤ B.card := by omega
    have hkone : (1 : ℝ) ≤ (B.card : ℝ) := by exact_mod_cast hkoneNat
    have hkpred : 0 ≤ (B.card : ℝ) - 1 := sub_nonneg.mpr hkone
    let T := weakSidonIntegerScale x
    let η := 29 * (T : ℝ) * ((3 : ℝ) / 4) ^ ((N - 1) / T)
    have hT : 1 ≤ T := weakSidonIntegerScale_pos hxpos
    have hTreal : (1 : ℝ) ≤ (T : ℝ) := by exact_mod_cast hT
    have hηnonneg : 0 ≤ η := weakSidonIntegerScale_tail_nonneg N x
    have hη : η < x ^ 2 / 2 := weakSidonIntegerScale_tail_lt_half hx hx4
    have hcost : (N : ℝ) + (2 : ℝ) / 3 * ((T : ℝ) - 1) + η ≤
        x ^ 4 + weakSidonBeta * x ^ 3 + η := by
      have hb := weakSidonIntegerScale_boundary_le hxnonneg hx4
      linarith
    have hupper : 1 + 3 * rampDiagonal T * ((B.card : ℝ) - 1) ≤
        1 + (weakSidonBeta / x ^ 3) * ((B.card : ℝ) - 1) := by
      have hm := mul_le_mul_of_nonneg_right
        (weakSidonIntegerScale_diagonal_le hxpos) hkpred
      linarith
    have hUnonneg : 0 ≤ 1 + 3 * rampDiagonal T * ((B.card : ℝ) - 1) := by
      have hm := mul_nonneg
        (mul_nonneg (by norm_num : (0 : ℝ) ≤ 3) (rampDiagonal_nonneg T)) hkpred
      linarith
    have hCnonneg : 0 ≤ x ^ 4 + weakSidonBeta * x ^ 3 + η := by
      have hb := weakSidonBeta_pos
      positivity
    have hrawCnonneg :
        0 ≤ (N : ℝ) + (2 : ℝ) / 3 * ((T : ℝ) - 1) + η := by
      have hboundary := mul_nonneg (by norm_num : (0 : ℝ) ≤ 2 / 3)
        (sub_nonneg.mpr hTreal)
      have hNnonneg : (0 : ℝ) ≤ (N : ℝ) := by positivity
      linarith
    have hraw := ramp_card_sq_le_certificate N T B (by omega) hT hBN
    have henergy := isWeakSidon_rampEnergy_le hB hT hkoneNat
    have hrawU : (B.card : ℝ) ^ 2 ≤
        ((N : ℝ) + (2 : ℝ) / 3 * ((T : ℝ) - 1) + η) *
          (1 + 3 * rampDiagonal T * ((B.card : ℝ) - 1)) := by
      exact hraw.trans (mul_le_mul_of_nonneg_left henergy hrawCnonneg)
    have hscaled : (B.card : ℝ) ^ 2 ≤
        (x ^ 4 + weakSidonBeta * x ^ 3 + η) *
          (1 + (weakSidonBeta / x ^ 3) * ((B.card : ℝ) - 1)) := by
      exact hrawU.trans (mul_le_mul hcost hupper hUnonneg hCnonneg)
    have hfinal := weakSecondOrder_of_scaled_certificate hx weakSidonBeta_pos
      weakSidonBeta_lt_two weakSidonBeta_sq hηnonneg hη hscaled
    rw [hcard, hx2] at hfinal
    simpa only [x, weakSidonBeta_eq_sqrt] using hfinal

end Sidon30

