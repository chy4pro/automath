# Batch 1 — Verbatim Lean Definitions

Source directory: `$HOME/workspace/claudecode/automath/problems/formal-conjectures/FormalConjectures/OEIS/`

Apache license header (lines 1-15 of each file) is excluded below; content starts from the first `import` line.

## 113010.lean

```lean
import FormalConjecturesUtil

/-!
# Number of digits of n raised to the power of the sum of the digits of n

*References:*
- [A113010](https://oeis.org/A113010)
-/

namespace OeisA113010

open Nat

/--
a n is the {Number of digits of n} raised to the power of {the sum of the digits of n}.
-/
def a (n : ℕ) : ℕ :=
  ((10).digits n).length ^ (List.sum ((10).digits n))

@[category test, AMS 11]
theorem a_0 : a 0 = 1 := by native_decide

@[category test, AMS 11]
theorem a_1 : a 1 = 1 := by native_decide

@[category test, AMS 11]
theorem a_2 : a 2 = 1 := by native_decide

@[category test, AMS 11]
theorem a_3 : a 3 = 1 := by native_decide

@[category test, AMS 11]
theorem a_4 : a 4 = 1 := by native_decide

/--
$n=1$ and $32$ are two fixed points. Are there any others?
-/
@[category research open, AMS 11]
theorem conjecture : answer(sorry) ↔ ∀ n : ℕ, a n = n ∧ n > 0 → n = 1 ∨ n = 32 := by
  sorry

end OeisA113010
```

## 113019.lean

```lean
import FormalConjecturesUtil

/-!
# Number of digits of n raised to the power of the digital root of n

*References:*
- [A113019](https://oeis.org/A113019)
-/

namespace OeisA113019

open Nat

/--
a n is the (Number of digits of n) raised to the power of (the digital root of n),
with appropriate adjustments for $n=0$.
-/
def a (n : ℕ) : ℕ :=
  -- The base: number of digits of n (adjusting n=0 to have 1 digit, like n=1).
  let numDigits : ℕ := (Nat.digits 10 (max 1 n)).length

  -- The exponent: digital root of n. This correctly yields 0 for n=0,
  -- and the standard 1..9 for n>0.
  let digitalRoot : ℕ := if n = 0 then 0 else (n - 1) % 9 + 1

  numDigits ^ digitalRoot

@[category test, AMS 11]
theorem a_0 : a 0 = 1 := by native_decide

@[category test, AMS 11]
theorem a_1 : a 1 = 1 := by native_decide

@[category test, AMS 11]
theorem a_2 : a 2 = 1 := by native_decide

@[category test, AMS 11]
theorem a_3 : a 3 = 1 := by native_decide

@[category test, AMS 11]
theorem a_4 : a 4 = 1 := by native_decide

/--
$n=1$ and $32$ are fixed points. Are there any others?
-/
@[category research open, AMS 11]
theorem conjecture : answer(sorry) ↔ ∀ n : ℕ, a n = n → n = 1 ∨ n = 32 := by
  sorry

end OeisA113019
```

## 108211.lean

```lean
import FormalConjecturesUtil

/-!
# $a(n) = 16n^2 + 1$

*References:*
- [A108211](https://oeis.org/A108211)
-/

namespace OeisA108211

/--
The primary defining sequence `a`.
`a n` is defined as $16n^2 + 1$.
-/
def a (n : ℕ) : ℕ := 16 * n ^ 2 + 1

/-- Term theorems verifying the first few values of the sequence against the official OEIS b-file -/
@[category test, AMS 11]
theorem a_1 : a 1 = 17 := by decide

@[category test, AMS 11]
theorem a_2 : a 2 = 65 := by decide

@[category test, AMS 11]
theorem a_3 : a 3 = 145 := by decide

@[category test, AMS 11]
theorem a_4 : a 4 = 257 := by decide

@[category test, AMS 11]
theorem a_5 : a 5 = 401 := by decide

open Real

/--
Conjecture:
$$a(n) = \left\lfloor \frac{1}{\frac{1}{4n} - \log(2) +
  \frac{1}{n+1} + \frac{1}{n+2} + \dots + \frac{1}{2n}} \right\rfloor.$$
-/
@[category research open, AMS 11]
theorem conjecture (n : ℕ) (hn : n > 0) :
    (a n : ℝ) =
      (⌊ 1 / ((4 * n : ℝ)⁻¹ - log 2 + ∑ k ∈ (Finset.Icc (n + 1) (2 * n)), (k : ℝ)⁻¹) ⌋ : ℝ) := by
  sorry

end OeisA108211
```

## 114831.lean

```lean
import FormalConjecturesUtil

/-!
# Each term is previous term plus floor of harmonic mean of two previous terms.

$a(1) = 1, a(2) = 2$ and
$a(n) = a(n-1) + \lfloor \frac{2 a(n-1) a(n-2)}{a(n-1) + a(n-2)} \rfloor$ for $n \ge 3$.

*References:*
- [A114831](https://oeis.org/A114831)
-/

namespace OeisA114831

open Filter Real Topology

/--
The primary defining sequence `a`.
Each term is previous term plus floor of harmonic mean of two previous terms.
-/
noncomputable def a : ℕ → ℕ
| 0 => 0 -- Dummy value, sequence starts at index 1
| 1 => 1
| 2 => 2
| n + 3 =>
  let an1 : ℕ := a (n + 2)
  let an2 : ℕ := a (n + 1)
  let num : ℚ := (2 * an1 * an2 : ℕ).cast
  let den : ℚ := (an1 + an2 : ℕ).cast
  let harmonicTermFloor : ℕ := Int.toNat (num / den).floor
  an1 + harmonicTermFloor

@[category test, AMS 11]
theorem a_1 : a 1 = 1 := by norm_num [a]

@[category test, AMS 11]
theorem a_2 : a 2 = 2 := by rw [a]

@[category test, AMS 11]
theorem a_3 : a 3 = 3 := by
  norm_num [a, Rat.floor, Int.toNat]

@[category test, AMS 11]
theorem a_4 : a 4 = 5 := by
  norm_num [a, Rat.floor, Int.toNat]

/--
Conjecture based on OEIS A114831: What is this sequence, asymptotically?
If the limit exists, the ratio of consecutive terms must tend to $\sqrt{3}$:
$$ \lim_{n \to \infty} \frac{a(n+1)}{a(n)} = \sqrt{3}. $$
That's because $a(n)$ is positive, monotonically increasing ($a(n) > a(n-1)$)
and $a(n+2) \geq a(n+1) + a(n)$.
So $a(n)$ grows exponentially, at least as fast as the Fibonnaci numbers.
Assuming $\frac{a(n+1)}{a(n)}$ tend to a limit L, solving for L in the definition of $a(n)$
gives $L=\sqrt{3}$.
-/
@[category research open, AMS 11]
theorem conjecture3 :
    Tendsto (fun n ↦ (a (n + 1) : ℝ) / (a n : ℝ)) atTop (nhds (Real.sqrt 3)) := by
  sorry

end OeisA114831
```

## 100434.lean

```lean
import FormalConjecturesUtil

/-!
# Expansion of g.f. $(1+x)(3+x)/(1+6x^2+x^4)$

This sequence is defined by the linear recurrence relation
$a(n) = -6 a(n-2) - a(n-4)$ for $n \ge 4$,
with initial values $a(0)=3$, $a(1)=4$, $a(2)=-17$, $a(3)=-24$.

*References:*
- [A100434](https://oeis.org/A100434)
-/

namespace OeisA100434

/-- The primary defining sequence `a`, which is the expansion of the generating function
$(1+x)(3+x)/(1+6x^2+x^4)$. It satisfies the recurrence $a(n) = -6 a(n-2) - a(n-4)$
for $n \ge 4$. -/
def a : ℕ → ℤ
  | 0 => 3
  | 1 => 4
  | 2 => -17
  | 3 => -24
  | n + 4 => -6 * a (n + 2) - a n

/-- $c(n)$ starts with $(1, -3, -7, 17)$ and satisfies the same recurrence as `a` -/
def c : ℕ → ℤ
  | 0 => 1
  | 1 => -3
  | 2 => -7
  | 3 => 17
  | n + 4 => -6 * c (n + 2) - c n

/-- $d(n)$ starts with $(2, 4, -10, -24)$ and satisfies the same recurrence as `a` -/
def d : ℕ → ℤ
  | 0 => 2
  | 1 => 4
  | 2 => -10
  | 3 => -24
  | n + 4 => -6 * d (n + 2) - d n

/-- $b(2n) = c(2n+1)$, $b(2n+1) = c(2n)$ -/
def b (n : ℕ) : ℤ :=
  if n % 2 = 0 then c (n + 1)
  else c (n - 1)

/-- $e(2n) = d(2n)/2$, $e(2n+1) = - d(2n)/2$ -/
def e (n : ℕ) : ℤ :=
  if n % 2 = 0 then
    d n / 2
  else
    -- n is positive, so n-1 is safe in ℕ
    - (d (n - 1) / 2)

/-- $f(2n) = f(2n+1) = d(2n+1)/2$ -/
def f (n : ℕ) : ℤ :=
  let m := n / 2
  d (2 * m + 1) / 2

/-- $g(2n) = 0, g(2n+1) = c(2n+1)$ -/
def g (n : ℕ) : ℤ :=
  if n % 2 = 0 then 0
  else c n

/-- Value of the sequence `a` at 0. -/
@[category test, AMS 11]
theorem a_0 : a 0 = 3 := by rfl

/-- Value of the sequence `a` at 1. -/
@[category test, AMS 11]
theorem a_1 : a 1 = 4 := by rfl

/-- Value of the sequence `a` at 2. -/
@[category test, AMS 11]
theorem a_2 : a 2 = -17 := by rfl

/-- Value of the sequence `a` at 3. -/
@[category test, AMS 11]
theorem a_3 : a 3 = -24 := by rfl

/-- Value of the sequence `a` at 4. -/
@[category test, AMS 11]
theorem a_4 : a 4 = 99 := by rfl

/--
For all $n \ge 0$, we have $a(2n) = - c(2n+1)$.
-/
@[category textbook, AMS 11]
theorem a_even (n : ℕ) : a (2 * n) = - c (2 * n + 1) := by
  induction n using Nat.twoStepInduction with
  | zero =>
    rfl
  | one =>
    rfl
  | more k ih1 ih2 =>
    have h_eq : 2 * (k + 2) = 2 * k + 4 := by omega
    have h_eq2 : 2 * (k + 2) + 1 = 2 * k + 5 := by omega
    rw [h_eq2, h_eq]
    have h_lhs : a (2 * k + 4) = -6 * a (2 * k + 2) - a (2 * k) := by rfl
    have h_rhs : c (2 * k + 5) = -6 * c (2 * k + 3) - c (2 * k + 1) := by rfl
    rw [h_lhs, h_rhs]
    have ih2' : a (2 * k + 2) = - c (2 * k + 3) := by
      have h_eq_ih : 2 * (k + 1) = 2 * k + 2 := by omega
      have h_eq2_ih : 2 * (k + 1) + 1 = 2 * k + 3 := by omega
      rw [← h_eq2_ih, ← h_eq_ih]
      exact ih2
    rw [ih1, ih2']
    ring

/--
For all $n \ge 0$, we have $a(2n+1) = d(2n+1)$.
-/
@[category textbook, AMS 11]
theorem a_odd (n : ℕ) : a (2 * n + 1) = d (2 * n + 1) := by
  induction n using Nat.twoStepInduction with
  | zero =>
    rfl
  | one =>
    rfl
  | more k ih1 ih2 =>
    have h_eq : 2 * (k + 2) + 1 = 2 * k + 5 := by omega
    rw [h_eq]
    have h_lhs : a (2 * k + 5) = -6 * a (2 * k + 3) - a (2 * k + 1) := by rfl
    have h_rhs : d (2 * k + 5) = -6 * d (2 * k + 3) - d (2 * k + 1) := by rfl
    rw [h_lhs, h_rhs]
    have ih2' : a (2 * k + 3) = d (2 * k + 3) := by
      have h_eq_ih : 2 * (k + 1) + 1 = 2 * k + 3 := by omega
      rw [← h_eq_ih]
      exact ih2
    rw [ih1, ih2']

/--
**Conjecture from Creighton Dement (A100434)**:
Let the auxiliary sequences c, d, e, f, g, b be defined as specified.
Then for all $n \ge 0$, $c(n) + d(n) = b(n)$.
-/
@[category research open, AMS 11]
theorem conjecture1 (n : ℕ) : c n + d n = b n := by
  sorry

/--
**Conjecture from Creighton Dement (A100434)**:
Let the auxiliary sequences c, d, e, f, g, b be defined as specified.
Then for all $n \ge 0$, $e(n) + f(n) = b(n)$.
-/
@[category research open, AMS 11]
theorem conjecture2 (n : ℕ) : e n + f n = b n := by
  sorry

/--
**Conjecture from Creighton Dement (A100434)**:
Let the auxiliary sequences c, d, e, f, g, b be defined as specified.
Then for all $n \ge 0$, $g(n) + a(n) = b(n)$.
-/
@[category research open, AMS 11]
theorem conjecture3 (n : ℕ) : g n + a n = b n := by
  sorry

end OeisA100434
```

## 109074.lean

```lean
import FormalConjecturesUtil

/-!
# Numerator of $\binom{6n-2}{2n} / \left(2 \binom{4n-1}{2n}\right)$

Conjecture: $\binom{6n-2}{2n} / \left(2 \binom{4n-1}{2n}\right) = A005156(n+1)/A005156(n)$

*References:*
- [A109074](https://oeis.org/A109074)
-/

namespace OeisA109074

open Nat

/--
The rational number defined by $\binom{6n-2}{2n} / \left(2 \binom{4n-1}{2n}\right)$,
whose numerator is A109074.
-/
def frac (n : ℕ) : ℚ :=
  let numTerm : ℕ := (6 * n - 2).choose (2 * n)
  let denTerm : ℕ := 2 * ((4 * n - 1).choose (2 * n))
  (numTerm : ℚ) / (denTerm : ℚ)

/--
The primary defining sequence `a`.
$a(n)$ is the numerator of $\binom{6n-2}{2n} / \left(2 \binom{4n-1}{2n}\right)$.
-/
def a (n : ℕ) : ℕ :=
  (frac n).num.natAbs

@[category test, AMS 11]
theorem a_0 : a 0 = 1 := by native_decide

@[category test, AMS 11]
theorem a_1 : a 1 = 1 := by native_decide

@[category test, AMS 11]
theorem a_2 : a 2 = 3 := by native_decide

@[category test, AMS 11]
theorem a_3 : a 3 = 26 := by native_decide

@[category test, AMS 11]
theorem a_4 : a 4 = 323 := by native_decide

/--
A005156: The sequence of values $\frac{1}{2n+1} \binom{3n}{n}$.
-/
def b (n : ℕ) : ℕ :=
  let num : ℕ := (3 * n).choose n
  let den : ℕ := 2 * n + 1
  num / den

/--
It is conjectured that binomial(6*n-2,2*n)/(2 * binomial(4*n-1,2*n)) = A005156(n+1)/A005156(n).
-/
@[category research open, AMS 11]
theorem conjecture (n : ℕ) (h_pos : n ≥ 1) :
    frac n = (b (n + 1) : ℚ) / (b n : ℚ) := by
  sorry

end OeisA109074
```

## 114362.lean

```lean
import FormalConjecturesUtil

/-!
# Numerator of $\zeta(4n)/\zeta(2n)^2$ (with $a(0)=2$ instead of $-2$)

The ratio $\zeta(4n)/\zeta(2n)^2$ for $n \ge 1$ is the rational number
$$ Q_n = -2 \frac{B_{4n}}{B_{2n}^2 \binom{4n}{2n}} $$
where $B_k$ is the $k$-th Bernoulli number. The sequence $a(n)$ is the numerator of $Q_n$,
with $a(0)$ defined as $2$.

*References:*
- [A114362](https://oeis.org/A114362)
-/

namespace OeisA114362

open scoped Nat Real
open Filter
open Complex

/--
The primary defining sequence `a`.
Numerator of $\zeta(4n)/\zeta(2n)^2$ (with $a(0)=2$ instead of $-2$).
-/
noncomputable def a (n : ℕ) : ℕ :=
  if n = 0 then
    2
  else
    let b4n : ℚ := bernoulli (4 * n)
    let b2n : ℚ := bernoulli (2 * n)
    let binomQn : ℚ := ↑(Nat.choose (4 * n) (2 * n))
    let qN : ℚ := -2 * b4n / (b2n * b2n * binomQn)
    qN.num.natAbs

@[category test, AMS 11]
theorem a_0 : a 0 = 2 := by
  congr

@[category test, AMS 11]
theorem a_1 : a 1 = 2 := by
  simp_all [a]
  norm_num only [bernoulli_eq_bernoulli'_of_ne_one, bernoulli'_four, bernoulli'_two, Nat.choose]

@[category test, AMS 11]
theorem a_2 : a 2 = 6 := by
  delta a
  norm_num +decide
    [bernoulli_eq_bernoulli'_of_ne_one, bernoulli'_eq_zero_of_odd, Int.natAbs_eq_iff, Nat.choose]
  rw [bernoulli'_def]
  have α := sum_bernoulli'
  norm_num only
    [←eq_sub_of_add_eq' (α _ ▸ Finset.sum_range_succ _ _).symm ▸ mul_div_cancel_left₀ _,
      Finset.sum_range_succ, or_false, or_true, Nat.choose]

@[category test, AMS 11]
theorem a_3 : a 3 = 691 := by
  delta and a
  norm_num [bernoulli_eq_bernoulli'_of_ne_one, two_mul, Nat.cast_choose]
  rw [bernoulli'_def, bernoulli'_def]
  have := sum_bernoulli'
  have R M := this (M+1) ▸ Finset.sum_range_succ _ _
  norm_num only
    [Nat.choose, ←sub_eq_of_eq_add' (R _) ▸ mul_div_cancel_left₀ _, Finset.sum_range_succ]

/--
Conjecture: if an integer $n > 1$ is odd, then $\zeta(2n)/\zeta(n)^2$ is irrational.
Cf. W. Kohnen (link) and my conjecture in A348829. - Thomas Ordowski, Jan 05 2022
-/
@[category research open, AMS 11]
theorem conjecture1 (n : ℕ) (hn_gt_one : 1 < n) (hn_odd : Odd n) :
    Irrational ((riemannZeta (2 * n : ℂ) / (riemannZeta (n : ℂ)) ^ 2).re) := by
  sorry

/-- `t n` is used in the second conjecture. -/
noncomputable def t (n : ℕ) : ℝ :=
  (riemannZeta (2 * (n : ℂ))).re / ((riemannZeta (n : ℂ)).re ^ 2)

/--
Conjecture:
$\frac{1 - t(n)}{1 + t(n)} = \frac{1}{2^n} + \frac{1}{3^n} + \frac{1}{5^n} + \frac{1}{7^n} +
  O(\frac{1}{11^n})$,
where $t(n) = \zeta(2n)/\zeta(n)^2$. Cf. A348829. - Thomas Ordowski, Nov 13 2022
-/
@[category research open, AMS 11]
theorem conjecture2 :
    (fun n : ℕ => (1 - t n) / (1 + t n) -
      (1 / (2:ℝ)^n + 1 / (3:ℝ)^n + 1 / (5:ℝ)^n + 1 / (7:ℝ)^n))
      =O[atTop] (fun n : ℕ => 1 / (11:ℝ)^n) := by
  sorry

end OeisA114362
```
