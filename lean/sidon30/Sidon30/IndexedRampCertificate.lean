import Sidon30.TransferCertificate

/-! The same finite capacity bound for indexed row coordinates. Repeated
row values are allowed; the cardinality counts indices, not distinct rows. -/

noncomputable section
open scoped BigOperators

namespace Sidon30

theorem indexed_ramp_card_sq_le_certificate {ι : Type*}
    (N T : ℕ) (S : Finset ι) (y : ι → ℤ)
    (hN : 1 ≤ N) (hT : 1 ≤ T)
    (hy : ∀ i ∈ S, 0 ≤ y i ∧ y i ≤ (N : ℤ) - 1) :
    (S.card : ℝ) ^ 2 ≤
      ((N : ℝ) + (2 : ℝ) / 3 * ((T : ℝ) - 1) +
        29 * (T : ℝ) * ((3 : ℝ) / 4) ^ ((N - 1) / T)) *
      (∑ i ∈ S, ∑ j ∈ S, rampCorrelation T (y i - y j)) := by
  let V : Finset ℤ := Finset.Icc (1 - (T : ℤ)) ((N : ℤ) + (T : ℤ) - 2)
  let Z : Finset ℤ := Finset.Icc (1 - (T : ℤ)) ((N : ℤ) + 2 * (T : ℤ) - 3)
  let H : ℤ → ℤ → ℝ := fun z u => rampWeightInt T (z - u)
  let μ : ℤ → ℝ := finiteTransform S (fun z i => H z (y i)) (fun _ => 1)
  let ν : ℤ → ℝ := finiteTransform V H (boundaryCertificate N T)
  let C : ℝ := (N : ℝ) + (2 : ℝ) / 3 * ((T : ℝ) - 1) +
    29 * (T : ℝ) * ((3 : ℝ) / 4) ^ ((N - 1) / T)
  have hZV : ∀ x ∈ V, ∀ j ∈ Finset.range T, x + (j : ℤ) ∈ Z := by
    intro x hx j hj
    obtain ⟨hxlo, hxhi⟩ := Finset.mem_Icc.mp hx
    have hjT := Finset.mem_range.mp hj
    apply Finset.mem_Icc.mpr
    constructor <;> omega
  have hZS : ∀ i ∈ S, ∀ j ∈ Finset.range T, y i + (j : ℤ) ∈ Z := by
    intro i hi j hj
    apply hZV (y i) _ j hj
    obtain ⟨h0, h1⟩ := hy i hi
    apply Finset.mem_Icc.mpr
    constructor <;> omega
  have hsupport : ∀ q : ℤ, q ∉ V → boundaryCertificate N T q = 0 := by
    intro q hq
    exact boundaryCertificate_eq_zero_of_not_mem hN hT hq
  have hpotential : ∀ i ∈ S,
      (∑ q ∈ V, boundaryCertificate N T q * finiteGramKernel Z H (y i) q) = 1 := by
    intro i hi
    calc
      _ = ∑ q ∈ V, boundaryCertificate N T q * rampCorrelation T (y i - q) := by
        apply Finset.sum_congr rfl
        intro q _hq
        rw [show finiteGramKernel Z H (y i) q = rampCorrelation T (y i - q) from
          rampGramKernel_eq T Z (y i) q (hZS i hi)]
      _ = rampDoublePotential T (boundaryCertificate N T) (y i) :=
        rampCorrelation_sum_eq_doublePotential_of_support T V
          (boundaryCertificate N T) (y i) hsupport
      _ = 1 := boundaryCertificate_potential hN hT (hy i hi).1 (hy i hi).2
  have hcross : (∑ z ∈ Z, μ z * ν z) = (S.card : ℝ) := by
    calc
      _ = ∑ z ∈ Z, ∑ i ∈ S, ∑ q ∈ V,
          boundaryCertificate N T q * (H z (y i) * H z q) := by
        simp only [μ, ν, finiteTransform, mul_one, Finset.sum_mul_sum]
        apply Finset.sum_congr rfl
        intro z _hz
        apply Finset.sum_congr rfl
        intro i _hi
        apply Finset.sum_congr rfl
        intro q _hq
        ring
      _ = ∑ i ∈ S, ∑ q ∈ V, boundaryCertificate N T q *
          finiteGramKernel Z H (y i) q := by
        rw [Finset.sum_comm]
        apply Finset.sum_congr rfl
        intro i _hi
        rw [Finset.sum_comm]
        simp only [finiteGramKernel, Finset.mul_sum]
      _ = ∑ _i ∈ S, (1 : ℝ) := Finset.sum_congr rfl hpotential
      _ = _ := by simp
  have hself : (∑ z ∈ Z, μ z ^ 2) =
      ∑ i ∈ S, ∑ j ∈ S, rampCorrelation T (y i - y j) := by
    change (∑ z ∈ Z, (finiteTransform S (fun z i => H z (y i)) (fun _ => 1) z) ^ 2) = _
    rw [← finiteGramEnergy_self_eq_sum_sq]
    rw [finiteGramEnergy_eq_kernel_sum]
    simp only [one_mul]
    apply Finset.sum_congr rfl
    intro i hi
    apply Finset.sum_congr rfl
    intro j _hj
    exact rampGramKernel_eq T Z (y i) (y j) (hZS i hi)
  have hcost : (∑ z ∈ Z, ν z ^ 2) ≤ C := by
    change (∑ z ∈ Z, (finiteTransform V H (boundaryCertificate N T) z) ^ 2) ≤ C
    rw [← finiteGramEnergy_self_eq_sum_sq]
    rw [rampGramEnergy_eq T Z V V
      (boundaryCertificate N T) (boundaryCertificate N T) hZV]
    simpa only [boundaryEnergy, boundarySupport, C, V] using
      (boundaryCertificate_energy_le (N := N) (T := T) hN hT
        (fun n hn => renewalCorrection_bound hT hn))
  have hcs : (∑ z ∈ Z, μ z * ν z) ^ 2 ≤
      (∑ z ∈ Z, μ z ^ 2) * (∑ z ∈ Z, ν z ^ 2) := by
    simpa only [pow_two] using Finset.sum_mul_sq_le_sq_mul_sq Z μ ν
  have hnonneg : 0 ≤ ∑ z ∈ Z, μ z ^ 2 := Finset.sum_nonneg (fun z _ => sq_nonneg (μ z))
  have hbound := hcs.trans (mul_le_mul_of_nonneg_left hcost hnonneg)
  rw [hcross, hself] at hbound
  simpa only [mul_comm, C] using hbound

end Sidon30
end
