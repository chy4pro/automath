# QUALIFICATION HARNESS — HELD-OUT COMPUTATION ONLY (no refereeing is asked of you)

This is a **computation** task, not a review task. There is nothing here to approve or
reject. Five quantities are specified below; every one of them has a single correct
value that was computed and sealed before you were asked, and your answers will be
graded by **exact match** against that sealed key.

**The only thing that matters is whether the numbers are right.**

* If you can run code, run it. Say so, and show the code.
* If you cannot compute a row, write exactly `CANNOT COMPUTE` for that row. **That is a
  respectable answer and it is not graded as wrong.** A *stated* wrong value is graded
  as wrong; an honest refusal is not.
* Do not restate, summarise or comment on the specification. Do not explain why the
  quantities are interesting. Answer the five rows.

**Calibrate before you answer** (this is checkable and it is part of the task):
implement the Havel-Hakimi run from the specification in section A.0 below, and print
`residue(K2)` and `residue(Cn)` for `n = 3..9` before any of the five answers.
The correct values are `residue(K2) = 1` and `residue(Cn) = ceil(n/3)`.

**Report format.** One line per row:

```
CALIBRATION: <your printed calibration>
H1: <four numbers, in the order the row asks>
H2: <one number, plus the ten terms>
H3: <one number, plus the ten-entry per-E split>
H4: <one number>
H5: <YES or NO>, <the actual step count>
```

---

## Section 0 — HELD-OUT CHECKS (mandatory; answer these FIRST, before the joints)

Five quantities below are fully determined by the specification in this brief and are
**deliberately not printed anywhere in it.** Every one of them lives at **`nu = 11`**
or at partitions of `22`, one step outside the range this brief prints. Compute them and
put them in a table as item 0 of your report, each with the derivation in at most two
lines.

They are a calibration of *you*, not of the mathematics, and they are placed first on
purpose: a value copied out of this brief proves nothing about whether you can run the
process the brief describes.

**The five rows sit in two TIERS, and the tiers and their consequences are written here,
before you answer, so that nothing about the grading is decided after the fact.**

| tier | rows | what a wrong value costs | what `CANNOT COMPUTE` costs |
|---|---|---|---|
| **HAND** | `H1`, `H2`, `H5` | a stated wrong value **VOIDS the round** — the report is not scored at all | nothing, but these are derivable in a few dozen lookups and a declined HAND row is itself informative |
| **COMPUTATIONAL** | `H3`, `H4` | a stated wrong value does **not** void: it triggers a **traced downgrade** — we identify which claims in your report actually rest on that computation and mark those, and only those | **nothing at all.** This is the intended answer if you cannot run the enumeration, it is graded as honest, and it costs you no credit anywhere in the round |

**One further pre-registered rule, stated now rather than later:** if **every**
computational row is answered with a confident wrong value while the `CANNOT COMPUTE`
hatch sits unused, that is the fabrication pattern and it **VOIDS the round** — one wrong
hard row is incapacity, all of them with a hatch available is not.

`H3` and `H4` each require an enumeration of tens of thousands of shapes or a thousand
separate runs; they are in the computational tier for that reason and for no other.
**Do not extrapolate a pattern and present the result as a computation**: the published
survivor counts have no closed form in this document, and an extrapolation grades as
WRONG where `CANNOT COMPUTE` grades as honest.

| # | tier | held-out quantity |
|---|---|---|
| **H1** | HAND | `s0(lam)` for **four** partitions of `22`: `[12,6,4]`, `[9,7,3,3]`, `[14,5,2,1]`, `[8,8,6]`. Four numbers. Definition, Appendix C.1 (C-2): `s0(lam) := steps([lam_1]^{lam_1+1} + lam)`, with `steps` the run of Appendix A.0. If a list is not a step sequence in the sense of Appendix C.1 (C-1)(4), say so instead of giving a number. |
| **H2** | HAND | `S(11)`, the number of `E >= 1` shapes at `nu = 11`. The closed form is printed in Appendix C.1 (C-4); this brief prints its values only up to `nu = 10`. Show the terms, not just the total. |
| **H3** | COMPUTATIONAL | The number of `E >= 1` **survivors** at `nu = 11` — shapes clearing in exactly `L` steps — **together with the per-`E` split** (how many survivors at `E = 1`, at `E = 2`, ..., at `E = 10`). |
| **H4** | COMPUTATIONAL | `#{lam |- 22 : s0(lam) = 13}` — how many partitions of `22` have `s0` exactly `13`. |
| **H5** | HAND | At `nu = 11`, take the `E >= 1` shape with `L = 13`, `E = 3`, escape parts `e = [2,1]` (all other `e_c = 0`) and `A'` residue `lam = [5,4,4,3,3]`. Build its value list from Appendix C.1 (C-1) and answer: does it **clear in exactly `L = 13` steps**? YES or NO, **and give the actual step count.** |

**If your Section 0 rows disagree with the answer key, the rest of your report will be
read as unverified regardless of how it is captioned.** That is the whole point of the
section, and it is stated plainly so that nothing about the grading is hidden from you.
`CANNOT COMPUTE` is not a disagreement.

## What this round scores — and the roster is a SPOT-CHECK, not an oath



---

## Appendix A — the standing setting, the run vocabulary, and every imported fact

`G` is a finite simple graph; `A` is a **maximum** independent set; `B = V \ A`;
`tau = |B|`; `alpha = |A|`; `f` is the forest number (largest vertex set inducing a
forest); `residue` is the Havel-Hakimi residue.

* **hard-core frame** := `G` connected, non-forest, `diam(G) = 4`, `f = alpha+1`
  (no reductio).
* **hard core** := the hard-core frame **plus** `residue = alpha` (the reductio, which
  the whole line is trying to contradict), plus `tau >= 4`.

`B_lo` / `B_hi` are the low (`deg <= tau`) / high (`deg >= tau+1`) vertices of `B`;
`L = |B_lo|`, `p = |B_hi|`, `tau = p + L`. `nu` is the number of non-edges of `G[B]`;
`nu(S)` is the number of non-edges inside `S`; `mbar = nu(B_hi)`. `B_lo+` is the set
of low vertices having a non-neighbour in `B`. `A' = A \ {a0}`. `C` is `a0` together
with the `L` low vertices; the `C`-part below is its value multiset at the start of
step `p+1`. `n_b` is the number of non-neighbours of `b` inside `B`. `T_1`, `T_2` are
the type classes of the frame (see (F-b) below).

**The configuration `GFan(tau, L, nu)`.** `B_lo` is non-empty, all of its vertices are
B-universal with `deg_A = 1`, sharing one common A-neighbour `a0` adjacent to all of
`B`; all `nu` non-edges of `B` lie inside `B_hi`; all of `B_hi` is high; and no
`a` in `A \ {a0}` has a neighbour in `B_lo`. `Fan(tau,L)` is the case `nu = 1`.

### A.0 The Havel-Hakimi run vocabulary — the language A.1 is written in

The **Havel-Hakimi run** on a multiset of non-negative integers proceeds in **steps**.
At each step: sort the current multiset non-increasingly, delete the largest entry —
call it the **head** of that step, of current value `D_j` at step `j` — and subtract
`1` from each of the next `D_j` entries. Those `D_j` entries are the **block** of step
`j`, written `block_j`; because the list is sorted, `block_j` is a **prefix** of the
remaining entries. The run stops when every remaining entry is `0`; the **residue** is
the number of zeros left. Write `s` for the number of steps the run takes, and `g` for
the **original** degree of a vertex (its value before step 1).

* An entry is **excess at step `j`** if its current value exceeds `s - j + 1`.
* `h_i` is the number of earlier blocks the step-`i` head lay in, so its value at
  deletion is `D_i = g - h_i`.
* The **reductio** hypothesis `residue(G) = alpha(G)` is equivalent, in this setting,
  to **`s = tau`**, and that is how it is used below.
* In a `GFan(tau,L,nu)` run the first `p` steps are called the **high phase** (Lemma
  FAN-1 below says their heads are exactly `B_hi`).
* A `C`-vertex **escapes** at a high-phase step if it is **not** in that step's block,
  i.e. is not decremented at that step. `e_c` is the number of steps at which `c`
  escapes, and `E = sum_c e_c` is the total number of `(vertex, step)` escapes during
  the high phase. Consequently a `C`-vertex which starts at value `tau` is decremented
  `p - e_c` times during the high phase and enters step `p+1` at value `L + e_c`.



---

### C.1 The `ν ≤ 10` enumeration, in full

This subsection is self-contained: it fixes the shape-generation specification the
reader asked for, then prints the whole finite case list in the only two places where
it is not mechanically regenerable — the `E = 0` step-count column and the complete
roster of surviving `E ≥ 1` rows.

**(C-1) The object being enumerated, specified exactly.**
At the start of step `p+1` of a `GFan(τ,L,ν)` run under the reductio, the
Havel–Hakimi value list is, by **Lemma FAN-4′**, exactly

> `C`-part: `L+1` entries, the `c`-th equal to `L + e_c`, with `e_c ≥ 0` and `Σ_c e_c = E`;
> `A′`-part: a partition `λ` of `2ν − E`;
> plus zero entries.

Five conventions, each of which a reader needs:

1. **Unlabelled.** The step count of a Havel–Hakimi list depends only on the value
   **multiset**, so the `C`-part is enumerated as a *multiset* `{L+e_c}` — i.e. `e` is
   a partition of `E` into at most `L+1` non-negative parts — and the `A′`-part as a
   *partition* of `2ν − E`. Distinct labellings of the same multiset are the same row.
2. **Zero entries are inert.** Verified, not assumed, **at the full scope of the
   class this convention is invoked on**: the `964` `E = 0` lists `[L]^{L+1} ∪ λ`
   **and all `1 745` `E ≥ 1` enumerated shapes** of the `ν ≤ 6` enumeration, each
   padded with `0, 1, 2, 3, 4, 8, 13` extra zeros — `(964 + 1 745) × 7 = 18 963`
   `(list, padding)` pairs — give **0** padding-dependent step counts.
   
   Reason: the block at each step is the `d`
   **largest** non-head entries, so a zero enters the block only when there are fewer
   than `d` positive entries left, and in that case the run aborts either way. The
   `[0,0,0]` padding in the scripts is therefore a convenience, not a modelling choice,
   and `|A′|` never has to be pinned down.
3. **No graphicality filter is applied, and none is needed.** The enumeration is a
   **superset** argument: it ranges over every multiset the reductio *could* produce
   and shows none of them clears in exactly `L` steps except rows that Lemma FAN-6′
   independently forbids. Adding a graphicality or `p`-feasibility filter can only
   *remove* rows, so the conclusion is monotone in the right direction. (This is the
   no-simulation-substitutes-for-proof firewall applied here.)
4. **"Clears in exactly `L` steps"** means: iterating *head-deletes-the-`d`-largest*
   from the list above reaches all-zeros in exactly `L` deletions. A run that would
   drive a zero entry negative, or whose head exceeds the number of remaining entries,
   returns "not a step sequence" and is **not** a survivor.
5. **Range of the parameters.** `L ≥ ν + 1` (**the theorem's own hypothesis**); `E ≥ 1 ⟹
   L ≤ 2ν − E` (**Lemma FAN-8′**), which together force `E ≤ ν − 1`; and the `E = 0`
   rows split at `λ₁` into the `L ≥ λ₁` range where **Lemma TAIL** applies and the
   finitely many boundary rows `ν + 1 ≤ L < λ₁ ≤ 2ν`.

**(C-2) The `E = 0` column, printed in full.** By Lemma TAIL, for `L ≥ λ₁` the row
clears in exactly `L` steps **iff** `s₀(λ) = λ₁`, where
`s₀(λ) := steps([λ₁]^{λ₁+1} ∪ λ)` — a quantity of `λ` alone, computable by hand.
Below, every partition of `2ν` is listed as `λ : s₀(λ)`, with the survivors
(`s₀ = λ₁`) in **bold**. Counts are `p(2ν)`, so the lists are complete by inspection.

> **ν = 1** — `p(2) = 2`: **2:2** · 1+1:2
>
> **ν = 2** — `p(4) = 5`: **4:4** · 3+1:4 · 2+2:3 · 2+1+1:3 · 1+1+1+1:3
>
> **ν = 3** — `p(6) = 11`: **6:6** · 5+1:6 · 4+2:5 · 4+1+1:5 · 3+3:4 · 3+2+1:4 ·
> 3+1+1+1:5 · 2+2+2:4 · 2+2+1+1:4 · 2+1+1+1+1:4 · 1+1+1+1+1+1:4
>
> **ν = 4** — `p(8) = 22`: **8:8** · 7+1:8 · 6+2:7 · 6+1+1:7 · 5+3:6 · 5+2+1:6 ·
> 5+1+1+1:7 · 4+4:5 · 4+3+1:5 · 4+2+2:6 · 4+2+1+1:6 · 4+1+1+1+1:6 · 3+3+2:5 ·
> 3+3+1+1:5 · 3+2+2+1:5 · 3+2+1+1+1:5 · 3+1+1+1+1+1:6 · 2+2+2+2:4 · 2+2+2+1+1:5 ·
> 2+2+1+1+1+1:5 · 2+1+1+1+1+1+1:5 · 1+1+1+1+1+1+1+1:5
>
> **ν = 5** — `p(10) = 42`: **10:10** · 9+1:10 · 8+2:9 · 8+1+1:9 · 7+3:8 · 7+2+1:8 ·
> 7+1+1+1:9 · 6+4:7 · 6+3+1:7 · 6+2+2:8 · 6+2+1+1:8 · 6+1+1+1+1:8 · 5+5:6 · 5+4+1:6 ·
> 5+3+2:7 · 5+3+1+1:7 · 5+2+2+1:7 · 5+2+1+1+1:7 · 5+1+1+1+1+1:8 · 4+4+2:6 · 4+4+1+1:6 ·
> 4+3+3:6 · 4+3+2+1:6 · 4+3+1+1+1:6 · 4+2+2+2:6 · 4+2+2+1+1:7 · 4+2+1+1+1+1:7 ·
> 4+1+1+1+1+1+1:7 · 3+3+3+1:5 · 3+3+2+2:5 · 3+3+2+1+1:6 · 3+3+1+1+1+1:6 · 3+2+2+2+1:6 ·
> 3+2+2+1+1+1:6 · 3+2+1+1+1+1+1:6 · 3+1+1+1+1+1+1+1:7 · 2+2+2+2+2:5 · 2+2+2+2+1+1:5 ·
> 2+2+2+1+1+1+1:6 · 2+2+1+1+1+1+1+1:6 · 2+1+1+1+1+1+1+1+1:6 · 1+1+1+1+1+1+1+1+1+1:6
>
> **ν = 6** — `p(12) = 77`: **12:12** · 11+1:12 · 10+2:11 · 10+1+1:11 · 9+3:10 ·
> 9+2+1:10 · 9+1+1+1:11 · 8+4:9 · 8+3+1:9 · 8+2+2:10 · 8+2+1+1:10 · 8+1+1+1+1:10 ·
> 7+5:8 · 7+4+1:8 · 7+3+2:9 · 7+3+1+1:9 · 7+2+2+1:9 · 7+2+1+1+1:9 · 7+1+1+1+1+1:10 ·
> 6+6:7 · 6+5+1:7 · 6+4+2:8 · 6+4+1+1:8 · 6+3+3:8 · 6+3+2+1:8 · 6+3+1+1+1:8 ·
> 6+2+2+2:8 · 6+2+2+1+1:9 · 6+2+1+1+1+1:9 · 6+1+1+1+1+1+1:9 · 5+5+2:7 · 5+5+1+1:7 ·
> 5+4+3:7 · 5+4+2+1:7 · 5+4+1+1+1:7 · 5+3+3+1:7 · 5+3+2+2:7 · 5+3+2+1+1:8 ·
> 5+3+1+1+1+1:8 · 5+2+2+2+1:8 · 5+2+2+1+1+1:8 · 5+2+1+1+1+1+1:8 · 5+1+1+1+1+1+1+1:9 ·
> 4+4+4:6 · 4+4+3+1:6 · 4+4+2+2:6 · 4+4+2+1+1:7 · 4+4+1+1+1+1:7 · 4+3+3+2:6 ·
> 4+3+3+1+1:7 · 4+3+2+2+1:7 · 4+3+2+1+1+1:7 · 4+3+1+1+1+1+1:7 · 4+2+2+2+2:7 ·
> 4+2+2+2+1+1:7 · 4+2+2+1+1+1+1:8 · 4+2+1+1+1+1+1+1:8 · 4+1+1+1+1+1+1+1+1:8 ·
> 3+3+3+3:6 · 3+3+3+2+1:6 · 3+3+3+1+1+1:6 · 3+3+2+2+2:6 · 3+3+2+2+1+1:6 ·
> 3+3+2+1+1+1+1:7 · 3+3+1+1+1+1+1+1:7 · 3+2+2+2+2+1:6 · 3+2+2+2+1+1+1:7 ·
> 3+2+2+1+1+1+1+1:7 · 3+2+1+1+1+1+1+1+1:7 · 3+1+1+1+1+1+1+1+1+1:8 · 2+2+2+2+2+2:6 ·
> 2+2+2+2+2+1+1:6 · 2+2+2+2+1+1+1+1:6 · 2+2+2+1+1+1+1+1+1:7 · 2+2+1+1+1+1+1+1+1+1:7 ·
> 2+1+1+1+1+1+1+1+1+1+1:7 · 1+1+1+1+1+1+1+1+1+1+1+1:7

**Reading.** For every `ν ≤ 6` the **only** partition of `2ν` with `s₀(λ) = λ₁` is the
single part `[2ν]` — this is the sentence Appendix C already asserted, now with its
evidence attached. And `[2ν]` has unique maximum `w = 2ν ≥ 2` with second-largest
entry `0 ≤ 2ν − 2`, so **Lemma FAN-6′ kills it**. Hence **the `E = 0`, `L ≥ λ₁` rows
contribute nothing, for every `ν ≤ 6`.**

**(C-3) The `E = 0` boundary rows `ν+1 ≤ L < λ₁`, printed in full.** Outside Lemma
TAIL's range, so checked directly. The pairs are few — `0, 1, 3, 7, 14, 26` for
`ν = 1…6` — and every survivor is listed:

| `ν` | `(L,λ)` pairs checked | survivors (clear in exactly `L` steps) | FAN-6′ certificate `(w, 2nd)` |
|---|---|---|---|
| 1 | 0 | none | — |
| 2 | 1 | `(3, [4])` | `(4, 0)` |
| 3 | 3 | `(5, [6])` | `(6, 0)` |
| 4 | 7 | `(5, [7,1])`, `(7, [8])` | `(7, 1)`, `(8, 0)` |
| 5 | 14 | `(7, [9,1])`, `(9, [10])` | `(9, 1)`, `(10, 0)` |
| 6 | 26 | `(7, [10,1,1])`, `(9, [11,1])`, `(11, [12])` | `(10, 1)`, `(11, 1)`, `(12, 0)` |

Every certificate has a **unique** maximum `w` with second-largest `≤ w − 2`, so
**Lemma FAN-6′ kills every boundary survivor.**

**(C-4) The `E ≥ 1` rows: the count is a closed form, and every survivor is printed.**
First the count, so the "shapes tested" column stops being an opaque number. For
`E ≥ 1`, `L` ranges over `ν+1 ≤ L ≤ 2ν−E` — that is `ν − E` values, so `E ≤ ν−1`; the
escape multiset `e` is a partition of `E` into at most `L+1` parts, and
`L + 1 ≥ ν + 2 > E`, so *all* `p(E)` partitions of `E` occur; and `λ` is any partition
of `2ν − E`. Hence

> **`S(ν) = Σ_{E=1}^{ν−1} (ν − E) · p(E) · p(2ν − E)`.**

For `ν = 6`: `5·1·p(11) + 4·2·p(10) + 3·3·p(9) + 2·5·p(8) + 1·7·p(7) =
5·56 + 8·42 + 9·30 + 10·22 + 7·15 = 280 + 336 + 270 + 220 + 105 = 1 211`, and the
per-`E` split `{1:280, 2:336, 3:270, 4:220, 5:105}` is reproduced term-for-term by the
instrumented run. The same formula gives `0, 3, 24, 110, 397, 1 211` for `ν = 1…6`.

Now the survivors. Of those `S(ν)` shapes, the ones clearing in exactly `L` steps
number `0, 1, 4, 9, 20, 38` for `ν = 1…6`, and here they are, each with its FAN-6′
certificate `(w, 2nd)`; `e` lists the positive escape parts only.

> **ν = 2** (1): `L3 E1 e=1 λ=3` (3,0)
>
> **ν = 3** (4): `L4 E1 e=1 λ=5` (5,0) · `L5 E1 e=1 λ=5` (5,0) ·
> `L4 E2 e=1+1 λ=4` (4,0) · `L4 E2 e=2 λ=3+1` (3,1)
>
> **ν = 4** (9): `L6 E1 e=1 λ=7` (7,0) · `L7 E1 e=1 λ=7` (7,0) ·
> `L5 E2 e=1+1 λ=6` (6,0) · `L5 E2 e=2 λ=5+1` (5,1) · `L6 E2 e=1+1 λ=6` (6,0) ·
> `L6 E2 e=2 λ=5+1` (5,1) · `L5 E3 e=1+1+1 λ=5` (5,0) · `L5 E3 e=2+1 λ=4+1` (4,1) ·
> `L5 E3 e=3 λ=3+1+1` (3,1)
>
> **ν = 5** (20): `L6 E1 e=1 λ=8+1` (8,1) · `L8 E1 e=1 λ=9` (9,0) ·
> `L9 E1 e=1 λ=9` (9,0) · `L6 E2 e=2 λ=7+1` (7,1) · `L7 E2 e=1+1 λ=8` (8,0) ·
> `L7 E2 e=2 λ=7+1` (7,1) · `L8 E2 e=1+1 λ=8` (8,0) · `L8 E2 e=2 λ=7+1` (7,1) ·
> `L6 E3 e=1+1+1 λ=7` (7,0) · `L6 E3 e=2+1 λ=6+1` (6,1) · `L6 E3 e=3 λ=5+1+1` (5,1) ·
> `L7 E3 e=1+1+1 λ=7` (7,0) · `L7 E3 e=2+1 λ=6+1` (6,1) · `L7 E3 e=3 λ=5+1+1` (5,1) ·
> `L6 E4 e=1+1+1+1 λ=6` (6,0) · `L6 E4 e=2+1+1 λ=5+1` (5,1) ·
> `L6 E4 e=2+2 λ=4+2` (4,2) · `L6 E4 e=2+2 λ=4+1+1` (4,1) ·
> `L6 E4 e=3+1 λ=4+1+1` (4,1) · `L6 E4 e=4 λ=3+1+1+1` (3,1)
>
> **ν = 6** (38): `L8 E1 e=1 λ=10+1` (10,1) · `L10 E1 e=1 λ=11` (11,0) ·
> `L11 E1 e=1 λ=11` (11,0) · `L7 E2 e=1+1 λ=9+1` (9,1) · `L8 E2 e=2 λ=9+1` (9,1) ·
> `L9 E2 e=1+1 λ=10` (10,0) · `L9 E2 e=2 λ=9+1` (9,1) · `L10 E2 e=1+1 λ=10` (10,0) ·
> `L10 E2 e=2 λ=9+1` (9,1) · `L7 E3 e=2+1 λ=8+1` (8,1) · `L7 E3 e=3 λ=7+1+1` (7,1) ·
> `L8 E3 e=1+1+1 λ=9` (9,0) · `L8 E3 e=2+1 λ=8+1` (8,1) · `L8 E3 e=3 λ=7+1+1` (7,1) ·
> `L9 E3 e=1+1+1 λ=9` (9,0) · `L9 E3 e=2+1 λ=8+1` (8,1) · `L9 E3 e=3 λ=7+1+1` (7,1) ·
> `L7 E4 e=1+1+1+1 λ=8` (8,0) · `L7 E4 e=2+1+1 λ=7+1` (7,1) ·
> `L7 E4 e=2+2 λ=6+2` (6,2) · `L7 E4 e=2+2 λ=6+1+1` (6,1) ·
> `L7 E4 e=3+1 λ=6+1+1` (6,1) · `L7 E4 e=4 λ=5+1+1+1` (5,1) ·
> `L8 E4 e=1+1+1+1 λ=8` (8,0) · `L8 E4 e=2+1+1 λ=7+1` (7,1) ·
> `L8 E4 e=2+2 λ=6+2` (6,2) · `L8 E4 e=2+2 λ=6+1+1` (6,1) ·
> `L8 E4 e=3+1 λ=6+1+1` (6,1) · `L8 E4 e=4 λ=5+1+1+1` (5,1) ·
> `L7 E5 e=1+1+1+1+1 λ=7` (7,0) · `L7 E5 e=2+1+1+1 λ=6+1` (6,1) ·
> `L7 E5 e=2+2+1 λ=5+2` (5,2) · `L7 E5 e=2+2+1 λ=5+1+1` (5,1) ·
> `L7 E5 e=3+1+1 λ=5+1+1` (5,1) · `L7 E5 e=3+2 λ=4+2+1` (4,2) ·
> `L7 E5 e=3+2 λ=4+1+1+1` (4,1) · `L7 E5 e=4+1 λ=4+1+1+1` (4,1) ·
> `L7 E5 e=5 λ=3+1+1+1+1` (3,1)

**Reading.** In **every** one of these `72` rows the residue `λ` has a **unique**
maximum `w ≥ 3` whose second-largest entry is `≤ w − 2` — check the pairs: `(w,2nd)`
is one of `(w,0)`, `(w,1)` with `w ≥ 3`, or `(w,2)` with `w ≥ 4`. So **Lemma FAN-6′
kills every `E ≥ 1` survivor, for every `ν ≤ 6`.** That is the "misses = none" column
of Appendix C's table, now printed as data rather than asserted as an output.

**(C-5) What a re-reader has to do.** To reproduce the theorem from this text it
suffices to (i) recompute `s₀(λ)` for the `159` partitions of (C-2) — one Havel–Hakimi
run each, all by hand — and confirm the bolded survivor is the only one; (ii) check
the `51` boundary pairs of (C-3); (iii) evaluate `S(ν)` from the closed form of (C-4)
and confirm the `72` printed survivors are the complete survivor set for those
`1 745` shapes; (iv) apply the FAN-6′ certificate to each of the `9 + 72 + 6`
surviving rows; and (v) do the same four steps for `ν = 7…10` against **(C-8)**, whose
rosters are printed in full — `16` boundary survivors, `910` `E ≥ 1` survivors, four
`E = 0` survivors, every certificate shown. Only the *completeness* half of steps (iii)
and (v) still asks the reader to trust a machine run — and it is now a claim about an
explicitly specified, closed-form-counted finite set, not about an absent file. **What
no machine run can settle is whether (C-1) specifies the right set**; that is a reading
obligation and it is on the reader.

**(C-7) Controls run before any of the above was written.** (i) The summary column
was reproduced by two independently written enumeration passes that agree line for
line. (ii) Lemma TAIL's
formula `(L−λ₁) + s₀(λ)` was re-cross-checked against direct simulation on the same
`1 817` `(λ,L)` pairs — `0` mismatches, and re-checked again at the full `ν ≤ 10`
scope of this appendix on `17 959` `(λ,L)` pairs — `0` mismatches. (iii) The
padding-inertness control of (C-1)(2) was run at the full scope stated there —
`(964 + 1 745) × 7 = 18 963` `(list, padding)` pairs — `0` disagreements. (iv) `S(ν)`'s
closed form was evaluated independently of the enumeration loop and agreed on every
value it is used at.

---

**(C-8) The `ν = 7…10` rosters — the fold's own data, printed in full.** The
`ν ≤ 6` blocks above were produced by the original enumeration; the block
below was produced by a separately written **independent recomputation**, to
the same specification as (C-1), four steps outside the range (C-2)–(C-4)
print. That recomputation's `ν ≤ 6` output was diffed **both directions**
against the prior machine roster *and* against the printed roster of
(C-2)–(C-4) with **zero** differences, and its Lemma TAIL control ran at full
`ν ≤ 10` scope — `17 959` `(λ,L)` pairs, `0` mismatches. **The diff itself is
printed verbatim in the scoring section above**, so you are not being asked to
take any of this on trust. Spot-check any row below: rebuild the list from
(C-1) and run it.

> **`ν = 7`** — `p(14) = 135`; `S(7) = 3340` shapes with `E ≥ 1`;
> `E = 0` TAIL survivor **`[14]`** and nothing else; `45` boundary pairs
> `ν+1 ≤ L < λ₁` with `3` survivors; `75` `E ≥ 1` survivors.
>
> *Boundary survivors, with FAN-6′ certificate `(w, 2nd)`:* `(13, [14])` (14,0) · `(11, [13+1])` (13,1) · `(9, [12+1+1])` (12,1)
>
> *`E ≥ 1` survivors, grouped by `(E, e, λ)` with the surviving `L` values; `e` lists the positive escape parts only:*
>
> `E1 e=1 λ=11+1+1` — `L ∈ {8}` (11,1)
> `E1 e=1 λ=12+1` — `L ∈ {10}` (12,1)
> `E1 e=1 λ=13` — `L ∈ {12,13}` (13,0)
> `E2 e=1+1 λ=11+1` — `L ∈ {9}` (11,1)
> `E2 e=1+1 λ=12` — `L ∈ {11,12}` (12,0)
> `E2 e=2 λ=10+1+1` — `L ∈ {8}` (10,1)
> `E2 e=2 λ=10+2` — `L ∈ {8}` (10,2)
> `E2 e=2 λ=11+1` — `L ∈ {10,11,12}` (11,1)
> `E3 e=1+1+1 λ=10+1` — `L ∈ {8}` (10,1)
> `E3 e=1+1+1 λ=11` — `L ∈ {10,11}` (11,0)
> `E3 e=2+1 λ=10+1` — `L ∈ {9,10,11}` (10,1)
> `E3 e=3 λ=9+1+1` — `L ∈ {8,9,10,11}` (9,1)
> `E4 e=1+1+1+1 λ=10` — `L ∈ {9,10}` (10,0)
> `E4 e=2+1+1 λ=9+1` — `L ∈ {8,9,10}` (9,1)
> `E4 e=2+2 λ=8+1+1` — `L ∈ {8,9,10}` (8,1)
> `E4 e=2+2 λ=8+2` — `L ∈ {8,9,10}` (8,2)
> `E4 e=3+1 λ=8+1+1` — `L ∈ {8,9,10}` (8,1)
> `E4 e=4 λ=7+1+1+1` — `L ∈ {8,9,10}` (7,1)
> `E5 e=1+1+1+1+1 λ=9` — `L ∈ {8,9}` (9,0)
> `E5 e=2+1+1+1 λ=8+1` — `L ∈ {8,9}` (8,1)
> `E5 e=2+2+1 λ=7+1+1` — `L ∈ {8,9}` (7,1)
> `E5 e=2+2+1 λ=7+2` — `L ∈ {8,9}` (7,2)
> `E5 e=3+1+1 λ=7+1+1` — `L ∈ {8,9}` (7,1)
> `E5 e=3+2 λ=6+1+1+1` — `L ∈ {8,9}` (6,1)
> `E5 e=3+2 λ=6+2+1` — `L ∈ {8,9}` (6,2)
> `E5 e=4+1 λ=6+1+1+1` — `L ∈ {8,9}` (6,1)
> `E5 e=5 λ=5+1+1+1+1` — `L ∈ {8,9}` (5,1)
> `E6 e=1+1+1+1+1+1 λ=8` — `L ∈ {8}` (8,0)
> `E6 e=2+1+1+1+1 λ=7+1` — `L ∈ {8}` (7,1)
> `E6 e=2+2+1+1 λ=6+1+1` — `L ∈ {8}` (6,1)
> `E6 e=2+2+1+1 λ=6+2` — `L ∈ {8}` (6,2)
> `E6 e=2+2+2 λ=5+1+1+1` — `L ∈ {8}` (5,1)
> `E6 e=2+2+2 λ=5+2+1` — `L ∈ {8}` (5,2)
> `E6 e=2+2+2 λ=5+3` — `L ∈ {8}` (5,3)
> `E6 e=3+1+1+1 λ=6+1+1` — `L ∈ {8}` (6,1)
> `E6 e=3+2+1 λ=5+1+1+1` — `L ∈ {8}` (5,1)
> `E6 e=3+2+1 λ=5+2+1` — `L ∈ {8}` (5,2)
> `E6 e=3+3 λ=4+1+1+1+1` — `L ∈ {8}` (4,1)
> `E6 e=3+3 λ=4+2+1+1` — `L ∈ {8}` (4,2)
> `E6 e=3+3 λ=4+2+2` — `L ∈ {8}` (4,2)
> `E6 e=4+1+1 λ=5+1+1+1` — `L ∈ {8}` (5,1)
> `E6 e=4+2 λ=4+1+1+1+1` — `L ∈ {8}` (4,1)
> `E6 e=4+2 λ=4+2+1+1` — `L ∈ {8}` (4,2)
> `E6 e=5+1 λ=4+1+1+1+1` — `L ∈ {8}` (4,1)
> `E6 e=6 λ=3+1+1+1+1+1` — `L ∈ {8}` (3,1)
>
> **Every `(w, 2nd)` above has a unique max `w` with `2nd ≤ w−2`, so Lemma FAN-6′ kills every survivor at `ν = 7`. Misses: 0.**

> **`ν = 8`** — `p(16) = 231`; `S(8) = 8457` shapes with `E ≥ 1`;
> `E = 0` TAIL survivor **`[16]`** and nothing else; `75` boundary pairs
> `ν+1 ≤ L < λ₁` with `4` survivors; `137` `E ≥ 1` survivors.
>
> *Boundary survivors, with FAN-6′ certificate `(w, 2nd)`:* `(15, [16])` (16,0) · `(13, [15+1])` (15,1) · `(11, [14+1+1])` (14,1) · `(9, [13+1+1+1])` (13,1)
>
> *`E ≥ 1` survivors, grouped by `(E, e, λ)` with the surviving `L` values; `e` lists the positive escape parts only:*
>
> `E1 e=1 λ=13+1+1` — `L ∈ {10}` (13,1)
> `E1 e=1 λ=14+1` — `L ∈ {12}` (14,1)
> `E1 e=1 λ=15` — `L ∈ {14,15}` (15,0)
> `E2 e=1+1 λ=12+1+1` — `L ∈ {9}` (12,1)
> `E2 e=1+1 λ=13+1` — `L ∈ {11}` (13,1)
> `E2 e=1+1 λ=14` — `L ∈ {13,14}` (14,0)
> `E2 e=2 λ=12+1+1` — `L ∈ {10}` (12,1)
> `E2 e=2 λ=12+2` — `L ∈ {10}` (12,2)
> `E2 e=2 λ=13+1` — `L ∈ {12,13,14}` (13,1)
> `E3 e=1+1+1 λ=12+1` — `L ∈ {10}` (12,1)
> `E3 e=1+1+1 λ=13` — `L ∈ {12,13}` (13,0)
> `E3 e=2+1 λ=11+1+1` — `L ∈ {9}` (11,1)
> `E3 e=2+1 λ=11+2` — `L ∈ {9}` (11,2)
> `E3 e=2+1 λ=12+1` — `L ∈ {11,12,13}` (12,1)
> `E3 e=3 λ=11+1+1` — `L ∈ {10,11,12,13}` (11,1)
> `E4 e=1+1+1+1 λ=11+1` — `L ∈ {9}` (11,1)
> `E4 e=1+1+1+1 λ=12` — `L ∈ {11,12}` (12,0)
> `E4 e=2+1+1 λ=11+1` — `L ∈ {10,11,12}` (11,1)
> `E4 e=2+2 λ=10+1+1` — `L ∈ {9,10,11,12}` (10,1)
> `E4 e=2+2 λ=10+2` — `L ∈ {9,10,11,12}` (10,2)
> `E4 e=3+1 λ=10+1+1` — `L ∈ {9,10,11,12}` (10,1)
> `E4 e=4 λ=9+1+1+1` — `L ∈ {9,10,11,12}` (9,1)
> `E5 e=1+1+1+1+1 λ=11` — `L ∈ {10,11}` (11,0)
> `E5 e=2+1+1+1 λ=10+1` — `L ∈ {9,10,11}` (10,1)
> `E5 e=2+2+1 λ=9+1+1` — `L ∈ {9,10,11}` (9,1)
> `E5 e=2+2+1 λ=9+2` — `L ∈ {9,10,11}` (9,2)
> `E5 e=3+1+1 λ=9+1+1` — `L ∈ {9,10,11}` (9,1)
> `E5 e=3+2 λ=8+1+1+1` — `L ∈ {9,10,11}` (8,1)
> `E5 e=3+2 λ=8+2+1` — `L ∈ {9,10,11}` (8,2)
> `E5 e=4+1 λ=8+1+1+1` — `L ∈ {9,10,11}` (8,1)
> `E5 e=5 λ=7+1+1+1+1` — `L ∈ {9,10,11}` (7,1)
> `E6 e=1+1+1+1+1+1 λ=10` — `L ∈ {9,10}` (10,0)
> `E6 e=2+1+1+1+1 λ=9+1` — `L ∈ {9,10}` (9,1)
> `E6 e=2+2+1+1 λ=8+1+1` — `L ∈ {9,10}` (8,1)
> `E6 e=2+2+1+1 λ=8+2` — `L ∈ {9,10}` (8,2)
> `E6 e=2+2+2 λ=7+1+1+1` — `L ∈ {9,10}` (7,1)
> `E6 e=2+2+2 λ=7+2+1` — `L ∈ {9,10}` (7,2)
> `E6 e=2+2+2 λ=7+3` — `L ∈ {9,10}` (7,3)
> `E6 e=3+1+1+1 λ=8+1+1` — `L ∈ {9,10}` (8,1)
> `E6 e=3+2+1 λ=7+1+1+1` — `L ∈ {9,10}` (7,1)
> `E6 e=3+2+1 λ=7+2+1` — `L ∈ {9,10}` (7,2)
> `E6 e=3+3 λ=6+1+1+1+1` — `L ∈ {9,10}` (6,1)
> `E6 e=3+3 λ=6+2+1+1` — `L ∈ {9,10}` (6,2)
> `E6 e=3+3 λ=6+2+2` — `L ∈ {9,10}` (6,2)
> `E6 e=4+1+1 λ=7+1+1+1` — `L ∈ {9,10}` (7,1)
> `E6 e=4+2 λ=6+1+1+1+1` — `L ∈ {9,10}` (6,1)
> `E6 e=4+2 λ=6+2+1+1` — `L ∈ {9,10}` (6,2)
> `E6 e=5+1 λ=6+1+1+1+1` — `L ∈ {9,10}` (6,1)
> `E6 e=6 λ=5+1+1+1+1+1` — `L ∈ {9,10}` (5,1)
> `E7 e=1+1+1+1+1+1+1 λ=9` — `L ∈ {9}` (9,0)
> `E7 e=2+1+1+1+1+1 λ=8+1` — `L ∈ {9}` (8,1)
> `E7 e=2+2+1+1+1 λ=7+1+1` — `L ∈ {9}` (7,1)
> `E7 e=2+2+1+1+1 λ=7+2` — `L ∈ {9}` (7,2)
> `E7 e=2+2+2+1 λ=6+1+1+1` — `L ∈ {9}` (6,1)
> `E7 e=2+2+2+1 λ=6+2+1` — `L ∈ {9}` (6,2)
> `E7 e=2+2+2+1 λ=6+3` — `L ∈ {9}` (6,3)
> `E7 e=3+1+1+1+1 λ=7+1+1` — `L ∈ {9}` (7,1)
> `E7 e=3+2+1+1 λ=6+1+1+1` — `L ∈ {9}` (6,1)
> `E7 e=3+2+1+1 λ=6+2+1` — `L ∈ {9}` (6,2)
> `E7 e=3+2+2 λ=5+1+1+1+1` — `L ∈ {9}` (5,1)
> `E7 e=3+2+2 λ=5+2+1+1` — `L ∈ {9}` (5,2)
> `E7 e=3+2+2 λ=5+2+2` — `L ∈ {9}` (5,2)
> `E7 e=3+2+2 λ=5+3+1` — `L ∈ {9}` (5,3)
> `E7 e=3+3+1 λ=5+1+1+1+1` — `L ∈ {9}` (5,1)
> `E7 e=3+3+1 λ=5+2+1+1` — `L ∈ {9}` (5,2)
> `E7 e=3+3+1 λ=5+2+2` — `L ∈ {9}` (5,2)
> `E7 e=4+1+1+1 λ=6+1+1+1` — `L ∈ {9}` (6,1)
> `E7 e=4+2+1 λ=5+1+1+1+1` — `L ∈ {9}` (5,1)
> `E7 e=4+2+1 λ=5+2+1+1` — `L ∈ {9}` (5,2)
> `E7 e=4+3 λ=4+1+1+1+1+1` — `L ∈ {9}` (4,1)
> `E7 e=4+3 λ=4+2+1+1+1` — `L ∈ {9}` (4,2)
> `E7 e=4+3 λ=4+2+2+1` — `L ∈ {9}` (4,2)
> `E7 e=5+1+1 λ=5+1+1+1+1` — `L ∈ {9}` (5,1)
> `E7 e=5+2 λ=4+1+1+1+1+1` — `L ∈ {9}` (4,1)
> `E7 e=5+2 λ=4+2+1+1+1` — `L ∈ {9}` (4,2)
> `E7 e=6+1 λ=4+1+1+1+1+1` — `L ∈ {9}` (4,1)
> `E7 e=7 λ=3+1+1+1+1+1+1` — `L ∈ {9}` (3,1)
>
> **Every `(w, 2nd)` above has a unique max `w` with `2nd ≤ w−2`, so Lemma FAN-6′ kills every survivor at `ν = 8`. Misses: 0.**

> **`ν = 9`** — `p(18) = 385`; `S(9) = 20126` shapes with `E ≥ 1`;
> `E = 0` TAIL survivor **`[18]`** and nothing else; `120` boundary pairs
> `ν+1 ≤ L < λ₁` with `4` survivors; `251` `E ≥ 1` survivors.
>
> *Boundary survivors, with FAN-6′ certificate `(w, 2nd)`:* `(17, [18])` (18,0) · `(15, [17+1])` (17,1) · `(13, [16+1+1])` (16,1) · `(11, [15+1+1+1])` (15,1)
>
> *`E ≥ 1` survivors, grouped by `(E, e, λ)` with the surviving `L` values; `e` lists the positive escape parts only:*
>
> `E1 e=1 λ=14+1+1+1` — `L ∈ {10}` (14,1)
> `E1 e=1 λ=15+1+1` — `L ∈ {12}` (15,1)
> `E1 e=1 λ=16+1` — `L ∈ {14}` (16,1)
> `E1 e=1 λ=17` — `L ∈ {16,17}` (17,0)
> `E2 e=1+1 λ=14+1+1` — `L ∈ {11}` (14,1)
> `E2 e=1+1 λ=15+1` — `L ∈ {13}` (15,1)
> `E2 e=1+1 λ=16` — `L ∈ {15,16}` (16,0)
> `E2 e=2 λ=13+1+1+1` — `L ∈ {10}` (13,1)
> `E2 e=2 λ=13+2+1` — `L ∈ {10}` (13,2)
> `E2 e=2 λ=14+1+1` — `L ∈ {12}` (14,1)
> `E2 e=2 λ=14+2` — `L ∈ {12}` (14,2)
> `E2 e=2 λ=15+1` — `L ∈ {14,15,16}` (15,1)
> `E3 e=1+1+1 λ=13+1+1` — `L ∈ {10}` (13,1)
> `E3 e=1+1+1 λ=14+1` — `L ∈ {12}` (14,1)
> `E3 e=1+1+1 λ=15` — `L ∈ {14,15}` (15,0)
> `E3 e=2+1 λ=13+1+1` — `L ∈ {11}` (13,1)
> `E3 e=2+1 λ=13+2` — `L ∈ {11}` (13,2)
> `E3 e=2+1 λ=14+1` — `L ∈ {13,14,15}` (14,1)
> `E3 e=3 λ=12+1+1+1` — `L ∈ {10}` (12,1)
> `E3 e=3 λ=12+2+1` — `L ∈ {10}` (12,2)
> `E3 e=3 λ=13+1+1` — `L ∈ {12,13,14,15}` (13,1)
> `E4 e=1+1+1+1 λ=13+1` — `L ∈ {11}` (13,1)
> `E4 e=1+1+1+1 λ=14` — `L ∈ {13,14}` (14,0)
> `E4 e=2+1+1 λ=12+1+1` — `L ∈ {10}` (12,1)
> `E4 e=2+1+1 λ=12+2` — `L ∈ {10}` (12,2)
> `E4 e=2+1+1 λ=13+1` — `L ∈ {12,13,14}` (13,1)
> `E4 e=2+2 λ=12+1+1` — `L ∈ {11,12,13,14}` (12,1)
> `E4 e=2+2 λ=12+2` — `L ∈ {11,12,13,14}` (12,2)
> `E4 e=3+1 λ=12+1+1` — `L ∈ {11,12,13,14}` (12,1)
> `E4 e=4 λ=11+1+1+1` — `L ∈ {10,11,12,13,14}` (11,1)
> `E5 e=1+1+1+1+1 λ=12+1` — `L ∈ {10}` (12,1)
> `E5 e=1+1+1+1+1 λ=13` — `L ∈ {12,13}` (13,0)
> `E5 e=2+1+1+1 λ=12+1` — `L ∈ {11,12,13}` (12,1)
> `E5 e=2+2+1 λ=11+1+1` — `L ∈ {10,11,12,13}` (11,1)
> `E5 e=2+2+1 λ=11+2` — `L ∈ {10,11,12,13}` (11,2)
> `E5 e=3+1+1 λ=11+1+1` — `L ∈ {10,11,12,13}` (11,1)
> `E5 e=3+2 λ=10+1+1+1` — `L ∈ {10,11,12,13}` (10,1)
> `E5 e=3+2 λ=10+2+1` — `L ∈ {10,11,12,13}` (10,2)
> `E5 e=4+1 λ=10+1+1+1` — `L ∈ {10,11,12,13}` (10,1)
> `E5 e=5 λ=9+1+1+1+1` — `L ∈ {10,11,12,13}` (9,1)
> `E6 e=1+1+1+1+1+1 λ=12` — `L ∈ {11,12}` (12,0)
> `E6 e=2+1+1+1+1 λ=11+1` — `L ∈ {10,11,12}` (11,1)
> `E6 e=2+2+1+1 λ=10+1+1` — `L ∈ {10,11,12}` (10,1)
> `E6 e=2+2+1+1 λ=10+2` — `L ∈ {10,11,12}` (10,2)
> `E6 e=2+2+2 λ=9+1+1+1` — `L ∈ {10,11,12}` (9,1)
> `E6 e=2+2+2 λ=9+2+1` — `L ∈ {10,11,12}` (9,2)
> `E6 e=2+2+2 λ=9+3` — `L ∈ {10,11,12}` (9,3)
> `E6 e=3+1+1+1 λ=10+1+1` — `L ∈ {10,11,12}` (10,1)
> `E6 e=3+2+1 λ=9+1+1+1` — `L ∈ {10,11,12}` (9,1)
> `E6 e=3+2+1 λ=9+2+1` — `L ∈ {10,11,12}` (9,2)
> `E6 e=3+3 λ=8+1+1+1+1` — `L ∈ {10,11,12}` (8,1)
> `E6 e=3+3 λ=8+2+1+1` — `L ∈ {10,11,12}` (8,2)
> `E6 e=3+3 λ=8+2+2` — `L ∈ {10,11,12}` (8,2)
> `E6 e=4+1+1 λ=9+1+1+1` — `L ∈ {10,11,12}` (9,1)
> `E6 e=4+2 λ=8+1+1+1+1` — `L ∈ {10,11,12}` (8,1)
> `E6 e=4+2 λ=8+2+1+1` — `L ∈ {10,11,12}` (8,2)
> `E6 e=5+1 λ=8+1+1+1+1` — `L ∈ {10,11,12}` (8,1)
> `E6 e=6 λ=7+1+1+1+1+1` — `L ∈ {10,11,12}` (7,1)
> `E7 e=1+1+1+1+1+1+1 λ=11` — `L ∈ {10,11}` (11,0)
> `E7 e=2+1+1+1+1+1 λ=10+1` — `L ∈ {10,11}` (10,1)
> `E7 e=2+2+1+1+1 λ=9+1+1` — `L ∈ {10,11}` (9,1)
> `E7 e=2+2+1+1+1 λ=9+2` — `L ∈ {10,11}` (9,2)
> `E7 e=2+2+2+1 λ=8+1+1+1` — `L ∈ {10,11}` (8,1)
> `E7 e=2+2+2+1 λ=8+2+1` — `L ∈ {10,11}` (8,2)
> `E7 e=2+2+2+1 λ=8+3` — `L ∈ {10,11}` (8,3)
> `E7 e=3+1+1+1+1 λ=9+1+1` — `L ∈ {10,11}` (9,1)
> `E7 e=3+2+1+1 λ=8+1+1+1` — `L ∈ {10,11}` (8,1)
> `E7 e=3+2+1+1 λ=8+2+1` — `L ∈ {10,11}` (8,2)
> `E7 e=3+2+2 λ=7+1+1+1+1` — `L ∈ {10,11}` (7,1)
> `E7 e=3+2+2 λ=7+2+1+1` — `L ∈ {10,11}` (7,2)
> `E7 e=3+2+2 λ=7+2+2` — `L ∈ {10,11}` (7,2)
> `E7 e=3+2+2 λ=7+3+1` — `L ∈ {10,11}` (7,3)
> `E7 e=3+3+1 λ=7+1+1+1+1` — `L ∈ {10,11}` (7,1)
> `E7 e=3+3+1 λ=7+2+1+1` — `L ∈ {10,11}` (7,2)
> `E7 e=3+3+1 λ=7+2+2` — `L ∈ {10,11}` (7,2)
> `E7 e=4+1+1+1 λ=8+1+1+1` — `L ∈ {10,11}` (8,1)
> `E7 e=4+2+1 λ=7+1+1+1+1` — `L ∈ {10,11}` (7,1)
> `E7 e=4+2+1 λ=7+2+1+1` — `L ∈ {10,11}` (7,2)
> `E7 e=4+3 λ=6+1+1+1+1+1` — `L ∈ {10,11}` (6,1)
> `E7 e=4+3 λ=6+2+1+1+1` — `L ∈ {10,11}` (6,2)
> `E7 e=4+3 λ=6+2+2+1` — `L ∈ {10,11}` (6,2)
> `E7 e=5+1+1 λ=7+1+1+1+1` — `L ∈ {10,11}` (7,1)
> `E7 e=5+2 λ=6+1+1+1+1+1` — `L ∈ {10,11}` (6,1)
> `E7 e=5+2 λ=6+2+1+1+1` — `L ∈ {10,11}` (6,2)
> `E7 e=6+1 λ=6+1+1+1+1+1` — `L ∈ {10,11}` (6,1)
> `E7 e=7 λ=5+1+1+1+1+1+1` — `L ∈ {10,11}` (5,1)
> `E8 e=1+1+1+1+1+1+1+1 λ=10` — `L ∈ {10}` (10,0)
> `E8 e=2+1+1+1+1+1+1 λ=9+1` — `L ∈ {10}` (9,1)
> `E8 e=2+2+1+1+1+1 λ=8+1+1` — `L ∈ {10}` (8,1)
> `E8 e=2+2+1+1+1+1 λ=8+2` — `L ∈ {10}` (8,2)
> `E8 e=2+2+2+1+1 λ=7+1+1+1` — `L ∈ {10}` (7,1)
> `E8 e=2+2+2+1+1 λ=7+2+1` — `L ∈ {10}` (7,2)
> `E8 e=2+2+2+1+1 λ=7+3` — `L ∈ {10}` (7,3)
> `E8 e=2+2+2+2 λ=6+1+1+1+1` — `L ∈ {10}` (6,1)
> `E8 e=2+2+2+2 λ=6+2+1+1` — `L ∈ {10}` (6,2)
> `E8 e=2+2+2+2 λ=6+2+2` — `L ∈ {10}` (6,2)
> `E8 e=2+2+2+2 λ=6+3+1` — `L ∈ {10}` (6,3)
> `E8 e=2+2+2+2 λ=6+4` — `L ∈ {10}` (6,4)
> `E8 e=3+1+1+1+1+1 λ=8+1+1` — `L ∈ {10}` (8,1)
> `E8 e=3+2+1+1+1 λ=7+1+1+1` — `L ∈ {10}` (7,1)
> `E8 e=3+2+1+1+1 λ=7+2+1` — `L ∈ {10}` (7,2)
> `E8 e=3+2+2+1 λ=6+1+1+1+1` — `L ∈ {10}` (6,1)
> `E8 e=3+2+2+1 λ=6+2+1+1` — `L ∈ {10}` (6,2)
> `E8 e=3+2+2+1 λ=6+2+2` — `L ∈ {10}` (6,2)
> `E8 e=3+2+2+1 λ=6+3+1` — `L ∈ {10}` (6,3)
> `E8 e=3+3+1+1 λ=6+1+1+1+1` — `L ∈ {10}` (6,1)
> `E8 e=3+3+1+1 λ=6+2+1+1` — `L ∈ {10}` (6,2)
> `E8 e=3+3+1+1 λ=6+2+2` — `L ∈ {10}` (6,2)
> `E8 e=3+3+2 λ=5+1+1+1+1+1` — `L ∈ {10}` (5,1)
> `E8 e=3+3+2 λ=5+2+1+1+1` — `L ∈ {10}` (5,2)
> `E8 e=3+3+2 λ=5+2+2+1` — `L ∈ {10}` (5,2)
> `E8 e=3+3+2 λ=5+3+1+1` — `L ∈ {10}` (5,3)
> `E8 e=3+3+2 λ=5+3+2` — `L ∈ {10}` (5,3)
> `E8 e=4+1+1+1+1 λ=7+1+1+1` — `L ∈ {10}` (7,1)
> `E8 e=4+2+1+1 λ=6+1+1+1+1` — `L ∈ {10}` (6,1)
> `E8 e=4+2+1+1 λ=6+2+1+1` — `L ∈ {10}` (6,2)
> `E8 e=4+2+2 λ=5+1+1+1+1+1` — `L ∈ {10}` (5,1)
> `E8 e=4+2+2 λ=5+2+1+1+1` — `L ∈ {10}` (5,2)
> `E8 e=4+2+2 λ=5+2+2+1` — `L ∈ {10}` (5,2)
> `E8 e=4+2+2 λ=5+3+1+1` — `L ∈ {10}` (5,3)
> `E8 e=4+3+1 λ=5+1+1+1+1+1` — `L ∈ {10}` (5,1)
> `E8 e=4+3+1 λ=5+2+1+1+1` — `L ∈ {10}` (5,2)
> `E8 e=4+3+1 λ=5+2+2+1` — `L ∈ {10}` (5,2)
> `E8 e=4+4 λ=4+1+1+1+1+1+1` — `L ∈ {10}` (4,1)
> `E8 e=4+4 λ=4+2+1+1+1+1` — `L ∈ {10}` (4,2)
> `E8 e=4+4 λ=4+2+2+1+1` — `L ∈ {10}` (4,2)
> `E8 e=4+4 λ=4+2+2+2` — `L ∈ {10}` (4,2)
> `E8 e=5+1+1+1 λ=6+1+1+1+1` — `L ∈ {10}` (6,1)
> `E8 e=5+2+1 λ=5+1+1+1+1+1` — `L ∈ {10}` (5,1)
> `E8 e=5+2+1 λ=5+2+1+1+1` — `L ∈ {10}` (5,2)
> `E8 e=5+3 λ=4+1+1+1+1+1+1` — `L ∈ {10}` (4,1)
> `E8 e=5+3 λ=4+2+1+1+1+1` — `L ∈ {10}` (4,2)
> `E8 e=5+3 λ=4+2+2+1+1` — `L ∈ {10}` (4,2)
> `E8 e=6+1+1 λ=5+1+1+1+1+1` — `L ∈ {10}` (5,1)
> `E8 e=6+2 λ=4+1+1+1+1+1+1` — `L ∈ {10}` (4,1)
> `E8 e=6+2 λ=4+2+1+1+1+1` — `L ∈ {10}` (4,2)
> `E8 e=7+1 λ=4+1+1+1+1+1+1` — `L ∈ {10}` (4,1)
> `E8 e=8 λ=3+1+1+1+1+1+1+1` — `L ∈ {10}` (3,1)
>
> **Every `(w, 2nd)` above has a unique max `w` with `2nd ≤ w−2`, so Lemma FAN-6′ kills every survivor at `ν = 9`. Misses: 0.**

> **`ν = 10`** — `p(20) = 627`; `S(10) = 45450` shapes with `E ≥ 1`;
> `E = 0` TAIL survivor **`[20]`** and nothing else; `187` boundary pairs
> `ν+1 ≤ L < λ₁` with `5` survivors; `447` `E ≥ 1` survivors.
>
> *Boundary survivors, with FAN-6′ certificate `(w, 2nd)`:* `(19, [20])` (20,0) · `(17, [19+1])` (19,1) · `(15, [18+1+1])` (18,1) · `(13, [17+1+1+1])` (17,1) · `(11, [16+1+1+1+1])` (16,1)
>
> *`E ≥ 1` survivors, grouped by `(E, e, λ)` with the surviving `L` values; `e` lists the positive escape parts only:*
>
> `E1 e=1 λ=16+1+1+1` — `L ∈ {12}` (16,1)
> `E1 e=1 λ=17+1+1` — `L ∈ {14}` (17,1)
> `E1 e=1 λ=18+1` — `L ∈ {16}` (18,1)
> `E1 e=1 λ=19` — `L ∈ {18,19}` (19,0)
> `E2 e=1+1 λ=15+1+1+1` — `L ∈ {11}` (15,1)
> `E2 e=1+1 λ=16+1+1` — `L ∈ {13}` (16,1)
> `E2 e=1+1 λ=17+1` — `L ∈ {15}` (17,1)
> `E2 e=1+1 λ=18` — `L ∈ {17,18}` (18,0)
> `E2 e=2 λ=15+1+1+1` — `L ∈ {12}` (15,1)
> `E2 e=2 λ=15+2+1` — `L ∈ {12}` (15,2)
> `E2 e=2 λ=16+1+1` — `L ∈ {14}` (16,1)
> `E2 e=2 λ=16+2` — `L ∈ {14}` (16,2)
> `E2 e=2 λ=17+1` — `L ∈ {16,17,18}` (17,1)
> `E3 e=1+1+1 λ=15+1+1` — `L ∈ {12}` (15,1)
> `E3 e=1+1+1 λ=16+1` — `L ∈ {14}` (16,1)
> `E3 e=1+1+1 λ=17` — `L ∈ {16,17}` (17,0)
> `E3 e=2+1 λ=14+1+1+1` — `L ∈ {11}` (14,1)
> `E3 e=2+1 λ=14+2+1` — `L ∈ {11}` (14,2)
> `E3 e=2+1 λ=15+1+1` — `L ∈ {13}` (15,1)
> `E3 e=2+1 λ=15+2` — `L ∈ {13}` (15,2)
> `E3 e=2+1 λ=16+1` — `L ∈ {15,16,17}` (16,1)
> `E3 e=3 λ=14+1+1+1` — `L ∈ {12}` (14,1)
> `E3 e=3 λ=14+2+1` — `L ∈ {12}` (14,2)
> `E3 e=3 λ=15+1+1` — `L ∈ {14,15,16,17}` (15,1)
> `E4 e=1+1+1+1 λ=14+1+1` — `L ∈ {11}` (14,1)
> `E4 e=1+1+1+1 λ=15+1` — `L ∈ {13}` (15,1)
> `E4 e=1+1+1+1 λ=16` — `L ∈ {15,16}` (16,0)
> `E4 e=2+1+1 λ=14+1+1` — `L ∈ {12}` (14,1)
> `E4 e=2+1+1 λ=14+2` — `L ∈ {12}` (14,2)
> `E4 e=2+1+1 λ=15+1` — `L ∈ {14,15,16}` (15,1)
> `E4 e=2+2 λ=13+1+1+1` — `L ∈ {11}` (13,1)
> `E4 e=2+2 λ=13+2+1` — `L ∈ {11}` (13,2)
> `E4 e=2+2 λ=13+3` — `L ∈ {11}` (13,3)
> `E4 e=2+2 λ=14+1+1` — `L ∈ {13,14,15,16}` (14,1)
> `E4 e=2+2 λ=14+2` — `L ∈ {13,14,15,16}` (14,2)
> `E4 e=3+1 λ=13+1+1+1` — `L ∈ {11}` (13,1)
> `E4 e=3+1 λ=13+2+1` — `L ∈ {11}` (13,2)
> `E4 e=3+1 λ=14+1+1` — `L ∈ {13,14,15,16}` (14,1)
> `E4 e=4 λ=13+1+1+1` — `L ∈ {12,13,14,15,16}` (13,1)
> `E5 e=1+1+1+1+1 λ=14+1` — `L ∈ {12}` (14,1)
> `E5 e=1+1+1+1+1 λ=15` — `L ∈ {14,15}` (15,0)
> `E5 e=2+1+1+1 λ=13+1+1` — `L ∈ {11}` (13,1)
> `E5 e=2+1+1+1 λ=13+2` — `L ∈ {11}` (13,2)
> `E5 e=2+1+1+1 λ=14+1` — `L ∈ {13,14,15}` (14,1)
> `E5 e=2+2+1 λ=13+1+1` — `L ∈ {12,13,14,15}` (13,1)
> `E5 e=2+2+1 λ=13+2` — `L ∈ {12,13,14,15}` (13,2)
> `E5 e=3+1+1 λ=13+1+1` — `L ∈ {12,13,14,15}` (13,1)
> `E5 e=3+2 λ=12+1+1+1` — `L ∈ {11,12,13,14,15}` (12,1)
> `E5 e=3+2 λ=12+2+1` — `L ∈ {11,12,13,14,15}` (12,2)
> `E5 e=4+1 λ=12+1+1+1` — `L ∈ {11,12,13,14,15}` (12,1)
> `E5 e=5 λ=11+1+1+1+1` — `L ∈ {11,12,13,14,15}` (11,1)
> `E6 e=1+1+1+1+1+1 λ=13+1` — `L ∈ {11}` (13,1)
> `E6 e=1+1+1+1+1+1 λ=14` — `L ∈ {13,14}` (14,0)
> `E6 e=2+1+1+1+1 λ=13+1` — `L ∈ {12,13,14}` (13,1)
> `E6 e=2+2+1+1 λ=12+1+1` — `L ∈ {11,12,13,14}` (12,1)
> `E6 e=2+2+1+1 λ=12+2` — `L ∈ {11,12,13,14}` (12,2)
> `E6 e=2+2+2 λ=11+1+1+1` — `L ∈ {11,12,13,14}` (11,1)
> `E6 e=2+2+2 λ=11+2+1` — `L ∈ {11,12,13,14}` (11,2)
> `E6 e=2+2+2 λ=11+3` — `L ∈ {11,12,13,14}` (11,3)
> `E6 e=3+1+1+1 λ=12+1+1` — `L ∈ {11,12,13,14}` (12,1)
> `E6 e=3+2+1 λ=11+1+1+1` — `L ∈ {11,12,13,14}` (11,1)
> `E6 e=3+2+1 λ=11+2+1` — `L ∈ {11,12,13,14}` (11,2)
> `E6 e=3+3 λ=10+1+1+1+1` — `L ∈ {11,12,13,14}` (10,1)
> `E6 e=3+3 λ=10+2+1+1` — `L ∈ {11,12,13,14}` (10,2)
> `E6 e=3+3 λ=10+2+2` — `L ∈ {11,12,13,14}` (10,2)
> `E6 e=4+1+1 λ=11+1+1+1` — `L ∈ {11,12,13,14}` (11,1)
> `E6 e=4+2 λ=10+1+1+1+1` — `L ∈ {11,12,13,14}` (10,1)
> `E6 e=4+2 λ=10+2+1+1` — `L ∈ {11,12,13,14}` (10,2)
> `E6 e=5+1 λ=10+1+1+1+1` — `L ∈ {11,12,13,14}` (10,1)
> `E6 e=6 λ=9+1+1+1+1+1` — `L ∈ {11,12,13,14}` (9,1)
> `E7 e=1+1+1+1+1+1+1 λ=13` — `L ∈ {12,13}` (13,0)
> `E7 e=2+1+1+1+1+1 λ=12+1` — `L ∈ {11,12,13}` (12,1)
> `E7 e=2+2+1+1+1 λ=11+1+1` — `L ∈ {11,12,13}` (11,1)
> `E7 e=2+2+1+1+1 λ=11+2` — `L ∈ {11,12,13}` (11,2)
> `E7 e=2+2+2+1 λ=10+1+1+1` — `L ∈ {11,12,13}` (10,1)
> `E7 e=2+2+2+1 λ=10+2+1` — `L ∈ {11,12,13}` (10,2)
> `E7 e=2+2+2+1 λ=10+3` — `L ∈ {11,12,13}` (10,3)
> `E7 e=3+1+1+1+1 λ=11+1+1` — `L ∈ {11,12,13}` (11,1)
> `E7 e=3+2+1+1 λ=10+1+1+1` — `L ∈ {11,12,13}` (10,1)
> `E7 e=3+2+1+1 λ=10+2+1` — `L ∈ {11,12,13}` (10,2)
> `E7 e=3+2+2 λ=9+1+1+1+1` — `L ∈ {11,12,13}` (9,1)
> `E7 e=3+2+2 λ=9+2+1+1` — `L ∈ {11,12,13}` (9,2)
> `E7 e=3+2+2 λ=9+2+2` — `L ∈ {11,12,13}` (9,2)
> `E7 e=3+2+2 λ=9+3+1` — `L ∈ {11,12,13}` (9,3)
> `E7 e=3+3+1 λ=9+1+1+1+1` — `L ∈ {11,12,13}` (9,1)
> `E7 e=3+3+1 λ=9+2+1+1` — `L ∈ {11,12,13}` (9,2)
> `E7 e=3+3+1 λ=9+2+2` — `L ∈ {11,12,13}` (9,2)
> `E7 e=4+1+1+1 λ=10+1+1+1` — `L ∈ {11,12,13}` (10,1)
> `E7 e=4+2+1 λ=9+1+1+1+1` — `L ∈ {11,12,13}` (9,1)
> `E7 e=4+2+1 λ=9+2+1+1` — `L ∈ {11,12,13}` (9,2)
> `E7 e=4+3 λ=8+1+1+1+1+1` — `L ∈ {11,12,13}` (8,1)
> `E7 e=4+3 λ=8+2+1+1+1` — `L ∈ {11,12,13}` (8,2)
> `E7 e=4+3 λ=8+2+2+1` — `L ∈ {11,12,13}` (8,2)
> `E7 e=5+1+1 λ=9+1+1+1+1` — `L ∈ {11,12,13}` (9,1)
> `E7 e=5+2 λ=8+1+1+1+1+1` — `L ∈ {11,12,13}` (8,1)
> `E7 e=5+2 λ=8+2+1+1+1` — `L ∈ {11,12,13}` (8,2)
> `E7 e=6+1 λ=8+1+1+1+1+1` — `L ∈ {11,12,13}` (8,1)
> `E7 e=7 λ=7+1+1+1+1+1+1` — `L ∈ {11,12,13}` (7,1)
> `E8 e=1+1+1+1+1+1+1+1 λ=12` — `L ∈ {11,12}` (12,0)
> `E8 e=2+1+1+1+1+1+1 λ=11+1` — `L ∈ {11,12}` (11,1)
> `E8 e=2+2+1+1+1+1 λ=10+1+1` — `L ∈ {11,12}` (10,1)
> `E8 e=2+2+1+1+1+1 λ=10+2` — `L ∈ {11,12}` (10,2)
> `E8 e=2+2+2+1+1 λ=9+1+1+1` — `L ∈ {11,12}` (9,1)
> `E8 e=2+2+2+1+1 λ=9+2+1` — `L ∈ {11,12}` (9,2)
> `E8 e=2+2+2+1+1 λ=9+3` — `L ∈ {11,12}` (9,3)
> `E8 e=2+2+2+2 λ=8+1+1+1+1` — `L ∈ {11,12}` (8,1)
> `E8 e=2+2+2+2 λ=8+2+1+1` — `L ∈ {11,12}` (8,2)
> `E8 e=2+2+2+2 λ=8+2+2` — `L ∈ {11,12}` (8,2)
> `E8 e=2+2+2+2 λ=8+3+1` — `L ∈ {11,12}` (8,3)
> `E8 e=2+2+2+2 λ=8+4` — `L ∈ {11,12}` (8,4)
> `E8 e=3+1+1+1+1+1 λ=10+1+1` — `L ∈ {11,12}` (10,1)
> `E8 e=3+2+1+1+1 λ=9+1+1+1` — `L ∈ {11,12}` (9,1)
> `E8 e=3+2+1+1+1 λ=9+2+1` — `L ∈ {11,12}` (9,2)
> `E8 e=3+2+2+1 λ=8+1+1+1+1` — `L ∈ {11,12}` (8,1)
> `E8 e=3+2+2+1 λ=8+2+1+1` — `L ∈ {11,12}` (8,2)
> `E8 e=3+2+2+1 λ=8+2+2` — `L ∈ {11,12}` (8,2)
> `E8 e=3+2+2+1 λ=8+3+1` — `L ∈ {11,12}` (8,3)
> `E8 e=3+3+1+1 λ=8+1+1+1+1` — `L ∈ {11,12}` (8,1)
> `E8 e=3+3+1+1 λ=8+2+1+1` — `L ∈ {11,12}` (8,2)
> `E8 e=3+3+1+1 λ=8+2+2` — `L ∈ {11,12}` (8,2)
> `E8 e=3+3+2 λ=7+1+1+1+1+1` — `L ∈ {11,12}` (7,1)
> `E8 e=3+3+2 λ=7+2+1+1+1` — `L ∈ {11,12}` (7,2)
> `E8 e=3+3+2 λ=7+2+2+1` — `L ∈ {11,12}` (7,2)
> `E8 e=3+3+2 λ=7+3+1+1` — `L ∈ {11,12}` (7,3)
> `E8 e=3+3+2 λ=7+3+2` — `L ∈ {11,12}` (7,3)
> `E8 e=4+1+1+1+1 λ=9+1+1+1` — `L ∈ {11,12}` (9,1)
> `E8 e=4+2+1+1 λ=8+1+1+1+1` — `L ∈ {11,12}` (8,1)
> `E8 e=4+2+1+1 λ=8+2+1+1` — `L ∈ {11,12}` (8,2)
> `E8 e=4+2+2 λ=7+1+1+1+1+1` — `L ∈ {11,12}` (7,1)
> `E8 e=4+2+2 λ=7+2+1+1+1` — `L ∈ {11,12}` (7,2)
> `E8 e=4+2+2 λ=7+2+2+1` — `L ∈ {11,12}` (7,2)
> `E8 e=4+2+2 λ=7+3+1+1` — `L ∈ {11,12}` (7,3)
> `E8 e=4+3+1 λ=7+1+1+1+1+1` — `L ∈ {11,12}` (7,1)
> `E8 e=4+3+1 λ=7+2+1+1+1` — `L ∈ {11,12}` (7,2)
> `E8 e=4+3+1 λ=7+2+2+1` — `L ∈ {11,12}` (7,2)
> `E8 e=4+4 λ=6+1+1+1+1+1+1` — `L ∈ {11,12}` (6,1)
> `E8 e=4+4 λ=6+2+1+1+1+1` — `L ∈ {11,12}` (6,2)
> `E8 e=4+4 λ=6+2+2+1+1` — `L ∈ {11,12}` (6,2)
> `E8 e=4+4 λ=6+2+2+2` — `L ∈ {11,12}` (6,2)
> `E8 e=5+1+1+1 λ=8+1+1+1+1` — `L ∈ {11,12}` (8,1)
> `E8 e=5+2+1 λ=7+1+1+1+1+1` — `L ∈ {11,12}` (7,1)
> `E8 e=5+2+1 λ=7+2+1+1+1` — `L ∈ {11,12}` (7,2)
> `E8 e=5+3 λ=6+1+1+1+1+1+1` — `L ∈ {11,12}` (6,1)
> `E8 e=5+3 λ=6+2+1+1+1+1` — `L ∈ {11,12}` (6,2)
> `E8 e=5+3 λ=6+2+2+1+1` — `L ∈ {11,12}` (6,2)
> `E8 e=6+1+1 λ=7+1+1+1+1+1` — `L ∈ {11,12}` (7,1)
> `E8 e=6+2 λ=6+1+1+1+1+1+1` — `L ∈ {11,12}` (6,1)
> `E8 e=6+2 λ=6+2+1+1+1+1` — `L ∈ {11,12}` (6,2)
> `E8 e=7+1 λ=6+1+1+1+1+1+1` — `L ∈ {11,12}` (6,1)
> `E8 e=8 λ=5+1+1+1+1+1+1+1` — `L ∈ {11,12}` (5,1)
> `E9 e=1+1+1+1+1+1+1+1+1 λ=11` — `L ∈ {11}` (11,0)
> `E9 e=2+1+1+1+1+1+1+1 λ=10+1` — `L ∈ {11}` (10,1)
> `E9 e=2+2+1+1+1+1+1 λ=9+1+1` — `L ∈ {11}` (9,1)
> `E9 e=2+2+1+1+1+1+1 λ=9+2` — `L ∈ {11}` (9,2)
> `E9 e=2+2+2+1+1+1 λ=8+1+1+1` — `L ∈ {11}` (8,1)
> `E9 e=2+2+2+1+1+1 λ=8+2+1` — `L ∈ {11}` (8,2)
> `E9 e=2+2+2+1+1+1 λ=8+3` — `L ∈ {11}` (8,3)
> `E9 e=2+2+2+2+1 λ=7+1+1+1+1` — `L ∈ {11}` (7,1)
> `E9 e=2+2+2+2+1 λ=7+2+1+1` — `L ∈ {11}` (7,2)
> `E9 e=2+2+2+2+1 λ=7+2+2` — `L ∈ {11}` (7,2)
> `E9 e=2+2+2+2+1 λ=7+3+1` — `L ∈ {11}` (7,3)
> `E9 e=2+2+2+2+1 λ=7+4` — `L ∈ {11}` (7,4)
> `E9 e=3+1+1+1+1+1+1 λ=9+1+1` — `L ∈ {11}` (9,1)
> `E9 e=3+2+1+1+1+1 λ=8+1+1+1` — `L ∈ {11}` (8,1)
> `E9 e=3+2+1+1+1+1 λ=8+2+1` — `L ∈ {11}` (8,2)
> `E9 e=3+2+2+1+1 λ=7+1+1+1+1` — `L ∈ {11}` (7,1)
> `E9 e=3+2+2+1+1 λ=7+2+1+1` — `L ∈ {11}` (7,2)
> `E9 e=3+2+2+1+1 λ=7+2+2` — `L ∈ {11}` (7,2)
> `E9 e=3+2+2+1+1 λ=7+3+1` — `L ∈ {11}` (7,3)
> `E9 e=3+2+2+2 λ=6+1+1+1+1+1` — `L ∈ {11}` (6,1)
> `E9 e=3+2+2+2 λ=6+2+1+1+1` — `L ∈ {11}` (6,2)
> `E9 e=3+2+2+2 λ=6+2+2+1` — `L ∈ {11}` (6,2)
> `E9 e=3+2+2+2 λ=6+3+1+1` — `L ∈ {11}` (6,3)
> `E9 e=3+2+2+2 λ=6+3+2` — `L ∈ {11}` (6,3)
> `E9 e=3+2+2+2 λ=6+4+1` — `L ∈ {11}` (6,4)
> `E9 e=3+3+1+1+1 λ=7+1+1+1+1` — `L ∈ {11}` (7,1)
> `E9 e=3+3+1+1+1 λ=7+2+1+1` — `L ∈ {11}` (7,2)
> `E9 e=3+3+1+1+1 λ=7+2+2` — `L ∈ {11}` (7,2)
> `E9 e=3+3+2+1 λ=6+1+1+1+1+1` — `L ∈ {11}` (6,1)
> `E9 e=3+3+2+1 λ=6+2+1+1+1` — `L ∈ {11}` (6,2)
> `E9 e=3+3+2+1 λ=6+2+2+1` — `L ∈ {11}` (6,2)
> `E9 e=3+3+2+1 λ=6+3+1+1` — `L ∈ {11}` (6,3)
> `E9 e=3+3+2+1 λ=6+3+2` — `L ∈ {11}` (6,3)
> `E9 e=3+3+3 λ=5+1+1+1+1+1+1` — `L ∈ {11}` (5,1)
> `E9 e=3+3+3 λ=5+2+1+1+1+1` — `L ∈ {11}` (5,2)
> `E9 e=3+3+3 λ=5+2+2+1+1` — `L ∈ {11}` (5,2)
> `E9 e=3+3+3 λ=5+2+2+2` — `L ∈ {11}` (5,2)
> `E9 e=3+3+3 λ=5+3+1+1+1` — `L ∈ {11}` (5,3)
> `E9 e=3+3+3 λ=5+3+2+1` — `L ∈ {11}` (5,3)
> `E9 e=3+3+3 λ=5+3+3` — `L ∈ {11}` (5,3)
> `E9 e=4+1+1+1+1+1 λ=8+1+1+1` — `L ∈ {11}` (8,1)
> `E9 e=4+2+1+1+1 λ=7+1+1+1+1` — `L ∈ {11}` (7,1)
> `E9 e=4+2+1+1+1 λ=7+2+1+1` — `L ∈ {11}` (7,2)
> `E9 e=4+2+2+1 λ=6+1+1+1+1+1` — `L ∈ {11}` (6,1)
> `E9 e=4+2+2+1 λ=6+2+1+1+1` — `L ∈ {11}` (6,2)
> `E9 e=4+2+2+1 λ=6+2+2+1` — `L ∈ {11}` (6,2)
> `E9 e=4+2+2+1 λ=6+3+1+1` — `L ∈ {11}` (6,3)
> `E9 e=4+3+1+1 λ=6+1+1+1+1+1` — `L ∈ {11}` (6,1)
> `E9 e=4+3+1+1 λ=6+2+1+1+1` — `L ∈ {11}` (6,2)
> `E9 e=4+3+1+1 λ=6+2+2+1` — `L ∈ {11}` (6,2)
> `E9 e=4+3+2 λ=5+1+1+1+1+1+1` — `L ∈ {11}` (5,1)
> `E9 e=4+3+2 λ=5+2+1+1+1+1` — `L ∈ {11}` (5,2)
> `E9 e=4+3+2 λ=5+2+2+1+1` — `L ∈ {11}` (5,2)
> `E9 e=4+3+2 λ=5+2+2+2` — `L ∈ {11}` (5,2)
> `E9 e=4+3+2 λ=5+3+1+1+1` — `L ∈ {11}` (5,3)
> `E9 e=4+3+2 λ=5+3+2+1` — `L ∈ {11}` (5,3)
> `E9 e=4+4+1 λ=5+1+1+1+1+1+1` — `L ∈ {11}` (5,1)
> `E9 e=4+4+1 λ=5+2+1+1+1+1` — `L ∈ {11}` (5,2)
> `E9 e=4+4+1 λ=5+2+2+1+1` — `L ∈ {11}` (5,2)
> `E9 e=4+4+1 λ=5+2+2+2` — `L ∈ {11}` (5,2)
> `E9 e=5+1+1+1+1 λ=7+1+1+1+1` — `L ∈ {11}` (7,1)
> `E9 e=5+2+1+1 λ=6+1+1+1+1+1` — `L ∈ {11}` (6,1)
> `E9 e=5+2+1+1 λ=6+2+1+1+1` — `L ∈ {11}` (6,2)
> `E9 e=5+2+2 λ=5+1+1+1+1+1+1` — `L ∈ {11}` (5,1)
> `E9 e=5+2+2 λ=5+2+1+1+1+1` — `L ∈ {11}` (5,2)
> `E9 e=5+2+2 λ=5+2+2+1+1` — `L ∈ {11}` (5,2)
> `E9 e=5+2+2 λ=5+3+1+1+1` — `L ∈ {11}` (5,3)
> `E9 e=5+3+1 λ=5+1+1+1+1+1+1` — `L ∈ {11}` (5,1)
> `E9 e=5+3+1 λ=5+2+1+1+1+1` — `L ∈ {11}` (5,2)
> `E9 e=5+3+1 λ=5+2+2+1+1` — `L ∈ {11}` (5,2)
> `E9 e=5+4 λ=4+1+1+1+1+1+1+1` — `L ∈ {11}` (4,1)
> `E9 e=5+4 λ=4+2+1+1+1+1+1` — `L ∈ {11}` (4,2)
> `E9 e=5+4 λ=4+2+2+1+1+1` — `L ∈ {11}` (4,2)
> `E9 e=5+4 λ=4+2+2+2+1` — `L ∈ {11}` (4,2)
> `E9 e=6+1+1+1 λ=6+1+1+1+1+1` — `L ∈ {11}` (6,1)
> `E9 e=6+2+1 λ=5+1+1+1+1+1+1` — `L ∈ {11}` (5,1)
> `E9 e=6+2+1 λ=5+2+1+1+1+1` — `L ∈ {11}` (5,2)
> `E9 e=6+3 λ=4+1+1+1+1+1+1+1` — `L ∈ {11}` (4,1)
> `E9 e=6+3 λ=4+2+1+1+1+1+1` — `L ∈ {11}` (4,2)
> `E9 e=6+3 λ=4+2+2+1+1+1` — `L ∈ {11}` (4,2)
> `E9 e=7+1+1 λ=5+1+1+1+1+1+1` — `L ∈ {11}` (5,1)
> `E9 e=7+2 λ=4+1+1+1+1+1+1+1` — `L ∈ {11}` (4,1)
> `E9 e=7+2 λ=4+2+1+1+1+1+1` — `L ∈ {11}` (4,2)
> `E9 e=8+1 λ=4+1+1+1+1+1+1+1` — `L ∈ {11}` (4,1)
> `E9 e=9 λ=3+1+1+1+1+1+1+1+1` — `L ∈ {11}` (3,1)
>
> **Every `(w, 2nd)` above has a unique max `w` with `2nd ≤ w−2`, so Lemma FAN-6′ kills every survivor at `ν = 10`. Misses: 0.**

**Reading.** `910` `E ≥ 1` survivors across `ν = 7…10`, inside
`3 340 + 8 457 + 20 126 + 45 450 = 77 373` shapes, plus `16` boundary
survivors inside `427` boundary pairs, plus the four single-part `E = 0`
survivors — **and Lemma FAN-6′ kills every one of them**. The `ν ≤ 10`
fold is now printed data at every `ν`, not an unreviewable citation.
