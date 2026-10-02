import Sidon30.Basic

/-!
Positive natural differences for the strong Sidon convention in Basic.
All subtraction below is natural subtraction, and its operands are
strictly ordered whenever it represents a positive difference.

This file has not been locally compiled; validation is delegated to CI.
-/

namespace Sidon30

/-- Each strictly positive natural difference has at most one ordered representation. -/
def UniquePositiveDifferences (A : Finset ℕ) : Prop :=
  ∀ a ∈ A, ∀ b ∈ A, ∀ c ∈ A, ∀ d ∈ A,
    b < a → d < c → a - b = c - d → a = c ∧ b = d

/-- The sum convention includes diagonal pairs; this is equivalent to
uniqueness of strictly positive differences. -/
theorem isSidon_iff_uniquePositiveDifferences (A : Finset ℕ) :
    IsSidon A ↔ UniquePositiveDifferences A := by
  constructor
  · intro hA a ha b hb c hc d hd hba hdc hdiff
    have hsum : a + d = c + b := by omega
    rcases le_total a d with had | hda
    · rcases le_total c b with hcb | hbc
      · obtain ⟨h₁, h₂⟩ := hA a ha d hd c hc b hb hsum had hcb
        constructor <;> omega
      · obtain ⟨h₁, h₂⟩ := hA a ha d hd b hb c hc (by omega) had hbc
        constructor <;> omega
    · rcases le_total c b with hcb | hbc
      · obtain ⟨h₁, h₂⟩ := hA d hd a ha c hc b hb (by omega) hda hcb
        constructor <;> omega
      · obtain ⟨h₁, h₂⟩ := hA d hd a ha b hb c hc (by omega) hda hbc
        constructor <;> omega
  · intro hA a ha b hb c hc d hd hsum hab hcd
    rcases lt_trichotomy a c with hac | hac | hca
    · have hdb : d < b := by omega
      have hdiff : c - a = b - d := by omega
      obtain ⟨h₁, h₂⟩ := hA c hc a ha b hb d hd hac hdb hdiff
      constructor <;> omega
    · constructor <;> omega
    · have hbd : b < d := by omega
      have hdiff : a - c = d - b := by omega
      obtain ⟨h₁, h₂⟩ := hA a ha c hc d hd b hb hca hbd hdiff
      constructor <;> omega

/-- Ordered pairs whose first coordinate is strictly larger than the second. -/
def positivePairs (A : Finset ℕ) : Finset (ℕ × ℕ) :=
  (A.product A).filter (fun p => p.2 < p.1)

@[simp]
theorem mem_positivePairs {A : Finset ℕ} {p : ℕ × ℕ} :
    p ∈ positivePairs A ↔ p.1 ∈ A ∧ p.2 ∈ A ∧ p.2 < p.1 := by
  simp only [positivePairs, Finset.mem_filter, Finset.mem_product, and_assoc]

/-- Natural subtraction is injective on the positive ordered pairs of a Sidon set. -/
theorem positiveDifference_injOn {A : Finset ℕ} (hA : IsSidon A) :
    Set.InjOn (fun p : ℕ × ℕ => p.1 - p.2)
      (↑(positivePairs A) : Set (ℕ × ℕ)) := by
  intro p hp q hq hpq
  rcases mem_positivePairs.mp hp with ⟨hpa, hpb, hplt⟩
  rcases mem_positivePairs.mp hq with ⟨hqa, hqb, hqlt⟩
  have h :=
    (isSidon_iff_uniquePositiveDifferences A).mp hA
      p.1 hpa p.2 hpb q.1 hqa q.2 hqb hplt hqlt hpq
  exact Prod.ext h.1 h.2

end Sidon30
