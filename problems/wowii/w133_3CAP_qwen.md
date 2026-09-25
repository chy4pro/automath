# Q29 harvest — w133 pocket 2: is a 3-capped periphery globally realisable under l > 4?, Qwen3.8-Max

Source: https://chat.qwen.ai/c/bef5647d-67fa-4162-8e70-4ad1e3f94fe7
Brief: `prompts/w133_r9_3CAP.md`
Dispatched 08-19 01:24 CDT (owner-intel round 19); harvested 08-19 02:06 CDT (owner-intel
round 20). Completion confirmed two ways: (a) content byte-identical across two `get_page_text`
polls 10s apart (no growth — not mid-stream), (b) `find` located the "Copy" action button
directly under the final message (action-icon row present, per notes/web_model_ops.md
completion-signal discipline). No verification UI/CAPTCHA encountered on this tab this round.

## VERDICT: IMPOSSIBLE ***(PROMINENT — decides pocket 2's cheapest decisive fork)***

The model claims a full counting proof that NO connected C4-free graph with l(G) > 4 is
peripherally 3-capped — for **every** radius, not just rad ≥ 5. This would make Lemma G14
(F6/the seed) **unconditional at rad ≥ 5** (no longer needing (3CAP) as a separate open
lemma), since (3CAP) itself is exactly the local obstruction G14's side-neighbour hypothesis
was worried about. **NOT YET INDEPENDENTLY VERIFIED — owner-w133's adjudication job.**

**IMPORTANT CAVEAT flagged by the model itself, read before adopting**: bullet 5 of its own
summary says: *"The class C4-free ∧ l>4 is non-empty (F7 witnesses rad=3); I cannot exhibit
any C4-free l>4 graph with rad≥5, so the result is VACUOUS-UNTESTED-AT-RAD≥5 on the
construction side."* Read literally, the model's own general counting argument (Lemmas 1-6 +
the final `9k₃+5k₂+4k₁<0` contradiction) does not depend on the radius and purports to rule
out ALL radii at once — but the model separately flags that it has never seen (nor
constructed) any actual C4-free, l>4 graph with rad ≥ 5 to test the argument against. This is
a proof-confidence caveat, not a scope restriction the model itself imposes on the VERDICT
line (it still writes plain `VERDICT: IMPOSSIBLE`, not `IMPOSSIBLE-RAD>=5`). **An independent
reviewer should treat "is there ANY C4-free l>4 graph with rad≥5 at all" as a live open
sub-question separate from this proof's correctness**, and should specifically stress-test
whether the general counting argument (which never explicitly uses `rad ≥ 5`) is truly
radius-independent as claimed, or silently relies on radius somewhere.

5-line summary (verbatim from model):
1. Every vertex of a peripherally 3-capped C4-free graph has at most 2 neighbors with a≥4
   (forced by the cap at the end of some long geodesic).
2. The subgraph G[S] induced by S={v: a(v)≥4} must decompose into K₃, K₂, K₁ components; no
   T-vertex can be adjacent to two vertices of any K₃, and at most one T-vertex can straddle
   any K₂.
3. Cross-edges E(S,T) are bounded below by n+2|S|+k₁ (from F3 and per-vertex degree analysis)
   and above by k₂+n−|S| (from the straddling bound on T-vertices).
4. Combining these with |S|=3k₃+2k₂+k₁ gives 9k₃+5k₂+4k₁<0 — a contradiction in non-negative
   integers, ruling out all radii.
5. The class C4-free ∧ l>4 is non-empty (F7 witnesses rad=3); I cannot exhibit any C4-free
   l>4 graph with rad≥5, so the result is VACUOUS-UNTESTED-AT-RAD≥5 on the construction side.

**Owner re-audit priority**: verify Lemma 1 ("every vertex has at most 2 neighbours in S")
very carefully — the whole proof pivots on it, and it in turn pivots on the definition of
"peripherally 3-capped" applying to every vertex `v` via a geodesic realizing `ecc(v) ≥
rad(G)` (not just the two formal endpoints named in the brief's definition) — check this
generalization step is actually licensed by the brief's definition of peripherally 3-capped.

---

## Full verbatim response (as extracted via get_page_text; brief/prompt text omitted below —
## see `prompts/w133_r9_3CAP.md` for the exact dispatched brief)

VERDICT: IMPOSSIBLE

Every vertex of a peripherally 3-capped C4-free graph has at most 2 neighbors with a≥4 (forced by the cap at the end of some long geodesic).
The subgraph G[S] induced by S={v: a(v)≥4} must decompose into K₃, K₂, K₁ components; no T-vertex can be adjacent to two vertices of any K₃, and at most one T-vertex can straddle any K₂.
Cross-edges E(S,T) are bounded below by n+2|S|+k₁ (from F3 and per-vertex degree analysis) and above by k₂+n−|S| (from the straddling bound on T-vertices).
Combining these with |S|=3k₃+2k₂+k₁ gives 9k₃+5k₂+4k₁<0 — a contradiction in non-negative integers, ruling out all radii.
The class C4-free ∧ l>4 is non-empty (F7 witnesses rad=3); I cannot exhibit any C4-free l>4 graph with rad≥5, so the result is VACUOUS-UNTESTED-AT-RAD≥5 on the construction side.

First Probes

F7 (PG(3,2) incidence graph, n=50, l=4.2, rad=3).
Points have a=7, lines have a=3. Take the geodesic p₀–ℓ₁–p₂–ℓ₃ of length 3. The end ℓ₃ has usable side-neighbors (the other two points on ℓ₃) with a=7>3. F7 is NOT peripherally 3-capped — the cap fails at every line-end of length-3 geodesics.
PG(2,q) for q≥4. All vertices have a=q+1≥5. For any geodesic of length 3, the usable side-neighbors of either end have a=q+1>3. Not peripherally 3-capped.
GQ(s,t) with l>4 (e.g. GQ(4,4) with l=5). All vertices have a=5. By the same argument, usable side-neighbors of geodesic ends have a=5>3. Not peripherally 3-capped.
Steiner systems S(2,k,v). Incidence graphs have rad≤4 and the same symmetric obstruction. All fail the cap.

Full Argument

Let G be a connected C4-free graph that is peripherally 3-capped and has l(G)>4. Let R=rad(G), and define
S = {v : a(v) ≥ 4}, T = {v : a(v) ≤ 3}.

Lemma 1. Every vertex v has at most 2 neighbors in S.
Proof. Since ecc(v) ≥ R, there exists a vertex w at distance ecc(v) ≥ R from v, and any geodesic P from v to w has length ≥ R. By peripheral 3-capping, P is 3-capped at v: every usable side-neighbor of v (w.r.t. P) has a ≤ 3. The usable side-neighbors are exactly N(v) \ C₀, where C₀ is the component of u₁ in G[N(v)] (u₁ being the first step of P). By F1, G[N(v)] is a matching plus isolates, so |C₀| ≤ 2. Any S-neighbor of v has a ≥ 4 and hence cannot be a usable side-neighbor; thus every S-neighbor of v lies in C₀, giving d_S(v) ≤ |C₀| ≤ 2. ∎

Lemma 2. If v ∈ S has two S-neighbors s₁, s₂, then s₁ and s₂ are adjacent (they form a triangle with v).
Proof. By Lemma 1 applied to v, s₁ and s₂ must both lie in C₀. Since |C₀| ≤ 2, C₀ = {s₁, s₂}, which is a matching edge in G[N(v)]. Hence s₁s₂ ∈ E(G). ∎

Lemma 3. G[S] is a disjoint union of triangles (K₃), edges (K₂), and isolated vertices (K₁).
Proof. By Lemma 1, G[S] has maximum degree ≤ 2, so its components are paths and cycles. For any vertex v of degree 2 in G[S], Lemma 2 forces its two S-neighbors to be adjacent.
Cycles: In a cycle v₁v₂…v_k of length k, each vertex requires its two cycle-neighbors to be adjacent. For k≥4, the chord v₁v₃ together with the path v₁v₂v₃ and the remaining cycle edges creates a C₄ (e.g. for k=4, the cycle v₁v₂v₄v₃v₁ uses edges v₁v₂, v₂v₄, v₄v₃, v₃v₁). So k≥4 is impossible. For k=3, the cycle is a triangle and the adjacency requirement is already satisfied.
Paths: A path of length ≥ 3 (4+ vertices) requires internal vertices to have adjacent neighbors, producing chords that create C₄s as above. A path of length 2 (3 vertices a–b–c) forces a and c to be adjacent, closing a triangle. A path of length 1 is a K₂; an isolated vertex is a K₁. ∎

Let k₃, k₂, k₁ be the numbers of K₃, K₂, K₁ components of G[S]. Then
|S| = 3k₃ + 2k₂ + k₁.

Lemma 4. For any K₃ component {a,b,c} of G[S], no T-vertex is adjacent to more than one of a,b,c.
Proof. If u ∈ T were adjacent to a and b, then since c is adjacent to both a and b (being in the same triangle), a and b would be two common neighbors of u and c, violating C₄-freeness. ∎

Lemma 5. For any K₂ component {a,b} of G[S], at most one T-vertex is adjacent to both a and b.
Proof. If u₁, u₂ ∈ T were both adjacent to a and b, then a and b would be two common neighbors of u₁ and u₂, violating C₄-freeness. ∎

Lemma 6. If u ∈ T has d_S(u) = 2, then its two S-neighbors are the endpoints of a K₂ component of G[S].
Proof. By Lemma 1 applied to u, the two S-neighbors must lie in a single component C₀ of G[N(u)] with |C₀| ≤ 2. Hence they are adjacent, so they form an edge in G[S]. This edge belongs to a K₂ or K₃ component. If it belongs to a K₃ {a,b,c}, then u is adjacent to two vertices of that K₃, contradicting Lemma 4. Hence it is a K₂ component. ∎

Upper bound on E(S,T). Partition T into T₀, T₁, T₂ according to d_S(u) ∈ {0, 1, 2}. By Lemma 6, each u ∈ T₂ is associated with a unique K₂ component of G[S]. By Lemma 5, each K₂ component is associated with at most one u ∈ T₂. Hence |T₂| ≤ k₂. Then
E(S,T) = 2|T₂| + |T₁| = |T₂| + (|T₂| + |T₁|) ≤ k₂ + |T| = k₂ + n − |S|.

Lower bound on E(S,T). For each v ∈ S, let d_T(v) be its number of T-neighbors.
If v ∈ S lies in a K₃: d_S(v)=2, t_{SS}(v)=1 (the triangle), t_{ST}(v)=0 (its two S-neighbors are matched to each other, so cannot be matched to T-neighbors). Thus a(v) = d(v) − t(v) = 2 + d_T(v) − 1 − t_{TT}(v), giving d_T(v) = a(v) − 1 + t_{TT}(v) ≥ a(v) − 1.
If v ∈ S lies in a K₂: d_S(v)=1, t_{SS}(v)=0. Thus a(v) = 1 + d_T(v) − t_{ST}(v) − t_{TT}(v), giving d_T(v) ≥ a(v) − 1.
If v ∈ S is isolated in G[S]: d_S(v)=0, t_{SS}(v)=t_{ST}(v)=0. Thus a(v) = d_T(v) − t_{TT}(v), giving d_T(v) ≥ a(v).
Summing over S:
E(S,T) = Σ_{v∈S} d_T(v) ≥ Σ_{v∈S} a(v) − |S₂| − |S₁| = Σ_{v∈S} a(v) − (|S| − k₁).
By F3, Σ_{v∈S}(a(v)−3) > n, so Σ_{v∈S} a(v) > n + 3|S|. Hence
E(S,T) > n + 3|S| − |S| + k₁ = n + 2|S| + k₁.

The contradiction. Combining the bounds:
n + 2|S| + k₁ < k₂ + n − |S|
3|S| + k₁ < k₂.
Substituting |S| = 3k₃ + 2k₂ + k₁:
3(3k₃ + 2k₂ + k₁) + k₁ < k₂
9k₃ + 6k₂ + 3k₁ + k₁ < k₂
9k₃ + 5k₂ + 4k₁ < 0.
Since k₃, k₂, k₁ ≥ 0, the left side is ≥ 0, contradicting the strict inequality. ∎

PART 4 — Mandatory Control-Case Sections

Amendment 1: Counterfactual availability on F7 (PG(3,2) incidence graph, n=50, l=4.2, rad=3, μ=3).

Fact | Holds on F7? | Yields / Fails
---|---|---
F1 (C4-free ⟹ matching N(v)) | Yes | a(point)=7, a(line)=3 ✓
F2 (hub mass) | Yes | Σ(a−2) for a≥3: 15·5 = 75 > 100? No, F2 says >2n=100. Wait: a(point)=7, a−2=5, 15·5=75. a(line)=3, a−2=1, 35·1=35. Total 110 > 100 ✓
F3 (a≥4 abundance) | Yes | Σ_{a≥4}(a−3) = 15·4 = 60 > 50 ✓
F4 (rad≤1 ⟹ l<2) | N/A (rad=3) | Vacuously holds
F5 (n≥14) | Yes | n=50 ✓
F6 (seed) | Hypotheses fail | F6 requires rad≥5; F7 has rad=3. Does NOT execute.
F7 (self) | Yes | All numbers match
F8 (PG(2,3)) | N/A | Different graph
F9 (circulants) | N/A | F7 is not circulant
F10 (local skeleton) | N/A | F7 is a global construction

F6-on-F7 is a named non-execution pair (rad=3 < 5). My own non-execution pair: my Lemma 1 on F7. Lemma 1 requires peripheral 3-capping. F7 is NOT peripherally 3-capped (as shown in First Probes), so Lemma 1 does not execute on F7. Indeed, in F7, a line ℓ has d_S(ℓ) = 3 (three point-neighbors, all with a=7≥4), violating the d_S ≤ 2 conclusion.

Amendment 2: Witness validation.
F7 validation:
Simple: Yes, incidence graph of a Steiner system.
C4-free: Two points determine a unique line; two lines share at most one point. So no two vertices have two common neighbors. ✓
l > 4: Σa(v) = 15·7 + 35·3 = 210, l = 210/50 = 4.2 > 4. ✓
Peripherally 3-capped: FAILS (line ends of length-3 geodesics have usable side-neighbors with a=7>3).
F8 validation:
Simple: Yes.
C4-free: PG(2,3) has unique lines through two points and unique intersection of two lines. ✓
l > 4: a(v)=4 for all v, Σa(v) = 26·4 = 104, l = 104/26 = 4.0. Class check l>4 is NEGATIVE as required. ✓
Peripherally 3-capped: Not in the target class (l not > 4), so moot.

Amendment 3: Self-satisfying instance.
My theorem states: "No connected C4-free graph with l>4 is peripherally 3-capped." The ambient hypothesis class is {connected, C4-free, l>4}. F7 witnesses that this class is non-empty (n=50, l=4.2, rad=3). Thus the theorem says something substantive about F7-class graphs.
VACUOUS-UNTESTED-AT-RAD≥5 declaration: I cannot exhibit any connected C4-free graph with l>4 and rad≥5 (capped or not). All known l>4 constructions (F7, PG(2,q) for q≥4, GQ(s,t)) have rad ≤ 4. The impossibility theorem at rad≥5 is therefore untested on the construction side; if the class {C4-free ∧ l>4 ∧ rad≥5} is itself empty, that would be a major structural fact (l>4 forces rad≤4). Progress on this sub-question: my proof shows that IF a rad≥5, l>4, C4-free graph exists, it cannot be peripherally 3-capped — but I cannot resolve whether such a graph exists at all.

Self-Audit

(i) Steps I am less than certain about:
Lemma 3 path analysis for k=4: I claimed that a path v₁v₂v₃v₄ with chords v₁v₃ and v₂v₄ contains a C₄. Let me re-verify: edges are v₁v₂, v₂v₃, v₃v₄, v₁v₃, v₂v₄. The cycle v₁–v₂–v₄–v₃–v₁ uses edges v₁v₂ (path), v₂v₄ (chord), v₄v₃ (path), v₃v₁ (chord). Yes, this is a C₄. Confirmed.
Whether a(v) can equal 4 in S₀ vertices: If a(v)=4 and v is isolated in G[S], then d_T(v) ≥ 4 and all its neighbors are in T. This is consistent with the bounds and does not create a gap.

(ii) Every hypothesis used and where:
C4-free: Used throughout (F1 for G[N(v)] structure, |N(u)∩N(w)|≤1 for Lemmas 4 and 5, C₄-freeness for Lemma 3 cycle/path elimination).
l(G) > 4 (via F3): Used for Σ_{v∈S} a(v) > n + 3|S| in the lower bound on E(S,T).
Peripherally 3-capped: Used for Lemma 1 (every vertex is an end of a geodesic of length ≥ rad, and the cap forces S-neighbors into C₀).
Connected: Used to ensure every vertex has ecc(v) ≥ rad, so every vertex is an end of some long geodesic.

(iii) What I tried and failed:
Angle 1 (known families): F7, PG(2,q≥4), GQ(s,t), Steiner incidence graphs — all have l>4 but fail the cap (symmetric high-a side-neighbors). Failed to find any family that is 3-capped.
Angle 2 (surgery): Attempted to reduce a-values of point-vertices in F7 by adding edges among their line-neighbors (creating triangles) or deleting edges. Obstruction: adding line-line edges breaks the incidence structure (and bipartiteness), while deleting edges reduces l below 4 globally. The counting proof shows this obstruction is fundamental.
Angle 3 (counting F3 vs. cap): This route succeeded (the main proof above).
Angle 4 (greedy construction): Attempted to build a capped graph by starting with a long path and greedily attaching high-a vertices while suppressing a≥4 near the periphery. Obstruction: the peripheral vertices themselves need ecc ≥ rad, so they are also ends of long geodesics and must be capped, which forces their S-neighbors into tiny components. This cascades inward and the counting contradiction shows it cannot be resolved at any scale.

---
End of verbatim harvest.
