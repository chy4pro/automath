import Sidon30.CorrectionBasic
import Sidon30.RenewalRampIdentity
import Sidon30.RampGramEnergy

/-!
An explicit finite, possibly signed boundary certificate. Its potential is
exactly one at every integer point of the closed N-point window.
No positivity of the certificate is asserted or needed.
-/

noncomputable section
open scoped BigOperators

namespace Sidon30

def boundaryCutoff (N T : ℕ) : ℕ := (N - 1) + (T - 1)

def clippedCorrection (T M : ℕ) (y : ℤ) : ℝ :=
  if y ≤ (M : ℤ) then renewalCorrectionInt T y else 0

def boundaryCertificate (N T : ℕ) (y : ℤ) : ℝ :=
  (if 0 ≤ y ∧ y ≤ (N : ℤ) - 1 then 1 else 0) +
    clippedCorrection T (boundaryCutoff N T) y +
    clippedCorrection T (boundaryCutoff N T) ((N : ℤ) - 1 - y)

theorem boundaryCutoff_cast {N T : ℕ} (hN : 1 ≤ N) (hT : 1 ≤ T) :
    (boundaryCutoff N T : ℤ) = (N : ℤ) + (T : ℤ) - 2 := by
  unfold boundaryCutoff
  omega

private theorem halfLine_indicator_identity {D y : ℤ} (hD : 0 ≤ D) :
    (if 0 ≤ y then (1 : ℝ) else 0) +
        (if 0 ≤ D - y then (1 : ℝ) else 0) =
      1 + (if 0 ≤ y ∧ y ≤ D then (1 : ℝ) else 0) := by
  split_ifs <;> norm_num <;> omega

/-- Truncation changes no coefficient that can contribute to a window potential. -/
theorem boundaryCertificate_eq_on_collar {N T : ℕ} (hN : 1 ≤ N) (hT : 1 ≤ T)
    {y : ℤ} (hylo : 1 - (T : ℤ) ≤ y)
    (hyhi : y ≤ (N : ℤ) + (T : ℤ) - 2) :
    boundaryCertificate N T y =
      renewalInt T y + renewalInt T ((N : ℤ) - 1 - y) - 1 := by
  have hcut := boundaryCutoff_cast hN hT
  have hyM : y ≤ (boundaryCutoff N T : ℤ) := by omega
  have hrM : (N : ℤ) - 1 - y ≤ (boundaryCutoff N T : ℤ) := by omega
  unfold boundaryCertificate clippedCorrection
  rw [if_pos hyM, if_pos hrM,
    renewalCorrectionInt_eq, renewalCorrectionInt_eq]
  have hh := halfLine_indicator_identity (y := y)
    (show 0 ≤ (N : ℤ) - 1 by omega)
  linarith

theorem boundaryCertificate_eq_zero_left {N T : ℕ} (hN : 1 ≤ N) (hT : 1 ≤ T)
    {y : ℤ} (hy : y < 1 - (T : ℤ)) : boundaryCertificate N T y = 0 := by
  have hcut := boundaryCutoff_cast hN hT
  have hyneg : y < 0 := by omega
  have hyM : y ≤ (boundaryCutoff N T : ℤ) := by omega
  have hrM : ¬ (N : ℤ) - 1 - y ≤ (boundaryCutoff N T : ℤ) := by omega
  have hwindow : ¬ (0 ≤ y ∧ y ≤ (N : ℤ) - 1) := by omega
  simp only [boundaryCertificate, clippedCorrection, if_neg hwindow,
    if_pos hyM, if_neg hrM, renewalCorrectionInt_of_neg T hyneg, zero_add]

theorem boundaryCertificate_eq_zero_right {N T : ℕ} (hN : 1 ≤ N) (hT : 1 ≤ T)
    {y : ℤ} (hy : (N : ℤ) + (T : ℤ) - 2 < y) :
    boundaryCertificate N T y = 0 := by
  have hcut := boundaryCutoff_cast hN hT
  have hrneg : (N : ℤ) - 1 - y < 0 := by omega
  have hyM : ¬ y ≤ (boundaryCutoff N T : ℤ) := by omega
  have hrM : (N : ℤ) - 1 - y ≤ (boundaryCutoff N T : ℤ) := by omega
  have hwindow : ¬ (0 ≤ y ∧ y ≤ (N : ℤ) - 1) := by omega
  simp only [boundaryCertificate, clippedCorrection, if_neg hwindow,
    if_neg hyM, if_pos hrM, renewalCorrectionInt_of_neg T hrneg, zero_add]

theorem boundaryCertificate_eq_zero_of_not_mem {N T : ℕ}
    (hN : 1 ≤ N) (hT : 1 ≤ T) {y : ℤ}
    (hy : y ∉ Finset.Icc (1 - (T : ℤ)) ((N : ℤ) + (T : ℤ) - 2)) :
    boundaryCertificate N T y = 0 := by
  by_cases hlo : y < 1 - (T : ℤ)
  · exact boundaryCertificate_eq_zero_left hN hT hlo
  · apply boundaryCertificate_eq_zero_right hN hT
    have hnot : ¬ (1 - (T : ℤ) ≤ y ∧ y ≤ (N : ℤ) + (T : ℤ) - 2) := by
      exact fun h => hy (Finset.mem_Icc.mpr h)
    omega

theorem rampDoublePotential_const {T : ℕ} (hT : 1 ≤ T) (c : ℝ) (x : ℤ) :
    rampDoublePotential T (fun _ => c) x = c := by
  unfold rampDoublePotential
  calc
    (∑ i ∈ Finset.range T, ∑ j ∈ Finset.range T,
        rampWeight T i * rampWeight T j * c) =
        ((∑ i ∈ Finset.range T, rampWeight T i) *
          (∑ j ∈ Finset.range T, rampWeight T j)) * c := by
      rw [Finset.sum_mul_sum]
      simp only [Finset.sum_mul]
    _ = c := by rw [sum_rampWeight hT]; ring

/-- The half-line renewal potential is one on the nonnegative integers. -/
theorem rampDoublePotential_renewal {T : ℕ} (hT : 1 ≤ T) {x : ℤ} (hx : 0 ≤ x) :
    rampDoublePotential T (renewalInt T) x = 1 := by
  unfold rampDoublePotential
  calc
    (∑ i ∈ Finset.range T, ∑ j ∈ Finset.range T,
        rampWeight T i * rampWeight T j * renewalInt T (x + (i : ℤ) - (j : ℤ))) =
        ∑ i ∈ Finset.range T, rampWeight T i := by
      apply Finset.sum_congr rfl
      intro i _hi
      calc
        (∑ j ∈ Finset.range T,
            rampWeight T i * rampWeight T j * renewalInt T (x + (i : ℤ) - (j : ℤ))) =
            rampWeight T i * (∑ j ∈ Finset.range T,
              rampWeight T j * renewalInt T (x + (i : ℤ) - (j : ℤ))) := by
          rw [Finset.mul_sum]
          apply Finset.sum_congr rfl
          intro j _hj
          ring
        _ = rampWeight T i := by
          rw [renewal_ramp_identity hT, if_pos (by omega : 0 ≤ x + (i : ℤ)), mul_one]
    _ = 1 := sum_rampWeight hT

theorem rampDoublePotential_reflected_renewal {T : ℕ} (hT : 1 ≤ T)
    {D x : ℤ} (hx : x ≤ D) :
    rampDoublePotential T (fun y => renewalInt T (D - y)) x = 1 := by
  have hswap : rampDoublePotential T (fun y => renewalInt T (D - y)) x =
      rampDoublePotential T (renewalInt T) (D - x) := by
    unfold rampDoublePotential
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl
    intro i _hi
    apply Finset.sum_congr rfl
    intro j _hj
    have harg : D - (x + (j : ℤ) - (i : ℤ)) = D - x + (i : ℤ) - (j : ℤ) := by omega
    rw [harg]
    ring
  rw [hswap]
  exact rampDoublePotential_renewal hT (by omega)

/-- The finite signed certificate has exactly unit potential on the N-point window. -/
theorem boundaryCertificate_potential {N T : ℕ} (hN : 1 ≤ N) (hT : 1 ≤ T)
    {x : ℤ} (hx0 : 0 ≤ x) (hxN : x ≤ (N : ℤ) - 1) :
    rampDoublePotential T (boundaryCertificate N T) x = 1 := by
  calc
    rampDoublePotential T (boundaryCertificate N T) x =
        rampDoublePotential T
          (fun y => renewalInt T y + renewalInt T ((N : ℤ) - 1 - y) - 1) x := by
      unfold rampDoublePotential
      apply Finset.sum_congr rfl
      intro i hi
      apply Finset.sum_congr rfl
      intro j hj
      have hiT := Finset.mem_range.mp hi
      have hjT := Finset.mem_range.mp hj
      rw [boundaryCertificate_eq_on_collar hN hT (by omega) (by omega)]
    _ = rampDoublePotential T (renewalInt T) x +
          rampDoublePotential T (fun y => renewalInt T ((N : ℤ) - 1 - y)) x -
          rampDoublePotential T (fun _ => 1) x := by
      simp only [rampDoublePotential, mul_sub, mul_add,
        Finset.sum_sub_distrib, Finset.sum_add_distrib]
    _ = 1 := by
      rw [rampDoublePotential_renewal hT hx0,
        rampDoublePotential_reflected_renewal hT hxN, rampDoublePotential_const hT]
      ring

end Sidon30

end
