# Task: prove or refute a majorization statement about Havel–Hakimi pivot sequences

**Brief E05 (RESTATED 2026-08-23 by owner-w61, round 43).** The previous framing —
*"(RH), independent second attempt, different framing (majorization / dominance order)"* — named a
direction but no statement. This brief supplies the sharp statement that direction leads to, together
with the measurement that says it is worth attacking. Reasons for the restatement are in §8.
Nothing this line holds is withheld.

This is a genuine open question from an active research effort in graph/partition combinatorics.
Everything you need is in this file. **You have no internet access and no access to any repository —
do not cite a source you cannot reconstruct here.** We want a real proof attempt or a real
counterexample. **If you can do neither, say so plainly and say exactly where you got stuck.** The
failure mode we specifically guard against is a **fluent wrong proof**: a confident, fully-worked
derivation that does not survive reconstruction. Everything you send back is checked line by line by
an independent reviewer who rebuilds each load-bearing step. **Give reasoning and an honest verdict,
not confidence language.**

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

A run **terminates** if it reaches `TERMINAL` without ever hitting `ABORT`. For a terminating list:

* `s(π)` := number of steps, `R(π)` := number of entries remaining at `TERMINAL` (all `0`) — the
  **residue**;
* `p(π)` := the multiset of pivots `{p_1,…,p_{s(π)}}`, written as a partition (weakly decreasing).

### Lemma C1-X (PROVED; elementary, supplied, do not re-derive)
For a terminating list `π` of length `n`:
> **(i)** `R(π) = n − s(π)`.  **(ii)** `2·sum(p(π)) = sum(π)`.

*Proof.* (i) One step deletes exactly one entry — the pivot — and the run stops precisely when every
remaining entry is `0`; after `s` steps `n − s` entries remain, all zero. (ii) A step with pivot `p`
deletes an entry equal to `p` and subtracts `1` from `p` other entries, so `sum` drops by exactly
`2p`; the run ends at `sum = 0`. ∎

> **Consequence to keep in view: `p(π)` is a partition of the integer `sum(π)/2`, and `s(π)` is its
> number of parts.**

---

## 2. The statement the effort actually needs

> **(RH).** Let `π` be a terminating list and let `π′` be obtained from `π` by one **elementary unit
> transfer down**:
> ```
> pi' = pi - e_i + e_j     with     pi_i >= pi_j + 2
> ```
> (subtract `1` from one entry, add `1` to an entry at least `2` smaller). Suppose `π′` also
> terminates. Then **`R(π′) ≤ R(π)`.**

A unit transfer down preserves both the length `n` and the sum, so by C1-X (i),

```
(RH)   <=>   s(pi) <= s(pi')   <=>   p(pi) has NO MORE PARTS than p(pi'),
```

and by C1-X (ii) `p(π)` and `p(π′)` are two partitions **of the same integer** `sum(π)/2`.

> **A precision note on the definition, recorded because it bit us.** An earlier statement of (RH)
> read *"subtract 1 from one entry, add 1 to an entry that is **not larger**"*. Taken literally that
> also admits `π_i = π_j`, which as a multiset move goes **UP** in dominance, not down — measured:
> **6 986 of 6 986** such moves over partitions of `N ∈ [2,16]` produce a `π′` that **dominates** `π`.
> It also admits `π_i = π_j + 1`, which is the identity as a multiset. **Only `π_i ≥ π_j + 2` is a
> genuine down-move, and that is the definition used throughout this brief.**

---

## 3. ⚠️ THE STATEMENT TO PROVE OR REFUTE

> ### (PIVOT-MAJ)
> Let `π` be a terminating list and `π′ = π − e_i + e_j` with `π_i ≥ π_j + 2`, and suppose `π′`
> terminates. Then the pivot partition of `π` **dominates** that of `π′`:
> ```
> p(pi)  >=  p(pi')       in the dominance (majorization) order on partitions of sum(pi)/2,
> ```
> i.e. for every `r ≥ 1`, the sum of the `r` largest pivots of `π` is `≥` the sum of the `r` largest
> pivots of `π′` (pad the shorter sequence with zeros; the totals are equal by C1-X (ii)).

### (PIVOT-MAJ) ⟹ (RH), and the implication is standard
For partitions `a`, `b` of the same integer, `a ⪰ b` in dominance implies `a* ⪯ b*` for the conjugate
partitions, and the number of parts of `a` equals `a*₁`. Hence `a ⪰ b ⟹ #parts(a) ≤ #parts(b)`.
Applied to `a = p(π)`, `b = p(π′)`: `s(π) ≤ s(π′)`, which is (RH). ∎

**The implication is strict, so this is real work rather than a restatement.** Over all pairs `(a,b)`
of partitions of the same `N ∈ [2,12]` (`12 646` pairs): dominance implied fewer-or-equal parts on
**5 762 of 5 762** cases with `0` failures, while **1 458** pairs have fewer-or-equal parts **without**
dominance — e.g. `a = (2,2)`, `b = (3,1)`. So (PIVOT-MAJ) is strictly stronger than (RH) and could be
false while (RH) is true. **If you refute (PIVOT-MAJ), that is a useful result: it closes this route
and redirects effort. Say so plainly rather than weakening the statement until it survives.**

---

## 4. What is MEASURED (so you attack the argument, not data we already have)

Censuses over stated finite populations. **Not proofs, and not what you are asked to check.**

**Population P3 — every partition `π` of `N ∈ [2,16]` whose run terminates, and every
`π′ = π − e_i + e_j` with `π_i ≥ π_j + 2` whose run also terminates. `1 324` pairs.** Exclusions:
lists whose run ABORTS, skipped on **both** sides and counted nowhere else.

| measured | result |
|---|---|
| C1-X (ii) `2·sum(pivots) = sum` | holds **209**, fails **0** (over the terminating lists of the population) |
| **(RH)** `s(π) ≤ s(π′)` | holds **1 324**, fails **0** |
| **(PIVOT-MAJ)** `p(π) ⪰ p(π′)` | holds **1 324**, fails **0** |
| corrupt companion — the **reversed** (RH), `s(π) ≥ s(π′)` | **fails 873 of 1 324** |
| corrupt companion — the **reversed** majorization, `p(π′) ⪰ p(π)` | **fails 1 072 of 1 324** |

**Population P4 — a second, DISJOINT population: `N ∈ [17,20]` only. `5 006` pairs.** Same
exclusions. **(RH)** holds `5 006` of `5 006`; **(PIVOT-MAJ)** holds `5 006` of `5 006`.

The two corrupt companions are there so the block is not vacuous: the reversed statements are false
on most of the population, so the test discriminates.

> **What this does NOT say.** (PIVOT-MAJ) is a **census**, not a theorem. No proof exists. `N > 20`
> is out of population and is claimed nowhere.

---

## 5. Context you should have (a related theorem, and why it does not settle this)

There is a known theorem in this area — **Hiller, "On the Domination Order among Elimination
Sequences"** — whose content, restated so you can use it without looking it up:

> An **elimination sequence** of a list `π` is what you get by laying off vertices in *any* order:
> repeatedly pick **any** entry `d`, delete it, and subtract `1` from **the `d` LARGEST** remaining
> entries (Kleitman–Wang, 1973: for a graphic sequence every such order stays graphic and ends in all
> zeros). Havel–Hakimi is the particular order that always picks the maximum. **Hiller's theorem: for
> any degree sequence, the elimination sequence derived from Havel–Hakimi DOMINATES every other
> elimination sequence of the same list.**
>
> **⚠️ The words "the `d` LARGEST" are load-bearing and are not decoration.** Subtracting `1` from an
> arbitrary `d` of the remaining entries does **not** preserve graphicness: on `π = (2,2,1,1)`, laying
> off a `2` and decrementing the two `1`s gives `(2,0,0)`, whose Havel–Hakimi run **aborts**;
> decrementing the two **largest** remaining entries instead gives `(1,1,0)`, which terminates. An
> earlier version of this brief stated the rule without "largest" and was wrong. If your argument uses
> a laying-off move, check the graphicness obligation explicitly at that move.

Read through C1-X (ii), every elimination sequence of `π` has the same total `sum(π)/2`, and a
dominating partition of a fixed total has no more parts than a dominated one. So

```
R(pi)  =  n  -  min { length of an elimination sequence of pi },   the min over ALL laying-off orders.
```

**Scope, stated because it has already misled one attempt.** Hiller's theorem compares elimination
orders of **ONE fixed list**. (RH) and (PIVOT-MAJ) compare **TWO different lists**. **Hiller does not
imply (RH).** What it supplies is the variational identity above — which is a genuinely different
lever, and it is the subject of a separate brief:

> **The other route, so you do not duplicate it.** Because `R(π)` is a **minimum over a family**, and
> minima are proved from **one witness**, (RH) also follows if one exhibits **any single** elimination
> sequence of `π` of length `≤ s(π′)` — e.g. by transporting `π′`'s Havel–Hakimi laying-off order to
> `π`. **That construction has already been attempted and it did NOT close. Do not spend this brief
> on it.** Your target is the pivot-majorization statement of §3.

### What the witness attempt achieved, and exactly where it stopped (told so you do not repeat it)

The transport was set up as a coupling: match survivors of the two runs bijectively and maintain a
per-entry difference `δ_v ∈ {−1,0,+1}`, with states **Type I** (one `+1` token `U`, one `−1` token
`D`), **Type II** (only `U`), **Type III** (only `D`). These cases were closed: Type I with the two
pivot vertices matched; Type I when the `π`-side pivot is `U`; Type I when it is `D` and a positive
outsider is available; Type II followed by pivoting `U`.

**The unclosed case, stated precisely:** *Type III whose `D`-token has `π`-value `0` (i.e.
`π′(D) = 1`), coinciding with every survivor outside the current decrement-set and pivot having
`π`-value `0`.* In that configuration no compliant move was found: pivoting `D` gives pivot value `0`
and desynchronizes the step budget; any pivot with `δ = 0` requires a decrement-set that avoids `D`
and avoids all-zero outsiders, which is unavailable. Neither an escape move nor a proof that the
state is unreachable under some global tie-breaking was obtained. A potential function `Σ|δ_v|` was
tried and is not monotone on the relevant branch.

**Do not treat that as evidence against (RH).** (RH) held on every instance examined; what failed is
that one construction scheme.

A literature search for (RH) or the general dominance-monotonicity of the residue found no source
stating it, with one gap: **Triesch, "Degree sequences of graphs and dominance order", J. Graph
Theory 22 (1996) 89–93** was not retrieved (paywalled, content unverified). If your argument
reconstructs something you recognize as a known result, **say which and state it in full** — that is
useful to us, but do not assert a citation you cannot reconstruct here.

---

## 6. Hints from the structure (use or ignore)

* A step with pivot `p` drops the sum by exactly `2p` (C1-X (ii) at the level of one step). So the
  pivot sequence is a "how the sum is spent" record, and dominance of pivot sequences is a statement
  that `π` **spends its sum earlier** than `π′` does.
* The first pivots are `max(π)` and `max(π′)`, and a unit transfer down satisfies
  `max(π′) ∈ {max(π) − 1, max(π)}`. The `r = 1` case of (PIVOT-MAJ) is therefore immediate; the
  content is in `r ≥ 2` and in the fact that after one step the two lists are **no longer related by a
  single unit transfer**, so a naive induction on `r` does not close.
* A natural induction hypothesis to try, and the one we could not make work: that after one lockstep
  step the pair `(step(π), step(π′))` is again related by a dominance move — possibly after adjusting
  for the two lists having different pivots. **State clearly if you make this work; that is the crux.**

---

## 7. What to send back

1. A proof of **(PIVOT-MAJ)**, or a counterexample (an explicit `π`, `i`, `j`, both pivot sequences
   written out, and the `r` at which the partial sums cross).
2. If (PIVOT-MAJ) is false but the weaker **(RH)** still looks reachable by a dominance argument,
   say what the right intermediate statement is.
3. If you can prove neither: the precise step that resisted.
4. **Check any counterexample against §4's populations first.** A counterexample with `N ≤ 20` would
   contradict a completed census and is far more likely to be an arithmetic slip — recompute the two
   Havel–Hakimi runs entry by entry before reporting it.
5. Do **not** report agreement with §4's numbers as a result. They are already in hand.

---

## 8. Why the previous E05 framing was restated (recorded for the file, not part of your task)

* The old row said "different framing (majorization / dominance order)" and named **no statement**.
  Dispatching that would have asked an engine to invent the target as well as prove it.
* The backlog note attached to the row said the framing "predates the S2-RED reduction". **That
  reason is wrong and is corrected here:** the S2-RED reduction is on the *odd* half of (MON) and
  does not touch (RH), which is the *even* half. What actually changed E05 is (a) the variational
  identity of §5, which moved the *witness-construction* route into a separate brief, and (b) the
  measurement in §4, which did not exist when the row was written and which is what makes
  (PIVOT-MAJ) worth an engine call rather than a guess.
* The definition of "unit transfer down" was **imprecise** in the source statement (§2's note). A
  brief carrying the imprecise version would have sent an engine at a statement that is false under
  one of its readings.
