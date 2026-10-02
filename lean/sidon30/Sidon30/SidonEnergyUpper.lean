import Sidon30.WeightedCount

/-!
Ordered-pair energy, its exact diagonal/positive-difference decomposition,
and the Sidon upper bound for an even real kernel on the integers.

The support version only requires that nonzero positive-difference weights
occur in the chosen finite set `D`. Thus a compactly supported kernel does
not require every difference of the Sidon set to lie in its support.
-/

noncomputable section

open scoped BigOperators

namespace Sidon30

/-- Energy over all ordered pairs, including the diagonal pairs. -/
def orderedPairEnergy (A : Finset ℕ) (f : ℤ → ℝ) : ℝ :=
  ∑ a ∈ A, ∑ b ∈ A, f ((a : ℤ) - (b : ℤ))

/-- A sum over positive pairs is the corresponding filtered double sum. -/
theorem positivePairs_sum_eq_double_sum (A : Finset ℕ) (w : ℕ → ℝ) :
    (∑ p ∈ positivePairs A, w (p.1 - p.2)) =
      ∑ a ∈ A, ∑ b ∈ A, if b < a then w (a - b) else 0 := by
  unfold positivePairs
  rw [Finset.sum_filter, Finset.product_eq_sprod, Finset.sum_product]

private theorem integerDifference_weight_split (f : ℤ → ℝ)
    (heven : ∀ d : ℤ, f (-d) = f d) (a b : ℕ) :
    f ((a : ℤ) - (b : ℤ)) =
      (if a = b then f 0 else 0) +
        (if b < a then f ((a - b : ℕ) : ℤ) else 0) +
        (if a < b then f ((b - a : ℕ) : ℤ) else 0) := by
  rcases lt_trichotomy a b with hab | hab | hba
  · have hneg : (a : ℤ) - (b : ℤ) = -((b - a : ℕ) : ℤ) := by omega
    rw [hneg, heven]
    simp only [hab, ne_of_lt hab, not_lt_of_ge hab.le, if_true, if_false, zero_add]
  · subst b
    simp
  · have hpos : (a : ℤ) - (b : ℤ) = ((a - b : ℕ) : ℤ) := by omega
    rw [hpos]
    simp only [hba, ne_of_gt hba, not_lt_of_ge hba.le, if_true, if_false,
      zero_add, add_zero]

/-- Exact decomposition: the diagonal contributes once and each positive
ordered pair contributes twice. No Sidon or sign assumption is needed. -/
theorem orderedPairEnergy_eq (A : Finset ℕ) (f : ℤ → ℝ)
    (heven : ∀ d : ℤ, f (-d) = f d) :
    orderedPairEnergy A f = (A.card : ℝ) * f 0 +
      2 * ∑ p ∈ positivePairs A, f ((p.1 - p.2 : ℕ) : ℤ) := by
  have hdiag :
      (∑ a ∈ A, ∑ b ∈ A, if a = b then f 0 else 0) =
        (A.card : ℝ) * f 0 := by
    calc
      _ = ∑ _a ∈ A, f 0 := by
        apply Finset.sum_congr rfl
        intro a ha
        simpa only [if_pos (rfl : a = a), ite_true] using
          (Finset.sum_eq_single_of_mem a ha
            (f := fun b : ℕ => if a = b then f 0 else 0)
            (by
              intro b _hb hba
              simp only [Ne.symm hba, if_false]))
      _ = _ := by simp only [Finset.sum_const, nsmul_eq_mul]
  have hpos := positivePairs_sum_eq_double_sum A (fun d => f (d : ℤ))
  have hneg :
      (∑ a ∈ A, ∑ b ∈ A, if a < b then f ((b - a : ℕ) : ℤ) else 0) =
        ∑ p ∈ positivePairs A, f ((p.1 - p.2 : ℕ) : ℤ) := by
    calc
      _ = ∑ a ∈ A, ∑ b ∈ A,
            if b < a then f ((a - b : ℕ) : ℤ) else 0 := Finset.sum_comm
      _ = _ := hpos.symm
  unfold orderedPairEnergy
  calc
    (∑ a ∈ A, ∑ b ∈ A, f ((a : ℤ) - (b : ℤ))) =
        (∑ a ∈ A, ∑ b ∈ A, if a = b then f 0 else 0) +
          (∑ a ∈ A, ∑ b ∈ A, if b < a then f ((a - b : ℕ) : ℤ) else 0) +
          (∑ a ∈ A, ∑ b ∈ A, if a < b then f ((b - a : ℕ) : ℤ) else 0) := by
      simp_rw [integerDifference_weight_split f heven, Finset.sum_add_distrib]
    _ = _ := by
      rw [hdiag, ← hpos, hneg]
      ring

/-- Sidon injectivity bounds a positive-pair sum by a nonnegative finite
weight sum. Only the nonzero weights must be covered by `D`. -/
theorem isSidon_positivePairSum_le_of_support {A D : Finset ℕ}
    (hA : IsSidon A) (w : ℕ → ℝ)
    (hcover : ∀ p ∈ positivePairs A, w (p.1 - p.2) ≠ 0 → p.1 - p.2 ∈ D)
    (hnonneg : ∀ d ∈ D, 0 ≤ w d) :
    (∑ p ∈ positivePairs A, w (p.1 - p.2)) ≤ ∑ d ∈ D, w d := by
  let P := (positivePairs A).filter (fun p => p.1 - p.2 ∈ D)
  have hfilter :
      (∑ p ∈ P, w (p.1 - p.2)) = ∑ p ∈ positivePairs A, w (p.1 - p.2) := by
    dsimp [P]
    exact Finset.sum_filter_of_ne hcover
  have hinj :
      Set.InjOn (fun p : ℕ × ℕ => p.1 - p.2) (↑P : Set (ℕ × ℕ)) := by
    intro p hp q hq hpq
    exact positiveDifference_injOn hA
      (Finset.mem_filter.mp hp).1 (Finset.mem_filter.mp hq).1 hpq
  have himap : P.image (fun p => p.1 - p.2) ⊆ D := by
    intro d hd
    obtain ⟨p, hp, rfl⟩ := Finset.mem_image.mp hd
    exact (Finset.mem_filter.mp hp).2
  have himage :
      (∑ d ∈ P.image (fun p => p.1 - p.2), w d) =
        ∑ p ∈ P, w (p.1 - p.2) := Finset.sum_image hinj
  calc
    (∑ p ∈ positivePairs A, w (p.1 - p.2)) = ∑ p ∈ P, w (p.1 - p.2) :=
      hfilter.symm
    _ = ∑ d ∈ P.image (fun p => p.1 - p.2), w d := himage.symm
    _ ≤ ∑ d ∈ D, w d :=
      Finset.sum_le_sum_of_subset_of_nonneg himap (fun d hd _ => hnonneg d hd)

/-- A convenient variant when `D` contains every positive difference. -/
theorem isSidon_positivePairSum_le {A D : Finset ℕ}
    (hA : IsSidon A) (w : ℕ → ℝ)
    (hcover : ∀ p ∈ positivePairs A, p.1 - p.2 ∈ D)
    (hnonneg : ∀ d ∈ D, 0 ≤ w d) :
    (∑ p ∈ positivePairs A, w (p.1 - p.2)) ≤ ∑ d ∈ D, w d := by
  exact isSidon_positivePairSum_le_of_support hA w
    (fun p hp _ => hcover p hp) hnonneg

/-- The ordered-pair energy bound for an even kernel, using only its
nonzero positive-difference support and nonnegativity on `D`. -/
theorem isSidon_orderedPairEnergy_le_of_support {A D : Finset ℕ}
    (hA : IsSidon A) (f : ℤ → ℝ)
    (heven : ∀ d : ℤ, f (-d) = f d)
    (hcover : ∀ p ∈ positivePairs A,
      f ((p.1 - p.2 : ℕ) : ℤ) ≠ 0 → p.1 - p.2 ∈ D)
    (hnonneg : ∀ d ∈ D, 0 ≤ f (d : ℤ)) :
    orderedPairEnergy A f ≤ (A.card : ℝ) * f 0 + 2 * ∑ d ∈ D, f (d : ℤ) := by
  rw [orderedPairEnergy_eq A f heven]
  apply add_le_add le_rfl
  exact mul_le_mul_of_nonneg_left
    (isSidon_positivePairSum_le_of_support hA (fun d => f (d : ℤ)) hcover hnonneg)
    (by norm_num)

/-- The same bound when the finite set `D` covers all positive differences. -/
theorem isSidon_orderedPairEnergy_le {A D : Finset ℕ}
    (hA : IsSidon A) (f : ℤ → ℝ)
    (heven : ∀ d : ℤ, f (-d) = f d)
    (hcover : ∀ p ∈ positivePairs A, p.1 - p.2 ∈ D)
    (hnonneg : ∀ d ∈ D, 0 ≤ f (d : ℤ)) :
    orderedPairEnergy A f ≤ (A.card : ℝ) * f 0 + 2 * ∑ d ∈ D, f (d : ℤ) := by
  exact isSidon_orderedPairEnergy_le_of_support hA f heven
    (fun p hp _ => hcover p hp) hnonneg

/-- The normalized correlation form, retaining the exact `card - 1` term.
The mass identity is explicit; no correlation facts are assumed implicitly. -/
theorem isSidon_orderedPairEnergy_le_normalized {A D : Finset ℕ}
    (hA : IsSidon A) (f : ℤ → ℝ) (a : ℝ)
    (heven : ∀ d : ℤ, f (-d) = f d)
    (hcover : ∀ p ∈ positivePairs A,
      f ((p.1 - p.2 : ℕ) : ℤ) ≠ 0 → p.1 - p.2 ∈ D)
    (hnonneg : ∀ d ∈ D, 0 ≤ f (d : ℤ))
    (hzero : f 0 = a) (hmass : 2 * (∑ d ∈ D, f (d : ℤ)) = 1 - a) :
    orderedPairEnergy A f ≤ 1 + a * ((A.card : ℝ) - 1) := by
  calc
    orderedPairEnergy A f ≤ (A.card : ℝ) * f 0 + 2 * ∑ d ∈ D, f (d : ℤ) :=
      isSidon_orderedPairEnergy_le_of_support hA f heven hcover hnonneg
    _ = 1 + a * ((A.card : ℝ) - 1) := by
      rw [hzero, hmass]
      ring

end Sidon30

end
