import Ext677Core7Free

set_option maxHeartbeats 400000
set_option maxRecDepth 4000

/-!
# A clean hand proof of the order-three Core-7 exclusion

The only finite step below is the bridge worksheet from the human proof.  Its
checker uses six explicit permutation codes and kernel reduction (`rfl`), not
`bv_decide`, `native_decide`, or a generated certificate axiom.  The fourth
bridge chain and the final three chains are handled symbolically.
-/

namespace Ext677

open Function

/-! ## Symbolic chain calculus -/

def HandChain (P Q R Z : Fin3 → Equiv.Perm Fin3) : Prop :=
  ∀ s t, P t (Q s (Z (R t s) t)) = s

/-- Formula (5) of the hand proof: a collision determines every cell of `Z`. -/
lemma handChain_collision_formula {X Y Z : Fin3 → Equiv.Perm Fin3}
    (h : HandChain X Y X Z) (s t : Fin3) :
    Z (X t s) t = (Y s).symm ((X t).symm s) := by
  apply (Y s).injective
  apply (X t).injective
  simpa [HandChain] using h s t

/-! ## Six permutation codes and the finite bridge worksheet -/

abbrev HandPermCode := Fin 6
abbrev HandCodeOp := Fin3 → HandPermCode

def handPermNatApp (p x : Nat) : Nat :=
  match p, x with
  | 0, x => x
  | 1, 0 => 0 | 1, 1 => 2 | 1, _ => 1
  | 2, 0 => 1 | 2, 1 => 0 | 2, _ => 2
  | 3, 0 => 1 | 3, 1 => 2 | 3, _ => 0
  | 4, 0 => 2 | 4, 1 => 0 | 4, _ => 1
  | _, 0 => 2 | _, 1 => 1 | _, _ => 0

def handPermApp (p : HandPermCode) (x : Fin3) : Fin3 :=
  Fin.ofNat 3 (handPermNatApp p x)

def handPermInvApp (p : HandPermCode) (x : Fin3) : Fin3 :=
  Fin.ofNat 3 (handPermNatApp (![0, 1, 2, 4, 3, 5] p) x)

lemma handPerm_inv_app (p : HandPermCode) (x : Fin3) :
    handPermInvApp p (handPermApp p x) = x := by
  fin_cases p <;> fin_cases x <;> rfl

lemma handPerm_app_inv (p : HandPermCode) (x : Fin3) :
    handPermApp p (handPermInvApp p x) = x := by
  fin_cases p <;> fin_cases x <;> rfl

lemma handPermApp_injective (p : HandPermCode) : Function.Injective (handPermApp p) := by
  intro x y h
  have hi := congrArg (handPermInvApp p) h
  simpa [handPerm_inv_app] using hi

def HandCodeChain (P Q R Z : HandCodeOp) : Prop :=
  ∀ s t, handPermApp (P t)
    (handPermApp (Q s) (handPermApp (Z (handPermApp (R t) s)) t)) = s

@[ext] structure HandFastOp where
  a : Nat
  b : Nat
  c : Nat
deriving DecidableEq, Inhabited

def handFastRow (P : HandFastOp) (s : Nat) : Nat :=
  match s with | 0 => P.a | 1 => P.b | _ => P.c

def handFastApp (p x : Nat) : Nat := handPermNatApp p x

def handFastInv (p : Nat) : Nat :=
  match p with | 3 => 4 | 4 => 3 | p => p

def handFastRowCode? (a b c : Nat) : Option Nat :=
  match a, b, c with
  | 0, 1, 2 => some 0 | 0, 2, 1 => some 1
  | 1, 0, 2 => some 2 | 1, 2, 0 => some 3
  | 2, 0, 1 => some 4 | 2, 1, 0 => some 5
  | _, _, _ => none

def handFastNextVal (P Q R : HandFastOp) (r t : Nat) : Nat :=
  let s := handFastApp (handFastInv (handFastRow R t)) r
  handFastApp (handFastInv (handFastRow Q s))
    (handFastApp (handFastInv (handFastRow P t)) s)

def handFastNext (P Q R : HandFastOp) : Option HandFastOp :=
  match
      handFastRowCode? (handFastNextVal P Q R 0 0) (handFastNextVal P Q R 0 1)
        (handFastNextVal P Q R 0 2),
      handFastRowCode? (handFastNextVal P Q R 1 0) (handFastNextVal P Q R 1 1)
        (handFastNextVal P Q R 1 2),
      handFastRowCode? (handFastNextVal P Q R 2 0) (handFastNextVal P Q R 2 1)
        (handFastNextVal P Q R 2 2) with
  | some a, some b, some c => some ⟨a, b, c⟩
  | _, _, _ => none

def handAllNat : Nat → (Nat → Bool) → Bool
  | 0, _ => true
  | n + 1, f => f n && handAllNat n f

def handAllFastOps (f : HandFastOp → Bool) : Bool :=
  handAllNat 6 fun a ↦ handAllNat 6 fun b ↦ handAllNat 6 fun c ↦ f ⟨a, b, c⟩

def handBridgeConclusion (F L E : HandFastOp) : Bool :=
  (L.a == L.b) && (L.a == L.c) &&
    handAllNat 3 fun s ↦ handAllNat 3 fun t ↦
      handFastApp (handFastRow E t)
        (handFastApp (handFastRow F s) (handFastApp (handFastInv L.a) t)) == s

def handFastComp (p q : Nat) : Nat :=
  ![![0, 1, 2, 3, 4, 5], ![1, 0, 4, 5, 2, 3],
    ![2, 3, 0, 1, 5, 4], ![3, 2, 5, 4, 0, 1],
    ![4, 5, 1, 0, 3, 2], ![5, 4, 3, 2, 1, 0]]
    (Fin.ofNat 6 p) (Fin.ofNat 6 q)

def handFastGauge (out row inp : Nat) (T : HandFastOp) : HandFastOp :=
  let cell (s : Nat) := handFastComp (handFastInv out)
    (handFastComp (handFastRow T (handFastApp row s)) inp)
  ⟨cell 0, cell 1, cell 2⟩

def handFastCodes : List Nat := List.range 6

def handFastOps : List HandFastOp :=
  handFastCodes.flatMap fun a ↦ handFastCodes.flatMap fun b ↦
    handFastCodes.map fun c ↦ ⟨a, b, c⟩

def handFReps : List HandFastOp :=
  [⟨0, 0, 0⟩, ⟨0, 0, 1⟩, ⟨0, 0, 3⟩, ⟨0, 1, 1⟩, ⟨0, 1, 2⟩,
   ⟨0, 1, 3⟩, ⟨0, 3, 3⟩, ⟨0, 3, 4⟩, ⟨1, 1, 1⟩, ⟨1, 1, 2⟩,
   ⟨1, 1, 3⟩, ⟨1, 2, 3⟩, ⟨1, 2, 5⟩, ⟨1, 3, 3⟩, ⟨1, 3, 4⟩,
   ⟨3, 3, 3⟩, ⟨3, 3, 4⟩]

def handFNormCheck : Bool :=
  handFastOps.all fun F ↦ handFastCodes.any fun b ↦ handFastCodes.any fun v ↦
    handFReps.any fun R ↦ handFastGauge b v b F == R

/-- Every first operation is put in a gauge representative before any collision check. -/
theorem hand_f_norm_check_true : handFNormCheck = true := by
  rfl

structure HandCollisionRep where
  F : HandFastOp
  K : HandFastOp
  I : HandFastOp
deriving DecidableEq, Inhabited

def handCollisionReps : List HandCollisionRep :=
  [⟨⟨0, 3, 4⟩, ⟨0, 0, 0⟩, ⟨0, 3, 4⟩⟩,
   ⟨⟨0, 3, 4⟩, ⟨0, 3, 4⟩, ⟨1, 1, 1⟩⟩,
   ⟨⟨1, 2, 5⟩, ⟨0, 3, 4⟩, ⟨1, 5, 2⟩⟩,
   ⟨⟨1, 2, 5⟩, ⟨0, 4, 3⟩, ⟨0, 0, 0⟩⟩,
   ⟨⟨1, 3, 4⟩, ⟨0, 0, 0⟩, ⟨0, 3, 4⟩⟩]

def handKNormCheck (R : HandFastOp) : Bool :=
  handFastOps.all fun K ↦
    match handFastNext R K R with
    | none => true
    | some I => handFastCodes.any fun c ↦ handCollisionReps.any fun T ↦
      (T.F == R) && (handFastGauge 0 0 c K == T.K) &&
        (handFastGauge c 0 0 I == T.I)

theorem hand_k_norm_000 : handKNormCheck ⟨0, 0, 0⟩ = true := by rfl
theorem hand_k_norm_001 : handKNormCheck ⟨0, 0, 1⟩ = true := by rfl
theorem hand_k_norm_003 : handKNormCheck ⟨0, 0, 3⟩ = true := by rfl
theorem hand_k_norm_011 : handKNormCheck ⟨0, 1, 1⟩ = true := by rfl
theorem hand_k_norm_012 : handKNormCheck ⟨0, 1, 2⟩ = true := by rfl
theorem hand_k_norm_013 : handKNormCheck ⟨0, 1, 3⟩ = true := by rfl
theorem hand_k_norm_033 : handKNormCheck ⟨0, 3, 3⟩ = true := by rfl
theorem hand_k_norm_034 : handKNormCheck ⟨0, 3, 4⟩ = true := by rfl
theorem hand_k_norm_111 : handKNormCheck ⟨1, 1, 1⟩ = true := by rfl
theorem hand_k_norm_112 : handKNormCheck ⟨1, 1, 2⟩ = true := by rfl
theorem hand_k_norm_113 : handKNormCheck ⟨1, 1, 3⟩ = true := by rfl
theorem hand_k_norm_123 : handKNormCheck ⟨1, 2, 3⟩ = true := by rfl
theorem hand_k_norm_125 : handKNormCheck ⟨1, 2, 5⟩ = true := by rfl
theorem hand_k_norm_133 : handKNormCheck ⟨1, 3, 3⟩ = true := by rfl
theorem hand_k_norm_134 : handKNormCheck ⟨1, 3, 4⟩ = true := by rfl
theorem hand_k_norm_333 : handKNormCheck ⟨3, 3, 3⟩ = true := by rfl
theorem hand_k_norm_334 : handKNormCheck ⟨3, 3, 4⟩ = true := by rfl

def handRepBridgeCheck (T : HandCollisionRep) : Bool :=
  handFastOps.all fun J ↦
    match handFastNext T.I J T.K with
    | none => true
    | some L =>
      match handFastNext T.K T.I L with
      | none => true
      | some E => handBridgeConclusion T.F L E

/-- Representative 0 (`034,000,034`), checked over the 216 choices of `J`. -/
theorem hand_rep0_check_true : handRepBridgeCheck (handCollisionReps[0]!) = true := by rfl
/-- Representative 1 (`034,034,111`), checked over the 216 choices of `J`. -/
theorem hand_rep1_check_true : handRepBridgeCheck (handCollisionReps[1]!) = true := by rfl
/-- Representative 2 (`125,034,152`), checked over the 216 choices of `J`. -/
theorem hand_rep2_check_true : handRepBridgeCheck (handCollisionReps[2]!) = true := by rfl
/-- Representative 3 (`125,043,000`), checked over the 216 choices of `J`. -/
theorem hand_rep3_check_true : handRepBridgeCheck (handCollisionReps[3]!) = true := by rfl
/-- Representative 4 (`134,000,034`), checked over the 216 choices of `J`. -/
theorem hand_rep4_check_true : handRepBridgeCheck (handCollisionReps[4]!) = true := by rfl

def handPack (P : HandCodeOp) : HandFastOp := ⟨P 0, P 1, P 2⟩

def handComp (p q : HandPermCode) : HandPermCode :=
  ⟨handFastComp p q, by
    fin_cases p <;> fin_cases q <;> decide⟩

def handInvCode (p : HandPermCode) : HandPermCode :=
  ![0, 1, 2, 4, 3, 5] p

lemma handComp_app (p q : HandPermCode) (x : Fin3) :
    handPermApp (handComp p q) x = handPermApp p (handPermApp q x) := by
  fin_cases p <;> fin_cases q <;> fin_cases x <;> rfl

lemma handInvCode_app (p : HandPermCode) (x : Fin3) :
    handPermApp (handInvCode p) x = handPermInvApp p x := by
  fin_cases p <;> fin_cases x <;> rfl

@[simp] lemma handInvCode_val (p : HandPermCode) :
    (handInvCode p).val = handFastInv p.val := by
  fin_cases p <;> rfl

@[simp] lemma handPermApp_val (p : HandPermCode) (x : Fin3) :
    (handPermApp p x).val = handFastApp p.val x.val := by
  fin_cases p <;> fin_cases x <;> rfl

@[simp] lemma handInvCode_zero : handInvCode 0 = 0 := rfl

@[simp] lemma handPermApp_zero (x : Fin3) : handPermApp 0 x = x := by
  fin_cases x <;> rfl

lemma handComp_assoc (p q r : HandPermCode) :
    handComp (handComp p q) r = handComp p (handComp q r) := by
  fin_cases p <;> fin_cases q <;> fin_cases r <;> rfl

lemma handComp_zero_left (p : HandPermCode) : handComp 0 p = p := by
  fin_cases p <;> rfl

lemma handComp_zero_right (p : HandPermCode) : handComp p 0 = p := by
  fin_cases p <;> rfl

lemma handComp_inv_left (p : HandPermCode) : handComp (handInvCode p) p = 0 := by
  fin_cases p <;> rfl

lemma handComp_inv_right (p : HandPermCode) : handComp p (handInvCode p) = 0 := by
  fin_cases p <;> rfl

lemma handInvCode_comp (p q : HandPermCode) :
    handInvCode (handComp p q) = handComp (handInvCode q) (handInvCode p) := by
  fin_cases p <;> fin_cases q <;> rfl

lemma handComp_right_cancel (r p q : HandPermCode) (h : handComp p r = handComp q r) :
    p = q := by
  calc
    p = handComp p 0 := (handComp_zero_right p).symm
    _ = handComp p (handComp r (handInvCode r)) := by rw [handComp_inv_right]
    _ = handComp (handComp p r) (handInvCode r) := (handComp_assoc _ _ _).symm
    _ = handComp (handComp q r) (handInvCode r) := by rw [h]
    _ = handComp q (handComp r (handInvCode r)) := handComp_assoc _ _ _
    _ = handComp q 0 := by rw [handComp_inv_right]
    _ = q := handComp_zero_right q

def handGauge (out row inp : HandPermCode) (T : HandCodeOp) : HandCodeOp :=
  fun s ↦ handComp (handInvCode out)
    (handComp (T (handPermApp row s)) inp)

lemma handGauge_app (out row inp : HandPermCode) (T : HandCodeOp) (s x : Fin3) :
    handPermApp (handGauge out row inp T s) x =
      handPermInvApp out (handPermApp (T (handPermApp row s)) (handPermApp inp x)) := by
  simp [handGauge, handComp_app, handInvCode_app]

lemma handGauge_inv_app (out row inp : HandPermCode) (T : HandCodeOp) (s x : Fin3) :
    handPermInvApp (handGauge out row inp T s) x =
      handPermInvApp inp (handPermInvApp (T (handPermApp row s)) (handPermApp out x)) := by
  apply handPermApp_injective (handGauge out row inp T s)
  simp [handGauge_app, handPerm_app_inv, handPerm_inv_app]

lemma handGauge_id (T : HandCodeOp) : handGauge 0 0 0 T = T := by
  funext s
  unfold handGauge
  simp [handComp_zero_left, handComp_zero_right]

lemma handPack_gauge (out row inp : HandPermCode) (T : HandCodeOp) :
    handPack (handGauge out row inp T) = handFastGauge out row inp (handPack T) := by
  have h0 : handFastRow (handPack T) (handFastApp row.val 0) =
      (T (handPermApp row 0)).val := by fin_cases row <;> rfl
  have h1 : handFastRow (handPack T) (handFastApp row.val 1) =
      (T (handPermApp row 1)).val := by fin_cases row <;> rfl
  have h2 : handFastRow (handPack T) (handFastApp row.val 2) =
      (T (handPermApp row 2)).val := by fin_cases row <;> rfl
  ext
  · change (handGauge out row inp T 0).val =
      handFastComp (handFastInv out.val)
        (handFastComp (handFastRow (handPack T) (handFastApp row.val 0)) inp.val)
    simp [handGauge, handComp, h0]
  · change (handGauge out row inp T 1).val =
      handFastComp (handFastInv out.val)
        (handFastComp (handFastRow (handPack T) (handFastApp row.val 1)) inp.val)
    simp [handGauge, handComp, h1]
  · change (handGauge out row inp T 2).val =
      handFastComp (handFastInv out.val)
        (handFastComp (handFastRow (handPack T) (handFastApp row.val 2)) inp.val)
    simp [handGauge, handComp, h2]

lemma handCodeChain_gauge {P Q R Z : HandCodeOp} (h : HandCodeChain P Q R Z)
    (alpha delta beta gamma eta : HandPermCode) :
    HandCodeChain (handGauge alpha delta beta P) (handGauge beta alpha gamma Q)
      (handGauge eta delta alpha R) (handGauge gamma eta delta Z) := by
  intro s t
  have hc := congrArg (handPermInvApp alpha)
    (h (handPermApp alpha s) (handPermApp delta t))
  simpa [handGauge_app, handPerm_app_inv, handPerm_inv_app] using hc

lemma handFastApp_code (p : HandPermCode) (x : Fin3) :
    handFastApp p x = handPermApp p x := by
  fin_cases p <;> fin_cases x <;> rfl

lemma handFastInv_code (p : HandPermCode) (x : Fin3) :
    handFastApp (handFastInv p) x = handPermInvApp p x := by
  fin_cases p <;> fin_cases x <;> rfl

lemma handFastRow_pack (P : HandCodeOp) (s : Fin3) :
    handFastRow (handPack P) s = P s := by
  fin_cases s <;> rfl

lemma handFast_next_formula {P Q R Z : HandCodeOp} (h : HandCodeChain P Q R Z)
    (r t : Fin3) :
    handFastNextVal (handPack P) (handPack Q) (handPack R) r t =
      (handPermApp (Z r) t).val := by
  let s := handPermInvApp (R t) r
  have hc := h s t
  have hz := congrArg
    (fun x ↦ handPermInvApp (Q s) (handPermInvApp (P t) x)) hc
  have hz' : handPermApp (Z r) t =
      handPermInvApp (Q s) (handPermInvApp (P t) s) := by
    simpa [s, handPerm_inv_app, handPerm_app_inv] using hz
  have hsval : handFastApp (handFastInv (R t).val) r.val = s.val := by
    simpa [s] using handFastInv_code (R t) r
  have hpval : handFastApp (handFastInv (P t).val) s.val =
      (handPermInvApp (P t) s).val := by
    simpa using handFastInv_code (P t) s
  have hqval : handFastApp (handFastInv (Q s).val)
      (handPermInvApp (P t) s).val =
      (handPermInvApp (Q s) (handPermInvApp (P t) s)).val := by
    simpa using handFastInv_code (Q s) (handPermInvApp (P t) s)
  calc
    handFastNextVal (handPack P) (handPack Q) (handPack R) r t =
        handFastApp (handFastInv (Q s).val)
          (handFastApp (handFastInv (P t).val) s.val) := by
            unfold handFastNextVal
            rw [handFastRow_pack R t, hsval]
            change handFastApp (handFastInv (handFastRow (handPack Q) s.val))
              (handFastApp (handFastInv (handFastRow (handPack P) t.val)) s.val) = _
            rw [handFastRow_pack Q s, handFastRow_pack P t]
    _ = (handPermInvApp (Q s) (handPermInvApp (P t) s)).val := by rw [hpval, hqval]
    _ = (handPermApp (Z r) t).val := congrArg Fin.val hz'.symm

lemma handFastRowCode_self (p : HandPermCode) :
    handFastRowCode? (handPermApp p 0) (handPermApp p 1) (handPermApp p 2) = some p := by
  fin_cases p <;> rfl

lemma handFastNext_complete {P Q R Z : HandCodeOp} (h : HandCodeChain P Q R Z) :
    handFastNext (handPack P) (handPack Q) (handPack R) = some (handPack Z) := by
  have hrow (r : Fin3) :
      handFastRowCode? (handFastNextVal (handPack P) (handPack Q) (handPack R) r 0)
          (handFastNextVal (handPack P) (handPack Q) (handPack R) r 1)
          (handFastNextVal (handPack P) (handPack Q) (handPack R) r 2) = some (Z r).val := by
    have h0 := handFast_next_formula h r (0 : Fin3)
    have h1 := handFast_next_formula h r (1 : Fin3)
    have h2 := handFast_next_formula h r (2 : Fin3)
    simpa using h0 ▸ h1 ▸ h2 ▸ handFastRowCode_self (Z r)
  unfold handFastNext
  have h0 : handFastRowCode? (handFastNextVal (handPack P) (handPack Q) (handPack R) 0 0)
      (handFastNextVal (handPack P) (handPack Q) (handPack R) 0 1)
      (handFastNextVal (handPack P) (handPack Q) (handPack R) 0 2) = some (Z 0).val := by
    simpa using hrow (0 : Fin3)
  have h1 : handFastRowCode? (handFastNextVal (handPack P) (handPack Q) (handPack R) 1 0)
      (handFastNextVal (handPack P) (handPack Q) (handPack R) 1 1)
      (handFastNextVal (handPack P) (handPack Q) (handPack R) 1 2) = some (Z 1).val := by
    simpa using hrow (1 : Fin3)
  have h2 : handFastRowCode? (handFastNextVal (handPack P) (handPack Q) (handPack R) 2 0)
      (handFastNextVal (handPack P) (handPack Q) (handPack R) 2 1)
      (handFastNextVal (handPack P) (handPack Q) (handPack R) 2 2) = some (Z 2).val := by
    simpa using hrow (2 : Fin3)
  rw [h0, h1, h2]
  congr

lemma handAllNat_spec (n : Nat) (f : Nat → Bool) :
    handAllNat n f = true ↔ ∀ i < n, f i = true := by
  induction n with
  | zero => simp [handAllNat]
  | succ n ih =>
      rw [handAllNat, Bool.and_eq_true, ih]
      constructor
      · rintro ⟨hn, h⟩ i hi
        by_cases hin : i = n
        · simpa [hin] using hn
        · exact h i (by omega)
      · intro h
        exact ⟨h n (by omega), fun i hi ↦ h i (by omega)⟩

lemma handAllFastOps_spec (f : HandFastOp → Bool) (h : handAllFastOps f = true)
    (P : HandFastOp) (ha : P.a < 6) (hb : P.b < 6) (hc : P.c < 6) : f P = true := by
  unfold handAllFastOps at h
  have ha' := (handAllNat_spec 6 _).mp h P.a ha
  have hb' := (handAllNat_spec 6 _).mp ha' P.b hb
  exact (handAllNat_spec 6 _).mp hb' P.c hc

lemma handBridgeConclusion_sound (F L E : HandCodeOp)
    (h : handBridgeConclusion (handPack F) (handPack L) (handPack E) = true) :
    (∀ s, L s = L 0) ∧
      ∀ s t, handPermApp (E t)
        (handPermApp (F s) (handPermInvApp (L 0) t)) = s := by
  unfold handBridgeConclusion at h
  rcases Bool.and_eq_true_iff.mp h with ⟨hpairs, hrel⟩
  rcases Bool.and_eq_true_iff.mp hpairs with ⟨h01, h02⟩
  simp only [beq_iff_eq] at h01 h02
  constructor
  · intro s
    apply Fin.ext
    fin_cases s
    · rfl
    · exact h01.symm
    · exact h02.symm
  · intro s t
    have hs := (handAllNat_spec 3 _).mp hrel s.val s.isLt
    have hst := (handAllNat_spec 3 _).mp hs t.val t.isLt
    simp only [beq_iff_eq] at hst
    have hinv : handFastApp (handFastInv (handPack L).a) t.val =
        (handPermInvApp (L 0) t).val := by
      simpa [handPack] using handFastInv_code (L 0) t
    have hFapp : handFastApp (F s).val (handPermInvApp (L 0) t).val =
        (handPermApp (F s) (handPermInvApp (L 0) t)).val := by
      simpa using handFastApp_code (F s) (handPermInvApp (L 0) t)
    have hEapp :
        handFastApp (E t).val (handPermApp (F s) (handPermInvApp (L 0) t)).val =
          (handPermApp (E t) (handPermApp (F s) (handPermInvApp (L 0) t))).val := by
      simpa using handFastApp_code (E t) (handPermApp (F s) (handPermInvApp (L 0) t))
    rw [handFastRow_pack, handFastRow_pack, hinv, hFapp, hEapp] at hst
    apply Fin.ext
    exact hst

lemma handPack_mem_fastOps (P : HandCodeOp) : handPack P ∈ handFastOps := by
  simp only [handFastOps, handFastCodes, List.mem_flatMap, List.mem_map,
    List.mem_range]
  refine ⟨(P 0).val, (P 0).isLt, (P 1).val, (P 1).isLt,
    (P 2).val, (P 2).isLt, ?_⟩
  rfl

/-- Gauge normalization of the first operation only; this checker has 216 inputs. -/
theorem hand_f_normalize (F : HandCodeOp) :
    ∃ b v : HandPermCode, ∃ R ∈ handFReps,
      handPack (handGauge b v b F) = R := by
  have hF := (List.all_eq_true.mp hand_f_norm_check_true)
    (handPack F) (handPack_mem_fastOps F)
  rcases List.any_eq_true.mp hF with ⟨bn, hbn, hb⟩
  rcases List.any_eq_true.mp hb with ⟨vn, hvn, hv⟩
  rcases List.any_eq_true.mp hv with ⟨R, hR, hEq⟩
  have hbn6 : bn < 6 := by simpa [handFastCodes] using hbn
  have hvn6 : vn < 6 := by simpa [handFastCodes] using hvn
  let b : HandPermCode := ⟨bn, hbn6⟩
  let v : HandPermCode := ⟨vn, hvn6⟩
  have hEq' : handFastGauge bn vn bn (handPack F) = R := by
    simpa using hEq
  refine ⟨b, v, R, hR, ?_⟩
  rw [handPack_gauge]
  simpa [b, v] using hEq'

lemma hand_k_norm_check_of_mem {R : HandFastOp} (hR : R ∈ handFReps) :
    handKNormCheck R = true := by
  simp [handFReps] at hR
  rcases hR with hR | hR | hR | hR | hR | hR | hR | hR | hR |
      hR | hR | hR | hR | hR | hR | hR | hR <;> subst R
  · exact hand_k_norm_000
  · exact hand_k_norm_001
  · exact hand_k_norm_003
  · exact hand_k_norm_011
  · exact hand_k_norm_012
  · exact hand_k_norm_013
  · exact hand_k_norm_033
  · exact hand_k_norm_034
  · exact hand_k_norm_111
  · exact hand_k_norm_112
  · exact hand_k_norm_113
  · exact hand_k_norm_123
  · exact hand_k_norm_125
  · exact hand_k_norm_133
  · exact hand_k_norm_134
  · exact hand_k_norm_333
  · exact hand_k_norm_334

/-- Once `F` is normalized, the collision is one of the five representatives. -/
theorem hand_k_normalize {F K I : HandCodeOp} {R : HandFastOp}
    (hR : R ∈ handFReps) (hFR : handPack F = R)
    (h : HandCodeChain F K F I) :
    ∃ c : HandPermCode, ∃ T ∈ handCollisionReps,
      T.F = R ∧ handPack (handGauge 0 0 c K) = T.K ∧
        handPack (handGauge c 0 0 I) = T.I := by
  have hK := (List.all_eq_true.mp (hand_k_norm_check_of_mem hR))
    (handPack K) (handPack_mem_fastOps K)
  have hn := handFastNext_complete h
  have hn' : handFastNext R (handPack K) R = some (handPack I) := by
    simpa [hFR] using hn
  rw [hn'] at hK
  rcases List.any_eq_true.mp hK with ⟨cn, hcn, hc⟩
  rcases List.any_eq_true.mp hc with ⟨T, hT, hEq⟩
  have hcn6 : cn < 6 := by simpa [handFastCodes] using hcn
  let c : HandPermCode := ⟨cn, hcn6⟩
  rcases Bool.and_eq_true_iff.mp hEq with ⟨hpair, hIcB⟩
  rcases Bool.and_eq_true_iff.mp hpair with ⟨hTFB, hKcB⟩
  have hTF : T.F = R := by simpa using hTFB
  have hKc : handFastGauge 0 0 cn (handPack K) = T.K := by simpa using hKcB
  have hIc : handFastGauge cn 0 0 (handPack I) = T.I := by simpa using hIcB
  refine ⟨c, T, hT, hTF, ?_, ?_⟩
  · rw [handPack_gauge]
    simpa [c] using hKc
  · rw [handPack_gauge]
    simpa [c] using hIc

lemma hand_rep_check_of_mem {T : HandCollisionRep} (hT : T ∈ handCollisionReps) :
    handRepBridgeCheck T = true := by
  simp [handCollisionReps] at hT
  rcases hT with hT | hT | hT | hT | hT <;> subst T
  · exact hand_rep0_check_true
  · exact hand_rep1_check_true
  · exact hand_rep2_check_true
  · exact hand_rep3_check_true
  · exact hand_rep4_check_true

/-- Soundness of a single normalized representative worksheet. -/
theorem hand_rep_bridge_sound {F K I J L E : HandCodeOp} {T : HandCollisionRep}
    (hT : T ∈ handCollisionReps)
    (hF : handPack F = T.F) (hK : handPack K = T.K) (hI : handPack I = T.I)
    (h2 : HandCodeChain I J K L) (h3 : HandCodeChain K I L E) :
    (∀ s, L s = L 0) ∧
      ∀ s t, handPermApp (E t)
        (handPermApp (F s) (handPermInvApp (L 0) t)) = s := by
  have hJ := (List.all_eq_true.mp (hand_rep_check_of_mem hT))
    (handPack J) (handPack_mem_fastOps J)
  have hn2 := handFastNext_complete h2
  have hn2' : handFastNext T.I (handPack J) T.K = some (handPack L) := by
    simpa [hI, hK] using hn2
  rw [hn2'] at hJ
  have hn3 := handFastNext_complete h3
  have hn3' : handFastNext T.K T.I (handPack L) = some (handPack E) := by
    simpa [hK, hI] using hn3
  change (match handFastNext T.K T.I (handPack L) with
    | none => true
    | some E => handBridgeConclusion T.F (handPack L) E) = true at hJ
  rw [hn3'] at hJ
  have hc : handBridgeConclusion (handPack F) (handPack L) (handPack E) = true := by
    simpa [hF] using hJ
  exact handBridgeConclusion_sound F L E hc

lemma hand_bridge_conclusion_ungauge (b v : HandPermCode) (F L E : HandCodeOp)
    (h : (∀ s, handGauge 0 b b L s = handGauge 0 b b L 0) ∧
      ∀ s t, handPermApp (handGauge v 0 b E t)
        (handPermApp (handGauge b v b F s)
          (handPermInvApp (handGauge 0 b b L 0) t)) = s) :
    (∀ s, L s = L 0) ∧
      ∀ s t, handPermApp (E t)
        (handPermApp (F s) (handPermInvApp (L 0) t)) = s := by
  have hrow (s : Fin3) : L (handPermApp b s) = L (handPermApp b 0) := by
    apply handComp_right_cancel b
    simpa [handGauge, handComp_zero_left] using h.1 s
  have hL (r : Fin3) : L r = L 0 := by
    have hr := hrow (handPermInvApp b r)
    have h0 := hrow (handPermInvApp b 0)
    simpa [handPerm_app_inv] using hr.trans h0.symm
  refine ⟨hL, ?_⟩
  intro s t
  let sv := handPermInvApp v s
  have hc := congrArg (handPermApp v) (h.2 sv t)
  simpa [sv, handGauge_app, handGauge_inv_app, hL,
    handPerm_app_inv, handPerm_inv_app] using hc

/-- Gauge-normalized finite bridge: only the five representatives are enumerated. -/
theorem hand_code_bridge_three_gauge (F K I J L E : HandCodeOp)
    (h1 : HandCodeChain F K F I) (h2 : HandCodeChain I J K L)
    (h3 : HandCodeChain K I L E) :
    (∀ s, L s = L 0) ∧
      ∀ s t, handPermApp (E t)
        (handPermApp (F s) (handPermInvApp (L 0) t)) = s := by
  rcases hand_f_normalize F with ⟨b, v, R, hR, hFR⟩
  let F0 := handGauge b v b F
  let K0 := handGauge b b 0 K
  let I0 := handGauge 0 b v I
  let J0 := handGauge v 0 0 J
  let L0 := handGauge 0 b b L
  let E0 := handGauge v 0 b E
  have hc1 : HandCodeChain F0 K0 F0 I0 := by
    simpa [F0, K0, I0] using handCodeChain_gauge h1 b v b 0 b
  have hc2 : HandCodeChain I0 J0 K0 L0 := by
    simpa [I0, J0, K0, L0] using handCodeChain_gauge h2 0 b v 0 b
  have hc3 : HandCodeChain K0 I0 L0 E0 := by
    simpa [K0, I0, L0, E0] using handCodeChain_gauge h3 b b 0 v 0
  have hFR0 : handPack F0 = R := by simpa [F0] using hFR
  rcases hand_k_normalize hR hFR0 hc1 with ⟨c, T, hT, hTF, hKc, hIc⟩
  let K1 := handGauge 0 0 c K0
  let I1 := handGauge c 0 0 I0
  let J1 := handGauge 0 c 0 J0
  have hc2' : HandCodeChain I1 J1 K1 L0 := by
    simpa [I1, J1, K1, handGauge_id] using
      handCodeChain_gauge hc2 c 0 0 0 0
  have hc3' : HandCodeChain K1 I1 L0 E0 := by
    simpa [I1, K1, handGauge_id] using
      handCodeChain_gauge hc3 0 0 c 0 0
  have hFrep : handPack F0 = T.F := hFR0.trans hTF.symm
  have hKrep : handPack K1 = T.K := by simpa [K1] using hKc
  have hIrep : handPack I1 = T.I := by simpa [I1] using hIc
  have hrep := hand_rep_bridge_sound hT hFrep hKrep hIrep hc2' hc3'
  exact hand_bridge_conclusion_ungauge b v F L E (by simpa [F0, L0, E0] using hrep)

def handPermCode (e : Equiv.Perm Fin3) : HandPermCode :=
  if e 0 = 0 then if e 1 = 1 then 0 else 1
  else if e 0 = 1 then if e 1 = 0 then 2 else 3
  else if e 1 = 0 then 4 else 5

lemma handPermCode_app (e : Equiv.Perm Fin3) (x : Fin3) :
    handPermApp (handPermCode e) x = e x := by
  have hn01 : e 0 ≠ e 1 := by
    intro h
    have := e.injective h
    have hv := congrArg Fin.val this
    norm_num at hv
  have hn02 : e 0 ≠ e 2 := by
    intro h
    have := e.injective h
    have hv := congrArg Fin.val this
    norm_num at hv
  have hn12 : e 1 ≠ e 2 := by
    intro h
    have := e.injective h
    have hv := congrArg Fin.val this
    norm_num at hv
  generalize h0 : e 0 = y0
  generalize h1 : e 1 = y1
  generalize h2 : e 2 = y2
  fin_cases y0 <;> fin_cases y1 <;> fin_cases y2 <;> fin_cases x <;>
    simp_all [handPermCode, handPermApp, handPermNatApp]
  all_goals (apply Fin.ext; rfl)

lemma handPermCode_inv_app (e : Equiv.Perm Fin3) (x : Fin3) :
    handPermInvApp (handPermCode e) x = e.symm x := by
  apply e.injective
  calc
    e (handPermInvApp (handPermCode e) x) =
        handPermApp (handPermCode e) (handPermInvApp (handPermCode e) x) := by
          symm
          exact handPermCode_app e _
    _ = x := handPerm_app_inv _ _
    _ = e (e.symm x) := (e.apply_symm_apply x).symm

def handCodeOp (T : Fin3 → Equiv.Perm Fin3) : HandCodeOp :=
  fun s ↦ handPermCode (T s)

lemma handCodeChain_of_handChain {P Q R Z : Fin3 → Equiv.Perm Fin3}
    (h : HandChain P Q R Z) :
    HandCodeChain (handCodeOp P) (handCodeOp Q) (handCodeOp R) (handCodeOp Z) := by
  intro s t
  simpa [HandCodeChain, handCodeOp, handPermCode_app] using h s t

/-- The bridge lemma of the hand proof. -/
theorem hand_bridge (F K I J L E G H : Fin3 → Equiv.Perm Fin3)
    (h1 : HandChain F K F I) (h2 : HandChain I J K L)
    (h3 : HandChain K I L E) (h4 : HandChain E F G H) :
    ∃ ℓ : Equiv.Perm Fin3, (∀ s, L s = ℓ) ∧ (∀ s, H s = ℓ.symm) := by
  rcases hand_code_bridge_three_gauge (handCodeOp F) (handCodeOp K) (handCodeOp I)
      (handCodeOp J) (handCodeOp L) (handCodeOp E)
      (handCodeChain_of_handChain h1) (handCodeChain_of_handChain h2)
      (handCodeChain_of_handChain h3) with ⟨hLcode, hEFcode⟩
  let ℓ := L 0
  have hL : ∀ s, L s = ℓ := by
    intro s
    apply Equiv.ext
    intro x
    calc
      L s x = handPermApp (handCodeOp L s) x := (handPermCode_app (L s) x).symm
      _ = handPermApp (handCodeOp L 0) x := by rw [hLcode s]
      _ = ℓ x := handPermCode_app (L 0) x
  have hEF : ∀ s t, E t (F s (ℓ.symm t)) = s := by
    intro s t
    have hc := hEFcode s t
    simpa [handCodeOp, handPermCode_app, handPermCode_inv_app, ℓ] using hc
  have hH : ∀ r, H r = ℓ.symm := by
    intro r
    apply Equiv.ext
    intro t
    let s := (G t).symm r
    have hg : G t s = r := by simp [s]
    have hc := h4 s t
    rw [hg] at hc
    have he := hEF s t
    apply (F s).injective
    apply (E t).injective
    exact hc.trans he.symm
  exact ⟨ℓ, hL, hH⟩

/-! ## The seven-chain contradiction -/

theorem core7_chains_no_solution : ¬ ∃ σ : Core7Pair → Fin3 → Equiv.Perm Fin3,
    core7Chains σ := by
  rintro ⟨σ, hσ⟩
  let A := σ 0
  let B := σ 11
  let C := σ 2
  let D := σ 12
  let M := σ 4
  let N := σ 3
  let E := σ 9
  let F := σ 13
  let G := σ 10
  let H := σ 1
  let I := σ 7
  let J := σ 8
  let K := σ 6
  let L := σ 5
  have h1 : HandChain A B C D := fun s t ↦ (hσ s t).1.symm
  have h2 : HandChain E F G H := fun s t ↦ (hσ s t).2.1.symm
  have h3 : HandChain I J K L := fun s t ↦ (hσ s t).2.2.1.symm
  have h4 : HandChain D M D N := fun s t ↦ (hσ s t).2.2.2.1.symm
  have h5 : HandChain F K F I := fun s t ↦ (hσ s t).2.2.2.2.1.symm
  have h6 : HandChain H L A B := fun s t ↦ (hσ s t).2.2.2.2.2.1.symm
  have h7 : HandChain K I L E := fun s t ↦ (hσ s t).2.2.2.2.2.2.symm
  rcases hand_bridge F K I J L E G H h5 h3 h7 h2 with ⟨ℓ, hL, hH⟩
  have hBA (s t : Fin3) : B (A t s) t = s := by
    have hc := h6 s t
    rw [hH t, hL s] at hc
    simpa using hc
  have hBs (s t : Fin3) : B s t = (A t).symm s := by
    have hc := hBA ((A t).symm s) t
    simpa using hc
  have hDcover (s t : Fin3) : D (C t s) t = t := by
    apply (B s).injective
    apply (A t).injective
    calc
      A t (B s (D (C t s) t)) = s := h1 s t
      _ = A t (B s t) := by rw [hBs]; simp
  have hD (r t : Fin3) : D r t = t := by
    simpa using hDcover ((C t).symm r) t
  have hMN (s t : Fin3) : M s (N s t) = s := by
    simpa only [hD] using h4 s t
  have heqN : N 0 0 = N 0 1 := by
    apply (M 0).injective
    rw [hMN 0 0, hMN 0 1]
  have heq : (0 : Fin3) = 1 := (N 0).injective heqN
  norm_num at heq

/-! ## Reuse of the clean semantic transport -/

/-- FIBRE-3 EXCLUSION, now ending in the hand proof rather than the BV certificate. -/
theorem fibre3_exclusion_clean
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
  let c3 : B → B → Fin3 → Fin3 → Fin3 := fun x y s t ↦
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
  exact core7_chains_no_solution
    ⟨core7SigmaOfLaw opB hB a c3 hinj3,
      core7_pattern_chains opB hB h255 a c3 hinj3 hEq43⟩

theorem fibre_two_or_three_exclusion_clean
    {M : Type u} {B : Type v} [Finite M] [Finite B]
    (opM : M → M → M) (opB : B → B → B)
    (hM : E677 opM) (hB : E677 opB) (h255 : E255 opB)
    (φ : M → B) (hφ : Function.Surjective φ)
    (hhom : IsMagmaHom opM opB φ) (a : B)
    (ha : Nat.card {m : M // φ m = a} = 2 ∨ Nat.card {m : M // φ m = a} = 3) : False :=
  ha.elim (fibre2_exclusion opM opB hM hB h255 φ hφ hhom a)
    (fibre3_exclusion_clean opM opB hM hB h255 φ hφ hhom a)

#print axioms core7_chains_no_solution
#print axioms fibre3_exclusion_clean
#print axioms fibre_two_or_three_exclusion_clean

end Ext677
