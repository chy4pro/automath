import ETP677Certs.L05

namespace ETP677Certs.L05Decide

/-- Kernel-reduction certificate for the L05 q=4 object. -/
theorem l05_q4_p6_certificate_decide :
    Certificate L05.object [0, 1, 2, 5, 15, 17] := by
  change branchObjectB L05.object = true ∧
    [0, 1, 2, 5, 15, 17].all (perfectB L05.object) = true ∧
    deltaZeroB L05.object = true
  set_option maxRecDepth 100000 in
    set_option maxHeartbeats 10000000 in
      decide

/-- The displayed list is the exact set of perfect rows. -/
theorem l05_q4_perfect_rows_exact :
    ∀ r < L05.object.n,
      perfectB L05.object r = true ↔ r ∈ [0, 1, 2, 5, 15, 17] := by
  set_option maxRecDepth 100000 in
    set_option maxHeartbeats 10000000 in
      decide

end ETP677Certs.L05Decide
