# Repair brief for A114362-c2 proof v2 (to be given to GPT-5.6 Pro web)

You recently reviewed a draft proof of the Ordowski conjecture
  (1 - t(n))/(1 + t(n)) = 2^{-n} + 3^{-n} + 5^{-n} + 7^{-n} + O(11^{-n}),
  t(n) = zeta(2n)/zeta(n)^2,
and found Critical Errors in the explicit small-n constants (your exact
counterexample at n=2: w_3 = 1/5, w_5 = 1/11, w_7 = 7/137). The underlying
mechanism (Euler product -> Mobius/tanh composition y = x_2 ⊕ x_3 ⊕ x_5 ⊕ x_7 ⊕ r
with a ⊕ b = (a+b)/(1+ab)) is sound and numerics support the theorem
(exact check at n=2: t=2/5, y=3/7, y - Σ = 3/7 - 15551/44100 = ... > 0 and
< 11^{-2}; ratios (y-Σ)/11^{-n} observed in [0.77, 0.95] for n = 2..30).

Please now write a COMPLETE corrected proof (v2) of the theorem, fixing all
issues you and the other reviewer raised. Suggested clean structure (adapt
freely if you have better):

1. Euler products for s = n >= 2 real: zeta(n) = Π_p (1-p^{-n})^{-1}
   absolutely convergent; hence t = Π_p (1-x_p)/(1+x_p), x_p = p^{-n}.
   Include the convergence justification.
2. Exact peeling identity: if t = ((1-a)/(1+a)) R then
   (1-t)/(1+t) = a ⊕ (1-R)/(1+R). Iterate for p = 2,3,5,7:
   y = x_2 ⊕ (x_3 ⊕ (x_5 ⊕ (x_7 ⊕ r))), r = (1-R_11)/(1+R_11) >= 0.
3. Upper bound: a ⊕ b <= a + b for a,b >= 0, so y <= x_2+x_3+x_5+x_7+r.
4. Lower bound: a ⊕ b >= (a+b)(1 - ab) for a,b in [0,1); unfold to get
   y >= S + r - (explicit correction), S = x_2+x_3+x_5+x_7.
5. Remainder: 0 <= r <= 1 - R_11 <= 2 Σ_{p>=11} x_p/(1-x_p)-type bound;
   derive an honest explicit bound valid for the range of n you use it in.
6. For the correction terms, track TRUE bounds (do NOT assume w_7 ~ x_7 at
   small n — that was the v1 error). Recommended: prove the final
   inequality |y - S| <= C * 11^{-n} for all n >= n_0 with clean constants
   for a modest n_0 (e.g. n_0 = 4 or 5), and settle the finitely many cases
   n = 2..n_0-1 by exact rational / certified computation: n=2 and n=4 are
   fully exact via t(2) = 2/5, t(4) = 6/7 (from zeta(2),zeta(4),zeta(8)
   closed forms); n = 3 (and 5 if needed) require certified bounds on
   zeta(3), zeta(6) (use rapidly convergent partial sums with integral tail
   bounds and carry exact rational intervals).
7. State the final theorem precisely as a big-O statement with your explicit
   constant, and (optional bonus) the sharper asymptotic
   (y - S)/11^{-n} -> 1.

Requirements: fully self-contained (every constant derived in-text; no
"machine-checked" references), exact rationals only (no decimal
approximations in the proof), all inequality directions explicit, and
define every symbol before use. This will be adversarially re-reviewed by
two other systems, so be rigorous.
