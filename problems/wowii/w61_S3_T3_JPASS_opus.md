# T3 J-PASS — independent adversarial referee report (opus)

VERDICT: PARTIAL — J1's mathematics is sound (I re-proved the disposal and found no `diam = 4` configuration in the branch, by proof and by exhaustive + randomised search), but J1's supporting claim "the branch contains **exactly 10** configurations" is a multiplicity-box artifact — the branch is an **infinite** family — and J2 leaves its own enclosing heading "*Two wording fixes adopted (neither is a defect)*" still asserting the score it withdraws; neither defect touches Theorem T3's conclusion.

TEXT VERSION REVIEWED: prompts/w61_S3_T3_JPASS.md

Tooling: my own `residueAux`/labelled Havel–Hakimi and my own Lemma-P parameteriser, written from the appendix-A/appendix-D specs, in
`/private/tmp/claude-501/-Users-user-workspace-claudecode-automath/56a6218b-985b-4b55-8a4d-79038be0c88d/scratchpad/`
(`hh.py`, `param.py`, `validate.py`, `branch.py`, `hunt.py`, `checks.py`, `fa.py`).
No number in this report is copied from the brief; every figure below was produced by those scripts. I read no other repository file.

**Calibration before use** (`hh.py`, required by probe 1):

```
residue(K2) = 1 expected 1 OK
residue(C3..C9) = 1,2,2,2,3,3,3  = ceil(n/3) for n=3..9   OK (7/7)
extra: residue(K_{1,5})=5, residue(P4)=2, residue(K_{2,3})=2 with heads (3,2,1)
```
`param.py`'s fast α and f routines were cross-validated against brute force (`validate.py`): 3 334 random instances + 462 exhaustive 0/1-multiplicity instances, **0 mismatches**.

---

## J-M1 — verdict: **SOUND with a bookkeeping defect in the reported enumeration**

The mathematical widening `k = 1 → k ≤ 1` is correct. The four sub-questions:

### (a) Does `k ≤ 1` give "at least two vertices of `B` have degree ≤ 3", and is that all the paragraph uses `k` for? — **YES / YES.**

`k := #{b ∈ B : deg(b) ≥ 4}` and `|B| = 3`, so `#{b : deg(b) ≤ 3} = 3 − k ≥ 2` whenever `k ≤ 1`. Trivially true, and the parenthetical "`k = 0` 时三点全部度 ≤3，更强" is correct.

I walked the amended paragraph clause by clause. `k` appears exactly once, in the opening clause. Everything after it runs on `p = 3`, on `deg(y) = deg_A(y)` (i.e. `deg_B(y) = 0`), and on (F-b):

| step | what it needs | needs `k = 1`? |
|---|---|---|
| designate two `b ∈ B` with `deg ≤ 3` as `y, z` | `k ≤ 1` | no |
| `deg_A(y) ≥ p = 3` | every type-`{x,y,z}` vertex is adjacent to `y` | no |
| `deg(y) = deg_A(y) ≤ 3` ⟹ `deg_A(y) = 3` | `deg_B(y) = 0` (see (b)) | no |
| `n_y = mu[{x,y}] = mu[{y,z}] = 0`, same for `z` | `deg_A(y) = n_y + mu[{x,y}] + mu[{y,z}] + p` | no |
| occurring types ⊆ `{ {x,y,z}, {x} }` | the vanishing above | no |
| (F-b) has no admissible pair ⟹ `diam ≠ 4` | (F-b), i.e. Lemma 4 + `f = α+1` + `diam = 4` | no |

No later step of the paragraph needs `k = 1` exactly. The re-designation "设为 y,z" is legitimate: the parameterisation is symmetric under relabelling of `B`, and at `k = 0` any two of the three work (indeed at `k = 0` all three choices apply simultaneously and force `n_x = 0` as well, i.e. `G = K_{3,3}` — strictly stronger than what the paragraph claims).

**But** — see defect D2 — the sentence *immediately following* the widened paragraph in the same T-b repair block ("后续 `p ≤ 2 ≤ X−2 ⟹ Lemma U ⟹ m ≤ X+4 与 m=X+6 矛盾` 原样有效") **does** need `k = 1` and is false at `k = 0`. J1's quoted paragraph stops at `矛盾。∎`, so this is strictly outside the amendment's text, but it is inside the block the `k = 0` bullet imports by "同上".

### (b) Does `deg_A(y) ≥ 3` with `deg(y) ≤ 3` force `deg_A(y) = 3` and the vanishing — including when `e_B ≠ 0`? — **YES; `e_B = 0` is used only as written, is available in both callers, and is in fact forced.**

Three separate statements, and they must be kept apart:

1. **As literally written the step uses `e_B = 0`.** The text writes `deg(y) = deg_A(y)`, an equality that holds only if `deg_B(y) = 0`. Taken as a standalone claim about "`k ≤ 1`" with no `e_B` hypothesis, this equality is unjustified.
2. **`e_B = 0` is genuinely available in every branch that reaches the paragraph.** The paragraph sits inside the bullet "**k=1, e_B=0**", so the `k = 1` caller supplies it by hypothesis. The `k = 0` caller supplies it *before* the "同上": "**k=0**：由 C2/C3 得 `e_B=0`；由 C1 与 codeg 条件同上得 `p∈{1,2}`" — the order is right, `e_B = 0` is derived first. (C2: `e_B=1 ⟹ k ≥ 1`; C3: `e_B=2 ⟹ k ≥ 2`; (F-c)/R1: `e_B ≤ 2`.) I confirmed the `(e_B,k)` occupancy numerically over 25 236 hard-core instances: cells `(1,0)`, `(2,0)`, `(2,1)` are **empty**, so `k=0 ⟹ e_B=0` and `k=1 ⟹ e_B ≤ 1` hold on the corpus.
3. **The dependence is removable, and `e_B ≠ 0` is vacuous here anyway.** Write `deg(y) = deg_A(y) + deg_B(y) ≥ deg_A(y) ≥ p = 3` and `deg(y) ≤ 3`; then *both* `deg_A(y) = 3` **and** `deg_B(y) = 0` follow, with no `e_B` hypothesis. The same for `z`. Since every edge of `G[B]` is incident to `y` or to `z` (|B| = 3), this forces `e_B = 0`. So in the branch `k ≤ 1, p = 3`, the hypothesis `e_B = 0` is a *consequence*, not an assumption. Verified exhaustively: over all four `G[B]` types with `p = 3`, multiplicities ≤ 6 and `k ≤ 1`, the 19 surviving tuples all have `G[B]` empty; `e_B ∈ {1,2,3}` produced **0** tuples.

So (b) is sound, and a one-clause strengthening (`≥` instead of `=`) would make it airtight even under a standalone reading. I record the `=`-vs-`≥` point as a nit, not a defect, because the hypothesis is available at both call sites.

### (c) Is the type list complete, and does (F-b) genuinely fail on it? — **YES / YES.**

From `deg_A(y) = 3 = p`: `n_y = mu[{x,y}] = mu[{y,z}] = 0`. From `deg_A(z) = 3 = p`: `n_z = mu[{x,z}] = mu[{y,z}] = 0`. That is 5 of the 7 multiplicities killed (`{y}, {z}, {x,y}, {x,z}, {y,z}`); the survivors are `p = mu[{x,y,z}] = 3` and `n_x = mu[{x}]`, unconstrained. So the occurring-type list is exactly `{x,y,z}` plus `{x}` when `n_x ≥ 1` — **complete**, and my enumeration returns precisely this shape and nothing else.

(F-b) needs two occurring types `T₁, T₂` that are **disjoint** with no `G[B]`-edge between them. The three candidate pairs are `({x,y,z},{x,y,z})`, `({x,y,z},{x})`, `({x},{x})`; all intersect (`{x} ⊂ {x,y,z}`), so no pair exists — regardless of `e_B`, and regardless of whether `n_x = 0`. The degenerate patterns probe 2 asks about are handled correctly: at `n_x = 0` only one type occurs and (F-b) still fails; the argument never assumes a multiplicity-0 type is non-empty. Note the argument correctly uses the *disjointness* requirement rather than the weaker corollary "`r ≥ 1`" — with `n_x ≥ 1` a singleton type *does* occur, so the `r ≥ 1` shortcut would **not** have produced a contradiction. The text takes the right route.

I verified (F-b) itself (the direction used, `diam = 4 ⟹ pair exists`) on **25 236** hard-core instances: **0 violations**; the converse (`pair exists ⟹ diam = 4`, Lemma P(d)) also had **0 violations** on the same scan.

### (d) Is the disposal exhaustive? — **YES mathematically, but the reported count of 10 is a box artifact: the branch is infinite.**

My own enumeration (below) returns, for the branch `k ≤ 1, e_B = 0, p = 3` under multiplicity box `mu[T] ≤ MAX`:

| MAX | configurations | k = 0 | k = 1 | diam values | diam = 4 |
|---|---|---|---|---|---|
| 1 | 4 | 1 | 3 | {2,3} | 0 |
| 2 | 7 | 1 | 6 | {2,3} | 0 |
| **3** | **10** | **1** | **9** | {2:1, 3:9} | **0** |
| 4 | 13 | 1 | 12 | {2,3} | 0 |
| 5 | 16 | 1 | 15 | {2,3} | 0 |
| 6 | 19 | 1 | 18 | {2,3} | 0 |
| 7 | 22 | 1 | 21 | {2,3} | 0 |

I reproduce the author's numbers **exactly** — 10 configurations, 1 with `k = 0` and 9 with `k = 1`, none of diameter 4 — but only at `MAX = 3`. The general count is `1 + 3·MAX`. The branch itself is the infinite family

> `G_t` = `K_{3,3}` (between `A₀ = {u₁,u₂,u₃}` of type `{x,y,z}` and `B = {x,y,z}`) plus `t ≥ 0` pendant vertices attached to `x`,

up to which vertex of `B` plays the role of `x`. Every `G_t` is connected, non-forest, has `τ = 3`, `f = α+1` (I checked `t` up to 100: `n = 6+t`, `m = 9+t`, `α = 3+t`, `f = 4+t`), `e_B = 0`, `p = 3`, `k = [t ≥ 1]`, and `diam(G_t) = 2` for `t = 0`, `3` for `t ≥ 1`. So the branch is non-empty and infinite, and "exactly 10 configurations" is false as a statement about the branch (it is the count inside the `MAX = 3` box).

**Is the parameterisation complete for this branch?** Yes. Every `τ = 3` configuration with a chosen maximum independent set `A` is `(mu, G[B])`, and `k`, `e_B`, `p` are all functions of `(mu, G[B])`; nothing in the branch escapes it. The incompleteness is in the **box**, not the parameterisation — and I closed the box gap in closed form: the derivation in (c) shows the branch is *exactly* `{p = 3, n_x = t ≥ 0, all other mu = 0}` up to relabelling, and for every member all A-vertices share the neighbour `x`, so `dist(a,a') ≤ 2` for all `a,a' ∈ A`, `dist(b,b') = 2`, `dist(a,b) ≤ 3`, hence `diam ≤ 3` **unconditionally** — this needs neither `f = α+1` nor the reductio. The disposal is therefore exhaustive over the whole infinite branch, not merely over a box.

**The hunt returned nothing** (as it must, given the above): exhaustive box scans to `MAX = 7`, all four `G[B]` types at `p = 3`, and 400 000 random draws with multiplicities up to 30 (3 808 survived the `k ≤ 1` filter) produced **0** configurations with `k ≤ 1, e_B = 0, p = 3, diam = 4`.

---

## My own enumeration of the branch — code and output

Core of `hh.py` (literal transcription of the appendix-A spec, `List.splitAt` truncation and ℕ-truncated `(·−1)`):

```python
def residue_aux(seq):
    s = sorted(seq, reverse=True); heads = []; traj = [list(s)]
    while True:
        if not s:            return 0, len(heads), heads, traj
        if s[0] == 0:        return 1 + (len(s) - 1), len(heads), heads, traj
        D, rest = s[0], s[1:]
        head_part, tail_part = rest[:D], rest[D:]          # List.splitAt truncation
        head_part = [max(0, v - 1) for v in head_part]     # ℕ-truncated (·−1)
        heads.append(D)
        s = sorted(head_part + tail_part, reverse=True)
```

Core of `param.py` (Lemma-P parameterisation; `TYPES` = the 7 non-empty subsets of `B = {0,1,2}`, `GB` = the 4 iso types of `G[B]`). Graphs are **built literally** and every quantity is read off the built graph:

```python
def build(mu, gb):
    adj = {v: set() for v in B}
    for (u, v) in GB[gb]: adj[u].add(v); adj[v].add(u)
    nxt = 3
    for i, t in enumerate(TYPES):
        for _ in range(mu[i]):
            adj[nxt] = set(t)
            for b in t: adj[b].add(nxt)
            nxt += 1
    return adj, Atypes
# alpha = max over G[B]-independent S ⊆ B of |S| + #{a : N(a) ∩ S = ∅}   (= Lemma P(b))
# f     = max over B' ⊆ B of |B'| + #{light A-vertices} + j, j ≤ 2 heavy ones, acyclicity checked
# diam  = BFS from every vertex;  k = #{b ∈ B : deg(b) ≥ 4};  residue via hh.residue_aux
```
Both α and f were validated against brute force (0/3 796 mismatches) before use.

Branch scan (`branch.py`), `p` pinned to 3, `G[B]` empty, the other six multiplicities swept over `[0,MAX]`, `k ≤ 1` filtered from the degrees, then filtered by *A is a maximum independent set* → *non-forest and `f = α+1`* → *diam*:

```
--- multiplicity box mu[T] in [0,3] (p fixed = 3) ---
  parameter tuples with k<=1 built & connected : 10
  ... of which A is a MAXIMUM ind. set (tau=3) : 10   (k-split {0: 1, 1: 9})
  ... of which also non-forest and f = alpha+1 : 10   (k-split {0: 1, 1: 9})
      diam distribution over those            : {2: 1, 3: 9}
  ... of which diam = 4 (i.e. IN the hard core): 0   <<< the hunt
      mu=(0,0,0,0,0,0,3)  n=6  m=9   degseq=[3,3,3,3,3,3]            k=0 diam=2 alpha=3 f=4 residue=2
      mu=(0,0,1,0,0,0,3)  n=7  m=10  degseq=[4,3,3,3,3,3,1]          k=1 diam=3 alpha=4 f=5 residue=3
      mu=(0,0,2,0,0,0,3)  n=8  m=11  degseq=[5,3,3,3,3,3,1,1]        k=1 diam=3 alpha=5 f=6 residue=3
      mu=(0,0,3,0,0,0,3)  n=9  m=12  degseq=[6,3,3,3,3,3,1,1,1]      k=1 diam=3 alpha=6 f=7 residue=4
      ... (the same three for mu[{y}] and mu[{x}] by relabelling: 1 + 3·3 = 10)
--- ... [0,7] --- 22 configurations (1 with k=0, 21 with k=1), diam ∈ {2,3}, diam-4 hits 0
Can e_B != 0 occur at all with k<=1 and p=3?  (all four G[B] types, mu ≤ 3)
  G[B]=empty     e_B=0 : k<=1 tuples=10  A-max=10  HC0=10  diam4=0
  G[B]=edge      e_B=1 : k<=1 tuples=0   ...
  G[B]=path      e_B=2 : k<=1 tuples=0   ...
  G[B]=triangle  e_B=3 : k<=1 tuples=0   ...
```
Wide cross-checks (`hunt.py`, `fa.py`), all four `G[B]`, `mu ≤ 3`:
```
hard-core (connected, non-forest, diam=4, f=alpha+1, tau=3) instances: 25236
(e_B,k) occupancy: {(0,0):3, (0,1):33, (0,2):681, (0,3):9210, (1,1):6, (1,2):177,
                    (1,3):8142, (2,2):27, (2,3):6957}      # (1,0),(2,0),(2,1) empty
(F-b) violations among them: 0        Lemma P(d) converse violations: 0
hard-core instances with k<=1, e_B=0, p=3: 0
k<=1, e_B=0, mu<=4, f=alpha+1, non-forest : p-distribution {1: 13, 2: 78, 3: 13}
   ... restricted to diam=4 (the hard core): p-distribution {1: 12, 2: 36}
instances with A maximum, non-forest, f=alpha+1 (no diam filter): 48064 (k: {0:13,1:125,2:1823,3:46103})
   (F-a)/Lemma 4 violations by k: 0 ;  Lemma C1 violations by k: 0
   control: of 3219 instances with f ≠ alpha+1, (F-a) fails in 3193  (f = α+1 is a real hypothesis)
```
The `p`-distribution line is the sharpest confirmation of J1: at `k ≤ 1, e_B = 0` the value `p = 3` **does occur** (13 instances at `MAX = 4`) among graphs satisfying every hard-core condition except `diam = 4`, and it disappears the moment the `diam = 4` filter is applied. That is exactly the claim J1 makes, and it is exactly why the branch cannot be dismissed as parameter-empty.

---

## J-B1 — verdict: **the withdrawal is correct, but J2 is incomplete**

* **Is the "undercount" reading wrong at `D_3 = 1`? — YES, J2 is right.** Lemma T's terminal shape is `[D_τ, 1^{D_τ}, 0^…]`; at `D_3 = 1` that is `[1, 1, 0^…]`, which has exactly **one** `1` after the head (two in total). The withdrawn diagnosis justified "undercounts" by the parenthetical "has `D_3` ones **after** the head" — i.e. by the very count, `1`, that the clause states. Under its own stated reading the diagnosis is self-defeating; there is no undercount. (Pedantically: under the *total*-ones reading the clause's `1` does undercount by one, `1` vs `2` — but that is not the reading the withdrawn diagnosis invoked, and J2 correctly scopes its claim to "after the head".)
* **Is R3's diagnosis the right one? — YES.** I recomputed the branch's trajectory from the degree sequence `[a₀+c₀+2, b₀+c₀+2, 3, 3, 2^{c₀}, 1^{a₀+b₀}]` for all **196** admissible triples `a₀,b₀,c₀ ∈ 1..7` with `X ≥ Y`: `D = (X, Y−1, 1)`, `L² = [1,1,1,1,0^…]`, and `Σ_{i≤3} D_i = m − 1` in **196/196**. Required after head = 1, actual after head = 3; required total = 2, actual total = 4. The clause pairs required-after-head (`1`) with actual-total (`4`) — precisely R3's description. It miscounts under either consistent reading, while the contradiction survives under either. Deleting it and keeping `Σ D_i = m−1 < m` is the right treatment.
* **Does J2 leave any other sentence still asserting the withdrawn score or diagnosis? — YES, one: the enclosing heading.** J2 replaces the bullet but not its parent heading, which reads

  > "### Two wording fixes adopted (**neither is a defect**)"

  After J2, the second item under that heading says the clause "**is a genuine miscount**", upheld as a defect (T-J4) and deleted by R3. The heading therefore contradicts the bullet it introduces, and both of its assertions are now wrong for that item: it is not a "wording fix" (it is a withdrawal plus a pointer to an operative repair), and it *is* a defect. This is defect **D3** below. I grepped the whole appendix for `terse` / `undercount` / `wording fix` / `neither is a defect`: the only residual assertion is that heading (line 632); no other sentence re-asserts the withdrawn score or diagnosis.

---

## Defects

### D1 (J1, bookkeeping — the reported enumeration). Repairable: **yes**. T3 conclusion: **survives**.

> "the author reports it contains exactly **10** configurations, **1 with `k = 0`** and 9 with `k = 1`, with `diam = 4` in **none** of them."

Why it fails: the branch `k ≤ 1, e_B = 0, p = 3` is **infinite**. Its members are exactly `p = 3, n_x = t ≥ 0` (all other multiplicities 0), up to relabelling of `B`; every one of them satisfies connected + non-forest + `τ = 3` + `f = α+1`, so no hard-core filter truncates the family. The count is `1 + 3·MAX` inside a box `mu ≤ MAX`, so `10` is the `MAX = 3` figure reported without its box. Smallest configuration exposing it: `MAX = 4` already yields **13** (add `t = 4`, i.e. `K_{3,3}` plus four pendants at one `B`-vertex, `degseq = [7,3,3,3,3,3,1,1,1,1]`, `n = 10`, `m = 13`, `α = 7`, `f = 8`, `diam = 3`) — a legitimate branch member outside the reported 10. Repair: state the box, or better, replace the count with the closed-form characterisation and the unconditional `diam ≤ 3` proof of (d), which covers the whole family and makes the scan redundant. **This is a defect in the numerical backing, not in the argument**: the mathematical claim ("`diam = 4` in none of them") is true of every member, as I proved.

### D2 (J1, scoping — the sentence next to the widened paragraph). Repairable: **yes, one clause**. T3 conclusion: **survives**.

> "因此 `p ∈ {1,2}` 的结论不变，后续 `"p ≤ 2 ≤ X−2 ⟹ Lemma U ⟹ m ≤ X+4 与 m=X+6 矛盾"` 原样有效。"

This sits immediately after the paragraph J1 widens, inside the same T-b repair block — the block the `k = 0` bullet imports by "同上". It is a **`k = 1`-only** claim and is **false at `k = 0`**, which is the "second most valuable outcome" the brief asks for, in its non-load-bearing form. Smallest (indeed only) configuration exposing it — the unique `k = 0` hard-core instance, which I re-derived independently:

```
degseq=[3,3,3,3,3,2,1]  mu=(n_z=1, mu[{x,y}]=1, p=2) gb=empty  n=7 m=9  X=3
   p ≤ 2 ≤ X−2 ?  X−2 = 1 < 2 = p        -> premise FAILS
   Lemma U 2nd premise (Δ ≥ #3s in R):  Δ=3, R=[3,3,3,3,2,1], #3s=4  -> FAILS
   Lemma U would give m ≤ Δ+4 = 7 ; true m = 9                       -> FALSE conclusion
   (m = X+6 = 9 does still hold; only the Lemma-U half breaks)
   HH heads=[3,3,2,1], steps=4, residue=3 = α−1
```
So a reader who takes J1's "`k ≤ 1`" as widening the surrounding block would resurrect exactly the blanket "`k ≤ 1 ⟹ Lemma U 可用`" claim that the 5bis revision note retracted, on the document's own control instance. Harmless in fact, because the `k = 0` bullet imports only the conclusion `p ∈ {1,2}` and then runs its own `p = 1` / `p = 2` treatment and its own explicit HH trajectory, never calling Lemma U. Repair: append "（在 `k = 1` 下）" to that sentence, or move it out of the widened block. Verified on the other side too: over the 45 hard-core instances with `k = 1, e_B = 0` (`mu ≤ 4`), `Y = Z = 3`, `m = X + 6` and `p ≤ X − 2` hold in **45/45**, so the sentence is correct at `k = 1`.

### D3 (J2, incomplete withdrawal). Repairable: **yes, one heading**. T3 conclusion: **survives**.

> "### Two wording fixes adopted (neither is a defect)"

The heading survives J2 and still asserts, of the very item J2 rewrites, that it is a wording fix and not a defect — while the replacement bullet calls it a genuine miscount upheld and deleted by R3. Smallest exposure: read the heading and its second bullet in sequence. Repair: retitle (e.g. "One wording fix adopted, one earlier score withdrawn") or add "（第二条已由 J2 撤回，见 R3）".

**Nit (not a defect).** The `p ≥ 4` sentence in the same block still ends "得 `k=3`，与 `k=1` 矛盾"; at `k = 0` the reader must substitute "与 `k=0` 矛盾". The derivation (`deg_A(b) ≥ p ≥ 4` for **all** `b`, hence `k = 3`) contradicts any `k ≤ 1`, so the substance is fine — but the sentence was not widened along with the `p = 3` one, leaving the block mixed-scope.

**Does Theorem T3's conclusion survive?** Yes, on all three counts. J1's disposal of `k ≤ 1, e_B = 0, p = 3` is correct and I proved it independently and unconditionally; the `k = 0` bullet's "同上" is legitimate for the conclusion it imports (`p ∈ {1,2}`), since the `p = 0`, `p ≥ 4` and `p = 3` exclusions are each valid at `k = 0`; and my scan confirms `p ∈ {1,2}` on every `k ≤ 1` hard-core instance.

---

## T12 — counterfactual availability

Concrete configuration: **`G₀ = K_{3,3}`** — the unique `k = 0` member of the branch (`mu`: `p = 3`, all else 0). My computation: `n = 6`, `m = 9`, `degseq = [3,3,3,3,3,3]`, `α = 3`, `τ = 3`, `f = 4 = α+1`, non-forest, `e_B = 0`, `k = 0`, `p = 3`, `codeg(u,v) = 3` for all three pairs, `diam = 2`, HH heads `(3,3,2,1)`, `s = 4`, `residue = 2 = α−1`. Second configuration `G₁ = K_{3,3} +` one pendant at `x` (`k = 1`): `n = 7`, `m = 10`, `degseq = [4,3,3,3,3,3,1]`, `α = 4`, `f = 5 = α+1`, `diam = 3`, heads `(4,3,2,1)`, `residue = 3 = α−1`.

| lemma the argument cites or has in scope | hypotheses on `G₀`? | what it yields / which hypothesis fails |
|---|---|---|
| **Lemma 3** (`f ≥ α+1`) | hold (connected, `n ≥ 2`) | `f ≥ 4`; true, `f = 4`. This is the T-c repair's source for `f = α+1` and it is `k`-independent. |
| **Fact 2** (`residue ≤ α`) | hold | `residue ≤ 3`; true, `residue = 2`. |
| **Lemma 4 / (F-a)** | hold (`A` maximum, `f = α+1`) | `codeg(u,v) ≥ 2` for the non-adjacent pairs. **Executes, but yields nothing new**: `codeg = p = 3 ≥ 2` already. Verified 0 violations over 48 064 instances with `f = α+1`, `k ∈ {0,1,2,3}`. |
| **(F-b)** | needs `diam = 4`, which **fails** on `G₀` (`diam = 2`) | Inside the reductio `diam = 4` is assumed, and (F-b) is the **only lemma that actually fires** in the widened paragraph: it demands a disjoint occurring pair, none exists, contradiction. |
| **Lemma C1** (`e_B=0 ⟹ deg(b) ≥ 2`) | hold | `deg(b) ≥ 2`. **Never executes in the `p = 3` sub-case** — the paragraph needs `deg_A(b) ≥ 3`, which comes from `p = 3` directly; C1's output is strictly weaker and is used nowhere. Cited at the head of the bullet ("由 C1 与 codeg 条件") and imported by "同上", but inert here. |
| **Lemma U** | first premise holds (`max(R) = 3 ≤ 3`); **second premise `Δ ≥ #{3s in R}` FAILS**: `Δ = 3`, `R = [3,3,3,3,3]`, five 3s | **Named as required: a lemma the text claims is available at `k ≤ 1` but which never executes.** The retracted blanket sentence "`k ≤ 1` … Lemma U 可用" would give `m ≤ Δ+4 = 7` against the true `m = 9`. The `p = 3` paragraph never calls it, and the `k = 0` bullet never calls it. |
| **Corollary N1** (`e_B=0`, `τ≥2`, all `deg(b) ≥ τ+1 ⟹ residue ≤ α−1`) | `e_B = 0` ✓, `τ = 3` ✓, **`deg(b) ≥ 4` FAILS** (`deg = 3` on all of `B`) | Unavailable exactly here — this is *why* the `k ≤ 1` branch needs a bespoke argument rather than the `τ`-uniform machinery. (Its conclusion happens to be true on `G₀` anyway: `residue = 2 = α−1`.) |
| **Theorem N** | premise (i) fails as above | Unavailable; same reason. |
| **Lemma S** (`deg ≥ τ+1 ⟹ head`) | vacuous on `G₀` (no vertex of degree ≥ 4) | Yields nothing. |
| **Lemma T** (terminal shape), **Lemma F3/F3′**, **Lemma H** | require the reductio `s = τ = 3`; on `G₀` `s = 4 ≠ τ` | Unavailable on any concrete member of the branch — every member has `residue ≤ α−1`, so the reductio is false there. Inside the reductio the branch is empty, which is the whole point of the paragraph. F3′ (repair R2) is the version that survives outside the reductio. |

Meta-observation on counterfactual availability: **every** concrete configuration in this branch violates the reductio (I computed `residue = α−1` or `α−2` for `t = 0..100`), so the branch is empty *inside* the reductio and the paragraph's job is only to show that emptiness by a `diam`-based route. J1 does that correctly and, as shown in (d), the route is even reductio-free.

---

## Trajectories

1. Read the brief in full (two passes; 792 lines), then wrote `hh.py` and calibrated it against `K₂` and `C₃…C₉` before computing anything else.
2. Wrote `param.py` from the Lemma-P spec, deriving α from the "max over `G[B]`-independent `S`" formula (which is Lemma P(b) rearranged) and f from a `|B| = 3`-specific argument (at most 2 "heavy" A-vertices can be kept, since `2j + e(B') ≤ (3+j)−1`). **Refused to trust either until** both matched brute force on 3 796 instances.
3. **Hunted first, as instructed.** Attempt 1: exhaustive box scan of the branch to `MAX = 7`. Attempt 2: all four `G[B]` types at `p = 3` (to break the `e_B = 0` assumption) — found the branch forces `e_B = 0`, so no entry there. Attempt 3: 400 000 random draws with multiplicities up to 30, seeking a large-`n` escape. Attempt 4: dropping `f = α+1` and non-forest to see whether a `diam = 4` member exists outside the hard core — none; the closed-form argument in (d) explains why (all A-vertices share the neighbour `x`, so `diam ≤ 3` unconditionally). The hunt is dead, and I can say *why* it is dead rather than merely that it failed.
4. Then attacked the `k = 0` boundary: recomputed the unique `k = 0` hard-core degree sequence and its Lemma-U data, which turned up defect D2.
5. Then J-B1: recomputed the `k=2/e_B=2` trajectory over 196 parameter triples and the two readings of Lemma T's terminal shape; then grepped the appendix for residual assertions of the withdrawn score, which turned up defect D3.
6. Cross-checks last: (F-a)/Lemma 4, Lemma C1, (F-b) and its converse over 25 236 hard-core and 48 064 `f = α+1` instances, split by `k`, to confirm probe 3 (hypotheses hold at `k = 0`, not merely at `k = 1`).

## What I could NOT check

* Anything in the body of Theorem T3 (case split, `k = 2`, `k = 3`, Lemma U's other call sites, R1/R3 as repairs) — out of scope by instruction; I checked R3's *content* only as far as J-B1 required.
* The author's scripts and their printed counts (`w61_tau3.py`, `w61_r3_repair.out`, `w61_r4_a2check.out`, …) — forbidden. Every number here is mine. Where the brief's figures were checkable (10 = 1 + 9; "`diam = 4` in none") I reproduced them exactly at `MAX = 3`; I could not check what box the author used, which is why D1 is stated as "unstated box" rather than "wrong scan".
* The Lean definitions (`Residue.lean`, `Induced.lean`) and hence whether `residueAux` really behaves as appendix A describes — I transcribed the spec as given and calibrated it against the two stated sanity checks, both of which pass.
* Fact 2's bibliography, and the falsification-stage counts of appendix A §2.
* Isomorphism-level counting: my enumeration is of `(mu, G[B])` tuples, i.e. labelled `B`; up to isomorphism the branch is `{G_t : t ≥ 0}`, one graph per `t`. If the author counted up to isomorphism with `t ≤ 9` he would also print "10"; either way the count is a truncation and D1 stands.
* My α/f routines are validated against brute force only for `n ≤ 13`; beyond that I rely on the structural derivations (which are exact for `|B| = 3`) plus the `t = 6` brute-force spot check.

## Out of scope, noticed anyway

*(Recorded only; none of this drove the verdict, and none of it is under review.)*

1. **§7.2 B, Lemma T's phrasing.** "第 τ−1 步后的表恰为 `[D_τ, 1^{D_τ}, 0^…]`" is exactly the shape that produced the J-B1 miscount: written this way the head is *also* a `1` when `D_τ = 1`, so "有 `D_τ` 个 1" is ambiguous by one. A phrasing like "头为 `D_τ`，其后恰 `D_τ` 个 1，其余为 0" would have prevented both the original clause and two rounds of adjudication about it.
2. **§7.3.3, `k = 2`, `e_B = 0` bullet.** "R 中值 ≥3 的项为 y 与 p 个 A-3（`Z≤2` 故 z 不在内），共 `1+p` 个" tacitly assumes `y ≠` the deleted `Δ`-entry and that no *other* `A`-entry of value 3 hides in `R`; it is fine because A-degrees are ≤ 3 and `Z ≤ 2`, but the count is asserted rather than derived, in the same style as the (already-repaired) gap T-a.
3. **Appendix C, Corollary N2's "等价的可用形式".** The contrapositive as printed ("若 (i) 成立、`e_B=0` 且 `m > Δ + τ(τ+1)/2 − 1`，则 `residue ≤ α−1`") silently drops the `residue = α` standing hypothesis that the same revision note just insisted "必须写进命题" — the contrapositive of "`residue=α` ∧ (i) ∧ `e_B=0` ⟹ `m ≤ …`" is "(i) ∧ `e_B=0` ∧ `m > …` ⟹ `residue ≠ α`", which by Fact 2 is `residue ≤ α−1`, so the statement is in fact correct; but it reads as if the hypothesis were being dropped again. Worth one clarifying clause given the history.
4. **§7.6 G firewall.** "Theorem MB and Proposition L2 … cannot be falsified numerically as composite statements; any direct test passes vacuously" is right, and the same firewall applies with equal force to the branch reviewed here: since every member of `k ≤ 1, e_B = 0, p = 3` has `residue < α`, no scan of that branch can ever test a statement that assumes the reductio. This is why I based the J-M1(d) verdict on the reductio-free `diam ≤ 3` proof rather than on any scan.
