# Erdős #859, Missing Lemma (B) — is the lcm second moment of practical numbers bounded?

STATUS: **WRITTEN AND HELD. NOT DISPATCHED.** Astra pool resets 21:38 on 14 Sep.
This is a single self-contained inequality. It does not depend on the rest of the campaign.

**SINGLE AGENT. Do not spawn sub-agents.**

## The question

An integer `m >= 1` is **practical** if every integer in `[1, m]` is a sum of distinct divisors
of `m`. Equivalently (Stewart), writing `m = p_1^{e_1}···p_k^{e_k}` with `p_1 < ··· < p_k`,
`m` is practical iff `p_j <= 1 + σ(p_1^{e_1}···p_{j-1}^{e_{j-1}})` for every `j`.

For `t >= 2` put `P(t) = {m practical : t < m <= 2t}` and

    B(t) = Σ_{m, m' ∈ P(t)} 1 / lcm(m, m').

**Prove: `B(t) <= K log log t` for an explicit absolute `K` and all `t >= t_0`.**

`B(t) = O(1)` would be stronger and is also welcome, but **the evidence says `B` is probably
unbounded**: it rises monotonically 0.469 → 0.584 over `t = 10^3 … 5·10^5` and the fit
`B ≈ 0.123 + 0.179 log log t` has residuals under 0.005 across that whole range. So aim at
`log log t`, which suffices for the application. Anything growing faster than `log log t` is also
a real answer — report it as such, with a construction, not a failed proof.

## Why it is worth doing

It is the last gap in an explicit lower bound for Erdős problem #859 (the density `d_t` of
`{n : t is a sum of distinct divisors of n}`). The chain, all of it already in place:

1. **Proved** (`problems/erdos859/LOWER_BOUND.md`, Lemma L1): `m` practical, `m | n`,
   `σ(m) >= t` ⟹ `n ∈ A_t`. Two lines. Verified on 56034 triples, zero counterexamples.
2. **Published input** (Weingartner, Quart. J. Math. 66 (2015) 743–758, Theorem 1, verbatim):
   "There is a positive constant `c` such that for `x >= 3`, `P(x) = c x/log x (1 + O(log log x/log x))`."
   Hence `A(t) := Σ_{m ∈ P(t)} 1/m ≍ 1/log t`.
3. **Cauchy–Schwarz**: with `f(n) = #{m ∈ P(t) : m | n}`, `d_t >= density(f >= 1) >= A²/B`.
4. **This lemma**: `B = O(1)` ⟹ `d_t >> 1/log²t`, i.e. **`c_2 = 2`, the first proof of Erdős's
   1970 assertion `d_t > 1/(log t)^{c_2}`**, which he stated with no proof at all.

## What has already been tried and eliminated — do not redo this

A solo attempt on 2026-09-09 (`problems/erdos859/LOWER_BOUND.md` §4c) ruled out two routes:

- **The model `h(g) = λ(g)·log t/log(t/g)` with a `t`-free `λ` is FALSE.** Measured `λ` grows with
  `t` at every fixed `g` (`g = 240`: 3.62, 4.64, 5.01 at `t = 1.6·10⁴, 6.4·10⁴, 2.56·10⁵`).
- **A uniform bound `A_g <= (A/g)·H` with `H = o(log t)` is IMPOSSIBLE.** `max_g h(g)` is attained
  at `g ≈ t`: the argmax measures 2010, 4004, 8004, 16008, 32010, 64020, 128010, 256014 for
  `t = 2·10³ … 2.56·10⁵`. There `g` is itself a single practical `m ∈ (t,2t]`, `A_g = 1/m`, and so
  `h(g) = 1/A ≈ 1.2 log t` exactly. Do not spend time looking for a uniform `H = o(log t)`.
  (A tempting fit `max h ≈ 2.6√(log t)` from mid-range `g` is wrong — it misses the true argmax.)
- **The elementary two-way split gives only `B ≪ log t`**: `A_g <= A` for `g <= G` and
  `A_g <= (log 2)/g + 1/t` for `g > G` yields `B ≲ 0.304 A²G² + 0.29 log(2t/G)`, optimised at
  `G ≈ (log t)^{3/2}` to `B ≪ 0.5 log t`. Short of the target by `log t/log log t`, and the loss
  is structural: `Σ_{g>G} φ(g)/g² ≍ log(2t/G)` only drops to `O(log log t)` when `G` is within
  `(log t)^{O(1)}` of `t`, and then the first term explodes.

**Invariant any candidate argument must reproduce:** `B/A² = Σ_g φ(g) h(g)²/g²` measures
0.792, 0.791, 0.817 times `log²t` at `t = 1.6·10⁴, 6.4·10⁴, 2.56·10⁵` — very stable.

## What is already known about B, numerically

Measured in `problems/erdos859/lower_probe3.py` and `lower_probe5.py` (all practicals sieved to
4·10^5):

| t | 10³ | 4·10³ | 1.6·10⁴ | 6.4·10⁴ | 1.28·10⁵ | 2.56·10⁵ | 5.12·10⁵ |
|---|---|---|---|---|---|---|---|
| B(t) | 0.469 | 0.477 | 0.516 | 0.551 | 0.561 | 0.571 | 0.584 |

(from `lemmaB_probe.py`, which computes `B` through the divisors of each practical rather than
pairwise gcds and so reaches `t = 5·10^5`.)

Write `B = Σ_g φ(g) A_g²` with `A_g = Σ_{m ∈ P(t), g | m} 1/m` (from `gcd(m,m') = Σ_{g|m, g|m'} φ(g)`).
**The `g`-profile is flat — no `g` dominates.** At `t = 5·10⁴` the largest single term is `g = 4`
at 1.3 % of `B`, and the mass by scale is: `g ∈ [1,10]` 8.6 %, `[11,100]` 20.5 %, `[101,10³]`
28.6 %, `[10³,10⁴]` 26.0 %, `> 10⁴` 16.3 %. As `t` grows the mass moves outward (the `> 10⁴` band
is 0 % at `t = 5000`, 9.9 % at `t = 2·10⁴`, 16.3 % at `t = 5·10⁴`). So each new scale of `g`
contributes a roughly constant amount, and any proof must handle **all** scales uniformly; there
is no main term to isolate.

Two facts that rule out the obvious attempts:

- The elementary bound `A_g <= (log 2)/g + 1/t` gives only `B ≲ log t` — off by `log²t`. It is
  nearly tight *per g* at large `g` (crude/`A_g` = 1.02 at `g = 240`, 1.04 at `g = 720`) but
  hopeless in aggregate, because it ignores that practicals have density `1/log x`.
- Practicals are far likelier than average to be divisible by a highly composite `g`: measured
  `A_g · g / A` climbs from 1.00 at `g = 1` to 8.59 at `g = 720`. Roughly `≍ (σ(g)/g)²`, but that
  fit was not tested past `g = 720` and should not be trusted as an ansatz.

About 23.5 % of all `g <= 2t` divide at least one member of `P(t)` (23505 of 10⁵ at `t = 5·10⁴`),
so "most `g` contribute nothing" is false and cannot be used.

## Rules

- Every constant explicit. No `O(·)` and no unnamed absolute constant survives into the answer.
- Any finite computation must be emitted as a runnable script with its output and the arithmetic
  used, and must agree with the measured table above where they overlap. A check that cannot fail
  counts as no check.
- If you reduce `B = O(1)` to a statement about practical numbers in divisibility classes, say so
  and give that statement precisely — a clean reduction is a real result here. Note that
  Weingartner's two relevant papers (arXiv:1405.2585, arXiv:1605.05204) contain **no** count of
  practical or dense-divisor integers in an arithmetic progression or divisibility class; that
  was checked directly, so do not assume such a count is available off the shelf.
- Do not report the disproof direction casually: `B → ∞` needs a construction, not a failed proof.

## Materials

- `problems/erdos859/LOWER_BOUND.md` — the whole chain, with the honest accounting.
- `problems/erdos859/lower_probe3.py`, `lower_probe5.py` — the measured `B`, `B/A` and `g`-profile.
- `problems/erdos859/lower_probe.py` — practical-number sieve and the Lemma L1 verification.
