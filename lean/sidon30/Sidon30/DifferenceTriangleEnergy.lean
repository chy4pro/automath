import Sidon30.DifferenceTriangleStatement
import Sidon30.TransferCertificate

/-!
Difference triangle sets share one positive-difference budget across rows.
The sigma index records the row of a pair; no cross-row energy is introduced.
The finite boundary certificate is used on the actual (m+1)-point window.
-/

noncomputable section
open scoped BigOperators

namespace Sidon30

/-- Positive pairs with their row index retained. -/
def dtsPositivePairs {n : ℕ} (X : Fin n → Finset ℕ) :
    Finset (Σ _i : Fin n, ℕ × ℕ) :=
  Finset.univ.sigma (fun i => positivePairs (X i))

@[simp]
theorem mem_dtsPositivePairs {n : ℕ} {X : Fin n → Finset ℕ}
    {p : Σ _i : Fin n, ℕ × ℕ} :
    p ∈ dtsPositivePairs X ↔ p.2 ∈ positivePairs (X p.1) := by
  simp only [dtsPositivePairs, Finset.mem_sigma, Finset.mem_univ, true_and]

/-- The defining global uniqueness applies only to pairs within one row. -/
theorem dts_positiveDifference_injOn {n k m : ℕ} {X : Fin n → Finset ℕ}
    (hX : IsDifferenceTriangleSet n k m X) :
    Set.InjOn (fun p : Σ _i : Fin n, ℕ × ℕ => p.2.1 - p.2.2)
      (↑(dtsPositivePairs X) : Set (Σ _i : Fin n, ℕ × ℕ)) := by
  rintro ⟨i, p⟩ hp ⟨j, q⟩ hq heq
  change p.1 - p.2 = q.1 - q.2 at heq
  rcases mem_positivePairs.mp (mem_dtsPositivePairs.mp hp) with ⟨hpa, hpb, hpord⟩
  rcases mem_positivePairs.mp (mem_dtsPositivePairs.mp hq) with ⟨hqa, hqb, hqord⟩
  obtain ⟨hij, hac, hbd⟩ := hX.2 i j p.1 hpa p.2 hpb q.1 hqa q.2 hqb
    hpord hqord heq
  have hpq : p = q := Prod.ext hac hbd
  subst j
  subst q
  rfl

theorem dts_positivePairSum_eq_sigma {n : ℕ} (X : Fin n → Finset ℕ)
    (w : ℕ → ℝ) :
    (∑ p ∈ dtsPositivePairs X, w (p.2.1 - p.2.2)) =
      ∑ i : Fin n, ∑ p ∈ positivePairs (X i), w (p.1 - p.2) := by
  unfold dtsPositivePairs
  rw [Finset.sum_sigma]

/-- There is a single nonnegative difference sum, not one copy per row. -/
theorem dts_positivePairSum_le_of_support {n k m : ℕ}
    {X : Fin n → Finset ℕ} {D : Finset ℕ}
    (hX : IsDifferenceTriangleSet n k m X) (w : ℕ → ℝ)
    (hcover : ∀ i : Fin n, ∀ p ∈ positivePairs (X i),
      w (p.1 - p.2) ≠ 0 → p.1 - p.2 ∈ D)
    (hnonneg : ∀ d ∈ D, 0 ≤ w d) :
    (∑ i : Fin n, ∑ p ∈ positivePairs (X i), w (p.1 - p.2)) ≤
      ∑ d ∈ D, w d := by
  let P := (dtsPositivePairs X).filter (fun p => p.2.1 - p.2.2 ∈ D)
  have hfilter :
      (∑ p ∈ P, w (p.2.1 - p.2.2)) =
        ∑ p ∈ dtsPositivePairs X, w (p.2.1 - p.2.2) := by
    dsimp [P]
    exact Finset.sum_filter_of_ne
      (fun p hp hn => hcover p.1 p.2 (mem_dtsPositivePairs.mp hp) hn)
  have hinj : Set.InjOn (fun p : Σ _i : Fin n, ℕ × ℕ => p.2.1 - p.2.2)
      (↑P : Set (Σ _i : Fin n, ℕ × ℕ)) := by
    intro p hp q hq hpq
    exact dts_positiveDifference_injOn hX
      (Finset.mem_filter.mp hp).1 (Finset.mem_filter.mp hq).1 hpq
  have himap : P.image (fun p => p.2.1 - p.2.2) ⊆ D := by
    intro d hd
    obtain ⟨p, hp, rfl⟩ := Finset.mem_image.mp hd
    exact (Finset.mem_filter.mp hp).2
  have himage :
      (∑ d ∈ P.image (fun p => p.2.1 - p.2.2), w d) =
        ∑ p ∈ P, w (p.2.1 - p.2.2) := Finset.sum_image hinj
  calc
    (∑ i : Fin n, ∑ p ∈ positivePairs (X i), w (p.1 - p.2)) =
        ∑ p ∈ dtsPositivePairs X, w (p.2.1 - p.2.2) :=
      (dts_positivePairSum_eq_sigma X w).symm
    _ = ∑ p ∈ P, w (p.2.1 - p.2.2) := hfilter.symm
    _ = ∑ d ∈ P.image (fun p => p.2.1 - p.2.2), w d := himage.symm
    _ ≤ ∑ d ∈ D, w d :=
      Finset.sum_le_sum_of_subset_of_nonneg himap (fun d hd _ => hnonneg d hd)

/-- Pair counting obtained from the exact ordered-pair decomposition at weight one. -/
theorem two_mul_positivePairSum_one (A : Finset ℕ) :
    2 * (∑ _p ∈ positivePairs A, (1 : ℝ)) =
      (A.card : ℝ) * ((A.card : ℝ) - 1) := by
  have heq := orderedPairEnergy_eq A (fun _ : ℤ => (1 : ℝ)) (fun _ => rfl)
  have hfull : orderedPairEnergy A (fun _ : ℤ => (1 : ℝ)) = (A.card : ℝ) ^ 2 := by
    simp only [orderedPairEnergy, Finset.sum_const, nsmul_eq_mul, mul_one]
    ring
  rw [hfull] at heq
  nlinarith only [heq]

/-- All n*k*(k+1)/2 positive within-row differences lie in {1,...,m}. -/
theorem dts_scope_count {n k m : ℕ} {X : Fin n → Finset ℕ}
    (hX : IsDifferenceTriangleSet n k m X) :
    (n : ℝ) * (k : ℝ) * ((k : ℝ) + 1) / 2 ≤ (m : ℝ) := by
  have hrow : ∀ i : Fin n,
      (∑ _p ∈ positivePairs (X i), (1 : ℝ)) = (k : ℝ) * ((k : ℝ) + 1) / 2 := by
    intro i
    have h := two_mul_positivePairSum_one (X i)
    rw [(hX.1 i).1] at h
    simp only [Nat.cast_add, Nat.cast_one] at h
    nlinarith only [h]
  have hcount := dts_positivePairSum_le_of_support
    (D := Finset.Icc 1 m) hX (fun _ => (1 : ℝ))
    (by
      intro i p hp _hn
      rcases mem_positivePairs.mp hp with ⟨hpa, hpb, hpord⟩
      have hpam : p.1 ≤ m := (Finset.mem_Icc.mp ((hX.1 i).2.2 hpa)).2
      apply Finset.mem_Icc.mpr
      constructor <;> omega)
    (by intro d _hd; norm_num)
  have hsum : (∑ i : Fin n, ∑ _p ∈ positivePairs (X i), (1 : ℝ)) =
      (n : ℝ) * ((k : ℝ) * ((k : ℝ) + 1) / 2) := by
    simp_rw [hrow]
    simp only [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul]
  calc
    (n : ℝ) * (k : ℝ) * ((k : ℝ) + 1) / 2 =
        ∑ i : Fin n, ∑ _p ∈ positivePairs (X i), (1 : ℝ) := by rw [hsum]; ring
    _ ≤ ∑ _d ∈ Finset.Icc 1 m, (1 : ℝ) := hcount
    _ = (m : ℝ) := by simp [Nat.card_Icc]

/-- Each row fits the actual m+1 point window, including both endpoints. -/
theorem dts_row_subset_range {n k m : ℕ} {X : Fin n → Finset ℕ}
    (hX : IsDifferenceTriangleSet n k m X) (i : Fin n) :
    X i ⊆ Finset.range (m + 1) := by
  intro a ha
  have ham : a ≤ m := (Finset.mem_Icc.mp ((hX.1 i).2.2 ha)).2
  apply Finset.mem_range.mpr
  omega

/-- Exact diagonal n*(k+1), with one shared positive-difference lattice budget. -/
theorem dts_rampEnergy_le {n k m T : ℕ} {X : Fin n → Finset ℕ}
    (hX : IsDifferenceTriangleSet n k m X) (hT : 1 ≤ T) :
    (∑ i : Fin n, orderedPairEnergy (X i) (rampCorrelation T)) ≤
      1 + rampDiagonal T * ((n : ℝ) * ((k : ℝ) + 1) - 1) := by
  have hpairs := dts_positivePairSum_le_of_support
    (D := Finset.Icc 1 (T - 1)) hX (fun d => rampCorrelation T (d : ℤ))
    (by
      intro i p hp hnz
      have hpos := (mem_positivePairs.mp hp).2.2
      apply Finset.mem_Icc.mpr
      constructor
      · omega
      · by_contra h
        have hlarge : T ≤ p.1 - p.2 := by omega
        apply hnz
        apply rampCorrelation_eq_zero_of_abs_le
        rw [abs_of_nonneg (by positivity : (0 : ℤ) ≤ ((p.1 - p.2 : ℕ) : ℤ))]
        exact_mod_cast hlarge)
    (by intro d _hd; exact rampCorrelation_nonneg T (d : ℤ))
  have hmass : 2 * (∑ d ∈ Finset.Icc 1 (T - 1), rampCorrelation T (d : ℤ)) =
      1 - rampDiagonal T := by
    rw [← sum_pos_rampCorrelation_eq_nat hT]
    exact two_mul_sum_pos_rampCorrelation hT
  have hsplit :
      (∑ i : Fin n, orderedPairEnergy (X i) (rampCorrelation T)) =
      (n : ℝ) * ((k : ℝ) + 1) * rampDiagonal T +
        2 * (∑ i : Fin n, ∑ p ∈ positivePairs (X i),
          rampCorrelation T ((p.1 - p.2 : ℕ) : ℤ)) := by
    calc
      _ = ∑ i : Fin n, (((k : ℝ) + 1) * rampDiagonal T +
          2 * ∑ p ∈ positivePairs (X i), rampCorrelation T ((p.1 - p.2 : ℕ) : ℤ)) := by
        apply Finset.sum_congr rfl
        intro i _hi
        rw [orderedPairEnergy_eq (X i) (rampCorrelation T) (rampCorrelation_neg T),
          rampCorrelation_zero hT, (hX.1 i).1]
        simp only [Nat.cast_add, Nat.cast_one]
      _ = (∑ _i : Fin n, ((k : ℝ) + 1) * rampDiagonal T) +
          2 * (∑ i : Fin n, ∑ p ∈ positivePairs (X i),
            rampCorrelation T ((p.1 - p.2 : ℕ) : ℤ)) := by
        rw [Finset.sum_add_distrib, Finset.mul_sum]
      _ = _ := by
        simp only [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul]
        ring
  rw [hsplit]
  nlinarith only [hpairs, hmass]

/-- Sum the actual finite signed-capacity inequality over rows separately. -/
theorem dts_sum_capacity {n k m T : ℕ} {X : Fin n → Finset ℕ}
    (hX : IsDifferenceTriangleSet n k m X) (hT : 1 ≤ T) :
    (n : ℝ) * ((k : ℝ) + 1) ^ 2 ≤
      ((m : ℝ) + 1 + (2 : ℝ) / 3 * ((T : ℝ) - 1) +
        29 * (T : ℝ) * ((3 : ℝ) / 4) ^ (m / T)) *
      (∑ i : Fin n, orderedPairEnergy (X i) (rampCorrelation T)) := by
  let C : ℝ := (m : ℝ) + 1 + (2 : ℝ) / 3 * ((T : ℝ) - 1) +
    29 * (T : ℝ) * ((3 : ℝ) / 4) ^ (m / T)
  change (n : ℝ) * ((k : ℝ) + 1) ^ 2 ≤
    C * (∑ i : Fin n, orderedPairEnergy (X i) (rampCorrelation T))
  calc
    (n : ℝ) * ((k : ℝ) + 1) ^ 2 = ∑ _i : Fin n, ((k : ℝ) + 1) ^ 2 := by
      simp only [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul]
    _ ≤ ∑ i : Fin n, C * orderedPairEnergy (X i) (rampCorrelation T) := by
      apply Finset.sum_le_sum
      intro i _hi
      have h := ramp_card_sq_le_certificate (m + 1) T (X i) (by omega) hT
        (dts_row_subset_range hX i)
      simpa only [C, (hX.1 i).1, Nat.cast_add, Nat.cast_one, Nat.add_sub_cancel] using h
    _ = C * (∑ i : Fin n, orderedPairEnergy (X i) (rampCorrelation T)) :=
      (Finset.mul_sum _ _ _).symm

/-- Normalized finite certificate. The cost retains m+1; only the harmless
negative diagonal correction is dropped before the later scalar step. -/
theorem dts_finite_certificate {n k m T : ℕ} {X : Fin n → Finset ℕ}
    (hn : 1 ≤ n) (hT : 1 ≤ T) (hX : IsDifferenceTriangleSet n k m X) :
    ((k : ℝ) + 1) ^ 2 ≤
      (((m : ℝ) + 1 + (2 : ℝ) / 3 * ((T : ℝ) - 1) +
        29 * (T : ℝ) * ((3 : ℝ) / 4) ^ (m / T)) / (n : ℝ)) *
      (1 + (n : ℝ) * rampDiagonal T * ((k : ℝ) + 1)) := by
  let C : ℝ := (m : ℝ) + 1 + (2 : ℝ) / 3 * ((T : ℝ) - 1) +
    29 * (T : ℝ) * ((3 : ℝ) / 4) ^ (m / T)
  have hnpos : (0 : ℝ) < (n : ℝ) := by exact_mod_cast (show 0 < n by omega)
  have hTpred : 0 ≤ (T : ℝ) - 1 := by
    have hTr : (1 : ℝ) ≤ (T : ℝ) := by exact_mod_cast hT
    linarith
  have hC : 0 ≤ C := by dsimp [C]; positivity
  have henergy : (∑ i : Fin n, orderedPairEnergy (X i) (rampCorrelation T)) ≤
      1 + (n : ℝ) * rampDiagonal T * ((k : ℝ) + 1) := by
    have he := dts_rampEnergy_le hX hT
    have ha := rampDiagonal_nonneg T
    nlinarith only [he, ha]
  have hraw : (n : ℝ) * ((k : ℝ) + 1) ^ 2 ≤
      C * (1 + (n : ℝ) * rampDiagonal T * ((k : ℝ) + 1)) :=
    (dts_sum_capacity hX hT).trans (mul_le_mul_of_nonneg_left henergy hC)
  change ((k : ℝ) + 1) ^ 2 ≤
    (C / (n : ℝ)) * (1 + (n : ℝ) * rampDiagonal T * ((k : ℝ) + 1))
  calc
    ((k : ℝ) + 1) ^ 2 ≤
        (C * (1 + (n : ℝ) * rampDiagonal T * ((k : ℝ) + 1))) / (n : ℝ) := by
      apply (le_div_iff₀ hnpos).mpr
      calc
        ((k : ℝ) + 1) ^ 2 * (n : ℝ) = (n : ℝ) * ((k : ℝ) + 1) ^ 2 := by ring
        _ ≤ _ := hraw
    _ = _ := by ring

end Sidon30

end
