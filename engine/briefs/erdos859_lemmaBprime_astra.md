# Erdős #859, Missing Lemma (B′) — an upper bound matching the proved lower bound

**SINGLE AGENT. Do not spawn sub-agents.** No time limit. Every constant explicit.

## The object

`m >= 1` is **practical** if every integer in `[1, m]` is a sum of distinct divisors of `m`;
equivalently (Stewart) `m = p_1^{e_1}···p_k^{e_k}` with `p_1 < ··· < p_k` is practical iff
`p_j <= 1 + sigma(p_1^{e_1}···p_{j-1}^{e_{j-1}})` for every `j`. For `t >= 2` put
`P(t) = {m practical : t < m <= 2t}` and

    B(t) = sum over ordered pairs m, m' in P(t) of 1/lcm(m, m').

Write `delta_W = 0.7136125…` for Weingartner's divisor-moment exponent (see §3).

## The target

> **Prove `B(t) <= C_eps (log t)^{2 delta_W - 1 + eps}` for every `eps > 0`, with `C_eps` explicit.**
> `2 delta_W - 1 = 0.4272250…`.

A clean `B(t) <= C (log t)^{2 delta_W - 1} (log log t)^{O(1)}` is better and also welcome.
Anything of the form `B(t) <= C (log t)^{theta}` with an explicit `theta < 1` is already useful —
report the smallest `theta` you can actually prove, and say plainly where it saturates.

## Why this is the right target, and what it buys

Let `A(t) = sum_{m in P(t)} 1/m` and `f(n) = #{m in P(t) : m | n}`. Then
`sum_{n<=x} f(n) ~ x A` and `sum_{n<=x} f(n)^2 ~ x B`, so by Cauchy–Schwarz the density of
`{n : f(n) >= 1}` is at least `A^2/B`. Every such `n` has a practical divisor `m > t`, hence
`sigma(m) >= m > t`, hence `t` is a sum of distinct divisors of `m` and therefore of `n`. So

    d_t >= A(t)^2 / B(t),

where `d_t` is the density of `{n : t is a sum of distinct divisors of n}` (Erdős problem 859).
By Weingartner's counting theorem for practical numbers (Quart. J. Math. 66 (2015) 743–758,
Theorem 1: `P(x) = c x/log x (1 + O(log log x/log x))`), `A(t)` is of order `1/log t`.

Therefore the target bound gives

    d_t >> (log t)^{-(1 + 2 delta_W) - eps},   1 + 2 delta_W = 2.4272250…

which is an **explicit `c_2`** in Erdős's 1970 assertion `d_t > 1/(log t)^{c_2}` — an assertion for
which the source (Erdős, Math. Essays Dedicated to A. J. Macintyre (1970), 123–133, §3 p. 130)
gives the words "We can prove that" and no proof, no reference and no constant.

## The order is already pinned FROM BELOW — this is not a guess

Proved and verified 2026-09-09 (`engine/harvest/erdos859_lemmaB_astra.md`, re-derived
independently in `problems/erdos859/verify_lemmaB_disproof.py`):

- With `S(t) = sum_{m in P(t)} tau(m)/m = sum_{g} A_g` and `H_phi(x) = sum_{g<=x} 1/phi(g)`,
  weighted Cauchy–Schwarz with dual vector `1/sqrt(phi(g))` gives `B(t) >= S(t)^2 / H_phi(2t)`,
  and elementarily `sum_{n<=x} 1/phi(n) <= e(1 + log x) < 3(1 + log x)`.
- `S(t)` is of order `(log t)^{delta_W}` by Weingartner, *The mean number of divisors for rough,
  dense and practical numbers*, arXiv:2104.07137v2, **Theorem 3**: for `theta(n) = sigma(n)+1`
  (which is exactly the practical-number case), `T(x) := sum_{n in B(x)} tau(n) = kappa x (log x)^delta
  + O(x)` with `delta = 0.7136125…`. He notes empirically `kappa = 0.54…` for practical numbers.
- Hence `B(t) >> (log t)^{2 delta_W - 1}`, and in particular `B(t)/(log t)^{2/5} -> infinity`.

**So `(log t)^{2 delta_W - 1}` is the true lower order. The task is the matching upper bound.**

Evidence that the two really match: the measured ratio `B/(S^2/H_phi)` is

| t | 10³ | 2·10³ | 4·10³ | 8·10³ | 1.6·10⁴ | 3.2·10⁴ | 6.4·10⁴ | 1.28·10⁵ | 2.56·10⁵ | 5.12·10⁵ |
|---|---|---|---|---|---|---|---|---|---|---|
| ratio | 1.345 | 1.358 | 1.382 | 1.383 | 1.396 | 1.398 | 1.407 | 1.416 | 1.427 | 1.436 |

Stable and barely drifting across nearly three decades of `t`. The Cauchy–Schwarz lower bound is
only about 40 % lossy, which is the reason to expect a matching upper bound rather than a gap.

Measured `B(t)` itself, and the companions:

| t | 10³ | 4·10³ | 1.6·10⁴ | 6.4·10⁴ | 2.56·10⁵ | 5.12·10⁵ |
|---|---|---|---|---|---|---|
| A(t) | 0.113442 | 0.093618 | 0.083423 | 0.075433 | 0.067143 | 0.063753 |
| B(t) | 0.46904 | 0.47666 | 0.51641 | 0.55094 | 0.57119 | 0.58412 |
| S(t) | 2.2655 | 2.4499 | 2.7267 | 2.9877 | 3.1939 | 3.3040 |
| H_phi(2t) | 14.713 | 17.407 | 20.101 | 22.796 | 25.490 | 26.837 |
| S/(log t)^{delta_W} | 0.5704 | 0.5414 | 0.5396 | 0.5374 | 0.5281 | 0.5256 |

Reproduce these before trusting anything you derive:
`problems/erdos859/lemmaB_probe.py` and `problems/erdos859/verify_lemmaB_disproof.py`.

## Already ruled out — do not redo

From `engine/briefs/erdos859_lemmaB_astra.md` and `problems/erdos859/LOWER_BOUND.md` §4c:

- The model `h(g) = lambda(g)·log t/log(t/g)` with a `t`-free `lambda` is FALSE (`lambda` grows
  with `t` at every fixed `g`; `g = 240` gives 3.62, 4.64, 5.01 at `t = 1.6·10⁴, 6.4·10⁴, 2.56·10⁵`).
- A uniform bound `A_g <= (A/g)·H` with `H = o(log t)` is IMPOSSIBLE: `max_g h(g)` is attained at
  `g ≈ t`, where `g` is itself a single practical `m in P(t)`, `A_g = 1/m`, and `h(g) = 1/A ≈ 1.2 log t`
  exactly. The argmax measures 2010, 4004, 8004, 16008, 32010, 64020, 128010, 256014 for
  `t = 2·10³ … 2.56·10⁵`.
- The elementary two-way split `A_g <= A` for `g <= G`, `A_g <= (log 2)/g + 1/t` for `g > G` gives
  `B <~ 0.304 A^2 G^2 + 0.29 log(2t/G)`, optimised at `G ≈ (log t)^{3/2}` to `B << 0.5 log t`.
  That is a valid but weak upper bound of exponent 1; the target is exponent `0.4272…`.

Note the last item is an existing, if weak, upper bound. **Beating exponent 1 is the minimum bar.**

## Suggested lines, in order

1. **Mirror the lower-bound argument.** The lower bound came from `sum_g A_g = S(t)` plus a
   dual-vector Cauchy–Schwarz. An upper bound for `sum_g phi(g) A_g^2` should come from a
   *pointwise* bound on `A_g` weighted by something whose `phi`-weighted sum is controlled by
   `S(t)` again. Concretely: `B = sum_{m,m'} gcd(m,m')/(mm')`, and `gcd(m,m') <= sqrt(gcd(m,m')·m)`
   type splittings, or the identity `gcd(m,m') = sum_{d | m, d | m'} phi(d)`, may let you compare
   `B` against `S(t)^2/H_phi` from above with a bounded factor.
2. **Divisor-moment input.** Since `S(t)` is a first divisor moment, `B` is close to a *second*
   divisor-correlation moment. Weingartner's Theorem 3 machinery (or the Tenenbaum–Weingartner
   Erdős–Kac theorem for dense-divisor integers, arXiv:2211.05819) may give the second moment
   `sum_{m in P(t)} tau(m)^2/m` directly; note `B <= sum_{m,m'} ...` can sometimes be dominated by
   a product of first moments plus a diagonal term.
3. **Diagonal versus off-diagonal.** The diagonal `sum_{m in P} 1/m = A ≈ 0.06` is negligible
   against `B ≈ 0.58`, so all the mass is off-diagonal and comes from pairs with large `gcd`.
   Characterise which pairs of practical numbers in a dyadic block share a large factor.

## Rules

- Every constant explicit. No `O(·)`, no "sufficiently large", no unnamed absolute constant
  survives into the final statement.
- Any finite computation must be emitted as a runnable script plus its output, and must agree with
  the measured tables above where they overlap. A check that cannot fail counts as no check.
- If you can only prove a weaker exponent `theta`, that is a real result — state it with its
  constant and say exactly what blocks the improvement.
- Do not assume any count of practical numbers in a divisibility class or arithmetic progression
  is available: Weingartner's arXiv:1405.2585 and arXiv:1605.05204 were checked directly and
  contain no such statement.
- Write findings incrementally to `engine/harvest/erdos859_lemmaBprime_astra.md`.
