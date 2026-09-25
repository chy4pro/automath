import ETP677Certs.R45L02

namespace ETP677Certs.NegativeControl

/-- The R45/L02 object after swapping table cells `(0,0)` and `(0,1)`. -/
def perturbed : Object := swapFirstTwoCells R45L02.object

/-- Negative control: the identical certificate claim for the two-cell perturbation is false. -/
theorem two_cell_perturbation_rejected :
    ¬ Certificate perturbed [4, 6, 10] := by
  change ¬ (branchObjectB perturbed = true ∧
    [4, 6, 10].all (perfectB perturbed) = true ∧ deltaZeroB perturbed = true)
  native_decide

end ETP677Certs.NegativeControl
