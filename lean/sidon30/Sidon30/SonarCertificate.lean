import Sidon30.SonarEnergy

/-! The exact triangle/ramp sandwich from finite sliding-window capacity.
The certificate remains signed. Repeated rows are permitted throughout. -/

noncomputable section
open scoped BigOperators
namespace Sidon30

theorem sonar_finite_sandwich {m n U V : ℕ} (y : Fin m → Fin n)
    (hA : IsSonar y) (hn : 1 ≤ n) (hU : 1 ≤ U) (hUm : U ≤ m) (hV : 1 ≤ V) :
    (m : ℝ) * (U : ℝ) - ((U : ℝ) ^ 2 - 1) / 3 ≤
      ((n : ℝ) + (2 : ℝ) / 3 * ((V : ℝ) - 1) +
        29 * (V : ℝ) * ((3 : ℝ) / 4) ^ ((n - 1) / V)) *
      ((m : ℝ) * rampDiagonal V + (U : ℝ) - 1) := by
  let C : ℝ := (n : ℝ) + (2 : ℝ) / 3 * ((V : ℝ) - 1) +
    29 * (V : ℝ) * ((3 : ℝ) / 4) ^ ((n - 1) / V)
  have hC : 0 ≤ C := by
    have hVr : (1 : ℝ) ≤ (V : ℝ) := by exact_mod_cast hV
    have hpred : 0 ≤ (V : ℝ) - 1 := by linarith
    dsimp [C]
    positivity
  have hlocal : ∀ k : ℕ,
      ((sonarFinWindow m U k).card : ℝ) ^ 2 ≤ C *
        (∑ i ∈ sonarFinWindow m U k, ∑ j ∈ sonarFinWindow m U k,
          rampCorrelation V (((y i).val : ℤ) - (y j).val)) := by
    intro k
    apply indexed_ramp_card_sq_le_certificate n V (sonarFinWindow m U k)
      (fun i => ((y i).val : ℤ)) hn hV
    intro i _hi
    have hi := (y i).isLt
    constructor <;> omega
  have hsum :
      (∑ k ∈ Finset.range (m + U), ((sonarFinWindow m U k).card : ℝ) ^ 2) ≤
      C * (∑ k ∈ Finset.range (m + U),
        ∑ i ∈ sonarFinWindow m U k, ∑ j ∈ sonarFinWindow m U k,
          rampCorrelation V (((y i).val : ℤ) - (y j).val)) := by
    rw [Finset.mul_sum]
    exact Finset.sum_le_sum (fun k _hk => hlocal k)
  rw [sonarFinWindow_card_sq_sum hUm, sonarFinWindow_sum_energy] at hsum
  have henergy := isSonar_triangleRampEnergy_le (U := U) (V := V) y hA hU hV
  have hbound := hsum.trans (mul_le_mul_of_nonneg_left henergy hC)
  have hUr : (0 : ℝ) < (U : ℝ) := by exact_mod_cast (show 0 < U by omega)
  have hmul : ((m : ℝ) * (U : ℝ) - ((U : ℝ) ^ 2 - 1) / 3) * (U : ℝ) ≤
      (C * ((m : ℝ) * rampDiagonal V + (U : ℝ) - 1)) * (U : ℝ) := by
    nlinarith only [hbound]
  exact (mul_le_mul_iff_of_pos_right hUr).mp hmul

end Sidon30
end
