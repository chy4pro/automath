# Q28 harvest — w133 pocket 1: Lemma G14 extended down to d = 3 and d = 4, Qwen3.8-Max

Source: https://chat.qwen.ai/c/d20a3189-b29b-4d55-b027-121e08fbc205
Brief: `prompts/w133_r9_G14low.md`
Dispatched 08-19 01:19 CDT (owner-intel round 19); harvested 08-19 02:06 CDT (owner-intel
round 20). Completion confirmed two ways: (a) content byte-identical across two `get_page_text`
polls 10s apart (no growth — not mid-stream), (b) `find` located the "Copy" action button
directly under the final message (action-icon row present, per notes/web_model_ops.md
completion-signal discipline). No verification UI/CAPTCHA encountered on this tab this round.

## VERDICT: SOLVED-BOTH ***(PROMINENT — decides pocket 1's D=3 open case)***

This is the model's claimed resolution of **both** d=3 and d=4 extensions of Lemma G14
(F3 in the brief). d ≥ 5 was already proved (G14); D = 2 is Theorem G12. **D = 3 is pocket
1's first genuinely open case** (residual lives at δ = 2 per G33, so degree floors are
useless there — a-value currency only, exactly as this brief required). d = 4 is also
claimed with zero extra hypotheses. **NOT YET INDEPENDENTLY VERIFIED — this is owner-w133's
adjudication job; flag as SOLVED-BOTH-CLAIMED pending re-audit, not yet adopted.**

5-line summary (verbatim from model):
1. For d=4, a complete proof is established with zero extra hypotheses: the standard
   construction w-x-u₀-…-u₄-y yields P₈ when any w survives the kills from {y, u₂, u₃}, and
   when all three kills are distinct, the alternative path z-u₀-x-w_y-y-u₄-u₃-u₂ is always
   induced because z~y is impossible by distance (dist(u₀,y)≥3).
2. For d=3, Case 1 (x ≁ y) is fully proved: the standard path works unless all three kills
   {y, u₂, u₃} hit distinct components; when that happens, the path w₁-y-z-u₀-u₁-u₂-w₂ (using
   the y-kill w₁, the u₂-kill w₂, and z∈N(u₀) outside u₁'s and x's components) is always
   induced P₇.
3. For d=3 Case 2 (x~y), the u₃-kill is impossible (would give x,u₃ two common neighbours y,w,
   a C4), leaving at most one kill on two candidates; the resulting survivor w₂ permits
   alternative paths through tail vertices mandated by F4.
4. Both control instances (PG(2,3) for d=3, PG(3,2) for d=4) satisfy all hypotheses with long
   induced paths.
5. No counterexample was found despite systematic construction attempts — every worst-case
   graph tried computationally admits P₇ or P₈.

**Owner re-audit flag (from the model's own Self-Audit — read before adopting):** d=3 Case 2
(x~y) Subcase 2b (the "extreme" degree-2 tail case) is explicitly marked NOT fully rigorous —
the model calls its own tail argument "structurally convincing but not airtight" and says "a
full proof would require a more systematic enumeration of tail configurations." **This is the
weak point of the d=3 claim and should be the first thing an independent reviewer attacks.**

---

## Full verbatim response (as extracted via get_page_text; brief/prompt text omitted below —
## see `prompts/w133_r9_G14low.md` for the exact dispatched brief)

VERDICT: SOLVED-BOTH

Summary:
For d=4, a complete proof is established with zero extra hypotheses: the standard construction w-x-u₀-…-u₄-y yields P₈ when any w survives the kills from {y, u₂, u₃}, and when all three kills are distinct, the alternative path z-u₀-x-w_y-y-u₄-u₃-u₂ is always induced because z~y is impossible by distance (dist(u₀,y)≥3).
For d=3, Case 1 (x ≁ y) is fully proved: the standard path works unless all three kills {y, u₂, u₃} hit distinct components; when that happens, the path w₁-y-z-u₀-u₁-u₂-w₂ (using the y-kill w₁, the u₂-kill w₂, and z∈N(u₀) outside u₁'s and x's components) is always induced P₇.
For d=3 Case 2 (x~y), the u₃-kill is impossible (would give x,u₃ two common neighbours y,w, a C4), leaving at most one kill on two candidates; the resulting survivor w₂ permits alternative paths through tail vertices mandated by F4.
Both control instances (PG(2,3) for d=3, PG(3,2) for d=4) satisfy all hypotheses with long induced paths.
No counterexample was found despite systematic construction attempts — every worst-case graph tried computationally admits P₇ or P₈.

Collision Re-audit

Re-deriving the F3 proof for d=3 and d=4 from first principles:
F3 construction: Path w-x-u₀-u₁-…-u_d-y, with w chosen from a surviving component of G[N(x)].
Component kills on G[N(x)] (u₀ occupies 1 component; each of the following destroys ≤1 component by C4-free |N(x)∩N(v)|≤1):

Kill | d=3 | d=4 | d≥5
---|---|---|---
u₀ (self) | 1 | 1 | 1
N(u₂) | ≤1 | ≤1 | ≤1
N(u₃) | ≤1 | ≤1 | ≤1
N(u₄) | — | 0 (dist(w,u₄)≥2) | 0
N(y) | ≤1 | ≤1 | 0 (dist(w,y)≥2)

Interface collisions:
d=4: dist(w,y)≥1 (w≠y but wy possible), dist(x,y)≥2 (x ≁ y guaranteed). Only C-1 (wy) is a collision.
d=3: dist(w,y)≥0, dist(x,y)≥1. Both C-1 and C-2 apply.
The owner's audit is confirmed complete: at d=4 only wy is a collision (xy is impossible by distance); at d=3 both wy and xy are possible, plus w=y.

Full Argument

Proof for d=4

Setup: Geodesic u₀-u₁-u₂-u₃-u₄, a(u₀)≥3, a(u₄)≥2, usable x∈N(u₀) with a(x)≥4. Choose y∈N(u₄) outside u₃'s component (so y ≁ u₃).

Step 1 — Kills: G[N(x)] has ≥4 components. u₀ occupies one; let C₁,C₂,C₃ be three others with representatives w₁,w₂,w₃. The u₄-kill is 0 because dist(w,u₄) ≥ dist(u₀,u₄)−dist(u₀,w) = 4−2 = 2, so no w is adjacent to u₄. Kills from {y, u₂, u₃} each destroy ≤1 component.

Step 2 — Standard path: If some w_i avoids all three kills, then w_i-x-u₀-u₁-u₂-u₃-u₄-y is an induced P₈.
Non-adjacencies: w_i ≁ u₀ (different component), w_i ≁ u₁ (else w_i-x-u₀-u₁-w_i is C4, using x ≁ u₁ since x is outside u₁'s component), w_i ≁ u₄ (dist≥2). For interior u₂,u₃: avoided by component choice. x ≁ u₂ (C4 with u₀), x ≁ u₃ (dist(x,u₃)≥2), x ≁ u₄ (dist≥3). y ≁ u₃ (by choice), y ≁ u₂ (else u₂,u₄ share neighbours y,u₃ → C4), y ≁ u₁ (else u₁,u₄ share y,u₃ via path → check: dist(u₁,y)≥dist(u₁,u₄)−1=2, so y ≁ u₁), y ≁ u₀ (dist(u₀,y)≥3). And x ≁ y because dist(x,y) ≥ dist(u₀,y)−1 ≥ 2. ✓

Step 3 — All three killed: Suppose w_y~y, w₂~u₂, w₃~u₃ (each kill hits a distinct component). Since a(u₀)≥3, pick z∈N(u₀) outside u₁'s and x's components (z ≁ u₁, z ≁ x).
Claim: z ≁ y. Proof: dist(u₀,y) ≥ dist(u₀,u₄)−1 = 3. If z~y, then dist(u₀,y) ≤ dist(u₀,z)+dist(z,y) = 1+1 = 2 < 3, contradiction. ∎
Alternative path: z-u₀-x-w_y-y-u₄-u₃-u₂ (8 vertices).
Edges: zu₀, u₀x, xw_y, w_yy, yu₄, u₄u₃, u₃~u₂. ✓
Chord verification:
z ≁ x (different components in G[N(u₀)]) ✓
z ≁ w_y (else u₀,w_y share x,z → C4) ✓
z ≁ y (proved above) ✓
z ≁ u₄ (dist(z,u₄) ≥ 4−1 = 3) ✓
z ≁ u₃ (dist(z,u₃) ≥ 3−1 = 2) ✓
z ≁ u₂ (else u₀,u₂ share z,u₁ → C4) ✓
u₀ ≁ w_y (different components in G[N(x)]) ✓
u₀ ≁ y (dist≥3) ✓
u₀ ≁ u₄ (dist=4), u₀ ≁ u₃ (dist=3), u₀ ≁ u₂ (dist=2) ✓
x ≁ y (dist(x,y)≥2), x ≁ u₄ (dist≥3), x ≁ u₃ (dist≥2), x ≁ u₂ (C4 with u₀) ✓
w_y ≁ u₄ (dist(w_y,u₄) ≥ 4−2 = 2) ✓
w_y ≁ u₃ (w_y is y-kill, not u₃-kill, so w_y ∉ N(u₃)) ✓
w_y ≁ u₂ (w_y is y-kill, not u₂-kill) ✓
y ≁ u₃ (y outside u₃'s component in G[N(u₄)]) ✓
y ≁ u₂ (else u₂,u₄ share y,u₃ → C4) ✓
u₄ ≁ u₂ (dist=2) ✓
All chords fail. Hence z-u₀-x-w_y-y-u₄-u₃-u₂ is an induced P₈. □

Proof for d=3

Setup: Geodesic u₀-u₁-u₂-u₃, a(u₀)≥3, a(u₃)≥2, usable x∈N(u₀) with a(x)≥4. Choose y∈N(u₃) outside u₂'s component.

Step 1 — Kills: G[N(x)] has ≥4 components. u₀ occupies one; pick representatives w₁,w₂,w₃ from three others. Kills from {y, u₂, u₃} each destroy ≤1 component.

Case 1: x ≁ y
Subcase 1a: Some w_i avoids all three kills. Then w_i-x-u₀-u₁-u₂-u₃-y is induced P₇ (same chord verification as d=4 Step 2, with dist(w,u₃)≥1 instead of ≥2 — still sufficient since w_i avoids N(u₃) by component choice).
Subcase 1b: All three killed distinctly: w₁~y, w₂~u₂, w₃~u₃. Pick z∈N(u₀) outside u₁'s and x's components.
Sub-subcase 1b-i: z ≁ y. Then z-u₀-x-w₁-y-u₃-u₂ is induced P₇:
Edges: zu₀, u₀x, xw₁, w₁y, yu₃, u₃u₂.
Chords: z ≁ x (different components), z ≁ w₁ (C4: u₀,w₁ share x,z), z ≁ y (assumed), z ≁ u₃ (dist≥2), z ≁ u₂ (C4 with u₀). u₀ ≁ w₁ (different components), u₀ ≁ y (dist≥2), u₀ ≁ u₃ (dist=3), u₀ ≁ u₂ (dist=2). x ≁ y (Case 1), x ≁ u₃ (dist≥2), x ≁ u₂ (C4). w₁ ≁ u₃ (not u₃-kill), w₁ ≁ u₂ (not u₂-kill). y ≁ u₂ (outside u₂'s component). ✓
Sub-subcase 1b-ii: z~y. Then w₁-y-z-u₀-u₁-u₂-w₂ is induced P₇:
Edges: w₁y, yz, zu₀, u₀u₁, u₁u₂, u₂w₂.
Chords: w₁ ≁ z (C4: u₀,w₁ share x,z), w₁ ≁ u₀ (different components), w₁ ≁ u₁ (C4: x,u₁ share w₁,u₀), w₁ ≁ u₂ (not u₂-kill), w₁ ≁ w₂ (different components). y ≁ u₀ (dist≥2), y ≁ u₁ (C4: u₁,u₃ share y,u₂), y ≁ u₂ (outside u₂'s component), y ≁ w₂ (since |N(x)∩N(y)|≤1 and w₁ is the unique common neighbour, w₂ ≁ y). z ≁ u₁ (different components in G[N(u₀)]), z ≁ u₂ (C4: u₀,u₂ share z,u₁), z ≁ w₂ (C4: u₀,w₂ share x,z). u₀ ≁ u₂ (dist=2), u₀ ≁ w₂ (share x, not adjacent). u₁ ≁ w₂ (share u₂, not adjacent). ✓

Case 2: x~y
Here y∈N(x), so y is a component of G[N(x)]. Let w₁,w₂ be representatives of two other components (a(x)≥4 gives ≥4 components total: u₀, y, w₁, w₂, ...).
Key observation: the u₃-kill is impossible. If some w∈N(x) were adjacent to u₃, then x and u₃ would share common neighbours w and y (since xy and yu₃), giving |N(x)∩N(u₃)|≥2, violating C4-free. So no w∈N(x) is adjacent to u₃.
Kills on {w₁,w₂}: only u₂ can kill (≤1). At least one survives; say w₂ ≁ u₂ (and w₂ ≁ u₃, w₂ ≁ y by component separation, w₂ ≁ u₀ by component separation, w₂ ≁ u₁ by C4).
Subcase 2a: d(u₁) ≥ 3 or d(u₂) ≥ 3 or d(u₀) ≥ 4 or a suitable tail exists.
The F4 condition (a(v)≥2 for all v) forces every vertex to have ≥2 neighbours. Vertices like z∈N(u₀), or neighbours of w₂, create "tail" structures. The path w₂-x-y-u₃-u₂-u₁-v (extending through a neighbour v of u₁ avoiding the path vertices) or w₂-x-y-u₃-u₂-v₂-v₃ (extending through u₂'s other neighbours) yields P₇, with chords blocked by C4-free and distance.
Subcase 2b (extreme): d(u₁)=2, d(u₂)=2, d(y)=2, a(u₀)=3.
Then N(u₁)={u₀,u₂}, N(u₂)={u₁,u₃}, N(y)={u₃,x}. Vertices z∈N(u₀), w₁,w₂∈N(x) each need a second neighbour (by F4). These second neighbours (say v_z, v₁, v₂) form tails. Any path through the tail z-v_z-... or w₂-v₂-... combined with the geodesic yields P₇. Computationally, every graph in this family has path(G)≥7 (verified: the extreme-case graph with tails v-v₁, v₂-v₃-v₄ has longest induced path = 12).
The structural reason: F4 forces enough "width" in the tails that bypassing the xu₀ and u₀u₁ chords is always possible by routing through the tail on one side and the y-u₃ edge on the other. □

PART 4 — Mandatory Control-Case Section

1. Counterfactual availability (PG(2,3))
PG(2,3) incidence graph: n=26, bipartite, 4-regular, C4-free, triangle-free, a(v)=4 for all v, diam=3.

Fact | Holds? | Yields | Fails?
---|---|---|---
F1 (a(v)=d(v)−t(v)) | Yes (t=0 everywhere) | a(v)=4 | —
F2 (baseline +3) | Yes (a(u₀)=4≥3, a(u₃)=4≥2) | path≥6 | —
F3 (d≥5 case) | N/A (d=3) | — | d≥5 hypothesis fails
F4 (no a=1 vertices) | Yes (all a=4) | Full applicability | —
F5 (local statement) | Yes | Small counterexamples in scope | —
F6 (PG(2,3) self-satisfying) | Yes | path≥9≥7 | —

Fact treated as available but not executing: F3 (requires d≥5, but PG(2,3) has d=3 geodesics). The d=3 proof developed above is the needed extension.

2. Witness validation
PG(2,3):
Simple, connected, 26 vertices: ✓
C4-free: two points lie on exactly one common line; two lines meet in exactly one point. No pair has 2 common neighbours. ✓
a-values: triangle-free 4-regular → a(v)=4 for all v. ✓
Geodesic: non-incident point-line pairs are at distance 3. ✓
Longest induced path: owner-verified ≥9. ✓
Explicit d=3 graph (from code):
Edge list: {u₀u₁, u₁u₂, u₂u₃, u₀x, u₀z₁, u₀z₂, xw₁, xw₂, xw₃, u₃y, u₃c, yw₁, w₂c, w₃u₂, z₁y, z₂c}
C4-free: verified computationally (all pairs have ≤1 common neighbour). ✓
a-values: a(u₀)=4, a(x)=4, a(u₃)=3, all others ≥2. ✓
path(G): 7. ✓

3. Self-satisfying instances
d=3 theorem (a(u₀)≥3, a(u₃)≥2, a(x)≥4): PG(2,3) satisfies all hypotheses with a(v)=4 everywhere, d=3 geodesics exist (non-incident point-line pairs), and path≥9≥7.
d=4 theorem: PG(3,2) point/line incidence graph (n=50, bipartite, C4-free, points have degree 7 with a=7, lines have degree 3 with a=3, diam=4). Geodesic line₀-point₁-line₂-point₃-line₄: a(line₀)=3≥3, a(line₄)=3≥2, usable side-neighbour is a point with a=7≥4. path≥12≥8.

Self-Audit

(i) Steps I am less than certain about:
Case 2 of d=3 (x~y), Subcase 2b: I proved that the u₃-kill is impossible and that tails from F4 provide alternative paths, but I did not give a fully rigorous case-free proof that a P₇ always exists when d(u₁)=d(u₂)=d(y)=2 and a(u₀)=3. The computational evidence is overwhelming (every attempted counterexample has path≥7, often much higher), but a purely deductive proof of this last subcase would require a more systematic enumeration of tail configurations.
In the d=4 proof, Step 3: I claimed w_y ≁ u₃ and w_y ≁ u₂ because w_y is the y-kill and not the u₃/u₂-kill. This is correct (each kill destroys a different component), but I should have explicitly noted that w_y being in the y-component means w_y ∈ N(x)∩N(y) and therefore w_y ∉ N(u₃) and w_y ∉ N(u₂) (since those are different components of G[N(x)]).

(ii) Every place I used a hypothesis:
C4-free: Used everywhere — for |N(x)∩N(v)|≤1, for chord non-adjacencies (e.g., w ≁ u₁ via C4 on x-u₀-u₁-w), for the impossibility of the u₃-kill in Case 2 (x,u₃ would share y,w).
Geodesic (shortest path): Used for dist(u₀,u₃)=3 and dist(u₀,u₄)=4, which force x ≁ u₃, x ≁ u₄, u₀ ≁ u₃, etc.
a(u₀)≥3: Used to guarantee the existence of z∈N(u₀) outside u₁'s and x's components.
a(u₃)≥2: Used to guarantee y exists outside u₂'s component.
a(x)≥4: Used to guarantee ≥3 non-u₀ components in G[N(x)], providing enough candidates for w and ensuring the budget to pay for kills.
F4 (no a=1 vertices): Used in Case 2 of d=3 to guarantee tail vertices exist (every vertex has a≥2, so neighbours of degree-2 vertices must have further neighbours, creating tails that provide alternative path routings).

(iii) What I tried and failed:
Constructing an explicit counterexample for d=3: I systematically tried to build C4-free graphs with d=3 geodesics, a(u₀)≥3, a(u₃)≥2, a(x)≥4, and path(G)≤6. Every construction either violated C4-free (e.g., the first attempt had u₀ and y sharing z and x), violated F4 (a=1 vertices), or had path(G)≥7. The most constrained graph (extreme case with d(u₁)=d(u₂)=d(y)=2) had path(G)=12 due to tail structures.
Direct repair of F3's proof for d=3 without the alternative path: The standard path w-x-u₀-u₁-u₂-u₃-y fails in Case 2 (xy) due to the xy chord. No choice of w can avoid this chord since it depends on x and y, not w. The alternative path was necessary.
Proving Case 2 Subcase 2b purely deductively: The tail argument is structurally convincing but not airtight. A full proof would require showing that for every C4-free graph with the specified degree/a-value constraints, at least one tail vertex can be threaded into an induced P₇.

---
End of verbatim harvest.
