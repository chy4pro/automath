# Erdős #859 — an EXPLICIT lower bound for A(t). This is the last blocker.

**SINGLE AGENT. Do not spawn sub-agents.** No time limit. Every constant explicit.

## The one thing to prove

`m` is **practical** if every integer in `[1,m]` is a sum of distinct divisors of `m`; equivalently
(Stewart) `m = p_1^{e_1}···p_k^{e_k}`, `p_1 < ··· < p_k`, is practical iff
`p_j <= 1 + sigma(p_1^{e_1}···p_{j-1}^{e_{j-1}})` for all `j`. Put `P(t) = {m practical : t < m <= 2t}`.

> **Prove: there are explicit `c_1 > 0` and `t_0` such that
> `A(t) := sum_{m in P(t)} 1/m >= c_1 / log t` for all `t >= t_0`.**

Both `c_1` and `t_0` must be actual numbers. A small `c_1` is fine; an unnamed one is not.

## Why this is worth a run

It is the last missing item in a chain that otherwise proves a statement Erdős asserted in 1970
without proof. The rest is already done and verified:

1. If `m` is practical, `m | n` and `sigma(m) >= t`, then `t` is a sum of distinct divisors of `n`.
   (Two lines. Verified on 56034 triples.)
2. With `f(n) = #{m in P(t) : m | n}`, Cauchy–Schwarz gives
   `d_t >= density(f >= 1) >= A(t)^2 / B(t)`, where
   `B(t) = sum over ordered pairs m, m' in P(t) of 1/lcm(m,m')` and `d_t` is the density of
   `{n : t is a sum of distinct divisors of n}` — Erdős problem 859.
3. **Proved and verified 2026-09-09:** `B(t) <= 20 000 000 000 (log t)^theta` for every real
   `t >= 2`, with `theta = 1 + log(3349/4000)/log 5 = 0.8896306804161379…`.
   (`engine/harvest/erdos859_lemmaBprime_astra.md`.)

So `A(t) >= c_1/log t` would give `d_t >= c_1^2 / (2·10^10 (log t)^{2+theta})`, i.e.
`d_t > (log t)^{-c_2}` for an explicit `c_2` slightly above `2.8896…` and an explicit `t_0` — the
first proof of Erdős's assertion `d_t > 1/(log t)^{c_2}` (Erdős, Math. Essays Dedicated to
A. J. Macintyre (1970), 123–133, §3 p. 130, where the entire proof given is the words
"We can prove that").

## What is known, and what is NOT available off the shelf

- Weingartner, Quart. J. Math. **66** (2015) 743–758, Theorem 1: `P(x) = c x/log x (1 + O(log log x/log x))`
  with `c = 1.33607…`. This gives the right ORDER but **its error constant is not explicit**, so it
  cannot be used directly here.
- Saias, *Entiers à diviseurs denses I*, J. Number Theory **62** (1997) 163–191, proves Chebyshev-type
  bounds `c_1 x log z/log x <= D(x,z) <= c_2 x log z/log x` by sieve methods. The constants are
  effective in principle; **I could not find them written numerically anywhere I could reach**.
  Extracting an explicit `c_1` from that argument is a legitimate and probably the shortest route.
- Weingartner's Theorem 2 (same 2015 paper) is the general machinery behind Theorem 1 and may be
  easier to make effective than the asymptotic itself.

**Do not assume any count of practical numbers in an arithmetic progression or divisibility class
is available** — arXiv:1405.2585 and arXiv:1605.05204 were checked directly and contain none.

## Elementary routes already ruled out — do not spend time on them

- `{2^a k : k <= 2^{a+1}}` consists of practical numbers (Stewart: every prime factor of `k` is
  `<= 2^{a+1} = 1 + sigma(2^a)`). But `m = 2^a k <= 2^{2a+1}` forces `2^a >= sqrt(m/2)`, so this
  family contributes only about `sqrt(t)` elements of `(t,2t]`.
- The same barrier hits `m = 2^a q` with `q` prime, and more generally any fixed-depth recursion
  `m = 2^a q_1 ··· q_k`, which reaches only about `t^{1 - 2^{-k}}` for fixed `k`.
- **A polynomial-count bound is worthless here.** If only `#P(t) >> t^{3/4}` then `A >> t^{-1/4}`
  and `A^2/B >> t^{-1/2}(log t)^{-theta}`, which decays polynomially and is far weaker than any
  `(log t)^{-c}`. Only a count of order `t/log t` is of any use.

So the depth of the recursion has to grow with `t` — that is the content of the published proofs,
and it is why this needs real work rather than a clever family.

## Check against these measured values

`A(t)` measured by exact sieve (`problems/erdos859/lemmaB_probe.py`):

| t | 10³ | 4·10³ | 1.6·10⁴ | 6.4·10⁴ | 2.56·10⁵ | 5.12·10⁵ |
|---|---|---|---|---|---|---|
| A(t) | 0.113442 | 0.093618 | 0.083423 | 0.075433 | 0.067143 | 0.063753 |
| A·log t | 0.7836 | 0.7772 | 0.8091 | 0.8330 | 0.8344 | 0.8375 |

`A·log t` sits near 0.8 and drifts slowly upward toward the predicted `c·log 2 = 0.926`. Any `c_1`
you prove must be below the measured `A·log t` at every `t` in this table, or the proof is wrong.

## Rules

- `c_1` and `t_0` are numbers. No `O(·)`, no "sufficiently large", no unnamed absolute constant.
- If you extract constants from a published sieve argument, reproduce the argument's structure in
  enough detail that a reader can check each constant, and cite the exact statement and page.
- Any finite computation: emit a runnable script and its output, and agree with the table above.
  A check that cannot fail counts as no check.
- If you can only prove `A(t) >= c_1/(log t)^{1+eps}` or `A(t) >= c_1 (log log t)^{-k}/log t`, that
  is still useful — report it, and say exactly what the loss costs in the final `c_2`.
- Write findings incrementally to `engine/harvest/erdos859_explicitA_astra.md`.
