/-
Erdős problem 30, second-order term for Sidon sets — formalisation project (pipeline smoke test).
Definitions only use Mathlib notions.
-/
import Mathlib

/-- A finite set of natural numbers is a Sidon set if `a + b = c + d` with `a ≤ b`, `c ≤ d`
(all four in the set) forces `a = c` and `b = d`. Diagonal sums are included. -/
def IsSidon (A : Finset ℕ) : Prop :=
  ∀ a ∈ A, ∀ b ∈ A, ∀ c ∈ A, ∀ d ∈ A, a + b = c + d → a ≤ b → c ≤ d → a = c ∧ b = d

theorem isSidon_empty : IsSidon ∅ := by
  intro a ha
  simp at ha
