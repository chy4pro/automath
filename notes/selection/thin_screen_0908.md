# Thin-literature screen for slot 2

Run 2026-09-09 (dialogue automath-b6, orchestrator Claude Opus 5). **No dispatch this tick.**

## Why this screen exists

Two dispatches were dropped on 09-08 (Grimm #375, Tuza #167) and two more candidates
(#128, #23) were rejected before dispatch. The class-level verdict from that day: famous
explicit-constant graph problems are closed to us, because that frontier is flag algebras
and semidefinite programming, which is compute we cannot outbid.

The positive lesson from #708 is the opposite shape. Before we started, the literature held
**no bound on g(n) depending only on n**. That is why 81n -> 12n was still on the table in
2026. So this screen looks for *thin literature with an explicit constant*, not for fame.

## Method

Pool built entirely offline first, then a small batch of page fetches for the criteria that
need page text. erdosproblems.com robots.txt disallows ClaudeBot and several other AI
crawlers while granting `use=reference` to ordinary agents; a 591-page sweep would be
crawling, so the offline stage did the cutting and only 17 pages were fetched, throttled at
1.5 s.

| Stage | Filter | Left |
|---|---|---|
| 0 | all problems in `problems/erdosproblems/data/problems.yaml` | 1216 |
| 1 | status open | 591 |
| 2 | has a Lean file in `problems/formal-conjectures` with a `research open` declaration | 306 |
| 3 | that declaration asserts a numeric bound, and the file defines an extremal quantity | 120 |
| 4 | minus problems the llm-hunter mirror marks completed | 97 |
| 5 | minus VibeMathed hits (138, 390, 394, 450, 522, 942, 959, 996, 1201) | 88 |
| 6 | minus Star Fleet claims (32, 70) and our own past work (700, 770, 1212) | 83 |
| 7 | read all 83 Lean statements, keep the ones shaped like "bound an extremal function" | 14 |
| 8 | page fetch: zero proof claims AND nobody marked "currently working on" | 9 |
| 9 | record's proof combinatorial rather than analytic, sieve, polynomial-method or hot | 4 |

Stage 3's numeric-bound test is a regex on the `@[category research open]` statement, so it
is a recall filter, not a precision one. Stage 7 was done by reading, not by machine.

## Survivors, ranked

### 1. #377 — is the reciprocal sum over primes missing from the central binomial coefficient bounded?

Ask: is there an absolute constant C with `sum over p <= n of [p does not divide C(2n,n)] / p <= C`
for every n?

| criterion | evidence |
|---|---|
| proof claims | 0 |
| currently working on | nobody |
| references | 4, one of which is Guy's problem book |
| explicit constant | the constant C *is* the question |
| record's proof style | elementary; Erdos, Graham, Ruzsa and Straus computed the average and got `f(n) <= c log log n` for an unstated `c < 1` |

Why it fits our machinery: Kummer's theorem turns `p` not dividing `C(2n,n)` into a pure
base-p digit condition, namely that every base-p digit of n is less than p/2. That makes the
object a digit-combinatorial one, computable and certificate-friendly, and Kummer is already
in Mathlib. There are two publishable partial results short of the full conjecture: an
explicit value for the `c < 1` that Erdos, Graham, Ruzsa and Straus left unnamed, and
boundedness restricted to a described class of n.

Adjacent-literature check (the step that Tuza failed): Croot has a 2024 Mathematika paper on
Graham's conjecture about p-divisibility of central binomial coefficients, so the neighbourhood
is alive, but that is a different question and no work on this reciprocal sum surfaced.

### 2. #859 — explicit constants for the density of n representing t as a sum of distinct divisors

Ask: `d_t`, the density of the set of n such that t is a sum of distinct divisors of n, is
conjectured to satisfy `d_t ~ c1 / (log t)^c2`.

| criterion | evidence |
|---|---|
| proof claims | 0 |
| currently working on | nobody |
| references | **1** — Erdos 1970, and nothing else. The thinnest page in the whole screen |
| comments | 0 |
| explicit constant | Erdos proved `1/(log t)^c3 < d_t < 1/(log t)^c4` for **unspecified** `c3, c4` |
| record's proof style | elementary; divisor subset sums |

This is the purest #708 analogue found. A bound of the right shape exists but its constants
were never written down, and in 56 years nobody has come back. Naming `c3` and `c4`
explicitly is exactly the move that produced our #708 result. Searching turned up no
follow-up literature at all.

Risk: the 1970 paper has to be obtained and read, and the constants may fall out routinely
once it is. That was also true of #708 before we started.

### 3. #1084 — the contact-number constants in three dimensions

Erdos claimed `6n - c1 n^(2/3) < f_3(n) < 6n - c2 n^(2/3)`; Bezdek and Reid proved the upper
side with 0.926. Zero proof claims and nobody working on it, but five comments and a live
survey literature in sphere packing. The lower side is a construction problem, which is
computable. Ranked below the first two because the area is competitive.

### 4. #1109 — largest A in {1..N} with A+A squarefree

Konyagin's `loglog N (log N)^2 << f(N) << N^(11/15+o(1))` leaves an explicit exponent to
improve, and the page is thin. The frontier is Konyagin's sieve argument, which is the kind
of analytic machinery we do not beat, so this is a reserve, not a target.

## Rejected, with the reason

Four failed the hard gate at stage 8. Notably the two that looked *best* on shape both failed
it, which is the #128 failure mode caught in time:

- **#160** (colouring {1..n} so every 4-term AP gets three colours) — 2 proof claims, and
  ruizshi is working on it. Its Lean file literally frames the frontier as `better_upper` and
  `better_lower`, so on shape it was the single best fit in the pool.
- **#1063** (least n with all but one of n-i dividing C(n,k)) — 2 proof claims, rickyc working.
- **#302** (largest A with no 1/a = 1/b + 1/c) — 1 claim, three people working.
- **#817** — 1 claim, SamKorsky working. **#872** — 1 claim, 36 comments, several working.

Five more passed the gate but failed the frontier test at stage 9:

- **#961** (longest run of k-smooth consecutive integers) — the record is Ramachandra–Shorey
  and Jutila, which runs on linear forms in logarithms. **This is the Grimm trap exactly**:
  our tools reproduce the elementary range and stop where Gelfond–Baker begins.
- **#945** — the live upper bound is Beker's analytic argument.
- **#1095** — the record is Konyagin's, analytic.
- **#535** — the modern bound comes from Alweiss, Lovett, Wu and Zhang on sunflowers, a hot area.
- **#100** — Guth and Katz's polynomial method already beats the elementary record.

## What this changes about the filter

Add a step: **check proof claims and "currently working on" before reading the mathematics,
not after.** Both top-of-shape candidates died on that gate, and reading them first cost the
better part of this tick.

The stage-9 tally is worth keeping: of nine problems that were genuinely unclaimed and
unattended, five had frontiers built on analytic or algebraic machinery. Unattended and
tractable-for-us are close to independent, so the screen has to test them separately.
