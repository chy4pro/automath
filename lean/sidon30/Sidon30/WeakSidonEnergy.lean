import Sidon30.WeakSidonStructure
import Sidon30.SidonRampEnergy

/-!
The weak-Sidon ordered-pair energy bound, including the diagonal.
The extra representations are charged to distinct middle points of
three-term arithmetic progressions; the remaining differences are unique.
-/

noncomputable section
open scoped BigOperators

namespace Sidon30

/-- Weighted base pairs are bounded by the full nonnegative difference sum. -/
theorem isWeakSidon_basePairSum_le_of_support {A D : Finset ℕ}
    (hA : IsWeakSidon A) (w : ℕ → ℝ)
    (hcover : ∀ p ∈ positivePairs A, w (p.1 - p.2) ≠ 0 → p.1 - p.2 ∈ D)
    (hnonneg : ∀ d ∈ D, 0 ≤ w d) :
    (∑ p ∈ weakBasePairs A, w (p.1 - p.2)) ≤ ∑ d ∈ D, w d := by
  let P := (weakBasePairs A).filter (fun p => p.1 - p.2 ∈ D)
  have hfilter :
      (∑ p ∈ P, w (p.1 - p.2)) = ∑ p ∈ weakBasePairs A, w (p.1 - p.2) := by
    dsimp [P]
    exact Finset.sum_filter_of_ne
      (fun p hp hn => hcover p (weakBasePairs_subset A hp) hn)
  have hinj : Set.InjOn (fun p : ℕ × ℕ => p.1 - p.2)
      (↑P : Set (ℕ × ℕ)) := by
    intro p hp q hq hpq
    exact weakBasePairs_difference_injOn hA
      (Finset.mem_filter.mp hp).1 (Finset.mem_filter.mp hq).1 hpq
  have himap : P.image (fun p => p.1 - p.2) ⊆ D := by
    intro d hd
    obtain ⟨p, hp, rfl⟩ := Finset.mem_image.mp hd
    exact (Finset.mem_filter.mp hp).2
  have himage :
      (∑ d ∈ P.image (fun p => p.1 - p.2), w d) =
        ∑ p ∈ P, w (p.1 - p.2) := Finset.sum_image hinj
  calc
    (∑ p ∈ weakBasePairs A, w (p.1 - p.2)) = ∑ p ∈ P, w (p.1 - p.2) :=
      hfilter.symm
    _ = ∑ d ∈ P.image (fun p => p.1 - p.2), w d := himage.symm
    _ ≤ ∑ d ∈ D, w d :=
      Finset.sum_le_sum_of_subset_of_nonneg himap (fun d hd _ => hnonneg d hd)

/-- Each extra pair costs at most the diagonal value, and their middle
points avoid at least one endpoint of the nonempty set. -/
theorem isWeakSidon_extraPairSum_le {A : Finset ℕ} (hA : IsWeakSidon A)
    (hcard : 1 ≤ A.card) (w : ℕ → ℝ) (a : ℝ) (ha : 0 ≤ a)
    (hbound : ∀ d, w d ≤ a) :
    (∑ p ∈ weakExtraPairs A, w (p.1 - p.2)) ≤ a * ((A.card : ℝ) - 1) := by
  have hcount : ((weakExtraPairs A).card : ℝ) ≤ (A.card : ℝ) - 1 := by
    have hn := weakExtraPairs_card_le_sub_one hA hcard
    have hr : ((weakExtraPairs A).card : ℝ) ≤ ((A.card - 1 : ℕ) : ℝ) := by
      exact_mod_cast hn
    simpa only [Nat.cast_sub hcard, Nat.cast_one] using hr
  calc
    (∑ p ∈ weakExtraPairs A, w (p.1 - p.2)) ≤ ∑ _p ∈ weakExtraPairs A, a := by
      apply Finset.sum_le_sum
      intro p _hp
      exact hbound (p.1 - p.2)
    _ = a * ((weakExtraPairs A).card : ℝ) := by
      simp only [Finset.sum_const, nsmul_eq_mul]
      ring
    _ ≤ a * ((A.card : ℝ) - 1) := mul_le_mul_of_nonneg_left hcount ha

/-- The exact base/extra decomposition gives the weak-Sidon positive-pair bound. -/
theorem isWeakSidon_positivePairSum_le_of_support {A D : Finset ℕ}
    (hA : IsWeakSidon A) (hcard : 1 ≤ A.card) (w : ℕ → ℝ)
    (a : ℝ) (ha : 0 ≤ a)
    (hcover : ∀ p ∈ positivePairs A, w (p.1 - p.2) ≠ 0 → p.1 - p.2 ∈ D)
    (hnonneg : ∀ d ∈ D, 0 ≤ w d) (hbound : ∀ d, w d ≤ a) :
    (∑ p ∈ positivePairs A, w (p.1 - p.2)) ≤
      (∑ d ∈ D, w d) + a * ((A.card : ℝ) - 1) := by
  have hsplit :
      (∑ p ∈ weakBasePairs A, w (p.1 - p.2)) +
        (∑ p ∈ weakExtraPairs A, w (p.1 - p.2)) =
      ∑ p ∈ positivePairs A, w (p.1 - p.2) := by
    exact Finset.sum_sdiff (weakExtraPairs_subset A)
  rw [← hsplit]
  exact add_le_add (isWeakSidon_basePairSum_le_of_support hA w hcover hnonneg)
    (isWeakSidon_extraPairSum_le hA hcard w a ha hbound)

/-- Normalized even kernels bounded by their nonnegative diagonal value
have weak-Sidon energy at most `1 + 3 a (card A - 1)`. -/
theorem isWeakSidon_orderedPairEnergy_le_normalized {A D : Finset ℕ}
    (hA : IsWeakSidon A) (hcard : 1 ≤ A.card) (f : ℤ → ℝ) (a : ℝ)
    (ha : 0 ≤ a) (heven : ∀ d : ℤ, f (-d) = f d)
    (hcover : ∀ p ∈ positivePairs A,
      f ((p.1 - p.2 : ℕ) : ℤ) ≠ 0 → p.1 - p.2 ∈ D)
    (hnonneg : ∀ d ∈ D, 0 ≤ f (d : ℤ)) (hbound : ∀ d : ℕ, f (d : ℤ) ≤ a)
    (hzero : f 0 = a) (hmass : 2 * (∑ d ∈ D, f (d : ℤ)) = 1 - a) :
    orderedPairEnergy A f ≤ 1 + 3 * a * ((A.card : ℝ) - 1) := by
  have hp := isWeakSidon_positivePairSum_le_of_support hA hcard
    (fun d => f (d : ℤ)) a ha hcover hnonneg hbound
  rw [orderedPairEnergy_eq A f heven, hzero]
  nlinarith

/-- The actual normalized ramp correlation has the required weak-Sidon
energy bound. Nonemptiness is explicit, including the singleton case. -/
theorem isWeakSidon_rampEnergy_le {A : Finset ℕ} {T : ℕ}
    (hA : IsWeakSidon A) (hT : 1 ≤ T) (hcard : 1 ≤ A.card) :
    orderedPairEnergy A (rampCorrelation T) ≤
      1 + 3 * rampDiagonal T * ((A.card : ℝ) - 1) := by
  apply isWeakSidon_orderedPairEnergy_le_normalized
    (D := Finset.Icc 1 (T - 1)) hA hcard (rampCorrelation T) (rampDiagonal T)
  · exact rampDiagonal_nonneg T
  · exact rampCorrelation_neg T
  · intro p hp hnz
    have hpos := (mem_positivePairs.mp hp).2.2
    apply Finset.mem_Icc.mpr
    constructor
    · omega
    · by_contra h
      have hlarge : T ≤ p.1 - p.2 := by omega
      apply hnz
      apply rampCorrelation_eq_zero_of_abs_le
      rw [abs_of_nonneg (by positivity : (0 : ℤ) ≤ ((p.1 - p.2 : ℕ) : ℤ))]
      exact_mod_cast hlarge
  · intro d _hd
    exact rampCorrelation_nonneg T (d : ℤ)
  · intro d
    exact rampCorrelation_le_diagonal hT (d : ℤ)
  · exact rampCorrelation_zero hT
  · rw [← sum_pos_rampCorrelation_eq_nat hT]
    exact two_mul_sum_pos_rampCorrelation hT

end Sidon30

end
