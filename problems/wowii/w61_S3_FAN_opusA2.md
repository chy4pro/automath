VERDICT: PARTIAL — I could not refute Theorem FAN, Corollary FAN-HC or any of FAN-1/3/4/6/7/8 (22 027 441 exhaustively enumerated `Fan(τ,L≥2)` degree sequences, 0 survivors, and every proof step checks out line by line), but repair F1 is **incomplete**: two sites in §7.8 still assert the withdrawn "`residue = α−1` exactly" as a consequence of the repaired Theorem FAN, and Lemma FAN-2's proof has a tie-break hole that F2 does not mention.
TEXT VERSION REVIEWED: prompts/w61_S3_FAN_A2.md

Judge: independent non-Qwen (Claude Opus). Section K treated as superseding section H throughout.
All code is my own, written from the appendix-A spec; nothing in `problems/wowii/` or `notes/`
was read or executed. Scratch code lives in my session scratchpad, not in the repo.
**No figure below is copied from the brief.** Calibration first (§(e0)), then everything else.

---

## (e0) Calibration of my `residueAux` before anything was trusted

```
residue(K2) = residue([1,1]) = 1                      (expected 1)                    OK
residue(C_n) = residue([2]*n), n = 3..9  ->  1,2,2,2,3,3,3
   ceil(n/3)                            ->  1,2,2,2,3,3,3                              OK
residue(K_n), n = 2..7  -> 1,1,1,1,1,1
residue(K_{1,k}), k = 1..6 -> 1,2,3,4,5,6
residue(K_{2,3}) = residue([3,3,2,2,2]) = 2 ,  s = 3
Lemma 1 spot-check on 628 random graphical sequences (n<=12):
   residue = n - s : 0 failures ;  Sum_i D_i = m : 0 failures ;  Nat-truncation events : 0
Fact 2 (residue <= alpha) on 109 326 connected graphs (exhaustive n<=7 + complete n=8 cover):
   0 violations ; residue = alpha in 36 108 of them.
```

`residueAux` is a function of the sorted list only, so `s` and `residue` are functions of the
degree **multiset**; this is used below and is the reason the exhaustive enumeration over
degree multisets is a *complete*, not a sampled, search of the Fan family inside its box.

---

## (a) Refutation search — what I actually searched

### a.1 What a `Fan(τ,L)` degree multiset is (my reconstruction, from Prop L2 + §7.8 A)

`B = V∖A`, `|B| = τ`; `G[B] = K_τ − uv` with `u,v ∈ B_hi`; `B_lo` = `L` B-universal vertices
of A-degree 1 all attached to one `a₀ ∈ A` which is adjacent to **all** of `B`; every
`a ∈ A′ = A∖{a₀}` has `N(a) ⊆ B_hi`. Writing `p = τ−L ≥ 2`, `d_x` = number of `A′`-neighbours
of `x ∈ B_hi`, `R = Σ_{x∈B_hi} d_x`, and `(e_i)` = the `A′` degrees, the degree multiset is

```
   u, v      :  τ − 1 + d_u ,  τ − 1 + d_v          (d_u,d_v >= 2 forced by deg >= τ+1)
   w in W    :  τ + d_w                             (d_w >= 1 forced by deg >= τ+1)
   B_lo, a0  :  τ  (L+1 times)
   A'        :  e_1..e_k , each 1 <= e_i <= p , Σ e_i = R
```

and such a graph exists **iff** the bipartite pair `((e_i),(d_x))` is Gale–Ryser realizable.
I verified `α(G) = 1 + k` exactly (branch-and-bound independence number) on every instance of
the small box — **0 mismatches** — so `residue = α ⟺ s = τ` is the right reductio test.

### a.2 The main search: exhaustive over the box, 22 million sequences, 0 survivors

```
STRICT Fan(tau,L>=2), box  tau <= 12,  R <= 24,  |A'| <= 20   (EXHAUSTIVE in that box)
   realizable Fan degree sequences enumerated : 22 027 441
   SURVIVORS with residue = alpha             : 0
   histogram of (alpha - residue)             : {1: 22027441}
   per L : {2:6655397, 3:5600053, 4:4327748, 5:2938862, 6:1639311,
            7:673627, 8:171585, 9:20212, 10:646}      (all with gap exactly 1)
   runtime 1060 s
```

Independent second pass through a differently-written driver (box `τ≤10, R≤20, |A′|≤16`):
**1 799 738** sequences, 0 survivors, gap `{1: 1799738}`.

Random *extreme* sweep well outside the systematic box (`τ` uniform in `[4,40]`, random
`d`-profiles and random `A′` partitions): **233 149** realizable Fan sequences, 0 survivors,
gap `= 1` in every one.

Generalised family `GFan(τ,L,ν)` (Fan with `ν` non-edges inside `B_hi`, §7.8 G's LEAD):
```
   nu = 2 , box tau<=9 R<=18 |A'|<=14 : 385 233 sequences, 0 survivors, gap {2:384656, 1:577}
   nu = 3 , same box                  : 230 945 sequences, 0 survivors, gap {2:15473, 3:215472}
```
So the §7.8 G lead's "at `L = 4`, `ν = 3`, `E = 2` survives the step count" shape is **not**
realized by any actual degree sequence in my box either.

**Result: Theorem FAN is not refuted. I found no `Fan(τ,L≥2)` graph with `residue = α`.**

### a.3 Per-lemma refutation attempts (each attacked separately)

Because the reductio is (conjecturally, and in my corpus actually) never satisfied by a Fan
graph, FAN-1/4/6/7/8 are *vacuously* true as stated. To attack them non-vacuously I did two
things: (i) tested their **abstract content** where it is reductio-free, and (ii) ran their
conclusions on real Fan graphs under **adversarial tie-breaking**, off the reductio.

* **FAN-1** ("first `p` heads are `B_hi`"). 13 139 real Fan graphs, four tie-break policies each
  (canonical; MAL-A = among tied maxima always prefer a **non**-`B_hi` head; MAL-B = inside the
  sort put `A′` vertices ahead of `C` vertices at equal value; MAL-C = both) = **52 556 labelled
  runs**: the first `p` heads are exactly `B_hi` in **52 556 / 52 556**. `s` is identical under
  all four policies in all runs (tie-break invariance of `s`, confirmed empirically).
  No counterexample.
* **FAN-4** (`A′` residue sums to 2). Same 52 556 runs: `A′` total at the start of step `p+1`
  is `2` in all of them. The underlying identity `dec_{A′} = R − 2 + E` was checked separately
  on a smaller box (`τ≤7, R≤10, |A′|≤8`, 2 325 graphs × 4 tie-breaks = 9 300 runs): 9 300 / 9 300
  hold, alongside `E = 0` and `C`-part `= [L]^{L+1}` in all 9 300. No counterexample.
* **FAN-6** (residue is `1+1`, never a single `2`). Tested as the abstract statement the proof
  actually uses — "start from a multiset `M_1` with all entries `≤ p`, and for `j = 1..p`
  decrement the `a_j` largest entries with `a_j ≥ 1` and no truncation; can `M_{p+1}` be a
  single `2`?" — over **1 488 521** admissible abstract runs (`p = 2..5`, `|A′| = 2..6`, all
  `M_1`, all `(a_j)` vectors): single-`2` residue **0 times**, `1+1` residue 179 331 times.
  No counterexample.
* **FAN-7** (`E ≤ 2`, `E = 2` impossible). The two `E = 2` shapes `[L+2, L^L]` and
  `[L+1,L+1,L^{L−1}]` are non-graphical for `L = 2…12` by my own Erdős–Gallai (and remain so
  with any number of trailing zeros). No counterexample.
* **FAN-8** (`E = 0`). `E = 0` in **52 556 / 52 556** labelled runs including the two malicious
  policies designed specifically to push a `C`-vertex out of a block. No counterexample.

### a.4 Control: the test is not vacuously negative

Perturb exactly **one** clause of the Fan configuration and re-run the same `residue = α` test
(box `τ≤8, R≤12, |A′|≤10`, exact `α` computed for every graph):

```
 P0  Fan itself (nu=1, the non-edge uv inside B_hi)          13 139 instances,      0 hits
 P1  put the edge uv back  (B is a clique, nu=0)             13 139 instances, 13 139 hits
 P2  nu = 2, both non-edges inside B_hi                      12 684 instances,      0 hits
 P3  nu = 1 but the non-edge MEETS B_lo                      13 139 instances, 13 139 hits
 P4  each B_lo gets one extra private A-neighbour            13 139 instances,      0 hits
 P5  a0 adjacent only to B_lo, not to all of B               13 139 instances,      0 hits
```

P1 and P3 give `residue = α` **100 % of the time**, so the test discriminates sharply. P3 is
the interesting one: moving the single `B`-non-edge from inside `B_hi` to a pair meeting
`B_lo` flips the family from "never satisfies the reductio" to "always satisfies it". That
makes Proposition L2 (b)/(d) — `B_lo⁺ = ∅` and `ν = m̄ = 1` — carry the **entire** weight of
Corollary FAN-HC's `L = 2` step, on a knife edge. Not a defect; a fragility note.

---

## (b) Per-joint verdicts

| joint | verdict | one-line reason |
|---|---|---|
| F-J1 | **SOUND** | Tie-break invariance is trivially true (`residueAux` is a function of the sorted list); the swapped-out entry is a maximum so it always sits in the block (`D_j ≥ 1`); the induction is valid, with the correct reading "there **exists** a tie-break", which is all the downstream lemmas need because they only ever conclude things about the step-`p+1` **value** multiset, which is tie-break invariant. |
| F-J2 | **SOUND** | `V = B_hi ⊔ C ⊔ A′` — exhaustive and disjoint. `Σ_{j≤p}D_j = Σ_{B_hi}deg − C(p,2)` is exactly DICH(b) summed. `Σ_{x∈B_hi} deg_B(x) = p(τ−1) − 2 = 2(τ−2)+(p−2)(τ−1) = pτ−p−2` — both printed forms agree and both are right, including at the boundary `p = 2` (`W = ∅`). The whole `dec_{A′} = R − 2` computation reproduces. |
| F-J3 | **SOUND** | Both cases (`a_j < μ`, `a_j ≥ μ`) check. The propagating invariant is the *quantitative* one the text actually prints (`max(M_{p−t}) = 3+t`, all others `≤ t+1`), and it is that gap `(3+t) − 1 > t+1` which supplies "no entry of value `v−1`". Fails correctly at `1+1`, and F4's diagnosis (non-unique maximum) is the right one — see defect note D-3 for why F4 was **necessary**. |
| F-J4 | **SOUND** | `E ≤ 2` from `A′ residue = 2 − E ≥ 0`; the two `E = 2` lists have head `> ` number of positive remaining entries, hence fail Erdős–Gallai at `i = 1`, hence contradict HH's preservation of graphicality. Verified `L = 2…12`. |
| F-J5 | **SOUND** | (i) `|block_t ∩ A′| = D_t − (p−t) − (L+1) + e_t ≥ 2` is an exact identity, not an estimate — the `τ`s cancel to give literally 2. (ii) "`x` survives steps `t…p`" **is** established: `x ∈ A′` and every head of steps `1…p` is a `B_hi` vertex by FAN-1, so `x` is not deleted; it loses `≤ 1` per step over `p−t+1` steps. No circularity: FAN-8 uses FAN-7's count, which is FAN-4's count re-run with `E`, and neither uses FAN-8 or FAN-6. |
| F-J6 | **SOUND, but resting on an import I cannot see** | L2(a)–(d) does supply every clause of the `Fan(τ,2)` definition, including "every `A`-vertex other than `a₀` attaches only inside `B_hi`" — `deg_A(b_i) = 1` with the common neighbour `a₀` means no `A′` vertex touches `B_lo`, and `B_lo` is all of `B∖B_hi`. But L2 rests on Theorem MB → Theorem SL and on **(F-b)**, which is *never stated or proved anywhere in the supplied text* (see (f)). |
| F-J7 | **PARTIAL — one live recurrence** | Re-derived from scratch, statement by statement (list in (b.1)). Nothing in §7.6/§7.8 is declared *outside* the reductio and proved only *inside* it. But the D1/D3 species **does** recur, in the place F1 was supposed to clean: §7.8 F's "Numerical agreement" paragraph re-attributes the withdrawn exact value to the repaired Theorem FAN (defect D-1), and Lemma FAN-3's proof still carries the same ex-falso identification (defect D-2). |
| F-J8 (i) | **SOUND** | `residue ≠ α` + Fact 2 (`residue ≤ α`) ⟹ `residue ≤ α−1`. Fact 2 is stated in §3, is genuinely needed (the reductio alone gives only `≠`), and is correctly cited. It is an external import; I verified it holds on 109 326 connected graphs, 0 violations. |
| F-J8 (ii) | **SOUND in substance, one wrong reason** | The demarcation is in the right place. But "**Lemma S does not fire (it needs `s = τ`)**" misdiagnoses: Lemma S's own proof is general-`s` (it is literally `F3′` at `j = 1`), so the general-`s` form *is* available at `s = τ+1`; what fails is that its threshold moves from `τ+1` to `s+1 = τ+2`, and the `B_hi` degrees sit at exactly `τ+1 = s`. Measured (my box, 13 139 Fan graphs): DICH(b) covers **all** of `B_hi` in only **2 292** (17.4 %) and **none** of `B_hi` in 108 — so the unavailability claim is right, for the right *quantitative* reason. Own witness beyond the author's: `Fan(5,2)`, `d_hi = (2,2,1)`, `A′ = [3,2]`, `deg = [6,6,6,5,5,5,3,2]`, `τ=5`, `α=3`, `s=6=τ+1`, where **all three** `B_hi` degrees equal `s`, so DICH(b) is unavailable for every one of them. |
| F-J8 (iii) | **DEFECT — 2 orphans found** | Full site list in (b.2). Two sites still consume the deleted claim: §7.8 F "Numerical agreement" (D-1) and §7.8 A Lemma FAN-3's closing clause (D-2). Everything else checked clean. |
| F-J8 (iv) | **SOUND, with one stale label** | Frame-vs-hard-core assignment is correct statement by statement (table in (b.3)). Two nits: Observation R1 is assigned to the frame but needs strictly less (connected + `diam = 4` + `A` maximum independent — neither `f = α+1` nor non-forest); and F3 silently bakes `τ ≥ 4` into "hard core", which retro-labels §7.4 D's and §7.6 C's "hard-core" numerics (computed at `τ = 2,3,4` with **no** reductio) as *frame* numbers, while those paragraphs still say "hard core". |

### b.1 F-J7, re-derived scope table (not reusing the author's audit, which F5 says was wrong)

Declared-reductio and genuinely reductio: Lemma HI (needs Lemma S), Theorem LOW (LOW1/2/3),
Lemma SL1, Lemma ID, Conjecture SL1, Theorem SL, Lemma FAN-1, FAN-2 (after F2), FAN-4, FAN-6,
FAN-7, FAN-8. Declared hard-core and genuinely hard-core: Prop L1, Cor L1′, Cor SL-HC,
Theorem MB, Cor L1-short, Cor MB1, Prop L2, Cor FAN-HC. Reductio-free and correctly so:
Lemma FAN-3 (a hypothesis-free statement about a value multiset), Observation FAN-5 (ditto),
Observation R1, Lemma 4, Lemma C\* (F3 moves it to the frame — correct; its proof uses Lemma 4
and (F-b) only). Internally-reductio-but-externally-clean: Theorem FAN, Theorem K, Cor K1.
**No statement is declared outside the reductio and proved only inside it.** The only
over-hypothesisation (safe direction) left after F3 is Observation R1 (see F-J8(iv)).

### b.2 F-J8(iii), orphan sweep — every site I checked

| site | uses "`residue = α−1` / `s = τ+1` exactly"? | verdict |
|---|---|---|
| §7.8 A "Numerical verdict" box (`α−residue` histogram) | yes, as a **measurement** | clean — it is data, not a derivation |
| §7.8 A "Mechanism check" M4 `s = τ+1` | yes, as a measurement | clean |
| §7.8 A **Lemma FAN-3**, proof, last clause "*— which is precisely the measured `α − residue = 1`*" | yes, as an **identification** of a reductio-internal value with the real one | **ORPHAN (D-2)** |
| §7.8 D Observation FAN-5 ("`[L]^{L+1},2` clears in exactly `L`") | no — pure multiset arithmetic | clean (and true: verified `L = 2…12`) |
| §7.8 E case-list table ("clears in" column, "the reductio needs exactly `L`") | inside the reductio only | clean |
| §7.8 E "Enlarged box" paragraph | measurement | clean |
| §7.8 F **"Numerical agreement"**: "*Theorem FAN predicts `residue = α − 1` for every `Fan(τ,L≥2)` degree sequence … including the off-by-one*" | yes, attributed to the **repaired** theorem | **ORPHAN (D-1)** |
| §7.8 F Theorem FAN proof "*Lemma FAN-3 gives `s = τ+1`, a contradiction*" | inside the reductio; only `s ≠ τ` is exported | clean |
| §7.8 F Corollary FAN-HC | consumes only the first sentence | clean |
| §7.8 G `GFan` LEAD | marked LEAD, and reductio-internal | clean |
| §7.6 A–G (HI, LOW, L1, L1′, SL1, ID, SL, SL-HC, MB, L1-short, MB1, L2) | none reference the exact value | clean |
| §7.5 (Z⁺, DICH, Theorem K, Cor K1) | Cor K1 concludes `≤ α−1` via reductio + Fact 2 (repair D2) | clean |
| §7.4 (BO, Z, DEC, CNT, N′, C\*) | no | clean |
| §7.7 / §7.9 (R1, R2, D1–D5) | no | clean |
| §7 reduction ("`f ≥ α+2` **or** `residue ≤ α−1`") | needs only `≤ α−1` | clean — this is why D-1/D-2 cost nothing |

### b.3 F-J8(iv), which frame each statement really needs

| statement | F3 assigns | actually needs | ok? |
|---|---|---|---|
| Observation R1 | frame | connected + `diam = 4` + `A` maximum independent (not `f = α+1`, not non-forest) | over-assigned, safe |
| Lemma 4 | frame | `f = α+1` + `A` maximum independent (not `diam = 4`) | over-assigned, safe |
| (F-b) | frame | `diam = 4` + `f = α+1` (via Lemma 5) | correct — but see (f) |
| Lemma C\* | frame | Lemma 4 + (F-b) ⟹ exactly the frame (non-forest is redundant: `f = α+1` with `diam = 4` already excludes forests) | correct |
| Proposition L1 | hard core | (LOW3) [reductio] + C\* + Lemma 4 + R1 | correct |
| Proposition L2 | hard core | Theorem MB [→ SL, reductio] + R1 + (F-b) + C\* | correct |
| Theorem MB | hard core | Theorem SL [reductio] + Lemma 4 + C\* | correct |
| Corollary SL-HC | hard core | Theorem K + R1 + Prop L1 + Cor L1′ + Theorem SL | correct (its parenthetical "`τ ≥ 3` in the hard core" is stale under F3's `τ ≥ 4`) |
| Corollary FAN-HC | hard core | Theorem K, Cor L1-short, Prop L2, Theorem FAN, Theorem T3 | correct |

**Empirical confirmation that the frame/hard-core line is in the right place.** In my corpus
there are 332 hard-core-**frame** graphs and **0** hard-core graphs (no frame graph has
`residue = α`), so every hard-core statement is vacuous on the corpus — as the text's own
firewall says. Restricting to `τ ≥ 4`, `L = 2` frame instances there are **42**; the
(LOW1/Theorem SL) slack over them is `{0: 33, 1: 9}`. That is, **Theorem SL's conclusion
`slack ≥ 1` is FALSE at 33 of them** — which is exactly right, because none of them satisfies
the reductio. So Theorem SL demonstrably consumes the reductio and is not free in the frame;
and the 9 with slack 1 are precisely the `Fan(4,2)` instances, matching Prop L2(e)'s
"slack exactly 1". Prop L2's four conclusions (a)–(d) hold at 9 of 42 and fail at 33 — again,
correct: L2 is a hard-core statement and is false in the frame.

---

## (c) Defects

### D-1. §7.8 F, "Numerical agreement" — the withdrawn claim is re-attributed to the repaired theorem. **REAL, repairable, conclusion survives.**

Quoted line (section H, part F, still standing after K):

> "**Numerical agreement.** Theorem FAN predicts `residue = α − 1` for *every* `Fan(τ,L≥2)`
> degree sequence. … Prediction and measurement agree exactly, including the off-by-one."

**Why it fails.** After repair F1, Theorem FAN predicts `residue ≤ α − 1` and nothing more —
F1(i) says in so many words "nothing in the argument bounds `s` from above". The paragraph
therefore states, as an output of the repaired theorem, exactly the sentence F1 deleted from
it. This is the D1 species (a claim whose scope is only valid under a hypothesis that has been
refuted) recurring **inside the repair section's own target**, which is precisely what F5
warns the author's audit missed.

**Smallest configuration exposing it.** Any `Fan(τ,L≥2)`; the smallest is `τ=4, L=2, p=2`,
`d_u=d_v=2`, `A′=[2,2]`: `deg = [5,5,4,4,4,2,2]`, `n=7`, `α=3`, `τ=4`, my computed
`s = 5 = τ+1`, `residue = 2 = α−1`. The measurement agrees with `residue = α−1`; the *theorem*
only entitles you to `residue ≤ α−1 = 2`. The agreement is real, the attribution is not.

**Repairable?** Yes, one word: "Theorem FAN predicts `residue ≤ α − 1`; **Observation FAN-E**
predicts `residue = α−1`, and that is what is measured."

**Does the CONCLUSION survive?** Yes. The §7 reduction needs only `residue ≤ α−1`.

### D-2. §7.8 A, Lemma FAN-3's proof, closing clause — the same ex-falso identification F1(ii) forbids. **REAL, repairable, conclusion survives.**

> "…so `s = τ+1` exactly — **which is precisely the measured `α − residue = 1`**. ∎"

**Why it fails.** Lemma FAN-3 is a conditional about a value multiset; its hypothesis (the
step-`p+1` list is `[L]^{L+1},1,1`) is only ever *derived* under the reductio `s = τ`. Under
F1(ii)'s own rule, the conclusion `s = τ+1` may not be identified with the real, off-reductio
`s`. F1 deletes the identical sentence from Theorem FAN but leaves this one in place.

Mitigating: the identification happens to be *correct*. I verified that the step-`p+1` multiset
really is `[L]^{L+1},1,1` on real (off-reductio) Fan runs in **52 556 / 52 556** labelled runs
including two malicious tie-break policies. So this is an audit-trail defect, not an error of
fact. It is still the species F-J7 was told to hunt.

**Smallest configuration.** `Fan(4,2)`, `deg = [5,5,4,4,4,2,2]` (above): the step-3 list is
`C`-part `[2,2,2]`, `A′`-part `[1,1]`, and `s = 5`; but that list is reached by a run for which
Lemma S and DICH(b) do not fire (all `B_hi` degrees `= 5 = s`).

**Repairable?** Yes — delete the clause, or mark it "(off the reductio this coincidence is
Observation FAN-E, not a consequence of FAN-3)".

**Conclusion survives?** Yes.

### D-3. Amendment F4 is **correct and necessary** — but the text under-states why. (Not a defect; recorded because the brief asked for a statement-by-statement verdict on the repairs.)

F4 says the clause that fails first for the `1+1` residue is uniqueness of the maximum, and
that when `|A′| = 2` there are no zero entries so the original reason was wrong. I confirmed
`|A′| = 2` is genuinely realizable at **every** `L ≥ 2`, not a curiosity:

```
 Fan(4,2) d_hi=[2,2] A'=[2,2]  deg=[5,5,4,4,4,2,2]      M_{p+1}=[1,1]  zeros present: NO
 Fan(5,3) d_hi=[2,2] A'=[2,2]  deg=[6,6,5,5,5,5,2,2]    M_{p+1}=[1,1]  zeros present: NO
 Fan(6,4) d_hi=[2,2] A'=[2,2]  deg=[7,7,6,6,6,6,6,2,2]  M_{p+1}=[1,1]  zeros present: NO
 Fan(6,2) d_hi=[2,2,1,1] A'=[2,2,1,1] deg=[7,7,7,7,6,6,6,2,2,1,1] M_{p+1}=[1,1,0,0] zeros: YES
```
(Also note `|A′| = 1` is impossible: `R ≥ 4 + (p−2) = p+2 > p ≥ max A′ degree`.) So the
original parenthetical was false in an infinite realizable sub-family, and F4 fixes it. Good
repair.

### D-4. Lemma FAN-2's proof is **not tie-safe at `j = L+1`**, and F2 does not say so. **REAL, superseded, zero impact.**

> "*Proof.* At step `j` the non-head entries above a `C`-entry are the `p − j` remaining high
> vertices …; every `A′` entry has value `≤ p ≤ τ−j+1` for `j ≤ L+1`, so **none is strictly
> above**. Hence `C ⊆ block_j` as soon as `D_j ≥ (p−j) + (L+1)` …"

**Why it fails.** "None is strictly above" is not enough when the bound is attained. At
`j = L+1` one has `p = τ−j+1` exactly, so an `A′` entry can **tie** with a `C`-entry. The block
is a prefix, and among tied values the sort order is arbitrary; if `q` `A′` entries sit at the
threshold value `τ−j+1`, then all of `C` is in `block_j` only if `D_j ≥ (p−j)+(L+1)+q`, i.e.
only if `q ≤ a_j := D_j − (p−j) − (L+1)`. The proof supplies exactly one unit of slack
(`D_j ≥ (p−j)+(L+1)+1`), so it covers `q ≤ 1` and no more. For `j < L+1` the inequality
`p < τ−j+1` is strict and the argument is airtight; the hole is exactly at the boundary the
lemma's own range condition `j ≤ min(p, L+1)` maximises.

**Smallest configuration exposing it.** None realizes it: over **8 884** real Fan runs whose
step `j = L+1` exists, `q = 0` every single time (the maximum `A′` value at step `j` is
`≤ p − (j−1)`, one below the `C` value). So the *conclusion* is safe. The defect is in the
argument only, and it cannot be patched from within FAN-2, because the fact that saves it
(the maximum `A′` entry is decremented at every step) is FAN-6's prefix property, which itself
presupposes `E = 0` — the very thing FAN-2 is trying to prove.

**Repairable?** Yes and already moot: FAN-8 proves `E = 0` unconditionally without FAN-2, and
F2 marks FAN-2 superseded. But §7.8 E's status line still lists **FAN-2 among the lemmas that
are "PROVED"**; it should say "superseded; its proof is tie-incomplete at `j = L+1`" or be
deleted outright.

**Conclusion survives?** Yes, entirely — FAN-2 is used nowhere.

### D-5. F3 leaves two stale labels. **Cosmetic.**

(i) §7.4 D and §7.6 C compute histograms over graphs they call "the hard core (connected,
non-forest, diam = 4, `f = α+1`)" — under F3 that set is the **frame**; the word "hard core"
now denotes something strictly smaller (and, on my corpus, empty). (ii) Corollary SL-HC's
parenthetical "note `τ ≥ 3` in the hard core" is stale under F3's `τ ≥ 4`. Neither changes any
proof.

### Things I attacked and could NOT break (recorded so the negative result is on the record)

* FAN-1's tie-break-invariance step. It is not merely true, it is trivially true: `residueAux`
  is a function of the descending-sorted list, so `s` and the whole value trajectory depend on
  the degree multiset alone. The "other entry lies in the block" step is safe because the
  swapped-out entry carries the maximum value and `D_j ≥ 1` always.
  At `j = 1` the "equality is a tie" branch is vacuous (a low head at step 1 has
  `D_1 = g ≤ τ < τ+1`), so the argument lands by a stronger route than it claims. Harmless.
* FAN-4's three-class bookkeeping, including the boundary `p = 2` (`W = ∅`).
* FAN-6's backward induction, both cases, and its base case.
* FAN-7's `E ≤ 2` and the non-graphicality of the two `E = 2` shapes.
* FAN-8's `|block_t ∩ A′| ≥ 2` (an exact identity) and the survival of `x` over steps `t…p`.
* Theorem SL's Steps 1–6 (I re-checked each; `slack ≥ 1` fails 0 times in 193 491 reductio
  instances of my corpus).
* Corollary FAN-HC's use of Prop L2 as rigidity — every `Fan` clause is supplied.

---

## (d) Control cases / counterfactual availability (T12) — REQUIRED SECTION

Five control instances. For each I go through **every** lemma the text claims is available.

### Control (a) — `Fan(4,2)`, `d_u=d_v=2`, `A′=[2,1,1]`, `deg = [5,5,4,4,4,2,1,1]`, `n=8`
My own recomputation (the author's F1 witness; I rebuilt the graph from the configuration and
found it also occurs as an actual atlas/cover graph, with edges
`{(0,2),(1,2),(1,4),(2,3),(2,5),(3,4),(3,5),(4,5),(4,6),(2,7),(3,7),(4,7),(5,7)}`,
`B = {2,3,4,5}`, `B_hi = {2,4}`, `B_lo = {3,5}`, `a₀ = 7`, `A′ = {0,1,6}`):
`α = 4` (computed exactly), `τ = 4`, `f = 5 = α+1`, `diam = 4`, non-forest ⇒ **hard-core
frame**, `residue = 3 = α−1`, `s = 5 = τ+1`.

| lemma the text claims available | hypotheses hold here? | what it yields | which hypothesis fails |
|---|---|---|---|
| Lemma 1 (residue `= n−s`, `ΣD_i = m`) | yes (unconditional) | `3 = 8−5`; `ΣD_i = 5+4+2+1+1 = 13 = m` | — |
| Fact 2 | yes | `3 ≤ 4` | — |
| Lemma 4 | yes (frame) | codegree conditions on `B` | — |
| Observation R1 | yes | `ν = 1 ≥ 1`, `B` not a clique | — |
| (F-b) + Lemma C\* | yes (frame) | `deg_A(u),deg_A(v) ≥ 3` | — |
| Lemma S (as printed, `s = τ`) | **no** | nothing | the standing `residue = α` |
| Lemma S (general-`s` form = `F3′` at `j=1`) | yes | survivors have degree `≤ s = 5`; `B_hi` degrees are `5`, so **it says nothing about `B_hi`** | threshold is `s+1 = 6 > 5` |
| Lemma F3′ | yes | survivor value `≤ s−j+1` — holds, checked | — |
| Lemma Z⁺ | yes (general `s`) | vacuous here (no later head is excess) | — |
| Lemma DICH(b) | **no** | nothing | needs `g ≥ s+1 = 6`; `Δ = 5` |
| Lemma DICH(c) | yes (`g ≤ s` for every vertex) | `D_i ≤ s−i+2 = 7−i`: gives `D_1≤6, D_2≤5, D_3≤4…` — true but **weaker than the actual `5,4,2,1,1`** | — |
| Lemma HI | **no** | nothing | built on Lemma S under the reductio |
| Theorem LOW / Theorem SL | **no** | nothing | reductio |
| Theorem K / **Corollary K1** | **no** | nothing | needs `min_B deg ≥ τ+1`; `B_lo` degrees are `τ = 4` |
| Proposition L2 | **no** (needs the reductio) | — but its four conclusions happen to hold here | reductio |
| Lemmas FAN-1/4/6/7/8 | **no** | nothing | reductio |
| Lemma FAN-3 | yes (hypothesis-free) — **but its hypothesis (the step-3 multiset) is not derivable here** | if you *measure* the step-3 list `[2,2,2,1,1,0]` it gives `s = 5` | its hypothesis has no proof off the reductio |

**Lemma named as "claimed available but never executes": Theorem K / Corollary K1.**
The FAN chain's own "Chain of dependence" lists Theorem K among what Corollary FAN-HC rests on,
and §7.5 advertises Corollary K1 as "this replaces Theorem N and Theorem N′ in the hard core".
Its hypothesis is `min_{b∈B} deg(b) ≥ τ+1`. In **every** `Fan(τ,L)` with `L ≥ 1` the `L` low
vertices have degree exactly `τ`. Measured: **0 of 13 139** Fan graphs satisfy it. So on the
entire target family Theorem K/K1 is unfireable; it contributes only the `L = 0` layer of
Corollary FAN-HC and nothing to Theorem FAN.

**Second such lemma: Lemma FAN-2.** F2 concedes it is superseded and "no longer used", yet the
§7.8 E status line still certifies it as PROVED. It executes nowhere, and (D-4) its proof is
incomplete at the one step where it is not implied by FAN-8.

**Third: Theorem SL at the target configuration.** Its hypotheses *do* hold in the hard core at
`L = 2`, and it *does* execute — but Prop L2(e) computes the slack of the `Fan(τ,2)`
configuration as exactly `1`, so `slack ≥ 1` is tight and yields nothing. (`Fan(τ,L)` has slack
`L(τ+1) − (Lτ + 1) = L−1`; for `L ≥ 3` the actual slack is `≥ 2` while SL still only gives
`≥ 1` — a **slack-≥2 counting step used where tightness is what would be needed**, exactly the
brief's probe 6. The text acknowledges this: "a general `slack ≥ L` would kill the whole family
at once".)

### Control (b) — `B` a clique (P1): `deg = [6,6,4,4,4,2,1,1]`, `n = 8`
`α = 4`, `τ = 4`, `residue = 4 = α` ⇒ **the reductio HOLDS**. Here Lemma S fires
(`deg ≥ τ+1 = 5` for both `B_hi`), DICH(b) fires (`g = 6 ≥ s+1 = 5`) and gives
`h_2 = 1`, `D_2 = 5`; Theorem K's hypothesis still fails (the two `B_lo` have degree 4), so
`K = B` is not forced — and indeed `L = 2`. Theorem LOW's (LOW1) reads
`Σ_{B_lo} deg + ν = 8 + 0 = 8 ≤ L(τ+1) = 10`, slack 2 ≥ 1 consistent with Theorem SL. This is
the control that shows the whole `residue = α` test is live: **13 139 of 13 139** P1 instances
have `residue = α`.

### Control (c) — the non-edge moved to touch `B_lo` (P3): `deg = [6,5,4,4,3,2,1,1]`
`α = 4 = residue`, `τ = 4`, `s = 4 = τ`: **reductio holds**, `L = 2`, `ν = 1`. Every clause of
`Fan` holds except that the unique `B`-non-edge meets `B_lo` instead of sitting inside `B_hi`.
Prop L2(b) (`B_lo⁺ = ∅`) is exactly what excludes this, and it is excluded via Theorem MB →
Theorem SL — reductio-only machinery. **13 139 of 13 139** P3 instances have `residue = α`.
This is the sharpest available evidence that Corollary FAN-HC's `L = 2` step is doing real
work and is not a formality.

### Control (d) — `K_{2,3}`, `deg = [3,3,2,2,2]`
`α = 3`, `τ = 2`, my computed heads `(3,2,1)`, `s = 3 ≠ τ`, `residue = 2 = α−1`. Lemma S as
printed is out of scope (its standing hypothesis `s = τ` fails); `F3′` is in scope and holds;
DICH(b) fires for the two degree-3 vertices (`3 ≥ s+1 = 4`? **no** — `s+1 = 4 > 3`, so DICH(b)
does **not** fire), DICH(c) fires for all and gives `D_i ≤ 5−i`, satisfied. This reproduces the
regime repair R2 was written for.

### Control (e) — a `τ = 4`, `L = 2` frame graph that is **not** a Fan
`n = 8`, edges `{(0,1),(0,2),(0,3),(0,4),(0,7),(1,2),(1,3),(1,4),(1,7),(2,3),(2,4),(3,5),(4,5),(5,6)}`,
`deg = [5,5,4,4,4,3,2,1]`, `α = 4`, `τ = 4`, `f = 5`, `diam = 4`, `residue = 3 ≠ α`.
`B = {0,1,2,5}`, `B_lo = {2,5}`, `ν = 3`. Here the **(LOW1)/Theorem SL slack is 0**, i.e.
Theorem SL's conclusion is *false* at this graph — correctly, since the reductio fails. 33 of
the 42 `τ ≥ 4, L = 2` frame instances in my corpus behave this way, and only the 9 that are
literally `Fan(4,2)` have slack 1. So: Theorem SL, Theorem MB and Proposition L2 all genuinely
consume the reductio; none of them is available in the frame.

### Machinery verification inside the reductio (where the FAN chain actually lives)

Corpus: exhaustive connected atlas `n ≤ 7` (995), a **complete** cover of connected `n = 8`
(`H + v` over the 853 connected 7-vertex graphs × 127 non-empty neighbourhoods = 108 331 pairs,
109 326 connected graphs after the atlas), plus 3 000 random `n = 9…12` — **111 742** connected
graphs; **193 491** `(graph, maximum independent set)` instances with `residue = α`, each run
under the canonical sort **and 3 randomised adversarial tie-breaks**.

```
  Lemma S           failures 0        Lemma F3'            failures 0
  Lemma Z+          failures 0        Lemma DICH(b) member failures 0
  DICH(b) equality  failures 0        Lemma DICH(c)        failures 0
  (LOW1)            failures 0        Theorem SL slack>=1  failures 0
  Theorem K (L=0 => B clique)  failures 0
  Lemma 4 (both clauses)       failures 0     Observation R1  failures 0
  (F-b) derivable from a diametral pair: 381 / 381 frame instances
  Lemma C* (deg_A >= 3 on T1 u T2):        0 failures
  hard-core FRAME graphs 332 ;  hard-core graphs (frame + residue = alpha)  0
```

---

## (e) Trajectories (my own implementation, all intermediate lists)

`L^i` = the descending-sorted list at the start of step `i+1`.

**T1 — `Fan(τ=5, L=2)`, `p=3`, `d_hi=(2,2,1)`, `A′=[3,2]`.** `n=8`, `m=19`,
`deg = [6,6,6,5,5,5,3,2]`, computed `α = 3`, `τ = 5`.
```
 L^0 = [6,6,6,5,5,5,3,2]   D_1 = 6
 L^1 = [5,5,4,4,4,2,2]     D_2 = 5
 L^2 = [4,3,3,3,2,1]       D_3 = 4
 L^3 = [2,2,2,1,1]         D_4 = 2
 L^4 = [1,1,1,1]           D_5 = 1
 L^5 = [1,1,0]             D_6 = 1
 L^6 = [0,0]               stop
 s = 6 = tau+1 ,  residue = 2 = alpha - 1 ,  alpha = 3 , tau = 5
 labelled heads: u, v, w1, b1, b2, a'1     -> first p=3 heads ARE B_hi
 at the start of step p+1 = 4:  C-part [2,2,2] = [L]^{L+1} ,  A'-part [1,1]  (total 2)
 NOTE: all three B_hi degrees are 6 = s, so DICH(b) (needs >= s+1 = 7) fires for NONE of them.
```

**T2 — `Fan(τ=6, L=3)`, `p=3`, `d_hi=(2,2,1)`, `A′=[3,2]`.** `n=9`, `m=25`,
`deg = [7,7,7,6,6,6,6,3,2]`, `α = 3`, `τ = 6`.
```
 L^0 = [7,7,7,6,6,6,6,3,2]  D_1 = 7
 L^1 = [6,6,5,5,5,5,2,2]    D_2 = 6
 L^2 = [5,4,4,4,4,2,1]      D_3 = 5
 L^3 = [3,3,3,3,1,1]        D_4 = 3
 L^4 = [2,2,2,1,1]          D_5 = 2
 L^5 = [1,1,1,1]            D_6 = 1
 L^6 = [1,1,0]              D_7 = 1
 L^7 = [0,0]                stop
 s = 7 = tau+1 , residue = 2 = alpha-1 , alpha = 3 , tau = 6
 heads: u, v, w1, b1, b2, b3, a'1 ;  step p+1 = 4: C-part [3,3,3,3], A'-part [1,1]
```

**T3 — `Fan(τ=7, L=4)`, `p=3`, `d_hi=(3,2,1)`, `A′=[3,2,1]`.** `n=11`, `m=33`,
`deg = [9,8,8,7,7,7,7,7,3,2,1]`, `α = 4`, `τ = 7`.
```
 L^0 = [9,8,8,7,7,7,7,7,3,2,1]  D_1 = 9
 L^1 = [7,7,6,6,6,6,6,2,1,1]    D_2 = 7
 L^2 = [6,5,5,5,5,5,1,1,1]      D_3 = 6
 L^3 = [4,4,4,4,4,1,1,0]        D_4 = 4
 L^4 = [3,3,3,3,1,1,0]          D_5 = 3
 L^5 = [2,2,2,1,1,0]            D_6 = 2
 L^6 = [1,1,1,1,0]              D_7 = 1
 L^7 = [1,1,0,0]                D_8 = 1
 L^8 = [0,0,0]                  stop
 s = 8 = tau+1 , residue = 3 = alpha-1 , alpha = 4 , tau = 7
 heads: u, v, w1, b1, b2, b3, b4, a'2 ; step p+1 = 4: C-part [4,4,4,4,4], A'-part [1,1,0]
 Here DICH(b) DOES fire for u (deg 9 >= s+1 = 9) but NOT for v,w1 (deg 8 < 9).
```

**T4 — `Fan(τ=4, L=2)`, `p=2`, `d_hi=(2,2)`, `A′=[2,1,1]` (independent recomputation of the
F1 witness).** `n=8`, `m=13`, `deg = [5,5,4,4,4,2,1,1]`, `α = 4` (computed exactly), `τ = 4`.
```
 L^0 = [5,5,4,4,4,2,1,1]  D_1 = 5
 L^1 = [4,3,3,3,1,1,1]    D_2 = 4
 L^2 = [2,2,2,1,1,0]      D_3 = 2
 L^3 = [1,1,1,1,0]        D_4 = 1
 L^4 = [1,1,0,0]          D_5 = 1
 L^5 = [0,0,0]            stop
 s = 5 = tau+1 , residue = 3 = alpha-1 , alpha = 4 , tau = 4
 heads: u, v, b1, b2, a'2 ; step p+1 = 3: C-part [2,2,2], A'-part [1,1,0]
```
(My recomputation agrees with the trajectory F1 prints. This graph is a genuine
**hard-core-frame** graph — `diam = 4`, non-forest, `f = 5 = α+1` — and is the only Fan shape
occurring in my exhaustive `n ≤ 8` corpus; it turns up 9 times among the `(graph, A)` frame
instances, which include isomorphic duplicates since the `n = 8` cover does no isomorphism
rejection.)

**T5 — `Fan(τ=6, L=2)`, `p=4`, `d_hi=(2,2,1,1)`, `A′=[2,2,1,1]`.** `n=11`, `m=26`,
`deg = [7,7,7,7,6,6,6,2,2,1,1]`, `α = 5`, `τ = 6`.
```
 L^0 = [7,7,7,7,6,6,6,2,2,1,1]  D_1 = 7
 L^1 = [6,6,6,5,5,5,2,1,1,1]    D_2 = 6
 L^2 = [5,5,4,4,4,1,1,1,1]      D_3 = 5
 L^3 = [4,3,3,3,1,1,1,0]        D_4 = 4
 L^4 = [2,2,2,1,1,0,0]          D_5 = 2
 L^5 = [1,1,1,1,0,0]            D_6 = 1
 L^6 = [1,1,0,0,0]              D_7 = 1
 L^7 = [0,0,0,0]                stop
 s = 7 = tau+1 , residue = 4 = alpha-1 , alpha = 5 , tau = 6
 heads: u, v, w1, w2, b1, b2, a'3 ; step p+1 = 5: C-part [2,2,2], A'-part [1,1,0,0]
```

**T6 (control, reductio HOLDS) — P1, `B` a clique:** `deg = [6,6,4,4,4,2,1,1]`, `α = 4`, `τ = 4`.
```
 L^0 = [6,6,4,4,4,2,1,1]  D_1 = 6
 L^1 = [5,3,3,3,1,1,0]    D_2 = 5
 L^2 = [2,2,2,0,0,0]      D_3 = 2
 L^3 = [1,1,0,0,0]        D_4 = 1
 L^4 = [0,0,0,0]          stop
 s = 4 = tau ,  residue = 4 = alpha  ->  RESIDUE = ALPHA
```

**T7 (control, reductio HOLDS) — P3, the non-edge meets `B_lo`:** `deg = [6,5,4,4,3,2,1,1]`,
`α = 4`, `τ = 4`.
```
 L^0 = [6,5,4,4,3,2,1,1]  D_1 = 6
 L^1 = [4,3,3,2,1,1,0]    D_2 = 4
 L^2 = [2,2,1,1,0,0]      D_3 = 2
 L^3 = [1,1,0,0,0]        D_4 = 1
 L^4 = [0,0,0,0]          stop
 s = 4 = tau ,  residue = 4 = alpha  ->  RESIDUE = ALPHA
```

**T8 (control) — `K_{2,3}`:** `deg = [3,3,2,2,2]`, `α = 3`, `τ = 2`.
```
 L^0 = [3,3,2,2,2]  D_1 = 3
 L^1 = [2,2,1,1]    D_2 = 2
 L^2 = [1,1,0]      D_3 = 1
 L^3 = [0,0]        stop
 s = 3 != tau = 2 , residue = 2 = alpha - 1
```

Additional abstract trajectories (direct tests of FAN-3 / FAN-5, `L = 2…12`):
`[L]^{L+1},1,1` clears in `L+1` steps for every `L = 2…12` (11/11 agree with FAN-3);
`[L]^{L+1},2` clears in exactly `L` steps for every `L = 2…12` (11/11 agree with FAN-5).
Both `E = 2` shapes are non-graphical for every `L = 2…12` (FAN-7).

---

## (f) What I could NOT check

1. **(F-b) — "occurring types `T₁,T₂ ⊆ B`, disjoint, with no `G[B]`-edge between them" is never
   stated or proved anywhere in the supplied text.** It is invoked as a standing hard-core
   assumption in §7.4 C (Lemma C\*), §7.6 B (Prop L1), Theorem MB and Prop L2(a),(b),(d) — and
   Prop L2 is what Corollary FAN-HC's `L = 2` step consumes. I reconstructed what it must mean
   and a proof (`T₁ = N_B(v₀)`, `T₂ = N_B(v₄)` for a diametral pair `v₀,v₄`, which Lemma 5 puts
   in `A`; disjointness and no crossing edge both follow from `dist(v₀,v₄) = 4`), and I verified
   this reconstruction holds in **381 of 381** frame `(graph, A)` instances of my corpus with 0
   `C*` failures. But the *text under review* does not contain it, so I am certifying my own
   reconstruction, not the author's. **This is the single largest unverifiable import in the
   `L = 2` layer of Corollary FAN-HC.**
2. **Theorem T3** (`τ ≤ 3` fully solved) is not in the appendix; Corollary FAN-HC's "`τ ≥ 4`"
   and F3's hard-core definition both depend on it. Not checked.
3. **Lemma 5** (radial-path forcing), quoted in §7.1 but not reproved; used by my (F-b)
   reconstruction. Not independently checked beyond my corpus test.
4. **Fact 2** is an external citation (Favaron–Mahéo–Saclé / Griggs–Kleitman). I verified it
   empirically (109 326 graphs, 0 violations) but did not verify the reference or the proof.
   Repair F1's conclusion depends on it.
5. **Observation FAN-E's unprovability claim.** I can confirm the measurement (all
   22 027 441 + 1 799 738 + 233 149 of my Fan sequences have `residue = α−1` exactly) and
   confirm that the specific tools named (Lemma S, DICH(b)) do not fire. I cannot confirm that
   *no* proof exists; the obvious next attempt — a second reductio on `s ≥ τ+2` — is not tried
   in the text, and I did not try it either.
6. **The `n = 8` cover** is complete for connected 8-vertex graphs but the `n = 9…12` part of
   my corpus is random (3 000 graphs), so the reductio-side lemma checks are exhaustive only to
   `n = 8`. No isomorphism rejection was done (duplicates cost time only).
7. **`GFan(τ,L,ν)` for `ν ≥ 2`** was swept with a single fixed placement pattern of the `ν`
   non-edges inside `B_hi`, not all placements. `ν ≥ 4` was not swept at all.
8. I did not re-review the K-chain (`Z⁺`/DICH/Theorem K/K1) as a target — per the brief it is
   out of scope — beyond verifying its statements numerically inside the reductio (0 failures)
   because the FAN chain depends on them.
9. **`Fan` graphs where `A` is not a maximum independent set** are outside Theorem FAN's intent;
   I checked that `α = 1 + |A′|` really is exact on every instance of the small box (0
   mismatches) and proved it by hand (`{b} ∪ A′` is independent of size `1+|A′|`, and
   `d_u,d_v ≥ 2` blocks the `{u,v} ∪ A′∖(N(u)∪N(v))` alternative), so this loophole is closed —
   but only for the configuration as I reconstructed it.

---

### Summary

The mathematics of the FAN chain survives a genuine attempt to break it: 22 million exhaustive
Fan degree sequences, 2.3 million more in secondary and extreme boxes, 52 556 adversarially
tie-broken labelled runs, 1.5 million abstract runs of FAN-6's induction, and a 111 742-graph
corpus for the underlying HH lemmas produced **zero** counterexamples, and every step of
FAN-1, FAN-3, FAN-4, FAN-6, FAN-7, FAN-8, Theorem FAN and Corollary FAN-HC checks out on
inspection. Repair F1 is the right repair and its (i)/(ii) diagnoses are correct. What F1
missed is that it deleted the offending sentence in **one** place and left the same claim
standing in **two** others (§7.8 F's "Numerical agreement", §7.8 A's FAN-3 proof), and F2
declared FAN-2 superseded without noticing that its proof is tie-incomplete at `j = L+1`.
Hence PARTIAL, not CLEAN — but no conclusion of the chain is threatened.
