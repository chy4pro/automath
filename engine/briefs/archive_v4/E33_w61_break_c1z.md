# Task: ADVERSARIAL — try to break "Theorem C1-Z" (a conditional monotonicity result for the
# Havel-Hakimi residue)

You are being asked to genuinely try to break a specific claimed theorem from an active
combinatorics research effort — not to confirm it, not to be diplomatic about it. If, after
genuinely trying, you cannot find a flaw, say so plainly and say what you checked; that is a valid
and useful outcome. If you find a flaw, however small, report it precisely — do not soften it. An
independent reviewer will check your work line by line by reconstructing it, not by trusting your
tone, so a fluent-sounding "looks fine to me" without having actually traced the cases is exactly
the failure mode we are guarding against. We are telling you up front about one gap the line's own
author already found in a LATER round (so you don't waste time simply rediscovering exactly that
one fact) — your job is to (a) independently confirm or refute that this really is a gap in the
theorem AS STATED, and (b) look hard for anything else wrong, beyond it.

## 1. Definitions (self-contained — assume no other context)

A **list** is a finite multiset of nonnegative integers, written in weakly-decreasing order
`L = (a_1 >= a_2 >= ... >= a_n)`. `n = |L|`.

**Havel-Hakimi (HH) step.** Given `L = (a_1 >= ... >= a_n)` with `a_1 > 0`, let `p = a_1` (the
"pivot"). Delete `a_1`. Subtract 1 from each of the next `p` largest remaining entries
`a_2,...,a_{p+1}`. Re-sort to get `L'` (length `n-1`). If `p > n-1` or any entry would go negative,
the step **ABORTS** (undefined).

**HH run, termination, residue.** Repeat the step from `L=:L_0` to get `L_1,L_2,...` until either a
step aborts, or the list is all zeros `0^r` (r >= 0). In the latter case `L` **terminates**; if
`s(L)` is the number of steps taken, define **residue** `R(L) := r`.

**Head-block lists.** For integer `c >= 1`:
```
W+(c) := [c, c, c, c-1, ..., c-1]     (three copies of c, then c copies of c-1; length c+3)
W-(c) := [c, c, c-1, ..., c-1]        (two copies of c, then c+1 copies of c-1; length c+3)
```
A **head-block list** is `W^eps(c) union tail` (eps in {+,-}), i.e. `W^eps(c)` plus an arbitrary
further list `tail` all of whose entries are `<= c-1`, re-sorted into one list.

**"Raise two entries by 1" (UP2).** Given a list `L`, choose two POSITIONS `i != j`, add 1 to the
entries at those positions, re-sort. The result `L'` is "`L` with two entries raised by 1" (a
`UP2` move).

**Two shapes that appear in this project's census of the relevant population** (`(MON)`-odd: all
terminating lists `T` with `sum(T)` odd, comparing `R(T)` to `R(T')` where `T'` is `T` with ONE
coordinate/part increased by 1 in the underlying indexed vector — this can restructure the sorted
list in one of two ways):

- **Shape S1 ("head_parity_flip")**: `T = W-(c) union tail`, `T'` differs from `T` by: one HEAD
  entry moves `c-1 -> c` and one TAIL entry moves `t -> t+1` — i.e. `T' = W+(c) union tail'` where
  `tail'` is `tail` with one entry incremented. **This IS a genuine `UP2` move** (two entries, at
  two positions, each raised by 1) — verified positionally, `3057` of `3057` instances checked in
  our own census, `0` exceptions.
- **Shape S2 ("max_rises")**: `T = W-(c) union tail`, `T'` is what you get when the part that rises
  is already `T`'s current maximum, so the head block changes SIZE: `T' = W+(c+1) union tail''`.
  **THIS IS NOT A `UP2` MOVE, and our own project initially mis-described it as one before
  catching the error.** The arithmetic: `|W+(c+1)| - |W-(c)| = (c+4)-(c+3) = 1` (length changes by
  1, not preserved) and `sum(W+(c+1)) - sum(W-(c)) = (c+1)(c+3) - (c^2+2c-1) = 2c+4 >= 6` (the sum
  changes by `2c+4`, never by exactly `2`, which is what a genuine two-entries-raised-by-1 move
  would require). **So `S2` pairs `(T,T')` are never `UP2` pairs, at any `c`** — this was proved
  arithmetically, not by census, after two independent engines flagged the original description as
  unsatisfiable and were found to be right.

The population sizes (censused directly, at `sum(T) <= 18`, by testing `0 <= R(T)-R(T') <= 1`
literally on every instance): **S1: 3,057 instances, 0 violations. S2: 1,016 instances, 0
violations.** Total population **4,073**, both censused with an empty exclusion list. (This direct
census is a fact on its own, independent of anything below — it is NOT itself a proof, and it is
not what Theorem C1-Z is trying to add; C1-Z is an attempt to explain WHY the census comes out
`{0,1}` via a mechanism, rather than merely reporting that it does.)

## 2. Two lemmas, PROVED, with their proofs (use freely, but check them — nothing here is off
## limits to your adversarial review)

**Lemma C1-X.** For every terminating list `L` of length `n`, with `s(L)` steps and pivots
`p_1,...,p_s`: **(i) `R(L) = n - s(L)`. (ii) `2 * SUM_t p_t = sum(L)`.** Also: `R` is a trajectory
invariant, `R(L_t) = R(L)` for every `t` along a terminating run.

*Proof.* (i) Each step deletes exactly one entry (the pivot); the run stops when every remaining
entry is 0, after `n-s` entries remain, all zero — that count is `R(L)` by definition. (ii) A step
with pivot `p` deletes an entry `= p` and subtracts 1 from `p` other entries, so the list-sum drops
by exactly `2p`; the run ends at sum 0, so summing over all steps gives (ii). The trajectory
invariance follows from (i) applied at each `L_t`: `R(L_t) = (n-t) - s(L_t)`, and `s(L_t) = s(L)-t`
since running `L_t` for the remaining steps reproduces the same terminal state as running `L` from
the start. QED.

**Lemma C1-Y (the terminal lemma).** For every `r >= 2`: `R(0^r) = r`, `R((1,1,0^{r-2})) = r-1`,
hence `R(0^r) - R((1,1,0^{r-2})) = 1`.

*Proof.* `0^r` is already terminal (all zeros), so its residue is `r` by definition. For
`(1,1,0^{r-2})` the maximum is 1; the HH step deletes it (pivot `p=1`) and subtracts 1 from the
next-largest entry — the other `1` — leaving `0^{r-1}`, which is terminal. So `s=1`, and by C1-X(i)
`R = (r) - 1`. QED. *(Independently spot-checked by our project for `r=2..12`, 11 of 11.)*

## 3. The lockstep dichotomy that Theorem C1-Z is built on

Take a pair `(A,B)` where `A` is a head-block list and `B` is `A` with two entries raised by 1
(a `UP2` pair — note per §1 this framing literally applies to shape S1 pairs; whether it applies
to S2 pairs is exactly part of what you are asked to check). Run the HH step on `A` and `B`
**in lockstep** (apply the step independently to each list at each stage `s`, for as long as both
are defined), producing `A_0,A_1,...` and `B_0,B_1,...`.

**Candidate Lemma C1-W**, quoted exactly:
> "(C1-W) Inside the head-block family, the lockstep difference is step-invariant: at every state,
> `B_s` is either equal to `A_s` or again `A_s` with two entries raised by 1; and EQ is absorbing
> (once merged, always merged)."

This is currently a **CENSUS**, not a proof: **6,469 state pairs examined, 0 breaks of the
invariant** — and (this is the fact we are telling you about up front, found by this project in a
round AFTER the one that stated Theorem C1-Z below) **that 6,469-state-pair census stepped 709
`S1` pairs and 0 `S2` pairs. Quoted exactly: "Candidate Lemma C1-W covers `S1` and only `S1`... so
`S2`, 1,016 of the 4,073 odd-half instances, still has NO mechanism and Theorem C1-Z's hypothesis
does not reach it."**

From stepping 709 `S1`-shaped pairs in lockstep (`sum(T) <= 14`), the outcomes and their `delta :=
R(A_0) - R(B_0)` (equivalently `R(T) - R(T')`) sort into exactly two rows:

| branch | delta | why |
|---|---|---|
| trajectories MERGE (become equal at some stage `s`, `A_s = B_s`) | **0** | equal states have equal residues, and `R` is a trajectory invariant (Lemma C1-X corollary) |
| trajectories NEVER merge -> end at `A = 0^r` vs `B = (1,1,0^{r-2})` | **1** | **Lemma C1-Y** |

## 4. Theorem C1-Z, quoted EXACTLY

> "**Theorem C1-Z (PROVED, CONDITIONAL — and the conditional half is exactly C1-W).**
> **If the lockstep dichotomy holds** — every head-block pair either merges or preserves the
> 'raise two by 1' difference to the terminal signature — **then `(MON)` holds, with delta ∈
> {0,1}**, and both values are the ones C1-X/C1-Y compute."

and, from the same source:

> "`(MON)`'s `{0,1}` histogram is no longer a census of outcomes. The outcomes are proved; what
> remains a census is the DICHOTOMY ITSELF, i.e. Candidate Lemma C1-W."

Here `(MON)` (restricted to the odd-sum population under discussion, "`(MON)`-odd") is the claim:
for every terminating list `T` with `sum(T)` odd and `T'` the corresponding list with one part
raised (shape S1 or S2 as in §1), `0 <= R(T) - R(T') <= 1`. The FULL `(MON)`-odd population that
the claim "`(MON)` holds" is about is **both shapes together: 3,057 (S1) + 1,016 (S2) = 4,073**.

## 5. What we want from you

**Part A — verify or refute the gap we told you about.** Theorem C1-Z's hypothesis is stated as
"the lockstep dichotomy holds... every head-block pair." Its conclusion is stated as "`(MON)`
holds" (unqualified — i.e., apparently claiming to cover the full 4,073-instance population, both
shapes). But: (a) C1-W's own machinery (§3) is phrased in terms of `UP2`-type pairs — "`B_s` is
`A_s` with two entries raised by 1" — and (b) §1 established, arithmetically, that shape S2 pairs
are **never** `UP2` pairs at all. Work through this carefully and answer precisely: **does Theorem
C1-Z's conclusion, taken literally, claim more than its own hypothesis (even if C1-W were fully
proved) could possibly deliver?** Is this a real logical gap in the theorem as stated, purely as a
matter of what implies what — independent of whether C1-W itself is true? Do not just agree with
us; check it by actually tracing what "the lockstep dichotomy" would have to mean for it to cover
S2, and whether that meaning is even well-formed given S2 pairs aren't UP2 pairs to begin with.

**Part B — look for anything else wrong, independent of the S2 issue.** Assuming for this part that
somehow the hypothesis genuinely covers the whole population (or restricting attention entirely to
the S1 half, where the UP2 framing is at least well-formed), scrutinize the deduction from
"lockstep dichotomy" to "`(MON)` holds with delta as computed" for OTHER gaps:
1. **Is the two-branch split in §3 actually exhaustive?** Could a lockstep pair do something other
   than "merge" or "run to the exact terminal signature `0^r` vs `(1,1,0^{r-2})`" — e.g., could `A`
   terminate (reach all zeros) while `B` has not yet, in a way that is neither "merged" nor
   matches the claimed terminal pair, because the two lists have different lengths at that point,
   or because "terminate" for one list while the other still has positive entries needs separate
   handling that isn't addressed?
2. **The "for every stage `s` for which both `A_s` and `B_s` are defined" clause in C1-W.** Could
   one of the two lists ABORT (in the technical HH sense from §1: pivot exceeds the number of
   remaining entries, or an entry would go negative) while the other does not, for some head-block
   pair? If so, what does "the dichotomy holds" even mean at that point, and does Theorem C1-Z's
   proof implicitly assume this never happens without justifying it?
3. **Does the terminal-signature argument in Lemma C1-Y actually apply as invoked?** C1-Y assumes
   you already have `A = 0^r` and `B = (1,1,0^{r-2})`; the "never merge" branch of C1-W's dichotomy
   only guarantees `B_s` is `A_s` with two entries raised at every step. Check explicitly: if `A`
   runs down to `0^r` and the pair has never merged, does "`B_s` is `A_s` with two raised" at that
   exact step FORCE `B = (1,1,0^{r-2})` (as opposed to, say, raising a different pair of the r
   zeros in the "same" set, or `B` having reached its own terminal state at a different step count
   than `A`)? Trace this precisely.
4. **Labeling honesty**: given that C1-W is explicitly only a CENSUS (not proved) and, per Part A,
   possibly doesn't even reach the whole population its "PROVED, CONDITIONAL" companion theorem
   claims to settle — is "Theorem C1-Z (PROVED, CONDITIONAL)" a fair label for what has actually
   been established, or does it overstate the conditional's scope regardless of whether C1-W turns
   out to be true?

**Part C — is there a way to save the conclusion?** Independent of whether the STATED proof of
Theorem C1-Z has a gap for shape S2: is there any DIFFERENT, more direct argument — not going
through the "UP2 lockstep" machinery of C1-W at all — that could establish `0 <= R(T)-R(T') <= 1`
for shape S2 pairs specifically, using only the definitions and the two proved lemmas (C1-X, C1-Y)
of §2? (You do not need to find such an argument — we are asking whether you can see one, partially
see one, or see why one is hard, given what shape S2 actually does structurally: the head block
changes SIZE rather than just having two entries swapped.)

## 6. What to hand back

Answer Parts A, B, and C separately and explicitly. For each specific issue you raise, say whether
you consider it (i) a genuine flaw in the theorem/proof as stated, (ii) a real gap in scope that
does not necessarily make the stated claims false but means they are not yet established, or (iii)
not actually a problem once you traced it carefully (and say why). End with one overall verdict:
**BROKEN** (you found a genuine flaw — state the sharpest one), **INCOMPLETE BUT NOT FALSE**
(the proof under-delivers relative to its label, but you found no reason to think `(MON)`-odd is
actually false), or **HOLDS UP** (you tried to break it and could not, after genuinely checking the
points above). If you could not make progress on some part, say so plainly rather than padding —
that is a valid answer too.
