import Sidon30.IntegerScaleAndTail

/-! Integer scale for n rows in the spatial window of m+1 points.
The quotient is m/T, and the extra 1/n in the certificate is explicit. -/

noncomputable section

namespace Sidon30

def dtsIntegerScale (n : ℕ) (x : ℝ) : ℕ :=
  Nat.ceil (Real.sqrt 2 * (n : ℝ) * x ^ 3)

def dtsScaleError (n m : ℕ) (x : ℝ) : ℝ :=
  29 * (dtsIntegerScale n x : ℝ) / (n : ℝ) *
    ((3 : ℝ) / 4) ^ (m / dtsIntegerScale n x) + 1 / (n : ℝ)

theorem dtsIntegerScale_pos {n : ℕ} {x : ℝ}
    (hn : 1 ≤ n) (hx : 0 < x) : 1 ≤ dtsIntegerScale n x := by
  have hnpos : (0 : ℝ) < (n : ℝ) := by exact_mod_cast (show 0 < n by omega)
  apply Nat.one_le_ceil_iff.mpr
  positivity

theorem dtsIntegerScale_lower (n : ℕ) (x : ℝ) :
    Real.sqrt 2 * (n : ℝ) * x ^ 3 ≤ (dtsIntegerScale n x : ℝ) :=
  Nat.le_ceil _

theorem dtsIntegerScale_lt {n : ℕ} {x : ℝ} (hx : 0 ≤ x) :
    (dtsIntegerScale n x : ℝ) < Real.sqrt 2 * (n : ℝ) * x ^ 3 + 1 :=
  Nat.ceil_lt_add_one (by positivity)

theorem dtsIntegerScale_sub_one_le {n : ℕ} {x : ℝ} (hx : 0 ≤ x) :
    (dtsIntegerScale n x : ℝ) - 1 ≤ Real.sqrt 2 * (n : ℝ) * x ^ 3 := by
  have h := dtsIntegerScale_lt (n := n) hx
  linarith

theorem dtsIntegerScale_upper {n : ℕ} {x : ℝ}
    (hn : 1 ≤ n) (hx : 120 ≤ x) :
    (dtsIntegerScale n x : ℝ) ≤ (3 : ℝ) / 2 * (n : ℝ) * x ^ 3 := by
  have hnR : (1 : ℝ) ≤ (n : ℝ) := by exact_mod_cast hn
  have hxpos : 0 < x := by linarith
  have hxone : 1 ≤ x := by linarith
  have hx2one : 1 ≤ x ^ 2 := one_le_pow₀ hxone
  have hx3large : (12 : ℝ) ≤ x ^ 3 := by
    have h := mul_le_mul_of_nonneg_left hx2one hxpos.le
    nlinarith
  have hnprod := mul_le_mul_of_nonneg_right hnR (pow_nonneg hxpos.le 3)
  have hs : Real.sqrt 2 ≤ (17 : ℝ) / 12 := by
    apply (Real.sqrt_le_left (by norm_num : (0 : ℝ) ≤ 17 / 12)).mpr
    norm_num
  have hmul := mul_le_mul_of_nonneg_right hs
    (by positivity : 0 ≤ (n : ℝ) * x ^ 3)
  have hceil := dtsIntegerScale_lt (n := n) hxpos.le
  nlinarith

theorem dtsIntegerScale_div_upper {n : ℕ} {x : ℝ}
    (hn : 1 ≤ n) (hx : 120 ≤ x) :
    (dtsIntegerScale n x : ℝ) / (n : ℝ) ≤ (3 : ℝ) / 2 * x ^ 3 := by
  have hnpos : (0 : ℝ) < (n : ℝ) := by exact_mod_cast (show 0 < n by omega)
  apply (div_le_iff₀ hnpos).mpr
  have h := dtsIntegerScale_upper hn hx
  nlinarith only [h]

theorem dtsIntegerScale_diagonal_le {n : ℕ} {x : ℝ}
    (hn : 1 ≤ n) (hx : 0 < x) :
    (n : ℝ) * rampDiagonal (dtsIntegerScale n x) ≤ sidonGamma / x ^ 3 := by
  have hT := dtsIntegerScale_pos hn hx
  have hTpos : (0 : ℝ) < (dtsIntegerScale n x : ℝ) := by
    exact_mod_cast (show 0 < dtsIntegerScale n x by omega)
  have hx3pos : 0 < x ^ 3 := pow_pos hx 3
  have hs : (Real.sqrt 2) ^ 2 = (2 : ℝ) := Real.sq_sqrt (by norm_num)
  have hprod : 4 * (n : ℝ) * x ^ 3 ≤
      2 * Real.sqrt 2 * (dtsIntegerScale n x : ℝ) := by
    calc
      4 * (n : ℝ) * x ^ 3 =
          (2 * Real.sqrt 2) * (Real.sqrt 2 * (n : ℝ) * x ^ 3) := by
        calc
          _ = 2 * (Real.sqrt 2) ^ 2 * (n : ℝ) * x ^ 3 := by rw [hs]; ring
          _ = _ := by ring
      _ ≤ (2 * Real.sqrt 2) * (dtsIntegerScale n x : ℝ) :=
        mul_le_mul_of_nonneg_left (dtsIntegerScale_lower n x) (by positivity)
  calc
    (n : ℝ) * rampDiagonal (dtsIntegerScale n x) ≤
        (n : ℝ) * (4 / (3 * (dtsIntegerScale n x : ℝ))) :=
      mul_le_mul_of_nonneg_left (rampDiagonal_le hT) (by positivity)
    _ = (4 * (n : ℝ)) / (3 * (dtsIntegerScale n x : ℝ)) := by ring
    _ ≤ sidonGamma / x ^ 3 := by
      apply (div_le_div_iff₀ (by positivity : 0 < 3 * (dtsIntegerScale n x : ℝ))
        hx3pos).mpr
      unfold sidonGamma
      nlinarith only [hprod]

theorem dtsIntegerScale_boundary_le {n m : ℕ} {x : ℝ}
    (hn : 1 ≤ n) (hx : 0 ≤ x) (hx4m : x ^ 4 * (n : ℝ) = (m : ℝ)) :
    ((m : ℝ) + (2 : ℝ) / 3 * ((dtsIntegerScale n x : ℝ) - 1)) / (n : ℝ) ≤
      x ^ 4 + sidonGamma * x ^ 3 := by
  have hnpos : (0 : ℝ) < (n : ℝ) := by exact_mod_cast (show 0 < n by omega)
  have hsub := dtsIntegerScale_sub_one_le (n := n) hx
  apply (div_le_iff₀ hnpos).mpr
  unfold sidonGamma
  nlinarith only [hsub, hx4m]

theorem dtsIntegerScale_quotient_bound {n m : ℕ} {x : ℝ}
    (hn : 1 ≤ n) (hx : 120 ≤ x) (hx4m : x ^ 4 * (n : ℝ) = (m : ℝ)) :
    x ≤ 2 * (((m / dtsIntegerScale n x : ℕ) : ℝ) + 2) := by
  have hxpos : 0 < x := by linarith
  have hnpos : (0 : ℝ) < (n : ℝ) := by exact_mod_cast (show 0 < n by omega)
  let T := dtsIntegerScale n x
  have hT : 1 ≤ T := dtsIntegerScale_pos hn hxpos
  have hdiv : m < T * (m / T + 1) := by
    have hrem := Nat.mod_lt m (show 0 < T by omega)
    have hid := Nat.mod_add_div m T
    nlinarith
  have hdivR : (m : ℝ) < (T : ℝ) * (((m / T : ℕ) : ℝ) + 1) := by
    exact_mod_cast hdiv
  have hTupper : (T : ℝ) ≤ 2 * (n : ℝ) * x ^ 3 := by
    have h := dtsIntegerScale_upper hn hx
    have hnonneg : 0 ≤ (n : ℝ) * x ^ 3 := by positivity
    dsimp [T]
    nlinarith only [h, hnonneg]
  have hupper := mul_le_mul_of_nonneg_right hTupper
    (by positivity : (0 : ℝ) ≤ ((m / T : ℕ) : ℝ) + 1)
  change x ≤ 2 * (((m / T : ℕ) : ℝ) + 2)
  by_contra h
  have hbad : 2 * (((m / T : ℕ) : ℝ) + 2) < x := lt_of_not_ge h
  have hnprod : 0 < (n : ℝ) * x ^ 3 := by positivity
  have hmul := mul_lt_mul_of_pos_right hbad hnprod
  nlinarith only [hdivR, hx4m, hupper, hmul, hnprod]

theorem dtsIntegerScale_geometric_tail_lt {n m : ℕ} {x : ℝ}
    (hn : 1 ≤ n) (hx : 120 ≤ x) (hx4m : x ^ 4 * (n : ℝ) = (m : ℝ)) :
    x * ((3 : ℝ) / 4) ^ (m / dtsIntegerScale n x) < (1 : ℝ) / 100 := by
  have hbound := dtsIntegerScale_quotient_bound hn hx hx4m
  have hr : 58 ≤ m / dtsIntegerScale n x := by
    have hrR : (58 : ℝ) ≤ ((m / dtsIntegerScale n x : ℕ) : ℝ) := by linarith
    exact_mod_cast hrR
  calc
    x * ((3 : ℝ) / 4) ^ (m / dtsIntegerScale n x) ≤
        sidonTailEnvelope (m / dtsIntegerScale n x) :=
      mul_le_mul_of_nonneg_right hbound (by positivity)
    _ < (1 : ℝ) / 100 := sidonTailEnvelope_lt hr

theorem dtsIntegerScale_tail_lt {n m : ℕ} {x : ℝ}
    (hn : 1 ≤ n) (hx : 120 ≤ x) (hx4m : x ^ 4 * (n : ℝ) = (m : ℝ)) :
    29 * (dtsIntegerScale n x : ℝ) / (n : ℝ) *
        ((3 : ℝ) / 4) ^ (m / dtsIntegerScale n x) < (87 : ℝ) / 200 * x ^ 2 := by
  have hxpos : 0 < x := by linarith
  have hsmall := dtsIntegerScale_geometric_tail_lt hn hx hx4m
  have hT := dtsIntegerScale_div_upper hn hx
  have hp : 0 ≤ ((3 : ℝ) / 4) ^ (m / dtsIntegerScale n x) := by positivity
  have hupper := mul_le_mul_of_nonneg_right hT
    (mul_nonneg (by norm_num : (0 : ℝ) ≤ 29) hp)
  have hmul := mul_lt_mul_of_pos_left hsmall
    (by positivity : (0 : ℝ) < ((87 : ℝ) / 2) * x ^ 2)
  nlinarith only [hupper, hmul]

theorem dtsScaleError_nonneg (n m : ℕ) (x : ℝ) : 0 ≤ dtsScaleError n m x := by
  unfold dtsScaleError
  positivity

theorem dtsScaleError_lt_half {n m : ℕ} {x : ℝ}
    (hn : 1 ≤ n) (hx : 120 ≤ x) (hx4m : x ^ 4 * (n : ℝ) = (m : ℝ)) :
    dtsScaleError n m x < x ^ 2 / 2 := by
  have hnpos : (0 : ℝ) < (n : ℝ) := by exact_mod_cast (show 0 < n by omega)
  have hnR : (1 : ℝ) ≤ (n : ℝ) := by exact_mod_cast hn
  have hinv : (1 : ℝ) / (n : ℝ) ≤ 1 := by
    apply (div_le_iff₀ hnpos).mpr
    simpa only [one_mul] using hnR
  have htail := dtsIntegerScale_tail_lt hn hx hx4m
  have hsq : (16 : ℝ) ≤ x ^ 2 := by nlinarith [sq_nonneg (x - 4)]
  unfold dtsScaleError
  nlinarith only [hinv, htail, hsq]

/-- The actual finite window has m+1 integer points. Its extra 1/n is
absorbed in `dtsScaleError`, leaving the principal variable x^4=m/n. -/
theorem dtsIntegerScale_cost_le {n m : ℕ} {x : ℝ}
    (hn : 1 ≤ n) (hx : 0 ≤ x) (hx4m : x ^ 4 * (n : ℝ) = (m : ℝ)) :
    (((m + 1 : ℕ) : ℝ) + (2 : ℝ) / 3 * ((dtsIntegerScale n x : ℝ) - 1) +
      29 * (dtsIntegerScale n x : ℝ) *
        ((3 : ℝ) / 4) ^ (((m + 1) - 1) / dtsIntegerScale n x)) / (n : ℝ) ≤
      x ^ 4 + sidonGamma * x ^ 3 + dtsScaleError n m x := by
  have hnpos : (0 : ℝ) < (n : ℝ) := by exact_mod_cast (show 0 < n by omega)
  have hb := dtsIntegerScale_boundary_le hn hx hx4m
  simp only [Nat.add_sub_cancel, Nat.cast_add, Nat.cast_one]
  have hid :
      ((m : ℝ) + 1 + (2 : ℝ) / 3 * ((dtsIntegerScale n x : ℝ) - 1) +
        29 * (dtsIntegerScale n x : ℝ) * ((3 : ℝ) / 4) ^ (m / dtsIntegerScale n x)) /
          (n : ℝ) =
      ((m : ℝ) + (2 : ℝ) / 3 * ((dtsIntegerScale n x : ℝ) - 1)) / (n : ℝ) +
        dtsScaleError n m x := by
    unfold dtsScaleError
    field_simp [ne_of_gt hnpos]
    <;> ring
  rw [hid]
  exact add_le_add_right hb _

end Sidon30

end
