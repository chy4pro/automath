import Sidon30.Basic

/-! Exact transfer targets. This module contains definitions only. -/

/-- At most `g` ordered representations of each nonzero integer difference.
The diagonal is excluded by the condition `d ≠ 0`. -/
def IsGThin (g : ℕ) (A : Finset ℕ) : Prop :=
  ∀ d : ℤ, d ≠ 0 →
    ((A.product A).filter (fun p => (p.1 : ℤ) - (p.2 : ℤ) = d)).card ≤ g

/-- Uniqueness of unordered sums of two distinct elements; diagonal sums
are not restricted. -/
def IsWeakSidon (A : Finset ℕ) : Prop :=
  ∀ a ∈ A, ∀ b ∈ A, ∀ c ∈ A, ∀ d ∈ A,
    a + b = c + d → a < b → c < d → a = c ∧ b = d

/-- All ordered, nondiagonal displacement vectors are distinct. -/
def IsSonar {m n : ℕ} (y : Fin m → Fin n) : Prop :=
  ∀ i j k l : Fin m, i ≠ j → k ≠ l →
    ((i.val : ℤ) - j.val, ((y i).val : ℤ) - (y j).val) =
      ((k.val : ℤ) - l.val, ((y k).val : ℤ) - (y l).val) →
    i = k ∧ j = l

def GThinSecondOrderBound : Prop :=
  ∀ (g N : ℕ) (A : Finset ℕ),
    1 ≤ g → 1 ≤ N → 120 ^ 4 ≤ g * N →
    A ⊆ Finset.Icc 1 N → IsGThin g A →
    (A.card : ℝ) ≤ Real.sqrt ((g : ℝ) * (N : ℝ)) +
      (2 * Real.sqrt 2 / 3) * Real.sqrt (Real.sqrt ((g : ℝ) * (N : ℝ))) + 1

def WeakSidonSecondOrderBound : Prop :=
  ∀ (N : ℕ) (A : Finset ℕ), 90 ^ 4 ≤ N →
    A ⊆ Finset.Icc 1 N → IsWeakSidon A →
    (A.card : ℝ) ≤ Real.sqrt (N : ℝ) +
      Real.sqrt ((8 : ℝ) / 3) * Real.sqrt (Real.sqrt (N : ℝ)) + 2

def SonarTriangleBound : Prop :=
  ∀ (m n : ℕ) (y : Fin m → Fin n), 48 ^ 3 ≤ n → IsSonar y →
    (m : ℝ) ≤ (n : ℝ) + 2 * Real.rpow (n : ℝ) ((2 : ℝ) / 3) +
      3 * Real.rpow (n : ℝ) ((1 : ℝ) / 3)
