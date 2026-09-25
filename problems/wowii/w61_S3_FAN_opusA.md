# S3 round A (non-Qwen, opus) — TARGET: FAN-CHAIN + D-DIFF

VERDICT: **PARTIAL** — the FAN chain's *operative* conclusion survives every attack I could
mount (0 counterexamples in 3.34 M self-computed labelled Havel–Hakimi runs), but Theorem FAN
as stated contains one confirmed defect: its second sentence ("*Equivalently*, every
`Fan(τ,L≥2)` graph has `residue = α − 1`, ... exactly `τ + 1` steps") is **not equivalent to**
and **not proved by** the argument given, and its one-line justification is an invalid
ex-falso inference; four further sub-gap scope/wording items are recorded.

TEXT VERSION REVIEWED: prompts/w61_S3_FAN_A.md (draft §7.8 + §7.9 D1-D5)

Tooling: my own `residueAux` transcription and my own labelled Havel–Hakimi, written from
appendix §1 only, in the session scratchpad. Calibrated: `residue(K₂) = 1`,
`residue(Cₙ) = ⌈n/3⌉` for `n = 3…9` (both reproduced exactly).

---

## Part 1 — per-joint table (F-J1 … F-J7)

| joint | verdict | one-line finding |
|---|---|---|
| **F-J1** | **CORRECT** (over-engineered) | The swap/tie-break-invariance claim is true — in fact *trivially* true: an HH step is a well-defined map on value **multisets**, so the value-multiset trajectory and `s` are independent of every tie-break, not merely of a swap of two equal entries. The "other entry lies in the block" step is fine (`D_j ≥ 1` throughout, so the second copy of the max heads the sorted remainder). The induction is valid: at `j ≤ p` a surviving high vertex has value `deg − (j−1) ≥ τ−j+2` by DICH(b) (available: Lemma S makes every `deg ≥ τ+1` vertex a head), and any *low* head at `j` is capped at `τ−j+2` by DICH(c) — so the max is attained by a high vertex, tie or not. Measured: in **0 of 18 831** runs does any non-`B_hi` entry even *tie* the maximum during the high phase, so the DICH(c) branch never executes (see counterfactual section). |
| **F-J2** | **CORRECT** | Classes `B_hi / C / A′` are exhaustive (`V = B_hi ⊔ C ⊔ A′`, `n = p+(L+1)+\|A′\|`) and disjoint; a head is never a recipient at its own step. `Σ_{j≤p} D_j = Σ_{B_hi} deg − C(p,2)` is DICH(b) summed. `Σ_{B_hi} deg_B = 2(τ−2)+(p−2)(τ−1) = pτ−p−2 = p(τ−1)−2` ✓ (needs `p ≥ 2`, which the set-up establishes from `u,v ∈ B_hi`). The displayed algebra `= p(p−1) − 2 + R − p(p−1)` is garbled but the value `R − 2` is right: `pτ − 2C(p,2) − p(L+1) = p(τ−p−L) = 0`. Cross-check: the two counts are consistent iff `2C(p,2) = p(p−1)` ✓. I verified `Σ_{B_hi} deg = pτ − 2 + R` on **1 118** constructed Fan graphs, 0 failures, and `a_j = g_j − τ` on **3 277 800** labelled runs, 0 failures. |
| **F-J3** | **CORRECT** (one inaccurate parenthetical) | Both cases propagate. `a_j < μ`: exactly `a_j` copies of `w` drop, so `max(M_{j+1}) = w = v` and `v−1` **is** present — contradiction ✓. `a_j ≥ μ`: all maxima drop, `max = w−1 = v`, multiplicity `μ`, so uniqueness forces `μ = 1` ✓. "Other entries `≤ max(other entries of M_{j+1}) + 1`" is right because the unique max of `M_j` maps onto the unique max of `M_{j+1}`, so the remaining `\|A′\|−1` entries map bijectively ✓. Invariant `M_{p−t}` = (max `3+t`, others `≤ t+1`) self-propagates for every `t` (`t+1 < t+2`), and `t = p−1` gives `max(M_1) = p+2 > p` ✓. The "block ∩ A′ = the `a_j` largest of `M_j`" step is tie-safe as a *multiset-of-values* statement (a prefix of the whole sorted list induces a prefix of the `A′` sub-list). It **does** correctly fail at `1+1` — but for a different reason than stated: see Defect D-4. |
| **F-J4** | **CORRECT** | `dec_{A′} = R − 2 + E` ⟹ residue `= 2 − E ≥ 0` ⟹ `E ≤ 2` ✓ (no truncation, by Lemma 1(2)'s graphicality argument). At `E = 2` the `A′` residue is `0` and the `C`-part is `[L+2, L^L]` or `[L+1,L+1,L^{L−1}]`; I independently confirmed **both shapes are non-graphical for `L = 2…6`** (head strictly exceeds the number of positive remaining entries — Erdős–Gallai fails at `k = 1`), and that appending the `A′` zeros does not rescue them. `E ≤ 2` and `E ≤ 1` both stand. |
| **F-J5** | **CORRECT** | (i) `\|block_t ∩ A′\| = D_t − (p−t) − (L+1) + e_t ≥ (τ−t+2) − (p−t) − (L+1) + 1 = 2` ✓ — the arithmetic collapses exactly because `τ = p+L`. (ii) Yes, it *is* established: `x ∈ A′` survives steps `t…p` because **Lemma FAN-1** makes every head of steps `1…p` a `B_hi` vertex, so no `A′` entry is deleted in the high phase; hence `v_{p+1}(x) ≥ v_t(x) − (p−t+1)` ✓. Chain: `τ−t+1 ≤ v_t(x) ≤ 1 + (p−t+1)` ⟹ `L ≤ 1` ✓. No circularity: FAN-7's count is re-derived with escapes and uses only FAN-1 + DICH(b). |
| **F-J6** | **CORRECT** | Prop L2 does supply every `Fan` clause. (b)+(d) give `G[B] = K_τ − uv`, `u,v ∈ B_hi`, `B_lo` B-universal; (c) gives `deg_A(b_i) = 1` with a common `a₀` adjacent to all of `B`, hence `deg(b_i) = τ` and `deg(a₀) = τ`, i.e. the `C`-block; and the clause the brief singles out — "every `A`-vertex other than `a₀` attaches only inside `B_hi`" — **does** follow, precisely from `deg_A(b_i) = 1` with the unique neighbour `a₀`: for `a ∈ A∖{a₀}`, `N(a) ⊆ B` and `N(a) ∩ B_lo = ∅`, so `N(a) ⊆ B_hi`. `p ≥ 2` is automatic. The unstated side-claim `α = 1 + \|A′\|` is **true** (any independent set takes ≤ 2 vertices of `B`, and `d_u, d_v ≥ 2` kills the `{u,v}∪…` alternative) — I verified it on **1 118** constructed Fan graphs, 0 failures. |
| **F-J7** | **DEFECT (1 real + 2 minor)** | The audit is **not** clean. (a) **Theorem FAN's second sentence is a statement outside the reductio whose only proof runs inside it** — exactly the species the audit is looking for (Defect D-1 below). (b) **Lemma FAN-2** is the one FAN lemma stated with *no* reductio marker while its proof uses `D_j = g_j − (j−1)` (DICH(b)) and Lemma FAN-1, both reductio-only (Defect D-2). (c) "the hard core" is expanded three different ways inside the appendix — §7.4 C `(connected, f = α+1, diam 4)`, §7.6 B `(connected, non-forest, diam 4, f = α+1)`, §7.6 G / SL-HC / FAN-HC `(… , residue = α)` — so Prop L1 and Theorem MB are *declared* under a weaker hypothesis set than their proofs use, rescued only by the §7.6 preamble (Defect D-3). Consequently §7.9's "**No recurrence of the D1/D3 species found in §7.6 or §7.8**" is **falsified**. |

---

## Part 2 — D-DIFF table (D1 … D5), diff-scoped

| # | verdict | check |
|---|---|---|
| **D1** | **CONFIRMED — diagnosis right, repair right, nothing new** | The number of non-head entries is `n − s`, not `α`. Both witnesses reproduced with my own code: `K_{2,3}` → `deg = [3,3,2,2,2]`, heads `(3,2,1)`, `s = 3`, `α = 3`, `n − s = 2`; control `[3,3,3,3,3,2,1]` → `s = 4`, `n − s = 3`, and I *realised* it as a connected graph (`A`-side `[3,3,2,1]` to an independent `B`-side `[3,3,3]`) with `α = 4` exactly, so the second witness is a genuine graph witness, not just a sequence. Repair "`\|K\| = s`, `n − s` survivors, `= α` iff `s = τ`" is exactly right (`residue = n − s` and `τ = n − α`). F3′ and Z⁺ are unaffected: F3′ uses only "≤1 decrement per step, must reach 0", and Z⁺'s survivor/later-head split is exhaustive under the corrected reading. |
| **D2** | **CONFIRMED** | `¬(residue ≤ α−1)` gives `residue ≥ α`; `residue = α` needs Fact 2. Repair correct and minimal. |
| **D3** | **CONFIRMED** | Lemma C\*'s proof cites only Lemma 4 (`f = α+1`) and (F-b); `s = τ` appears nowhere in it. Over-hypothesisation, safe direction, real Lean hazard. Repair (a parenthetical) is correct and introduces nothing. |
| **D4** | **CONFIRMED** | `T₁,T₂ ⊆ B` disjoint, so `\|T₁ ∪ T₂\| ≤ τ` — not `O(1)`. The *bound* is the constant. Repair correct; the strategic reading (constant vs. `τ+1`) is unchanged. |
| **D5** | **CONFIRMED — and the corollary it adds is correct** | `C(τ,2) − (τ−2) = (τ²−3τ+4)/2`, discriminant `−7`, so positive for every `τ`; I recomputed `τ = 1…9` → `1,1,2,4,7,11,16,22,29`, matching the repair exactly. "Incompatible for every `τ ≥ 1`" ✓. The added corollary — N(iii)/N′(iii′) are redundant given Theorem K + Fact 2 — is **correct** and **non-circular**: Theorem K's proof uses Lemma S + DICH(b) + `hs = Σ_B deg − m = e_B`, never Theorem N. The N2 "等价 → 逆否 + Fact 2" fix is right (the literal contrapositive yields only `residue ≠ α`). |

**Does any repair create a NEW inconsistency elsewhere?** **No.** D1's redefinition of "survivor" is used nowhere as a *count*: Lemma S's `#{deg ≥ τ+1} ≤ τ`, Lemma H's `τ−j−1` later heads, Theorem N's `K = B` and Lemma HI's `\|I_lo\| = L` all draw on `\|K\| = s = τ` under the standing reductio, not on the survivor count. D5's new forward reference (§7.2 B Theorem N → §7.5 Theorem K) is acyclic. *One sibling the pass does not fix (noted, not scored, K-chain-adjacent so out of my scope):* Lemma T's second sentence ("若第 τ−1 步后有两个条目 ≥2，则 residue ≤ α−1") has exactly the D2 shape — it needs Fact 2 to get from `s ≠ τ` to `residue ≤ α−1`.

---

## Defects

### D-1 (real, in a statement marked PROVED). Theorem FAN's second sentence is unproved, and the sentence justifying it is an invalid inference.

**Quoted line (§7.8 F, Theorem FAN):**

> "For every `τ` and every `L ≥ 2` there is **no** graph with the `Fan(τ,L)` configuration
> satisfying `residue(G) = α(G)`. **Equivalently, every `Fan(τ,L≥2)` graph has
> `residue = α − 1`, its Havel–Hakimi process taking exactly `τ + 1` steps.**"

and, in the proof:

> "So the list at the start of step `p+1` is `[L]^{L+1}, 1, 1` (plus zeros), and Lemma FAN-3
> gives `s = τ + 1`, a contradiction. **The last sentence is Lemma FAN-3's second half.**"

**Why it fails.** Two errors, one on top of the other.

1. **"Equivalently" is false.** `residue ≠ α` plus Fact 2 gives only `residue ≤ α − 1`,
   i.e. `s ≥ τ + 1`. Nothing in the appendix bounds `s` from above, so
   `residue = α − 1` / `s = τ + 1` is **strictly stronger** than the first sentence, not
   equivalent to it.
2. **The justification is ex falso.** Every ingredient of "the list at the start of step
   `p+1` is `[L]^{L+1},1,1`" was derived *under* `s = τ`, the hypothesis the proof then
   refutes. It cannot be re-used after the contradiction. And the machinery genuinely
   collapses at `s = τ+1`: Lemma S then reads "survivors have degree `≤ s = τ+1`", so a
   `B_hi` vertex of degree exactly `τ+1` need **not** be a head; and DICH(b) demands
   `g ≥ s+1 = τ+2`, so such a vertex falls under DICH(c) only, and FAN-1's
   `D_j ≥ τ−j+2` — the load-bearing inequality of the whole chain — is no longer derivable.

**Smallest configuration exposing it.** `Fan(4,2)` with `A′` neighbourhoods `{u},{v},{u,v}`:
`n = 8`, `deg = [5,5,4,4,4,2,1,1]`, `α = 4`, `τ = 4`, `diam = 4`, `f = α+1 = 5` — a genuine
hard-core-shaped instance. Its true run has `s = 5 = τ+1`, so `residue = 3 = α−1` (the
conclusion happens to be true). But **every `B_hi` degree here is exactly `τ+1 = 5 < s+1 = 6`**,
so at the true `s` neither Lemma S nor DICH(b) fires on `B_hi` at all. The claim is therefore
about a regime in which the proof's own tools are unavailable — the tightest possible witness
that the inference is not licensed.

**Repairable?** **Yes, cheaply** — delete the "Equivalently … exactly `τ + 1` steps" clause,
or restate it as a measured observation (it *is* measured: `s = τ+1` in all 3 277 800 of my
labelled runs). Nothing downstream uses it: Corollary FAN-HC, the `L ≥ 3` residual and §7.8 G
all consume only the first sentence. The "Numerical agreement" paragraph should then read
"consistent with", not "Theorem FAN predicts".

**Does the CONCLUSION survive?** **Yes.** Theorem FAN's first sentence and Corollary FAN-HC
(hard core has `L ≥ 3`) are unaffected.

### D-2 (minor, scope). Lemma FAN-2 is declared without the reductio and proved only inside it.

> "**Lemma FAN-2 (no escape, partial).** For `j ≤ min(p, L+1)`, `block_j ⊇ C`."

No hypothesis marker, yet the proof's `D_j = g_j − (j−1) ≥ τ−j+2` is DICH(b) plus Lemma FAN-1,
both reductio-only. Every other FAN lemma carries "under the reductio" and FAN-3 is correctly
flagged hypothesis-free; FAN-2 is the omission. Harmless (superseded by FAN-8 and explicitly
"no longer used"), but it is a live instance of the D1/D3 species inside §7.8 and it is what
§7.9's scope-audit paragraph missed. Repairable: add the marker or delete the lemma.
Conclusion unaffected. (Its *conclusion* is empirically true off the reductio too: `E = 0` in
all 3 277 800 runs.)

### D-3 (minor, scope). "The hard core" is expanded three inequivalent ways.

§7.4 C: "*Assume the hard core (G connected, `f = α+1`, diam = 4)*"; §7.6 B: "*Hard-core
standing assumptions (G connected, non-forest, diam 4, `f = α+1`)*"; §7.6 G / Cor SL-HC /
Cor FAN-HC: "*(connected, non-forest, `diam = 4`, `f = α+1`, `residue = α`)*"; §7.1: with
`residue = α` **and** `τ ≥ 3`. Proposition L1 and Theorem MB are stated "in the hard core"
under the second reading but proved from (LOW3)/Theorem SL, which need `residue = α`; only the
§7.6 preamble rescues them. Repairable: fix one expansion and use it. Conclusion unaffected.

### D-4 (minor, wording). FAN-6's parenthetical misdiagnoses why the induction stops at `1+1`.

> "*(The same induction does **not** apply to `1+1`: there `v = 1` and `v−1 = 0` is present as
> the zero entries, so the "maximum does not drop" case is open …)*"

The clause that actually fails first is **uniqueness of the maximum**: `M_{p+1} = [1,1,…]` has
`max = 1` with multiplicity 2. Computed: `\|A′\| = 2` → `M_{p+1} = [1,1]`, unique = **False**,
and `v−1 = 0` is **not** present at all — so the stated reason is simply wrong in that
sub-case. Exposition only; FAN-6 needs to kill only the single-`2` case. Repairable in one
clause. Conclusion unaffected.

### D-5 (minor, over-strong claim in §7.9). The scope-audit sentence is falsified by D-1/D-2/D-3.

> "**No recurrence of the D1/D3 species found in §7.6 or §7.8.** This audit is the owner's and
> has not itself been S3'd."

Three recurrences above. The honest caveat in the same sentence is what saves it; the sentence
itself should be weakened. Conclusion unaffected.

**Slack test.** The one counting step the text needs *tight* is FAN-8's
`\|block_t ∩ A′\| ≥ 2` — and it is exactly tight (`= 2`), by design, since the `τ = p+L`
cancellation is exact. No slack-≥-2-where-tightness-is-needed step found. Conversely FAN-7's
`E ≤ 2` is slack by one relative to the `E ≤ 1` actually used; that is honest (`E = 2` is
killed separately and correctly).

---

## Control cases / counterfactual availability (T12) — REQUIRED section

Four controls, all built and measured by me. "Fires" = hypotheses genuinely hold **and** the
lemma yields something at that instance.

**Control (a) — `Fan(4,2)`, hard-core shape.** `A′`-neighbourhoods `{u},{v},{u,v}`; `n = 8`,
`deg = [5,5,4,4,4,2,1,1]`, `α = 4`, `τ = 4`, `diam = 4`, `f = 5 = α+1`, non-forest, connected,
Lemma 4 satisfied at **every** `B`-pair (checked). Measured `residue = 3 = α−1`, `s = 5`.

* **Fact 2** — holds, gives `residue ≤ 4`; fires, non-binding.
* **Lemma 1(1)(2)** — holds; `residue = n − s = 8 − 5 = 3` ✓, `Σ D_i = 5+4+2+1+1 = 13 = m` ✓.
* **Lemma S** — hypotheses **fail as the text uses them**: `s = 5 ≠ τ = 4`, so the §7.2 B form
  ("survivors have degree `≤ τ`") is unavailable; the general form gives only `≤ s = 5`, which
  does **not** force `B_hi` to be heads. *This is the D1/R2 species alive inside §7.8.*
* **Lemma DICH(b)** — **unavailable**: needs `g ≥ s+1 = 6`, and `max deg = 5`. So on the very
  configuration the chain is about, DICH(b) fires **zero times** in the true run.
* **Lemma DICH(c)** — available (`g ≤ s` for all heads); yields `D_i ≤ s−i+2`, satisfied with
  slack at every position.
* **Theorem K / Corollary K1 / Theorem N / N′ / Corollary N1 / N2** — **all unavailable**:
  hypothesis (i) "every `b ∈ B` has `deg(b) ≥ τ+1`" fails (`deg(b_lo) = τ = 4`).
* **Theorem LOW / Theorem SL / Theorem MB / Prop L2 / Theorem FAN** — all are reductio
  statements and the reductio is **false** here, so all are vacuously satisfied; none of them
  can be *tested* on (a). Only Theorem FAN's first sentence has content, and it is confirmed:
  no `residue = α`.
* **Lemma C\*** — available (hard core, no reductio needed — this is exactly D3's point) and
  it fires: `deg_A(u) = deg_A(v) = 3 ≥ 3` ✓.

**Control (b) — `Fan(4,2) + uv`, i.e. `B = K_4`: exactly one Fan hypothesis broken.**
`n = 8`, `deg = [6,6,4,4,4,2,1,1]`, `α = 4`, `τ = 4`, `diam = 3`, `f = 5 = α+1`.
Measured **`residue = 4 = α`, `s = 4 = τ`: the reductio HOLDS here.** This is the
discriminating control — the residue test is **not** vacuously negative, and I reproduce the
draft's own claim (its "36 650 of 46 138 `B`-clique cases") independently.
* **Observation R1** — hypothesis `diam = 4` **fails** (`diam = 3`), consistently with `B`
  being a clique. R1 does not fire.
* **Theorem LOW (LOW1)** — available and fires: `Σ_{B_lo} deg + ν = 8 + 0 = 8 ≤ L(τ+1) = 10`.
* **Theorem SL** — available and fires: `slack = 2 ≥ 1` ✓.
* **Lemma HI** — fires: `B_hi = {u,v}`, `p = 2`, and the labelled run's head positions split
  `I_hi = {1,2}`, `I_lo = {3,4}`, `\|I_lo\| = 2 = L` ✓.
* **Theorem K / K1** — **unavailable** (hypothesis (i) fails: `deg(b_lo) = 4 = τ`), even
  though its *conclusion* (`B` a clique) is true here. A clean example of a conclusion holding
  where the theorem cannot be invoked.
* **Theorem FAN** — unavailable: `G[B] = K_τ`, not `K_τ − uv`, so this is not a `Fan`.

**Control (c) — `Fan(4,2)` with `b_lo₁` given a second `A′`-neighbour.** `n = 9`,
`deg = [5,5,5,4,4,2,1,1,1]`, `α = 5`, `τ = 4`, `diam = 4`, `f = 7 = α+2`. `deg(b_lo₁)` rises to
`τ+1`, so `L` drops from 2 to 1 and the instance leaves the `Fan(τ,2)` family entirely.
Measured `residue = 4 = α−1`, `s = 5`, consistent with Corollary L1-short — but **Corollary
L1-short is itself unavailable** here, since `f = α+2 ≠ α+1` puts the graph outside the hard
core, so Lemma 4, Lemma C\*, Theorem MB and Prop L2 all have failing hypotheses.

**Control (d) — `K_{2,3}`.** `deg = [3,3,2,2,2]`, `α = 3`, `τ = 2`, `s = 3`, `residue = 2`.
The standing off-reductio witness: `s ≠ τ`, so **Lemma S, Lemma F3, Lemma T, Lemma H,
Corollary N2 (pre-repair), Theorem N** are all unavailable, while **Lemma F3′, Lemma Z⁺ and
Lemma DICH** are available (general `s`) and hold. This reproduces the R2/D1 finding from
scratch.

### Named: lemmas the text claims are available but which never actually execute

1. **Lemma DICH(c), at its call site inside Lemma FAN-1.** FAN-1's proof reserves a branch for
   "*A low head at `j` has `D_j ≤ τ − j + 2` by DICH(c); equality is a tie with the remaining
   high vertex, and the fixed tie-break takes the high vertex*". Its hypotheses genuinely hold
   (any low head has `g ≤ τ = s`), and it would yield `D_j ≤ τ−j+2`. **But it never fires.**
   Measured over **18 831** labelled runs (canonical + `preferC` + `preferA′` adversarial
   policies) on 6 277 Fan graphs: the number of runs in which any non-`B_hi` entry so much as
   **ties** the maximum at a high-phase step is **0**. The maximum is always *strictly* a
   `B_hi` vertex, so FAN-1's tie-break machinery — the joint the brief flags as the most
   delicate — protects against a case that does not occur in the family it is applied to.
2. **Lemma Z (§7.4, the `β_j = 0` version).** Its hypothesis holds at **0 of 18 831** runs at
   any high-phase step `j ≤ p` (during the high phase every block contains the `p−j` remaining
   `B_hi` heads plus, at `j = p`, the `L` later `C`-heads, so `β_j ≥ 1` always). It holds only
   at the trivially-final step. Lemma Z, Lemma DEC and Corollary CNT contribute nothing to the
   FAN chain; the chain runs on Z⁺/DICH.
3. **Lemma FAN-2** — the text itself says it is "superseded … and no longer used"; it is still
   carried in the PROVED status list. `E = 0` in all runs, so its conclusion is subsumed.
4. **Lemma FAN-7's `E = 2` clause and the `E = 1` row of the §7.8 E case table** — never
   execute: `E = 0` in **3 277 800 of 3 277 800** labelled runs across 8 tie-break policies.
   The case list is complete and correct, but three of its four rows are counterfactual.
5. **Theorem K, Corollary K1, Theorem N, Theorem N′, Corollary N1** — the "Chain of
   dependence" line lists Theorem K under Corollary FAN-HC. It *is* used, but only for the
   `L = 0` branch; on the `L = 2` branch (the one Theorem FAN exists to close) their common
   hypothesis (i) fails by construction, since `Fan` puts `B_lo` at degree exactly `τ`.

---

## Trajectories (own implementation, all intermediate lists)

Calibration first: `residue(K₂) = 1`; `residue(Cₙ) = ⌈n/3⌉`, `n = 3…9`, exact.

**T1 — `Fan(4,2)`, hard-core shape (`L = 2`).** `τ = 4`, `p = 2`, `α = 4`, `n = 8`,
`diam = 4`, `f = α+1`, `residue = 3 = α−1`, `s = 5 = τ+1`.
```
step 1 [5,5,4,4,4,2,1,1]  head u(5)   block={v,b1,b2,a0,a3}
step 2 [4,3,3,3,1,1,1]    head v(4)   block={b1,b2,a0,a1}
step 3 [2,2,2,1,1,0]      head b1(2)  block={b2,a0}      <- C-part [2,2,2]=[L]^{L+1}, A'=(1,1,0)
step 4 [1,1,1,1,0]        head b2(1)  block={a0}
step 5 [1,1,0,0]          head a1(1)  block={a3}
final  [0,0,0]            -> residueAux returns 3
```

**T2 — `Fan(6,2)` (`L = 2`).** `τ = 6`, `p = 4`, `α = 7`, `n = 13`, `diam = 4`,
`residue = 6 = α−1`, `s = 7 = τ+1`.
```
step 1 [7,7,7,7,6,6,6,1,1,1,1,1,1]  head w1(7)  block={w2,w3,w4,b1,b2,a0,A'}
step 2 [6,6,6,5,5,5,1,1,1,1,1,0]    head w2(6)
step 3 [5,5,4,4,4,1,1,1,1,0,0]      head w3(5)
step 4 [4,3,3,3,1,1,1,0,0,0]        head w4(4)
step 5 [2,2,2,1,1,0,0,0,0]          head b1(2)   <- C-part [2,2,2], A'-residue (1,1,0,0,0,0)
step 6 [1,1,1,1,0,0,0,0]            head b2(1)
step 7 [1,1,0,0,0,0,0]              head a(1)
final  [0,0,0,0,0,0]                -> residue 6
```

**T3 — `Fan(7,3)` (`L = 3`).** `τ = 7`, `p = 4`, `α = 8`, `n = 15`, `diam = 4`,
`residue = 7 = α−1`, `s = 8 = τ+1`.
```
step 1 [9,9,8,8,7,7,7,7,2,1,1,1,1,1,1]
step 2 [8,7,7,6,6,6,6,1,1,1,1,1,1,0]
step 3 [6,6,5,5,5,5,1,1,1,1,0,0,0]
step 4 [5,4,4,4,4,1,1,1,0,0,0,0]
step 5 [3,3,3,3,1,1,0,0,0,0,0]   <- C-part [3,3,3,3]=[L]^{L+1}, A'-residue (1,1,0,0,0,0,0)
step 6 [2,2,2,1,1,0,0,0,0,0]
step 7 [1,1,1,1,0,0,0,0,0]
step 8 [1,1,0,0,0,0,0,0]
final  [0,0,0,0,0,0,0]           -> residue 7
```

**T4 — control `Fan(4,2)+uv` (`B = K_4`).** `τ = 4`, `α = 4`, `n = 8`, `diam = 3`,
`f = α+1`, **`residue = 4 = α`, `s = 4 = τ`** — the reductio holds.
```
step 1 [6,6,4,4,4,2,1,1]  head u(6)
step 2 [5,3,3,3,1,1,0]    head v(5)
step 3 [2,2,2,0,0,0]      head b1(2)
step 4 [1,1,0,0,0]        head b2(1)
final  [0,0,0,0]          -> residue 4 = alpha
```

**T5 — control `K_{2,3}`.** `α = 3`, `τ = 2`, `s = 3 ≠ τ`, `residue = 2 = α−1`.
`[3,3,2,2,2] → [2,2,1,1] → [1,1,0] → [0,0]`, heads `(3,2,1)`.

**T6 — control `[3,3,3,3,3,2,1]` (D1's second witness, realised as a graph).** `n = 7`,
`α = 4`, `τ = 3`, `s = 4`, `n − s = 3 ≠ α`, `residue = 3`, `diam = 4`, `f = 5 = α+1`.
`[3,3,3,3,3,2,1] → [3,2,2,2,2,1] → [2,1,1,1,1] → [1,1,0,0] → [0,0,0]`.

### Refutation search (the single most valuable outcome — **not found**)

| box | Fan(τ,L≥2) instances | runs | `residue = α` survivors |
|---|---|---|---|
| strict (Gale–Ryser realisable), `τ ≤ 9`, `R ≤ 16..18`, `\|A′\| ≤ 12` | **409 725** | **3 277 800** labelled (8 tie-break policies: canonical, prefer-`B_hi`, prefer-`C`, prefer-`A′`, 4 random) | **0** |
| superset, realisability **dropped**, `τ ≤ 8`, `R ≤ 14`, `\|A′\| ≤ 10` | 48 016 | — | **0** |
| built as actual graphs, `τ ≤ 7` | 6 277 | 43 939 | **0** (`α = 1+\|A′\|` verified) |
| `Fan(4,2)` with `diam = 4` **and** `f = α+1` (true hard-core shape) | 10 | — | **0**, all `α − residue = 1` |

Per-run structural measurements over the 3 277 800 runs: `M1` (heads `1..p` are exactly
`B_hi`) fails **0**; `E > 0` **0**; `A′` sum at step `p+1` `≠ 2` **0**; `A′` residue
`≠ (1,1)` **0**; `a_j ≠ g_j − τ` **0**; "a maximum `A′` entry is decremented" fails **0**;
`C`-part `≠ [L]^{L+1}` **0**; `s ≠ τ+1` **0**.

One divergence from the draft's numbers, benign: in my *unrestricted* superset (realisability
dropped entirely) `α − residue` takes the values `{1: 42128, 2: 5643, 3: 245}`, not `{1: …}`
alone. Every instance with `α − residue ≥ 2` is **non**-Gale–Ryser-realisable, i.e. not a
graph; among the 409 725 realisable ones the value is `1` without exception. So the draft's
"`1 700 094 of 1 700 094` superset" figure is consistent provided its "superset" still imposes
realisability — worth stating explicitly in the text, since "superset" is defined there only
as "dropping the occurring-type requirement".

Also verified directly: **Observation FAN-5** (`[L]^{L+1},1,1` clears in `L+1`, `[L]^{L+1},2`
clears in `L`) for `L = 2…9`; the **complete §7.8 E case table** for `L = 2…9` including the
`E = 1` row clearing in exactly `L` (so FAN-8 really is load-bearing); and the
**non-graphicality of both `E = 2` shapes** for `L = 2…6`.

---

## What I could NOT check

* **(F-b), "occurring type", "witness `a₁`"** are never defined in the appendix, and the fact
  that (F-b) *holds* in the hard core is nowhere proved here. Lemma C\*, Theorem MB and
  Proposition L2 all rest on it, so F-J6's rigidity step is verified only modulo (F-b). I
  reconstructed the intended reading (`T_i = N_B(a_i)` for some `a_i ∈ A`) and C\*'s proof is
  valid under it, but that is my reconstruction, not the text's.
* **Theorem T3** (`τ ≤ 3` fully solved), **Theorem C**, **Corollary B1**, **Theorem A/B2** —
  not in the appendix; Corollary FAN-HC's "`τ ≥ 4`" is taken on trust.
* **Fact 2** (Favaron–Mahéo–Saclé) — cited, not proved; the draft itself flags the
  bibliographic data as from memory.
* **§7.3 5bis / T3 / the R1,R2,R3 repairs** and the **K-chain (Z⁺/DICH/Theorem K/K1)** — out
  of scope per the brief; I re-derived only DICH(b)/(c)'s *use* at the FAN call sites, not the
  lemmas themselves.
* **Every `.py`/`.out` cited in the draft** — I was forbidden to open them and did not. All
  numbers above are my own, from my own implementation.
* **`w61_S3_KCHAIN_opusB.md`'s "5 842 009 trajectories"** and the gate-counting in §7.9's last
  section: procedural, not mathematical; not assessed.
