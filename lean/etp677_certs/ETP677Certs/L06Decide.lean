import ETP677Certs.L06

namespace ETP677Certs.L06Decide

-- The displayed list is the exact set of perfect rows.
set_option maxRecDepth 100000 in
set_option maxHeartbeats 10000000 in
theorem l06_q7_perfect_rows_exact :
    ∀ r < L06.object.n,
      perfectB L06.object r = true ↔
        r ∈ [0, 4, 5, 6, 10, 13, 14, 15, 16, 21, 23, 31, 37, 39] := by
  decide

end ETP677Certs.L06Decide
