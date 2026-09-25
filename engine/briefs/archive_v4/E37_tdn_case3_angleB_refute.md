# Task: does a named lemma survive weakening its hypothesis from "=2" to "<=3"? (angle: hunt for a counterexample FIRST, prove only if none is found)

This is a genuine open mathematical question that arose from an active research effort on a
combinatorics paper. **Your primary job on this angle is adversarial: try hard to BREAK the claim
below with an explicit small example before attempting to prove it.** A cross-family reviewer will
check any proof you offer line by line, and will check any counterexample by direct substitution,
so a fluent-sounding wrong proof is the failure mode we most want to avoid — an honest "I could
not find a counterexample and I could not prove it either, here is exactly how far I got" is a
completely valid and valued answer. Give reasoning and a verdict, not confidence language.

## 1. Setting (self-contained — assume no other context)

Let `p` be an odd prime. Everything below lives in the vector space `F_p^2` (all arithmetic is mod
`p`, coordinatewise). Fix a function `f : F_p^2 -> F_p^2` with `f(0) = 0` (otherwise arbitrary —
you get to choose `f` freely when hunting for a counterexample).

For `u` a nonzero vector in `F_p^2`, define the "carry" `c_u(x)` for `x in F_p^2`: it is a fixed
vector (independent of `f`) whose two coordinates are each `0` or `-1 mod p`, determined only by
`u` and `x`. Concretely, if you lift `x` and `u` to representatives in `{0,...,p-1}^2`, then
coordinate `i` of `c_u(x)` is `-1 mod p` if `x_i + u_i >= p` (a "carry" occurred in that
coordinate when adding the lifted representatives) and `0` otherwise. Define
```
d_u f(x) := f(x+u) - f(x) + c_u(x)          (mod p, a vector in F_p^2; x+u is mod p)
A_u(f)   := { d_u f(x) : x in F_p^2 }        (the SET of values taken, x ranging over ALL of F_p^2)
```
It is already established (usable freely, no need to re-derive) that `|A_u(f)| >= 2` for every
nonzero `u`, for every `f` in the class under study.

### Two identities you may use freely (verified computationally 400/400 on random `f` in our own
checks; not something you need to re-derive, but you SHOULD use them as computational tools below)

**Cycle identity.** For any nonzero `u` and any base point `x`, summing around the orbit
`x, x+u, x+2u, ..., x+(p-1)u` (exactly `p` distinct points, since `p` prime, `u != 0`):
```
sum_{i=0}^{p-1} d_u f(x + i*u)  =  -u        (mod p, vector sum in F_p^2)
```

**Curl identity.** For all `u, v, x in F_p^2`:
```
d_u f(x+v) - d_u f(x)  =  d_v f(x+u) - d_v f(x)        (mod p)
```

### A proved sub-fact (given WITH its proof, for your use and to check)

**LEMMA (2-PT RIGIDITY).** If `|A_u(f)| = 2`, say `A_u(f) = {a,b}`, then there is a nonzero
`n* in F_p \ {0}` with `n*(a-b) = -u (mod p)` — so `a-b` is a nonzero scalar multiple of `u`.
*Proof.* Along one orbit-line `L` of `<u>`, with `n(L)` points valued `a` and `p-n(L)` valued `b`,
the cycle identity gives `n(L)*(a-b) = -u (mod p)`. The right side is the same for every line, so
(since `a != b` and `p` is prime) `n(L)` must be the same residue `n*` mod `p` on every line, and
`n* != 0` (else `-u=0`). Hence `a-b = (n*)^{-1}(-u)`. QED. (Corroborated computationally, 200/200,
in our own checks.)

## 2. The exact claim under attack

Fix `u, v` nonzero and INDEPENDENT (not scalar multiples of each other — automatically a basis of
`F_p^2`). Every nonzero `w` has a unique `w = lambda*u + mu*v`. Call `w` **mixed** if
`lambda != 0 AND mu != 0` (`(p-1)^2` such `w` out of `p^2-1` nonzero vectors).

The claim to attack:
> **CLAIM.** If `u, v` are independent, `|A_u(f)| <= 3`, and `|A_v(f)| <= 3`, then
> `|A_w(f)| >= 4` for EVERY mixed `w = lambda*u + mu*v`.

Context you should know, honestly stated: the source paper proves this claim under the STRONGER
hypothesis `|A_u(f)| = 2` AND `|A_v(f)| = 2` exactly (call that LEM-A; we have not independently
verified LEM-A itself beyond the 2-point rigidity sub-fact above, so treat it as a claim, not a
certainty). What is open, and what you are attacking, is whether relaxing `=2` to `<=3` (i.e.
allowing `|A_u|` and `|A_v|` to each be `2` OR `3`) still forces `|A_w| >= 4` on mixed directions.
Nobody currently knows the answer; a `<=3` hypothesis is weaker (more `f` satisfy it) so the CLAIM
could plausibly be false even though the `=2` version is believed true.

## 3. What we want from you — ANGLE B: attack first, prove only as fallback

**Step 1 — small-`p` adversarial search, by hand.** Work at `p = 3` first (`F_3^2` has 9 points;
`f` assigns one of 9 values to each of 9 points, with `f(0,0)=(0,0)` fixed, so 8 free values —
small enough to reason about directly, or to organize a systematic partial search over structured
candidates). Pick a concrete independent pair, e.g. `u=(1,0)`, `v=(0,1)`. Try to CONSTRUCT (by
direct choice, or by a structured ansatz — e.g. `f` piecewise-linear on cosets, or built from a
smaller building block) an `f` with `|A_u(f)| in {2,3}`, `|A_v(f)| in {2,3}`, and `|A_w(f)| <= 3`
for at least one of the 4 mixed directions `w in {u+v, u-v, u+2v, u-2v}` (mod 3, i.e. `w` with both
coefficients nonzero — at `p=3` the nonzero coefficients are `1` or `2`). Report EVERY attempt that
fails and why, not just a final answer — a near-miss is useful data even if you don't find a full
counterexample. If `p=3` search space is small enough, be as systematic as you can (e.g. fix a
structural form for `f` and vary parameters within it, rather than one-off guesses).

**Step 2 — if step 1 finds nothing at `p=3`, try `p=5`** (`F_5^2`, 25 points) using whatever
structural insight step 1 gave you (e.g. if a near-miss suggested a promising family of `f`, try
scaling it up).

**Step 3 — if no counterexample turns up, attempt the positive direction as a fallback.** Try to
adapt the §1 rigidity argument to 3-point sets (write out the cycle-identity constraint for a
3-element `A_u(f) = {a,b,c}` explicitly: along each line `L`, counts `n_a(L)+n_b(L)+n_c(L)=p` give
`n_a(L)*a+n_b(L)*b+n_c(L)*c = -u`, and — unlike the 2-point case — the counts need NOT be constant
across lines, since 3 unknowns are not pinned down the same way by a 2-dimensional target). Work
out precisely what structure on `{a,b,c}` this DOES force, and whether it is enough, combined with
the curl identity, to force `|A_w| >= 4` on mixed `w`. If you can push this through, that is a
proof; if you get stuck, say exactly where.

## 4. What to hand back

End with exactly one of:
- **CLAIM APPEARS FALSE** — give the most explicit counterexample you found: `p`, `u`, `v`, `f`
  (as an explicit table of values if small enough, or an explicit formula), the mixed `w`, and the
  computed values `|A_u(f)|`, `|A_v(f)|`, `|A_w(f)|`. This is the most valuable possible answer if
  you can get it.
- **PROOF COMPLETE** — if your search found nothing and your fallback proof attempt actually
  closed the gap, give the full argument.
- **NEITHER** — report your best near-miss counterexample attempts (what broke, and why) AND your
  best partial proof attempt (how far it got, where it breaks). This is a fully acceptable answer;
  do not manufacture false confidence in either direction to avoid giving this answer.
