# Task: attempt to prove (or refute) — many centres ⟹ no vertex is radius-extremal from all of them (angle: eccentricity / compactness, NOT centre-counting)

This is a proof-attempt task on the same target as a parallel independent attempt, but we want a
genuinely DIFFERENT strategy from you: instead of counting/pigeonhole arguments directly on the
centre set, we want you to attack it through **eccentricity structure and "compactness"** of the
graph — i.e., relationships like `diam(H) ≤ 2·rad(H)`, how eccentricities of nearby vertices
relate to each other (`|ecc(u) - ecc(v)| ≤ d(u,v)`, a standard fact you may use and should verify),
and what it means structurally for a graph to have MANY vertices all achieving the minimum
eccentricity. If you find yourself falling back to pure centre-counting, that's fine if it's what
actually works — but please attempt the eccentricity/compactness route first and report honestly
if it doesn't get you there.

If you cannot complete it, say so plainly and report exactly where the argument breaks, or produce
an explicit counterexample if the claim is false. Give reasoning and a verdict, not confidence
language.

## Background (self-contained — identical framework to the parallel centre-counting attempt)

All graphs are simple, finite, connected, undirected. `d_H(u,v)` = shortest-path distance,
`ecc_H(v) := max_u d_H(v,u)`, `rad(H) := min_v ecc_H(v)`, `diam(H) := max_v ecc_H(v)`.
`Ctr(H) := { c ∈ V(H) : ecc_H(c) = rad(H) }` (the centre set).

**Standard fact you may use (verify it briefly in your own words before using it):** for any two
vertices `u,v`, `|ecc_H(u) - ecc_H(v)| ≤ d_H(u,v)`. (Reason: any vertex farthest from `u` is at
distance at most `d_H(u,v) + ecc_H(v)` from `v`'s perspective via the triangle inequality, etc. —
state this cleanly yourself.) Also standard: `rad(H) ≤ diam(H) ≤ 2·rad(H)`.

**Definition (radius-extremal for the centre set).** `w ∈ V(H)` is **radius-extremal for
`Ctr(H)`** if `d_H(c,w) = rad(H)` for EVERY `c ∈ Ctr(H)`.

**Structural hypotheses of the family under study (attempt the proof WITH these; a more general
proof without them, if you find one, is even better — say so explicitly):**
- `H` is `C4`-free: no 4 distinct vertices `a,b,c,d` with edges `ab,bc,cd,da`.
- `a(v) := α(H[N(v)])` (independence number of the subgraph induced on `v`'s open neighbourhood).
  `μ(H) := min_v a(v)`. Assume `μ(H) ≥ 2`.

## The claim to attack

> **If `|Ctr(H)|` is sufficiently large, then no vertex `w ∈ V(H)` is radius-extremal for
> `Ctr(H)`.**

No precise threshold is given — determining a workable threshold is part of the task. Calibrate
against this empirical evidence (not a proof, evidence only): on 248 designed hosts (built by
single-edge/single-vertex deletions from a `PG(2,5)`-incidence-graph core, `C4`-free, `μ≥2`), every
host had 50–55 centres, and among 2232 (vertex,host) instances satisfying the weaker condition
`ecc(w) = rad+1`, **0** also satisfied "radius-extremal for `Ctr(H)`" — never co-occurred, on this
one structured family (not exhaustive, not general).

## What we want from you — Angle B: eccentricity structure / compactness

1. Suppose `w` is radius-extremal for `Ctr(H)`: `d(c,w) = rad(H)` for every centre `c`. Consider
   TWO distinct centres `c_1, c_2 ∈ Ctr(H)`. Using the standard eccentricity-Lipschitz fact above
   applied at `c_1, c_2` (both have `ecc = rad(H)`), what constraint does this place on
   `d(c_1,c_2)`? Now bring `w` into it: `d(c_1,w) = d(c_2,w) = rad(H)`. Think of `c_1,c_2,w` as
   forming a geometric configuration and use the triangle inequality among all three pairwise
   distances, PLUS whatever you can derive about how `ecc(c_1), ecc(c_2)` constrain
   `d(c_1,c_2)` via nearby vertices, to see how much "room" there is for many centres to coexist
   with a single common radius-extremal `w`.
2. Try to formalize "the graph is compact/dense around the centre set" as: if `|Ctr(H)|` is large,
   are the centres necessarily close to each other (small diameter of the SUBGRAPH induced on
   `Ctr(H)`, or small pairwise distances within `H`)? If you can prove such a compactness
   statement (even a weak one) from `|Ctr(H)|` being large — using the `C4`-free and/or `μ(H)≥2`
   hypotheses if needed — then combine it with part 1's constraint to derive a contradiction with
   `w` being simultaneously far (distance exactly `rad(H)`, which is FIXED and can be large) from
   every centre in a tightly clustered set. Be careful: "many centres" does not obviously imply
   "centres are close together" in general graphs — you may need the `C4`-free/`μ≥2` hypotheses
   to get this, or you may find it's simply false and the right argument goes a different way;
   report honestly which.
3. As a sanity check, consider a VERTEX-TRANSITIVE example (e.g. a cycle `C_n`, or a more
   elaborate vertex-transitive `C4`-free graph) where EVERY vertex is a centre (`Ctr(H) = V(H)`,
   so `|Ctr(H)|` is as large as possible). Does such a graph ever have a vertex radius-extremal for
   the whole vertex set? Work this out explicitly for at least one concrete vertex-transitive
   family and report what you find — this may directly settle whether the claim can even be true
   in the stated generality, or whether it critically needs some hypothesis (like `C4`-freeness or
   the specific structured family) that rules out high-symmetry counterexamples.

Structure your answer as: (1) the eccentricity/compactness argument and how far it gets, (2) the
vertex-transitive sanity check and what it shows, (3) your best threshold or a clear statement of
why the eccentricity route does not close the claim.

End with exactly one of: **PROOF COMPLETE (state the threshold and full argument)**, **PARTIAL
(state what you established and the precise remaining gap)**, or **CLAIM APPEARS FALSE (give an
explicit graph, ideally an infinite family with `|Ctr(H)| → ∞`, containing a radius-extremal
vertex)**.
