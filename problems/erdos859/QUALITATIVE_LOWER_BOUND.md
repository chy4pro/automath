# Erdős #859 — qualitative lower bound by partial summation

Written by the incoming Codex coordinator, 2026-09-09. This fills the specific unrecorded step identified during handoff. It is a local mathematical derivation from published results, not a claim of priority, a numerical onset, or a Lean certificate. Independent external review remains outstanding.

All logarithms are natural. Write `P(x)` for the number of practical integers at most x, and

    T(x) = sum_{m <= x, m practical} tau(m),
    A(t) = sum_{t < m <= 2t, m practical} 1/m,
    S(t) = sum_{t < m <= 2t, m practical} tau(m)/m.

The pair sum B and the density d_t have the definitions in [LOWER_BOUND.md](LOWER_BOUND.md). The dyadic identities below hold for real t; the density consequence is asserted for integer t.

## 1. Published inputs and the practical-number specialization

Weingartner's [Practical numbers and the distribution of divisors, Theorem 1](https://arxiv.org/pdf/1405.2585), arXiv:1405.2585v3, printed page 1, supplies a positive c with

    P(x) = c*x/log(x) + O(x*log(log(x))/log(x)^2).

Theorem 3 of [The mean number of divisors for rough, dense and practical numbers](https://arxiv.org/pdf/2104.07137), arXiv:2104.07137v2, printed page 5, supplies a positive nu with

    T(x) = nu*x*(log x)^delta + O(x),

where delta is the paper's constant, approximately 0.7136125, with `0 < delta < 1`. This delta is NOT the Erdős–Ford upper-bound exponent.

The preceding paragraph on printed page 4 identifies practical integers with `theta(n) = sigma(n)+1`. Crucially, Theorem 3's upper hypothesis is `theta(n) << n*exp((log n)^a)`, not a unit-coefficient inequality, and it requires `a < (1-delta)/(2-delta) = 0.2226...`. Taking `a = 1/5 = 0.2` satisfies this constraint. Indeed

    max(2,n) <= sigma(n)+1 <= n*(2+log n)
                              << n*exp((log n)^(1/5)).

The harmonic bound follows from `sigma(n)/n = sum_{d|n} 1/d <= 1+log n`. The last comparison holds eventually and its constant absorbs finitely many small n. Thus an absolute multiplicative factor in a bound for theta is allowed; the former concern about a factor 122 not fitting the theorem was caused by miscopying `<<` as `<=`.

The two stated source pages were read directly from the arXiv PDFs during this takeover. Neither input provides the numerical error constants required for a fully explicit onset here: the coefficient `nu` (and the coefficient `c` from Theorem 1) and the onset `t_1` below are unspecified by the source theorems. This route has not had a G2 (prior-literature/priority) check.

## 2. Exact summation identity and the first moment

For a cumulative weighted count `F(x) = sum_{n<=x} a_n`, partial summation gives exactly

    sum_{t<n<=2t} a_n/n
      = F(2t)/(2t) - F(t)/t + integral_t^(2t) F(u)/u^2 du.        (1)

This treats both real endpoints correctly: the lower endpoint is excluded and the upper is included.

Set `L = log t`, `h = log 2`, and use `F=P`. On the whole fixed-ratio interval `[t,2t]`, the error in `P(u)/u` is `O(log L/L^2)`. The endpoint difference of the main term is

    c*(1/(L+h) - 1/L) = O(1/L^2),

and its integral term is

    c*integral_L^(L+h) dv/v = c*h/L + O(1/L^2).

The error integral is `O(log L/L^2)` as well, so

    A(t) = c*h/L + O(log L/L^2).                               (2)

In particular `A(t) ~ c*(log 2)/log t`.

## 3. The previously missing T-to-S step

Apply (1) with `a_n = tau(n)` on practical n and zero elsewhere, so `F=T`. The two endpoint errors and the integrated error are all `O(1)`. The main endpoint difference is

    nu*((L+h)^delta - L^delta) = O(L^(delta-1)) = O(1),

while the main integral is

    nu*integral_L^(L+h) v^delta dv
      = nu*h*L^delta + O(L^(delta-1)).

Consequently

    S(t) = nu*(log 2)*(log t)^delta + O(1),                    (3)

and therefore `S(t) ~ nu*(log 2)*(log t)^delta`.

The factor `log 2` matters. The paper's empirical `nu approximately 0.54` is a cumulative-count coefficient, not the limiting coefficient of `S(t)/(log t)^delta`. The latter would be approximately `0.54*log 2`, if that empirical estimate is used. Neither decimal is needed by the proof, and the short finite table is not evidence that these coefficients coincide.

## 4. Density consequence and its exact scope

The elementary practical-divisor inclusion and Cauchy–Schwarz give `d_t >= A(t)^2/B(t)`. Also `B(t) <= S(t)`: writing

    A_g = sum_{t<m<=2t, m practical, g|m} 1/m,

one has `g*A_g <= 1`, `phi(g) <= g`, and hence

    B(t) = sum_g phi(g)*A_g^2 <= sum_g A_g = S(t).

For sufficiently large integer t, (2) and (3) imply

    d_t >= A(t)^2/S(t)
         = (c^2*(log 2)/nu + o(1)) * (log t)^(-2-delta).        (4)

In particular there exist positive K and t_1 with `d_t >= K*(log t)^(-2-delta)` for every integer `t >= t_1`.

For every fixed `beta > 2+delta`, eventually `K*(log t)^(beta-2-delta) > 1`, giving

    d_t > (log t)^(-beta).

One may take `beta=3`, since delta is below 1. This proves the qualitative asserted logarithmic form from the published inputs. It does not provide a numerical t_1, and it does not justify coefficient 1 at the exact exponent `2+delta`. Any statement of that exact unit-coefficient bound would need additional information.

The effective A4/A5 route is separate: it trades a weaker exponent for named coefficients and a named onset. The original sharp asymptotic question in Erdős (33) remains open. No first-proof or novelty claim is made here.
