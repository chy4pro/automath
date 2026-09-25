# Task: does every EXTREMAL function lie in the paper's already-proved "Case A"? (angle:
# adversarial — hunt for a counterexample, and stress-test the "strictness" half)

This is a genuine open question from an active research effort on a combinatorics paper. We want a
real, honest adversarial attempt — you are being asked to try to BREAK a claim the research line's
own owner prefers, not to confirm it. If you cannot break it and cannot find any weak point, say so
plainly; that is a valued, useful answer, not a failure. Everything you send back will be checked
line by line by an independent reviewer who reconstructs each load-bearing step rather than
trusting your tone, so a fluent-sounding argument that skips a step is exactly the failure mode
being guarded against. Give reasoning and an honest verdict, not confidence language.

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
nonzero `u`, for every `f` in the class under study, and `A_{-u}(f) = -A_u(f)`.

There is also a set `T_f` built from `f`, and a difference set `T_f - T_f`, and the following
identity is **established and directly verified by literal computation**:
```
|T_f - T_f|  =  1 + SUM over all nonzero u in F_p^2 of |A_u(f)|
```

**Cycle identity** (established): for any nonzero `u` and base point `x`, summing around the orbit
`x, x+u, ..., x+(p-1)u`: `sum_{i=0}^{p-1} d_u f(x+i*u) = -u (mod p)`.

**Curl identity** (established): for all `u,v,x`: `d_u f(x+v) - d_u f(x) = d_v f(x+u) - d_v f(x)
(mod p)`.

**2-PT RIGIDITY** (established, proved from the cycle identity): if `|A_u(f)| = 2`, say
`A_u(f)={a,b}`, then `a-b` is a nonzero scalar multiple of `u` — the 2-element image is forced onto
the line through the origin parallel to `u`.

## 2. "Case A", and the paper's proved theorem about it (established — published; use freely)

Call `u,v` **independent** if neither is a scalar multiple of the other. `f` is in **Case A** if
there exist independent `u,v` with `|A_u(f)| = |A_v(f)| = 2`. **The paper's Case A theorem
(PROVED, published):** if `f` is in Case A via `u,v`, then `|A_w(f)| >= 4` for every `w` mixed
relative to `u,v` (i.e. `w = lambda*u+mu*v` with `lambda,mu` both nonzero).

## 3. The target theorem, extremality, and the route in question

The paper's own open conjecture: **`|T_f-T_f| >= (2p-1)^2` for every `f` with `f(0)=0`**. This is
attained with equality by `f == 0`. Call `f` **extremal** if `|T_f-T_f| = (2p-1)^2` exactly.

The route under test, **(b2)**, quoted exactly as the line's own owner stated it:

> "(b2) extremal characterisation | every f attaining `(2p-1)^2` lies in Case A (measured: **50/50**
> do) => conjecture reduces to Case A + strictness off it, and Case A is already proved | ...
> live, and it is the one I prefer"

and

> "`(b2)` 'every extremal `f` lies in Case A' (50/50 measured) — normal-form, live, and preferred:
> it reduces the conjecture to published work plus strictness."

**(b2) has TWO parts, and this brief wants you to attack BOTH:**
1. **Necessity**: every extremal `f` lies in Case A.
2. **Strictness "off" Case A**: functions structurally close to but outside Case A must have
   `|T_f-T_f|` strictly greater than `(2p-1)^2` — this is the second half needed to actually finish
   the reduction to "published work plus a strictness argument."

## 4. Measured evidence, quoted exactly — ONE class, `p = 5`

Sub-population: normal-form `f`, `f(0)=0`, `A_{e1}(f) = {(0,0),(1,0)}` EXACTLY (so `|A_{e1}|=2` is
fixed by construction), `|A_{e2}(f)| <= 3` (`e1=(1,0)`, `e2=(0,1)`). **10,925** normal-form members
(**273,125** de-normalized). Every quantity below: exclusion list empty, no sampling.

```
min S_u   (4 nonzero multiples of e1)          =  8
min S_v   (4 nonzero multiples of e2)          =  8
min S_m   (16 mixed w)                         = 62
1 + sum of these THREE INDEPENDENT minima      = 79
min of the TOTAL, taken JOINTLY                = 81   <- the conjecture's target (2p-1)^2
```

> **The three minima are not simultaneously attainable.** Any argument bounding the direction
> classes separately can prove at most `79` on this class — 2 short. **The loss is in the
> separation, not in the floors.**

> **The 300 members with `S_m = 62` (its own separate minimum) have `min(S_u+S_v) = 22` there,
> giving total `>= 85`. The members that actually reach `81` are the ones with `S_m = 64`** (not
> `S_m`'s own minimum of 62) **and simultaneously `S_u=8, S_v=8`. Mixed-direction loss is paid for
> by axis-direction gain, at better than 1:1.**

> **Exactly 50 of the 10,925 are extremal (`|T_f-T_f|=81`). All 50 have `|A_{e2}|=2`** (hence Case
> A via `e1,e2`). **The other 900 have `|A_{e2}|=3` (NOT Case A) and NONE is extremal — totals
> start at 85, four above the box.**

**Scope honesty:** this is ONE class of 104 at `p=5`, with `|A_{e1}|` already fixed at exactly 2 by
construction (i.e. every member of this class is already "half-way" into Case A along the `e1`
axis before anything is measured). It says nothing about `|A_{e1}| = 3`, and nothing directly about
general `p`.

## 5. What we want from you

### Angle B, part 1 — hunt for a counterexample to NECESSITY

Try to construct, or give a strong structural argument for the likely existence of, an `f` (ANY
odd prime `p`, ANY class — do not restrict yourself to the one class measured above) that is
extremal (`|T_f-T_f| = (2p-1)^2`) but is **NOT** in Case A. Specifically:

1. Consider `f` where the directions achieving `|A_u|=2` all lie on a **single** line through the
   origin (so no independent pair is simultaneously at 2). Using 2-PT RIGIDITY and the cycle/curl
   identities, can you build (or rule out) such an `f` reaching `81`? Note the class above already
   guarantees `|A_{e1}|=2`, so it cannot test this scenario — you need to reason about a
   genuinely different class or construction.
2. Consider `f` where NO direction at all achieves `|A_u|=2` (every `|A_u| >= 3`). Does the
   arithmetic plausibly allow `1 + SUM|A_u| = (2p-1)^2` for some `p`? Do a back-of-envelope bound:
   with `p^2-1` nonzero directions each `>= 3`, what is the cheapest possible total, and how does
   it compare to `(2p-1)^2` as `p` grows? Is this sub-case obviously impossible, or does it need a
   real argument?
3. If you believe no counterexample can exist, say what general mechanism (not specific to the one
   measured class) would rule it out — the measured trade-off in §4 ("mixed-direction loss is paid
   for by axis-direction gain, at better than 1:1") is a fact about ONE class; does an analogous
   trade-off plausibly hold in general, and can you say why or why not?

### Angle B, part 2 — stress-test the STRICTNESS half

Even granting necessity, (b2)'s reduction needs: any `f` that leaves Case A pays a strict penalty.
The only evidence at hand is the 900-member set in §4, and that set is drawn from a class that is
already very close to Case A (`|A_{e1}|=2` fixed, only `|A_{e2}|` varies to 3). It is NOT evidence
about functions that are far from Case A in every direction.

1. Is there any reason to expect the "always >= 85, never extremal" pattern to hold for functions
   with, say, `|A_u| >= 3` for ALL `u` (the maximally-non-Case-A case), or could such functions in
   principle come arbitrarily close to `81` (or even below it, which would refute the CONJECTURE
   itself, not just the route) for some larger `p`? Reason about this using the identities of §1,
   not by assuming the pattern generalizes.
2. Try to identify the WORST case for strictness: what is the structural profile of an `f` that is
   "as close as possible" to Case A without being in it (e.g. `|A_u|=2` on one line and `|A_v|=3`
   for the best available independent `v`, as in the measured class) versus one that is "as far as
   possible" (no direction at 2 anywhere) — does the strictness argument plausibly need to handle
   both, or does one dominate?

## 6. What to hand back

End with exactly one of:
- **COUNTEREXAMPLE FOUND (or a strong constructive argument for one)** — describe it as explicitly
  as you can: prime `p`, the function or family, and why it is extremal but outside Case A.
- **NO COUNTEREXAMPLE FOUND, WITH A STRUCTURAL ARGUMENT FOR WHY NONE CAN EXIST** — give the
  argument; be explicit about what is proved versus conjectured.
- **NO COUNTEREXAMPLE FOUND, NO STRUCTURAL ARGUMENT EITHER WAY** — say so plainly; this is a valid
  outcome of a genuine search.

Separately, give your honest read on the STRICTNESS half (§5 part 2): does the evidence in §4
generalize, or is it an artifact of the one class studied being already close to Case A? If you
find that the identities of §1-2 are being used incorrectly anywhere above, or the setup looks
internally inconsistent, say so explicitly — that would itself be a valuable finding.
