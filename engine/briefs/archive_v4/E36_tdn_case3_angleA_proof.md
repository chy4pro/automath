# Task: does a named lemma survive weakening its hypothesis from "=2" to "<=3"? (angle: direct proof attempt, extending the existing rigidity mechanism)

This is a genuine open mathematical question that arose from an active research effort on a
combinatorics paper. We want a real proof attempt. If you cannot close it, say so plainly and
report exactly where the argument breaks. An honest "I could not close this" is far more valuable
to us than a fluent-sounding argument that skips a step. Give reasoning and a verdict, not
confidence language. Someone will check your work line by line, so every step must actually be
justified, not asserted.

## 1. Setting (self-contained — assume no other context)

Let `p` be an odd prime. Everything below lives in the vector space `F_p^2` (all arithmetic is
mod `p`, coordinatewise, unless stated otherwise). Fix a function `f : F_p^2 -> F_p^2` with
`f(0) = 0` (otherwise arbitrary).

For `u` a nonzero vector in `F_p^2`, define the "carry" `c_u(x)` for `x in F_p^2`: it is a fixed
vector (independent of `f`) whose two coordinates are each `0` or `-1 mod p`; you do not need its
exact formula for anything below, only that it is fixed once `u` is fixed (does not depend on `f`).
Define
```
d_u f(x) := f(x+u) - f(x) + c_u(x)          (mod p, a vector in F_p^2)
A_u(f)   := { d_u f(x) : x in F_p^2 }        (the SET of values taken, as x ranges over ALL of F_p^2)
```
`A_u(f)` is a nonempty subset of `F_p^2`. It is already established (and you may use freely,
without re-deriving) that `|A_u(f)| >= 2` for every nonzero `u`, for every `f` in the class under
study.

### Two identities you may use freely (established facts about this construction; verified
computationally 400/400 on random `f` in our own checks, and not something you need to re-derive)

**Cycle identity.** For any nonzero `u` and any base point `x`, summing around the orbit
`x, x+u, x+2u, ..., x+(p-1)u` (which has exactly `p` distinct points, since `p` is prime and
`u != 0`):
```
sum_{i=0}^{p-1} d_u f(x + i*u)  =  -u        (mod p, vector sum in F_p^2)
```

**Curl identity.** For all `u, v, x in F_p^2`:
```
d_u f(x+v) - d_u f(x)  =  d_v f(x+u) - d_v f(x)        (mod p)
```

## 2. A proved sub-lemma you may use freely — WITH its proof, so you can check it

**LEMMA (2-PT RIGIDITY).** If `|A_u(f)| = 2`, say `A_u(f) = {a, b}` with `a != b`, then there is a
nonzero scalar `n* in F_p \ {0}` such that `n*(a-b) = -u (mod p)`. In particular `a - b` is a
nonzero scalar multiple of `u` — the two-element image set lies on the line through the origin
spanned by `u`.

*Proof (given here for you to verify — this is our own reconstruction from the cycle identity,
not copied from anywhere; check it before relying on it).* Fix a line `L` = one orbit
`{x, x+u, ..., x+(p-1)u}`. Since `A_u(f) = {a,b}` globally, every point of `L` has `d_u f` equal to
`a` or `b`. Let `n(L)` (an integer in `[0,p]`) be the number of points of `L` where the value is
`a`; then `p - n(L)` points have value `b`. The cycle identity applied to `L` gives
`n(L)*a + (p-n(L))*b = -u (mod p)`, i.e. (since `p = 0 mod p`) `n(L)*(a-b) = -u (mod p)`, treating
`n(L)` as its residue mod `p`. This holds for EVERY line `L` (every orbit of `<u>` — there are `p`
of them, partitioning `F_p^2`), and the right-hand side `-u` does not depend on `L`. If two lines
`L, L'` had `n(L) != n(L') (mod p)`, then `(n(L)-n(L'))` would be invertible mod `p` (nonzero,
`p` prime), forcing `a - b = 0` from `n(L)(a-b) = n(L')(a-b)` — contradicting `a != b`. So `n(L)`
is the SAME value `n*` mod `p` for every line, and `n*(a-b) = -u`. If `n* = 0` this reads `0 = -u`,
contradicting `u != 0`; so `n* != 0`, hence invertible, hence `a - b = (n*)^{-1}*(-u)`, a nonzero
scalar multiple of `u`. QED.

(This sub-fact — "2-point images are forced onto a line parallel to `u`" — was also confirmed by
direct computation in our own checks, 200/200 random functions at two primes, so the proof above
is corroborated, not merely asserted.)

## 3. The lemma whose robustness is the actual question

Fix `u, v` nonzero and INDEPENDENT (i.e. not scalar multiples of each other — equivalently, since
`F_p^2` is 2-dimensional, `{u,v}` is a basis). Every nonzero `w in F_p^2` then has a UNIQUE
expression `w = lambda*u + mu*v` with `lambda, mu in F_p`, not both zero. Call `w` **mixed** if
`lambda != 0 AND mu != 0` (there are `(p-1)^2` such `w`, out of `p^2-1` nonzero vectors total).

**The paper's own lemma (call it LEM-A), stated here as CONTEXT — this is a claim from the source
paper, not something we have independently verified beyond the 2-point rigidity sub-fact of §2
above:**
> If `u, v` are independent and `|A_u(f)| = 2` AND `|A_v(f)| = 2`, then `|A_w(f)| >= 4` for EVERY
> mixed `w = lambda*u + mu*v`.

We do not have the paper's proof text to give you beyond what is above; what we DO know (and can
tell you honestly) is that the `=2` case's proof is understood to use ONLY the 2-point rigidity
fact of §2 (that `A_u`, resp. `A_v`, is forced onto a line through 0 parallel to `u`, resp. `v`) —
nothing more exotic. We are told, and pass on to you as a claim to check rather than a fact to
trust, that the `=2` hypothesis is essential to the paper's argument and that no analogous
rigidity is currently known for 3-point sets.

## 4. THE QUESTION — this is what we want answered

> **Does LEM-A survive weakening `|A_u(f)| = 2` and `|A_v(f)| = 2` to `|A_u(f)| <= 3` and
> `|A_v(f)| <= 3`?** That is: if `u, v` are independent, `|A_u(f)| <= 3`, and `|A_v(f)| <= 3`
> (each is `2` or `3`, using the `>= 2` floor from §1), must `|A_w(f)| >= 4` STILL hold for every
> mixed `w = lambda*u + mu*v`? Or is there an `f` (any prime `p`, the smaller the better) with
> `|A_u(f)| <= 3`, `|A_v(f)| <= 3`, and `|A_w(f)| <= 3` for SOME mixed `w`?

## 5. What we want from you — ANGLE A: extend the rigidity mechanism directly

Attempt to generalize the §2 proof technique to the 3-point case, and use it (plus the curl
identity) to either prove or refute the claim of §4.

1. **Generalize §2's argument to `|A_u(f)| = 3`.** Say `A_u(f) = {a,b,c}`. Redo the §2 computation:
   for a line `L`, let `(n_a(L), n_b(L), n_c(L))` be the counts of each value along `L`
   (`n_a+n_b+n_c = p`). The cycle identity gives `n_a(L)*a + n_b(L)*b + n_c(L)*c = -u (mod p)` for
   every line `L`. Unlike the 2-point case, this is now ONE vector equation (2 scalar equations)
   with potentially THREE different `(n_a,n_b,n_c)` triples across different lines (not forced to
   be constant, since three unknowns are not pinned down by a 2-dimensional target the way two
   unknowns with `n_a+n_b=p` fixed were). Work out EXACTLY what constraint this puts on `{a,b,c}`
   as `L` ranges over all `p` lines. Does it still force `{a,b,c}` (or some derived quantity like
   the affine span, or a specific sub-line) into a special position relative to `u`? Be precise —
   do not hand-wave "it should still be rigid."
2. **Use the curl identity to connect `A_u`-structure and `A_v`-structure to `A_w`-structure at a
   mixed `w`.** The curl identity directly relates `d_u f` and `d_v f` at shifted points. Try to
   build an explicit lower bound on `|A_w(f)|` (for mixed `w`) purely from whatever constraint you
   derived in step 1 for `u` and the analogous one for `v`. Show your work at the level of: "if
   `A_w(f)` had only 3 elements, then [specific consequence], which contradicts [specific fact],
   because [specific reason]." A proof sketch that does not reach this level of specificity is not
   sufficient — we need the actual chain of implications, not a plausibility argument.
3. **If you get stuck at a specific step, name the step precisely** (e.g. "the 3-point analogue of
   the rigidity constraint from step 1 is [X], but I cannot rule out [specific configuration] from
   it") rather than describing the difficulty in general terms.
4. **Try small primes by hand if it helps intuition** (`p=3` gives `F_3^2`, 9 points; `p=5` gives
   `F_5^2`, 25 points) but the goal is a general argument for all `p`, or a general
   counterexample/obstruction, not just small-case computation.

## 6. What to hand back

End with exactly one of:
- **PROOF COMPLETE** — the claim of §4 holds in general; give the full argument.
- **PARTIAL** — state exactly how far you got (e.g. "I can show `|A_w| >= 4` when [extra
  condition], but not in general" or "I can show the 3-point rigidity constraint is [X], but
  connecting it to `A_w` requires [Y] which I could not establish"), and exactly where it breaks.
- **CLAIM APPEARS FALSE** — give as explicit a counterexample as you can: a prime `p`, independent
  `u,v`, and (ideally) an explicit `f` or family of `f` with `|A_u| <= 3`, `|A_v| <= 3`, and
  `|A_w| <= 3` for some specific mixed `w`. If you cannot construct `f` explicitly but have a
  strong structural argument that one must exist, say that instead and be explicit about what is
  proved versus conjectured.

If you find that the 2-point rigidity lemma of §2, or the cycle/curl identities, appear to be used
incorrectly anywhere above, say so explicitly — that would itself be a valuable finding.
