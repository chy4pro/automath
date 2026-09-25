import Mathlib

/-!
# The shape-only Core-7 obstruction over a three-element fibre
-/

namespace Ext677

open Function

/-- A fibre row is a permutation of the three fibre symbols. -/
abbrev Core7Row := Equiv.Perm (Fin 3)

/-- A permutation-row fibre operation. -/
abbrev Core7Op := Fin 3 → Core7Row

/-- One equation-(4) fibre instance:
`P_t(Q_s(S_{R_t(s)}(t))) = s`. -/
def Core7E (P Q R S : Core7Op) : Prop :=
  ∀ s t, P t (Q s (S (R t s) t)) = s

/-- Raw-function version of `Core7E`, used in the final self-contained statement. -/
def Core7ERaw (P Q R S : Fin 3 → Fin 3 → Fin 3) : Prop :=
  ∀ s t, P t (Q s (S (R t s) t)) = s

/-- Every row of a raw fibre operation is bijective. -/
def Core7RowsBijective (T : Fin 3 → Fin 3 → Fin 3) : Prop :=
  ∀ s, Function.Bijective (T s)

/-- Collision elimination: in `E(X,Y,X,Z)`, every cell of `Z` is forced by
`X` and `Y`. -/
theorem core7_collision_forces (X Y Z : Core7Op) (h : Core7E X Y X Z)
    (s t : Fin 3) :
    Z (X t s) t = (Y s).symm ((X t).symm s) := by
  apply (Y s).injective
  apply (X t).injective
  simpa using h s t

/-- Executable universal quantification over `Fin n`; unlike a commutative
finset fold, `List.all` genuinely short-circuits. -/
def core7AllFin {n : Nat} (p : Fin n → Bool) : Bool :=
  (List.finRange n).all p

/-- Correctness of `core7AllFin`. -/
theorem core7AllFin_eq_true {n : Nat} (p : Fin n → Bool) :
    core7AllFin p = true ↔ ∀ x, p x = true := by
  simp [core7AllFin]

/-- Executable existential quantification over `Fin n`. -/
def core7AnyFin {n : Nat} (p : Fin n → Bool) : Bool :=
  (List.finRange n).any p

/-- Correctness of `core7AnyFin`. -/
theorem core7AnyFin_eq_true {n : Nat} (p : Fin n → Bool) :
    core7AnyFin p = true ↔ ∃ x, p x = true := by
  simp [core7AnyFin]

/-- An explicit enumeration of the six permutations of `Fin 3`. -/
def core7RowDecode : Fin 6 → Core7Row
  | 0 => Equiv.refl _
  | 1 => Equiv.swap 0 1
  | 2 => Equiv.swap 0 2
  | 3 => Equiv.swap 1 2
  | 4 => (Equiv.swap 0 1).trans (Equiv.swap 1 2)
  | 5 => (Equiv.swap 1 2).trans (Equiv.swap 0 1)

/-- The same six permutations as a proof-free executable lookup table. -/
def core7RowEval : Fin 6 → Fin 3 → Fin 3 := fun r x =>
  (![![0, 1, 2], ![1, 0, 2], ![2, 1, 0],
    ![0, 2, 1], ![2, 0, 1], ![1, 2, 0]] : Fin 6 → Fin 3 → Fin 3) r x

/-- The row digit selected by a base-six operation code. -/
def core7Digit (code : Fin 216) (s : Fin 3) : Fin 6 :=
  if s = 0 then ⟨code.val % 6, by omega⟩
  else if s = 1 then ⟨(code.val / 6) % 6, by omega⟩
  else ⟨(code.val / 36) % 6, by omega⟩

/-- Proof-free evaluation of an encoded operation. -/
def core7Eval (code : Fin 216) (s t : Fin 3) : Fin 3 :=
  core7RowEval (core7Digit code s) t

/-- Base-six decoding of a number below `6³` into three permutation rows. -/
def core7Decode (code : Fin 216) : Core7Op := fun s =>
  core7RowDecode (core7Digit code s)

/-- The executable table agrees with the permutation-valued decoder. -/
theorem core7Decode_apply (code : Fin 216) (s t : Fin 3) :
    core7Decode code s t = core7Eval code s t := by
  native_decide +revert

/-- The explicit base-six decoder has no duplicate operation codes. -/
theorem core7Decode_injective : Function.Injective core7Decode := by
  native_decide

/-- There are exactly `6³ = 216` permutation-row operations. -/
theorem core7Op_card : Fintype.card Core7Op = 216 := by
  native_decide

/-- Hence the explicit decoder enumerates every permutation-row operation. -/
theorem core7Decode_bijective : Function.Bijective core7Decode :=
  (Fintype.bijective_iff_injective_and_card core7Decode).2
    ⟨core7Decode_injective, by simpa using core7Op_card.symm⟩

/-- The inverse code of a permutation-row operation. -/
noncomputable def core7Encode : Core7Op → Fin 216 :=
  (Equiv.ofBijective core7Decode core7Decode_bijective).symm

@[simp]
theorem core7Decode_encode (T : Core7Op) : core7Decode (core7Encode T) = T :=
  (Equiv.ofBijective core7Decode core7Decode_bijective).apply_symm_apply T

/-- Executable form of one Core-7 equation. -/
def core7ECheck (P Q R S : Core7Op) : Bool :=
  core7AllFin fun s : Fin 3 =>
    core7AllFin fun t : Fin 3 =>
      decide (P t (Q s (S (R t s) t)) = s)

/-- Executable form of the bridge's coordinate-free cancellation conclusion. -/
def core7CancelCheck (H L : Core7Op) : Bool :=
  core7AllFin fun s : Fin 3 =>
    core7AllFin fun t : Fin 3 =>
      core7AllFin fun z : Fin 3 =>
        decide (H t (L s z) = z)

/-- Proof-free executable form of an equation on operation codes. -/
def core7ECode (p q r u : Fin 216) : Bool :=
  core7AllFin fun s : Fin 3 =>
    core7AllFin fun t : Fin 3 =>
      decide (core7Eval p t
        (core7Eval q s (core7Eval u (core7Eval r t s) t)) = s)

/-- Proof-free executable cancellation check on operation codes. -/
def core7CancelCode (h l : Fin 216) : Bool :=
  core7AllFin fun s : Fin 3 =>
    core7AllFin fun t : Fin 3 =>
      core7AllFin fun z : Fin 3 =>
        decide (core7Eval h t (core7Eval l s z) = z)

/-- The complete staged finite `S₃` bridge search. Each false antecedent stops
that branch before the remaining operations are enumerated. -/
def Core7BridgeCheck : Bool :=
  core7AllFin fun f : Fin 216 =>
    core7AllFin fun k : Fin 216 =>
      core7AllFin fun i : Fin 216 =>
        if core7ECode f k f i = true then
          core7AllFin fun l : Fin 216 =>
            if core7AnyFin (fun j : Fin 216 => core7ECode i j k l) = true then
              core7AllFin fun e : Fin 216 =>
                if core7ECode k i l e = true then
                  core7AllFin fun h : Fin 216 =>
                    if core7AnyFin (fun g : Fin 216 => core7ECode e f g h) = true then
                      core7CancelCode h l
                    else true
                else true
              else true
        else true

/-- Native evaluation of the finite bridge table. -/
theorem core7_bridge_check : Core7BridgeCheck = true := by
  native_decide

/-- Logical bridge for explicitly decoded operation codes. -/
theorem core7_bridge_decoded :
    ∀ f k i : Fin 216,
      Core7E (core7Decode f) (core7Decode k) (core7Decode f) (core7Decode i) →
    ∀ j l : Fin 216,
      Core7E (core7Decode i) (core7Decode j) (core7Decode k) (core7Decode l) →
    ∀ e : Fin 216,
      Core7E (core7Decode k) (core7Decode i) (core7Decode l) (core7Decode e) →
    ∀ g h : Fin 216,
      Core7E (core7Decode e) (core7Decode f) (core7Decode g) (core7Decode h) →
        ∀ s t z : Fin 3, core7Decode h t (core7Decode l s z) = z := by
  intro f k i hfkfi j l hijkl e hkile g h hefgh
  have hall := core7_bridge_check
  simp only [Core7BridgeCheck, core7AllFin_eq_true] at hall
  have hfkfi' := show core7ECode f k f i = true by
    simpa [core7ECode, core7AllFin_eq_true, Core7E, core7Decode_apply] using hfkfi
  have hijkl' := show core7ECode i j k l = true by
    simpa [core7ECode, core7AllFin_eq_true, Core7E, core7Decode_apply] using hijkl
  have hkile' := show core7ECode k i l e = true by
    simpa [core7ECode, core7AllFin_eq_true, Core7E, core7Decode_apply] using hkile
  have hefgh' := show core7ECode e f g h = true by
    simpa [core7ECode, core7AllFin_eq_true, Core7E, core7Decode_apply] using hefgh
  have hj : core7AnyFin (fun j : Fin 216 => core7ECode i j k l) = true :=
    (core7AnyFin_eq_true _).2 ⟨j, hijkl'⟩
  have hg : core7AnyFin (fun g : Fin 216 => core7ECode e f g h) = true :=
    (core7AnyFin_eq_true _).2 ⟨g, hefgh'⟩
  have h₁ := hall f k i
  simp only [hfkfi', ite_true, core7AllFin_eq_true] at h₁
  have h₂ := h₁ l
  simp only [hj, ite_true, core7AllFin_eq_true] at h₂
  have h₃ := h₂ e
  simp only [hkile', ite_true, core7AllFin_eq_true] at h₃
  have h₄ := h₃ h
  simp only [hg, ite_true] at h₄
  simpa [core7CancelCode, core7AllFin_eq_true, core7Decode_apply] using h₄

/-- Coordinate-free finite bridge fact. The staged implications are intentional:
they let the native decision procedure reject a collision triple before enumerating
the later operations. This is the finite `S₃` classification/bridge check. -/
theorem core7_bridge_finite :
    ∀ F K I : Core7Op, Core7E F K F I →
    ∀ J L : Core7Op, Core7E I J K L →
    ∀ E : Core7Op, Core7E K I L E →
    ∀ G H : Core7Op, Core7E E F G H →
      ∀ s t z : Fin 3, H t (L s z) = z := by
  intro F K I hFKFI J L hIJKL E hKILE G H hEFGH
  simpa only [core7Decode_encode] using
    core7_bridge_decoded (core7Encode F) (core7Encode K) (core7Encode I)
      (by simpa only [core7Decode_encode] using hFKFI)
      (core7Encode J) (core7Encode L)
      (by simpa only [core7Decode_encode] using hIJKL)
      (core7Encode E) (by simpa only [core7Decode_encode] using hKILE)
      (core7Encode G) (core7Encode H)
      (by simpa only [core7Decode_encode] using hEFGH)

/-- The symbolic cancellation endgame, conditional only on the finite bridge fact. -/
theorem core7_endgame
    (bridge :
      ∀ F K I : Core7Op, Core7E F K F I →
      ∀ J L : Core7Op, Core7E I J K L →
      ∀ E : Core7Op, Core7E K I L E →
      ∀ G H : Core7Op, Core7E E F G H →
        ∀ s t z : Fin 3, H t (L s z) = z) :
    ¬ ∃ A B C D E F G H I J K L M0 N : Core7Op,
      Core7E A B C D ∧ Core7E E F G H ∧ Core7E I J K L ∧
      Core7E D M0 D N ∧ Core7E F K F I ∧
      Core7E H L A B ∧ Core7E K I L E := by
  rintro ⟨A, B, C, D, E, F, G, H, I, J, K, L, M0, N,
    hABCD, hEFGH, hIJKL, hDMDN, hFKFI, hHLAB, hKILE⟩
  have hcancel : ∀ s t z : Fin 3, H t (L s z) = z :=
    bridge F K I hFKFI J L hIJKL E hKILE G H hEFGH
  have hBA : ∀ s t : Fin 3, B (A t s) t = s := by
    intro s t
    have h := hHLAB s t
    exact (hcancel s t (B (A t s) t)).symm.trans h
  have hAB : ∀ r t : Fin 3, A t (B r t) = r := by
    intro r t
    let s := (A t).symm r
    have hs : A t s = r := (A t).apply_symm_apply r
    have h := hBA s t
    rw [hs] at h
    calc
      A t (B r t) = A t s := congrArg (A t) h
      _ = r := hs
  have hD : ∀ r t : Fin 3, D r t = t := by
    intro r t
    let s := (C t).symm r
    have hs : C t s = r := (C t).apply_symm_apply r
    have hmain := hABCD s t
    have href := hAB s t
    apply (B s).injective
    apply (A t).injective
    rw [hs] at hmain
    exact hmain.trans href.symm
  have hconstant : ∀ s t : Fin 3, M0 s (N s t) = s := by
    intro s t
    have h := hDMDN s t
    simpa only [hD] using h
  have hzero := hconstant (0 : Fin 3) (0 : Fin 3)
  have hone := hconstant (0 : Fin 3) (1 : Fin 3)
  have hN : N 0 0 = N 0 1 := (M0 0).injective (hzero.trans hone.symm)
  exact Fin.zero_ne_one ((N 0).injective hN)

/-- Core-7 for permutation-valued rows. -/
theorem core7_perm_rows :
    ¬ ∃ A B C D E F G H I J K L M0 N : Core7Op,
      Core7E A B C D ∧ Core7E E F G H ∧ Core7E I J K L ∧
      Core7E D M0 D N ∧ Core7E F K F I ∧
      Core7E H L A B ∧ Core7E K I L E :=
  core7_endgame core7_bridge_finite

/-- Turn a raw operation with bijective rows into a permutation-row operation. -/
noncomputable def core7OpOf (T : Fin 3 → Fin 3 → Fin 3)
    (hT : Core7RowsBijective T) : Core7Op :=
  fun s => Equiv.ofBijective (T s) (hT s)

@[simp]
theorem core7OpOf_apply (T : Fin 3 → Fin 3 → Fin 3)
    (hT : Core7RowsBijective T) (s t : Fin 3) :
    core7OpOf T hT s t = T s t := rfl

/-- The requested self-contained shape-only Core-7 theorem. The seven quadruples are,
in order, `(A,B,C,D)`, `(E,F,G,H)`, `(I,J,K,L)`, `(D,M0,D,N)`,
`(F,K,F,I)`, `(H,L,A,B)`, and `(K,I,L,E)`. -/
theorem core7 :
    ¬ ∃ A B C D E F G H I J K L M0 N : Fin 3 → Fin 3 → Fin 3,
      Core7RowsBijective A ∧ Core7RowsBijective B ∧
      Core7RowsBijective C ∧ Core7RowsBijective D ∧
      Core7RowsBijective E ∧ Core7RowsBijective F ∧
      Core7RowsBijective G ∧ Core7RowsBijective H ∧
      Core7RowsBijective I ∧ Core7RowsBijective J ∧
      Core7RowsBijective K ∧ Core7RowsBijective L ∧
      Core7RowsBijective M0 ∧ Core7RowsBijective N ∧
      Core7ERaw A B C D ∧ Core7ERaw E F G H ∧ Core7ERaw I J K L ∧
      Core7ERaw D M0 D N ∧ Core7ERaw F K F I ∧
      Core7ERaw H L A B ∧ Core7ERaw K I L E := by
  classical
  rintro ⟨A, B, C, D, E, F, G, H, I, J, K, L, M0, N,
    hA, hB, hC, hD, hE, hF, hG, hH, hI, hJ, hK, hL, hM0, hN,
    hABCD, hEFGH, hIJKL, hDMDN, hFKFI, hHLAB, hKILE⟩
  apply core7_perm_rows
  refine ⟨core7OpOf A hA, core7OpOf B hB, core7OpOf C hC, core7OpOf D hD,
    core7OpOf E hE, core7OpOf F hF, core7OpOf G hG, core7OpOf H hH,
    core7OpOf I hI, core7OpOf J hJ, core7OpOf K hK, core7OpOf L hL,
    core7OpOf M0 hM0, core7OpOf N hN, ?_⟩
  simpa only [Core7E, Core7ERaw, core7OpOf_apply] using
    And.intro hABCD (And.intro hEFGH (And.intro hIJKL
      (And.intro hDMDN (And.intro hFKFI (And.intro hHLAB hKILE)))))

#print axioms core7_collision_forces
#print axioms core7AllFin_eq_true
#print axioms core7AnyFin_eq_true
#print axioms core7Decode_apply
#print axioms core7Decode_injective
#print axioms core7Op_card
#print axioms core7Decode_bijective
#print axioms core7Decode_encode
#print axioms core7_bridge_check
#print axioms core7_bridge_decoded
#print axioms core7_bridge_finite
#print axioms core7_endgame
#print axioms core7_perm_rows
#print axioms core7OpOf_apply
#print axioms core7

end Ext677
