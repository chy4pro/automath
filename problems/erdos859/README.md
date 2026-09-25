# Erdős #859 — an explicit upper bound for the density d_t

Result obtained 2026-09-09 by the automath dialogue seat (Claude Opus 5), by reading Erdős's
1970 paper and feeding Ford's 2008 theorem into Erdős's own two-class split.
**Line closed 2026-09-25: subsumed by the literature (Hughes arXiv:2609.25446 for the upper bound; Pollack–Thompson 2013 / Weingartner 2015 give a lower bound of exponent 1, stronger than ours). See [CLOSURE_20260925.md](CLOSURE_20260925.md) and [G2_LITERATURE_20260925.md](G2_LITERATURE_20260925.md). Not published; no priority claim.**
See "Status and honest accounting" and [the current lower-bound status](LOWER_BOUND.md).

## The problem

For `t >= 1` let

    A_t = { n in N : t is a sum of distinct divisors of n }.

`A_t` is closed under taking multiples and every element is a multiple of an element not
exceeding `t!`, so `A_t` has an asymptotic density `d_t` (Erdős 1970, §3, p. 130).

Erdős proved `d_t -> 0` and asserted `1/(log t)^{c_3} < d_t < 1/(log t)^{c_4}` for unspecified
positive constants, and asked (his equation (33)) whether

    d_t = (1 + o(1)) c_3 / (log t)^{c_4}.

erdosproblems.com records this as problem 859. Neither constant is given anywhere in the source.

## Result

Write `delta = 1 - (1 + log log 2)/log 2 = 0.0860713321...` (the Erdős–Ford exponent).

> **Theorem.** There is an absolute constant `C` such that for every integer `t >= 8100`,
>
>     d_t  <=  C (log t)^{-delta} (log log t)^{delta - 3/2},
>
> where `delta - 3/2 = -1.4139286679...`. In particular `d_t <<_eps (log t)^{-delta+eps}` for
> every `eps > 0`.

> **Corollary.** If Erdős's (33) holds, i.e. `d_t = (1+o(1)) c_3 (log t)^{-c_4}` with `c_3 > 0`,
> then necessarily `c_4 > delta`. The inequality is strict, and the strictness is exactly what
> Ford's theorem buys: the weaker bound `d_t = (log t)^{-delta+o(1)}`, which was already
> available to Erdős, rules out `c_4 < delta` but not `c_4 = delta`.

## Proof

Fix `t >= 8100` and set `y = t/(log t)^2`, `z = t`. Split `A_t` by whether `n` has a divisor in
the open interval `(y, z)`.

### Lemma A (class 2, Erdős's argument made explicit)

*The set of `n in A_t` having no divisor in `(t/(log t)^2, t)` has upper density at most
`2/log t + 1/t`.*

Let `n` be such an integer and write `t = d_1 + ... + d_k` with `d_1 > ... > d_k` distinct
divisors of `n`.

- If `d_1 = t` then `t | n`. The set of such `n` has density `1/t`.
- Otherwise every `d_i < t`. Being a divisor of `n` and not lying in `(t/(log t)^2, t)`, each
  satisfies `d_i <= t/(log t)^2`. Since the `d_i` sum to `t`, we get `k >= (log t)^2`. The `d_i`
  are distinct divisors of `n` bounded by `t`, so with `tau_t(n) = #{d | n : d <= t}` we have
  `tau_t(n) >= (log t)^2`.

Now count on average:

    sum_{n <= x} tau_t(n) = sum_{d <= t} floor(x/d) <= x sum_{d <= t} 1/d <= x (1 + log t),

so `#{n <= x : tau_t(n) >= (log t)^2} <= x (1 + log t)/(log t)^2 <= 2x/log t` for `t >= e`.
Adding the density-`1/t` set proves the lemma. (This is exactly Erdős's (31) and (32); the only
thing added here is carrying the constants and handling the `t | n` case separately.) ∎

**Strengthening (referee, 2026-09-09).** The `2/log t` can be replaced by `1/(log t)^2`. Put
`S_y(n) = Σ_{d|n, d<=y} d`. For the non-exceptional `n` above every summand is `<= y`, so
`S_y(n) >= t`; while `Σ_{n<=x} S_y(n) = Σ_{d<=y} d·⌊x/d⌋ <= x⌊y⌋`. Hence the class-2 upper density
is at most `⌊y⌋/t + 1/t <= 1/(log t)^2 + 1/t`. Using the closed endpoint `(y,t]` in Lemma B
(harmless for an upper bound, and it absorbs the multiples of `t`), the combination becomes
`d_t <= eps(y,t) + ⌊y⌋/t <= eps(y,t) + (log t)^{-2}`. This does not change the order of the
theorem — class 1 dominates either way — but it makes the class-2 term negligible rather than
merely subordinate.

### Lemma B (class 1, from Ford)

Let `H(x,y,z)` count `n <= x` with a divisor in `(y,z]`, and `eps(y,z) = lim_x H(x,y,z)/x`,
which exists for each fixed pair (Ford, §1.1). Ford, *The distribution of integers with a
divisor in a given interval*, Ann. of Math. **168** (2008), 367–433, **Theorem 1(v)**: if
`x > 100000`, `100 <= y <= z - 1` and `y <= sqrt(x)`, then with `u` defined by `z = y^{1+u}`,

    H(x,y,z)/x  ≍  u^delta (log(2/u))^{-3/2}        when  2y <= z <= y^2,

with absolute implied constants. Letting `x -> infinity` gives the same bounds for `eps(y,z)`.

For `y = t/(log t)^2` and `z = t` the hypotheses hold whenever `t >= 8100`: the binding
condition is `y >= 100`, i.e. `t >= 100 (log t)^2`, which first holds at `t = 8100` (at
`t = 8100`, `y = 100.01...`); `2y <= z` reduces to `(log t)^2 >= 2`, and `z <= y^2` to
`(log t)^4 <= t`, both far weaker. ∎

### Lemma C (evaluating the Ford term)

With `y = t/(log t)^2`, `z = t`,

    u = log(z/y)/log y = 2 log log t / (log t - 2 log log t),

so `u = (2 log log t / log t)(1 + O(log log t / log t))` and therefore
`u^delta ≍ (log log t / log t)^delta`. Also

    log(2/u) = log( (log t - 2 log log t) / log log t ) = log log t - log log log t + o(1) ≍ log log t.

Hence `u^delta (log(2/u))^{-3/2} ≍ (log t)^{-delta} (log log t)^{delta - 3/2}`. ∎

### Combining

    d_t  <=  eps(y,z) + 2/log t + 1/t  <<  (log t)^{-delta}(log log t)^{delta-3/2} + 2/log t.

The first term dominates, since

    (log t)^{-delta}(log log t)^{delta-3/2} / (1/log t) = (log t)^{1-delta}(log log t)^{delta-3/2} -> infinity

because `1 - delta = 0.9139... > 0`. This proves the Theorem.

For the Corollary, suppose `d_t = (1+o(1)) c_3 (log t)^{-c_4}` with `c_3 > 0`.
If `c_4 < delta`, then `d_t / [(log t)^{-delta}(log log t)^{delta-3/2}] ≍ (log t)^{delta-c_4}(log log t)^{3/2-delta} -> infinity`,
contradicting the Theorem. If `c_4 = delta`, the Theorem gives
`d_t <= C (log t)^{-delta}(log log t)^{-1.4139...} = o((log t)^{-delta})`, contradicting
`d_t ~ c_3 (log t)^{-delta}` with `c_3 > 0`. Hence `c_4 > delta`. ∎

## Numerical verification

`check859.py` verifies: the value of `delta`; that all hypotheses of Ford Theorem 1(v) first
hold at `t = 8100`; that `u^delta (log(2/u))^{-3/2}` and `(log t)^{-delta}(log log t)^{delta-3/2}`
agree up to a bounded factor which decreases toward `2^delta = 1.0614...` (ratio 2.96 at
`log t = 20`, 1.11 at `log t = 10^80`); and that the class-1 term dominates `2/log t` by a
factor tending to infinity.

`empirical_dt.py` is an independent check that the object itself is read correctly: it computes
`|A_t ∩ [1, 200000]|/200000` by subset-sum over the divisors. The first four values come out
exactly right against hand computation — `d_1 = 1`; `d_2 = 1/2` (`A_2` = the evens);
`d_3 = 2/3` (`A_3 = {2 | n} ∪ {3 | n}`, since `3 = 3 = 1+2`); `d_4 = 1/2`
(`A_4 = {4 | n} ∪ {3 | n}`, since `4 = 4 = 1+3`) — which rules out a misreading of the
definition. The empirical densities then fall very slowly (0.34 at `t = 20`, 0.30 at `t = 60`),
as an exponent of `0.086` demands.

## Status and honest accounting

**What is genuinely new here is narrow, and it should be reported that way.**

- **The exponent `delta` was already available to Erdős in 1970.** His own result
  `eps(y,2y) = (log y)^{-delta+o(1)}` covers `(y, y(log t)^2)` after splitting into
  `O(log log t)` dyadic intervals, giving `d_t = (log t)^{-delta+o(1)}` immediately. So naming
  his `c_1` is bibliographic archaeology, not new mathematics. Anyone who traced the reference
  could obtain it from the cited estimates. Whether this combination was previously recorded has not been established.
- **What Ford buys is the removal of the `o(1)`**: the shape
  `(log t)^{-delta}(log log t)^{delta-3/2}` is strictly stronger, and it is what makes the
  Corollary's strict inequality `c_4 > delta` provable. That part could not have been stated
  before 2008.
- **The lower bound is developed separately.** See [LOWER_BOUND.md](LOWER_BOUND.md) and
  [QUALITATIVE_LOWER_BOUND.md](QUALITATIVE_LOWER_BOUND.md). The qualitative partial-summation
  argument is now written. A4's effective fallback gives a candidate exponent `73/25` at a
  named enormous onset; its numerical certificate has been rerun, and the complete effective
  chain has now had a cross-vendor mathematical review (below). The sharp asymptotic question (33) remains open.
- **This is a page of mathematics.** It is not a Zenodo version and not an X thread. It is the
  R0 of an #859 campaign, and the right time to publish is when the lower bound is also
  explicit, or when the method is shown to saturate.
- **Refereed 2026-09-09** by an independent seat (ChatGPT 6 Pro, 20 m 53 s) against a
  self-contained statement of the whole proof, instructed to find the error rather than agree:
  `engine/harvest/erdos859_referee_pro.md`. Verdict: all five checked items CORRECT, no exponent
  or endpoint repair needed. It supplied the Lemma A strengthening above; it confirmed the
  threshold is tight (`8099 - 100(log 8099)^2 = -0.0926 < 0`, while `8100` gives `+0.6852 > 0`);
  and it gave the uniform comparison `2^delta·B(t) <= u^delta (log(2/u))^{-3/2} <= (8·4^delta)·B(t)`
  with `8·4^delta = 9.0138…`, so one valid choice is `C = (8·4^delta)·C_F + 1`. The missing
  multiplication sign was corrected during the Codex takeover; the literal `84^delta` is only 1.46428.
  Two of its
  independently checkable claims were re-verified here and both hold exactly.
- **Still not explicit: Ford's own constant `C_F`**, which his paper does not give numerically.
  An absolute `C` exists; a *numerical* `C` does not follow from the quoted input. Said plainly
  rather than papered over.
- **Correction to how the (33) question was framed.** I had posed it as a dichotomy: either the
  class-1 bound is tight, or the exponent exceeds `delta`. **Those are not exhaustive.** With
  `q_t = dens(A_t | E_t)` one has exactly `d_t = q_t·eps(y,t) + r_t`, `0 <= r_t <= (log t)^{-2}`,
  so `d_t/eps(y,t) = q_t + o(1)`. A third scenario, `q_t ≍ (log log t)^{-delta} -> 0`, gives
  `d_t ≍ (log t)^{-delta}(log log t)^{-3/2}`: same leading exponent, smaller iterated-log factor,
  **and (33) still false**. So `q_t -> 0` does not force a larger exponent; the real question is
  constant loss versus iterated-log loss versus a further power of `log t`.
- **A pointwise counterexample worth keeping** (referee; re-verified here): `t = 8100`,
  `n = 3^8 = 6561` has divisors `243, 729, 2187, 6561` in `(y, t]` and `sigma(n) = 9841 > 8100`,
  yet `8100 = (102010000)_3` carries a digit 2, so it is not a sum of distinct powers of 3. Both
  `E_t => A_t` and `(E_t and S_t(n) >= t) => A_t` fail pointwise. General obstruction: for
  `n = pa` with `p` prime, `p ∤ a`, `p > sigma(a)`, `Sigma(pa) = Sigma(a) + p·Sigma(a)`, so
  representability forces `t mod p ∈ Sigma(a) ⊆ [0, sigma(a)]`.
- **Fixed-length representations cannot carry the tight case**: with `D_t` requiring a divisor in
  `(t/2, t]`, the same Ford input gives `dens(D_t | E_t) ≍ (log log t)^{-delta} -> 0`, so any
  representation using at most `K` summands has conditional probability tending to 0.
- **Refereed 2026-09-25**, for the lower bound: the effective chain (LOWER_BOUND.md) and the
  qualitative Weingartner route (QUALITATIVE_LOWER_BOUND.md) were reviewed by a Claude Opus
  agent, cross-vendor relative to the Astra/Codex producers of those results. No mathematical
  error was found. No Lean formalization exists for either route. The referee did not rerun the
  project's Python scripts (python3 was unavailable in its session); it independently rechecked
  the numerical certificates in Perl, in floating point, not directed rounding. See
  [REFEREE_CLAUDE_20260925.md](REFEREE_CLAUDE_20260925.md). This does not solve Erdős (33) and
  supports no priority claim.

## Sources

- Erdős, *Some Extremal Problems in Combinatorial Number Theory*, Mathematical Essays Dedicated
  to A. J. Macintyre, Ohio Univ. Press (1970), 123–133, §3 p. 130.
  `https://users.renyi.hu/~p_erdos/1970-21.pdf`
- Ford, *The distribution of integers with a divisor in a given interval*, Ann. of Math. 168
  (2008), 367–433. `https://www.ford126.web.illinois.edu/wwwpapers/hxyz.pdf`
- Problem page: `https://www.erdosproblems.com/859`
