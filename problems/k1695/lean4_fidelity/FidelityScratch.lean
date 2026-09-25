import K1695.TranspositionLemmaFull
import Mathlib.NumberTheory.Real.Irrational

open scoped Matrix
open Matrix

namespace Lean4Fidelity

noncomputable section

/- Concrete rank-two eigenspace examples for the full T2 equivalence. -/
def rankTwoE (R : Type*) [Field R] : Matrix (Fin 4) (Fin 4) R :=
  Matrix.diagonal ![0, 0, 1, 1]

def rankTwoA (R : Type*) [Field R] : Matrix (Fin 4) (Fin 4) R :=
  1 + rankTwoE R

lemma rankTwoA_sub_one (R : Type*) [Field R] :
    rankTwoA R - (1 : R) • (1 : Matrix (Fin 4) (Fin 4) R) = rankTwoE R := by
  simp [rankTwoA]

lemma rank_rankTwoE_rat : (rankTwoE ℚ).rank = 2 := by
  classical
  rw [rankTwoE, Matrix.rank_diagonal]
  native_decide

lemma rank_rankTwoE_zmod3 : (rankTwoE (ZMod 3)).rank = 2 := by
  classical
  rw [rankTwoE, Matrix.rank_diagonal]
  native_decide

lemma d01_not_mem_rankTwoE_range (R : Type*) [Field R] :
    K1695.transpositionVector (K := R) 0 1 ∉
      LinearMap.range (rankTwoE R).mulVecLin := by
  rintro ⟨x, hx⟩
  have h0 := congrFun hx 0
  simp [rankTwoE, Matrix.mulVec, dotProduct, Fin.sum_univ_four,
    K1695.transpositionVector] at h0

lemma d01_not_mem_rankTwoE_transpose_range (R : Type*) [Field R] :
    K1695.transpositionVector (K := R) 0 1 ∉
      LinearMap.range (rankTwoE R).transpose.mulVecLin := by
  simpa [rankTwoE] using d01_not_mem_rankTwoE_range R

example :
    ((rankTwoA ℚ) * K1695.transpositionMatrix (K := ℚ) 0 1 -
        (1 : ℚ) • 1).rank = 4 - 1 ↔
      K1695.transpositionVector (K := ℚ) 0 1 ∉
          LinearMap.range ((rankTwoA ℚ) - (1 : ℚ) • 1).mulVecLin ∧
        K1695.transpositionVector (K := ℚ) 0 1 ∉
          LinearMap.range ((rankTwoA ℚ) - (1 : ℚ) • 1).transpose.mulVecLin := by
  apply K1695.t2_rank_eq_iff_both_sides_not_mem
  · decide
  · norm_num
  · rw [rankTwoA_sub_one]
    exact rank_rankTwoE_rat

example :
    ((rankTwoA (ZMod 3)) * K1695.transpositionMatrix (K := ZMod 3) 0 1 -
        (1 : ZMod 3) • 1).rank = 4 - 1 ↔
      K1695.transpositionVector (K := ZMod 3) 0 1 ∉
          LinearMap.range ((rankTwoA (ZMod 3)) - (1 : ZMod 3) • 1).mulVecLin ∧
        K1695.transpositionVector (K := ZMod 3) 0 1 ∉
          LinearMap.range
            ((rankTwoA (ZMod 3)) - (1 : ZMod 3) • 1).transpose.mulVecLin := by
  apply K1695.t2_rank_eq_iff_both_sides_not_mem
  · decide
  · norm_num
  · rw [rankTwoA_sub_one]
    exact rank_rankTwoE_zmod3

example :
    ((rankTwoA ℚ) * K1695.transpositionMatrix (K := ℚ) 0 1 -
      (1 : ℚ) • 1).rank = 3 := by
  have hiff := K1695.t2_rank_eq_iff_both_sides_not_mem
    (rankTwoA ℚ) (1 : ℚ) (0 : Fin 4) (1 : Fin 4) (by decide) (by norm_num)
    (by rw [rankTwoA_sub_one]; exact rank_rankTwoE_rat)
  apply hiff.mpr
  constructor <;> rw [rankTwoA_sub_one]
  · exact d01_not_mem_rankTwoE_range ℚ
  · exact d01_not_mem_rankTwoE_transpose_range ℚ

example :
    ((rankTwoA (ZMod 3)) * K1695.transpositionMatrix (K := ZMod 3) 0 1 -
      (1 : ZMod 3) • 1).rank = 3 := by
  have hiff := K1695.t2_rank_eq_iff_both_sides_not_mem
    (rankTwoA (ZMod 3)) (1 : ZMod 3) (0 : Fin 4) (1 : Fin 4)
    (by decide) (by norm_num)
    (by rw [rankTwoA_sub_one]; exact rank_rankTwoE_zmod3)
  apply hiff.mpr
  constructor <;> rw [rankTwoA_sub_one]
  · exact d01_not_mem_rankTwoE_range (ZMod 3)
  · exact d01_not_mem_rankTwoE_transpose_range (ZMod 3)

/- Concrete general-degree easy-inclusion instances of T4. -/
def concreteA (R : Type*) [Field R] : Matrix (Fin 4) (Fin 4) R :=
  Matrix.diagonal ![0, 1, 1, 0]

def concreteVector (R : Type*) [Field R] : Fin 4 → R := ![1, 0, 1, 0]

example :
    (fun i => algebraMap ℚ ℚ
      (((Polynomial.aeval (concreteA ℚ) (minpoly ℚ (1 : ℚ))).mulVec
        (concreteVector ℚ)) i)) ∈
      LinearMap.range
        ((concreteA ℚ).map (algebraMap ℚ ℚ) - (1 : ℚ) • 1).mulVecLin :=
  K1695.t4_minpoly_mulVec_mem_range
    (concreteA ℚ) (1 : ℚ) (isIntegral_one : IsIntegral ℚ (1 : ℚ)) (concreteVector ℚ)

example :
    (fun i => algebraMap (ZMod 3) (ZMod 3)
      (((Polynomial.aeval (concreteA (ZMod 3)) (minpoly (ZMod 3) (1 : ZMod 3))).mulVec
        (concreteVector (ZMod 3))) i)) ∈
      LinearMap.range
        ((concreteA (ZMod 3)).map (algebraMap (ZMod 3) (ZMod 3)) -
          (1 : ZMod 3) • 1).mulVecLin :=
  K1695.t4_minpoly_mulVec_mem_range
    (concreteA (ZMod 3)) (1 : ZMod 3)
      (isIntegral_one : IsIntegral (ZMod 3) (1 : ZMod 3)) (concreteVector (ZMod 3))

/- The older quadratic hard-inclusion theorem has satisfiable hypotheses over Q. -/
example : ∃ q : Fin 4 → ℚ,
    (0 : Fin 4 → ℚ) =
      ((concreteA ℚ) * (concreteA ℚ) - 0 • (concreteA ℚ) - 2 • 1).mulVec q := by
  have hsqrt : Real.sqrt 2 ∉ Set.range (algebraMap ℚ ℝ) := by
    simpa [Irrational] using irrational_sqrt_two
  refine K1695.l7_quadratic_descent_with_decomposition
      (A := concreteA ℚ) (μ := Real.sqrt 2) hsqrt (2 : ℚ) (0 : ℚ) ?_
      (0 : Fin 4 → ℚ) (0 : Fin 4 → ℚ) (0 : Fin 4 → ℚ) (0 : Fin 4 → ℝ) ?_ ?_
  · norm_num [Real.mul_self_sqrt]
  · ext i
    simp
  · ext i
    simp [concreteA]

end

end Lean4Fidelity

/- Complete theorem-level axiom audit for both imported modules. -/
#print axioms K1695.l1_matrix_identity
#print axioms K1695.l1_mul_self
#print axioms K1695.l1_unit_inv
#print axioms K1695.l1_matrix_inv
#print axioms K1695.rank_mul_transposition
#print axioms K1695.smul_vecMulVec
#print axioms K1695.l2_rank_identity
#print axioms K1695.matrix_rank_add_le
#print axioms K1695.l3_rank_one_update_bounds
#print axioms K1695.exists_ker_dotProduct_ne_zero_of_not_mem_range_transpose
#print axioms K1695.l6a_rank_one_update_eq_add_one
#print axioms K1695.l6prime_t2_corrected
#print axioms K1695.one_mu_coefficients_eq_zero
#print axioms K1695.l7_quadratic_descent_with_decomposition
#print axioms K1695.l4_t0
#print axioms K1695.l5_t3_corrected

#print axioms K1695.dotProduct_eq_zero_of_mem_range_transpose_of_mulVec_eq_zero
#print axioms K1695.dotProduct_preimage_well_defined
#print axioms K1695.rank_one_update_le_of_left_mem
#print axioms K1695.rank_one_update_le_of_right_mem
#print axioms K1695.rank_one_update_le_of_one_side_mem
#print axioms K1695.rank_one_update_eq_of_left_not_mem_right_mem
#print axioms K1695.rank_one_update_eq_of_left_mem_right_not_mem
#print axioms K1695.rank_one_update_eq_sub_one
#print axioms K1695.rank_one_update_eq_of_preimage_scalar_ne_zero
#print axioms K1695.t2_rank_le_of_one_side_mem
#print axioms K1695.t2_rank_eq_iff_both_sides_not_mem
#print axioms K1695.t1_rank_drop_iff
#print axioms K1695.t4_minpoly_mulVec_mem_range
#print axioms K1695.cubic_coefficients_eq_zero
#print axioms K1695.t4_cubic_descent_with_decomposition
#print axioms K1695.t4_cubic_minpoly_descent_with_decomposition
