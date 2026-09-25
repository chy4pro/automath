# Task: prove a step-invariance statement on a rigid two-parameter family of integer lists

**Brief E07 (drafted 2026-08-23 by owner-w61, round 43).** The E07 row originally read *"re-derive
Lemma C1-Y (terminal residues, delta = 1) independently"*. **That item is STRUCK** — reasons in §8;
in short, C1-Y is a three-line lemma that is already verified and nobody is waiting on it, and
sending it would be filler. What is below is the statement the line actually needs on that same part
of the argument. C1-Y itself is supplied in §3 as machinery, so nothing is withheld.

This is a genuine open question from an active research effort in graph/partition combinatorics.
Everything you need is in this file. **You have no internet access and no access to any repository —
do not cite a source you cannot reconstruct here.** We want a real proof attempt. **If you cannot
prove it, say so plainly and say exactly where you got stuck** — that is a valued answer, not a
failure. The failure mode we specifically guard against is a **fluent wrong proof**: a confident,
fully-worked derivation that does not survive reconstruction. Everything you send back is checked
line by line by an independent reviewer who rebuilds each load-bearing step. **Give reasoning and an
honest verdict, not confidence language.**

---

## 1. The process (verbatim; assume no other context)

Finite lists of non-negative integers, treated as multisets, always written weakly decreasing. One
**Havel–Hakimi step** on a list `L`:

```
sort L weakly decreasing  ->  s
if s is empty or s[0] == 0 :  TERMINAL   (the run stops here)
d    := s[0]                              (the PIVOT of this step)
rest := s[1:]
if d > len(rest) :            ABORT       (the list is not graphic)
blk  := rest[:d] ;  tail := rest[d:]
if any entry of blk is 0 :    ABORT
next := sort_desc( [x-1 for x in blk] + tail )
```

A run **terminates** if it reaches `TERMINAL` without ever hitting `ABORT`. For a terminating list of
length `n`: `s(L)` := number of steps; `R(L)` := number of entries remaining at `TERMINAL` (all `0`)
— the **residue**.

### Lemma C1-X (PROVED; supplied, do not re-derive)
> **(i)** `R(L) = n − s(L)`.  **(ii)** `2·(sum of pivots) = sum(L)`.

*Proof.* (i) One step deletes exactly one entry — the pivot — and the run stops precisely when every
remaining entry is `0`; after `s` steps `n − s` entries remain, all zero. (ii) A step with pivot `p`
deletes an entry equal to `p` and subtracts `1` from `p` other entries, so `sum` drops by exactly
`2p`; the run ends at `sum = 0`. ∎
> **Corollary, used constantly: `R` is CONSTANT along a trajectory**, `R(L_t) = (n−t) − s(L_t) = R(L)`.

---

## 2. The family — and it is very rigid

For `c ≥ 1` define the two head blocks

```
W+(c) = [c]*3 ++ [c-1]*c        length c+3,   sum c(c+2)
W-(c) = [c]*2 ++ [c-1]*(c+1)    length c+3,   sum c^2+2c-1
```

Fix `c ≥ 1` and a weakly decreasing `tail` with all entries in `[0, c]`. Put

```
L   =  W-(c)   ++ tail
L'  =  W+(c+1) ++ tail
```

These are the two sides of the statement the effort is after. They do **not** have the same length
(`|L′| − |L| = 1`) and their sums differ by `2c+4`, so they are not a perturbation of one another.

### Lemma S2-STEP (PROVED; supplied, do not re-derive)
One Havel–Hakimi step on `L′` neither terminates nor aborts, and produces

```
L'_1  =  L  with exactly TWO entries equal to c-1 replaced by c.
```

Hence `len(L'_1) = len(L)` and `sum(L'_1) = sum(L) + 2`.

*Proof.* `W+(c+1) = [c+1]³ ++ [c]^{c+1}` and every entry of `tail` is `≤ c`, so the pivot is
`d = c+1` and, with `m := #{j : tail_j = c}`,
`rest = [c+1]² ++ [c]^{c+1+m} ++ tail_{<c}`, of length `c+3+|tail| ≥ c+1 = d`: no length abort.
`blk = rest[:c+1] = [c+1]² ++ [c]^{c−1}` (uses `c+1+m ≥ c−1`, true for every `c ≥ 1`), and every entry
of `blk` is `≥ c ≥ 1`: no zero abort. Subtracting `1` gives `[c]² ++ [c−1]^{c−1}`; the untouched
remainder is `[c]^{2+m} ++ tail_{<c}`. As multisets

```
L'_1 = {c : 4+m} u {c-1 : c-1} u tail_{<c}
L    = {c : 2+m} u {c-1 : c+1} u tail_{<c}
```

which differ exactly by moving two copies of `c−1` up to `c`. `L` carries `c+1 ≥ 2` copies of `c−1`,
so the move is always available. ∎

*(The `c = 1` boundary is inside the lemma, not excluded: there `c−1 = 0` and the two raised entries
are the two zeros of `W−(1) = [1,1,0,0]`. Worked: `L′ = W+(2) = (2,2,2,1,1) → (1,1,1,1) = L'_1`,
`L = (1,1,0,0)`.)*

Because `R` is a trajectory invariant, `R(L′) = R(L'_1)`.

> ### THE RIGIDITY THAT MAKES THIS THE EASY CASE
> Write `A_0 := L` and `B_0 := L'_1`. Then **`B_0` is `A_0` with two entries raised by `1`, and BOTH
> raised entries are copies of `c−1` sitting inside the head block `W−(c)`.** They are at the *same*
> level and in the *same* block. (The sibling family this brief is NOT about raises one head entry
> and one tail entry, at different levels — that case is genuinely harder and is a separate brief.)

---

## 3. The lockstep, the classifier, and the two proved branches

Step `A` and `B` one step each, in **lockstep**: `A_{t+1} = step(A_t)`, `B_{t+1} = step(B_t)`. The
lockstep ends when either list reaches `TERMINAL`/`ABORT`, or when `A_t = B_t` (call this **EQ**).
Because `R` is a trajectory invariant, `R(A_0) − R(B_0) = R(A_t) − R(B_t)` at every joint stage.

`relation(A,B)` classifies how `B` differs from `A` (both sorted decreasing):

| value | exact condition |
|---|---|
| `EQ` | `A == B` as multisets |
| `UP2` | `len(A) = len(B)`, `sum(B) = sum(A)+2`, and there are positions `x ≤ y` with `B = sort(A with A[x]+1 and A[y]+1)` |
| `UNIT_DOWN` | `len` equal, `sum` equal, every partial sum of `B` is `≤` that of `A`, and the difference is one unit moved from a larger entry to a smaller one |
| `DOM` | `len` equal, `sum` equal, `B` dominated by `A`, not the `UNIT_DOWN` shape |
| `OTHER` | none of the above |

`EQ` is **absorbing**: the step is a function of the multiset alone.

### Lemma C1-Y (PROVED; supplied)
For `r ≥ 2`: `R(0^r) = r` and `R((1,1,0^{r−2})) = r − 1`, so the difference is exactly `1`.
*Proof.* `0^r` is already `TERMINAL`, so its residue is `r`. For `(1,1,0^{r−2})` the pivot is `1`; the
step deletes it and subtracts `1` from the other `1`, leaving `0^{r−1}`, terminal. So `s = 1` and
`R = r − 1` by C1-X (i). ∎

### The two-branch theorem (PROVED; supplied)
Suppose `B_0` is `A_0` with two entries raised by `1`, the relation is `UP2` at **every** joint state,
and both runs terminate. Then **exactly one** of:

1. **`EQ` occurs** at a finite stage — then `delta := R(A_0) − R(B_0) = 0`;
2. **`EQ` never occurs** — the lockstep ends with `A_s = 0^r` terminal and `B_s = (1,1,0^{r−2})`, and
   C1-Y gives `delta = 1`.

Third branch (`B` terminal while `A` is not) is **empty by proof**: `B = A` with two entries raised,
so `B = 0^m` would force two entries of `A` to equal `−1`. ∎

**So the entire remaining obligation is the hypothesis: `UP2` at every joint state.**

---

## 4. ⚠️ THE STATEMENT TO PROVE

> ### (S2-PERSIST)
> Let `c ≥ 1`, let `tail` be weakly decreasing with entries in `[0,c]`, and let `A_0 = L = W−(c) ++
> tail`, `B_0 = L'_1` as in Lemma S2-STEP. Step them in lockstep. Then at **every** joint state,
> `relation(A_t, B_t)` is `EQ` or `UP2` — the difference never becomes anything else.
>
> **Consequence, immediate from §3:** `delta = R(L) − R(L′) ∈ {0,1}`, which is the statement the
> effort needs and which is currently only a census.

An equivalent localized form, which may be the easier handle:

> ### (S2-G) — the same statement, one step at a time
> Put `g_t := sum(B_t) − sum(A_t)`, so `g_0 = 2`. By C1-X (ii) applied to one step,
> `g_{t+1} = g_t − 2·(p_B(t) − p_A(t))` where `p_A(t) = max(A_t)`, `p_B(t) = max(B_t)`.
> Prove that at every joint state **`p_B(t) = p_A(t)`, until the step at which `A_t` and `B_t` become
> equal** — i.e. `g_t ≡ 2` while the pair is distinct, and the two pivots never differ.
> Then `g` never leaves `{0,2}`, and `EQ` is reached exactly when the pivots first differ.

*(Note the asymmetry with the sibling family. There, `g` takes the value `0` at genuinely intermediate
joint states — the difference becomes a sum-preserving dominance move and only later merges. On
**this** family, measured in §5, `g = 0` occurs **only at the `EQ` state itself**, and the pivot gap
`p_B − p_A` is `0` at every stepped state except the single step that forms `EQ`. That is what
"rigid" buys, and it is why this case is the one worth attacking first.)*

---

## 5. What is MEASURED (so you attack the argument, not data we already have)

Censuses over stated finite populations. **Not proofs, and not what you are asked to check.**

**Population Q1 — the `686` distinct `(c, tail)` pairs arising in the effort's census range.**
Exclusions: none; `0` pairs abort on either side.

| measured | result |
|---|---|
| one HH step on `L′` terminates or aborts | **0** of 686 |
| `L'_1 = L` with exactly two `(c−1) → c` | **686** of 686 |
| `len(L'_1) = len(L)` · `sum(L'_1) = sum(L)+2` | **686** / **686** |
| `relation(L, L'_1)` | **`{UP2: 686}`** |
| `R(L′) = R(L'_1)` · `s(L′) − s(L'_1)` | **686** of 686 · **`{1: 686}`** |
| **relation-persistence over the whole lockstep** | **686 of 686** |
| joint-state relations seen, whole lockstep | **`{EQ: 626, UP2: 3394}`** |
| joint states needing `UNIT_DOWN` **or** `DOM` | **0 of 4 020** |
| how the lockstep exited | `{EQ reached: 626, a terminal state: 60}` |
| `delta` | `{0: 626, 1: 60}`, and `626 + 60 = 686` |
| `g_t = sum(B_t) − sum(A_t)` over all `4 020` joint states | **`{0: 626, 2: 3394}`** — and every `g = 0` state **is** the `EQ` state; `g` is never `0` at an intermediate state |
| `p_B − p_A` over all `3 334` **stepped** joint states | **`{0: 2708, 1: 626}`** — never negative, never `≥ 2` |
| cross-tab `(g_t, p_B − p_A)` at stepped states | **`{(2,0): 2708, (2,1): 626}`** — the pivots differ **exactly** on the `626` steps that form `EQ`, and nowhere else |

**Population Q2 — an independent sweep that does not come from the census at all: every `c ∈ [1,12]`
and every weakly decreasing `tail` of length `≤ 4` with entries in `[1,c]` — `6 187` pairs.**
Lemma S2-STEP holds **6 187 of 6 187**; `0` steps abort or terminate. Of those, `3 080` satisfy a
parity condition the original statement imposed and **`3 107` do not** — so **S2-STEP does not use the
parity**. Exclusions: none; `c > 12` and `|tail| > 4` are out of population and claimed nowhere.

**Corrupt companions, so the block is not vacuous** (all on Q1): `L′` itself a `UP2` partner of `L` —
**0 of 686**; a "three entries raised" reading — **0 of 686**; **two** steps on `L′` landing on a `UP2`
partner of `L` — **0 of 686**, so the step count in Lemma S2-STEP is one and is not arbitrary.

> **⚠️ A warning that matters.** The general "raise two entries by `1`" statement is **FALSE** without
> the head block. Over all terminating partitions of `N ∈ [2,16]`, `R(L′) ≤ R(L)` fails on **97** of
> **732** distinct such pairs. Minimal counterexamples, given so you do not "prove" something false:
> ```
> (2,2,2,1,1)   -> (3,3,2,1,1)     residue 2 -> 3
> (2,2,1,1,1,1) -> (3,3,1,1,1,1)   residue 3 -> 4
> (3,2,2,2,1)   -> (4,3,2,2,1)     residue 2 -> 3
> ```
> **Any proof must use the `W−(c)` head-block structure of `A_0` and the fact that the two raised
> entries are both copies of `c−1` inside it.** A proof that never uses this is wrong, and the three
> lists above will show where.

---

## 6. A worked instance, in full

```
c = 1, tail = ()          W-(1) = [1,1,0,0]     W+(2) = [2,2,2,1,1]
L  = (1,1,0,0)            HH:  (1,1,0,0) -> (0,0,0)                            s = 1,  R = 3
L' = (2,2,2,1,1)          HH:  (2,2,2,1,1) -> (1,1,1,1) -> (1,1,0) -> (0,0)    s = 3,  R = 2
L'_1 = (1,1,1,1)          = L with the two 0s raised to 1.       delta = R(L) - R(L') = 1.
lockstep on (A_0,B_0) = ((1,1,0,0),(1,1,1,1)):
   stage 0   A=(1,1,0,0)   B=(1,1,1,1)   UP2   g=2
   stage 1   A=(0,0,0)     B=(1,1,0)     UP2   g=2      <-- A is TERMINAL here; lockstep ends
   R(A)=3, R(B)=2, delta=1, and this is branch 2 of the two-branch theorem with r=3.
```

---

## 7. What to send back

1. A proof of **(S2-PERSIST)** or of **(S2-G)**. Either closes the same obligation.
2. Partial credit is real: a proof for `tail = ()` (all `c`), or for `|tail| ≤ 1`, or for `c` large,
   is worth having and should be sent even if the general case resists.
3. If you cannot close it: the precise step that resisted, stated so someone else can start there.
4. If you believe the statement is **false**, an explicit `(c, tail)` with the joint state at which it
   fails and both full trajectories. **Check it against §5's populations first** — a counterexample
   inside Q1 or Q2 contradicts a completed census and is far more likely to be an arithmetic slip.
5. Do **not** report agreement with §5's numbers as a result. They are already in hand.

---

## 8. Why the original E07 was struck (recorded for the file, not part of your task)

The row asked for an independent re-derivation of Lemma C1-Y (`R(0^r) = r`,
`R((1,1,0^{r−2})) = r−1`). Its proof is the three lines printed in §3, it has been checked
numerically for `r = 2..12` (`11` of `11`), and **no line of work is waiting on the answer.** The
governing rule for this backlog is *"does someone actually need the answer?"* — a re-derivation of a
three-line, already-verified lemma does not pass it, and dispatching it would cost a call now and cost
an adjudication later for nothing. **A struck row is a good outcome; an obsolete brief dispatched is
not.** C1-Y is retained above as supplied machinery so that the replacement brief withholds nothing.
