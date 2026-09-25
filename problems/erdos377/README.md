# Erdős #377 — round 1: a correction to EGRS 1975, and an honest empty ledger on the main target

Run: Astra (gpt-6-astra high), single agent, 1 h 36 m 30 s, 2026-09-09.
Record: `engine/harvest/erdos377_r1_astra.md` (23 KB) + `engine/harvest/erdos377_r1_astra_data/`.
Refereed by the dialogue seat before anything was written here.

## The problem

`f(n) = Σ_{p ≤ n, p ∤ C(2n,n)} 1/p`. Erdős, Graham, Ruzsa and Straus, *On the prime factors of
(2n choose n)*, Math. Comp. **29** (1975), 83–92, say on p. 83: "The most striking fact is that we
cannot decide if `f(n)` is unbounded." That is erdosproblems.com #377.

## D1 — NOT CLOSED. Reported as empty.

No `(c, c', n_0)` with `c > 0` and `c' < 1` was proved. The positive-`(c, n_0)` ledger is empty,
its reference coefficient is zero, and the gap to the `1−ε` the authors say they believe is the
full `1−ε`. An `R1` sub-case gave `1/(3 log n)` for `n ≥ 10^9`, which is not of the required order.

**The missing input, stated concretely.** An effective pointwise prime-distribution estimate on
growing digit ranges: explicit `β ∈ (0,1)`, `η > 0`, `A ≥ 0`, `N` such that for every `n ≥ N`,

    Σ_{exp((log n)^β) < p ≤ n, p | C(2n,n)} 1/p  ≥  η[M(n) − M(exp((log n)^β))] − A,

where `M` is the Mertens sum. The bracket has leading term `(1−β) log log n`, and explicit Mertens
bounds then convert `(β, η, A, N)` into a D1 triple. Neither the EGRS mean/variance results nor
termwise endpoint estimates supply such parameters.

**D3 — a saturation barrier was proved** for the specified termwise-Mertens endpoint method,
covering every carry level, showing that method gives log-log coefficient zero. It is a barrier
for that method, not an impossibility theorem.

## D2 — the printed statement of EGRS Theorem 4 is FALSE, and the corrected version is closed

> **EGRS 1975, Theorem 4, p. 89, as printed:** for `α < 1`,
> `#{m ≤ n^α : m ∤ C(2n,n)} = c(α) n^α + o(n^α)`, where **`c(α) → 1` as `α → 0`**, followed by
> "(In fact, `c(α)` can be explicitly calculated.)"

**The complement is the wrong way round.** It is the *divisor* constant that tends to 1; the
*nondivisor* constant tends to 0.

**Verified independently here** (`chk377.py` logic: `v_p(C(2n,n)) = (2 s_p(n) − s_p(2n))/(p−1)`,
Legendre; `m | C(2n,n)` iff `v_p(m) ≤ v_p(C)` for all `p`):

| n | α = 1/2 | 1/3 | 1/4 | 1/5 |
|---|---|---|---|---|
| 10⁷ — proportion of `m ≤ n^α` **not** dividing | 0.1619 | 0.0698 | 0.0357 | 0.0400 |
| 10⁷ — proportion **dividing** | 0.8381 | 0.9302 | 0.9643 | 0.9600 |
| 10⁶ — not dividing | 0.2820 | 0.1616 | 0.1290 | 0.1333 |
| 10⁴ — not dividing | 0.1100 | 0.0000 | 0.0000 | 0.0000 |

The nondivisor proportion falls toward 0 as `α → 0`; the divisor proportion rises toward 1. This
is the direction the intuition demands: for small `m` and large `n`, adding `n + n` in base `p`
produces many carries, so small `m` almost always divides `C(2n,n)`.

The numbers fluctuate with `n` because Theorem 4 is an *almost all `n`* statement — which is the
second defect the run flagged: **the printed Theorem 4 does not repeat the "almost all `n`"
qualification** carried by the preceding display (6) on p. 89, and there is in fact no all-`n`
constant at any of the four `α` values tested.

**The corrected statement is closed**, with an explicit convergent series for the almost-all
density, an effective truncation bound, and four certified intervals; the width at `α = 1/2` was
driven from unknown to `7.07069 × 10⁻⁷`. Details, formulas and the interval certificates are in
the harvest record and its `_data/` directory.

## Status

- This is a **correction to a 1975 Math. Comp. paper**, plus an explicit constant where the
  authors wrote "can be explicitly calculated" and did not. It is not a resolution of #377.
- **Not published.** It needs a second referee pass on the corrected density formula before it
  goes anywhere, and the main question (D1) is untouched.
- G2, done by the run and re-checked here: Croot–Mousavi–Schmidt (arXiv:2201.11274, Mathematika 70
  (2024)) and Bloom–Croot (arXiv:2509.02835) concern simultaneous small digits in finitely many
  fixed bases and infinitely many `n`; neither gives the all-`n` reciprocal-prime bound, so no
  priority claim is certified.
- One brief error of mine that the run caught and I verified: I had claimed the range `p > √n`
  "is exactly the starred sum" of p. 90 and might alone give a usable `c`. Both halves false — the
  starred sum is over **all** `p ≤ n`, and `Σ_{√n < p ≤ n} 1/p → log 2 = 0.693147`, a constant, so
  no range above `√n` can carry a `log log n` coefficient. See `engine/briefs/erdos377_r1_astra.md`.
