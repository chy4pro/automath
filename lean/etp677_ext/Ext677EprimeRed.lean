import Ext677Window
import Mathlib.Tactic

/-!
# Submagma and quotient reductions for the E-prime property

The E-prime property says that `L14X6` holds at some point in the image of `U`.
-/

namespace Ext677

universe u v

/-- A subset closed under the explicitly presented magma operation. -/
def IsSubmagma {M : Type u} (op : M → M → M) (S : Set M) : Prop :=
  ∀ ⦃x y : M⦄, x ∈ S → y ∈ S → op x y ∈ S

/-- The operation restricted to a closed subset. -/
def submagmaOp {M : Type u} (op : M → M → M) {S : Set M}
    (hS : IsSubmagma op S) : S → S → S :=
  fun x y => ⟨op x.1 y.1, hS x.2 y.2⟩

/-- The square unary term `S(x)=x*x`. -/
def X6S {M : Type u} (op : M → M → M) (x : M) : M := op x x

/-- The E-prime target: `L14X6` holds at some point in the image of `U`. -/
def EprimeProperty {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) : Prop :=
  ∃ x : M, L14X6 op h677 (X6U op x)

/-- Membership in the image of the unary map `U`. -/
def InUImage {M : Type u} (op : M → M → M) (a : M) : Prop :=
  ∃ x : M, X6U op x = a

/-- E-prime can equivalently be stated using an explicit point in `Im(U)`. -/
theorem eprime_iff_exists_inUImage {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) :
    EprimeProperty op h677 ↔ ∃ a : M, InUImage op a ∧ L14X6 op h677 a := by
  constructor
  · rintro ⟨x, hx⟩
    exact ⟨X6U op x, ⟨x, rfl⟩, hx⟩
  · rintro ⟨a, ⟨x, rfl⟩, hx⟩
    exact ⟨x, hx⟩

/-- R1: E677 is inherited by a closed subtype. -/
theorem submagma_E677 {M : Type u} (op : M → M → M) {S : Set M}
    (hS : IsSubmagma op S) (h677 : E677 op) :
    E677 (submagmaOp op hS) := by
  intro x y
  apply Subtype.ext
  exact h677 x.1 y.1

/-- R1: E255 is inherited by a closed subtype. -/
theorem submagma_E255 {M : Type u} (op : M → M → M) {S : Set M}
    (hS : IsSubmagma op S) (h255 : E255 op) :
    E255 (submagmaOp op hS) := by
  intro x
  apply Subtype.ext
  exact h255 x.1

/-- Idempotent-freeness is inherited by a closed subtype. -/
theorem submagma_idempotent_free {M : Type u} (op : M → M → M) {S : Set M}
    (hS : IsSubmagma op S) (hfree : ∀ x, op x x ≠ x) :
    ∀ x, submagmaOp op hS x x ≠ x := by
  intro x h
  exact hfree x.1 (congrArg Subtype.val h)

/-- Left division computed in a finite E677 submagma agrees with ambient left division. -/
theorem submagma_val_ldiv {M : Type u} [Finite M] (op : M → M → M) {S : Set M}
    (hS : IsSubmagma op S) (h677 : E677 op) (x z : S) :
    (ldiv (submagmaOp op hS) (submagma_E677 op hS h677) x z).1 =
      ldiv op h677 x.1 z.1 := by
  apply ldiv_unique op h677
  exact congrArg Subtype.val
    (op_ldiv (submagmaOp op hS) (submagma_E677 op hS h677) x z)

/-- The inclusion of a finite E677 submagma preserves `S,U,W,P,F`. -/
theorem submagma_val_SUWPF {M : Type u} [Finite M] (op : M → M → M) {S : Set M}
    (hS : IsSubmagma op S) (h677 : E677 op) (x : S) :
    (X6S (submagmaOp op hS) x).1 = X6S op x.1 ∧
    (X6U (submagmaOp op hS) x).1 = X6U op x.1 ∧
    (X6W (submagmaOp op hS) x).1 = X6W op x.1 ∧
    (X6P (submagmaOp op hS) (submagma_E677 op hS h677) x).1 = X6P op h677 x.1 ∧
    (L12F (submagmaOp op hS) (submagma_E677 op hS h677) x).1 =
      L12F op h677 x.1 := by
  let opN := submagmaOp op hS
  let hN : E677 opN := submagma_E677 op hS h677
  have hP : (X6P opN hN x).1 = X6P op h677 x.1 := by
    unfold X6P
    rw [submagma_val_ldiv op hS h677 x (X6U opN x)]
    rfl
  let q1 := ldiv opN hN x x
  let q2 := ldiv opN hN x q1
  let q3 := ldiv opN hN x q2
  let q4 := ldiv opN hN x q3
  have hq1 : q1.1 = ldiv op h677 x.1 x.1 :=
    submagma_val_ldiv op hS h677 x x
  have hq2 : q2.1 = ldiv op h677 x.1 (ldiv op h677 x.1 x.1) := by
    exact (submagma_val_ldiv op hS h677 x q1).trans (congrArg _ hq1)
  have hq3 : q3.1 = ldiv op h677 x.1 (ldiv op h677 x.1 (ldiv op h677 x.1 x.1)) := by
    exact (submagma_val_ldiv op hS h677 x q2).trans (congrArg _ hq2)
  have hq4 : q4.1 =
      ldiv op h677 x.1 (ldiv op h677 x.1 (ldiv op h677 x.1 (ldiv op h677 x.1 x.1))) := by
    exact (submagma_val_ldiv op hS h677 x q3).trans (congrArg _ hq3)
  refine ⟨rfl, rfl, rfl, hP, ?_⟩
  change q4.1 = _
  exact hq4

/-- The inclusion preserves all seven automatic pattern/window coordinates. -/
theorem submagma_val_pattern {M : Type u} [Finite M] (op : M → M → M) {S : Set M}
    (hS : IsSubmagma op S) (h677 : E677 op) (a : S) :
    (L13U (submagmaOp op hS) a).1 = L13U op a.1 ∧
    (L13P (submagmaOp op hS) (submagma_E677 op hS h677) a).1 = L13P op h677 a.1 ∧
    (L13B (submagmaOp op hS) (submagma_E677 op hS h677) a).1 = L13B op h677 a.1 ∧
    (L13D (submagmaOp op hS) (submagma_E677 op hS h677) a).1 = L13D op h677 a.1 ∧
    (L13V (submagmaOp op hS) (submagma_E677 op hS h677) a).1 = L13V op h677 a.1 ∧
    (L13C (submagmaOp op hS) (submagma_E677 op hS h677) a).1 = L13C op h677 a.1 ∧
    (L13W (submagmaOp op hS) a).1 = L13W op a.1 := by
  let opN := submagmaOp op hS
  let hN : E677 opN := submagma_E677 op hS h677
  have hP : (L13P opN hN a).1 = L13P op h677 a.1 := by
    unfold L13P
    rw [submagma_val_ldiv op hS h677 a (L13U opN a)]
    rfl
  have hB : (L13B opN hN a).1 = L13B op h677 a.1 := by
    unfold L13B
    exact (submagma_val_ldiv op hS h677 a (L13P opN hN a)).trans (congrArg _ hP)
  have hD : (L13D opN hN a).1 = L13D op h677 a.1 := by
    change op (L13B opN hN a).1 (L13B opN hN a).1 =
      op (L13B op h677 a.1) (L13B op h677 a.1)
    rw [hB]
  have hV : (L13V opN hN a).1 = L13V op h677 a.1 := by
    change op (L13D opN hN a).1 (L13B opN hN a).1 =
      op (L13D op h677 a.1) (L13B op h677 a.1)
    rw [hD, hB]
  have hC : (L13C opN hN a).1 = L13C op h677 a.1 := by
    change op (L13B opN hN a).1 (L13V opN hN a).1 =
      op (L13B op h677 a.1) (L13V op h677 a.1)
    rw [hB, hV]
  exact ⟨rfl, hP, hB, hD, hV, hC, rfl⟩

/-- R1: an `L14X6` point in a submagma remains an `L14X6` point in the ambient magma. -/
theorem submagma_lift_X6 {M : Type u} [Finite M] (op : M → M → M) {S : Set M}
    (hS : IsSubmagma op S) (h677 : E677 op) (a : S)
    (hx6 : L14X6 (submagmaOp op hS) (submagma_E677 op hS h677) a) :
    L14X6 op h677 a.1 := by
  rcases submagma_val_pattern op hS h677 a with ⟨hU, hP, _hB, _hD, hV, hC, hW⟩
  rcases hx6 with ⟨hvw, hvu, hca, hcw, hcu, hcp⟩
  have lift_ne (p q : S) (P Q : M) (hp : p.1 = P) (hq : q.1 = Q) (hne : p ≠ q) :
      P ≠ Q := by
    intro hPQ
    apply hne
    apply Subtype.ext
    exact hp.trans (hPQ.trans hq.symm)
  unfold L14X6
  exact ⟨lift_ne _ _ _ _ hV hW hvw, lift_ne _ _ _ _ hV hU hvu,
    lift_ne _ _ _ _ hC rfl hca, lift_ne _ _ _ _ hC hW hcw,
    lift_ne _ _ _ _ hC hU hcu, lift_ne _ _ _ _ hC hP hcp⟩

/-- R1: membership in `Im(U)` lifts from a submagma to the ambient magma. -/
theorem submagma_lift_inUImage {M : Type u} (op : M → M → M) {S : Set M}
    (hS : IsSubmagma op S) (a : S) :
    InUImage (submagmaOp op hS) a → InUImage op a.1 := by
  rintro ⟨x, hx⟩
  refine ⟨x.1, ?_⟩
  exact congrArg Subtype.val hx

/-- R1: the E-prime property lifts from every finite E677 submagma. -/
theorem submagma_lift_Eprime {M : Type u} [Finite M] (op : M → M → M) {S : Set M}
    (hS : IsSubmagma op S) (h677 : E677 op)
    (hE : EprimeProperty (submagmaOp op hS) (submagma_E677 op hS h677)) :
    EprimeProperty op h677 := by
  obtain ⟨x, hx⟩ := hE
  refine ⟨x.1, ?_⟩
  have hlift := submagma_lift_X6 op hS h677 (X6U (submagmaOp op hS) x) hx
  rw [(submagma_val_SUWPF op hS h677 x).2.1] at hlift
  exact hlift

/-- The inductively generated submagma on one element. -/
inductive GeneratedBy {M : Type u} (op : M → M → M) (g : M) : M → Prop
  | generator : GeneratedBy op g g
  | mul {x y : M} : GeneratedBy op g x → GeneratedBy op g y → GeneratedBy op g (op x y)

/-- The generated set is closed under the magma operation. -/
theorem generatedBy_closed {M : Type u} (op : M → M → M) (g : M) :
    IsSubmagma op {x | GeneratedBy op g x} := by
  intro x y hx hy
  exact GeneratedBy.mul hx hy

/-- An explicitly presented magma is monogenic when one element generates every point. -/
def IsMonogenic {M : Type u} (op : M → M → M) : Prop :=
  ∃ g : M, ∀ x : M, GeneratedBy op g x

/-- The generated subtype is monogenic. -/
theorem generated_submagma_monogenic {M : Type u} (op : M → M → M) (g : M) :
    IsMonogenic (submagmaOp op (generatedBy_closed op g)) := by
  refine ⟨⟨g, GeneratedBy.generator⟩, ?_⟩
  rintro ⟨x, hx⟩
  induction hx with
  | generator => exact GeneratedBy.generator
  | mul hx hy ihx ihy => exact GeneratedBy.mul ihx ihy

/-- R2: proving E-prime for monogenic finite idempotent-free E677+E255 magmas suffices. -/
theorem eprime_monogenic_reduction
    (hmono : ∀ {N : Type u} [Finite N] (opN : N → N → N) (hN677 : E677 opN),
      IsMonogenic opN → E255 opN →
      (∀ x, opN x x ≠ x) → EprimeProperty opN hN677) :
    ∀ {M : Type u} [Finite M] [Nonempty M] (opM : M → M → M) (h677 : E677 opM),
      E255 opM → (∀ x, opM x x ≠ x) → EprimeProperty opM h677 := by
  intro M _ _ opM h677 h255 hfree
  let g : M := Classical.choice ‹Nonempty M›
  let hS := generatedBy_closed opM g
  let opN := submagmaOp opM hS
  have hN677 : E677 opN := submagma_E677 opM hS h677
  have hN255 : E255 opN := submagma_E255 opM hS h255
  have hNfree : ∀ x, opN x x ≠ x := submagma_idempotent_free opM hS hfree
  have hNmono : IsMonogenic opN := generated_submagma_monogenic opM g
  have hNE : EprimeProperty opN hN677 := hmono opN hN677 hNmono hN255 hNfree
  exact submagma_lift_Eprime opM hS h677 hNE

/-- R3: E-prime lifts along every surjective homomorphism of finite E677 magmas. -/
theorem quotient_lift_Eprime {M : Type u} {B : Type v} [Finite M] [Finite B]
    (opM : M → M → M) (opB : B → B → B)
    (hM : E677 opM) (hB : E677 opB) (φ : M → B)
    (hφ : Function.Surjective φ) (hhom : IsMagmaHom opM opB φ)
    (hE : EprimeProperty opB hB) : EprimeProperty opM hM := by
  obtain ⟨x, hx⟩ := hE
  obtain ⟨xLift, hxLift⟩ := hφ x
  exact ⟨xLift, window_lift_X6 opM opB hM hB φ hφ hhom x xLift hxLift hx⟩

/-- R3: E-prime in either a chosen submagma or a chosen quotient implies E-prime above. -/
theorem submagma_or_quotient_lift_Eprime
    {M : Type u} {B : Type v} [Finite M] [Finite B]
    (opM : M → M → M) {S : Set M} (hS : IsSubmagma opM S)
    (opB : B → B → B) (hM : E677 opM) (hB : E677 opB) (φ : M → B)
    (hφ : Function.Surjective φ) (hhom : IsMagmaHom opM opB φ)
    (hsource : EprimeProperty (submagmaOp opM hS) (submagma_E677 opM hS hM) ∨
      EprimeProperty opB hB) : EprimeProperty opM hM := by
  rcases hsource with hsub | hquot
  · exact submagma_lift_Eprime opM hS hM hsub
  · exact quotient_lift_Eprime opM opB hM hB φ hφ hhom hquot

/-- A counterexample to E-prime has no E-prime submagma and no E-prime quotient. -/
theorem eprime_counterexample_no_submagma_or_quotient
    {M : Type u} {B : Type v} [Finite M] [Finite B]
    (opM : M → M → M) {S : Set M} (hS : IsSubmagma opM S)
    (opB : B → B → B) (hM : E677 opM) (hB : E677 opB) (φ : M → B)
    (hφ : Function.Surjective φ) (hhom : IsMagmaHom opM opB φ)
    (hnot : ¬ EprimeProperty opM hM) :
    ¬ EprimeProperty (submagmaOp opM hS) (submagma_E677 opM hS hM) ∧
      ¬ EprimeProperty opB hB := by
  constructor
  · exact fun hsub => hnot (submagma_lift_Eprime opM hS hM hsub)
  · exact fun hquot => hnot (quotient_lift_Eprime opM opB hM hB φ hφ hhom hquot)

#print axioms eprime_iff_exists_inUImage
#print axioms submagma_E677
#print axioms submagma_E255
#print axioms submagma_idempotent_free
#print axioms submagma_val_ldiv
#print axioms submagma_val_SUWPF
#print axioms submagma_val_pattern
#print axioms submagma_lift_X6
#print axioms submagma_lift_inUImage
#print axioms submagma_lift_Eprime
#print axioms generatedBy_closed
#print axioms generated_submagma_monogenic
#print axioms eprime_monogenic_reduction
#print axioms quotient_lift_Eprime
#print axioms submagma_or_quotient_lift_Eprime
#print axioms eprime_counterexample_no_submagma_or_quotient

end Ext677
