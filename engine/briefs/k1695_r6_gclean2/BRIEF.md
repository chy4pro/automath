# K6-GC-LEAN-2 — repair round for GoodCount3.lean (your file from K6-GC-LEAN; the line compiled it)

Your file `GoodCount3.lean` (verbatim as you wrote it) was compiled with `lake env lean` against the
line's Mathlib (Lean 4, Mathlib master of August 2026). It produced 45 errors; the complete compiler
output is below (file:line:col, message, and goal states). Please return the COMPLETE corrected file
(one ```lean block), no `sorry`, no `native_decide`, no new axioms. Notes from the line:
* line 26: `(mul_eq_zero.1 this).1` — `.1` on an `Or` is not a projection; use `.elim id id` or
  `by rcases mul_eq_zero.1 this with h | h <;> exact h`.
* line 41: `eq_neg_of_add_eq_zero_left` already exists in Mathlib — rename yours (or use Mathlib's).
* Many `simp` steps on `br`/`Delta` fail: prefer `unfold br Delta` (or `simp only [br, Delta]`) followed by
  `ring` / `linear_combination`, and give explicit `linear_combination` certificates for the polynomial
  identities (e.g. silence ⟹ (p²−q²)·A = 0 is `linear_combination p * h1 - q * h2`).
* For the 3×3 determinant use `Matrix.det_fin_three` and `Matrix.mulVec`, `Matrix.of`, `![…]` with
  `simp [Matrix.mulVec, Matrix.dotProduct, Fin.sum_univ_three]` or `decide`-free `fin_cases`.
* `Equiv.Perm.permMatrix` in Mathlib: `(σ.permMatrix K) i j = if σ.symm i = j then 1 else 0`
  (i.e. `PEquiv.toMatrix (σ.toPEquiv)` … check `Equiv.Perm.permMatrix_apply` / `PEquiv.toMatrix_apply`);
  if the convention fights you, state GC3 with an explicit column-permuted matrix
  `Matrix.of fun i j => A i (σ j)` instead — the line accepts either statement.
If a lemma resists, isolate it as a separate `lemma` with the smallest possible statement so the
line can repair it by hand; keep the final theorem statement unchanged in meaning.

## Compiler output (complete)
```
K1695/GoodCount3.lean:26:8: error: Invalid projection: Projections extract constructor fields for one-constructor inductive types. The expression
  mul_eq_zero.mp this
has type `a = 0 ∨ a = 0` which is not a one-constructor inductive type.
K1695/GoodCount3.lean:41:6: error: `eq_neg_of_add_eq_zero_left` has already been declared
K1695/GoodCount3.lean:76:4: error: Tactic `simp` failed with a nested error:
maximum recursion depth has been reached
use `set_option maxRecDepth <num>` to increase limit
use `set_option diagnostics true` to get diagnostic information
K1695/GoodCount3.lean:78:4: error: Tactic `simp` failed with a nested error:
maximum recursion depth has been reached
use `set_option maxRecDepth <num>` to increase limit
use `set_option diagnostics true` to get diagnostic information
K1695/GoodCount3.lean:89:22: error: unsolved goals
K : Type u_1
inst✝ : Field K
a b c : K × K
ha : Delta a b c = 0 ∧ Delta a c b = 0
hb : Delta b a c = 0 ∧ Delta b c a = 0
p : K := a.1
q : K := a.2
r : K := b.1
s : K := b.2
u : K := c.1
v : K := c.2
A : K := br a b
B : K := br a c
C : K := br b c
ha1 : p * A + q * B = 0
ha2 : p * B + q * A = 0
hb1 : -r * A + s * C = 0
hb2 : r * C - s * A = 0
hA0 : A = 0
hAC : br a c ≠ 0
hqB : q * B = 0
hpB : p * B = 0
hq0 : q = 0
hp0 : p = 0
⊢ a.1 * c.2 - a.2 * c.1 = 0
K1695/GoodCount3.lean:95:22: error: unsolved goals
K : Type u_1
inst✝ : Field K
a b c : K × K
ha : Delta a b c = 0 ∧ Delta a c b = 0
hb : Delta b a c = 0 ∧ Delta b c a = 0
p : K := a.1
q : K := a.2
r : K := b.1
s : K := b.2
u : K := c.1
v : K := c.2
A : K := br a b
B : K := br a c
C : K := br b c
ha1 : p * A + q * B = 0
ha2 : p * B + q * A = 0
hb1 : -r * A + s * C = 0
hb2 : r * C - s * A = 0
hA0 : A = 0
hBC : br b c ≠ 0
hsC : s * C = 0
hrC : r * C = 0
hs0 : s = 0
hr0 : r = 0
⊢ b.1 * c.2 - b.2 * c.1 = 0
K1695/GoodCount3.lean:115:14: error: unsolved goals
K : Type u_1
inst✝ : Field K
a b c : K × K
ha : Delta a b c = 0 ∧ Delta a c b = 0
hb : Delta b a c = 0 ∧ Delta b c a = 0
hspan : br a b ≠ 0 ∨ br a c ≠ 0 ∨ br b c ≠ 0
p : K := a.1
q : K := a.2
r : K := b.1
s : K := b.2
u : K := c.1
v : K := c.2
A : K := br a b
B : K := br a c
C : K := br b c
ha1 : p * A + q * B = 0
ha2 : p * B + q * A = 0
hb1 : -r * A + s * C = 0
hb2 : r * C - s * A = 0
hA : A ≠ 0
hpq_mul : (p ^ 2 - q ^ 2) * A = 0
hpq_eq : p ^ 2 = q ^ 2
hb1' : r * A - s * C = 0
hrs_mul : (r ^ 2 - s ^ 2) * A = 0
hrs_eq : r ^ 2 = s ^ 2
hp0 : p = 0
hq0 : q = 0
⊢ a.1 * b.2 - a.2 * b.1 = 0
K1695/GoodCount3.lean:123:14: error: unsolved goals
K : Type u_1
inst✝ : Field K
a b c : K × K
ha : Delta a b c = 0 ∧ Delta a c b = 0
hb : Delta b a c = 0 ∧ Delta b c a = 0
hspan : br a b ≠ 0 ∨ br a c ≠ 0 ∨ br b c ≠ 0
p : K := a.1
q : K := a.2
r : K := b.1
s : K := b.2
u : K := c.1
v : K := c.2
A : K := br a b
B : K := br a c
C : K := br b c
ha1 : p * A + q * B = 0
ha2 : p * B + q * A = 0
hb1 : -r * A + s * C = 0
hb2 : r * C - s * A = 0
hA : A ≠ 0
hpq_mul : (p ^ 2 - q ^ 2) * A = 0
hpq_eq : p ^ 2 = q ^ 2
hb1' : r * A - s * C = 0
hrs_mul : (r ^ 2 - s ^ 2) * A = 0
hrs_eq : r ^ 2 = s ^ 2
hp : p ≠ 0
hq : q ≠ 0
hr0 : r = 0
hs0 : s = 0
⊢ a.1 * b.2 - a.2 * b.1 = 0
Try this:
  [apply] ring_nf
  
  The `ring` tactic failed to close the goal. Use `ring_nf` to obtain a normal form.
    
  Note that `ring` works primarily in *commutative* rings. If you have a noncommutative ring, abelian group or module, consider using `noncomm_ring`, `abel` or `module` instead.
K1695/GoodCount3.lean:133:22: error: unsolved goals
K : Type u_1
inst✝ : Field K
a b c : K × K
ha : Delta a b c = 0 ∧ Delta a c b = 0
hb : Delta b a c = 0 ∧ Delta b c a = 0
hspan : br a b ≠ 0 ∨ br a c ≠ 0 ∨ br b c ≠ 0
p : K := a.1
q : K := a.2
r : K := b.1
s : K := b.2
u : K := c.1
v : K := c.2
A : K := br a b
B : K := br a c
C : K := br b c
ha1 : p * A + q * B = 0
ha2 : p * B + q * A = 0
hb1 : -r * A + s * C = 0
hb2 : r * C - s * A = 0
hA : A ≠ 0
hpq_mul : (p ^ 2 - q ^ 2) * A = 0
hpq_eq : p ^ 2 = q ^ 2
hb1' : r * A - s * C = 0
hrs_mul : (r ^ 2 - s ^ 2) * A = 0
hrs_eq : r ^ 2 = s ^ 2
hp : p ≠ 0
hq : q ≠ 0
hr : r ≠ 0
hs : s ≠ 0
hpq : p = q
hrs : r = s
⊢ a.1 * b.2 - a.2 * b.1 = 0
K1695/GoodCount3.lean:142:41: error: Application type mismatch: The argument
  this
has type
  A + B = 0
but is expected to have type
  B + A = 0
in the application
  eq_neg_of_add_eq_zero_left this
K1695/GoodCount3.lean:156:14: warning: Possibly looping simp theorem: `Delta.eq_1`

Note: Possibly caused by: `br_antisymm`

Hint: You can disable a simp theorem from the default simp set by passing `- theoremName` to `simp`.
K1695/GoodCount3.lean:156:21: warning: Possibly looping simp theorem: `br_antisymm`

Hint: You can disable a simp theorem from the default simp set by passing `- theoremName` to `simp`.
K1695/GoodCount3.lean:156:8: error: Tactic `simp` failed with a nested error:
maximum recursion depth has been reached
use `set_option maxRecDepth <num>` to increase limit
use `set_option diagnostics true` to get diagnostic information
K1695/GoodCount3.lean:159:14: warning: Possibly looping simp theorem: `Delta.eq_1`

Note: Possibly caused by: `br_antisymm`

Hint: You can disable a simp theorem from the default simp set by passing `- theoremName` to `simp`.
K1695/GoodCount3.lean:159:21: warning: Possibly looping simp theorem: `br_antisymm`

Hint: You can disable a simp theorem from the default simp set by passing `- theoremName` to `simp`.
K1695/GoodCount3.lean:159:8: error: Tactic `simp` failed with a nested error:
maximum recursion depth has been reached
use `set_option maxRecDepth <num>` to increase limit
use `set_option diagnostics true` to get diagnostic information
K1695/GoodCount3.lean:164:31: error: Tactic `rewrite` failed: Did not find an occurrence of the pattern
  -A
in the target expression
  A = 0

K : Type u_1
inst✝ : Field K
a b c : K × K
ha : Delta a b c = 0 ∧ Delta a c b = 0
hb : Delta b a c = 0 ∧ Delta b c a = 0
hspan : br a b ≠ 0 ∨ br a c ≠ 0 ∨ br b c ≠ 0
p : K := a.1
q : K := a.2
r : K := b.1
s : K := b.2
u : K := c.1
v : K := c.2
A : K := br a b
B : K := br a c
C : K := br b c
ha1 : p * A + q * B = 0
ha2 : p * B + q * A = 0
hb1 : -r * A + s * C = 0
hb2 : r * C - s * A = 0
hA : A ≠ 0
hpq_mul : (p ^ 2 - q ^ 2) * A = 0
hpq_eq : p ^ 2 = q ^ 2
hb1' : r * A - s * C = 0
hrs_mul : (r ^ 2 - s ^ 2) * A = 0
hrs_eq : r ^ 2 = s ^ 2
hp : p ≠ 0
hq : q ≠ 0
hr : r ≠ 0
hs : s ≠ 0
hpq : p = q
hsr : s = -r
hB : B = -A
hC : C = -A
hsum : r * (u + v) = -A
D1 : Delta c a b = A * (u + v)
D2 : Delta c b a = A * (u + v)
h : A * (u + v) = 0
huv : u + v = 0
⊢ A = 0
K1695/GoodCount3.lean:168:31: error: Tactic `rewrite` failed: Did not find an occurrence of the pattern
  -A
in the target expression
  A = 0

K : Type u_1
inst✝ : Field K
a b c : K × K
ha : Delta a b c = 0 ∧ Delta a c b = 0
hb : Delta b a c = 0 ∧ Delta b c a = 0
hspan : br a b ≠ 0 ∨ br a c ≠ 0 ∨ br b c ≠ 0
p : K := a.1
q : K := a.2
r : K := b.1
s : K := b.2
u : K := c.1
v : K := c.2
A : K := br a b
B : K := br a c
C : K := br b c
ha1 : p * A + q * B = 0
ha2 : p * B + q * A = 0
hb1 : -r * A + s * C = 0
hb2 : r * C - s * A = 0
hA : A ≠ 0
hpq_mul : (p ^ 2 - q ^ 2) * A = 0
hpq_eq : p ^ 2 = q ^ 2
hb1' : r * A - s * C = 0
hrs_mul : (r ^ 2 - s ^ 2) * A = 0
hrs_eq : r ^ 2 = s ^ 2
hp : p ≠ 0
hq : q ≠ 0
hr : r ≠ 0
hs : s ≠ 0
hpq : p = q
hsr : s = -r
hB : B = -A
hC : C = -A
hsum : r * (u + v) = -A
D1 : Delta c a b = A * (u + v)
D2 : Delta c b a = A * (u + v)
h : A * (u + v) = 0
huv : u + v = 0
⊢ A = 0
K1695/GoodCount3.lean:174:39: error: Type mismatch: After simplification, term
  ha1
 has type
  p * A + -(p * B) = 0
but is expected to have type
  p * A - p * B = 0
K1695/GoodCount3.lean:193:14: warning: Possibly looping simp theorem: `Delta.eq_1`

Note: Possibly caused by: `br_antisymm`

Hint: You can disable a simp theorem from the default simp set by passing `- theoremName` to `simp`.
K1695/GoodCount3.lean:193:21: warning: Possibly looping simp theorem: `br_antisymm`

Hint: You can disable a simp theorem from the default simp set by passing `- theoremName` to `simp`.
K1695/GoodCount3.lean:193:8: error: Tactic `simp` failed with a nested error:
maximum recursion depth has been reached
use `set_option maxRecDepth <num>` to increase limit
use `set_option diagnostics true` to get diagnostic information
K1695/GoodCount3.lean:196:14: warning: Possibly looping simp theorem: `Delta.eq_1`

Note: Possibly caused by: `br_antisymm`

Hint: You can disable a simp theorem from the default simp set by passing `- theoremName` to `simp`.
K1695/GoodCount3.lean:196:21: warning: Possibly looping simp theorem: `br_antisymm`

Hint: You can disable a simp theorem from the default simp set by passing `- theoremName` to `simp`.
K1695/GoodCount3.lean:196:8: error: Tactic `simp` failed with a nested error:
maximum recursion depth has been reached
use `set_option maxRecDepth <num>` to increase limit
use `set_option diagnostics true` to get diagnostic information
Try this:
  [apply] ring_nf
  
  The `ring` tactic failed to close the goal. Use `ring_nf` to obtain a normal form.
    
  Note that `ring` works primarily in *commutative* rings. If you have a noncommutative ring, abelian group or module, consider using `noncomm_ring`, `abel` or `module` instead.
K1695/GoodCount3.lean:208:22: error: unsolved goals
K : Type u_1
inst✝ : Field K
a b c : K × K
ha : Delta a b c = 0 ∧ Delta a c b = 0
hb : Delta b a c = 0 ∧ Delta b c a = 0
hspan : br a b ≠ 0 ∨ br a c ≠ 0 ∨ br b c ≠ 0
p : K := a.1
q : K := a.2
r : K := b.1
s : K := b.2
u : K := c.1
v : K := c.2
A : K := br a b
B : K := br a c
C : K := br b c
ha1 : p * A + q * B = 0
ha2 : p * B + q * A = 0
hb1 : -r * A + s * C = 0
hb2 : r * C - s * A = 0
hA : A ≠ 0
hpq_mul : (p ^ 2 - q ^ 2) * A = 0
hpq_eq : p ^ 2 = q ^ 2
hb1' : r * A - s * C = 0
hrs_mul : (r ^ 2 - s ^ 2) * A = 0
hrs_eq : r ^ 2 = s ^ 2
hp : p ≠ 0
hq : q ≠ 0
hr : r ≠ 0
hs : s ≠ 0
hqp : q = -p
hsr : s = -r
⊢ a.1 * b.2 - a.2 * b.1 = 0
K1695/GoodCount3.lean:89:38: warning: This simp argument is unused:
  hp0

Hint: Omit it from the simp argument list.
  [apply] simp [B, br, hq0]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
K1695/GoodCount3.lean:89:43: warning: This simp argument is unused:
  hq0

Hint: Omit it from the simp argument list.
  [apply] simp [B, br, hp0]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
K1695/GoodCount3.lean:95:38: warning: This simp argument is unused:
  hr0

Hint: Omit it from the simp argument list.
  [apply] simp [C, br, hs0]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
K1695/GoodCount3.lean:95:43: warning: This simp argument is unused:
  hs0

Hint: Omit it from the simp argument list.
  [apply] simp [C, br, hr0]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
K1695/GoodCount3.lean:115:30: warning: This simp argument is unused:
  hp0

Hint: Omit it from the simp argument list.
  [apply] simp [A, br, hq0]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
K1695/GoodCount3.lean:115:35: warning: This simp argument is unused:
  hq0

Hint: Omit it from the simp argument list.
  [apply] simp [A, br, hp0]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
K1695/GoodCount3.lean:123:30: warning: This simp argument is unused:
  hr0

Hint: Omit it from the simp argument list.
  [apply] simp [A, br, hs0]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
K1695/GoodCount3.lean:123:35: warning: This simp argument is unused:
  hs0

Hint: Omit it from the simp argument list.
  [apply] simp [A, br, hr0]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
K1695/GoodCount3.lean:134:21: warning: This simp argument is unused:
  hpq

Hint: Omit it from the simp argument list.
  [apply] simp [A, br, hrs]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
K1695/GoodCount3.lean:134:26: warning: This simp argument is unused:
  hrs

Hint: Omit it from the simp argument list.
  [apply] simp [A, br, hpq]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
K1695/GoodCount3.lean:209:21: warning: This simp argument is unused:
  hqp

Hint: Omit it from the simp argument list.
  [apply] simp [A, br, hsr]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
K1695/GoodCount3.lean:209:26: warning: This simp argument is unused:
  hsr

Hint: Omit it from the simp argument list.
  [apply] simp [A, br, hqp]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
K1695/GoodCount3.lean:240:31: error: Tactic `simp` failed with a nested error:
maximum recursion depth has been reached
use `set_option maxRecDepth <num>` to increase limit
use `set_option diagnostics true` to get diagnostic information
K1695/GoodCount3.lean:244:31: error: Tactic `simp` failed with a nested error:
maximum recursion depth has been reached
use `set_option maxRecDepth <num>` to increase limit
use `set_option diagnostics true` to get diagnostic information
K1695/GoodCount3.lean:245:31: error: Tactic `simp` failed with a nested error:
maximum recursion depth has been reached
use `set_option maxRecDepth <num>` to increase limit
use `set_option diagnostics true` to get diagnostic information
K1695/GoodCount3.lean:255:15: error: Type mismatch: After simplification, term
  hn.left
 has type
  Not (Delta x2 x0 x1 = 0)
but is expected to have type
  Not (deltaSix x0 x1 x2 4 = 0)
K1695/GoodCount3.lean:255:40: error: Type mismatch: After simplification, term
  hn.right
 has type
  Not (Delta x2 x1 x0 = 0)
but is expected to have type
  Not (deltaSix x0 x1 x2 5 = 0)
K1695/GoodCount3.lean:263:15: error: Type mismatch: After simplification, term
  hn.left
 has type
  Not (Delta x1 x0 x2 = 0)
but is expected to have type
  Not (deltaSix x0 x1 x2 2 = 0)
K1695/GoodCount3.lean:263:40: error: Type mismatch: After simplification, term
  hn.right
 has type
  Not (Delta x1 x2 x0 = 0)
but is expected to have type
  Not (deltaSix x0 x1 x2 3 = 0)
K1695/GoodCount3.lean:271:13: error: Type mismatch: After simplification, term
  hn.left
 has type
  Not (Delta x1 x0 x2 = 0)
but is expected to have type
  Not (deltaSix x0 x1 x2 2 = 0)
K1695/GoodCount3.lean:271:38: error: Type mismatch: After simplification, term
  hn.right
 has type
  Not (Delta x1 x2 x0 = 0)
but is expected to have type
  Not (deltaSix x0 x1 x2 3 = 0)
K1695/GoodCount3.lean:279:11: error: Type mismatch: After simplification, term
  hn.left
 has type
  Not (Delta x0 x1 x2 = 0)
but is expected to have type
  Not (deltaSix x0 x1 x2 0 = 0)
K1695/GoodCount3.lean:279:36: error: Type mismatch: After simplification, term
  hn.right
 has type
  Not (Delta x0 x2 x1 = 0)
but is expected to have type
  Not (deltaSix x0 x1 x2 1 = 0)
K1695/GoodCount3.lean:288:9: error: Type mismatch: After simplification, term
  hn.left
 has type
  Not (Delta x0 x1 x2 = 0)
but is expected to have type
  Not (deltaSix x0 x1 x2 0 = 0)
K1695/GoodCount3.lean:288:34: error: Type mismatch: After simplification, term
  hn.right
 has type
  Not (Delta x0 x2 x1 = 0)
but is expected to have type
  Not (deltaSix x0 x1 x2 1 = 0)
Try this:
  [apply] ring_nf
  
  The `ring` tactic failed to close the goal. Use `ring_nf` to obtain a normal form.
    
  Note that `ring` works primarily in *commutative* rings. If you have a noncommutative ring, abelian group or module, consider using `noncomm_ring`, `abel` or `module` instead.
K1695/GoodCount3.lean:304:62: error: unsolved goals
K : Type u_1
inst✝ : Field K
v w : Fin 3 → K
⊢ det ![![1, 0, 0], v, w] = v 1 * w 2 - v 2 * w 1
K1695/GoodCount3.lean:305:8: warning: This simp argument is unused:
  Matrix.det_fin_three

Hint: Omit it from the simp argument list.
  [apply] simp

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
K1695/GoodCount3.lean:323:6: warning: This simp argument is unused:
  Equiv.refl_apply

Hint: Omit it from the simp argument list.
  [apply] simp [permOfIndex, deltaSix, Equiv.trans_apply, Equiv.swap_apply_def]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
K1695/GoodCount3.lean:329:23: error: Application type mismatch: The argument
  h
has type
  permOfIndex i = permOfIndex j
but is expected to have type
  ?m.13 = ?m.14
in the application
  congr_fun h
K1695/GoodCount3.lean:353:51: error: unsolved goals
K : Type u_1
inst✝ : Field K
A : Matrix (Fin 3) (Fin 3) K
σ : Perm (Fin 3)
B : Matrix (Fin 3) (Fin 3) K := A * Perm.permMatrix K σ
i j : Fin 3
⊢ A i (σ j) = ∑ x, if j = σ x then A i x else 0
K1695/GoodCount3.lean:361:35: error(lean.unknownIdentifier): Unknown constant `Matrix.dotProduct`
K1695/GoodCount3.lean:359:38: error: unsolved goals
K : Type u_1
inst✝ : Field K
A : Matrix (Fin 3) (Fin 3) K
σ : Perm (Fin 3)
B : Matrix (Fin 3) (Fin 3) K := A * Perm.permMatrix K σ
Bentry : ∀ (i j : Fin 3), B i j = A i (σ j)
v : Fin 3 → K := B *ᵥ e1Vec
r : Fin 3
⊢ (vecHead fun j => A r (σ j)) = A r (σ 0)
K1695/GoodCount3.lean:370:42: error(lean.unknownIdentifier): Unknown constant `Matrix.dotProduct`
Try this:
  [apply] ring_nf
  
  The `ring` tactic failed to close the goal. Use `ring_nf` to obtain a normal form.
    
  Note that `ring` works primarily in *commutative* rings. If you have a noncommutative ring, abelian group or module, consider using `noncomm_ring`, `abel` or `module` instead.
K1695/GoodCount3.lean:369:33: error: unsolved goals
K : Type u_1
inst✝ : Field K
A : Matrix (Fin 3) (Fin 3) K
σ : Perm (Fin 3)
B : Matrix (Fin 3) (Fin 3) K := A * Perm.permMatrix K σ
Bentry : ∀ (i j : Fin 3), B i j = A i (σ j)
v : Fin 3 → K := B *ᵥ e1Vec
hv : v = fun r => A r (σ 0)
w : Fin 3 → K := B *ᵥ v
r : Fin 3
⊢ (vecHead fun j => (B * B) r j) = A r (σ 0) * A 0 (σ 0) + A r (σ 1) * A 1 (σ 0) + A r (σ 2) * A 2 (σ 0)
K1695/GoodCount3.lean:375:4: error: Type mismatch: After simplification, term
  det_e1_aux v w
 has type
  det ![![1, 0, 0], v, w] = v 1 * w 2 - v 2 * w 1
but is expected to have type
  det ![![1, 0, 0], B *ᵥ ![1, 0, 0], (B * B) *ᵥ ![1, 0, 0]] = v 1 * w 2 - v 2 * w 1
K1695/GoodCount3.lean:354:54: warning: This simp argument is unused:
  Matrix.of_apply

Hint: Omit it from the simp argument list.
  [apply] simp [B, Matrix.mul_apply, Equiv.Perm.permMatrix, Finset.sum_ite_eq, Finset.sum_ite_eq', mul_ite, one_mul,
    zero_mul, Finset.mem_univ, eq_comm]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
K1695/GoodCount3.lean:355:6: warning: This simp argument is unused:
  Finset.sum_ite_eq

Hint: Omit it from the simp argument list.
  [apply] simp [B, Matrix.mul_apply, Equiv.Perm.permMatrix, Matrix.of_apply, Finset.sum_ite_eq', mul_ite, one_mul,
    zero_mul, Finset.mem_univ, eq_comm]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
K1695/GoodCount3.lean:355:25: warning: This simp argument is unused:
  Finset.sum_ite_eq'

Hint: Omit it from the simp argument list.
  [apply] simp [B, Matrix.mul_apply, Equiv.Perm.permMatrix, Matrix.of_apply, Finset.sum_ite_eq, mul_ite, one_mul,
    zero_mul, Finset.mem_univ, eq_comm]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
K1695/GoodCount3.lean:355:54: warning: This simp argument is unused:
  one_mul

Hint: Omit it from the simp argument list.
  [apply] simp [B, Matrix.mul_apply, Equiv.Perm.permMatrix, Matrix.of_apply, Finset.sum_ite_eq, Finset.sum_ite_eq',
    mul_ite, zero_mul, Finset.mem_univ, eq_comm]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
K1695/GoodCount3.lean:355:63: warning: This simp argument is unused:
  zero_mul

Hint: Omit it from the simp argument list.
  [apply] simp [B, Matrix.mul_apply, Equiv.Perm.permMatrix, Matrix.of_apply, Finset.sum_ite_eq, Finset.sum_ite_eq',
    mul_ite, one_mul, Finset.mem_univ, eq_comm]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
K1695/GoodCount3.lean:356:6: warning: This simp argument is unused:
  Finset.mem_univ

Hint: Omit it from the simp argument list.
  [apply] simp [B, Matrix.mul_apply, Equiv.Perm.permMatrix, Matrix.of_apply, Finset.sum_ite_eq, Finset.sum_ite_eq',
    mul_ite, one_mul, zero_mul, eq_comm]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
K1695/GoodCount3.lean:361:54: warning: This simp argument is unused:
  Fin.sum_univ_three

Hint: Omit it from the simp argument list.
  [apply] simp [v, e1Vec, Matrix.mulVec, Matrix.dotProduct, Bentry]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
K1695/GoodCount3.lean:370:16: warning: This simp argument is unused:
  hv

Hint: Omit it from the simp argument list.
  [apply] simp [w, v, e1Vec, Matrix.mulVec, Matrix.dotProduct, Fin.sum_univ_three, Bentry]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
K1695/GoodCount3.lean:371:6: warning: This simp argument is unused:
  Fin.sum_univ_three

Hint: Omit it from the simp argument list.
  [apply] simp [w, v, hv, e1Vec, Matrix.mulVec, Matrix.dotProduct, Bentry]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
K1695/GoodCount3.lean:371:26: warning: This simp argument is unused:
  Bentry

Hint: Omit it from the simp argument list.
  [apply] simp [w, v, hv, e1Vec, Matrix.mulVec, Matrix.dotProduct, Fin.sum_univ_three]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
K1695/GoodCount3.lean:392:10: error: Tactic `introN` failed: There are no additional binders or `let` bindings in the goal to introduce

K : Type u_1
inst✝ : Field K
A : Matrix (Fin 3) (Fin 3) K
hA : IsUnit A.det
x : Fin 3 → K × K := fun i => (A 1 i, A 2 i)
h :
  ¬(br (A 1 0, A 2 0) (A 1 1, A 2 1) ≠ 0 ∨ br (A 1 0, A 2 0) (A 1 2, A 2 2) ≠ 0 ∨ br (A 1 1, A 2 1) (A 1 2, A 2 2) ≠ 0)
⊢ br (x 0) (x 1) = 0
K1695/GoodCount3.lean:395:10: error: Tactic `introN` failed: There are no additional binders or `let` bindings in the goal to introduce

K : Type u_1
inst✝ : Field K
A : Matrix (Fin 3) (Fin 3) K
hA : IsUnit A.det
x : Fin 3 → K × K := fun i => (A 1 i, A 2 i)
h :
  ¬(br (A 1 0, A 2 0) (A 1 1, A 2 1) ≠ 0 ∨ br (A 1 0, A 2 0) (A 1 2, A 2 2) ≠ 0 ∨ br (A 1 1, A 2 1) (A 1 2, A 2 2) ≠ 0)
h01 : br (x 0) (x 1) = 0
⊢ br (x 0) (x 2) = 0
K1695/GoodCount3.lean:398:10: error: Tactic `introN` failed: There are no additional binders or `let` bindings in the goal to introduce

K : Type u_1
inst✝ : Field K
A : Matrix (Fin 3) (Fin 3) K
hA : IsUnit A.det
x : Fin 3 → K × K := fun i => (A 1 i, A 2 i)
h :
  ¬(br (A 1 0, A 2 0) (A 1 1, A 2 1) ≠ 0 ∨ br (A 1 0, A 2 0) (A 1 2, A 2 2) ≠ 0 ∨ br (A 1 1, A 2 1) (A 1 2, A 2 2) ≠ 0)
h01 : br (x 0) (x 1) = 0
h02 : br (x 0) (x 2) = 0
⊢ br (x 1) (x 2) = 0
K1695/GoodCount3.lean:414:28: warning: Try `simp at hA` instead of `simpa using hA`

Note: This linter can be disabled with `set_option linter.unnecessarySimpa false`
K1695/GoodCount3.lean:387:44: error: unsolved goals
K : Type u_1
inst✝ : Field K
A : Matrix (Fin 3) (Fin 3) K
hA : IsUnit A.det
x : Fin 3 → K × K := fun i => (A 1 i, A 2 i)
h :
  ¬(br (A 1 0, A 2 0) (A 1 1, A 2 1) ≠ 0 ∨ br (A 1 0, A 2 0) (A 1 2, A 2 2) ≠ 0 ∨ br (A 1 1, A 2 1) (A 1 2, A 2 2) ≠ 0)
h01 : br (x 0) (x 1) = 0
h02 : br (x 0) (x 2) = 0
h12 : br (x 1) (x 2) = 0
hdet : A.det = A 0 0 * br (x 1) (x 2) - A 0 1 * br (x 0) (x 2) + A 0 2 * br (x 0) (x 1)
hdet0 : A.det = 0
⊢ False
K1695/GoodCount3.lean:438:6: error: Type mismatch: After simplification, term
  h
 has type
  det
      ![e1Vec, (A * Perm.permMatrix K (permOfIndex i)) *ᵥ e1Vec,
        (A * Perm.permMatrix K (permOfIndex i) * (A * Perm.permMatrix K (permOfIndex i))) *ᵥ e1Vec] =
    Delta (A 1 ((permOfIndex i) 0), A 2 ((permOfIndex i) 0)) (A 1 ((permOfIndex i) 1), A 2 ((permOfIndex i) 1))
      (A 1 ((permOfIndex i) 2), A 2 ((permOfIndex i) 2))
but is expected to have type
  det
      ![e1Vec, (A * Perm.permMatrix K (permOfIndex i)) *ᵥ e1Vec,
        (A * Perm.permMatrix K (permOfIndex i) * (A * Perm.permMatrix K (permOfIndex i))) *ᵥ e1Vec] =
    deltaSix (A 1 0, A 2 0) (A 1 1, A 2 1) (A 1 2, A 2 2) i
K1695/GoodCount3.lean:445:6: error: Type mismatch: After simplification, term
  h
 has type
  det
      ![e1Vec, (A * Perm.permMatrix K (permOfIndex j)) *ᵥ e1Vec,
        (A * Perm.permMatrix K (permOfIndex j) * (A * Perm.permMatrix K (permOfIndex j))) *ᵥ e1Vec] =
    Delta (A 1 ((permOfIndex j) 0), A 2 ((permOfIndex j) 0)) (A 1 ((permOfIndex j) 1), A 2 ((permOfIndex j) 1))
      (A 1 ((permOfIndex j) 2), A 2 ((permOfIndex j) 2))
but is expected to have type
  det
      ![e1Vec, (A * Perm.permMatrix K (permOfIndex j)) *ᵥ e1Vec,
        (A * Perm.permMatrix K (permOfIndex j) * (A * Perm.permMatrix K (permOfIndex j))) *ᵥ e1Vec] =
    deltaSix (A 1 0, A 2 0) (A 1 1, A 2 1) (A 1 2, A 2 2) j
```
