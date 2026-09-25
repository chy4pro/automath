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
# GFAN family paste brief — WOWII-61 S3, first adversarial round on §7.12/§7.13

**Driver note (do NOT paste / do not act on this box).** Self-contained: header +
verbatim appendix (the reviewer cannot read repository files). Queue row **Q25**.
Fresh conversation, one judge, no other judge's report shown to it. Same-source
check: §7.12 and §7.13 are **Claude-authored throughout** (owner-w61, round 5,
14:4x–15:0x CDT). A prior Qwen pre-chew round on the same target returned harvests
that were **explicitly not adopted** (no statement, witness or table from it entered
the draft), and the section was recorded as **Qwen-free** at the time it was written;
a Qwen judge is therefore eligible. **Lemma TAIL is refereed in a parallel row
(Q24)** — this brief refereess how §7.13 D *uses* it, not its proof.

TARGET: THE GFAN FAMILY — Lemma CAP, Theorem RIG, Corollaries RIG-1/RIG-2,
Lemmas FAN-4′/FAN-8′/FAN-6′, Theorem GFAN2, Theorem GFANν (`ν ≤ 6`)

## Who you are

You are an INDEPENDENT adversarial reviewer. You are not the author and have no
stake in the result. Your job is to find defects. A CLEAN verdict that misses a real
defect is the worst outcome; a false alarm you retract after computing is fine.
Everything below is under review, including every line labelled PROVED.

Work offline. Do not search the web; everything you need is in this message.

## Why this text and why now

§7.12 and §7.13 are the newest mathematics in the document and have had **zero**
adversarial rounds. They were written fast, in one hour, and they contain the only
**computer-assisted** result in the whole line: Theorem GFANν's `ν = 3…6` cases rest
on an enumeration, with only the *finiteness* of the case list hand-proved. That
demarcation — where the hand proof stops and the machine starts — is a named joint
below, and it is the single most important thing you will check.

Budget consequence: nobody has attacked this text. Spend your time on proofs and on
reproducing the enumeration yourself, not on out-enumerating prior numerics.

## REFUTE FIRST — the required order of work

For **each** named statement, in this order:

1. **Try to refute it.** Build instances satisfying all of its hypotheses and look
   for a failing conclusion. The multiset-level statements (FAN-4′, FAN-6′, FAN-8′,
   GFAN2, GFANν) are directly falsifiable by computation; the configuration-level
   statements (CAP, RIG) need a generator for the `GFan` configuration — write one.
   Say exactly what box you searched.
2. **Then verify the proof**, step by step, in the author's own order.
3. **Then audit the hypotheses** (joint J-SCOPE).

A statement you verified only by "the numbers agree" is **not** clean — say so.

## The named joints — one verdict each, by statement name

| joint | statement | what to attack |
|---|---|---|
| **J-CAP** | **Lemma CAP** + **Corollary CAP1** | `1 ≤ deg_A(b) ≤ n_b + 1` for `b ∈ B_lo`. The lower bound uses maximality of `A` (not maximal-ity): check the argument `N(b) ⊆ B ⟹ A ∪ {b}` independent is right, and that it needs `A` maximum or only maximal. The upper bound is arithmetic on `deg_B(b) = (τ−1) − n_b`: check it at `n_b = 0`, at `n_b = τ−1`, and when `b` has a neighbour counted twice. The stated hypothesis set is "only that `A` is a maximum independent set" — verify no frame, reductio or `diam` hypothesis sneaks in. |
| **J-RIG** | **Theorem RIG** (a)–(e) and its "Consequently" clause | (a) is CAP1; (b) uses Lemma 4 on two adjacent low vertices — check the common-neighbour conclusion is the form Lemma 4 supplies for *adjacent* pairs, and check the `L = 1` parenthetical is not doing hidden work; (c) quantifies over `w ∈ B∖{b}` — check the argument covers `w ∈ B_lo` and `w ∈ B_hi` alike; (d) is where `diam = 4` enters, via Observation R1; (e) is a one-liner off (a). Then the **"Consequently `G` carries exactly the configuration `GFan(τ,L,ν)`"** clause: the theorem proves five bullets and then asserts they *are* the `GFan` clause list — check clause by clause against the definition quoted in appendix section D, including "all of `B_hi` is high" and the `A′`-attachment clause. Is "exactly" earned (both directions), or is only one direction proved? |
| **J-RIG-NU** | The `ν ≤ L−1` clause of Theorem RIG | It is the only part needing the hard core, and it is imported from **Corollary MB1**, which is itself under review in a parallel round and currently has **zero clean rounds**. Do **not** referee MB1's proof here. Referee the *import*: is MB1's hypothesis ("every low vertex is B-universal") exactly Theorem RIG's hypothesis, is its conclusion exactly `ν ≤ L−1`, and is the scope claim "(a)–(e) hold in the hard-core frame, only `ν ≤ L−1` needs the hard core" correct as stated? The section claims a *measured witness* that the bound is false in the frame — check that the witness, as described, really is outside the hard core rather than a computation error. |
| **J-RIG12** | **Corollary RIG-1** and **Corollary RIG-2** | RIG-1 claims to remove a tightness argument from an earlier proposition; check it really does not reintroduce one. RIG-2 chains: `GFan(τ,L,ν)` with `1 ≤ ν ≤ L−1`; `ν = 1` killed by Theorem FAN; hence `2 ≤ ν ≤ L−1`; hence empty at `L = 2`; hence at `L = 3` the single configuration `GFan(τ,3,2)`. Check each implication, and check the `L = 2` conclusion against the `ν ≥ 1` floor. |
| **J-FAN4P** | **Lemma FAN-4′** (residue mass `2ν − E`) | The bookkeeping at general `ν`. Re-derive independently: `Σ_{x∈B_hi} deg_B(x) = p(τ−1) − 2ν` (are all `ν` non-edges inside `B_hi`, and is each missed by *both* endpoints — what if a non-edge has an endpoint outside `B_hi`?); `Σ_{x∈B_hi} deg_A(x) = p + R`; the decrement split "`C(p,2)` to later high heads, `p(L+1) − E` to `C`, the rest to `A′`" — is that split exhaustive and disjoint? Check the definition of an "escape" is the same in FAN-4′ and FAN-8′. Check the `C`-entry claim `L + e_c`. |
| **J-FAN8P** | **Lemma FAN-8′** (escape bound `L ≤ 2ν − E`) | The counting at an escape step: `|block_t ∩ A′| ≥ (τ−t+2) − (p−t) − (L+1) + e_t`. Check `D_t ≥ τ − t + 2` is available for a **high** head at step `t` (which direction of the head dichotomy supplies it), check the two subtracted sets are disjoint and inside the block, check the prefix argument `v_t(x) ≥ v_t(c)` when `c` escapes, and check the final inequality chain at `t = 1` and `t = p`. Does the lemma need `E ≥ 1`, or is it vacuous/true at `E = 0`? |
| **J-FAN6P** | **Lemma FAN-6′** (backward induction, generalized) | The hypothesis was **restated** — "cannot have a unique maximum `w ≥ 1` whose second-largest entry is `≤ w − 2`". Does the induction really need only that? Attack: (i) the claim that the `a_j` decremented `A′` entries are the `a_j` **largest** entries of `M_j` (prefix + ties); (ii) `a_j = D_j − (p−j) − (L+1) + e_j ≥ 1 + e_j` — where does `≥ 1` come from, and is it true at `j = 1`; (iii) the multiplicity case split (`a_j < μ` vs `a_j ≥ μ`) — is it exhaustive, and is "`μ = 1` forced" correct; (iv) the backward propagation `v_{p+1−t} = w + t`, `σ_{p+1−t} ≤ σ + t` — does it survive an entry *leaving* `A′`; (v) the terminal contradiction `max(M_1) ≤ p`. Also check the bracketed list of residues it does and does not kill (`[w]`, `[3,1]`, `[4,1]`, `[4,2]` vs `[1,1]`, `[2,1]`, `[2,2]`, `[2,1,1]`, `[1,1,1,1]`) — recompute it yourself. |
| **J-GFAN2** | **Theorem GFAN2** (`GFan(τ,L,2)` is empty for `L ≥ 3`) | Step 1's escape budget; Step 2's trajectory for `L ≥ 4` (the "while the common `C`-value is `t ≥ 3` the block is exactly the other `C`-entries" claim is a prefix claim — attack the tie case, and check the three displayed trajectories by your own simulation); Step 3's **eight-row table** at `L = 3` — reproduce every row's "steps to clear" independently and check the row list is **complete** (why are these eight the only admissible `(E, C`-part`, A′` residue`)` shapes? is `E ≥ 2` really excluded, and are all partitions of `4` and `3` present?). |
| **J-GFANNU** | **Theorem GFANν (`ν ≤ 6`) — the computer-assisted demarcation. THE JOINT THIS ROUND TURNS ON.** | Two separate questions, answer both explicitly. **(1) Is the finiteness argument hand-proved?** The case list is claimed finite because of FAN-4′, FAN-8′, Corollary MB1 and Lemma TAIL. Check the case split is **exhaustive**: `E = 0` with `L ≥ λ₁` (TAIL), `E = 0` with `ν + 1 ≤ L < λ₁ ≤ 2ν` ("checked directly"), and `E ≥ 1` (bounded by FAN-8′ to `ν+1 ≤ L ≤ 2ν−E`). Is every `(ν, L, E, λ)` covered exactly once? Is `λ₁ ≤ 2ν` justified? Is the use of MB1 legitimate given MB1 is under review elsewhere — i.e. does the theorem's statement carry the hypothesis MB1 needs? **(2) Is the enumeration reproducible?** You do not have the script. Reconstruct it from the specification in the appendix: for each `ν ≤ 6`, generate every admissible shape, run your own step-count, and report your own table of "rows FAN-6′ misses" and "shapes tested at `E ≥ 1`" (the appendix prints 0/3/24/110/397/1211 — **do not reuse those numbers**; produce yours and compare). If your counts differ, say whether the difference is a bookkeeping artifact or a hole in the proof. Also check the headline claim "at `E = 0` the **only** residue clearing in exactly `L` steps is the single part `[2ν]`, for every `ν ≤ 6`". If the enumeration is **not** reconstructible from the text as given, that is itself a reportable defect: a computer-assisted proof must be reproducible from its own description. |
| **J-CORHC** | **Corollary GFAN2-HC**, **Corollary GFAN2-L3**, **Corollary GFANν-HC** | Each is a short chain over `ν` and `L`. Check the inputs each one actually needs (Theorem FAN for `ν = 1`; GFAN2 for `ν = 2`; Corollary L1-short for `L = 1`; RIG for the configuration; MB1 for `ν ≤ L−1`) and check the arithmetic of the floors (`ν ≥ 3, L ≥ 4` then `ν ≥ 7, L ≥ 8`). One of them is marked superseded but kept — check the superseding statement really implies it. |
| **J-SCOPE** | **statement-hypothesis audit — every statement in §7.12/§7.13** | The document assigns each statement to one of three tiers: **reductio only** (`residue = α`, no structural hypothesis); **hard-core frame** (connected, non-forest, `diam = 4`, `f = α+1`); **hard core** (frame + reductio + `τ ≥ 4`). The assignment is quoted verbatim in appendix section T. For **each** of Lemma CAP, CAP1, Theorem RIG (a)–(e), the `ν ≤ L−1` clause, RIG-1, RIG-2, FAN-4′, FAN-8′, FAN-6′, GFAN2, GFAN2-HC, GFAN2-L3, GFANν, GFANν-HC: decide from **its own proof** which tier it needs, and report mismatches in **both** directions with a witness where one exists. Report separately every statement that is about **multisets only** and needs no graph hypothesis at all. |

## The three repair-species probes — run each by name, report a section for each

1. **Statement riders are separate proof obligations.** A "consequently", an
   "equivalently", a parenthetical, a status line, a "Kept because…" note — each
   carries its own burden. (Candidates: RIG's "Consequently … exactly `GFan`";
   FAN-6′'s bracketed residue list; GFAN2's "Every case is excluded"; the
   `〔computer-assisted〕` bracket; the "obvious conjecture" paragraph — verify it is
   stated as a conjecture everywhere it is used, including in later corollaries.)
2. **Scope-widening contagion.** After each generalisation in the text — and this
   whole section is a generalisation of `Fan` to `GFan`, `1` to `ν` — re-read the
   *following* sentences and check each independently at the new boundary. Lemmas
   FAN-4′/6′/8′ are claimed to hold "exactly as" their unprimed originals; check each
   claim of verbatim carry-over against the actual proof, especially where the
   original used `ν = 1` numerically.
3. **Box-vs-branch quantification artifact.** A claim quantified over a finite
   computational box, presented as quantified over the mathematical family. The
   scans run `L = 3…11` and `ν ≤ 6`; every general-`L` or general-`ν` claim must come
   from a closed-form argument, not from the scan. Find every place where a scan
   result is stated as a theorem, and every place where the numbers are correctly
   demoted to illustration — report both lists.

## T12 controls — all three amendments apply

1. **Counterfactual availability (REQUIRED).** For every lemma the text claims is
   **available** in the branch a control instance lands in, verify that lemma's
   hypotheses **on the control** — not only the steps the text executes. Name at
   least one lemma the text treats as available but which never actually executes,
   with the reason. Good controls: a `GFan`-shaped graph that fails the reductio; a
   frame instance with `ν > L−1`; a multiset shape with `E ≥ 1` at `L > 2ν − E`.
2. **Witness validation.** Any graph you exhibit must be validated against **EVERY**
   defining constraint of the class — most basic FIRST (connected; `A` a **maximum**
   independent set; `diam = 4`; `f = α+1`; and, clause by clause, the full `GFan`
   list: `B_lo` all B-universal with `deg_A = 1` sharing one B-universal `a₀`, all
   `ν` non-edges inside `B_hi`, `A′` attaching only inside `B_hi`, all of `B_hi`
   high). A witness violating the class definition is worse than no witness.
3. **Non-vacuity.** Any repaired statement you propose must ship at least one
   explicit instance (vertex/edge list, or explicit multiset) satisfying **all** of
   its own hypotheses; if you find none, say so and mark it possibly vacuous. Apply
   this to the *existing* statements too: does a `GFan(τ,L,ν)` graph satisfying the
   frame exist at all, for some small `(τ,L,ν)`? Exhibit one or report that you
   could not.

## Mandatory computation

* Write your **own** labelled Havel–Hakimi / `residueAux` from the spec in appendix
  section A and calibrate before trusting it: `residue(K₂) = 1`,
  `residue(Cₙ) = ⌈n/3⌉` for `n = 3…9`. Show the calibration output.
  **Reuse no number printed in this brief.**
* Write your own `GFan(τ,L,ν)` generator and your own shape enumerator; run every
  multiset under the canonical descending sort **and** randomised adversarial
  tie-breaks.
* Boundaries: `L = 1, 2, 3`; `ν = 1, 2, 3`; `L = ν`, `L = ν+1`, `L = 2ν`; `E = 0, 1,
  2`; `p = 0` and `p = 1`; `A′ = ∅`; `τ = 4` (the smallest hard-core `τ`).

## What is NOT under review

* The `residueAux` spec, Lemma 1, Fact 2, Lemma S/S′, Lemma F3′, Lemma DICH, Lemma
  Z⁺, Theorem K — certified by four independent judges across two model families.
  Use them freely.
* Lemma 4, Lemma C\*, Observation R1, (F-b) — background. **Lemma 4's proof is out of
  scope by provenance rule** (produced by a different reviewer family); you may and
  should check *how* §7.12 uses it.
* **Theorem LOW, Theorem SL, Theorem MB, Corollary MB1, Proposition L2** (appendix
  section F) — under review in a **parallel round**; supplied here only so you can
  check the imports. Referee the import, not the proof (joint J-RIG-NU).
* **Lemma TAIL's own proof** — under review in a parallel round. Referee only how
  Theorem GFANν *uses* it (joint J-GFANNU).
* Anything you find wrong in the above goes in "out of scope, noticed anyway" and
  does not drive your verdict.

## Deliverable format

Line 1: `VERDICT: CLEAN | PARTIAL | GAP | REFUTED` + one sentence.
Line 2: `TEXT VERSION REVIEWED: w61_S3_GFAN_qwen (Q25)`.
Then, in order:

1. **Refutation log** — per statement: box searched, what you built, what you found;
   plus your calibration output.
2. **Joint table** — one row per named joint (J-CAP, J-RIG, J-RIG-NU, J-RIG12,
   J-FAN4P, J-FAN8P, J-FAN6P, J-GFAN2, J-GFANNU, J-CORHC, J-SCOPE) with an individual
   verdict. **J-GFANNU must answer its two questions separately and must print your
   own reconstructed table.**
3. **Defects** — quoted line, why it fails, smallest configuration, repairable y/n,
   **does the CONCLUSION survive**, and **BOOKKEEPING** or **MATHEMATICS**.
4. A section **per named repair-species probe** (three sections, by name).
5. The **T12 section** (all three amendments, by number).
6. What you could NOT check, explicitly — including any part of the enumeration you
   could not reconstruct.
7. Out-of-scope observations, last.

**State plainly in your verdict line whether any MATHEMATICS defect was found**, and
state separately whether the computer-assisted part of Theorem GFANν is, in your
judgement, **reproducible from the text as written**.

## How the appendix is organised

* **A** — the conjecture, `residueAux` spec, Lemma 1, Fact 2. Definitions.
* **B** — the reduction, Lemma 4, Observation R1. Background.
* **C** — the τ-uniform toolkit, Lemma C\*, and the K-chain (Lemma Z⁺, Lemma DICH,
  Theorem K). Certified; context.
* **D** — the `Fan(τ,L)` set-up, Lemma FAN-1, Lemma FAN-3, Lemma FAN-4, Observation
  FAN-5, Theorem FAN, and the `GFan(τ,L,ν)` definition. Certified except where noted;
  context.
* **F** — §7.6's Theorem LOW / SL / MB / MB1 / L2. **Parallel round; imports only.**
* **G** — **§7.12 in full. UNDER REVIEW.**
* **H** — **§7.13 in full, including D. UNDER REVIEW** (Lemma TAIL's proof excepted —
  parallel round).
* **T** — the three-tier scope assignment, verbatim. Under review via J-SCOPE.

**Sections G, H and T are what you are reviewing.**


**Warning on lettering.** The appendix sections are lettered **A, B, C, …** by this
brief. The excerpts inside them keep the original document's own sub-section letters
("### A.", "### B.", …), which are **not** the appendix letters. When you cite a
location, quote the line, do not cite a letter alone.

=== APPENDIX — the text under review (authoritative) ===


### A. Exact statement, the `residueAux` spec, Lemma 1, Fact 2 (draft §1–§3)

## 1. Exact statement, read off the Lean

`G.diam : ℕ`, so `⌈(G.diam : ℝ)/3⌉` is the ordinary integer `⌈d/3⌉`. Both sides are
casts of naturals, so the Lean goal is equivalent to the integer inequality

> **(C61)**  for connected `G` on `n ≥ 2` vertices:  `residue(G) + ⌈d/3⌉ ≤ f(G)`

with

* `f(G) := largestInducedForestSize G = max { |S| : G.induce S is acyclic }`
  (`FormalConjecturesForMathlib/Combinatorics/SimpleGraph/Induced.lean`);
* `d := diam(G)` (Mathlib `SimpleGraph.diam`, `= ediam.toNat`; the usual diameter since `G`
  is connected and the vertex type is finite);
* `residue(G) := residueAux (degree sequence sorted descending)`
  (`FormalConjecturesForMathlib/Combinatorics/SimpleGraph/Residue.lean`), where
  `residueAux [] = 0`, `residueAux (0 :: s) = 1 + |s|`, and otherwise recurse on one
  Havel–Hakimi step.

The Python `residue_seq` in the verification script is a literal transcription of
`residueAux` (including `List.splitAt` truncation and ℕ‑truncated `(· - 1)`).
Sanity checks reproduced by stage W: `residue(K₂) = 1` (matches the `example` in the Lean
file) and `residue(Cₙ) = ⌈n/3⌉` for `n = 3…9`.

Throughout: `α(G)` = independence number, `μ(G)` = maximum matching size,
`∇(G) := n − f(G)` = decycling (feedback‑vertex) number, `m` = number of edges,
`Δ` = maximum degree.

---

## 2. Falsification stage (requirement 1) — no counterexample

Script: `notes/proofs/wowii61_verify.py`. Runtime 100 s for `all` (stages A–E) on one core.

```
[A: exhaustive n=2..7 (all connected graphs, atlas)] tested=995  violations=0  tight(slack=0)=151
    min slack = 0  at atlas n=2 E=[(0, 1)]: n=2 diam=1 residue=1 f=2
[B: exhaustive n=8 (cover of all connected 8-vertex graphs)] tested=108331  violations=0  tight(slack=0)=2640
    min slack = 0  at n=8 E=[(0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(7,6)]: n=8 diam=2 residue=7 f=8
[C: structured families] tested=1209  violations=0  tight(slack=0)=86
[D1: uniform random connected graphs n=9,10] tested=7994  violations=0  tight(slack=0)=14
[D2: simulated annealing minimising slack, n=9..13] tested=32376  violations=0  tight(slack=0)=1955
```

*Completeness of stage B.* Every connected graph has a non‑cut vertex, so every connected
graph on 8 vertices is `H + v` for some connected `H` on 7 vertices and some non‑empty
`N(v) ⊆ V(H)`. Stage B enumerates all `853 × 127 = 108 331` such pairs (no isomorphism
rejection — duplicates only cost time), hence covers all 11 117 connected 8‑vertex graphs.

*Structured families (stage C, `n ≤ 26`).* paths, cycles, path/cycle powers `P_n^k, C_n^k`
(`k ≤ 4`), lexicographic blow‑ups `P_m[K_r], C_m[K_r], P_m[E_r], C_m[E_r]`, chains of
cliques sharing cut vertices, theta graphs, caterpillars, random trees. 0 violations.

*Slack behaviour.* The minimum of `f − residue − ⌈d/3⌉` over all connected graphs with
`n ≤ 8`, by diameter:

| `d` | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| min slack (`n ≤ 8`, exhaustive) | 0 | 0 | 0 | **0** | 1 | 2 | 2 |
| min `f − α` | 1 | 1 | 1 | **1** | 2 | 2 | 4 |

So the inequality is **tight exactly up to `d = 4`** and gets loose for larger diameter.
All extremal (slack 0) examples with `d ≥ 5` are absent; the whole difficulty of the
conjecture sits at `d ≤ 4`.

---

## 3. Two basic reformulations

**Lemma 1 (residue = n − #steps).** Let `s(G)` be the number of Havel–Hakimi steps
`residueAux` performs, and `D₁, …, D_s` the successive heads (= current maxima). Then

1. `residue(G) = n − s(G)`;
2. `D₁ = Δ ≥ D₂ ≥ … ≥ D_s ≥ 1` and `Σᵢ Dᵢ = m`.

*Proof.* (1) `havelHakimiStep_length_cons` says each step shortens the list by exactly one,
and the recursion stops on a list whose head — hence, the list being sorted descending,
every entry — is `0`, returning its length. After `s` steps the length is `n − s`.
(2) Havel–Hakimi preserves graphicality (Havel 1955, Hakimi 1962), so at every step the
head `Dᵢ` is at most the number of remaining strictly positive entries; therefore the
ℕ‑truncated `(· − 1)` never truncates and one step decreases the sum of the list by exactly
`2Dᵢ` (`Dᵢ` removed as the head, `Dᵢ` further units removed by the decrements). The sum
starts at `2m` and ends at `0`. Monotonicity: the new list is obtained from the old one by
deleting the head and decreasing some entries, so its maximum cannot increase. ∎

**Theorem D (equivalent form).** (C61) is equivalent to
> `s(G) ≥ ∇(G) + ⌈diam(G)/3⌉`,

i.e. *the Havel–Hakimi process must run for at least `⌈d/3⌉` steps more than the decycling
number*. (Immediate from `residue = n − s`, `f = n − ∇`.) The classically known part is
`s ≥ ∇ + 1` (Corollary of Fact 2 + Lemma 3 below).

**Fact 2 (Favaron–Mahéo–Saclé 1991; short proof Griggs–Kleitman 1994).**
`residue(G) ≤ α(G)` for every graph `G`.
*(Cited, not reproved here. The bibliographic data is from memory and should be re‑checked
before formalisation; the inequality itself is asserted by the script on all 30 995 graphs
of stage E and never fails.)*

---



### B. The reduction, Lemma 4 / Lemma 5 / Theorem 6, Observation R1 (draft §7, §7.1)

## §7 新增（2026-08-18，root 推导）：残余情形归约为单一二分命题

已知：Fact 2（residue ≤ α）、Corollary B1（f ≥ α + ⌊(d−1)/4⌋ + 1）、Theorem A+B2
（d ∈ {1,2,3,5,6,9} 已决）、穷举显示**全部未覆盖图的直径恰为 4**。

d = 4 时：⌈d/3⌉ = 2，B1 只给 f ≥ α + 1，而 residue ≤ α 给 residue + 2 ≤ α + 2
——差恰好 1。故：

> **归约（root 推导并核验）**：Conjecture 61 的全部残余情形 ⟺
> 对每个连通图 G 且 diam(G) = 4：**f(G) ≥ α(G) + 2 或 residue(G) ≤ α(G) − 1。**

与 SC1/SC2 路线的关系（重要澄清）：GPT 的 d=8 chained-C₄ 反例（α=7, f=9）杀死的是
SC1 的**一般形式**；但残余缺口只在 d=4，而 d=4 时 SC1 退化为 f ≥ α+1 = 恰好 B1 已证。
因此 SC1 之死不影响本路线，真正待证的只剩上述二分（= SC2 在 d=4 的内容）。

攻坚已派（Qwen 新会话，2026-08-18 05:3x）：产出将落 notes/reviews/wowii61_qwen_solve.md。

## §7.1 Qwen 求解会话产出（08-18 06:0x，root 逐行亲核全部采纳）

**Lemma 4（配对障碍）** A 为最大独立集，B=V∖A，若 f=α+1，则对 B 中相异 u,v：
uv∈E ⟹ N_A(u)∩N_A(v)≠∅；uv∉E ⟹ |N_A(u)∩N_A(v)|≥2。
[证：G[A∪{u,v}] 的圈只能是三角形 u−v−a 或四圈 u−a−v−b；否则得 α+2 顶点诱导森林。✅]

**Lemma 5（径向路径强制模式）** 硬情形（diam=4, f=α+1）下，对任意最大独立集 A 与
任意径向路 v0..v4：v0,v4∈A、v1,v3∈B、v1≁v3 且 |N_A(v1)∩N_A(v3)|≥2。
[root 亲核关键步：I={i:v_i∈B} 中若有下标差 ≥3 则该对无公共邻居，违反 Lemma 4；
故 I 落在长度 ≤2 区间内，又必须触及 {0,1} 与 {3,4} ⟹ I∋1,3 且 0,4∉I。✅]

**Theorem 6（τ≤2 情形全解决）** diam=4 且 τ(G)=n−α ≤ 2 ⟹ 二分命题成立。
[机制：τ=1 是星（diam≤2）；τ=2 时 diam=4 逼出 xy∉E、A_x,A_y≠∅、|A_c|≥2，
度序列完全确定；若 residue=α 则 HH 恰 2 步，但 D1=a+c 且第二大度 b+c 必在第一步
被减 1 ⟹ D1+D2 ≤ m−1，与 ΣD_i=m 矛盾 ⟹ s≥3 ⟹ residue ≤ α−1。✅]

**Theorem 7（森林情形）** 连通森林 diam=4 ⟹ f ≥ α+2。（此前已由 Theorem C 覆盖，
此处给出更直接的证明：τ≥2 ⟹ α=n−τ ≤ n−2 = f−2。）

### 残余硬核（收窄后）
连通、非森林、diam=4、**f=α+1 且 residue=α**、τ≥3。
（注意这是两个极端条件的交，正对应 Obstacle O1 所说的"两个 slack 同时取最小"。）

### root 新观察（08-18 06:1x，可能是通向全解的钥匙）
**观察 R1（root 证明）：diam(G)=4 ⟹ B=V∖A 不是团。**
[证：A 极大独立 ⟹ 每个 a∈A 至少有一个邻居在 B（连通、A 独立）。若 B 是团，
则任意 a,a'∈A 有 a−b−b'−a' ⟹ dist ≤3；a∈A,b∈B 有 dist ≤2；B 内 dist ≤1。
故 diam ≤3，矛盾。∎]
**计数框架**：residue=α ⟺ HH 恰 τ 步（因 n−residue=n−α=τ）；由 Lemma 1(2)
Σ_{i≤τ} D_i = m，而 m = Σ_{v∈B} deg(v) − e(B)，且观察 R1 给出 e(B) ≤ τ(τ−1)/2 − 1。
若能证"D_i ≤ d_i − (i−1)"（d_i = 第 i 大度）则得 Σ D_i ≤ Σ_{i≤τ} d_i − τ(τ−1)/2
< m，矛盾，全案闭合。**但该递减断言一般不成立**（反例：k-正则图中 D_2 = d_2，
因未被减的位置 D_1+2 仍等于 d_2）——真正待补的正是"多个等度顶点"情形的控制。
此路线已回递给 Qwen 会话（tab 2130629790）。

---


### C1. The tau-uniform toolkit and standing conventions (draft §7.2)

## §7.2 owner-w61 回合 1（2026-08-18 07:xx）：T002 收割件核验 + 新的 head-decay 定理

### A. T002 收割件（`problems/wowii/qwen_w61_tau_harvest_0818.md`）逐行核验结论

| 段落 | 判定 | 说明 |
|---|---|---|
| §1 生存者矩阵界 `Σ_{j≤k} z_j ≤ Σ_i min(D_i,k)` | **正确但弱** | 行容量 D_i、列和 z_j 的 0-1 矩阵论证成立；这是纯容量（Gale–Ryser 型）界，不含 HH 的排序信息，Qwen 自己也指出了这点 |
| §2 累积推论 `h·q_h ≤ Σ_{i≤τ} min(D_i,q_h)` | **正确但基本空转** | `q_h = max(0, p_h−τ)`，而 `p_1=α` 时 `q_1=α−τ`，其余 h 多数给 `q_h=0` |
| §4 Family I（B 独立，c 个万有点 + 2 私叶） | **结论正确，c=3 的显式序列写错** | 原文 c=3 写成 `[4,4,3,3,3,1,1]`（7 项、和 19 为奇数、**非图序列**）；正确应为 `[4,4,3,3,3,3,1,1]`（n=8, m=11）。已重算：HH 轨迹 4→3→2→1→1，s=5，residue=3=α−1 ✓，结论不受影响。c≥4 的轨迹逐步复核无误 |
| §4 Family II（B 内一条边） | **正确** | 步 2 后的序列原文写作 `[c−1,2,1^{c+1},0^{c−2}]`（长度错），正确为 `[c−1,2,1^{c+1}]`；"≥2 个大于 1 的项 ⟹ 第 3 步不可能终止"这一关键推理成立 |
| §5 混合族未解 | **属实** | 见下 D 节：τ=3 混合族现已被完整参数化并穷举扫描 |

**采纳**：§1/§2 作为背景（弱），§4 两族的**终止形状论证**提炼为下面的 Lemma T 并推广。

### B. 新引理（全 τ 通用，均已数值验证，见 `problems/wowii/w61_lemH.py`）

以下恒设：G 连通，A 为最大独立集，B=V∖A（最小点覆盖），τ=|B|，α=|A|，
e_B=|E(G[B])|，m=|E|。对 d(G) 跑带标签的 Havel–Hakimi：每步排序降序、删去头、
把其后 D 项各减 1；s = 步数，D_1≥…≥D_s 为各步头值（Lemma 1(2)），K = 头集合，
其余 α 个条目称**生存者**。由 Lemma 1(1) residue=n−s，由 Fact 2 有 s ≥ τ。
**以下恒设 residue(G)=α，即 s=τ**（这是残余硬核的假设，用于反证）。

> **Lemma S（生存者度界）.** 每个生存者的度 ≤ τ；等价地，凡 deg(v) ≥ τ+1 的顶点必为头，
> 从而 `#{v : deg v ≥ τ+1} ≤ τ`。
> [证：生存者每步至多被减 1，τ 步后必须归零。∎]

> **Lemma T（终止形状）.** s=τ 当且仅当第 τ−1 步后的表恰为 `[D_τ, 1^{D_τ}, 0^…]`。
> [证：末步删头并把其后 D_τ 项减 1 后全为 0。∎ 这正是 Qwen Family I/II 证明的引擎。]
>
> **第二句（Repair V6 已落地，2026-08-18 17:5x CDT；改为反证之外陈述）.** 设 `G`
> 为任意图（**不设反证**），故由 Fact 2 有 `s ≥ τ`。若第 `τ−1` 步后有两个条目 `≥ 2`，
> 则由第一句得 `s ≠ τ`，**再由 Fact 2** 得 `s ≥ τ+1`，从而
> `residue = n − s ≤ n − τ − 1 = α−1`（Lemma 1(1)）。
> *（在 §7.2 B 的常设反证 `s=τ` 之内读，此句前件与第一句矛盾，故空真；上面这条
> 反证之外的陈述才是每个调用点实际引用的那条。）*

> **Lemma F3（衰减）.** 对 1≤j≤τ，第 j 步开始时每个生存者的值 ≤ τ−j+1。
> [证：只剩 j..τ 共 τ−j+1 步，每步至多减 1，末了须为 0。∎]

> **Lemma H（头衰减，本回合核心）.** 设第 i 个被删的头（2≤i≤τ）原度为 g_i、删除时值为 D_i，
> 令 h_i := g_i−D_i 为它在前 i−1 步中吸收的减量数。若 h_i ≤ i−2，则
> **D_i ≤ τ − i + 2 + h_i**。
>
> *证.* 该头在前 i−1 步中恰有 h_i 步被减，令 J 为其余 |J| = i−1−h_i ≥ 1 步之集。
> 取 j∈J，设它在第 j 步开始时的值为 v ≥ D_i。第 j 步被减的是紧跟头之后的 D_j 项，
> 而该头不在其中，故这 D_j 项的值都 ≥ v ≥ D_i。它们要么是生存者，要么是编号
> 在 {j+1,…,τ}∖{i} 中的头（共 τ−j−1 个）。若 D_i > τ−j+1，则由 Lemma F3 第 j 步
> 没有任何生存者的值达到 D_i，于是 D_j ≤ τ−j−1 < D_i，与 D_j ≥ D_i（头值不增，
> Lemma 1(2)）矛盾。故对每个 j∈J 有 D_i ≤ τ−j+1；取 j = max J ≥ |J| = i−1−h_i 即得。∎

> **Theorem N（新，全 τ）.** 设 G 连通，A 最大独立集，B=V∖A，τ=|B|，e_B=|E(G[B])|。若
> (i) 每个 b∈B 有 deg(b) ≥ τ+1；(ii) e_B ≤ τ−2；(iii) min_{b∈B} deg(b) ≥ 2e_B+3，
> 则 **residue(G) ≤ α(G) − 1**。
>
> *证.* 反设 residue=α，则 s=τ。由 (i)+Lemma S，B 的每个点都是头；又 |K|=τ=|B|，
> 故 **K=B**。于是 Σ_i g_i = Σ_{b∈B} deg(b) = m + e_B，而 Σ_i D_i = m（Lemma 1(2)），
> 故 Σ_i h_i = e_B。特别地 h_τ ≤ e_B ≤ τ−2，Lemma H 对 i=τ 适用，给出 D_τ ≤ 2 + h_τ，
> 从而 min_{b∈B} deg(b) ≤ g_τ = D_τ + h_τ ≤ 2 + 2h_τ ≤ 2e_B + 2，与 (iii) 矛盾。∎

> **Corollary N1.** 若 B 独立（e_B=0）、τ≥2 且每个 b∈B 有 deg(b) ≥ τ+1，则 residue ≤ α−1。

> **Corollary N2（和式版）.** 〔**08-18 S3 第二轮修订**：原文漏写 residue=α，作为无条件
> 命题为**假**；反例 K_{2,3}，见下〕若 **residue(G)=α(G)**（即 s=τ，本节 §7.2 B 的
> 恒设站位）且 (i) 成立、e_B=0，则所有 h_i=0，Lemma H 对每个 i≥2 给出
> D_i ≤ τ−i+2，于是 **m ≤ Δ(G) + τ(τ+1)/2 − 1**。
> 等价的可用形式（逆否，反证站位显式化）：**若 (i) 成立、e_B=0 且
> m > Δ(G) + τ(τ+1)/2 − 1，则 residue(G) ≤ α(G) − 1。**
>
> *反例（Qwen S3 第二轮提出，owner 亲核复现，`w61_adjudicate.out`）*：G=K_{2,3}，
> B=二元部。则 α=3、τ=2、e_B=0、B-度均为 3=τ+1（(i) 成立）、Δ=3、m=6，
> 而 Δ+τ(τ+1)/2−1 = 5 < 6。此图 HH 头为 (3,2,1)、s=3≠τ=2，故 residue=2=α−1，
> 反证站位本就不成立——**这正说明该站位必须写进命题**。
> 该缺陷不影响 Lemma H 与 Theorem N（二者均未使用 N2）。

**这条线覆盖了 Qwen 两族并推广到一切 τ**：Family I(τ,c)（B 独立、c 个万有点、2 私叶）
的 B-度为 c+1,c+1,c,…,c，当 c ≥ τ+1 时 Corollary N1 直接给出 residue ≤ α−1；
Family II(τ,c)（B 内一条边）同理由 Theorem N 覆盖。数值确认见
`problems/wowii/w61_famgen.out`：τ=3..7、c=2..10 共 65 个硬核实例，
**0 反例**，且 c ≥ τ+1 的全部实例 Theorem N 假设成立。

**数值验证（先跑后写，`problems/wowii/w61_lemH.out`）**：n≤7 穷举 995 图 + n=8 穷举覆盖
108 331 图 + n=9..12 随机 12 000 图 + 结构族，共 **116 873 连通图**（其中 residue=α 者
36 612 个）：Lemma S / F3 / H **失败 0**；Theorem N 假设命中 153 个图，**反例 0**。

### C. 一条重要的战略事实：硬核的 τ 无界

Family I(τ,c) 对每个 τ≥3、c≥τ 都真的落在残余硬核内（连通、非森林、diam=4、f=α+1、
n−α=τ；见 `w61_famgen.out` 逐例确认）。**因此逐个 τ 的情形分析永远不会终止**，
必须要 τ-一致的论证——Theorem N 正是第一个这样的论证。

### D. τ=3 的完整参数化与穷举扫描

> **Lemma P（τ=3 参数化）.** 设 G 在残余硬核中且 τ=3，A 为最大独立集，B={x,y,z}。
> 因 A 独立，每个 a∈A 的邻域是 B 的非空子集，故 G 在同构意义下**完全**由 7 个重数
> `mu[T] = #{a∈A : N(a)=T}`（T⊆B 非空）连同 G[B]（4 种同构型）决定。且
> (a) 每个 b∈B 有 A-邻居；(b) α=n−3 ⟺ 对每个 G[B]-独立的 S⊆B 有 |N_A(S)| ≥ |S|；
> (c) f=α+1 ⟺ 对每个 v，G−v 含圈（因 α+2=n−1）；(d) diam=4 ⟺ 存在两个出现的类型
> T_1,T_2 互不相交且其间无 G[B]-边（且此时 diam≤4 自动成立），特别地必有单点类型出现；
> (e) e_B ≤ 2（观察 R1）。

据此 `problems/wowii/w61_tau3.py` 对重数盒 `[0,MAX]^7 × 4 种 G[B]` 做**穷举**扫描
（不是搜索：盒内的每个 τ=3 硬核图都被覆盖，无需同构剔除，也不涉及 SAT/大空间穷举）。
MAX=5 结果（`problems/wowii/w61_tau3_max5.out`；MAX=3 结果同形，见 stdout）：

```
[tau=3] 参数元组 1 119 744；落在硬核-减-residue（连通、非森林、diam=4、f=α+1、τ=3）内：591 710
[tau=3] 按 e_B 分布: {e_B=0: 224035, e_B=1: 196075, e_B=2: 171600}  # e_B=3 从未出现 ⟹ 数值确认观察 R1
[tau=3] residue ≥ α（即反例）: 0
[tau=3] slack3 = m − (D1+D2+D3) 分布: {1: 171614, 2: 196571, 3: 223525}  # 最小恰为 1
```

**紧例（slack=1）**：B={x,y,z} 独立，A = {u_1,u_2 万有, w~{x,y}, e~{z}}；
n=7, m=9, α=4, 度序列 `[3,3,3,3,3,2,1]`，D=(3,3,2)，Σ_{i≤3}D_i = 8 = m−1，residue=3=α−1。

### E. 负面结果：逐项递减界这条路已死（省下后续工夫）

上面这个紧例中 d=(3,3,3,3,3,2,1)、D=(3,3,2)，故 δ_2 := d_2−D_2 = **0**：
§7 末尾 root 猜想的逐项断言 `D_i ≤ d_i − (i−1)` 在硬核内部就已失效（不必去正则图找）。
而所需的和式 `Σ_{i≤τ}δ_i ≥ σ + e_B + 1` 在该例中取等（1 = 0+0+1），**是紧的**，
因此任何只用逐项减量估计的证明都不可能补上这一步。Lemma H 换掉的正是这一环：
它不去估计 δ_i，而是用 Lemma F3 的**生存者衰减**把头值 D_i 直接压到 τ−i+2+h_i。

### F. 收窄后的残余（τ=3 与一般 τ）

一般 τ：硬核中必有 ¬[(i)∧(ii)∧(iii)]，即
**(1) 某个 b∈B 的度 ≤ τ，或 (2) e_B ≥ τ−1，或 (3) min_{b∈B} deg(b) ≤ 2e_B+2。**
τ=3 时 R1 给 e_B≤2，故 (ii) 只排除 e_B∈{0,1}；残余 = { e_B=2 } ∪ { 某 B-度 ≤ 3 }
∪ { min B-度 ≤ 2e_B+2 }。下一步：把 Lemma H 用到 i<τ（而不只是 i=τ）以吃掉
"某个 B-度小"的情形，并对 K≠B（即某个 B-点是生存者，其度 ≤ τ）单独处理。

---


### C2. Type notation and the structural facts (F-a)/(F-b)/(F-c) (draft §7.3 §0)


### 0. 记号与站位假设

设 A 为最大独立集，B=V∖A={x,y,z}。对 a∈A 有 ∅≠N(a)⊆B，记
`mu[T] = #{a∈A : N(a)=T}`（T⊆B 非空），并写 n_x=mu[{x}]、n_{xy}=mu[{x,y}]、
p=mu[{x,y,z}]；q = Σ_{|T|=2} mu[T]，r = Σ_{|T|=1} mu[T]，故 α=p+q+r、n=α+3、
A 的度谱为 3^p 2^q 1^r（A 的每个点度 ≤ τ=3）。记 codeg(u,v)=mu[{u,v}]+p，
e_B=|E(G[B])|，B 度记 X ≥ Y ≥ Z，**k := #{b∈B : deg(b) ≥ 4}**（只有 B 点能有度 ≥4）。

**反证站位**：设 f=α+1 且 residue=α，即 HH 恰 3 步，Σ_{i≤3}D_i=m，
且（Lemma T）第 2 步后的表恰为 `[D_3, 1^{D_3}, 0^…]`。

由 f=α+1（Lemma 4）、diam=4 得三条结构事实：
* **(F-a)** uv∉E(G[B]) ⟹ codeg(u,v) ≥ 2；uv∈E(G[B]) ⟹ codeg(u,v) ≥ 1。
* **(F-b)** 存在两个出现的类型 T₁,T₂ 互不相交且其间无 G[B]-边。
  [因 (F-a) 给 dist(b,b')≤2、故 dist(a,b)≤3，diam=4 只能由 A–A 对实现，
   而 dist(a,a')=4 ⟺ N(a)∩N(a')=∅ 且其间无 B-边。] 特别地必有单点类型出现，r ≥ 1。


### C3. Block occupancy and Lemma C* (draft §7.4)

## §7.4 owner-w61 round 3 (2026-08-18, written 08:26 CDT): block occupancy — a tau-uniform mechanism, and the measured obstacle to tau-uniformisation

Written in English per the 08-18 language directive; the standing conventions are
exactly those of §7.2 B (A a maximum independent set, B = V∖A, τ = |B|,
e_B = |E(G[B])|, labelled Havel–Hakimi on d(G), heads D_1 ≥ … ≥ D_s with
Σ D_i = m by Lemma 1(2)). Throughout §7.4 we work under the reductio hypothesis
**residue(G) = α(G)**, i.e. s = τ.

### A. The mechanism

Two new pieces of bookkeeping. At step j the algorithm deletes the head and
decrements the next D_j entries; call those D_j entries the **block** of step j.

* `hs := Σ_i h_i = Σ_{v ∈ K} deg(v) − m` — the total number of decrements
  absorbed by heads (K = the set of τ head vertices). When K = B this is e_B.
* `β_j := #{entries of the block of step j that are deleted as a head at some
  later step}`.

> **Lemma BO (block occupancy).** `Σ_{j=1}^{τ} β_j = hs`. In particular at most
> `hs` of the τ steps have `β_j ≥ 1`.
>
> *Proof.* Every decrement absorbed by a head is absorbed at exactly one earlier
> step, and at that step the head lies in the block. Summing over heads counts
> each such incidence once on each side. ∎

> **Lemma Z (a zero-occupancy step forces global decay).** If `β_j = 0` then
> every head deleted after step j already has value `≤ τ − j + 1` at the start of
> step j; consequently `D_i ≤ τ − j + 1` for all `i > j`.
>
> *Proof.* β_j = 0 says no later head lies in the block. The block is the prefix
> of the D_j largest entries after the head in the non-increasing order, so every
> entry outside it (other than the head) has value ≤ every block value; hence
> every later head has value ≤ min(block). All block entries are survivors, so by
> Lemma F3 their values at the start of step j are ≤ τ − j + 1. Head values never
> increase, so D_i ≤ τ − j + 1 for i > j. ∎
>
> *Tie-safety.* The argument never needs to know **which** of several equal
> entries the sort put in the block: a non-increasing prefix dominates its
> complement whatever the tie-break. (Verified computationally under randomised
> adversarial tie-breaking, see D.)

> **Lemma DEC (τ-uniform head decay).** For every `i ≥ hs + 2`:
> `D_i ≤ τ − i + 2 + hs`.
>
> *Proof.* Let `Z_i := {j < i : β_j = 0}`; by Lemma BO, `|Z_i| ≥ (i−1) − hs ≥ 1`.
> Put `j* := max Z_i`. Since `Z_i` is a set of distinct positive integers,
> `j* ≥ |Z_i| ≥ i − 1 − hs`. Lemma Z at `j*` gives
> `D_i ≤ τ − j* + 1 ≤ τ − i + 2 + hs`. ∎

**Why this matters: it is an independent re-derivation of Lemma H's payload.**
When K = B we have hs = e_B and every h_i ≤ e_B, so Lemma H's conclusion
`D_i ≤ τ − i + 2 + h_i` implies Lemma DEC; conversely Lemma DEC delivers exactly
the inequality Theorem N applies at `i = τ`, by a route that never mentions the
per-head bookkeeping `h_i` and never re-sorts a partially decremented list. Since
Lemma H is the single most load-bearing and most tie-sensitive step of §7.2, and
is currently in S3 adversarial review, this is a **cross-check of its engine by a
structurally different argument** — both verified numerically with 0 failures,
including under adversarial tie-breaking.

### B. The counting corollary and a Δ-side companion to Theorem N

> **Corollary CNT.** Under residue = α,
> `m ≤ min(τ, hs+1)·Δ + Σ_{i=hs+2}^{τ} (τ − i + 2 + hs)` (empty sum if hs+2 > τ).
> If moreover every `b ∈ B` has `deg(b) ≥ τ+1` — so K = B by Lemma S, hence
> hs = e_B — and `e_B ≤ τ − 2`, this reads
> `m ≤ (e_B+1)Δ + τ(τ+1)/2 − (e_B+1)(e_B+2)/2`.
> For `e_B = 0` this is exactly Corollary N2.
>
> *Caution (found by numerical test, not by inspection).* The `min(τ, ·)` is not
> cosmetic: dropping it makes the bound FALSE, e.g. `K_6` has τ=5, hs=10, m=15
> while `(hs+1)Δ + τ(τ+1)/2 − (hs+1)(hs+2)/2 = 4`.

> **Theorem N′ (τ-uniform, Δ-side companion of Theorem N).** Let G be connected,
> A a maximum independent set, B = V∖A, τ = |B|, e_B = |E(G[B])|, Δ = Δ(G). If
> (i) every `b ∈ B` has `deg(b) ≥ τ+1`; (ii) `e_B ≤ τ − 2`; and
> (iii′) `e_B · Δ < τ(τ−1)/2 + e_B(e_B+1)/2`, then `residue(G) ≤ α(G) − 1`.
>
> *Proof.* Suppose residue = α. By (i) and Lemma S every b ∈ B is a head, and
> |K| = τ = |B| gives K = B, so hs = e_B. Since A-degrees are ≤ τ < τ+1, Δ is
> attained inside B, so
> `m = Σ_{b∈B} deg(b) − e_B ≥ Δ + (τ−1)(τ+1) − e_B`. Combining with Corollary CNT
> (whose hypothesis e_B ≤ τ−2 makes the sum non-empty) and simplifying, a
> contradiction arises exactly when `τ(τ−1)/2 + e_B(e_B+1)/2 > e_B·Δ`, which is
> (iii′). ∎
>
> `e_B = 0` reduces (iii′) to `0 < τ(τ−1)/2`, true for τ ≥ 2: **Corollary N1 is
> the e_B = 0 case of Theorem N′.**

**Honest assessment of N′ (see D for the numbers).** N′ is the *Δ-small* side of
the same coin whose *min-degree-large* side is Theorem N; the two hypothesis sets
are formally incomparable. But on the 116 189-graph corpus N′'s hypothesis fires
137 times and **every one of those already satisfies Theorem N's (iii)** — so N′
buys no measured new coverage. Its value this round is the mechanism (BO/Z/DEC)
and the cross-validation of Lemma H, not the theorem statement.
*Firewall: this is not evidence for or against Theorem N being repairable or
broken; the S3 verdict on Lemma H is a separate matter.*

### C. Structural side: the τ-uniform analogue of C1–C3

> **Lemma C\* (τ-uniform).** Assume the hard core (G connected, f = α+1,
> diam = 4). Let `T₁, T₂` be occurring types realising (F-b) (disjoint, no
> G[B]-edge between them). Then every `b ∈ T₁ ∪ T₂` has `deg_A(b) ≥ 3`, hence
> `deg(b) ≥ 3 + deg_B(b)`.
>
> *Proof.* Let `b ∈ T₁` and pick any `b′ ∈ T₂`. There is no G[B]-edge between T₁
> and T₂, so `bb′ ∉ E`, and Lemma 4 (f = α+1) gives `|N_A(b) ∩ N_A(b′)| ≥ 2`. The
> witness `a₁` of type `T₁` is adjacent to b and, since `b′ ∉ T₁`, not adjacent to
> b′; so `a₁` is none of those ≥ 2 common neighbours. Hence `deg_A(b) ≥ 2 + 1 = 3`.
> Symmetrically for `b ∈ T₂`. ∎

This generalises **C3** (its τ=3, e_B=2 instance is precisely "deg(e_i) ≥ 4 for
the two path endpoints") and the `deg_A(w) ≥ 3` half of **C2**, and it is the
first B-degree bound in this line that does not case on the isomorphism type of
G[B].

### D. Numerical backing (run before the statements were written)

`problems/wowii/w61_blockocc.py` → `w61_blockocc.out`. Corpus: exhaustive n ≤ 7
(995), exhaustive cover of n = 8 (108 331), 10 000 random connected graphs
n = 9…12, structured families incl. Family I(τ,c) — **116 189 connected graphs,
36 664 of them with residue = α**. Every labelled claim is tested under the
canonical sort AND three randomised adversarial tie-breaks per graph:

```
[+D structured] tested=116189 residue=alpha:36664
   fails={'BO':0,'ZERO':0,'DEC':0,'KB':0,'NP':0,'CNT':0}
   hits={'KB':5888,'NP':137,'CNT':146656,'NP_new':0,'N_old':137}
```

(`KB` = "all B-degrees ≥ τ+1 ⟹ K = B and hs = e_B", 5 888 hits, 0 failures;
`NP_new` = N′-hits *not* covered by Theorem N = **0**, the honest assessment above.)

`problems/wowii/w61_cstar.py` → `w61_cstar.out`, exhaustive n ≤ 7 plus the n = 8
cover, restricted to the **hard-core frame** (connected, non-forest, diam = 4,
f = α+1; **no reductio** — 〔**Repair G5(i) 已落地**, 2026-08-18 17:5x CDT: this corpus
was mislabelled "hard core", which under Repair F3 additionally requires
`residue = α`〕):

```
[C* +n=8 cover] hard-core graphs=340  (F-b) pairs=399  C* failures=0
[C*] hard-core tau histogram: {2: 14, 3: 200, 4: 118}
[C*] hard-core cases with min_B deg >= tau+1 (Theorem N hyp (i)), per tau:
     {2: 14, 3: 91, 4: 5}
```

### E. The measured obstacle (this is the round's main strategic finding)

The last line above is the point. Theorem N / N′ both stand or fall with
hypothesis **(i) every B-degree ≥ τ+1**, which is what forces `K = B` and hence
`hs = e_B`. Inside the hard core (i) holds in **91 of 200** τ=3 cases but in only
**5 of 118** τ=4 cases, and Lemma C\* shows why: (F-b) plus Lemma 4 only ever
force `deg_A(b) ≥ 3` for the O(1) vertices of `T₁ ∪ T₂`, and `deg_A(b) ≥ 2` for
any b with a non-neighbour in B — bounds that do **not** grow with τ, while (i)
demands τ+1. So the τ=3 proof's shape does not lift: at τ=3 the constant 3 and
the requirement τ+1 = 4 are within reach of one extra step (that is exactly what
C2/C3 do), and from τ ≥ 4 they diverge.

**Consequence for round 4.** The `K = B` regime is a shrinking corner, not the
main case; the τ-uniform argument must handle `K ≠ B`, i.e. B-vertices of degree
≤ τ that are *survivors* while some A-vertices become heads. In that regime
`hs = e_B + Σ_{a ∈ A∩K} deg(a) − Σ_{b ∈ B∖K} deg(b)`, and Lemma DEC degrades as
`hs` grows — so the next lemma to look for is an upper bound on `hs` when K ≠ B,
or a version of Lemma Z that survives β_j ≥ 1 by charging the occupancy to
G[B]-edges.

**Status markers.** Lemmas BO, Z, DEC, Corollary CNT, Theorem N′ and Lemma C\*
are **PROVED** (complete proofs above, modulo Fact 2 and Lemma 1 only) and
numerically verified as recorded in D; they have **not yet been through S3
adversarial review** (round-1 review this round covered Theorem N and Theorem T3
only).

---


### C4. The K-chain: Lemma Z+, Lemma DICH, Theorem K, Corollary K1 (draft §7.5)

## §7.5 owner-w61 round 3, late (2026-08-18, 09:0x CDT): **Theorem K — the K = B corner is a clique, hence empty at diam 4**

Provenance: derived by an owner-w61 helper (Claude `fable`, task = "the K ≠ B
step") on top of §7.4; **the proof chain below was re-derived and checked line by
line by owner-w61**, and the headline claim was re-verified by an *independent*
script (`problems/wowii/w61_thmK_check.py` → `.out`, written by the owner, not by
the helper). The helper's own probe scripts are `w61_r4_probe.py` /
`w61_r4_existsA.py` with archived outputs. 〔**S3 status, 2026-08-18 14:3x CDT:
this whole chain (Lemma Z⁺, Lemma DICH, Theorem K, Corollary K1, and Lemma F3′ of
§7.7) is now **PROVED-S3** — two clean rounds from different model families plus
the D-DIFF confirmation pass; registry and evidence in **§7.11**.〕

Standing conventions of §7.2 B / §7.4. Write `s` for the number of HH steps (no
reductio needed unless stated); "excess at step j" means an entry's current value
exceeds `s − j + 1`.

> **Lemma Z⁺ (block occupancy, sharpened — supersedes Lemma Z).** At the start of
> step j, every later head whose current value exceeds `s − j + 1` lies in the
> block of step j (and is therefore decremented at step j).
>
> *Proof.* Let x be deleted at step i > j, with current value v > s − j + 1, and
> suppose x ∉ block_j. The block is a prefix of the non-head entries in
> non-increasing order, so v ≤ min(block). If some block entry is a survivor then
> min(block) ≤ s − j + 1 by Lemma F3, contradicting v > s − j + 1. Otherwise all
> D_j block entries are later heads; together with x that is D_j + 1 later heads,
> while only s − j heads remain, so D_j ≤ s − j − 1. But every block entry is at
> most the head value D_j, so v ≤ min(block) ≤ D_j ≤ s − j − 1 < s − j + 1 —
> contradiction. ∎ (Draft Lemma Z is the β_j = 0 case; this version needs no
> hypothesis on β_j at all, answering §7.4 E's first question.)

> **Lemma DICH (head dichotomy).** For the head deleted at step i, of original
> degree g:
> (a) *persistence* — if it is excess at step j < i then by Z⁺ it is decremented
> at step j, so it is excess at step j+1 as well;
> (b) if `g ≥ s+1` it is excess at step 1, hence at every step 1…i−1, hence in
> every earlier block: **h_i = i − 1 and D_i = g − (i−1) exactly**;
> (c) if `g ≤ s` then **D_i ≤ s − i + 2, unconditionally**.
>
> *Proof of (c).* If it is never excess before deletion, its value at step i−1 is
> ≤ s − (i−1) + 1 = s − i + 2 and values never increase (for i = 1, D_1 = g ≤ s).
> Otherwise let j₀ ≥ 2 be the first excess step; its value at step j₀ − 1 is
> ≤ s − j₀ + 2, and by (a) it is decremented at each of the i − j₀ steps
> j₀ … i−1, so D_i ≤ (s − j₀ + 2) − (i − j₀) = s − i + 2. ∎

DICH **subsumes Lemma H** (low heads get Lemma H's conclusion with *no*
hypothesis; high heads get an equality), and it is a fresh, tie-safe derivation —
so if S3 review ever broke Lemma H, this line would survive.

> **Theorem K.** Assume residue(G) = α(G) (so s = τ) and that every `b ∈ B` has
> `deg(b) ≥ τ + 1`. Then `K = B` and **e_B = C(τ,2)**, i.e. **B is a clique**.
>
> *Proof.* By Lemma S and the hypothesis every b ∈ B is a head; |K| = s = τ = |B|
> gives K = B, hence hs = e_B (§7.4 A). Every head now has original degree
> ≥ τ + 1 = s + 1, so DICH(b) applies to each: h_i = i − 1. Summing,
> `e_B = hs = Σ_{i=1}^{τ} (i−1) = τ(τ−1)/2 = C(τ,2)`. ∎

> **Corollary K1 (this replaces Theorem N and Theorem N′ in the hard core).** Let
> G be connected with `diam(G) = 4`. If some maximum independent set A has
> `min_{b ∈ B} deg(b) ≥ τ + 1`, then **residue(G) ≤ α(G) − 1**.
>
> *Proof.* Otherwise residue = α and Theorem K makes B a clique, contradicting
> Observation R1 (§7.1: diam = 4 ⟹ B is not a clique). ∎

**Both of Theorem N's auxiliary hypotheses are gone**: (ii) `e_B ≤ τ−2` and
(iii) `min_B deg ≥ 2e_B+3` are deleted; hypothesis (i) alone suffices at diam 4.
Theorem N′ (§7.4 B) is likewise absorbed. Note also that Theorem K explains
*why* those hypotheses looked awkward: (ii) says e_B ≤ τ−2 while Theorem K says
the only consistent value is C(τ,2) — the two are incompatible for τ ≥ 3, which
is exactly why Theorem N could conclude.

**Independent numerical check** (`w61_thmK_check.py`, owner-written, does not
reuse the helper's code): exhaustive n ≤ 7, the exhaustive n = 8 cover, and 6 000
denser random graphs n = 9…12 — **114 914 connected graphs, 1 464 instances with
residue = α and all B-degrees ≥ τ+1, of which 0 had B a non-clique.**

**What this does NOT do (firewall).** §7.4 E measured that hypothesis (i) itself
holds in only 5 of 118 hard-core cases at τ = 4, and Corollary K1 does not weaken
(i). So the residual hard core is still essentially the K ≠ B regime; Theorem K
closes the corner cleanly rather than enlarging the covered region. The helper
additionally reports a counting bound (CNT2), a low-vertex budget inequality
(LOW) and a rigidity statement for the one-low-vertex case, plus a **refutation**
of the hoped-for bound `hs ≤ e_B + O(t)` when K ≠ B; those are recorded in the
round-3 report and are **not yet adopted into this draft** pending owner
line-by-line verification in round 4.

---


### D. The `Fan(tau,L)` set-up, FAN-1/3/4/5, Theorem FAN, and the `GFan(tau,L,nu)` definition (draft §7.8)

## §7.8 owner-w61 round 4 (rebuild, 2026-08-18, written 13:1x CDT): adjudication of the Fan attack and of the S3 round-A2 pair

Three items, all reproduced from scratch by the owner before adoption. New scripts:
`problems/wowii/w61_r4_fanL.py` → `.out`, `w61_r4_fanmech.py` → `.out`,
`w61_r4_a2check.py` → `.out` (none reuses a helper's or a predecessor's code).

### A. The Fan family: verdict, mechanism, and what is actually proved

Qwen tab B (`problems/wowii/w61_KNEB_qwen_B.md`) claims: *no graph of the form
`Fan(τ,L)` with `L ≥ 2` satisfies the reductio*, via a "no-escape" Lemma 1
(`r + 2L ≤ 2`) plus a Lemma 2 on the residual partition. The full derivation
lives only in the Qwen transcript; the harvest carries a summary, so a
line-by-line certification of Lemma 1 was **not possible from the artifact**.
What I did instead: reproduce the conclusion and the mechanism numerically, and
prove the parts I can prove myself.

**Set-up.** In `Fan(τ,L)` put `C := B_lo ∪ {a₀}`, `p := τ − L = |B_hi| ≥ 2`
(`u,v ∈ B_hi` forces `L ≤ τ−2`). Every `c ∈ C` has `deg(c) = τ` exactly
(`τ−1` inside `B` plus `a₀`, resp. `a₀`'s `τ` B-neighbours); every `w ∈ B_hi` has
`deg(w) ≥ τ+1`; every `a ∈ A′ := A∖{a₀}` has `N(a) ⊆ B_hi`, so `deg(a) ≤ p`.
`residue` is a function of the degree multiset alone and `α = 1 + |A′|` is exact
here, so the reductio holds iff `residue(deg) = 1 + |A′|`.

**What these runs do and do not establish** 〔**Repair V3 已落地**, 2026-08-18 17:5x
CDT; this firewall governs **every** numerical block of §7.8, including the `M1–M4`
block below and the `H1–H5` block of §7.8 E〕**.** Every FAN lemma is stated under the
reductio `s = τ`, and Theorem FAN proves no `Fan(τ,L≥2)` graph satisfies it — real
`Fan` runs have `s = τ+1`. The `M`/`H` blocks are therefore **not** instances of the
lemmas; they are **mechanism checks on the same combinatorial machinery off the
reductio**, and they corroborate the *shape* of the argument (which entries occupy
which blocks, that `C` never escapes, that the residue is `1+1`) rather than the
lemmas' conclusions. The lemmas themselves rest on their proofs alone. The only
numerics that test a *statement* here are those of Theorem FAN's conclusion
(`residue ≤ α−1`, confirmed with no exception) and Observation FAN-E.

> **Numerical verdict (`w61_r4_fanL.out`).** Over the parameter box
> `τ ≤ 8`, `R = Σ_{x∈B_hi} d_x ≤ 16`, `|A′| ≤ 12`: **63 239** bipartite-realizable
> `Fan(τ,L≥2)` degree sequences, **0** with `residue = α`. Dropping the
> occurring-type requirement (a strict superset) — **99 619** sequences, **0**
> survivors. Control `L = 1` — **106 811** sequences, **0** survivors (agrees with
> Corollary L1-short). And the failure is *uniform and sharp*: the histogram of
> `α − residue` is `{1: 63 239}` — **every** Fan sequence in the box has
> `residue = α − 1`, i.e. `s = τ + 1`, an overrun by exactly one step.

> **Mechanism check (`w61_r4_fanmech.out`), 64 911 labelled HH runs
> (canonical + 2 randomised adversarial tie-breaks per instance):**
> M1 "the first `p` heads are exactly `B_hi`" — 0 failures;
> M2 "no `C`-vertex escapes a block during the high phase" (tab B's Lemma 1) —
> 0 failures; M3 "the multiset at the start of step `p+1` is exactly
> `[L]^{L+1}, 1, 1`" (tab B's Lemma 2) — 0 failures, `EXACT` in **all** 64 911 runs;
> M4 `s = τ+1` — 0 failures. Counterfactual-availability control: the same
> residue test applied to shapes that break **one** Fan hypothesis gives
> `residue = α` in 36 650 of 46 138 `B`-clique cases (so the test discriminates and
> is not vacuously negative), and 0 for the two other perturbations.

**What I prove myself** (not merely reproduce):

> **Lemma FAN-1 (high phase first).** Under the reductio, the first `p` heads of a
> `Fan(τ,L)` run may be taken to be exactly the `p` vertices of `B_hi`.
>
> *Proof.* Swapping the roles of two entries of **equal current value** (one taken
> as head, the other as a block member) leaves the value-multiset trajectory
> unchanged, hence leaves `s` unchanged; so the reductio is tie-break invariant
> and we may fix the tie-break. Induct on `j ≤ p`: if all heads before `j` are
> high, then `p − (j−1) ≥ 1` high vertices remain, each in every earlier block by
> DICH(b), hence of value `deg − (j−1) ≥ τ − j + 2`, so `D_j ≥ τ − j + 2`. A low
> head at `j` has `D_j ≤ τ − j + 2` by DICH(c); equality is a tie with the
> remaining high vertex, and the fixed tie-break takes the high vertex. ∎

> **Lemma FAN-2 (no escape, partial — under the reductio; proof tie-incomplete at
> `j = L+1`, see §7.14 G3; superseded by FAN-8 and unused)** 〔**Repairs F2 + G3(1)
> 已落地**, 2026-08-18 17:5x CDT〕**.** For `j ≤ min(p, L+1)`, `block_j ⊇ C`.
>
> *Proof.* At step `j` the non-head entries above a `C`-entry are the `p − j`
> remaining high vertices (value `≥ τ−j+2`); every `A′` entry has value
> `≤ p ≤ τ−j+1` for `j ≤ L+1`, so none is strictly above. Hence `C ⊆ block_j` as
> soon as `D_j ≥ (p−j) + (L+1)`, and `D_j = g_j − (j−1) ≥ τ−j+2 = (p−j)+(L+1)+1`. ∎

> **Lemma FAN-3 (the endgame is unconditional).** If at the start of step `p+1`
> the remaining multiset is `[L]^{L+1}, 1, 1` (`L ≥ 2`), the process does **not**
> terminate at step `τ = p+L`; it terminates at step `τ+1`.
>
> *Proof.* Head values are non-increasing in HH (after deleting a head of value `d`
> and decrementing, no entry exceeds `d`). At step `p+1` the max is `L`, the `L`
> other `L`-entries are the top `L` non-head entries, so `block_{p+1}` is exactly
> them and the two `1`s survive untouched: the list becomes `[L−1]^L, 1, 1`.
> Inductively at the start of step `p+j` it is `[L+1−j]^{L+2−j}, 1, 1`, so at the
> start of step `p+L` it is `[1]^2, 1, 1 = [1,1,1,1]`: the head is `1`, `D = 1`,
> one entry is zeroed and `[0,1,1]` remains. Hence `s ≥ τ+1`; one further step
> clears it, so `s = τ+1` exactly. ∎ 〔**Repair G2 已落地**, 2026-08-18 17:5x CDT: the
> clause "*which is precisely the measured `α − residue = 1`*" is **deleted** — off
> the reductio that coincidence is **Observation FAN-E**, not a consequence of
> FAN-3.〕

**Status.** `Fan(τ,L≥2)` is **eliminated from the hard core conditionally on one
step**: 〔**Repair V4 已落地**, 2026-08-18 17:5x CDT〕 Lemma FAN-1 and FAN-3 are
PROVED here; **Lemma FAN-2's proof is tie-incomplete at `j = L+1`** (§7.14 G3) and it
is **superseded by FAN-8 and unused**;
the residual is exactly *"no `C`-vertex escapes `block_j` for `L+1 < j ≤ p`, and
the `A′` residue at step `p+1` is `1,1`"* — i.e. tab B's Lemma 1 in the range
`j > L+1` together with its Lemma 2. 〔**Status amendment, 13:3x CDT: both residuals are now PROVED** — see §7.8 D/E/F
(Lemmas FAN-4, FAN-6, FAN-7, FAN-8 and **Theorem FAN**). §7.8 A/B/C are left
unedited as the audit trail of the adjudication that found the target. Lemma FAN-2
is superseded by Lemma FAN-8 and is no longer used.〕

Both are verified numerically with 0
failures over 64 911 adversarial runs but are **NOT** owner-certified as proofs.
The reduction of the residual: an `A′` vertex that is *excess* at step `j` must
have escaped at least `L+1` of the first `j−1` blocks (its degree is `≤ p = τ−L`
while DICH(a)+Z⁺ force its value at step `j` to be exactly `τ−j+2`) — that is the
named handle for closing it. **This is not yet a milestone; it is a
conditionally-proved elimination with a sharp, uniform numerical signature.**

### B. Repair R3 (§7.3 5bis, k=2 / e_B=2 terminal-shape count) — T-J4 UPHELD

Round A2 (`w61_S3_T3R_qwenA2.md`, PARTIAL) reports one non-load-bearing defect.
Original (§7.3, k=2 / e_B=2):

> "故 D_3 = 1，而终止形状要求恰有 D_3=1 个 1，实有 4 个，矛盾
> （等价地 Σ_{i≤3}D_i = X+(Y−1)+1 = m−1 < m）。"

**UPHELD.** Lemma T's terminal shape at `D_3 = 1` is `[1, 1, 0^…]`: **two** ones in
total, **one** after the head — while `L² = [1,1,1,1,0^…]` has four in total, three
after the head. The sentence pairs the "required" count of one reading with the
"actual" count of the other, so it miscounts under either consistent reading.

*Repair.* Delete the terminal-count clause and keep the sum contradiction:

> 故 `D_3 = 1`。于是 `Σ_{i≤3} D_i = X + (Y−1) + 1 = m − 1 < m`，与 Lemma 1(2)
> （反证假设 `s = τ = 3` 下 `Σ_{i=1}^{3} D_i = m`）矛盾。∎

**Numerical backing** (`w61_r4_a2check.out`, part 2): over all **726** parameter
instances `a₀,b₀,c₀ ∈ 1..11` of that branch — the displayed trajectory
`D = (X, Y−1, 1)` and `L² = [1,1,1,1,0^…]` are correct in **726/726**; the sum
identity `Σ_{i≤3} D_i = m − 1` holds in **726/726**; the terminal-count sentence
miscounts in **726/726** and the contradiction survives its deletion in
**726/726**. So the defect is textual and the branch's conclusion is unaffected.

### C. K-chain round A2 CLEAN — owner verification

`w61_S3_KCHAIN_qwenA2.md` returns **CLEAN**. Per the pre-registered scoring rule
(dispatch file, "Scoring rule for the closure rounds") it qualifies: its control
section performs the counterfactual-availability check and *names lemmas the text
claims are available but which never execute* (Theorem K / Corollary K1
unavailable on control (a); DEC and CNT available but "deliberately weak"; the
reductio-only family absent on (b) and (d)), and it computes seven trajectories,
so probe-4 and probe-5 are both met.

I re-checked the joint that both previous rounds' defects touched, K-J1/K-J2:

* **K-J1** — Lemma Z⁺'s proof with F3′ substituted: `x ∉ block_j` gives
  `v ≤ min(block_j)`; a survivor in the block bounds `min(block_j) ≤ s−j+1` by
  **F3′ (general `s`)**, contradiction; otherwise all `D_j` block entries are later
  heads, and with `x` that is `D_j + 1` of the `s − j` remaining heads, so
  `D_j ≤ s−j−1` and `v ≤ D_j < s−j+1`. Sound; the only scope-sensitive citation is
  now F3′, which is general-`s`. **CORRECT.**
* **K-J2** — DICH(a) is Z⁺ applied stepwise; (b) `g ≥ s+1` is excess at step 1
  hence at every step `< i`, giving `h_i = i−1` and `D_i = g−(i−1)` exactly; (c)
  splits on whether an excess step occurs, and the first excess step is `≥ 2`
  precisely because `g ≤ s`. Both boundaries the judge names (`i = 1`, and first
  excess `j₀ = i`) hold. **CORRECT.**

**Numerical backing** (`w61_r4_a2check.out`, part 1; my own labelled-HH code):
**94 419** labelled runs — exhaustive connected graphs `n ≤ 6` (of whose canonical
runs 17 660 are reductio and 9 815 are **non**-reductio, the regime where the old
F3 citation was out of scope) plus 4 000 random graphs `n = 8…13`, each under the
canonical sort and two randomised adversarial tie-breaks. Failures:
`F3′ = 0`, `Z⁺ = 0`, `DICH(b) = 0`, `DICH(c) = 0`, `DICH(c) at i=1 = 0`,
`DICH(c) at j₀ = i = 0`.

**Gate status (honest).** K-CHAIN now has **one** clean round (A2, verified above);
T3-REPAIRED does **not** — round A2 is PARTIAL, and R3 above is a fresh repair, so
T3 needs a further clean round on the R3 text. Per the planner's standing ruling
**both targets still require the round-B opus judge**; neither gate closes on this
round. The `w61_S3_KCHAIN_qwenA2.md` out-of-scope note (Corollary N2 read at
`τ = 0` on `K₁`) is accepted as a future-proofing note, not a defect: add `τ ≥ 1`
if N2 is ever exported outside the connected-`n ≥ 2` setting.

### D. Addendum to §7.8 A (13:1x CDT): the residual-sum is a counting identity, and the partition `1+1` is load-bearing

Two further results, both obtained after §7.8 A was written; script
`problems/wowii/w61_r4_fanres.py` → `.out`.

> **Lemma FAN-4 (the `A′` residue sums to exactly 2).** In `Fan(τ,L)` under the
> reductio, assume only that no `C`-vertex escapes a block during the high phase
> (steps `1…p`). Then the `A′` entries at the start of step `p+1` sum to
> **exactly 2**.
>
> *Proof.* By Lemma FAN-1 the heads of steps `1…p` are `B_hi`, so
> `Σ_{j≤p} D_j = Σ_{x∈B_hi} deg(x) − Σ_{j=1}^{p}(j−1) = Σ_{B_hi} deg − C(p,2)`
> using DICH(b). Now `Σ_{x∈B_hi} deg_B(x) = 2(τ−2) + (p−2)(τ−1) = pτ − p − 2`
> (`u,v` miss the edge `uv`, the `p−2` vertices of `W` do not) and
> `Σ_{x∈B_hi} deg_A(x) = p + R` where `R := Σ_{x∈B_hi} d_x` counts the
> `A′`-attachments (`a₀` contributes the `p`). So `Σ_{B_hi} deg = pτ − 2 + R`.
> Count the same `Σ_{j≤p} D_j` decrements by recipient: a high head deleted at
> position `i ≤ p` receives `i−1` of them (DICH(b)), total `C(p,2)`; each of the
> `L+1` vertices of `C` receives `p` by hypothesis, total `p(L+1)`; the rest go to
> `A′`. Hence
> `dec_{A′} = (pτ − 2 + R − C(p,2)) − C(p,2) − p(L+1) = p(p−1) − 2 + R − p(p−1)
> = R − 2`, and `A′` starts at total `R`, leaving total `2`. ∎

So the residual `A′` partition is **either `1+1` or a single `2`** — nothing else
is arithmetically possible. This matters more than it looks:

> **Observation FAN-5 (`1+1` vs `2` decides the whole family; now a corollary of
> Lemma TAIL).** 〔**Repair V5 已落地**, 2026-08-18 17:5x CDT〕 For every `L ≥ 2`,
> the multiset `[L]^{L+1}, 1, 1` clears in `L+1` Havel–Hakimi steps and
> `[L]^{L+1}, 2` clears in exactly `L`. **PROVED** — the first half is Lemma FAN-3;
> the second is **Lemma TAIL (§7.13 D) at `λ = [2]`**: `λ₁ = 2` and
> `s₀(λ) = steps([2]^3 ∪ [2]) = 2 = λ₁`, so the total is `(L−2) + 2 = L` for every
> `L ≥ 2`. Independently verified for `L = 2…9` (`w61_r5_bcheck.out`), TAIL's
> prediction matching direct simulation at every `L`; Q14 supplies a second,
> independent proof of the same half. **A `Fan(τ,L)` instance whose `A′` residue is a
> single `2` would therefore be a genuine hard-core survivor.**
>
> **Citation caveat (Repair W2, from Q18's D2).** Lemma TAIL's **general** half is
> itself `PROVED, 0 clean S3 rounds` (§7.12/§7.13 have no S3 row yet). What is
> independently verified at S3 strength here is the **`λ = [2]` instance only**.
> Accordingly **Observation FAN-5 does not carry a PROVED-S3 row** — see §7.11
> row-block R-9…R-13, constraint 1.

This corrects a scope reading of tab B's Lemma 2, which justifies "`1+1`, not a
single `2`" only via the two diameter-witness singleton types and presents it as
an `L`-independent detail: it is in fact the *single* load-bearing point of the
whole Fan elimination at **every** `L ≥ 2`, not a technicality of `L = 2`.

**Numerical status of the residual** (`w61_r4_fanres.out` part B): over
**450 303** superset `Fan(τ,L≥2)` degree sequences (`τ ≤ 9`, `R ≤ 18`,
`|A′| ≤ 14`, *no* occurring-type requirement) the multiset at the start of step
`p+1` is `[L]^{L+1}` together with `A′` residue `(1,1)` in **450 303 of 450 303**
— the `C`-part is exact every time (so the full no-escape statement, Problem D,
also holds throughout the box) and the `(2)` partition **never** occurs.

**Sharpened residual for §7.8 A.** After this addendum the Fan elimination is
missing exactly two things, both narrow:
1. **no escape in the range `L+1 < j ≤ p`** (Lemma FAN-2 covers `j ≤ L+1`); the
   handle is unchanged, and is now sharper: at the first escaping step `j` the
   block count forces **at least two** `A′` entries of value `≥ τ−j+1` at step `j`,
   each of degree `≤ p = τ−L`, hence each having escaped `≥ L` of the first `j−1`
   blocks;
2. **the residual partition is `1+1`, not `2`** — by Lemma FAN-4 the only
   remaining freedom, and by Observation FAN-5 the point on which the entire
   family turns.

Both are in the Q9 Qwen brief (`prompts/w61_FANRES_qwen.md`, Problems D and E).

### E. Second addendum (13:2x CDT): the escape budget, and the Fan residual collapses to ONE case

> **Lemma FAN-6 (the residual partition is `1+1`, never a single `2`).** In
> `Fan(τ,L)` under the reductio, assume no `C`-vertex escapes during the high
> phase. Then the `A′` residue at the start of step `p+1` is `1+1`.
>
> *Proof.* Write `M_j` for the `A′` value multiset at the start of step `j`. Since
> all of `B_hi` (DICH(b)) and all of `C` (hypothesis) lie in `block_j`, the number
> of `A′` entries in `block_j` is `a_j = D_j − (p−j) − (L+1) = g_j − τ ≥ 1`, and —
> the block being a **prefix** of the sorted list — they are the `a_j` largest
> entries of `M_j`. In particular **a maximum entry of `M_j` is always
> decremented.** By Lemma FAN-4 the total of `M_{p+1}` is `2`, so it is `1+1` or a
> single `2`; suppose it is a single `2`. Say `M_{j+1}` has a **unique** maximum
> `v` and does **not** contain the value `v−1`. At step `j` let `M_j` have maximum
> `w` of multiplicity `μ`. If `a_j < μ` the maximum does not drop, `w = v`, and the
> `a_j ≥ 1` decremented copies land at `v−1` — which `M_{j+1}` does not contain, a
> contradiction. So `a_j ≥ μ`: all maxima drop, `w = v+1`, and `M_{j+1}` contains
> `μ` copies of `v`, forcing `μ = 1`. Every other entry of `M_j` is either in the
> block (its `M_{j+1}` value `+1`) or out of it (unchanged), so all of them are
> `≤ max(other entries of M_{j+1}) + 1`. Hence the hypothesis propagates
> **backwards**: `M_{p+1} = [2]` has unique max `2` and no `1`, so `M_p = [3,1^b]`
> (unique max `3`, others `≤ 1`), `M_{p−1}` has unique max `4` and others `≤ 2`,
> and inductively `M_{p−t}` has maximum `3+t` with all other entries `≤ t+1` — in
> particular `v−1` is never present, so the induction never stops. At `t = p−1`
> this gives `max(M_1) = p+2`. But `M_1` is the multiset of `A′` **degrees**, and
> every `a ∈ A′` has `N(a) ⊆ B_hi`, so `max(M_1) ≤ p`. Contradiction. ∎
>
> *(The induction does not apply to `1+1`: its maximum is **not unique** — value 1
> with multiplicity 2 — and the induction's first step needs a unique maximum. FAN-6
> has to kill only the single-`2` case, which is why this is not a gap.)*
> 〔**Repair F4 已落地**, 2026-08-18 17:5x CDT; the old reason ("`v−1 = 0` is present
> as the zero entries") is false whenever `|A′| = 2`, which is realizable at every
> `L ≥ 2` (`Fan(4,2)`, `Fan(5,3)`, `Fan(6,4)` with `A′ = [2,2]`).〕

> **Lemma FAN-7 (escape budget).** In `Fan(τ,L)` under the reductio, let `E` be the
> total number of (vertex, step) escapes of `C`-vertices during the high phase.
> Then `E ≤ 2`; and `E = 2` is impossible. Hence `E ≤ 1`.
>
> *Proof.* Repeat the count of Lemma FAN-4 with `dec_C = p(L+1) − E`: it gives
> `dec_{A′} = R − 2 + E`, so the `A′` residue is `2 − E ≥ 0`, whence `E ≤ 2`. If
> `E = 2` the `A′` residue is `0` and the `C`-part at the start of step `p+1` is
> `[L+2, L^L]` or `[L+1, L+1, L^{L−1}]` — in both the head exceeds the number of
> **positive** remaining entries (`L+2 > L` resp. `L+1 > L`), so the next step
> would drive a zero entry negative, which is impossible for the degree sequence
> of a graph. ∎

**Complete case list of the Fan residual** (verified by direct simulation for
`L = 2…9`; `E` = escape budget, "clears in" = number of further HH steps, and the
reductio needs exactly `L`):

| `E` | `A′` residue | list at start of step `p+1` | clears in | status |
|---|---|---|---|---|
| 0 | `1,1` | `[L]^{L+1}, 1, 1` | `L+1` | **killed** (Lemma FAN-3) |
| 0 | `2` | `[L]^{L+1}, 2` | `L` | **killed** (Lemma FAN-6) |
| 1 | `1` | `[L+1], [L]^L, 1` | `L` | **OPEN — the whole residual** |
| 2 | — | `[L+2],[L]^L` / `[L+1]^2,[L]^{L−1}` | — | **killed** (Lemma FAN-7, non-graphical) |

So `Fan(τ,L≥2)` is eliminated **except for the single case `E = 1`**: exactly one
`C`-vertex escapes exactly one high-phase block, and exactly one `A′` entry
survives the high phase, at value `1`. Everything else in the family is now
closed by owner-proved lemmas FAN-1…FAN-7.

**What `E = 1` forces** (partial, for the follow-up brief): if `c ∈ C` escapes
`block_t`, then `block_t` contains `(p−t)` high vertices, the other `L`
`C`-vertices and `a_t = g_t − τ + 1 ≥ 2` `A′` entries, and — the block being a
prefix above `c` — **each of those `≥ 2` `A′` entries has value `≥ τ − t + 1` at
step `t`**. Since every `A′` degree is `≤ p = τ − L`, this forces `t ≥ L + 1` and
makes each of them escape at least `L` of the first `t−1` blocks, while Lemma
FAN-6's prefix property says a maximum `A′` entry is decremented at **every**
step. That tension is the handle.

**Numerical status** (`problems/wowii/w61_r4_fanE.py` → `.out`): over **508 239**
high-phase runs (superset box `τ ≤ 9`, `R ≤ 16`, `|A′| ≤ 12`, three tie-breaks
each) all five structural hypotheses of Lemma FAN-6 hold with **0** failures —
`H1` (high in block), `H2` (`C` in block, i.e. `E = 0`), `H3` (`a_j = g_j − τ ≥ 1`),
`H4` (block ∩ `A′` is a prefix and the maximum is always decremented), `H5`
(`A′` total `≥ 2` throughout) — and the outcome is `C`-part `[L]^{L+1}` with `A′`
residue `(1,1)` in **508 239 of 508 239**. So `E = 1` is never realized in the
box, but it is not yet excluded by proof.

*Status 〔**Repairs G3/V4/V5 已落地**, 2026-08-18 17:5x CDT〕: Lemmas FAN-1, FAN-3,
FAN-4, FAN-6, FAN-7 are **PROVED** (modulo Lemma 1, Lemma S, Lemma DICH, Lemma F3′,
all of which are PROVED-S3). **Lemma FAN-2 is struck from this list** — its proof is
tie-incomplete at `j = L+1`, and FAN-8 supersedes it. **Observation FAN-5 is PROVED**
but its second half now rests on Lemma TAIL, whose general form is S3-pending (W2), so
it stays out of the S3 registry. The elimination of `Fan(τ,L≥2)` from the hard core
was, at the time this line was written, conditional on the `E = 1` case alone; §7.8 F
closes it, and **§7.8's chain is PROVED-S3 as of §7.11 rows R-9/R-10**.*

**Enlarged box** (`problems/wowii/w61_r4_fanL_big.out`, `τ ≤ 10`, `R ≤ 20`,
`|A′| ≤ 14`): **1 098 141** strict and **1 700 094** superset `Fan(τ,L≥2)` degree
sequences, `α − residue = 1` for **every single one**, `0` survivors, and the
minimum of `α − residue` is `1` at every `L = 2…8`. Combined with the case list
above this says the residual `E = 1` case is not merely rare in the box — it never
occurs there at all.

### F. **Theorem FAN — the whole `Fan(τ,L≥2)` family is eliminated** (13:3x CDT)

The `E = 1` case of the table in §7.8 E is now closed, and it closes the whole
family. The argument is three lines and does not need Lemma FAN-2 at all.

> **Lemma FAN-8 (no escape, unconditional).** In `Fan(τ,L)` with `L ≥ 2`, under the
> reductio, no `C`-vertex escapes a block during the high phase: `E = 0`.
>
> *Proof.* Suppose `E ≥ 1` and let `t ≤ p` be a step at which `e_t ≥ 1` vertices of
> `C` escape; let `c` be one of them. By Lemma FAN-1 the head of step `t` is a
> `B_hi` vertex, so `D_t = g_t − (t−1) ≥ τ − t + 2`, and by DICH(b) the `p − t`
> remaining `B_hi` vertices all lie in `block_t`; so does each of the
> `(L+1) − e_t` non-escaping `C`-vertices. Hence
> `|block_t ∩ A′| = D_t − (p−t) − (L+1) + e_t ≥ (τ−t+2) − (p−t) − (L+1) + 1 = 2`,
> so `block_t` contains some `x ∈ A′`. Because `block_t` is a **prefix** of the
> sorted list and `c ∉ block_t`, `v_t(x) ≥ v_t(c) ≥ τ − t + 1` (`c` has been
> decremented at most `t−1` times). Now by Lemma FAN-7's count the `A′` entries sum
> to `2 − E ≤ 1` at the start of step `p+1`, so `v_{p+1}(x) ≤ 1`; and `x` is **not
> deleted** in steps `t…p` (all those heads are `B_hi`, Lemma FAN-1), so it loses at
> most one per step and `v_{p+1}(x) ≥ v_t(x) − (p−t+1)`. Therefore
> `τ − t + 1 ≤ v_t(x) ≤ 1 + (p − t + 1)`, i.e. `τ ≤ p + 1 = τ − L + 1`, i.e.
> `L ≤ 1` — contradicting `L ≥ 2`. ∎

> **Theorem FAN** 〔**Repair F1 已落地**, 2026-08-18 17:5x CDT〕**.** For every `τ` and
> every `L ≥ 2` there is **no** graph with the `Fan(τ,L)` configuration satisfying
> `residue(G) = α(G)`. Consequently, by Fact 2, every `Fan(τ,L≥2)` graph has
> **`residue ≤ α − 1`**.
>
> *Proof.* Assume `residue = α`, i.e. `s = τ`. By Lemma FAN-1 the heads of steps
> `1…p` are exactly `B_hi`. By Lemma FAN-8, `E = 0`, so by Lemma FAN-4 the `A′`
> entries sum to exactly `2` at the start of step `p+1`, and by Lemma FAN-6 they are
> `1 + 1`; the `C`-entries are then all at `τ − p = L`. So the list at the start of
> step `p+1` is `[L]^{L+1}, 1, 1` (plus zeros), and Lemma FAN-3 gives `s = τ + 1`, a
> contradiction. ∎ 〔The old closing sentence "*The last sentence is Lemma FAN-3's
> second half*" is **deleted** by F1: `residue ≠ α` plus Fact 2 yields only
> `residue ≤ α−1`, and FAN-3's `s = τ+1` is derived *under* the refuted reductio, so
> it may not be carried out of it.〕

> **Observation FAN-E (numerical, NOT proved)** 〔landed with F1〕**.** Measured over
> 1 098 141 strict and 1 700 094 superset `Fan(τ,L≥2)` degree sequences
> (`w61_r4_fanL_big.out`), `residue = α − 1` and `s = τ + 1` in **every** instance.
> This is a **lead**: no proof is available, because at `s = τ+1` the reductio-only
> toolkit (Lemma S, DICH(b)) is unavailable — witness `Fan(4,2)` with `A′ = [2,1,1]`,
> `deg = [5,5,4,4,4,2,1,1]`, where every `B_hi` degree is `τ+1 = 5 = s`.

> **Corollary FAN-HC (the hard core has `L ≥ 3`).** In the hard core (connected,
> non-forest, `diam = 4`, `f = α+1`, `residue = α`) the number of `B`-vertices of
> degree `≤ τ` satisfies `L ≥ 3`; together with Theorem T3 the residual hard core
> is **`τ ≥ 4` and `L ≥ 3`**.
>
> *Proof.* `L = 0` is Theorem K + Observation R1; `L = 1` is Corollary L1-short.
> `L = 2`: by **Proposition L2** every hard-core instance with `L = 2` is rigidly
> the configuration `Fan(τ,2)` — Proposition L2(a)–(d) supplies every clause of the
> `Fan` definition, the "all other `A`-vertices attach inside `B_hi`" clause coming
> from `deg_A(b_i) = 1` — and Theorem FAN says no such graph has `residue = α`.
> `τ ≥ 4` is Theorem T3 and is not improved here. ∎
>
> 〔Note the asymmetry, deliberately: Theorem FAN kills the *whole* `Fan(τ,L)`
> family for every `L ≥ 2`, but it only removes the hard core's `L = 2` layer,
> because rigidity (Proposition L2) is available at `L = 2` only. For `L ≥ 3` a
> hard-core instance need not be a fan, and no analogue of Proposition L2 is known —
> that is the next structural target.〕

**Chain of dependence.** Theorem FAN rests on Lemma 1, Lemma S, Lemma DICH and
Lemma F3′ (all in S3 this round) plus Lemmas FAN-1/3/4/6/7 proved above; Corollary
FAN-HC additionally rests on Theorem K, Corollary L1-short, Theorem SL and
Proposition L2 (§7.6), which carry the same S3 dependency. **No step of Theorem FAN
uses a Qwen-supplied argument**: tab B's Lemma 1 (which could not be certified from
its harvest) is superseded by Lemma FAN-8, whose proof is different and shorter,
and tab B's Lemma 2 is superseded by Lemmas FAN-4 + FAN-6.

**Numerical agreement** 〔**Repair G1 已落地**, 2026-08-18 17:5x CDT〕**.** Theorem FAN
predicts `residue ≤ α − 1` for every `Fan(τ,L≥2)` degree sequence, and that is
confirmed with no exception. **Observation FAN-E** (numerical, not proved) predicts the
sharper `residue = α − 1` with `s = τ + 1`, and that is what is measured: **1 098 141 /
1 098 141** strict and **1 700 094 / 1 700 094** superset sequences
(`w61_r4_fanL_big.out`), and `E = 0` with residue partition `(1,1)` in **508 239 /
508 239** labelled high-phase runs under adversarial tie-breaks (`w61_r4_fanE.out`).
**The off-by-one is FAN-E's, not the theorem's.**

*Status 〔updated 17:5x CDT〕: **Theorem FAN — PROVED-S3** (§7.11 row R-10), resting on
Lemma 1 / Lemma S / Lemma DICH / Lemma F3′ (R-1…R-5, PROVED-S3) and Lemmas
FAN-1/3/4/6/7/8 (R-9). **Corollary FAN-HC — PROVED, 0 clean S3 rounds, and it does NOT
move**: it additionally rests on §7.6's Theorem K / Theorem SL / Theorem MB /
Corollary L1-short / Proposition L2, and the §7.6 chain has no clean S3 round (§7.11
row-block constraint 2).*

### G. LEAD (not a theorem): how far Theorem FAN generalizes — `GFan(τ,L,ν)`

Recorded as a **lead** for the `L ≥ 3` push; the counts below are owner-derived but
the configuration lemmas that would make them apply are not.

Drop "`G[B] = K_τ` minus one edge" and keep everything else (`B_lo` all
B-universal with `deg_A = 1` sharing one B-universal `a₀`, all `ν` non-edges of `B`
inside `B_hi`, all of `B_hi` high). Call this `GFan(τ,L,ν)`; `Fan(τ,L)` is `ν = 1`.
Then `Σ_{x∈B_hi} deg_B(x) = p(τ−1) − 2ν`, and re-running Lemma FAN-4 gives

> `dec_{A′} = R − 2ν + E`, so the `A′` entries total **`2ν − E`** at step `p+1`,

and re-running Lemma FAN-8 gives `τ − t + 1 ≤ (2ν−E) + (p−t+1)`, i.e.

> **`L ≤ 2ν − E`**; in particular `E = 0` whenever `L ≥ 2ν`.

Lemma FAN-6's backward induction needs only the block-prefix property, so it
generalizes verbatim and kills **any single-part `A′` residue** `[w]` with `w ≥ 2`
(it forces `max(A′ degrees) = w + p > p`). Enumerating the remaining shapes (`C`-part
= `L+1` entries at `L` carrying `E` escape units, `A′` residue any partition of
`2ν−E`) and asking which clear in exactly `L` steps:

* `ν = 1`: only `[2]` — single-part, dead. **That is Theorem FAN.**
* `ν = 2`: only `[4]` (`E=0`) and `[3]` (`E=1`) — both single-part, **dead for
  every `L ≥ 3`** (and `ν = 2` needs `L ≥ 3` by Corollary MB1's `ν ≤ L−1`).
* `ν = 3`: dead for `L ≥ 5`; at **`L = 4`** the shape `E = 2` (one `C`-vertex
  escaping twice) with `A′` residue `[3,1]` survives the step count — the first
  genuine obstruction. So the generalization is **not** uniform in `ν`.

**Why this matters for `L ≥ 3`.** Corollary MB1 gives `ν = m̄ ≤ L−1` when every low
vertex is B-universal, and when `ν = L−1` Theorem SL's (LOW3) form forces
`Σ_{B_lo} deg_A = L`, hence `deg_A(b) = 1` for all `b ∈ B_lo`, hence (Lemma 4 on the
`B_lo` clique) a shared `a₀` — i.e. **`ν = L−1` is rigidly `GFan(τ,L,L−1)`**. Combined
with the list above, that layer is dead for `L = 2` and `L = 3` and open from
`L = 4` on. Anything below `ν = L−1` is not yet pinned to a configuration at all —
that is exactly the missing rigidity theorem.

*Status: **LEAD, not proved.** The two displayed counts follow from the §7.8
arguments with `ν` in place of `1`, but no configuration lemma here has been
written out or S3'd, and the `ν = L−1` rigidity sketch above leans on Theorem SL and
Corollary MB1 in a way that needs checking. Do not cite as a result.*

---


### F. §7.6 imports — Theorem LOW / SL / MB / MB1 / L2 (PARALLEL ROUND; imports only)

## §7.6 owner-w61 round 4 (2026-08-18, written 09:3x CDT): **Theorem LOW — a τ-uniform bound that survives K ≠ B**, and the reduction of the hard core to L ≥ 2

Standing conventions of §7.2 B / §7.4 / §7.5. Throughout §7.6 we work under the
reductio hypothesis **residue(G) = α(G)**, i.e. `s = τ`. New notation:

* `B_hi := {b ∈ B : deg(b) ≥ τ+1}`, `p := |B_hi|`; `B_lo := B ∖ B_hi`, **`L := |B_lo| = τ − p`**;
* `ν := C(τ,2) − e_B` = the number of **non-adjacent pairs inside B** (so
  Observation R1 reads `ν ≥ 1` at diam 4);
* `ν(S)` = non-adjacent pairs inside `S ⊆ B`; `m̄ := ν(B_hi)`;
* `I_hi`, `I_lo` = the sets of head *positions* of original degree `≥ τ+1`,
  resp. `≤ τ`.

**Provenance and verification status.** The round-3 helper reported two
statements (`CNT2`, `LOW`) that §7.5 recorded as *not adopted, pending owner
line-by-line verification in round 4*. This round I re-derived the bound from
Lemma DICH **before** opening the helper's probe script; the result coincides
with the helper's `LOW` and `CNT2` exactly. That is the verification §7.5 was
waiting for, so they are adopted here, in the owner's own derivation, as
**Theorem LOW**. Numerics are the owner's own script
`problems/wowii/w61_r4_low.py` → `w61_r4_low.out` (independent labelled-HH
implementation and independent corpus driver — it does **not** reuse
`w61_r4_probe.py`).

### A. The bound

> **Lemma HI (`I_hi = B_hi`).** `B_hi` is exactly the set of heads of original
> degree ≥ τ+1; in particular `|I_hi| = p` and `|I_lo| = L`.
>
> *Proof.* Every `a ∈ A` has `N(a) ⊆ B`, so `deg(a) ≤ |B| = τ`; hence every
> vertex of degree ≥ τ+1 lies in B. By Lemma S every such vertex is a head. ∎

> **Theorem LOW (τ-uniform; no hypothesis on K).** Under `residue(G) = α(G)`,
>
> **(LOW1)**  `Σ_{b ∈ B_lo} deg(b) + ν ≤ L·(τ+1).`
>
> Equivalently, splitting B-degrees into their A- and B-parts,
>
> **(LOW2)**  `Σ_{b ∈ B_lo} deg_A(b) + e(B_lo) + m̄ ≤ L(L+3)/2`, and
> **(LOW3)**  `Σ_{b ∈ B_lo} deg_A(b) + m̄ ≤ 2L + ν(B_lo)`.
>
> *Proof.* `Σ_{i=1}^{τ} D_i = m` (Lemma 1(2)). Split the head positions by
> Lemma HI. For `i ∈ I_hi` Lemma DICH(b) gives `D_i = g_i − (i−1)` **exactly**;
> for `i ∈ I_lo` Lemma DICH(c) gives `D_i ≤ τ − i + 2`. Hence
>
> `m ≤ Σ_{b∈B_hi} deg(b) − Σ_{i∈I_hi}(i−1) + Σ_{i∈I_lo}(τ − i + 2)`.
>
> On the other hand every edge has an endpoint in B (A is independent), edges
> inside B being counted twice, so `m = Σ_{b∈B} deg(b) − e_B`. Subtracting,
>
> `Σ_{b∈B_lo} deg(b) − e_B ≤ − Σ_{i∈I_hi}(i−1) + Σ_{i∈I_lo}(τ − i + 2)`.
>
> The right-hand side is **independent of which positions the low heads occupy**:
> adding and subtracting `Σ_{i∈I_lo}(i−1)`,
>
> `− Σ_{i∈I_hi}(i−1) + Σ_{i∈I_lo}(τ−i+2) = − Σ_{i=1}^{τ}(i−1) + Σ_{i∈I_lo}[(i−1) + (τ−i+2)]
>  = − C(τ,2) + L(τ+1)`,
>
> because the bracket collapses to the constant `τ+1`. With `e_B = C(τ,2) − ν`
> this is (LOW1). For (LOW2) write `Σ_{B_lo} deg(b) = Σ_{B_lo} deg_A(b) + 2e(B_lo)
> + e(B_lo,B_hi)` and `ν = ν(B_lo) + ν(B_lo,B_hi) + m̄` with
> `ν(B_lo) = C(L,2) − e(B_lo)` and `ν(B_lo,B_hi) = Lp − e(B_lo,B_hi)`; the
> crossing terms cancel and `L(τ+1) − C(L,2) − Lp = L(L+3)/2`. (LOW3) is (LOW2)
> with `e(B_lo) = C(L,2) − ν(B_lo)`. ∎

**Theorem K is the case `L = 0`.** Then (LOW1) reads `ν ≤ 0`, i.e. `e_B = C(τ,2)`:
B is a clique. So Theorem LOW **subsumes Theorem K** (and hence Theorem N,
Theorem N′ and Corollary N1, which §7.5 already showed are absorbed by K), and it
is the first statement in this line that says something when `K ≠ B` — indeed it
never mentions K at all: the high/low split is by **degree**, not by head status,
and Lemma HI makes the two agree only on `B_hi`.

### B. What it gives in the hard core at `L = 1`

Hard-core standing assumptions (G connected, non-forest, diam 4, `f = α+1`):
Lemma 4, Observation R1 (`ν ≥ 1`), (F-b) (occurring types `T₁,T₂ ⊆ B`, disjoint,
no G[B]-edge between them) and Lemma C\* (`deg_A(b) ≥ 3` for `b ∈ T₁ ∪ T₂`).

> **Proposition L1.** In the hard core with `L = 1`, write `B_lo = {b₀}`. Then
> `b₀` is adjacent to **every** other vertex of B, and moreover
> `deg_A(b₀) = 1`, `deg(b₀) = τ`, `ν = m̄ = 1`; the unique non-adjacent pair of B
> is a pair `u,v ∈ B_hi`, `T₁ = {u}`, `T₂ = {v}`, `deg_A(u), deg_A(v) ≥ 3`, and
> the unique A-neighbour `a₀` of `b₀` is adjacent to **all** of B.
>
> *Proof.* `L = 1` gives `ν(B_lo) = 0`, so (LOW3) reads `deg_A(b₀) + m̄ ≤ 2`.
> *(i)* If `b₀ ∈ T₁ ∪ T₂` then Lemma C\* gives `deg_A(b₀) ≥ 3 > 2` — impossible.
> So `b₀ ∉ T₁ ∪ T₂`, i.e. `T₁, T₂ ⊆ B_hi`.
> *(ii)* If `b₀` had a non-neighbour in B, Lemma 4 would give `deg_A(b₀) ≥ 2`,
> hence `m̄ = 0`, i.e. `B_hi` is a clique; but `T₁, T₂` are disjoint non-empty
> subsets of `B_hi`, so some `u ∈ T₁`, `v ∈ T₂` are adjacent, contradicting (F-b).
> So `b₀` is adjacent to all of `B∖{b₀}`, whence every non-adjacent pair of B lies
> inside `B_hi`: `ν = m̄`. By R1 `ν ≥ 1`, so `deg_A(b₀) + m̄ ≤ 2` forces
> `deg_A(b₀) = 1` and `ν = m̄ = 1`. Then `deg(b₀) = (τ−1) + 1 = τ`. Since the only
> non-adjacent pair of B is that single pair `uv ⊆ B_hi`, and all cross pairs of
> `T₁ × T₂` must be non-adjacent, `|T₁| = |T₂| = 1` and `{T₁,T₂} = {{u},{v}}`;
> Lemma C\* gives `deg_A(u), deg_A(v) ≥ 3`. Finally, for each `w ∈ B∖{b₀}` the
> pair `(b₀,w)` is adjacent, so Lemma 4 gives a common A-neighbour, which must be
> the unique A-neighbour `a₀` of `b₀`; hence `a₀` is adjacent to every
> `w ∈ B∖{b₀}` and to `b₀`. ∎

> **Corollary L1′.** In the hard core with `L = 1`, the slack of (LOW1) is
> **exactly 0**: `Σ_{b∈B_lo} deg(b) + ν = τ + 1 = L(τ+1)`.
>
> *Proof.* Immediate from Proposition L1: `deg(b₀) = τ` and `ν = 1`. ∎

This is the payoff of the round: the whole `L = 1` regime has been compressed
into the single **slack-0** configuration described by Proposition L1 — and
slack-0 is measurably a `L = 0` phenomenon (see C). Explicitly:

> **Conditional Theorem.** If `slack := L(τ+1) − (Σ_{b∈B_lo} deg(b) + ν) ≥ 1`
> holds whenever `L ≥ 1` (under the reductio hypothesis), then the hard core has
> `L ≥ 2`; combined with Theorem K (`L = 0` impossible at diam 4) the residual
> hard core becomes `L ≥ 2`, `τ ≥ 4`.

What is proved of the antecedent so far:

> **Lemma SL1.** If `p = 0` (equivalently `Δ ≤ τ`, equivalently `L = τ`) then
> `slack ≥ τ + 1 − Δ ≥ 1`.
> *Proof.* Position 1 is then a low head and `D_1 = Δ` (Lemma 1(2)), so its
> contribution `τ − 1 + 2 − D_1 = τ+1−Δ ≥ 1`. ∎

`Lemma SL1` does **not** cover `L = 1` (there `p = τ−1 ≥ 1`, so position 1 is a
high head); the `L = 1` case of the antecedent is open. **This is the single
highest-value open step of the line right now**: `slack = Σ_{i∈I_lo}(τ−i+2−D_i)`,
so it asks exactly whether every low head can simultaneously attain the DICH(c)
bound with equality.

### C. Numerical backing (run before the statements were written)

`problems/wowii/w61_r4_low.py` → `w61_r4_low.out`. Corpus: the exhaustive
connected-graph atlas `n ≤ 7` (995 graphs), 6 000 random graphs `n = 8…12` at
five densities, and Family I(τ,c) for τ = 3…7, c = 2…8 — **6 403 connected
graphs, 34 040 reductio trajectory checks** (every graph is run under the
canonical sort **and** three randomised adversarial tie-breaks, and every
maximum independent set A is tested, not just one):

```
[A n<=7 exhaustive atlas] graphs=995  reductio traj-checks=8776   fails={}
[+B random n=8..12]       graphs=6368 reductio traj-checks=34040  fails={}
[+C Family I(tau,c)]      graphs=6403 reductio traj-checks=34040  fails={}
     (checked: LOW1, LOW2, LOW3, POS = the position-independence identity,
      DICHb, DICHc, KHI = Lemma HI, KSUB = Theorem K as the L=0 case)
[SLACK] min slack of LOW1 per L: {0:0, 1:1, 2:1, 3:2, 4:2, 5:3, 6:4, 7:5,
                                  8:6, 9:7, 10:8}
[HARDCORE] (connected, non-forest, diam 4, f=alpha+1, reductio NOT imposed)
           L histogram aggregated over tau: {0:20, 1:7, 2:2, 3:3, 4:1, 5:1}
```

Two readings.

* **(LOW1) is tight exactly at `L = 0`.** All 324 `L = 0` instances have slack 0
  (forced — that is Theorem K); **no instance with `L ≥ 1` has slack 0** in the
  whole corpus. So the antecedent of the Conditional Theorem is measurably true,
  and by Corollary L1′ the residual `L = 1` configuration of Proposition L1 is
  never realised numerically. (`L ≥ 6` is thinly sampled — it only occurs at
  large τ — so the apparent growth `slack ≳ ⌈L/2⌉` is a **lead, not a claim**.)
* The hard-core `L` histogram says `L ≤ 1` carries most of the mass, which is why
  Proposition L1 is worth more than a general-`L` partial result.

*Firewall.* The `[HARDCORE]` histogram is computed **without** imposing
residue = α (under the conjecture the hard core with the reductio is empty), so
it describes the regime a completed proof must cover; it is **not** evidence for
or against any statement of §7.6 A/B, all of which assume the reductio.

### D. Status markers and the banned route

* **PROVED** (complete proofs above, modulo Lemma 1, Lemma S, Lemma DICH):
  Lemma HI, **Theorem LOW** (LOW1/LOW2/LOW3), Proposition L1, Corollary L1′,
  Lemma SL1. Numerically verified as recorded in C. **Not yet through S3** —
  Theorem LOW rests on Lemma DICH, which is itself in S3 this round (K-CHAIN
  brief, joint K-J2), so §7.6 inherits that dependency.
* **Adopted from round 3** (owner-verified this round by independent
  re-derivation): the helper's `LOW` and `CNT2` — they are Theorem LOW (LOW2) and
  (LOW1) respectively. The helper's one-low-vertex rigidity statement is
  superseded by Proposition L1, which is proved here from Theorem LOW alone.
* **Banned route confirmed.** The hoped-for `hs ≤ e_B + O(t)` for `K ≠ B` stays
  refuted; `w61_r4_probe.out`'s `[HS]` table shows `hs − e_B` reaching ±τ-scale
  values at every τ ≥ 4 and `hs − e_B − t` unbounded in the sample. Theorem LOW
  sidesteps this by never bounding `hs` at all: it uses DICH(b)/(c) positionwise
  and lets the position sum collapse.
* **Open, in priority order.** (1) `slack ≥ 1` when `L ≥ 1` — closes `L = 1` by
  Corollary L1′. (2) `L = 2`. (3) a lower bound on `deg_A(b)` growing with the
  number of B-non-neighbours of `b` (Lemma 4 alone gives only 2, since the
  codegree-2 witnesses may coincide) — this is what an `L`-uniform argument needs.

### E. The open step, sharpened to a pure Havel–Hakimi statement

At `L = 1` the inequality of Theorem LOW can be traced back to a single head, and
the trace is an **identity**, not an estimate. Write `i₀` for the position of the
unique low head.

> **Lemma ID (`L = 1`).** Under the reductio hypothesis with `L = 1`,
> `deg(b₀) + ν = (i₀ − 1) + D_{i₀}`, hence
> `slack = τ − i₀ + 2 − D_{i₀}`.
>
> *Proof.* `m = Σ_{b∈B_hi} deg(b) + deg(b₀) − e_B`. On the other side, Lemma HI
> and DICH(b) give `m = Σ_{i∈I_hi}(g_i − (i−1)) + D_{i₀}
> = Σ_{b∈B_hi} deg(b) − [C(τ,2) − (i₀−1)] + D_{i₀}`, since `I_hi = {1,…,τ}∖{i₀}`
> and `Σ_{i=1}^{τ}(i−1) = C(τ,2)`. Equating and using `e_B = C(τ,2) − ν` gives the
> identity; the slack form is `L(τ+1) − (deg(b₀)+ν)` with `L = 1`. ∎

So the decisive open step of §7.6 B is **equivalent** to a purely
Havel–Hakimi statement, one unit stronger than Lemma DICH(c) and only for the
low head:

> **Conjecture SL1.** Under the reductio hypothesis, if exactly one `b ∈ B` has
> `deg(b) ≤ τ`, then the unique low head satisfies `D_{i₀} ≤ τ − i₀ + 1`.
>
> Equivalent graph-theoretic form: `deg_A(b₀) + m̄ ≤ 1`, i.e. **`deg_A(b₀) = 1`
> and `B_hi` is a clique** (the two are equivalent by Lemma ID; `deg_A(b₀) ≥ 1`
> always, since A is a *maximum* independent set).

**Why this matters.** Proposition L1 forces `m̄ = 1` in the hard core at `L = 1`.
So Conjecture SL1 ⟹ the hard core has no `L = 1` case; with Theorem K it would
leave `L ≥ 2, τ ≥ 4`.

**Numerical backing for Conjecture SL1** (`problems/wowii/w61_r4_slack.py` →
`w61_r4_slack.out`; corpus deliberately enriched with *near-split* graphs —
B a clique minus a few random edges — because that is exactly the regime
Proposition L1 lives in):

```
[atlas n<=7]              graphs=554  checks=2194  SL_fail=0 SL1_fail=0 L1=110
[+random n=8..14 dense]   graphs=3022 checks=20325 SL_fail=0 SL1_fail=0 L1=232
[+near-split]             graphs=5913 checks=26514 SL_fail=0 SL1_fail=0 L1=1240
[minslack per L] {0:0, 1:1, 2:1, 3:2, 4:2, 5:3, 6:3, 7:4, 8:5, 9:6, 10:7, 11:9, 12:12}
[L=1 profile (deg_A(b0), mbar)] {(1, 0): 1240}
```

The last line is the striking one: across **all 1 240** reductio instances with
`L = 1`, the pair `(deg_A(b₀), m̄)` is `(1,0)` — never anything else. `SL_fail`
counts violations of the weaker `L ≥ 1 ⟹ slack ≥ 1` over all 26 514 checks: also
0. (Five trajectories per graph — canonical sort plus four randomised adversarial
tie-breaks — and every maximum independent set is tested.)

*Status: `Conjecture SL1` is a **CONJECTURE**, numerically supported, not proved.
Lemma ID and Proposition L1 are PROVED. The Conditional Theorem of §7.6 B is
proved as a conditional only.*

### F. **Theorem SL — the open step of E is now proved** (2026-08-18, 11:0x CDT)

〔Status amendment to §7.6 E: `Conjecture SL1` is **no longer a conjecture**. It
is the `L = 1` case of Theorem SL below, which is proved for every `L ≥ 1`. §7.6 E
is left unedited as the audit trail of how the target was found.〕

> **Theorem SL (slack positivity).** Assume the reductio hypothesis
> `residue(G) = α(G)` (so `s = τ`) and `τ ≥ 2`. If `L ≥ 1` then
>
> `slack := L(τ+1) − ( Σ_{b∈B_lo} deg(b) + ν ) ≥ 1`,
>
> i.e. **`Σ_{b∈B_lo} deg(b) + ν ≤ L(τ+1) − 1`**, one unit stronger than
> Theorem LOW (LOW1). Equivalently `Σ_{b∈B_lo} deg_A(b) + e(B_lo) + m̄ ≤ L(L+3)/2 − 1`.
>
> *Proof.* Recall from the proof of Theorem LOW that
> `slack = Σ_{i∈I_lo} (τ − i + 2 − D_i)`, each summand being `≥ 0` by Lemma
> DICH(c). Suppose `slack = 0`; then
>
> **(∗) every low head satisfies `D_i = τ − i + 2` exactly.**
>
> Let `i₀ := max I_lo` and let `x` be the head deleted at step `i₀`, of original
> degree `g = deg(x) ≤ τ`. Write `v_k` for `x`'s value at the start of step `k`,
> and `block_k` for the set of entries decremented at step `k`.
>
> *Step 1 (`i₀ ≥ 2`).* If `i₀ = 1` then `I_lo = {1}`, so every head at a position
> `2,…,τ` is high, of original degree `≥ τ+1`; but `D_1 = Δ = g ≤ τ` (Lemma 1(2)),
> contradicting that `Δ` is the maximum degree. (If `L = τ` there are no high
> heads and `i₀ = τ ≥ 2` directly.)
>
> *Step 2 (an escape step exists, and it sits exactly at the Lemma F3 threshold).*
> Let `E := {k < i₀ : x ∉ block_k}`. Since `v_{i₀} = g − (i₀ − 1 − |E|)` and
> `v_{i₀} = D_{i₀} = τ − i₀ + 2` by (∗), we get `|E| = τ + 1 − g ≥ 1`. Put
> `j := max E`. From step `j+1` to step `i₀−1` the entry `x` is decremented every
> time, so `v_{i₀} = v_j − (i₀ − 1 − j)`, whence **`v_j = τ − j + 1`**.
>
> *Step 3 (what `block_j` can contain).* `block_j` is the prefix of the `D_j`
> largest non-head entries in the non-increasing order, and `x` is a non-head
> entry of step `j` lying **outside** it; hence every entry of `block_j` has value
> `≥ v_j = τ − j + 1`. By Lemma F3 every survivor has value `≤ τ − j + 1` at the
> start of step `j`. Therefore each survivor in `block_j` has value **exactly**
> `τ − j + 1`, and so — needing `τ − j + 1` further decrements in the `τ − j + 1`
> remaining steps — **lies in `block_k` for every `k ∈ [j, τ]`**. Write `s_j` for
> the number of survivors in `block_j`.
>
> *Step 4 (the head part of `block_j`).* Every entry of `block_j` is either a
> survivor or a head deleted later. Let `ℓ_j := #{i ∈ I_lo : i > j}` and note
> `x` is one of these and `x ∉ block_j`, so the low later heads contribute
> `λ_j ≤ ℓ_j − 1`. Every **high** later head lies in every earlier block by Lemma
> DICH(b), and there are `(τ − j) − ℓ_j` of them. Hence
> `D_j = |block_j| = (τ − j − ℓ_j) + λ_j + s_j`.
>
> *Step 5 (`s_j ≤ 2`).* All heads after position `i₀` are high (`i₀ = max I_lo`),
> so by DICH(b) all `τ − i₀` of them lie in `block_{i₀}`; by Step 3 the `s_j`
> survivors lie in `block_{i₀}` too, and these sets are disjoint. Hence
> `D_{i₀} ≥ s_j + (τ − i₀)`, and `D_{i₀} = τ − i₀ + 2` gives **`s_j ≤ 2`**.
>
> *Step 6 (contradiction).* Steps 4 and 5 give
> `D_j ≤ (τ − j − ℓ_j) + (ℓ_j − 1) + 2 = τ − j + 1`.
> But position `j < i₀` is a head position, and either it is **high**, so
> `D_j = g_j − (j−1) ≥ (τ+1) − (j−1) = τ − j + 2` by DICH(b), or it is **low**, so
> `D_j = τ − j + 2` by (∗). Either way `D_j ≥ τ − j + 2 > τ − j + 1 ≥ D_j`. ∎

**Note on sharpness.** The theorem is *not* the statement "the last low head
satisfies `D_{i₀} ≤ τ − i₀ + 1`" — that stronger claim is **false** (1 925
counterexamples in the corpus below, recorded as `sharp_fail`). What Step 6
extracts is that the escape step `j` must itself be a **low** head position
carrying strict inequality; so equality can never hold at *all* low heads
simultaneously, which is exactly `slack ≥ 1` and no more.

> **Corollary SL-HC (the hard core has `L ≥ 2`).** Let G be in the hard core
> (connected, non-forest, `diam = 4`, `f = α+1`, `residue = α`). Then at least two
> vertices of B have degree `≤ τ`.
>
> *Proof.* `L = 0` is impossible: Theorem K would make B a clique, contradicting
> Observation R1. `L = 1` is impossible: Proposition L1 forces `deg(b₀) = τ` and
> `ν = 1`, so by Corollary L1′ the slack is exactly `0`, contradicting Theorem SL
> (note `τ ≥ 4` in the hard core) 〔**Repair G5(ii) 已落地**, 2026-08-18 17:5x CDT:
> the parenthetical read "`τ ≥ 3` … so `τ ≥ 2` holds", stale under Repair F3's
> `τ ≥ 4`〕. ∎

Together with Theorem T3 (τ ≤ 3 fully solved) the **residual hard core is now
`τ ≥ 4` and `L ≥ 2`**, i.e. at least two B-vertices are survivors-or-low —
`K ≠ B` is no longer merely the main case, it is the *only* case, and it now
carries a quantitative floor.

**Numerical backing** (`problems/wowii/w61_r4_thmSL.py` → `w61_r4_thmSL.out`).
Every intermediate assertion of the proof is checked separately, not just the
conclusion; corpus = exhaustive atlas `n ≤ 7`, 9 000 random graphs `n = 8…13` at
mixed densities, 4 000 near-split graphs, five trajectories each (canonical sort
plus four randomised adversarial tie-breaks):

```
[atlas n<=7]          traj=2740   L>=1=2435   eqhead=145   sharp_fail=130
[+random+near-split]  traj=19710  L>=1=14275  eqhead=2300  sharp_fail=1925
[s_j histogram at equality heads] {2: 2300}
   all of P1a,P1c,P2,P3a,P3b,P4,P5,P6a,P6b,P6c,F3,SL_fail = 0
```

Reading: `SL_fail = 0` over 14 275 instances with `L ≥ 1` (the conclusion);
`P4 = 0` (DICH(b): high heads in every earlier block); `F3 = 0`; `P1c = 0`
(Step 2's `v_j = τ−j+1`); `P2 = 0` (Step 3's prefix domination); `P3a/P3b = 0`
(Step 3's survivors at threshold, in every later block); `P5 = 0` (Step 5);
`P6a/P6b = 0` (Step 4's block decomposition); `P6c = 0` (Step 6's `D_j ≤ τ−j+1`).
The `s_j` histogram is `{2: 2300}` — `s_j` is **always exactly 2** at an
equality head, i.e. Step 5's bound `s_j ≤ 2` is attained every time it is used.

**Status.** Theorem SL, Corollary SL-HC: **PROVED** (complete proofs above,
modulo Lemma 1, Lemma F3, Lemma DICH), numerically verified step by step as
recorded. **Not yet through S3** — like Theorem LOW they rest on Lemma DICH,
which is in S3 this round (K-CHAIN brief, joint K-J2). **Next open step: `L = 2`.**

### G. The master budget inequality, a one-line `L = 1`, and the exact `L = 2` residual

Combining Theorem SL with the hard-core structure gives a single inequality that
drives every case. Notation, all inside the hard core (G connected, non-forest,
`diam = 4`, `f = α+1`, `residue = α`), with `T₁,T₂` the occurring types of (F-b):

* `B_lo⁺ := {b ∈ B_lo : b has a non-neighbour in B}` (so `B_lo ∖ B_lo⁺` are the
  low vertices adjacent to **all** of `B∖{b}` — call them *B-universal*);
* `c := |B_lo ∩ (T₁ ∪ T₂)|`; `m̄ = ν(B_hi)` as before.

> **Theorem MB (master budget).** In the hard core, for `L ≥ 1`,
> **`|B_lo⁺| + c + m̄ ≤ L + ν(B_lo) − 1`.**
>
> *Proof.* Lemma 4 gives `deg_A(b) ≥ 2` for every `b ∈ B_lo⁺` and `deg_A(b) ≥ 1`
> for every `b ∈ B_lo` (the latter because A is a **maximum** independent set, so
> no `b ∈ B` has all its neighbours in B). Lemma C\* gives `deg_A(b) ≥ 3` for
> `b ∈ T₁ ∪ T₂`, and every such `b` lies in `B_lo⁺` (it has the whole of the other
> type as non-neighbours). Hence
> `Σ_{b∈B_lo} deg_A(b) ≥ (L − |B_lo⁺|)·1 + (|B_lo⁺| − c)·2 + c·3 = L + |B_lo⁺| + c`.
> Substituting into the (LOW3) form of Theorem SL,
> `Σ_{b∈B_lo} deg_A(b) + m̄ ≤ 2L + ν(B_lo) − 1`, gives the claim. ∎

> **Corollary L1-short (a one-line replacement for the §7.6 B route).** The hard
> core has no `L = 1` case.
>
> *Proof.* `L = 1` gives `ν(B_lo) = 0`, so Theorem MB reads
> `|B_lo⁺| + c + m̄ ≤ 0`: the unique `b₀` is B-universal, `c = 0` and `m̄ = 0`.
> B-universality of `b₀` means no non-edge of B meets `b₀`, so `ν = m̄ = 0` and B
> is a **clique** — contradicting Observation R1. ∎

〔This supersedes the longer route of §7.6 B/F (Proposition L1 + Corollary L1′ +
Theorem SL applied at slack 0), which is left in place as the audit trail. Both
are correct; this one is shorter and does not need Proposition L1.〕

> **Corollary MB1 (a floor on L).** In the hard core, if every low vertex is
> B-universal then `ν = m̄ ≤ L − 1`, so `L ≥ ν + 1 ≥ 2`.
>
> *Proof.* B-universality of all of `B_lo` gives `ν(B_lo) = ν(B_lo,B_hi) = 0`,
> hence `ν = m̄`, and `c = 0` (a B-universal vertex has no non-neighbour, so it
> cannot lie in `T₁ ∪ T₂`). Theorem MB then reads `m̄ ≤ L − 1`; and `ν ≥ 1` by R1. ∎

> **Proposition L2 (the `L = 2` case is rigid).** Suppose the hard core has an
> instance with `L = 2`, `B_lo = {b₁,b₂}`. Then **all** of the following hold:
> (a) `b₁ ∼ b₂`; (b) both are B-universal; (c) `deg_A(b₁) = deg_A(b₂) = 1` and
> their unique A-neighbours coincide in a single vertex `a₀` which is adjacent to
> **all** of B; (d) `ν = m̄ = 1`, i.e. `G[B] = K_τ` minus exactly one edge `uv`
> with `u,v ∈ B_hi`, and `T₁ = {u}`, `T₂ = {v}`, `deg_A(u), deg_A(v) ≥ 3`;
> (e) the slack of (LOW1) is exactly 1, so Theorem SL is **tight** here.
>
> *Proof.* Theorem MB reads `|B_lo⁺| + c + m̄ ≤ 1 + ν(B_lo)`.
> *(a)* If `b₁ ≁ b₂` then `ν(B_lo) = 1` and both lie in `B_lo⁺`, so
> `2 + c + m̄ ≤ 2`, giving `c = m̄ = 0`. Then `B_hi` is a clique and
> `T₁,T₂ ⊆ B_hi` (as `c = 0`) are disjoint and non-empty, so some `u ∈ T₁` is
> adjacent to some `v ∈ T₂` — contradicting (F-b). Hence `b₁ ∼ b₂` and
> `ν(B_lo) = 0`, so `|B_lo⁺| + c + m̄ ≤ 1`.
> *(b)* If some `b_i ∈ B_lo⁺` then `c = m̄ = 0` and the same (F-b) contradiction
> recurs. Hence `B_lo⁺ = ∅` and `c = 0`, leaving `m̄ ≤ 1`.
> *(d)* Both `b_i` being B-universal, every non-edge of B lies inside `B_hi`, so
> `ν = m̄ ≤ 1`; R1 gives `ν ≥ 1`, so `ν = m̄ = 1`. The unique non-adjacent pair of
> B is that single pair `uv ⊆ B_hi`; since all cross pairs of `T₁ × T₂` are
> non-adjacent, `T₁ = {u}` and `T₂ = {v}`, and Lemma C\* gives
> `deg_A(u), deg_A(v) ≥ 3`.
> *(c)* Theorem MB is now tight, and re-running its degree count with
> `|B_lo⁺| = c = 0`, `m̄ = 1` forces `Σ_{b∈B_lo} deg_A(b) = 2`, i.e.
> `deg_A(b₁) = deg_A(b₂) = 1`. Since `b₁ ∼ b₂`, Lemma 4 supplies a common
> A-neighbour, which must be the unique A-neighbour of each; call it `a₀`. For
> every `w ∈ B∖{b₁}` the pair `(b₁,w)` is adjacent, so Lemma 4 gives a common
> A-neighbour, necessarily `a₀`; hence `a₀` is adjacent to all of B.
> *(e)* `deg(b_i) = (τ−1) + 1 = τ`, so
> `slack = 2(τ+1) − (2τ + ν) = 2τ + 2 − 2τ − 1 = 1`. ∎

**Where this leaves the line.** `L = 0` and `L = 1` are closed; `L = 2` is closed
*except* for the single rigid configuration of Proposition L2, on which Theorem SL
is tight (slack 1) and therefore cannot help. Note the configuration is the exact
`L = 2` analogue of the one Theorem SL killed at `L = 1`: `L` B-universal low
vertices of A-degree 1 sharing one universal A-neighbour `a₀`, over `B = K_τ − uv`.
Call this the **fan configuration** `Fan(τ, L)`; its slack is `L − 1`, so a general
`slack ≥ L` would kill the whole family at once. That, or a structural argument
against `Fan(τ,2)`, is the next step.

*Status:* Theorem MB, Corollary L1-short, Corollary MB1, Proposition L2 —
**PROVED** (from Theorem SL, Lemma 4, Lemma C\*, Observation R1). Not yet
numerically re-verified independently of §7.6 C/F, and not yet through S3.



### G. **THE TEXT UNDER REVIEW — draft §7.12 in full**

## §7.12 owner-w61 round 5: **Theorem RIG — the B-universal layer is rigidly `GFan`, at every `L`** (2026-08-18, 14:4x CDT)
## §7.12 owner-w61 round 5: **Theorem RIG — the B-universal layer is rigidly `GFan`, at every `L`** (2026-08-18, 14:4x CDT)

This is the decisive step of the `L ≥ 3` rigidity target (planner-approved next
structural target, 13:3x). It is short, it needs no tightness argument, and it
subsumes and simplifies Proposition L2. Script (owner's own, written this round,
reusing no earlier `w61_*` code): `problems/wowii/w61_r5_rig.py` → `.out`.

Notation as in §7.6: `B_hi = {b ∈ B : deg(b) ≥ τ+1}`, `B_lo = B ∖ B_hi`,
`L = |B_lo|`, `ν = C(τ,2) − e_B`, `m̄ = ν(B_hi)`; a vertex `b ∈ B` is
**B-universal** if it is adjacent to all of `B ∖ {b}`, and `B_lo⁺` is the set of
low vertices that are *not* B-universal. Scope terms are Repair F3's:
**hard-core frame** = connected, non-forest, `diam = 4`, `f = α+1` (no reductio);
**hard core** = frame + `residue = α` (+ `τ ≥ 4`).

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
> Consequently `G` carries **exactly** the configuration `GFan(τ, L, ν)` of §7.8 G,
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
> clauses of §7.8 G are exactly (a)+(b)+(c) ("`B_lo` all B-universal with
> `deg_A = 1` sharing one B-universal `a₀`"), (d) ("all `ν` non-edges of `B` inside
> `B_hi`") and (e) (the `A′`-attachment clause), plus "`B_hi` is high", which is
> the definition of `B_hi`. The final bound `ν ≤ L−1` is **Corollary MB1** applied
> to this hypothesis (all low vertices B-universal), and that corollary rests on
> Theorem MB → Theorem SL, which live in the hard core. ∎

**Scope, stated exactly (this is the D1/D3 species discipline).** (a)–(c) and (e)
need only: `A` a maximum independent set, plus **Lemma 4**, i.e. `f = α+1`; (d)
needs additionally `diam = 4` (Observation R1). So **(a)–(e) hold in the
hard-core frame, with no reductio**. Only the bound `ν ≤ L−1` needs the hard core
— and that is not a formality: see the measured witness in §7.12 D.

### C. What it closes

> **Corollary RIG-1 (Proposition L2 without its tightness argument).** In the hard
> core with `L = 2`, Proposition L2 (a),(b) force `B_lo⁺ = ∅`; Theorem RIG then
> gives L2 (c) and (d) directly, and `ν ≤ L−1 = 1` with `ν ≥ 1` gives `ν = m̄ = 1`,
> i.e. `Fan(τ,2)`.
>
> This **removes the tightness re-run** from Proposition L2(c) ("Theorem MB is now
> tight, and re-running its degree count … forces `Σ deg_A = 2`"). That step was
> the pre-declared failure mode **L-d** of the §7.6 error prior (dispatch file,
> 12:27 entry: "tightness arguments need the inequality chain to be tight at
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
kill `GFan(τ,L,2)`. §7.8 G's LEAD already computes what that needs — with `ν` in
place of `1`, Lemma FAN-4 becomes "`A′` total `= 2ν − E`" and Lemma FAN-8 becomes
"`L ≤ 2ν − E`", so at `ν = 2` and `L ≥ 3` only `E ∈ {0,1}` survives, with `A′`
residue `4` resp. `3`; the LEAD asserts that among the partitions of those totals
only the single-part ones `[4]`, `[3]` clear in exactly `L` steps, and Lemma FAN-6's
backward induction kills every single-part residue `[w]`, `w ≥ 2`. **That is a
LEAD, not a proof** — the two generalized identities and the step-count enumeration
have not been written out. Writing them out is the next decisive step.

### D. The other layer (`B_lo⁺ ≠ ∅`) is NOT excluded at `L ≥ 3`

At `L = 2`, Proposition L2 (a),(b) forced `B_lo⁺ = ∅` via Theorem MB plus (F-b).
**That argument does not survive `L = 3`**, and I record the reason so no successor
re-derives it as a theorem. With `k := |B_lo⁺| = 1` and `ν(B_lo) = 0`, Theorem MB
reads `1 + c + m̄ ≤ L + 0 − 1 = 2`, which is satisfiable in two ways:

* `c = 0`, `m̄ = 1`: then `T₁, T₂ ⊆ B_hi` are singletons `{u},{v}` spanning the
  unique `B_hi` non-edge — no (F-b) contradiction arises, because `m̄ = 1 ≠ 0`.
  Theorem MB is tight, so `Σ_{B_lo} deg_A = L + k + c = 4`, i.e. the one
  non-universal low vertex has `deg_A = 2` and the other two have `deg_A = 1`.
* `c = 1`, `m̄ = 0`: the non-universal low vertex is itself in `T₁`, and `T₂` sits
  inside its `B_hi` non-neighbourhood; Lemma C\* gives `deg_A ≥ 3` there, so
  Lemma CAP forces `n_b ≥ 2` for that vertex.

Both are budget-consistent. The (F-b) contradiction that closed `L = 2` used
`m̄ = 0` **and** `c = 0` simultaneously, and at `L ≥ 3` the budget no longer forces
both. So the residual hard core splits as

> **`L ≥ 3` = [B-universal layer: `GFan(τ,L,ν)`, `2 ≤ ν ≤ L−1`] ∪ [`B_lo⁺ ≠ ∅`].**

Lemma CAP is the new handle on the second layer: `deg_A(b) ≤ n_b + 1` converts
every A-degree lower bound into a **non-edge** lower bound. Concretely, Lemma C\*
(`deg_A ≥ 3` on `T₁ ∪ T₂`) now reads: **every low vertex in `T₁ ∪ T₂` has at least
two non-neighbours in `B`**, and Lemma 4 (`deg_A ≥ 2` on `B_lo⁺`) is exactly
"`n_b ≥ 1`", which is its definition — i.e. Lemma 4's contribution to Theorem MB is
recovered by Lemma CAP for free, and Lemma C\*'s is strictly strengthened.

### E. Numerical backing (run before the statements above were written)

`problems/wowii/w61_r5_rig.py` → `w61_r5_rig.out`. Own labelled implementation of
`residueAux`, own graph code, own corpora; no earlier `w61_*` script is imported or
read.

* **Lemma CAP / Corollary CAP1**: over exhaustive connected graphs `n ≤ 7` (atlas,
  995 graphs, **2 931** `(graph, maximum-independent-set)` pairs), 1 200 random
  connected `n = 8…10` (4 382 pairs), 400 random connected `n = 11…12` (1 737
  pairs) and 600 targeted frame instances (622 pairs) — **1 926 B-universal low
  vertices tested, `deg_A = 1` in every one, 0 failures.**
* **Theorem RIG (a)–(e)**: uniform random graphs almost never land in the frame
  (12 frame instances across the 2 195 exhaustive + random graphs above), so a
  targeted generator was written
  — build `B` with a chosen non-edge set, attach `A`-vertices with random non-empty
  types, keep only instances that pass connected + `diam = 4` + non-forest +
  `f = α+1` + "`A` is a **maximum** independent set". That yields **622 hard-core
  frame instances**, of which **31** satisfy the hypothesis `B_lo⁺ = ∅`.
  **All five conclusions (i)–(vi) hold in 31/31; 0 failures**, and 0 failures on
  the 2 atlas instances as well.
* **The scope demarcation is measured, not assumed.** On the hypothesis set the
  `(L, ν)` histogram is `{(1,1): 22, (1,3): 2, (2,1): 3, (3,1): 4}`. The two
  `(L, ν) = (1, 3)` instances are frame instances with **`ν = 3 > L − 1 = 0`** —
  i.e. the bound `ν ≤ L−1` is **false in the frame** and genuinely needs the
  reductio, exactly as the proof says (it enters only through Corollary MB1 →
  Theorem MB → Theorem SL). None of the 622 frame instances satisfies
  `residue = α`, which is consistent with the whole project: the hard core is
  empty on everything reachable at this size.

*Status: **Lemma CAP, Corollary CAP1, Theorem RIG, Corollaries RIG-1 and RIG-2 —
PROVED** (from Lemma 4, Observation R1, and — for the `ν ≤ L−1` clause only —
Corollary MB1, hence Theorem SL, hence Lemma DICH, which is now **PROVED-S3**,
§7.11). Not yet through S3: this section is round 5's new text and has had no
adversarial round. Theorem FAN's own S3 round A2 is in flight.*

---


### H. **THE TEXT UNDER REVIEW — draft §7.13 in full (D included; Lemma TAIL proof refereed in the parallel round)**

## §7.13 owner-w61 round 5: **Theorem GFAN2 — the `GFan(τ,L,2)` layer is eliminated, and the hard core has no B-universal instance below `L = 4`** (2026-08-18, 15:0x CDT)

This closes the target named in §7.12 C. Scripts (owner's own, this round):
`problems/wowii/w61_r5_gfan2.py` → `.out`, and the explicit shape table
`w61_r5_gfan2_L3.out`. Setting: `GFan(τ,L,ν)` as in §7.8 G, i.e. `B_lo` (size `L`)
all B-universal with `deg_A = 1` sharing a `B`-universal `a₀`, all `ν` non-edges of
`B` inside `B_hi`, `A′ := A∖{a₀}` attaching only inside `B_hi`; `C := B_lo ∪ {a₀}`,
`p := τ − L = |B_hi|`. Throughout, the reductio `residue = α` (`s = τ`).

**Set-up carries over verbatim from §7.8.** Every `c ∈ C` has `deg(c) = τ` exactly
(`b ∈ B_lo`: `(τ−1) + 1`; `a₀`: adjacent to all of `B` and nothing else), every
`w ∈ B_hi` has `deg(w) ≥ τ+1`, and every `a ∈ A′` has `deg(a) ≤ p < τ`. Hence
**Lemma FAN-1 applies word for word** (its proof uses only "the `B_hi` vertices are
the vertices of degree `≥ τ+1`" and DICH(c) for the rest): the heads of steps
`1 … p` are exactly `B_hi`.

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
> uses. Lemma FAN-6 is the case `w = 2`, second entry `0`. Repair F4 already
> corrected the parenthetical that misdiagnosed why `1+1` escapes: the reason is
> that its maximum is not unique. The residues this kills are exactly those with a
> **gap of at least 2 below a unique top**: `[w]` for every `w ≥ 1`, `[3,1]`,
> `[4,1]`, `[4,2]`, … ; it does **not** apply to `[1,1]`, `[2,1]`, `[2,2]`,
> `[2,1,1]`, `[1,1,1,1]`.〕

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
> `w61_r5_gfan2_L3.out`:
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
> 〔**Superseded by Corollary GFANν-HC of §7.13 D**, which raises this to `ν ≥ 7`,
> `L ≥ 8`. Kept because its proof is the hand-written one.〕
>
> *Proof.* Theorem RIG (§7.12) makes the instance `GFan(τ,L,ν)` with
> `1 ≤ ν ≤ L−1`; `ν = 1` is `Fan(τ,L)`, killed for `L ≥ 2` by **Theorem FAN**, and
> `ν = 2` is killed for `L ≥ 3` by **Theorem GFAN2**. `L = 1` is Corollary L1-short
> and `L = 2` forces `ν = 1`. So `ν ≥ 3`, whence `L ≥ ν + 1 ≥ 4`. ∎

> **Corollary GFAN2-L3.** In the hard core with `L = 3`, **some low vertex is not
> B-universal** (`B_lo⁺ ≠ ∅`). Equivalently: the entire `L = 3` layer of the hard
> core lives in the residual regime mapped in §7.12 D.

### C. Numerical backing (run before the statements were written)

`problems/wowii/w61_r5_gfan2.py` → `.out`; own step-count code, no reuse.
Over `L = 3…11` and every admissible `(E, C\text{-part}, A′\text{-partition})` shape:

* `ν = 1` **control**: the only shape clearing in exactly `L` steps is
  `([L]^{L+1}, [2])` at every `L = 2…9` — reproducing Theorem FAN's own case table
  (the `E = 1` rows are excluded by FAN-8′ at `ν = 1`, and `[1,1]` clears in `L+1`).
* `ν = 2` (**this theorem**): 96 shapes tested; the shapes clearing in exactly `L`
  are precisely `([L]^{L+1}, [4])` for every `L = 3…11` and `([4,3,3,3], [3])` at
  `L = 3` — **all single-part, hence all killed by FAN-6′**, and the explicit check
  "any multi-part survivor?" returns **NONE**.
* `ν = 3` (**LEAD check — and §7.8 G's LEAD is corrected here**): 298 shapes tested
  over `L = 3…11`, 20 clear in exactly `L` steps. §7.8 G called the row
  `L = 4`, `E = 2`, `C = [6,4,4,4,4]`, `A′ = [3,1]` "the first genuine obstruction"
  — **it is not one**: `[3,1]` has a unique maximum two above the rest, so
  **Lemma FAN-6′ kills it**. Classifying all 20 survivors by FAN-6′: **every
  survivor with `L ≥ 4` is killed** (residues `[5]`, `[4]`, `[3,1]`, `[6]`), and the
  only survivors FAN-6′ misses are at `L = 3` with `E = 3` and residues `[2,1]` /
  `[1,1,1]` — **which cannot occur anyway**, since `ν = 3` needs `ν ≤ L−1`, i.e.
  `L ≥ 4`. So `ν = 3` is dead for `4 ≤ L ≤ 11` by this scan — **and §7.13 D now
  proves it for every `L`**, together with `ν = 4, 5, 6`.

*Status: **Lemma FAN-4′, Lemma FAN-8′, Lemma FAN-6′, Theorem GFAN2, Corollaries
GFAN2-HC and GFAN2-L3 — PROVED** (modulo Lemma 1 / Lemma S / Lemma DICH / Lemma
F3′, which are **PROVED-S3** as of §7.11, plus Theorem FAN for the `ν = 1` input of
GFAN2-HC and Theorem RIG of §7.12). **Not yet through S3**: §7.12 and §7.13 are
round 5's new text and have had no adversarial round; they are queued for the next
S3 dispatch. §7.8 G's LEAD is now partly superseded — its `ν = 2` line is a
theorem, and its `ν = 3` diagnosis is corrected above.*

### D. **Lemma TAIL, and the elimination of `GFan(τ,L,ν)` for every `ν ≤ 6`** (15:0x CDT)

Step 2 of Theorem GFAN2 used a trajectory that is uniform in `L`. That is not an
accident of `ν = 2`; it is a general reduction, and it turns the whole family into a
**finite** check for each `ν`.

> **Lemma TAIL.** Let `E = 0`, so the multiset at the start of step `p+1` is
> `[L]^{L+1} ∪ λ` with `λ` the `A′` residue, `λ₁ := max λ`. If `L ≥ λ₁` then the
> number of further Havel–Hakimi steps is
> **`(L − λ₁) + s₀(λ)`, where `s₀(λ) := steps([λ₁]^{λ₁+1} ∪ λ)`**.
> Consequently "clears in exactly `L` steps" is equivalent to **`s₀(λ) = λ₁`**, a
> condition on `λ` **alone** — it does not depend on `L`.
>
> *Proof.* Suppose at some stage the list is `[t]^{t+1} ∪ λ` with `t > λ₁` (true at
> `t = L`). The head is `t`; the remaining entries of value `t` are exactly the
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
> is killed by **Lemma FAN-6′**. The enumeration is
> `problems/wowii/w61_r5_gfan2.py` functions `tail_check` / `escape_check` /
> `complete_check`, output `w61_r5_gfan2_complete.out`:
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
> is finite *because* of FAN-4′/FAN-8′/MB1/TAIL, which are hand-proved above, and
> the enumeration inside that finite list is machine-checked and reproducible from
> the archived script. `ν = 1` is Theorem FAN and `ν = 2` is Theorem GFAN2, both of
> which have complete hand proofs; `ν = 3…6` rest on the enumeration.〕

> **Corollary GFANν-HC.** In the hard core, if every low vertex is B-universal then
> **`ν ≥ 7` and `L ≥ 8`**.
>
> *Proof.* Theorem RIG gives `GFan(τ,L,ν)` with `ν ≤ L−1`, i.e. `L ≥ ν+1`; Theorem
> GFANν eliminates every `ν ≤ 6`. ∎

**Cross-check of Lemma TAIL** (`w61_r5_gfan2_complete.out`, first line): the
predicted count `(L − λ₁) + s₀(λ)` was compared with direct simulation on
**1 817** `(λ, L)` pairs (`ν ≤ 6`, `λ₁ ≤ L ≤ 15`) — **0 mismatches**.

**The obvious conjecture, stated as a conjecture.** The table's pattern is uniform:
at `E = 0` only `λ = [2ν]` survives, and every `E ≥ 1` survivor has a unique
maximum with a gap of `≥ 2` below it. If that holds for all `ν`, then **the entire
B-universal layer of the hard core is empty at every `L`** — which with §7.12 D
would reduce the whole hard core to the `B_lo⁺ ≠ ∅` regime. Two precise sub-claims:
(C1) for every `ν` and every partition `λ` of `2ν` other than `[2ν]`,
`s₀(λ) ≠ λ₁`; (C2) every `(L,E)` survivor with `E ≥ 1` has `λ` with a unique
maximum whose second-largest entry is `≤ λ₁ − 2`. **Neither is proved.**

*Status: **Lemma TAIL, Theorem GFANν (`ν ≤ 6`), Corollary GFANν-HC — PROVED**
(GFANν computer-assisted as declared). (C1)/(C2) — **CONJECTURE**. Not through S3.*



### T. **UNDER REVIEW — the three-tier scope assignment (draft §7.10, Repair F3 as amended)**

### Repair F3 — "the hard core" is expanded three inequivalent ways. **UPHELD.**

§7.4 C says "(G connected, `f = α+1`, diam = 4)"; §7.6 B says "(G connected,
non-forest, diam 4, `f = α+1`)"; §7.6 G / Cor SL-HC / Cor FAN-HC say "(connected,
non-forest, `diam = 4`, `f = α+1`, `residue = α`)"; §7.1 adds `τ ≥ 3`. *Repair —
one canonical pair of terms, to be used from here on:*

> **hard-core frame** := `G` connected, non-forest, `diam(G) = 4`, `f = α+1`
> (no reductio). **hard core** := the hard-core frame **plus** `residue = α`
> (**plus** `τ ≥ 4` after Theorem T3).

〔**Repair V2 已落地**, 2026-08-18 17:5x CDT — the original two-tier assignment
("Lemma 4, Lemma C\*, Observation R1 and (F-b) hold in the **frame**; Theorem LOW,
Theorem SL, Theorem MB, Proposition L1/L2, Corollaries SL-HC and FAN-HC live in the
**hard core**") over-hypothesised Theorem LOW and Theorem SL, whose proofs use the
reductio alone. Witness: `C₅` has `deg = [2,2,2,2,2]`, `α = 2`, `τ = 3`,
`residue = 2`, so the reductio holds while `diam = 2` and `f = 4 ≠ α+1 = 3` — outside
the frame entirely. **Three tiers, not two:**〕

> **reductio only** (`residue = α`, no structural hypothesis): Lemma S/S′, Lemma T/T′,
> Lemma F3′, Lemma DICH, Lemma Z⁺, **Theorem LOW**, **Theorem SL**.
> **hard-core frame**: Lemma 4, Lemma C\*, Observation R1, (F-b).
> **hard core** (frame + reductio + `τ ≥ 4`): Theorem MB, Proposition L1/L2,
> Corollaries SL-HC, L1-short, FAN-HC, and the FAN lemmas that are *about a `Fan`
> configuration* (FAN-1, FAN-2, FAN-4, FAN-6, FAN-7, FAN-8, Theorem FAN).

〔**Repair W1 已落地** (from Q18's D1), same step: the blanket "**every** FAN lemma
stays in the hard core" **over-assigns**. **Lemma FAN-3** is a hypothesis-free
statement about a value multiset (`[L]^{L+1},1,1` clears in `L+1` steps) — witness
`[2,2,2,1,1]`, which is not a `Fan` configuration and on which FAN-3 still holds — and
**Observation FAN-5**'s content is likewise multiset-level. Both are carved out of the
hard-core tier and sit in the **no-hypothesis** tier; FAN-3 remains valid in the hard
core either way, so no user is affected.〕

With that reading every statement in §7.6/§7.8 is correctly scoped.
