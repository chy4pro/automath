/-
Translation from the natural-number window {1, ..., N} to {0, ..., N - 1}.
The lower endpoint assumption prevents truncated subtraction from identifying points.
-/
import Sidon30.Basic

namespace Sidon30

/-- Shift a finite set down by one using natural-number subtraction. -/
def shiftWindow (A : Finset ℕ) : Finset ℕ :=
  A.image (fun a => a - 1)

@[simp]
theorem mem_shiftWindow {A : Finset ℕ} {b : ℕ} :
    b ∈ shiftWindow A ↔ ∃ a ∈ A, a - 1 = b := by
  simp only [shiftWindow, Finset.mem_image]

/-- Subtracting one is injective on a set contained in {1, ..., N}. -/
theorem shiftWindow_card {A : Finset ℕ} {N : ℕ}
    (hAN : A ⊆ Finset.Icc 1 N) :
    (shiftWindow A).card = A.card := by
  unfold shiftWindow
  apply Finset.card_image_of_injOn
  intro a ha b hb hab
  change a - 1 = b - 1 at hab
  have ha1 : 1 ≤ a := (Finset.mem_Icc.mp (hAN ha)).1
  have hb1 : 1 ≤ b := (Finset.mem_Icc.mp (hAN hb)).1
  omega

/-- The shifted set lies in the N-point window {0, ..., N - 1}. -/
theorem shiftWindow_subset_range {A : Finset ℕ} {N : ℕ}
    (hAN : A ⊆ Finset.Icc 1 N) :
    shiftWindow A ⊆ Finset.range N := by
  intro b hb
  rcases mem_shiftWindow.mp hb with ⟨a, ha, hshift⟩
  have ha1 : 1 ≤ a := (Finset.mem_Icc.mp (hAN ha)).1
  have haN : a ≤ N := (Finset.mem_Icc.mp (hAN ha)).2
  apply Finset.mem_range.mpr
  omega

/-- The shift preserves the sum-based Sidon condition, including diagonal sums. -/
theorem isSidon_shiftWindow {A : Finset ℕ} {N : ℕ}
    (hA : IsSidon A) (hAN : A ⊆ Finset.Icc 1 N) :
    IsSidon (shiftWindow A) := by
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
  have hxy : x ≤ y := by omega
  have huv : u ≤ v := by omega
  obtain ⟨hxu, hyv⟩ := hA x hx y hy u hu v hv hsum' hxy huv
  constructor <;> omega

end Sidon30
