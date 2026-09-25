VERDICT: PARTIAL — Theorem T3's conclusion is SOUND and I could not refute it after an exhaustive search of every τ=3 graph on n ≤ 37 vertices plus ~86 M further large-n instances, and every load-bearing step of the k-case analysis (including R1, R2, R3) checks out; but the repaired text still carries two real textual defects, both one line long and neither load-bearing: the **T-b repair is scoped to `k=1` while the `k=0` bullet reaches it by "同上" and needs it too**, and **R3 leaves §7.7's contradictory adjudication of the very sentence it deletes standing (and that adjudication is itself arithmetically wrong)**.
TEXT VERSION REVIEWED: prompts/w61_S3_T3R3.md

All numbers below were produced by my own code (scratch dir
`…/scratchpad/w61/`: `hh.py`, `search.py`, `search2.py`, `struct.py`,
`control.py`, `probes.py`, `branches.py`, `brute7.py`, `bigsearch.py`).
**No figure printed in the brief is reused anywhere in this report.**
Calibration first: my `residueAux` transcription gives `residue(K₂) = 1`,
`residue(Cₙ) = ⌈n/3⌉` for n = 3…9, `residue(Kₙ) = 1` and `residue(S_n) = n−1`
for n ≤ 7, and the identity `residue = n − s` fails 0 times over every
descending sequence of length ≤ 7. A second, count-based implementation
(`residue_counts`, needed for n up to 10⁶) agrees with the list implementation
on 30 166 random graphical sequences, 0 mismatches, and returns
`residue(C_1000000) = 333334 = ⌈10⁶/3⌉`.

---

# (a) Refutation search — what space, what code, what it returned

**Target of the search.** A connected non-forest `G` with `diam = 4`,
`τ = n − α = 3`, `f = α+1`, `residue = α`. I did not use a single lemma of the
text as a filter: `α`, `diam`, `f` and `residue` are each computed from scratch.

**Why the search space is what it is.** `τ = 3` means `|B| = |V∖A| = 3` for a
maximum independent set `A`, and since `A` is independent the graph is
determined up to isomorphism by `(G[B] iso-type, μ)` where
`μ[T] = #{a ∈ A : N(a) = T}` over the 7 nonempty `T ⊆ B`. So enumerating all
7-part **compositions** of `α` (not a bounded box) together with the 4 types of
`G[B]` is a *complete* enumeration of every τ = 3 graph on `n = α+3` vertices.
I also proved for myself (and used) that `diam` of such a graph is a function of
`(G[B], support of μ)` alone — the quotient on `B ∪ {occurring types}` is a
graph homomorphic image of `G` and lifts shortest paths — which is what makes
the huge-multiplicity search below meaningful.

| # | space searched | size | refutations |
|---|---|---|---|
| S1 | **all 2²¹ labelled graphs on 7 vertices**, brute force, no parameterisation at all (`brute7.py`) | 2 097 152 graphs; 420 210 connected with α = 4 exactly; 7 560 in the hard core | **0** |
| S2 | **complete** enumeration of *every* τ = 3 graph with α ≤ 34, i.e. **every n ≤ 37** (`search2.py 34`) | 89 834 932 parameter tuples, 721 764 distinct degree spectra, 628 s | **0** |
| S3 | multiplicity box `μ ∈ [0..10]⁷ × 4` (reaches n = 73 for balanced μ) (`search.py 10`) | 77 932 836 tuples, 915 s | **0** |
| S4 | large-n targeted: all 140 of the 508 `(G[B], support)` pairs with quotient diameter 4, then a geometric multiplicity ladder up to 100 000 and 1.5 M log-uniform random draws up to ≈3·10⁵ (`bigsearch.py`) | 6 179 553 ladder + 1 500 000 random assignments, `n` up to ≈10⁶ | **0** |

**The search is not vacuous — here is the funnel** (S2, α ≤ 34):

```
parameter tuples (min deg_A(b) >= 1)            89 834 932
  residue = alpha  (s = 3)                      22 544 804
  ... and diam = 4                                  26 447
  ... and tau = 3                                    26 378
  ... and non-forest                                 24 013
  ... and f = alpha+1     ==>  REFUTATION                 0
```

and the same shape in S3 (19 499 321 → 4 933 → 4 910 → 4 433 → **0**). So there
are **24 013 near-misses** at n ≤ 37: connected, non-forest, `diam = 4`,
`τ = 3`, `residue = α` — every one of them killed only by the *last*
condition, `f = α+1`. The smallest is `μ = {xz:1, yz:2}` on an independent `B`,
`d(G) = [3,2,2,2,2,1]`, `n = 6`, `α = 3`, `residue = 3 = α`, `diam = 4`, but
`G − y` is a forest so `f = α+2`. **Theorem T3 is therefore genuinely tight**:
weakening `f = α+1` to `f ≤ α+2` makes it false immediately. I mention this
because it means none of the branch arguments can be slack — and indeed the
minimum of `m − Σ_{i≤3} D_i` over the whole hard core is exactly **1**
(histogram over the complete α ≤ 12 hard core, 44 574 instances:
`{1: 10384, 2: 15008, 3: 19182}`), attained at `d(G) = [3,3,3,3,3,2,1]`.

**Cross-validation of the parameterisation.** S1 is completely independent of
the parameterisation machinery. It finds exactly **5** hard-core degree
sequences at n = 7:

```
[3,3,3,3,3,2,1] (1260 labelled copies)   residue = 3 = alpha-1   heads (3,3,2,1)
[4,3,3,3,3,1,1] (2520)                   residue = 3 = alpha-1   heads (4,2,2,1)
[4,4,3,3,2,1,1] (1260)                   residue = 3 = alpha-1   heads (4,3,1,1)
[4,4,3,3,3,2,1] (1260)                   residue = 3 = alpha-1   heads (4,3,2,1)
[4,4,4,3,3,1,1] (1260)                   residue = 3 = alpha-1   heads (4,3,2,1)
```

— exactly the five instances my parameterised enumerator produces for the five
`(e_B,k)` cells occupied at n = 7. That validates `quotient_diam`, `vc_le2` and
the `f`-test used everywhere else.

**Conclusion of (a): NOT REFUTED.** No counterexample exists on ≤ 37 vertices,
none in the 10-bounded multiplicity box up to n = 73, and none among ~7.7 M
huge-multiplicity instances up to n ≈ 10⁶.

---

# (b) Per-joint verdicts

| joint | verdict | basis |
|---|---|---|
| **T-J1** — k-split exhaustive; (F-b) disjoint-pair arguments; `k=0 ⇒ e_B=0`, `k=1 ⇒ e_B≤1` | **CLEAN** | `k ∈ {0,1,2,3}` is trivially exhaustive and every `(e_B,k)` combination is covered. I enumerated by machine, for each of the 4 `G[B]` types, *all* pairs `{T₁,T₂}` of disjoint nonempty subsets with no `G[B]`-edge between them: empty → 6 pairs, one edge → **exactly 3**, all containing `{w}`; path → **exactly 1**, `{{e₁},{e₂}}`; triangle → **0**. That is verbatim the case list C2 and C3 use, so both are exhaustive, and the triangle line re-proves (F-c). `k=0 ⇒ e_B=0` and `k=1 ⇒ e_B≤1` follow from C2(`k≥1`)/C3(`k≥2`); checked directly on **2 602 772** hard-core instances (complete for α ≤ 22): 0 failures, and the cells `(1,0),(2,0),(2,1)` are empty. |
| **T-J2** — `k=3` endgame after **R1** | **CLEAN** | R1 is valid and necessary. Over **17 347** graphical `k=3` shapes (`X≥Y≥Z≥4` plus entries ≤3): `D₁ = X` and `D₂ = Y−1` fail **0** times (so the branch's opening is tie-break-proof); the *original* exclusion "no entry of `L¹∖{H₂}` is ≥ 4" fails **10 461** times (e.g. `d = [5,5,5,3,3,3,2]`, `L¹ = [4,4,2,2,2,2]`, `L¹∖{H₂} = [4,2,2,2,2]`), so the round-A defect was real; the **repaired** exclusion "no entry of `L¹∖{H₂}` equals `Z`" fails **0** times. The (i)/(ii) split is exhaustive (`H₂` is an A-entry or one of the two surviving B-entries) and case (i) is genuinely reachable — under a tie-break preferring A-entries, `d = [4,4,4,3,3,3,1]` puts an A-entry at the head of step 2 — and in every such shape `Y = Z = 4` exactly as the repair asserts (0 exceptions). (ii-a) `max(L²) ≤ max(3, Z−1)` whenever `H₂ ∈ {y,z}`: 0 failures. |
| **T-J3** — **Lemma U** and its two hypotheses at both call sites | **CLEAN** | Lemma U's statement is correct (over 2 251 shapes where both premises hold, `max(L¹) ≤ 2` and `Σ_{i≤3}D_i ≤ Δ+4` fail 0 times), and its proof is tie-break-robust (all value-3 entries are the *maximum* of `R`, so if there are ≤ Δ of them they lie in the first Δ positions under **any** descending order). The retracted blanket claim is genuinely false — smallest witnesses `[3,3,3,3,3,1]` (Δ=3, four 3s in R, m = 8 > Δ+4 = 7) and the text's own control `[3,3,3,3,3,2,1]` (m = 9 > 7). Both live call sites verified: **k=1,e_B=1 case II** has `p = 2`, `Y=Z=3`, so `#{3s in R} = p+2 = 4 ≤ X` (X ≥ 4) ✓ and `m = X+5 > X+4`; **k=1,e_B=0** has `p ∈ {1,2}`, `Y=Z=3`, `#{3s in R} = p+2 ≤ 4 ≤ X` ✓ and `m = X+6 > X+4`. `p ∈ {1,2}`, `Y=Z=3` and `m = X+6` (resp. `X+5`) are reductio-free and I confirmed them on every hard-core instance in those cells: 0 failures. `k=0` does not call Lemma U (it runs HH directly), as the revision note says. |
| **T-J4** — `k=2 / e_B=2` after **R3** | **CLEAN** | Yes, the sum contradiction closes the branch alone. Over **32 800** admissible triples (`1 ≤ b₀ ≤ a₀ ≤ 40`, `1 ≤ c₀ ≤ 40`, i.e. every boundary case including `a₀=b₀=c₀=1`, `a₀=b₀` ties, `c₀` large): the degree sequence is graphical everywhere, `m = a₀+b₀+2c₀+5` is right **32 800/32 800**, `L¹ = [Y−1,2,2,1^{c₀+b₀+1},0^{a₀−1}]` right 32 800/32 800, `L² = [1,1,1,1,0^…]` right 32 800/32 800, `D = (X, Y−1, 1)` right 32 800/32 800, and `Σ_{i≤3}D_i = m−1` holds 32 800/32 800. The branch's *upstream* parameterisation (`deg(c)=3`, `p=1`, `n_c = μ[{c,e₁}] = μ[{c,e₂}] = 0`, `c₀ ≥ 1`, `a₀,b₀ ≥ 1`, and the displayed `d(G)`) is reductio-free, and I verified it against **every** hard-core instance in cell `(e_B,k) = (2,2)` — 1 330 instances, complete for α ≤ 22 — with **0** mismatches. Tie-breaks are harmless: the step-1 block ends inside a run of equal 1s (or exactly at the last 2 when `a₀=1`) and the step-2 block ends inside a run of equal 1s, so the multiset is unaffected; independently, over 1 062 random graphical sequences × 4 adversarial tie-breaks the head sequence `D₁…D_s` never changed. |
| **T-J5** — `p ≥ 3` exclusion, `k=1,e_B=0`, and the Lemma 3 dependence | **PARTIAL** | The mathematics is right: the T-b repair's `p = 3` argument is correct (`deg_A(y) ≥ p = 3` and `deg(y) = deg_A(y) ≤ 3` force `n_y = μ[{x,y}] = μ[{y,z}] = 0`, same for `z`, leaving only types `{x,y,z}` and possibly `{x}`, which are not disjoint ⇒ no (F-b) pair). Confirmed empirically: **0** hard-core instances with `k ≤ 1`, `e_B = 0`, `p = 3` (and the `(k,p)` histogram over the whole hard core, complete for α ≤ 22, is `{(0,2):3, (1,1):54, (1,2):162}` — `p = 3` never occurs, and `k=0` only ever has `p=2`). T-c is also fine: I re-proved Lemma 3 myself (for `v ∉ A`, `G[A ∪ {v}]` has all its edges at `v`, so it is a star, hence a forest ⇒ `f ≥ α+1`), so the negation `f ≤ α+1 ∧ residue ≥ α` does collapse to `f = α+1 ∧ residue = α` via Lemma 3 + Fact 2. **But** the repair is written only for `k = 1` and the `k=0` bullet reaches the same defective sentence through "同上" — defect **D1** below. |
| **T-J6** — does R3 leave anything dangling? | **PARTIAL** | R3's own edit is clean: the deleted clause is the last sentence of the branch, nothing downstream refers to it, the §7.3.4 numerical line (`F3(k=2,e_B=2) 1331 组参数`) is about a parameter family and is unaffected, and the replacement sentence is correct. **But** R3 leaves the §7.7 "Two wording fixes adopted (neither is a defect)" bullet standing, which (i) quotes a sentence that no longer exists in the amended text, (ii) scores it *"terse but correct"* — flatly contradicting §7.8 B's "**UPHELD**" for the same sentence — and (iii) mis-diagnoses it. Defect **D2** below. I also record two exposition remarks (E1, E2). |

---

# (c) Defects

## D1 (real, minor, repairable, conclusion survives) — the T-b repair does not cover the `k=0` call site

Quoted line (§7.3.3, `k ≤ 1` section, `k=0` bullet, line 464 of the brief):

> "**k=0**：由 C2/C3 得 e_B=0；由 C1 与 codeg 条件**同上**得 p∈{1,2}，…"

The "同上" points at the `k=1, e_B=0` bullet, whose `p ≥ 3` exclusion reads

> "p ≥3 给 deg(y) ≥ p+…>3，矛盾"

and which §7.3 5bis **declares false** at `p = 3` (correctly). The registered
repair, however, is headed

> "**缺口 T-b（§7.3.3，k≤1 的 "k=1, e_B=0" 分支）**"

and its body opens

> "**p = 3 单独处理**：**k=1 要求** B 中至少两点度 ≤3，设为 y,z"

so as written the repair is a statement about the `k=1` branch only. The `k=0`
bullet therefore still inherits, by "同上", a sentence the text itself has
declared false, and no repair is stated for it.

*Why it fails.* At `k = 0, e_B = 0, p = 3` the discarded reasoning gives
`deg_A(y) ≥ 3`, which is **not** `> 3`; `deg(y) = 3` is admissible. So the
sentence does not exclude `p = 3` at `k = 0` any more than it did at `k = 1`.

*Smallest configuration exposing it.* `e_B = 0`, `p = 3`, `n_x = n_y = n_z =
μ[{x,y}] = μ[{x,z}] = μ[{y,z}] = 0` — i.e. `α = 3`, `n = 6`,
`d(G) = [3,3,3,3,3,3]` (= `K_{3,3}`). Every B-degree is exactly 3 so `k = 0`,
`e_B = 0`, and the quoted sentence yields nothing. (The configuration is of
course killed by the *repair's* argument — only the type `{x,y,z}` occurs, so
(F-b) has no candidate pair and `diam = 3 ≠ 4` — but that argument is not
stated for `k = 0`.)

*Repairable?* **Yes, one word.** The repair's only use of the hypothesis is
"`k=1` 要求 B 中至少两点度 ≤3"; at `k = 0` **all three** B-degrees are ≤ 3, so
the identical argument runs (and is even shorter: all three give
`n_b = μ[pairs ∋ b] = 0`, so `r = 0`, contradicting (F-b)'s `r ≥ 1`). Changing
"k=1 要求" to "k ≤ 1 要求" repairs it.

*Does the CONCLUSION survive?* **Yes.** Empirically there is no hard-core
instance with `k ≤ 1`, `e_B = 0`, `p = 3` at all (0 out of all 2 602 772
hard-core instances with α ≤ 22 — see §(d)), and the repaired argument covers
`k = 0` verbatim.

*Why I am reporting a one-word defect.* This is exactly the failure mode of the
two previous rounds: a repair whose scope is narrower than its call sites. The
`k=0` bullet is a live branch of the exhaustive case split, and it currently
cites a sentence the same document marks as a false proposition.

## D2 (real, minor, repairable, conclusion survives) — R3 leaves §7.7's contradictory adjudication of the deleted sentence standing, and that adjudication is itself wrong

§7.7 (section J), "Two wording fixes adopted (**neither is a defect**)":

> "§7.3 5bis, k=2/e_B=2: '終止形狀要求恰有 D_3=1 個 1，實有 4 個' undercounts the
> terminal shape (`[D_3, 1^{D_3}, 0^…]` has `D_3` ones **after** the head). The
> decisive argument in that branch is the sum `Σ_{i≤3} D_i = m−1 < m`, which is
> unaffected. **Scored *terse but correct*.**"

§7.8 B (section K, = R3) adjudicates the *same sentence* the other way —
"**UPHELD**", a defect — and deletes it. After R3 the amended text contains two
mutually contradictory adjudications of one clause, and the §7.7 one quotes a
sentence that is no longer in the text. That is precisely a sentence left
dangling by R3.

Worse, **§7.7's diagnosis is arithmetically wrong** while §7.8 B's is right. At
`D₃ = 1` the terminal shape is `[1, 1, 0^…]`: one `1` **after** the head. So
"終止形狀要求恰有 D_3 = 1 個 1" is *correct* under the after-head reading —
it does **not** "undercount the terminal shape". The actual error is the one
§7.8 B names: the "required" count is read after-the-head while the "actual"
count (4) is read as a total (`L² = [1,1,1,1,0^…]` has 4 ones in total, 3 after
the head). My check: over the 32 800 admissible `(a₀,b₀,c₀)`, the deleted clause
is literally right under a consistent reading in **0** of them, under either
reading — so the deletion is justified and §7.7's "terse but correct" score is
not.

*Repairable?* **Yes** — strike the §7.7 bullet or mark it superseded by R3.
*Conclusion survives?* **Yes**, entirely; the sum argument is unaffected (0
failures in 32 800 instances).

## E1 (exposition only, not a defect) — the `k=2` preamble's `D₃` formula is silently contradicted by its own `e_B=2` sub-branch

The preamble asserts `D_3 = Z+1−e_B` for all three `k=2` sub-branches; with
`Z = 3, e_B = 2` that reads `D₃ = 2`, whereas the `e_B=2` bullet computes
`D₃ = 1` from the explicit trajectory and never remarks on the clash. This is
*not* an error — both are consequences of the reductio and the clash **is** the
contradiction, restated as `Σ_{i≤3}D_i = m−1 < m` — but a reader can lose the
thread. One clause ("the reductio forces `D₃ = Z+1−e_B = 2`, but the explicit
trajectory gives `max(L²) = 1`") would make the branch self-evident.

## E2 (exposition only) — two unflagged inferential shortcuts

* `k=2, e_B=0`: "故第 1 步有一个值为 3 的项未被减" is asserted, not derived; the
  valid argument is the contrapositive counting in the *next* sentence (if all
  `1+p` entries of value ≥ 3 in `R` are decremented then `L¹ = [Y−1, ≤2, …]`,
  hence `D₃ ≤ 2 ≠ 3`). I verified the underlying implication directly — "if
  `#{entries ≥ 3 in R} ≤ X` then `D₃ ≤ 2`" fails **0** times over 19 665
  graphical `k=2` shapes — so the step is sound as stated, just under-argued.
  (It is the engine of *both* the `e_B=0` and `e_B=1` sub-branches.)
* `k=2, e_B=2`: "设 X = a₀+c₀+2 ≥ Y = b₀+c₀+2" is a WLOG (relabel `e₁ ↔ e₂`),
  not flagged as such.

**No load-bearing defect found.** Every step that carries weight — the k-split,
C1/C2/C3, (F-a)/(F-b)/(F-c), Lemma U and both its call sites, the R1-repaired
`k=3` endgame, the R3-repaired `k=2/e_B=2` sum contradiction, and the T-b and
T-c repairs — verified.

**Note on R2.** R2 (generalising Lemma F3 to F3′ for arbitrary `s`) has **no
bearing on T3**: T3's proof cites Lemma 1, Fact 2, Lemma 3, Lemma 4, Lemma T,
Lemma U and C1–C3, and never cites F3, Lemma S, Lemma H or Theorem N. I still
checked R2 itself: F3 *as stated* (with `τ`) fails on 4 of my 9 control
instances, F3′ (with `s`) fails on **none** of them, and `K_{2,3}`
(`d = [3,3,2,2,2]`, `α = 3`, `τ = 2`, heads `(3,2,1)`, `s = 3 ≠ τ`) is a live
witness that the old citation reached outside its scope. R2 is correct and is a
genuine strengthening.

---

# (d) Control-case / counterfactual-availability section (T12) — REQUIRED PROBE

I built one control instance for **every occupied `(e_B,k)` cell** (all 9), each
a genuine member of the hard core (connected, non-forest, `diam = 4`,
`f = α+1`, `τ = 3`) but of course **outside** the reductio, since `residue = α`
is empty there. For each I audited *every* lemma the branch would have
available — hypotheses first, then what it actually yields.

Cell representatives (my own construction; `p,q,r` and B-degrees are mine):

| cell `(e_B,k)` | `d(G)` | n | α | residue | s | notes |
|---|---|---|---|---|---|---|
| (0,0) | `[3,3,3,3,3,2,1]` | 7 | 4 | 3 = α−1 | 4 | the unique `k=0` hard-core graph |
| (0,1) | `[4,3,3,3,2,2,2,1]` | 8 | 5 | 3 = α−2 | 5 | `p=1`, B-deg `(3,3,4)` |
| (0,2) | `[4,4,3,3,3,2,2,1]` | 8 | 5 | 3 = α−2 | 5 | B-deg `(3,4,4)` |
| (0,3) | `[4,4,4,3,3,3,2,1]` | 8 | 5 | 3 = α−2 | 5 | B-deg `(4,4,4)` |
| (1,1) | `[4,3,3,3,3,1,1]` | 7 | 4 | 3 = α−1 | 4 | C2 case II |
| (1,2) | `[4,4,3,3,3,2,1]` | 7 | 4 | 3 = α−1 | 4 | |
| (1,3) | `[5,5,4,3,3,3,2,1]` | 8 | 5 | 3 = α−2 | 5 | |
| (2,2) | `[4,4,3,3,2,1,1]` | 7 | 4 | 3 = α−1 | 4 | **exactly the R3 branch with `a₀=b₀=c₀=1`** |
| (2,3) | `[4,4,4,3,3,1,1]` | 7 | 4 | 3 = α−1 | 4 | |

## Per-lemma availability audit

**Always available and executing correctly on all 9 controls:**

* **Lemma 1(1)** `residue = n − s`: holds on 9/9 (e.g. (2,2): `3 = 7 − 4`).
* **Lemma 1(2)** `Σ_i D_i = m` over *all* `s` steps: holds on 9/9 (e.g. (0,3):
  `4+3+2+2+1 = 12 = m`). Note the truncated sum `Σ_{i≤3} D_i` is `m−1`, `m−2`
  or `m−3` on the controls — never `m` — which is the whole content of T3.
* **Fact 2** `residue ≤ α`: holds 9/9 (strictly, on all of them).
* **Lemma 3** `f ≥ α+1`: holds 9/9; I re-proved it rather than citing it.
* **Lemma 4 / (F-a)**: I re-proved it myself (`G[A ∪ {u,v}]` has α+2 vertices
  so must contain a cycle; `A` independent forces that cycle to be `u–v–a` or
  `u–a–v–b`, giving `codeg ≥ 1` resp. `≥ 2`) and then checked the codegree
  conditions on **44 574** hard-core instances (complete for α ≤ 12) — 0
  failures. Likewise **(F-b)** 0 failures, `r ≥ 1` 0 failures, and `e_B ≤ 2` 0
  failures (**(F-c)**).

**Available exactly where the branch says, and executing:**

* **Lemma C1** (`e_B = 0`): available in cells (0,\*), and yields
  `min B-deg ≥ 2` — true on every one (0 failures). It is the *hidden*
  citation the 5bis "另记" registers for `k=2, e_B=0 ⇒ D₃ = 3`, and it is
  genuinely needed there: without `Z ≥ 2` the step `D₃ = Z+1 ≤ 3 ⇒ D₃ = 3`
  does not go through.
* **Lemma C2** (`e_B = 1`): available in cells (1,\*); yields all B-degrees ≥ 3
  and `k ≥ 1`. 0 failures.
* **Lemma C3** (`e_B = 2`): available in cells (2,\*); on the (2,2) control it
  yields `deg(e₁) = deg(e₂) = 4 ≥ 4` and `deg(c) = 3 ≥ 3`, `k = 2 ≥ 2`. 0
  failures over 1 330 `(2,2)` and 688 579 `(2,3)` instances (α ≤ 22).
* **Lemma U**: premises hold — and it **executes** — on exactly the controls in
  cells (0,1) and (1,1), the two cells that correspond to its two call sites.
  On (0,1): `Δ = 4 ≥ #{3s in R} = 3`, `max(R) = 3`, so `Σ_{i≤3}D_i ≤ 8` while
  `m = 10` ⇒ `residue ≤ α−1` (true: `residue = α−2`). On (1,1): `Δ = 4 ≥ 4`,
  `Σ_{i≤3}D_i ≤ 8` while `m = 9` ⇒ `residue ≤ α−1` (true). On (0,0) premise 2
  fails (`Δ = 3 < 4 = #{3s in R}`); applied anyway it would claim `m ≤ 7`
  against the true `m = 9` — this is the retracted blanket claim, and I
  reproduce the failure independently. On all `k ≥ 2` controls premise 1 fails
  (`max(R) ≥ 4`).

**Lemmas the text has available in a branch but which NEVER execute** (the
required naming):

1. **Lemma T, in the `k=2 / e_B=2` branch.** Lemma T is declared available in
   the reductio set-up ("且（Lemma T）第 2 步后的表恰为 `[D_3,1^{D_3},0^…]`") and
   §7.2 B calls its "two entries ≥ 2" corollary "这正是 … 证明的引擎". On the
   (2,2) control `L² = [1,1,1,1,0]` has **zero** entries ≥ 2, so the corollary
   cannot fire. This is not an accident of one control: over **all 32 800**
   admissible `(a₀,b₀,c₀)` of that branch, `L² = [1,1,1,1,0^…]` always, so the
   "two entries ≥ 2" test fires **0 / 32 800** times. **Lemma T never executes
   in the `k=2/e_B=2` branch** — which is exactly why the terminal-shape clause
   there had to be a miscount and why R3 was forced to fall back on the sum.
   R3 is therefore not merely a wording fix but the removal of a lemma
   invocation that could never have worked. (It also does not fire on the
   (0,0), (1,1), (1,2) or (2,3) controls; it does fire on (0,1), (0,2), (0,3),
   (1,3).)
2. **Theorem N and Corollary N1, in the `k=3` branch.** On the (0,3) control
   both are fully available — `(i)` all B-degrees `≥ τ+1 = 4` ✓, `(ii)`
   `e_B = 0 ≤ τ−2 = 1` ✓, `(iii)` `min B-deg = 4 ≥ 2e_B+3 = 3` ✓ — and they
   would immediately give `residue ≤ α−1`, which is the branch's goal. T3's
   `k=3` argument never cites them; it re-derives the same conclusion through
   (ii-a). Not an error, but it means the §7.3.5 claim that Theorem N "已决"
   a slice of the τ = 3 problem is never cashed inside T3.
3. **Lemma S / Lemma F3 / Lemma H, everywhere in T3.** All three are stated
   under §7.2 B's standing hypothesis `residue = α` (`s = τ`), which is false
   on every control (as it must be — the reductio set is conjecturally empty).
   Their hypotheses therefore genuinely fail on all 9 controls. Two sharp
   consequences: **(a)** on the (0,3) control **Lemma S's conclusion is
   actually FALSE** — the survivors are `{y, A[xy], A[xyz]}` with degrees
   `4,3,2` and `4 > τ = 3` — so the reductio hypothesis is load-bearing, not
   decorative; **(b)** **Lemma F3 as stated (with `τ`) is false** on the (0,1),
   (0,2), (0,3) and (1,3) controls, while **F3′ (R2, with `s`) holds on all
   nine** — an independent confirmation that the R2 scope defect was real and
   that R2 fixes it in the right direction.
4. **Corollary N2**, in every branch: it now carries the standing hypothesis
   `residue = α` explicitly (second-round revision), so it is unavailable on
   every control. Its stated counterexample `K_{2,3}` reproduces on my code:
   `α = 3, τ = 2, e_B = 0`, B-degrees `3,3 = τ+1`, `Δ = 3`, `m = 6`, and
   `Δ + τ(τ+1)/2 − 1 = 5 < 6` — but heads `(3,2,1)`, `s = 3 ≠ τ = 2`, so
   `residue = 2 = α−1` and the reductio stance never held. The revision is
   necessary and correct.

## Structural audit on the complete hard core (my own scan)

Every claim below was checked on **every** τ = 3 hard-core instance with
α ≤ 22, i.e. every hard-core graph on n ≤ 25 vertices — **2 602 772**
instances (`struct.py 22`, 221 s) — with the reductio **not** assumed:

```
(e_B,k) cells: {(0,0):3, (0,1):216, (0,2):22302, (0,3):1033518,
                (1,1):38, (1,2):6403, (1,3):850383, (2,2):1330, (2,3):688579}
   -> (1,0), (2,0), (2,1) are EMPTY, confirming C2's k>=1 and C3's k>=2
k=0 => e_B=0                         failures 0
k=1 => e_B<=1                        failures 0
k<=1, e_B=0  =>  p in {1,2}          failures 0  ((k,p) histogram {(0,2):3,(1,1):54,(1,2):162})
k<=1, e_B=0  =>  Y=Z=3, m=X+6        failures 0
k=1,  e_B=1  =>  Y=Z=3, m=X+5        failures 0;  case (I) (deg(w)>=4) occurs 0 times,
                                                  case (II) 38 times
k=2,  e_B=1  =>  Z=3                 failures 0
k=2,  e_B=2  =>  full R3 parameterisation (p=1, n_c=mu[ce_i]=0, c0,a0,b0>=1,
                 d(G) and m = a0+b0+2c0+5)                   failures 0 / 1330
k=0          =>  d(G) = [3,3,3,3,3,2,1] and the graph is UNIQUE up to iso
                 (exactly 3 (G[B],mu) representatives, all the same graph)
T-b probe: hard-core instances with k<=1, e_B=0, p=3         0
```

A second scan (`search2.py 12 hard`, complete for α ≤ 12, 44 574 hard-core
instances) additionally checked **(F-a)**, **(F-b)**, `r ≥ 1`, `e_B ≤ 2`, C1,
C2, C3 directly: **0 failures on every one**; a third (box `μ ≤ 3`, 25 236
instances) reproduced the same. Slack histogram of `m − Σ_{i≤3} D_i` over the
complete α ≤ 12 hard core: `{1: 10384, 2: 15008, 3: 19182}` — **the minimum is
exactly 1**, attained at `d(G) = [3,3,3,3,3,2,1]`.

**Firewall.** One claim I could *not* test this way and must flag: the
`k=2, e_B=0` sub-branch's `Z = 2` is **reductio-dependent**, and the hard core
*without* the reductio contains 18 882 instances in that cell (α ≤ 22) with
`min B-deg = 3` or `4`. My own test of it therefore "failed" 18 882 times —
that is a firewall artefact of my test, not a defect of the text; the text's own
firewall note makes the same point about `k=3 ⇒ e_B=2`. The correct
reductio-free ingredient of that sub-branch (the counting step) is verified
separately: 0 failures in 19 665 shapes.

---

# (e) Trajectories (my own implementation, all intermediate lists)

```
T1  k=0 hard-core graph  A = {u1,u2 universal, w~{y,z}, l~{x}}
    d = [3,3,3,3,3,2,1]   n=7  m=9   (alpha=4, tau=3, diam=4, f=5=alpha+1)
      L^0 = [3, 3, 3, 3, 3, 2, 1]     head D_1 = 3
      L^1 = [3, 2, 2, 2, 2, 1]        head D_2 = 3
      L^2 = [2, 1, 1, 1, 1]           head D_3 = 2
      L^3 = [1, 1, 0, 0]              head D_4 = 1
      L^4 = [0, 0, 0]
      D = (3,3,2,1)  s = 4  residue = 3 = alpha-1
      sum_i D_i = 9 = m ;  sum_{i<=3} D_i = 8 = m-1     <-- the tight case, slack 1

T2  R3 branch k=2/e_B=2 at the boundary (a0,b0,c0) = (1,1,1)
    d = [4,4,3,3,2,1,1]   n=7  m=9   (X=Y=4, so the step-1 head is a TIE)
      L^0 = [4, 4, 3, 3, 2, 1, 1]     head D_1 = 4
      L^1 = [3, 2, 2, 1, 1, 1]        head D_2 = 3      (= Y-1, as the text says)
      L^2 = [1, 1, 1, 1, 0]           head D_3 = 1      (= 1, as the text says)
      L^3 = [1, 1, 0, 0]              head D_4 = 1
      L^4 = [0, 0, 0]
      D = (4,3,1,1)  s = 4  residue = 3 = alpha-1
      sum_{i<=3} D_i = 8 = m-1 < m = 9   <-- R3's contradiction, verbatim

T3  R3 branch, (a0,b0,c0) = (3,1,2)
    d = [7,5,3,3,2,2,1,1,1,1]   n=10  m=13
      L^0 = [7, 5, 3, 3, 2, 2, 1, 1, 1, 1]   head D_1 = 7
      L^1 = [4, 2, 2, 1, 1, 1, 1, 0, 0]      head D_2 = 4
      L^2 = [1, 1, 1, 1, 0, 0, 0, 0]         head D_3 = 1
      L^3 = [1, 1, 0, 0, 0, 0, 0]            head D_4 = 1
      L^4 = [0, 0, 0, 0, 0, 0]
      D = (7,4,1,1)  sum_{i<=3} = 12 = m-1 < 13

T4  R3 branch, extreme c0: (a0,b0,c0) = (1,1,9), X = Y = 12
    d = [12,12,3,3,2,2,2,2,2,2,2,2,2,1,1]   n=15  m=25
      L^0 = [12,12,3,3,2,2,2,2,2,2,2,2,2,1,1]   head D_1 = 12
      L^1 = [11,2,2,1,1,1,1,1,1,1,1,1,1,1]     head D_2 = 11
      L^2 = [1,1,1,1,0,0,0,0,0,0,0,0,0]        head D_3 = 1
      L^3 = [1,1,0,0,0,0,0,0,0,0,0,0]          head D_4 = 1
      L^4 = [0,...]
      D = (12,11,1,1)  sum_{i<=3} = 24 = m-1 < 25

T5  k=1/e_B=1 control, the cell where Lemma U really executes
    d = [4,3,3,3,3,1,1]   n=7  m=9   (Delta=4, #3s in R = 4 <= Delta)
      L^0 = [4, 3, 3, 3, 3, 1, 1]     head D_1 = 4
      L^1 = [2, 2, 2, 2, 1, 1]        head D_2 = 2      <-- Lemma U: all <= 2 after step 1
      L^2 = [2, 1, 1, 1, 1]           head D_3 = 2
      L^3 = [1, 1, 0, 0]              head D_4 = 1
      D = (4,2,2,1)  sum_{i<=3} = 8 = Delta+4 < m = 9   <-- Lemma U's bound is TIGHT here

T6  R1's k=3 witness   d = [5,5,5,3,3,3,2]   n=7  m=13
      L^0 = [5, 5, 5, 3, 3, 3, 2]     head D_1 = 5
      L^1 = [4, 4, 2, 2, 2, 2]        head D_2 = 4
      L^2 = [3, 2, 1, 1, 1]           head D_3 = 3
      L^3 = [1, 1, 0, 0]              head D_4 = 1
      L^1 minus the step-2 head = [4,2,2,2,2]:  contains an entry >= 4
         => the PRE-R1 exclusion "no entry >= 4" is FALSE here
         but contains no entry EQUAL to Z = 5  => the R1 exclusion HOLDS.

T7  K_{3,5}   d = [5,5,5,3,3,3,3,3]   n=8  m=15
      L^0 = [5,5,5,3,3,3,3,3]   head D_1 = 5
      L^1 = [4,4,3,3,2,2,2]     head D_2 = 4      (again an entry >= 4 survives)
      L^2 = [3,2,2,2,2,1]       head D_3 = 3
      L^3 = [2,1,1,1,1]         head D_4 = 2
      L^4 = [1,1,0,0]           head D_5 = 1

T8  K_{2,3} (Corollary N2's counterexample, tau = 2)   d = [3,3,2,2,2]  n=5  m=6
      L^0 = [3,3,2,2,2]   head D_1 = 3
      L^1 = [2,2,1,1]     head D_2 = 2
      L^2 = [1,1,0]       head D_3 = 1
      L^3 = [0,0]
      D = (3,2,1)  s = 3  residue = 2 = alpha-1,  tau = 2 so s != tau
      => exactly the regime where Lemma F3 as stated is unavailable (R2's point).

T9  k=3 with Y = Z = 4, where the tie makes case (i) of the R1 argument live
    d = [4,4,4,3,3,3,1]   n=7  m=11
      L^0 = [4,4,4,3,3,3,1]  head D_1 = 4
      L^1 = [3,3,3,2,2,1]    head D_2 = 3
      L^2 = [2,2,2,1,1]      head D_3 = 2
      L^3 = [1,1,1,1]        head D_4 = 1
      L^4 = [1,1,0]          head D_5 = 1
    labelled run, tie-break PREFERRING A-entries:
      step 1: head = x (4), block = [y, z, a1, a2]
      step 2: head = a3 (3)  <-- H_2 IS an A-entry: case (i) is reachable
              block = [y, z, a1]
      step 3: head = a2 (2), step 4: head = a1 (1), step 5: head = y (1)
    labelled run, tie-break PREFERRING B-entries:
      step 1: head = x (4);  step 2: head = y (3)  <-- case (ii)
    Both give the SAME head multiset D = (4,3,2,1,1). Consistent with case (i)'s
    claim: y and z both enter L^2 with value 2, so L^2 has >= 2 entries >= 2 (it
    has three), which is what the repaired argument uses.
```

Tie-break invariance was checked systematically: 1 062 random graphical
sequences × 4 adversarial label permutations each — the head sequence
`D₁…D_s` (hence `residue`) changed **0** times. Only the *identity* of the head
and of the decrement block moves, never the multiset — which is why the text's
case split on "who is `H₂`" is the right way to handle ties, and why it must be
exhaustive over labels (it is).

---

# (f) What I could NOT check

1. **Fact 2** (`residue ≤ α`, Favaron–Mahéo–Saclé / Griggs–Kleitman) is cited,
   not proved, and I have no web access. I verified it numerically on every
   graph I generated (0 failures over >126 000 hard-core instances and all
   n = 7 graphs), but the attribution — which the text itself flags as "from
   memory" — remains unverified. T3 depends on it twice (to get `residue = α`
   from `residue ≥ α`, and for `s ≥ τ`).
2. **Lemma 5, Theorem 6, Theorem 7, Corollary B1, Theorem A/B2** are outside the
   T3 block; I did not audit their proofs. T3 does not use Lemma 5.
3. **§7.5 / §7.6** (Lemma Z⁺, Lemma DICH, Theorem K, Corollary K1, Theorem MB,
   Proposition L2, Theorem SL) are the K-chain target, not T3. I verified R2's
   Lemma F3′ statement and proof but not Z⁺ or DICH themselves.
4. **The Lean-level reduction** (that the Mathlib goal is equivalent to (C61),
   and that `residueAux` is faithfully transcribed) I took from appendix A. My
   confidence rests only on the two calibration facts I could reproduce
   (`residue(K₂) = 1`, `residue(Cₙ) = ⌈n/3⌉`), plus `residue(Kₙ) = 1` and
   `residue(star) = n−1`, plus the `residue = n − s` identity.
5. **Completeness of the refutation search beyond n = 37.** S2 is exhaustive for
   every τ = 3 graph on n ≤ 37; S3 covers the multiplicity box `≤ 10` (n ≤ 73);
   S4 covers 140 support patterns with multiplicities up to ~3·10⁵ on a ladder
   and at random. That is not literally every τ = 3 graph at every n. A
   counterexample, if one existed, would need a `(G[B], support)` shape whose
   quotient diameter is 4 and multiplicities outside all of the above.
6. **The author's scripts and their outputs** (`w61_tau3.py`, `w61_lemH.py`,
   `w61_r3_repair.out`, `w61_r4_a2check.out`, …) — forbidden by the isolation
   rule and not consulted. Every count in this report is mine. Where the brief
   quotes a number I recomputed the corresponding fact independently rather
   than checking the number (e.g. R3's "726/726" I replaced with my own
   32 800/32 800 over a wider parameter range; R1's `[5,5,5,3,3,3,2]` and
   `K_{3,5}` L¹ values I recomputed and they agree).
7. **Isomorphism-class counts.** My enumerations are over `(G[B], μ)` pairs, not
   isomorphism classes, so cell counts in §(d) over-count by the order of the
   `G[B]`-automorphism action; this affects only the reported cardinalities,
   never the 0-failure verdicts.
