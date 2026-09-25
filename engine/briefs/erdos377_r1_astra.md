# Erdős #377, round 1 — explicit constants for the central-binomial reciprocal sum

STATUS: **WRITTEN AND HELD. NOT DISPATCHED.** Astra pool resets 21:38 on 14 Sep.
Re-run G2 against Croot / Mousavi / Schmidt immediately before sending.

**SINGLE AGENT. Do not spawn sub-agents.** One agent, one workspace, sequential routes.

## The object

For n >= 1 put

    f(n) = sum over primes p <= n with p not dividing C(2n,n) of 1/p.

Erdős, Graham, Ruzsa and Straus (Math. Comp. 29 (1975), 83-92) record the governing fact as
their equation (1), p. 84, and it is the whole reason this problem is tractable by counting:

    p does not divide C(2n,n)  <=>  every digit of n in base p is < p/2.

(Equivalently, adding n + n in base p produces no carry. This is Kummer's theorem.)

The open question, in the authors' words on p. 83, is "we cannot decide if f(n) is unbounded".
**That is not your target.** Your targets are the explicit constants the paper leaves unnamed.

## What the source does and does not contain — read this before planning

Verified by reading the scan page by page (notes/selection/primary_read_0909.md):

- p. 90, equation (7):  `sum over p <= n dividing C(2n,n) of 1/p > c log log n`, introduced by
  "it is not difficult to prove". **No value of c. No proof. Anywhere.**
- Immediately after: "There is no doubt that (7) holds for any `c > 1 - eps`, and this would
  follow, of course, from the boundedness of f(n)." So the authors mark the gap between
  "some c" and "any c < 1" as open. Do not re-derive their remark and report it as a result.
- Theorem 4, p. 89: `#{m <= n^alpha : m does not divide C(2n,n)} = c(alpha) n^alpha + o(n^alpha)`,
  `c(alpha) -> 1` as `alpha -> 0`, with the parenthesis "(In fact, c(alpha) can be explicitly
  calculated.)" — **and it is never calculated in the paper.**
- Theorems 2 and 3 give the mean and second moment of f: `c_0 = sum_{k>=2} (log k)/2^k`, and
  `c_0^2`. These are done; do not redo them.

## Deliverables, each a number or a formula, in priority order

**D1 (primary).** An explicit admissible constant `c > 0` in (7), together with a complete
proof, and hence the first explicit `c' < 1` such that `f(n) <= c' log log n` for all
`n >= n_0`, with `n_0` explicit. Report the triple `(c, c', n_0)`. A bound with an
unquantified "sufficiently large n" is not a deliverable.

**D2.** The explicit `c(alpha)` of Theorem 4, as a closed form or an absolutely convergent
series with an effective truncation error, valid on a stated range of `alpha`. Include a
numerical table at `alpha = 1/2, 1/3, 1/4, 1/5` with rigorous error bars.

**D3 (only if D1 closes early).** Push `c'` down. Every improvement must come with its own
`n_0`. State plainly where the method saturates and why; a proved saturation barrier is worth
as much to us as a better constant, and is a publishable result in its own right.

## Routes, with a budget each

Work them in order. Stop a route the moment its gap metric stalls for two consecutive steps
and record why.

- **R1, digit counting, budget 30%.** Bound from below the density of primes p <= n for which
  n has at least one base-p digit >= p/2.

  **CORRECTION, 2026-09-09 — the version of R1 first written here was wrong, and the seat caught
  it in its first pass.** I had said the range `p > sqrt(n)` "is exactly the star sum" of p. 90 and
  that this sub-case alone might give a usable `c`. Both halves are false. (i) The starred sum on
  p. 90 runs over **all** primes `p <= n` with `n = kp + r`, `p/2 < r < p`, not over `p > sqrt(n)`.
  (ii) By Mertens the whole range `sqrt(n) < p <= n` carries reciprocal mass
  `log log n - log log sqrt(n) -> log 2 = 0.693147...`, a **constant**, so no sub-range above
  `sqrt(n)` can contribute a positive coefficient of `log log n`. Any `c log log n` must come from
  the SMALL primes. Verified independently at n = 1e6 .. 1e100: the mass is 0.693147 to six places
  at every scale.

  So R1 is: work the small-prime range, where the multi-digit structure is the whole content.
  Note also that "two digits" does not reduce to checking the units digit: for
  `sqrt(n) < p <= sqrt(2n)` the leading digit can itself carry, whereas for `p > sqrt(2n)` the
  leading digit `k < p/2` automatically; and every prime in `(2n/3, n]` does force a units-digit
  carry for `n >= 3`.
- **R2, short ranges by Mertens with explicit error, budget 25%.** Combine R1 with explicit
  Mertens estimates (use Rosser-Schoenfeld style explicit forms, cite the exact theorem and
  page) over dyadic ranges `n^{1/(r+1)} < p <= n^{1/r}`, mirroring the paper's own decomposition
  on p. 87. The per-range contribution is what produces `c_0`; you need the same decomposition
  with all constants carried explicitly rather than absorbed into o(1).
- **R3, Theorem 4 constant, budget 25%.** Independent of R1/R2. Compute `c(alpha)`.
- **R4, verification and write-up, budget 20%.**

**Gap metric.** For D1, report after every step the current best pair `(c, n_0)` and the
distance `1 - eps - c` to the value the authors say they believe. For D2, report the width of
the rigorous interval around `c(alpha)` at `alpha = 1/2`.

## Red lines

- Every constant must be traceable to an inequality you have proved, not to a numerical fit.
  If a step needs a computation, emit the computation as a script plus its output, and state
  the interval arithmetic used.
- Explicit means explicit: no `O(.)`, no "sufficiently large", no unnamed absolute constant
  survives into a deliverable. If you cannot make a step effective, say so and stop the route.
- Do not claim (7) for any c you have not proved. Do not restate the authors' belief as a result.
- Small cases must be checked numerically against a direct computation of f(n) from the digit
  criterion, for n up to at least 10^6, before any bound is reported.
- If a route reproduces something already in the 1975 paper, say so and abandon it. The paper
  is in the workspace; read it rather than reconstructing it.

## Verification

Lean formalisation is not required in round 1, but the statements must be written so that they
can be formalised later: fully quantified, no floating hypotheses, constants as explicit
rationals or as named closed forms. Kummer is available in Mathlib. Anything that reaches a
Zenodo version will need the standard stack (Statement.lean importing only Mathlib, plus
FinalCheck.lean freezing the axiom set to [propext, Classical.choice, Quot.sound]).

## Materials in the workspace

- The 1975 paper: `https://users.renyi.hu/~p_erdos/1975-27.pdf` (10 pages, scan, no text
  layer). If your environment lacks poppler, extract the page JPEGs with pure Python: the
  pages are DCTDecode image XObjects, so locating each `/Subtype /Image` dictionary containing
  `DCTDecode` and writing the bytes between `stream` and `endstream` yields readable JPEGs.
  Do not install anything to read it.
- `notes/selection/primary_read_0909.md` — the reading, with page references.
