import Sidon30.Basic

/-! Normalized difference triangle sets and the exact optional scope bounds.
Only within-row differences are restricted; rows may share marks. -/

/-- Each of n rows has k+1 distinct nonnegative marks, includes zero, and
lies at or below m. All positive within-row differences, across all rows,
are distinct. This is equivalent to uniqueness of nonzero ordered
within-row differences; no cross-row difference condition is imposed. -/
def IsDifferenceTriangleSet (n k m : ℕ) (X : Fin n → Finset ℕ) : Prop :=
  (∀ i : Fin n, (X i).card = k + 1 ∧ 0 ∈ X i ∧ X i ⊆ Finset.Icc 0 m) ∧
  (∀ i j : Fin n, ∀ a ∈ X i, ∀ b ∈ X i, ∀ c ∈ X j, ∀ d ∈ X j,
    b < a → d < c → a - b = c - d → i = j ∧ a = c ∧ b = d)

def DifferenceTriangleScopeBound : Prop :=
  ∀ (n k m : ℕ) (X : Fin n → Finset ℕ),
    1 ≤ n → 20365 ≤ k → IsDifferenceTriangleSet n k m X →
    (n : ℝ) * ((Real.sqrt (4 * (k : ℝ) + (8 : ℝ) / 9) -
      2 * Real.sqrt 2 / 3) / 2) ^ 4 < (m : ℝ)

/-- Here k sqrt(k) is the positive-real k^(3/2) occurring in the paper. -/
def DifferenceTriangleExpandedBound : Prop :=
  ∀ (n k m : ℕ) (X : Fin n → Finset ℕ),
    1 ≤ n → 20365 ≤ k → IsDifferenceTriangleSet n k m X →
    (n : ℝ) * ((k : ℝ) ^ 2 - (4 * Real.sqrt 2 / 3) *
      ((k : ℝ) * Real.sqrt (k : ℝ)) + (16 : ℝ) / 9 * (k : ℝ) -
      2 * Real.sqrt (k : ℝ)) ≤ (m : ℝ)
