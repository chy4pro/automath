import Ext677
import Mathlib.Data.Fintype.EquivFin
import Mathlib.Data.Fintype.Order
import Mathlib.Logic.Relation
import Mathlib.SetTheory.Cardinal.NatCard
import Mathlib.Tactic

/-!
# Collision structure for the E677 simple-case attack

The counting identities are formulated with ordered distinct pairs. This removes any
unnecessary linear-order assumption from the main results.
-/

namespace Ext677

open Function

universe u

/-- Two rows collide when they agree in at least one column. -/
def Rho {M : Type u} (op : M → M → M) (a b : M) : Prop :=
  ∃ t, op a t = op b t

/-- The transitive collision relation. Since `Rho` is reflexive and symmetric, this is
the connected-component relation of the undirected collision graph. -/
def RhoStar {M : Type u} (op : M → M → M) : M → M → Prop :=
  Relation.TransGen (Rho op)

/-- The collision columns of two rows. -/
noncomputable def collisionSet {M : Type u} [Fintype M]
    (op : M → M → M) (a b : M) : Finset M := by
  classical
  exact Finset.univ.filter fun t => op a t = op b t

/-- Number of collision columns for an ordered row pair. -/
noncomputable def collisionCount {M : Type u} [Fintype M]
    (op : M → M → M) (a b : M) : ℕ :=
  Nat.card {t : M // op a t = op b t}

/-- The cardinality used below is exactly the cardinality of the requested finite
collision set `F(a,b)`. -/
theorem collisionSet_card_eq_collisionCount {M : Type u} [Fintype M]
    (op : M → M → M) (a b : M) :
    (collisionSet op a b).card = collisionCount op a b := by
  classical
  rw [collisionSet, collisionCount, Nat.card_eq_fintype_card]
  exact (Fintype.card_subtype fun t => op a t = op b t).symm

/-- Column multiplicity `N(t,v)`. -/
noncomputable def Ncount {M : Type u} [Fintype M]
    (op : M → M → M) (t v : M) : ℕ :=
  Nat.card {a : M // op a t = v}

theorem rho_refl {M : Type u} (op : M → M → M) (a : M) : Rho op a a :=
  ⟨a, rfl⟩

theorem rho_symm {M : Type u} {op : M → M → M} {a b : M} :
    Rho op a b → Rho op b a := by
  rintro ⟨t, h⟩
  exact ⟨t, h.symm⟩

theorem rhoStar_refl {M : Type u} (op : M → M → M) (a : M) : RhoStar op a a :=
  Relation.TransGen.single (rho_refl op a)

theorem rhoStar_symm {M : Type u} {op : M → M → M} {a b : M} :
    RhoStar op a b → RhoStar op b a := by
  intro h
  induction h using Relation.TransGen.trans_induction_on with
  | single h => exact Relation.TransGen.single (rho_symm h)
  | trans _ _ ih₁ ih₂ => exact ih₂.trans ih₁

/-- The full congruence condition (B) for the collision closure. -/
def CollisionCongruenceCondition {M : Type u} (op : M → M → M) : Prop :=
  ∀ a b, RhoStar op a b → ∀ c,
    RhoStar op (op c a) (op c b) ∧ RhoStar op (op a c) (op b c)

/-- The same transport requirement restricted to collision generators. -/
def CollisionGeneratorTransport {M : Type u} (op : M → M → M) : Prop :=
  ∀ a b c, Rho op a b →
    RhoStar op (op c a) (op c b) ∧ RhoStar op (op a c) (op b c)

/-- C2. It suffices, and is necessary, to verify collision transport on generators. -/
theorem C2_generator_transport_criterion {M : Type u} (op : M → M → M) :
    CollisionCongruenceCondition op ↔ CollisionGeneratorTransport op := by
  constructor
  · intro h a b c hab
    exact h a b (Relation.TransGen.single hab) c
  · intro h a b hab c
    constructor
    · induction hab using Relation.TransGen.trans_induction_on with
      | single hab => exact (h _ _ c hab).1
      | trans _ _ ih₁ ih₂ => exact ih₁.trans ih₂
    · induction hab using Relation.TransGen.trans_induction_on with
      | single hab => exact (h _ _ c hab).2
      | trans _ _ ih₁ ih₂ => exact ih₁.trans ih₂

/-- Collision-closed subsets. -/
def RhoClosed {M : Type u} (op : M → M → M) (S : Set M) : Prop :=
  ∀ ⦃a b⦄, a ∈ S → Rho op a b → b ∈ S

theorem rhoStar_mem_of_closed {M : Type u} {op : M → M → M} {S : Set M}
    (hS : RhoClosed op S) {a b : M} (ha : a ∈ S) (hab : RhoStar op a b) : b ∈ S := by
  induction hab using Relation.TransGen.trans_induction_on with
  | single h => exact hS ha h
  | trans _ _ ih₁ ih₂ => exact ih₂ (ih₁ ha)

/-- Connectedness of the collision graph, expressed using its path relation. -/
def CollisionConnected {M : Type u} (op : M → M → M) : Prop :=
  ∀ a b, RhoStar op a b

/-- C3. With `RhoStar` chosen as the transitive closure of the symmetric collision
relation, graph connectedness is exactly universal reachability. -/
theorem C3_connected_iff {M : Type u} (op : M → M → M) :
    (∀ a b, RhoStar op a b) ↔ CollisionConnected op := Iff.rfl

/-- C3, useful contrapositive form: disconnectedness is equivalent to the existence of
a proper nonempty collision-closed subset. -/
theorem C3_disconnected_iff_closed_subset {M : Type u} (op : M → M → M) :
    (∃ a b, ¬ RhoStar op a b) ↔
      ∃ S : Set M, S.Nonempty ∧ S ≠ Set.univ ∧ RhoClosed op S := by
  constructor
  · rintro ⟨a, b, hab⟩
    let S : Set M := {x | RhoStar op a x}
    refine ⟨S, ⟨a, rhoStar_refl op a⟩, ?_, ?_⟩
    · intro hS
      apply hab
      have : b ∈ S := by simp [hS]
      exact this
    · intro x y hx hxy
      exact hx.trans (Relation.TransGen.single hxy)
  · rintro ⟨S, ⟨a, ha⟩, hproper, hclosed⟩
    have hnotall : ∃ b, b ∉ S := by
      by_contra h
      push Not at h
      apply hproper
      ext x
      simp [h x]
    obtain ⟨b, hb⟩ := hnotall
    refine ⟨a, b, ?_⟩
    intro hab
    exact hb (rhoStar_mem_of_closed hclosed ha hab)

/-- A type whose cardinality is the left side of the collision second moment. -/
def ColumnPairCertificates {M : Type u} (op : M → M → M) :=
  Σ t : M, Σ v : M,
    {a : M // op a t = v} × {b : M // op b t = v}

/-- A type whose cardinality counts ordered row-pair collision certificates. -/
def OrderedCollisionCertificates {M : Type u} (op : M → M → M) :=
  Σ a : M, Σ b : M, {t : M // op a t = op b t}

/-- Re-index the same collision certificates by column/value or by ordered row pair. -/
def columnPairEquivOrderedCollision {M : Type u} (op : M → M → M) :
    ColumnPairCertificates op ≃ OrderedCollisionCertificates op where
  toFun p := ⟨p.2.2.1.1, p.2.2.2.1, p.1, p.2.2.1.2.trans p.2.2.2.2.symm⟩
  invFun p := ⟨p.2.2.1, op p.1 p.2.2.1,
    ⟨p.1, rfl⟩, ⟨p.2.1, p.2.2.2.symm⟩⟩
  left_inv p := by rcases p with ⟨t, v, ⟨a, ha⟩, ⟨b, hb⟩⟩; subst v; rfl
  right_inv p := by rcases p with ⟨a, b, t, h⟩; rfl

/-- C1, ordered form: the second moment is the total number of ordered collision
certificates. -/
theorem C1_collision_second_moment_ordered {M : Type u} [Fintype M]
    (op : M → M → M) :
    (∑ t : M, ∑ v : M, (Ncount op t v) ^ 2) =
      ∑ a : M, ∑ b : M, collisionCount op a b := by
  classical
  have hcard := Nat.card_congr (columnPairEquivOrderedCollision op)
  simpa [ColumnPairCertificates, OrderedCollisionCertificates, Ncount, collisionCount,
    Nat.card_eq_fintype_card, pow_two] using hcard

/-- C1, diagonal/off-diagonal form. -/
theorem C1_collision_second_moment {M : Type u} [Fintype M] [DecidableEq M]
    (op : M → M → M) :
    let n := Fintype.card M
    (∑ t : M, ∑ v : M, (Ncount op t v) ^ 2) =
      n ^ 2 + ∑ a : M, ∑ b ∈ Finset.univ.erase a, collisionCount op a b := by
  classical
  dsimp only
  rw [C1_collision_second_moment_ordered]
  calc
    (∑ a : M, ∑ b : M, collisionCount op a b) =
        ∑ a : M, (collisionCount op a a +
          ∑ b ∈ Finset.univ.erase a, collisionCount op a b) := by
            apply Finset.sum_congr rfl
            intro a _
            rw [← Finset.sum_erase_add _ _ (Finset.mem_univ a)]
            exact Nat.add_comm _ _
    _ = (∑ a : M, collisionCount op a a) +
        ∑ a : M, ∑ b ∈ Finset.univ.erase a, collisionCount op a b := by
          rw [Finset.sum_add_distrib]
    _ = (Fintype.card M) ^ 2 +
        ∑ a : M, ∑ b ∈ Finset.univ.erase a, collisionCount op a b := by
          congr 1
          simp [collisionCount, pow_two]

theorem rho_iff_collisionCount_pos {M : Type u} [Fintype M]
    (op : M → M → M) (a b : M) : Rho op a b ↔ 0 < collisionCount op a b := by
  constructor
  · rintro ⟨t, ht⟩
    exact Finite.card_pos_iff.mpr ⟨⟨t, ht⟩⟩
  · intro h
    obtain ⟨⟨t, ht⟩⟩ := Finite.card_pos_iff.mp h
    exact ⟨t, ht⟩

/-- Under universal collision, the off-diagonal collision count is its minimum
`n*(n-1)` plus a sum of nonnegative collision excesses. -/
theorem offDiagonal_collision_excess {M : Type u} [Fintype M] [DecidableEq M]
    (op : M → M → M) (huniv : ∀ a b, a ≠ b → Rho op a b) :
    (∑ a : M, ∑ b ∈ Finset.univ.erase a, collisionCount op a b) =
      Fintype.card M * (Fintype.card M - 1) +
        ∑ a : M, ∑ b ∈ Finset.univ.erase a, (collisionCount op a b - 1) := by
  classical
  calc
    (∑ a : M, ∑ b ∈ Finset.univ.erase a, collisionCount op a b) =
        ∑ a : M, ∑ b ∈ Finset.univ.erase a,
          (1 + (collisionCount op a b - 1)) := by
            apply Finset.sum_congr rfl
            intro a _
            apply Finset.sum_congr rfl
            intro b hb
            have hne : b ≠ a := Finset.ne_of_mem_erase hb
            have hpos := (rho_iff_collisionCount_pos op a b).mp (huniv a b hne.symm)
            omega
    _ = ∑ a : M, ((Finset.univ.erase a).card +
        ∑ b ∈ Finset.univ.erase a, (collisionCount op a b - 1)) := by
          apply Finset.sum_congr rfl
          intro a _
          rw [Finset.sum_add_distrib]
          simp
    _ = Fintype.card M * (Fintype.card M - 1) +
        ∑ a : M, ∑ b ∈ Finset.univ.erase a, (collisionCount op a b - 1) := by
          rw [Finset.sum_add_distrib]
          congr 1
          simp [Finset.card_erase_of_mem]

/-- C1 corollary. Universal collision forces the sharp second-moment lower bound,
and equality holds exactly when every distinct pair has one collision certificate. -/
theorem C1_universal_rho_bound_and_eq_iff {M : Type u} [Fintype M] [DecidableEq M]
    (op : M → M → M) (huniv : ∀ a b, a ≠ b → Rho op a b) :
    let n := Fintype.card M
    (2 * n ^ 2 - n ≤ ∑ t : M, ∑ v : M, (Ncount op t v) ^ 2) ∧
      ((∑ t : M, ∑ v : M, (Ncount op t v) ^ 2) = 2 * n ^ 2 - n ↔
        ∀ a b, a ≠ b → collisionCount op a b = 1) := by
  classical
  dsimp only
  let n := Fintype.card M
  let moment := ∑ t : M, ∑ v : M, (Ncount op t v) ^ 2
  let off := ∑ a : M, ∑ b ∈ Finset.univ.erase a, collisionCount op a b
  let excess := ∑ a : M, ∑ b ∈ Finset.univ.erase a, (collisionCount op a b - 1)
  have hmoment : moment = n ^ 2 + off := C1_collision_second_moment op
  have hoff : off = n * (n - 1) + excess := offDiagonal_collision_excess op huniv
  have hbase : n ^ 2 + n * (n - 1) = 2 * n ^ 2 - n := by
    by_cases hn : n = 0
    · simp [hn]
    · have hnpos : 1 ≤ n := Nat.one_le_iff_ne_zero.mpr hn
      have hnle : n ≤ n ^ 2 := by nlinarith
      have hprod : n * (n - 1) = n ^ 2 - n := by
        rw [Nat.mul_sub_left_distrib]
        simp [pow_two]
      rw [hprod]
      omega
  change (2 * n ^ 2 - n ≤ moment) ∧
    (moment = 2 * n ^ 2 - n ↔
      ∀ a b, a ≠ b → collisionCount op a b = 1)
  constructor
  · omega
  · constructor
    · intro heq a b hab
      have hexcess : excess = 0 := by omega
      have houter : ∀ x ∈ (Finset.univ : Finset M),
          (∑ y ∈ Finset.univ.erase x, (collisionCount op x y - 1)) = 0 :=
        (Finset.sum_eq_zero_iff_of_nonneg fun _ _ => Nat.zero_le _).mp hexcess
      have hinner : ∀ y ∈ Finset.univ.erase a, collisionCount op a y - 1 = 0 :=
        (Finset.sum_eq_zero_iff_of_nonneg fun _ _ => Nat.zero_le _).mp
          (houter a (Finset.mem_univ a))
      have hle : collisionCount op a b ≤ 1 :=
        Nat.sub_eq_zero_iff_le.mp (hinner b (by simp [hab.symm]))
      have hge : 1 ≤ collisionCount op a b :=
        (rho_iff_collisionCount_pos op a b).mp (huniv a b hab)
      omega
    · intro hone
      have hexcess : excess = 0 := by
        apply Finset.sum_eq_zero
        intro a _
        apply Finset.sum_eq_zero
        intro b hb
        have hne : a ≠ b := (Finset.ne_of_mem_erase hb).symm
        simp [hone a b hne]
      omega

/-- Left division undoes a left product in both directions. -/
theorem ldiv_op {M : Type u} [Finite M] (op : M → M → M) (h677 : E677 op)
    (y x : M) : ldiv op h677 y (op y x) = x := by
  symm
  exact ldiv_unique op h677 rfl

/-- The common-certificate map used in C4. -/
noncomputable def Xi {M : Type u} [Finite M]
    (op : M → M → M) (h677 : E677 op) (t x : M) : M :=
  ldiv op h677 x (ldiv op h677 t x)

theorem Xi_ldiv {M : Type u} [Finite M] (op : M → M → M) (h677 : E677 op)
    (t a : M) : Xi op h677 t (ldiv op h677 t a) = op a t := by
  unfold Xi
  rw [← key_identity op h677 (ldiv op h677 t a) t]
  simp only [op_ldiv]

/-- Ordered distinct collision certificates. -/
def CollisionCertificates {M : Type u} (op : M → M → M) :=
  {p : M × (M × M) // p.1 ≠ p.2.1 ∧ op p.1 p.2.2 = op p.2.1 p.2.2}

/-- Ordered distinct common-Xi certificates. -/
def CommonXiCertificates {M : Type u} [Finite M] (op : M → M → M)
    (h677 : E677 op) :=
  {p : M × (M × M) // p.1 ≠ p.2.1 ∧
    Xi op h677 p.2.2 p.1 = Xi op h677 p.2.2 p.2.1}

/-- C4's explicit KEY certificate equivalence. -/
noncomputable def keyCertificateEquiv {M : Type u} [Finite M]
    (op : M → M → M) (h677 : E677 op) :
    CollisionCertificates op ≃ CommonXiCertificates op h677 where
  toFun p := ⟨(ldiv op h677 p.1.2.2 p.1.1,
      (ldiv op h677 p.1.2.2 p.1.2.1, p.1.2.2)), by
    constructor
    · intro h
      apply p.2.1
      simpa only [op_ldiv] using congrArg (op p.1.2.2) h
    · change Xi op h677 p.1.2.2 (ldiv op h677 p.1.2.2 p.1.1) =
        Xi op h677 p.1.2.2 (ldiv op h677 p.1.2.2 p.1.2.1)
      rw [Xi_ldiv, Xi_ldiv]
      exact p.2.2⟩
  invFun p := ⟨(op p.1.2.2 p.1.1, (op p.1.2.2 p.1.2.1, p.1.2.2)), by
    constructor
    · exact fun h => p.2.1 ((L1_left_bij op h677 p.1.2.2).1 h)
    · change op (op p.1.2.2 p.1.1) p.1.2.2 = op (op p.1.2.2 p.1.2.1) p.1.2.2
      rw [key_identity op h677 p.1.1 p.1.2.2,
        key_identity op h677 p.1.2.1 p.1.2.2]
      exact p.2.2⟩
  left_inv p := by
    rcases p with ⟨⟨a, ⟨b, t⟩⟩, hp⟩
    apply Subtype.ext
    simp only [op_ldiv]
  right_inv p := by
    rcases p with ⟨⟨x, ⟨y, t⟩⟩, hp⟩
    apply Subtype.ext
    simp only [ldiv_op]

/-- C4. The stated map on triples is bijective, with inverse given by left
multiplication by the certificate column. -/
theorem C4_key_certificate_bijection {M : Type u} [Finite M]
    (op : M → M → M) (h677 : E677 op) :
    Function.Bijective (keyCertificateEquiv op h677) :=
  (keyCertificateEquiv op h677).bijective

/-- Xi-fibre multiplicity `E(t,v)`. -/
noncomputable def Ecount {M : Type u} [Fintype M]
    (op : M → M → M) (h677 : E677 op) (t v : M) : ℕ :=
  Nat.card {x : M // Xi op h677 t x = v}

/-- Common-Xi certificate multiplicity `C(x,y)`. -/
noncomputable def commonXiCount {M : Type u} [Fintype M]
    (op : M → M → M) (h677 : E677 op) (x y : M) : ℕ :=
  Nat.card {t : M // Xi op h677 t x = Xi op h677 t y}

/-- C4 corollary: common-certificate double count in ordered form. -/
theorem C4_common_certificate_double_count {M : Type u} [Fintype M] [DecidableEq M]
    (op : M → M → M) (h677 : E677 op) :
    let n := Fintype.card M
    (∑ t : M, ∑ v : M, (Ecount op h677 t v) ^ 2) =
      n ^ 2 + ∑ x : M, ∑ y ∈ Finset.univ.erase x, commonXiCount op h677 x y := by
  simpa [Ecount, commonXiCount, Ncount, collisionCount] using
    C1_collision_second_moment (fun x t => Xi op h677 t x)

/-- Under pointwise equality of the N and E multiplicities, their second moments agree. -/
theorem C4_second_moments_eq_of_N {M : Type u} [Fintype M]
    (op : M → M → M) (h677 : E677 op)
    (hN : ∀ t v, Ncount op t v = Ecount op h677 t v) :
    (∑ t : M, ∑ v : M, (Ncount op t v) ^ 2) =
      ∑ t : M, ∑ v : M, (Ecount op h677 t v) ^ 2 := by
  simp_rw [hN]

/-- The fixed-point certificates used in C5. -/
def FixedPointCertificates {M : Type u} (op : M → M → M) (t v : M) :=
  {x : M // op t (op x v) = x}

/-- C5's explicit fibre-to-fixed-point equivalence. -/
noncomputable def columnFiberEquivFixedPoints {M : Type u} [Finite M]
    (op : M → M → M) (h677 : E677 op) (t v : M) :
    {a : M // op a t = v} ≃ FixedPointCertificates op t v where
  toFun a := ⟨ldiv op h677 t a.1, by
    have h := h677 (ldiv op h677 t a.1) t
    simpa only [op_ldiv, a.2] using h.symm⟩
  invFun x := ⟨op t x.1, by
    have hx₁ : op x.1 v = ldiv op h677 t x.1 :=
      ldiv_unique op h677 x.2
    have hx₂ : v = ldiv op h677 x.1 (ldiv op h677 t x.1) :=
      ldiv_unique op h677 hx₁
    rw [key_identity op h677 x.1 t]
    exact hx₂.symm⟩
  left_inv a := by
    apply Subtype.ext
    exact op_ldiv op h677 t a.1
  right_inv x := by
    apply Subtype.ext
    exact ldiv_op op h677 t x.1

/-- C5. In an E677 magma, column multiplicity equals the number of solutions of
`t * (x * v) = x`. -/
theorem C5_N_eq_fixedPoint_count {M : Type u} [Fintype M]
    (op : M → M → M) (h677 : E677 op) (t v : M) :
    Ncount op t v = Nat.card (FixedPointCertificates op t v) := by
  classical
  exact Nat.card_congr (columnFiberEquivFixedPoints op h677 t v)

#print axioms rho_refl
#print axioms rho_symm
#print axioms rhoStar_refl
#print axioms rhoStar_symm
#print axioms collisionSet_card_eq_collisionCount
#print axioms C2_generator_transport_criterion
#print axioms rhoStar_mem_of_closed
#print axioms C3_connected_iff
#print axioms C3_disconnected_iff_closed_subset
#print axioms C1_collision_second_moment_ordered
#print axioms C1_collision_second_moment
#print axioms rho_iff_collisionCount_pos
#print axioms offDiagonal_collision_excess
#print axioms C1_universal_rho_bound_and_eq_iff
#print axioms ldiv_op
#print axioms Xi_ldiv
#print axioms C4_key_certificate_bijection
#print axioms C4_common_certificate_double_count
#print axioms C4_second_moments_eq_of_N
#print axioms C5_N_eq_fixedPoint_count

end Ext677
