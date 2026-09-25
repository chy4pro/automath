# Task: ADVERSARIAL cross-family stress test — does this eleven-step chain actually prove what it
# claims ("one 2-direction forces the box")?

This is a genuine open question from an active research effort on a combinatorics/number-theory
paper (arXiv:2606.27961, "transversal difference numbers"). We believe we have derived a theorem
strictly stronger than the one already published in the source paper, and we want it BROKEN if it
can be broken. We want a real adversarial attempt, not a plausibility read-through. **If you cannot
break it, say so plainly and say exactly where you got stuck** — "I could not break it, and here is
where I got stuck" is a valued, useful answer, not a failure. The failure mode we are specifically
guarding against is a FLUENT WRONG REFUTATION: a confident-sounding claim that some step fails,
which does not actually hold up once someone reconstructs it. Everything you send back will be
checked line by line by an independent cross-family reviewer who verifies each load-bearing step by
reconstructing it, not by trusting your tone or your confidence language. **Give reasoning and an
honest verdict, not confidence language.**

## 0. Context (stated so you aim at the right target — not something to re-derive or verify)

The source paper proves a rigidity theorem only under the hypothesis that TWO INDEPENDENT directions
`u,v` both have `|A_u| = |A_v| = 2` ("Case A"). The claim below needs only ONE such direction — it
is strictly stronger than the paper's proved result.

It has already been checked computationally on a complete class of 10,925 normal-form functions at
`p=5` (the enumeration is reported `complete = True` — it ran to the end, not to a clock or a cap),
and every one of the four bounds the argument below predicts was attained EXACTLY by the minimum
over that class: the per-coset budget (predicted `2p−1 = 9`, measured min `9`), the per-column bound
(predicted `4p−2 = 18`, measured min `18`), the off-axis sum `S_off` (predicted `(p−1)(4p−2) = 72`,
measured min `72`), and the total `|T_f−T_f|` (predicted `(2p−1)² = 81`, measured min `81`). This
computational agreement is **not** a proof and is **not** part of what you are being asked to check —
it is told to you only so that you attack the ARGUMENT itself rather than spend your effort
re-discovering agreement the computation already found on that one class. A genuine counterexample,
if one exists, has to come from OUTSIDE that already-checked population (a different `p`, a
different function) or has to be a logical gap in the argument, not a numerical mismatch on data
already examined.

## 1. Setting and definitions (verbatim; assume no other context, no access to any paper)

Let `p` be an odd prime. Fix a function `f : F_p^2 -> F_p^2` with `f(0) = 0` (otherwise arbitrary).
All arithmetic is mod `p`, coordinatewise, unless stated otherwise.

For `y` in `F_p^2`, write `[y]` for the standard integer representative of `y` with both coordinates
in `{0, 1, ..., p-1}` (the usual lift). For `u` a nonzero vector in `F_p^2`, define the carry vector

```
c_u(x) := ( [x+u] - [x] - [u] ) / p       (computed coordinatewise in Z, dividing by p; each
                                            coordinate works out to exactly 0 or -1, then read as
                                            an element of F_p, i.e. 0 or p-1)
```

and then

```
d_u f(x) := f(x+u) - f(x) + c_u(x)         (mod p, a vector in F_p^2)
A_u(f)   := { d_u f(x) : x in F_p^2 }       (the SET of values taken, x ranging over ALL of F_p^2)
```

There is also a set `T_f` (a "transversal") built from `f`, and a difference set `T_f - T_f`, and the
following identity is established and directly verified by literal computation (you do not need to
re-derive it):

```
|T_f - T_f|  =  1 + SUM over all nonzero u in F_p^2 of |A_u(f)|
```

### Two structural identities (established; carry-level parts verified exhaustively — you may use
### these freely, they are not what you are being asked to check)

For `u_c` the `c`-th coordinate of `u` represented in `{0,...,p-1}` (`c = 1,2`; same convention for
`v_c`):

**(I) COCYCLE.** For all `u, v, x`:  `d_{u+v} f(x) = d_u f(x) + d_v f(x+u) + ε(u,v)`,
with `ε(u,v)_c = ⌊(u_c+v_c)/p⌋ ∈ {0,1}`.

**(II) TELESCOPE.** For `1 ≤ k ≤ p−1`:  `d_{ku} f(x) = Σ_{i<k} d_u f(x+iu) + γ(u,k)`,
with `γ(u,k)_c = ⌊k·u_c/p⌋`.

(As used below, `γ(u,p)` means the same closed-form expression `⌊p·u_c/p⌋ = u_c` evaluated at `k=p`,
i.e. `γ(u,p) = u`; this extends the stated range `1≤k≤p−1` by one, and is used once, in Step 1
below, exactly as our own working notes use it. If you think this extension needs its own
justification and isn't automatic, that is a fair and useful thing to flag — we are not asserting it
is beyond question, only telling you it is how the source text uses it.)

### (VI), derived from (I), with its one-line reason — this is the key mechanism the eleven steps run on

`ε(u,v)_c = ⌊(u_c+v_c)/p⌋` is **symmetric in `u` and `v`**. Apply (I) once as `u+v` and once
as `v+u`; the left-hand sides (`d_{u+v} f(x)` in both cases) are identical, so

```
d_u f(x) + d_v f(x+u) + ε(u,v)  =  d_v f(x) + d_u f(x+v) + ε(v,u)
```

and, because `ε(u,v) = ε(v,u)`, the `ε` terms cancel, leaving:

> **(VI)   d_v f(x+u) − d_v f(x)  =  d_u f(x+v) − d_u f(x)      for ALL u, v, x and ALL f.**

### 1.1 What "established" means here (so you know what's free to use vs. what you're checking)

Everything in this section 1 — the definitions, (I), (II), and (VI) as derived from them — is prior
work on this line, checked by direct exhaustive computation at multiple primes with zero violations
found. It is **not** what you are being asked to re-verify. What you ARE being asked to check is the
eleven-step argument in section 3 below, which is built on top of these.

## 2. Additional notation used only inside the argument (quoted from the same line's own working
## notes, included here so the argument in section 3 is actually readable — not invented for this
## brief)

- `⟨u⟩` denotes the additive subgroup `{0, u, 2u, ..., (p-1)u}` generated by `u` — a line through the
  origin in `F_p^2`, exactly `p` points (since `p` is prime and `u != 0`, the map `k -> k*u` from
  `F_p` is injective, hence an isomorphism onto its image). A "`u`-orbit" or "`u`-coset" is a coset
  `x + ⟨u⟩` of this subgroup; there are exactly `p` of them and they partition `F_p^2`.
- `π` denotes the quotient map `F_p^2 -> F_p^2/⟨u⟩`, a group of order `p` (since `⟨u⟩` has order `p`
  inside the order-`p^2` group `F_p^2`). `π` applied to a set means the image set.
- **Labelling `L`** — the one piece of apparatus from an earlier round's write-up that step 2 below
  needs, quoted here rather than left implicit: once `A_u = {a, a+s}` is known to be a 2-element set
  (the hypothesis of the whole argument), label each point `x` by which of the two values `d_u f(x)`
  takes: `L(x) = 0` if `d_u f(x) = a`, and `L(x) = 1` if `d_u f(x) = a+s`. For a fixed `u`-coset
  (orbit), its "weight" is the number of points on it with `L = 1`.
- Fixing some `v` not in `⟨u⟩`, the `p` distinct `u`-cosets are indexed by `n = 0,...,p-1` via base
  points `z_n = n·v` (so `z_{n+1} = z_n + v`); `W_n(i) := L(z_n + i·u)` is the length-`p` `0/1`
  "labelling word" of coset `n` (`i` ranging over `F_p`), and its weight (number of `1`s) is written
  `t` in the steps below.
- `K_k` (step 5) denotes a constant vector depending only on `k`. Its exact formula is not given in
  the source text quoted below — the only property step 5 uses is that `π` applied to a set
  translated by `K_k` equals `π(K_k)` plus `π` of the untranslated set (`π(K_k + S) = π(K_k) + π(S)`
  for any set `S`), which holds automatically because `π` is a group homomorphism applied pointwise
  to a translated set.
- `δ_{n0}` and `φ_k` (step 6) are quoted verbatim from the source and not elaborated further here —
  if their meaning is unclear to you, **say so explicitly as part of your answer** rather than
  guessing silently and building on a guess.

## 3. THE THEOREM AND ITS ELEVEN-STEP PROOF, quoted verbatim from the line's own working notes

> **THEOREM.** **If some `u ≠ 0` has `|A_u| = 2`, then `|T_f − T_f| ≥ (2p−1)²`.**

The paper's proved case is `|A_u| = |A_v| = 2` for **two independent** directions (Case A). This
needs **one**. Proof, in the order the controls check it:

**1.** `|A_w| ≥ 2` for every `w ≠ 0`. The cycle identity `Σ_i d_w f(x+iw) = −w ≠ 0` (which is (II) at
`k = p`, since `γ(w,p) = w`) kills `|A_w| = 1`, because a constant value `a` would give `p·a = 0`.

**2.** `A_u = {a, a+s}` with `s = c·u`, and the labelling weight `t` is the same on every `u`-orbit.
From the same cycle identity, `p·a + t(x)·s = −u`, so `t(x)·s = −u`: `s ∈ ⟨u⟩`, `t·c = −1`,
`1 ≤ t ≤ p−1`. *(This re-derives §6's 2-point rigidity from the cycle identity alone — "§6" is a
section of the source paper / an earlier round's notes, not included in this brief; the derivation
in this step is self-contained without it, this parenthetical is just noting where else the same
fact appears.)*

**3.** Put `β = d_v f` for any `v ∉ ⟨u⟩`. By (VI), `β(x+u) − β(x) = (L(x+v) − L(x))·s ∈ ⟨u⟩`.
So `π∘β` is **constant on every `u`-coset**, where `π` is the quotient by `⟨u⟩`. Write `h(n)` for
its value on `u`-coset `n`. **This is the exchange mechanism the task book asked for, and it is
exactly (VI) plus `s ∥ u`.** ("the task book" = the internal planning document for this round, not
included here — the point stands regardless: this step's content is fully derived above from (VI)
and step 2.)

**4.** `h` is non-constant. The cycle identity along `v` gives `Σ_n β(nv) = −v`, hence
`Σ_n h(n) = π(−v) ≠ 0`; a constant `h` sums to `p·h = 0`. So `g := |im h| ≥ 2`.

**5.** The column formula. By (I)+(II), for every `k`,
`A_{ku+v} = K_k + { ñ(y,k)·s + β(y) : y }` with `ñ(y,k) = Σ_{j=1}^{k} L(y − ju)`.
Since `s ∈ ⟨u⟩`, `π(A_{ku+v}) = π(K_k) + im h`, so `|A_{ku+v}| = Σ_{γ ∈ im h} |C_k(γ)| ≥ g`, where
`C_k(γ)` is the set of `⟨u⟩`-coordinates of the part lying over `γ`.

**6.** The per-coset budget. Fix `γ`, pick ONE `u`-coset `n₀` with `h(n₀) = γ`, and let `W_n` be the
labelling word of coset `n` with base points `z_n = n·v` (so `z_{n+1} = z_n + v`). Then
`φ_k(i) = c·ñ(i,k) + δ_{n₀}(i)` satisfies
`φ_k(i+1) − φ_k(i) = c·( W_{n₀+1}(i) − W_{n₀}(i−k) )`.
So `|C_k(γ)| ≥ 2` **unless every step vanishes**, i.e. unless `W_{n₀+1}` is `W_{n₀}` shifted by `k`.

**7.** At most one `k` can be exceptional. `W_{n₀}` has prime length `p` and weight `t` with
`1 ≤ t ≤ p−1`, so it is **aperiodic**: its `p` rotations are distinct. Hence
`Σ_{k ∈ F_p} |C_k(γ)| ≥ 2p − 1`.

**8.** Column bound. `S^{(v)} := Σ_{k∈F_p} |A_{ku+v}| = Σ_γ Σ_k |C_k(γ)| ≥ g(2p−1) ≥ 4p − 2`.

**9.** The `p(p−1)` directions off `⟨u⟩` partition into the `p−1` columns `{ku + mv}`, `m = 1..p−1`,
so `S_off ≥ (p−1)(4p−2)`.

**10.** `S_{⟨u⟩} ≥ 2(p−1)` by step 1.

**11.** `|T_f−T_f| = 1 + S_{⟨u⟩} + S_off ≥ 1 + 2(p−1) + (p−1)(4p−2) = 1 + 4p(p−1) = (2p−1)²`. ∎

**Closing remark, quoted verbatim (not a 12th step — the argument's own commentary on itself):**
"Every inequality in the chain is tight simultaneously, which is why it lands on `(2p−1)²`
**exactly** and not above it — and why round 3's `(V)` cap and this floor are the same phenomenon
seen from the two sides." (The "round 3 `(V)` cap" is a reference to other, unincluded material from
an earlier round of this research line — not something you need in order to evaluate the argument
above; quoted here in full rather than trimmed, per this brief's instruction to withhold nothing.)

## 4. THE QUESTION — what we actually want from you

> **Find an `f` (any odd prime `p`, `f(0)=0`) and a direction `u != 0` with `|A_u(f)| = 2`, such that
> `|T_f − T_f| < (2p−1)²` — OR — name the FIRST of the eleven steps above (by number) that does not
> follow from what precedes it, and explain exactly what breaks.**

Please attack the argument step by step, in order:

1. Go through each step in turn as a place to break. For each step, either confirm it follows from
   what precedes it (briefly say why), or identify precisely what additional, unjustified assumption
   it is smuggling in.
2. If you believe you have found a counterexample function, construct it as explicitly as you can
   (state `p`, state `f` or a rule for `f`, state `u`, and compute `A_u` and enough of the other
   `A_w` to get `|T_f-T_f|`) rather than arguing abstractly that one should exist.
3. If you get stuck partway, say exactly which step and exactly what you would need to resolve it —
   that is a fully valid answer.
4. Do not perform an exhaustive computer search or census at one small `p` as your primary method —
   this argument claims to hold for ALL odd primes `p`, and the class of counterexample most worth
   finding (if one exists) is a structural one, not a brute-force hit. A hand-checked tiny example
   (e.g. `p=3`) as illustration is fine, but is not the deliverable.

## 5. What to hand back

End with exactly one of:
- **CHAIN HOLDS** — you checked all eleven steps and found no gap; say briefly why each step you
  found least obvious in fact follows.
- **BREAKS AT STEP N** — name the step number, quote what it claims, and give the precise reason it
  does not follow (a missing case, an unjustified quantifier swap, an identity that does not actually
  say what it's used to say, etc.).
- **COUNTEREXAMPLE FOUND** — an explicit `(f, p, u)` with `|A_u(f)|=2` and `|T_f-T_f| < (2p-1)^2`,
  computed out.
- **I COULD NOT MAKE PROGRESS / I COULD NOT BREAK IT, HERE IS WHERE I GOT STUCK** — say plainly what
  you tried and where it stalled. This is a valued and useful answer, not a failure — we would much
  rather receive this than a confident claim of a break that does not hold up under reconstruction.

If anything above looks internally inconsistent, underspecified, or like notation you cannot resolve
(the `K_k`, `δ_{n0}`, `φ_k` items in section 2 are the most likely candidates), **say so explicitly**
— that is itself a valuable finding, not a reason to guess silently and move on.
