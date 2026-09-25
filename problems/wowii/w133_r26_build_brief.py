#!/usr/bin/env python3
"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!  UNSAFE TO RE-RUN.  DO NOT USE THIS FILE TO BUILD A BRIEF.                    !!
!!                                                                              !!
!!  Marked unsafe by owner-w133 round 29 on the planner's ruling                 !!
!!  (`orchestration/planner_msgs/cert_w133_r28.md` section 3, RULING CV third    !!
!!  instance).  It is marked HERE, in the file, and not only in the ledger,      !!
!!  because the next person to re-run it will not have read a cert.              !!
!!                                                                              !!
!!  WHY.  This builder cuts the three link texts out of the draft at THREE       !!
!!  HARD-CODED LINE RANGES -- draft(4592,4717), draft(4793,4897), draft(5005,    !!
!!  5093).  Round 27 entered an in-place correction to section 36 ABOVE them.    !!
!!  Section 35's range still coincides with its anchor; section 36's and         !!
!!  section 37's DO NOT.  draft(5005,5093) now begins on a blank line and        !!
!!  TRUNCATES SECTION 37's TAIL: re-running this file today yields a brief       !!
!!  SILENTLY MISSING 8 LINES OF THE LINK WHERE THE CHAIN CLOSES.  Nothing about  !!
!!  the failure is visible in the output -- the brief still looks complete.      !!
!!                                                                              !!
!!  WHAT IS AND IS NOT AFFECTED.  The r26 DISPATCH is unaffected: the shipped    !!
!!  bytes (automath-sandbox/briefs/w133_r26_chain.md) are frozen and were        !!
!!  correct at build time.  It is the INSTRUMENT that is no longer safe.         !!
!!                                                                              !!
!!  USE INSTEAD: problems/wowii/w133_r29_build_q41.py, which cuts at SECTION     !!
!!  ANCHORS ("## 35.1 The statement", "## 36.1 ...", "## 37.1 ...") -- addresses !!
!!  that survive insertion.                                                      !!
!!                                                                              !!
!!  This file now REFUSES TO RUN.  If you genuinely need the r26 build           !!
!!  reproduced against a pinned old draft, pass  --unsafe-i-read-cert-r28-s3 .   !!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

w133 r26 -- build the VERIFICATION-GATE brief on the chain
    G58 (S35) -> G59/(B),(B') (S36) -> S37 (Z1..Z6)  =>  (D3-C6).

The three link texts are extracted VERBATIM from the draft, so the judge reads what the ledger
holds and not a paraphrase.  Everything else in the brief is framing, guards-at-import-site
(RULING AZ), the held-out table, and the questions.
"""
import subprocess, sys, os

DRAFT = "notes/proofs/wowii133_draft.md"

# --- UNSAFE INTERLOCK (owner-w133 r29, cert_w133_r28 section 3) ---------------------
# It aborts by DEFAULT, and before aborting it MEASURES and PRINTS today's drift, so the
# reader is shown the defect rather than told about it.  A banner is a slogan; a refusal
# that prints its own evidence is a gate.
_RANGES = {"S35": (4592, 4717), "S36": (4793, 4897), "S37": (5005, 5093)}
_ANCHORS = {"S35": "## 35.1 The statement",
            "S36": "## 36.1 The statement",
            "S37": "## 37.1 The statement"}
if "--unsafe-i-read-cert-r28-s3" not in sys.argv:
    print("REFUSING TO RUN -- this builder is UNSAFE (cert_w133_r28 section 3, RULING CV).")
    try:
        _l = open(DRAFT, encoding="utf-8").read().split("\n")
        print("  measured against today's draft (%d lines):" % len(_l))
        for _k in ("S35", "S36", "S37"):
            _lo, _hi = _RANGES[_k]
            _a = [i + 1 for i, x in enumerate(_l) if x.startswith(_ANCHORS[_k])]
            _first = _l[_lo - 1] if 0 < _lo <= len(_l) else "<out of range>"
            print("    %s hard-coded lo=%-5d anchor now at %-8s  drift=%-6s first cut line: %r"
                  % (_k, _lo, _a or "MISSING", (_a[0] - _lo) if _a else "n/a", _first[:60]))
    except Exception as _e:                      # pragma: no cover - diagnostic only
        print("  (could not measure drift: %s)" % _e)
    print("  Use problems/wowii/w133_r29_build_q41.py instead (cuts at section anchors).")
    sys.exit(2)
print("WARNING: running an UNSAFE builder under explicit override.")
# -----------------------------------------------------------------------------------
OUT = os.path.expanduser("~/workspace/claudecode/automath-sandbox/briefs/w133_r26_chain.md")

def draft(lo, hi):
    with open(DRAFT) as f:
        lines = f.readlines()
    return "".join(lines[lo - 1:hi])

# the held-out table is read from the key script's own output, so brief and key cannot drift
KEYOUT = open("problems/wowii/w133_r26_key.out").read()
hosts = {}
for line in open("problems/wowii/w133_r26_key.key.txt"):
    if " edges: " in line:
        nm, e = line.split(" edges: ")
        hosts[nm.strip()] = e.strip()
rows = []
for line in open("problems/wowii/w133_r26_key.key.txt"):
    parts = line.rstrip("\n").split("\t")
    if len(parts) == 4 and parts[0].startswith("V"):
        rows.append(parts)          # rid, tier, question, ANSWER (answer NEVER goes in the brief)

B = []
w = B.append

w("""# VERIFICATION REVIEW — a PROOF CHAIN, not a new theorem

You are being asked to **review a chain of three results that have never been checked by anyone
other than their author**. The author is the same person for all three, they were produced in
three consecutive working sessions, and each one imports the previous. **A chain is exactly as
strong as its weakest unverified link**, and that is the whole reason this review exists.

**READ THIS FIRST, because it changes what a useful answer looks like.** The question is *not*
"is the final theorem true?". The author already believes it is, and independent bounded
enumeration agrees with it over 802 853 regions. The question is **whether the LINKS hold**:

> **(P1) — THE PRIMARY QUESTION, and answering only this one is a success for this brief.**
> At each point where the chain imports an earlier statement, **is that statement's hypothesis
> actually satisfied where it is used, and is its conclusion used exactly as stated — not
> silently strengthened, not applied to a larger set than it was proved for, not applied with a
> different definition of the same symbol?**

Two ranked below it, attempt them only if (P1) is settled:

> **(P2)** Is the assembly `(Z1)` — `Sigma_v (a(v)-3) <= n_3 + 2m - 6` — valid *as arithmetic*
> from the four inputs it names? Every term must be accounted for exactly once.
> **(P3)** Are the case analyses **complete** as claimed? Each is stated as "N frames, k survive".
> You cannot re-run them. What you *can* check is whether the case split, as described, exhausts
> the possibilities the argument needs it to exhaust, and whether the survivors listed are
> consistent with the conclusions drawn from them.

If you settle (P1) and go no further, write **`(P2)/(P3) NOT ATTEMPTED`** and stop. That is an
accepted answer and it is better than a thin pass over all three.

**A LOCATED GAP IS THE BEST OUTCOME OF THIS REVIEW, better than a clean verdict.** If one link
fails, name **which link, which step id, and what is missing**. "I could not verify step (Z5)
because the frame count is not reproducible from the text" is a valuable answer. A general
statement that the argument "seems plausible" is worth nothing here.

---

# PART 0 — THE HELD-OUT TABLE. Do this BEFORE reading any mathematics, and answer it in your reply.

Four graphs are printed below on vertex set `{0,...,n-1}`. **They are TEST GRAPHS ONLY.** They
are not instances of anything, no argument in this brief refers to them, and nothing below asks
you to reason about them. They exist so that the reviewer's arithmetic can be checked. **One of
the four is deliberately NOT in the class** — do not assume the class hypotheses hold for any of
them.

Definitions you need, and nothing else:
* `d(v)` = degree. `t(v)` = number of edges of `G` with both ends in `N(v)`. **`a(v) := d(v) - t(v)`**.
* `Z := (z_0,...,z_5) = (0,1,2,3,4,5)` in cyclic order in every printed graph.
* The **trace** of `v` not in `Z` is `N(v) ∩ Z`. `W_1` = trace of size 1; `W_cons` = trace of size
  2 at cycle-distance 1; `W_anti` = trace of size 2 at cycle-distance 3; `W_0` = empty trace.
* `T_Z := Sigma_{z in Z} t(z)`.  `n_3 := #{ v in W_1 : a(v) = 3 }`.
* "longest induced path" is counted **in VERTICES** (so a single edge is 2).
""")

for nm in ("K1", "K2", "K3", "K4"):
    w("* **%s** edges: `%s`" % (nm, hosts[nm]))

w("""
**Tiers are disclosed, deliberately, so you can spend your effort where it is worth spending:**

| row | tier | question |
|---|---|---|""")
for rid, tier, q, _a in rows:
    q2 = q.replace("|", "/")
    w("| **%s** | **%s** | %s |" % (rid, tier, q2))

w("""
**Tier H** rows are bounded local inspection of the printed edge list; they are hand-derivable and
a confidently stated wrong value on one of them **voids this entire review, mathematics included**.
**Tier C** rows are not reliably hand-derivable at this size; a wrong Tier-C value is recorded
against the specific row and demotes only conclusions that read that quantity.

> **`CANNOT COMPUTE — <reason>` is an ACCEPTED answer on ANY row, Tier H included. It is not a
> void and it is not a downgrade.** A stated wrong number is far worse than a refusal. Answer
> every row you attempt in the form `V1 = ...`, one row per line, before the mathematics.

---

# PART 1 — HYPOTHESES, and the imports, WITH THEIR GUARDS AT THE POINT OF IMPORT

Throughout, and **byte-for-byte** in all three links: `G` is a **connected**, **C4-free** graph
containing an **induced 6-cycle** `Z = (z_0,...,z_5)`, and **`G` has no induced P7**. The target
is

> **(D3-C6)**: under exactly those hypotheses, `Sigma_{v in V} a(v) <= 3n`, equivalently
> `Sigma_v (a(v) - 3) <= 0`.

**Five earlier statements are imported by the chain. Each is restated here IN FULL with its own
hypotheses**, so that you can check the import without following a reference. Where a guard
cannot travel with the statement, that is said explicitly.

**IMPORT 1 — `G54` (off-cycle attachment classification).**
> *Hypotheses: `Z` an induced 6-cycle of a **C4-free** graph, `w` not in `Z`.*
> Then `N(w) ∩ Z` contains no pair at cycle-distance 2; hence `|N(w) ∩ Z| <= 2`, and a 2-element
> trace is **consecutive or antipodal**.
> *Proof: if `w ~ z_i` and `w ~ z_{i+2}` then `z_i, z_{i+2}` have common neighbours `z_{i+1}` and
> `w`, a C4. Any 3 vertices of a 6-cycle contain a distance-2 pair.*
> **GUARD AT THIS IMPORT SITE:** G54 needs **C4-freeness only** — it does not need P7-freeness or
> connectivity, so it survives passage to any induced subgraph containing `Z`. This is what makes
> the frame tables below legitimate.

**IMPORT 2 — `G55` (on-cycle charge identity).**
> *Hypotheses: `Z` an induced C6 of a **C4-free** graph; `Off(z) := N(z) \\ Z`.*
> `a(z) = 2 + |Off(z)| - t(z)`, hence `Sigma_{z in Z}(a(z)-2) = Sigma_{z in Z}(|Off(z)| - t(z))`.
> *Proof: `Z` induced gives `d(z) = 2 + |Off(z)|`; C4-freeness makes `G[N(v)]` a **matching** (if
> `x ~ y ~ z` inside `N(v)` then `v-x-y-z-v` is a C4), so `a(v) = d(v) - t(v)`.*
> **GUARD AT THIS IMPORT SITE:** the matching step is **not** true of graphs in general — it is
> exactly where C4-freeness is spent. **And G55's named limitation travels with it:** a `Z`-local
> charge count **cannot see charge living away from `Z`**, because the off-cycle population
> attached to `Z` is unbounded. That is why the chain needs links 1 and 2 at all.

**IMPORT 3 — `G57` (the consecutive-trace lemma).**
> *Hypotheses: `G` C4-free, `Z` an induced C6, **no induced P7**.*
> `W_cons` vertices never occupy the same slot **(i)** nor overlapping slots **(ii)**; hence the
> occupied slots are independent in the slot-6-cycle and **`|W_cons| <= 3`**, attained **(iii)**;
> at slot distance 2 two such vertices are non-adjacent, at distance 3 both occur **(iv)**.
> *Proof of (ii), the one that uses P7: with traces `{z_0,z_1}` and `{z_1,z_2}` every adjacency
> among the 8 vertices is forced except the bit `ww'`; `w !~ w'` gives the induced P7
> `w z_0 z_5 z_4 z_3 z_2 w'`, and `w ~ w'` gives a C4 at `(w, z_2)` via `z_1, w'`.*
> **GUARD AT THIS IMPORT SITE:** G57 **does** need P7-freeness, so unlike G54 it may only be
> applied inside the class — never to an arbitrary induced subgraph chosen for convenience.

**IMPORT 4 — `§34.4a` (`|W_anti| <= 3`).**
> Each antipodal **slot** holds at most one vertex: two vertices with the same antipodal trace
> `{z_i, z_{i+3}}` are two common neighbours of `z_i` and `z_{i+3}`, a C4. There are 3 slots.
> **GUARD AT THIS IMPORT SITE:** C4-freeness only. Attained at `n = 9` by
> `0-1,1-2,2-3,3-4,4-5,5-0,6-0,6-3,7-1,7-4,8-2,8-5` (C4-free, induced C6, longest induced path 5).

**IMPORT 5 — the definition of `a`, and it is the one place a symbol could silently change
meaning.** `a(v) = d(v) - t(v)` is used identically in all three links and in `(D3-C6)`.
**This is worth one of your checks**: the chain's failure mode of exactly this shape would be a
step where `a` means "size of a maximum independent set in `N(v)`" in one link and `d - t` in
another. Under C4-freeness `G[N(v)]` is a matching, so the two agree — but the agreement is a
*consequence of C4-freeness*, not a definition, and it is imported as such.

**A GUARD THAT CANNOT MOVE, said here rather than hidden.** The three links are supported by
machine enumerations — frame tables of 32 to 872 frames, and two sweeps over 802 853 and 90 859
regions. **You cannot re-run those and this brief does not pretend you can.** Their populations
are printed inside the text below, deliberately, so that you can at least check them for internal
consistency (e.g. that a table's "N frames" is the product of the free bits it describes). Where
a conclusion rests only on an unreproducible count, **say so** — that is a legitimate and useful
finding, not a failure to review.

---

# PART 2 — LINK 1, `G58` (draft §35), VERBATIM

""")
w(draft(4592, 4717))

w("""
---

# PART 3 — LINK 2, `G59` = (B)/(B'), (draft §36), VERBATIM

""")
w(draft(4793, 4897))

w("""
---

# PART 4 — LINK 3, the `Z`-term (draft §37), VERBATIM — this is where the chain closes

""")
w(draft(5005, 5093))

w("""
---

# PART 5 — THREE CONTROLS, IN THE AUTHOR'S OWN WORDS, on how hand reasoning about this object
# has actually failed

These are not rhetorical. They are three self-reported errors from the three sessions that
produced the three links above, and they went wrong in **three different directions**. They are
here because they tell you where to point your scepticism — and because a reviewer who reproduces
one of them will recognise it.

1. **True but not sharp.** A hand bound was correct and was then used as if it were tight. The
   enumeration showed the true extremum was strictly smaller, and an argument built on the loose
   value silently proved less than it claimed.
2. **A claim inverted.** The author argued that a leaking `W_1` vertex **excludes** an occupied
   antipodal slot. The enumeration says they **coexist** (2 survivors of 32). The true statement
   is weaker and is the one now in (Z5): a leak excludes the **second** slot, not the first.
3. **A hand argument that DISPROVED a true theorem.** From "each leak needs two far neighbours,
   made distinct by C4-freeness", the author built `k` leaks at a single hexagon vertex, computed
   `Sigma(a-3) = k - 6`, and so obtained `+1` at `k = 7` — a *counterexample to (D3-C6)*. **(Z3)
   says `k <= 1`**, and an induced P7 kills the construction already at `k = 2`. The hand
   argument did not fail to prove the theorem; it disproved it.

**The moral the author drew, and you should hold him to it:** on this object, plausible local
reasoning is unreliable in both directions, and the enumerations are the load-bearing part. If a
step in PART 2-4 is justified by prose rather than by an enumeration whose population is printed,
**that step is the one to attack.**

---

# PART 6 — WHAT WILL NOT BE READ, stated in advance so you do not spend budget on it

* **Any argument whose mechanism bounds `n`, or that concludes "`n >= ...`" or "the class is
  finite", is refused without being read on its merits.** The class is known to contain
  arbitrarily large members (Theorem G49 of this project; its construction is deliberately not
  reprinted). If your reasoning reaches such a conclusion, you have made an error upstream.
* **Any argument concluding `W_1 = ∅` or `W_cons = ∅` is refuted before it is read.** Both are
  non-empty inside the hypotheses; explicit `n = 9` in-hypothesis witnesses exist for both. That
  conclusion is the *P6*-level statement, and dropping P6 for P7 is precisely what destroys it.
* **A counterexample is graded exactly as strictly as a proof.** If you believe you have one,
  give the complete edge list and validate it **most-basic-first**: C4-freeness FIRST, then `Z`
  induced, then longest induced path `<= 6`, then the `a`-values. An unvalidated counterexample
  is recorded as a fabrication, not as a refutation.

---

# PART 7 — OUTPUT FORMAT (please follow it exactly)

```
V1 = ...          (one line per held-out row, FIRST, before any mathematics)
...
V9 = ...

VERDICT: CLEAN | GAP | REFUTED
(P1) LINKS: for each import site you checked -- site, imported statement, hypothesis satisfied?
     conclusion used as stated?  one line each.
(P2) ...  or  (P2) NOT ATTEMPTED
(P3) ...  or  (P3) NOT ATTEMPTED
GAPS: link / step id / what is missing.  One line each.  Empty if none.
```

**Length: aim for about 1200 words of deliverable.** If your answer is running long, **cut the
discussion and keep the findings** — a located gap in ten words outranks three pages of summary.
Do not restate the mathematics back to me; I wrote it. Tell me where it breaks, or tell me,
link by link, that it does not.
""")

text = "\n".join(B)
with open(OUT, "w") as f:
    f.write(text)
print("BRIEF WRITTEN: %s  (%d bytes, %d words)" % (OUT, len(text.encode()), len(text.split())))
