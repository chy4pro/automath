# A route-class negative for the finite implication E677 ⟹ E255

**DRAFT v1 (owner-677, round 33).** Status: complete outline with every load-bearing
sentence written; the numbered lemma statements are transcribed from the ledger and **each
names an executable artefact with negative controls — which for the six universal lemmas
checks bounded instances and printed reasoning, not the universal statement.** The phrase
this replaces was "**each carries its machine-verified provenance**", and Appendix A records
why it was withdrawn. Nothing in this file is self-promoted: every tag of the form
`(Rnn/NAME)` names a registry entry with a script, an `.out` and a negative control behind
it.

---

## 0. What this paper is, and what it is not

The Equational Theories Project's remaining open question at the finite level is whether

> every **finite** magma satisfying **E677** (`x = y ◇ (x ◇ ((y ◇ x) ◇ y))`)
> satisfies **E255** (`x = ((x ◇ x) ◇ x) ◇ x`).

**We do not settle it.** This paper reports a *negative* result about a **class of routes**
to it, together with two witnessed separations, one proved limitation, and the methodology
by which those were established and audited.

**The target is open and contested.** At the time of writing it is the subject of two open,
unmerged pull requests on the Equational Theories Project's own repository and of a
dedicated public database maintained outside it. A negative paper that presents a contested
open problem as uncontested is wrong on its first page, so the three live contemporaneous
artefacts are named in §1 before anything of ours is stated. This is a stronger position
than "uncontested", not a weaker one: it means the obstruction we describe is one that
active work is currently running into.

### The four claims

1. **A structural negative about a route class** (§3). Eight routes to the finite
   implication are closed, each for a *named* reason, and the reasons sort into three
   species: aggregation, arity ≤ 2, and entailment. The arity accounting is exact — the
   target has arity **3**, the maximum arity available in the aggregated stock is **2**, so
   **the gap is one**, not `q − 1`.
2. **Two witnessed separations** (§4). The abstract subsystem admits models in which `P` is
   not a line; and *stock minus the hypothesis `δ = 0`* admits **realizable** such models —
   16 real `q = 2` design classes carrying `q+1` perfect rows in non-line position,
   by complete enumeration with no sampling.
3. **One proved limitation, stated as a result rather than as an absence** (§5). The
   arity-3 antecedent is **unsatisfiable at `q = 2`**, and it has no witness in the only
   `q ≥ 3` exhaustion we own (1,070,784 objects; `|P| = 0` on 100% of them).
4. **The methodology** (§6), which is ours outright and is the part with no literature
   relative: chance rates computed on this line's own data, row-independence established
   *before* multiplication, derivation grading with its scope printed on the brief's face,
   and a four-round series of gate-blindness findings in which the apparatus built to catch
   wrong assertions was repeatedly itself the wrong assertion.

### The six things this paper does not claim

These are stated here, at the front, rather than buried in a limitations section, because
each was reached by a specific check that could have gone the other way.

- **(i) Not the phenomenon — only the instantiation.** The obstruction we hit has names in
  two literatures we would never have searched from inside this problem: **binary
  decomposability** in constraint satisfaction, and **the standard equations of a `k`-set**
  in finite geometry. We claim that *this* implication, on *this* stock, runs into it, and
  we cite both names. We do not claim the obstruction.
- **(ii) Not that the minimum-weight characterisation is prime-order-only.** That was our
  own folklore. It is retracted twice over: on literature grounds (the characterisation
  holds for all `q = p^h`), and then on our own computation — seven of the 24 moduli
  carrying a `Z/n`-linear 677-magma are composite, and `49 = 7²` is a prime power. What is
  prime-order-only is *our certificate*, not the theorem.
- **(iii) No figure of that kind is used as evidence anywhere in this paper; `~1/240` is
  named here only to record that it was refused.** (The earlier wording of this bullet read
  "appears nowhere in this paper, in any form" — a sentence containing the string, hence
  literally false, in a paper about numeric exactness. A retraction that re-asserts what it
  retracts is the same defect with better manners.) That figure was imported
  across a line boundary from a different campaign — it is that campaign's Gate A rate on
  that campaign's tables — recorded here as "computed", and inverted from a *conjunction*
  statement into a *per-row* one. It is retracted. The rate that is ours is **(R27/ROWRATE)**,
  measured on 677 data: 14 rows spanning **1/2 to 1/1.8 × 10⁹**, with a 200,000-draw
  empirical control and a negative control firing at 120×. It is quoted **only as a
  conjunction over a stated row set, never per row, and never from a verdict row** — the two
  worst-conditioned rows in that table are precisely the two verdict rows, which is why the
  restriction exists.
- **(iv) Not that `(COND)` is true or false, that the target is resolved, or that any
  automated return is a theorem.** A return that passes every check we have is a
  **candidate**.
- **(v) Not that we were first to look.** See §1.
- **(vi) Not that the `Z/n`-linear sub-case is ours or that we settled it.** PR #1435 reaches
  it by a different and stronger route (coefficient ideals with Nullstellensatz
  certificates). Our `n ≤ 120` enumeration is a **bounded cross-check**, run to verify that
  we could reproduce a competitor's published generators from scratch — not a result.

---

## 1. The three live contemporaneous artefacts

Read before this draft's first line was written, and cited accurately rather than merely
present.

**(a) PR #1440**, `teorth/equational_theories`, open draft. 455 changed files. **436
countermodel magmas at 37 distinct orders** (5 through 99, plus one at 249 and an explicit
`ZMod 31 × ZMod 31 × ZMod 31` extension of order 29,791). Nineteen conditional theorems of
the form `E677 ∧ EqX ∧ Finite ⟹ E255`. Three engines: superposition ATP, finite model search
harvested from a third-party database, and a Lean implication mini-graph with transitive
closure.

> **It does not contain our result, and the reason is that it is a different object, not a
> smaller one.** Every theorem on that branch carries `[Finite G]` or names a concrete
> magma; the largest object is `q = 31` *written out*, not a `q`-family. There is no arity
> accounting (the word does not occur), no route taxonomy, no design or plane or `P` or `δ`
> object, and **no negative result of any kind about the target**. The intersection of its
> method with our eight closed routes is **empty**.

**A provenance caveat, and we state plainly why it is not special pleading.** All 436 of
those countermodel theorems carry `@[equational_result native]`, an attribute that PR
gates `native_decide` behind; they are therefore not kernel-checked. The nine hand-curated
entries use `decideFin!` and are. We raise this because **this project has forbidden
`native_decide` in its own verification chain since its first week** — the rule is at
registry line 405 and predates this encounter by 28 rounds. A caveat that predates the
artefact it applies to is an observation. One invented on contact would be a scruple, and
we would not have made it.

**(b) PR #1435**, `teorth/equational_theories`, open, not a draft, +170,931 lines:
"LINEAR: complete implication graph via coefficient ideals + Nullstellensatz certificates".
It determines the linear implication graph for all **810** laws of ≤ 2 variables under
`x ◇ y = a x + b y`, and claims zero open pairs. **E677 (two variables) and E255 (one
variable) are both inside that set**, so the pair we care about is inside its claim — in
the linear sub-case.

**We re-derived rather than imported.** A 40-line integer bivariate-polynomial kernel with
no dependencies, run on our side, gives the coefficient conditions

- E677: `1 − ab − ab³` (x-part), `−a − b³ − a²b²` (y-part);
- E255: `1 − b − ab − a²b − a³`, y-part empty as a one-variable law requires.

**All three agree exactly with #1435's published generators.** That is the one place a
competitor's number appears in this paper, and it appears as an *input* that is then
independently reproduced, not as a citation that is adopted.

**(c) The `eq677.icarm.cloud` / `memoryleak47` / `icarm` database line.** Its front page
states that the target is "the main open question remaining from the Equational Theories
Project."

### The strongest honest sentence available, and whose sentence it is

PR #1440 generates an implication graph under the base assumption `Equation677 + Finite`:
4,693 nodes, 10,750 raw edges, 461,973 refutations. Of 1,394 canonical equation classes,
148 already imply E255 and 1,244 are open. The line worth quoting is the third one:

> `Equations not implying Equation255 : 0`

In that entire corpus, under `E677 + Finite`, **not one equation is known to fail to imply
E255**. So there is no negative result anywhere in this target's neighbourhood.

**This is recorded as a fact about their fact-database, not as a claim of ours.** It is a
statement about what that generated graph currently contains — about the state of a
mechanically-produced corpus at a moment in time — and it would change the day someone adds
a refutation. It is the honest frame for a negative paper, and it is context. It is not one
of the four claims and does not enter them.

---

## 2. The literature pass: **RUN, not COMPLETE**

A structural negative is worthless if the obstruction it describes is a known theorem under
another name. So a literature pass was run, and its result is the single most consequential
thing in §0's omission list: **the obstruction we found has names in two literatures.**

**The pass is RUN. It is not COMPLETE, and the distinction is load-bearing.** What was
established is that on the keys below the channel *answered* — a positive control on the
same endpoint returned 15 results — so every zero reported is a **true zero on that key**,
not a dead channel. What was *not* established is that the key set is adequate. A search is
bounded by its keys, and the keys are ours.

**The key list, attached so a reader can price the pass rather than trust it:**

| # | Channel | Keys |
|---|---------|------|
| 1 | arXiv | `all:"equational theory project"`; `abs:"magma" AND abs:"equational theories"` |
| 2 | GitHub | `repo:teorth/equational_theories 677`; `677+255`; open-PR list; `memoryleak47/eq677`; `eq677.icarm.cloud` |
| 3 | arXiv | `"standard equations"+"projective plane"`; `"k-set"+"intersection numbers"+"projective plane"`; `"characterization of lines"+"finite projective plane"` |

Channel 2 is the one that mattered and the one that had never been run: it is where both
open PRs and the third repository were found. The third repository was found in a site
footer, not in a search — **the channel list is itself bounded by its keys**, and that is a
limit of this pass, stated here rather than discovered by a reader.

**What the pass returned, and what it costs us.** Our arity obstruction is a named
phenomenon in two places: **binary decomposability** (constraint satisfaction — the question
of when a relation is determined by its binary projections) and **the standard equations of
a `k`-set** (finite geometry — the moment identities of §3.1 are exactly those). Neither
literature would have been reached from inside this problem, and neither was.

> **We claim the instantiation. We never claim the phenomenon.**

This costs us the general statement and keeps the specific one: that the E677 ⟹ E255 stock,
aggregated, retains nothing but `|P|`, and that the gap to the target is exactly one level of
arity. **No closed route reopens.** All eight remain closed for the reasons they were closed
for; what changes is that two of those reasons now have citations attached.

---

## 3. The route-class negative

*(Structure note: the species table is frozen. §3 is therefore a **transcription** — one row
per closed route with its named reason, one row per species — not a composition. This is
deliberate: the taxonomy was fixed before the write-up began so that the write-up could not
quietly re-scope it.)*

### 3.1 The aggregation species

Write `k_c := |P ∩ ℓ_c|` for the intersection numbers of a point set `P` with the lines of
`PG(2,q)`.

**Lemma (R19/MOMENTS)** *[proved, all `q`; verified on `PG(2,2..4)` over 334 / 586 / 922
subsets].* The two plane identities available to the stock are precisely the first two
binomial moments of `k`:

  `Σ_c C(k_c,1) = (q+1)|P|`  and  `Σ_c C(k_c,2) = C(|P|,2)`.

**Both are functions of `|P|` alone.** They hold for *every* point set, and therefore carry
**zero** information about the configuration of `P`.

This is sharper than saying that pair-level facts are weak. It is that *after aggregation
they retain nothing but the cardinality.* Moment 3 is not `|P|`-determined (measured: 2, 3
and 5 distinct values at `q = 2,3,4` over `(q+1)`-sets), and a line and a `(q+1)`-arc have
**identical** moments 1 and 2 — `(q+1)²` and `C(q+1,2)` — differing first at moment 3
(`C(q+1,3)` versus `0`).

**Corollary.** Every configurational conclusion this line has ever drawn had to enter
through a per-line cap `k_c ≤ K`, and any such cap converts to a bound of `(K−1)(q+1)+1` —
which is `q²` at `K = q` and `1` at the geometrically unavailable `K = 1`. **One sentence
covers six of the eight closed routes.** A further consequence kills a candidate family
before a line of it was written: the plane axioms give `A Aᵀ = qI + J`, so for any point set
`‖Aᵀ 1_P‖² = q|P| + |P|²`, again determined by `|P|` alone — the entire spectral/eigenvalue
family is refused for the same reason.

### 3.2 The arity species, and the exact accounting

**Lemma (R23/ARITY3)** *[proved, all `q`; exhausted at `q = 2,3,5` with a non-line negative
control at each].* For `|P| = q+1`, the statement "`P` is a line" is **exactly** "every
3-subset of `P` is collinear" — i.e. moment 3 of the `k`-profile is maximal.

So the target is an **arity-3** condition on `P`. The stock, aggregated, has maximum arity
**2** (§3.1). **The gap is one.** This corrects a figure this campaign carried for several
rounds: the gap is not `q − 1`, and the replacement specification is therefore *array-side
arity 3*, not *import of an arity-`q+1` plane theorem*.

**One coordinate that looks like an exit and is not.** The secant count `#{c : k_c ≥ 2}` is a
good **coordinate** and a refused **target**: under the standing hypothesis `|P| = q+1`,
`sec ≤ j` is logically identical to "`P` is a line" for every `j ∈ [1,q]`, so proposing it
as the thing to be proved is a **renaming**, not a reduction. We flag this because we
advertised it as live for one round before pricing it.

### 3.3 The entailment species

**Lemma (R23/IMPORT-VOID)** *[proved].* If a statement `I` is **valid** over the model class
— true of every point set in every projective plane of order `q` — then for any theory `T`,
`Cons(T ∪ {I}) = Cons(T)`. A valid statement is entailed by every theory, so adding it
changes nothing.

**Consequence, and it is the sharpest of the three species.** The exit "import an ingredient
of arity `q+1` from plane geometry" was never an exit. Assmus–Key, Bose–Burton, Rédei /
direction sets, Blokhuis–Ball, Szőnyi — all are valid, and **none of them can make the
target derivable if it is not already.** This closes an entire prospective family, including
future members of it, without examining them individually.

The only ingredient that can change what the stock entails is a **new array-side fact** —
one that constrains the design data, not the plane.

### 3.4 The eight routes

| # | Route | Reason closed | Species |
|---|-------|---------------|---------|
| 1 | Global double count of `I = {(x,c) : x ∈ D_c}` | (R12/DEGEN), all `q` | aggregation |
| 2 | The `g`-fibre line-union exclusion | retired empirically, all `q` | aggregation |
| 3 | The plane's pair count / any per-line cap used **aggregatively** | (R14/PAIRCAP), all `q` | aggregation |
| 4 | The T-sum over all `n` values | all `q` | aggregation |
| 5 | Residual non-negativity summed over the `n` rows | all `q` | aggregation |
| 6 | The separator / pair-uniqueness route | all `q` | arity ≤ 2 |
| 7 | (R20/LINECAP) used aggregatively (summed over `n` lines) | (R21/VARCAP) + (R21/CAPDEFICIT), all `q` | aggregation |
| 8 | Importing **any** valid theorem of `PG(2,q)` as the ingredient establishing "`P` is a line" | (R23/IMPORT-VOID), all `q` | entailment |

**Each refusal names its live neighbour**, because a refusal written broadly enough to be
safe is broad enough to condemn something that is still alive. Row 3: the *non-aggregative*
use of a per-line cap survives — at a single column a cap bounds `k_c`, and under `P ⊆ ℓ_c`
it forces `t_{c*} = 0`. Row 7: the same cap at **one** column, with no sum and neither moment
identity, is alive and is admitted as a branch discharge. Row 8: an **array-side** fact of
arity 3 in `P` is alive and is the only thing that is — subject to §5.

---

## 4. Two witnessed separations

**4.1 Abstract.** The abstract subsystem admits models in which `P` is not a line. This
separates "what the stock proves" from "what the target asserts" at the level of the
subsystem, but says nothing about whether such models are realizable as design data.

**4.2 Realizable, and this is the one that costs something.** Stock *minus* the hypothesis
`δ = 0` admits **realizable** models: **16 of the 20 real `q = 2` design classes carry `q+1`
perfect rows in non-line position**, by complete enumeration of the `q = 2` extremal branch
(46 assignment orbits, all completions, no sampling). Every quantity was recomputed from the
raw tables; the source file's own labels were used only as a cross-check that had to agree.

**Consequence.** The arity-3 condition of §3.2 is **false without `δ = 0`** — the hypothesis
is not decoration, and any replacement ingredient must consume it. No scalar weakening below
`nz(δ) ≤ 2` is available.

---

## 5. One proved limitation, stated as a result

The arity-3 route of §3.2 is alive as a *shape*. Its **adjudication** is not, and we prefer
to state that as a theorem about the control set rather than as an absence of witnesses.

**(R25/ONESIDED)** *[proved].* No `q = 2` object can test the hypothesis such a brief would
have to state: the antecedent is **unsatisfiable** at `q = 2`.

**(R26/CTRL-EMPTY)** *[computed, complete].* In the only `q ≥ 3` exhaustion we own — the
translation-invariant family at `q = 3`, 1,070,784 objects — the `δ` distribution is a point
mass at zero and so is the `|P|` distribution: `δ = 0` on 100%, `|P| = 0` on 100%. **The
control set is empty.**

So an object with `δ = 0` **and** `|P| ≥ 3` is, at `q = 3`, either rowcap *attainment*
(open) or a *refutation* of a standing proposition — i.e. constructing the control set is
one of this campaign's two open outcomes. **The adjudication cannot be cheaper than the open
problem it was meant to help settle.** That is a result about the method's reach, and we
report it as one.

---

## 6. Methodology

This section is the part with no literature relative, and it is the part we would defend
first.

**6.1 Chance rates computed on this line's own data.** **(R27/ROWRATE)**: 14 rows, rates
spanning 1/2 to 1/1.8 × 10⁹, with a 200,000-draw empirical control and a negative control
firing at 120×. Quoted as a **conjunction** over a stated row set. Never per row. Never from
a verdict row — the two worst-conditioned rows in the table are the two verdict rows.

**6.2 Row-independence established before multiplication.** **(R27/ROWDEP)**: of six rows
assumed independent, three were not, and the naive product overstated by **3.3 × 10⁷**. The
finding is on our own new table, caught by the instrument the same round built.

**6.3 Derivation grading, with its scope on the brief's face.** **(R27/DERIV-SCOPE)** states
what derivation grading *cannot* see, printed where the grader is used rather than in a
methods appendix.

**6.4 The gate-blindness series, reported because it is the finding.** Four consecutive
rounds produced a defect of one species: **the assertion was wrong and the data were right.**
Fifteen instances are on the ledger, three of them from the round that built the fix in §6.5.
The three that matter here:

- A negative control asserted that the projection magma `x ◇ y = x` *satisfies* E677. On any
  magma with `|M| ≥ 2` it does not — E677's right-hand side is then `y`, forcing `x = y`.
  **The apparatus meant to catch wrong assertions was itself the wrong assertion.**
- The predicate for E255 was hand-written with the wrong number of operations, and the second
  time it reported a competitor's order-9 Cayley table as **refuting E255** — i.e. as a
  counterexample resolving the entire open problem. It was caught by the competitor's own
  fact list, which is the wrong direction for a check to run in.
- **The lesson, recorded in prose after the first instance, did not prevent the second.** The
  memorial sat one screen above the repeat.

**6.5 The response, and the reason it is in a methods section rather than an acknowledgement.**
The two equations are now written **once**, as term trees, in a single checked module. The
Cayley-table check, the `Z/n`-linear check and the symbolic coefficient-ideal derivation are
*interpreters over those same trees*, so there is no second place **on the live verdict path**
in which an operation count can be typed. That qualifier is measured, not defensive, and §6.6
states what it excludes. The tree is then compared **structurally** — node for node, against a
frozen transcription of the equation's published statement parsed back into a tree — at import:
**a law re-typed as a tree that differs from the published statement in any way raises before it
reaches a datum.**

> **That sentence is a correction, and the correction is the point.** Until review it read *"the
> op count is derived from the tree and audited against a frozen statement of each law at import:
> a mis-typed law raises before it reaches a datum."* The audit compared **operation count and
> variable set, and nothing else.** An external reviewer supplied the class nobody had injected:
> `x = (x◇x)◇(x◇x)` is three operations over `{x}`, identical to `E255` on **both** audited
> dimensions, **passed in silence, and is a different law** — separated by four order-2 magmas,
> e.g. `[[1,0],[0,0]]`, where `E255` fails and it holds. **The function was named `_shape_audit`
> and audited everything except the shape.** Re-scored against a fault set that includes the three
> dimensions it never measured — association, variable placement, and which variable stands on the
> left — the audit certified `LIVE 4/4` scores **4/9**; the structural audit scores **9/9**, and
> each of the nine faults is shown to be a genuinely different law by exhibiting a separating
> magma. **The four original faults were all drawn from the two dimensions the check already
> measured, which is why `4/4` meant nothing.**

Every prior copy was
lifted verbatim from its original file and checked against the module over 286 Cayley tables
and 22,139 `(a,b,n)` triples — **zero disagreements**, which is what licences the replacement.

Two findings came out of building it, and both sharpen §6.4 rather than softening it:

- **The two mis-typings were the same characters, not the same idea in a new notation.** Our
  own record of the first instance described it as a different formulation; checked against
  the file, it was not — the second was a character-for-character re-typing of the first.
- **The witness that caught the first defect could not have caught the version we thought had
  been written.** *Lemma:* on a magma satisfying E255, the four-operation variant
  `(((x◇x)◇x)◇x)◇x` evaluates to `x◇x`, so it holds **iff the magma is idempotent.** The
  witness used was idempotent. The defect was caught only because the expression actually
  typed was structurally always-false. **The control that caught it was a coincidence of the
  defect's shape, not a property of the witness** — which is precisely why a memorial is not a
  control.

> **A lesson recorded in prose is not a control. A control is a thing that fires.**

**6.6 And the limit of that fix, which we state because it is the honest reading — and
because the module's own description of its power was, on first writing, false.** The module
makes **one** class of error impossible. It does not make us careful.

**The fix contains two mechanisms, not one, and they cover different defects.** The first is
a *structural audit*: each law is a term tree, and at import that tree is compared node for node
against a frozen transcription of the equation's published statement. It is live — fault
injection trips it on all nine faults in a set built from the dimensions its predecessor did
**not** measure, including a four-operation `E255`, a three-operation `E677`, an `E255` carrying a
stray second variable, a three-operation one-variable `E255` with the wrong bracketing, an `E677`
with its two variables exchanged, and an `E677` whose left-hand side is `y`. Its predecessor,
which measured operation count and variable set only, trips on **four of those nine** — and the
five it misses are exactly the five that reach the audit's namesake. The second is a *monopoly*:
every interpreter routes
through one evaluator, so no round has an occasion to write a raw indexing expression at all.

**Which mechanism caught what is the part worth reporting, because the module's own comment
got it wrong.** That comment claimed the audit "would have caught both defects at import."
Run, it does not: the expression both rounds actually wrote is `t[t[t[t[x][x]][x]][x]]`, which
applies the operation **three** times and leaves a **dangling row index** — it is not a
mis-typed law but a hand-written subscript expression, and *a dangling row index is not
expressible as a term tree*, so the audit has nothing to audit. A file that imports the module
and then writes that predicate verbatim runs to completion and returns the wrong answer with
the audit silent. Against the two defects that were actually committed the audit covers
**zero of two**; what it does cover is a genuine four-operation variant that a later round
*reconstructed* and no round ever committed. The defect that *was* committed is covered by the
monopoly — and the monopoly is enforced by a repository sweep, not by the audit. **The sweep is
the control; the module is only where the sweep points.**

**And the monopoly holds over the live verdict path, not over the repository — we say so because
we measured it and the first wording did not.** §6.5's claim that there is "no second place in
which an operation count can be typed" was written unqualified. Swept **by shape, with every
identifier erased** — not by function name, which under-reports for the same reason this section
already gives, namely that the symbolic form carries no `def` — **10 files outside the module and
its frozen archive still contain a shape-exact re-typing of E677, of E255, or of the dangling-index
defect, 19 occurrences in all.** Every one of them is a helper of a route this paper reports as
**closed**; none of them is reachable from any number this paper cites. That is the reason the
qualifier is *live verdict path* and not *repository*, and it is the whole reason:

> **A defect in a closed-route helper cannot move a claim now. It is not evidence that there was
> no defect while the route was open, and we have not looked.** The 10 files were **located, not
> checked**; no closed route has been re-adjudicated, and no claim is made about their correctness
> in either direction.

We report the count rather than the reassurance because the reassurance is the same species as the
defect: **a monopoly asserted over a population nobody counted is a label claiming more than its
artefact establishes**, which is precisely the failure this section exists to record. The
name-based sweep that returned "clean" one round earlier was not wrong about what it counted; it
was pointed at names, and **a name is a mark someone else left.**

**The arithmetic in our own account of the defect was also wrong, in three places and three
rounds running:** two rounds' comments and the module's header all called that expression "four
operations." It is three applications plus a dangling subscript. We report this because the
count was the subject of the round that got it wrong.

**And the round that built the module produced three more defects of the same family, plus two
of the reviewer's.** Ours: a hand-transcribed control table missing six rows (caught by the
module's own well-formedness check); an unbound variable inside a negative control (caught by
it failing to run); and a grep result written down before the grep was run (caught by nothing
but the habit of running it afterwards). The reviewer's, in the pass that checked that round:
the same defective expression re-typed a third time — reported as a passing negative control,
because a predicate that returns `False` unconditionally agrees with every negative control
ever written and disagrees only with a positive one — and a fault-injection probe that
mis-unpacked its own argument and reported a live guard as dead. Both were found only because
a negative result was diagnosed instead of reported.

**The correct claim for a methodology section is therefore narrower than "the problem is
solved," and narrower than we first wrote it.** One specific recurring failure now has a
mechanical stop; a second, adjacent failure is stopped by a different mechanism that has to be
named separately or it gets credited to the first; the rest are unstopped. **A control that
overstates its own coverage belongs to the same species as the defects it was built to catch —
and ours did, in the sentence that described it.**

---

## 7. What remains open

`(COND)` with `δ = 0`: **open**. The line case: **open**. The target: **open, and contested
by three artefacts across three repositories.** The `Z/n`-linear sub-case is settled in the
literature by #1435's route and confirmed on our side for `n ≤ 120` — 70 linear 677-magmas
over 24 moduli, **no counterexample**, with the symbolic filter and the full `n²` sweep run
against each other on all 583,219 triples without a single disagreement.

**And one boundary we state rather than let pass.** All 24 of those moduli are **odd**. That
is **not** evidence for an odd-order conjecture. Even-order finite 677-magmas exist — at
orders 16, 76, 80 and 96. **Order 16 we verified ourselves from its table
(`R31_m16_provenance`); orders 76, 80 and 96 are QUOTED INPUTS from an external database and
we have not reproduced them** — they are load-bearing only for the negative point that even
orders occur at all, which order 16 alone already establishes. They
simply are not `Z/n`-linear. **The `Z/n`-linear family is a strict sub-family, and a property
of it is not a property of the target.**

---

## Appendix A — Provenance

**Every umbrella in this appendix was narrowed after review, and the four sentences it
replaces are printed below it.** An external reviewer's label audit returned five CRITICAL
rows against this appendix alone, all of one species: a provenance label claiming more than
the artefact under it establishes. Each was re-derived here before being adopted — we do not
adopt a finding because a judge we respect made it — and each survived.

- **Numbered lemmas.** The paper cites **13** numbered lemmas. **Six** of them
  (`R19/MOMENTS`, `R20/LINECAP`, `R21/CAPDEFICIT`, `R21/VARCAP`, `R23/ARITY3`,
  `R23/IMPORT-VOID`) are labelled `PROVED, all q` — **universal statements, which no bounded
  script verifies.** Three of the six (`MOMENTS`, `CAPDEFICIT`, `ARITY3`) pair the hand proof
  with a bounded machine check at named orders; **three (`LINECAP`, `VARCAP`, `IMPORT-VOID`)
  do not.** `R23/IMPORT-VOID` is the sharpest case: its script *prints the proof as a string
  literal* and then checks a bounded side-measurement. **The correct claim is that every
  numbered lemma has an executable artefact that exits 0 with zero failures, and that for the
  six universal lemmas that artefact verifies bounded instances and printed reasoning, not the
  universal statement.**
- **Exit codes.** The cited `.out` files do exit 0 with zero failures. **That establishes
  successful execution of the checks each script contains — nothing wider.** It was previously
  offered as the evidence for "machine-verified", which is the same sentence doing two jobs.
- **Counts.** Many counts in this paper carry an explicit census (§3's subset counts, §4's
  enumerations, §6.6's 10 files / 19 occurrences, §7's 583,219 triples). **There is no
  artefact that audits every prose number in this paper against a source, and we do not have
  one.** "Every count in this paper was counted" is therefore withdrawn, not requalified.
- **Quoted external numbers.** §7 quotes even-order 677-magmas at orders **16, 76, 80 and
  96**. Only **order 16** is frozen and re-derived locally (`R31_m16_provenance`). **Orders
  76, 80 and 96 are quoted inputs that we have not reproduced**, and §7 now says so on its
  face.
- **Retractions.** Every retracted figure is retracted by name in the registry rather than
  rewritten in place. **This one is unchanged; the reviewer did not challenge it and neither
  do we.**

> **The four sentences this replaces, kept because a withdrawn label is evidence and a deleted
> one is not:** *"Every numbered lemma is machine-verified with negative controls, in scripts
> that exit 0 with zero failures. Every retracted figure is retracted by name in the registry
> rather than rewritten in place. Every count in this paper was counted; where a number is
> quoted from an artefact we did not produce, it is marked as an input and reproduced
> independently before use."*

**Open provenance limits, stated:**
- PR #1440 was read at the level of its diff structure, its Lean statements and its
  generated-theorem shapes. Its 1,684 ATP-generated proof terms were **not** read
  individually; the claim that none contains something of ours is a claim about their
  *statement shapes*, which are uniform, not about their contents.
- The `n ≤ 120` linear enumeration is bounded and confined to `Z/n`-linear magmas. The target
  quantifies over all finite magmas.
- The literature pass is **RUN, not COMPLETE** (§2).
- The predicate-unification sweep of §6.5 does **not** re-adjudicate the closed routes. That a
  helper belongs to a closed route means a defect in it cannot move a claim *now*; it does not
  mean there was no defect when the route was open.
