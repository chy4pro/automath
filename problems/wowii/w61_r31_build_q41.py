#!/usr/bin/env python3
"""
w61_r31_build_q41.py -- build prompts/w61_S3_C125_r31.md, the SS7.25 two-family brief.

ONE brief text, dispatched to TWO families (Qwen = Q41, Gemini = Q42).  Both
families are admissible on these six statements per the planner's r30 cert SS3.

WRITE-TIME GATES, every one of them positive-controlled against a deliberately
corrupted copy of the brief (a gate that cannot fire is not a gate):
  G1  the AH1 phrase "reduced to a construction" (and the whole "reduces C1 to"
      family) must NOT appear.
  G2  no "closes the ... S3 surface" variant, in English or Chinese, may appear.
  G3  no held-out answer may appear beside its own row's object.
  G4  no private email; no API key shape; no status leak of the form
      "PROVED-S3 / promoted / family 1 / family 2 / registry row".
  G5  the population/verdict schema is present and the six statements are all
      addressed by the verdict table (completeness asserted, not probed).

Self-limits with sys.exit on any failure.  Nothing is written unless all gates pass.
"""
import sys, re, hashlib
from pathlib import Path

ROOT = Path("$HOME/workspace/claudecode/automath")
OUT  = ROOT / "prompts/w61_S3_C125_r31.md"
KEYF = ROOT / "problems/wowii/w61_r31_heldout_key.txt"

KEY = {}
for line in KEYF.read_text().splitlines():
    if re.match(r"^[AB]\d = ", line):
        k, v = line.split(" = ")
        KEY[k] = v.strip()
assert set(KEY) == {"A1", "A2", "A3", "B1", "B2", "B3"}, KEY
print("key rows loaded : %s" % sorted(KEY))

BRIEF = r"""# Independent review task — six statements about a deletion process on integer lists

You are being asked to **review six short mathematical statements and their proofs**.
Everything you need is in this file. Do not look for context elsewhere; there is none
you are missing, and there is no "house style" you are expected to match.

**What we want from you.** For each of the six numbered statements: is the statement
**true as stated**, and does the **proof given below actually prove it**? Those are two
different questions and we want both answered separately. A true statement with a broken
proof is a finding we want. A proof that is fine but proves something narrower than the
statement claims is a finding we want. A statement that is simply false is the most
valuable finding of all and you should say so plainly.

**We are not asking you to be agreeable and we are not asking you to be harsh.** We are
asking you to be *specific*. "This step is unjustified" is worth little; "this step
assumes `c < w-1` but the recursion is applied at `c = w-1`" is worth a great deal.

---

## 0. The one thing we ask you NOT to do

Do not tell us what you think we want to hear about how promising the material is, and do
not grade the *writing*. Grade the mathematics.

**Refusals, and the direction each one refuses.** These are narrow and each names the
nearby thing that survives:

* **Refused: re-proving the imported theorem in section 1.4** (the residue/independence
  bound). It is an external result and we are not asking you to verify it.
  **Survives, and we want it:** telling us that we have *applied* it outside its
  hypotheses, or cited it for something it does not say.
* **Refused: replacing a proof with a different proof of the same statement.** We are not
  asking for better proofs.
  **Survives, and we want it:** saying that a given proof does not work *and why*, and (if
  you like) sketching what a correct argument would have to establish.
* **Refused: numerical evidence as a verdict.** "I checked ten cases and it held" is not
  an answer to "does this proof prove this statement".
  **Survives, and we want it:** a **counterexample**, which is a complete answer to the
  truth question and should be stated with the explicit list it is built from.

---

## 1. Definitions — self-contained, and the only place vocabulary is defined

### 1.1 Partitions

A **partition** `lambda = (lambda_1 >= lambda_2 >= ... >= lambda_k)` is a weakly
decreasing list of positive integers. `k` is its number of **parts**, `lambda_1` its
largest part, and `Sum(lambda)` the sum of its parts. We write `w := lambda_1` throughout.

### 1.2 The step process

Let `L` be a finite list of non-negative integers. **One step** of the process:

1. Sort `L` into weakly decreasing order.
2. Let `d` be the first entry (the **head**). If `d = 0` the list is **terminal** and the
   process stops.
3. **Delete** the head. Let `rest` be what remains.
4. If `d > len(rest)`, the process **aborts**.
5. Let the **block** be the first `d` entries of `rest` (in the sorted order). If any block
   entry is `0`, the process **aborts** (a step may never drive an entry negative).
6. Subtract `1` from every block entry. The result, together with the untouched remainder
   of `rest`, is the new list.

Each step therefore **deletes exactly one entry** and decrements `d` others.

`L` is a **step sequence** if repeated stepping reaches a terminal list without aborting.
For such an `L`:

* `steps(L)` := the number of steps performed;
* `residue(L)` := the number of entries **remaining** in the terminal list.

If the process aborts, both are undefined and we say `L` is not a step sequence.

### 1.3 The padded list and `s0`

For a partition `lambda` with `w = lambda_1`, define

> `M(lambda) := [w]^(w+1) + lambda`

— that is, `w+1` copies of the value `w`, followed by the parts of `lambda`. Note
`|M(lambda)| = (w+1) + k`. Define `s0(lambda) := steps(M(lambda))` when it exists.

**A fully worked example, given to you so that the definitions are unambiguous.** Take
`lambda = (2,1,1)`, so `w = 2`, `k = 3`, and `M = [2,2,2] + [2,1,1] = [2,2,2,2,1,1]`.

| step | list (sorted) | head `d` | block | result |
|---|---|---|---|---|
| 1 | `[2,2,2,2,1,1]` | `2` | the two leading `2`s | `[2,1,1,1,1]` |
| 2 | `[2,1,1,1,1]` | `2` | two of the `1`s | `[1,1,0,0]` |
| 3 | `[1,1,0,0]` | `1` | the remaining `1` | `[0,0,0]` |
| — | `[0,0,0]` | `0` | — | terminal |

So `steps(M) = 3` and `residue(M) = 3`, i.e. `s0((2,1,1)) = 3`.

**This example is disclosed on purpose**: you must be able to *use* these definitions, so
we hand you one instance with its answer. It is not part of anything held out below.

### 1.4 One imported theorem, stated at the import site

> **Imported (Favaron–Mahéo–Saclé).** For any finite list `d` of non-negative integers that
> is realizable as the degree sequence of a simple graph `G`, and for which the process
> above terminates, `residue(d) <= alpha(G)`, where `alpha(G)` is the size of a largest
> independent set of `G`.

We use this **only** in the direction printed: an upper bound on `residue` obtained from a
graph. **We are not asking you to prove it.** We *are* asking you to check that we have not
used it outside its hypotheses.

`alpha(G)` and `omega(G)` denote independence and clique number; `Gbar` is the complement.
A **realization** of a list `d` is a simple graph whose degree sequence is `d`.

---

## 2. The six statements

### Statement 1 — Lemma C1-A

> **Lemma C1-A.** For `w >= 0` write `T(w) := steps([w]^(w+2))`. Then **`T(w) = w` for
> even `w`**, and for **odd `w`** the list `[w]^(w+2)` is **not a step sequence**.
> Consequently `s0([2v]) = 2v = lambda_1` for every `v >= 1`.
>
> *Proof.* Let `w >= 2` and start from `[w]^(w+2)`. **Step 1:** the head is `w`; the
> remaining `w+1` entries all equal `w`, so the block — the top `w` of them — is `w` copies
> of `w`, which become `w-1`, and one copy of `w` is left untouched. The list is now
> `[w]^1 + [w-1]^w`, of size `w+1`. **Step 2:** the head is that lone `w`; the remaining `w`
> entries all equal `w-1`, so the block is **all** of them (there are exactly `w`, as the
> head demands) and they become `w-2`. The list is now `[w-2]^w = [w-2]^((w-2)+2)`. Both
> steps are legal precisely when `w >= 2` (step 2 needs `w-1 >= 1`). Hence
> `T(w) = 2 + T(w-2)` for `w >= 2`. The base cases: `T(0) = 0`, since `[0]^2` has head `0`;
> and `T(1)` is undefined, since `[1]^3 -> [1,0]` — one step deletes the head **and**
> decrements one entry, so a three-entry list has a **two**-entry image — and the next step
> has head `1` with only a zero available, which would drive a zero entry negative.
> Induction on the parity classes gives `T(w) = w` for even `w` and abortion for odd `w`.
> Finally `[lambda_1]^(lambda_1+1) + [2v]` at `lambda = [2v]` **is** `[2v]^(2v+2)`, so
> `s0([2v]) = T(2v) = 2v`. ∎

### Statement 2 — Lemma C1-A′

> **Lemma C1-A′.** `V(c) := steps([c]^(c+3)) = c + 1` for every `c >= 1`.
>
> *Proof.* Write `W(t) := [t]^2 + [t-1]^t`. **Step 1:** from `[c]^(c+3)` the head is `c` and
> the block is `c` of the `c+2` remaining copies, leaving `[c]^2 + [c-1]^c` — which **is**
> `W(c)`. **The shape reproduces itself:** for every `t >= 1` the head of `W(t)` is `t`, the
> rest is `[t]^1 + [t-1]^t` of size `t+1`, the block is its top `t` entries
> `[t]^1 + [t-1]^(t-1)`, which become `[t-1]^1 + [t-2]^(t-1)`, and one `t-1` stays outside,
> giving `W(t-1)` (at `t = 1` the exponent `t-1` is `0`, so no entry of value `t-2` is ever
> created). `W(0) = [0]^2` has head `0` and is terminal. So the run is **one** step down to
> `W(c)` and then **`c`** steps down to `W(0)`: `V(c) = 1 + c`. ∎

### Statement 3 — Proposition C1-B

> **Proposition C1-B.** Let `lambda` have `k` parts and `lambda_1 = w`, and let
> `M := M(lambda) = [w]^(w+1) + lambda`. Then, whenever the process on `M` terminates,
> **`s0(lambda) = w  <==>  residue(M) = k + 1`**, and more generally
> `s0(lambda) = (w + 1 + k) - residue(M)`.
>
> *Proof.* `residue` is by definition the number of entries remaining when the head reaches
> `0`, and each step deletes exactly one entry, so `steps(M) = |M| - residue(M)` for every
> terminating `M`. Here `|M| = (w+1) + k`. ∎

### Statement 4 — Corollary C1-C

> **Corollary C1-C.** Let `lambda` have `k` parts and let `M = M(lambda)` terminate. If `M`
> has a realization `G` with `alpha(G) <= k`, then `s0(lambda) != lambda_1`.
>
> *Proof.* The imported bound of section 1.4 gives `residue(M) <= alpha(G)` for every graph
> `G` realizing `M`. If `alpha(G) <= k` then `residue(M) <= k < k+1`, so
> `s0(lambda) != w` by Proposition C1-B. ∎

**A note on what this corollary is and is not, which we state because it is the joint we
most want scrutinised.** It is a **sufficient condition**, in one direction only. It
converts the question for a *given* `lambda` into the question of whether a *particular
graph exists*, and Statement 6 below shows that for an infinite set of `lambda` **that
graph does not exist**. So we make no claim that this corollary settles the general
question, and if you find us using it as though it did, anywhere in this file, that is
exactly the kind of defect we are asking you to report.

### Statement 5 — Theorem C1-2

> **Theorem C1-2.** Let `lambda = (w, c)` with `1 <= c <= w`. Then `M(lambda)` is a step
> sequence **iff `w + c` is even**, and in that case **`s0(lambda) = w + 1 = lambda_1 + 1`**.
>
> *Proof.* Write `U(w,c) := steps([w]^(w+2) + [c])` — this is `s0((w,c))`, since
> `[w]^(w+1) + (w,c) = [w]^(w+2) + [c]`. **Recursion.** Suppose `c <= w-2`. Step 1: the head
> is `w`, and among the `w+1` remaining copies of `w` together with `c < w` the top `w` are
> all `w`s, so the list becomes `[w]^1 + [w-1]^w + [c]`. Step 2: the head is that lone `w`;
> the rest is `[w-1]^w + [c]` of size `w+1`, and since `c < w-1` its top `w` entries are
> exactly the `w` copies of `w-1`, which become `w-2`. The list is `[w-2]^((w-2)+2) + [c]`.
> Hence **`U(w,c) = 2 + U(w-2,c)` for `c <= w-2`**. **Base.**
> `U(c,c) = steps([c]^(c+2) + [c]) = steps([c]^(c+3)) = c+1` by Lemma C1-A′. **Parity.** A
> completed run satisfies `Sum(M) = 2 * Sum(heads)`, so `Sum(M)` must be even; here
> `Sum(M) = w(w+2) + c`, which is even exactly when `w + c` is (both parities of `w`
> checked). When `w = c (mod 2)` the recursion descends in steps of `2` from `w` to the base
> at `c`, giving `U(w,c) = 2*(w-c)/2 + (c+1) = w + 1`. When `w != c (mod 2)` the sum is odd
> and no completed run exists. ∎

### Statement 6 — Observation C1-G

> **Observation C1-G.** Let `k = 2` and `lambda = (w, c)` with `w >= c >= 1` and `w + c`
> even. If `M(lambda)` has a realization with `alpha <= 2`, then **`w + 2 <= 3c`**.
>
> *Proof.* `M = [w]^(w+2) + [c]` has `N = w + 3` entries, so a realization `G` has `N`
> vertices and the complement `Gbar` has degree sequence `[2]^(w+2) + [w+2-c]`:
> each vertex of `G`-degree `w` has `Gbar`-degree `(N-1) - w = 2`, and the vertex of
> `G`-degree `c` has `Gbar`-degree `(N-1) - c = w+2-c`. Now `alpha(G) <= 2` iff `Gbar` is
> triangle-free. Let `u` be the vertex of `Gbar`-degree `D0 := w+2-c`. Triangle-freeness
> makes `N(u)` independent in `Gbar`, so each of its `D0` vertices — all of `Gbar`-degree
> `2` — spends its one remaining edge outside `{u} + N(u)`. That set has
> `N - 1 - D0 = c` vertices, each of `Gbar`-degree `2`, so it absorbs at most `2c` edge-ends.
> Hence `D0 <= 2c`, i.e. `w + 2 <= 3c`. ∎
>
> **Corollary (the instance that matters).** For odd `w >= 3` and `lambda = (w,1)` the
> condition reads `w + 2 <= 3`, which fails. So **no** realization of `M((w,1))` has
> `alpha <= 2 = k`, and Corollary C1-C's hypothesis is unsatisfiable on an infinite family.

**Stated exactly, because we will not overstate it:** Observation C1-G is a **necessary**
condition only. Whether `w + 2 <= 3c` is also **sufficient** for such a realization to
exist is **open**, we have not proved it, and we are not asking you to assume it.

---

## 3. The background conjecture, so you know what the statements are for

> **Conjecture C1.** For every `v >= 1` and every partition `lambda` of `2v` other than the
> single part `[2v]`, `s0(lambda) != lambda_1`.

Statement 5 settles the case `k = 2` and Statement 1 handles the excluded single part; the
case `k >= 3` is open. C1 has been machine-checked with no violation found over every
`lambda` whose padded list terminates and whose sum is at most `36`. **We do not offer that
as a proof and we do not print the case counts here**; more cases is not a proof.

**Nothing in section 3 is a statement you are asked to grade.** It is here so that you can
tell whether a proof in section 2 quietly assumes the conjecture it is supposed to support.

---

## 4. Held-out table — MANDATORY, and read the grading rules before you answer

This section exists because we cannot tell, from a fluent review alone, whether a reviewer
computed anything. Six rows. **Answer every one.**

**`CANNOT COMPUTE` is a first-class answer and is graded as clean.** If you cannot or will
not run the process far enough to be sure of a row, write **`CANNOT COMPUTE`** for that row.
That costs you nothing. **A wrong confident number costs you a great deal.** Do not guess.

**Grading, pre-registered here before we see your answer:**

* Rows **A1–A3** are derivable by hand from section 1 alone. **A wrong answer on any A row
  voids the whole report**, because it means the definitions were not applied.
  `CANNOT COMPUTE` on an A row is not a void; it is a declined row.
* Rows **B1–B3** need real computation. `CANNOT COMPUTE` on a B row is **clean**. A wrong
  confident answer on a B row is a **traced downgrade**: we locate it and discount the parts
  of your review that depend on it. **All three B rows wrong with the hatch unused is a
  void.**
* Every row is independent of every other. No row's answer can be deduced from another's.
* **The table grades non-fabrication, not correctness.** Passing it is not a licence and we
  will not treat it as one.

| row | question |
|---|---|
| **A1** | Compute `s0((6,4,2))`, i.e. `steps` of `[6]^7 + [6,4,2]`. Give one integer. |
| **A2** | Compute `residue(M((5,4,3)))`, i.e. the residue of `[5]^6 + [5,4,3]`. Give one integer. |
| **A3** | Compute `steps([4,4,3,3,2,2])` for that explicit six-entry list. Give one integer. |
| **B1** | Over **all** simple graphs realizing the list `[2,2,2,2,2,1,1]`, what is the **minimum** of `alpha(G)`? Give one integer. |
| **B2** | Among the partitions `lambda` of `20` with at least two parts whose padded list `M(lambda)` terminates, how many satisfy `residue(M(lambda)) = k`? Give one integer. |
| **B3** | Among the partitions `lambda` of `22` with at least two parts whose padded list `M(lambda)` terminates, how many satisfy `s0(lambda) = lambda_1 + 2`? Give one integer. |

---

## 5. What to send back

**Part 1 — the six verdicts.** One row per statement, in this exact shape:

| statement | statement TRUE? | proof VALID? | defect class | one-sentence reason |
|---|---|---|---|---|

* **statement TRUE?** — `TRUE` / `FALSE` / `UNDECIDED-BY-ME`.
* **proof VALID?** — `VALID` / `GAP` / `BROKEN`.
  `GAP` = a step is unjustified but repairable as far as you can see. `BROKEN` = the proof
  cannot be repaired without a new idea, or proves something else.
* **defect class** — `MATHEMATICS` (the argument is wrong or incomplete), `SCOPE` (the proof
  proves a narrower or different statement than the one displayed), `BOOKKEEPING` (a printed
  intermediate, index, or arithmetic slip that does not affect the conclusion), or `NONE`.

**Part 2 — the findings themselves.** For each non-`NONE` row, the specific sentence or
step, quoted, and what is wrong with it. Order them by how much they matter.

**Part 3 — the held-out table.** Six rows, answers only.

**Part 4 — one paragraph: what is the weakest joint in this file?** Not necessarily a
defect — the place where, if you had to bet on something being wrong, you would bet.

**Please do not** open with a summary of what the file says. We wrote it; we know. Start at
Part 1.
"""

# ============================================================ WRITE-TIME GATES
FAILED = []

def gate(name, fn, must_fire_on):
    """fn(text) -> list of offending strings.  Runs on the real brief (must be
    empty) AND on a corrupted copy (must be non-empty)."""
    real = fn(BRIEF)
    ctrl = fn(must_fire_on)
    ok_real = (len(real) == 0)
    ok_ctrl = (len(ctrl) > 0)
    print("   %-28s brief: %d hit(s) %-6s | positive control: %d hit(s) %s"
          % (name, len(real), "OK" if ok_real else "** FAIL",
             len(ctrl), "OK (gate is live)" if ok_ctrl else "** DEAD GATE"))
    if real:
        for h in real[:6]:
            print("        offending: %r" % (h,))
    if not (ok_real and ok_ctrl):
        FAILED.append(name)

print()
print("=" * 78)
print("WRITE-TIME GATES  (each shown firing on a corrupted copy before being trusted)")
print("=" * 78)
print("   brief population : %d chars, %d lines, %d statement blocks"
      % (len(BRIEF), BRIEF.count("\n"), len(re.findall(r"^### Statement \d", BRIEF, re.M))))

# --- G1: the AH1 over-read
G1_PAT = re.compile(r"reduc\w*\s+(?:to|by)\s+a?\s*construction|reduces\s+C1|"
                    r"reduction of C1|reduced to an independence", re.I)
gate("G1 AH1 'reduced to'", lambda t: G1_PAT.findall(t),
     BRIEF + "\nC1's general case is reduced to a construction problem.\n")

# --- G2: the AH3 closure over-claim, EN and ZH
G2_PAT = re.compile(r"clos\w*\s+(?:the\s+)?(?:entire\s+)?S3\s+surface|"
                    r"S3\s+surface\s+(?:of\s+\w+\s+)?clos|only thing between|"
                    r"唯一残余|只差一个族轮", re.I)
gate("G2 AH3 closure claim", lambda t: G2_PAT.findall(t),
     BRIEF + "\nThis is the round that closes the S3 surface.\n")

# --- G3: held-out answers must not stand beside their row's object
def g3(t):
    hits = []
    probes = {
        "A1": (r"s0\(\(6,\s*4,\s*2\)\)\s*=\s*" + KEY["A1"], "s0((6,4,2)) = %s" % KEY["A1"]),
        "A2": (r"residue\(M\(\(5,\s*4,\s*3\)\)\)\s*=\s*" + KEY["A2"], "residue(M((5,4,3))) = %s" % KEY["A2"]),
        "A3": (r"steps\(\[4,\s*4,\s*3,\s*3,\s*2,\s*2\]\)\s*=\s*" + KEY["A3"], "steps([4,4,3,3,2,2]) = %s" % KEY["A3"]),
        "B1": (r"minimum of `?alpha[^\n]{0,24}=\s*" + KEY["B1"], "minimum of alpha = %s" % KEY["B1"]),
        "B2": (r"residue\(M\(lambda\)\)\s*=\s*k[^\n]{0,20}\b" + KEY["B2"] + r"\b", "residue(M(lambda)) = k ... %s" % KEY["B2"]),
        "B3": (r"lambda_1 \+ 2[^\n]{0,20}\b" + KEY["B3"] + r"\b", "lambda_1 + 2 ... %s" % KEY["B3"]),
    }
    for row, (pat, _) in probes.items():
        for m in re.findall(pat, t, re.I):
            hits.append("%s: %s" % (row, m))
    return hits
CORRUPT3 = BRIEF + "\n\ns0((6,4,2)) = %s\nresidue(M((5,4,3))) = %s\n" % (KEY["A1"], KEY["A2"])
gate("G3 held-out answer leak", g3, CORRUPT3)

# --- G4: private identity / status leak
# the private local-part is CONSTRUCTED, never written literally, so this script is
# not itself an artifact carrying it.  Liveness is proved by the positive control below.
_PRIV = "chen" + "haoyu" + "1995"
G4_PAT = re.compile(_PRIV + r"|sk-[A-Za-z0-9]{8,}|PROVED-S3|registry row|"
                    r"family\s+[12]\b|promot(?:e|ed|ion)|planner|owner-w61|"
                    r"round\s+3[01]\b", re.I)
gate("G4 identity/status leak", lambda t: G4_PAT.findall(t),
     BRIEF + "\nThis is family 2 and it promotes the statement to PROVED-S3.\n"
           + "\ncontact: " + _PRIV + "@example.invalid\n")

# --- G5: completeness of the verdict surface, asserted not probed
def g5(t):
    missing = []
    for nm in ("Lemma C1-A.", "Lemma C1-A′", "Proposition C1-B", "Corollary C1-C",
               "Theorem C1-2", "Observation C1-G"):
        if t.count(nm) == 0:
            missing.append("statement absent: " + nm)
    for row in ("A1", "A2", "A3", "B1", "B2", "B3"):
        if t.count("**%s**" % row) == 0:
            missing.append("held-out row absent: " + row)
    for tok in ("CANNOT COMPUTE", "statement TRUE?", "proof VALID?", "defect class"):
        if tok not in t:
            missing.append("schema token absent: " + tok)
    # population contiguity: the six statement headings must be 1..6 with no gap
    nums = [int(x) for x in re.findall(r"^### Statement (\d)", t, re.M)]
    if nums != list(range(1, 7)):
        missing.append("statement numbering not contiguous 1..6: %s" % nums)
    return missing
gate("G5 schema completeness", g5, BRIEF.replace("### Statement 4", "### Statement 9"))

print()
if FAILED:
    print("!! GATES FAILED: %s -- NOTHING WRITTEN.  exit(2)" % FAILED)
    sys.exit(2)

OUT.write_text(BRIEF)
h = hashlib.sha256(BRIEF.encode()).hexdigest()
print("=" * 78)
print("WROTE %s" % OUT)
print("   chars (code points) : %d" % len(BRIEF))
print("   bytes               : %d" % len(BRIEF.encode()))
print("   sha256              : %s" % h)
print("   tail (last 2 lines) : %r" % BRIEF.strip().splitlines()[-1])
print("=" * 78)
