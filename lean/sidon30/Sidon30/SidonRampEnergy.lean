import Sidon30.SidonEnergyUpper
import Sidon30.RampGramEnergy

/-!
The normalized Sidon energy bound for the actual ramp correlation, and its
identification with a finite Gram energy after embedding the natural set in Z.
-/

noncomputable section
open scoped BigOperators

namespace Sidon30

theorem sum_pos_rampCorrelation_eq_nat {T : ℕ} (hT : 1 ≤ T) :
    (∑ d ∈ Finset.Icc (1 : ℤ) ((T : ℤ) - 1), rampCorrelation T d) =
      ∑ d ∈ Finset.Icc 1 (T - 1), rampCorrelation T (d : ℤ) := by
  refine Finset.sum_bij (fun d _ => d.toNat) ?_ ?_ ?_ ?_
  · intro d hd
    have hd' := Finset.mem_Icc.mp hd
    apply Finset.mem_Icc.mpr
    constructor <;> omega
  · intro a ha b hb hab
    have ha' := Finset.mem_Icc.mp ha
    have hb' := Finset.mem_Icc.mp hb
    omega
  · intro d hd
    have hd' := Finset.mem_Icc.mp hd
    refine ⟨(d : ℤ), ?_, ?_⟩
    · apply Finset.mem_Icc.mpr
      constructor <;> omega
    · simp
  · intro d hd
    have hd' := Finset.mem_Icc.mp hd
    have hcast : (d.toNat : ℤ) = d := by omega
    rw [hcast]

/-- The generic Sidon count bound instantiated with the normalized ramp kernel. -/
theorem isSidon_rampEnergy_le {A : Finset ℕ} {T : ℕ}
    (hA : IsSidon A) (hT : 1 ≤ T) :
    orderedPairEnergy A (rampCorrelation T) ≤
      1 + rampDiagonal T * ((A.card : ℝ) - 1) := by
  apply isSidon_orderedPairEnergy_le_normalized
    (D := Finset.Icc 1 (T - 1)) hA (rampCorrelation T) (rampDiagonal T)
  · exact rampCorrelation_neg T
  · intro p hp hnz
    have hpos := (mem_positivePairs.mp hp).2.2
    apply Finset.mem_Icc.mpr
    constructor
    · omega
    · by_contra h
      have hlarge : T ≤ p.1 - p.2 := by omega
      apply hnz
      apply rampCorrelation_eq_zero_of_abs_le
      rw [abs_of_nonneg (by positivity : (0 : ℤ) ≤ ((p.1 - p.2 : ℕ) : ℤ))]
      exact_mod_cast hlarge
  · intro d _hd
    exact rampCorrelation_nonneg T (d : ℤ)
  · exact rampCorrelation_zero hT
  · rw [← sum_pos_rampCorrelation_eq_nat hT]
    exact two_mul_sum_pos_rampCorrelation hT

def liftedSidonSet (A : Finset ℕ) : Finset ℤ := A.image (fun a => (a : ℤ))

@[simp]
theorem mem_liftedSidonSet {A : Finset ℕ} {x : ℤ} :
    x ∈ liftedSidonSet A ↔ ∃ a ∈ A, (a : ℤ) = x := by
  simp only [liftedSidonSet, Finset.mem_image]

@[simp]
theorem liftedSidonSet_card (A : Finset ℕ) : (liftedSidonSet A).card = A.card := by
  unfold liftedSidonSet
  apply Finset.card_image_of_injOn
  intro a _ha b _hb hab
  change (a : ℤ) = (b : ℤ) at hab
  exact_mod_cast hab

theorem liftedSidonSet_mem_window {A : Finset ℕ} {N : ℕ}
    (hAN : A ⊆ Finset.range N) {x : ℤ} (hx : x ∈ liftedSidonSet A) :
    0 ≤ x ∧ x ≤ (N : ℤ) - 1 := by
  rcases mem_liftedSidonSet.mp hx with ⟨a, ha, rfl⟩
  have haN := Finset.mem_range.mp (hAN ha)
  constructor <;> omega

theorem liftedSidonSet_pairEnergy (A : Finset ℕ) (f : ℤ → ℝ) :
    (∑ x ∈ liftedSidonSet A, ∑ y ∈ liftedSidonSet A, f (x - y)) =
      orderedPairEnergy A f := by
  unfold liftedSidonSet orderedPairEnergy
  rw [Finset.sum_image]
  · apply Finset.sum_congr rfl
    intro a _ha
    rw [Finset.sum_image]
    intro b _hb c _hc hbc
    change (b : ℤ) = (c : ℤ) at hbc
    exact_mod_cast hbc
  · intro a _ha b _hb hab
    change (a : ℤ) = (b : ℤ) at hab
    exact_mod_cast hab

/-- The Sidon energy estimate in the same Gram representation as the certificate. -/
theorem rampGramEnergy_liftedSidon_le {A : Finset ℕ} {T : ℕ}
    (hA : IsSidon A) (hT : 1 ≤ T) (Z : Finset ℤ)
    (hZ : ∀ x ∈ liftedSidonSet A, ∀ j ∈ Finset.range T, x + (j : ℤ) ∈ Z) :
    finiteGramEnergy Z (liftedSidonSet A) (liftedSidonSet A)
        (fun z x : ℤ => rampWeightInt T (z - x)) (fun _ => 1) (fun _ => 1) ≤
      1 + rampDiagonal T * ((A.card : ℝ) - 1) := by
  rw [rampGramEnergy_eq T Z (liftedSidonSet A) (liftedSidonSet A)
    (fun _ => 1) (fun _ => 1) hZ]
  simp only [one_mul]
  rw [liftedSidonSet_pairEnergy]
  exact isSidon_rampEnergy_le hA hT

end Sidon30

end
