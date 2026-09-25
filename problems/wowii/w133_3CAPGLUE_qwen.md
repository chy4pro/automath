# w133 pocket 2 — (FAR-2), what (3CAP-GLUE) reduces to at rad>=5 — v4 — Qwen3.8-Max harvest

Source conversation: https://chat.qwen.ai/c/c92d26d5-ca58-4443-92ff-55965adbd83c (queue row Q32, v3/v4 LIVE)
Dispatched: qwen-driver-r15, 2026-08-22 09:13 CDT (model confirmed Qwen3.8-Max via ref-click,
checkmark+badge screenshot before paste; single slow `pbcopy`+`cmd+V` of the
driver-instructions-stripped body, 18468B, landed inline as textarea text, not an attachment;
byte-check freeze discipline held on the source brief before and after paste — no mid-dispatch
race).
Brief: `prompts/w133_r11_3CAPGLUE.md`, brief version **v4** (self-contained; PART1 definitions,
PART2 facts F1-F12 incl. the sharpened F5 seed and the new F12 no-far-end-hypothesis fact, PART3
targets — Problem A (PEEL-RAD), Problem B (FAR-2, equivalent to Problem A per the brief's own
framing), Problem C (secondary); PART4 mandatory control section incl. W1/W2). Qwen is SOLVER
here (TIGHT inversion), not judge.

Completion confirmed independently by two separate rounds: (1) qwen-poll-haiku-r1, 09:49:55 CDT,
via action-icon row present + `get_page_text` byte-identical across two 10s-spaced polls; (2)
this harvest round (qwen-harvest-r16, `date` 2026-08-22 09:54 CDT), re-confirmed via the same
two-signal protocol — `find` located the "Copy" button in the action-icon row under the final
assistant message, and two `get_page_text` calls 10 seconds apart returned byte-identical
content (no further streaming). No CAPTCHA or verification UI encountered. Chrome browser
session was held under lease `gemini-shootout-r1` (unrelated concurrent task) for the entire
duration of this harvest; this round entered WITHOUT acquiring the Chrome lease (read-only
navigation of an already-open tab, tabId 2130629957, no conflict with the Gemini shoot-out),
mirroring the precedent set by qwen-poll-haiku-r1 earlier this same lease-holding period. No tab
was closed.

**VERDICT: REFUTED**

Everything below is UNVERIFIED engine output; owner-w133 adjudicates line by line before any
adoption.

**What the refutation claims to refute (one sentence, no judgment):** the model claims to refute
Problem B / (FAR-2) — the claim that some geodesic of length >= rad(G) has a usable
side-neighbour with a>=4 at one end AND a>=2 at the other end — by exhibiting an explicit
54-vertex C4-free graph (PG(2,4) incidence graph with six 2-vertex pendant hairs) with l=13/3>4,
rad=5, in which every non-3-capped geodesic of length >= rad has an a=1 (leaf) vertex at its far
end; the model explicitly states this same graph does NOT refute Problem A, since it separately
exhibits an induced 9-vertex path (path(G)=9=rad(G)+4) inside the same graph.

**Numbers/witness-object note (preserved exactly below in the verbatim harvest, flagged here for
quick reference):** core = PG(2,4) point/line incidence graph over GF(4) (21 points + 21 lines =
42 core vertices), six named attachment vertices `P_x,P_y,P_z,L_x,L_y,L_z` each given a 2-vertex
pendant hair (`s—h_s—f_s`), total `n = 54`; `Σ_v a(v) = 234`, `l(G) = 234/54 = 13/3`; `rad(G) =
5`, `diam(G) = 7`; the exhibited induced 9-path is `P0—L1—P1—L2—P2—L3—P3—L4—P4` with explicit
GF(4) point/line coordinates and dot-product incidence checks for every consecutive and
non-consecutive pair. Peeling all a=1 vertices from this graph is claimed to leave exactly the
bare PG(2,4) incidence graph with rad=3 (a drop from 5), which the model uses to refute route A1
(peeling preserves radius >= 5) without claiming a general A2 exchange lemma.

---

## Verbatim harvest (via get_page_text)

You are solving a hard research-level graph theory problem from a competition. No internet, no
literature lookup, no external tools: work only from the definitions and facts below and from
your own reasoning. If you want to cite a named theorem, state it explicitly and prove it, or
mark it clearly as an assumption.

**Deliverable format (read first).** Begin with one line:
`VERDICT: SOLVED-PEELRAD | SOLVED-FAR2 | REFUTED | PARTIAL | OBSTRUCTION-IDENTIFIED`,
then a 5-line summary, then the full argument. End with a self-audit listing (i) every step
you are less than certain about, (ii) every place you used a hypothesis (name which one), and
(iii) what you tried and failed. **Every graph you name must come with an explicit edge list**,
or an explicit incidence/group recipe with the derivation shown. A description is not
verifiable and will not be adopted.

**Persistence.** Do not stop at the first obstruction: name it precisely, then take the next
route. Attack from at least four angles: (1) direct — re-choose the geodesic so that its far
end has a large `a`; (2) counting — play the global abundance fact F3 against the set of
possible far ends; (3) the peeling/hair-exchange route (Problem A below); (4) counterexample hunting — a
graph where **every** geodesic of length ≥ rad that has a high-`a` usable side-neighbour at one
end has an `a = 1` vertex at the other. Report the obstruction hit on each.

---

## PART 1 — Definitions

All graphs are finite, simple, connected, undirected. `n` = |V|, `N(v)` = neighbours of `v`,
`d(v) = |N(v)|`.

* **C4-free** := **no two distinct vertices have two common neighbours** (equivalently: no
4-cycle as a **subgraph**, not merely no induced one). Use this strong form.
* `a(v)` := independence number of `G[N(v)]`. C4-free ⟹ `G[N(v)]` is a **matching plus
isolated vertices** ⟹ **`a(v) = d(v) − t(v)`** (`t(v)` = triangles through `v`);
"**`u`'s component**" always means `u`'s component of that matching-plus-isolates graph.
* `l(G) := (1/n)·Σ_v a(v)`; so `l(G) > 4 ⟺ Σ_v a(v) > 4n`. `μ(G) := min_v a(v)`.
* `ecc`, `rad`, `diam` as usual; **`path(G)`** := number of **vertices** of a longest induced
path; a **geodesic** is a shortest path (hence induced).
* A **usable side-neighbour** of the end `u₀` of a geodesic `u₀ … u_d` is `x ∈ N(u₀)` lying
**outside `u₁`'s component of `G[N(u₀)]`**; one exists iff `a(u₀) ≥ 2`.
* A geodesic is **3-capped at the end `u₀`** if every usable side-neighbour of `u₀` has
`a ≤ 3`. `G` is **peripherally 3-capped** if every geodesic of length ≥ `rad(G)` is 3-capped
at both ends.

## PART 2 — Facts you may use freely
*(owner-proved or owner-machine-verified; each carries its **tightness verdict** — a non-tight
fact silently propagates into everything that leans on it.)*

**F1.** C4-free ⟹ `a(v) = d(v) − t(v)` and `⌈d(v)/2⌉ ≤ a(v) ≤ d(v)`. *Tight: both bounds
attained (perfect matching / triangle-free).*

**F2 (mass).** `l > 4` ⟹ `Σ_{v : a(v) ≥ 3}(a(v) − 2) > 2n`. *Tight: consumes ONLY `l > 4`.*

**F3 (abundance).** `l > 4` ⟹ `Σ_{v : a(v) ≥ 4}(a(v) − 3) > n`. *Tight: consumes ONLY
`l > 4`; it places `a ≥ 4` vertices **somewhere**, never in a named position — that gap
between global abundance and positional placement is the recurring difficulty on this line.*

**F4 (the cap-break — PROVED this cycle, and it is your starting point).** A connected
C4-free graph that is peripherally 3-capped has `l < 4`. Contrapositive, which is how you will
use it:
> **`G` connected, C4-free, `l(G) > 4` ⟹ there is a geodesic `P` of length ≥ `rad(G)` and an
> end `u₀` of `P` carrying a usable side-neighbour `x` with `a(x) ≥ 4`** (in particular
> `a(u₀) ≥ 2`).
*Tight: it is radius-uniform (no `rad ≥ 5` anywhere in its proof) and it gives you the
side-neighbour at ONE end only — it says nothing whatever about the other end. That silence
is exactly the target below.*

**F5 (the seed, in its SHARPENED form — owner-proved, and the sharpening is this round's).**
C4-free, geodesic `u₀ … u_d` with **`d ≥ 5`**, **`a(u₀) ≥ 2`**, **`a(u_d) ≥ 2`**, and some
usable side-neighbour `x` of `u₀` with **`a(x) ≥ 4`** ⟹ **`path(G) ≥ d + 4`**.
*Proof.* Take `y ∈ N(u_d)` outside `u_{d−1}`'s component (exists as `a(u_d) ≥ 2`). `G[N(x)]`
has ≥ 4 components; `u₀`'s is one; `x ≁ u₂` (else `u₀,u₂` share `x,u₁`) and `x ≁ u₃`
(distance), so `|N(x)∩N(u₂)| ≤ 1`, `|N(x)∩N(u₃)| ≤ 1` kill ≤ 1 component each; take `w` in a
survivor. Then `w ≁ u₀` (component), `w ≁ u₁` (else `w–x–u₀–u₁–w` is a C4), `w ≁ u₂,u₃`
(choice), `dist(w,u_i) ≥ i − 2 ≥ 2` for `i ≥ 4`, `dist(w,y) ≥ d − 3 ≥ 2`,
`dist(x,y) ≥ d − 2 ≥ 3`. So `w,x,u₀,…,u_d,y` is an induced path on `d + 4` vertices. ∎
*Tight, and read this carefully because it is the point of the whole brief: the construction
**never uses a third component of `G[N(u₀)]`**, so the older form of this fact — which
demanded `a(u₀) ≥ 3` — was carrying a redundant hypothesis at `d ≥ 5`. The redundancy is
real and was machine-tested non-vacuously (120 certified frames with `a(u₀) = 2` exactly,
`d ≥ 5`, 0 failures). It is NOT redundant at `d = 3, 4`, where the known proofs need a third
component. **What remains unbought at `d ≥ 5` is therefore the FAR end, `a(u_d) ≥ 2`.***

**F6 (low-`d` companions — ADOPTED-pending-independent-judge; use only for the secondary
problem, and flag any use).** The same conclusion holds at `d = 4` with `a(u₀) ≥ 3`,
`a(u₄) ≥ 2`, `a(x) ≥ 4`; and at `d = 3` with `a(u₀) ≥ 3`, `a(u₃) ≥ 2`, `a(x) ≥ 4` **plus** the
extra hypothesis that some usable side-neighbour `y` of `u₃` has `y ≁ x`. *Status: proofs
complete and owner-re-derived; an independent adversarial pass is in flight. Tight in the
relevant direction: both genuinely consume `a(u₀) ≥ 3`.*

**F7 (peeling).** Deleting a vertex with `a(v) = 1` preserves connectivity, C4-freeness and
the distances among the survivors. The mass bookkeeping depends on the **type** of the deleted
vertex, and getting this wrong is a known trap: for a **leaf** `v` (attached at `p`), `Σa` drops
by 2 (`v`'s own 1, and 1 at `p`, which loses an isolated vertex of `G[N(p)]`); for a
**triangle-leaf** `v` (with `N(v) = {p,q}`, `p ~ q`), `Σa` drops by only **1** — `p` and `q`
each lose one degree **and** one triangle, so `a = d − t` is unchanged at both. With `n ↦ n−1`,
`Σa − 4n` therefore rises by **+2 (leaf)** or **+3 (triangle-leaf)** — in both cases it rises,
so **peeling preserves `l > 4`**. Iterating gives a subgraph
with `a(v) ≥ 2` everywhere. *Tight: it preserves `l > 4` and distances among survivors, but
**it is NOT known to preserve `rad ≥ 5`** — deleting peripheral material can shrink the
radius, and no bound on the drop is proved. That gap is Problem A below.*

**F8 (radius base case).** C4-free and `rad ≤ 1` ⟹ `l < 2`; so no `l > 4` graph has
`rad ≤ 1`. *Tight: stars approach `l = 2`.*

**F9 (`n` floor).** No C4-free graph with `l > 3` exists on `n ≤ 13` vertices (exhaustive).
*Tight: a floor, not a characterisation.*

**F10 (verified controls — owner-built and verified this round; recompute anything you rely
on).**
* **W2 — the hard control, and the first graph known to sit in the hard window.**
`G = Cay(PSL(2,11), S)` with `S = {g, g⁻¹}` for the three `SL(2,11)` matrices
`[5 0; 2 9]`, `[1 5; 0 1]`, `[1 6; 10 6]` (elements taken mod `±I`). Verified: `n = 660`,
connected, **6-regular**, **triangle-free**, **C4-free**, hence `a(v) = 6` for every `v` and
**`l = 6 > 4`**; **`rad = diam = 5`**; a certified induced path on **168** vertices.
*Why it matters: `diam + 1 = 6 < rad + 4 = 9`, so the cheap bound `path ≥ diam + 1` does NOT
settle it — every argument you write must execute on W2.*
* **W1 — the low-`μ`, large-radius control.** Two copies of the PG(2,5) point/line incidence
graph (each: 62 vertices, 6-regular, bipartite, C4-free, all `a = 6`), joined by a path with
5 new internal vertices attached at two distinct vertices of each copy. Verified: `n = 129`,
C4-free, **`l = 252/43 = 5.86 > 4`**, **`rad = 6`**, `diam = 12`, `min_v a(v) = 2`.
*Why it matters: it shows `l > 4` graphs need not be regular or high-`μ`, and it is where
`a = 2` vertices and long geodesics coexist. It is `diam`-heavy, so `path ≥ diam + 1`
settles it — it is a legality control, not a hard one.*
* **PG(3,2) point/line incidence graph** (= STS(15) incidence): `n = 50`, C4-free,
`a(point) = 7`, `a(line) = 3`, `l = 4.2 > 4`, **`rad = 3`**, `diam = 4`.
*Why it matters: `l > 4` with `rad < 5` — the control on which the target's own hypothesis
fails, i.e. your amendment-1 non-execution example is available for free here.*
* **PG(2,3) incidence graph**: `n = 26`, 4-regular, C4-free, every `a = 4`, **`l = 4.0` — NOT
`> 4`**, `rad = diam = 3`. *The below-threshold control: your class-membership check must
come out NEGATIVE on it.*

**F11 (what is already proved, and it is why this brief is narrow — read before choosing a
route).** F4 + F5 already settle everything except the `a = 1` case:
> **If `G` is connected, C4-free, `l(G) > 4`, `rad(G) ≥ 5` and `μ(G) ≥ 2` (no vertex of
> `a`-value 1), then `path(G) ≥ rad(G) + 4`.**
*Proof.* F4 gives a geodesic `u₀ … u_d` with `d ≥ rad ≥ 5` and a usable side-neighbour `x` of
`u₀` with `a(x) ≥ 4`. `μ ≥ 2` gives `a(u₀) ≥ 2` and `a(u_d) ≥ 2` for free, and by F5 that is
all the seed needs. Apply F5: `path ≥ d + 4 ≥ rad + 4`. ∎
*Tight: certified end-to-end on W1 and W2 (50 runs: a real cap-break geodesic located on the
graph, the F5 path built and verified chord-free); on **W2 the built path has exactly
`9 = rad + 4` vertices**, so the mechanism has no slack to spare. **Consequence: the ONLY
remaining case is a graph that HAS a vertex with `a(v) = 1` — a leaf, or a vertex whose whole
neighbourhood is one edge of a triangle. Everything below is about that case and nothing
else.***

**F12 (the second half of what is already proved — this is the sharpest fact in the brief).**
C4-free, geodesic `u₀ … u_d` with **`d ≥ 6`**, `a(u₀) ≥ 2`, and a usable side-neighbour `x` of
`u₀` with `a(x) ≥ 4` ⟹ **`path(G) ≥ d + 3`, with NO hypothesis on `a(u_d)`.**
*Proof.* If `a(u_d) ≥ 2`, F5 gives `d+4`. Otherwise `a(u_d) = 1`, so `N(u_d)` is `{u_{d−1}}`
(leaf) or `{u_{d−1}, q}` with `q ~ u_{d−1}` (triangle-leaf). **Truncate** to `u₀ … u_{d−

Thinking completed
VERDICT: REFUTED
Summary:
I refute Problem B (FAR-2) with an explicit finite simple connected C4-free graph G with l(G)=13/3>4, rad(G)=5, in which every geodesic of length at least 5 that has a usable side-neighbour of a≥4 at one end has an a=1 vertex at the other end.
The graph is the incidence graph of PG(2,4) with two-vertex pendant hairs attached at three non-collinear points and three non-concurrent coordinate lines; the full incidence recipe and all computations are below.
This graph realises exactly Problem A's "last configuration": the only non-3-capped geodesics of length ≥rad are core-to-leaf geodesics of length exactly 5, with the leaf (a=1) opposite the cap-breaking end.
Nevertheless I exhibit an induced 9-vertex path, so path(G)≥9=rad(G)+4; therefore this is not a counterexample to Problem A, only a counterexample to the FAR-2 route.
The peeling route is obstructed: peeling all a=1 vertices leaves the PG(2,4) incidence graph, whose radius is 3, so A1 is false here; I did not prove a general A2 exchange.
Full argument
I lead with the counterexample to Problem B, because it is the complete deliverable and it sits inside the exact configuration described in Problem A.
1. The graph G
1.1 The core: incidence graph of PG(2,4)
Let F = GF(4) = {0,1,α,α^2} with α^2 = α + 1; equivalently α^3=1 and the field has characteristic 2, so subtraction equals addition.
A point is a 1-dimensional subspace of F^3, represented by a nonzero triple [x:y:z], with scalar multiples identified.
A line is a 2-dimensional subspace, represented by a nonzero coefficient triple [a:b:c], with scalar multiples identified, and interpreted as the equation
a x + b y + c z = 0.
A point [x:y:z] is incident with a line [a:b:c] iff
a x + b y + c z = 0.
There are 21 points and 21 lines. The core graph H is the bipartite incidence graph:
V(H) = {points} ∪ {lines},
E(H) = { P L : point P is incident with line L }.
This is the standard point/line incidence graph of the projective plane PG(2,4).
1.2 The six attachment vertices in the core
Choose the three coordinate points
P_x = [1:0:0],
P_y = [0:1:0],
P_z = [0:0:1],
and the three coordinate lines
L_x = [1:0:0] (equation x = 0),
L_y = [0:1:0] (equation y = 0),
L_z = [0:0:1] (equation z = 0).
The three points are non-collinear. The three lines are not concurrent: L_x ∩ L_y = P_z, but P_z ∉ L_z.
Let
S = {P_x, P_y, P_z, L_x, L_y, L_z}.
1.3 The hairs
For every s ∈ S, add two new vertices:
h_s (hair internal vertex),
f_s (hair leaf).
Add exactly two edges for each s:
s — h_s — f_s.
No other edges are added.
Thus G has
|V(G)| = 42 + 6·2 = 54.
The explicit added edge list is:
P_x—h_P_x—f_P_x
P_y—h_P_y—f_P_y
P_z—h_P_z—f_P_z
L_x—h_L_x—f_L_x
L_y—h_L_y—f_L_y
L_z—h_L_z—f_L_z
2. Validation of the defining constraints
2.1 Simple, finite, connected
G is finite and simple by construction. The core H is connected because PG(2,4) is a projective plane: any point is incident with lines, any two points are joined by a line, and any two lines meet. Each hair is attached to a core vertex, so G is connected.
2.2 C4-free
In H, no two vertices have two common neighbours:
two distinct points lie on exactly one common line;
two distinct lines meet in exactly one point;
a point and a line are in opposite bipartition classes, so they have no common neighbour.
Therefore H contains no C4 as a subgraph.
The added hairs cannot create a C4:
each leaf f_s has degree 1;
each internal hair vertex h_s has neighbours {s, f_s}, and s is not adjacent to f_s;
h_s has no neighbours in the core except s;
two distinct hair vertices from different hairs have no common neighbour;
if h_s and a core vertex t ≠ s have a common neighbour, it is only s, and only when s~t.
Thus no pair of distinct vertices gains two common neighbours. G is C4-free.
2.3 Triangle-free, hence a(v)=d(v)
H is bipartite, hence triangle-free. The added hairs are pendant paths of length 2, and no edge joins a hair internal vertex to any core vertex except its root. Thus G is triangle-free.
Therefore for every vertex v,
a(v) = d(v)
by F1, or directly because G[N(v)] is an empty graph.
2.4 Exact a-values and l(G)
Core degrees:
unattached core vertices: degree 5, so a=5;
attached core vertices in S: degree 6, so a=6.
Hair vertices:
each internal h_s: degree 2, so a=2;
each leaf f_s: degree 1, so a=1.
There are:
6 attached core vertices;
42−6=36 unattached core vertices;
6 internal hair vertices;
6 leaves.
Hence
Σ_v a(v)
= 6·6 + 36·5 + 6·2 + 6·1
= 36 + 180 + 12 + 6
= 234.
Since n=54,
l(G) = 234 / 54 = 13/3 > 4.
3. Radius and diameter of G
3.1 Distances inside the core H
In the incidence graph of a projective plane:
two distinct points have distance 2;
two distinct lines have distance 2;
a point and an incident line have distance 1;
a point and a non-incident line have distance 3.
Thus
diam(H) = 3.
3.2 Every core vertex has eccentricity 5 in G
Let v be a core point. Since the three selected lines L_x,L_y,L_z have empty common intersection, v is not incident with at least one of them. Say v ∉ L. Then in H,
dist_H(v,L) = 3.
In G, the leaf f_L is at distance
dist_G(v, f_L) = dist_H(v,L) + 2 = 5.
No vertex is farther from v: core vertices are at distance at most 3, internal hair vertices at distance at most 4, leaves at distance at most 5. Hence
ecc_G(v) = 5.
The same argument applies to a core line M: the three selected points P_x,P_y,P_z are non-collinear, so no line contains all three. Thus some selected point P is not incident with M, giving
dist_H(P,M)=3,
dist_G(f_P,M)=5,
and again ecc_G(M)=5.
So every core vertex has eccentricity exactly 5.
3.3 Hair vertices have eccentricity at least 5
Let s ∈ S. If s is a selected point, there is a selected line L∈S not incident with s; if s is a selected line, there is a selected point P∈S not incident with s. In either case there is some t∈S with
dist_H(s,t)=3.
Then
dist_G(h_s, f_t) = 1 + 3 + 2 = 6,
so ecc_G(h_s) ≥ 6.
Also
dist_G(f_s, f_t) = 2 + 3 + 2 = 7,
so ecc_G(f_s) ≥ 7.
Thus no hair vertex has eccentricity below 5.
3.4 Radius and diameter
Since all core vertices have eccentricity 5, and all hair vertices have eccentricity at least 5,
rad(G) = 5.
For diameter, take P_x and L_x. They are not incident, so dist_H(P_x,L_x)=3. Hence
dist_G(f_{P_x}, f_{L_x}) = 2 + 3 + 2 = 7.
No distance can exceed 7, because the core diameter is 3 and each hair has depth 2. Therefore
diam(G) = 7.
4. Geodesics of length at least rad(G)=5
Let:
C = core vertices;
P = internal hair vertices h_s;
L = leaves f_s.
The a-values are:
a(C) ∈ {5,6},
a(P) = 2,
a(L) = 1.
Because G is triangle-free, G[N(v)] is edgeless for every v. Thus for a geodesic ending at v with penultimate neighbour z, every neighbour of v other than z is a usable side-neighbour.
4.1 Distance table
For s,t ∈ S, write δ(s,t)=dist_H(s,t).
endpoint types

distance in G

maximum

C–C

dist_H

3

C–h_s

dist_H(C,s)+1

4

C–f_s

dist_H(C,s)+2

5

h_s–h_t

δ(s,t)+2 if s≠t

5

h_s–f_t

1 if s=t; otherwise δ(s,t)+3

6

f_s–f_t

δ(s,t)+4 if s≠t

7
Therefore geodesics of length at least 5 can only be of the following types:
C–L of length 5;
P–P of length 5;
P–L of length 5 or 6;
L–L of length 5, 6, or 7.
4.2 Capping behaviour
C–L, length 5
Such a geodesic has the form
v ... s — h_s — f_s,
where v is a core vertex with dist_H(v,s)=3.
At the core end v, the penultimate neighbour is a core neighbour. Since v has at least five core neighbours, there are at least four other core neighbours. Each has a=5 or 6. Hence v has usable side-neighbours of a≥4. So this geodesic is not 3-capped at the core end.
At the leaf end f_s, a=1, so there is no usable side-neighbour. It is 3-capped vacuously.
Thus these are non-3-capped geodesics, and the end opposite the cap-breaking core end has a=1.
P–P, length 5
Such a geodesic has the form
h_s — s ... t — h_t,
with δ(s,t)=3. At h_s, the penultimate neighbour is s; the only other neighbour is f_s, which has a=1. Similarly at h_t. Thus both ends are 3-capped.
P–L, length 5 or 6
If the end is an internal hair vertex h_s, the shortest path uses the core neighbour s as the penultimate neighbour. The only other neighbour is f_s, with a=1. Hence the P end is 3-capped. The leaf end is also 3-capped because a=1.
L–L, length 5, 6, or 7
Both ends are leaves with a=1, so both ends are 3-capped.
4.3 Conclusion for Problem B
The only geodesics of length at least 5 that are not 3-capped at an end are the C–L geodesics of length 5. For every such geodesic, the end opposite the cap-breaking core end is a leaf with a=1.
Therefore there is no geodesic of length at least rad(G)=5 with:
a usable side-neighbour of a≥4 at one end, and
a≥2 at the other end.
This refutes Problem B (FAR-2).
5. Relation to Problem A
The graph satisfies the exact "last configuration" described in Problem A:
every geodesic of length at least rad(G)=5 that is not 3-capped at an end has length exactly 5;
the end opposite the non-3-capped end has a=1.
However, it does not refute Problem A, because it still has an induced path on 9 = rad(G)+4 vertices.
6. Explicit induced path on 9 vertices
I now exhibit an induced path entirely inside the core H.
Use the following points and lines in PG(2,4):
P0 = [1:0:0]
L1 = [0:1:0] (y = 0)
P1 = [0:0:1]
L2 = [1:1:0] (x + y = 0)
P2 = [1:1:0]
L3 = [1:1:1] (x + y + z = 0)
P3 = [0:1:1]
L4 = [α:1:1] (α x + y + z = 0)
P4 = [1:α:0]
The path is
P0 — L1 — P1 — L2 — P2 — L3 — P3 — L4 — P4.
This has 9 vertices.
6.1 Consecutive incidences
Check dot products in GF(4):
P0·L1 = [1:0:0]·[0:1:0] = 0.
P1·L1 = [0:0:1]·[0:1:0] = 0.
P1·L2 = [0:0:1]·[1:1:0] = 0.
P2·L2 = [1:1:0]·[1:1:0] = 1+1 = 0.
P2·L3 = [1:1:0]·[1:1:1] = 1+1+0 = 0.
P3·L3 = [0:1:1]·[1:1:1] = 0+1+1 = 0.
P3·L4 = [0:1:1]·[α:1:1] = 0+1+1 = 0.
P4·L4 = [1:α:0]·[α:1:1] = α + α + 0 = 0.
So all consecutive edges exist.
6.2 No non-consecutive incidences
We need only check point-line pairs that are not consecutive.
For P0 = [1:0:0]:
P0·L2 = 1 ≠ 0,
P0·L3 = 1 ≠ 0,
P0·L4 = α ≠ 0.
For P1 = [0:0:1]:
P1·L3 = 1 ≠ 0,
P1·L4 = 1 ≠ 0.
For P2 = [1:1:0]:
P2·L1 = 1 ≠ 0,
P2·L4 = α + 1 = α^2 ≠ 0.
For P3 = [0:1:1]:
P3·L1 = 1 ≠ 0,
P3·L2 = 1 ≠ 0.
For P4 = [1:α:0]:
P4·L1 = α ≠ 0,
P4·L2 = 1 + α = α^2 ≠ 0,
P4·L3 = 1 + α = α^2 ≠ 0.
All non-consecutive point-line pairs are non-incident. Since the graph is bipartite, same-type pairs are never adjacent. Therefore the displayed 9-vertex path is induced.
Thus
path(G) ≥ 9 = rad(G) + 4.
So this graph is a counterexample to FAR-2, but not a counterexample to Problem A.
7. The four requested attack angles and their obstructions
7.1 Angle 1 — direct rechoice of the geodesic
The direct route asks for a geodesic of length at least rad with a high-a usable side-neighbour at one end and a≥2 at the other.
Obstruction: in the graph above, every geodesic of length at least 5 with a usable side-neighbour of a≥4 at one end is a core-to-leaf geodesic of length 5. The other end is a leaf with a=1. Core-to-core geodesics have length at most 3, and core-to-internal-hair geodesics have length at most 4, so they never reach the radius threshold. Thus direct rechoice fails completely.
7.2 Angle 2 — counting with F3
F3 says that l>4 forces
Σ_{v:a(v)≥4} (a(v)-3) > n.
In the graph above this is abundantly true. There are:
6 core vertices with a=6, contributing 6·3=18;
36 core vertices with a=5, contributing 36·2=72.
So
Σ_{a≥4} (a-3) = 90 > 54 = n.
But all of this abundance is located in the core. The far ends of radius-reaching cap-break geodesics are leaves. This is precisely the global-to-positional obstruction: F3 supplies high-a vertices somewhere, but it supplies no mechanism to put one at the far end of a cap-break geodesic.
7.3 Angle 3 — peeling / hair exchange
Peel all a=1 vertices. In G this removes the six leaves, then the six internal hair vertices. The remaining graph is exactly the PG(2,4) incidence graph H.
For H:
l(H) = 5,
μ(H) = 5,
rad(H) = 3.
Thus peeling drops the radius from 5 to 3. This disproves route A1 in general: peeling can drop the radius below 5, even under the ambient hypotheses.
Route A2 would require a quantitative exchange: convert the peeled depth h=2 into two extra induced-path vertices. In this example the exchange is possible, because the core already contains the induced 9-path above. But I did not prove a general lemma that the peeled material or the core slack always supplies exactly the missing rad(G)-rad(G′) vertices. That is the precise obstruction.
7.4 Angle 4 — counterexample hunting
The graph above is the outcome of the counterexample hunt. It satisfies:
connected;
finite;
simple;
C4-free;
l=13/3>4;
rad=5;
every non-3-capped geodesic of length at least rad has length exactly rad;
every such geodesic has an a=1 vertex opposite the cap-breaking end.
It therefore realises the feared obstruction to FAR-2.
I tried to push this into a counterexample to Problem A by replacing the PG(2,4) core with a smaller, path-tight l>4 core. I failed: the PG(2,4) core already contains an induced 9-path, and I found no explicit C4-free l>4 core with radius 3 and no induced 9-path.
8. Mandatory control-case section
8.1 Controls named
The controls are those from the brief:
W2: Cay(PSL(2,11), S) as specified in F10.
W1: two copies of the PG(2,5) incidence graph joined by a path with five internal vertices, as specified in F10.
PG(3,2): point/line incidence graph of projective 3-space over GF(2).
PG(2,3): point/line incidence graph of the projective plane over GF(3).
I rely on F10 for the owner-verified numerical properties of W1 and W2; I do not recompute the 660-vertex Cayley graph from the matrices in this answer. My new graph is independently verified from the field recipe above.
8.2 Facts used and their execution on controls
F1: C4-free implies a(v)=d(v)-t(v) and ⌈d/2⌉≤a(v)≤d(v)
W2: C4-free and triangle-free, so a(v)=d(v)=6. Executes.
W1: C4-free; executes. The path internal vertices have a=2; the PG(2,5) parts have a=6.
PG(3,2): C4-free; executes, giving point a=7, line a=3.
PG(2,3): C4-free; executes, giving all a=4.
F3: abundance
W2: l=6>4; executes.
W1: l=252/43>4; executes.
PG(3,2): l=4.2>4; executes.
PG(2,3): l=4, not >4; hypothesis fails.
This is one requested example of a fact treated as available in the general discussion but not executing on a control: F3 fails on PG(2,3).
F4: cap-break
W2: l>4; executes, giving a non-3-capped geodesic of length at least rad=5.
W1: executes.
PG(3,2): executes with rad=3.
PG(2,3): fails because l=4, not >4.
F5: seed at d≥5
W2: has geodesics of length 5; all endpoints have a=6, so F5 executes and gives a 9-vertex induced path from such a geodesic.
W1: has long geodesics; executes where the hypotheses are met.
PG(3,2): diam=4, so the d≥5 hypothesis fails.
PG(2,3): diam=3, so the d≥5 hypothesis fails.
Thus F5 does not execute on PG(3,2) or PG(2,3).
F7: peeling
The base controls W2, W1, PG(3,2), PG(2,3) have no a=1 vertices in the versions listed in F10, so the nontrivial peeling operation does not execute there. In my new graph, peeling does execute and leaves the PG(2,4) core.
F11: μ≥2 theorem
W2: l>4, rad=5, μ=6; executes and gives path≥9.
W1: l>4, rad=6, μ=2; executes.
PG(3,2): rad=3, so the rad≥5 hypothesis fails.
PG(2,3): l=4, so the l>4 hypothesis fails.
This is another requested example: F11 does not execute on PG(3,2), and also not on PG(2,3).
F12: no far-end hypothesis at d≥6
W2: diam=5, so the d≥6 hypothesis fails. This is a mandatory explicit failure on W2.
W1: has geodesics of length at least 6; executes where the other hypotheses are met.
PG(3,2): diam=4; fails.
PG(2,3): diam=3; fails.
8.3 W2 mandatory statement
My negative result does not trace on W2. W2 has μ=6, so F11 already supplies a geodesic satisfying FAR-2. The graph I constructed is a control against FAR-2, not against W2. Any proof of Problem A must still execute on W2; this answer does not provide such a proof.
8.4 Witness validation / amendment 2
The only new graph exhibited is the PG(2,4)+hairs graph. It has been validated above against:
finiteness;
simplicity;
connectedness;
C4-freeness;
exact a-values;
exact l=13/3;
rad=5;
diam=7;
geodesic capping classification;
explicit induced path on 9 vertices.
8.5 Self-satisfying instance / amendment 3
The negative statement "FAR-2 is false" is instantiated non-vacuously by the explicit graph above. No added hypothesis empties the class.
9. Self-audit
9.1 Steps I am less than certain about
I have not enumerated all 21 points and all 21 lines of PG(2,4) individually. I relied on the standard field/incidence recipe and the elementary projective-plane facts that two points determine one line and two lines meet in one point. These are standard, but a fully mechanical edge-list check was not performed.
The induced 9-path was checked by hand using GF(4) arithmetic. I believe the dot-product checks are correct, but a machine check would remove any residual arithmetic doubt.
I do not know the exact value of path(G) for the constructed graph; I only prove path(G)≥9.
I did not independently recompute the W2 Cayley graph properties from the three matrices; I used F10 as given.
9.2 Every place I used a hypothesis
C4-free: used to ensure the strong common-neighbour condition, to validate the core incidence graph, and to use F1-style neighbourhood independence. In the constructed graph the graph is actually triangle-free, so a(v)=d(v) directly.
l>4: verified explicitly for the constructed graph; used conceptually in F3/F4/F11/F12 comparisons.
rad≥5: verified explicitly as rad=5.
F1: used to justify a(v)=d(v) in triangle-free C4-free setting.
F3: used only in the counting-angle discussion; the constructed graph satisfies it.
F4/F5/F11/F12: used only as contextual facts to locate the result inside the brief's hierarchy; the counterexample verification itself does not depend on them.
F7: used in the peeling-angle discussion; peeling the constructed graph gives the PG(2,4) core.
9.3 What I tried and failed
Direct FAR-2 proof. I tried to rechoose the cap-break geodesic so that its far end has a≥2. The constructed graph blocks this: all radius-reaching cap-break geodesics end at leaves.
Counting placement. I tried to use F3 to force a high-a vertex into a far-end position. The constructed graph shows the obstruction: high-a mass can be entirely central.
Peeling radius preservation (A1). I tried to prove that peeling cannot drop the radius below 5. The constructed graph refutes this: peeling drops radius from 5 to 3.
General hair-exchange lemma (A2). I tried to prove that a radius drop of h under peeling can always be converted into h extra induced-path vertices. I could verify this in the example, but I did not obtain a general proof.
Counterexample to Problem A. I tried to modify the construction to make path(G)<rad(G)+4, especially by replacing the PG(2,4) core with a path-tight core. I failed to construct such a graph. The exhibited graph still has an induced 9-path.
Thinking
AI-generated content may not be accurate.
