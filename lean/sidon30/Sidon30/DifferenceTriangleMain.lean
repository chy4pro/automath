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

end Sidon30
