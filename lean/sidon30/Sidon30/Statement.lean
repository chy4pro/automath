import Sidon30.Basic

/-!
# The exact Sidon second-order target

This file states a proposition; it does not prove it. `Basic` imports only
Mathlib and supplies the existing `IsSidon` definition, including diagonal
pair sums. No proof card is imported here.

The fourth root is written as two real square roots so that the exponent
cannot accidentally be interpreted as division in the natural numbers.
-/

/-- Every Sidon subset of `{1, ..., N}` obeys the explicit second-order
bound for every natural number `N ≥ 120^4 = 207360000`. The two square roots
are the nonnegative real fourth root; `N` need not be a fourth power. -/
def SidonSecondOrderBound : Prop :=
  ∀ (N : ℕ) (A : Finset ℕ),
    120 ^ 4 ≤ N →
    A ⊆ Finset.Icc 1 N →
    IsSidon A →
    (A.card : ℝ) ≤
      Real.sqrt (N : ℝ) +
        (2 * Real.sqrt 2 / 3) * Real.sqrt (Real.sqrt (N : ℝ)) + 1
