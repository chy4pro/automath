import Ext677
import Mathlib.Data.Finite.Prod
import Mathlib.Data.Setoid.Basic
import Mathlib.SetTheory.Cardinal.NatCard

/-!
# Quotient coordinatization and minimal-counterexample reduction for E677

This file supplies the two quotient links used by the finite extension reduction.
-/

namespace Ext677

open Function

universe u v

/-- L7a. A surjective magma homomorphism carries E677 to the target. -/
theorem L7a_E677_of_surjective_hom {M : Type u} {B : Type v}
    (opM : M → M → M) (opB : B → B → B) (hM : E677 opM)
    (f : M → B) (hf : Function.Surjective f) (hhom : IsMagmaHom opM opB f) :
    E677 opB := by
  intro x y
  obtain ⟨x', rfl⟩ := hf x
  obtain ⟨y', rfl⟩ := hf y
  calc
    f x' = f (opM y' (opM x' (opM (opM y' x') y'))) := congrArg f (hM x' y')
    _ = opB (f y') (opB (f x') (opB (opB (f y') (f x')) (f y'))) := by
      rw [hhom, hhom, hhom, hhom]

/-- L7. Equal finite fibres of a surjective E677 homomorphism give pair coordinates,
with permutation rows and the blueprint equation (4). -/
theorem L7_coordinatization {M : Type u} {B : Type v} [Finite M] [Finite B]
    (opM : M → M → M) (opB : B → B → B) (hM : E677 opM)
    (f : M → B) (hf : Function.Surjective f) (hhom : IsMagmaHom opM opB f)
    (m : ℕ) (hfibre : ∀ b : B, Nat.card {x : M // f x = b} = m) :
    ∃ (Fib : Type) (_ : Finite Fib) (e : M ≃ B × Fib)
      (c : B → B → Fib → Fib → Fib),
      Nat.card Fib = m ∧
      (∀ x, (e x).1 = f x) ∧
      (∀ x y, e (opM x y) = productOp opB c (e x) (e y)) ∧
      (∀ x y s, Function.Injective (c x y s)) ∧
      Eq4 opB (L7a_E677_of_surjective_hom opM opB hM f hf hhom) c := by
  classical
  let fibreEquiv : ∀ b : B, {x : M // f x = b} ≃ Fin m :=
    fun b => Finite.equivFinOfCardEq (hfibre b)
  let e : M ≃ B × Fin m :=
    (Equiv.sigmaFiberEquiv f).symm.trans (Equiv.sigmaEquivProdOfEquiv fibreEquiv)
  have he_fst (x : M) : (e x).1 = f x := by
    rfl
  let c : B → B → Fin m → Fin m → Fin m := fun x y s t =>
    (e (opM (e.symm (x, s)) (e.symm (y, t)))).2
  have he_op (x y : M) : e (opM x y) = productOp opB c (e x) (e y) := by
    apply Prod.ext
    · simp only [productOp]
      rw [he_fst, hhom, ← he_fst, ← he_fst]
    · simp only [productOp, c]
      rw [e.symm_apply_apply, e.symm_apply_apply]
  have hc_inj (x y : B) (s : Fin m) : Function.Injective (c x y s) := by
    intro t₁ t₂ ht
    let a := e.symm (x, s)
    let b₁ := e.symm (y, t₁)
    let b₂ := e.symm (y, t₂)
    have hop : opM a b₁ = opM a b₂ := by
      apply e.injective
      apply Prod.ext
      · rw [he_fst, he_fst, hhom, hhom]
        change opB (f (e.symm (x, s))) (f (e.symm (y, t₁))) =
          opB (f (e.symm (x, s))) (f (e.symm (y, t₂)))
        rw [← he_fst, ← he_fst, ← he_fst]
        simp
      · exact ht
    have hb : b₁ = b₂ := (L1_left_bij opM hM a).1 hop
    exact congrArg Prod.snd (e.symm.injective hb)
  have hprod : E677 (productOp opB c) := by
    intro p q
    simpa only [e.apply_symm_apply, he_op] using
      congrArg e (hM (e.symm p) (e.symm q))
  refine ⟨Fin m, inferInstance, e, c, ?_, he_fst, he_op, hc_inj, ?_⟩
  · simp
  · exact (L3_eq4_iff opB
      (L7a_E677_of_surjective_hom opM opB hM f hf hhom) c).mp hprod

#print axioms L7a_E677_of_surjective_hom
#print axioms L7_coordinatization

/-- Transport an explicit magma operation through an equivalence. -/
def transportOpEquiv {A : Type u} {C : Type v} (e : A ≃ C) (op : A → A → A) :
    C → C → C := fun x y => e (op (e.symm x) (e.symm y))

/-- E677 is invariant under transport by an equivalence. -/
theorem E677_transportOpEquiv {A : Type u} {C : Type v} (e : A ≃ C)
    (op : A → A → A) (h : E677 op) : E677 (transportOpEquiv e op) := by
  intro x y
  apply e.symm.injective
  simpa [transportOpEquiv] using h (e.symm x) (e.symm y)

/-- E255 is invariant under transport by an equivalence. -/
theorem E255_transportOpEquiv_iff {A : Type u} {C : Type v} (e : A ≃ C)
    (op : A → A → A) : E255 (transportOpEquiv e op) ↔ E255 op := by
  constructor
  · intro h x
    apply e.injective
    simpa [E255At, transportOpEquiv] using h (e x)
  · intro h x
    simpa [E255At, transportOpEquiv] using
      congrArg e (h (e.symm x))

/-- A congruence for an explicitly presented magma. -/
structure MagmaCongruence {N : Type u} (op : N → N → N) where
  toSetoid : Setoid N
  op_rel : ∀ {x x' y y'}, toSetoid.r x x' → toSetoid.r y y' →
    toSetoid.r (op x y) (op x' y')

abbrev MagmaCongruence.Rel {N : Type u} {op : N → N → N}
    (θ : MagmaCongruence op) : N → N → Prop := θ.toSetoid.r

/-- The carrier of the quotient by a magma congruence. -/
abbrev MagmaQuotient {N : Type u} {op : N → N → N} (θ : MagmaCongruence op) :=
  Quotient θ.toSetoid

/-- The canonical quotient map. -/
def quotientMap {N : Type u} {op : N → N → N} (θ : MagmaCongruence op) :
    N → MagmaQuotient θ := Quotient.mk θ.toSetoid

/-- The induced operation on a congruence quotient. -/
def quotientOp {N : Type u} {op : N → N → N} (θ : MagmaCongruence op) :
    MagmaQuotient θ → MagmaQuotient θ → MagmaQuotient θ :=
  Quotient.map₂ op fun _ _ hx _ _ hy => θ.op_rel hx hy

@[simp] theorem quotientOp_mk {N : Type u} {op : N → N → N}
    (θ : MagmaCongruence op) (x y : N) :
    quotientOp θ (quotientMap θ x) (quotientMap θ y) = quotientMap θ (op x y) := rfl

/-- The quotient map is a surjective magma homomorphism. -/
theorem quotientMap_surjective_hom {N : Type u} {op : N → N → N}
    (θ : MagmaCongruence op) :
    Function.Surjective (quotientMap θ) ∧ IsMagmaHom op (quotientOp θ) (quotientMap θ) := by
  exact ⟨Quotient.mk_surjective, fun _ _ => rfl⟩

/-- The equality congruence condition. -/
def MagmaCongruence.IsTrivial {N : Type u} {op : N → N → N}
    (θ : MagmaCongruence op) : Prop := ∀ x y, θ.Rel x y → x = y

/-- The universal congruence condition. -/
def MagmaCongruence.IsTotal {N : Type u} {op : N → N → N}
    (θ : MagmaCongruence op) : Prop := ∀ x y, θ.Rel x y

/-- An explicit magma is simple when every congruence is equality or universal. -/
def IsSimple {N : Type u} (op : N → N → N) : Prop :=
  ∀ θ : MagmaCongruence op, θ.IsTrivial ∨ θ.IsTotal

/-- An E677 counterexample to E255. -/
def IsCounterexample {N : Type u} (op : N → N → N) : Prop := E677 op ∧ ¬ E255 op

set_option linter.style.haveILetI false in
/-- L8. A cardinal-minimal finite counterexample is simple, or it has a proper
nontrivial quotient satisfying E677 and E255, with uniform proper nontrivial fibres. -/
theorem L8_minimal_counterexample_dichotomy {N : Type u} [Finite N]
    (opN : N → N → N) (hcounter : IsCounterexample opN)
    (hminimal : ∀ k, k < Nat.card N → ∀ op : Fin k → Fin k → Fin k,
      ¬ IsCounterexample op) :
    IsSimple opN ∨
      ∃ θ : MagmaCongruence opN,
        ¬ θ.IsTrivial ∧ ¬ θ.IsTotal ∧
        1 < Nat.card (MagmaQuotient θ) ∧
        Nat.card (MagmaQuotient θ) < Nat.card N ∧
        E677 (quotientOp θ) ∧ E255 (quotientOp θ) ∧
        ∃ m : ℕ, 1 < m ∧ m < Nat.card N ∧
          (∀ q : MagmaQuotient θ,
            Nat.card {x : N // quotientMap θ x = q} = m) ∧
          Nat.card N = Nat.card (MagmaQuotient θ) * m := by
  classical
  by_cases hs : IsSimple opN
  · exact Or.inl hs
  · right
    rw [IsSimple] at hs
    push Not at hs
    obtain ⟨θ, hnotTrivial, hnotTotal⟩ := hs
    rw [MagmaCongruence.IsTrivial] at hnotTrivial
    rw [MagmaCongruence.IsTotal] at hnotTotal
    push Not at hnotTrivial hnotTotal
    obtain ⟨a, b, hab, habne⟩ := hnotTrivial
    obtain ⟨c, d, hcd⟩ := hnotTotal
    let qmap : N → MagmaQuotient θ := quotientMap θ
    have hqsurj : Function.Surjective qmap := Quotient.mk_surjective
    have hqhom : IsMagmaHom opN (quotientOp θ) qmap := fun _ _ => rfl
    have hq677 : E677 (quotientOp θ) :=
      L7a_E677_of_surjective_hom opN (quotientOp θ) hcounter.1 qmap hqsurj hqhom
    have haclass : qmap a = qmap b := Quotient.sound hab
    have hqnotinj : ¬ Function.Injective qmap := by
      intro hinj
      exact habne (hinj haclass)
    have hcdclass : qmap c ≠ qmap d := by
      intro h
      exact hcd (Quotient.exact h)
    have hqone : 1 < Nat.card (MagmaQuotient θ) :=
      Finite.one_lt_card_iff_nontrivial.mpr ⟨⟨qmap c, qmap d, hcdclass⟩⟩
    letI : Fintype N := Fintype.ofFinite N
    letI : Fintype (MagmaQuotient θ) := Fintype.ofFinite (MagmaQuotient θ)
    have hqlt : Nat.card (MagmaQuotient θ) < Nat.card N := by
      simpa only [Nat.card_eq_fintype_card] using
        Fintype.card_lt_of_surjective_not_injective qmap hqsurj hqnotinj
    have hq255 : E255 (quotientOp θ) := by
      by_contra hnot255
      let e : MagmaQuotient θ ≃ Fin (Nat.card (MagmaQuotient θ)) :=
        Finite.equivFin (MagmaQuotient θ)
      let opFin := transportOpEquiv e (quotientOp θ)
      have hfinCounter : IsCounterexample opFin := by
        refine ⟨E677_transportOpEquiv e (quotientOp θ) hq677, ?_⟩
        intro hfin255
        exact hnot255 ((E255_transportOpEquiv_iff e (quotientOp θ)).mp hfin255)
      exact hminimal (Nat.card (MagmaQuotient θ)) hqlt opFin hfinCounter
    let qa : MagmaQuotient θ := qmap a
    let m : ℕ := Nat.card {x : N // qmap x = qa}
    have hclasses : ∀ q : MagmaQuotient θ, Nat.card {x : N // qmap x = q} = m := by
      intro q
      exact L2_quotient_fibres opN (quotientOp θ) hcounter.1 hq677 qmap hqsurj hqhom q qa
    let xa : {x : N // qmap x = qa} := ⟨a, rfl⟩
    let xb : {x : N // qmap x = qa} := ⟨b, haclass.symm⟩
    have hxab : xa ≠ xb := by
      intro h
      exact habne (congrArg Subtype.val h)
    have hmone : 1 < m :=
      Finite.one_lt_card_iff_nontrivial.mpr ⟨⟨xa, xb, hxab⟩⟩
    have hout : ∃ z : N, qmap z ≠ qa := by
      by_cases hc : qmap c = qa
      · exact ⟨d, fun hd => hcdclass (hc.trans hd.symm)⟩
      · exact ⟨c, hc⟩
    have hvalNotSurj : ¬ Function.Surjective
        (Subtype.val : {x : N // qmap x = qa} → N) := by
      intro hsurj
      obtain ⟨z, hz⟩ := hout
      obtain ⟨x, hx⟩ := hsurj z
      apply hz
      simpa [hx] using x.property
    have hmlt : m < Nat.card N := by
      simpa only [m, Nat.card_eq_fintype_card] using
        Fintype.card_lt_of_injective_not_surjective
          (Subtype.val : {x : N // qmap x = qa} → N) Subtype.val_injective hvalNotSurj
    have hfactor : Nat.card N = Nat.card (MagmaQuotient θ) * m := by
      obtain ⟨Fib, _, e, _, hFib, _, _, _, _⟩ :=
        L7_coordinatization opN (quotientOp θ) hcounter.1 qmap hqsurj hqhom m hclasses
      calc
        Nat.card N = Nat.card (MagmaQuotient θ × Fib) := Nat.card_congr e
        _ = Nat.card (MagmaQuotient θ) * Nat.card Fib := by simp
        _ = Nat.card (MagmaQuotient θ) * m := by rw [hFib]
    refine ⟨θ, ?_, ?_, hqone, hqlt, hq677, hq255, m, hmone, hmlt, hclasses, hfactor⟩
    · intro htrivial
      exact habne (htrivial a b hab)
    · intro htotal
      exact hcd (htotal c d)

#print axioms E677_transportOpEquiv
#print axioms E255_transportOpEquiv_iff
#print axioms quotientOp_mk
#print axioms quotientMap_surjective_hom
#print axioms L8_minimal_counterexample_dichotomy

end Ext677
