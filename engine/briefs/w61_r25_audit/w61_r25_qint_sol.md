You are reviewing a REVIEW BRIEF — a document that will be handed to an independent
adversarial mathematics reviewer. You are NOT being asked to review the mathematics.

Answer exactly ONE question:

**What in this document would cause a competent reviewer to answer a DIFFERENT QUESTION
than the one being asked?**

This is a QUESTION-INTEGRITY review. Concretely, look for: instructions that contradict
each other; an obligation stated as withdrawn in one place and demanded in another;
scope statements that do not match the scope the report format asks for; grading rules
that could be read two ways; anything that would push a reviewer toward a verdict rather
than toward a finding; labels, cross-references, or section numbers that do not resolve;
held-out calibration rows whose wording does not determine a unique answer; and any place
where the document tells the reviewer to do X and then, elsewhere, tells them not to.

Rank your findings by how likely each is to change what the reviewer actually does.
Be specific: quote the conflicting passages. Do NOT review the mathematics. Do NOT
summarise the document. Maximum 1200 words.

=== THE DOCUMENT BEGINS ===
# GFAN family — SECOND-FAMILY round (S3-D3a) **and** first round on Theorem GFANnu (S3-D3b) — codex `gpt-5.6-sol`

**Driver note (do NOT act on this box; it is addressed to the operator, not to you).**
Queue row **Q33**. Dispatch method: codex TUI in screen session `codex`, `/model` ->
`gpt-5.6-sol` high, then send ONE line -- `Read prompts/w61_S3_GFAN_sol.md and execute
the task in it.` -- and confirm "Working" appears on a `hardcopy`. Do not paste the
brief into the TUI. If the approval box appears, answer `a`. A Qwen round on the
GFANnu half runs in parallel; the two judges are independent and neither is shown the
other's brief or output.

TARGET, in two parts:
* **Part 1 (the group):** Lemma CAP, Corollary CAP1, Theorem RIG, Corollaries RIG-1
  and RIG-2, Lemmas FAN-4', FAN-8', FAN-6', Theorem GFAN2, Corollaries GFAN2-HC and
  GFAN2-L3.
* **Part 2 (the computer-assisted one):** Theorem GFANnu (`nu <= 6`) and Corollary
  GFANnu-HC.

## Who you are

You are an INDEPENDENT adversarial reviewer. You are not the author and have no stake
in the result. Your job is to find defects. A CLEAN verdict that misses a real defect
is the worst outcome; a false alarm you retract after computing is fine. Everything
below is under review, including every line labelled PROVED.

Part 1 has had **one** adversarial round, from a different model family. **You are not
being shown that report and you must not go looking for it** -- see the read
restriction. Your round is the second of the two independent families this document
requires, and two families agreeing is the whole point: a round that reproduces another
judge's reading because it read that judge is worth nothing here. Several passages have
been **edited since that round**. They are not marked, deliberately: find them the way
you would find anything else, by checking every line.

## Read restriction -- a hard constraint, not a preference

You are running with filesystem access inside a repository that contains the full
working record of this project, including other judges' reports and the author's notes
on what he expects you to find. Reading any of it destroys the independence this round
exists to provide.

* **Everything you need is in this file.** Treat it as the complete, authoritative text.
* **Do NOT open, grep, or otherwise read**: `notes/proofs/wowii61_draft.md`, anything
  under `notes/reviews/`, anything matching `problems/wowii/w61_*`, anything matching
  `prompts/w61_*` other than this file, anything under `orchestration/`, or any file
  whose name contains `dispatch`, `adjudicate`, `harvest`, `gfan`, `embed`, or `qwen`.
  In particular **do not run the author's archived enumeration scripts** -- reproduce
  anything you need from the specification, in your own code.
* You **may** write and run your own scratch code, and read files you created yourself.
* If a joint cannot be settled without a restricted file, **say so and mark that joint
  UNRESOLVED**. Do not read it. Do not search the web.

**Write your report to `problems/wowii/w61_S3_GFAN_sol.md`** (create it; do not read
any other file in that directory). Put your scripts in
`problems/wowii/w61_S3_GFAN_sol_check.py` and **keep their raw stdout** in
`problems/wowii/w61_S3_GFAN_sol_check.out` -- raw output, not a hand-written summary.
Print the verdict line to the terminal as well.

## Why this target, and what turns on it

The line's remaining uncertified surface is exactly what is in this file. Everything
else in the project has been through two independent families and is certified. So a
defect here is load-bearing in a way that a defect elsewhere no longer is.

Part 1 is a rigidity result and a case analysis: Theorem RIG says that a whole
structural layer, if non-empty, is forced into one named configuration `GFan(tau,L,nu)`;
Theorem GFAN2 then kills the `nu = 2` slice of it. Part 2 is a **computer-assisted**
theorem: four hand-proved bounds make a case list finite for each `nu`, and a finite
check inside that list finishes it. The finite check is printed in full in Appendix C.1
-- specification and data both -- so it is checkable without the author's files.

## REFUTE FIRST -- the required order of work

1. **Build your own tools and calibrate them before use.** Implement Havel-Hakimi from
   the specification below; calibrate against `residue(K2) = 1` and
   `residue(Cn) = ceil(n/3)` for `n = 3..9`, and print the calibration. **A number you
   report before your calibration is printed does not count.**
2. **Try to refute Theorem GFANnu by computation** (Part 2): regenerate the finite case
   list from the specification in Appendix C.1 for at least `nu = 1,2,3,4`, and find a
   shape that clears in exactly `L` steps and is **not** killed by Lemma FAN-6'. One
   such shape refutes the theorem. Reuse none of the printed numbers while doing this;
   compare only afterwards.
3. **Try to refute Theorem GFAN2** the same way, and Theorem RIG by construction: build
   a graph in the hard-core frame with `B_lo` non-empty and every low vertex
   B-universal, and check whether all five conclusions (a)-(e) actually hold.
4. **Then, and only then**, review the joints line by line.
5. Report what you could NOT check. That section is mandatory.

## Named joints -- give each an explicit verdict

| joint | what to check |
|---|---|
| **J-CAP** | Lemma CAP and Corollary CAP1: the degree cap and the `deg_A(b) = 1` it buys. Does the lower bound need `A` **maximum** or only maximal? Is the upper-bound arithmetic right at both boundaries (`n_b = 0` and `n_b = tau-1`)? Is any frame or reductio hypothesis used silently? |
| **J-RIG** | Theorem RIG (a)-(e) clause by clause. Where exactly does `diam = 4` enter? Is Lemma 4 used in the form it is stated? Is the trailing `nu <= L-1` correctly attributed? |
| **J-RIG-EQ** | Theorem RIG's word **"exactly"**: the proof matches each `GFan` clause to one of (a)-(e) and then asserts the converse. Is the converse actually definitional, or is something being smuggled? |
| **J-RIG12** | Corollaries RIG-1 and RIG-2. RIG-1 claims to remove a tightness argument from an earlier proposition -- does it? RIG-2's chain (`nu = 1` killed by Theorem FAN, `L = 2` empty, `L = 3` a single configuration) -- is each link earned? |
| **J-FAN4P** | Lemma FAN-4': the residue mass `2nu - E` and the `C`-entries `L + e_c`. Re-derive the degree-sum bookkeeping yourself; the `p`-terms are supposed to cancel via `tau = p + L`. |
| **J-FAN8P** | Lemma FAN-8': the escape bound `L <= 2nu - E`. Are the two subtracted sets disjoint and genuinely inside the block? Is the prefix inequality tie-safe? What does the lemma say at `E = 0`? |
| **J-FAN6P** | Lemma FAN-6' and its proof. Also the bracket listing which residues it kills: is that list right at its smallest cases? Is the treatment of zero entries stated, and used consistently between FAN-6' and FAN-4'? |
| **J-GFAN2** | Theorem GFAN2: Step 1's escape budget, Step 2's three `L >= 4` trajectories, and all eight `L = 3` rows. Simulate them yourself. Is the row list **complete** -- is anything excluded that should not be? |
| **J-CORHC** | Corollaries GFAN2-HC, GFAN2-L3, GFANnu-HC. Arithmetic and dependency only. |
| **J-FIN** | (Part 2) Theorem GFANnu's finiteness argument. The split into `E=0/L>=lam_1`, `E=0/nu+1<=L<lam_1`, `E>=1` -- disjoint? exhaustive? Is `lam_1 <= 2nu` justified? Does anything force `E <= nu-1`, and is it used consistently? Do the four imports match their statements? |
| **J-SPEC** | (Part 2) Appendix C.1's five conventions. Are they sufficient to pin the enumerated set exactly? Is the unlabelled/multiset reduction legitimate? Is the zero-inertness claim true -- test it. Is "no graphicality filter is needed" valid, and does its monotonicity run in the direction the conclusion needs? |
| **J-DATA** | (Part 2) The printed data. Recompute `s0(lam)` for the partitions of `2nu`, `nu <= 6`; check the boundary pair counts `0,1,3,7,14,26`; derive the closed form `S(nu)` yourself and check `0,3,24,110,397,1211`; regenerate the roster of `72` surviving `E >= 1` rows and ask whether it is **complete** -- does your run produce a survivor that is not printed? Is any printed row not actually a survivor? |
| **J-KILL** | (Part 2) Lemma FAN-6' against every printed survivor. Watch the boundary certificates `(w, 2nd) = (4, 2)` and `(3, 1)`. |
| **J-SCOPE** | Every statement in this file: what hypotheses does its own proof consume, versus what it is filed under? Report both under- and over-hypothesis. Under-hypothesis is a MATHEMATICS defect; over-hypothesis is bookkeeping. |

## Classify every defect

Tag each finding **MATHEMATICS** (a claim is false, a proof does not prove its
statement, an import does not match, an enumeration is incomplete or wrong, a statement
is used outside the hypotheses it was proved under) or **BOOKKEEPING** (label,
cross-reference, wording, a true statement stated imprecisely, a missing convention a
reader can supply uniquely). **State plainly in your verdict line whether any
MATHEMATICS defect was found.**

## Mandatory control section (a verdict without it does not count)

1. **Counterfactual availability.** Build a concrete instance that has the *shape* of
   an admissible configuration but **violates** one standing hypothesis -- e.g. a
   `Fan`/`GFan`-shaped degree sequence failing the reductio, or a residue total not
   equal to `2nu - E`. Confirm the named lemmas are **unavailable** on it, so the
   hypotheses are load-bearing rather than decorative. Print the instance.
2. **Witness validation in class-definition order.** For any graph you name as a
   witness, verify the class predicates in the order the class defines them
   (connected, then `A` **maximum** by exhaustive enumeration, then `diam`, then `f`,
   then non-forest, then `residue` vs `alpha`) and print each.
3. **Vacuity honesty.** If your search box contains no instance satisfying the full
   hypotheses of a composite statement, **say so explicitly** and do not present the
   absence of a counterexample as positive evidence. Attack the ingredients separately
   instead, and label that as what it is.
4. **What I could NOT check.** Mandatory. Every joint or sub-claim you did not settle,
   and why.

## Verdict tags -- use exactly one

`CLEAN` (no defect of either class) - `PARTIAL` (bookkeeping defects only, no
mathematics defect) - `GAP` (a proof obligation you could not verify, stated as such,
with what would settle it) - `REFUTED` (an explicit counterexample, printed in full).

## Report format

Open with a single `VERDICT:` line, then `TEXT VERSION REVIEWED: w61_S3_GFAN_sol
(Q33)`. Then the joint table with one verdict per named joint, then the defect list
with a MATHEMATICS/BOOKKEEPING tag on each, then the refutation log (what you tried and
what it produced, with code output), then the mandatory control section, then "What I
could not check".

---

## Appendix A -- the standing setting

`G` is a finite simple graph; `A` is a **maximum** independent set; `B = V \ A`;
`tau = |B|`; `alpha = |A|`; `f` is the forest number (largest vertex set inducing a
forest); `residue` is the Havel-Hakimi residue (repeatedly delete the largest entry `d`
and subtract 1 from the next `d` entries; the residue is the number of zeros left).

* **hard-core frame** := `G` connected, non-forest, `diam(G) = 4`, `f = alpha+1`
  (no reductio).
* **hard core** := the hard-core frame **plus** `residue = alpha` (the reductio), plus
  `tau >= 4`.

`B_lo` / `B_hi` are the low (`deg <= tau`) / high (`deg >= tau+1`) vertices of `B`;
`L = |B_lo|`, `p = |B_hi|`, `tau = p + L`. `nu` is the number of non-edges of `G[B]`;
`mbar` is the number of non-edges lying inside `B_hi`. `B_lo^+` is the set of low
vertices having a non-neighbour in `B`. `A' = A \ {a0}`. `C` is `a0` together with the
`L` low vertices; the `C`-part below is its value multiset at the start of step `p+1`.

**The configuration `GFan(tau, L, nu)`.** `B_lo` is non-empty, all of its vertices are
B-universal with `deg_A = 1`, sharing one common A-neighbour `a0` adjacent to all of
`B`; all `nu` non-edges of `B` lie inside `B_hi`; all of `B_hi` is high; and no
`a` in `A \ {a0}` has a neighbour in `B_lo`. `Fan(tau,L)` is the case `nu = 1`.

**Facts you may assume without refereeing them** (all separately certified; check only
that each *import* matches -- hypothesis supplied = hypothesis required, conclusion
used = conclusion proved; a mismatched import IS in scope and IS a MATHEMATICS defect):

* **Lemma 4**: in the frame, any two adjacent vertices of `B` have a common
  A-neighbour.
* **Observation R1**: in the frame, `diam = 4` implies `B` is not a clique, so
  `nu >= 1`.
* **Lemma C\***, **(F-b)**: the frame facts about occurring types.
* **Lemma S**, **Lemma DICH**, **Lemma Z+**, **Lemma F3'**, **Theorem K**: the
  certified toolkit.
* **Theorem MB**, **Corollary MB1** (`nu = mbar <= L-1`, so `L >= nu+1 >= 2`, when
  every low vertex is B-universal), **Theorem SL**, **Proposition L2**.
* **Theorem FAN**: the whole `Fan(tau, L>=2)` family is eliminated from the hard core.
* **Lemma TAIL**: stated in Appendix C where it is used.
* **Favaron-Maheo-Sacle**: `residue <= alpha`.

---

## Appendix B -- Part 1, the text under review

### A. The degree cap, and the one-line rigidity it buys

> **Lemma CAP (degree cap on low vertices).** Let `A` be a **maximum** independent
> set, `B = V∖A`, `τ = |B|`, and let `b ∈ B_lo` have `n_b` non-neighbours in `B`.
> Then **`1 ≤ deg_A(b) ≤ n_b + 1`**.
>
> *Proof.* `deg_A(b) ≥ 1`: otherwise `N(b) ⊆ B`, so `A ∪ {b}` is independent,
> contradicting maximality of `A`. For the upper bound,
> `deg_B(b) = (τ−1) − n_b`, and `b ∈ B_lo` means `deg(b) ≤ τ`, so
> `deg_A(b) = deg(b) − deg_B(b) ≤ τ − (τ−1−n_b) = n_b + 1`. ∎
>
> *Hypotheses used: only that `A` is a maximum independent set.* No frame, no
> reductio, no `diam` condition.

> **Corollary CAP1.** A **B-universal** low vertex has `deg_A(b) = 1` exactly.
> (`n_b = 0` in Lemma CAP.)

This is the step. Everything below is Lemma 4 bookkeeping on top of it.
### B. Theorem RIG

> **Theorem RIG.** Work in the **hard-core frame**, and suppose `B_lo ≠ ∅` and
> **every low vertex is B-universal** (`B_lo⁺ = ∅`). Then:
> (a) `deg_A(b) = 1` for every `b ∈ B_lo`;
> (b) the unique A-neighbours of the low vertices all coincide in one vertex `a₀`;
> (c) `a₀` is adjacent to **all** of `B`;
> (d) every non-edge of `B` lies inside `B_hi`, i.e. `ν = m̄`, and `ν ≥ 1`;
> (e) every `a ∈ A ∖ {a₀}` has `N(a) ∩ B_lo = ∅`.
>
> Consequently `G` carries **exactly** the configuration `GFan(τ, L, ν)` of Appendix A,
> with `ν = m̄ ≥ 1`. In the **hard core** (i.e. adding the reductio) one has in
> addition **`ν ≤ L − 1`**.
>
> *Proof.* (a) is Corollary CAP1. For (b), any two low vertices are adjacent
> (B-universality), so Lemma 4 gives them a common A-neighbour, which by (a) must
> be the unique A-neighbour of each; hence all coincide, in a vertex `a₀`. (For
> `L = 1` take `a₀` to be the unique A-neighbour of the unique low vertex.) For
> (c), fix `b ∈ B_lo`; for every `w ∈ B∖{b}` we have `b ∼ w`, so Lemma 4 gives a
> common A-neighbour of `b` and `w`, which by (a) is `a₀`; hence `a₀ ∼ w` for all
> `w ∈ B∖{b}`, and `a₀ ∼ b` by definition. (d): a non-edge of `B` incident to a low
> vertex would exhibit a non-neighbour of that vertex in `B`, contradicting
> B-universality; so every non-edge lies inside `B_hi` and `ν = m̄`. `ν ≥ 1` is
> Observation R1 (`diam = 4` ⟹ `B` is not a clique). (e): if `a ≠ a₀` had a
> neighbour `b ∈ B_lo` then `deg_A(b) ≥ 2`, contradicting (a). The `GFan(τ,L,ν)`
> clauses of Appendix A are exactly (a)+(b)+(c) ("`B_lo` all B-universal with
> `deg_A = 1` sharing one B-universal `a₀`"), (d) ("all `ν` non-edges of `B` inside
> `B_hi`") and (e) (the `A′`-attachment clause), plus "`B_hi` is high", which is
> the definition of `B_hi`. **Conversely**, the configuration `GFan(τ,L,ν)` of Appendix A
> *is* the conjunction of exactly those clauses and asserts nothing else, so the
> match is an equality and not merely an implication — which is what "exactly"
> claims. The final bound `ν ≤ L−1` is **Corollary MB1** applied
> to this hypothesis (all low vertices B-universal), and that corollary rests on
> Theorem MB → Theorem SL, which live in the hard core. ∎

**Scope, stated exactly (this is the D1/D3 species discipline).** (a)–(c) and (e)
need only: `A` a maximum independent set, plus **Lemma 4**, i.e. `f = α+1`; (d)
needs additionally `diam = 4` (Observation R1). So **(a)–(e) hold in the
hard-core frame, with no reductio**. Only the bound `ν ≤ L−1` needs the hard core
— and that is not a formality: see the measured witness in the companion section (not supplied).

### C. What it closes

> **Corollary RIG-1 (Proposition L2 without its tightness argument).** In the hard
> core with `L = 2`, Proposition L2 (a),(b) force `B_lo⁺ = ∅`; Theorem RIG then
> gives L2 (c) and (d) directly, and `ν ≤ L−1 = 1` with `ν ≥ 1` gives `ν = m̄ = 1`,
> i.e. `Fan(τ,2)`.
>
> This **removes the tightness re-run** from Proposition L2(c) ("Theorem MB is now
> tight, and re-running its degree count … forces `Σ deg_A = 2`"). That step was
> a pre-declared failure mode of the earlier error prior ( "tightness arguments need the inequality chain to be tight at
> *every* link, which is not spelled out"). It is now unnecessary: `deg_A(b) = 1`
> follows from the degree cap alone.

> **Corollary RIG-2 (the B-universal layer collapses to `ν ≥ 2`).** In the hard
> core with `L ≥ 2` and every low vertex B-universal, Theorem RIG gives
> `GFan(τ,L,ν)` with `1 ≤ ν ≤ L−1`; the case `ν = 1` is exactly `Fan(τ,L)`, which
> **Theorem FAN eliminates**. Hence that layer reduces to
> **`GFan(τ,L,ν)` with `2 ≤ ν ≤ L−1`** — in particular it is **empty for `L = 2`**
> (re-deriving Corollary FAN-HC's `L ≥ 3` on this layer) and, at **`L = 3`**,
> reduces to the **single** configuration `GFan(τ,3,2)`.

So the `L ≥ 3` push now has one named finite target on this layer, not a search:
kill `GFan(τ,L,2)`. Appendix A's LEAD already computes what that needs — with `ν` in
place of `1`, Lemma FAN-4 becomes "`A′` total `= 2ν − E`" and Lemma FAN-8 becomes
"`L ≤ 2ν − E`", so at `ν = 2` and `L ≥ 3` only `E ∈ {0,1}` survives, with `A′`
residue `4` resp. `3`; the LEAD asserts that among the partitions of those totals
only the single-part ones `[4]`, `[3]` clear in exactly `L` steps, and Lemma FAN-6's
backward induction kills every single-part residue `[w]`, `w ≥ 2`. **That is a
LEAD, not a proof** — the two generalized identities and the step-count enumeration
have not been written out. Writing them out is the next decisive step.
### A. The three generalized lemmas

> **Lemma FAN-4′ (residue mass).** In `GFan(τ,L,ν)` under the reductio, let `E` be
> the total number of `(vertex, step)` escapes of `C`-vertices during the high
> phase. Then at the start of step `p+1` the `A′` entries sum to exactly
> **`2ν − E`**, and the `C`-entries are `L + e_c` (`c ∈ C`, `Σ_c e_c = E`).
>
> *Proof.* Exactly Lemma FAN-4's count with `ν` in place of `1`. By FAN-1 and
> DICH(b), `Σ_{j≤p} D_j = Σ_{B_hi} deg − C(p,2)`. Here
> `Σ_{x∈B_hi} deg_B(x) = p(τ−1) − 2ν` (each of the `ν` non-edges lies inside `B_hi`
> and is missed by both endpoints) and `Σ_{x∈B_hi} deg_A(x) = p + R`, where
> `R := Σ_{a∈A′} deg(a)` and the `p` counts `a₀`'s edges to `B_hi`; so
> `Σ_{B_hi} deg = pτ − 2ν + R`. Splitting the decrements by recipient — `C(p,2)` to
> later high heads (DICH(b)), `p(L+1) − E` to `C`, the rest to `A′` — and using
> `p(L+1) = pτ − p² + p` and `2C(p,2) = p² − p`, gives
> `dec_{A′} = R − 2ν + E`, so the `A′` total is `R − dec_{A′} = 2ν − E`. Each
> `c ∈ C` starts at `τ` and is decremented `p − e_c` times, ending at `L + e_c`. ∎

> **Lemma FAN-8′ (escape bound).** In `GFan(τ,L,ν)` under the reductio, if `E ≥ 1`
> then **`L ≤ 2ν − E`**.
>
> *Proof.* Exactly Lemma FAN-8's argument. At an escape step `t` with `e_t ≥ 1`
> escapes, the head is high (FAN-1) so `D_t ≥ τ − t + 2`, the `p−t` remaining high
> vertices lie in `block_t` (DICH(b)), and so do the `(L+1) − e_t` non-escaping
> `C`-vertices; hence
> `|block_t ∩ A′| ≥ (τ−t+2) − (p−t) − (L+1) + e_t = 1 + e_t ≥ 2`, using
> `τ − p − L = 0`. Pick `x ∈ block_t ∩ A′`; as `block_t` is a prefix and the escaping
> `c ∉ block_t`, `v_t(x) ≥ v_t(c) ≥ τ − t + 1`. By FAN-4′ the `A′` mass at step
> `p+1` is `2ν − E`, so `v_{p+1}(x) ≤ 2ν − E`; and `x` is not deleted in steps
> `t … p` (all those heads are `B_hi`), so `v_{p+1}(x) ≥ v_t(x) − (p−t+1)`.
> Therefore `τ − t + 1 ≤ (2ν−E) + (p−t+1)`, i.e. `L = τ − p ≤ 2ν − E`. ∎

> **Lemma FAN-6′ (backward induction, generalized).** In `GFan(τ,L,ν)` under the
> reductio, the `A′` multiset at the start of step `p+1` **cannot** have a unique
> maximum `w ≥ 1` whose second-largest entry is `≤ w − 2`.
>
> *Proof.* Write `M_j` for the `A′` value multiset at the start of step `j`. All of
> `B_hi` (DICH(b)) and all non-escaping `C`-vertices lie in `block_j`, so the number
> of `A′` entries in `block_j` is `a_j = D_j − (p−j) − (L+1) + e_j ≥ 1 + e_j ≥ 1`,
> and — the block being a prefix of the sorted list — they are the `a_j` largest
> entries of `M_j`; in particular a maximum entry of `M_j` is decremented at every
> step. Suppose `M_{j+1}` has a unique maximum `v` and no entry of value `v−1`. Let
> `M_j` have maximum `w′` of multiplicity `μ`. If `a_j < μ`, the maximum does not
> drop, `w′ = v`, and the `a_j ≥ 1` decremented copies land at `v−1`, which
> `M_{j+1}` does not contain — contradiction. So `a_j ≥ μ`: every maximum drops,
> `w′ = v+1`, and `M_{j+1}` contains `μ` copies of `v`, forcing `μ = 1`. Every other
> entry of `M_j` is either in the block (its `M_{j+1}` value `+1`) or out of it
> (unchanged), so all are `≤ max(other entries of M_{j+1}) + 1`. Hence, writing
> `σ_{j}` for the second-largest entry of `M_j`, the pair (unique max `v_j`,
> `σ_j ≤ v_j − 2`) propagates backwards: from `(w, σ ≤ w−2)` at `p+1` one gets
> `v_{p+1−t} = w + t` and `σ_{p+1−t} ≤ σ + t ≤ w + t − 2 = v_{p+1−t} − 2` for every
> `t`, so the induction never stops. At `t = p` it gives `max(M_1) = w + p`. But
> `M_1` is the multiset of `A′` **degrees** and every `a ∈ A′` has `N(a) ⊆ B_hi`, so
> `max(M_1) ≤ p`. Contradiction. ∎
>
> 〔This is Lemma FAN-6 with its hypothesis stated in the form its proof actually
> uses. Lemma FAN-6 is the case `w = 2`, second entry `0`. The reason `1+1` escapes is that its
> maximum is not unique -- not that a `0` entry is present. **Convention (stated once, here, and used by every
> user of this lemma):** the `A′` value multiset carries its **zero entries** — every
> `a ∈ A′` contributes its current value, zero included — so the "second-largest
> entry" of a residue with a single positive part is `0`, not `−∞`. The residues this
> kills are exactly those with a **gap of at least 2 below a unique top**: `[w]` for
> every **`w ≥ 2`**, `[3,1]`, `[4,1]`, `[4,2]`, … ; it does **not** apply to `[1]`,
> `[1,1]`, `[2,1]`, `[2,2]`, `[2,1,1]`, `[1,1,1,1]`.
> 〕

### B. Theorem GFAN2

> **Theorem GFAN2.** For every `τ` and every `L ≥ 3` there is **no** graph with the
> `GFan(τ,L,2)` configuration satisfying `residue(G) = α(G)`.
>
> *Proof.* Assume `residue = α`, i.e. `s = τ`. By FAN-1 the heads of steps `1…p` are
> `B_hi`, so exactly `L` steps remain after step `p`; the multiset at the start of
> step `p+1` is `{L + e_c : c ∈ C}` together with an `A′` residue of total
> `2ν − E = 4 − E` (Lemma FAN-4′), and that multiset must clear in **exactly `L`**
> further steps.
>
> *Step 1 — the escape budget.* By Lemma FAN-8′, `E ≥ 1` forces `L ≤ 4 − E`. So for
> `L ≥ 4` we have `E = 0`, and for `L = 3` we have `E ≤ 1`.
>
> *Step 2 — `L ≥ 4`.* Here `E = 0`, the `C`-part is `[L]^{L+1}` and the `A′` residue
> is a partition of `4`. The partitions `[4]` and `[3,1]` have a unique maximum with
> the next entry at least 2 below it, so **Lemma FAN-6′ kills both**. For the
> remaining three, run the process: while the common `C`-value is `t ≥ 3` the head
> is a `C`-entry, the `L−k` other `C`-entries are the only entries of value `≥ 3`,
> so the block is exactly those and the `A′` entries (all `≤ 2`) are untouched;
> hence after `L−2` steps the list is `[2]^3` together with the untouched residue.
> Then
> `[2,2] : [2]^5 → [2,2,1,1] → [1,1,0] → 0` — 3 further steps, total `L+1`;
> `[2,1,1] : [2,2,2,2,1,1] → [2,1,1,1,1] → [1,1,0,0] → 0` — 3 further, total `L+1`;
> `[1,1,1,1] : [2,2,2,1,1,1,1] → [1]^6 → → →` — 4 further, total `L+2`.
> All exceed `L`, so none can occur. Every case is excluded.
>
> *Step 3 — `L = 3`.* The complete list of admissible shapes is eight rows
> (`E ∈ {0,1}`; `E ≥ 2` is excluded by Step 1), and it is short enough to display —
> the author's archived run:
>
> | `E` | `C`-part | `A′` residue | steps to clear | verdict |
> |---|---|---|---|---|
> | 0 | `[3,3,3,3]` | `[4]` | **3** | killed by FAN-6′ |
> | 0 | `[3,3,3,3]` | `[3,1]` | 4 | ≠ 3, and also FAN-6′ |
> | 0 | `[3,3,3,3]` | `[2,2]` | 4 | ≠ 3 |
> | 0 | `[3,3,3,3]` | `[2,1,1]` | 4 | ≠ 3 |
> | 0 | `[3,3,3,3]` | `[1,1,1,1]` | 5 | ≠ 3 |
> | 1 | `[4,3,3,3]` | `[3]` | **3** | killed by FAN-6′ |
> | 1 | `[4,3,3,3]` | `[2,1]` | 4 | ≠ 3 |
> | 1 | `[4,3,3,3]` | `[1,1,1]` | 4 | ≠ 3 |
>
> Only the two single-part residues clear in exactly `L = 3` steps, and Lemma FAN-6′
> kills both. Hence no case survives. ∎

> **Corollary GFAN2-HC (the B-universal layer needs `L ≥ 4` and `ν ≥ 3`).** In the
> hard core, if every low vertex is B-universal then `L ≥ 4` and `ν ≥ 3`.
> 〔**Superseded by Corollary GFANν-HC of Appendix C**, which raises this to `ν ≥ 7`,
> `L ≥ 8`. Kept because its proof is the hand-written one.〕
>
> *Proof.* Theorem RIG makes the instance `GFan(τ,L,ν)` with
> `1 ≤ ν ≤ L−1`; `ν = 1` is `Fan(τ,L)`, killed for `L ≥ 2` by **Theorem FAN**, and
> `ν = 2` is killed for `L ≥ 3` by **Theorem GFAN2**. `L = 1` is Corollary L1-short
> and `L = 2` forces `ν = 1`. So `ν ≥ 3`, whence `L ≥ ν + 1 ≥ 4`. ∎

> **Corollary GFAN2-L3.** In the hard core with `L = 3`, **some low vertex is not
> B-universal** (`B_lo⁺ ≠ ∅`). Equivalently: the entire `L = 3` layer of the hard
> core lives in the residual regime mapped in the companion section (not supplied).

---

## Appendix C — Theorem GFANnu and its enumeration

**Lemma TAIL, and the elimination of `GFan(τ,L,ν)` for every `ν ≤ 6`.**

Step 2 of Theorem GFAN2 used a trajectory that is uniform in `L`. That is not an
accident of `ν = 2`; it is a general reduction, and it turns the whole family into a
**finite** check for each `ν`.

> **Lemma TAIL.** Let `E = 0`, so the multiset at the start of step `p+1` is
> `[L]^{L+1} ∪ λ` with `λ` the `A′` residue, **`λ` non-empty**, `λ₁ := max λ`. If `L ≥ λ₁` then the
> number of further Havel–Hakimi steps is
> **`(L − λ₁) + s₀(λ)`, where `s₀(λ) := steps([λ₁]^{λ₁+1} ∪ λ)`**.
> Consequently, **still under `L ≥ λ₁`**, "clears in exactly `L` steps" is equivalent
> to **`s₀(λ) = λ₁`**, a condition on `λ` **alone** — within that range it does not
> depend on `L`.
>
> *Proof.* If `L = λ₁` the list already **is** `[λ₁]^{λ₁+1} ∪ λ` and the count reads
> `0 + s₀(λ)`, so there is nothing to prove; assume `L > λ₁`. Suppose at some
> stage the list is `[t]^{t+1} ∪ λ` with `t > λ₁` (true at
> `t = L` **since `L > λ₁`**). The head is `t`; the remaining entries of value `t` are exactly the
> other `t` copies, and every `λ`-entry is `< t`; so the block — the top `t`
> non-head entries — is exactly those `t` copies, they become `t−1`, and `λ` is
> untouched. Hence `[t]^{t+1} ∪ λ → [t−1]^{t} ∪ λ`, one step. Iterating from
> `t = L` down to `t = λ₁` uses `L − λ₁` steps and leaves `[λ₁]^{λ₁+1} ∪ λ`. ∎

> **Theorem GFANν (`ν ≤ 6`).** For every `τ`, every `ν ≤ 6` and every `L ≥ ν + 1`,
> there is **no** graph with the `GFan(τ,L,ν)` configuration satisfying
> `residue(G) = α(G)`.
>
> *Proof.* Four proved bounds make the case list finite for each `ν`:
> **FAN-4′** (the `A′` residue totals `2ν − E`, the `C`-part is `{L + e_c}` with
> `Σ e_c = E`), **FAN-8′** (`E ≥ 1 ⟹ L ≤ 2ν − E`, so `E ≥ 1` occurs only for the
> finitely many pairs `ν + 1 ≤ L ≤ 2ν − E`), **Corollary MB1** (`L ≥ ν + 1`), and
> **Lemma TAIL** (for `E = 0` and `L ≥ λ₁`, survival depends on `λ` alone; the
> finitely many boundary rows `ν + 1 ≤ L < λ₁ ≤ 2ν` are checked directly). Every
> shape in the resulting finite list either fails "clears in exactly `L` steps" or
> is killed by **Lemma FAN-6′**. The enumeration gives:
>
> | `ν` | `E = 0` rows FAN-6′ misses | `E ≥ 1` shapes tested | `E ≥ 1` rows FAN-6′ misses | verdict for `L ≥ ν+1` |
> |---|---|---|---|---|
> | 1 | none | 0 | none | ELIMINATED |
> | 2 | none | 3 | none | ELIMINATED |
> | 3 | none | 24 | none | ELIMINATED |
> | 4 | none | 110 | none | ELIMINATED |
> | 5 | none | 397 | none | ELIMINATED |
> | 6 | none | 1 211 | none | ELIMINATED |
>
> At `E = 0` the **only** residue clearing in exactly `L` steps is the single part
> `[2ν]`, for every `ν ≤ 6` — and `[2ν]` is killed by FAN-6′. ∎
>
> 〔**This is a computer-assisted proof**, and it is stated as such: the case list
> is finite *because* of FAN-4′/FAN-8′/MB1/TAIL, which are hand-proved above.
> Within that finite list, every step **except the completeness of the `E ≥ 1`
> survivor roster** is now checkable by hand from Appendix C.1 alone; that single
> remaining step is a seconds-scale machine check over an explicitly specified,
> closed-form-counted finite set. `ν = 1` is Theorem FAN and `ν = 2` is Theorem
> GFAN2, both of which have complete hand proofs; `ν = 3…6` rest on the
> enumeration.〕

> **Corollary GFANν-HC.** In the hard core, if every low vertex is B-universal then
> **`ν ≥ 7` and `L ≥ 8`**.
>
> *Proof.* Theorem RIG gives `GFan(τ,L,ν)` with `ν ≤ L−1`, i.e. `L ≥ ν+1`; Theorem
> GFANν eliminates every `ν ≤ 6`. ∎

**Cross-check of Lemma TAIL.** The
predicted count `(L − λ₁) + s₀(λ)` was compared with direct simulation on
**1 817** `(λ, L)` pairs (`ν ≤ 6`, `λ₁ ≤ L ≤ 15`) — **0 mismatches**.

**The obvious conjecture, stated as a conjecture.** The table's pattern is uniform:
at `E = 0` only `λ = [2ν]` survives, and every `E ≥ 1` survivor has a unique
maximum with a gap of `≥ 2` below it. If that holds for all `ν`, then **the entire
B-universal layer of the hard core is empty at every `L`** — which
would reduce the whole hard core to the `B_lo⁺ ≠ ∅` regime. Two precise sub-claims:
(C1) for every `ν` and every partition `λ` of `2ν` other than `[2ν]`,
`s₀(λ) ≠ λ₁`; (C2) every `(L,E)` survivor with `E ≥ 1` has `λ` with a unique
maximum whose second-largest entry is `≤ λ₁ − 2`. **Neither is proved.**

---

### C.1 The enumeration, in full

This subsection is self-contained: it fixes the shape-generation specification, then prints the whole finite case list in the only two places where
it is not mechanically regenerable — the `E = 0` step-count column and the complete
roster of surviving `E ≥ 1` rows.

**(B-1) The object being enumerated, specified exactly.**
At the start of step `p+1` of a `GFan(τ,L,ν)` run under the reductio, the
Havel–Hakimi value list is, by **Lemma FAN-4′**, exactly

> `C`-part: `L+1` entries, the `c`-th equal to `L + e_c`, with `e_c ≥ 0` and `Σ_c e_c = E`;
> `A′`-part: a partition `λ` of `2ν − E`;
> plus zero entries.

Five conventions, each of which the reader had to guess and now does not:

1. **Unlabelled.** The step count of a Havel–Hakimi list depends only on the value
   **multiset**, so the `C`-part is enumerated as a *multiset* `{L+e_c}` — i.e. `e` is
   a partition of `E` into at most `L+1` non-negative parts — and the `A′`-part as a
   *partition* of `2ν − E`. Distinct labellings of the same multiset are the same row.
2. **Zero entries are inert.** Verified, not assumed: over all `480` lists
   `[L]^{L+1} ∪ λ` with `ν ≤ 4`, `λ ⊢ 2ν`, `1 ≤ L ≤ 12`, padding with
   `0, 1, 2, 3, 4, 8` extra zeros gives **0** padding-dependent step counts
   (control run, block (D)). Reason: the block at each step is the `d`
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
5. **Range of the parameters.** `L ≥ ν + 1` (**Corollary MB1**); `E ≥ 1 ⟹
   L ≤ 2ν − E` (**Lemma FAN-8′**), which together force `E ≤ ν − 1`; and the `E = 0`
   rows split at `λ₁` into the `L ≥ λ₁` range where **Lemma TAIL** applies and the
   finitely many boundary rows `ν + 1 ≤ L < λ₁ ≤ 2ν`.

**(B-2) The `E = 0` column, printed in full.** By Lemma TAIL, for `L ≥ λ₁` the row
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
single part `[2ν]` — this is the sentence Appendix A already asserted, now with its
evidence attached. And `[2ν]` has unique maximum `w = 2ν ≥ 2` with second-largest
entry `0 ≤ 2ν − 2`, so **Lemma FAN-6′ kills it**. Hence **the `E = 0`, `L ≥ λ₁` rows
contribute nothing, for every `ν ≤ 6`.**

**(B-3) The `E = 0` boundary rows `ν+1 ≤ L < λ₁`, printed in full.** Outside Lemma
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

**(B-4) The `E ≥ 1` rows: the count is a closed form, and every survivor is printed.**
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
of the table in Appendix C, now printed as data rather than asserted as an output.

**(B-5) What a re-reader has to do.** To reproduce the theorem from this text it
suffices to (i) recompute `s₀(λ)` for the `159` partitions of (B-2) — one Havel–Hakimi
run each, all by hand — and confirm the bolded survivor is the only one; (ii) check
the `51` boundary pairs of (B-3); (iii) evaluate `S(ν)` from the closed form of (B-4)
and confirm the `72` printed survivors are the complete survivor set for those
`1 745` shapes; and (iv) apply the FAN-6′ certificate to each of the `9 + 72 + 6`
surviving rows. Only step (iii)'s completeness claim still asks the reader to trust a
machine run — and it is now a claim about an explicitly specified, closed-form-counted
finite set, not about an absent file.

**(B-6) Controls run before any of the above was written.** (i) The summary column
was reproduced by two independently written enumeration passes that agree line for
line. (ii) Lemma TAIL's
formula `(L−λ₁) + s₀(λ)` was re-cross-checked against direct simulation on the same
`1 817` `(λ,L)` pairs — `0` mismatches. (iii) The padding-inertness control of (B-1)(2)
was run on `480` lists × `6` paddings — `0` disagreements. (iv) `S(ν)`'s closed form
was evaluated independently of the enumeration loop and agreed on all six values.
