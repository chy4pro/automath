# Task: does every EXTREMAL function lie in the paper's already-proved "Case A"? (angle: direct
# necessity proof attempt)

This is a genuine open question from an active research effort on a combinatorics paper. We want
a real proof attempt, not a plausibility sketch. If you cannot close it, say so plainly and report
exactly where the argument breaks — that is a valued, useful answer, not a failure. A fluent
argument that skips a step is the outcome we are specifically trying to avoid: everything you send
back will be checked line by line by an independent reviewer who verifies each load-bearing step
by reconstructing it, not by trusting your tone. Give reasoning and an honest verdict, not
confidence language.

## 1. Setting (self-contained — assume no other context, no access to any paper or repository)

Let `p` be an odd prime. Everything lives in the vector space `F_p^2` (all arithmetic mod `p`,
coordinatewise, unless stated otherwise). Fix a function `f : F_p^2 -> F_p^2` with `f(0) = 0`
(otherwise arbitrary).

For `u` a nonzero vector in `F_p^2`, there is a fixed "carry" vector `c_u(x)` (depending on `u`
and `x` but not on `f`) whose exact formula you do not need. Define
```
d_u f(x) := f(x+u) - f(x) + c_u(x)          (mod p, a vector in F_p^2)
A_u(f)   := { d_u f(x) : x in F_p^2 }        (the SET of values taken, x ranging over ALL of F_p^2)
```
`A_u(f)` is a nonempty subset of `F_p^2`. **Established, use freely:** `|A_u(f)| >= 2` for every
nonzero `u`, for every `f` in the class under study.

There is also a set `T_f` (a "transversal") built from `f`, and a difference set `T_f - T_f`, and
the following identity is **established and directly verified by literal computation** (you do
not need to re-derive it):
```
|T_f - T_f|  =  1 + SUM over all nonzero u in F_p^2 of |A_u(f)|
```

### Two identities you may use freely (established; verified computationally hundreds of times in
### our own checks, not something you need to re-derive)

**Cycle identity.** For any nonzero `u` and any base point `x`, summing around the orbit
`x, x+u, x+2u, ..., x+(p-1)u` (exactly `p` distinct points, since `p` is prime and `u != 0`):
```
sum_{i=0}^{p-1} d_u f(x + i*u)  =  -u        (mod p, vector sum in F_p^2)
```

**Curl identity.** For all `u, v, x in F_p^2`:
```
d_u f(x+v) - d_u f(x)  =  d_v f(x+u) - d_v f(x)        (mod p)
```

## 2. A proved sub-lemma you may use freely — WITH its proof

**LEMMA (2-PT RIGIDITY).** If `|A_u(f)| = 2`, say `A_u(f) = {a, b}` with `a != b`, then there is a
nonzero scalar `n* in F_p \ {0}` such that `n*(a-b) = -u (mod p)`. In particular `a - b` is a
nonzero scalar multiple of `u`.

*Proof.* Fix a line `L` = one orbit `{x, x+u, ..., x+(p-1)u}`. Since `A_u(f) = {a,b}` globally,
every point of `L` has `d_u f` equal to `a` or `b`. Let `n(L)` be the number of points of `L`
where the value is `a`; then `p - n(L)` points have value `b`. The cycle identity applied to `L`
gives `n(L)*a + (p-n(L))*b = -u (mod p)`, i.e. `n(L)*(a-b) = -u (mod p)` (treating `n(L)` as its
residue mod `p`, since `p = 0 mod p`). This holds for EVERY line `L` (every orbit of `<u>`, there
are `p` of them, partitioning `F_p^2`), and the right-hand side `-u` does not depend on `L`. If two
lines `L, L'` had `n(L) != n(L') (mod p)`, then `(n(L)-n(L'))` would be invertible mod `p`,
forcing `a - b = 0` from `n(L)(a-b) = n(L')(a-b)`, contradicting `a != b`. So `n(L)` is the SAME
value `n*` mod `p` for every line, and `n*(a-b) = -u`. If `n* = 0` this reads `0 = -u`,
contradicting `u != 0`; so `n*` is invertible, hence `a - b = (n*)^{-1}*(-u)`, a nonzero scalar
multiple of `u`. QED.

## 3. The paper's proved theorem, "Case A" (established — published, not something to re-derive
## or attack; use it freely as a black box)

Call two nonzero vectors `u, v` **independent** if neither is a scalar multiple of the other
(equivalently `{u,v}` is a basis of `F_p^2`). Every nonzero `w` then has a unique expression
`w = lambda*u + mu*v`; call `w` **mixed** (relative to `u,v`) if `lambda != 0 AND mu != 0`.

**"Case A" hypothesis on `f`:** there exist independent `u, v` with `|A_u(f)| = 2` AND
`|A_v(f)| = 2`.

**The paper's Case A theorem (PROVED, published):** if `f` is in Case A (for some independent
pair `u,v`), then `|A_w(f)| >= 4` for EVERY `w` mixed relative to that `u,v`.

**Consequence you may use freely:** if `f` is in Case A via `u,v`, then, writing `S_u :=
SUM_{k=1}^{p-1} |A_{ku}(f)|` (the axis-direction sum along `u`'s line), `S_v` similarly along
`v`'s line, and `S_m := SUM` over the `(p-1)^2` mixed `w`, we get `S_u = 2(p-1)` (all `p-1` points
of `u`'s line, by 2-PT RIGIDITY, are forced through the mechanism that makes `|A_{ku}|` behave; in
particular the value 2 is achieved at `k=1` and the floor `>=2` applies at every `k`, so
`S_u >= 2(p-1)`, with equality iff EVERY nonzero multiple of `u`, not just `u` itself, has
`|A_{ku}| = 2`), `S_v >= 2(p-1)` similarly, and `S_m >= 4(p-1)^2` by the Case A theorem applied
pointwise to each mixed `w`. Hence `|T_f-T_f| = 1 + S_u + S_v + S_m >= 1 + 2(p-1) + 2(p-1) +
4(p-1)^2`. At `p=5` this reads `1 + 8 + 8 + 64 = 81 = (2p-1)^2`.

## 4. The target theorem of the source paper (context, not something to prove here)

The paper's own conjecture (its "hard direction", open in general — NOT what we are asking you to
prove) is: **`|T_f - T_f| >= (2p-1)^2` for every `f` with `f(0)=0`.** It is known that this bound
is attained with equality by `f == 0` (the paper's own published control value). Call an `f`
**extremal** if `|T_f - T_f| = (2p-1)^2` exactly (i.e. it attains the conjectured minimum).

## 5. Measured evidence that motivates today's question — quoted exactly as measured, on ONE
## specific sub-population, at `p = 5`

The sub-population studied: normal-form `f` with `f(0)=0`, `A_{e1}(f) = {(0,0),(1,0)}` EXACTLY
(so `|A_{e1}(f)| = 2` is already fixed by construction), and `|A_{e2}(f)| <= 3` (`e1=(1,0)`,
`e2=(0,1)`). This sub-population has **10,925** normal-form members (**273,125** after
de-normalizing by the group action). Every quantity below was computed on ALL of them, exclusion
list empty, no sampling:

```
min S_u   (4 nonzero multiples of e1, i.e. sum over k=1..4 of |A_{k*e1}(f)|)   =  8
min S_v   (4 nonzero multiples of e2)                                          =  8
min S_m   (16 mixed w, i.e. w = lambda*e1 + mu*e2, lambda,mu both nonzero)     = 62
1 + (sum of these THREE INDEPENDENT minima)                                    = 79
min of the TOTAL |T_f - T_f|, taken JOINTLY over the same f                    = 81
the conjecture's target (2p-1)^2                                               = 81
```

> **The three minima are not simultaneously attainable by one function.** Any argument that bounds
> the direction classes `S_u`, `S_v`, `S_m` **separately** can prove at most `79` on this class,
> and is therefore exactly 2 short of `81`, however sharp each per-class bound is made. **The loss
> is in the separation, not in the floors.** This is why the paper's original proof strategy (which
> does bound the classes separately) cannot reach `81` even where it works.

And directly on the question this brief asks:

> **Among the 10,925 members, exactly 50 attain `|T_f - T_f| = 81` (extremal). All 50 have
> `|A_{e2}(f)| = 2`** (hence are in Case A via `u=e1, v=e2`, since `|A_{e1}|=2` was already fixed).
> **The other 900 members violate the Case A theorem's would-be-weakened hypothesis (they have
> `|A_{e2}| = 3`, so are NOT in Case A) and NONE of them is extremal — their totals start at 85,
> four above 81.** The two sets are disjoint.

The route this measurement motivates (call it **(b2)**), quoted exactly as the line's own owner
stated it:

> "(b2) extremal characterisation | every f attaining `(2p-1)^2` lies in Case A (measured: **50/50**
> do) => conjecture reduces to Case A + strictness off it, and Case A is already proved | ...
> live, and it is the one I prefer"

and, from the same round's summary:

> "`(b2)` 'every extremal `f` lies in Case A' (50/50 measured) — normal-form, live, and preferred:
> it reduces the conjecture to published work plus strictness."

**Scope honesty, stated plainly:** the 50/50 above is measured on ONE class (`A_{e1}` exactly
`{(0,0),(1,0)}`) of 104 total classes at ONE prime (`p=5`). It does **not** cover `|A_{e1}| = 3`,
and it says nothing directly about general `p`.

## 6. THE QUESTION — what we actually want answered

> **Does every extremal `f` (any odd prime `p`, `f(0)=0`, `|T_f-T_f| = (2p-1)^2`, with NO
> restriction to the one class above) necessarily lie in Case A — i.e. must there exist SOME pair
> of independent directions `u, v` with `|A_u(f)| = |A_v(f)| = 2`?**

This is the "necessity" direction. (The "sufficiency" direction — Case A implies `|T_f-T_f| >= 81`
— is already established, see §3.) Route (b2) needs necessity to make the reduction work: extremal
=> Case A => (by the already-proved Case A theorem, plus a strictness argument this brief is not
asking you to supply) the conjecture follows.

## 7. What we want from you — ANGLE A: a direct proof attempt

Attempt to prove necessity directly, working from minimality.

1. **Set up the contrapositive precisely.** Suppose `f` is NOT in Case A: for every pair of
   independent `u, v`, at least one of `|A_u(f)|, |A_v(f)|` is `>= 3`. Your goal is to show this
   forces `|T_f-T_f| > (2p-1)^2` (strictly), i.e. `f` cannot be extremal.
2. **Try to use the identities of §1-2 globally, not just on one basis pair.** The `p+1` lines
   through the origin partition the `p^2-1` nonzero vectors. On each line, `|A_u|` for the `p-1`
   nonzero points of that line is `>= 2` pointwise (§1). Work out what you CAN and CANNOT say about
   how `|A_{ku}|` varies across different scalar multiples `k` of a fixed `u` on the same line —
   do the identities of §1-2 give you any relation between `A_u` and `A_{2u}`, say? (Do not assume
   more than what §1-2 actually establish; if you need a fact you cannot derive from them, say so
   explicitly rather than assuming it.)
3. **A natural sub-question to attack first, since it may be more tractable:** if `|A_u(f)| >= 3`
   for **every** nonzero `u` (no direction at all achieves the floor of 2), can you lower-bound
   `1 + SUM_{u != 0} |A_u(f)|` strictly above `(2p-1)^2`? (Naive counting gives `1 + 3(p^2-1)`,
   which is already far above `(2p-1)^2` for `p >= 5` — so this extreme sub-case may close easily;
   the real difficulty is the boundary case where SOME directions are at 2 but never two
   independent ones simultaneously, e.g. all the size-2 directions lie on a single line.)
4. **The harder sub-case:** suppose the set of directions `u` with `|A_u(f)| = 2` is nonempty but
   is contained in a single line through the origin (so no independent pair both at 2 exists).
   Does 2-PT RIGIDITY (§2) plus the cycle/curl identities let you say anything about `|A_w|` for
   `w` NOT on that line? Try to build an explicit lower bound and compare it to `(2p-1)^2`.
5. **Be precise about where you are stuck.** If you can only close special cases, state exactly
   which ones, and name the specific obstruction in the case(s) you cannot close (e.g. "I cannot
   rule out [specific configuration] because the identities give me [specific weaker fact] instead
   of what I need").
6. **Do not attempt exhaustive computation or a census at any prime.** We want a general structural
   argument (or a precise account of why one is currently out of reach), not a hand-verification at
   a specific small `p`. Small-`p` sanity checks are fine as illustration but are not the deliverable.

## 8. What to hand back

End with exactly one of:
- **PROOF COMPLETE** — necessity holds in general; give the full argument.
- **PARTIAL** — state exactly how far you got (e.g. "I can rule out the all-directions->=3 case, but
  the single-line-of-2s case requires [X], which I could not establish") and exactly where it
  breaks.
- **CLAIM APPEARS FALSE, OR I SUSPECT IT IS FALSE** — describe as precisely as you can what a
  counterexample would have to look like (even if you cannot construct one), and why you believe
  no proof of necessity can work.
- **I COULD NOT MAKE PROGRESS** — say so plainly, and say what you would need (a fact, a tool, a
  different framing) to get traction. This is a valid and useful answer.

If anything in §1-3 above looks to you like it is being used incorrectly, or looks internally
inconsistent, say so explicitly — that would itself be a valuable finding.
