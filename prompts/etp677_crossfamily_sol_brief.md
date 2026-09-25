# CROSS-FAMILY VERIFICATION TASK — ETP-677 structure paper (10.5281/zenodo.22054879)

## Your role

You are an independent verifier reading a mathematics paper end-to-end and taking
**responsibility** for it, not producing a stylistic opinion. You are from a different
model family than whoever drafted this paper, which is exactly why you were asked: the
project's rule is that a paper is only trusted after a reviewer from a genuinely different
model family has read it and signed a verification note.

You are **not** a solver, **not** a co-author, and you are **not being asked to fix
anything**. Do not attempt to correct, patch, strengthen, or complete any claim you flag —
report only. This is explicitly a partial-results paper (it does not resolve the main
conjecture) and says so in its own abstract; do not flag a statement merely for being
partial. Judge each individual statement on whether **its own claimed status matches its
own evidence**, not on whether the paper resolves the full open problem.

This note is an **internal audit artifact**. It will not be published, will not ship with
the paper, and no one will see your working process except the team running this check —
so there is no reason to soften a finding for presentation. State exactly what you found.

You have a real shell and file-system access to this repository
(`~/workspace/claudecode/automath`, which is your current working directory). Use it: open
files yourself rather than working from summary, and where a claim rests on a Python
script, actually run the script and report what you observed, rather than accepting a
description of what it would output as a substitute for running it, whenever running it is
feasible in reasonable time. If a script is too expensive to run to completion, say so
explicitly and explain what you did instead (e.g. re-derive a smaller sub-case by hand, or
inspect the script logic and its already-existing `.out` file critically rather than
trusting it blindly).

## The paper

Primary source, read directly from disk (do not ask for it to be pasted — open it
yourself with your own tools; it is long, about 450KB / 8000 lines, so read it in sections
rather than trying to load it all into one view):

- `papers/etp677_structure/main.tex` — the complete LaTeX source. This is the paper.
- `papers/etp677_structure/main.pdf` — the compiled, rendered form of the same text, if you
  want to see it typeset.

Near the top of `main.tex` there is a verification-status marker block (search for
`\newcommand{\statusbox}` and the macros defined right after it, e.g. `\CONJ`, and similar
— read the surrounding comment block, which explains what each status marker asserts and
what evidence tier it corresponds to). Every numbered assertion (theorem / lemma /
proposition / corollary / observation / fact) in the paper carries one of these markers;
definitions, open problems and the conjecture itself carry none.

Near the end of `main.tex` there is a section titled "Verification artefacts" (search
`\section{Verification artefacts}`) — a long table mapping specific evidence files under
`problems/etp677/` to the specific theorems/propositions/lemmas each one establishes. This
table is your map for tasks 1 and 2 below.

The bibliography (`\begin{thebibliography}` block, 41 `\bibitem` entries) is near the very
end of the file, after the verification-artefacts table.

## What you must do

Work through the **entire** paper — do not sample. For each of the following three tasks,
be exhaustive, not illustrative: list every instance you found, not a representative
handful.

### 1. Every citation

For **all 41** `\bibitem` entries in the bibliography, open the source and confirm it
**actually says what the paper attributes to it**. Existence is not enough: a citation can
resolve to a real object and still be misattributed, over-cited, or cited for more than it
supports. Of these 41, only a small minority carry a machine-resolvable identifier (arXiv
id, DOI) you can check by fetching the source directly if you have network/web access; the
rest are prose citations to books, papers, or named results that you must check by what you
already know of the literature, or by any web access you have, or — failing that — by
flagging exactly what about them you could not independently confirm. Also check every
*internal* citation to an evidence artefact: where the paper's own "Verification artefacts"
table (or inline text) names a file under `problems/etp677/` as the source of a number or a
claim, open that specific file (per the read-restriction rule in the next section) and
confirm it actually computes what the paper says it computes.

Sign off on **every citation**, one line each, with exactly one of:
`resolved | says-what-we-claim | MISATTRIBUTED | COULD-NOT-OPEN`. Enumerate the full list —
do not summarize a sample.

### 2. Load-bearing numbers only

A load-bearing number is a **count, bound, size, population, or rate** that the paper's
argument or a claimed conclusion actually depends on — e.g. a count of models checked, a
count of cases in a case split, a count of graph/magma instances enumerated, a percentage
or fraction of a search space covered, an explicit numeric bound. This does **not** include
years, section/theorem/equation numbers, or standard mathematical constants.

For every load-bearing number you find, **re-derive it independently** using the evidence
artefact the paper cites for it (re-run the script yourself if you can execute Python —
state that you did and report the actual output — or hand-recompute from first principles
if it is small enough, stating which method you used). **Critically, for each number also
ask: what exact population was this number measured on, and does the sentence carrying the
number correctly name that population?** A number can be a real, correctly-computed
measurement and still be a defect if the surrounding sentence describes a different (larger,
smaller, or differently-scoped) population than what was actually measured — this is a
distinct failure from the number simply being wrong, and it is at least as important to
catch.

Report, per number: the paper's claimed value, the population the sentence claims it
covers, what you independently got and on what population, and a verdict of
`MATCH / MISMATCH / POPULATION-MISMATCH / COULD-NOT-REDERIVE`. Enumerate all of them; do
not sample.

### 3. Claim wording versus evidence status, per statement

For **every** numbered statement in the paper (theorem/lemma/proposition/corollary/
observation/fact/conjecture):

- Check that the status marker attached to it (the `\CONJ{...}`-style box, or whichever
  markers the paper defines — see the block near the top described above) matches what the
  statement's own proof, as actually written in the paper, delivers.
- Check the **verb** the surrounding prose uses about each statement (proved / shown /
  established / follows / reduces to / implies / settles / eliminates / closed / etc.)
  against what the statement's own proof, as given, actually supports. Flag any claim whose
  verb exceeds its support.
- **Cross-check every status marker against `problems/etp677/campaign_registry.md`**, which
  is this campaign's own status-authority ledger (a running research log). For any marker
  that claims a specific verification round, review pass, or ledger entry backs a
  statement, find the corresponding row/entry in `campaign_registry.md` and confirm it
  **actually names that specific statement** (not a same-family cousin, not a differently
  scoped version of it, not nothing at all). A marker that cites a ledger row which does not
  exist, or exists but is about a different statement, is a defect.
- **Give special scrutiny to any place where an implication is reported as though it were a
  settled conclusion** — i.e., where the text has established "A and B together would imply
  C" (a conditional), but a nearby sentence, remark, abstract line, or table entry then
  states or treats C itself as established, when C's own status has not actually been
  separately nailed down. Hunt for this shape throughout the whole document — the abstract,
  every summary table, every closing remark of every section — since summarizing prose is
  exactly where an implication is most likely to get silently upgraded into a conclusion.

List every claim you flag: quote the exact passage, name which of these problems it has,
and explain briefly why the wording exceeds (or falls short of) its support.

### 4. Report what you could NOT verify

Be explicit and itemized: no web access for an external reference, a script too expensive
to actually re-run in full, an ambiguous notation you could not pin down, a claim whose
evidence file was not locatable or not permitted under the read restriction below, etc. The
scope of your note is part of the note — an unqualified "everything checks out" is not an
acceptable substitute for saying exactly what you did and did not manage to check.

## Read restriction — read this carefully before opening anything

This is a genuine, independent-engagement review: nobody is handing you an answer key, and
the project has deliberately withheld its own prior review notes so that whatever you find
is your own. To keep that clean, you may open:

(a) `papers/etp677_structure/main.tex` and `papers/etp677_structure/main.pdf` — the paper
    itself, in full;
(b) `problems/etp677/campaign_registry.md` — the status-authority ledger described in task
    3 above. It is long (~7000 lines); use it primarily to look up the specific rows a
    status marker names, not as a source you read cover to cover. Nothing in it should be
    treated as a defect list about *this verification task* — it is the campaign's own
    working research log, not a review of your work;
(c) any file directly under `problems/etp677/` (in any subdirectory) **whose filename is
    explicitly named in the paper's own "Verification artefacts" table** (or named inline
    in the paper's running text as the source of a specific claim) — open or run these
    ONLY to re-derive the specific number/claim the paper attaches to that filename.

`problems/etp677/` contains several hundred files, and a good number of them are **not**
evidence artefacts the paper cites — they are the campaign's own internal review/audit
scaffolding (filenames containing things like `adjudicate`, `dispatch`, `audit`, `gap`,
`heldout`, `review`, `predispatch`, `payload`). Do **not** open any file under
`problems/etp677/` whose name is not the exact filename the paper cites, even if it looks
related or tempting — in particular avoid anything with `adjudicate`, `dispatch`, `audit`,
`heldout`, `review`, `predispatch`, `payload`, `harvest`, `erratum`, `crossfamily`,
`findings`, or `defect` in its name. These are not evidence; several of them are exactly
the kind of internal review material this task is designed to keep held out from you.

Do **not** open, list, or grep anything under `orchestration/` or `notes/` at all, for any
reason — these directories hold this project's own prior review notes, audit findings, and
process scaffolding, and reading any of them would defeat the purpose of this check. If
completing a task above seems to require reading something in one of these places, do not
open it — mark that specific check `COULD-NOT-VERIFY` and say why.

If you are unsure whether a file is in-scope, treat it as out of scope and note that you
skipped it and why, rather than opening it to check.

## Deliverable

Write your complete verification note to `problems/etp677/crossfamily_r1_note.md`.

Open the note with exactly this line, filled in:

> Verified by \<your model family/name\>, \<today's date\>. N citations opened, M
> load-bearing numbers re-derived.

Then include, in full:

- **Findings** — every flagged claim (species: MISATTRIBUTED CITATION / UNRESOLVABLE
  CITATION / UNSOURCED NUMBER / POPULATION-MISMATCHED NUMBER / UNEXECUTED VERIFICATION
  CLAIM / CLAIM EXCEEDS EVIDENCE / STATUS MARKER WITHOUT MATCHING LEDGER ROW / IMPLICATION
  REPORTED AS CONCLUSION / other — name the closest fit, or say "none of the above" and
  describe it), quote, and explanation.
- **Could not verify** — the explicit itemized list from task 4 above.
- **Per-citation table** — all 41 citations, one row each, per the format in task 1.
- **Per-number table** — every load-bearing number, one row each, per the format in task 2.

If you truly find nothing wrong anywhere, say so plainly and explain what you actually
checked to reach that conclusion — a clean verdict with no visible work is worth nothing to
the team relying on this note.

Take the time this deserves. This is a responsibility-bearing pass over the largest thing
this campaign has published, not a speed exercise.
