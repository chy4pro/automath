# Erdős #859 — lower-bound record and current verification status

Started 2026-09-09 by Claude Opus 5; reconciled by the incoming Codex coordinator the same day.
This is a chronological record: early numerical conjectures and superseded targets are historical.

**Closed 2026-09-25:** the G2 check found the exponent-1 lower bound `d_t ≥ c/log t` already in the literature (Pollack–Thompson 2013, Weingartner 2015; Hughes 2026 gives `0.79/log t`), which is stronger than everything below. See [CLOSURE_20260925.md](CLOSURE_20260925.md). The record below is kept as history.

**Current state:** elementary reductions established; the qualitative partial-summation route is
written in [QUALITATIVE_LOWER_BOUND.md](QUALITATIVE_LOWER_BOUND.md). A5 completed same-vendor
review of the effective B bound. A4 completed an effective A fallback at exponent `101/100`, not
the requested exponent 1; Codex reran its independent exact checker successfully. Cross-vendor
mathematical review of the effective chain and the qualitative route was completed 2026-09-25 by
a Claude referee agent, which found no mathematical error; see
[REFEREE_CLAUDE_20260925.md](REFEREE_CLAUDE_20260925.md). It is still not a Lean proof or a
release-cleared result. See §4f and [the takeover review](../../notes/CODEX_TAKEOVER_REVIEW_20260909.md).
Question (33) remains open. No priority claim is made.

Erdős 1970, §3 p. 130, asserts "We can prove that for `t > t_0`, `d_t > 1/(log t)^{c_2}`" and
that sentence is the entire proof — no reference, no sketch, no constant.

## 1. Reduction lemma — PROVED

Recall `A_t = {n : t is a sum of distinct divisors of n}`. Call `m` **practical** if every
integer in `[1, m]` is a sum of distinct divisors of `m`; it is standard (and the numerics below
confirm it) that this forces the stronger statement for every integer in `[1, σ(m)]`.

> **Lemma L1.** If `m` is practical, `m | n`, and `σ(m) >= t`, then `n ∈ A_t`.

*Proof.* `t <= σ(m)` and `m` practical give `t = d_1 + ... + d_k` with the `d_i` distinct
divisors of `m`. Every `d_i` divides `m`, which divides `n`. ∎

Two lines, elementary, and Lean-formalisable as it stands.

**Verified**: `lower_probe.py` tested every triple `(t, m, n)` with `t <= 60`, `m <= 400`
practical with `σ(m) >= t`, and `n = mk <= 200000` — **56034 triples, zero counterexamples**.

So with `F(n) := max{σ(m) : m | n, m practical}` and `S_t := {n : F(n) >= t}` we have
`S_t ⊆ A_t`, and `d_t >= density(S_t)`.

## 2. How strong is this route? Measured: `1/log t`, i.e. `c_2 = 1`

`lower_probe4.py` sieves all 185111 practical numbers up to `2·10^6`, computes `F(n)` for every
`n <= 2·10^6` by propagating `σ(m)` from each practical `m` to its multiples, and reads off
`density(S_t)` for all `t` at once.

| t | density(S_t) | ×log t | ×log²t |
|---|---|---|---|
| 100 | 0.1546 | 0.712 | 3.28 |
| 300 | 0.1289 | 0.735 | 4.19 |
| 1 000 | 0.1018 | 0.704 | 4.86 |
| 3 000 | 0.0924 | 0.740 | 5.93 |
| 10 000 | 0.0922 | 0.850 | 7.82 |
| 30 000 | 0.0917 | 0.946 | 9.75 |

`density(S_t)·log t` sits between 0.70 and 0.95 and is flat; `density(S_t)·log²t` climbs
steadily. (Rows past `t ≈ 10^5` are contaminated by the cutoff `N = 2·10^6`, since `σ(m) >= t`
forces `m ≳ t/log log t` and then only a couple of multiples of `m` fit below `N`.)

**So the practical-divisor route supports `c_2 = 1`, not merely some constant.** It is also not
a lossy detour: at `t = 50 … 800` the family already captures **25–39 %** of `A_t`
(`lower_probe2.py`).

## 3. What can actually be certified: Cauchy–Schwarz gives only `1/log²t`

Take `P = {practical m ∈ (t, 2t]}`, `f(n) = #{m ∈ P : m | n}`. Then
`Σ_{n<=x} f(n) ≈ x·A` and `Σ_{n<=x} f(n)² ≈ x·B` with

    A = Σ_{m∈P} 1/m,        B = Σ_{m,m'∈P} 1/lcm(m,m'),

so `d_t >= density(f >= 1) >= A²/B`. `A ≍ 1/log t` follows from Weingartner's theorem that the
practical numbers have counting function `C x/log x`, `C = 1.33607…` (checked here: `P(x)`
against `Cx/log x` is within 1.5 % at `x = 10^3 … 2·10^5`; and `A·log t` measures 0.78 → 0.84,
rising toward `C log 2 = 0.926`).

But `B/A` is **not** bounded (`lower_probe3.py`):

| t | 200 | 1 000 | 5 000 | 20 000 | 100 000 | 200 000 |
|---|---|---|---|---|---|---|
| B/A | 3.18 | 4.14 | 5.27 | 6.36 | 7.67 | 8.28 |

`B/A ≈ 0.65 log t`, so `A²/B ≈ 1.23/log²t` — which matches the measured `A²/B = 0.008278` at
`t = 2·10^5` against `1.23/log²t = 0.008270`. **Cauchy–Schwarz on this family certifies `c_2 = 2`
at best**, because the family is positively correlated and CS ignores that.

## 4. Where it stalls, precisely

Even `c_2 = 2` is **not** rigorous here, because it needs an upper bound on

    B = Σ_g φ(g) A_g²,      A_g = Σ_{m ∈ P, g | m} 1/m.

The elementary bound `A_g <= (log 2)/g + 1/t` gives `B ≲ Σ_g φ(g)(log 2)²/g² ≍ log t`, which is
off by a factor `log²t` from the measured `B ≈ 0.5`. The bound is nearly tight *per g* at large
`g` (at `t = 20000`, crude/`A_g` is 1.02 at `g = 240` and 1.04 at `g = 720`) yet catastrophic in
aggregate — because it pretends `A_g ≈ (log 2)/g` for **every** `g`, whereas `A_g = 0` for most
`g`: a practical number has a constrained prime structure (Stewart: `p_i <= 1 + σ(p_1^{e_1}…p_{i-1}^{e_{i-1}})`).
The correlation runs the other way too — measured `A_g·g/A` climbs from 1.00 at `g = 1` to 8.59
at `g = 720`, i.e. practicals are far likelier than average to be divisible by a highly composite `g`.

**The missing input is a count of practical numbers divisible by `g`, uniform in `g`.**

### 4a. Weingartner read, 2026-09-09 — the uniformity is NOT there

Both candidate papers were downloaded and read (text extracted from the arXiv PDFs):

- **arXiv:1405.2585**, *Practical numbers and the distribution of divisors*, Quart. J. Math. 66
  (2015) 743–758. **Theorem 1, verbatim:** "There is a positive constant `c` such that for
  `x >= 3`, `P(x) = c x/log x (1 + O(log log x/log x))`." This is exactly the input already used
  for `A`, and it is now confirmed at the source rather than from a summary. The abstract's
  second result is an estimate for the count of integers whose **maximum ratio of consecutive
  divisors** is at most `t`, uniform in `t >= 2` — uniformity in the *density threshold*, not in
  a divisor.
- **arXiv:1605.05204**, *A sieve problem and its application*, Mathematika 63 (2017). It studies
  the general set `B` of `n = p_1^{a_1}···p_k^{a_k}` with `p_{j+1} <= θ(p_1^{a_1}···p_j^{a_j})`,
  proves `B` always has a natural density `1 − L` (Theorem 1) with an explicit error term, gives
  a criterion for that density to be positive or zero (Theorem 2), and shows `B = D` when
  `θ(n)/n` is non-decreasing (Theorem 4), where `D` is the dense-divisor set `d_{j+1} <= θ(d_j)`.

Word counts across both papers: "divisible" 1, "progression" 0, "mod" 0, "coprime" 0,
"uniformly in" 0. **Neither paper counts practical or dense-divisor integers in a divisibility
class or an arithmetic progression.** The needed statement is not in this literature as far as
this read goes, and I am not going to improvise it.

### 4b. But the diagnostic simplifies the gap to one clean sentence

**Historical, refuted target:** §4d disproves both bounded B and `B = O(log log t)`.
The observations below explain the failed proposal; do not redispatch it.

`lower_probe5.py` computes the full `g`-profile of `B = Σ_g φ(g) A_g²`. **No `g` dominates.** At
`t = 50000` the largest single term is `g = 4` at 1.3 % of `B`, and the mass is spread almost
evenly by scale:

| g range | [1,10] | [11,100] | [101,1000] | [1001,10⁴] | >10⁴ |
|---|---|---|---|---|---|
| share of B | 8.6 % | 20.5 % | 28.6 % | 26.0 % | 16.3 % |

and as `t` grows the mass moves outward (the `>10⁴` band is 0 % at `t = 5000`, 9.9 % at
`t = 20000`, 16.3 % at `t = 50000`). Each new scale of `g` contributes a roughly constant amount:
**that is the mechanism behind `B/A ≈ 0.65 log t`.**

The useful consequence: since `A ≍ 1/log t`, the statement `B/A ≍ log t` is the same as
`B ≍ 1`. So the whole gap collapses to a single self-contained question:

> **Missing Lemma (B).** Is `B(t) = Σ_{m,m' practical ∈ (t,2t]} 1/lcm(m,m')` bounded by an
> absolute constant?

Measured: `B` = 0.459, 0.469, 0.487, 0.520, 0.546, 0.558, 0.568 at `t` = 200, 10³, 5·10³,
2·10⁴, 5·10⁴, 10⁵, 2·10⁵ — a 24 % rise while `log t` more than doubles. The inference that B
must be bounded or grow like `log log t` was unjustified and later refuted in §4d.

> **Historical conditional calculation, with false hypotheses:** `B = O(1)` would give
> `d_t >> 1/log²t`; `B = O(log log t)` would leave an extra `log log t` denominator.
> Either would yield coefficient 1 at exponent `2+eps` at an unspecified onset, not necessarily
> at the exact exponent 2. Section 4d rules out both proposed B bounds.

This was the proposed engine target at that time. It is superseded, not a current instruction.

**Note on what it would still not give.** Even `B = O(1)` leaves Cauchy–Schwarz lossy by a full
factor of `log t` against the measured strength of the family (§2: `1/log t`). Getting a rigorous
`c_2 = 1` needs a second-moment replacement that survives the positive correlation — a weighted
Turán argument, or a direct sieve on the union of multiples — not a better bound on `B`.

## 5. A structural cap that IS proved — and what it explains

> **Proposition.** No construction using a single fixed practical core can give a density
> better than `≍ log log t / t`.

*Proof.* Lemma L1 needs `σ(m) >= t`, and the multiples of a fixed `m` have density `1/m`. By
Robin's unconditional bound `σ(m)/m < e^γ log log m + 0.6483/log log m` for `m >= 3`, with
`e^γ = 1.7810724…`, `σ(m) >= t` forces `m > t/(e^γ log log t + o(1))` whenever `m <= t`, and
`m > t` trivially otherwise. Either way `1/m ≲ e^γ log log t / t`. ∎

This is why every "clever single construction" fails, and I checked the obvious ones against it:
a fixed power of two needs `2^{b+1} > t`; `lcm(1..k)` needs `k ≈ √(2t)` and is `e^{√(2t)}`;
`m = 2^a q` with `q` prime is practical only for `q <= 2^{a+1}` (Stewart), forcing `2^a ≳ √t`
and a density `≈ 1/(√t log t)`; a fixed core plus a divisor near `t` needs a divisor in an
interval of multiplicative length `1 + σ(m)/t`, which is short unless `m ≳ t`.

**So the `(log t)^{-c_2}` strength must come from the union over `≈ t/log t` distinct cores** —
from the distribution of practical numbers, not from any single construction.

That is the real finding of this session. It explains why Erdős wrote "We can prove that" and
moved on: for him the lower bound was an application of his own divisor-density technology.
**Both halves of #859 rest on the same body of theory** — the upper bound on `H(x,y,z)`
(Erdős–Ford), the lower bound on the distribution of dense-divisor integers
(Erdős–Tenenbaum–Weingartner). The problem is not two problems; it is one, seen twice.

## 6. Honest accounting

**Historical accounting before §4d–§4f.** The current status is at the top of this file;
in particular the proposed next step below was refuted.

- **Proved here**: Lemma L1, and the single-core cap of §5. Both elementary, both verified.
- **Measured, not proved**: that the route reaches `1/log t` (`c_2 = 1`).
- **Not proved, and I am not claiming it**: any explicit `c_2` whatsoever. Erdős's assertion
  remains, as of this file, unreconstructed.
- **Gap to the upper bound**: even the measured `1/log t` is a long way from
  `(log t)^{-0.0861}(log log t)^{-1.414}`. The truth is somewhere in `[1/log t, (log t)^{-δ}]`
  and neither end is known.
- **Weingartner was read on 2026-09-09 and does not close it** (§4a). The gap is now reduced to
  the single Missing Lemma (B) of §4b, which is a clean self-contained inequality rather than a
  vague appeal to machinery. That is progress on the shape of the problem, not on the bound.
- Superseded next step: Missing Lemma (B) was sent to an engine and refuted. Do not redispatch
  it or infer an exact unit-coefficient exponent 2 from the earlier heuristic.

## 4c. Attack on Missing Lemma (B), 2026-09-09 — not closed, but the target moved

`lemmaB_probe.py` recomputes `B` through `B = Σ_g φ(g) A_g²` using the divisors of each practical
rather than pairwise gcds, which pushes `t` from `2·10^5` to `5·10^5`:

| t | 10³ | 2·10³ | 4·10³ | 8·10³ | 1.6·10⁴ | 3.2·10⁴ | 6.4·10⁴ | 1.28·10⁵ | 2.56·10⁵ | 5.12·10⁵ |
|---|---|---|---|---|---|---|---|---|---|---|
| B | 0.469 | 0.465 | 0.477 | 0.498 | 0.516 | 0.537 | 0.551 | 0.561 | 0.571 | 0.584 |

### The target should be `B ≪ log log t`, not `B = O(1)`

`B` rises monotonically by 24 % across the range, and the fit `B ≈ 0.123 + 0.179 log log t` is
close: predicted vs measured is 0.553/0.551 at `t = 6.4·10⁴`, 0.564/0.561 at `1.28·10⁵`,
0.574/0.571 at `2.56·10⁵` — residuals under 0.005 throughout. A bounded `B` would have to
explain a monotone rise; `log log t` explains it.

**This is good news.** `B ≪ log log t` still gives `d_t ≫ 1/(log²t · log log t)`, hence
`d_t > (log t)^{-2-ε}` for every `ε > 0` and all large `t` — an effective lower bound. No
priority claim; G2 literature check pending. So the lemma to aim at is the weaker and more
plausible one.

### Route (a): one model refuted

The natural model `h(g) = λ(g)·log t/log(t/g)` with a `t`-free `λ` is **false**. Measured `λ(g)`
grows with `t` at every fixed `g` (`g = 240`: 3.62, 4.64, 5.01 at `t = 1.6·10⁴, 6.4·10⁴, 2.56·10⁵`;
`g = 720`: 2.62, 3.74, 4.87). `λ` also rises then falls in `g`, so it is not monotone either.

### Route (b): killed outright

The plan was a uniform bound `A_g ≪ (A/g)·H` with `H = o(log t)`, which would give `B = O(1)`.
**No such bound exists.** `max_g h(g)` is attained at `g ≈ t` — the argmax measures 2010, 4004,
8004, 16008, 32010, 64020, 128010, 256014 for `t` = 2·10³ … 2.56·10⁵, i.e. `g` is a single
practical number `m ∈ (t,2t]` itself. There `A_g = 1/m` and so `h(g) = 1/A` exactly, and `1/A ≈ 1.2 log t`.
So `h` is unbounded of order `log t` and any `H = o(log t)` is refuted.

I had briefly fitted `max h ≈ 2.6√(log t)` from mid-range `g` before computing the true argmax;
that fit was measuring a non-maximal region and is wrong. Recorded so the mistake is not repeated.

### Route (c): elementary split gives only `B ≪ log t`

Using `A_g <= A` for `g <= G` and `A_g <= (log 2)/g + 1/t` for `g > G`:

    B ≲ 0.304·A²G² + 0.29·log(2t/G),

optimised at `G ≈ (log t)^{3/2}`, giving `B ≪ 0.5 log t`. That is a factor `log t/log log t` from
the target. The loss is structural, not arithmetic: the second sum `Σ_{g>G} φ(g)/g² ≍ log(2t/G)`
only becomes `O(log log t)` when `G` is within `(log t)^{O(1)}` of `t`, and then the first sum
explodes.

### Invariant any proof must reproduce

`B/A² = Σ_g φ(g)h(g)²/g² = 0.792, 0.791, 0.817` times `log²t` at `t = 1.6·10⁴, 6.4·10⁴, 2.56·10⁵`.
Remarkably stable, and a useful check on any candidate argument.

### Where it stands

Not closed. Routes (a) and (b) are eliminated, (c) is short by `log t/log log t`, and the target
is now the weaker `B ≪ log log t`. The brief `engine/briefs/erdos859_lemmaB_astra.md` has been
updated with all of this so the next attempt does not redo it.

## 4d. Missing Lemma (B) is FALSE — and the target moves, it does not die

Dispatched to Astra (gpt-6-astra high) 2026-09-09; finished in 10 m 24 s.
Record: `engine/harvest/erdos859_lemmaB_astra.md`, checker
`engine/harvest/erdos859_lemmaB_astra_check.py`. **Independently re-derived and re-verified here**
(`verify_lemmaB_disproof.py`) before being accepted.

> **Theorem (Astra, verified).** `B(t)/(log t)^{2/5} -> infinity.` In particular `B(t)/log log t
> -> infinity`, so no absolute `K` gives `B(t) <= K log log t`. **Missing Lemma (B) is false.**

The chain, all three links checked here:

1. **`B >= S(t)^2 / H_phi(2t)`**, where `S(t) = Σ_{m∈P(t)} tau(m)/m = Σ_g A_g` (each divisor `g`
   of `m` contributes `1/m` to `A_g`) and `H_phi(x) = Σ_{g<=x} 1/phi(g)`. This is weighted
   Cauchy–Schwarz with dual vector `1/sqrt(phi(g))`. It is an affirmative lower bound, not an
   inference from a failed upper bound. Astra also supplies the elementary explicit denominator
   `Σ_{n<=x} 1/phi(n) <= e(1+log x) < 3(1+log x)` via `n/phi(n) = Σ_{d|n} mu(d)^2/phi(d)`.
   *Checked numerically every row: `B/(S^2/H_phi)` = 1.345, 1.358, 1.382, 1.383, 1.396, 1.398,
   1.407, 1.416, 1.427, 1.436 at `t = 10^3 … 5.12·10^5` — always `> 1`, and stable, so the
   inequality is valid and only ~40 % lossy.*
2. **`S(t) ≍ (log t)^{delta_W}` with `delta_W = 0.7136125…`**, from Weingartner,
   *The mean number of divisors for rough, dense and practical numbers*, arXiv:2104.07137v2,
   **Theorem 3**, read verbatim at source here: "`T(x) := Σ_{n∈B(x)} tau(n) = kappa x (log x)^delta
   + O(x)`, where `delta = 0.7136125…`". Weingartner adds "empirical evidence suggests that
   `kappa = 0.54…` in the case of practical numbers". *Checked: `S(t)/(log t)^{0.7136125}` measures
   0.570, 0.551, 0.541, 0.542, 0.540, 0.541, 0.537, 0.533, 0.528, 0.526 — finite diagnostics only.*
   The correct limiting dyadic coefficient is `kappa*log 2`, not kappa itself; see
   [the partial-summation derivation](QUALITATIVE_LOWER_BOUND.md).
3. **`H_phi(2t) ≍ log t`** — standard; measured 14.71 → 26.84 against `1.94·log(2t)`.

Astra's presentation is careful in a way worth recording: it uses only two consequences of
Theorem 3 that carry **no unknown constant** — `T(2x)/T(x) -> 2` and, from `delta_W > 7/10`,
`T(x)/(x(log x)^{7/10}) -> infinity` — so `kappa` and the error constant never enter. Its own
checker reproduces all ten of my `A`, `B`, `S`, `H_phi` values to 9 decimal places and all three
stated invariants, and it explicitly labels the finite table "diagnostics, not evidence proving an
infinite limit."

**Source correction, Codex 2026-09-09:** Theorem 3 actually assumes
`max(2,n) <= theta(n) << n exp((log n)^a)`, with an implied constant. The factor 122 is allowed,
and `a=1/5` already fits the range. The former concern came from transcribing `<<` as `<=`,
not from a mathematical gap. Printed pages 4–5 explicitly identify the practical-number case.

### What this changes

**The Cauchy–Schwarz route survives; only my target was wrong.** `d_t >= A^2/B` needs an *upper*
bound on `B`, and `B` is now known to be at least of order `(log t)^{2·delta_W - 1} =
(log t)^{0.4272…}`. Since the measured ratio `B/(S^2/H_phi) ≈ 1.35–1.44` is nearly constant, the
natural conjecture is that this is the true order. So:

> **New target — Missing Lemma (B′).** Prove `B(t) << (log t)^{2·delta_W - 1 + eps}` for every
> `eps > 0`. With `A ≍ 1/log t` this gives
> `d_t >> (log t)^{-(1 + 2·delta_W) - eps}`. A coefficient-free statement needs additional
> exponent slack and an onset argument; the endpoint exponent is not automatically attained.

This names a concrete correlation target weaker than the refuted exponent-2 proposal.
The finite ratio is diagnostic only. No first-proof or novelty claim has been established.

## 4e. Lemma (B′): an explicit upper bound is PROVED, and with it a route to an explicit c_2

Dispatched to Astra 2026-09-09; finished in 24 m 37 s. Record
`engine/harvest/erdos859_lemmaBprime_astra.md` (26 KB) plus five scripts. Its independent verifier
was run here and passes everything, reproducing all ten of my `A, B, S, H_phi` rows exactly.

> **Theorem (Astra producer; independent OpenAI review; cross-vendor review: REFEREE_CLAUDE_20260925.md, no error found).**
> For every real `t >= 2`,
> `S(t) <= 19,200,096,768 · (log t)^theta`, where
> `theta = 1 + log(3349/4000)/log 5 = 0.8896306804161379…`. Since `B(t) <= S(t)` (§ load-bearing step
> below), this also gives `B(t) <= 19,200,096,768 · (log t)^theta`; the rounded corollary
> `B(t) <= 20,000,000,000 · (log t)^theta` is used elsewhere in this file for convenience.

The target exponent `2·delta_W − 1 = 0.4272…` was **not** reached. But this beats exponent 1 — the
minimum bar, since the elementary split already gave exponent 1 — and it is explicit and uniform
from `t = 2`, with no unnamed constant.

### The load-bearing step is elementary and I checked it

For `y > 0`, `Σ_{y<k<=2y} 1/k <= 1` (at most `⌊y⌋+1` eligible integers, each `>= ⌊y⌋+1`). Applying
it to `m = gk` with `k ∈ (t/g, 2t/g]` gives `g·A_g <= 1`, and since `phi(g) <= g`,

    B = Σ_g phi(g) A_g²  <=  Σ_g (g A_g) A_g  <=  Σ_g A_g  =  S(t).          (2.1)

**`B <= S` on every measured row** (0.469 ≤ 2.266, …, 0.584 ≤ 3.304), and their verifier confirms it
at 509 integer and half-integer `t` in exact rational arithmetic.

### What it buys, and the one thing still missing

`d_t >= A(t)²/B(t)` with `A ≍ 1/log t` gives

    d_t  >>  (log t)^{-(2 + theta)}  =  (log t)^{-2.8896306804…},

This is a big-Omega bound with an unspecified positive coefficient. It yields coefficient 1
at any strictly larger exponent and an unspecified onset, not automatically at `2+theta`.
For qualitative existence the stronger published-moment route is already available; see
[QUALITATIVE_LOWER_BOUND.md](QUALITATIVE_LOWER_BOUND.md). What remained missing here was
numerical effectivity for A, not existence. A4 subsequently supplied the fallback in §4f.

Note also the constant `2·10^10` is astronomically lossy — at `t = 5·10^5` the bound reads
`1.98·10^11` against a measured `B = 0.584`. That is harmless for an asymptotic statement but it
pushes the `t_0` at which the conclusion beats the trivial bound absurdly high.

### Two sharper statements the run left on the table

- **An explicit S bound could give B exponent `delta_W approximately 0.7136125` and raw density
  exponent `2+delta_W`.** Coefficient 1 still needs exponent slack or a coefficient check.
  Weingartner's Theorem 3 gives `S ≍ (log t)^{delta_W}` but states no
  numerical leading coefficient or additive error, which is exactly why the run built the weaker
  self-contained majorant instead. Correct call under the explicit-constant rule.
- **The precise missing correlation estimate**, in the form the run identified: an *aggregate*
  bound on `B/S = Σ_g (A_g/S) phi(g) A_g` at scale `(log t)^{delta_W - 1 + eps}`. This is an average
  with weights `A_g/S`, so it does **not** require the uniform pointwise estimate already ruled out
  in §4c. Its proved input is only `0 <= u_g <= 1`, which loses a factor `(log t)^{1-delta_W}`
  relative to `S²/H_phi`; the finite ratios 1.345 … 1.436 measure that variance but cannot bound it.

It also checked the Erdős–Kac source I suggested — Tenenbaum–Weingartner, arXiv:2211.05819,
Theorem 10.1 — and correctly rejected it: its generating-function estimate is for `|z| = 1` near
`z = 1`, and a Gaussian limit near the mean does not supply the divisor-square moment or the
pairwise divisibility correlation needed here.

## 4f. Effective A fallback delivered; exact exponent 1 remains open

A4 finished after 20m05s. Its report is `engine/harvest/erdos859_explicitA_astra.md`, claiming

    A(t) >= 2^(-4·10^9) · (log t)^(-101/100), for every real t >= 1024.

Codex read the report and reran the independent Fraction-series verifier: exit 0, all 401 rows,
damaged-vector rejection and finite arithmetic checks passed. With §4e (precise constant
19,200,096,768), this gives the combined bound

    d_t >= [2^(-8·10^9)/19,200,096,768] · (log t)^(-2.9096306804…), for integer t >= 1024,

where `101/50+theta = 2.9096306804161379…`. The separate coefficient-free consequence is

    d_t > (log t)^(-73/25), for integer t >= exp(2^(10^12)).

This onset is valid but not tight; `log2 log t > 7.72·10^11` already suffices. Honesty note: the
effective bound above beats the trivial `d_t >= 1/(2t)` (from a power of 2 in `(t,2t]`) only when
`log t > 5.55·10^9`.

**Status:** numerical certificates reproduced and local review recorded; cross-vendor mathematical
review of the effective chain was completed 2026-09-25 (REFEREE_CLAUDE_20260925.md), no
mathematical error found. No Lean proof, release clearance, or priority claim follows from these
tests. The requested `A(t) >= c_1/log t` was not obtained.
The obstruction proved by A4 concerns its fixed-cutoff finite-grid method, not all methods.

## Scripts

`lower_probe.py` (L1 check, practical counts), `lower_probe2.py` (second moment vs true density,
capture fraction), `lower_probe3.py` (B/A growth, the `A_g` loss), `lower_probe4.py` (the `F(n)`
sieve giving the whole `density(S_t)` curve), `lower_probe5.py` (the `g`-profile of `B`), `lemmaB_probe.py` (B to `t = 5·10^5` via the
`A_g` route), `lemmaB_shape.py` (the refuted `λ` model and the `B/A²` invariant),
`lemmaB_maxh.py` (the `argmax = g ≈ t` observation that kills route (b)),
`verify_lemmaB_disproof.py` (independent check of the Astra chain: `B >= S^2/H_phi` row by row,
and `S/(log t)^{0.7136125}` flat).
