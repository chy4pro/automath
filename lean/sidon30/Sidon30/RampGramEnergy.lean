import Sidon30.CorrelationFacts
import Sidon30.FiniteEnergyCS

/-!
Identification of a finite ramp Gram kernel with the ramp autocorrelation.
Every support inclusion is explicit. For a cross energy it suffices to cover
the shifted supports of the left coefficient array; identifying both self
energies in Cauchy--Schwarz requires the corresponding inclusion for each array.
-/

noncomputable section

open scoped BigOperators

namespace Sidon30

/-- The integer support of a ramp shifted to start at `x`. -/
def shiftedRampSupport (T : ℕ) (x : ℤ) : Finset ℤ :=
  (Finset.range T).image (fun j : ℕ => x + (j : ℤ))

theorem mem_shiftedRampSupport {T : ℕ} {x z : ℤ} :
    z ∈ shiftedRampSupport T x ↔ 0 ≤ z - x ∧ z - x < (T : ℤ) := by
  unfold shiftedRampSupport
  constructor
  · intro hz
    obtain ⟨j, hj, heq⟩ := Finset.mem_image.mp hz
    have hjlt : j < T := Finset.mem_range.mp hj
    constructor <;> omega
  · rintro ⟨h0, hT⟩
    apply Finset.mem_image.mpr
    refine ⟨(z - x).toNat, ?_, ?_⟩
    · apply Finset.mem_range.mpr
      omega
    · omega

theorem rampWeightInt_eq_zero_of_not_shiftedSupport (T : ℕ) (x z : ℤ)
    (hz : z ∉ shiftedRampSupport T x) :
    rampWeightInt T (z - x) = 0 := by
  by_cases h0 : 0 ≤ z - x
  · have hT : (T : ℤ) ≤ z - x := by
      by_contra h
      exact hz (mem_shiftedRampSupport.mpr ⟨h0, lt_of_not_ge h⟩)
    exact rampWeightInt_eq_zero_of_le hT
  · exact rampWeightInt_eq_zero_of_neg (lt_of_not_ge h0)

/-- The Gram kernel is the autocorrelation once `Z` covers the first ramp's
shifted support. No positivity or location assumption on `x` or `y` is needed. -/
theorem rampGramKernel_eq (T : ℕ) (Z : Finset ℤ) (x y : ℤ)
    (hZ : ∀ j ∈ Finset.range T, x + (j : ℤ) ∈ Z) :
    finiteGramKernel Z (fun z u : ℤ => rampWeightInt T (z - u)) x y =
      rampCorrelation T (x - y) := by
  have hsubset : shiftedRampSupport T x ⊆ Z := by
    intro z hz
    obtain ⟨j, hj, rfl⟩ := Finset.mem_image.mp hz
    exact hZ j hj
  have hinj : Set.InjOn (fun j : ℕ => x + (j : ℤ))
      (↑(Finset.range T) : Set ℕ) := by
    intro i _hi j _hj hij
    omega
  have hsum :
      (∑ z ∈ shiftedRampSupport T x,
        rampWeightInt T (z - x) * rampWeightInt T (z - y)) =
      ∑ z ∈ Z, rampWeightInt T (z - x) * rampWeightInt T (z - y) := by
    apply Finset.sum_subset hsubset
    intro z _hz hnot
    rw [rampWeightInt_eq_zero_of_not_shiftedSupport T x z hnot, zero_mul]
  unfold finiteGramKernel
  calc
    (∑ z ∈ Z, rampWeightInt T (z - x) * rampWeightInt T (z - y)) =
        ∑ z ∈ shiftedRampSupport T x,
          rampWeightInt T (z - x) * rampWeightInt T (z - y) := hsum.symm
    _ = ∑ j ∈ Finset.range T,
          rampWeightInt T (x + (j : ℤ) - x) *
            rampWeightInt T (x + (j : ℤ) - y) := Finset.sum_image hinj
    _ = rampCorrelation T (x - y) := by
      unfold rampCorrelation
      apply Finset.sum_congr rfl
      intro j _hj
      have hfirst : x + (j : ℤ) - x = (j : ℤ) := by ring
      have hsecond : x + (j : ℤ) - y = (j : ℤ) + (x - y) := by ring
      rw [hfirst, hsecond, rampWeightInt_natCast]

/-- A canonical finite outer interval for a ramp starting between `lo` and `hi`. -/
theorem rampGramKernel_Icc (T : ℕ) (lo hi x y : ℤ)
    (hxlo : lo ≤ x) (hxhi : x ≤ hi) :
    finiteGramKernel (Finset.Icc lo (hi + (T : ℤ) - 1))
        (fun z u : ℤ => rampWeightInt T (z - u)) x y =
      rampCorrelation T (x - y) := by
  apply rampGramKernel_eq
  intro j hj
  have hjlt : j < T := Finset.mem_range.mp hj
  apply Finset.mem_Icc.mpr
  constructor <;> omega

/-- The signed-array energy bridge, with every finite support displayed. -/
theorem rampGramEnergy_eq (T : ℕ) (Z S V : Finset ℤ) (μ ν : ℤ → ℝ)
    (hZ : ∀ x ∈ S, ∀ j ∈ Finset.range T, x + (j : ℤ) ∈ Z) :
    finiteGramEnergy Z S V (fun z x : ℤ => rampWeightInt T (z - x)) μ ν =
      ∑ x ∈ S, ∑ y ∈ V, μ x * ν y * rampCorrelation T (x - y) := by
  rw [finiteGramEnergy_eq_kernel_sum]
  apply Finset.sum_congr rfl
  intro x hx
  apply Finset.sum_congr rfl
  intro y _hy
  rw [rampGramKernel_eq T Z x y (hZ x hx)]

/-- Interval specialization of the signed-array energy bridge. -/
theorem rampGramEnergy_Icc (T : ℕ) (lo hi : ℤ) (S V : Finset ℤ)
    (μ ν : ℤ → ℝ) (hS : ∀ x ∈ S, lo ≤ x ∧ x ≤ hi) :
    finiteGramEnergy (Finset.Icc lo (hi + (T : ℤ) - 1)) S V
        (fun z x : ℤ => rampWeightInt T (z - x)) μ ν =
      ∑ x ∈ S, ∑ y ∈ V, μ x * ν y * rampCorrelation T (x - y) := by
  apply rampGramEnergy_eq
  intro x hx j hj
  obtain ⟨hxlo, hxhi⟩ := hS x hx
  have hjlt : j < T := Finset.mem_range.mp hj
  apply Finset.mem_Icc.mpr
  constructor <;> omega

/-- The ramp potential as a finite double convolution. The coefficient array
need not be finitely supported, since only the displayed finite values are used. -/
def rampDoublePotential (T : ℕ) (μ : ℤ → ℝ) (x : ℤ) : ℝ :=
  ∑ i ∈ Finset.range T, ∑ j ∈ Finset.range T,
    rampWeight T i * rampWeight T j * μ (x + (i : ℤ) - (j : ℤ))

/-- A finite correlation-kernel sum equals the double convolution whenever
its summation set contains every location sampled by that convolution. -/
theorem rampCorrelation_sum_eq_doublePotential (T : ℕ) (V : Finset ℤ)
    (μ : ℤ → ℝ) (x : ℤ)
    (hV : ∀ i ∈ Finset.range T, ∀ j ∈ Finset.range T,
      x + (i : ℤ) - (j : ℤ) ∈ V) :
    (∑ y ∈ V, μ y * rampCorrelation T (x - y)) = rampDoublePotential T μ x := by
  calc
    (∑ y ∈ V, μ y * rampCorrelation T (x - y)) =
        ∑ y ∈ V, ∑ i ∈ Finset.range T, ∑ j ∈ Finset.range T,
          μ y * (if (j : ℤ) - (i : ℤ) = x - y then
            rampWeight T i * rampWeight T j else 0) := by
      apply Finset.sum_congr rfl
      intro y _hy
      rw [rampCorrelation_eq_double]
      simp_rw [Finset.mul_sum]
    _ = ∑ i ∈ Finset.range T, ∑ j ∈ Finset.range T, ∑ y ∈ V,
          μ y * (if (j : ℤ) - (i : ℤ) = x - y then
            rampWeight T i * rampWeight T j else 0) := by
      rw [Finset.sum_comm]
      apply Finset.sum_congr rfl
      intro i _hi
      rw [Finset.sum_comm]
    _ = rampDoublePotential T μ x := by
      unfold rampDoublePotential
      apply Finset.sum_congr rfl
      intro i hi
      apply Finset.sum_congr rfl
      intro j hj
      have hs := Finset.sum_eq_single_of_mem
        (f := fun y : ℤ => μ y *
          (if (j : ℤ) - (i : ℤ) = x - y then
            rampWeight T i * rampWeight T j else 0))
        (x + (i : ℤ) - (j : ℤ)) (hV i hi j hj)
        (by
          intro y _hy hne
          have hdiff : (j : ℤ) - (i : ℤ) ≠ x - y := by omega
          simp only [if_neg hdiff, mul_zero])
      have hselected : (j : ℤ) - (i : ℤ) =
          x - (x + (i : ℤ) - (j : ℤ)) := by ring
      rw [hs, if_pos hselected]
      ring

end Sidon30

end
