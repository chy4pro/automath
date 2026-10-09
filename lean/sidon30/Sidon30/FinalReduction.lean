import Sidon30.Statement
import Sidon30.ShiftWindow
import Sidon30.IntegerScaleAndTail
import Sidon30.SecondOrderFinal

/-!
An explicit interface for the remaining finite certificate, and the reduction
from that interface to the exact target statement. The certificate proposition
is not an axiom and is not proved in this file. The final theorem can only be
closed by supplying its proof from the finite boundary construction.
-/

namespace Sidon30

/-- The finite certificate inequality, on a window with exactly N points. -/
def DiscreteSidonCertificateBound : Prop :=
  ∀ (N T : ℕ) (A : Finset ℕ),
    1 ≤ N → 1 ≤ T → A ⊆ Finset.range N → IsSidon A →
    (A.card : ℝ) ^ 2 ≤
      ((N : ℝ) + (2 : ℝ) / 3 * ((T : ℝ) - 1) +
        29 * (T : ℝ) * ((3 : ℝ) / 4) ^ ((N - 1) / T)) *
      (1 + rampDiagonal T * ((A.card : ℝ) - 1))

/-- The exact rational fourth-root lower bound at the new natural onset. -/
theorem sidon_fourthRoot_gt_of_onset {N : ℕ} (hN : 4600000 ≤ N) :
    (463 : ℝ) / 10 < Real.sqrt (Real.sqrt (N : ℝ)) := by
  let x := Real.sqrt (Real.sqrt (N : ℝ))
  have hxnonneg : 0 ≤ x := Real.sqrt_nonneg _
  have hx2 : x ^ 2 = Real.sqrt (N : ℝ) := Real.sq_sqrt (Real.sqrt_nonneg _)
  have hx4 : x ^ 4 = (N : ℝ) := by
    calc
      x ^ 4 = (x ^ 2) ^ 2 := by ring
      _ = (N : ℝ) := by rw [hx2, Real.sq_sqrt (by positivity)]
  have hNr : (4600000 : ℝ) ≤ (N : ℝ) := by exact_mod_cast hN
  change (463 : ℝ) / 10 < x
  by_contra h
  have hle : x ≤ (463 : ℝ) / 10 := le_of_not_gt h
  have hpow : x ^ 4 ≤ ((463 : ℝ) / 10) ^ 4 := by gcongr
  norm_num at hpow
  nlinarith only [hpow, hx4, hNr]

/-- The finite certificate yields the audited target at every N ≥ 4600000. -/
theorem sidon_second_order_of_discreteCertificate'
    (hcertificate : DiscreteSidonCertificateBound) : SidonSecondOrderBound' := by
  intro N A hN hAN hA
  let B := shiftWindow A
  have hB : IsSidon B := isSidon_shiftWindow hA hAN
  have hBN : B ⊆ Finset.range N := shiftWindow_subset_range hAN
  have hcard : B.card = A.card := shiftWindow_card hAN
  let x := Real.sqrt (Real.sqrt (N : ℝ))
  have hxnonneg : 0 ≤ x := Real.sqrt_nonneg _
  have hx2 : x ^ 2 = Real.sqrt (N : ℝ) := Real.sq_sqrt (Real.sqrt_nonneg _)
  have hx4 : x ^ 4 = (N : ℝ) := by
    calc
      x ^ 4 = (x ^ 2) ^ 2 := by ring
      _ = (N : ℝ) := by rw [hx2, Real.sq_sqrt (by positivity)]
  have hx : (463 : ℝ) / 10 ≤ x := (sidon_fourthRoot_gt_of_onset hN).le
  have hxpos : 0 < x := by linarith
  by_cases hkzero : B.card = 0
  · have hAzero : A.card = 0 := hcard.symm.trans hkzero
    rw [hAzero]
    norm_num only [Nat.cast_zero]
    positivity
  · have hkone : (1 : ℝ) ≤ (B.card : ℝ) := by
      exact_mod_cast (show 1 ≤ B.card by omega)
    have hkpred : 0 ≤ (B.card : ℝ) - 1 := sub_nonneg.mpr hkone
    let T := sidonIntegerScale x
    let η := 29 * (T : ℝ) * ((3 : ℝ) / 4) ^ ((N - 1) / T)
    have hT : 1 ≤ T := sidonIntegerScale_pos hxpos
    have hηnonneg : 0 ≤ η := sidonIntegerScale_tail_nonneg N x
    have hη : η < x ^ 2 / 2 := sidonIntegerScale_tail_lt_half_sharp hx hx4
    have hcost : (N : ℝ) + (2 : ℝ) / 3 * ((T : ℝ) - 1) + η ≤
        x ^ 4 + sidonGamma * x ^ 3 + η := by
      have hb := sidonIntegerScale_boundary_le hxnonneg hx4
      linarith
    have hupper : 1 + rampDiagonal T * ((B.card : ℝ) - 1) ≤
        1 + (sidonGamma / x ^ 3) * ((B.card : ℝ) - 1) := by
      have hm := mul_le_mul_of_nonneg_right
        (sidonIntegerScale_diagonal_le hxpos) hkpred
      linarith
    have hUnonneg : 0 ≤ 1 + rampDiagonal T * ((B.card : ℝ) - 1) := by
      have hm := mul_nonneg (rampDiagonal_nonneg T) hkpred
      linarith
    have hCnonneg : 0 ≤ x ^ 4 + sidonGamma * x ^ 3 + η := by
      have hg := sidonGamma_pos
      positivity
    have hraw := hcertificate N T B (by omega) hT hBN hB
    have hscaled : (B.card : ℝ) ^ 2 ≤
        (x ^ 4 + sidonGamma * x ^ 3 + η) *
          (1 + (sidonGamma / x ^ 3) * ((B.card : ℝ) - 1)) := by
      exact hraw.trans (mul_le_mul hcost hupper hUnonneg hCnonneg)
    have hfinal := secondOrder_of_scaled_certificate_one (by linarith : 1 ≤ x) sidonGamma_pos
      sidonGamma_lt_one sidonGamma_sq hηnonneg hη hscaled
    rw [hcard, hx2] at hfinal
    simpa only [x, sidonGamma] using hfinal

/-- Compatibility reduction for the unchanged original specification. -/
theorem sidon_second_order_of_discreteCertificate
    (hcertificate : DiscreteSidonCertificateBound) : SidonSecondOrderBound := by
  intro N A hN hAN hA
  exact sidon_second_order_of_discreteCertificate' hcertificate N A
    (le_trans (by norm_num : 4600000 ≤ 120 ^ 4) hN) hAN hA

end Sidon30
