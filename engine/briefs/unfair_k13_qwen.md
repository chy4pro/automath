# ATTACK BRIEF — UNFAIR 0-1 POLYNOMIAL, TRINOMIAL k = 13 SLICE (LLM-first)
Step 0 (G2): state status as you know it + solved-after-cutoff risk (recent work resolved k = 5,7,9,11
and all sufficiently large odd k; k = 13 is reported as the first natural remaining gap). Attack regardless.
SETTING: "unfair 0-1 polynomial" problem — for a polynomial P(t) = sum a_i t^i with a_i in {0,1}
(here the TRINOMIAL case: exactly three nonzero coefficients, so P(t) = 1 + t^b + t^c up to
normalisation), consider the coefficient sequence of P(t)^k / (or the k-fold convolution of the
0-1 coefficient vector) and the question of whether the resulting distribution can be "fair"
(all masses equal / a specified balance condition) — STATE THE PRECISE FORM you are attacking in
your own words first, from the literature you know, and flag any ambiguity explicitly before proving.
TARGET: settle the k = 13 trinomial slice.
METHOD HINTS: specialise the mechanisms that worked for k = 5,7,9,11 rather than re-running a
continuation-tree exhaustion: (i) first-zero / anchor arguments pinning the smallest index where the
convolution can vanish; (ii) log-concavity of packets of consecutive coefficients; (iii) a finite
symbolic inequality in the two exponents (b,c) after normalisation; (iv) reduction to a bounded
region of (b,c) plus a finite check.
DELIVERABLES: precise statement; numbered lemmas; either a complete proof for k = 13 or an explicit
counterexample trinomial; a verification plan (finite computations + Lean targets); if incomplete,
the EXACT residual open statement. Machines verify; the argument must be yours. No hand-waving.
