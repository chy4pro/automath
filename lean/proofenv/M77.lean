import Mathlib.Tactic

/-!
# An order-77 magma satisfying E677, non-idempotent and not right-cancellative

This file formalises the model produced by campaign #1
(see `problems/etp677/R6C_codex_report.md`).

## The model

The carrier is `F₁₁ × F₇`, of order `77 = 11 * 7`.  Writing
`d = y - x (mod 11)` for the base offset and

* `(a_d, b_d) = (4, 1)` for `d = 0`,
* `(a_d, b_d) = (0, 1)` for `d` a nonzero quadratic residue mod `11`,
  i.e. `d ∈ {1, 3, 4, 5, 9}`,
* `(a_d, b_d) = (3, 5)` for `d` a non-residue, i.e. `d ∈ {2, 6, 7, 8, 10}`,

the multiplication is

`(x, s) * (y, t) = (6 * x + 6 * y  mod 11,  a_d * s + b_d * t  mod 7)`.

## Representation

For efficient kernel evaluation the carrier is realised as `Fin 77`, with the
pair `(x, s) ∈ F₁₁ × F₇` encoded as the natural number `7 * x + s`.  All
arithmetic is plain `Nat` arithmetic, which the kernel evaluates with its
GMP-accelerated `Nat` primitives; a `Fin 11 × Fin 7` carrier would instead force
the kernel through `Fin`/`Fintype` instance layers on both coordinates.
`M77.mulN_enc` certifies that the encoded operation is literally the displayed
formula on pairs, and `M77.offs_sub` certifies that the truncated-subtraction
offset `(y + 11 - x) % 11` is the genuine difference `y - x` mod `11`, so the
encoding is not load-bearing for the meaning of the statements below.

## Results

* `M77.E677` : `∀ x y, x = y * (x * ((y * x) * y))` — the equation E677 holds.
* `M77.E255` : `∀ x, x = ((x * x) * x) * x` — the equation E255 holds.
* `M77.not_idempotent` : `∃ x, x * x ≠ x`.
* `M77.not_right_cancellative` : `∃ a b t, a ≠ b ∧ a * t = b * t`.
* `M77.right_translation_not_injective` : the stronger statement that *every*
  one of the 77 right translations is non-injective, with explicit witnesses.

Every proof is by `decide`, i.e. by kernel evaluation of the finite check.
`native_decide` is **not** used anywhere.  The audit at the end of the file
records that no proof depends on `Classical.choice`.
-/

namespace M77

/-! ## The multiplication -/

/-- `isQR d` says that `d` is a nonzero quadratic residue modulo `11`.
The nonzero squares mod `11` are `1, 3, 4, 5, 9`. -/
def isQR (d : Nat) : Bool := d = 1 || d = 3 || d = 4 || d = 5 || d = 9

/-- The fibre coefficient `a_d`: `4` at offset `0`, `0` at a nonzero quadratic
residue offset, `3` at a non-residue offset. -/
def coefA (d : Nat) : Nat := if d = 0 then 4 else if isQR d then 0 else 3

/-- The fibre coefficient `b_d`: `1` at offset `0`, `1` at a nonzero quadratic
residue offset, `5` at a non-residue offset. -/
def coefB (d : Nat) : Nat := if d = 0 then 1 else if isQR d then 1 else 5

/-- Encoding of a pair `(x, s) ∈ F₁₁ × F₇` as an element of `Fin 77`. -/
def enc (x s : Nat) : Nat := 7 * x + s

/-- The base offset `d = y - x (mod 11)` of a pair of encoded elements. -/
def offs (a b : Nat) : Nat := (b / 7 + 11 - a / 7) % 11

/-- The multiplication of the model, expressed on encodings. -/
def mulN (a b : Nat) : Nat :=
  7 * ((6 * (a / 7) + 6 * (b / 7)) % 11)
    + (coefA (offs a b) * (a % 7) + coefB (offs a b) * (b % 7)) % 7

theorem mulN_lt (a b : Nat) : mulN a b < 77 := by
  have h1 : (6 * (a / 7) + 6 * (b / 7)) % 11 < 11 := Nat.mod_lt _ (by omega)
  have h2 : (coefA (offs a b) * (a % 7) + coefB (offs a b) * (b % 7)) % 7 < 7 :=
    Nat.mod_lt _ (by omega)
  show 7 * ((6 * (a / 7) + 6 * (b / 7)) % 11)
      + (coefA (offs a b) * (a % 7) + coefB (offs a b) * (b % 7)) % 7 < 77
  omega

/-- For `x < 11` the truncated-subtraction expression `y + 11 - x` used in
`offs` represents the genuine integer difference `y - x` modulo `11`. -/
theorem offs_sub (x y : Nat) (hx : x < 11) :
    ((y + 11 - x : Nat) : Int) % 11 = ((y : Int) - (x : Int)) % 11 := by
  omega

/-- The encoded multiplication really is the displayed formula
`(x, s) * (y, t) = (6x + 6y mod 11, a_d s + b_d t mod 7)` with
`d = y - x mod 11`. -/
theorem mulN_enc (x s y t : Nat) (hs : s < 7) (ht : t < 7) :
    mulN (enc x s) (enc y t) =
      enc ((6 * x + 6 * y) % 11)
        ((coefA ((y + 11 - x) % 11) * s + coefB ((y + 11 - x) % 11) * t) % 7) := by
  have e1 : (7 * x + s) / 7 = x := by omega
  have e2 : (7 * x + s) % 7 = s := by omega
  have e3 : (7 * y + t) / 7 = y := by omega
  have e4 : (7 * y + t) % 7 = t := by omega
  show 7 * ((6 * ((7 * x + s) / 7) + 6 * ((7 * y + t) / 7)) % 11)
      + (coefA (offs (7 * x + s) (7 * y + t)) * ((7 * x + s) % 7)
        + coefB (offs (7 * x + s) (7 * y + t)) * ((7 * y + t) % 7)) % 7 = _
  rw [offs, e1, e2, e3, e4, enc]

/-- The magma structure on `Fin 77`. -/
instance instMul : Mul (Fin 77) := ⟨fun a b => ⟨mulN a.val b.val, mulN_lt _ _⟩⟩

theorem val_mul (a b : Fin 77) : (a * b).val = mulN a.val b.val := rfl

/-- Guard: the `*` appearing in every statement below elaborates to `instMul`,
the magma operation defined above, and **not** to `Fin 77`'s ring
multiplication.  If instance resolution ever picked the ring structure this
`rfl` would fail. -/
example : ∀ a b : Fin 77, a * b = ⟨mulN a.val b.val, mulN_lt _ _⟩ := fun _ _ => rfl

set_option maxRecDepth 100000

/-! ## E677 -/

/-- **E677 holds identically in this order-77 magma.**  All `77² = 5929`
instances are verified by kernel evaluation. -/
theorem E677 : ∀ x y : Fin 77, x = y * (x * ((y * x) * y)) := by decide

/-! ## E255 -/

/-- **E255 holds identically**, even though the magma is far from idempotent:
`x * x = (x, 5s)`, `(x * x) * x = (x, 0)`, `((x * x) * x) * x = (x, s)`. -/
theorem E255 : ∀ x : Fin 77, x = ((x * x) * x) * x := by decide

/-! ## Non-idempotency -/

/-- The magma is **not** idempotent: the element `(0, 1)`, encoded as `1`,
squares to `(0, 5)`, encoded as `5`.  (In fact only the 11 elements `(x, 0)`
are idempotent.) -/
theorem not_idempotent : ∃ x : Fin 77, x * x ≠ x :=
  ⟨1, by decide⟩

theorem not_all_idempotent : ¬ ∀ x : Fin 77, x * x = x := by
  obtain ⟨x, hx⟩ := not_idempotent
  exact fun h => hx (h x)

/-! ## Failure of right cancellation -/

/-- The magma is **not** right-cancellative: the distinct elements `(0, 0)` and
`(0, 1)` (encoded `0` and `1`) both send `(1, 0)` (encoded `7`) to `(6, 0)`
(encoded `42`).  The offset here is `d = 1`, a nonzero quadratic residue, where
the fibre operation is `(s, t) ↦ t` and so forgets the left argument. -/
theorem not_right_cancellative :
    ∃ a b t : Fin 77, a ≠ b ∧ a * t = b * t :=
  ⟨0, 1, 7, by decide, by decide⟩

/-- First witness row for the column `c`: the element `(y - 1, 0)`, where `y` is
the base coordinate of `c`.  The offset from this row to `c` is `1`, a nonzero
quadratic residue mod `11`, so the fibre operation at that offset is
`(s, t) ↦ t`, which forgets `s`. -/
def rowA (c : Fin 77) : Fin 77 := ⟨7 * ((c.val / 7 + 10) % 11), by omega⟩

/-- Second witness row for the column `c`: the element `(y - 1, 1)`. -/
def rowB (c : Fin 77) : Fin 77 := ⟨7 * ((c.val / 7 + 10) % 11) + 1, by omega⟩

/-- **Every one of the 77 right translations is non-injective.**  This is the
strong form of the failure of right cancellation, matching the report's claim
that all 77 columns collapse. -/
theorem right_translation_not_injective :
    ∀ c : Fin 77, rowA c ≠ rowB c ∧ rowA c * c = rowB c * c := by decide

/-! ## Sanity checks on the model data -/

example : coefA 0 = 4 ∧ coefB 0 = 1 := by decide

example : (coefA 1 = 0 ∧ coefB 1 = 1) ∧ (coefA 3 = 0 ∧ coefB 3 = 1) ∧
    (coefA 4 = 0 ∧ coefB 4 = 1) ∧ (coefA 5 = 0 ∧ coefB 5 = 1) ∧
    (coefA 9 = 0 ∧ coefB 9 = 1) := by decide

example : (coefA 2 = 3 ∧ coefB 2 = 5) ∧ (coefA 6 = 3 ∧ coefB 6 = 5) ∧
    (coefA 7 = 3 ∧ coefB 7 = 5) ∧ (coefA 8 = 3 ∧ coefB 8 = 5) ∧
    (coefA 10 = 3 ∧ coefB 10 = 5) := by decide

example : (1 : Fin 77) * (1 : Fin 77) = (5 : Fin 77) := by decide

example : (0 : Fin 77) * (7 : Fin 77) = (42 : Fin 77) := by decide

example : (1 : Fin 77) * (7 : Fin 77) = (42 : Fin 77) := by decide

/-! ## Axiom audit

`native_decide` is not used; no proof below depends on `Classical.choice`. -/

#print axioms mulN_lt
#print axioms offs_sub
#print axioms mulN_enc
#print axioms E677
#print axioms E255
#print axioms not_idempotent
#print axioms not_all_idempotent
#print axioms not_right_cancellative
#print axioms right_translation_not_injective

end M77
