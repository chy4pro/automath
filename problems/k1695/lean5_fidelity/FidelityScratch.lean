import K1695.CyclicToMinpoly

open scoped Matrix

open Matrix Polynomial

-- Independent axiom audit for every theorem declared in CyclicToMinpoly.lean.
#print axioms K1695.minpoly_eq_charpoly_of_krylov_linearIndependent
#print axioms K1695.kourovka_16_95_n3
#print axioms K1695.krylov_feedback_linearIndependent
#print axioms K1695.deleteCoordinate_mulVec
#print axioms K1695.cyclic_standardBasis_of_principalBlock

-- Fully elaborated public types; these expose any hidden typeclass parameters.
#check @K1695.minpoly_eq_charpoly_of_krylov_linearIndependent
#check @K1695.kourovka_16_95_n3
#check @K1695.cyclic_standardBasis_of_principalBlock

-- Mathlib's right-permutation convention: output column j is input column sigma.symm j.
example {K : Type*} [Field K] (A : Matrix (Fin 3) (Fin 3) K)
    (σ : Equiv.Perm (Fin 3)) (i j : Fin 3) :
    (A * σ.permMatrix K) i j = A i (σ.symm j) :=
  K1695.mul_permMatrix_apply A σ i j

-- The quantifier really ranges over all six permutations of Fin 3.
example : Fintype.card (Equiv.Perm (Fin 3)) = 6 := by decide

def rationalMatrix : Matrix (Fin 3) (Fin 3) ℚ := 1

def zmod2Matrix : Matrix (Fin 3) (Fin 3) (ZMod 2) := 1

def zmod3Matrix : Matrix (Fin 3) (Fin 3) (ZMod 3) := 1

example : IsUnit rationalMatrix.det := by
  simp [rationalMatrix]

example : IsUnit zmod2Matrix.det := by
  simp [zmod2Matrix]

example : IsUnit zmod3Matrix.det := by
  simp [zmod3Matrix]

example : ∃ σ : Equiv.Perm (Fin 3),
    minpoly ℚ (rationalMatrix * σ.permMatrix ℚ) =
      (rationalMatrix * σ.permMatrix ℚ).charpoly :=
  K1695.kourovka_16_95_n3 rationalMatrix (by
    simp [rationalMatrix])

example : ∃ σ : Equiv.Perm (Fin 3),
    minpoly (ZMod 2) (zmod2Matrix * σ.permMatrix (ZMod 2)) =
      (zmod2Matrix * σ.permMatrix (ZMod 2)).charpoly :=
  K1695.kourovka_16_95_n3 zmod2Matrix (by
    simp [zmod2Matrix])

example : ∃ σ : Equiv.Perm (Fin 3),
    minpoly (ZMod 3) (zmod3Matrix * σ.permMatrix (ZMod 3)) =
      (zmod3Matrix * σ.permMatrix (ZMod 3)).charpoly :=
  K1695.kourovka_16_95_n3 zmod3Matrix (by
    simp [zmod3Matrix])

def singularRationalMatrix : Matrix (Fin 3) (Fin 3) ℚ := 0

example : ¬ IsUnit singularRationalMatrix.det := by
  simp [singularRationalMatrix]

-- For this concrete singular matrix the notebook conclusion itself is false, so the
-- invertibility hypothesis is not merely an artifact of the proof interface.
example : ¬ ∃ σ : Equiv.Perm (Fin 3),
    minpoly ℚ (singularRationalMatrix * σ.permMatrix ℚ) =
      (singularRationalMatrix * σ.permMatrix ℚ).charpoly := by
  rintro ⟨σ, hσ⟩
  simp [singularRationalMatrix, Matrix.charpoly_zero] at hσ
  have hcoeff := congrArg (fun p : ℚ[X] => p.coeff 1) hσ
  norm_num at hcoeff
