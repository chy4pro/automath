import Sidon30.Differences

/-!
Finite weighted counting of positive difference representations.
There is no measure theory, infinite sum, or numerical certificate here.
This file has not been locally compiled; validation is delegated to CI.
-/

open scoped BigOperators

namespace Sidon30

/-- The ordered representations of a difference, restricted to positive pairs. -/
def positiveDifferenceRepresentations (A : Finset ℕ) (d : ℕ) :
    Finset (ℕ × ℕ) :=
  (positivePairs A).filter (fun p => p.1 - p.2 = d)

/-- Number of ordered positive-difference representations. -/
def positiveDifferenceCount (A : Finset ℕ) (d : ℕ) : ℕ :=
  (positiveDifferenceRepresentations A d).card

@[simp]
theorem mem_positiveDifferenceRepresentations {A : Finset ℕ} {d : ℕ}
    {p : ℕ × ℕ} :
    p ∈ positiveDifferenceRepresentations A d ↔
      p ∈ positivePairs A ∧ p.1 - p.2 = d := by
  simp only [positiveDifferenceRepresentations, Finset.mem_filter]

/-- Diagonal pairs and truncated nonpositive differences are excluded. -/
@[simp]
theorem positiveDifferenceCount_zero (A : Finset ℕ) :
    positiveDifferenceCount A 0 = 0 := by
  unfold positiveDifferenceCount
  apply Finset.card_eq_zero.mpr
  apply Finset.eq_empty_of_forall_notMem
  intro p hp
  rcases mem_positiveDifferenceRepresentations.mp hp with ⟨hpair, hdiff⟩
  have hpos : p.2 < p.1 := (mem_positivePairs.mp hpair).2.2
  omega

/-- Every difference has at most one positive ordered representation in a Sidon set. -/
theorem positiveDifferenceCount_le_one {A : Finset ℕ}
    (hA : IsSidon A) (d : ℕ) :
    positiveDifferenceCount A d ≤ 1 := by
  unfold positiveDifferenceCount
  apply Finset.card_le_one.mpr
  intro p hp q hq
  rcases mem_positiveDifferenceRepresentations.mp hp with ⟨hpair, hdiff⟩
  rcases mem_positiveDifferenceRepresentations.mp hq with ⟨hqpair, hqdiff⟩
  exact positiveDifference_injOn hA hpair hqpair (hdiff.trans hqdiff.symm)

/-- Pointwise representation counts at most one majorize any nonnegative finite weight sum. -/
theorem weighted_count_le_sum {D : Finset ℕ} (r : ℕ → ℕ) (w : ℕ → ℝ)
    (hr : ∀ d ∈ D, r d ≤ 1) (hw : ∀ d ∈ D, 0 ≤ w d) :
    (∑ d ∈ D, (r d : ℝ) * w d) ≤ ∑ d ∈ D, w d := by
  apply Finset.sum_le_sum
  intro d hd
  have hr' : (r d : ℝ) ≤ 1 := by
    exact_mod_cast hr d hd
  simpa only [one_mul] using mul_le_mul_of_nonneg_right hr' (hw d hd)

/-- The finite nonnegative-weight Sidon difference majorization. -/
theorem isSidon_weightedDifferenceCount_le_sum {A D : Finset ℕ}
    (hA : IsSidon A) (w : ℕ → ℝ) (hw : ∀ d ∈ D, 0 ≤ w d) :
    (∑ d ∈ D, (positiveDifferenceCount A d : ℝ) * w d) ≤
      ∑ d ∈ D, w d := by
  exact weighted_count_le_sum (positiveDifferenceCount A) w
    (fun d _hd => positiveDifferenceCount_le_one hA d) hw

end Sidon30
