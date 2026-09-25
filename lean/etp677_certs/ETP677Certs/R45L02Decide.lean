import ETP677Certs.R45L02

namespace ETP677Certs.R45L02Decide

/-- Kernel-reduction certificate for the R45/L02 q=3 object. -/
theorem r45_l02_q3_certificate_decide :
    Certificate R45L02.object [4, 6, 10] := by
  change branchObjectB R45L02.object = true ∧
    [4, 6, 10].all (perfectB R45L02.object) = true ∧
    deltaZeroB R45L02.object = true
  set_option maxRecDepth 100000 in
    set_option maxHeartbeats 10000000 in
      decide

/-- The displayed list is the exact set of perfect rows. -/
theorem r45_l02_q3_perfect_rows_exact :
    ∀ r < R45L02.object.n,
      perfectB R45L02.object r = true ↔ r ∈ [4, 6, 10] := by
  set_option maxRecDepth 100000 in
    set_option maxHeartbeats 10000000 in
      decide

end ETP677Certs.R45L02Decide
