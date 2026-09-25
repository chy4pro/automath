# PREPARED AND HELD — erratum text and new-version diff for 10.5281/zenodo.22054651

**STATUS: PUBLISHED.** Task T010 (`orchestration/tasks/T010_zenodo_w61_newversion.md`), executed
2026-08-23 ~08:26-08:41 CDT with explicit user authorization (Zenodo confirmed logged in). A NEW
VERSION was published — **10.5281/zenodo.22069069** (Version v2, Aug 23, 2026) — carrying the
corrected PDF (`papers/wowii61/Partial-Results-WOWII-61-Graffiti-v2.pdf`, sha256
`ffacdeef3943a9b01adb088a0cf27be760625016466690ffdbe04d69ff810a4c`, md5 confirmed on-screen at
upload). **The original v1, 10.5281/zenodo.22054651, was NOT retracted or deleted and remains
citable** (per the absolute "never retract" rule). Title, authors, description and license were
left exactly as v1; the corrections are stated in a new "Additional Description" field (type
Notes) on the v2 record, covering: the C1-remark over-statement (§3 wording below used as the
base), the 340→332 graph-count fix, the Fact F-b unsupported clause removal, corrected status
markers, the abstract's τ≤3 over-claim, and a set of unsourced/wrongly-scoped figures replaced
with measured values. Framed throughout as a precision/accuracy correction — no theorem, no
certified row and no conclusion of the paper was withdrawn. Recorded in
`orchestration/watch_ledger.md`. The sections below are the ORIGINAL PLANNING DRAFT prepared
before this action; they are kept for the record and are no longer "held."

---

## 1. What is wrong, and how we know it is wrong *in the published artifact* and not merely in a source file

The published PDF (`papers/wowii61/main.pdf`, mtime 2026-08-22 02:23, the closeout-batch
build) carries, in the partial-progress remark on Conjecture C1 (item (iii)):

> "… so the general case is **reduced to a construction problem**."

**Machine-confirmed against the PDF itself, not inferred from the source.** The PDF's
content streams were decompressed and its text-showing operators concatenated; over that
text the string `reducedto` occurs **exactly once** and `constructionproblem` occurs
**exactly once**, in the same sentence. The repaired forms `sufficientcondition` and
`notareduction` occur **zero** times. Population: the whole document. So the published
artifact carries the over-read and does not carry the repair.

**Why it is an over-read.** The statement it summarises (Corollary C1-C in the working
ledger) is a **one-directional sufficiency**: C1 holds for a given λ *if* the padded list
admits a realization with independence number ≤ k. "Reduced to" asserts that exhibiting
such a graph is *the remaining work*, i.e. that the graph always exists. **It does not
always exist.** For odd `w ≥ 3` and `λ = (w,1)` no realization of `[w]^{w+2} ∪ [1]` has
independence number ≤ 2, while C1 is true there — so the "reduction" is unsatisfiable on an
infinite family of genuine instances. (Proved by hand; exhaustive over all 180 realizations
at `w = 3`; reproduced by a second, structurally different enumerator at `w = 3,5,7,9`; and
subsumed by the wider two-parameter criterion `w + 2 ≤ 3c`.)

## 2. Frame it accurately — this is an ACCURACY CORRECTION, not a retraction

* **No theorem changes.** The corollary itself is a sufficiency and it is **true**. What is
  withdrawn is a sentence about what remains to be done.
* **Nothing downstream rests on it.** The certified registry row R-22 rests on the seven
  Part-1 statements, not on this remark; every S3 status in the paper is exactly what its
  evidence supports.
* **The remark is already filed at the paper's weakest tier** ("hand proofs; never queued
  for review"), so no review-backed claim is affected.
* The paper's *conclusions* are unchanged. One sentence overstates the status of one route.

## 3. ERRATUM TEXT (drop-in, for a Zenodo "additional notes" field or a new-version front page)

> **Erratum (accuracy correction; no result is withdrawn).**
> In the remark recording partial progress on Conjecture C1, item (iii) reads "…so the
> general case is reduced to a construction problem." That is an over-statement. The
> condition given there — that the padded list admit a realization with independence number
> at most `k` — is **sufficient** for the conjecture at a given partition, in one direction
> only; it is **not** a reduction, because the required realization does not always exist.
> For every odd `w ≥ 3` and `λ = (w,1)`, no realization of `[w]^{w+2} ∪ [1]` has
> independence number at most `k = 2`, while the conjecture does hold at those `λ` by the
> two-part case proved in the same remark. More generally, for `k = 2` and `λ = (w,c)` a
> realization with independence number at most 2 requires `w + 2 ≤ 3c`.
> **No theorem, no certified row and no conclusion of the paper is affected**: the condition
> is a sufficiency and remains true, and the remark is filed at the paper's weakest tier.
> The corrected sentence reads: "…so the general case acquires a sufficient condition. That
> condition is not known to be satisfiable in general … It is therefore a sufficient
> condition and not a reduction."

## 4. NEW-VERSION DIFF (already applied to source; the PDF has not been rebuilt or uploaded)

`papers/wowii61/body.tex`, inside `\begin{remark}[partial progress on Conjecture~\ref{conj:C1}]`:

```diff
-at most $k$ --- so the general case is reduced to a construction problem. (iv) For $k \le 2$
+at most $k$ --- so the general case acquires a sufficient condition. That condition is
+not known to be satisfiable in general: for $\lambda = (w,1)$ with $w \ge 3$ odd, no
+realization with independence number at most $k$ exists, although $C1$ holds there.
+It is therefore a sufficient condition and not a reduction. (iv) For $k \le 2$
```

**Verification owed before any upload, and NOT yet done:** rebuild `main.pdf` from the
repaired source and re-run the same stream-decompression probe over the new PDF, asserting
`reducedto` → 0 occurrences and `notareduction` → 1. **A source repair is not a published
repair, which is the entire point of this file.**

## 5. The two options, stated neutrally for the user

| option | what it does | cost |
|---|---|---|
| **A. Zenodo "additional notes" erratum on the existing DOI** | The existing record keeps its DOI and gains the erratum text of §3. The PDF still carries the sentence. | Lowest effort. The artifact and its correction are one click apart but not in the same file. |
| **B. New version of the record** | Rebuild the PDF from the repaired source, upload as a new version. Zenodo mints a new version DOI under the same concept DOI; the old version stays citable. | Requires the §4 rebuild-and-verify step first. Cleanest, and it is what "the record should be right" means. |
| **C. Do nothing** | Defensible: no theorem is wrong, and the remark is at the weakest tier. | The published record keeps a sentence we know to be an over-read. |

**We do not recommend a choice here. It is the user's record and the user's name on it.**

---

# 6. PREPARED AND HELD — corrected wording for the v2 correction notice (owner-w61, r42)

**STATUS: PUBLISHED 2026-08-23 12:45 CDT.** The §6.4 replacement wording below (opening bookend,
item 4, closing bookend) was applied to `10.5281/zenodo.22069069` as a **metadata-only Edit of the
existing record** — no new version, no new PDF, no new DOI, file checksum unchanged
(`d87d994997a6d705e8bf5c2137a2706c`). This supersedes the original planner ruling below (which had
deferred this to "the next version, not a fourth release today") — the task that executed this was
dispatched as a metadata correction specifically, on the grounds that the bookends were false as
published (self-contradicting item 4) and the fix does not require a new file. See
`orchestration/watch_ledger.md` ("WOWII-61 v2 notice text — metadata correction") for the full
verification record and `orchestration/RESOURCES.md` (Chrome lease row `zenodo-notice-fix`) for the
execution log. Item 6's figure-count clause was left exactly as published (PENDING, not invented).
Original planner ruling, kept for the record: `orchestration/planner_msgs/cert_mirror_reconcile.md`
§4: *"fix with the next version, not a fourth release today"*, because item 4 does disclose the
re-tiering and the cost of the loose wording falls on us, not on a third party.

## 6.1 Provenance — what I read, and where it came from

- **The published notice was read from the Zenodo record itself**, not from any local file and not
  from another agent's transcription: `GET https://zenodo.org/api/records/22069069`,
  field `metadata.notes`, HTML stripped. That is the authority for the "before" text below.
- **The seven statements were identified in my own hand from the two PDFs**, by decompressing their
  content streams and reading Table 1 out of each:
  - `papers/wowii61/Partial-Results-WOWII-61-Graffiti-v2.pdf`, sha256
    `ffacdeef3943a9b01adb088a0cf27be760625016466690ffdbe04d69ff810a4c` — **matches the sha256 this
    file's §0 header records as the artifact uploaded as v2**, so this local file IS the published v2.
  - `papers/wowii61/main.pdf` (mtime 2026-08-22 02:23) — the v1 build, per §1 of this file.
  - Interpreter: `.venv/bin/python3` (pure stdlib `zlib`/`re`; neither sympy nor networkx involved).
- I did **not** take the seven names from `cert_mirror_reconcile.md` §3 or from
  `orchestration/watch_ledger.md`; I re-derived them and they agree with both.

## 6.2 What Table 1 actually says in each version — transcribed from the PDFs

`\034` is the `fi` ligature in the extracted stream text; expanded here.

| Table 1 entry | v1 (`main.pdf`) | v2 (published) |
|---|---|---|
| §4 `certified (rows R-1–R-5)` | Lemma 4.1, Lemma 4.2, **Lemma 4.3**, Lemma 4.4, Lemma 4.5, Theorem 4.6, Corollary 4.7 | Lemma 4.2, Lemma 4.4, Lemma 4.5, Theorem 4.6, Corollary 4.7 |
| §4 `elementary; full proofs given` | — (no such §4 entry) | **Lemma 4.1, Lemma 4.3** |
| §5 `certified (root-reduction block)` | **Lemma 5.1, Observation 5.2, Fact 5.3, Lemma 5.4** | **ENTRY ABSENT** |
| §5 `elementary; full proofs given` | — (no such §5 entry) | **Lemma 5.1, Observation 5.2, Fact 5.3, Lemma 5.4** |
| §6 `certified (row R-13)` | **Theorem 6.1**, Theorem 6.2 | Theorem 6.2 |
| §6 `elementary; full proof given` | — (no such §6 entry) | **Theorem 6.1** |

**Count: seven statements** — Lemma 4.1, Lemma 4.3, Lemma 5.1, Observation 5.2, Fact 5.3,
Lemma 5.4, Theorem 6.1. **Population: every row of Table 1 in both PDFs; no row excluded.**
No other Table 1 entry differs between the two versions.

### 6.3 ⚠️ A SHARPENING THE RULING SHOULD SEE BEFORE IT IS RE-AFFIRMED
`cert_mirror_reconcile.md` §3 allows that *"if 'certified row' meant Appendix-A registry rows the
statement may be defensible."* **On this evidence it is not defensible on either reading:**

1. **A certified row is literally gone.** The Table 1 entry `certified (root-reduction block)`
   exists in v1 and **does not exist in v2**. That is a certified row being removed, not a marker
   being adjusted.
2. **Two surviving registry-row entries changed coverage.** `certified (rows R-1–R-5)` no longer
   covers Lemma 4.1 or Lemma 4.3; `certified (row R-13)` no longer covers Theorem 6.1. The row
   identifiers persist; what they certify shrank.

So *"no certified row is affected"* is false under the Table-1 reading **and** under the
registry-row reading. **This is reported, not acted on** — `cert_mirror_reconcile.md` §4 keeps the
erratum path open *"if anything sharpens this"*, and whether it sharpens it enough to change the
ruling is the planner's call, not mine. **Nothing has been published.**

## 6.4 THE THREE REPLACEMENTS (drop-in, for the next version's notes field)

### (a) Opening bookend

> **BEFORE (published):** *"This version corrects a small number of imprecisions found after
> publication. No theorem, no certified result, and no conclusion of the paper is withdrawn or
> changed in substance."*

> **AFTER:**
> This version corrects six imprecisions found after publication. No theorem, no proof and no
> conclusion of the paper is withdrawn or changed in substance. Seven statements do, however, have
> their verification tier corrected **downward**: they are listed by name in item 4. Each of them
> remains in the paper with its full proof; what changes is the strength of the evidence claimed
> for it, not its content.

### (b) Item 4

> **BEFORE (published):** *"**4. Status markers.** A small number of status markers (e.g.
> 'certified') have been corrected to the tier that the paper's own evidence actually supports."*

> **AFTER:**
> **4. Verification tiers.** **Seven** statements are moved out of the "certified" tier into
> "elementary; full proof given", because that is the tier the paper's own evidence supports.
> They are **Lemma 4.1, Lemma 4.3, Lemma 5.1, Observation 5.2, Fact 5.3, Lemma 5.4 and
> Theorem 6.1**. In Table 1 this narrows the "certified (rows R-1–R-5)" entry, which no longer
> covers Lemma 4.1 or Lemma 4.3; narrows the "certified (row R-13)" entry, which no longer covers
> Theorem 6.1; and removes the "certified (root-reduction block)" entry entirely, its four
> statements having moved to the elementary tier. All seven statements, and their proofs, are
> unchanged.

### (c) Closing bookend

> **BEFORE (published):** *"No theorem, no certified row, and no conclusion of the paper is
> affected."*

> **AFTER:**
> No theorem, no proof and no conclusion of the paper is withdrawn or altered. The certification
> ledger **is** affected, in exactly the way item 4 sets out: seven statements are now recorded at
> a lower verification tier than version 1 recorded them at, and one Table 1 entry
> ("certified (root-reduction block)") is removed as a consequence. No statement is withdrawn.

## 6.5 One further loose phrase, flagged and NOT fixed — because fixing it needs a number I do not have

Item **6** of the published notice reads *"A small number of unsourced or wrongly-scoped figures
have been replaced with the correct measured values."* This is the same vague-quantifier shape the
ruling struck in item 4. **I have not counted them, so I am not writing a count: the replacement
figure is `PENDING`,** and it needs the v1/v2 figure diff before the next version ships. Naming it
here so it is not rediscovered a third time.

## 6.6 Discipline

- **Not published. Not uploaded. No Zenodo write of any kind was performed this round** — the only
  network call was the read-only `GET` in §6.1.
- The v1 record `10.5281/zenodo.22054651` and the v2 record `10.5281/zenodo.22069069` both remain
  citable and untouched. **Never retract** stands.
- Nothing about verification process, provenance, hashes, auditors or model families appears in any
  of the §6.4 replacement text — standing user directive; the published artifact stays plain.
