import Sidon30.TransferStatement
import Sidon30.WeightedCount
import Sidon30.ShiftWindow

/-!
The positive-difference structure of a weak Sidon set. An extra pair is the
upper edge of a three-term arithmetic progression. Removing these pairs
leaves an injective difference map; their middle points are also distinct.
-/

namespace Sidon30

/-- Translation by one preserves uniqueness of strict unordered sums. -/
theorem isWeakSidon_shiftWindow {A : Finset ℕ} {N : ℕ}
    (hA : IsWeakSidon A) (hAN : A ⊆ Finset.Icc 1 N) :
    IsWeakSidon (shiftWindow A) := by
  intro a ha b hb c hc d hd hsum hab hcd
  rcases mem_shiftWindow.mp ha with ⟨x, hx, hxa⟩
  rcases mem_shiftWindow.mp hb with ⟨y, hy, hyb⟩
  rcases mem_shiftWindow.mp hc with ⟨u, hu, huc⟩
  rcases mem_shiftWindow.mp hd with ⟨v, hv, hvd⟩
  have hx1 : 1 ≤ x := (Finset.mem_Icc.mp (hAN hx)).1
  have hy1 : 1 ≤ y := (Finset.mem_Icc.mp (hAN hy)).1
  have hu1 : 1 ≤ u := (Finset.mem_Icc.mp (hAN hu)).1
  have hv1 : 1 ≤ v := (Finset.mem_Icc.mp (hAN hv)).1
  have hsum' : x + y = u + v := by omega
  have hxy : x < y := by omega
  have huv : u < v := by omega
  obtain ⟨hxu, hyv⟩ := hA x hx y hy u hu v hv hsum' hxy huv
  constructor <;> omega

/-- Two distinct positive representations of one difference must join at
one endpoint, and therefore form a three-term arithmetic progression. -/
theorem isWeakSidon_difference_collision {A : Finset ℕ}
    (hA : IsWeakSidon A) {a b c d : ℕ}
    (ha : a ∈ A) (hb : b ∈ A) (hc : c ∈ A) (hd : d ∈ A)
    (hba : b < a) (hdc : d < c) (heq : a - b = c - d)
    (hne : a ≠ c) : b = c ∨ d = a := by
  by_cases hbc : b = c
  · exact Or.inl hbc
  by_cases hda : d = a
  · exact Or.inr hda
  exfalso
  rcases lt_or_gt_of_ne (Ne.symm hda) with had | hda'
  · rcases lt_or_gt_of_ne hbc with hbc' | hcb
    · obtain ⟨hab, _⟩ := hA a ha d hd b hb c hc (by omega) had hbc'
      omega
    · obtain ⟨hac, _⟩ := hA a ha d hd c hc b hb (by omega) had hcb
      exact hne hac
  · rcases lt_or_gt_of_ne hbc with hbc' | hcb
    · obtain ⟨_, hac⟩ := hA d hd a ha b hb c hc (by omega) hda' hbc'
      exact hne hac
    · obtain ⟨hdc', _⟩ := hA d hd a ha c hc b hb (by omega) hda' hcb
      omega

/-- Upper edges of three-term arithmetic progressions in `A`. -/
def weakExtraPairs (A : Finset ℕ) : Finset (ℕ × ℕ) :=
  (positivePairs A).filter (fun p =>
    p.1 - p.2 ≤ p.2 ∧ p.2 - (p.1 - p.2) ∈ A)

/-- Positive pairs remaining after removing the upper edges of progressions. -/
def weakBasePairs (A : Finset ℕ) : Finset (ℕ × ℕ) :=
  positivePairs A \ weakExtraPairs A

@[simp]
theorem mem_weakExtraPairs {A : Finset ℕ} {p : ℕ × ℕ} :
    p ∈ weakExtraPairs A ↔ p ∈ positivePairs A ∧
      p.1 - p.2 ≤ p.2 ∧ p.2 - (p.1 - p.2) ∈ A := by
  simp only [weakExtraPairs, Finset.mem_filter]

@[simp]
theorem mem_weakBasePairs {A : Finset ℕ} {p : ℕ × ℕ} :
    p ∈ weakBasePairs A ↔ p ∈ positivePairs A ∧ p ∉ weakExtraPairs A := by
  simp only [weakBasePairs, Finset.mem_sdiff]

theorem weakExtraPairs_subset (A : Finset ℕ) :
    weakExtraPairs A ⊆ positivePairs A := by
  intro p hp
  exact (mem_weakExtraPairs.mp hp).1

theorem weakBasePairs_subset (A : Finset ℕ) :
    weakBasePairs A ⊆ positivePairs A := by
  intro p hp
  exact (mem_weakBasePairs.mp hp).1

/-- The two representations of a repeated difference include an extra pair. -/
theorem isWeakSidon_collision_has_extra {A : Finset ℕ}
    (hA : IsWeakSidon A) {p q : ℕ × ℕ}
    (hp : p ∈ positivePairs A) (hq : q ∈ positivePairs A)
    (heq : p.1 - p.2 = q.1 - q.2) (hne : p ≠ q) :
    p ∈ weakExtraPairs A ∨ q ∈ weakExtraPairs A := by
  rcases mem_positivePairs.mp hp with ⟨hpa, hpb, hpord⟩
  rcases mem_positivePairs.mp hq with ⟨hqa, hqb, hqord⟩
  have hfirst : p.1 ≠ q.1 := by
    intro h
    apply hne
    apply Prod.ext
    · exact h
    · omega
  rcases isWeakSidon_difference_collision hA hpa hpb hqa hqb
      hpord hqord heq hfirst with h | h
  · left
    apply mem_weakExtraPairs.mpr
    refine ⟨hp, ?_, ?_⟩
    · omega
    · have hz : p.2 - (p.1 - p.2) = q.2 := by omega
      rw [hz]
      exact hqb
  · right
    apply mem_weakExtraPairs.mpr
    refine ⟨hq, ?_, ?_⟩
    · omega
    · have hz : q.2 - (q.1 - q.2) = p.2 := by omega
      rw [hz]
      exact hpb

/-- The base pairs have distinct positive differences. -/
theorem weakBasePairs_difference_injOn {A : Finset ℕ} (hA : IsWeakSidon A) :
    Set.InjOn (fun p : ℕ × ℕ => p.1 - p.2)
      (↑(weakBasePairs A) : Set (ℕ × ℕ)) := by
  intro p hp q hq heq
  change p.1 - p.2 = q.1 - q.2 at heq
  rcases mem_weakBasePairs.mp hp with ⟨hp, hpnot⟩
  rcases mem_weakBasePairs.mp hq with ⟨hq, hqnot⟩
  by_contra hne
  rcases isWeakSidon_collision_has_extra hA hp hq heq hne with h | h
  · exact hpnot h
  · exact hqnot h

/-- Two progressions cannot have the same middle point: their distinct
endpoint pairs would have the same strict unordered sum. -/
theorem weakExtraPairs_middle_injOn {A : Finset ℕ} (hA : IsWeakSidon A) :
    Set.InjOn (fun p : ℕ × ℕ => p.2)
      (↑(weakExtraPairs A) : Set (ℕ × ℕ)) := by
  intro p hp q hq heq
  change p.2 = q.2 at heq
  rcases mem_weakExtraPairs.mp hp with ⟨hpp, hple, hpl⟩
  rcases mem_weakExtraPairs.mp hq with ⟨hqp, hqle, hql⟩
  rcases mem_positivePairs.mp hpp with ⟨hpa, hpb, hpord⟩
  rcases mem_positivePairs.mp hqp with ⟨hqa, hqb, hqord⟩
  have hsum : p.2 - (p.1 - p.2) + p.1 = q.2 - (q.1 - q.2) + q.1 := by omega
  have hpstrict : p.2 - (p.1 - p.2) < p.1 := by omega
  have hqstrict : q.2 - (q.1 - q.2) < q.1 := by omega
  obtain ⟨_, hfirst⟩ := hA _ hpl _ hpa _ hql _ hqa hsum hpstrict hqstrict
  exact Prod.ext hfirst heq

/-- Extra pairs also have distinct differences; two such pairs with one
shared endpoint would give a forbidden four-term arithmetic progression. -/
theorem weakExtraPairs_difference_injOn {A : Finset ℕ} (hA : IsWeakSidon A) :
    Set.InjOn (fun p : ℕ × ℕ => p.1 - p.2)
      (↑(weakExtraPairs A) : Set (ℕ × ℕ)) := by
  intro p hp q hq heq
  change p.1 - p.2 = q.1 - q.2 at heq
  rcases mem_weakExtraPairs.mp hp with ⟨hpp, hple, hpl⟩
  rcases mem_weakExtraPairs.mp hq with ⟨hqp, hqle, hql⟩
  rcases mem_positivePairs.mp hpp with ⟨hpa, hpb, hpord⟩
  rcases mem_positivePairs.mp hqp with ⟨hqa, hqb, hqord⟩
  by_cases hfirst : p.1 = q.1
  · apply Prod.ext hfirst
    omega
  exfalso
  rcases isWeakSidon_difference_collision hA hpa hpb hqa hqb
      hpord hqord heq hfirst with h | h
  · have hsum : q.2 - (q.1 - q.2) + p.1 = q.2 + q.1 := by omega
    have hord : q.2 - (q.1 - q.2) < p.1 := by omega
    obtain ⟨he, _⟩ := hA _ hql _ hpa _ hqb _ hqa hsum hord hqord
    omega
  · have hsum : p.2 - (p.1 - p.2) + q.1 = p.2 + p.1 := by omega
    have hord : p.2 - (p.1 - p.2) < q.1 := by omega
    obtain ⟨he, _⟩ := hA _ hpl _ hqa _ hpb _ hpa hsum hord hpord
    omega

/-- Every positive difference of a weak Sidon set has multiplicity at most two. -/
theorem isWeakSidon_positiveDifferenceCount_le_two {A : Finset ℕ}
    (hA : IsWeakSidon A) (d : ℕ) : positiveDifferenceCount A d ≤ 2 := by
  let R := positiveDifferenceRepresentations A d
  have hb : (R \ weakExtraPairs A).card ≤ 1 := by
    apply Finset.card_le_one.mpr
    intro p hp q hq
    rcases Finset.mem_sdiff.mp hp with ⟨hpr, hpnot⟩
    rcases Finset.mem_sdiff.mp hq with ⟨hqr, hqnot⟩
    rcases mem_positiveDifferenceRepresentations.mp hpr with ⟨hpp, hpd⟩
    rcases mem_positiveDifferenceRepresentations.mp hqr with ⟨hqp, hqd⟩
    exact weakBasePairs_difference_injOn hA
      (mem_weakBasePairs.mpr ⟨hpp, hpnot⟩)
      (mem_weakBasePairs.mpr ⟨hqp, hqnot⟩) (hpd.trans hqd.symm)
  have he : (R ∩ weakExtraPairs A).card ≤ 1 := by
    apply Finset.card_le_one.mpr
    intro p hp q hq
    rcases Finset.mem_inter.mp hp with ⟨hpr, hpe⟩
    rcases Finset.mem_inter.mp hq with ⟨hqr, hqe⟩
    have hpd := (mem_positiveDifferenceRepresentations.mp hpr).2
    have hqd := (mem_positiveDifferenceRepresentations.mp hqr).2
    exact weakExtraPairs_difference_injOn hA hpe hqe (hpd.trans hqd.symm)
  have hs := Finset.card_sdiff_add_card_inter R (weakExtraPairs A)
  change R.card ≤ 2
  omega

/-- Extra middle points avoid the minimum; this form includes singleton sets. -/
theorem weakExtraPairs_card_le_sub_one {A : Finset ℕ}
    (hA : IsWeakSidon A) (hcard : 1 ≤ A.card) :
    (weakExtraPairs A).card ≤ A.card - 1 := by
  have hne : A.Nonempty := Finset.card_pos.mp (by omega)
  have hsubset : (weakExtraPairs A).image (fun p => p.2) ⊆ A.erase (A.min' hne) := by
    intro m hm
    obtain ⟨p, hp, rfl⟩ := Finset.mem_image.mp hm
    rcases mem_weakExtraPairs.mp hp with ⟨hpp, hple, hpl⟩
    rcases mem_positivePairs.mp hpp with ⟨hpa, hpb, hpord⟩
    have hmin : A.min' hne ≤ p.2 - (p.1 - p.2) := A.min'_le _ hpl
    apply Finset.mem_erase.mpr
    exact ⟨by omega, hpb⟩
  calc
    (weakExtraPairs A).card = ((weakExtraPairs A).image (fun p => p.2)).card :=
      (Finset.card_image_of_injOn (weakExtraPairs_middle_injOn hA)).symm
    _ ≤ (A.erase (A.min' hne)).card := Finset.card_le_card hsubset
    _ = A.card - 1 := Finset.card_erase_of_mem (A.min'_mem hne)

/-- With at least two points, extra middle points avoid both endpoints. -/
theorem weakExtraPairs_card_le_sub_two {A : Finset ℕ}
    (hA : IsWeakSidon A) (hcard : 2 ≤ A.card) :
    (weakExtraPairs A).card ≤ A.card - 2 := by
  have hne : A.Nonempty := Finset.card_pos.mp (by omega)
  have hminmax : A.min' hne < A.max' hne :=
    A.min'_lt_max'_of_card (by omega)
  have hmaxmem : A.max' hne ∈ A.erase (A.min' hne) :=
    Finset.mem_erase.mpr ⟨by omega, A.max'_mem hne⟩
  have hsubset : (weakExtraPairs A).image (fun p => p.2) ⊆
      (A.erase (A.min' hne)).erase (A.max' hne) := by
    intro m hm
    obtain ⟨p, hp, rfl⟩ := Finset.mem_image.mp hm
    rcases mem_weakExtraPairs.mp hp with ⟨hpp, hple, hpl⟩
    rcases mem_positivePairs.mp hpp with ⟨hpa, hpb, hpord⟩
    have hmin : A.min' hne ≤ p.2 - (p.1 - p.2) := A.min'_le _ hpl
    have hmax : p.1 ≤ A.max' hne := A.le_max' _ hpa
    apply Finset.mem_erase.mpr
    refine ⟨by omega, Finset.mem_erase.mpr ⟨by omega, hpb⟩⟩
  have hbound : (weakExtraPairs A).card ≤
      ((A.erase (A.min' hne)).erase (A.max' hne)).card := by
    rw [← Finset.card_image_of_injOn (weakExtraPairs_middle_injOn hA)]
    exact Finset.card_le_card hsubset
  rw [Finset.card_erase_of_mem hmaxmem,
    Finset.card_erase_of_mem (A.min'_mem hne)] at hbound
  omega

/-- The finite set of positive differences with at least two representations. -/
def weakRepeatedDifferences (A : Finset ℕ) : Finset ℕ :=
  ((positivePairs A).image (fun p => p.1 - p.2)).filter
    (fun d => 2 ≤ positiveDifferenceCount A d)

/-- Repeated positive differences are exactly the gaps of three-term
arithmetic progressions, represented by their upper edges. -/
theorem weakRepeatedDifferences_eq_image {A : Finset ℕ} (hA : IsWeakSidon A) :
    weakRepeatedDifferences A = (weakExtraPairs A).image (fun p => p.1 - p.2) := by
  ext d
  constructor
  · intro hd
    have hcount := (Finset.mem_filter.mp hd).2
    have htwo : 1 < (positiveDifferenceRepresentations A d).card := by
      change 2 ≤ (positiveDifferenceRepresentations A d).card at hcount
      omega
    obtain ⟨p, hp, q, hq, hpq⟩ := Finset.one_lt_card.mp htwo
    rcases mem_positiveDifferenceRepresentations.mp hp with ⟨hpp, hpd⟩
    rcases mem_positiveDifferenceRepresentations.mp hq with ⟨hqp, hqd⟩
    rcases isWeakSidon_collision_has_extra hA hpp hqp
        (hpd.trans hqd.symm) hpq with he | he
    · exact Finset.mem_image.mpr ⟨p, he, hpd⟩
    · exact Finset.mem_image.mpr ⟨q, he, hqd⟩
  · intro hd
    obtain ⟨p, hp, rfl⟩ := Finset.mem_image.mp hd
    rcases mem_weakExtraPairs.mp hp with ⟨hpp, hple, hpl⟩
    rcases mem_positivePairs.mp hpp with ⟨hpa, hpb, hpord⟩
    apply Finset.mem_filter.mpr
    refine ⟨Finset.mem_image.mpr ⟨p, hpp, rfl⟩, ?_⟩
    have htwo : 1 < (positiveDifferenceRepresentations A (p.1 - p.2)).card := by
      apply Finset.one_lt_card.mpr
      refine ⟨p, mem_positiveDifferenceRepresentations.mpr ⟨hpp, rfl⟩,
        (p.2, p.2 - (p.1 - p.2)), ?_, ?_⟩
      · apply mem_positiveDifferenceRepresentations.mpr
        constructor
        · apply mem_positivePairs.mpr
          exact ⟨hpb, hpl, by omega⟩
        · change p.2 - (p.2 - (p.1 - p.2)) = p.1 - p.2
          omega
      · intro heq
        have heq' := congrArg Prod.fst heq
        change p.1 = p.2 at heq'
        omega
    change 2 ≤ (positiveDifferenceRepresentations A (p.1 - p.2)).card
    omega

/-- At most `card A - 2` positive differences are repeated. -/
theorem isWeakSidon_repeatedDifferences_card_le {A : Finset ℕ}
    (hA : IsWeakSidon A) (hcard : 2 ≤ A.card) :
    (weakRepeatedDifferences A).card ≤ A.card - 2 := by
  rw [weakRepeatedDifferences_eq_image hA]
  exact Finset.card_image_le.trans (weakExtraPairs_card_le_sub_two hA hcard)

end Sidon30
