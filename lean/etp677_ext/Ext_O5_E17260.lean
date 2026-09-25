import Mathlib.Data.Fin.Basic
import Mathlib.Tactic
import Std.Tactic.BVDecide

/-!
# E17260 finite-table witness stub

This file is intentionally not part of the current `lakefile.toml` roots and
was not compiled by the engineering ticket.  If a concrete finite witness is
found, insert its table below and discharge the closed law with `decide`,
`native_decide`, or `bv_decide` before connecting it to any publication claim.
-/

namespace E17260

abbrev Table (n : Nat) := Fin n → Fin n → Fin n

/-- The order-five law `x = (y◇x)◇(z◇(x◇(z◇z)))`. -/
def Law {n : Nat} (table : Table n) : Prop :=
  ∀ x y z,
    x = table (table y x) (table z (table x (table z z)))

/-- Executable form used by a closed concrete-table certificate. -/
def lawDecide {n : Nat} (table : Table n) : Bool :=
  decide (Law table)

/-- Bridge from a successful evaluation of a concrete table to the Prop law. -/
theorem law_of_decide_eq_true {n : Nat} (table : Table n)
    (h : lawDecide table = true) : Law table := by
  exact of_decide_eq_true h

/-!
Witness template (replace `candidate` by a closed table definition):

```lean
def candidate : Table N := fun x y => -- concrete `Fin N` entry

theorem candidate_satisfies : Law candidate := by
  native_decide

-- For a Boolean/BitVec-backed closed table, the alternative template is:
theorem candidate_satisfies_bv : Law candidate := by
  bv_decide
```
-/

end E17260
