# Qwen r5 Parallel Solver — WOWII-133 RES(b) Emptiness (two-tab variant)

Target: decide whether an **admissible** graph exists — C4-free, connected, `rad=2`,
`diam=3`, `l(C)>3` (strict), and every vertex `h` with `a(h)>=3` has `ecc(h)<=2` (condition
C5). Optional extra hypothesis C6 (no induced P6) may be used and is used by both variants
below. Brief: `prompts/w133_r5_RES_qwen.md` (S2 template set T1+no-internet+T8+T11, plus T12
control case and T13 conclusion-first tag).

**Both tabs converge on the same substantive result**, reached independently (judge-
independence honored — neither tab shown the other's output):

> Under (C6): if a diameter-3 pair `u,z` has `a(u)=a(z)=2`, the induced 6-cycle forced by
> Fact 7 leads to a contradiction with `l(C)>3` (mass count `F(C) := Σ(a(v)-3) <= -2 < 0`,
> so `l(C)<=3`) — **this branch is proved empty**. The one open obstruction in both tabs is
> the **triangular-endpoint branch**: a diameter-3 pair where an endpoint has `a(u)=1`
> (degree 2, lying in a triangle) is NOT covered by the Fact-7 rigidity, and neither tab
> closes it.

Neither tab reaches a full SOLVED-EMPTY / SOLVED-CONSTRUCTED verdict on the original
(C5)-only question. Owner-w133 re-verifies every line before adoption (draft §15.3–§15.6 +
§16 remain authoritative).

---

## Tab A — as-written brief

- Conversation: https://chat.qwen.ai/c/f186ea5f-0c4f-43c2-b69c-479b3609e053
- Model: Qwen3.8-Max (confirmed switched before dispatch)
- Dispatched: 08-18 ~09:2x CDT; harvested 08-18 11:06 CDT (owner-intel round 3, post-outage)
- Verdict tag: **PARTIAL**

### Structure of Tab A's argument

1. Defines `e(v) := a(v)-2`, mass `M := Σ_{h∈H} e(h) > n` (Fact 1 restated).
2. Restricts to the branch with a diameter pair `u,z` with `a(u)=a(z)=2`. Under (C6), Fact 7
   gives the induced 6-cycle `Z = (u,p,q,z,r,s)` (renamed from the brief's `u,u1,u2,z,y,x`).
3. **Lemma 3.1 / Corollary 3.2**: under (C6), no zero-`Z`-neighbour vertex can be adjacent to
   any of the four "adjacent-pair" slots `P,Q,A,B` — proved via an explicit induced-P6
   exhibit for each case (contradicts C6). Consequently Fact 10's hypothetical "one
   zero-neighbour high vertex" cannot exist.
4. **Lemma 3.3**: the only zero-`Z`-neighbour vertex that can matter is a single vertex `W`
   adjacent to both distance-3 slots `C,D` — and even that contributes zero positive excess
   (`a(W)∈{1,2}` depending on whether `C~D`).
5. **Lemma 4.1/4.2**: enumerates the only 7 possible slot-slot edges (`PQ,PB,PD,QB,QC,AB,CD`)
   from the C4-free matching property, plus a shared-Z-neighbour exclusion rule.
6. **Lemma 5.1**: cycle vertices `p,r` can only be high if slot `C` is present (excess exactly
   1 each); `q,s` only if `D` is present.
7. **Lemma 6.1** (uses C5 directly): if slot `P` is high it must be adjacent to slot `Q` (to
   keep its eccentricity `<=2`, since `P`'s cycle-distance to `z` is 3) — this is flagged as
   "a crucial place where (C5) enters."
8. **Case analysis (Section 7)**, split on which of `C,D` are present (Cases 1/2/3, with
   subcases 3a/3b) — in every case, exhaustively bounds total excess `M` and shows `M < n`,
   contradicting Fact 1's `M>n`. Concludes **Theorem 8.1**: no admissible-under-(C6) graph has
   a diameter pair with `a(u)=a(z)=2`.
9. **Section 9 — the open obstruction**: the complementary case where every diameter-3 pair
   has an endpoint with `a=1` (a triangle vertex of degree 2). Splits into 9.1 (third triangle
   vertex also degree 2 — ruled out, contradicts C5 via Fact 3) and 9.2 (third triangle vertex
   degree >=3 — **not resolved**; "the triangle creates chords that prevent the automatic
   formation of the induced 6-cycle, and the slot classification does not directly apply").
10. Reports genuinely attempting all four required attack angles (counting/extremal, local
    structure, direct construction, algebraic/Moore-bound) with named obstructions for each,
    per the brief's persistence requirement.

## Tab B — construction-first variant

- Conversation: https://chat.qwen.ai/c/ca90288c-54ab-4dae-8562-b6c976dee453
- Model: Qwen3.8-Max (confirmed switched before dispatch)
- Dispatched: 08-18 ~09:2x CDT; harvested 08-18 11:06 CDT (owner-intel round 3, post-outage)
- Prompt prefix (variant instruction): "Focus your first attempt on CONSTRUCTING such a graph
  before trying to prove impossibility."
- Verdict tag: **PARTIAL**

### Structure of Tab B's argument

1. Reports genuinely trying construction first (Angle C: modifying Hoffman-Singleton, Heawood,
   Petersen, ER_q polarity-graph cores) — names the obstruction as a "dominating-edge
   obstruction": C4-freeness prevents a low diameter-endpoint from being both attached (to
   keep it low) and having the dense high core within distance 2, simultaneously.
2. Reformulates the mass condition as `F(C) := Σ_v (a(v)-3) > 0` (equivalent to `l(C)>3`);
   `a=3` neutral, `a=2` contributes -1, `a=1` contributes -2, need `a>=4` vertices to win.
   Names this the **"booster-deficit obstruction"**: any local move to raise one high vertex's
   `a`-value forces auxiliary vertices/edges whose own `F`-contribution cancels or outweighs
   the gain.
3. **Independently derives the same six-slot classification** as Tab A (relabeled `A,B,P,Q,R,S`
   instead of Tab A's `P,Q,A,B,C,D` — different naming, same six slot positions and adjacency
   structure), with a cleaner discharging-style proof:
   - Assigns `β(X) ∈ {1,2}` (adjacent-pair vs opposite-pair slot) and shows
     `a(X) = β(X) + comp(N_O(X))` where `O` is the induced graph on present slots.
   - Classifies all possible connected components of `O` (isolated slots, single edges, length-2
     paths, one triangle `ABQ`, one isolated edge `RS`) and shows every component's total
     `F`-contribution is `<=0`, with equality only for the `RS` edge.
   - Concludes the same **Theorem-equivalent partial result**: under the *additional*
     restriction that no outside vertex has 0 neighbours on the rigidity 6-cycle,
     `F(C) <= -2 < 0`, contradicting `l(C)>3`.
4. **Section 5**: proves, under (C6), that Fact 10's hypothetical high zero-`Z`-neighbour
   vertex is impossible (explicit induced-P6 exhibit), matching Tab A's Lemma 3.1/Cor 3.2.
5. **Section 7 — two named open obstructions** (matching Tab A's gaps, independently derived):
   - **7.1 Low zero-neighbour auxiliaries**: low (`a<=2`) vertices with 0 neighbours on `Z`
     are not fully ruled out as "boosters" — Tab B believes the booster-deficit obstruction
     still applies but does not have a complete proof covering all configurations.
   - **7.2 The triangular-endpoint case `a(u)=1`**: same open branch as Tab A's Section 9.
     Tab B additionally gives an explicit *minimal example* satisfying (C1)(C2)(C3)(C6) in
     this regime — two triangles `upq` and `zrs` joined by cross-edges `pr`, `qs` — noting it
     satisfies rad=2/diam=3/C4-free/no-induced-P6 but its `l`-value is "far below 3", so it is
     not itself a counterexample; the open question is whether every augmentation of this
     shape can be shown to keep `F<=0`.

## Cross-tab agreement assessment

The two tabs used different notation and different starting strategies (as-written vs
construction-first) but arrived at **structurally the same partial result** — non-existence
in the `a(u)=a(z)=2` diameter-pair branch under (C6), reduced to an equivalent six-slot
classification, with the same two obstructions left open (triangular a=1 endpoints; possible
low zero-Z-neighbour boosters). This convergence from independent starting points is a
positive signal for the correctness of the six-slot reduction, but **it is not a proof** —
both tabs could share a common blind spot inherited from the shared Facts 1–10 preamble in
the brief (which was handed to both, not independently derived). Owner-w133 should treat the
six-slot classification and Theorem 8.1 / the equivalent Tab-B theorem as the most promising
verified partial result, and prioritize independent (non-Qwen) verification of Lemma 6.1 (the
(C5)-dependent step forcing `P~Q`) since both tabs flag it as the crux where (C5) enters.

## Same-source / independence note

Neither tab was shown the other's output, Spark output, or any other model's report — pure
judge/solver independence honored per the queue row and brief.

## Extraction caveat

Both raw captures (`get_page_text`) render KaTeX math with a duplicated visual-unicode +
ASCII-annotation pattern (e.g. `𝑀 M:=...` appears twice in a row) rather than the DOM-rewrite
LaTeX-source method from `notes/web_model_ops.md` (not needed here since content was legible
without it, given time budget). The summaries above were written from careful reading of the
duplicated raw text and preserve every named lemma/theorem, case split, and numeric bound;
they are not a byte-exact transcript. If owner-w133 needs the byte-exact original for a
specific step, re-fetch from the conversation URLs above (both tabs were left generating
uninterrupted through the 09:28-11:00 CDT outage — Qwen's browser-side generation costs zero
Claude quota and was unaffected).
