# K6-GC-LEAN-3 — third repair round for GoodCount3.lean (your round-2 file compiled: 33 errors, down from 45)

Return the COMPLETE corrected file (one ```lean block), no `sorry`/`admit`/`native_decide`, no new axioms.
The full compiler output is below. Diagnosis from the line — the errors are systematic, not mathematical:
1. **`let`-bound abbreviations do not unfold.** In `deltaSix_count_ge_two` and the `group*` lemmas you
   introduce `p q r s u … : K := …` with `let`/`set`; afterwards `simpa [Delta, A, B]`, `ring`,
   `linear_combination` and `exact` see opaque `p`, `q`, `A`, `B` (e.g. line 88: `this : -(b.1 * br a b) +
   b.2 * br b c = 0` is "not" `-r * A + s * C = 0`; lines 176/252: `ring failed`). Fix: do NOT use `let`.
   Either (a) state each algebraic step as a standalone lemma over plain variables
   `(p q r s A B C : K) (h1 : p*A + q*B = 0) (h2 : p*B + q*A = 0) …` and apply it with explicit
   arguments, or (b) use `set p := a.1 with hp` and rewrite with `hp` before `ring`/`linear_combination`,
   or (c) work directly with `a.1`, `a.2`, `br a b` everywhere (verbose but robust); after `unfold Delta br`
   every identity is a polynomial identity in the coordinates and `linear_combination` with explicit
   coefficients closes it.
2. Lines 350–403: `Application type mismatch` / `Expected type must not contain metavariables` /
   `failed to synthesize instance` — give the `Finset.filter` predicate explicitly with its `DecidablePred`
   (use `open Classical` or `[DecidableEq K]` is not available for a general field — write
   `classical` at the start of the tactic block, and state cardinalities as `2 ≤ (Finset.univ.filter (fun i : Fin 6 => f i ≠ 0)).card`
   with `f : Fin 6 → K` a plain function `![Δ₁, …, Δ₆]`); avoid `Finset.card_pos`-style lemmas with
   implicit arguments the elaborator cannot infer — supply them.
3. Line 503: `Unknown identifier i` — a binder is missing (`fun i => …` or `∀ i,`); check the statement of
   `goodCount3` and `det_colPerm_krylov_eq_Delta`.
4. Lines 432/455 `rewrite` failed and 445/451 `unsolved goals` — inside the 3×3 determinant reduction:
   prove `det_e1_aux` as `Matrix.det_fin_three` + `simp [Matrix.of_apply, Matrix.cons_val', Matrix.vecHead,
   Matrix.vecTail]` + `ring`, and keep the statement literally in terms of `!![…]` entries.
Keep the final theorem's meaning unchanged: for every field K and A : Matrix (Fin 3) (Fin 3) K with
IsUnit A.det, at least two column permutations σ make e₁ Krylov-cyclic for the column-permuted matrix.

## Compiler output (complete)
```
K1695/GoodCount3.lean:31:2: warning: try 'simp' instead of 'simpa'

Note: This linter can be disabled with `set_option linter.unnecessarySimpa false`
K1695/GoodCount3.lean:88:4: error: Type mismatch
  this
has type
  -(b.1 * br a b) + b.2 * br b c = 0
but is expected to have type
  -r * A + s * C = 0
K1695/GoodCount3.lean:103:32: error: Application type mismatch: The argument
  this
has type
  q = 0 ∨ B = 0
but is expected to have type
  ?m.367 * ?m.368 = 0
in the application
  mul_eq_zero.mp this
K1695/GoodCount3.lean:107:32: error: Application type mismatch: The argument
  this
has type
  p = 0 ∨ B = 0
but is expected to have type
  ?m.389 * ?m.390 = 0
in the application
  mul_eq_zero.mp this
K1695/GoodCount3.lean:113:32: error: Application type mismatch: The argument
  this
has type
  s = 0 ∨ C = 0
but is expected to have type
  ?m.414 * ?m.415 = 0
in the application
  mul_eq_zero.mp this
K1695/GoodCount3.lean:117:32: error: Application type mismatch: The argument
  this
has type
  r = 0 ∨ C = 0
but is expected to have type
  ?m.436 * ?m.437 = 0
in the application
  mul_eq_zero.mp this
K1695/GoodCount3.lean:176:10: error: ring failed, ring expressions not equal
K : Type u
inst✝ : Field K
a b c : K × K
ha : Delta a b c = 0 ∧ Delta a c b = 0
hb : Delta b a c = 0 ∧ Delta b c a = 0
p : K := ⋯
q : K := ⋯
r : K := ⋯
s : K := ⋯
u : K := ⋯
v : K := ⋯
A : K := ⋯
B : K := ⋯
C : K := ⋯
hspan : A ≠ 0 ∨ B ≠ 0 ∨ C ≠ 0
A_eq : A = p * s - q * r
B_eq : B = p * v - q * u
C_eq : C = r * v - s * u
hba : br b a = -A
hca : br c a = -B
hcb : br c b = -C
ha1 : p * A + q * B = 0
ha2 : p * B + q * A = 0
hb1 : -r * A + s * C = 0
hb2 : r * C - s * A = 0
hA : A ≠ 0
hpq_mul : (p ^ 2 - q ^ 2) * A = 0
hpq_eq : p ^ 2 = q ^ 2
hrs_mul : (r ^ 2 - s ^ 2) * A = 0
hrs_eq : r ^ 2 = s ^ 2
hpq : p = q
hrs : r = -s
hsr : s = -r
hp_ne_zero : p ≠ 0
hr_ne_zero : r ≠ 0
this : q * A + q * B = 0
⊢ p * A + p * B - A * q - B * q = 0
K1695/GoodCount3.lean:252:10: error: ring failed, ring expressions not equal
K : Type u
inst✝ : Field K
a b c : K × K
ha : Delta a b c = 0 ∧ Delta a c b = 0
hb : Delta b a c = 0 ∧ Delta b c a = 0
p : K := ⋯
q : K := ⋯
r : K := ⋯
s : K := ⋯
u : K := ⋯
v : K := ⋯
A : K := ⋯
B : K := ⋯
C : K := ⋯
hspan : A ≠ 0 ∨ B ≠ 0 ∨ C ≠ 0
A_eq : A = p * s - q * r
B_eq : B = p * v - q * u
C_eq : C = r * v - s * u
hba : br b a = -A
hca : br c a = -B
hcb : br c b = -C
ha1 : p * A + q * B = 0
ha2 : p * B + q * A = 0
hb1 : -r * A + s * C = 0
hb2 : r * C - s * A = 0
hA : A ≠ 0
hpq_mul : (p ^ 2 - q ^ 2) * A = 0
hpq_eq : p ^ 2 = q ^ 2
hrs_mul : (r ^ 2 - s ^ 2) * A = 0
hrs_eq : r ^ 2 = s ^ 2
hpq : p = -q
hrs : r = s
hq : q = -p
hp_ne_zero : p ≠ 0
hr_ne_zero : r ≠ 0
hB : B = A
this : s * C - s * A = 0
⊢ r * C - r * A - C * s + A * s = 0
K1695/GoodCount3.lean:350:41: error: Application type mismatch: The argument
  h1'
has type
  Delta x1 x0 x2 = 0 ∧ Delta x1 x2 x0 = 0
but is expected to have type
  Delta x1 x2 x0 = 0 ∧ Delta x1 x0 x2 = 0
in the application
  Delta_third_ne_zero x1 x2 x0 h1'
K1695/GoodCount3.lean:357:9: error(lean.synthInstanceFailed): failed to synthesize instance of type class
  DecidablePred fun i => deltaSix x0 x1 x2 i ≠ 0

Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.
K1695/GoodCount3.lean:364:51: error: Expected type must not contain metavariables
  ?m.100 ≠ ?m.101
K1695/GoodCount3.lean:364:43: error: Application type mismatch: The argument
  h.right
has type
  deltaSix x0 x1 x2 5 ≠ 0
but is expected to have type
  ?m.98 ?m.101
in the application
  card_ge_two_of_two_ne_zero ?m.104 h.right
K1695/GoodCount3.lean:367:53: error: Expected type must not contain metavariables
  ?m.139 ≠ ?m.140
K1695/GoodCount3.lean:367:45: error: Application type mismatch: The argument
  h.right
has type
  deltaSix x0 x1 x2 3 ≠ 0
but is expected to have type
  ?m.137 ?m.140
in the application
  card_ge_two_of_two_ne_zero ?m.143 h.right
K1695/GoodCount3.lean:369:10: warning: `push_neg` has been deprecated. Prefer using `push Not` instead.
If you'd rather continue using `push_neg` in your project, you can implement it as follows:
```
open Lean.Parser.Tactic in
macro "push_neg" cfg:optConfig loc:(location)? : tactic =>
  `(tactic| push $cfg:optConfig Not $[$loc]?)
```
K1695/GoodCount3.lean:370:10: error: Type mismatch
  hz1
has type
  deltaSix x0 x1 x2 2 = 0 → deltaSix x0 x1 x2 3 ≠ 0
but is expected to have type
  p 2 ∨ p 3
K1695/GoodCount3.lean:372:10: warning: `push_neg` has been deprecated. Prefer using `push Not` instead.
If you'd rather continue using `push_neg` in your project, you can implement it as follows:
```
open Lean.Parser.Tactic in
macro "push_neg" cfg:optConfig loc:(location)? : tactic =>
  `(tactic| push $cfg:optConfig Not $[$loc]?)
```
K1695/GoodCount3.lean:373:10: error: Type mismatch
  hz2
has type
  deltaSix x0 x1 x2 4 = 0 → deltaSix x0 x1 x2 5 ≠ 0
but is expected to have type
  p 4 ∨ p 5
K1695/GoodCount3.lean:384:53: error: Expected type must not contain metavariables
  ?m.279 ≠ ?m.280
K1695/GoodCount3.lean:384:45: error: Application type mismatch: The argument
  h.right
has type
  deltaSix x0 x1 x2 1 ≠ 0
but is expected to have type
  ?m.277 ?m.280
in the application
  card_ge_two_of_two_ne_zero ?m.283 h.right
K1695/GoodCount3.lean:386:10: warning: `push_neg` has been deprecated. Prefer using `push Not` instead.
If you'd rather continue using `push_neg` in your project, you can implement it as follows:
```
open Lean.Parser.Tactic in
macro "push_neg" cfg:optConfig loc:(location)? : tactic =>
  `(tactic| push $cfg:optConfig Not $[$loc]?)
```
K1695/GoodCount3.lean:387:10: error: Type mismatch
  hz0
has type
  deltaSix x0 x1 x2 0 = 0 → deltaSix x0 x1 x2 1 ≠ 0
but is expected to have type
  p 0 ∨ p 1
K1695/GoodCount3.lean:389:10: warning: `push_neg` has been deprecated. Prefer using `push Not` instead.
If you'd rather continue using `push_neg` in your project, you can implement it as follows:
```
open Lean.Parser.Tactic in
macro "push_neg" cfg:optConfig loc:(location)? : tactic =>
  `(tactic| push $cfg:optConfig Not $[$loc]?)
```
K1695/GoodCount3.lean:390:10: error: Type mismatch
  hz2
has type
  deltaSix x0 x1 x2 4 = 0 → deltaSix x0 x1 x2 5 ≠ 0
but is expected to have type
  p 4 ∨ p 5
K1695/GoodCount3.lean:399:8: warning: `push_neg` has been deprecated. Prefer using `push Not` instead.
If you'd rather continue using `push_neg` in your project, you can implement it as follows:
```
open Lean.Parser.Tactic in
macro "push_neg" cfg:optConfig loc:(location)? : tactic =>
  `(tactic| push $cfg:optConfig Not $[$loc]?)
```
K1695/GoodCount3.lean:400:8: error: Type mismatch
  hz0
has type
  deltaSix x0 x1 x2 0 = 0 → deltaSix x0 x1 x2 1 ≠ 0
but is expected to have type
  p 0 ∨ p 1
K1695/GoodCount3.lean:402:8: warning: `push_neg` has been deprecated. Prefer using `push Not` instead.
If you'd rather continue using `push_neg` in your project, you can implement it as follows:
```
open Lean.Parser.Tactic in
macro "push_neg" cfg:optConfig loc:(location)? : tactic =>
  `(tactic| push $cfg:optConfig Not $[$loc]?)
```
K1695/GoodCount3.lean:403:8: error: Type mismatch
  hz1
has type
  deltaSix x0 x1 x2 2 = 0 → deltaSix x0 x1 x2 3 ≠ 0
but is expected to have type
  p 2 ∨ p 3
K1695/GoodCount3.lean:432:6: error: Tactic `rewrite` failed: Did not find an occurrence of the pattern
  det ?A
in the target expression
  det ![![1, 0, 0], v, w] = v 1 * w 2 - v 2 * w 1

K : Type u
inst✝ : Field K
v w : Fin 3 → K
⊢ det ![![1, 0, 0], v, w] = v 1 * w 2 - v 2 * w 1

Note: The target expression is not type-correct under the `implicit` transparency level, which may have triggered the failure. This is usually caused by unfolding of semireducible definitions in prior tactic steps. Use `set_option linter.tacticCheckInstances true` to investigate the source of the issue.
Full error:
  Application type mismatch: The argument
    ![![1, 0, 0], v, w]
  has type
    Fin (Nat.succ 0).succ.succ → Fin (Nat.succ 0).succ.succ → K
  but is expected to have type
    Matrix (Fin (Nat.succ 0).succ.succ) (Fin (Nat.succ 0).succ.succ) K
  in the application
    det ![![1, 0, 0], v, w]
K1695/GoodCount3.lean:445:47: error: unsolved goals
K : Type u
inst✝ : Field K
A : Matrix (Fin 3) (Fin 3) K
σ : Perm (Fin 3)
B : Matrix (Fin 3) (Fin 3) K := colPerm A σ
r : Fin 3
⊢ (vecHead fun j => A r (σ j)) = A r (σ 0)
Try this:
  [apply] ring_nf
  
  The `ring` tactic failed to close the goal. Use `ring_nf` to obtain a normal form.
    
  Note that `ring` works primarily in *commutative* rings. If you have a noncommutative ring, abelian group or module, consider using `noncomm_ring`, `abel` or `module` instead.
K1695/GoodCount3.lean:451:31: error: unsolved goals
K : Type u
inst✝ : Field K
A : Matrix (Fin 3) (Fin 3) K
σ : Perm (Fin 3)
B : Matrix (Fin 3) (Fin 3) K := colPerm A σ
hv : B *ᵥ e1Vec = fun r => A r (σ 0)
r : Fin 3
⊢ (vecHead fun j => A r (σ 0) * A 0 (σ j) + A r (σ 1) * A 1 (σ j) + A r (σ 2) * A 2 (σ j)) =
    A r (σ 0) * A 0 (σ 0) + A r (σ 1) * A 1 (σ 0) + A r (σ 2) * A 2 (σ 0)
K1695/GoodCount3.lean:455:6: error: Tactic `rewrite` failed: Did not find an occurrence of the pattern
  det ![![1, 0, 0], B *ᵥ e1Vec, (B * B) *ᵥ e1Vec]
in the target expression
  det ![e1Vec, colPerm A σ *ᵥ e1Vec, (colPerm A σ * colPerm A σ) *ᵥ e1Vec] =
    Delta (A 1 (σ 0), A 2 (σ 0)) (A 1 (σ 1), A 2 (σ 1)) (A 1 (σ 2), A 2 (σ 2))

K : Type u
inst✝ : Field K
A : Matrix (Fin 3) (Fin 3) K
σ : Perm (Fin 3)
B : Matrix (Fin 3) (Fin 3) K := colPerm A σ
hv : B *ᵥ e1Vec = fun r => A r (σ 0)
hw : (B * B) *ᵥ e1Vec = fun r => A r (σ 0) * A 0 (σ 0) + A r (σ 1) * A 1 (σ 0) + A r (σ 2) * A 2 (σ 0)
⊢ det ![e1Vec, colPerm A σ *ᵥ e1Vec, (colPerm A σ * colPerm A σ) *ᵥ e1Vec] =
    Delta (A 1 (σ 0), A 2 (σ 0)) (A 1 (σ 1), A 2 (σ 1)) (A 1 (σ 2), A 2 (σ 2))

Note: The target expression is not type-correct under the `implicit` transparency level, which may have triggered the failure. This is usually caused by unfolding of semireducible definitions in prior tactic steps. Use `set_option linter.tacticCheckInstances true` to investigate the source of the issue.
Full error:
  Application type mismatch: The argument
    ![e1Vec, colPerm A σ *ᵥ e1Vec, (colPerm A σ * colPerm A σ) *ᵥ e1Vec]
  has type
    Fin (Nat.succ 2) → Fin (Nat.succ 2) → K
  but is expected to have type
    Matrix (Fin (Nat.succ 2)) (Fin (Nat.succ 2)) K
  in the application
    det ![e1Vec, colPerm A σ *ᵥ e1Vec, (colPerm A σ * colPerm A σ) *ᵥ e1Vec]
K1695/GoodCount3.lean:461:7: error(lean.synthInstanceFailed): failed to synthesize instance of type class
  DecidablePred fun i =>
    det ![e1Vec, colPerm A (permOfIndex i) *ᵥ e1Vec, (colPerm A (permOfIndex i) * colPerm A (permOfIndex i)) *ᵥ e1Vec] ≠
      0

Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.
K1695/GoodCount3.lean:482:4: warning: `push_neg` has been deprecated. Prefer using `push Not` instead.
If you'd rather continue using `push_neg` in your project, you can implement it as follows:
```
open Lean.Parser.Tactic in
macro "push_neg" cfg:optConfig loc:(location)? : tactic =>
  `(tactic| push $cfg:optConfig Not $[$loc]?)
```
K1695/GoodCount3.lean:503:62: error(lean.unknownIdentifier): Unknown identifier `i`
K1695/GoodCount3.lean:503:62: error(lean.unknownIdentifier): Unknown identifier `i`
K1695/GoodCount3.lean:503:62: error(lean.unknownIdentifier): Unknown identifier `i`
K1695/GoodCount3.lean:503:62: error(lean.unknownIdentifier): Unknown identifier `i`
K1695/GoodCount3.lean:503:62: error(lean.unknownIdentifier): Unknown identifier `i`
K1695/GoodCount3.lean:503:62: error(lean.unknownIdentifier): Unknown identifier `i`
K1695/GoodCount3.lean:499:74: error: unsolved goals
case «0»
K : Type u
inst✝ : Field K
A : Matrix (Fin 3) (Fin 3) K
hA : IsUnit A.det
x : Fin 3 → K × K := fun j => (A 1 j, A 2 j)
hdet_expand : A.det = A 0 0 * br (x 1) (x 2) - A 0 1 * br (x 0) (x 2) + A 0 2 * br (x 0) (x 1)
hspan : br (x 0) (x 1) ≠ 0 ∨ br (x 0) (x 2) ≠ 0 ∨ br (x 1) (x 2) ≠ 0
hcount : 2 ≤ sorry
hEq :
  det
      ![e1Vec, colPerm A (permOfIndex sorry) *ᵥ e1Vec,
        (colPerm A (permOfIndex sorry) * colPerm A (permOfIndex sorry)) *ᵥ e1Vec] =
    Delta (A 1 ((permOfIndex sorry) 0), A 2 ((permOfIndex sorry) 0))
      (A 1 ((permOfIndex sorry) 1), A 2 ((permOfIndex sorry) 1))
      (A 1 ((permOfIndex sorry) 2), A 2 ((permOfIndex sorry) 2))
⊢ ¬det ![e1Vec, colPerm A 1 *ᵥ e1Vec, (colPerm A 1 * colPerm A 1) *ᵥ e1Vec] = 0 ↔
    ¬Delta (A 1 0, A 2 0) (A 1 1, A 2 1) (A 1 2, A 2 2) = 0

case «1»
K : Type u
inst✝ : Field K
A : Matrix (Fin 3) (Fin 3) K
hA : IsUnit A.det
x : Fin 3 → K × K := fun j => (A 1 j, A 2 j)
hdet_expand : A.det = A 0 0 * br (x 1) (x 2) - A 0 1 * br (x 0) (x 2) + A 0 2 * br (x 0) (x 1)
hspan : br (x 0) (x 1) ≠ 0 ∨ br (x 0) (x 2) ≠ 0 ∨ br (x 1) (x 2) ≠ 0
hcount : 2 ≤ sorry
hEq :
  det
      ![e1Vec, colPerm A (permOfIndex sorry) *ᵥ e1Vec,
        (colPerm A (permOfIndex sorry) * colPerm A (permOfIndex sorry)) *ᵥ e1Vec] =
    Delta (A 1 ((permOfIndex sorry) 0), A 2 ((permOfIndex sorry) 0))
      (A 1 ((permOfIndex sorry) 1), A 2 ((permOfIndex sorry) 1))
      (A 1 ((permOfIndex sorry) 2), A 2 ((permOfIndex sorry) 2))
⊢ ¬det
          ![e1Vec, colPerm A (Equiv.swap 1 2) *ᵥ e1Vec,
            (colPerm A (Equiv.swap 1 2) * colPerm A (Equiv.swap 1 2)) *ᵥ e1Vec] =
        0 ↔
    ¬Delta (A 1 0, A 2 0) (A 1 2, A 2 2) (A 1 1, A 2 1) = 0

case «2»
K : Type u
inst✝ : Field K
A : Matrix (Fin 3) (Fin 3) K
hA : IsUnit A.det
x : Fin 3 → K × K := fun j => (A 1 j, A 2 j)
hdet_expand : A.det = A 0 0 * br (x 1) (x 2) - A 0 1 * br (x 0) (x 2) + A 0 2 * br (x 0) (x 1)
hspan : br (x 0) (x 1) ≠ 0 ∨ br (x 0) (x 2) ≠ 0 ∨ br (x 1) (x 2) ≠ 0
hcount : 2 ≤ sorry
hEq :
  det
      ![e1Vec, colPerm A (permOfIndex sorry) *ᵥ e1Vec,
        (colPerm A (permOfIndex sorry) * colPerm A (permOfIndex sorry)) *ᵥ e1Vec] =
    Delta (A 1 ((permOfIndex sorry) 0), A 2 ((permOfIndex sorry) 0))
      (A 1 ((permOfIndex sorry) 1), A 2 ((permOfIndex sorry) 1))
      (A 1 ((permOfIndex sorry) 2), A 2 ((permOfIndex sorry) 2))
⊢ ¬det
          ![e1Vec, colPerm A (Equiv.swap 0 1) *ᵥ e1Vec,
            (colPerm A (Equiv.swap 0 1) * colPerm A (Equiv.swap 0 1)) *ᵥ e1Vec] =
        0 ↔
    ¬Delta (A 1 1, A 2 1) (A 1 0, A 2 0) (A 1 2, A 2 2) = 0

case «3»
K : Type u
inst✝ : Field K
A : Matrix (Fin 3) (Fin 3) K
hA : IsUnit A.det
x : Fin 3 → K × K := fun j => (A 1 j, A 2 j)
hdet_expand : A.det = A 0 0 * br (x 1) (x 2) - A 0 1 * br (x 0) (x 2) + A 0 2 * br (x 0) (x 1)
hspan : br (x 0) (x 1) ≠ 0 ∨ br (x 0) (x 2) ≠ 0 ∨ br (x 1) (x 2) ≠ 0
hcount : 2 ≤ sorry
hEq :
  det
      ![e1Vec, colPerm A (permOfIndex sorry) *ᵥ e1Vec,
        (colPerm A (permOfIndex sorry) * colPerm A (permOfIndex sorry)) *ᵥ e1Vec] =
    Delta (A 1 ((permOfIndex sorry) 0), A 2 ((permOfIndex sorry) 0))
      (A 1 ((permOfIndex sorry) 1), A 2 ((permOfIndex sorry) 1))
      (A 1 ((permOfIndex sorry) 2), A 2 ((permOfIndex sorry) 2))
⊢ ¬det
          ![e1Vec, colPerm A (Equiv.trans (Equiv.swap 1 2) (Equiv.swap 0 1)) *ᵥ e1Vec,
            (colPerm A (Equiv.trans (Equiv.swap 1 2) (Equiv.swap 0 1)) *
                colPerm A (Equiv.trans (Equiv.swap 1 2) (Equiv.swap 0 1))) *ᵥ
              e1Vec] =
        0 ↔
    ¬Delta (A 1 1, A 2 1) (A 1 2, A 2 2) (A 1 0, A 2 0) = 0

case «4»
K : Type u
inst✝ : Field K
A : Matrix (Fin 3) (Fin 3) K
hA : IsUnit A.det
x : Fin 3 → K × K := fun j => (A 1 j, A 2 j)
hdet_expand : A.det = A 0 0 * br (x 1) (x 2) - A 0 1 * br (x 0) (x 2) + A 0 2 * br (x 0) (x 1)
hspan : br (x 0) (x 1) ≠ 0 ∨ br (x 0) (x 2) ≠ 0 ∨ br (x 1) (x 2) ≠ 0
hcount : 2 ≤ sorry
hEq :
  det
      ![e1Vec, colPerm A (permOfIndex sorry) *ᵥ e1Vec,
        (colPerm A (permOfIndex sorry) * colPerm A (permOfIndex sorry)) *ᵥ e1Vec] =
    Delta (A 1 ((permOfIndex sorry) 0), A 2 ((permOfIndex sorry) 0))
      (A 1 ((permOfIndex sorry) 1), A 2 ((permOfIndex sorry) 1))
      (A 1 ((permOfIndex sorry) 2), A 2 ((permOfIndex sorry) 2))
⊢ ¬det
          ![e1Vec, colPerm A (Equiv.trans (Equiv.swap 0 1) (Equiv.swap 1 2)) *ᵥ e1Vec,
            (colPerm A (Equiv.trans (Equiv.swap 0 1) (Equiv.swap 1 2)) *
                colPerm A (Equiv.trans (Equiv.swap 0 1) (Equiv.swap 1 2))) *ᵥ
              e1Vec] =
        0 ↔
    ¬Delta (A 1 2, A 2 2) (A 1 0, A 2 0) (A 1 1, A 2 1) = 0

case «5»
K : Type u
inst✝ : Field K
A : Matrix (Fin 3) (Fin 3) K
hA : IsUnit A.det
x : Fin 3 → K × K := fun j => (A 1 j, A 2 j)
hdet_expand : A.det = A 0 0 * br (x 1) (x 2) - A 0 1 * br (x 0) (x 2) + A 0 2 * br (x 0) (x 1)
hspan : br (x 0) (x 1) ≠ 0 ∨ br (x 0) (x 2) ≠ 0 ∨ br (x 1) (x 2) ≠ 0
hcount : 2 ≤ sorry
hEq :
  det
      ![e1Vec, colPerm A (permOfIndex sorry) *ᵥ e1Vec,
        (colPerm A (permOfIndex sorry) * colPerm A (permOfIndex sorry)) *ᵥ e1Vec] =
    Delta (A 1 ((permOfIndex sorry) 0), A 2 ((permOfIndex sorry) 0))
      (A 1 ((permOfIndex sorry) 1), A 2 ((permOfIndex sorry) 1))
      (A 1 ((permOfIndex sorry) 2), A 2 ((permOfIndex sorry) 2))
⊢ ¬det
          ![e1Vec, colPerm A (Equiv.swap 0 2) *ᵥ e1Vec,
            (colPerm A (Equiv.swap 0 2) * colPerm A (Equiv.swap 0 2)) *ᵥ e1Vec] =
        0 ↔
    ¬Delta (A 1 2, A 2 2) (A 1 1, A 2 1) (A 1 0, A 2 0) = 0
```
