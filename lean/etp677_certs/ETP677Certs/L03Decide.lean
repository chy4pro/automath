import ETP677Certs.L03

namespace ETP677Certs.L03Decide

/-- Kernel-reduction certificate for the L03 q=3 object. -/
theorem l03_q3_four_perfect_certificate_decide :
    Certificate L03.object [4, 5, 6, 10] := by
  change branchObjectB L03.object = true ∧
    [4, 5, 6, 10].all (perfectB L03.object) = true ∧
    deltaZeroB L03.object = true
  set_option maxRecDepth 100000 in
    set_option maxHeartbeats 10000000 in
      decide

/-- The displayed list is the exact set of perfect rows. -/
theorem l03_q3_perfect_rows_exact :
    ∀ r < L03.object.n,
      perfectB L03.object r = true ↔ r ∈ [4, 5, 6, 10] := by
  set_option maxRecDepth 100000 in
    set_option maxHeartbeats 10000000 in
      decide

end ETP677Certs.L03Decide
