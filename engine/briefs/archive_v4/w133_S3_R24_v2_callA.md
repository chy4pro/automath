# S3 adversarial review brief — WOWII-133 §24 diff (G41, G42, G43, G44)

**Engine target: muse-spark-1.2 (Meta family) — PRECISION / cross-family S3 vote.**
**Version: v2 FINAL, FROZEN 2026-08-22 09:2x CDT (owner-w133, round 12).**
*(v1 → v2, planner directive 09:2x: retrofit of the mandatory anti-echo harness — PART 0.5
execution-environment declaration and PART 6 HELD-OUT CHECKS — after muse-spark's w61/Q34
report was ruled VOID as a "fluent echo report". No mathematical content changed; one
printed numeric value was **removed** from PART 3 D4 and moved into the held-out table.)*
Under the READY-row freeze discipline this file must not be edited after dispatch; a
correction requires a new version stamp and a fresh conversation.

---

# PART 0 — YOUR TASK AND YOUR DELIVERABLE FORMAT

You are an adversarial reviewer. You are given a **diff**: four new statements (G41, G42,
G43, G44) with their complete proofs, plus the background they rest on. Your job is to
**break them**, and failing that, to certify them.

**Do not search the internet.** Work from this file alone; you may write and run your own
code. **Do not use a SAT solver.** Do not assume anything not written here.

Your report MUST begin with exactly these two lines:

```
VERDICT: CLEAN | PARTIAL | GAP | REFUTED
MATHEMATICS DEFECT FOUND: YES | NO
```

The second line is a **separate bit** from the verdict word and it is the gate this review
turns on. Set it **YES** if and only if you find a defect in a step, a hypothesis or a
citation **inside** one of the four proofs under review (the joints marked MATHEMATICS
below). A defect in a status sentence, a cross-reference, a label, or a piece of prose
around the proofs is **BOOKKEEPING** and does not set the bit — but you must still report
it, and if you think the classification is borderline, **say so explicitly and give both
readings**, do not bury the call.

Then, for each joint R12-M1 … R12-M4 and R12-B1 … R12-B3 below, give a verdict
(CLEAN / GAP / REFUTED) with your reasoning. Then the mandatory probes (PART 5) and the
**HELD-OUT CHECKS table (PART 6) — a report without that table is VOID, not merely
incomplete.**

---

# PART 0.5 — EXECUTION-ENVIRONMENT DECLARATION (mandatory, and it must be the THIRD line of your report)

Immediately after the two verdict lines, print exactly one of:

```
EXECUTION: NONE -- every numeric claim below is hand-derived.
EXECUTION: CODE -- <language/runtime>; programs and raw outputs are pasted in the appendix.
```

If you declare `CODE` you must paste, in an appendix, **the exact source of every program
you ran and its raw unedited output**. If you declare `NONE`, then **every** number you
state must be accompanied by the hand derivation that produced it, in one or two lines.

**This is not a formality and it is enforced.** A previous report from this engine family
was ruled VOID because it recited every number that its brief had printed and **fabricated
every number it would have had to compute**, while presenting all of them as verified. The
PART 6 held-out table exists specifically to detect that failure mode. Presenting a number
as computed when you did not compute it voids the entire round, regardless of how good the
rest of the review is. **If you cannot compute something, write `CANNOT COMPUTE` and say
why — that answer is accepted and costs you nothing.**

Every graph you exhibit — counterexample, control, or illustration — must be given as a
**complete edge list** and validated against **EVERY** defining constraint of the class it
illustrates, **the most basic constraint first** (simple, connected, **C4-free FIRST**,
then a-values, then geodesics, then `path`), not only the constraints your argument uses.
A witness that secretly contains a C4 is worse than no witness.

---

# PART 1 — DEFINITIONS (exact; use these and nothing else)

All graphs are finite, simple, undirected, connected.

* **C4-free**: no two distinct vertices have two or more common neighbours (equivalently
  no 4-cycle as a subgraph; chords irrelevant). **Triangles are allowed.**
* `N(v)` = open neighbourhood; `a(v) := alpha(G[N(v)])` = independence number of the graph
  induced on `N(v)`; `d(v)` = degree; `t(v)` = number of triangles containing `v`.
* `l(G) := (1/n) * sum_v a(v)`, `n = |V(G)|`;  `mu(G) := min_v a(v)`.
* `path(G)` := the number of **vertices** of a longest induced path. An **induced P_k** is
  a chordless path on `k` vertices.
* `ecc(v)`, `rad(G)`, `diam(G)` as usual. A **geodesic** `u_0 … u_d` is a shortest path
  (`dist(u_i,u_j) = |i-j|`), hence automatically induced, so `path(G) >= diam(G) + 1`
  always.
* A **usable side-neighbour** of the end `u_0` of a geodesic `u_0 … u_d` is a vertex
  `x in N(u_0)` lying **outside `u_1`'s component of `G[N(u_0)]`**. One exists iff
  `a(u_0) >= 2`.
* A geodesic is **3-capped at the end `u_0`** if every usable side-neighbour `x` of `u_0`
  has `a(x) <= 3` (vacuously so if there is none). `G` is **peripherally 3-capped** if
  **every geodesic of length >= rad(G) is 3-capped at both ends**.
* An **`a = 1` vertex** is a leaf (degree 1) or a **triangle-leaf** (degree 2 with its two
  neighbours adjacent). These are exactly the vertices with `a(v) = 1`.

---

# PART 2 — BACKGROUND FACTS (context; NOT under review — but see the audit in PART 5)

**F1.** C4-free `<=>` no two vertices have two common neighbours `=>` `G[N(v)]` is a
matching plus isolated vertices `=>` `a(v) = d(v) - t(v)`, and the components of
`G[N(v)]` are singletons or single edges, exactly `a(v)` of them.

**F2 — Lemma G14 (PROVED earlier, treat as given, but its PROOF is reproduced because
R12-M1 is about that proof).** *Let `G` be C4-free with a geodesic `u_0 … u_d`, `d >= 5`,
`a(u_0) >= 3`, `a(u_d) >= 2`, and let `x in N(u_0)` be a usable side-neighbour with
`a(x) >= 4`. Then `path(G) >= d + 4`.*
**Proof as originally written.** Pick `y in N(u_d)` outside `u_{d-1}`'s component of
`G[N(u_d)]` (possible since `a(u_d) >= 2`). Pick `w in N(x)` as follows: `G[N(x)]` has
`a(x) >= 4` components; one of them contains `u_0`; `|N(x) cap N(u_2)| <= 1` and
`|N(x) cap N(u_3)| <= 1` by C4-freeness (note `x !~ u_2` and `x !~ u_3`), so those two
intersections destroy at most one component each; at least one component survives, and we
take `w` in it. Then: `w !~ u_0` (different component of `G[N(x)]` — careful, `w` is
chosen outside `u_0`'s component); `w !~ u_1` (else `w, x, u_0, u_1` is a C4);
`w !~ u_2, u_3` by the choice; for `i >= 4`, `dist(w, u_i) >= i - 2 >= 2`; `w` is not on
the geodesic (`dist(u_0, w) = 2` and `w != u_2` since `x !~ u_2`); `dist(w, y) >= d - 3
>= 2` so `w !~ y` and `w != y`; and `dist(x, y) >= d - 2 >= 3`. Hence
`w, x, u_0, u_1, …, u_d, y` induces a path on `d + 4` vertices. **QED**

**F3 — Theorem G38 (PROVED earlier; a non-Qwen S3 pass returned `MATHEMATICS DEFECT
FOUND: NO` on it).** *A connected C4-free **peripherally 3-capped** graph has `l < 4`.*
**F3' — the contrapositive used below.** *Any connected C4-free graph with `l > 4` has a
geodesic of length `>= rad` with an end `u_0` carrying a usable side-neighbour `x` with
`a(x) >= 4`.*

**F4 — peeling (corrected form).** Deleting an `a = 1` vertex from a C4-free graph keeps
it C4-free and connected, and raises `sum_v a(v) - 3n` by `+1` (leaf) or `+2`
(triangle-leaf), so **always by `>= +1`**. *(The project previously stated "exactly +1";
that was false for triangle-leaves and has been corrected. Every use needs only `>= +1`.)*

**F5 — the two standing witnesses (owner-constructed, machine-verified; recompute what you
use).**
* **W1** = two disjoint copies of the point/line incidence graph of `PG(2,5)` (each
  `n = 62`, 6-regular, bipartite, C4-free), joined by a path with 5 new internal vertices
  attached at two distinct vertices of each copy. Verified: `n = 129`, C4-free,
  `l = 252/43 = 5.8604…`, `rad = 6`, `diam = 12`, `mu = 2`, a-histogram
  `{2: 5, 6: 122, 7: 2}`.
* **W2** = `Cay(PSL(2,11), S)` with `S = {g, g^-1 : g in {[5 0; 2 9], [1 5; 0 1],
  [1 6; 10 6]}}` over `GF(11)`. Verified: `n = 660`, connected, 6-regular,
  **triangle-free**, **C4-free**, hence `a(v) = 6` for all `v` and `l = 6`;
  vertex-transitive so `rad = diam = 5`; certified induced path on 168 vertices.
  W2 is the project's **hard positive control**: `diam + 1 = 6 < rad + 4 = 9`, so the
  trivial device `path >= diam + 1` does NOT settle it.
* **PG(2,3) incidence**: `n = 26`, 4-regular, bipartite, C4-free, every `a(v) = 4`,
  `l = 4.0` exactly, `rad = diam = 3`. This is the **below-threshold control** for `l > 4`
  and the **below-threshold control** for `rad >= 5`.

---

# PART 3 — THE DIFF UNDER REVIEW (four statements with full proofs)

## D1. Lemma G41 — "G14's hypothesis `a(u_0) >= 3` is redundant at `d >= 5`"

> **Lemma G41.** `G` C4-free, geodesic `u_0 … u_d` with `d >= 5`, **`a(u_0) >= 2`**,
> `a(u_d) >= 2`, and some usable side-neighbour `x` of `u_0` with `a(x) >= 4`. Then
> `path(G) >= d + 4`.

**Proof as written.** G14's construction (F2 above), unchanged. The construction never
selects a **third** component of `G[N(u_0)]` — it names only `x` — so `a(u_0) >= 2`
(which "some usable side-neighbour `x`" already presupposes) is all it consumes. **QED**

**Scope guard as written.** At `d = 4` and `d = 3` the corresponding proofs (Lemmas G36,
G37, not under review here) pick a second side-neighbour `z in N(u_0)` outside **both**
`u_1`'s and `x`'s components, which genuinely needs `a(u_0) >= 3`. So G41 does **not**
propagate downwards.

**Certification claimed.** 120 machine-certified frames with `a(u_0) = 2` **exactly** and
`d >= 5` on path-joined `PG(2,5)` chains; the construction built a chord-free `d+4` path
every time; 0 failures.

## D2. Theorem G42 — pocket 2's `rad >= 5` branch closes for `mu >= 2`

> **Theorem G42.** `G` connected, C4-free, `l(G) > 4`, `rad(G) >= 5`, and `mu(G) >= 2`
> (no vertex of a-value 1). Then `path(G) >= rad(G) + 4`.

**Proof as written.** By F3' (G38's contrapositive) there is a geodesic `u_0 … u_d` with
`d >= rad(G) >= 5` and a usable side-neighbour `x` of `u_0` with `a(x) >= 4`. Since
`mu(G) >= 2`, both `a(u_0) >= 2` and `a(u_d) >= 2` hold for free — and `a(u_0) >= 2` is
now all the seed needs, by G41. Apply G41 at `d >= 5`: `path(G) >= d + 4 >= rad(G) + 4`.
**QED**

**Certification claimed.** 50 end-to-end runs on W1 and W2: a real cap-break geodesic
located on the graph, the G41 path built by the proof's own recipe, certified induced, and
compared with `rad + 4`. **On W2 the constructed path has exactly `9 = rad + 4` vertices**
— the mechanism delivers the bound with no slack.

## D3. Lemma G43 — far-end truncation

> **Lemma G43.** `G` C4-free with a geodesic `u_0 … u_d`, **`d >= 6`**, `a(u_0) >= 2`, and
> a usable side-neighbour `x` of `u_0` with `a(x) >= 4`. Then `path(G) >= d + 3`, **with
> no hypothesis at all on `a(u_d)`**.

**Proof as written.** If `a(u_d) >= 2`, G41 gives `d + 4 >= d + 3`. So let `a(u_d) = 1`;
then `N(u_d)` is either `{u_{d-1}}` (leaf) or `{u_{d-1}, q}` with `q ~ u_{d-1}`
(triangle-leaf). **Truncate** to the geodesic `u_0 … u_{d-1}`, of length `d - 1 >= 5`, and
take `y := u_d` as the far-side vertex. This is legitimate: `u_d in N(u_{d-1})`, and `u_d`
lies outside `u_{d-2}`'s component of `G[N(u_{d-1})]` — in the leaf case `u_d` is isolated
there; in the triangle-leaf case its component is `{u_d, q}`, and `u_{d-2} !in {u_d, q}`
because `u_{d-2} != u_d` (distance 2) and `u_{d-2} = q` would force
`dist(u_{d-2}, u_d) = 1`, contradicting the geodesic. *(Note `u_{d-2} ~ q` is also
impossible: `q` would then have two neighbours inside `G[N(u_{d-1})]`, which is a
matching.)* Hence `a(u_{d-1}) >= 2` with `y = u_d` witnessing it, `x` is still a usable
side-neighbour of `u_0` for the truncated geodesic (same first step `u_1`), and G41 at
`d - 1 >= 5` gives `path >= (d-1) + 4 = d + 3`. **QED**

**Certification claimed.** 24 truncation runs on graphs that **do** carry `a = 1` vertices
(leaf and triangle-leaf variants of a chain graph of W1's family), 0 failures. *(Their `l`
values are deliberately NOT printed here — see PART 6, rows H3/H4.)*

## D4. Corollary G44 — the `a = 1` case shrinks to one configuration

> **Corollary G44.** `G` connected, C4-free, `l(G) > 4`, `rad(G) >= 5`. Then
> `path(G) >= rad(G) + 4` **unless** *every* geodesic of length `>= rad` that fails to be
> 3-capped at an end has **length exactly `rad`** *and* **`a = 1` at its far end**.

**Proof as written.** Such a geodesic exists by G38 (F3'). If one of them has length
`d >= rad + 1 >= 6`, G43 gives `path >= d + 3 >= rad + 4`. If one of them has far end with
`a >= 2`, G41 gives `path >= d + 4 >= rad + 4`. **QED**

**Non-vacuity claimed.** The class `{C4-free, l > 4, rad >= 5, some a = 1 vertex}` is
claimed to be inhabited by **W1 + a leaf** and **W1 + a triangle-leaf**, so the residual
configuration cannot be dismissed as empty without an argument. *(The `l` values of those
two graphs are deliberately NOT printed anywhere in this brief — see PART 6, rows H3/H4.)*

---

# PART 4 — THE JOINTS (verdict each one)

| ID | Class | What to verify |
|---|---|---|
| **R12-M1** | **MATHEMATICS — a gate joint** | **G41's redundancy claim.** Re-derive F2's construction line by line and determine **exactly** which hypotheses each step consumes. The claim is that `a(u_0) >= 3` is never used. Check in particular: (i) does "`w` is chosen outside `u_0`'s component of `G[N(x)]`" require anything about `G[N(u_0)]`? (ii) is `w !~ u_0` actually justified — `w in N(x)` and `u_0 in N(x)`, so `w !~ u_0` needs `w` outside `u_0`'s **component** of the matching `G[N(x)]`, not merely a different vertex; is the component count `>= 4` used correctly (one for `u_0`, at most one killed by `N(x) cap N(u_2)`, at most one by `N(x) cap N(u_3)`, leaving `>= 1`)? (iii) the claims `x !~ u_2` and `x !~ u_3` — where do they come from, and are they used before they are established? (iv) `dist(w,y) >= d - 3` and `dist(x,y) >= d - 2`: verify both, and identify **the exact smallest `d`** for which every inequality in the proof holds — the lemma claims `d >= 5`; is `d >= 5` right, too weak, or too strong? (v) Finally, the **scope guard**: confirm or refute that the redundancy does **not** extend to `d = 4` or `d = 3`. |
| **R12-M2** | **MATHEMATICS — the gate joint the theorem turns on** | **G42's interface between F3' and G41.** This is a three-line proof whose entire risk is in the handoff. Verify: (i) does F3' (G38's contrapositive) really deliver a usable side-neighbour with `a(x) >= 4` **at an end of a geodesic of length `>= rad`** — and at the end you then call `u_0`? The definition of "3-capped at an end" is per-end; make sure the orientation is not silently swapped. (ii) The proof needs `d >= 5`; it gets it from `d >= rad >= 5`. Check that F3' gives a geodesic of length `>= rad` and not `= rad`, and that `rad >= 5` is used only there. (iii) `mu >= 2 => a(u_0) >= 2 and a(u_d) >= 2`: trivial, but confirm nothing else is needed at the far end. (iv) The conclusion is `path >= d + 4 >= rad + 4`; check the direction of that inequality. (v) **Vacuity**: the hypotheses are `l > 4`, `rad >= 5`, `mu >= 2` — verify from W1's data that they are simultaneously satisfiable, and say what happens if they are not. |
| **R12-M3** | **MATHEMATICS** | **G43's truncation.** The delicate part is the triangle-leaf sub-case. Verify: (i) that `a(u_d) = 1` really forces `N(u_d) in {{u_{d-1}}, {u_{d-1}, q}}` with `q ~ u_{d-1}` — could `a(u_d) = 1` arise some other way? (ii) that `u_0 … u_{d-1}` is still a geodesic (immediate, but state it); (iii) that `u_d` is outside `u_{d-2}`'s component of `G[N(u_{d-1})]` in **both** sub-cases, including the parenthetical argument that `u_{d-2} !~ q`; (iv) that `x` remains a **usable** side-neighbour of `u_0` for the truncated geodesic — the definition refers to `u_1`'s component of `G[N(u_0)]`, which is unchanged, so this should be free; confirm; (v) that `a(x) >= 4` is still available and that G41's own hypotheses (`d-1 >= 5`, `a(u_0) >= 2`, `a(u_{d-1}) >= 2`) all hold; (vi) **the arithmetic**: G41 at `d-1` gives `(d-1)+4 = d+3`, and the lemma claims `d >= 6`; is `d >= 6` exactly right? What is claimed at `d = 5`? |
| **R12-M4** | **MATHEMATICS** | **G44's quantifier structure.** The statement is "conclusion **unless** every bad geodesic is short-and-a=1-ended". Verify the logical form: G38/F3' guarantees **at least one** geodesic of length `>= rad` that is not 3-capped at an end; the negation of the "unless" clause says **some** such geodesic has length `> rad` **or** has `a >= 2` at its far end. Check that the proof's two cases really cover that negation, that "far end" is unambiguously defined relative to the end where the cap breaks, and that a geodesic could not fail to be 3-capped at **both** ends in a way that breaks the orientation bookkeeping. Also check the numeric chain `d >= rad + 1 >= 6` (it needs `rad >= 5`) and `d + 3 >= rad + 4`. |
| **R12-B1** | BOOKKEEPING | **The two witnesses W1 and W2 (F5).** For **W1**: verify the exact mass arithmetic claimed for the general chain, `n(k) = 72k - 10` and `sum_v a(v) = 394k - 22` (so `l(k) = (394k-22)/(72k-10)` decreasing to `394/72 = 5.472…`), and the a-value bookkeeping behind it (each internal path vertex has `a = 2`; each attachment vertex gains exactly `+1`; every other vertex keeps `a = 6`) — is "gains exactly `+1`" right, and does it depend on the attachment vertex having no triangle? Verify C4-freeness is preserved by the path-joining. For **W2**: verify the general device — *vertex-transitive `=>` rad = diam*, and *triangle-free `k`-regular `=>` `l = k` exactly* — and say whether the device needs C4-freeness anywhere. You are **not** required to rebuild `Cay(PSL(2,11), S)`, but if you do, report what you find. |
| **R12-B2** | BOOKKEEPING | **The ledger claims drawn from the diff.** (i) "The VACUOUS-UNTESTED annotation on G38's `rad >= 5` consequence is LIFTED" — does W1 actually satisfy `l > 4` **and** `rad >= 5`, and does that lift the annotation as stated? (ii) "(3CAP-GLUE) is halved by G41 at `rad >= 5`, leaving exactly the far end, named (FAR-2)" — is that an accurate account of what G41 removes? (iii) "Pocket 2's `rad >= 5` branch reduces entirely to the `a = 1` case" (from G42) and then "to ONE configuration" (from G44) — are those two reduction claims correct **and** consistent with each other? (iv) F4's corrected peeling arithmetic: verify the `+1` / `+2` split and confirm that G42/G43/G44 do not use peeling at all. |
| **R12-B3** | BOOKKEEPING | **Tightness and non-vacuity annotations.** (i) The claim that on W2 the G42 construction yields a path of **exactly** `rad + 4 = 9` vertices, presented as evidence that the check is not passing by a huge accidental margin — is that a fair reading, given that `path(W2) >= 168`? State the honest version. (ii) The claim that `{C4-free, l > 4, rad >= 5, some a = 1 vertex}` is inhabited by `W1 + leaf` and `W1 + triangle-leaf` — check that attaching a leaf to W1 preserves C4-freeness and keeps `l > 4`, and recompute `l` for both. (iii) Is there any statement in the diff whose **hypotheses have no exhibited instance**? |

---

# PART 5 — TWO MANDATORY PROBES (a report missing either is rejected)

## PROBE 1 — the statement-hypothesis audit, BOTH directions

Build a table with one row for **each** of: F1, F2 (G14), F3 (G38), F3', F4, G41, G42,
G43, G44. For each row give **two** verdicts:

* **Direction A (statement WIDER than its proof — a real defect).** Is the statement as
  printed true only under some hypothesis its proof silently uses but the statement omits?
  If yes, give a **counterexample to the statement as printed** (edge list).
* **Direction B (statement NARROWER than its proof — free generality).** Does the proof in
  fact establish something stronger (a weaker hypothesis, a stronger conclusion, a wider
  class)? If yes, state the stronger version. **Direction B findings are adopted, not
  penalised** — G41 itself is a Direction-B finding about G14, so this probe is exactly the
  species that produced the diff, and a second one would be valuable.

## PROBE 2 — the control section, three parts

1. **Positive controls that must execute.** Run each of G41/G42/G43/G44 against **W2** and
   **W1** and report, per statement, whether its hypotheses hold and whether its conclusion
   holds. **W2 is mandatory** — it is the only known instance where the trivial
   `path >= diam + 1` device does not settle the conclusion.
2. **Below-threshold controls that must NOT execute.** `PG(2,3) incidence` has `l = 4.0`
   (not `> 4`) and `rad = 3` (not `>= 5`). Confirm that G42 and G44 do **not** execute on
   it, and name the **first** hypothesis that fails, for each.
3. **Counterfactual availability check (this is the part that has caught defects before).**
   For every lemma the text claims is AVAILABLE in the branch a control lands in, verify
   that lemma's hypotheses **on the control** — not only the steps the text actually
   executes. Example of the failure species to hunt: the text says "by G41" in a situation
   where G41's `a(x) >= 4` is not actually available.

## PROBE 3 (short, but do not skip) — the frame/graph currency rule

This project has twice been misled by reporting "0 counterexamples in N local
configurations" in a way that reads as evidence about **graphs**. A local configuration
(geodesic + a few named neighbours) is not a graph, and `path(G)` is a property of the
whole graph. **Audit every certification claim in PART 3** ("120 certified frames", "50
end-to-end runs", "24 truncation runs") and state, for each, whether the claimed evidence
is about **configurations** or about **completed graphs**, and whether the surrounding
prose respects that distinction.

---

# PART 6 — HELD-OUT CHECKS (mandatory table; a report without it is VOID)

Every row below asks for a value that the mathematics under review **implies** but that
this brief **deliberately does not print anywhere**. Reproduce the table in your report
with your answers filled in, one derivation line per row.

**Rules.** (1) You may not answer a row by quoting a number printed elsewhere in this
brief — none of these are printed, so any such quote is a fabrication. (2)
`CANNOT COMPUTE — <reason>` is an **accepted** answer and costs you nothing. (3) A
confidently stated wrong value in this table **voids the round**; an honest
`CANNOT COMPUTE` does not.

| row | held-out question |
|---|---|
| **H1** | Build the **2-copy chain with `L = 7` internal path vertices** (same recipe as W1 but 7 internal vertices instead of 5). Give `n`, `sum_v a(v)`, and `l` as an **exact fraction** and as a decimal to 4 places. Show the three-part a-value bookkeeping that produces the sum. |
| **H2** | How many **edges** does W2 have? State the one-line derivation. |
| **H3** | Attach **one leaf** to W1. Give the new `n`, the new `sum_v a(v)`, and the new `l` as an **exact fraction**. Does the answer depend on which vertex of W1 you attach it to? Justify. |
| **H4** | Attach **one triangle-leaf** to W1 (a new vertex adjacent to both ends of an existing edge). Give the new `n`, `sum_v a(v)` and `l` as an **exact fraction**, and say why the answer differs from H3 in the direction it does. Also state which edges of W1 are legal attachment sites and why. |
| **H5** | Does the `PG(2,3)` incidence graph contain an **induced P7**? Answer yes/no **and give a witness as an explicit vertex sequence** (define your point/line labelling first), or `CANNOT COMPUTE`. |
| **H6** | In G41's proof, suppose `a(x) = 4` **exactly**. Count the components of `G[N(x)]` that are guaranteed to survive the selection of `w`, showing each subtraction. Then answer: **would a `u_4`-kill also be required at `d >= 5`, and what would that do to the count?** Justify your answer from the distances, not from our text. |
| **H7** | In G43's **triangle-leaf** sub-case, how many vertices does the finally constructed induced path have, and **which vertices of the original geodesic `u_0 … u_d`, if any, are absent from it?** Name them, or say "none" — and justify. |
| **H8** | In G42's proof, **at exactly which step is the hypothesis `rad(G) >= 5` consumed**, and what is the **weakest hypothesis that could replace it** while leaving the proof intact word for word? State the resulting stronger theorem. |

---

# PART 7 — WHAT A USEFUL REPORT LOOKS LIKE

* If you can **refute** any of G41–G44, that is the single most valuable outcome: give the
  edge list and the failing step. A refutation of G41 would also retract G42, G43 and G44.
* If you cannot, say so plainly and show the strongest attack you tried and why it failed.
* Word budget: aim for 2000–4000 words. Completeness of the joint verdicts beats breadth.
* Do not restate the diff back to us; we have it. Report only findings.


---
DELIVERY OVERRIDE (transport constraint — the gateway 500s on long generations; your
report is split into two calls; this is CALL A):
Deliver ONLY these sections now, hard cap 1100 words total:
1. PART 0.5 execution-environment declaration (first line, as demanded).
2. The full held-out table (all 8 rows, with derivations).
3. Joints R12-M1..R12-M4 verdict rows only.
Do NOT deliver the B-joints, probes, defect log, or final verdict yet — CALL B will
request them. End with the line: END-OF-CALL-A