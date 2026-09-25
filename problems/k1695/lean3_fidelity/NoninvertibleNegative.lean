import K1695.CyclicVectorThree

open scoped Matrix

def singularRationalMatrix : Matrix (Fin 3) (Fin 3) ℚ :=
  0

-- Intentionally ill-typed negative control: omitting the determinant-unit
-- proof must leave a function where an existential proposition is expected.
example : ∃ σ : Equiv.Perm (Fin 3), ∃ v : Fin 3 → ℚ,
    LinearIndependent ℚ
      ![v, (singularRationalMatrix * σ.permMatrix ℚ) *ᵥ v,
        (singularRationalMatrix * σ.permMatrix ℚ) *ᵥ
          ((singularRationalMatrix * σ.permMatrix ℚ) *ᵥ v)] :=
  K1695.kourovka_16_95_n3_cyclic_vector singularRationalMatrix
