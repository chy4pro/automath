import Ext677PatternPairs
import Ext677Fibre2
import Std.Tactic.BVDecide
import Mathlib.Tactic

/-!
# The gauge-free Core-7 certificate and exclusion of three-element fibres

The Boolean certificate uses the 378 permutation-matrix bits of the Python
`core7_free.py` encoder.  Intermediate values in the seven chains are inlined
as static 3-by-3 multiplexers; this leaves the same primary Boolean variables
and avoids trusting an external parser or SAT solver.
-/

namespace Ext677

open Function

universe u v

abbrev Core7Pair := Fin 14
abbrev Fin3 := Fin 3

def core7SigBit (a : BitVec 378) (p s t z : Nat) : Bool :=
  a.getLsbD (p * 27 + s * 9 + t * 3 + z)

def core7OneHot3 (x y z : Bool) : Bool :=
  (x || y || z) && !(x && y) && !(x && z) && !(y && z)

def core7RowValid (a : BitVec 378) (p s : Nat) : Bool :=
  core7OneHot3 (core7SigBit a p s 0 0) (core7SigBit a p s 0 1) (core7SigBit a p s 0 2) &&
  core7OneHot3 (core7SigBit a p s 1 0) (core7SigBit a p s 1 1) (core7SigBit a p s 1 2) &&
  core7OneHot3 (core7SigBit a p s 2 0) (core7SigBit a p s 2 1) (core7SigBit a p s 2 2) &&
  core7OneHot3 (core7SigBit a p s 0 0) (core7SigBit a p s 1 0) (core7SigBit a p s 2 0) &&
  core7OneHot3 (core7SigBit a p s 0 1) (core7SigBit a p s 1 1) (core7SigBit a p s 2 1) &&
  core7OneHot3 (core7SigBit a p s 0 2) (core7SigBit a p s 1 2) (core7SigBit a p s 2 2)

def core7Rows3 (a : BitVec 378) (p : Nat) : Bool :=
  core7RowValid a p 0 && core7RowValid a p 1 && core7RowValid a p 2

def core7AllValid (a : BitVec 378) : Bool :=
  core7Rows3 a 0 && core7Rows3 a 1 && core7Rows3 a 2 && core7Rows3 a 3 &&
  core7Rows3 a 4 && core7Rows3 a 5 && core7Rows3 a 6 && core7Rows3 a 7 &&
  core7Rows3 a 8 && core7Rows3 a 9 && core7Rows3 a 10 && core7Rows3 a 11 &&
  core7Rows3 a 12 && core7Rows3 a 13

def core7SelectedBit (a : BitVec 378) (p : Nat) (s t : BitVec 2) (z : Nat) : Bool :=
  (s == 0 && t == 0 && core7SigBit a p 0 0 z) ||
  (s == 0 && t == 1 && core7SigBit a p 0 1 z) ||
  (s == 0 && t == 2 && core7SigBit a p 0 2 z) ||
  (s == 1 && t == 0 && core7SigBit a p 1 0 z) ||
  (s == 1 && t == 1 && core7SigBit a p 1 1 z) ||
  (s == 1 && t == 2 && core7SigBit a p 1 2 z) ||
  (s == 2 && t == 0 && core7SigBit a p 2 0 z) ||
  (s == 2 && t == 1 && core7SigBit a p 2 1 z) ||
  (s == 2 && t == 2 && core7SigBit a p 2 2 z)

def core7App (a : BitVec 378) (p : Nat) (s t : BitVec 2) : BitVec 2 :=
  if core7SelectedBit a p s t 0 then 0 else
  if core7SelectedBit a p s t 1 then 1 else 2

def core7Chain (a : BitVec 378) (p1 p2 p3 p4 : Nat)
    (s t : BitVec 2) : Bool :=
  let r1 := core7App a p1 t s
  let r2 := core7App a p2 r1 t
  let r3 := core7App a p3 s r2
  let r4 := core7App a p4 t r3
  r4 == s

def core7ChainAll (a : BitVec 378) (p1 p2 p3 p4 : Nat) : Bool :=
  core7Chain a p1 p2 p3 p4 0 0 && core7Chain a p1 p2 p3 p4 0 1 &&
  core7Chain a p1 p2 p3 p4 0 2 && core7Chain a p1 p2 p3 p4 1 0 &&
  core7Chain a p1 p2 p3 p4 1 1 && core7Chain a p1 p2 p3 p4 1 2 &&
  core7Chain a p1 p2 p3 p4 2 0 && core7Chain a p1 p2 p3 p4 2 1 &&
  core7Chain a p1 p2 p3 p4 2 2

def core7Formula (a : BitVec 378) : Bool :=
  core7AllValid a &&
  core7ChainAll a 2 12 11 0 &&
  core7ChainAll a 10 1 13 9 &&
  core7ChainAll a 6 5 8 7 &&
  core7ChainAll a 12 3 4 12 &&
  core7ChainAll a 13 7 6 13 &&
  core7ChainAll a 0 11 5 1 &&
  core7ChainAll a 5 9 7 6

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
/-- Kernel-checked UNSAT certificate for the gauge-free Core-7, order-three instance. -/
theorem core7_free_three_unsat (a : BitVec 378) : core7Formula a = false := by
  simp only [core7Formula, core7AllValid, core7Rows3, core7RowValid, core7ChainAll,
    core7Chain, core7App, core7SelectedBit, core7SigBit, core7OneHot3]
  bv_decide (config := { timeout := 120 })

/-! ## Semantic bridge -/

def core7Chains (σ : Core7Pair → Fin3 → Equiv.Perm Fin3) : Prop :=
  ∀ s t,
    s = σ 0 t (σ 11 s (σ 12 (σ 2 t s) t)) ∧
    s = σ 9 t (σ 13 s (σ 1 (σ 10 t s) t)) ∧
    s = σ 7 t (σ 8 s (σ 5 (σ 6 t s) t)) ∧
    s = σ 12 t (σ 4 s (σ 3 (σ 12 t s) t)) ∧
    s = σ 13 t (σ 6 s (σ 7 (σ 13 t s) t)) ∧
    s = σ 1 t (σ 5 s (σ 11 (σ 0 t s) t)) ∧
    s = σ 6 t (σ 7 s (σ 9 (σ 5 t s) t))

def core7SemanticBit (σ : Core7Pair → Fin3 → Equiv.Perm Fin3) (i : Fin 378) : Bool :=
  let p : Core7Pair := Fin.ofNat 14 (i.val / 27)
  let s : Fin3 := Fin.ofNat 3 (i.val / 9)
  let t : Fin3 := Fin.ofNat 3 (i.val / 3)
  let z : Fin3 := Fin.ofNat 3 i.val
  decide (σ p s t = z)

set_option maxRecDepth 100000 in
def core7SemanticBits (σ : Core7Pair → Fin3 → Equiv.Perm Fin3) : BitVec 378 :=
  BitVec.setWidth 378 (BitVec.ofBoolListLE (List.ofFn (core7SemanticBit σ)))

lemma core7SemanticBits_get (σ : Core7Pair → Fin3 → Equiv.Perm Fin3)
    (p : Core7Pair) (s t z : Fin3) :
    core7SigBit (core7SemanticBits σ) p.val s.val t.val z.val = decide (σ p s t = z) := by
  let i := p.val * 27 + s.val * 9 + t.val * 3 + z.val
  have hi : i < 378 := by
    dsimp [i]
    omega
  have hp : Fin.ofNat 14 (i / 27) = p := by
    apply Fin.ext
    simp [i]
    omega
  have hs : Fin.ofNat 3 (i / 9) = s := by
    apply Fin.ext
    simp [i]
    omega
  have ht : Fin.ofNat 3 (i / 3) = t := by
    apply Fin.ext
    simp [i]
    omega
  have hz : Fin.ofNat 3 i = z := by
    apply Fin.ext
    simp [i]
    omega
  unfold core7SigBit core7SemanticBits
  change (BitVec.setWidth 378 (BitVec.ofBoolListLE (List.ofFn (core7SemanticBit σ)))).getLsbD i = _
  rw [BitVec.getLsbD_setWidth, BitVec.getLsbD_ofBoolListLE,
    List.getD_eq_getElem?_getD, List.getElem?_ofFn]
  simp only [hi, decide_true, Bool.true_and, ↓reduceDIte, Option.getD_some]
  unfold core7SemanticBit
  dsimp only
  rw [hp, hs, ht, hz]

lemma core7SemanticBits_getNat (σ : Core7Pair → Fin3 → Equiv.Perm Fin3)
    (p : Core7Pair) (s t z : Nat) (hs : s < 3) (ht : t < 3) (hz : z < 3) :
    core7SigBit (core7SemanticBits σ) p.val s t z =
      decide (σ p ⟨s, hs⟩ ⟨t, ht⟩ = ⟨z, hz⟩) := by
  simpa using core7SemanticBits_get σ p ⟨s, hs⟩ ⟨t, ht⟩ ⟨z, hz⟩

lemma core7OneHot_value (x : Fin3) :
    core7OneHot3 (decide (x = 0)) (decide (x = 1)) (decide (x = 2)) = true := by
  fin_cases x <;> decide

lemma core7OneHot_perm_column (e : Equiv.Perm Fin3) (z : Fin3) :
    core7OneHot3 (decide (e 0 = z)) (decide (e 1 = z)) (decide (e 2 = z)) = true := by
  have h := e.apply_symm_apply z
  generalize hpre : e.symm z = q at h
  have hne (i : Fin3) (hi : i ≠ q) : e i ≠ z := by
    intro hiz
    exact hi (e.injective (hiz.trans h.symm))
  fin_cases q <;> simp_all [core7OneHot3]

lemma core7Semantic_row_valid (σ : Core7Pair → Fin3 → Equiv.Perm Fin3)
    (p : Core7Pair) (s : Fin3) :
    core7RowValid (core7SemanticBits σ) p.val s.val = true := by
  simp only [core7RowValid]
  rw [core7SemanticBits_getNat σ p s.val 0 0 (by omega) (by omega) (by omega),
    core7SemanticBits_getNat σ p s.val 0 1 (by omega) (by omega) (by omega),
    core7SemanticBits_getNat σ p s.val 0 2 (by omega) (by omega) (by omega),
    core7SemanticBits_getNat σ p s.val 1 0 (by omega) (by omega) (by omega),
    core7SemanticBits_getNat σ p s.val 1 1 (by omega) (by omega) (by omega),
    core7SemanticBits_getNat σ p s.val 1 2 (by omega) (by omega) (by omega),
    core7SemanticBits_getNat σ p s.val 2 0 (by omega) (by omega) (by omega),
    core7SemanticBits_getNat σ p s.val 2 1 (by omega) (by omega) (by omega),
    core7SemanticBits_getNat σ p s.val 2 2 (by omega) (by omega) (by omega)]
  have hr0 := core7OneHot_value ((σ p s) 0)
  have hr1 := core7OneHot_value ((σ p s) 1)
  have hr2 := core7OneHot_value ((σ p s) 2)
  have hc0 := core7OneHot_perm_column (σ p s) 0
  have hc1 := core7OneHot_perm_column (σ p s) 1
  have hc2 := core7OneHot_perm_column (σ p s) 2
  simp [hr0, hr1, hr2, hc0, hc1, hc2]

lemma core7Semantic_row_valid_nat (σ : Core7Pair → Fin3 → Equiv.Perm Fin3)
    (p s : Nat) (hp : p < 14) (hs : s < 3) :
    core7RowValid (core7SemanticBits σ) p s = true := by
  simpa using core7Semantic_row_valid σ ⟨p, hp⟩ ⟨s, hs⟩

lemma core7Semantic_all_valid (σ : Core7Pair → Fin3 → Equiv.Perm Fin3) :
    core7AllValid (core7SemanticBits σ) = true := by
  simp only [core7AllValid, core7Rows3]
  simp [core7Semantic_row_valid_nat σ]

def fin3BV (x : Fin3) : BitVec 2 := BitVec.ofNat 2 x.val

lemma core7Semantic_selected (σ : Core7Pair → Fin3 → Equiv.Perm Fin3)
    (p : Core7Pair) (s t z : Fin3) :
    core7SelectedBit (core7SemanticBits σ) p.val (fin3BV s) (fin3BV t) z.val =
      decide ((σ p s) t = z) := by
  fin_cases s <;> fin_cases t <;> fin_cases z <;>
    simp [core7SelectedBit, fin3BV, core7SemanticBits_getNat σ p]

lemma core7Semantic_selectedNat (σ : Core7Pair → Fin3 → Equiv.Perm Fin3)
    (p : Core7Pair) (s t : Fin3) (z : Nat) (hz : z < 3) :
    core7SelectedBit (core7SemanticBits σ) p.val (fin3BV s) (fin3BV t) z =
      decide ((σ p s) t = ⟨z, hz⟩) := by
  simpa using core7Semantic_selected σ p s t ⟨z, hz⟩

lemma core7Semantic_app (σ : Core7Pair → Fin3 → Equiv.Perm Fin3)
    (p : Core7Pair) (s t : Fin3) :
    core7App (core7SemanticBits σ) p.val (fin3BV s) (fin3BV t) = fin3BV ((σ p s) t) := by
  unfold core7App
  have h0 := core7Semantic_selectedNat σ p s t 0 (by omega)
  have h1 := core7Semantic_selectedNat σ p s t 1 (by omega)
  rw [h0, h1]
  generalize h : (σ p s) t = z
  fin_cases z <;> simp_all [fin3BV]

lemma core7Semantic_appNat (σ : Core7Pair → Fin3 → Equiv.Perm Fin3)
    (p : Nat) (hp : p < 14) (s t : Fin3) :
    core7App (core7SemanticBits σ) p (fin3BV s) (fin3BV t) =
      fin3BV ((σ ⟨p, hp⟩ s) t) := by
  simpa using core7Semantic_app σ ⟨p, hp⟩ s t

lemma bitVec2_zero_eq_fin3BV : (0 : BitVec 2) = fin3BV 0 := rfl
lemma bitVec2_one_eq_fin3BV : (1 : BitVec 2) = fin3BV 1 := rfl
lemma bitVec2_two_eq_fin3BV : (2 : BitVec 2) = fin3BV 2 := rfl

set_option maxRecDepth 100000 in
/-- The explicit permutation-matrix encoding is a satisfying Boolean assignment. -/
lemma core7Semantic_satisfies (σ : Core7Pair → Fin3 → Equiv.Perm Fin3)
    (hσ : core7Chains σ) : core7Formula (core7SemanticBits σ) = true := by
  have hv := core7Semantic_all_valid σ
  simp only [core7Formula, hv, Bool.true_and]
  rcases hσ 0 0 with ⟨h000, h100, h200, h300, h400, h500, h600⟩
  rcases hσ 0 1 with ⟨h001, h101, h201, h301, h401, h501, h601⟩
  rcases hσ 0 2 with ⟨h002, h102, h202, h302, h402, h502, h602⟩
  rcases hσ 1 0 with ⟨h010, h110, h210, h310, h410, h510, h610⟩
  rcases hσ 1 1 with ⟨h011, h111, h211, h311, h411, h511, h611⟩
  rcases hσ 1 2 with ⟨h012, h112, h212, h312, h412, h512, h612⟩
  rcases hσ 2 0 with ⟨h020, h120, h220, h320, h420, h520, h620⟩
  rcases hσ 2 1 with ⟨h021, h121, h221, h321, h421, h521, h621⟩
  rcases hσ 2 2 with ⟨h022, h122, h222, h322, h422, h522, h622⟩
  simp only [core7ChainAll, core7Chain]
  rw [bitVec2_zero_eq_fin3BV, bitVec2_one_eq_fin3BV, bitVec2_two_eq_fin3BV]
  simp only [core7Semantic_appNat σ 0 (by omega), core7Semantic_appNat σ 1 (by omega),
    core7Semantic_appNat σ 2 (by omega), core7Semantic_appNat σ 3 (by omega),
    core7Semantic_appNat σ 4 (by omega), core7Semantic_appNat σ 5 (by omega),
    core7Semantic_appNat σ 6 (by omega), core7Semantic_appNat σ 7 (by omega),
    core7Semantic_appNat σ 8 (by omega), core7Semantic_appNat σ 9 (by omega),
    core7Semantic_appNat σ 10 (by omega), core7Semantic_appNat σ 11 (by omega),
    core7Semantic_appNat σ 12 (by omega), core7Semantic_appNat σ 13 (by omega)]
  simp only [Bool.and_eq_true, beq_iff_eq]
  repeat' apply And.intro
  all_goals first
    | exact congrArg fin3BV h000.symm | exact congrArg fin3BV h001.symm
    | exact congrArg fin3BV h002.symm | exact congrArg fin3BV h010.symm
    | exact congrArg fin3BV h011.symm | exact congrArg fin3BV h012.symm
    | exact congrArg fin3BV h020.symm | exact congrArg fin3BV h021.symm
    | exact congrArg fin3BV h022.symm | exact congrArg fin3BV h100.symm
    | exact congrArg fin3BV h101.symm | exact congrArg fin3BV h102.symm
    | exact congrArg fin3BV h110.symm | exact congrArg fin3BV h111.symm
    | exact congrArg fin3BV h112.symm | exact congrArg fin3BV h120.symm
    | exact congrArg fin3BV h121.symm | exact congrArg fin3BV h122.symm
    | exact congrArg fin3BV h200.symm | exact congrArg fin3BV h201.symm
    | exact congrArg fin3BV h202.symm | exact congrArg fin3BV h210.symm
    | exact congrArg fin3BV h211.symm | exact congrArg fin3BV h212.symm
    | exact congrArg fin3BV h220.symm | exact congrArg fin3BV h221.symm
    | exact congrArg fin3BV h222.symm | exact congrArg fin3BV h300.symm
    | exact congrArg fin3BV h301.symm | exact congrArg fin3BV h302.symm
    | exact congrArg fin3BV h310.symm | exact congrArg fin3BV h311.symm
    | exact congrArg fin3BV h312.symm | exact congrArg fin3BV h320.symm
    | exact congrArg fin3BV h321.symm | exact congrArg fin3BV h322.symm
    | exact congrArg fin3BV h400.symm | exact congrArg fin3BV h401.symm
    | exact congrArg fin3BV h402.symm | exact congrArg fin3BV h410.symm
    | exact congrArg fin3BV h411.symm | exact congrArg fin3BV h412.symm
    | exact congrArg fin3BV h420.symm | exact congrArg fin3BV h421.symm
    | exact congrArg fin3BV h422.symm | exact congrArg fin3BV h500.symm
    | exact congrArg fin3BV h501.symm | exact congrArg fin3BV h502.symm
    | exact congrArg fin3BV h510.symm | exact congrArg fin3BV h511.symm
    | exact congrArg fin3BV h512.symm | exact congrArg fin3BV h520.symm
    | exact congrArg fin3BV h521.symm | exact congrArg fin3BV h522.symm
    | exact congrArg fin3BV h600.symm | exact congrArg fin3BV h601.symm
    | exact congrArg fin3BV h602.symm | exact congrArg fin3BV h610.symm
    | exact congrArg fin3BV h611.symm | exact congrArg fin3BV h612.symm
    | exact congrArg fin3BV h620.symm | exact congrArg fin3BV h621.symm
    | exact congrArg fin3BV h622.symm

/-- There is no semantic family of 42 permutations satisfying the seven chains. -/
theorem core7_free_three_no_semantic :
    ¬ ∃ σ : Core7Pair → Fin3 → Equiv.Perm Fin3, core7Chains σ := by
  rintro ⟨σ, hσ⟩
  have hs := core7Semantic_satisfies σ hσ
  have hu := core7_free_three_unsat (core7SemanticBits σ)
  rw [hs] at hu
  exact Bool.noConfusion hu

/-! ## Pattern realization and fibre transport -/

noncomputable def core7BasePair {B : Type u} [Finite B]
    (op : B → B → B) (hB : E677 op) (a : B) : Core7Pair → B × B := fun p =>
  let b := L13B op hB a
  let c := L13C op hB a
  let d := L13D op hB a
  let u := L13U op a
  let v := L13V op hB a
  let w := L13W op a
  let q := L13P op hB a
  ![(a,b), (a,d), (a,q), (a,u), (a,w), (b,b), (b,c), (b,v),
    (c,d), (d,b), (d,v), (q,a), (u,a), (v,b)] p

noncomputable def core7SigmaOfLaw {B : Type u} [Finite B]
    (op : B → B → B) (hB : E677 op) (a : B)
    (c : B → B → Fin3 → Fin3 → Fin3)
    (hinj : ∀ x y s, Function.Injective (c x y s)) :
    Core7Pair → Fin3 → Equiv.Perm Fin3 := fun p s =>
  let xy := core7BasePair op hB a p
  Equiv.ofBijective (c xy.1 xy.2 s)
    ⟨hinj xy.1 xy.2 s, Finite.injective_iff_surjective.mp (hinj xy.1 xy.2 s)⟩

lemma core7SigmaOfLaw_apply {B : Type u} [Finite B]
    (op : B → B → B) (hB : E677 op) (a : B)
    (c : B → B → Fin3 → Fin3 → Fin3)
    (hinj : ∀ x y s, Function.Injective (c x y s)) (p : Core7Pair) (s t : Fin3) :
    core7SigmaOfLaw op hB a c hinj p s t =
      c (core7BasePair op hB a p).1 (core7BasePair op hB a p).2 s t := rfl

lemma core7_eq4_occurrence {B : Type u} [Finite B]
    (op : B → B → B) (hB : E677 op)
    (c : B → B → Fin3 → Fin3 → Fin3) (hEq4 : Eq4 op hB c)
    (x y : B) (s t : Fin3) :
    s = c (L10P1 op hB (x,y)).1 (L10P1 op hB (x,y)).2 t
      (c (L10P2 op (x,y)).1 (L10P2 op (x,y)).2 s
        (c (L10P4 op (x,y)).1 (L10P4 op (x,y)).2
          (c (L10P3 (x,y)).1 (L10P3 (x,y)).2 t s) t)) := by
  simpa [L10P1, L10P2, L10P3, L10P4] using hEq4 x y s t

lemma core7_pattern_chains {B : Type u} [Finite B]
    (op : B → B → B) (hB : E677 op) (h255 : E255 op) (a : B)
    (c : B → B → Fin3 → Fin3 → Fin3)
    (hinj : ∀ x y s, Function.Injective (c x y s))
    (hEq4 : Eq4 op hB c) : core7Chains (core7SigmaOfLaw op hB a c hinj) := by
  intro s t
  have hpa := core7_eq4_occurrence op hB c hEq4 (L13P op hB a) a s t
  have hvd := core7_eq4_occurrence op hB c hEq4 (L13V op hB a) (L13D op hB a) s t
  have hcb := core7_eq4_occurrence op hB c hEq4 (L13C op hB a) (L13B op hB a) s t
  have hau := core7_eq4_occurrence op hB c hEq4 a (L13U op a) s t
  have hbv := core7_eq4_occurrence op hB c hEq4 (L13B op hB a) (L13V op hB a) s t
  have hba := core7_eq4_occurrence op hB c hEq4 (L13B op hB a) a s t
  have hbb := core7_eq4_occurrence op hB c hEq4 (L13B op hB a) (L13B op hB a) s t
  rcases L15_pair_p_a op hB h255 a with ⟨hpa1, hpa2, hpa3, hpa4⟩
  rcases L15_pair_v_d op hB h255 a with ⟨hvd1, hvd2, hvd3, hvd4⟩
  rcases L15_pair_c_b op hB h255 a with ⟨hcb1, hcb2, hcb3, hcb4⟩
  rcases L15_pair_a_u op hB h255 a with ⟨hau1, hau2, hau3, hau4⟩
  rcases L15_pair_b_v op hB h255 a with ⟨hbv1, hbv2, hbv3, hbv4⟩
  rcases L15_pair_b_a op hB h255 a with ⟨hba1, hba2, hba3, hba4⟩
  rcases L15_pair_b_b op hB h255 a with ⟨hbb1, hbb2, hbb3, hbb4⟩
  rw [hpa1, hpa2, hpa3, hpa4] at hpa
  rw [hvd1, hvd2, hvd3, hvd4] at hvd
  rw [hcb1, hcb2, hcb3, hcb4] at hcb
  rw [hau1, hau2, hau3, hau4] at hau
  rw [hbv1, hbv2, hbv3, hbv4] at hbv
  rw [hba1, hba2, hba3, hba4] at hba
  rw [hbb1, hbb2, hbb3, hbb4] at hbb
  simpa [core7SigmaOfLaw_apply, core7BasePair] using
    And.intro hpa (And.intro hvd (And.intro hcb (And.intro hau (And.intro hbv (And.intro hba hbb)))))

/-- FIBRE-3 EXCLUSION: no finite surjective E677 homomorphism onto an E255
base can have a fibre of cardinality three. -/
theorem fibre3_exclusion
    {M : Type u} {B : Type v} [Finite M] [Finite B]
    (opM : M → M → M) (opB : B → B → B)
    (hM : E677 opM) (hB : E677 opB) (h255 : E255 opB)
    (φ : M → B) (hφ : Function.Surjective φ)
    (hhom : IsMagmaHom opM opB φ) (a : B)
    (ha : Nat.card {m : M // φ m = a} = 3) : False := by
  classical
  have hfibres (y : B) : Nat.card {m : M // φ m = y} = 3 :=
    (L2_quotient_fibres opM opB hM hB φ hφ hhom y a).trans ha
  obtain ⟨Fib, hFibFinite, _e, c, hFibCard, _hefst, _heop, hinj, hEq4⟩ :=
    L7_coordinatization opM opB hM φ hφ hhom 3 hfibres
  let _ : Finite Fib := hFibFinite
  let e3 : Fib ≃ Fin3 := Finite.equivFinOfCardEq hFibCard
  let c3 : B → B → Fin3 → Fin3 → Fin3 := fun x y s t =>
    e3 (c x y (e3.symm s) (e3.symm t))
  have hinj3 : ∀ x y s, Function.Injective (c3 x y s) := by
    intro x y s t₁ t₂ ht
    apply e3.symm.injective
    apply hinj x y (e3.symm s)
    exact e3.injective ht
  have hEq43 : Eq4 opB hB c3 := by
    intro x y s t
    apply e3.symm.injective
    simpa [c3] using hEq4 x y (e3.symm s) (e3.symm t)
  exact core7_free_three_no_semantic
    ⟨core7SigmaOfLaw opB hB a c3 hinj3,
      core7_pattern_chains opB hB h255 a c3 hinj3 hEq43⟩

theorem fibre_two_or_three_exclusion
    {M : Type u} {B : Type v} [Finite M] [Finite B]
    (opM : M → M → M) (opB : B → B → B)
    (hM : E677 opM) (hB : E677 opB) (h255 : E255 opB)
    (φ : M → B) (hφ : Function.Surjective φ)
    (hhom : IsMagmaHom opM opB φ) (a : B)
    (ha : Nat.card {m : M // φ m = a} = 2 ∨ Nat.card {m : M // φ m = a} = 3) : False :=
  ha.elim (fibre2_exclusion opM opB hM hB h255 φ hφ hhom a)
    (fibre3_exclusion opM opB hM hB h255 φ hφ hhom a)

#print axioms core7_free_three_unsat
#print axioms core7_free_three_no_semantic
#print axioms core7_pattern_chains
#print axioms fibre3_exclusion
#print axioms fibre_two_or_three_exclusion

end Ext677
