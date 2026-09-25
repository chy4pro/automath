VERDICT: PARTIAL — the FAN chain's mathematics (FAN-1…FAN-8, Theorem FAN, Corollary FAN-HC) survives every attack I made and I could not refute it, but repairs K and L leave six confirmed defects, five BOOKKEEPING and one MATHEMATICS, none of which touches the conclusion.
TEXT VERSION REVIEWED: `prompts/w61_S3_FAN_B.md`

**My verdict line is BOOKKEEPING-driven.** The single mathematics defect (D5, Lemma T′) is
real but sits in an unused toolkit lemma. Every load-bearing mathematical step of the FAN
chain checked out.

Scale used per joint: **CLEAN** = attacked, no defect found; **PARTIAL** = confirmed
defect(s), conclusion unaffected; **GAP** = something the text asserts is not established;
**REFUTED** = counterexample.

All figures below are from my own implementation (`hh.py` / `fan.py` in my scratch
directory), written from the appendix-A spec and calibrated before use:
`residue(K₂) = 1`; `residue(Cₙ) = ⌈n/3⌉` for n = 3…9 — 8/8. **No number printed in the
brief is reused anywhere in this report.**

---

## (a) Bookkeeping table B-J1 … B-J6

| joint | verdict | finding |
|---|---|---|
| **B-J1** attribution sweep | **PARTIAL** | Repair **G1 is correct** — it is the right diagnosis and the right replacement text, and I rebuilt its witness independently (`Fan(4,2)`, `A′=[2,2]`, `deg = [5,5,4,4,4,2,2]`: my code gives `s = 5 = τ+1`, `residue = 2 = α−1`, `α = 3` — matches). But **it is not the only such sentence**: see **D3**. The whole numerical apparatus of §7.8 (A's `M1…M4`, E's `H1…H5`, F's counts) is measured on runs where `s = τ+1`, i.e. where the reductio — the standing hypothesis of *every* FAN lemma — is false, and §7.8 never says so, although §7.6 G supplies exactly that firewall for the identical situation. |
| **B-J2** orphan sweep | **CLEAN** | I checked all six named sites plus four more; **no statement anywhere in H/K/L still depends on `residue = α−1` / `s = τ+1` exactly.** Sites checked, all clean: (1) §7.8 E's four-row case table — its "clears in" column is a pure computation on the step-`p+1` multiset, not a claim about the true `s`; I recomputed every entry (table in (f)) and all four rows are right for `L = 2…30`. (2) §7.8 G's `GFan` LEAD: I re-derived both displayed counts independently — `Σ_{x∈B_hi} deg_B(x) = p(τ−1) − 2ν` ⟹ `dec_{A′} = R − 2ν + E` ⟹ `A′` total `= 2ν − E`, and FAN-8's inequality re-run gives `τ−t+1 ≤ (2ν−E) + (p−t+1)` i.e. `L ≤ 2ν−E`. Both correct, both reductio-internal, neither uses the withdrawn value. (3) **Lemma FAN-3's statement and proof**: the "it terminates at step `τ+1`" half is a genuine unconditional consequence of the multiset hypothesis (verified for `L = 2…30`, and with 0…4 trailing zeros), so it is not an orphan; the one ex-falso clause was in its proof and **G2 correctly deletes it**. (4) **Corollary FAN-HC** consumes only Theorem FAN's *first* sentence — verified line by line. (5) Observation FAN-5, (6) §7.8 A's "Numerical verdict", (7) §7.8 A's "Mechanism check", (8) §7.8 E's "Enlarged box", (9) §7.8 E's residual paragraph, (10) §7.8 F's "Chain of dependence" — all report measurements as measurements. |
| **B-J3** status-line audit | **PARTIAL** | I verified **G3's diagnosis of FAN-2 independently and it is correct** (details under B-J6). But the sweep is incomplete twice over. **D1:** §7.8 A's own status paragraph — "*Lemma FAN-1, FAN-2 (for `j ≤ min(p,L+1)`) and FAN-3 are PROVED here*" — still carries FAN-2 at PROVED; G3(2) names only "*Section H part E's status line*". **D4:** §7.8 E's status line also lists **Observation FAN-5** as PROVED, but FAN-5's second half is supported in the text only by "*Verified by direct simulation for `L = 2…8`*". Every other status line in H/K/L is correct as of section L (§7.8 C's gate note, §7.8 F's, §7.8 G's "LEAD, not proved", K's and L's closing lists). |
| **B-J4** scope labels | **PARTIAL** | **D2:** repair **F3 itself mis-scopes two statements.** F3 asserts "*Theorem LOW, Theorem SL, Theorem MB, Proposition L1/L2, Corollaries SL-HC and FAN-HC live in the **hard core***", but Theorem LOW is stated "*Under `residue(G) = α(G)`*" and Theorem SL "*Assume the reductio hypothesis … and `τ ≥ 2`*" — **neither needs connectivity, non-forest, `diam = 4`, `f = α+1` or `τ ≥ 4`.** Their proofs use only Lemma 1(2), Lemma HI and DICH. So F3's closing "*with that reading every statement in §7.6/§7.8 is correctly scoped*" is false for those two, and it is a fresh instance of exactly the **D3 species** that section J records and that F5 says repairs F1–F3 are supposed to be the foundation for. **D7 (minor, outside H/K/L but named by F3):** Lemma C\*'s own hypothesis line still reads "*Assume the hard core (G connected, `f = α+1`, diam = 4)*" — under F3 that phrase now means frame **plus** `residue = α`, which C\* does not use, and the parenthetical also drops "non-forest". G5(i) renamed the two *corpora* but not this. **No stale `τ ≥ 3` survives anywhere in H/K/L** (the only one, in Corollary SL-HC, is in section F and is what G5(ii) fixes). Per-statement frame requirements are tabulated under (d)/D2. |
| **B-J5** citation-scope audit | **CLEAN** | Every citation in section H is of a form actually available at its call site. Checked: FAN-1 (DICH(b), DICH(c) — both general-`s`, applied at `s = τ`); FAN-2 (DICH(b) + FAN-1, reductio-only, and **F2 correctly adds the marker**); FAN-3 (cites nothing reductio-only — monotonicity of head values, i.e. Lemma 1(2)); FAN-4 (DICH(b), FAN-1); FAN-6 (DICH(b), FAN-4, block-prefix); FAN-7 (FAN-4's count + Lemma 1(2) for non-graphicality); FAN-8 (FAN-1, DICH(b), FAN-7's count); Theorem FAN; Corollary FAN-HC (Theorem K, R1, Cor L1-short, Prop L2, T3). **No reductio-only form is used at a point where the reductio has been refuted**, and no general-`s` form is credited with more than it gives — G4 is right that F1's "*Lemma S does not fire*" was the wrong diagnosis and that S′ fires vacuously; I confirmed numerically that on the `Fan(4,2)` witness S′'s threshold `s+1 = 6` exceeds `Δ = 5`, so it fires on **0** vertices. *Terse-but-correct (not scored a defect):* FAN-1's proof applies DICH(b) to "the remaining high vertices" without first citing Lemma S / Lemma HI to establish that they are heads at all; the citation is available (`deg ≥ τ+1 = s+1`) but is not made. |
| **B-J6** repairs and new lemmas | **GAP** | **G1 correct** (witness rebuilt and reproduced). **G2 correct** — FAN-3's hypothesis is only ever *derived* under the reductio, so identifying its `s = τ+1` with the real `s` is precisely the F1(ii) inference; deletion is the right repair, and the parenthetical replacement is honest. **G3 correct but incomplete** — diagnosis verified independently: at `j = L+1` we have `p = τ − j + 1` exactly, so an `A′` entry can tie with a `C`-entry and a prefix-block can take the `A′` entry and leave the `C`-entry out; with `q` such `A′` entries the proof needs `D_j ≥ (p−j)+(L+1)+q` and supplies `D_j ≥ τ−j+2 = (p−j)+(L+1)+1`, i.e. exactly `q ≤ 1`. For `j < L+1` the inequality is strict and the step is airtight. (My own measurement: over 1 328 176 labelled Fan runs the observed `q` at `j = L+1` was **0** every time — so the hole is real but never bites in the box.) Incompleteness = **D1**. **G4 correct** and a genuine improvement. **G5 correct but incomplete** (**D7**). **Lemma S′: correct** — the proof is genuinely general-`s` (a survivor drops by at most one per step under `max(x−1,0)` and must be 0 after `s` steps); 0 failures over all 6 058 graphical sequences on `n ≤ 9` and 2 094 labelled random runs, 1 137 of them with `s ≠ τ`. **Lemma T′: the "only if" direction is FALSE as stated — D5.** **"H′ is subsumed by DICH" is TRUE**, and I re-derived why: for `g ≤ s`, DICH(c) gives `D_i ≤ s−i+2 ≤ s−i+2+h_i` (strictly stronger, and hypothesis-free); for `g ≥ s+1`, DICH(b) forces `h_i = i−1`, which **contradicts H′'s hypothesis `h_i ≤ i−2`**, so H′ is vacuous there. Subsumption holds, but by vacuity on the high branch — worth stating, since it means H′ never executes (see (e)). **Closure claim:** true for the four tools as re-derived (F3′ ✓, S′ ✓, T′ first sentence ✓ modulo D5, H via DICH ✓; T′'s second sentence needing Fact 2 is correctly flagged — the route is `s ≠ τ` plus `s ≥ τ` from Fact 2, giving `residue ≤ α−1`). **But "All four tools of §7.2 B" undercounts (D6):** §7.2 B contains **seven** boxed statements — Lemma S, Lemma T, Lemma F3, Lemma H, **Theorem N, Corollary N1, Corollary N2**. I checked the three extra ones and the closure claim survives on them (N/N1 are conditionals whose proofs run the reductio internally; N2 is genuinely reductio-scoped and *cannot* be generalised — its own `K_{2,3}` counterexample shows why, which I reproduced: `α = 3`, `τ = 2`, but my code gives `s = 3`, heads `(3,2,1)`, `residue = 2 = α−1`). So there is no *fifth tool where the claim fails*, but the count is wrong. |

---

## (b) Mathematics table M-J1 … M-J6

| joint | verdict | finding |
|---|---|---|
| **M-J1** FAN-1 | **CLEAN** | The tie-break-invariance step is **true, and in fact stronger than the text needs**: `residueAux` is defined on a *sorted list*, so the whole value-multiset trajectory — and hence `s` — is a function of the degree multiset alone, for *any* tie-break, both when two maxima compete for headship and when two equal entries straddle the block boundary. So "we may fix the tie-break" is licensed. Small stylistic point: the text says "fix the tie-break" but the argument actually chooses adaptively at each tie; that is still valid, because invariance holds step-by-step. The induction **does** give "the first `p` heads are exactly `B_hi`": at step `j ≤ p` at least one high vertex survives, is a head (Lemma S, `deg ≥ τ+1 = s+1`), lies in every earlier block (DICH(b)), hence has value `g − (j−1) ≥ τ−j+2`, so `D_j ≥ τ−j+2`; a low head would need `D_j ≤ τ−j+2` (DICH(c)), so equality and a tie, resolved to the high vertex. At `j = 1` there is not even a tie: DICH(c) gives `D_1 = g ≤ s = τ < τ+1`. Since `|B_hi| = p`, the first `p` heads are exactly `B_hi`. Sound. |
| **M-J2** FAN-4 | **CLEAN** | The three recipient classes are **exhaustive and disjoint**: `V = B_hi ⊔ C ⊔ A′` with `C = B_lo ∪ {a₀}`, `A′ = A∖{a₀}` — nothing is left over, and no entry is double-counted (`a₀` is in `C`, not `A′`). `Σ_{j≤p} D_j = Σ_{B_hi} deg − C(p,2)` is right: DICH(b) gives `D_j = g_j − (j−1)` exactly and `Σ_{j=1}^{p}(j−1) = C(p,2)`. `Σ_{x∈B_hi} deg_B(x) = 2(τ−2) + (p−2)(τ−1) = pτ − p − 2 = p(τ−1) − 2` — I recomputed it and it is right for `G[B] = K_τ − uv` with `u,v ∈ B_hi` (and the `GFan` version `p(τ−1) − 2ν` is right when all `ν` non-edges sit inside `B_hi`). The cancellation is exact: `pτ − p(p−1) − p(L+1) = 0` because `τ = p + L`, giving `dec_{A′} = R − 2` and residue `2`. No ℕ-truncation risk (Lemma 1(2), the sequence stays graphical), and `C`-entries stay `≥ L ≥ 2 > 0` throughout the high phase so no decrement is absorbed by a zero. |
| **M-J3** FAN-6 | **CLEAN** | The invariant propagates in both branches, and both branches are **tie-safe**, which I checked separately. `a_j < μ`: the block's `A′` part is a top-prefix, so if one copy of the max `w` is left outside then *every* block `A′` entry equals `w`; all `a_j ≥ 1` of them land at `w−1`, `max` does not drop so `w = v`, and `v−1` appears in `M_{j+1}` — contradiction. `a_j ≥ μ`: no copy of `w` can be outside (else `μ > a_j`), so all drop, `max(M_{j+1}) = w−1 = v`, uniqueness forces `μ = 1`; and no *other* entry of `M_j` can map to `v` (that would break uniqueness), so all others are `≤ max(other entries of M_{j+1}) + 1`. The chain `M_{p−t}` = (max `3+t`, others `≤ t+1`) is self-sustaining because `t+1 < t+2 = v−1` always, so the induction never stalls, and `max(M_1) = p+2 > p ≥ max(A′ degrees)` closes it. It **correctly fails** for the `1+1` residue, and **for the reason F4 gives, not the original one**: `[1,1]` has maximum 1 of multiplicity 2, so the induction's uniqueness premise fails at step 0. I confirmed F4's sub-case: with `|A′| = 2` there are no zero entries at all, so the withdrawn "`v−1 = 0` is present as the zero entries" is simply false there; and section L's standing fact `|A′| ≥ 2` (`R ≥ p+2 > p ≥ max A′ degree`, so one `A′` vertex cannot carry `R`) is correct, so the sub-case is an infinite subfamily, not a corner. |
| **M-J4** FAN-7 | **CLEAN** | `E ≤ 2` is immediate and right: re-running FAN-4's count with `dec_C = p(L+1) − E` gives `dec_{A′} = R − 2 + E`, hence `A′` residue `= 2 − E ≥ 0`. The non-graphicality step is right and I verified it computationally for `L = 2…11`: at the start of step `p+1` the `E = 2` shapes are `[L+2, L^L]` and `[L+1, L+1, L^{L−1}]` on `L+1` `C`-entries with all `A′` entries at 0, so the number of **positive** entries after the head is `L`, while the head is `L+2` resp. `L+1` — truncation in both, impossible by Lemma 1(2). The case list is complete: `E ≥ 3` is excluded by `2−E ≥ 0`, and for each `E ∈ {0,1,2}` the partitions of `2−E` are exhausted. |
| **M-J5** FAN-8 | **CLEAN** | (i) `|block_t ∩ A′| = D_t − (p−t) − (L+1) + e_t ≥ (τ−t+2) − (p−t) − (L+1) + 1 = 2` — I recomputed the algebra, it collapses to exactly `τ − p − L + 2 = 2`, with `e_t ≥ 1` the only input. Slack test: this is **tight**, not slack ≥ 2, and the text uses only "`≥ 2`, so some `x ∈ A′` exists", i.e. it uses less than it proves — safe. (ii) `x` surviving steps `t…p` **is** established, and by the right thing: Lemma FAN-1 says every head of steps `1…p` is a `B_hi` vertex, so no `A′` entry is deleted in that range; hence `x` loses at most one per step over the `p−t+1` steps `t…p`, giving `v_{p+1}(x) ≥ v_t(x) − (p−t+1)`. Combined with `v_t(x) ≥ v_t(c) ≥ τ−t+1` (prefix domination, `c ∉ block_t`, `c` decremented at most `t−1` times from degree `τ`) and `v_{p+1}(x) ≤ 2−E ≤ 1`, this yields `τ ≤ p+1`, i.e. `L ≤ 1`. No circularity: FAN-8 uses FAN-7's *count*, and FAN-7 uses FAN-4's counting method; neither uses FAN-6 or FAN-8. |
| **M-J6** FAN-HC / L2 | **CLEAN** | Proposition L2 **does** supply every clause of the `Fan(τ,L)` definition at `L = 2`. Clause by clause: `B_lo` = 2 B-universal vertices — L2(a),(b); `deg_A(b_i) = 1` with a common `a₀` adjacent to all of `B` — L2(c); `G[B] = K_τ − uv` with `u,v ∈ B_hi` — L2(d); `deg(w) ≥ τ+1` for `w ∈ B_hi` — definitional; `p = τ−2 ≥ 2` — from `u,v ∈ B_hi` and `τ ≥ 4`; `deg(c) = τ` for `c ∈ C` — `(τ−1)+1` for `b_i`, `τ` for `a₀`. And the clause the joint singles out — "**every `A`-vertex other than `a₀` attaches only inside `B_hi`**" — **is** supplied, exactly as the text says: `deg_A(b_i) = 1` with `a₀` the unique `A`-neighbour means no other `A`-vertex is adjacent to `b₁` or `b₂`, so `N(a) ⊆ B ∖ B_lo = B_hi` for every `a ∈ A′`. I also re-derived L2 itself from Theorem MB and found its algebra correct (`|B_lo⁺| + c + m̄ ≤ 1 + ν(B_lo)`; the (F-b) contradiction in (a) and (b); `Σ_{B_lo} deg_A = 2` in (c) from `2L + ν(B_lo) − 1 = 3` and `m̄ = 1`; slack `= 2(τ+1) − (2τ+1) = 1` in (e)). The `L ≥ 3` arithmetic of FAN-HC (`L=0` Theorem K + R1, `L=1` Cor L1-short, `L=2` L2 + Theorem FAN) has no off-by-one. |

---

## (c) Refutation attempt — box, code, result

**Code.** `hh.py` (residueAux transcription: sorted-descending list, delete head `D`,
`max(v−1,0)` on the next `min(D, len)` entries, re-sort; stop when the head is 0 and return
the length) and `fan.py` (labelled variant carrying vertex classes `Bhi / C / Ap`, with an
adversarial tie-break that randomly permutes each equal-value group before the prefix is
taken). Calibrated on `residue(K₂)=1` and `residue(Cₙ)=⌈n/3⌉`, `n = 3…9`, before use.
Cross-checks that came out right independently: `residue(K_{2,3}) = 2` with `s = 3 ≠ τ = 2`;
`residue([3,3,3,3,3,2,1]) = 3` with `s = 4`, so `n−s = 3 ≠ α = 4`; `residue(K₆) = 1`;
`residue(Petersen) = 3`.

**Box searched.** All `Fan(τ,L)` degree sequences with

* `4 ≤ τ ≤ 9`, `L ≥ 2`, `p = τ − L ≥ 2`;
* `d_u, d_v ≥ 2` and `d_w ≥ 1` for the `p−2` vertices of `W` (forced by `deg ≥ τ+1`);
* `R = Σ_{x∈B_hi} d_x ≤ 14`, `2 ≤ |A′| ≤ 10`;
* the `A′`-degree partition constrained to parts `≤ p` **and** Gale–Ryser-realizable
  against `(d_x)_{x∈B_hi}` (so every sequence I counted is genuinely realizable as the
  bipartite `A′ ↔ B_hi` attachment of a Fan graph).

**Result — 332 044 instances; 1 328 176 labelled runs (canonical + 3 randomised
adversarial tie-breaks each).**

```
L histogram of instances : {2:164599, 3:103105, 4:47322, 5:14341, 6:2482, 7:195}
alpha - residue          : {1: 332044}          <- 0 survivors, and never 0 or >=2
s = tau+1                : 332044 / 332044      <- 0 violations
M1 (first p heads = B_hi): 0 failures / 1328176
E (C-escapes, high phase): {0: 1328176}         <- E >= 1 never occurred
q (#A' entries at/above the C-value at step j = L+1) : {0: 1328176}
state at start of step p+1 = [L]^(L+1) + A' residue (1,1) : 1328176 / 1328176
```

**Empty.** I did not refute anything. Per the brief I report the box rather than claiming
to have out-enumerated prior effort; my box is smaller than the text's and my marginal
value was in the sweep. Two honest observations about what this box *can* say:

1. It cannot test FAN-1/2/4/6/7/8 **as stated**, because every run in it has `s = τ+1`, so
   the reductio hypothesis of all of them is false throughout. It tests off-reductio
   analogues. (This is D3.)
2. The `q = 0` column is the direct measurement of the hole G3 identifies: the tie at
   `j = L+1` that FAN-2's proof does not cover never actually materialised, which is
   consistent with G3's "impact: none".

---

## (d) Defects

### D1 — §7.8 A's status line still carries Lemma FAN-2 at PROVED. **BOOKKEEPING.**

> **Quoted (section H, §7.8 A, "Status."):** "`Fan(τ,L≥2)` is **eliminated from the hard core conditionally on one step**: Lemma FAN-1, FAN-2 (for `j ≤ min(p,L+1)`) and FAN-3 are PROVED here"

> **Quoted (section L, G3 part 2):** "**Section H part E's status line must stop listing FAN-2 as PROVED.**"

*Why it fails.* G3 establishes — correctly — that FAN-2's proof is tie-incomplete at
`j = L+1`, so FAN-2 is not PROVED. It then names **one** site. §7.8 A's status paragraph is
a second site of the identical species and is not repaired. A reader following section L's
supersession rule can recover the right status from L's closing list ("*Lemma FAN-2: no
longer claimed PROVED*"), but G3's own wording asserts a completed sweep that is not
complete — which is the exact defect species the brief says this document keeps producing.

*Smallest configuration exposing it.* None needed; it is a textual inconsistency between
two status lines in the same document. The mathematical content it mis-states is exposed by
any Fan instance whose high phase reaches step `j = L+1` with two `A′` entries at value `p`.

*Repairable:* **yes**, one clause ("and FAN-2 (for `j ≤ min(p,L+1)`)" struck from §7.8 A's
status line, or G3(2) reworded to "every status line in §7.8").
*Does the CONCLUSION survive:* **yes.** FAN-2 is cited by nothing; FAN-8 proves `E = 0`
unconditionally without it. I verified there is no path from FAN-2 to Theorem FAN.

---

### D2 — Repair F3 assigns Theorem LOW and Theorem SL to the wrong frame. **BOOKKEEPING.**

> **Quoted (section K, amendment F3):** "Claimed: Lemma 4, Lemma C\*, Observation R1 and (F-b) hold in the **frame**; **Theorem LOW, Theorem SL**, Theorem MB, Proposition L1/L2, Corollaries SL-HC and FAN-HC live in the **hard core**; with that reading every statement in §7.6/§7.8 is correctly scoped."

*Why it fails.* Theorem LOW is stated "**Under `residue(G) = α(G)`**" and Theorem SL
"**Assume the reductio hypothesis `residue(G) = α(G)` (so `s = τ`) and `τ ≥ 2`**". Neither
statement, and neither proof, uses connectivity, non-forest, `diam = 4`, `f = α+1` or
`τ ≥ 4`. Theorem LOW's proof uses Lemma 1(2), Lemma HI (which needs only that `A` is a
maximum independent set) and DICH(b)/(c); Theorem SL's proof uses DICH, F3′ and Lemma 1(2)
and nothing else. Under F3's own canonical definitions, "hard core" = frame + reductio
(+ `τ ≥ 4`), so F3 declares both inside four hypotheses they never use. This is precisely
the **D3 species** recorded in section J ("*Lemma C\* is declared inside a reductio it never
uses*"), reintroduced inside the repair that F5 says the scope discipline now rests on:
"*The scope discipline of §7.6/§7.8 rests on Repairs F1–F3, not on that audit.*"

*Smallest configuration exposing it.* Any graph with `residue = α` and `diam ≠ 4` — e.g.
`C₅` (`α = 2`, `τ = 3`, my code: `s = 3 = τ`, `residue = 2 = α`, `diam = 2`). Theorem LOW
and Theorem SL both apply to it and are both true on it; F3's reading says they do not
apply.

*Repairable:* **yes** — move Theorem LOW and Theorem SL into a third bucket
("reductio only, no frame"). *Does the CONCLUSION survive:* **yes.** This is
over-hypothesisation (the safe direction): §7.6/§7.8 only ever *apply* LOW and SL inside
the hard core, so no false conclusion follows. The cost is the one section J already priced
— a Lean pass transcribing declared hypotheses would carry four spurious hypotheses into
LOW and SL and fail to discharge them.

---

### D3 — §7.8's numerical blocks are measured off the reductio, with no firewall; G1 repairs only one of them. **BOOKKEEPING.**

> **Quoted (section H, §7.8 A, "Mechanism check"):** "64 911 labelled HH runs … M1 'the first `p` heads are exactly `B_hi`' — 0 failures; M2 … — 0 failures; M3 … — 0 failures … M4 `s = τ+1` — 0 failures."

> **Quoted (section H, §7.8 E, "Numerical status"):** "over **508 239** high-phase runs … **all five structural hypotheses of Lemma FAN-6 hold with 0 failures**"

*Why it fails.* `M4` states that every run in those corpora has `s = τ+1`. The standing
hypothesis of Lemma FAN-1, FAN-2, FAN-4, FAN-6, FAN-7 and FAN-8 is `residue = α`, i.e.
`s = τ`. So **the reductio is false in every measured run**, and none of these numbers can
confirm or refute those lemmas as stated; they confirm off-reductio analogues that the text
nowhere states or claims. My own box makes the point sharply: all 1 328 176 of my labelled
runs have `s = τ+1`, so `M1`-type agreement is agreement about something the lemma does not
say. §7.6 G supplies exactly the right disclosure for exactly this situation — "*statements
about the hard core **with** the reductio, which is conjecturally empty — so they cannot be
falsified numerically as composite statements; any direct test passes vacuously. What can
be tested is each **ingredient** separately*" — and §7.8 carries no such paragraph. Repair
**G1** fixes the one sentence that re-attributes the *residue value*, and leaves the
*mechanism* attributions untouched; so the answer to B-J1's "check it is the only one" is
**no**.

*Smallest configuration exposing it.* `Fan(4,2)` with `A′ = [2,2]`: my code gives `s = 5`,
`τ = 4`, so `residue = α` is false — yet this instance is inside the measured corpus and is
counted as an `M1` success.

*Repairable:* **yes** — one firewall paragraph in §7.8, on the §7.6 G model, restating the
`M`- and `H`-checks as ingredient checks. *Does the CONCLUSION survive:* **yes.** Theorem
FAN is a reductio and needs no numerical support; the numbers were never load-bearing.

---

### D4 — Observation FAN-5 is listed PROVED but half of it is only simulated. **BOOKKEEPING.**

> **Quoted (section H, §7.8 E, Status):** "*Lemmas FAN-1, FAN-2, FAN-3, FAN-4, FAN-6, FAN-7 and **Observation FAN-5** are **PROVED***"

> **Quoted (section H, §7.8 D, Observation FAN-5):** "the multiset `[L]^{L+1}, 1, 1` clears in `L+1` Havel–Hakimi steps (Lemma FAN-3), but `[L]^{L+1}, 2` clears in exactly `L` steps. **Verified by direct simulation for `L = 2…8`**"

*Why it fails.* The first half is Lemma FAN-3 (proved). The second half — "`[L]^{L+1}, 2`
clears in exactly `L` steps" — is asserted **for every `L ≥ 2`** but supported only by
simulation up to `L = 8`. A statement whose only warrant is a finite simulation is not
PROVED. (The claim is *true*: I checked `L = 2…30` with 0 failures, and it has a two-line
induction — one step sends `[L]^{L+1}, 2` to `[L−1]^L, 2`, down to `[2,2,2,2]` after `L−2`
steps, which clears in 2 — but the text does not give it.)

*Smallest configuration exposing it.* `L = 9`, the first value outside the simulated range.

*Repairable:* **yes**, by adding the induction or by demoting FAN-5 to "numerical".
*Does the CONCLUSION survive:* **yes.** FAN-5 is motivational; the single-`2` case is killed
by Lemma FAN-6, not by FAN-5's step count.

---

### D5 — Lemma T′'s "only if" direction is false as stated. **MATHEMATICS.**

> **Quoted (section L, addendum):** "**Lemma T′ (terminal shape, general `s`).** For every `k ≥ 1`, the run has exactly `k` steps **iff** the list at the start of step `k` is `[D_k, 1^{D_k}, 0^…]`. *Proof.* Verbatim the proof of Lemma T: the last step deletes a head of value `D_k` and decrements the `D_k` entries after it, and the result is all-zero **exactly when** those entries were `1` and the rest `0`. ∎"

*Why it fails.* The "⟸" direction is fine. The "⟹" direction is not. Terminating at step `k`
requires only that `max(r_i − 1, 0) = 0` for the `min(D_k, ·)` decremented entries and
`r_i = 0` beyond them — i.e. the list is `[D_k, 1^a, 0^…]` with `a ≤ D_k`, **not**
`a = D_k`. Forcing `a = D_k` needs `D_k ≤ #{positive entries after the head}`, which is
exactly the no-ℕ-truncation fact of **Lemma 1(2)** and holds only because the list is the
degree sequence of a graph. T′ is stated for "the run" with the word *any* generality in its
title ("general `s`") and its proof asserts "exactly when" without that input. This is the
mirror image of the defect species G4 and R2 were repairing: not "stated more narrowly than
its proof", but **stated more broadly than its proof**, in a lemma newly added by the repair
set under review.

*Smallest configuration exposing it.* `[4,1,1,0,0,0]`: my code runs it in exactly **1** step
(head 4, the two 1s and two 0s are decremented, everything becomes 0), yet the list is not
`[4, 1^4, 0^…]` — only two 1s follow the head. `[2,1,0,0]` is a 4-entry witness. Both are
non-graphical, which is the point: I verified T′ over **all 6 058 graphical sequences on
`n ≤ 9` with 0 failures**, so within the document's standing convention (labelled HH on
`d(G)`) the lemma is true.

*Repairable:* **yes**, trivially — add "for the degree sequence of a graph" or cite Lemma
1(2) in the "only if" direction.
*Does the CONCLUSION survive:* **yes.** Lemma T′ is recorded for the toolkit-closure claim
and is cited by nothing in the FAN chain (Lemma T is used only in §7.3 5bis, outside this
target).

---

### D6 — "All four tools of §7.2 B" undercounts §7.2 B. **BOOKKEEPING.**

> **Quoted (section L, Closure claim):** "**All four tools of §7.2 B** are now general-`s` … so **no tool of §7.2 B is stated more narrowly than its proof**."

*Why it fails.* §7.2 B contains **seven** boxed statements: Lemma S, Lemma T, Lemma F3,
Lemma H, **Theorem N**, **Corollary N1**, **Corollary N2**. The closure claim quantifies over
"tools of §7.2 B" but audits only four of them, so as written it is an unaudited universal.
I checked the other three and the *claim itself survives*: Theorem N and Corollary N1 are
conditionals concluding `residue ≤ α−1` whose proofs run the reductio internally (both
implicitly needing Fact 2 to upgrade `residue ≥ α` to `residue = α` — the D2-species point,
and §7.2 B's convention block does name Fact 2); Corollary N2 is genuinely reductio-scoped
and cannot be generalised at all, as its own `K_{2,3}` witness shows (I reproduced it: `α=3`,
`τ=2`, `s=3`, heads `(3,2,1)`, `residue = 2`). So: **no fifth tool where the claim fails**,
but the quantifier is wrong.

*Repairable:* **yes** — say "all four *Havel–Hakimi tools*" and note N/N1/N2 separately.
*Does the CONCLUSION survive:* **yes.**

---

### D7 — G5's stale-label sweep misses Lemma C\*'s own hypothesis line. **BOOKKEEPING (minor).**

> **Quoted (section D, §7.4 C):** "**Lemma C\* (τ-uniform).** Assume **the hard core** (G connected, `f = α+1`, diam = 4)."

*Why it fails.* Under F3, "hard core" = frame + `residue = α` (+ `τ ≥ 4`), while the
parenthetical expands it as three conditions with no reductio **and no "non-forest"** — so
the sentence names the wrong term *and* mis-expands it. F3 itself asserts "Lemma C\* … hold[s]
in the **frame**", and G5(i) renamed the §7.4 D and §7.6 C *corpora* but not this hypothesis
line. Its proof needs only Lemma 4, (F-b), and `f = α+1` — i.e. less than the frame, so the
statement is fine mathematically.

*Repairable:* **yes**. *Does the CONCLUSION survive:* **yes** (over-labelling only). Strictly
this site is in section D, not H/K/L, so it is outside B-J4's literal sweep — I record it
because F3 explicitly claims to have fixed the term everywhere.

---

**Defect classification summary.** BOOKKEEPING: D1, D2, D3, D4, D6, D7. MATHEMATICS: D5.
**The verdict line is BOOKKEEPING-driven.** No defect of either class threatens Theorem FAN
or Corollary FAN-HC.

---

## (e) Control cases / counterfactual availability (T12)

Five control instances, run through my labelled implementation. For each, every lemma the
text treats as available in the FAN chain, with (i) do its hypotheses genuinely hold,
(ii) what does it yield, (iii) which hypothesis fails.

| control | `n` | `τ` | `α` | `s` | `residue` | reductio `s = τ`? |
|---|---|---|---|---|---|---|
| (a) `Fan(4,2)`, `A′=[2,2]`, `deg=[5,5,4,4,4,2,2]` | 7 | 4 | 3 | 5 | 2 | **NO** (`s = τ+1`) |
| (b) `Fan(4,2)`, `A′=[2,1,1]`, `deg=[5,5,4,4,4,2,1,1]` | 8 | 4 | 4 | 5 | 3 | **NO** (`s = τ+1`) |
| (c) `K_{2,3}`, `deg=[3,3,2,2,2]` | 5 | 2 | 3 | 3 | 2 | **NO** |
| (d) `C₅`, `deg=[2,2,2,2,2]` | 5 | 3 | 2 | 3 | 2 | **YES** |
| (e) `K₆`, `deg=[5,5,5,5,5,5]` | 6 | 5 | 1 | 5 | 1 | **YES** |

Availability, lemma by lemma:

* **Lemma 1(1)(2)** — hypotheses hold on all five (graphical sequences). Yields `residue = n−s`
  and `ΣD_i = m`: checked on (a) `7−5 = 2` ✓, (b) `8−5 = 3` ✓, (c) `5−3 = 2` ✓, (d) `5−3 = 2` ✓,
  (e) `6−5 = 1` ✓. **Executes everywhere.**
* **Lemma S (reductio form, `deg ≥ τ+1 ⟹ head`)** — hypothesis `s = τ` **fails on (a),(b),(c)**,
  holds on (d),(e). Where it fails, its *statement* still happens to be true (I checked: on (a)
  the heads in order are `Bhi, Bhi, C, C, A′`, so both degree-5 vertices are heads), which is
  precisely why the F1/G4 correction mattered: truth is not availability.
* **Lemma S′ (general `s`)** — hypotheses hold on all five. **Yields nothing on any of them:**
  its threshold is `s+1`, and `#{v : deg v ≥ s+1}` is **0** on (a), (b), (c), (d) and (e).
  G4's diagnosis ("*fires but is vacuous*") is confirmed, and it is vacuous on *every* control
  I tried, not just the Fan witness.
* **Lemma DICH(a)** — general-`s`, hypotheses hold everywhere; yields persistence of excess.
* **Lemma DICH(b)** — needs a head of original degree `≥ s+1`. **NAMED LEMMA THAT NEVER
  EXECUTES: DICH(b) fires on 0 heads in all five controls** (thresholds 6, 6, 4, 4, 6 against
  maximum degrees 5, 5, 3, 2, 5). This is the sharpest counterfactual finding of this section:
  DICH(b) is the single most-cited tool of the FAN chain — FAN-1, FAN-2, FAN-4, FAN-6, FAN-8
  all lean on it — and inside the `Fan` family it can only fire under `s = τ`, which
  **Theorem FAN itself proves never happens**. So on every realizable Fan graph the chain's
  main engine is unavailable; it executes only inside the empty reductio. That is legitimate
  reductio practice, but it means the text's numerical "verification" of the DICH(b)-derived
  steps (D3) is verification of something else.
* **Lemma DICH(c)** — needs `g ≤ s`; fires on **5, 5, 3, 3, 5** heads respectively, i.e. on
  *every* head of every control. Available and non-vacuous everywhere.
* **Lemma F3′** — general-`s`, hypotheses hold everywhere; 0 failures in my labelled runs
  (2 094 runs, 1 137 with `s ≠ τ`).
* **Lemma T′** — hypotheses hold on all five (they are graphical). Yields the terminal shape:
  on (a) the list at the start of the last step is `[1,1,0]` = `[D,1^D,0^…]` with `D = 1` ✓.
  **Off graphical inputs it does not hold at all** — D5.
* **Lemma H′** — **SECOND LEMMA THAT NEVER EXECUTES.** Its hypothesis `h_i ≤ i−2` is
  unsatisfiable on any head with `g ≥ s+1` (DICH(b) forces `h_i = i−1`), and on heads with
  `g ≤ s` DICH(c) already gives a strictly stronger bound with no hypothesis. So H′ has no
  call site anywhere, on any input. Section L's "*No new lemma is needed: H′ is already
  subsumed by Lemma DICH*" is correct — but the mechanism is vacuity on one branch and
  strict domination on the other, which the text does not say.
* **Lemma FAN-2** — **THIRD LEMMA THAT NEVER EXECUTES**: superseded by FAN-8, cited by
  nothing, and its hypothesis (the reductio) is false on (a) and (b), the only Fan controls.
* **Theorem FAN / Corollary FAN-HC** — FAN applies to (a) and (b) and yields
  `residue ≤ α−1`: confirmed, `2 ≤ 2` and `3 ≤ 3`, both tight. FAN-HC does **not** apply to
  (a) or (b): they fail `diam = 4` (in (a), `a₀` is adjacent to all of `B` and both `A′`
  vertices attach to both `u` and `v`, so the diameter is 2). Correctly, the text never
  claims otherwise.
* **Lemma 4, Lemma C\*, Observation R1** — frame statements; hypotheses **fail** on (a),(b),
  (c),(d),(e) (none has `diam = 4` with `f = α+1`), so they are unavailable on all five
  controls. The discriminating power of the controls is therefore limited to the HH toolkit,
  which is what the FAN chain is made of.

---

## (f) Trajectories (my implementation, full intermediate lists)

Four `Fan(τ,L≥2)` runs (`L = 2, 2, 3, 4`) plus controls. Every list below is output of my
own code, not transcribed from the brief.

**1. `Fan(4,2)`, `A′ = [2,2]` — `deg = [5,5,4,4,4,2,2]`, `n = 7`, `τ = 4`, `p = 2`, `α = 3`.**
This is repair G1's witness, rebuilt from the `Fan` definition (`B = K₄ − uv`; `a₀ ~` all of
`B`; `a₁, a₂ ~ {u,v}`; `m = 13`).
```
start of step 1  [5, 5, 4, 4, 4, 2, 2]
start of step 2  [4, 3, 3, 3, 2, 1]
start of step 3  [2, 2, 2, 1, 1]      <- start of step p+1 = [L]^(L+1),1,1 = [2,2,2],1,1
start of step 4  [1, 1, 1, 1]
start of step 5  [1, 1, 0]
terminal         [0, 0]
heads D = [5, 4, 2, 1, 1]   s = 5 = tau+1   residue = 2 = alpha-1
```

**2. `Fan(4,2)`, `A′ = [2,1,1]` — `deg = [5,5,4,4,4,2,1,1]`, `n = 8`, `τ = 4`, `α = 4`.**
(Repair F1's witness; my run agrees with the trajectory F1 prints, and confirms that at
`s = 5` the maximum degree is 5 < `s+1 = 6`, so DICH(b) has no call site.)
```
start of step 1  [5, 5, 4, 4, 4, 2, 1, 1]
start of step 2  [4, 3, 3, 3, 1, 1, 1]
start of step 3  [2, 2, 2, 1, 1, 0]
start of step 4  [1, 1, 1, 1, 0]
start of step 5  [1, 1, 0, 0]
terminal         [0, 0, 0]
heads D = [5, 4, 2, 1, 1]   s = 5 = tau+1   residue = 3 = alpha-1
```

**3. `Fan(6,3)`, `d = (2,2,1)`, `A′ = [2,2,1]` — `deg = [7,7,7,6,6,6,6,2,2,1]`, `n = 10`,
`τ = 6`, `p = 3`, `L = 3`, `α = 4`, `m = 25`.**
```
start of step 1  [7, 7, 7, 6, 6, 6, 6, 2, 2, 1]
start of step 2  [6, 6, 5, 5, 5, 5, 2, 1, 1]
start of step 3  [5, 4, 4, 4, 4, 1, 1, 1]
start of step 4  [3, 3, 3, 3, 1, 1, 0]   <- step p+1: C-part [3,3,3,3] = [L]^(L+1), A' = 1,1
start of step 5  [2, 2, 2, 1, 1, 0]
start of step 6  [1, 1, 1, 1, 0]
start of step 7  [1, 1, 0, 0]
terminal         [0, 0, 0]
heads D = [7, 6, 5, 3, 2, 1, 1]   s = 7 = tau+1   residue = 3 = alpha-1
```

**4. `Fan(7,4)`, `d = (2,2,1)`, `A′ = [3,2]` — `deg = [8,8,8,7,7,7,7,7,3,2]`, `n = 10`,
`τ = 7`, `p = 3`, `L = 4`, `α = 3`, `m = 32`.**
```
start of step 1  [8, 8, 8, 7, 7, 7, 7, 7, 3, 2]
start of step 2  [7, 7, 6, 6, 6, 6, 6, 2, 2]
start of step 3  [6, 5, 5, 5, 5, 5, 2, 1]
start of step 4  [4, 4, 4, 4, 4, 1, 1]   <- step p+1: C-part [4,4,4,4,4], A' residue 1,1
start of step 5  [3, 3, 3, 3, 1, 1]
start of step 6  [2, 2, 2, 1, 1]
start of step 7  [1, 1, 1, 1]
start of step 8  [1, 1, 0]
terminal         [0, 0]
heads D = [8, 7, 6, 4, 3, 2, 1, 1]   s = 8 = tau+1   residue = 2 = alpha-1
```

**5. Controls.**
```
K_{2,3}  [3,3,2,2,2] -> [2,2,1,1] -> [1,1,0] -> [0,0]        heads (3,2,1)  s=3  residue=2  (alpha=3, tau=2)
K_6      [5,5,5,5,5,5] -> [4,4,4,4,4] -> [3,3,3,3] -> [2,2,2] -> [1,1] -> [0]   s=5  residue=1
Petersen [3]*10 -> [3,3,3,3,3,3,2,2,2] -> [3,3,2,2,2,2,2,2] -> [2,2,2,2,2,1,1]
         -> [2,2,1,1,1,1] -> [1,1,1,1,0] -> [1,1,0,0] -> [0,0,0]                s=7  residue=3
```

**6. §7.8 E's four-row case table, recomputed from scratch** ("clears in" = further HH steps
from the start of step `p+1`; the reductio needs exactly `L`):

| `L` | `[L]^{L+1},1,1` | `[L]^{L+1},2` | `[L+1],[L]^L,1` | `[L+2],[L]^L` | `[L+1]^2,[L]^{L−1}` |
|---|---|---|---|---|---|
| 2 | 3 | 2 | 2 | truncates | truncates |
| 3 | 4 | 3 | 3 | truncates | truncates |
| 4 | 5 | 4 | 4 | truncates | truncates |
| 5 | 6 | 5 | 5 | truncates | truncates |
| 6 | 7 | 6 | 6 | truncates | truncates |
| 7 | 8 | 7 | 7 | truncates | truncates |
| 8 | 9 | 8 | 8 | truncates | truncates |
| 9 | 10 | 9 | 9 | truncates | truncates |
| 10 | 11 | 10 | 10 | truncates | truncates |
| 11 | 12 | 11 | 11 | truncates | truncates |

so column 1 is `L+1` and columns 2 and 3 are `L`, confirming the table's four rows; extended
to `L = 2…30` with 0 deviations, and column 1 re-checked with 0…4 trailing zeros appended
(FAN-3 is insensitive to the zeros). "truncates" = the head exceeds the number of positive
remaining entries, i.e. FAN-7's non-graphicality step, verified as a computation rather than
taken on trust.

---

## (g) What I could NOT check

1. **Theorem SL's proof (Steps 1–6) and Theorem MB**, beyond the algebra of their statements
   and their use in Proposition L2. The brief's dependence chain routes Corollary FAN-HC
   through them, and M-J1…M-J6 do not name them; I verified L2's derivation *from* MB and
   MB's derivation *from* SL's (LOW3) form, and I re-derived (LOW1)⇔(LOW2)⇔(LOW3), but I did
   not adversarially attack Theorem SL's six-step argument itself. **If Theorem SL is wrong,
   Corollary FAN-HC falls; Theorem FAN does not.**
2. **Theorem K, Theorem T3, Corollary L1-short's ingredients, Lemma 4, Lemma C\* and
   Observation R1** — accepted as given per the brief's scope (section J: "Do NOT re-review
   the K-chain"). I did check Corollary L1-short's own two-line argument and found it sound.
3. **Whether `α = 1 + |A′|` is exact for every sequence in my enumeration box.** I enumerated
   at the degree-sequence level with Gale–Ryser realizability of the `A′ ↔ B_hi` attachment,
   and verified `α` by hand only on the small named witnesses. If some enumerated sequence
   admits a larger independent set, its `α − residue` entry would be wrong — this would make
   my box *weaker*, not produce a false refutation, since I found no survivors either way.
4. **Whether the hard core is non-empty at `L = 2`** (i.e. whether Proposition L2's rigid
   configuration is realizable with `diam = 4` and `f = α+1`). Not needed for the proof, but
   it means Corollary FAN-HC may be eliminating an already-empty layer; I did not measure it.
5. **Lemma Z⁺ and Lemma DICH's proofs at the level the K-chain brief demands.** I re-read
   them and found no fault (Z⁺'s two-branch argument is tie-safe: prefix domination gives
   `v ≤ min(block)` under any tie-break, and the all-later-heads branch counts `D_j + 1`
   against `s − j`), but joint K-J2 is another round's business.
6. **Bibliographic verification of Fact 2** (Favaron–Mahéo–Saclé / Griggs–Kleitman) — no web
   access, and the text itself flags the citation as from memory.
