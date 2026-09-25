# Recon: ETP finite implication "Equation 677 → Equation 255"

Date of recon: 2026-08-16. Target: the Equational Theories Project (ETP,
github.com/teorth/equational_theories) open problem "does E677 imply E255 for
finite magmas?"

## 1. Exact definitions (verified against Lean source, not just prose)

Source of truth: `equational_theories/Equations/Eqns1_999.lean` (single
binary operation `◇`), confirmed line-for-line:

```
equation 255 := x = ((x ◇ x) ◇ x) ◇ x          (line 260)
equation 677 := x = y ◇ (x ◇ ((y ◇ x) ◇ y))    (line 682)
equation 47  := x = x ◇ (x ◇ (x ◇ x))          (line 52, in same file)
```

`equation 2910` is in `Eqns2000_2999.lean` (line 916):

```
equation 2910 := x = ((y ◇ (x ◇ y)) ◇ x) ◇ y
```

Using `L_y x := y◇x`, `R_y x := x◇y`, `S x := x◇x`, the blueprint rewrites:
- **677**: `x = L_y L_x L_{L_y x} y`, i.e. `x = L_y (x ◇ R_y L_y x)`.
- **255**: `x = (Sx ◇ x) ◇ x`.

**Duality check (I derived this manually and it matches the paper's own
labeling):** define the "mirror" of a term by swapping the argument order of
every `◇` recursively (`mirror(a◇b) = mirror(b)◇mirror(a)`). Applying this to
677's RHS gives exactly `((y◇(x◇y))◇x)◇y` = E2910; applying it to 255's RHS
gives exactly `x◇(x◇(x◇x))` = E47. So E2910 is literally the opposite-magma
(dual) equation of E677, and E47 is the dual of E255 — confirming the paper's
statement that `E2910 ⊧_fin E47` is the "equivalent dual" problem to
`E677 ⊧_fin E255`. The arXiv paper's appendix table (Section on named
equations) independently labels E2910 as `(Dual of (E677))` and tags E677 as
`(Last open implication)`.

## 2. Status as of 2026-08-16: STILL OPEN

This is confirmed by three independent, up-to-date sources:

1. **The ETP paper** (Tao et al., "The Equational Theories Project:
   Advancing Collaborative Mathematical Research at Scale," arXiv:2512.07087,
   submitted 2025-12-08, revised 2025-12-16). Verbatim from the paper
   (Problem 8.1):
   > "However, there was (up to duality) precisely one finite implication
   > which we could not settle, which we leave as an open problem: Problem
   > 8.1. Does the law `x ≃ y◇(x◇((y◇x)◇y))` (E677) imply the law
   > `x ≃ ((x◇x)◇x)◇x` (E255) for finite magmas? This problem appears to be
   > 'immune' to many of our constructions, such as the linear magma
   > construction or the magma cohomology construction; the greedy
   > construction does show that `E677 ⊭ E255`, but the construction is
   > inherently infinite in nature. We tentatively conjecture that
   > `E677 ⊭_fin E255`; we refer the reader to the blueprint for several
   > partial results in this direction."
   Also earlier in the paper: "For the finite implication graph
   `E ⊧_fin E′`, we could similarly formalize all but two implications
   [677→255 and its dual 2910→47] ... we tentatively conjecture this
   implication to be false ... but the refutation appears to be 'immune' to
   most of the techniques that we developed for the project." They note the
   *unrestricted* (infinite-allowed) version `E677 ⊧ E255` **was** refuted,
   via a greedy construction (Section 5.5 of the paper) — but that
   construction is inherently infinite and gives no finite counterexample.
   The paper explicitly lists resolving this as future work item (1) in its
   concluding "future directions" section, with a pointer to the blueprint
   chapter for partial results.

2. **The GitHub repo, checked live today (2026-08-16) via the GitHub API**
   (not scraped HTML, to avoid any hallucination risk):
   - No merge, closed issue, or main-branch commit resolves it. `git log`
     on `main` for 2026-07-22 → 2026-08-16 shows only 2 commits, neither
     touching 677/255.
   - **Issue #1464**, "Equation 677 -> 255: Lean orbit lemma and
     DRAT-certified order-10 exclusion" (opened 2026-07-22 by
     `cameronsaddress`, still **open**, 2 comments, last activity
     2026-07-22T23:41:45Z) — the most recent substantive claim on the
     problem. Still pending maintainer review; not merged. See §3 below for
     content.
   - **PR #1440**, "Dedicated 677" (opened 2026-05-19 by Timeroot, still
     **open as a draft**, 455 files changed, +36,508/−20 lines, most recent
     commit 2026-08-13, i.e. **3 days before this recon**). This is an
     active, unmerged, collaborative branch (contributors include
     `Timeroot`, `b-reinke`, `blefloch`) building tooling specifically to
     attack 677→255: a "Finite677 mini-graph" search infrastructure
     (`most_wanted_677.txt`, generated via
     `lake exe extract_implications raw --proven --finite-only | python
     scripts/generate_finite677_graph.py --focus Equation255 --close
     --most-wanted 500`), a growing library of E677 countermodels of orders
     11, 13, 16, 19, 21, 25, ... (folder
     `equational_theories/Generated/Eq677Models/Countermodels677/`), Lean
     proofs of implications from 677+other-laws, and commits like
     "Construct finite counterexample for 677 + 1232 -> 4293" and "Add proof
     finite 4093 + 677 => 2" — i.e. side results about how 677 interacts
     with *other* laws, not (yet) a resolution of 677→255 itself.
   - The mini-graph snapshot in that branch (`most_wanted_677.txt`) reports,
     as of its last generation: 4693 other equations considered under
     "677+Finite"; 148 equations (grouped into 1394 canonical classes) are
     already known to imply 255 in this context; **0** are known not to
     imply it; **1244 of 1394 classes remain "Unknown."** The file ranks
     candidate intermediate equations by a heuristic "value" score for
     which one to attack next (top candidates in the snapshot: chains
     through Equation4065, Equation3456, Equation3253, Equation4380,
     Equation3862, Equation4590/Equation280, Equation1629, Equation3050/3522,
     etc., mostly routed through Equation3, Equation8, Equation255, or
     Equation280).
   - `commentary/Equation677.md` (current `main`) states plainly: "This
     equation is the last one to resist analysis for either the infinite or
     finite magma part of the project. The implication to Equation 255 for
     finite models remains open... It is immune to linear models and the
     cohomological approach... The finite spectrum of (cardinalities of
     finite magmas satisfying) this law is unknown" — with links to two
     Zulip threads (see §4).

3. **Blog confirmation**: Tao's post "The Equational Theories Project:
   Advancing Collaborative Mathematical Research at Scale" (terrytao.
   wordpress.com, 2025-12-09) states the project "resolved all of the
   22,028,942 implications except for one (and its dual)" for finite
   magmas, and that they "were unable to resolve even after months of
   effort," pointing to the blueprint page. The follow-up post "Mathematics
   Distillation Challenge – Equational Theories" (2026-03-13) still treats
   E677→E255 as the outstanding case (a commenter speculates about a
   finiteness-forces-idempotency path to a proof, but this is explicitly
   commentary, not an official resolution, and no such proof has since
   landed in the repo).

**Verdict: STILL OPEN as of 2026-08-16.** Not resolved. Conjectured false
(i.e. a finite counterexample — a finite 677-magma violating 255 — is
believed to exist) but neither a counterexample nor a proof of the
implication has been found/verified. This is (up to the E2910⊧E47 duality)
the single remaining open finite implication out of the ETP's ~22 million
finite implications.

## 3. Search effort / state of the art

**Structural results (blueprint, `blueprint/src/chapter/677.tex`,
confirmed against raw source):**
- Lemma "Basic properties of 677 magma": in any finite 677-magma, all left
  multiplications `L_y` are bijective (invertible), with
  `L_y⁻¹ x = x ◇ R_y L_y x`. Also: if `y◇x = x` then `y = Sx◇x`; in
  particular **255 holds for `x` iff the equation `y◇x = x` is solvable**.
- Lemma "255-equiv": seven pairwise-equivalent reformulations of "255 holds
  at `x`" in a finite 677-magma (in terms of solvability of `R_x y = x`,
  `R_x L_x z = x`, `L_x R_x z = z`, `R_x L_x y = y`, `L_x S y = y`, etc.).
- **No linear counterexamples**: if `M` is a finite 677-magma that is an
  abelian group with `x◇y = αx + βy + c` (α, β endomorphisms), then `M`
  satisfies 255. Proof reduces to surjectivity/injectivity of `R_x`.
- **No counterexamples via linear extension**: a stronger version — if
  `G×M` satisfies 677 where `G` already satisfies 677+255 and `M` is an
  abelian group with the product operation affine-linear in the `M`
  coordinate, then `G×M` also satisfies 255. So you can't build a
  counterexample as a linear extension of a "good" base.
- Over finite fields `F_p`, linear 677-models classify into exactly two
  families (Type 1: β a primitive 10th root of unity, α=1−β, c=0,
  translation-invariant; Type 2: α a primitive cube root of unity with a
  quartic/cubic constraint on β) — concrete examples given (`x◇y=2x−y` on
  F₅; `x◇y=4x+3y`, `x◇y=4x+y` on F₇; `x◇y=5x−4y+c` on F₃₁). All satisfy 255,
  so the entire linear/affine ansatz is a dead end for a counterexample.
- A **non-right-cancellative finite 677-magma** is explicitly constructed
  (via a field of size 16 with primitive cube/fifth roots of unity combined
  with a field of size 31), showing 677 does allow non-trivial/non-generic
  structure — i.e. 677 doesn't force cancellativity, so the easy sufficient
  condition for 255 (right-cancellativity) can genuinely fail.
- The **free 677-magma** on any generating set is explicitly constructed
  (via a tree/pairing combinatorial rule) and is shown **not** to satisfy
  255 — confirming the implication is non-trivial even ignoring finiteness,
  and giving the intuition for why unrestricted magmas refute it (this
  underlies the paper's "greedy construction" refutation of the
  *unrestricted* `E677 ⊧ E255`, Section 5.5 of the arXiv paper).

**Computational search bounds:**
- From the arXiv paper (benchmarking section on ATP tuning, using E677 as
  the running example precisely because it's numerically hard): Mace4 can
  exhaustively rule out *plain* E677 models (not yet conditioned on
  refuting 255) at size 8 in 1.5s and find a size-9 model in 16s; exhausting
  size 9 for plain E677 takes ~150–210s with good solver configuration
  (worse configs don't finish in 20h); Vampire's finite-model builder can't
  do either in 10 minutes. Table 4 in the paper extends benchmarking of
  special E677 models up to size 16. These numbers are about the general
  difficulty of finding/exhausting E677 models at all (used as an ATP
  tuning case study), not specifically about excluding a 677∧¬255
  counterexample.
- The **specific, sharper claim** — a computer search targeting
  677-magmas that violate 255 — comes from the pending
  **GitHub issue #1464** (2026-07-22, not yet reviewed/merged):
  - A new Lean-verified structural lemma was added (candidate, in branch
    `cameronsaddress:agent/equation677-orbit-lemma`, commit `8ad6e19`):
    in every finite 677-magma, `c◇c=a ∧ a◇c=a ⟹ c=a`, equivalently
    `(c◇c)◇c = c◇c ↔ c◇c = c`.
  - Using this "fixer" lemma to canonically relabel the forward orbit of a
    hypothetical 255-failure point, the author reduced order-10
    exhaustiveness to 45 orbit cases, encoded each as CNF with one-hot
    multiplication tables + symmetry breaking, and solved all 45 with
    Glucose 4.2, independently re-verified via `drat-trim` DRAT
    certificates (certificate archive ~1–2.8 GB). Result claimed: **all 45
    order-10 cases are UNSAT ⇒ any finite counterexample to 677→255 must
    have at least 11 elements**, *subject to review of the encoding/orbit
    argument* (i.e. not yet independently confirmed by maintainers).
  - A follow-up comment (same day) reports **near-miss order-11
    configurations**: two very different (differing in 109/121 cells)
    order-11 tables that satisfy the 255-failure condition and violate
    677 in only 30 of 121 instances (rather than 0). A local Hamming-ball
    SAT search (CaDiCaL + DRAT-verified) around one of these found no
    genuine 677-counterexample within Hamming distance 30 of it. This is
    only a *local* exclusion (doesn't extend the order bound past 10), but
    is offered as evidence that the obstruction is "global" rather than
    something a local table-repair/local-search heuristic could fix —
    i.e. a plausible reason why naive local search / SAT-guided repair
    hasn't found a genuine order-11 (or higher) counterexample yet.
  - **Caveat**: as of 2026-08-16 this issue is still open/unreviewed, no PR
    has been opened from it, and the certificate bundles have not yet been
    hosted/merged into the repo. Treat "order ≥ 11" as a strong, technically
    plausible but not yet institutionally verified claim.
- The **PR #1440 "Dedicated 677" branch** (draft, most recent commit
  2026-08-13) is a parallel, broader effort: it has generated and
  Lean-verified a library of concrete finite E677 countermodels at orders
  11, 13, 16, 19, 21, 25 (many "Model25nNN" variants — at least 29 distinct
  order-25 models alone) plus special models (e.g. a size-249 model), and
  built machinery to prove/refute implications from `677 + (other law)` to
  various targets. This is infrastructure/raw material (a "most wanted"
  list of intermediate lemmas to prove) rather than a resolution.

**Summary of state of the art (best available numbers as of 2026-08-16):**
counterexamples to plain E677 satisfiability are understood up through at
least order 25; but a genuine finite counterexample to **677→255**
specifically (a finite 677-magma that fails 255) has, per the pending and
unreviewed order-10 DRAT exclusion, **not been found for any order ≤ 10**,
and near-miss order-11 tables exist but none has been confirmed to actually
satisfy 677 exactly. No finite counterexample has been publicly announced;
the smallest possible one, if it exists, has ≥ 11 elements per the
unreviewed claim (or the bound implicit in the published paper's
benchmarking, which is weaker/unspecified for this exact question).

## 4. Zulip

Two relevant threads are pointed to by `commentary/Equation677.md`, both in
Zulip channel **458659-Equational** on `leanprover.zulipchat.com`:
- Topic **"FINITE: 677 -> 255"** — direct discussion of this problem, linked
  at permalink
  `https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255/near/486373274`
- Topic **"Order 3 Spectra"** (re: unknown finite spectrum of E677) —
  `https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/Order.203.20Spectra/with/527073087`

**Could not fetch actual message content**: leanprover.zulipchat.com
requires an authenticated session even for these public-repo-linked
channels/topics (confirmed: the anonymous `/api/v1/messages` endpoint
returns `"Not logged in: API authentication or user session required"`, and
the rendered page is JS-only so WebFetch only sees loading placeholders). If
message-level detail from these threads is needed, someone with Zulip login
access to that realm should pull them directly — recommend a follow-up with
browser automation + login, or asking a project participant.

## 5. Other remaining open finite implications

Per the arXiv paper's own accounting, there are **none** beyond this pair:
"there was (up to duality) precisely one finite implication which we could
not settle" — i.e., of the full ~22.03 million finite implications
(`E ⊧_fin E′` edges among the 4694 equations with ≤4 operation-applications),
exactly two are unresolved, and they are the dual pair
`E677 ⊧_fin E255` / `E2910 ⊧_fin E47`, which (via the mirror-magma
symmetry shown in §1) are logically equivalent to each other — solving one
solves both. So there is only **one** genuinely distinct open finite
implication target in ETP right now; there is not a broader menu of
several open finite implications to pick from. (By contrast, the
*unrestricted*, i.e. not-necessarily-finite, implication graph has more
residual open problems — e.g. E1729 was cited by Tao as having taken
"months of effort" to resolve — but that's a different, already-closed
case for the general graph, not a currently-open item, and it's outside the
finite-magma scope this recon was asked to check.)

## Sources

- [Equation 677 — ETP blueprint chapter](https://teorth.github.io/equational_theories/blueprint/677-chapter.html) (raw tex: `blueprint/src/chapter/677.tex` in the repo)
- [teorth/equational_theories — commentary/Equation677.md](https://github.com/teorth/equational_theories/blob/main/commentary/Equation677.md)
- [teorth/equational_theories — equational_theories/Equations/Eqns1_999.lean](https://github.com/teorth/equational_theories/blob/main/equational_theories/Equations/Eqns1_999.lean) (source of exact definitions of E255, E677, E47)
- [teorth/equational_theories — equational_theories/Equations/Eqns2000_2999.lean](https://github.com/teorth/equational_theories/blob/main/equational_theories/Equations/Eqns2000_2999.lean) (source of E2910)
- [The Equational Theories Project: Advancing Collaborative Mathematical Research at Scale, arXiv:2512.07087](https://arxiv.org/abs/2512.07087) / [HTML version](https://arxiv.org/html/2512.07087v1) — Problem 8.1, Section 5.5 (greedy construction), Section 7.3 (ATP benchmarking on E677), Section 9 (spectrum), concluding future-directions list
- [Terence Tao — "The Equational Theories Project: Advancing Collaborative Mathematical Research at Scale" (2025-12-09)](https://terrytao.wordpress.com/2025/12/09/the-equational-theories-project-advancing-collaborative-mathematical-research-at-scale/)
- [Terence Tao — "Mathematics Distillation Challenge – Equational Theories" (2026-03-13)](https://terrytao.wordpress.com/2026/03/13/mathematics-distillation-challenge-equational-theories/)
- [GitHub Issue #1464 — "Equation 677 -> 255: Lean orbit lemma and DRAT-certified order-10 exclusion"](https://github.com/teorth/equational_theories/issues/1464) (open, 2026-07-22)
- [GitHub PR #1440 — "Dedicated 677"](https://github.com/teorth/equational_theories/pull/1440) (open/draft, active through 2026-08-13)
- [teorth/equational_theories repository](https://github.com/teorth/equational_theories)
- Zulip channel 458659-Equational, topics "FINITE: 677 -> 255" and "Order 3 Spectra" on leanprover.zulipchat.com (linked from the commentary file above; content not directly accessible without an authenticated Zulip session)
