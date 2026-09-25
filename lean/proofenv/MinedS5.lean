/-
S5 UNIT-COST PROBE (corpus mining r3).
Source row : 2608.15525#1  (arXiv:2608.15525, "Concluding remarks", Conjecture 5.1(2))
Verbatim   : "Conjecture 5.1. Let G be a connected subcubic graph.
              ... (2) If G is cubic, then 8γ(G) ≤ 17ρ(G) + 7."
Paper's own definitions (abstract): γ(G) = domination number, ρ(G) = packing number.
NOTHING in Mathlib defines either, so both are authored here.
-/
import Mathlib

namespace MinedS5

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- `S` dominates: every vertex is in `S` or adjacent to a member of `S`. -/
def IsDominating (G : SimpleGraph V) (S : Finset V) : Prop :=
  ∀ v : V, v ∈ S ∨ ∃ u ∈ S, G.Adj u v

/-- `S` is a packing: distinct members have disjoint closed neighbourhoods. -/
def IsPacking (G : SimpleGraph V) (S : Finset V) : Prop :=
  ∀ u ∈ S, ∀ v ∈ S, u ≠ v →
    ∀ w : V, ¬ ((u = w ∨ G.Adj u w) ∧ (v = w ∨ G.Adj v w))

open scoped Classical in
/-- Domination number γ(G). -/
noncomputable def gamma (G : SimpleGraph V) : ℕ :=
  sInf {n | ∃ S : Finset V, IsDominating G S ∧ S.card = n}

open scoped Classical in
/-- Packing number ρ(G). -/
noncomputable def rho (G : SimpleGraph V) : ℕ :=
  sSup {n | ∃ S : Finset V, IsPacking G S ∧ S.card = n}

/-- arXiv:2608.15525, Conjecture 5.1(2). -/
theorem conj_5_1_2 (G : SimpleGraph V) [DecidableRel G.Adj]
    (hconn : G.Connected) (hcubic : ∀ v : V, G.degree v = 3) :
    8 * gamma G ≤ 17 * rho G + 7 := by
  sorry

-- fidelity self-checks: the two definitions must not be vacuous or trivial.
section Fidelity
variable (G : SimpleGraph V)

/-- The whole vertex set dominates: γ is a min over a nonempty set. -/
example : IsDominating G Finset.univ := fun v => Or.inl (Finset.mem_univ v)

/-- The empty set is a packing: ρ is a sup over a nonempty set. -/
example : IsPacking G (∅ : Finset V) := by
  intro u hu; exact absurd hu (Finset.notMem_empty u)

/-- A singleton is always a packing (so ρ ≥ 1 whenever V is nonempty). -/
example (x : V) : IsPacking G {x} := by
  intro u hu v hv hne
  rw [Finset.mem_singleton] at hu hv
  exact absurd (hu.trans hv.symm) hne

end Fidelity

end MinedS5
