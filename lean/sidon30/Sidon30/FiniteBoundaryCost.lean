import Sidon30.FiniteBoundaryPotential
import Sidon30.CorrectionFiniteMass
import Sidon30.CorrectionFiniteL1

/-!
The cost of the concrete finite signed boundary certificate. All sums are
finite. The pointwise renewal error estimate is an explicit input, supplied
by the renewal contraction theorem when the final bound is assembled.
-/

noncomputable section
open scoped BigOperators

namespace Sidon30

def boundarySupport (N T : ℕ) : Finset ℤ :=
  Finset.Icc (1 - (T : ℤ)) ((N : ℤ) + (T : ℤ) - 2)

def boundaryWindow (N : ℕ) : Finset ℤ :=
  Finset.Icc 0 ((N : ℤ) - 1)

def boundaryTailFactor (N T : ℕ) : ℝ :=
  ((3 : ℝ) / 4) ^ ((N - 1) / T)

def boundaryEnergy (N T : ℕ) : ℝ :=
  ∑ x ∈ boundarySupport N T, ∑ y ∈ boundarySupport N T,
    boundaryCertificate N T x * boundaryCertificate N T y *
      rampCorrelation T (x - y)

theorem boundaryTailFactor_nonneg (N T : ℕ) : 0 ≤ boundaryTailFactor N T := by
  unfold boundaryTailFactor
  positivity

private theorem cost_pow_le_one (n : ℕ) : ((3 : ℝ) / 4) ^ n ≤ 1 := by
  induction n with
  | zero => norm_num
  | succ n ih =>
      rw [pow_succ]
      have hn : 0 ≤ ((3 : ℝ) / 4) ^ n := by positivity
      nlinarith

private theorem cost_pow_antitone {a b : ℕ} (hab : a ≤ b) :
    ((3 : ℝ) / 4) ^ b ≤ ((3 : ℝ) / 4) ^ a := by
  have hb : b = a + (b - a) := by omega
  rw [hb, pow_add]
  have h := mul_le_mul_of_nonneg_left (cost_pow_le_one (b - a))
    (show 0 ≤ ((3 : ℝ) / 4) ^ a by positivity)
  simpa only [mul_one] using h

theorem renewalCorrection_tail_le {N T : ℕ} (hN : 1 ≤ N)
    (hq : ∀ n : ℕ, 1 ≤ n →
      |renewalCorrection T n| ≤ ((3 : ℝ) / 4) ^ ((n - 1) / T))
    {n : ℕ} (hn : N ≤ n) :
    |renewalCorrection T n| ≤ boundaryTailFactor N T := by
  apply le_trans (hq n (by omega))
  unfold boundaryTailFactor
  apply cost_pow_antitone
  exact Nat.div_le_div_right (by omega : N - 1 ≤ n - 1)

private theorem cost_clip_zero_neg (T M : ℕ) {y : ℤ} (hy : y < 0) :
    clippedCorrection T M y = 0 := by
  unfold clippedCorrection
  split_ifs <;> simp only [renewalCorrectionInt_of_neg T hy]

private theorem cost_clip_zero_outside (T M : ℕ) {y : ℤ}
    (hy : y ∉ Finset.Icc (0 : ℤ) (M : ℤ)) : clippedCorrection T M y = 0 := by
  by_cases hneg : y < 0
  · exact cost_clip_zero_neg T M hneg
  · have hhi : ¬ y ≤ (M : ℤ) := by
      intro h
      exact hy (Finset.mem_Icc.mpr ⟨by omega, h⟩)
    simp only [clippedCorrection, if_neg hhi]

theorem clippedCorrection_tail_le {N T : ℕ} (hN : 1 ≤ N)
    (hq : ∀ n : ℕ, 1 ≤ n →
      |renewalCorrection T n| ≤ ((3 : ℝ) / 4) ^ ((n - 1) / T))
    (M : ℕ) {y : ℤ} (hy : (N : ℤ) ≤ y) :
    |clippedCorrection T M y| ≤ boundaryTailFactor N T := by
  unfold clippedCorrection
  split_ifs with hM
  · have hy0 : 0 ≤ y := by omega
    rw [renewalCorrectionInt, if_pos hy0]
    exact renewalCorrection_tail_le hN hq (by omega)
  · simpa only [abs_zero] using boundaryTailFactor_nonneg N T

theorem boundaryWindow_subset {N T : ℕ} (hT : 1 ≤ T) :
    boundaryWindow N ⊆ boundarySupport N T := by
  intro y hy
  have hy' := Finset.mem_Icc.mp hy
  apply Finset.mem_Icc.mpr
  constructor <;> omega

private theorem cost_prefix_subset {N T : ℕ} (hN : 1 ≤ N) (hT : 1 ≤ T) :
    Finset.Icc (0 : ℤ) (boundaryCutoff N T : ℤ) ⊆ boundarySupport N T := by
  intro y hy
  have hy' := Finset.mem_Icc.mp hy
  have hc := boundaryCutoff_cast hN hT
  apply Finset.mem_Icc.mpr
  constructor <;> omega

theorem clippedCorrection_boundary_support {N T : ℕ} (hN : 1 ≤ N)
    (hT : 1 ≤ T) (y : ℤ) (hy : y ∉ boundarySupport N T) :
    clippedCorrection T (boundaryCutoff N T) y = 0 := by
  apply cost_clip_zero_outside
  exact fun h => hy (cost_prefix_subset hN hT h)

theorem boundarySupport_reflect_mem {N T : ℕ} {y : ℤ} :
    (N : ℤ) - 1 - y ∈ boundarySupport N T ↔ y ∈ boundarySupport N T := by
  simp only [boundarySupport, Finset.mem_Icc]
  omega

theorem reflectedCorrection_boundary_support {N T : ℕ} (hN : 1 ≤ N)
    (hT : 1 ≤ T) (y : ℤ) (hy : y ∉ boundarySupport N T) :
    clippedCorrection T (boundaryCutoff N T) ((N : ℤ) - 1 - y) = 0 := by
  apply clippedCorrection_boundary_support hN hT
  exact fun h => hy (boundarySupport_reflect_mem.mp h)

theorem sum_boundary_reflect (N T : ℕ) (F : ℤ → ℝ) :
    (∑ y ∈ boundarySupport N T, F ((N : ℤ) - 1 - y)) =
      ∑ y ∈ boundarySupport N T, F y := by
  refine Finset.sum_bij (fun y _ => (N : ℤ) - 1 - y) ?_ ?_ ?_ ?_
  · intro y hy
    exact boundarySupport_reflect_mem.mpr hy
  · intro a _ha b _hb hab
    omega
  · intro y hy
    refine ⟨(N : ℤ) - 1 - y, boundarySupport_reflect_mem.mpr hy, ?_⟩
    omega
  · intro y _hy
    rfl

private theorem cost_sum_clip_prefix (T M : ℕ) (F : ℝ → ℝ) :
    (∑ y ∈ Finset.Icc (0 : ℤ) (M : ℤ), F (clippedCorrection T M y)) =
      ∑ n ∈ Finset.range (M + 1), F (renewalCorrection T n) := by
  refine Finset.sum_bij (fun y _ => y.toNat) ?_ ?_ ?_ ?_
  · intro y hy
    have hy' := Finset.mem_Icc.mp hy
    apply Finset.mem_range.mpr
    omega
  · intro a ha b hb hab
    have ha' := Finset.mem_Icc.mp ha
    have hb' := Finset.mem_Icc.mp hb
    omega
  · intro n hn
    have hn' := Finset.mem_range.mp hn
    refine ⟨(n : ℤ), Finset.mem_Icc.mpr ⟨by omega, by omega⟩, ?_⟩
    simp
  · intro y hy
    have hy' := Finset.mem_Icc.mp hy
    simp only [clippedCorrection, if_pos hy'.2, renewalCorrectionInt, if_pos hy'.1]

theorem sum_clippedCorrection_boundary {N T : ℕ} (hN : 1 ≤ N) (hT : 1 ≤ T)
    (F : ℝ → ℝ) (hF : F 0 = 0) :
    (∑ y ∈ boundarySupport N T,
      F (clippedCorrection T (boundaryCutoff N T) y)) =
      ∑ n ∈ Finset.range (boundaryCutoff N T + 1), F (renewalCorrection T n) := by
  calc
    _ = ∑ y ∈ Finset.Icc (0 : ℤ) (boundaryCutoff N T : ℤ),
        F (clippedCorrection T (boundaryCutoff N T) y) := by
      apply Finset.sum_congr_of_eq_on_inter
      · intro y _hy hnot
        rw [cost_clip_zero_outside T (boundaryCutoff N T) hnot, hF]
      · intro y hy hnot
        exact False.elim (hnot (cost_prefix_subset hN hT hy))
      · intro y _hy _hy'
        rfl
    _ = _ := cost_sum_clip_prefix T (boundaryCutoff N T) F

theorem card_boundaryWindow (N : ℕ) : (boundaryWindow N).card = N := by
  rw [boundaryWindow, Int.card_Icc]
  omega

theorem card_boundarySupport {N T : ℕ} (hN : 1 ≤ N) (hT : 1 ≤ T) :
    (boundarySupport N T).card = N + 2 * (T - 1) := by
  rw [boundarySupport, Int.card_Icc]
  omega

theorem card_boundaryOutside {N T : ℕ} (hN : 1 ≤ N) (hT : 1 ≤ T) :
    (boundarySupport N T \ boundaryWindow N).card = 2 * (T - 1) := by
  rw [Finset.card_sdiff_of_subset (boundaryWindow_subset hT),
    card_boundarySupport hN hT, card_boundaryWindow]
  omega

private theorem cost_sum_indicator {N T : ℕ} (hT : 1 ≤ T) :
    (∑ y ∈ boundarySupport N T,
      if 0 ≤ y ∧ y ≤ (N : ℤ) - 1 then (1 : ℝ) else 0) = (N : ℝ) := by
  calc
    _ = ∑ _y ∈ boundaryWindow N, (1 : ℝ) := by
      apply Finset.sum_congr_of_eq_on_inter
      · intro y _hy hnot
        have h : ¬ (0 ≤ y ∧ y ≤ (N : ℤ) - 1) :=
          fun h => hnot (Finset.mem_Icc.mpr h)
        simp only [if_neg h]
      · intro y hy hnot
        exact False.elim (hnot (boundaryWindow_subset hT hy))
      · intro y _hy hyW
        exact if_pos (Finset.mem_Icc.mp hyW)
    _ = _ := by simp only [Finset.sum_const, card_boundaryWindow, nsmul_eq_mul, mul_one]

/-- Exact signed mass; index zero of both corrections is included. -/
theorem boundaryCertificate_mass {N T : ℕ} (hN : 1 ≤ N) (hT : 1 ≤ T) :
    (∑ y ∈ boundarySupport N T, boundaryCertificate N T y) =
      (N : ℝ) + 2 * correctionPrefixMass T (boundaryCutoff N T) := by
  simp only [boundaryCertificate, Finset.sum_add_distrib]
  rw [cost_sum_indicator hT,
    sum_boundary_reflect N T (clippedCorrection T (boundaryCutoff N T))]
  simp only [sum_clippedCorrection_boundary hN hT (fun z => z) rfl]
  change (N : ℝ) + correctionPrefixMass T (boundaryCutoff N T) +
    correctionPrefixMass T (boundaryCutoff N T) = _
  ring

theorem correctionPrefixMass_boundary_error {N T : ℕ} (hN : 1 ≤ N)
    (hT : 1 ≤ T)
    (hq : ∀ n : ℕ, 1 ≤ n →
      |renewalCorrection T n| ≤ ((3 : ℝ) / 4) ^ ((n - 1) / T)) :
    |correctionPrefixMass T (boundaryCutoff N T) - ((T : ℝ) - 1) / 3| ≤
      ((T : ℝ) - 1) / 3 * boundaryTailFactor N T := by
  have hM : T - 1 ≤ boundaryCutoff N T := by unfold boundaryCutoff; omega
  rw [correction_finite_mass hT hM]
  calc
    _ ≤ ∑ j ∈ Finset.range T,
        |rampWeight T j * (∑ n ∈ Finset.Icc (boundaryCutoff N T - j + 1)
          (boundaryCutoff N T), renewalCorrection T n)| :=
      Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ j ∈ Finset.range T, rampWeight T j * ((j : ℝ) * boundaryTailFactor N T) := by
      apply Finset.sum_le_sum
      intro j hj
      have hjT := Finset.mem_range.mp hj
      have hjM : j ≤ boundaryCutoff N T := by unfold boundaryCutoff; omega
      have hc : (Finset.Icc (boundaryCutoff N T - j + 1)
          (boundaryCutoff N T)).card = j := by
        rw [Nat.card_Icc]
        omega
      rw [abs_mul, abs_of_nonneg (rampWeight_nonneg T j)]
      apply mul_le_mul_of_nonneg_left _ (rampWeight_nonneg T j)
      calc
        _ ≤ ∑ n ∈ Finset.Icc (boundaryCutoff N T - j + 1)
            (boundaryCutoff N T), |renewalCorrection T n| :=
          Finset.abs_sum_le_sum_abs _ _
        _ ≤ ∑ _n ∈ Finset.Icc (boundaryCutoff N T - j + 1)
            (boundaryCutoff N T), boundaryTailFactor N T := by
          apply Finset.sum_le_sum
          intro n hn
          have hn' := Finset.mem_Icc.mp hn
          apply renewalCorrection_tail_le hN hq
          unfold boundaryCutoff at hn'
          omega
        _ = (j : ℝ) * boundaryTailFactor N T := by
          simp only [Finset.sum_const, hc, nsmul_eq_mul]
    _ = ((T : ℝ) - 1) / 3 * boundaryTailFactor N T := by
      calc
        _ = (∑ j ∈ Finset.range T, (j : ℝ) * rampWeight T j) *
            boundaryTailFactor N T := by
          rw [Finset.sum_mul]
          apply Finset.sum_congr rfl
          intro j _hj
          ring
        _ = _ := by rw [sum_mul_rampWeight hT]

/-- A kernel bound applied to a finite signed array, with explicit support. -/
theorem abs_rampDoublePotential_le_diagonal {T : ℕ} (hT : 1 ≤ T)
    (V : Finset ℤ) (μ : ℤ → ℝ) (hμ : ∀ y : ℤ, y ∉ V → μ y = 0) (x : ℤ) :
    |rampDoublePotential T μ x| ≤ rampDiagonal T * ∑ y ∈ V, |μ y| := by
  rw [← rampCorrelation_sum_eq_doublePotential_of_support T V μ x hμ]
  calc
    _ ≤ ∑ y ∈ V, |μ y * rampCorrelation T (x - y)| :=
      Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ y ∈ V, rampDiagonal T * |μ y| := by
      apply Finset.sum_le_sum
      intro y _hy
      rw [abs_mul, abs_of_nonneg (rampCorrelation_nonneg T (x - y))]
      calc
        _ ≤ |μ y| * rampDiagonal T :=
          mul_le_mul_of_nonneg_left (rampCorrelation_le_diagonal hT (x - y)) (abs_nonneg _)
        _ = _ := by ring
    _ = _ := (Finset.mul_sum V (fun y => |μ y|) (rampDiagonal T)).symm

private theorem cost_diagonal_nine_halves {T : ℕ} (hT : 1 ≤ T) :
    rampDiagonal T * ((9 : ℝ) / 2 * (T : ℝ)) ≤ 6 := by
  have hTpos : (0 : ℝ) < (T : ℝ) := by exact_mod_cast (show 0 < T by omega)
  have h := (le_div_iff₀ (by positivity : (0 : ℝ) < 3 * (T : ℝ))).mp
    (rampDiagonal_le hT)
  nlinarith

theorem clippedCorrection_potential_le_six {N T : ℕ} (hN : 1 ≤ N)
    (hT : 1 ≤ T)
    (hq : ∀ n : ℕ, 1 ≤ n →
      |renewalCorrection T n| ≤ ((3 : ℝ) / 4) ^ ((n - 1) / T)) (x : ℤ) :
    |rampDoublePotential T (clippedCorrection T (boundaryCutoff N T)) x| ≤ 6 := by
  calc
    _ ≤ rampDiagonal T * ∑ y ∈ boundarySupport N T,
        |clippedCorrection T (boundaryCutoff N T) y| :=
      abs_rampDoublePotential_le_diagonal hT _ _
        (clippedCorrection_boundary_support hN hT) x
    _ ≤ rampDiagonal T * ((9 : ℝ) / 2 * (T : ℝ)) := by
      apply mul_le_mul_of_nonneg_left _ (rampDiagonal_nonneg T)
      rw [sum_clippedCorrection_boundary hN hT abs (abs_zero)]
      exact sum_abs_renewalCorrection_le_nine_halves hT hq (boundaryCutoff N T)
    _ ≤ 6 := cost_diagonal_nine_halves hT

theorem reflectedCorrection_potential_le_six {N T : ℕ} (hN : 1 ≤ N)
    (hT : 1 ≤ T)
    (hq : ∀ n : ℕ, 1 ≤ n →
      |renewalCorrection T n| ≤ ((3 : ℝ) / 4) ^ ((n - 1) / T)) (x : ℤ) :
    |rampDoublePotential T
      (fun y => clippedCorrection T (boundaryCutoff N T) ((N : ℤ) - 1 - y)) x| ≤ 6 := by
  calc
    _ ≤ rampDiagonal T * ∑ y ∈ boundarySupport N T,
        |clippedCorrection T (boundaryCutoff N T) ((N : ℤ) - 1 - y)| :=
      abs_rampDoublePotential_le_diagonal hT _ _
        (reflectedCorrection_boundary_support hN hT) x
    _ ≤ rampDiagonal T * ((9 : ℝ) / 2 * (T : ℝ)) := by
      apply mul_le_mul_of_nonneg_left _ (rampDiagonal_nonneg T)
      rw [sum_boundary_reflect N T (fun y => |clippedCorrection T (boundaryCutoff N T) y|),
        sum_clippedCorrection_boundary hN hT abs abs_zero]
      exact sum_abs_renewalCorrection_le_nine_halves hT hq (boundaryCutoff N T)
    _ ≤ 6 := cost_diagonal_nine_halves hT

private theorem cost_indicator_potential {N T : ℕ} (hT : 1 ≤ T) (x : ℤ) :
    |rampDoublePotential T
      (fun y => if 0 ≤ y ∧ y ≤ (N : ℤ) - 1 then 1 else 0) x| ≤ 1 := by
  have hnonneg : 0 ≤ rampDoublePotential T
      (fun y => if 0 ≤ y ∧ y ≤ (N : ℤ) - 1 then 1 else 0) x := by
    unfold rampDoublePotential
    apply Finset.sum_nonneg
    intro i _hi
    apply Finset.sum_nonneg
    intro j _hj
    exact mul_nonneg (mul_nonneg (rampWeight_nonneg T i) (rampWeight_nonneg T j))
      (by split_ifs <;> norm_num)
  rw [abs_of_nonneg hnonneg]
  calc
    _ ≤ rampDoublePotential T (fun _ => 1) x := by
      unfold rampDoublePotential
      apply Finset.sum_le_sum
      intro i _hi
      apply Finset.sum_le_sum
      intro j _hj
      apply mul_le_mul_of_nonneg_left _
        (mul_nonneg (rampWeight_nonneg T i) (rampWeight_nonneg T j))
      split_ifs <;> norm_num
    _ = 1 := rampDoublePotential_const hT 1 x

/-- A global potential bound, including points outside the window. -/
theorem boundaryCertificate_potential_abs_le {N T : ℕ} (hN : 1 ≤ N)
    (hT : 1 ≤ T)
    (hq : ∀ n : ℕ, 1 ≤ n →
      |renewalCorrection T n| ≤ ((3 : ℝ) / 4) ^ ((n - 1) / T)) (x : ℤ) :
    |rampDoublePotential T (boundaryCertificate N T) x| ≤ 13 := by
  have heq : rampDoublePotential T (boundaryCertificate N T) x =
      rampDoublePotential T (fun y => if 0 ≤ y ∧ y ≤ (N : ℤ) - 1 then 1 else 0) x +
      rampDoublePotential T (clippedCorrection T (boundaryCutoff N T)) x +
      rampDoublePotential T
        (fun y => clippedCorrection T (boundaryCutoff N T) ((N : ℤ) - 1 - y)) x := by
    simp only [rampDoublePotential, boundaryCertificate, mul_add, Finset.sum_add_distrib]
  rw [heq]
  have h1 := cost_indicator_potential (N := N) hT x
  have h2 := clippedCorrection_potential_le_six hN hT hq x
  have h3 := reflectedCorrection_potential_le_six hN hT hq x
  have h12 := abs_add_le
    (rampDoublePotential T (fun y => if 0 ≤ y ∧ y ≤ (N : ℤ) - 1 then 1 else 0) x)
    (rampDoublePotential T (clippedCorrection T (boundaryCutoff N T)) x)
  have h123 := abs_add_le
    (rampDoublePotential T (fun y => if 0 ≤ y ∧ y ≤ (N : ℤ) - 1 then 1 else 0) x +
      rampDoublePotential T (clippedCorrection T (boundaryCutoff N T)) x)
    (rampDoublePotential T
      (fun y => clippedCorrection T (boundaryCutoff N T) ((N : ℤ) - 1 - y)) x)
  linarith

theorem boundaryCertificate_outside_pointwise {N T : ℕ} (hN : 1 ≤ N)
    (hq : ∀ n : ℕ, 1 ≤ n →
      |renewalCorrection T n| ≤ ((3 : ℝ) / 4) ^ ((n - 1) / T))
    {x : ℤ} (hx : x ∉ boundaryWindow N) :
    |boundaryCertificate N T x| ≤ boundaryTailFactor N T := by
  have hwindow : ¬ (0 ≤ x ∧ x ≤ (N : ℤ) - 1) :=
    fun h => hx (Finset.mem_Icc.mpr h)
  unfold boundaryCertificate
  rw [if_neg hwindow, zero_add]
  by_cases hxneg : x < 0
  · rw [cost_clip_zero_neg T (boundaryCutoff N T) hxneg, zero_add]
    exact clippedCorrection_tail_le hN hq (boundaryCutoff N T) (by omega)
  · have hxN : (N : ℤ) ≤ x := by omega
    rw [cost_clip_zero_neg T (boundaryCutoff N T)
      (by omega : (N : ℤ) - 1 - x < 0), add_zero]
    exact clippedCorrection_tail_le hN hq (boundaryCutoff N T) hxN

theorem boundaryCertificate_outside_l1 {N T : ℕ} (hN : 1 ≤ N) (hT : 1 ≤ T)
    (hq : ∀ n : ℕ, 1 ≤ n →
      |renewalCorrection T n| ≤ ((3 : ℝ) / 4) ^ ((n - 1) / T)) :
    (∑ x ∈ boundarySupport N T \ boundaryWindow N, |boundaryCertificate N T x|) ≤
      2 * ((T : ℝ) - 1) * boundaryTailFactor N T := by
  calc
    _ ≤ ∑ _x ∈ boundarySupport N T \ boundaryWindow N, boundaryTailFactor N T := by
      apply Finset.sum_le_sum
      intro x hx
      exact boundaryCertificate_outside_pointwise hN hq (Finset.mem_sdiff.mp hx).2
    _ = _ := by
      simp only [Finset.sum_const, card_boundaryOutside hN hT, nsmul_eq_mul]
      rw [Nat.cast_mul, Nat.cast_sub hT]
      norm_num

theorem boundaryEnergy_eq_potential_sum {N T : ℕ} (hN : 1 ≤ N) (hT : 1 ≤ T) :
    boundaryEnergy N T = ∑ x ∈ boundarySupport N T,
      boundaryCertificate N T x * rampDoublePotential T (boundaryCertificate N T) x := by
  unfold boundaryEnergy
  apply Finset.sum_congr rfl
  intro x _hx
  rw [← rampCorrelation_sum_eq_doublePotential_of_support T (boundarySupport N T)
    (boundaryCertificate N T) x
    (fun y hy => boundaryCertificate_eq_zero_of_not_mem hN hT hy), Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro y _hy
  ring

/-- Only the two exterior collars contribute to the energy-minus-mass error. -/
theorem boundaryEnergy_mass_error {N T : ℕ} (hN : 1 ≤ N) (hT : 1 ≤ T)
    (hq : ∀ n : ℕ, 1 ≤ n →
      |renewalCorrection T n| ≤ ((3 : ℝ) / 4) ^ ((n - 1) / T)) :
    |boundaryEnergy N T - ∑ x ∈ boundarySupport N T, boundaryCertificate N T x| ≤
      28 * ((T : ℝ) - 1) * boundaryTailFactor N T := by
  have herr : boundaryEnergy N T - ∑ x ∈ boundarySupport N T, boundaryCertificate N T x =
      ∑ x ∈ boundarySupport N T \ boundaryWindow N,
        boundaryCertificate N T x *
          (rampDoublePotential T (boundaryCertificate N T) x - 1) := by
    rw [boundaryEnergy_eq_potential_sum hN hT, ← Finset.sum_sub_distrib]
    calc
      _ = ∑ x ∈ boundarySupport N T, boundaryCertificate N T x *
          (rampDoublePotential T (boundaryCertificate N T) x - 1) := by
        apply Finset.sum_congr rfl
        intro x _hx
        ring
      _ = _ := by
        apply Finset.sum_congr_of_eq_on_inter
        · intro x hx hnot
          have hxW : x ∈ boundaryWindow N := by
            by_contra h
            exact hnot (Finset.mem_sdiff.mpr ⟨hx, h⟩)
          have hx' := Finset.mem_Icc.mp hxW
          rw [boundaryCertificate_potential hN hT hx'.1 hx'.2, sub_self, mul_zero]
        · intro x hx hnot
          exact False.elim (hnot (Finset.mem_sdiff.mp hx).1)
        · intro x _hx _hx'
          rfl
  rw [herr]
  calc
    _ ≤ ∑ x ∈ boundarySupport N T \ boundaryWindow N,
        |boundaryCertificate N T x *
          (rampDoublePotential T (boundaryCertificate N T) x - 1)| :=
      Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ x ∈ boundarySupport N T \ boundaryWindow N, 14 * |boundaryCertificate N T x| := by
      apply Finset.sum_le_sum
      intro x _hx
      have hp := boundaryCertificate_potential_abs_le hN hT hq x
      have ha := abs_add_le (rampDoublePotential T (boundaryCertificate N T) x) (-1 : ℝ)
      have hd : |rampDoublePotential T (boundaryCertificate N T) x - 1| ≤ 14 := by
        norm_num at ha
        linarith
      rw [abs_mul]
      calc
        _ ≤ |boundaryCertificate N T x| * 14 :=
          mul_le_mul_of_nonneg_left hd (abs_nonneg _)
        _ = _ := by ring
    _ = 14 * ∑ x ∈ boundarySupport N T \ boundaryWindow N, |boundaryCertificate N T x| :=
      (Finset.mul_sum _ _ _).symm
    _ ≤ 14 * (2 * ((T : ℝ) - 1) * boundaryTailFactor N T) :=
      mul_le_mul_of_nonneg_left (boundaryCertificate_outside_l1 hN hT hq) (by norm_num)
    _ = _ := by ring

/-- The cost of the actual finite signed certificate. The only analytic input
is the displayed pointwise renewal bound; all mass and boundary errors above
are finite identities or finite inequalities. -/
theorem boundaryCertificate_energy_le {N T : ℕ} (hN : 1 ≤ N) (hT : 1 ≤ T)
    (hq : ∀ n : ℕ, 1 ≤ n →
      |renewalCorrection T n| ≤ ((3 : ℝ) / 4) ^ ((n - 1) / T)) :
    boundaryEnergy N T ≤ (N : ℝ) + (2 : ℝ) / 3 * ((T : ℝ) - 1) +
      29 * (T : ℝ) * ((3 : ℝ) / 4) ^ ((N - 1) / T) := by
  have hmass := correctionPrefixMass_boundary_error hN hT hq
  have hmassup := (le_abs_self
    (correctionPrefixMass T (boundaryCutoff N T) - ((T : ℝ) - 1) / 3)).trans hmass
  have henergy := boundaryEnergy_mass_error hN hT hq
  have henergyup := (le_abs_self
    (boundaryEnergy N T - ∑ x ∈ boundarySupport N T, boundaryCertificate N T x)).trans henergy
  rw [boundaryCertificate_mass hN hT] at henergyup
  have htail := boundaryTailFactor_nonneg N T
  have hTreal : (1 : ℝ) ≤ (T : ℝ) := by exact_mod_cast hT
  have hcoeff : (2 * (((T : ℝ) - 1) / 3) + 28 * ((T : ℝ) - 1)) * boundaryTailFactor N T ≤
      (29 * (T : ℝ)) * boundaryTailFactor N T := by
    apply mul_le_mul_of_nonneg_right _ htail
    linarith
  change boundaryEnergy N T ≤ (N : ℝ) + (2 : ℝ) / 3 * ((T : ℝ) - 1) +
    29 * (T : ℝ) * boundaryTailFactor N T
  nlinarith

end Sidon30

end
