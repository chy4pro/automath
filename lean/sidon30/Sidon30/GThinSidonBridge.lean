import Sidon30.GThinMain
import Sidon30.Statement

namespace Sidon30

/-- The strong Sidon convention implies one ordered representation of each
nonzero signed difference, including the negative differences. -/
theorem isSidon_isGThin_one {A : Finset ℕ} (hA : IsSidon A) : IsGThin 1 A := by
  intro d hd
  apply Finset.card_le_one.mpr
  intro p hp q hq
  obtain ⟨hpA, hpd⟩ := Finset.mem_filter.mp hp
  obtain ⟨hqA, hqd⟩ := Finset.mem_filter.mp hq
  obtain ⟨hp1, hp2⟩ := Finset.mem_product.mp hpA
  obtain ⟨hq1, hq2⟩ := Finset.mem_product.mp hqA
  have hdiff : (p.1 : ℤ) - p.2 = (q.1 : ℤ) - q.2 := hpd.trans hqd.symm
  by_cases hpos : p.2 < p.1
  · have hqpos : q.2 < q.1 := by omega
    have hnat : p.1 - p.2 = q.1 - q.2 := by omega
    obtain ⟨h1, h2⟩ := (isSidon_iff_uniquePositiveDifferences A).mp hA
      p.1 hp1 p.2 hp2 q.1 hq1 q.2 hq2 hpos hqpos hnat
    exact Prod.ext h1 h2
  · have hneg : p.1 < p.2 := by omega
    have hqneg : q.1 < q.2 := by omega
    have hnat : p.2 - p.1 = q.2 - q.1 := by omega
    obtain ⟨h2, h1⟩ := (isSidon_iff_uniquePositiveDifferences A).mp hA
      p.2 hp2 p.1 hp1 q.2 hq2 q.1 hq1 hneg hqneg hnat
    exact Prod.ext h1 h2

end Sidon30

/-- A second derivation of the unchanged Sidon specification, by setting g=1.
The original `sidon_second_order` proof and guards remain independent. -/
theorem sidon_second_order_from_gThin : SidonSecondOrderBound := by
  intro N A hN hAN hA
  simpa only [Nat.cast_one, one_mul] using
    (g_thin_second_order 1 N A (by omega) (by omega)
      (by simpa only [one_mul] using hN) hAN (Sidon30.isSidon_isGThin_one hA))
