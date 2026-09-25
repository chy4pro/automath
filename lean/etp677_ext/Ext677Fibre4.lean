import Ext677Minimal
import Std.Tactic.BVDecide
import Mathlib.Tactic

set_option maxHeartbeats 400000
set_option maxRecDepth 4000

/-!
# Exclusion of four-element fibres at an E255 defect

The finite lemma in this file is the order-four Core-7 permutation-matrix
formula with the four distinguished nonfixed-point clauses.  It is discharged
by one `bv_decide` certificate.  The semantic bridge and fibre transport are
ordinary kernel-checked proofs.
-/

namespace Ext677

open Function

universe u v

abbrev Fin4 := Fin 4

/-! ## The order-four Boolean formula -/

def core7nh4SigBit (a : BitVec 896) (p s t z : Nat) : Bool :=
  a.getLsbD (p * 64 + s * 16 + t * 4 + z)

def core7nh4OneHot4 (a b c d : Bool) : Bool :=
  (a || b || c || d) &&
    !(a && b) && !(a && c) && !(a && d) &&
    !(b && c) && !(b && d) && !(c && d)

def core7nh4RowValid (a : BitVec 896) (p s : Nat) : Bool :=
  core7nh4OneHot4 (core7nh4SigBit a p s 0 0) (core7nh4SigBit a p s 0 1)
      (core7nh4SigBit a p s 0 2) (core7nh4SigBit a p s 0 3) &&
  core7nh4OneHot4 (core7nh4SigBit a p s 1 0) (core7nh4SigBit a p s 1 1)
      (core7nh4SigBit a p s 1 2) (core7nh4SigBit a p s 1 3) &&
  core7nh4OneHot4 (core7nh4SigBit a p s 2 0) (core7nh4SigBit a p s 2 1)
      (core7nh4SigBit a p s 2 2) (core7nh4SigBit a p s 2 3) &&
  core7nh4OneHot4 (core7nh4SigBit a p s 3 0) (core7nh4SigBit a p s 3 1)
      (core7nh4SigBit a p s 3 2) (core7nh4SigBit a p s 3 3) &&
  core7nh4OneHot4 (core7nh4SigBit a p s 0 0) (core7nh4SigBit a p s 1 0)
      (core7nh4SigBit a p s 2 0) (core7nh4SigBit a p s 3 0) &&
  core7nh4OneHot4 (core7nh4SigBit a p s 0 1) (core7nh4SigBit a p s 1 1)
      (core7nh4SigBit a p s 2 1) (core7nh4SigBit a p s 3 1) &&
  core7nh4OneHot4 (core7nh4SigBit a p s 0 2) (core7nh4SigBit a p s 1 2)
      (core7nh4SigBit a p s 2 2) (core7nh4SigBit a p s 3 2) &&
  core7nh4OneHot4 (core7nh4SigBit a p s 0 3) (core7nh4SigBit a p s 1 3)
      (core7nh4SigBit a p s 2 3) (core7nh4SigBit a p s 3 3)

def core7nh4Rows4 (a : BitVec 896) (p : Nat) : Bool :=
  core7nh4RowValid a p 0 && core7nh4RowValid a p 1 &&
    core7nh4RowValid a p 2 && core7nh4RowValid a p 3

def core7nh4AllValid (a : BitVec 896) : Bool :=
  core7nh4Rows4 a 0 && core7nh4Rows4 a 1 && core7nh4Rows4 a 2 &&
  core7nh4Rows4 a 3 && core7nh4Rows4 a 4 && core7nh4Rows4 a 5 &&
  core7nh4Rows4 a 6 && core7nh4Rows4 a 7 && core7nh4Rows4 a 8 &&
  core7nh4Rows4 a 9 && core7nh4Rows4 a 10 && core7nh4Rows4 a 11 &&
  core7nh4Rows4 a 12 && core7nh4Rows4 a 13

def core7nh4SelectedBit (a : BitVec 896) (p : Nat)
    (s t : BitVec 2) (z : Nat) : Bool :=
  (s == 0 && t == 0 && core7nh4SigBit a p 0 0 z) ||
  (s == 0 && t == 1 && core7nh4SigBit a p 0 1 z) ||
  (s == 0 && t == 2 && core7nh4SigBit a p 0 2 z) ||
  (s == 0 && t == 3 && core7nh4SigBit a p 0 3 z) ||
  (s == 1 && t == 0 && core7nh4SigBit a p 1 0 z) ||
  (s == 1 && t == 1 && core7nh4SigBit a p 1 1 z) ||
  (s == 1 && t == 2 && core7nh4SigBit a p 1 2 z) ||
  (s == 1 && t == 3 && core7nh4SigBit a p 1 3 z) ||
  (s == 2 && t == 0 && core7nh4SigBit a p 2 0 z) ||
  (s == 2 && t == 1 && core7nh4SigBit a p 2 1 z) ||
  (s == 2 && t == 2 && core7nh4SigBit a p 2 2 z) ||
  (s == 2 && t == 3 && core7nh4SigBit a p 2 3 z) ||
  (s == 3 && t == 0 && core7nh4SigBit a p 3 0 z) ||
  (s == 3 && t == 1 && core7nh4SigBit a p 3 1 z) ||
  (s == 3 && t == 2 && core7nh4SigBit a p 3 2 z) ||
  (s == 3 && t == 3 && core7nh4SigBit a p 3 3 z)

def core7nh4App (a : BitVec 896) (p : Nat) (s t : BitVec 2) : BitVec 2 :=
  if core7nh4SelectedBit a p s t 0 then 0 else
  if core7nh4SelectedBit a p s t 1 then 1 else
  if core7nh4SelectedBit a p s t 2 then 2 else 3

def core7nh4Chain (a : BitVec 896) (p1 p2 p3 p4 : Nat)
    (s t : BitVec 2) : Bool :=
  let r1 := core7nh4App a p1 t s
  let r2 := core7nh4App a p2 r1 t
  let r3 := core7nh4App a p3 s r2
  let r4 := core7nh4App a p4 t r3
  r4 == s

def core7nh4ChainAll (a : BitVec 896) (p1 p2 p3 p4 : Nat) : Bool :=
  core7nh4Chain a p1 p2 p3 p4 0 0 && core7nh4Chain a p1 p2 p3 p4 0 1 &&
  core7nh4Chain a p1 p2 p3 p4 0 2 && core7nh4Chain a p1 p2 p3 p4 0 3 &&
  core7nh4Chain a p1 p2 p3 p4 1 0 && core7nh4Chain a p1 p2 p3 p4 1 1 &&
  core7nh4Chain a p1 p2 p3 p4 1 2 && core7nh4Chain a p1 p2 p3 p4 1 3 &&
  core7nh4Chain a p1 p2 p3 p4 2 0 && core7nh4Chain a p1 p2 p3 p4 2 1 &&
  core7nh4Chain a p1 p2 p3 p4 2 2 && core7nh4Chain a p1 p2 p3 p4 2 3 &&
  core7nh4Chain a p1 p2 p3 p4 3 0 && core7nh4Chain a p1 p2 p3 p4 3 1 &&
  core7nh4Chain a p1 p2 p3 p4 3 2 && core7nh4Chain a p1 p2 p3 p4 3 3

def core7nh4Formula (a : BitVec 896) : Bool :=
  core7nh4AllValid a &&
  !core7nh4SigBit a 12 0 0 0 && !core7nh4SigBit a 12 1 0 0 &&
  !core7nh4SigBit a 12 2 0 0 && !core7nh4SigBit a 12 3 0 0 &&
  core7nh4ChainAll a 2 12 11 0 &&
  core7nh4ChainAll a 10 1 13 9 &&
  core7nh4ChainAll a 6 5 8 7 &&
  core7nh4ChainAll a 12 3 4 12 &&
  core7nh4ChainAll a 13 7 6 13 &&
  core7nh4ChainAll a 0 11 5 1 &&
  core7nh4ChainAll a 5 9 7 6

set_option maxHeartbeats 800000 in
set_option maxRecDepth 100000 in
/-- The single finite certificate: Core-7 plus NH has no order-four model. -/
theorem core7nh4_unsat (a : BitVec 896) : core7nh4Formula a = false := by
  simp (config := { maxSteps := 1000000 }) only
    [core7nh4Formula, core7nh4AllValid, core7nh4Rows4,
    core7nh4RowValid, core7nh4ChainAll, core7nh4Chain, core7nh4App,
    core7nh4SelectedBit, core7nh4SigBit, core7nh4OneHot4]
  bv_decide (config := { timeout := 600, maxSteps := 1000000 })

/-! ## Semantic bridge -/

def core7Chains4 (σ : Core7Pair → Fin4 → Equiv.Perm Fin4) : Prop :=
  ∀ s t,
    s = σ 0 t (σ 11 s (σ 12 (σ 2 t s) t)) ∧
    s = σ 9 t (σ 13 s (σ 1 (σ 10 t s) t)) ∧
    s = σ 7 t (σ 8 s (σ 5 (σ 6 t s) t)) ∧
    s = σ 12 t (σ 4 s (σ 3 (σ 12 t s) t)) ∧
    s = σ 13 t (σ 6 s (σ 7 (σ 13 t s) t)) ∧
    s = σ 1 t (σ 5 s (σ 11 (σ 0 t s) t)) ∧
    s = σ 6 t (σ 7 s (σ 9 (σ 5 t s) t))

def core7nh4SemanticBit (σ : Core7Pair → Fin4 → Equiv.Perm Fin4)
    (i : Fin 896) : Bool :=
  let p : Core7Pair := Fin.ofNat 14 (i.val / 64)
  let s : Fin4 := Fin.ofNat 4 (i.val / 16)
  let t : Fin4 := Fin.ofNat 4 (i.val / 4)
  let z : Fin4 := Fin.ofNat 4 i.val
  decide (σ p s t = z)

def core7nh4SemanticBits (σ : Core7Pair → Fin4 → Equiv.Perm Fin4) : BitVec 896 :=
  BitVec.setWidth 896 (BitVec.ofBoolListLE (List.ofFn (core7nh4SemanticBit σ)))

lemma core7nh4SemanticBits_get (σ : Core7Pair → Fin4 → Equiv.Perm Fin4)
    (p : Core7Pair) (s t z : Fin4) :
    core7nh4SigBit (core7nh4SemanticBits σ) p.val s.val t.val z.val =
      decide (σ p s t = z) := by
  let i := p.val * 64 + s.val * 16 + t.val * 4 + z.val
  have hi : i < 896 := by dsimp [i]; omega
  have hp : Fin.ofNat 14 (i / 64) = p := by
    apply Fin.ext
    simp [i]
    omega
  have hs : Fin.ofNat 4 (i / 16) = s := by
    apply Fin.ext
    simp [i]
    omega
  have ht : Fin.ofNat 4 (i / 4) = t := by
    apply Fin.ext
    simp [i]
    omega
  have hz : Fin.ofNat 4 i = z := by
    apply Fin.ext
    simp [i]
    omega
  unfold core7nh4SigBit core7nh4SemanticBits
  change (BitVec.setWidth 896
    (BitVec.ofBoolListLE (List.ofFn (core7nh4SemanticBit σ)))).getLsbD i = _
  rw [BitVec.getLsbD_setWidth, BitVec.getLsbD_ofBoolListLE,
    List.getD_eq_getElem?_getD, List.getElem?_ofFn]
  simp only [hi, decide_true, Bool.true_and, ↓reduceDIte, Option.getD_some]
  unfold core7nh4SemanticBit
  dsimp only
  rw [hp, hs, ht, hz]

lemma core7nh4SemanticBits_getNat (σ : Core7Pair → Fin4 → Equiv.Perm Fin4)
    (p : Core7Pair) (s t z : Nat) (hs : s < 4) (ht : t < 4) (hz : z < 4) :
    core7nh4SigBit (core7nh4SemanticBits σ) p.val s t z =
      decide (σ p ⟨s, hs⟩ ⟨t, ht⟩ = ⟨z, hz⟩) := by
  simpa using core7nh4SemanticBits_get σ p ⟨s, hs⟩ ⟨t, ht⟩ ⟨z, hz⟩

lemma core7nh4OneHot_value (x : Fin4) :
    core7nh4OneHot4 (decide (x = 0)) (decide (x = 1))
      (decide (x = 2)) (decide (x = 3)) = true := by
  fin_cases x <;> decide

lemma core7nh4OneHot_perm_column (e : Equiv.Perm Fin4) (z : Fin4) :
    core7nh4OneHot4 (decide (e 0 = z)) (decide (e 1 = z))
      (decide (e 2 = z)) (decide (e 3 = z)) = true := by
  have h := e.apply_symm_apply z
  generalize hpre : e.symm z = q at h
  have hne (i : Fin4) (hi : i ≠ q) : e i ≠ z := by
    intro hiz
    exact hi (e.injective (hiz.trans h.symm))
  fin_cases q <;> simp_all [core7nh4OneHot4]

lemma core7nh4Semantic_row_valid (σ : Core7Pair → Fin4 → Equiv.Perm Fin4)
    (p : Core7Pair) (s : Fin4) :
    core7nh4RowValid (core7nh4SemanticBits σ) p.val s.val = true := by
  simp only [core7nh4RowValid]
  rw [core7nh4SemanticBits_getNat σ p s.val 0 0 (by omega) (by omega) (by omega),
    core7nh4SemanticBits_getNat σ p s.val 0 1 (by omega) (by omega) (by omega),
    core7nh4SemanticBits_getNat σ p s.val 0 2 (by omega) (by omega) (by omega),
    core7nh4SemanticBits_getNat σ p s.val 0 3 (by omega) (by omega) (by omega),
    core7nh4SemanticBits_getNat σ p s.val 1 0 (by omega) (by omega) (by omega),
    core7nh4SemanticBits_getNat σ p s.val 1 1 (by omega) (by omega) (by omega),
    core7nh4SemanticBits_getNat σ p s.val 1 2 (by omega) (by omega) (by omega),
    core7nh4SemanticBits_getNat σ p s.val 1 3 (by omega) (by omega) (by omega),
    core7nh4SemanticBits_getNat σ p s.val 2 0 (by omega) (by omega) (by omega),
    core7nh4SemanticBits_getNat σ p s.val 2 1 (by omega) (by omega) (by omega),
    core7nh4SemanticBits_getNat σ p s.val 2 2 (by omega) (by omega) (by omega),
    core7nh4SemanticBits_getNat σ p s.val 2 3 (by omega) (by omega) (by omega),
    core7nh4SemanticBits_getNat σ p s.val 3 0 (by omega) (by omega) (by omega),
    core7nh4SemanticBits_getNat σ p s.val 3 1 (by omega) (by omega) (by omega),
    core7nh4SemanticBits_getNat σ p s.val 3 2 (by omega) (by omega) (by omega),
    core7nh4SemanticBits_getNat σ p s.val 3 3 (by omega) (by omega) (by omega)]
  have hr0 := core7nh4OneHot_value ((σ p s) 0)
  have hr1 := core7nh4OneHot_value ((σ p s) 1)
  have hr2 := core7nh4OneHot_value ((σ p s) 2)
  have hr3 := core7nh4OneHot_value ((σ p s) 3)
  have hc0 := core7nh4OneHot_perm_column (σ p s) 0
  have hc1 := core7nh4OneHot_perm_column (σ p s) 1
  have hc2 := core7nh4OneHot_perm_column (σ p s) 2
  have hc3 := core7nh4OneHot_perm_column (σ p s) 3
  simp [hr0, hr1, hr2, hr3, hc0, hc1, hc2, hc3]

lemma core7nh4Semantic_row_valid_nat
    (σ : Core7Pair → Fin4 → Equiv.Perm Fin4)
    (p s : Nat) (hp : p < 14) (hs : s < 4) :
    core7nh4RowValid (core7nh4SemanticBits σ) p s = true := by
  simpa using core7nh4Semantic_row_valid σ ⟨p, hp⟩ ⟨s, hs⟩

lemma core7nh4Semantic_all_valid (σ : Core7Pair → Fin4 → Equiv.Perm Fin4) :
    core7nh4AllValid (core7nh4SemanticBits σ) = true := by
  simp only [core7nh4AllValid, core7nh4Rows4]
  simp [core7nh4Semantic_row_valid_nat σ]

def fin4BV (x : Fin4) : BitVec 2 := BitVec.ofNat 2 x.val

lemma core7nh4Semantic_selected (σ : Core7Pair → Fin4 → Equiv.Perm Fin4)
    (p : Core7Pair) (s t z : Fin4) :
    core7nh4SelectedBit (core7nh4SemanticBits σ) p.val (fin4BV s) (fin4BV t) z.val =
      decide ((σ p s) t = z) := by
  fin_cases s <;> fin_cases t <;> fin_cases z <;>
    simp [core7nh4SelectedBit, fin4BV, core7nh4SemanticBits_getNat σ p]

lemma core7nh4Semantic_selectedNat
    (σ : Core7Pair → Fin4 → Equiv.Perm Fin4)
    (p : Core7Pair) (s t : Fin4) (z : Nat) (hz : z < 4) :
    core7nh4SelectedBit (core7nh4SemanticBits σ) p.val (fin4BV s) (fin4BV t) z =
      decide ((σ p s) t = ⟨z, hz⟩) := by
  simpa using core7nh4Semantic_selected σ p s t ⟨z, hz⟩

lemma core7nh4Semantic_app (σ : Core7Pair → Fin4 → Equiv.Perm Fin4)
    (p : Core7Pair) (s t : Fin4) :
    core7nh4App (core7nh4SemanticBits σ) p.val (fin4BV s) (fin4BV t) =
      fin4BV ((σ p s) t) := by
  unfold core7nh4App
  have h0 := core7nh4Semantic_selectedNat σ p s t 0 (by omega)
  have h1 := core7nh4Semantic_selectedNat σ p s t 1 (by omega)
  have h2 := core7nh4Semantic_selectedNat σ p s t 2 (by omega)
  rw [h0, h1, h2]
  generalize h : (σ p s) t = z
  fin_cases z <;> simp_all [fin4BV]

lemma core7nh4Semantic_appNat (σ : Core7Pair → Fin4 → Equiv.Perm Fin4)
    (p : Nat) (hp : p < 14) (s t : Fin4) :
    core7nh4App (core7nh4SemanticBits σ) p (fin4BV s) (fin4BV t) =
      fin4BV ((σ ⟨p, hp⟩ s) t) := by
  simpa using core7nh4Semantic_app σ ⟨p, hp⟩ s t

lemma core7nh4Semantic_chain (σ : Core7Pair → Fin4 → Equiv.Perm Fin4)
    (p1 p2 p3 p4 : Nat) (hp1 : p1 < 14) (hp2 : p2 < 14)
    (hp3 : p3 < 14) (hp4 : p4 < 14) (s t : Fin4)
    (h : s = σ ⟨p4, hp4⟩ t
      (σ ⟨p3, hp3⟩ s (σ ⟨p2, hp2⟩ (σ ⟨p1, hp1⟩ t s) t))) :
    core7nh4Chain (core7nh4SemanticBits σ) p1 p2 p3 p4 (fin4BV s) (fin4BV t) = true := by
  unfold core7nh4Chain
  rw [core7nh4Semantic_appNat σ p1 hp1]
  change (core7nh4App (core7nh4SemanticBits σ) p4 (fin4BV t)
    (core7nh4App (core7nh4SemanticBits σ) p3 (fin4BV s)
      (core7nh4App (core7nh4SemanticBits σ) p2
        (fin4BV ((σ ⟨p1, hp1⟩ t) s)) (fin4BV t))) == fin4BV s) = true
  rw [core7nh4Semantic_appNat σ p2 hp2]
  rw [core7nh4Semantic_appNat σ p3 hp3]
  rw [core7nh4Semantic_appNat σ p4 hp4]
  simp only [beq_iff_eq]
  exact congrArg fin4BV h.symm

lemma core7nh4Semantic_chain_all (σ : Core7Pair → Fin4 → Equiv.Perm Fin4)
    (p1 p2 p3 p4 : Nat) (hp1 : p1 < 14) (hp2 : p2 < 14)
    (hp3 : p3 < 14) (hp4 : p4 < 14)
    (h : ∀ s t, s = σ ⟨p4, hp4⟩ t
      (σ ⟨p3, hp3⟩ s (σ ⟨p2, hp2⟩ (σ ⟨p1, hp1⟩ t s) t))) :
    core7nh4ChainAll (core7nh4SemanticBits σ) p1 p2 p3 p4 = true := by
  have hc (s t : Fin4) :=
    core7nh4Semantic_chain σ p1 p2 p3 p4 hp1 hp2 hp3 hp4 s t (h s t)
  unfold core7nh4ChainAll
  rw [show (0 : BitVec 2) = fin4BV 0 from rfl,
    show (1 : BitVec 2) = fin4BV 1 from rfl,
    show (2 : BitVec 2) = fin4BV 2 from rfl,
    show (3 : BitVec 2) = fin4BV 3 from rfl]
  simp only [hc]
  decide

/-- A semantic Core-7+NH family produces a satisfying bit assignment. -/
lemma core7nh4Semantic_satisfies (σ : Core7Pair → Fin4 → Equiv.Perm Fin4)
    (hσ : core7Chains4 σ) (hnh : ∀ t, σ 12 t 0 ≠ 0) :
    core7nh4Formula (core7nh4SemanticBits σ) = true := by
  have hv := core7nh4Semantic_all_valid σ
  have hn (t : Fin4) : core7nh4SigBit (core7nh4SemanticBits σ) 12 t.val 0 0 = false := by
    change core7nh4SigBit (core7nh4SemanticBits σ) (12 : Core7Pair).val t.val 0 0 = false
    rw [core7nh4SemanticBits_getNat σ 12 t.val 0 0 (by omega) (by omega) (by omega)]
    simp [hnh t]
  have hn0 : core7nh4SigBit (core7nh4SemanticBits σ) 12 0 0 0 = false := by
    simpa using hn 0
  have hn1 : core7nh4SigBit (core7nh4SemanticBits σ) 12 1 0 0 = false := by
    simpa using hn 1
  have hn2 : core7nh4SigBit (core7nh4SemanticBits σ) 12 2 0 0 = false := by
    simpa using hn 2
  have hn3 : core7nh4SigBit (core7nh4SemanticBits σ) 12 3 0 0 = false := by
    simpa using hn 3
  have h0 := core7nh4Semantic_chain_all σ 2 12 11 0
    (by omega) (by omega) (by omega) (by omega) (fun s t ↦ (hσ s t).1)
  have h1 := core7nh4Semantic_chain_all σ 10 1 13 9
    (by omega) (by omega) (by omega) (by omega) (fun s t ↦ (hσ s t).2.1)
  have h2 := core7nh4Semantic_chain_all σ 6 5 8 7
    (by omega) (by omega) (by omega) (by omega) (fun s t ↦ (hσ s t).2.2.1)
  have h3 := core7nh4Semantic_chain_all σ 12 3 4 12
    (by omega) (by omega) (by omega) (by omega) (fun s t ↦ (hσ s t).2.2.2.1)
  have h4 := core7nh4Semantic_chain_all σ 13 7 6 13
    (by omega) (by omega) (by omega) (by omega) (fun s t ↦ (hσ s t).2.2.2.2.1)
  have h5 := core7nh4Semantic_chain_all σ 0 11 5 1
    (by omega) (by omega) (by omega) (by omega) (fun s t ↦ (hσ s t).2.2.2.2.2.1)
  have h6 := core7nh4Semantic_chain_all σ 5 9 7 6
    (by omega) (by omega) (by omega) (by omega) (fun s t ↦ (hσ s t).2.2.2.2.2.2)
  simp [core7nh4Formula, hv, hn0, hn1, hn2, hn3, h0, h1, h2, h3, h4, h5, h6]

/-- There is no semantic order-four Core-7 family satisfying NH. -/
theorem core7nh4_no_semantic :
    ¬ ∃ σ : Core7Pair → Fin4 → Equiv.Perm Fin4,
      core7Chains4 σ ∧ ∀ t, σ 12 t 0 ≠ 0 := by
  rintro ⟨σ, hchains, hnh⟩
  have hs := core7nh4Semantic_satisfies σ hchains hnh
  have hu := core7nh4_unsat (core7nh4SemanticBits σ)
  rw [hs] at hu
  exact Bool.noConfusion hu

/-! ## Pattern realization over `Fin 4` -/

noncomputable def fibre4PermOfLaw {B : Type u} [Finite B]
    (c : B → B → Fin4 → Fin4 → Fin4)
    (hinj : ∀ x y s, Function.Injective (c x y s))
    (x y : B) (s : Fin4) : Equiv.Perm Fin4 :=
  Equiv.ofBijective (c x y s)
    ⟨hinj x y s, Finite.injective_iff_surjective.mp (hinj x y s)⟩

noncomputable def core7Sigma4OfLaw {B : Type u} [Finite B]
    (op : B → B → B) (hB : E677 op) (a : B)
    (c : B → B → Fin4 → Fin4 → Fin4)
    (hinj : ∀ x y s, Function.Injective (c x y s)) :
    Core7Pair → Fin4 → Equiv.Perm Fin4 := fun p s =>
  let xy := core7BasePair op hB a p
  fibre4PermOfLaw c hinj xy.1 xy.2 s

lemma core7Sigma4OfLaw_apply {B : Type u} [Finite B]
    (op : B → B → B) (hB : E677 op) (a : B)
    (c : B → B → Fin4 → Fin4 → Fin4)
    (hinj : ∀ x y s, Function.Injective (c x y s))
    (p : Core7Pair) (s t : Fin4) :
    core7Sigma4OfLaw op hB a c hinj p s t =
      c (core7BasePair op hB a p).1 (core7BasePair op hB a p).2 s t := rfl

lemma core7_eq4_occurrence4 {B : Type u} [Finite B]
    (op : B → B → B) (hB : E677 op)
    (c : B → B → Fin4 → Fin4 → Fin4) (hEq4 : Eq4 op hB c)
    (x y : B) (s t : Fin4) :
    s = c (L10P1 op hB (x,y)).1 (L10P1 op hB (x,y)).2 t
      (c (L10P2 op (x,y)).1 (L10P2 op (x,y)).2 s
        (c (L10P4 op (x,y)).1 (L10P4 op (x,y)).2
          (c (L10P3 (x,y)).1 (L10P3 (x,y)).2 t s) t)) := by
  simpa [L10P1, L10P2, L10P3, L10P4] using hEq4 x y s t

lemma core7_pattern_chains4 {B : Type u} [Finite B]
    (op : B → B → B) (hB : E677 op) (h255 : E255 op) (a : B)
    (c : B → B → Fin4 → Fin4 → Fin4)
    (hinj : ∀ x y s, Function.Injective (c x y s))
    (hEq4 : Eq4 op hB c) : core7Chains4 (core7Sigma4OfLaw op hB a c hinj) := by
  intro s t
  have hpa := core7_eq4_occurrence4 op hB c hEq4 (L13P op hB a) a s t
  have hvd := core7_eq4_occurrence4 op hB c hEq4 (L13V op hB a) (L13D op hB a) s t
  have hcb := core7_eq4_occurrence4 op hB c hEq4 (L13C op hB a) (L13B op hB a) s t
  have hau := core7_eq4_occurrence4 op hB c hEq4 a (L13U op a) s t
  have hbv := core7_eq4_occurrence4 op hB c hEq4 (L13B op hB a) (L13V op hB a) s t
  have hba := core7_eq4_occurrence4 op hB c hEq4 (L13B op hB a) a s t
  have hbb := core7_eq4_occurrence4 op hB c hEq4 (L13B op hB a) (L13B op hB a) s t
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
  simpa [core7Sigma4OfLaw_apply, core7BasePair] using
    And.intro hpa (And.intro hvd (And.intro hcb
      (And.intro hau (And.intro hbv (And.intro hba hbb)))))

/-! ## The symbolic NH amplification -/

/-- Lemma 1: the two extra lifted E677 chains amplify the defect at `β`
to the four nonfixed-point constraints required by the finite lemma. -/
lemma fibre4_symbolic_nh
    (X A Bop C D : Fin4 → Equiv.Perm Fin4)
    (haa : ∀ s t, D t (C s (Bop (A t s) t)) = s)
    (hau : ∀ s t, X t (D s (C (X t s) t)) = s)
    (hdef : X (Bop (A 0 0) 0) 0 ≠ 0) :
    ∀ t, X t 0 ≠ 0 := by
  let β := Bop (A 0 0) 0
  have hbase : D 0 (C 0 β) = 0 := haa 0 0
  intro t hfix
  have ht : D 0 (C 0 t) = 0 := by
    apply (X t).injective
    simpa [hfix] using hau 0 t
  have htβ : t = β := by
    apply (C 0).injective
    apply (D 0).injective
    exact ht.trans hbase.symm
  exact hdef (by simpa [β, htβ] using hfix)

lemma fibre4_chain_aa {B : Type u} [Finite B]
    (op : B → B → B) (hB : E677 op) (a : B)
    (c : B → B → Fin4 → Fin4 → Fin4) (hEq4 : Eq4 op hB c)
    (s t : Fin4) :
    c a (X6W op a) t
      (c a (X6U op a) s (c (op a a) a (c a a t s) t)) = s := by
  have h := (hEq4 a a s t).symm
  rw [← X1_W_iterate op hB a] at h
  simpa [X6U] using h

lemma fibre4_chain_au {B : Type u} [Finite B]
    (op : B → B → B) (hB : E677 op) (h255 : E255 op) (a : B)
    (c : B → B → Fin4 → Fin4 → Fin4) (hEq4 : Eq4 op hB c)
    (s t : Fin4) :
    c (X6U op a) a t
      (c a (X6W op a) s (c a (X6U op a) (c (X6U op a) a t s) t)) = s := by
  have hua : op (X6U op a) a = a := window_U_mul op hB h255 a
  have hau : op a (X6U op a) = X6W op a := window_mul_U op hB h255 a
  have hdiv : ldiv op hB (X6U op a) a = a := (ldiv_unique op hB hua).symm
  have h := (hEq4 a (X6U op a) s t).symm
  rw [hua, hau, hdiv] at h
  exact h

/-! ## Fibre transport and exclusion -/

/-- FIBRE-4 DEFECT EXCLUSION: a four-element fibre cannot contain a point
where E255 fails when the E677 quotient satisfies E255. -/
theorem fibre4_defect_exclusion
    {M : Type u} {B : Type v} [Finite M] [Finite B]
    (opM : M → M → M) (opB : B → B → B)
    (hM : E677 opM) (hB : E677 opB) (h255 : E255 opB)
    (φ : M → B) (hφ : Function.Surjective φ)
    (hhom : IsMagmaHom opM opB φ)
    (m₀ : M) (hfail : ¬ E255At opM m₀)
    (ha : Nat.card {m : M // φ m = φ m₀} = 4) : False := by
  classical
  let a : B := φ m₀
  have hfibres (y : B) : Nat.card {m : M // φ m = y} = 4 :=
    (L2_quotient_fibres opM opB hM hB φ hφ hhom y a).trans ha
  obtain ⟨Fib, hFibFinite, e, c, hFibCard, he_fst, he_op, hinj, hEq4⟩ :=
    L7_coordinatization opM opB hM φ hφ hhom 4 hfibres
  let _ : Finite Fib := hFibFinite
  let q : Fib := (e m₀).2
  let eBase : Fib ≃ Fin4 := Finite.equivFinOfCardEq hFibCard
  let e4 : Fib ≃ Fin4 := eBase.trans (Equiv.swap (eBase q) 0)
  have he4q : e4 q = 0 := by simp [e4]
  let E : B × Fib ≃ B × Fin4 := Equiv.prodCongr (Equiv.refl B) e4
  let ee : M ≃ B × Fin4 := e.trans E
  let c4 : B → B → Fin4 → Fin4 → Fin4 := fun x y s t ↦
    e4 (c x y (e4.symm s) (e4.symm t))
  have hinj4 : ∀ x y s, Function.Injective (c4 x y s) := by
    intro x y s t₁ t₂ ht
    apply e4.symm.injective
    apply hinj x y (e4.symm s)
    exact e4.injective ht
  have hEq44 : Eq4 opB hB c4 := by
    intro x y s t
    apply e4.symm.injective
    simpa [c4] using hEq4 x y (e4.symm s) (e4.symm t)
  have hee_op (x y : M) :
      ee (opM x y) = productOp opB c4 (ee x) (ee y) := by
    rcases hx : e x with ⟨bx, sx⟩
    rcases hy : e y with ⟨by0, sy⟩
    have heex : ee x = (bx, e4 sx) := by
      simp [ee, E, hx]
    have heey : ee y = (by0, e4 sy) := by
      simp [ee, E, hy]
    change E (e (opM x y)) = _
    rw [he_op]
    rw [heex, heey]
    simp [E, c4, productOp, hx, hy]
  have hee_m₀ : ee m₀ = (a, 0) := by
    apply Prod.ext
    · change (e m₀).1 = a
      exact he_fst m₀
    · change e4 (e m₀).2 = 0
      exact he4q
  have hprod4 : E677 (productOp opB c4) :=
    (L3_eq4_iff opB hB c4).2 hEq44
  have hfail4 : ¬ E255At (productOp opB c4) (a, 0) := by
    intro hf
    apply hfail
    unfold E255At at hf ⊢
    apply ee.injective
    simp only [hee_op, hee_m₀]
    exact hf
  have hstar : ¬ ∃ s, c4 (X6U opB a) a s 0 = 0 := by
    simpa [X6U] using
      (L4_defect_iff opB hB h255 c4 hprod4 a 0).mp hfail4
  let X : Fin4 → Equiv.Perm Fin4 := fibre4PermOfLaw c4 hinj4 (X6U opB a) a
  let A : Fin4 → Equiv.Perm Fin4 := fibre4PermOfLaw c4 hinj4 a a
  let Bop : Fin4 → Equiv.Perm Fin4 :=
    fibre4PermOfLaw c4 hinj4 (opB a a) a
  let C : Fin4 → Equiv.Perm Fin4 := fibre4PermOfLaw c4 hinj4 a (X6U opB a)
  let D : Fin4 → Equiv.Perm Fin4 := fibre4PermOfLaw c4 hinj4 a (X6W opB a)
  have haa : ∀ s t, D t (C s (Bop (A t s) t)) = s := by
    intro s t
    exact fibre4_chain_aa opB hB a c4 hEq44 s t
  have hau : ∀ s t, X t (D s (C (X t s) t)) = s := by
    intro s t
    exact fibre4_chain_au opB hB h255 a c4 hEq44 s t
  have hdef : X (Bop (A 0 0) 0) 0 ≠ 0 := by
    intro hf
    apply hstar
    exact ⟨Bop (A 0 0) 0, hf⟩
  have hnhX : ∀ t, X t 0 ≠ 0 :=
    fibre4_symbolic_nh X A Bop C D haa hau hdef
  let σ := core7Sigma4OfLaw opB hB a c4 hinj4
  have hchains : core7Chains4 σ := core7_pattern_chains4 opB hB h255 a c4 hinj4 hEq44
  have hnh : ∀ t, σ 12 t 0 ≠ 0 := by
    intro t
    simpa [σ, X, core7Sigma4OfLaw, core7BasePair, X6U, L13U] using hnhX t
  exact core7nh4_no_semantic ⟨σ, hchains, hnh⟩

/-! ## Minimal-counterexample corollaries -/

/-- Every class of a proper nontrivial congruence of a minimal counterexample
has at least five elements. -/
theorem minimal_counterexample_congruence_class_ge_five
    {M : Type u} [Finite M] (op : M → M → M)
    (hmin : IsMinimalCounterexample op) (θ : MagmaCongruence op)
    (hnotTrivial : ¬ θ.IsTrivial) (hnotTotal : ¬ θ.IsTotal)
    (q : MagmaQuotient θ) :
    5 ≤ Nat.card {m : M // quotientMap θ m = q} := by
  have hB : E677 (quotientOp θ) :=
    L7a_E677_of_surjective_hom op (quotientOp θ) hmin.1.1
      (quotientMap θ) (quotientMap_surjective_hom θ).1
      (quotientMap_surjective_hom θ).2
  have hnotinj : ¬ Function.Injective (quotientMap θ) := by
    intro hinj
    apply hnotTrivial
    intro x y hxy
    exact hinj (Quotient.sound hxy)
  have hcollision : ∃ x y, quotientMap θ x = quotientMap θ y ∧ x ≠ y := by
    rw [Function.Injective] at hnotinj
    push Not at hnotinj
    exact hnotinj
  have hnotconst : ¬ ∃ q, ∀ m, quotientMap θ m = q := by
    rintro ⟨q, hq⟩
    apply hnotTotal
    intro x y
    exact Quotient.exact ((hq x).trans (hq y).symm)
  have h255 : E255 (quotientOp θ) := by
    rcases hmin.2 (MagmaQuotient θ) (quotientOp θ) (quotientMap θ)
      (quotientMap_surjective_hom θ).1 (quotientMap_surjective_hom θ).2 hcollision with
      hconst | h255
    · exact (hnotconst hconst).elim
    · exact h255
  have hge4 : 4 ≤ Nat.card {m : M // quotientMap θ m = q} :=
    minimal_counterexample_congruence_class_ge_four_clean op hmin θ
      hnotTrivial hnotTotal q
  have hne4 : Nat.card {m : M // quotientMap θ m = q} ≠ 4 := by
    intro hq4
    have hnot255 : ¬ E255 op := hmin.1.2
    rw [E255] at hnot255
    push Not at hnot255
    obtain ⟨m₀, hfail⟩ := hnot255
    have hm₀ : Nat.card {m : M // quotientMap θ m = quotientMap θ m₀} = 4 :=
      (equal_fibres op (quotientOp θ) hmin.1.1 hB (quotientMap θ)
        (quotientMap_surjective_hom θ).1 (quotientMap_surjective_hom θ).2
        (quotientMap θ m₀) q).trans hq4
    exact fibre4_defect_exclusion op (quotientOp θ) hmin.1.1 hB h255
      (quotientMap θ) (quotientMap_surjective_hom θ).1
      (quotientMap_surjective_hom θ).2 m₀ hfail hm₀
  omega

/-- A minimal counterexample is simple or all classes of every proper
nontrivial congruence have cardinality at least five. -/
theorem minimal_counterexample_no_class_le_four
    {M : Type u} [Finite M] (op : M → M → M)
    (hmin : IsMinimalCounterexample op) :
    IsSimple op ∨ ∀ (θ : MagmaCongruence op),
      ¬ θ.IsTrivial → ¬ θ.IsTotal → ∀ q : MagmaQuotient θ,
        5 ≤ Nat.card {m : M // quotientMap θ m = q} := by
  right
  intro θ hnotTrivial hnotTotal q
  exact minimal_counterexample_congruence_class_ge_five op hmin θ
    hnotTrivial hnotTotal q

#print axioms fibre4_symbolic_nh
#print axioms core7nh4_unsat
#print axioms core7nh4_no_semantic
#print axioms fibre4_defect_exclusion
#print axioms minimal_counterexample_congruence_class_ge_five
#print axioms minimal_counterexample_no_class_le_four

end Ext677
