import Sidon30.TransferStatement
import Sidon30.SidonRampEnergy
import Sidon30.ShiftWindow

/-! Finite difference counting for bounded multiplicity, including the exact diagonal. -/

noncomputable section
open scoped BigOperators

namespace Sidon30

theorem isGThin_positiveDifferenceCount_le {g : ℕ} {A : Finset ℕ}
    (hA : IsGThin g A) (d : ℕ) : positiveDifferenceCount A d ≤ g := by
  by_cases hd : d = 0
  · subst d
    simp
  · have hdZ : (d : ℤ) ≠ 0 := by exact_mod_cast hd
    calc
      positiveDifferenceCount A d ≤
          ((A.product A).filter (fun p => (p.1 : ℤ) - (p.2 : ℤ) = (d : ℤ))).card := by
        apply Finset.card_le_card
        intro p hp
        obtain ⟨hpA, hdiff⟩ := mem_positiveDifferenceRepresentations.mp hp
        obtain ⟨ha, hb, hba⟩ := mem_positivePairs.mp hpA
        apply Finset.mem_filter.mpr
        constructor
        · exact Finset.mem_product.mpr ⟨ha, hb⟩
        · omega
      _ ≤ g := hA (d : ℤ) hdZ

/-- Reindex a finitely supported positive-pair sum by its difference fibers. -/
theorem positivePairSum_eq_countSum_of_support {A D : Finset ℕ}
    (w : ℕ → ℝ)
    (hcover : ∀ p ∈ positivePairs A, w (p.1 - p.2) ≠ 0 → p.1 - p.2 ∈ D) :
    (∑ p ∈ positivePairs A, w (p.1 - p.2)) =
      ∑ d ∈ D, (positiveDifferenceCount A d : ℝ) * w d := by
  have hinner : ∀ p ∈ positivePairs A,
      (∑ d ∈ D, if p.1 - p.2 = d then w d else 0) = w (p.1 - p.2) := by
    intro p hp
    calc
      _ = if p.1 - p.2 = p.1 - p.2 then w (p.1 - p.2) else 0 := by
        apply Finset.sum_eq_single (p.1 - p.2)
        · intro d _hd hne
          simp only [Ne.symm hne, if_false]
        · intro hnot
          have hz : w (p.1 - p.2) = 0 := by
            by_contra hn
            exact hnot (hcover p hp hn)
          simp only [hz, if_true]
      _ = _ := by simp
  calc
    _ = ∑ p ∈ positivePairs A, ∑ d ∈ D,
        if p.1 - p.2 = d then w d else 0 := by
      apply Finset.sum_congr rfl
      intro p hp
      exact (hinner p hp).symm
    _ = ∑ d ∈ D, ∑ p ∈ positivePairs A,
        if p.1 - p.2 = d then w d else 0 := Finset.sum_comm
    _ = _ := by
      apply Finset.sum_congr rfl
      intro d _hd
      rw [← Finset.sum_filter]
      change (∑ _p ∈ positiveDifferenceRepresentations A d, w d) = _
      simp only [Finset.sum_const, nsmul_eq_mul, positiveDifferenceCount]

theorem isGThin_positivePairSum_le_of_support {g : ℕ} {A D : Finset ℕ}
    (hA : IsGThin g A) (w : ℕ → ℝ)
    (hcover : ∀ p ∈ positivePairs A, w (p.1 - p.2) ≠ 0 → p.1 - p.2 ∈ D)
    (hnonneg : ∀ d ∈ D, 0 ≤ w d) :
    (∑ p ∈ positivePairs A, w (p.1 - p.2)) ≤ (g : ℝ) * ∑ d ∈ D, w d := by
  rw [positivePairSum_eq_countSum_of_support w hcover, Finset.mul_sum]
  apply Finset.sum_le_sum
  intro d hd
  have hc : (positiveDifferenceCount A d : ℝ) ≤ (g : ℝ) := by
    exact_mod_cast isGThin_positiveDifferenceCount_le hA d
  exact mul_le_mul_of_nonneg_right hc (hnonneg d hd)

/-- Nonzero differences cost at most g copies; the diagonal still costs one copy. -/
theorem isGThin_rampEnergy_le {g T : ℕ} {A : Finset ℕ}
    (hA : IsGThin g A) (hT : 1 ≤ T) :
    orderedPairEnergy A (rampCorrelation T) ≤
      (g : ℝ) + rampDiagonal T * ((A.card : ℝ) - (g : ℝ)) := by
  have hpairs := isGThin_positivePairSum_le_of_support
    (D := Finset.Icc 1 (T - 1)) hA (fun d => rampCorrelation T (d : ℤ))
    (by
      intro p hp hnz
      have hpos := (mem_positivePairs.mp hp).2.2
      apply Finset.mem_Icc.mpr
      constructor
      · omega
      · by_contra h
        have hlarge : T ≤ p.1 - p.2 := by omega
        apply hnz
        apply rampCorrelation_eq_zero_of_abs_le
        rw [abs_of_nonneg (by positivity : (0 : ℤ) ≤ ((p.1 - p.2 : ℕ) : ℤ))]
        exact_mod_cast hlarge)
    (by intro d _hd; exact rampCorrelation_nonneg T (d : ℤ))
  have hmass : 2 * (∑ d ∈ Finset.Icc 1 (T - 1), rampCorrelation T (d : ℤ)) =
      1 - rampDiagonal T := by
    rw [← sum_pos_rampCorrelation_eq_nat hT]
    exact two_mul_sum_pos_rampCorrelation hT
  have hmassg := congrArg (fun z : ℝ => (g : ℝ) * z) hmass
  rw [orderedPairEnergy_eq A (rampCorrelation T) (rampCorrelation_neg T),
    rampCorrelation_zero hT]
  nlinarith only [hpairs, hmassg]

theorem isGThin_shiftWindow {g N : ℕ} {A : Finset ℕ}
    (hA : IsGThin g A) (hAN : A ⊆ Finset.Icc 1 N) :
    IsGThin g (shiftWindow A) := by
  intro d hd
  let P := ((shiftWindow A).product (shiftWindow A)).filter
    (fun p => (p.1 : ℤ) - (p.2 : ℤ) = d)
  let Q := (A.product A).filter (fun p => (p.1 : ℤ) - (p.2 : ℤ) = d)
  let F : ℕ × ℕ → ℕ × ℕ := fun p => (p.1 + 1, p.2 + 1)
  have hpre : ∀ b ∈ shiftWindow A, b + 1 ∈ A := by
    intro b hb
    obtain ⟨a, ha, hab⟩ := mem_shiftWindow.mp hb
    have ha1 := (Finset.mem_Icc.mp (hAN ha)).1
    have heq : b + 1 = a := by omega
    rw [heq]
    exact ha
  have hinj : Set.InjOn F (↑P : Set (ℕ × ℕ)) := by
    intro p _hp q _hq hpq
    have h1 := congrArg Prod.fst hpq
    have h2 := congrArg Prod.snd hpq
    dsimp [F] at h1 h2
    apply Prod.ext <;> omega
  have hsub : P.image F ⊆ Q := by
    intro p hp
    obtain ⟨q, hq, rfl⟩ := Finset.mem_image.mp hp
    obtain ⟨hqmem, hqd⟩ := Finset.mem_filter.mp hq
    obtain ⟨hq1, hq2⟩ := Finset.mem_product.mp hqmem
    apply Finset.mem_filter.mpr
    constructor
    · exact Finset.mem_product.mpr ⟨hpre q.1 hq1, hpre q.2 hq2⟩
    · dsimp [F]
      omega
  change P.card ≤ g
  calc
    P.card = (P.image F).card := (Finset.card_image_of_injOn hinj).symm
    _ ≤ Q.card := Finset.card_le_card hsub
    _ ≤ g := hA d hd

end Sidon30

end
