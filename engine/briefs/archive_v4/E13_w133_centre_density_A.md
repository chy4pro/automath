# Task: attempt to prove (or refute) — many centres ⟹ no vertex is radius-extremal from all of them (angle: direct centre-counting)

We want a genuine proof attempt of a precise graph-theory claim that arose from computational
evidence but has never been proved. If you cannot complete it, say so plainly and report exactly
where the argument breaks, or produce an explicit counterexample if it is false. An honest
"I could not close this" or a real counterexample is far more valuable to us than a hand-wavy
argument. Give reasoning and a verdict, not confidence language.

## Background (self-contained)

All graphs are simple, finite, connected, undirected. For a graph `H`, `d_H(u,v)` is shortest-path
distance, `ecc_H(v) := max_u d_H(v,u)`, `rad(H) := min_v ecc_H(v)`.

**Definition (centre set).** `Ctr(H) := { c ∈ V(H) : ecc_H(c) = rad(H) }`, the set of "central"
vertices.

**Definition (radius-extremal for the centre set).** A vertex `w ∈ V(H)` is **radius-extremal for
`Ctr(H)`** if, for EVERY centre `c ∈ Ctr(H)`, `d_H(c, w) = rad(H)` — i.e. `w` sits at distance
exactly `rad(H)` from every single centre simultaneously (the maximum possible distance any
centre-vertex `c` can have to anything, since `ecc(c)=rad(H)` means `rad(H)` IS the farthest any
vertex is from `c`).

**Why this matters (context, not something you need to verify):** if a graph `H = G'` has a vertex
`w` that is radius-extremal for `Ctr(G')`, then attaching a single pendant vertex at `w` provably
increases the radius by exactly 1 (`rad(G'+\text{pendant at }w) = rad(G')+1`) — this is an
already-established fact (an "if and only if", called (RAD-1P) on this line) that you may take as
given; it is the reason this question matters, not something to re-derive here.

**Additional structural hypotheses used in the family under study (you should attempt the proof
WITH these hypotheses; if you can prove a more general version without them, that is even better —
say so explicitly):**
- `H` is `C4`-free: no 4 distinct vertices `a,b,c,d` with edges `ab,bc,cd,da`.
- For `v ∈ V(H)`, `a(v) := α(H[N(v)])` (independence number of the subgraph induced on `v`'s open
  neighbourhood). `μ(H) := min_v a(v)`. Assume `μ(H) ≥ 2`.

## The claim to attack

> **If `|Ctr(H)|` is sufficiently large, then no vertex `w ∈ V(H)` is radius-extremal for
> `Ctr(H)`.**

This is deliberately NOT given a precise threshold — that is part of what we want you to
determine. Below is the empirical evidence that motivated the claim; use it to calibrate what
threshold (if any) you think is the right one to attempt, and say explicitly what threshold your
proof actually needs.

**Measured evidence (a census on ONE designed family, NOT exhaustive, NOT a proof):** on 248
connected, `C4`-free, `μ ≥ 2` host graphs (built by single-edge/single-vertex deletions from a
`PG(2,5)`-incidence-graph core, so a specific structured family, not general graphs), every host
had between 50 and 55 centres (mean 51.25). Among these hosts, 2232 (vertex, host) instances had
`ecc(w) = rad+1` for some vertex `w` at all — a first, weaker condition — but among exactly those,
**0** were also radius-extremal for the centre set (i.e., the SECOND, stronger condition never
co-occurred with the first, in this designed family). The authors explicitly note this is a
statement about ONE family, not a general theorem, and that no proof or general counterexample
search was attempted.

## What we want from you — Angle A: direct centre-counting / pigeonhole

Attempt a proof via counting and pigeonhole-type arguments on the centre set directly:
1. Start with the smallest interesting case: suppose `|Ctr(H)| ≥ 2`, i.e. there exist two DISTINCT
   centres `c_1 ≠ c_2`. Suppose for contradiction some `w` is at distance exactly `rad(H)` from
   BOTH `c_1` and `c_2`. What can you derive from the triangle inequality applied to `c_1, c_2, w`
   and to `c_1, c_2` directly (`d(c_1,c_2) ≤ 2·rad(H)`, and also `d(c_1,c_2) ≤ ecc(c_1) = rad(H)`
   since `c_2` cannot be farther from `c_1` than `c_1`'s eccentricity)? Is 2 centres already enough
   to derive a contradiction, or can you construct an explicit small example (any graph, need not
   be `C4`-free or satisfy `μ≥2`) with exactly 2 centres and a vertex radius-extremal for both?
   Work this out concretely — do not assume either way.
2. If 2 centres is not enough, push the counting further: try to show that as `|Ctr(H)|` grows,
   the SET of vertices that could simultaneously be at distance `rad(H)` from every centre shrinks,
   by intersecting, for each centre `c`, the "distance-exactly-`rad(H)`-from-`c`" set (a subset of
   `V(H)`), and using some structural fact (e.g., a counting/degree bound, or the `C4`-free +
   `μ≥2` hypotheses) to show these sets cannot all have a common element once there are "enough"
   of them. Try to find the smallest threshold `k` such that you can prove "`|Ctr(H)| ≥ k` ⟹ no
   radius-extremal `w`" — even if `k` turns out to be much smaller or larger than the 50–55 seen
   empirically, report the exact threshold your proof achieves and where the argument would break
   for smaller `k`.
3. Explicitly test whether the `C4`-free and `μ(H) ≥ 2` hypotheses are actually used anywhere in
   your argument. If your proof works without them, say so — that would be a strictly stronger and
   more useful result.

Structure your answer as: (1) your attempted threshold `k` and the counting argument, (2) where it
succeeds or where it needs a case split you cannot close, (3) any explicit small counterexamples
you found along the way (even if they don't refute the "large `|Ctr(H)|`" version, a counterexample
at small `|Ctr(H)|` is useful data).

End with exactly one of: **PROOF COMPLETE (state the threshold k and full argument)**, **PARTIAL
(state the best threshold you could prove, and where it breaks for smaller counts)**, or **CLAIM
APPEARS FALSE (give an explicit graph with arbitrarily large `|Ctr(H)|`, or a specific large
example, containing a radius-extremal vertex)**.
