# Task: close (or refute) the one open case of a graph-theory reduction lemma

This is a genuine open question from an active research effort on a graph-theory conjecture. We
want a real proof attempt, or an explicit refutation, or an honest account of exactly where every
approach you try breaks. A cross-family reviewer checks load-bearing steps by construction, so an
"I could not close this" with the obstruction stated precisely is worth far more to us than a
fluent argument with a gap. Give reasoning and a verdict, not confidence language.

## 1. Definitions (self-contained — assume no other context)

All graphs are simple, finite, connected, undirected, and `C4`-free (no 4 distinct vertices
`a,b,c,d` with edges `ab,bc,cd,da`). For a graph `H`: `d_H(u,v)` is shortest-path distance,
`ecc_H(v) := max_u d_H(v,u)`, `rad(H) := min_v ecc_H(v)`. `path(H)` := the number of vertices in
the longest INDUCED path of `H` (a path with no chords — no edges between non-consecutive path
vertices). For `v ∈ V(H)`, `a(v) := α(H[N(v)])`, the independence number of the subgraph induced
on `v`'s open neighbourhood; `l(H) :=` the mean of `a(v)` over all `v ∈ V(H)`.

**THE CONJECTURE (the thing this whole research line is trying to prove, for every connected
`C4`-free graph `H`):**
```
path(H)  >=  rad(H) + floor(l(H))
```
This is open in general. The question below is about a REDUCTION strategy for it — an argument of
the form "if the conjecture holds for a smaller graph `G'`, it holds for a larger graph `G` built
from `G'` in a specific way" — not about proving the conjecture itself. **You may (and should) use
"the conjecture holds for `G'`" as a HYPOTHESIS when it appears below; you are not being asked to
prove the conjecture for `G'` itself.**

## 2. The multi-hair construction

`G` is built from a connected `C4`-free graph `G'` (with `n' := |V(G')| >= 2`) by attaching `k >= 1`
**hairs**: pairwise vertex-disjoint induced paths `x_i^1 - x_i^2 - ... - x_i^{h_i}` (length `h_i
>= 1` vertices each), where `x_i^1` is joined by an edge to a **root** `w_i ∈ V(G')`, the roots
`w_1,...,w_k` are **distinct** vertices of `G'`, and there are **no other edges** — the hairs
attach only at their roots and only to `G'`, not to each other. So `V(G) = V(G') ⊔ (all hair
vertices)`. Write `H := sum_i h_i` (total hair length), `l' := l(G')`, `r' := rad(G')`.

## 3. Tools you may use freely — already established, verified computationally, not to be
re-derived (you MAY re-derive them if useful, but they are given so you don't have to)

**(MH-ECC-1)**, eccentricity of a core vertex `c ∈ V(G')`:
```
ecc_G(c) = max( ecc_{G'}(c),  max_i ( d_{G'}(c, w_i) + h_i ) )
```

**(MH-ECC-2)**, eccentricity of a hair vertex `u = x_i^j` (the `j`-th vertex of hair `i`,
`1 <= j <= h_i`):
```
ecc_G(u) = max( h_i - j,  j + ecc_{G'}(w_i),  max_{m != i} ( j + d_{G'}(w_i, w_m) + h_m ) )
```

Both were derived by hand and certified against brute-force BFS on **2436** (graph, core-vertex)
pairs and **780** (graph, hair-vertex) pairs, over 252 hair configurations on 6 structured base
graphs, `k <= 3`, `h_i <= 3` — **0 mismatches**.

**IMPORTANT, and easy to get wrong: `rad(G)` need NOT be attained on `V(G')`, and can be strictly
below every core vertex's eccentricity.** Explicit certified example: `G' = K_2` (two adjacent
vertices `w_1, w_2`), one hair of length **100** at `w_1` and one hair of length **1** at `w_2`.
Then `ecc_G(w_1) = 100`, `ecc_G(w_2) = 101`, but **`rad(G) = 51`**, attained at a UNIQUE vertex
strictly inside the long hair (the vertex `x_1^{51}`, 51 steps out along the length-100 hair) —
`min` over `V(G')` of `ecc_G` is `100`, far above the true radius. **Do not assume the centre of
`G` lies in `G'`.**

**(MH-L)**, exact formula for `l(G)` (proven and machine-certified 252/252, matches exactly, not
an inequality):
```
l(G) = ( n' * l' + 2H ) / ( n' + H )
```
(Why, briefly, if useful: every hair-interior vertex has `a = 2`, every hair-tip vertex has
`a = 1`, and every root `c` has `a_G(c) = a_{G'}(c) + [c is some w_i]`; summing and dividing by
`n(G) = n' + H` gives the formula.)

**(MH-C)**, proven from (MH-L) alone (full proof below since it is short and you should be able to
verify it in one read):
```
floor( l(G) )  <=  floor( l(G') )        -- UNCONDITIONALLY, for every k >= 1 and every h_i >= 1
```
*Proof.* If `l' >= 2`: `l(G) <= l' <=> n'l' + 2H <= l'(n'+H) <=> 2H <= l'H <=> l' >= 2`. True by
hypothesis, so `l(G) <= l'`, hence `floor(l(G)) <= floor(l') `. If `l' < 2`: were `l(G) >= 2`, then
`n'l' + 2H >= 2n' + 2H`, i.e. `l' >= 2` — contradiction. So `l(G) < 2` too, and since `l' >= 1`
always (connected `G'` with `n' >= 2` — every vertex has `a >= ... ` at least giving mean `>= 1`
in this problem's standing setup, take as given), `floor(l(G)) <= 1 = floor(l')`. QED. This proof
uses NOTHING about `k`, `h_i`, or which vertices are roots — it is unconditional.

**(MH-I)**, PROVED, given as context (this is NOT what you are being asked to do — it is the
already-closed half of the problem, shown here so you see exactly what remains):
> If `rad(G) = rad(G')`, then "the conjecture holds for `G'`" implies "the conjecture holds for
> `G`".
*Proof.* `G'` is an induced subgraph of `G`, so `path(G) >= path(G')` always (any induced path of
`G'` is still an induced path of `G`, since no hair vertex is adjacent to any non-root vertex of
`G'` and the hairs add no edges inside `G'`). Combined with (MH-C):
`path(G) >= path(G') >= rad(G') + floor(l(G')) >= rad(G) + floor(l(G))`,
using `path(G') >= rad(G')+floor(l(G'))` (the conjecture for `G'`, given), `floor(l(G')) >=
floor(l(G))` (MH-C), and `rad(G')=rad(G)` (this case's hypothesis). QED. Certified on **88 of 88**
census instances with `rad(G)=rad(G')` (`k in {2,3}`, `h_i <= 3`, 5 structured base graphs, 16-
vertex cap for exact induced-path computation, not exhaustive).

## 4. THE OPEN CASE — this is what we want you to attack

**CASE II: `rad(G) > rad(G')`.** (MH-I)'s proof breaks immediately here, because it used
`rad(G')=rad(G)` in the last step — without it, `path(G) >= rad(G')+floor(l(G'))` says nothing
about `rad(G)`, which is strictly larger.

**Measured, NOT proved:** on a census of 112 fully-computed instances (5 structured base graphs,
`k ∈ {2,3}` hairs, `h_i <= 3`, roots among the first four vertices of each base, 16-vertex cap for
exact induced-path search — not exhaustive, a designed family only), **24 instances fall into Case
II, and the conjecture held on all 24**. That is a measurement on one family, not a proof, and it
is explicitly the one thing this line has not closed.

### A proposed reduction — OURS, not the paper's or any prior engine's; check it before using it

We (the humans coordinating this line) worked out the following sufficient condition ourselves,
specifically for this brief. It is NOT independently verified beyond the algebra shown — verify it
yourself as your first step, and if you find an error, say so and correct it before proceeding.

> **(MH-II), proposed target:** In the Case II setting (`rad(G) > rad(G')`),
> ```
> path(G)  >=  path(G') + ( rad(G) - rad(G') )
> ```

**Why (MH-II) would finish Case II, if true** (verify this chain yourself — it is short):
```
path(G) >= path(G') + (rad(G)-rad(G'))                          [ (MH-II) ]
        >= (rad(G')+floor(l(G'))) + (rad(G)-rad(G'))             [ conjecture for G', given ]
        =  rad(G) + floor(l(G'))
        >= rad(G) + floor(l(G))                                  [ (MH-C) ]
```
which is exactly the conjecture for `G`. So (MH-II) plus the already-proved (MH-C) and
`path(G)>=path(G')` would close Case II completely, by the same style of argument as (MH-I).

## 5. What we want from you

1. **First, verify the algebra in §4 yourself** (the chain of inequalities showing (MH-II) ⟹
   Case II closes). Confirm it is correct, or find the error if there is one.
2. **Attempt to prove (MH-II)** using (MH-ECC-1) and (MH-ECC-2) from §3. The natural approach: (a)
   get a lower bound on `path(G)` by exhibiting an explicit induced path of `G` — e.g. take a
   longest induced path of `G'` and try to extend it through the deepest hair(s), or build a new
   path that runs from deep in one hair, through `G'`, to deep in another hair — and (b) get an
   upper bound on `rad(G) - rad(G')` from (MH-ECC-1)/(MH-ECC-2) (remember: the centre of `G` need
   not be in `G'` — see the `K_2`+hairs(100,1) example in §3 — so bounding `rad(G)` may require
   reasoning about hair-interior vertices via (MH-ECC-2), not just core vertices via (MH-ECC-1)).
   Work out the general `k`-hair case if you can; if you can only do `k=1` or `k=2` hairs, report
   that as partial progress and say exactly what blocks the general case.
3. **If (MH-II) turns out to be FALSE, say so and give a counterexample** (an explicit `G'`, hair
   lengths and roots, with `path(G) < path(G') + (rad(G)-rad(G'))`) — and then tell us whether the
   CONJECTURE still holds for that example anyway (i.e. whether (MH-II) was merely a wrong choice
   of sufficient condition, not a sign that Case II itself is false) or whether it exposes an
   actual problem with Case II.
4. **If you can attack Case II directly, WITHOUT going through (MH-II)**, that is equally welcome
   — (MH-II) is a proposed route, not a required one. Any proof or refutation of "Case II: `rad(G)
   > rad(G')` and the conjecture for `G'` implies the conjecture for `G`" is what we actually want.

## 6. What to hand back

End with exactly one of:
- **CASE II CLOSED** — full proof that `rad(G) > rad(G')` plus the conjecture for `G'` implies the
  conjecture for `G`, in general (state exactly what hypotheses on `k`, `h_i`, etc. it needs, if
  any).
- **PARTIAL** — state precisely what you could prove (e.g. "(MH-II) holds for `k <= 2` hairs, proof
  attached, but the general `k` case needs [X] which I could not establish") and exactly where the
  general argument breaks.
- **CASE II APPEARS FALSE** — an explicit multi-hair `G` (base `G'`, roots, hair lengths) where
  `rad(G) > rad(G')`, the conjecture holds for `G'`, but the conjecture FAILS for `G` — this would
  be a significant finding (it would mean the multi-hair reduction strategy itself cannot work, not
  just that this particular sufficient condition was the wrong one), so be as explicit and checkable
  as you can (real graph, real distances, real independence-number computations, not a sketch).
