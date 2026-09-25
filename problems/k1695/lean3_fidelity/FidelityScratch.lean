import K1695.CyclicVectorThree

open scoped Matrix
open Matrix

namespace K1695Lean3Fidelity

-- Concrete invertible inputs in three different fields.
def rationalMatrix : Matrix (Fin 3) (Fin 3) ℚ :=
  1

def modTwoMatrix : Matrix (Fin 3) (Fin 3) (ZMod 2) :=
  1

def modThreeMatrix : Matrix (Fin 3) (Fin 3) (ZMod 3) :=
  1

def singularRationalMatrix : Matrix (Fin 3) (Fin 3) ℚ :=
  0

example : IsUnit rationalMatrix.det := by
  simp [rationalMatrix]

example : IsUnit modTwoMatrix.det := by
  simp [modTwoMatrix]

example : IsUnit modThreeMatrix.det := by
  simp [modThreeMatrix]

-- `Equiv.Perm (Fin 3)` is the full six-element symmetric group.
example : Fintype.card (Equiv.Perm (Fin 3)) = 6 := by
  native_decide

example : ∃ σ : Equiv.Perm (Fin 3), ∃ v : Fin 3 → ℚ,
    LinearIndependent ℚ
      ![v, (rationalMatrix * σ.permMatrix ℚ) *ᵥ v,
        (rationalMatrix * σ.permMatrix ℚ) *ᵥ
          ((rationalMatrix * σ.permMatrix ℚ) *ᵥ v)] := by
  apply K1695.kourovka_16_95_n3_cyclic_vector rationalMatrix
  simp [rationalMatrix]

example : ∃ σ : Equiv.Perm (Fin 3), ∃ v : Fin 3 → ZMod 2,
    LinearIndependent (ZMod 2)
      ![v, (modTwoMatrix * σ.permMatrix (ZMod 2)) *ᵥ v,
        (modTwoMatrix * σ.permMatrix (ZMod 2)) *ᵥ
          ((modTwoMatrix * σ.permMatrix (ZMod 2)) *ᵥ v)] := by
  apply K1695.kourovka_16_95_n3_cyclic_vector modTwoMatrix
  simp [modTwoMatrix]

example : ∃ σ : Equiv.Perm (Fin 3), ∃ v : Fin 3 → ZMod 3,
    LinearIndependent (ZMod 3)
      ![v, (modThreeMatrix * σ.permMatrix (ZMod 3)) *ᵥ v,
        (modThreeMatrix * σ.permMatrix (ZMod 3)) *ᵥ
          ((modThreeMatrix * σ.permMatrix (ZMod 3)) *ᵥ v)] := by
  apply K1695.kourovka_16_95_n3_cyclic_vector modThreeMatrix
  simp [modThreeMatrix]

-- The noninvertible control has determinant zero, so the theorem's sole
-- matrix hypothesis cannot be supplied.
example : ¬IsUnit singularRationalMatrix.det := by
  simp [singularRationalMatrix]

-- Partial application visibly leaves the impossible invertibility premise.
#check K1695.kourovka_16_95_n3_cyclic_vector singularRationalMatrix

-- Selected statement checks requested by the fidelity ticket.
#check @K1695.kourovka_16_95_n3_cyclic_vector
#check @K1695.kourovka_16_95_n3_every_coordinate
#check @K1695.t2_rank_two_matrix
#check @K1695.t2_six_choices_scalar

-- Independent axiom print for every theorem declaration in the imported file.
#print axioms K1695.mul_permMatrix_apply
#print axioms K1695.matrixOfCols2_mulVec
#print axioms K1695.detCols2_control_identity
#print axioms K1695.ctrl2_iff_detCols2_ne_zero
#print axioms K1695.linearIndependent_pair_iff_detCols2_ne_zero
#print axioms K1695.linearIndependent_e0_of_det_dropFirst_ne_zero
#print axioms K1695.ctrl3_e0_of_ctrl2_lowerBlock
#print axioms K1695.ctrl3_conjugate
#print axioms K1695.swap_permMatrix_mulVec_e0
#print axioms K1695.exists_pair_coordinates
#print axioms K1695.t2_six_choices_scalar
#print axioms K1695.t2_six_choices_of_first_pair
#print axioms K1695.t2_three_columns_of_pair
#print axioms K1695.exists_independent_column_pair_of_rank_eq_two
#print axioms K1695.t2_rank_two_matrix
#print axioms K1695.rank_deleteFirstRow_eq_two
#print axioms K1695.kourovka_16_95_n3_e0
#print axioms K1695.kourovka_16_95_n3_every_coordinate
#print axioms K1695.kourovka_16_95_n3_cyclic_vector

end K1695Lean3Fidelity
