import Sidon30.SonarCertificate
import Sidon30.SonarFinal

/-! The exact sonar target, discharged by the finite triangle/ramp certificate. -/

/-- Ordered displacement uniqueness gives the paper's triangle-kernel bound,
with the exact onset and real powers. No row-injectivity hypothesis is needed. -/
theorem sonar_triangle_bound : SonarTriangleBound := by
  intro m n y hn hA
  let x := Sidon30.sonarCubeRoot n
  have hx : 48 ≤ x := Sidon30.sonarCubeRoot_ge hn
  have hxpos : 0 < x := by linarith
  have hx3 : x ^ 3 = (n : ℝ) := Sidon30.sonarCubeRoot_cube n
  have hpoly : (m : ℝ) ≤ x ^ 3 + 2 * x ^ 2 + 3 * x := by
    by_cases hUm : Sidon30.sonarHorizontalScale x ≤ m
    · have hsandwich := Sidon30.sonar_finite_sandwich y hA (by omega)
        (Sidon30.sonarHorizontalScale_pos hxpos) hUm
        (Sidon30.sonarVerticalScale_pos hxpos)
      exact Sidon30.sonar_of_finite_sandwich hx hx3 (by positivity) hsandwich
    · have hmU : (m : ℝ) ≤ (Sidon30.sonarHorizontalScale x : ℝ) := by
        exact_mod_cast (show m ≤ Sidon30.sonarHorizontalScale x by omega)
      have hupper := Sidon30.sonarHorizontalScale_upper x
      have hcube : 0 ≤ x ^ 3 := pow_nonneg hxpos.le 3
      linarith
  change (m : ℝ) ≤ Sidon30.sonarCubeRoot n ^ 3 +
    2 * Sidon30.sonarCubeRoot n ^ 2 + 3 * Sidon30.sonarCubeRoot n at hpoly
  rw [Sidon30.sonarCubeRoot_cube, Sidon30.sonarCubeRoot_sq] at hpoly
  exact hpoly
