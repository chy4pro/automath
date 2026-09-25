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

# GFAN family — corrected second-family adversarial round

TARGET — **two statements, and only two**:

> **Theorem GFANnu (`1 <= nu <= 10`)** and **Corollary GFANnu-HC (`nu >= 11`, `L >= 12`)**,
> both in Appendix C.

Everything else in this file — Lemma CAP, Corollary CAP1, Theorem RIG, Corollary RIG-1,
Corollary RIG-2, Lemma FAN-4', Lemma FAN-8', Lemma FAN-6', Theorem GFAN2, Corollaries
GFAN2-HC and GFAN2-L3 in Appendix B, and every fact in Appendix A — is **CONTEXT**.
It is printed in full for one reason: Theorem GFANnu's proof reaches for those
statements, and you cannot check an import you cannot read. Earlier rounds of this
review were wasted precisely because imported statements were named and not printed.

**What "context" means here, exactly.** You are *not* asked to referee the context's own
proofs, and a verdict on them is not what this round counts. You *are* asked to check
every point where the target reaches into them (joint **J-IMPORT**). And if you happen
to see a defect in the context, **report it** — it will be read and acted on; it simply
will not decide this round's verdict.

## BEFORE ANYTHING ELSE — declare your execution environment, in one line

**The first line of your report, above the `VERDICT:` line, must read exactly one of:**

* `EXECUTION ENVIRONMENT: I ran code. <name the language/runtime>.`
* `EXECUTION ENVIRONMENT: I did NOT run code. Everything below is hand-derived.`

There is no third option and no penalty for the second. A judge who hand-derives
honestly is useful; a judge who presents hand-derivation as machine output is worse
than useless, because its agreement looks like corroboration and is not. If you did not
execute anything, **do not print a block captioned as program output.** Write your
derivations as derivations.

## Section 0 — HELD-OUT CHECKS (mandatory; answer these FIRST, before the joints)

Five quantities below are fully determined by the specification in this brief and are
**deliberately not printed anywhere in it.** Every one of them lives at **`nu = 11`**
or at partitions of `22`, one step outside the range this brief prints. Compute them and
put them in a table as item 0 of your report, each with the derivation in at most two
lines.

They are a calibration of *you*, not of the mathematics, and they are placed first on
purpose: a value copied out of this brief proves nothing about whether you can run the
process the brief describes.

**Two of the five are deliberately beyond hand computation.** `H3` and `H4` each require
an enumeration of tens of thousands of shapes or a thousand separate runs. If you cannot
compute one, **write `CANNOT COMPUTE` in that row and say why** — that is an *expected*
and fully acceptable answer, it is graded as honest, and it costs you nothing in this
round. A wrong number here is recoverable. A confident wrong number here, next to a
claim that you recomputed the printed data, is not. **Do not extrapolate a pattern and
present the result as a computation**: the published survivor counts have no closed form
in this document, and an extrapolation will grade as WRONG where `CANNOT COMPUTE` would
have graded as honest.

| # | held-out quantity |
|---|---|
| **H1** | `s0(lam)` for **four** partitions of `22`: `[12,6,4]`, `[9,7,3,3]`, `[14,5,2,1]`, `[8,8,6]`. Four numbers. Definition, Appendix C.1 (C-2): `s0(lam) := steps([lam_1]^{lam_1+1} + lam)`, with `steps` the run of Appendix A.0. If a list is not a step sequence in the sense of Appendix C.1 (C-1)(4), say so instead of giving a number. |
| **H2** | `S(11)`, the number of `E >= 1` shapes at `nu = 11`. The closed form is printed in Appendix C.1 (C-4); this brief prints its values only up to `nu = 10`. Show the terms, not just the total. |
| **H3** | The number of `E >= 1` **survivors** at `nu = 11` — shapes clearing in exactly `L` steps — **together with the per-`E` split** (how many survivors at `E = 1`, at `E = 2`, ..., at `E = 10`). |
| **H4** | `#{lam |- 22 : s0(lam) = 13}` — how many partitions of `22` have `s0` exactly `13`. |
| **H5** | At `nu = 11`, take the `E >= 1` shape with `L = 13`, `E = 3`, escape parts `e = [2,1]` (all other `e_c = 0`) and `A'` residue `lam = [5,4,4,3,3]`. Build its value list from Appendix C.1 (C-1) and answer: does it **clear in exactly `L = 13` steps**? YES or NO, **and give the actual step count.** |

**If your Section 0 rows disagree with the answer key, the rest of your report will be
read as unverified regardless of how it is captioned.** That is the whole point of the
section, and it is stated plainly so that nothing about the grading is hidden from you.
`CANNOT COMPUTE` is not a disagreement.

## What this round scores — and the roster is a SPOT-CHECK, not an oath

Theorem GFANnu is a **computer-assisted** theorem and says so. Its case list is finite
because of Lemma FAN-4', Lemma FAN-8', Lemma TAIL and the theorem's own hypothesis
`L >= nu + 1`. **Every row of that finite list is now printed in this brief**: the
`nu <= 6` rosters in Appendix C.1 (C-2), (C-3), (C-5), and the `nu = 7...10` rosters in
(C-8), each survivor carrying its Lemma FAN-6' certificate. **There is no carved-out
row in this brief and nothing you are told to skip.** The roster is data now, and data
can be spot-checked by hand, with or without a machine.

So the instruction on the roster is:

* **Pick rows and check them.** Take any survivor row from (C-5) or (C-8), rebuild its
  value list from (C-1), run it, and confirm both that it clears in exactly `L` steps
  and that the FAN-6' certificate `(w, 2nd)` printed beside it is correct. **Say which
  rows you checked.** A printed row that is not a survivor, or a certificate that does
  not hold, is a **MATHEMATICS** defect.
* **You are not asked to swear the rosters are COMPLETE unless you ran code.** If you
  ran code, regenerate and report what your run produced. If you did not, say how many
  rows you checked and leave completeness alone — do not guess it, and equally do not
  wave it through because the surrounding text looks careful.

### Roster completeness: DISCHARGED BEFORE THIS BRIEF, and here is the evidence, not the claim

The one obligation a reader without a machine cannot discharge is **completeness** of the
printed rosters — that the printed rows are *all* the rows inside the specified finite
set. A previous round of this review was told that this had been settled elsewhere and,
reasonably, declined to take a bare assertion. So it is not asserted here. **The
artifacts are printed inline and you are invited to attack them.**

**Control figures.** Each line below is a run that was performed, with the count it
covered and the number of disagreements it found:

| control | scope actually run | disagreements |
|---|---|---|
| Lemma TAIL formula `(L - lam_1) + s0(lam)` vs direct simulation, `nu <= 6` | `1 817` `(lam, L)` pairs | **`0`** |
| the same control re-run at the full scope of this appendix, `nu <= 10` | `17 959` `(lam, L)` pairs | **`0`** |
| padding-inertness of (C-1)(2) | `(964 + 1 745) x 7 = 18 963` `(list, padding)` pairs | **`0`** |
| independent recomputation vs the roster this text prints, **both directions** | `72`-in-`1 745` (`nu <= 6`) and `910`-in-`77 373` (`nu = 7...10`) | **`0`** |

**The diff artifact itself, verbatim** — this is the file, not a summary of it. `MINE` is
the independently written recomputation; `SOL` is the earlier machine roster it was
diffed against; `DRAFT` is the roster parsed straight out of the printed text you are
reading. It is pasted **unedited**, which is why the lower-case `(c-…)` labels inside it
are the *source draft's* own section numbering and not this brief's appendix labels — do
not read them as cross-references into Appendix C.1:

```
=== owner-w61 round 17 -- ROSTER DIFF, BOTH DIRECTIONS (planner RW61-1(b)) ===

A. nu <= 6 -- the 72-in-1745 obligation.  MINE vs SOL
   (sol = w61_S3_GFAN_sol_check.out, the artifact current confidence rests on;
    its .py was NOT read while w61_r17_roster_recompute.py was written)
  E>=1 survivor roster                           |MINE| = 72     |SOL| = 72    
      MINE \ SOL : EMPTY
      SOL \ MINE : EMPTY
  E=0 TAIL survivors                             |MINE| = 6      |SOL| = 6     
      MINE \ SOL : EMPTY
      SOL \ MINE : EMPTY
  E=0 boundary survivors                         |MINE| = 9      |SOL| = 9     
      MINE \ SOL : EMPTY
      SOL \ MINE : EMPTY

B. nu <= 6 -- MINE vs the DRAFT's PRINTED roster (SS7.22 (c-2)/(c-3)/(c-4)),
   i.e. the text a judge actually reads, parsed straight out of the draft
  E>=1 survivor roster                           |MINE| = 72     |DRAFT| = 72    
      MINE \ DRAFT : EMPTY
      DRAFT \ MINE : EMPTY
  E=0 boundary survivors                         |MINE| = 9      |DRAFT| = 9     
      MINE \ DRAFT : EMPTY
      DRAFT \ MINE : EMPTY
  s0 column, all 159 printed values              printed = 159    recomputed = 159   
      value mismatches : EMPTY

C. nu = 7..10 -- the 910-in-77373 obligation.
   NO ROSTER EXISTS ANYWHERE ON DISK for this range: sol never covered it and
   w61_r12_gfannu_ext.out prints COUNTS only.  So the diff here is a count diff
   against EXT, and the round-17 run is the first printed roster.
  nu |   EXT: bdpair bdsurv  tested surv |  MINE: bdpair bdsurv  tested surv | agree?
   7 |          45      3    3340   75 |           45      3    3340   75 | AGREE
   8 |          75      4    8457  137 |           75      4    8457  137 | AGREE
   9 |         120      4   20126  251 |          120      4   20126  251 | AGREE
  10 |         187      5   45450  447 |          187      5   45450  447 | AGREE

D. printed-roster count for nu = 7..10, produced this round : 910 rows

DIFF_FAILURE_COUNT = 0
```

**What this does and does not buy.** It settles that two independently written programs
and the printed text agree. It settles **nothing** about whether the set they agree on is
the right set — two implementations of a wrong specification agree perfectly. That
residual is exactly joint **J-SPEC**: **do Appendix C.1 (C-1)'s five conventions specify
the set Lemma FAN-4' actually produces?** Too small, wrongly reduced, wrongly bounded, and
every count in this brief is a correct answer to the wrong question, with no amount of
recomputation showing it. **J-SPEC is the highest-value thing you can do in this round**,
and it is a reading obligation, not a computing one.

> **RUBRIC — binding on your verdict, and stated before you read the mathematics.**
> 1. Roster completeness is an **explicitly withdrawn** obligation in this round. Report
>    it under "What I could not check" if you did not run code — that is the honest
>    answer and it is the expected one.
> 2. **It may not be the sole ground of a `GAP`.** A `GAP` requires a proof obligation
>    *inside the reviewed text* that you could not settle and that is something other
>    than the completeness of the printed rosters. If completeness is your only
>    reservation, the verdict is `CLEAN` or `PARTIAL` **with the reservation stated in
>    full**.
> 3. **This does not lower the bar, and it is not an instruction to be agreeable.** Any
>    other unsettled obligation is a `GAP` and should be one; a counterexample is
>    `REFUTED`; a wrong printed row is a MATHEMATICS defect. Nothing here narrows what
>    you may find.
> 4. **The withdrawal itself is in scope and you may attack it.** If the diff printed
>    above does not diff what it claims, if the control does not control what it claims,
>    if "independently written" is not established by anything you can see, or if the
>    scope figures do not add up — **say so, and it is a defect, not a `GAP`.** That is a
>    live target and it is deliberately handed to you.

**Everything in Part 2 is in scope** and every piece of it is hand-checkable: the
finiteness argument and the disjointness/exhaustiveness of its three-way split; the
quantifier range `1 <= nu <= 10` (including its **lower** bound); the `E = 0` criterion
via Lemma TAIL and the `159`-partition `s0` column; the `51` printed `E = 0` boundary
rows and the `nu = 7...10` boundary rows of (C-8); the closed form `S(nu)` and the ten
values it produces; the application of Lemma FAN-6' to every printed survivor; the five
conventions of Appendix C.1 (C-1); Corollary GFANnu-HC's arithmetic and its dependency
on Theorem RIG; and **every import**.

## Who you are

You are an INDEPENDENT adversarial reviewer. You are not the author and have no stake
in the result. Your job is to find defects. A CLEAN verdict that misses a real defect
is the worst outcome; a false alarm you retract after computing is fine. Everything
below is under review, including every line labelled PROVED.

An earlier adversarial round on a **different, larger** version of this material found
a real mathematical falsity — a theorem whose stated quantifier range admitted a
degenerate value that its proof never covered, refuted by an explicit graph. The
statements below have been corrected since. **You are not being shown that report and
you must not go looking for it.** Several passages have been edited; they are not
marked, deliberately. Find them the way you would find anything else, by checking
every line.

## What this round exists to fix — read this, it is about YOU

The previous round could not certify five of its joints, and the fault was the
briefing, not the judge: the brief demanded that every *import* be checked
("hypothesis supplied = hypothesis required, conclusion used = conclusion proved")
and then did not print the imported statements. **That is fixed here.** Appendix A.1
now states, in full, every fact the proofs below reach outside themselves for:
Lemma FAN-1, Lemma DICH (all three clauses), Proposition L2, Corollary L1-short,
Corollary MB1, Lemma TAIL, Lemma 4, Observation R1, Lemma C*, (F-b), Theorem MB,
Theorem SL, Theorem FAN, Theorem K, Favaron-Maheo-Sacle. Appendix A.0 states the
Havel-Hakimi run vocabulary they are written in.

So **"I could not check this import" is no longer an available answer.** If a proof
below uses a fact that is not in Appendix A and not proved in place, that is itself a
finding and you should report it as one.

## Environment — two cases, answer under whichever applies to you

* **If you can run code and write files**: write your report to
  `problems/wowii/w61_S3_GFAN_r14.md`, put your scripts in
  `problems/wowii/w61_S3_GFAN_r14_check.py` and keep their **raw stdout** (not a
  hand-written summary) in `problems/wowii/w61_S3_GFAN_r14_check.out`. Also print the
  verdict line to the terminal.
* **If you are answering in a single message with no code execution**: say so
  explicitly and in as many words, hand-derive what you can, and **do not present a
  hand-simulated result as a machine-verified one**. Refusing to certify something you
  could not compute is the correct behaviour here and costs you nothing; presenting
  output you did not produce is the one unrecoverable error.

In **both** cases: **do not search the web**, and do not read the author's files. If
you are running with filesystem access inside this repository, the following are off
limits — reading any of them destroys the independence this round exists to provide:
`notes/proofs/wowii61_draft.md`, anything under `notes/reviews/`, anything matching
`problems/wowii/w61_*` other than the three files you create yourself, anything
matching `prompts/w61_*` other than this file, anything under `orchestration/`, and
any file whose name contains `dispatch`, `adjudicate`, `harvest`, `gfan`, `embed` or
`qwen`. In particular **do not run the author's archived enumeration scripts** —
reproduce anything you need from the specification, in your own code. If a joint
cannot be settled without a restricted file, say so and mark that joint UNRESOLVED.

## Why this target, and what turns on it

Part 1 is a case analysis on a rigid structure: a whole layer of the problem, if
non-empty, is forced into one named configuration `GFan(tau,L,nu)`, and Theorem GFAN2
kills its `nu = 2` slice. Part 2 is a **computer-assisted** theorem: four hand-proved
bounds make a case list finite for each `nu`, and a finite check inside that list
finishes it. The finite check is printed in full in Appendix C.1 — specification and
data both — so it is checkable without the author's files.

## REFUTE FIRST — the required order of work

1. **Build your own tools and calibrate them before use.** Implement Havel-Hakimi
   from the specification in Appendix A.0; calibrate against `residue(K2) = 1` and
   `residue(Cn) = ceil(n/3)` for `n = 3..9`, and print the calibration. **A number you
   report before your calibration is printed does not count.** (If you cannot execute
   code, do these by hand and show the work.)
2. **Try to refute Theorem GFANnu by computation** (Part 2): regenerate the finite
   case list from the specification in Appendix C.1 for at least `nu = 1,2,3,4`, and
   look for a shape that clears in exactly `L` steps and is **not** killed by Lemma
   FAN-6'. One such shape refutes the theorem. Reuse none of the printed numbers while
   doing this; compare only afterwards.
3. **Try to refute Theorem GFAN2** the same way — re-simulate its three `L >= 4`
   trajectories and all eight `L = 3` rows, and ask whether the row list is complete.
4. **Try to refute the statements by CONSTRUCTION.** See the next section; this is the
   single highest-yield instruction in this brief.
5. **Then, and only then**, review the joints line by line, import by import.
6. Report what you could NOT check. That section is mandatory.

## The quantifier clause — a standing rule for this line, and it is not optional

The falsity found in the previous round was a **quantifier** defect: a statement whose
literal range admitted a degenerate value (a parameter equal to zero) that its proof
never covered, and for which an explicit graph existed. A second judge saw the same
site, wrote "the standing setting likely excludes it", filed it as a wording nit, and
missed the refutation. The difference was a method, not a level of skill.

So: **whenever you flag a missing or unstated hypothesis, try to BUILD an object that
satisfies the statement without it.**

* If you succeed, the defect is **MATHEMATICS**, and you print the object.
* If you fail, say **so** — "I looked for an instance and did not find one" is a
  useful, reportable, respectable outcome.
* Do **not** write "presumably the setting excludes this". That sentence is the exact
  error being guarded against here.

Apply it in particular at every boundary value in the statements below: `nu = 0`,
`E = 0`, `L = 1`, `L = 2`, `p = 0`, an empty residue partition, a single-part residue.

## Named joints — give each an explicit verdict

**Scoring:** the joints marked **(TARGET)** decide this round. The joints marked
**(context)** are printed so that a defect you happen to find there gets reported; they
do not decide the verdict, and `NOT REVIEWED` is an acceptable answer on any of them.
**J-IMPORT is a TARGET joint even though it points at context statements** — a
mismatched import is a defect *of the target*, not of the thing imported.


| joint | what to check |
|---|---|
| **J-FAN4P** *(context)* | Lemma FAN-4': the residue mass `2nu - E` and the `C`-entries `L + e_c`. Re-derive the degree-sum bookkeeping yourself; the `p`-terms are supposed to cancel via `tau = p + L`. Check the FAN-1 and DICH(b) imports against their statements in Appendix A.1. What does the lemma say when `E = 0`? when `p = 0`? |
| **J-FAN8P** *(context)* | Lemma FAN-8': the escape bound `L <= 2nu - E`. Are the two subtracted sets disjoint and genuinely inside the block? Is the prefix inequality tie-safe? What does the lemma say at `E = 0` — is the hypothesis `E >= 1` doing work, or is it decoration? |
| **J-FAN6P** *(context)* | Lemma FAN-6' and its proof. Also the bracket listing which residues it kills: is that list right at its smallest cases? Is the zero-entry convention stated, and is it used consistently between FAN-6' and FAN-4'? |
| **J-GFAN2** *(context)* | Theorem GFAN2: Step 1's escape budget, Step 2's three `L >= 4` trajectories, and all eight `L = 3` rows. Simulate them yourself. Is the row list **complete** — is anything excluded that should not be? |
| **J-RIG1** *(context)* | Corollary RIG-1. It claims that Proposition L2 (a),(b) force `B_lo+ = empty` and that Theorem RIG then supplies the rest, **removing** a tightness argument from L2's own proof. Proposition L2 is printed in Appendix A.1: does the corollary use exactly clauses (a),(b), does it use them in the direction stated, and is the removal real or circular (does the shorter route secretly re-use the thing it claims to remove)? |
| **J-CORHC** *(TARGET for GFANnu-HC only; context for GFAN2-HC / GFAN2-L3)* | Corollaries GFAN2-HC, GFAN2-L3 and GFANnu-HC. Arithmetic and dependency only. GFAN2-HC's `L = 1` exclusion is claimed to follow from RIG's own `1 <= nu <= L-1` with no outside import — verify that, and verify that Corollary L1-short (printed in Appendix A.1) is genuinely **unused** anywhere in Appendix B. |
| **J-FIN** *(TARGET)* | Theorem GFANnu's finiteness argument. The split into `E=0 / L>=lam_1`, `E=0 / nu+1<=L<lam_1`, `E>=1` — disjoint? exhaustive? Is `lam_1 <= 2nu` justified? Does anything force `E <= nu-1`, and is it used consistently? Do the four imports match their statements? **And: is the quantifier range `1 <= nu <= 10` right — is the lower bound necessary, and is it sufficient?** |
| **J-SPEC** *(TARGET)* | Appendix C.1's five conventions. Are they sufficient to pin the enumerated set exactly? Is the unlabelled/multiset reduction legitimate? Is the zero-inertness claim true — test it. Is "no graphicality filter is needed" valid, and does its monotonicity run in the direction the conclusion needs? |
| **J-DATA** *(TARGET)* | The printed data. Recompute `s0(lam)` for the partitions of `2nu`, `nu <= 6`; check the boundary pair counts `0,1,3,7,14,26` and `45,75,120,187`; derive the closed form `S(nu)` yourself and check `0,3,24,110,397,1211` and `3340,8457,20126,45450`. Then **spot-check the survivor rosters**: pick rows from (C-5) and from (C-8), rebuild each from (C-1), and verify both that it survives and that its FAN-6' certificate holds — **and name the rows you checked**. A printed row that is not a survivor is a MATHEMATICS defect. Completeness of the rosters is asked of you **only if you ran code**; if you did, say what your run produced. |
| **J-KILL** *(TARGET)* | Lemma FAN-6' against every printed survivor. Watch the boundary certificates `(w, 2nd) = (4, 2)` and `(3, 1)`. |
| **J-IMPORT** *(TARGET)* | **The joint this round was rebuilt for.** For EVERY use of an Appendix A.1 fact anywhere in Appendix B or C: is the hypothesis the caller supplies the hypothesis the imported statement requires, and is the conclusion the caller uses the conclusion the imported statement proves? Do not referee the imports' own proofs — they are separately certified. A mismatched import IS in scope and IS a MATHEMATICS defect. Give a verdict per import, not one verdict for the joint. |
| **J-SCOPE** *(TARGET)* | For **Theorem GFANnu and Corollary GFANnu-HC**: what hypotheses does its own proof consume, versus what it is filed under? Report both under- and over-hypothesis. Under-hypothesis is a MATHEMATICS defect; over-hypothesis is bookkeeping. Watch for a scope note that *weakens* an import's hypotheses in passing — asserting that a cited lemma holds under less than it was proved under is an affirmative claim and needs a proof of its own. |

## Classify every defect

Tag each finding **MATHEMATICS** (a claim is false, a proof does not prove its
statement, an import does not match, an enumeration is incomplete or wrong, a
statement is used outside the hypotheses it was proved under) or **BOOKKEEPING**
(label, cross-reference, wording, a true statement stated imprecisely, a missing
convention a reader can supply uniquely). **State plainly in your verdict line whether
any MATHEMATICS defect was found.**

## Mandatory control section (a verdict without it does not count)

1. **Counterfactual availability.** Build a concrete instance that has the *shape* of
   an admissible configuration but **violates** one standing hypothesis — e.g. a
   `GFan`-shaped degree sequence failing `residue = alpha`, or a residue total not
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

## Verdict tags — use exactly one, PER TARGET STATEMENT

Give **two** verdict lines, one for Theorem GFANnu and one for Corollary GFANnu-HC, and
then the single overall `VERDICT:` line the report format asks for. A defect in one of
the two is not automatically a defect in the other, and a joint verdict that hides which
statement is affected cannot be scored.


`CLEAN` (no defect of either class) - `PARTIAL` (bookkeeping defects only, no
mathematics defect) - `GAP` (a proof obligation you could not verify, stated as such,
with what would settle it) - `REFUTED` (an explicit counterexample, printed in full).

**Reminder of the one rubric constraint, repeated here so it cannot be missed:** roster
completeness is an explicitly withdrawn obligation whose evidence is printed inline in
the scoring section, and it **may not be the sole ground of a `GAP`**. Every other
ground for a `GAP` stands untouched, and the withdrawal's own evidence is itself a live
target — attacking it is a defect report, not a `GAP`.

## Report format, and length caps

Open with the `EXECUTION ENVIRONMENT:` line, then a single `VERDICT:` line, then
`TEXT VERSION REVIEWED: w61_S3_GFAN_r20`. Then, in this order:

0. **the Section 0 held-out table** — five rows, H1...H5, each with its derivation in at
   most two lines. This comes before everything else;
1. the joint table — one verdict per named joint, **<= 40 words of justification each**;
2. the import table for J-IMPORT — one row per Appendix A.1 fact actually used, with
   the caller, the hypothesis match and the conclusion match, **<= 30 words each**;
3. the defect list — each with a MATHEMATICS/BOOKKEEPING tag, **<= 200 words each**;
4. the refutation log — what you tried and what it produced, with raw output;
5. the mandatory control section;
6. "What I could not check".

**Spend your length on 3 and 4, not on 1.** Do not restate the statements back to me;
do not summarise the brief; do not write an executive summary. A defect stated in
three lines with a printed witness is worth more than four pages of paraphrase.

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

### A.1 The imported facts — stated in full; do NOT referee their proofs

Each of these is separately certified. Your job with them is **import matching only**:
does the caller supply the hypothesis the statement requires, and does the caller use
only the conclusion the statement proves?

**Lemma 4.** In the hard-core frame, any two adjacent vertices of `B` have a common
A-neighbour. (Note the hypothesis: this is a statement *in the frame* — `A` maximum,
`f = alpha+1`, `G` connected and non-forest. Nothing in this document certifies a
version of Lemma 4 assuming `f = alpha+1` alone.)

**Observation R1.** In the frame, `diam(G) = 4` implies `B` is not a clique, hence
`nu >= 1`.

**Lemma C\*, (F-b).** The frame facts about occurring types: `T_1` and `T_2` are
disjoint type classes inside `B`, every cross pair in `T_1 x T_2` is non-adjacent
((F-b)), and a vertex of `T_1` or `T_2` has `deg_A >= 3` (Lemma C\*).

**Lemma S, Lemma Z+, Lemma F3', Theorem K, Theorem MB, Theorem SL, Theorem FAN,
Favaron-Maheo-Sacle (`residue <= alpha`).** The certified toolkit. Theorem FAN says
the whole `Fan(tau, L >= 2)` family is eliminated from the hard core. Theorem MB reads
`|B_lo+| + c + mbar <= (L - 1) + nu(B_lo)` where `c = |B_lo ∩ (T_1 ∪ T_2)|`; Theorem
SL's (LOW3) form reads `sum_{b in B_lo} deg_A(b) + mbar <= 2L + nu(B_lo) - 1`.

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

**Why FAN-1 is available on `GFan(τ,L,ν)`.** Every `c ∈ C` has `deg(c) = τ` exactly
(`b ∈ B_lo`: `(τ−1) + 1`; `a₀`: adjacent to all of `B` and nothing else), every
`w ∈ B_hi` has `deg(w) ≥ τ+1`, and every `a ∈ A′` has `deg(a) ≤ p < τ`. Hence
**Lemma FAN-1 applies word for word** (its proof uses only "the `B_hi` vertices are
the vertices of degree `≥ τ+1`" and DICH(c) for the rest): the heads of steps
`1 … p` are exactly `B_hi`.

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
> *(c)* Theorem MB is now tight, and **both** of the bounds its proof combines are
> re-run simultaneously at `L = 2`, `|B_lo⁺| = c = 0`, `m̄ = 1`, `ν(B_lo) = 0`:
> the degree count of Theorem MB gives the **lower** bound
> `Σ_{b∈B_lo} deg_A(b) ≥ L + |B_lo⁺| + c = 2`, while the (LOW3) form of Theorem SL
> gives the **upper** bound `Σ_{b∈B_lo} deg_A(b) ≤ 2L + ν(B_lo) − 1 − m̄ = 2`.
> The two meet, so `Σ_{b∈B_lo} deg_A(b) = 2`, i.e.
> `deg_A(b₁) = deg_A(b₂) = 1`. Since `b₁ ∼ b₂`, Lemma 4 supplies a common
> A-neighbour, which must be the unique A-neighbour of each; call it `a₀`. For
> every `w ∈ B∖{b₁}` the pair `(b₁,w)` is adjacent, so Lemma 4 gives a common
> A-neighbour, necessarily `a₀`; hence `a₀` is adjacent to all of B.
> *(e)* `deg(b_i) = (τ−1) + 1 = τ`, so
> `slack = 2(τ+1) − (2τ + ν) = 2τ + 2 − 2τ − 1 = 1`. ∎

> **Corollary L1-short.** The hard
> core has no `L = 1` case.
>
> *Proof.* `L = 1` gives `ν(B_lo) = 0`, so Theorem MB reads
> `|B_lo⁺| + c + m̄ ≤ 0`: the unique `b₀` is B-universal, `c = 0` and `m̄ = 0`.
> B-universality of `b₀` means no non-edge of B meets `b₀`, so `ν = m̄ = 0` and B
> is a **clique** — contradicting Observation R1. ∎

> **Corollary MB1 (a floor on L).** In the hard core, if every low vertex is
> B-universal then `ν = m̄ ≤ L − 1`, so `L ≥ ν + 1 ≥ 2`.
>
> *Proof.* B-universality of all of `B_lo` gives `ν(B_lo) = ν(B_lo,B_hi) = 0`,
> hence `ν = m̄`, and `c = 0` (a B-universal vertex has no non-neighbour, so it
> cannot lie in `T₁ ∪ T₂`). Theorem MB then reads `m̄ ≤ L − 1`; and `ν ≥ 1` by R1. ∎

**Lemma TAIL** is stated in Appendix C, where it is used.

---

## Appendix B — Part 1, the text under review

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
>
> *Minimal scope, separated bound by bound.* The **lower** bound `deg_A(b) ≥ 1` uses
> only that `A` is **maximal**: if `b` had no A-neighbour, `A ∪ {b}` would be
> independent, contradicting maximality — cardinality is never invoked. The **upper**
> bound `deg_A(b) ≤ n_b + 1` uses **neither** maximality nor maximum cardinality, only
> the definitions of `B_lo`, `τ` and `n_b`. So the lemma holds verbatim for any
> **maximal** independent set. The statement is left as "maximum" because every
> consumer in this document supplies a maximum `A` anyway and because `α = |A|` is used
> in the same breath. Corollary CAP1 inherits the same sharpening.
> 

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
need only: `A` a maximum independent set, plus **Lemma 4**; (d)
needs additionally `diam = 4` (Observation R1). So **(a)–(e) hold in the
hard-core frame, with no reductio**. Only the bound `ν ≤ L−1` needs the hard core
— and that is not a formality: see the measured witness in the companion section (not supplied).

### C. What it closes

> **Corollary RIG-1 (Proposition L2 without its tightness argument).** In the hard
> core with `L = 2`, Proposition L2 (a),(b) force `B_lo⁺ = ∅`; Theorem RIG then
> gives L2 (c) and the **configuration/numerical part** of L2 (d) directly, and
> `ν ≤ L−1 = 1` with `ν ≥ 1` gives `ν = m̄ = 1`, i.e. `Fan(τ,2)`.
>
> This **removes the tightness re-run** from Proposition L2(c) ("Theorem MB is now
> tight, and re-running its degree count … forces `Σ deg_A = 2`"). That step was
> the pre-declared failure mode **L-d** of the the certified toolkit error prior (dispatch file,
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
>
> *Two readings of the zero convention, separated, and only the second is used.*
> **(i)** *factual* — whenever `|A′|` exceeds the number of positive residues, real
> zero entries are present. **(ii)** *conventional* — for the purpose of the phrase
> "second-largest entry" in this lemma, a residue with a single positive part is read
> as having second-largest `0` **whether or not** a real zero entry is present.
> **(ii)** is the reading this lemma and every certificate in Appendix C.1 use. Nothing
> depends on which holds in a given instance: the lemma's operative content is "there
> is no entry equal to `w−1`", which for a single-part residue `[w]` with `w ≥ 2` is
> true under both readings, while `[1]` is excluded under both.
>
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
> 〔**Superseded by Corollary GFANν-HC of Appendix C**, which raises this to `ν ≥ 11`,
> `L ≥ 12`. Kept because its proof is the hand-written one.〕
>
> *Proof.* Theorem RIG (the certified toolkit) makes the instance `GFan(τ,L,ν)` with
> `1 ≤ ν ≤ L−1`; `ν = 1` is `Fan(τ,L)`, killed for `L ≥ 2` by **Theorem FAN**, and
> `ν = 2` is killed for `L ≥ 3` by **Theorem GFAN2**. `L = 1` cannot occur: RIG's own
> bound `1 ≤ ν ≤ L−1` already forces `L ≥ 2`. And `L = 2` forces `ν = 1`. So `ν ≥ 3`,
> whence `L ≥ ν + 1 ≥ 4`. ∎
> 

> **Corollary GFAN2-L3.** In the hard core with `L = 3`, **some low vertex is not
> B-universal** (`B_lo⁺ ≠ ∅`). Equivalently: the entire `L = 3` layer of the hard
> core lives in the residual regime mapped in the companion section (not supplied).

---

## Appendix C — Theorem GFANnu and its enumeration

### D. **Lemma TAIL, and the elimination of `GFan(τ,L,ν)` for every `ν ≤ 10`** (15:0x CDT)

Step 2 of Theorem GFAN2 used a trajectory that is uniform in `L`. That is not an
accident of `ν = 2`; it is a general reduction, and it turns the whole family into a
**finite** check for each `ν`.

> **Lemma TAIL.** Let `E = 0`, so the multiset at the start of step `p+1` is
> `[L]^{L+1} ∪ λ` with `λ` the `A′` residue, **`λ` non-empty**, `λ₁ := max λ`
> . If `L ≥ λ₁` then the
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

> **Theorem GFANν (`1 ≤ ν ≤ 10`).** For every `τ`, every `ν` with **`1 ≤ ν ≤ 10`** and
> every `L ≥ ν + 1`, there is **no** graph with the `GFan(τ,L,ν)` configuration
> satisfying `residue(G) = α(G)`.
>
> *Proof.* Four proved bounds make the case list finite for each `ν`:
> **FAN-4′** (the `A′` residue totals `2ν − E`, the `C`-part is `{L + e_c}` with
> `Σ e_c = E`), **FAN-8′** (`E ≥ 1 ⟹ L ≤ 2ν − E`, so `E ≥ 1` occurs only for the
> finitely many pairs `ν + 1 ≤ L ≤ 2ν − E`), **the theorem's own hypothesis
> `L ≥ ν + 1`** , and
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
> | 7 | none | 3 340 | none | ELIMINATED |
> | 8 | none | 8 457 | none | ELIMINATED |
> | 9 | none | 20 126 | none | ELIMINATED |
> | 10 | none | 45 450 | none | ELIMINATED |
>
> At `E = 0` **and `L ≥ λ₁`** — i.e. inside Lemma TAIL's range, where "clears in
> exactly `L` steps" is the `L`-free criterion `s₀(λ) = λ₁` — the **only** residue
> clearing in exactly `L` steps is the single part `[2ν]`, for every `1 ≤ ν ≤ 10`, and
> `[2ν]` is killed by FAN-6′. Outside that range the finitely many boundary rows
> `ν+1 ≤ L < λ₁` have their **own** survivors, tabulated in the certified toolkit (C-3), each with its
> own FAN-6′ certificate. ∎
>
> 〔**This is a computer-assisted proof**, and it is stated as such: the case list
> is finite *because* of FAN-4′/FAN-8′/TAIL and the theorem's own hypothesis
> `L ≥ ν + 1`, all hand-proved above.
> Within that finite list, every step **except the completeness of the `E ≥ 1`
> survivor roster** is now checkable by hand from Appendix C.1 alone; that single
> remaining step is a seconds-scale machine check over an explicitly specified,
> closed-form-counted finite set. `ν = 1` is Theorem FAN and `ν = 2` is Theorem
> GFAN2, both of which have complete hand proofs; `ν = 3…10` rest on the
> enumeration, which is printed in full in Appendix C.1 — `(C-2)`–`(C-5)` for
> `ν ≤ 6` and `(C-8)` for `ν = 7…10`.〕

> **Corollary GFANν-HC.** In the hard core, if every low vertex is B-universal then
> **`ν ≥ 11` and `L ≥ 12`**.
>
> *Proof.* Theorem RIG gives `GFan(τ,L,ν)` with **`1 ≤ ν ≤ L−1`** — the lower bound
> is RIG (d), i.e. Observation R1 — so `L ≥ ν+1`; Theorem GFANν eliminates every
> `ν` with `1 ≤ ν ≤ 10`, which by that lower bound is every `ν ≤ 10` available here. ∎
> 

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
