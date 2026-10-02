import Sidon30.Differences

/-!
A first finite cardinality consequence of positive-difference injectivity.
The interval is the closed natural interval from 1 to N.
This file has not been locally compiled; validation is delegated to CI.
-/

namespace Sidon30

/-- Positive ordered pairs inject into the N-1 possible positive differences. -/
theorem positivePairs_card_le_pred {A : Finset ℕ} {N : ℕ}
    (hA : IsSidon A) (hAN : A ⊆ Finset.Icc 1 N) :
    (positivePairs A).card ≤ N - 1 := by
  have hmap :
      Set.MapsTo (fun p : ℕ × ℕ => p.1 - p.2 - 1)
        (↑(positivePairs A) : Set (ℕ × ℕ))
        (↑(Finset.range (N - 1)) : Set ℕ) := by
    intro p hp
    rcases mem_positivePairs.mp hp with ⟨hpa, hpb, hplt⟩
    have haN : p.1 ≤ N := (Finset.mem_Icc.mp (hAN hpa)).2
    have hb1 : 1 ≤ p.2 := (Finset.mem_Icc.mp (hAN hpb)).1
    apply Finset.mem_range.mpr
    omega
  have hinj :
      Set.InjOn (fun p : ℕ × ℕ => p.1 - p.2 - 1)
        (↑(positivePairs A) : Set (ℕ × ℕ)) := by
    intro p hp q hq hpq
    have hplt : p.2 < p.1 := (mem_positivePairs.mp hp).2.2
    have hqlt : q.2 < q.1 := (mem_positivePairs.mp hq).2.2
    apply positiveDifference_injOn hA hp hq
    omega
  have hcard :
      (positivePairs A).card ≤ (Finset.range (N - 1)).card :=
    Finset.card_le_card_of_injOn
      (fun p : ℕ × ℕ => p.1 - p.2 - 1) hmap hinj
  simpa only [Finset.card_range] using hcard

end Sidon30
