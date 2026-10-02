import Sidon30.IntegerScaleAndTail

/-! Integer scales and explicit tails for the bounded-multiplicity transfer. -/

noncomputable section

namespace Sidon30

def gThinIntegerScale (g : ℕ) (x : ℝ) : ℕ :=
  Nat.ceil (Real.sqrt 2 * x ^ 3 / (g : ℝ))

theorem gThinIntegerScale_pos {g : ℕ} {x : ℝ}
    (hg : 1 ≤ g) (hx : 0 < x) : 1 ≤ gThinIntegerScale g x := by
  have hgpos : (0 : ℝ) < (g : ℝ) := by exact_mod_cast (show 0 < g by omega)
  apply Nat.one_le_ceil_iff.mpr
  positivity

theorem gThinIntegerScale_lower {g : ℕ} (hg : 1 ≤ g) (x : ℝ) :
    Real.sqrt 2 * x ^ 3 ≤ (g : ℝ) * (gThinIntegerScale g x : ℝ) := by
  have hgpos : (0 : ℝ) < (g : ℝ) := by exact_mod_cast (show 0 < g by omega)
  have hceil : Real.sqrt 2 * x ^ 3 / (g : ℝ) ≤ (gThinIntegerScale g x : ℝ) :=
    Nat.le_ceil _
  have h := (div_le_iff₀ hgpos).mp hceil
  simpa only [mul_comm] using h

theorem gThinIntegerScale_lt {g : ℕ} {x : ℝ}
    (hg : 1 ≤ g) (hx : 0 ≤ x) :
    (g : ℝ) * (gThinIntegerScale g x : ℝ) < Real.sqrt 2 * x ^ 3 + (g : ℝ) := by
  have hgpos : (0 : ℝ) < (g : ℝ) := by exact_mod_cast (show 0 < g by omega)
  have hceil : (gThinIntegerScale g x : ℝ) < Real.sqrt 2 * x ^ 3 / (g : ℝ) + 1 :=
    Nat.ceil_lt_add_one (by positivity)
  have hmul := mul_lt_mul_of_pos_left hceil hgpos
  have hid : (g : ℝ) * (Real.sqrt 2 * x ^ 3 / (g : ℝ) + 1) =
      Real.sqrt 2 * x ^ 3 + (g : ℝ) := by
    field_simp [ne_of_gt hgpos]
    <;> ring
  rw [hid] at hmul
  exact hmul

theorem gThinIntegerScale_sub_one_le {g : ℕ} {x : ℝ}
    (hg : 1 ≤ g) (hx : 0 ≤ x) :
    (g : ℝ) * ((gThinIntegerScale g x : ℝ) - 1) ≤ Real.sqrt 2 * x ^ 3 := by
  have h := gThinIntegerScale_lt hg hx
  nlinarith

theorem gThinIntegerScale_upper {g : ℕ} {x : ℝ}
    (hg : 1 ≤ g) (hx : 120 ≤ x) (hgx : (g : ℝ) ≤ x ^ 2) :
    (g : ℝ) * (gThinIntegerScale g x : ℝ) ≤ (3 : ℝ) / 2 * x ^ 3 := by
  have hxpos : 0 < x := by linarith
  have hs : Real.sqrt 2 ≤ (17 : ℝ) / 12 := by
    apply (Real.sqrt_le_left (by norm_num : (0 : ℝ) ≤ 17 / 12)).mpr
    norm_num
  have hmul := mul_le_mul_of_nonneg_right hs (pow_nonneg hxpos.le 3)
  have hxlarge := mul_le_mul_of_nonneg_right (show (12 : ℝ) ≤ x by linarith)
    (sq_nonneg x)
  have hceil := gThinIntegerScale_lt hg hxpos.le
  nlinarith

theorem gThinIntegerScale_diagonal_le {g : ℕ} {x : ℝ}
    (hg : 1 ≤ g) (hx : 0 < x) :
    rampDiagonal (gThinIntegerScale g x) / (g : ℝ) ≤ sidonGamma / x ^ 3 := by
  have hT := gThinIntegerScale_pos hg hx
  have hTpos : (0 : ℝ) < (gThinIntegerScale g x : ℝ) := by
    exact_mod_cast (show 0 < gThinIntegerScale g x by omega)
  have hgpos : (0 : ℝ) < (g : ℝ) := by exact_mod_cast (show 0 < g by omega)
  have hx3pos : 0 < x ^ 3 := pow_pos hx 3
  have hs : (Real.sqrt 2) ^ 2 = (2 : ℝ) := Real.sq_sqrt (by norm_num)
  have hprod : 4 * x ^ 3 ≤
      2 * Real.sqrt 2 * ((g : ℝ) * (gThinIntegerScale g x : ℝ)) := by
    calc
      4 * x ^ 3 = (2 * Real.sqrt 2) * (Real.sqrt 2 * x ^ 3) := by
        calc
          _ = 2 * (Real.sqrt 2) ^ 2 * x ^ 3 := by rw [hs]; ring
          _ = _ := by ring
      _ ≤ (2 * Real.sqrt 2) * ((g : ℝ) * (gThinIntegerScale g x : ℝ)) :=
        mul_le_mul_of_nonneg_left (gThinIntegerScale_lower hg x) (by positivity)
  calc
    rampDiagonal (gThinIntegerScale g x) / (g : ℝ) ≤
        (4 / (3 * (gThinIntegerScale g x : ℝ))) / (g : ℝ) :=
      div_le_div_of_nonneg_right (rampDiagonal_le hT) hgpos.le
    _ = 4 / (3 * ((g : ℝ) * (gThinIntegerScale g x : ℝ))) := by
      field_simp [ne_of_gt hgpos, ne_of_gt hTpos]
      <;> ring
    _ ≤ sidonGamma / x ^ 3 := by
      apply (div_le_div_iff₀ (by positivity :
        0 < 3 * ((g : ℝ) * (gThinIntegerScale g x : ℝ))) hx3pos).mpr
      unfold sidonGamma
      nlinarith [hprod]

theorem gThinIntegerScale_boundary_le {g N : ℕ} {x : ℝ}
    (hg : 1 ≤ g) (hx : 0 ≤ x) (hN : x ^ 4 = (g : ℝ) * (N : ℝ)) :
    (g : ℝ) * ((N : ℝ) + (2 : ℝ) / 3 * ((gThinIntegerScale g x : ℝ) - 1)) ≤
      x ^ 4 + sidonGamma * x ^ 3 := by
  have h := gThinIntegerScale_sub_one_le hg hx
  unfold sidonGamma
  nlinarith

/-- The original spatial quotient is retained after multiplying the scale by g. -/
theorem gThinIntegerScale_quotient_bound {g N : ℕ} {x : ℝ}
    (hg : 1 ≤ g) (hN : 1 ≤ N) (hx : 120 ≤ x)
    (hx4 : x ^ 4 = (g : ℝ) * (N : ℝ)) (hgx : (g : ℝ) ≤ x ^ 2) :
    x ≤ 2 * ((((N - 1) / gThinIntegerScale g x : ℕ) : ℝ) + 2) := by
  have hxpos : 0 < x := by linarith
  have hgpos : (0 : ℝ) < (g : ℝ) := by exact_mod_cast (show 0 < g by omega)
  let T := gThinIntegerScale g x
  have hT : 1 ≤ T := gThinIntegerScale_pos hg hxpos
  have hdiv : N - 1 < T * ((N - 1) / T + 1) := by
    have hrem := Nat.mod_lt (N - 1) (show 0 < T by omega)
    have hid := Nat.mod_add_div (N - 1) T
    nlinarith
  have hdivR : ((N - 1 : ℕ) : ℝ) <
      (T : ℝ) * ((((N - 1) / T : ℕ) : ℝ) + 1) := by exact_mod_cast hdiv
  rw [Nat.cast_sub hN, Nat.cast_one] at hdivR
  have hdivg := mul_lt_mul_of_pos_left hdivR hgpos
  have hscaled : x ^ 4 - (g : ℝ) <
      ((g : ℝ) * (T : ℝ)) * ((((N - 1) / T : ℕ) : ℝ) + 1) := by
    nlinarith only [hdivg, hx4]
  have hTupper : (g : ℝ) * (T : ℝ) ≤ 2 * x ^ 3 := by
    have h := gThinIntegerScale_upper hg hx hgx
    have hp := pow_nonneg hxpos.le 3
    dsimp [T]
    linarith
  have hupper := mul_le_mul_of_nonneg_right hTupper
    (by positivity : (0 : ℝ) ≤ (((N - 1) / T : ℕ) : ℝ) + 1)
  change x ≤ 2 * ((((N - 1) / T : ℕ) : ℝ) + 2)
  by_contra h
  have hbad : 2 * ((((N - 1) / T : ℕ) : ℝ) + 2) < x := lt_of_not_ge h
  have hmul := mul_lt_mul_of_pos_right hbad (pow_pos hxpos 3)
  have hcube := mul_le_mul_of_nonneg_right (show (1 : ℝ) ≤ x by linarith)
    (sq_nonneg x)
  nlinarith only [hscaled, hupper, hmul, hgx, hcube, sq_nonneg x]

theorem gThinIntegerScale_geometric_tail_lt {g N : ℕ} {x : ℝ}
    (hg : 1 ≤ g) (hN : 1 ≤ N) (hx : 120 ≤ x)
    (hx4 : x ^ 4 = (g : ℝ) * (N : ℝ)) (hgx : (g : ℝ) ≤ x ^ 2) :
    x * ((3 : ℝ) / 4) ^ ((N - 1) / gThinIntegerScale g x) < (1 : ℝ) / 100 := by
  have hbound := gThinIntegerScale_quotient_bound hg hN hx hx4 hgx
  have hr : 58 ≤ (N - 1) / gThinIntegerScale g x := by
    have hrR : (58 : ℝ) ≤ (((N - 1) / gThinIntegerScale g x : ℕ) : ℝ) := by
      linarith
    exact_mod_cast hrR
  calc
    x * ((3 : ℝ) / 4) ^ ((N - 1) / gThinIntegerScale g x) ≤
        sidonTailEnvelope ((N - 1) / gThinIntegerScale g x) :=
      mul_le_mul_of_nonneg_right hbound (by positivity)
    _ < (1 : ℝ) / 100 := sidonTailEnvelope_lt hr

theorem gThinIntegerScale_tail_lt_half {g N : ℕ} {x : ℝ}
    (hg : 1 ≤ g) (hN : 1 ≤ N) (hx : 120 ≤ x)
    (hx4 : x ^ 4 = (g : ℝ) * (N : ℝ)) (hgx : (g : ℝ) ≤ x ^ 2) :
    29 * (g : ℝ) * (gThinIntegerScale g x : ℝ) *
        ((3 : ℝ) / 4) ^ ((N - 1) / gThinIntegerScale g x) < x ^ 2 / 2 := by
  have hxpos : 0 < x := by linarith
  have hsmall := gThinIntegerScale_geometric_tail_lt hg hN hx hx4 hgx
  have hT := gThinIntegerScale_upper hg hx hgx
  have hp : 0 ≤ ((3 : ℝ) / 4) ^ ((N - 1) / gThinIntegerScale g x) := by positivity
  have hupper := mul_le_mul_of_nonneg_right hT
    (mul_nonneg (by norm_num : (0 : ℝ) ≤ 29) hp)
  have hmul := mul_lt_mul_of_pos_left hsmall
    (by positivity : (0 : ℝ) < ((87 : ℝ) / 2) * x ^ 2)
  have hstrong : 29 * (g : ℝ) * (gThinIntegerScale g x : ℝ) *
      ((3 : ℝ) / 4) ^ ((N - 1) / gThinIntegerScale g x) <
      (87 : ℝ) / 200 * x ^ 2 := by
    nlinarith only [hupper, hmul]
  have hx2pos := pow_pos hxpos 2
  nlinarith

end Sidon30

end
