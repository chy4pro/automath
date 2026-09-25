import Ext677
import Mathlib.Algebra.Order.Archimedean.Basic
import Mathlib.Tactic

/-!
# The R46 amplification reduction

E255 density is multiplicative under direct products. Consequently, one finite E677
magma with an E255 defect produces finite E677 magmas of arbitrarily small E255 density.
-/

namespace Ext677

universe u v

/-- The coordinatewise product of two explicitly presented magma operations. -/
def directProductOp {M : Type u} {N : Type v} (opM : M → M → M)
    (opN : N → N → N) : M × N → M × N → M × N
  | (x, y), (x', y') => (opM x x', opN y y')

/-- The rational density of points satisfying E255 in a finite magma. -/
noncomputable def E255Density {M : Type u} [Finite M] (op : M → M → M) : ℚ :=
  (Nat.card {x : M // E255At op x} : ℚ) / (Nat.card M : ℚ)

/-- A1: E255 at a point of a direct product is the conjunction of its coordinates. -/
theorem amplify_product_E255At {M : Type u} {N : Type v}
    (opM : M → M → M) (opN : N → N → N) (x : M) (y : N) :
    E255At (directProductOp opM opN) (x, y) ↔
      E255At opM x ∧ E255At opN y := by
  simp [E255At, directProductOp]

/-- A2: E677 is preserved by direct products. -/
theorem amplify_product_E677 {M : Type u} {N : Type v}
    (opM : M → M → M) (opN : N → N → N)
    (hM : E677 opM) (hN : E677 opN) :
    E677 (directProductOp opM opN) := by
  rintro ⟨x, y⟩ ⟨x', y'⟩
  apply Prod.ext
  · simpa only [directProductOp] using hM x x'
  · simpa only [directProductOp] using hN y y'

/-- A2: E255 is preserved by direct products. -/
theorem amplify_product_E255 {M : Type u} {N : Type v}
    (opM : M → M → M) (opN : N → N → N)
    (hM : E255 opM) (hN : E255 opN) :
    E255 (directProductOp opM opN) := by
  rintro ⟨x, y⟩
  exact (amplify_product_E255At opM opN x y).2 ⟨hM x, hN y⟩

/-- E255 points in a direct product are exactly pairs of E255 points. -/
def e255ProductEquiv {M : Type u} {N : Type v}
    (opM : M → M → M) (opN : N → N → N) :
    {p : M × N // E255At (directProductOp opM opN) p} ≃
      {x : M // E255At opM x} × {y : N // E255At opN y} where
  toFun p :=
    ⟨⟨p.1.1, (amplify_product_E255At opM opN p.1.1 p.1.2).1 p.2 |>.1⟩,
      ⟨p.1.2, (amplify_product_E255At opM opN p.1.1 p.1.2).1 p.2 |>.2⟩⟩
  invFun p :=
    ⟨(p.1.1, p.2.1),
      (amplify_product_E255At opM opN p.1.1 p.2.1).2 ⟨p.1.2, p.2.2⟩⟩
  left_inv p := by
    apply Subtype.ext
    rfl
  right_inv p := by
    apply Prod.ext <;> apply Subtype.ext <;> rfl

/-- A3: E255 density is multiplicative under finite direct products. -/
theorem amplify_density_product {M : Type u} {N : Type v} [Finite M] [Finite N]
    (opM : M → M → M) (opN : N → N → N) :
    E255Density (directProductOp opM opN) = E255Density opM * E255Density opN := by
  have hgood :
      Nat.card {p : M × N // E255At (directProductOp opM opN) p} =
        Nat.card {x : M // E255At opM x} * Nat.card {y : N // E255At opN y} := by
    rw [Nat.card_congr (e255ProductEquiv opM opN), Nat.card_prod]
  have hsubM : Nat.card {x : M // E255At opM x} ≤ Nat.card M :=
    Nat.card_le_card_of_injective Subtype.val Subtype.val_injective
  have hsubN : Nat.card {y : N // E255At opN y} ≤ Nat.card N :=
    Nat.card_le_card_of_injective Subtype.val Subtype.val_injective
  unfold E255Density
  rw [hgood, Nat.card_prod]
  push_cast
  by_cases hMcard : Nat.card M = 0
  · have hMgood : Nat.card {x : M // E255At opM x} = 0 := by omega
    simp [hMcard, hMgood]
  by_cases hNcard : Nat.card N = 0
  · have hNgood : Nat.card {y : N // E255At opN y} = 0 := by omega
    simp [hNcard, hNgood]
  · have hMcardQ : (Nat.card M : ℚ) ≠ 0 := by exact_mod_cast hMcard
    have hNcardQ : (Nat.card N : ℚ) ≠ 0 := by exact_mod_cast hNcard
    field_simp

/-- The coordinatewise magma operation on the finite power `Fin k → A`. -/
def powerOp {A : Type u} (op : A → A → A) {k : ℕ} :
    (Fin k → A) → (Fin k → A) → (Fin k → A) :=
  fun x y i => op (x i) (y i)

/-- E255 at a point of a finite power is pointwise E255. -/
theorem amplify_power_E255At {A : Type u} (op : A → A → A) (k : ℕ)
    (x : Fin k → A) :
    E255At (powerOp op) x ↔ ∀ i, E255At op (x i) := by
  constructor
  · intro h i
    exact congrFun h i
  · intro h
    funext i
    exact h i

/-- E255 points in a finite power are functions into the E255 subtype. -/
def e255PowerEquiv {A : Type u} (op : A → A → A) (k : ℕ) :
    {x : Fin k → A // E255At (powerOp op) x} ≃
      (Fin k → {a : A // E255At op a}) where
  toFun x i := ⟨x.1 i, (amplify_power_E255At op k x.1).1 x.2 i⟩
  invFun x := ⟨fun i => (x i).1,
    (amplify_power_E255At op k (fun i => (x i).1)).2 (fun i => (x i).2)⟩
  left_inv x := by
    apply Subtype.ext
    rfl
  right_inv x := by
    funext i
    apply Subtype.ext
    rfl

/-- E677 is preserved by every finite power. -/
theorem amplify_power_E677 {A : Type u} (op : A → A → A) (h677 : E677 op) (k : ℕ) :
    E677 (powerOp op (k := k)) := by
  intro x y
  funext i
  exact h677 (x i) (y i)

/-- E255 is preserved by every finite power. -/
theorem amplify_power_E255 {A : Type u} (op : A → A → A) (h255 : E255 op) (k : ℕ) :
    E255 (powerOp op (k := k)) := by
  intro x
  exact (amplify_power_E255At op k x).2 fun i => h255 (x i)

/-- E255 density of a finite power is the corresponding power of the density. -/
theorem amplify_density_power {A : Type u} [Finite A] (op : A → A → A) (k : ℕ) :
    E255Density (powerOp op (k := k)) = E255Density op ^ k := by
  have hgood :
      Nat.card {x : Fin k → A // E255At (powerOp op) x} =
        Nat.card {a : A // E255At op a} ^ k := by
    rw [Nat.card_congr (e255PowerEquiv op k), Nat.card_fun, Nat.card_fin]
  unfold E255Density
  rw [hgood, Nat.card_fun, Nat.card_fin]
  push_cast
  exact (div_pow (Nat.card {a : A // E255At op a} : ℚ) (Nat.card A : ℚ) k).symm

/-- A single failure of E255 makes the E255 density strictly less than one. -/
theorem amplify_density_lt_one_of_not_E255At {A : Type u} [Finite A]
    (op : A → A → A) (x : A) (hx : ¬ E255At op x) :
    E255Density op < 1 := by
  classical
  let _ : Nonempty A := ⟨x⟩
  let _ : Fintype A := Fintype.ofFinite A
  have hcard : Fintype.card {a : A // E255At op a} < Fintype.card A :=
    Fintype.card_subtype_lt hx
  unfold E255Density
  rw [Nat.card_eq_fintype_card, Nat.card_eq_fintype_card, div_lt_one]
  · exact_mod_cast hcard
  · exact_mod_cast Fintype.card_pos

/-- A4: one finite E677 magma of density below one yields arbitrarily sparse examples. -/
theorem amplify_arbitrarily_sparse {A : Type u} [Finite A]
    (op : A → A → A) (h677 : E677 op) (hdensity : E255Density op < 1) :
    ∀ ε : ℚ, 0 < ε →
      ∃ (M : Type u) (_ : Finite M) (opM : M → M → M),
        E677 opM ∧ E255Density opM < ε := by
  intro ε hε
  obtain ⟨k, hk⟩ := exists_pow_lt_of_lt_one hε hdensity
  let M := Fin k → A
  let opM : M → M → M := powerOp op
  refine ⟨M, inferInstance, opM, ?_, ?_⟩
  · exact amplify_power_E677 op h677 k
  · simpa only [M, opM, amplify_density_power] using hk

/-- A5': a positive uniform E255-density lower bound forces E255 everywhere. -/
theorem amplify_uniform_lower_bound_forces_E255
    (c : ℚ) (hc : 0 < c)
    (hlower : ∀ {M : Type u} [Finite M] (opM : M → M → M),
      E677 opM → c ≤ E255Density opM) :
    ∀ {M : Type u} [Finite M] (opM : M → M → M), E677 opM → E255 opM := by
  intro M _ opM h677
  by_contra h255
  simp only [E255, not_forall] at h255
  obtain ⟨x, hx⟩ := h255
  let _ : Nonempty M := ⟨x⟩
  have hdensity : E255Density opM < 1 :=
    amplify_density_lt_one_of_not_E255At opM x hx
  obtain ⟨P, hPfinite, opP, hP677, hPsparse⟩ :=
    amplify_arbitrarily_sparse opM h677 hdensity c hc
  let _ : Finite P := hPfinite
  exact (not_lt_of_ge (hlower opP hP677)) hPsparse

#print axioms amplify_product_E255At
#print axioms amplify_product_E677
#print axioms amplify_product_E255
#print axioms amplify_density_product
#print axioms amplify_power_E255At
#print axioms amplify_power_E677
#print axioms amplify_power_E255
#print axioms amplify_density_power
#print axioms amplify_density_lt_one_of_not_E255At
#print axioms amplify_arbitrarily_sparse
#print axioms amplify_uniform_lower_bound_forces_E255

end Ext677
