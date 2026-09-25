CLEAN: every step of the K-chain (Z⁺ → DICH → Theorem K → Corollary K1) is valid as written and tie-safe, Repair R2's Lemma F3′ is correctly stated, correctly proved and does repair every use; the only defects I found are four sub-gap wording/scope items, the sharpest being that R2 generalised the *lemma* to arbitrary `s` but left the *definition* of its subject term "生存者/survivor" (§7.2 B: "其余 **α** 个条目") tied to `s = τ`.

TEXT VERSION REVIEWED: prompts/w61_S3_R2A2.md (post-R1/R2 repairs, draft appendix section G = §7.7)

TARGET = K-CHAIN (appendix sections A, B, C, D, F, G; section E ignored entirely).
Round-B independent opus judge. I read only the brief file. All numbers below are from my
own throwaway implementation of `residueAux` (labelled Havel–Hakimi, `List.splitAt`
truncation, ℕ-truncated `(·−1)`), written from the spec in appendix §1 alone; no author
script, output or other judge's verdict was consulted.

---

## (1) Per-joint verdicts

| joint | verdict | one line |
|---|---|---|
| **K-J1** Lemma Z⁺ + Repair R2 / F3′ | **OK** | The prefix step is tie-safe for the right reason (`x ∉ block ⟹ v ≤ min(block)` holds under *every* tie-break); the counting branch `D_j + 1 ≤ s − j ⟹ D_j ≤ s−j−1` is correct; F3′ is true, correctly proved (truncation cannot break it) and its substitution repairs the *only* place Z⁺ reached outside scope. Defect **D1** (below) is residual, one clause. |
| **K-J2** Lemma DICH (a)(b)(c) | **OK** | (a)'s arithmetic `v > s−j+1 ⟹ v−1 > s−(j+1)+1` is right; (b)'s induction gives `h_i = i−1`, `D_i = g−(i−1)` **exactly** (no truncation, since an excess entry has value ≥ 2); (c) is genuinely unconditional — `i = 1` is covered by the parenthetical `D_1 = g ≤ s ≤ s+1`, and `j₀ = i` falls under case 1 ("never excess *before deletion*") giving the *same* bound `s−i+2`. Boundary `g = s` vs `g = s+1` agree: both yield `D_i ≤ s−i+2`, so (b)/(c) join without a seam. |
| **K-J3** Theorem K | **OK** | `\|K\| = s` (each step deletes one distinct vertex), `B ⊆ K` by Lemma S + (i), `\|B\| = τ = s` ⟹ `K = B`; `hs = Σ_{b∈B}deg b − m = e_B` needs only A independent; `Σ_{i=1}^{τ}(i−1) = τ(τ−1)/2 = C(τ,2)` ✓. Uncited but true: the identity `Σ h_i = Σ_{v∈K}deg v − m` rests on Lemma 1(2) and on no-truncation. |
| **K-J4** Corollary K1 | **OK** | Observation R1's proof needs only *maximal* independence + connectivity, so it holds for **every** maximum independent set; the existential "**some** maximum independent set A" is therefore sound and is the strongest correct form. `τ = n−α` does **not** depend on the choice of A; `B`, `e_B`, `min_B deg` **do** (control (c) has 4 maximum independent sets with `e_B ∈ {0,1,1,2}`), and the proof never mixes two choices. Defect **D2**: "Otherwise residue = α" silently uses Fact 2. |
| **K-J5** toolkit sweep | **OK** | The K-chain needs exactly: Lemma 1(1)(2), Fact 2, **F3′**, Lemma S, Observation R1, §7.4 A's `hs` identity. It does **not** need T, H, BO, Z, DEC, CNT, N, N′, N1, N2, C\*. After R2 I find **no remaining under-hypothesised citation**. The one residual scope error runs the *safe* way (over-hypothesisation): **Lemma C\*** is stated inside §7.4, whose standing hypothesis is `residue = α`, but its proof never uses it, and §7.4 E/D then applies it to 340 hard-core graphs that are *not* filtered by `residue = α`. Defects **D3**, **D4**. |
| **K-J6** patched Corollary N2 | **OK** | Patched statement, its derivation via Lemma S → `hs = e_B = 0` → all `h_i = 0` → Lemma H (`h_i = 0 ≤ i−2` for `i ≥ 2`) → `m ≤ Δ + Σ_{t=2}^{τ} t = Δ + τ(τ+1)/2 − 1`, all correct; I re-derived Lemma H itself line by line and it is sound and tie-safe. `K_{2,3}` arithmetic reproduced **exactly** (α=3, τ=2, e_B=0, B-degrees 3=τ+1, Δ=3, m=6 > 5, HH heads (3,2,1), s=3≠τ, residue=2=α−1). I also found a **second, independent counterexample** to the unqualified form: control (b). Defect **D5** (the word "等价"). |

**Verdict on the CONCLUSION:** Theorem K, Corollary K1 and the patched Corollary N2 all
survive intact. None of D1–D5 touches any conclusion; each is a one-clause repair.

---

## (2) Defects found (all sub-gap; quoted line, why, smallest configuration, repair)

I found **no** false statement and **no** inference that could fail. What follows is the
complete list of what I would send back to the author, ordered by severity.

### D1 — [K-J1 / K-J5] Repair R2 generalises the lemma but not its subject term

> "**Lemma F3′ (survivor decay, general `s` — no reductio).** … At the start of step `j`
> (`1 ≤ j ≤ s`) every **survivor** has value `≤ s − j + 1`."

and the term it quantifies over, imported verbatim by §7.5 ("Standing conventions of §7.2 B / §7.4"):

> "s = 步数，D_1≥…≥D_s 为各步头值（Lemma 1(2)），K = 头集合，**其余 α 个条目称生存者**"

**Why it fails as written.** §7.2 B defines a survivor as one of "the other **α** entries".
The number of non-head entries is `n − s`, which equals `α` **only when `s = τ`** — i.e.
exactly the hypothesis R2 was removing. So in the general-`s` regime that R2 buys, the
term "survivor" is defined by a count that is wrong. This is the *same species* of scope
slip as the R2 defect itself (a general-`s` object defined by an `s = τ` quantity), sitting
one line away from the repair, and R2's own wrap-up sentence — "with that substitution
both are proved in exactly the generality in which they are stated, and **nothing else in
§7.5 changes**" — asserts that nothing else needs touching.

**Smallest configuration exposing it.** Control (d) `K_{2,3}`: `α = 3`, `τ = 2`, `s = 3`,
`n − s = 2`. F3′ at `j = 2` is a statement about the **2** non-head entries, not about "the
α = 3 entries"; there is no set of 3 survivors to quantify over. (Control (a) is worse:
`α = 4`, `n − s = 3`.)

**Consequence.** None mathematically: F3′'s own proof fixes the intended reading
("A survivor is decremented at most once per step"), and Z⁺'s dichotomy
survivor/later-head is exhaustive under that reading. Purely a definitional defect.

**Repairable, how.** Add to R2: "*throughout, **survivor** := an entry never deleted as a
head; there are `n − s` of them, which is `α` exactly when `s = τ`.*" One clause.

### D2 — [K-J4] Corollary K1's reductio standpoint does not cite Fact 2

> "*Proof.* Otherwise residue = α and Theorem K makes B a clique, contradicting
> Observation R1 (§7.1: diam = 4 ⟹ B is not a clique). ∎"

"Otherwise" negates `residue ≤ α − 1`, which gives `residue ≥ α`; upgrading that to
`residue = α` needs `residue ≤ α`, i.e. **Fact 2**, which is nowhere named in §7.5.

**Why I do NOT score this a gap** (and where a stricter referee would): §7.5 opens
"Standing conventions of §7.2 B / §7.4", and §7.2 B's convention block explicitly contains
"由 Lemma 1(1) residue=n−s，由 **Fact 2** 有 s ≥ τ". The needed fact is therefore imported
by the sentence that sets the section's conventions, which makes this *terse-but-correct*
rather than unjustified. I record it because it is the **same shape** as the round-A gap
T-c (an uncited standpoint premise) that §7.7 upheld — the difference being that T-c's
missing Lemma 3 lived in §4.1 and was imported by nothing. **Repair:** "Otherwise, by
Fact 2, residue = α".

### D3 — [K-J5] Lemma C\* is declared inside a reductio it never uses, and is then used outside it

§7.4's preamble:

> "Throughout §7.4 we work under the reductio hypothesis **residue(G) = α(G)**, i.e. s = τ."

but Lemma C\*, stated inside §7.4 C, hypothesises only the hard core:

> "**Lemma C\* (τ-uniform).** Assume the hard core (G connected, f = α+1, diam = 4). …"

and its proof uses only Lemma 4 and (F-b) — never `s = τ`. §7.4 D then tests it on
"hard-core graphs=340" with **no** `residue = α` filter, and §7.4 E reasons from it about
all 118 τ=4 hard-core cases.

**Why this is the *safe* direction.** The declared scope is *narrower* than the proof
needs, so every use inside §7.4 is licensed and every use outside is licensed by the proof
though not by the declaration. It is the mirror image of the R2 defect and cannot produce
a false conclusion — but a formalisation pass that transcribes the declared hypotheses
will carry a spurious `residue = α` into C\* and then fail to discharge it at the C\* use
sites in §7.4 D/E. **Repair:** move C\* out of the §7.4 reductio scope, or add "*(C\*'s
proof does not use the reductio)*".

Verified on the controls: C\* is available and tight on control (a) — `T₁ = {y,z}`,
`T₂ = {x}` (disjoint, `e_B = 0` so no `G[B]`-edge between them), and
`deg_A(x) = deg_A(y) = deg_A(z) = 3`, i.e. exactly the bound — while `residue = α−1` there,
so the declared `residue = α` is false at that very instance.

### D4 — [K-J5, minor] "the O(1) vertices of `T₁ ∪ T₂`" is wrong

> "(F-b) plus Lemma 4 only ever force `deg_A(b) ≥ 3` for the **O(1) vertices** of `T₁ ∪ T₂`"

`T₁` and `T₂` are *types*, i.e. subsets of `B`; they are disjoint, so `|T₁ ∪ T₂| ≤ τ` and
can equal `τ` (take `T₁ = {b₁,b₂,b₃}`, `T₂ = {b₄,b₅,b₆}` at τ = 6). The correct statement
is that the *bound* is the constant 3, not that the *set* is O(1). The strategic
conclusion ("bounds that do not grow with τ, while (i) demands τ+1") is unaffected.

### D5 — [K-J3 / K-J6, minor] two overstated equivalences

* > "(ii) says e_B ≤ τ−2 while Theorem K says the only consistent value is C(τ,2) — the two are **incompatible for τ ≥ 3**"

  `C(τ,2) − (τ−2) = (τ²−3τ+4)/2 > 0` for **all** τ (discriminant 9−16 < 0); I checked
  τ = 1…7 explicitly. So they are incompatible for every τ ≥ 1, and consequently
  **Theorem N's (iii) and Theorem N′'s (iii′) are outright redundant** given Theorem K +
  Fact 2 — a strengthening the text stops one inch short of stating.

* > "等价的可用形式（逆否，反证站位显式化）：**若 (i) 成立、e_B=0 且 m > Δ(G) + τ(τ+1)/2 − 1，则 residue(G) ≤ α(G) − 1。**"

  The literal contrapositive concludes `residue ≠ α`; getting `residue ≤ α−1` needs
  Fact 2 on top. "等价" should read "逆否 + Fact 2".

### Non-defects I checked and am supplying justification for rather than scoring (per the brief)

* Z⁺'s `min(block)` presupposes `block ≠ ∅`; true because `residueAux` returns on head 0,
  so every executed step has `D_j ≥ 1`. Unstated.
* §7.4 A's `hs := Σ_i h_i = Σ_{v∈K} deg(v) − m` cites nothing; it is `Σ_i(g_i − D_i)` with
  `Σ D_i = m` (Lemma 1(2)) and no truncation (Lemma 1(2)'s proof). Correct.
* DICH(b)'s "hence at every step 1…i−1" is a one-line induction on (a). Correct.
* Corollary N2's "则所有 h_i=0" silently reuses Theorem N's `K = B ⟹ hs = e_B` step. Correct.
* "DICH **subsumes Lemma H**": verified. If `h_i ≤ i−2` then `g ≤ s` (a head with `g ≥ s+1`
  has `h_i = i−1`), so DICH(c) gives `D_i ≤ s−i+2 ≤ τ−i+2+h_i`. True, and strictly stronger.

---

## (3) Control cases — counterfactual availability check

For each control I ran my own trajectory (§4) and then, for **every** lemma of sections
A/B/C/D/F/G, decided whether its hypotheses actually hold *there* and what it would yield
if applied. "Available" below means hypotheses genuinely satisfied on that instance, not
"the text applies it".

All four control facts asserted in the brief were **independently reproduced by my code**:
(a) `[3,3,3,3,3,2,1]` head values `(3,3,2)`, n=7, m=9, `ΣD_{i≤3} = 8 = m−1`;
(b) diam 4, α 6, f 7 (so `f ≥ α + ⌈d/3⌉ = 8` is false);
(c) diam 4, α 5, residue 5 (so `α+1 ≥ residue + ⌈d/3⌉` is false);
(d) `K_{2,3}` refutes the unqualified N2.

### Control (a) — `d(G) = [3,3,3,3,3,2,1]`, the τ=3 k=0 graph
`n=7, m=9, Δ=3, α=4, τ=3, diam=4, f=5=α+1` (**in the hard core**), `residue=3=α−1, s=4`.
Heads (vertex order) `[x,u₂,w,u₁]`, `D=(3,3,2,1)`, `h=(0,0,0,2)`, `K={x,u₁,u₂,w}`.
B = {x,y,z}, `e_B=0`, `min_B deg = 3 < τ+1 = 4`.

| lemma | available here? | what it actually yields |
|---|---|---|
| Lemma 1(1),(2) | yes | `residue = 7−4 = 3` ✓, `ΣD = 9 = m` ✓, `D₁ = 3 = Δ` ✓ |
| Fact 2 | yes | `3 ≤ 4` ✓ |
| **Lemma F3′** | **yes** (general `s`) | per step (j, bound `s−j+1`, max survivor value) = (1,4,3),(2,3,2),(3,2,1),(4,1,1) — holds with slack |
| Lemma F3 (as stated) | **NO** | `s=4 ≠ τ=3`: the §7.2 B standing hypothesis fails **at the control**. This is precisely the R2 situation |
| Lemma S | **NO** | needs `s=τ`. (Counterfactually it would say survivor degrees ≤ 3 — true but vacuous, since Δ=3) |
| Lemma T | yes (an iff about `s=τ`) | list after step τ−1=2 is `[2,1,1,1,1]`; terminal shape would be `[2,1,1,0,0]`; no match ⟹ correctly **predicts `s ≠ τ`** |
| **Lemma Z⁺** | **yes** — but **NEVER EXECUTES** | no later head is ever excess (max value 3 ≤ `s−j+1` at every j). **This is the lemma the text claims is available and which fires zero times on the control.** |
| Lemma DICH(a) | yes | vacuous (no excess entry) |
| Lemma DICH(b) | **yes — never executes** | needs a head of original degree ≥ `s+1 = 5`; Δ=3 |
| Lemma DICH(c) | yes, fires 4× | (i,g,D_i,bound `s−i+2`) = (1,3,3,5),(2,3,3,4),(3,2,2,3),(4,3,1,2) — all satisfied |
| Lemma BO / Z / DEC / CNT | **NO** | all four are stated under §7.4's standing `residue = α`, false here (`s=4, τ=3`) |
| Theorem N / N′ / N1 | **NO** | (i) fails: `min_B deg = 3 < 4` |
| Corollary N2, patched | **NO** | both `residue=α` and (i) fail |
| N2 contrapositive form | **NO** | (i) fails — *note* `m = 9 > Δ+τ(τ+1)/2−1 = 8`, so a reader who forgot (i) would apply it and get `residue ≤ α−1`, which is **true here by accident** |
| N2 unqualified (refuted form) | (i) fails, so it does not even fire here | — |
| **Theorem K** | **NO** | `residue ≠ α` **and** (i) fails |
| **Corollary K1** | **NO** | diam = 4 ✓ but (i) fails |
| Observation R1 | yes | B is not a clique: `e_B = 0 < 3 = C(3,2)` ✓ |
| Lemma 4 / Lemma C\* | yes (hard core: f=α+1, diam=4) | `T₁={y,z}, T₂={x}` ⟹ `deg_A(b) ≥ 3` for all of B; actual `deg_A = 3,3,3` — **tight** |

**Slack test.** The brief's rule: any counting step giving slack ≥ 2 at this instance is
wrong. Under the (false) reductio `s = τ = 3`: DICH(c) gives `D₁≤4, D₂≤3, D₃≤2`, i.e.
`ΣD ≤ 9 = m` — **slack 0, no contradiction**, which is correct (the k=0 branch must run HH
directly). Corollary CNT is unavailable, and even counterfactually it needs `hs`, which is
not pinned here because Lemma S constrains nothing (all degrees ≤ τ): with `hs ≥ 1` it
gives `m ≤ 9` (slack 0); only the *unjustified* choice `hs = 0` gives `m ≤ 8 = m−1`, i.e.
**slack exactly 1**, matching the truth `ΣD_{i≤3} = 8`. **No K-chain step produces slack ≥ 2
on the control.**

### Control (b) — 8-vertex graph `{01,12,13,14,25,56,71,75}`
`n=8, m=8, d=[5,3,2,2,1,1,1,1], Δ=5, α=6, τ=2, diam=4, f=7=α+1` (**hard core**),
`residue=5=α−1, s=3`. Unique maximum independent set `A={0,2,3,4,6,7}`, `B={1,5}`,
`e_B=0`, `min_B deg = 3 = τ+1` ⟹ **hypothesis (i) HOLDS**.

| lemma | available? | yields |
|---|---|---|
| F3′ | yes | (1,3,2),(2,2,1),(3,1,1) ✓ |
| F3 / S / BO / Z / DEC / CNT | **NO** (`s=3 ≠ τ=2`) | never execute |
| Lemma T | yes | after step τ−1=1: `[2,1,1,1,1,0,0]` vs shape `[2,1,1,0,0,0,0]` ⟹ correctly predicts `s ≠ τ` |
| **Z⁺** | yes — **never executes** | no later head is excess |
| DICH(b) | yes, fires once | `i=1, g=5 ≥ s+1=4`: predicts `h₁=0`, `D₁=5` ✓ |
| DICH(c) | yes, fires 2× | (2,3,2,bound 3), (3,1,1,bound 2) ✓ |
| **Theorem K** | **NO** — `residue ≠ α`, though (i) holds | — |
| **Corollary K1** | **YES, and it executes** | diam=4 ✓ and (i) ✓ ⟹ `residue ≤ α−1 = 5`; actual residue **5** ✓ **correct**. Trace of the reductio it runs: assume `s=τ=2`; then `K=B={1,5}` with `g=5,3 ≥ s+1=3`, DICH(b) gives `h=(0,1)`, `hs=1=e_B`, but the true `e_B=0` — contradiction, and `C(2,2)=1 ≠ 0` says B is not a clique, matching R1 |
| Theorem N / N′ / N1 | yes | all three fire and correctly give `residue ≤ α−1` |
| N2 patched | **NO** (`residue ≠ α`) | — |
| N2 contrapositive | yes | `m=8 > Δ+τ(τ+1)/2−1 = 7` ⟹ `residue ≤ α−1` ✓ |
| **N2 unqualified** | fires | asserts `m = 8 ≤ 7` — **FALSE. This is a second counterexample to the unqualified N2, independent of `K_{2,3}`**, and it is a *diam-4 hard-core* one, so it is closer to the line of attack than `K_{2,3}` is |
| R1 | yes | `e_B = 0 < 1 = C(2,2)` ✓ B not a clique |
| C\* | yes (hard core) | `deg_A(b) ≥ 3` for `b ∈ T₁∪T₂`; `deg_A(1)=5, deg_A(5)=3` ✓ |

### Control (c) — 8-vertex tree `{01,12,23,24,25,26,73}`
`n=8, m=7, d=[5,2,2,1,1,1,1,1], Δ=5, α=5, τ=3, diam=4, f=8` (forest, so **not** hard core),
`residue=5=α`, `s=3=τ` — **the reductio hypothesis HOLDS here**, so this is the control on
which the §7.2 B/§7.4 machinery *is* available. **Four** maximum independent sets, with
`B` and `e_B` varying: `e_B ∈ {1,0,2,1}` — the K-J4 choice-dependence probe.

| lemma | available? | yields |
|---|---|---|
| F3, F3′, S | **yes** (`s=τ=3`) | survivor degrees `{1,1,1,1,2}` all ≤ τ=3 ✓; `#{deg ≥ 4} = 1 ≤ τ` ✓ |
| Lemma T | yes | after step 2: `[1,1,0,0,0,0]` = terminal shape ⟹ correctly predicts `s = τ` ✓ |
| **Z⁺** | yes — **never executes** | no later head is excess (bound 3, 2, 1 vs values 2, 1, 1) |
| DICH(b) | fires once | `i=1, g=5 ≥ s+1=4` ⟹ `h₁=0`, `D₁=5` ✓ |
| DICH(c) | fires 2× | (2,2,1,bound 3), (3,1,1,bound 2) ✓ |
| BO | yes | `β = (1,0,0)`, `Σβ = 1 = hs` ✓ |
| Z | yes | zero-occupancy steps `j ∈ {2,3}`; gives `D_i ≤ τ−j+1` ✓ |
| DEC | yes | `i=3`: `D₃ = 1 ≤ τ−3+2+hs = 3` ✓ |
| CNT | yes | `m = 7 ≤ min(3,2)·5 + 3 = 13` ✓ |
| Theorem N / N′ / N1 / N2 / **K** / **K1** | **NO for all four choices of A** | (i) fails everywhere (`min_B deg ∈ {1,1,2,1}`) |
| R1 | yes | `e_B < C(3,2)=3` for every choice ✓ |
| C\* | **NO** | `f = 8 ≠ α+1`; the hard core hypothesis fails (this graph is closed by the *f*-side of the dichotomy, `f = 8 ≥ α+2`) |

**Note (tie-break dependence of `hs`, K-J5):** on this control `hs` is *not* canonical. If
the step-2/3 heads are the degree-2 vertices, `hs = 2`; if they are leaves, `hs = 0`. `s`
and the `D_i` are canonical (I verified over 5.84M trajectories that `s` never varies), but
`hs`, `K`, `β_j` are not. Every §7.4 lemma is stated per-trajectory, so this is sound; it
does mean `hs` in Lemma DEC / Corollary CNT may legitimately be replaced by the minimum
over tie-breaks, a free strengthening the text does not take.

### Control (d) — `K_{2,3}` (the N2 counterexample)
`n=5, m=6, d=[3,3,2,2,2], Δ=3, α=3, τ=2, diam=2, f=4, residue=2=α−1, s=3`.
`A` = the 3-part (unique maximum independent set), `B` = the 2-part, `e_B=0`,
`min_B deg = 3 = τ+1` ⟹ (i) holds.

| lemma | available? | yields |
|---|---|---|
| F3, S, BO, Z, DEC, CNT | **NO** (`s=3 ≠ τ=2`) | never execute — **exactly the R2 finding, reproduced independently** |
| **F3′** | **yes** | (1,3,2),(2,2,2),(3,1,1) ✓ — this is what R2 buys |
| Lemma T | yes | after step 1: `[2,2,1,1]` vs shape `[2,1,1,0]` ⟹ correctly predicts `s ≠ τ` |
| **Z⁺** | yes — **never executes** | no later head is excess |
| DICH(b) | yes — **never executes** | needs `g ≥ s+1 = 4`; Δ=3 |
| DICH(c) | fires 3× | (1,3,3,4),(2,3,2,3),(3,2,1,2) ✓ |
| Theorem N / N′ / N1 / N2-contrapositive | yes | all fire, all correctly give `residue ≤ α−1 = 2` ✓ |
| N2 patched | **NO** (`residue ≠ α`) | — the revision note is right that the standpoint is what was missing |
| **N2 unqualified** | fires | asserts `m = 6 ≤ Δ+τ(τ+1)/2−1 = 5` — **FALSE** ✓ counterexample confirmed |
| Theorem K | **NO** (`residue ≠ α`) | — |
| Corollary K1 / R1 / C\* | **NO** | diam = 2 ≠ 4 |

### Summary of the availability check
* **Named lemma claimed available that never executes:** **Lemma Z⁺** — available on all
  four controls (that generality is precisely what Repair R2 purchases), and it fires
  **zero** times on **every** one of them. **Lemma DICH(b)** likewise never executes on
  (a) and (d). So R2's repair is correct but has **no operative content on any control
  instance**; its value is entirely at instances like the τ=3 live instance below.
* **Lemmas the text's standing scope makes unavailable exactly at the controls:** F3, S,
  BO, Z, DEC, CNT at (a), (b), (d) — three of the four controls have `s ≠ τ`. This is
  R2's point, independently reproduced, and it is why I checked every §7.5 citation again.
* **Everything the K-chain actually needs is available wherever the K-chain executes**: on
  control (b) Corollary K1 fires and returns the true answer.

---

## (4) Trajectories I computed (full intermediate lists)

Implementation: sort non-increasing, delete head `D`, subtract 1 from the next `D` entries
(`splitAt`-truncated, ℕ-truncated), recurse; stop when the head is 0 and return the length.
Labelled, so heads/survivors are tracked per vertex.

```
CONTROL (a)  d = [3,3,3,3,3,2,1]   (vertices x,y,z = B; u1,u2 universal; w~{y,z}; l~{x})
 step 1: L⁰ = [3,3,3,3,3,2,1]  head=x(3)   block = {y,z,u1}      -> D1=3
 step 2: L¹ = [3,2,2,2,2,1]    head=u2(3)  block = {y,z,u1}      -> D2=3
 step 3: L² = [2,1,1,1,1]      head=w(2)   block = {y,z}         -> D3=2
 step 4: L³ = [1,1,0,0]        head=u1(1)  block = {l}           -> D4=1
 stop:   [0,0,0]  residue = 3 = α−1        D = (3,3,2,1), ΣD = 9 = m
 Σ_{i≤3} D_i = 8 = m−1  (matches the brief exactly; slack 1, never 2)

CONTROL (b)  d = [5,3,2,2,1,1,1,1]
 step 1: L⁰ = [5,3,2,2,1,1,1,1]  head=1(5)  block = {5,2,7,0,3}  -> D1=5
 step 2: L¹ = [2,1,1,1,1,0,0]    head=5(2)  block = {2,4}        -> D2=2
 step 3: L² = [1,1,0,0,0,0]      head=6(1)  block = {7}          -> D3=1
 stop:   [0,0,0,0,0]  residue = 5 = α−1    D = (5,2,1), ΣD = 8 = m

CONTROL (c)  d = [5,2,2,1,1,1,1,1]   (residue = α: the reductio holds)
 step 1: L⁰ = [5,2,2,1,1,1,1,1]  head=2(5)  block = {1,3,0,4,5}  -> D1=5
 step 2: L¹ = [1,1,1,1,0,0,0]    head=1(1)  block = {3}          -> D2=1
 step 3: L² = [1,1,0,0,0,0]      head=6(1)  block = {7}          -> D3=1
 stop:   [0,0,0,0,0]  residue = 5 = α       D = (5,1,1), ΣD = 7 = m
 Lemma T check: L² = [1,1,0,0,0,0] = [D₃, 1^{D₃}, 0…] ✓ (predicts s = τ, correct)

CONTROL (d)  K_{2,3}, d = [3,3,2,2,2]
 step 1: L⁰ = [3,3,2,2,2]  head=u1(3)  block = {u2,v1,v2}  -> D1=3
 step 2: L¹ = [2,2,1,1]    head=u2(2)  block = {v3,v1}     -> D2=2
 step 3: L² = [1,1,0]      head=v2(1)  block = {v3}        -> D3=1
 stop:   [0,0]  residue = 2 = α−1     D = (3,2,1), ΣD = 6 = m
 N2 unqualified bound Δ+τ(τ+1)/2−1 = 3+3−1 = 5 < 6 = m  → refuted ✓

LIVE INSTANCE for the K-chain (τ=3, B = triangle, every B-degree = 4 = τ+1)
 A = {a1,a2,a3}, b1~a1,a2 ; b2~a2,a3 ; b3~a3,a1 ; B a triangle.  d = [4,4,4,2,2,2], m=9
 step 1: L⁰ = [4,4,4,2,2,2]  head=b1(4)  block = {b2,b3,a1,a2}  -> D1=4
 step 2: L¹ = [3,3,2,1,1]    head=b2(3)  block = {b3,a3,a1}     -> D2=3
 step 3: L² = [2,1,1,0]      head=b3(2)  block = {a2,a3}        -> D3=2
 stop:   [0,0,0]  residue = 3 = α  ⟹ s = τ = 3, the reductio holds
 Z⁺ FIRES 3×: (j=1, b2, value 4 > s−j+1 = 3, in block ✓), (j=1, b3, 4 > 3, in block ✓),
              (j=2, b3, value 3 > s−j+1 = 2, in block ✓)
 DICH(b) FIRES 3×: g = 4 ≥ s+1 = 4 for each ⟹ h = (0,1,2) = (i−1) ✓ and D_i = g−(i−1) ✓
 BO: β = (2,1,0), Σβ = 3 = hs ✓;  Theorem K: K = B ✓ and e_B = 3 = C(3,2) ✓ (B IS a clique)
 diam = 2, so R1 is silent — Corollary K1 correctly does not apply.

K_6 (Corollary CNT's caution instance):  D = (5,4,3,2,1), ΣD = 15 = m, τ=5, hs=10;
 dropping min(τ,·) gives (hs+1)Δ + τ(τ+1)/2 − (hs+1)(hs+2)/2 = 55+15−66 = 4 < 15 = m
 → the caution is arithmetically correct ✓

[5,5,5,3,3,3,2] (section G row R1; T3 target, checked only for arithmetic):
 L¹ = [4,4,2,2,2,2] ✓ — after deleting H₂ an entry of value 4 remains, so the original
 "no entry ≥ 4" exclusion is indeed false; the repaired "no entry = Z = 5" holds ✓
```

### Corpus verification (my own code, my own graphs)

1. **Canonical + randomised tie-break sweep**: exhaustive labelled connected graphs on
   n = 4,5,6 plus ~7 000 random connected graphs n = 7…11 — **34 265 graphs**, 19 339 with
   `residue = α`, each also run under 2 randomised adversarial tie-breaks.
   Failures: `Lemma 1(1)` 0, `ΣD_i = m` 0, `D₁=Δ` 0, monotonicity 0, `s ≥ τ` 0,
   **F3′ 0, F3 0, S 0, T (both directions) 0, Z⁺ 0 (25 786 non-vacuous firings),
   DICH(b) 0 (58 347 firings), DICH(c) 0, BO 0, Z 0, DEC 0, CNT 0, K=B 0, hs=e_B 0,
   Theorem K 0 (7 159 firings), Corollary K1 0 (550 firings), N 0, N′ 0, N1 0, N2-patched 0.**
   The two known-false controls behaved as they must: `D_i ≤ d_i − (i−1)` failed 74 482
   times and **unqualified N2 failed 981 times**, first witness `K_{2,3}`.
2. **Exhaustive tie-break enumeration** (much stronger than randomisation): for 28 163
   graphs I enumerated *every* legal trajectory — every choice of which maximal entry is
   deleted and every choice of which equal-valued entries fill the block —
   **5 842 009 trajectories**. Failures: F3′ 0, Z⁺ 0 (100 054 firings), DICH(b) 0
   (403 031 firings), DICH(c) 0, Lemma S 0, `K=B` 0, `hs=e_B` 0, **Theorem K 0
   (15 615 firings)**. `s` never varied with the tie-break (0/28 163), confirming that
   `s` and the `D_i` are canonical while `K`, `hs`, `β_j` are not.
3. **Targeted constructive hunt for a Theorem-K counterexample**: for τ = 2,3,4 I built
   every graph from (a graph `H` on `B`, a multiset of neighbourhood types for `A`) with
   every B-degree ≥ τ+1, kept those where `A` is genuinely a *maximum* independent set,
   and tested `residue = α ⟹ B` a clique. τ=2: 51 firings, τ=3: 966, τ=4: 782 — **0
   counterexamples**, and 0 counterexamples to K1 on the 581 diam-4 instances.
4. Algebra checked symbolically/exhaustively: the CNT sum identity
   `Σ_{i=e_B+2}^{τ}(τ−i+2+e_B) = τ(τ+1)/2 − (e_B+1)(e_B+2)/2` for all τ ≤ 8; Theorem N′'s
   "contradiction arises **exactly** when (iii′)" for all τ ≤ 8, e_B ≤ τ−2, Δ ≤ 24 — the
   "exactly" is correct, not merely sufficient; `C(τ,2) > τ−2` for all τ ≥ 1.

---

## (5) What I could not check, and why

1. **Fact 2** (`residue ≤ α`, Favaron–Mahéo–Saclé / Griggs–Kleitman) is cited, not proved,
   and the appendix itself flags the bibliography as "from memory". The whole K-chain rests
   on it twice (Corollary K1's standpoint; `s ≥ τ`). I did not attempt to prove it; I only
   confirmed it never fails on my 34 265-graph corpus.
2. **Lemma 3** (`f ≥ α+1`), **Corollary B1**, **Theorem A/B2**, **Theorem C**, and the
   claim that "全部未覆盖图的直径恰为 4" are outside the appendix; the reduction in §7 is
   taken as given.
3. **§7.6** — Repair R2 says "Theorem K, Corollary K1 and **all of §7.6** assume the
   reductio, so they may keep citing F3 as before". §7.6 is **not in the appendix**, so I
   could not verify that claim. If any §7.6 statement is phrased for general `s`, R2's
   blanket sentence has the same defect R2 was fixing. **Flagged for the owner.**
4. The **measured numbers** (116 189 / 116 873 / 114 914-graph corpora, "91 of 200 τ=3",
   "5 of 118 τ=4", "N′ fires 137 times", "1 464 instances", "70 017 sequences", "19 324
   trajectories") come from author scripts I was instructed not to open and could not
   regenerate at that scale. My independent corpora agree qualitatively at every point I
   could compare (0 failures for every K-chain claim; the `K = B` regime is rare; hypothesis
   (i) is rare at τ = 4).
5. **Section E** (Theorem T3, the 5bis repairs, Repair R1) was excluded by the brief; I
   touched Repair R1 only to confirm the arithmetic of the `[5,5,5,3,3,3,2]` witness quoted
   in section G, which is correct. No verdict on T-J1…T-J5.
6. The **Lean-side** claims (that `residue_seq` transcribes `residueAux`, that
   `havelHakimiStep_length_cons` says what §3 says it says, the `Induced.lean` / `Residue.lean`
   definitions) — no repository access; I implemented `residueAux` from the appendix's prose
   spec and reproduced the appendix's own sanity checks (`residue(K₂)=1`, `residue(Cₙ)=⌈n/3⌉`
   for n = 3…9 — both confirmed by my implementation).
