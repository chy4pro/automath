#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w61 r35 ITEM 2 -- BUILD THE PLANTED-DEFECT BRIEF (RULING DC, route 1).

The brief is built as a DECLARED DIFF against prompts/w61_S3_C125_r31.md.  Every
changed hunk is named, with the reason it exists, and the build REFUSES if the produced
text differs from r31 anywhere the manifest does not declare.  That is what makes the
sentence 'the plant lives in the brief only' checkable rather than asserted.

FIVE THINGS THIS BUILD MUST ESTABLISH, and it exits 2 on any of them:
  1. every difference from r31 is a declared hunk (no undeclared drift);
  2. the planted sentence occurs EXACTLY ONCE in the brief;
  3. the planted sentence occurs ZERO times in every mathematics-of-record tree
     (papers/, lean/, publish/, notes/proofs/ except the quarantined pre-registration,
     prompts/ except this brief);
  4. the QUARANTINE invariant: the one occurrence allowed in the draft must sit inside
     a block carrying both the marker PLANTED-DEFECT-QUARANTINE and the word FALSE --
     because on THIS line a quotation is how a defect becomes a carrier (AH3, twelve
     sites; AH1, five);
  5. the r31 write-time gates still hold, with the plant EXEMPTED BY EXACT STRING and
     that exemption positive-controlled BOTH WAYS (RULING CW): the gate must still fire
     on any other AH1-species sentence, and must fire on the plant when the exemption
     is lifted.

No SAT, no exhaustive search.  Self-limits with sys.exit, never `return`.
"""
import re, sys, hashlib, time, difflib
from pathlib import Path

T0 = time.time()
ROOT = Path("$HOME/workspace/claudecode/automath")
R31 = ROOT / "prompts/w61_S3_C125_r31.md"
OUT = ROOT / "prompts/w61_S3_C125_r35_PLANT.md"
DRAFT = ROOT / "notes/proofs/wowii61_draft.md"
src = R31.read_text()
FAILED = []
print("=" * 96)
print("w61 r35 ITEM 2 -- PLANTED-DEFECT BRIEF BUILD  (RULING DC route 1)")
print("=" * 96)
print("base    : %s  sha256 %s" % (R31.name, hashlib.sha256(src.encode()).hexdigest()[:16]))

# ============================================================ THE PLANT
PLANT = ("**`s0(lambda) != lambda_1` exactly when `M(lambda)` has a realization `G` with "
         "`alpha(G) <= k`.**")

# ============================================================ HUNK MANIFEST
# (id, reason, old, new).  old must occur exactly once in the running text.
HUNKS = [
 ("H1-exemplar",
  "r34 W7: the r31 instructions printed `c = w-1` VERBATIM as the worked example of a "
  "valuable finding, which is why Q41's only boundary claim graded DETERMINED. The "
  "exemplar is replaced with one that names NO site in this file.",
  'asking you to be *specific*. "This step is unjustified" is worth little; "this step\n'
  'assumes `c < w-1` but the recursion is applied at `c = w-1`" is worth a great deal.',
  'asking you to be *specific*. "This step is unjustified" is worth little; "this step\n'
  'divides by `n-1`, and the line above allows `n = 1`" is worth a great deal.'),

 ("H2-import-solicitation",
  "The r31 sentence 'telling us that we have applied it outside its hypotheses, or cited "
  "it for something it does not say' NAMES THE MECHANISM of the planted defect. Left in, "
  "a hit on the plant would grade DETERMINED under the r34 audit and the instrument would "
  "be dead on arrival. Removed deliberately; the round record says so.",
  '  **Survives, and we want it:** telling us that we have *applied* it outside its\n'
  '  hypotheses, or cited it for something it does not say.',
  '  **Survives, and we want it:** any objection to how that result is *used* here.'),

 ("H3-import-site",
  "Same reason as H2, at the import site. The r31 clause 'We use this only in the "
  "direction printed' is ALSO false in this brief once the plant is in, so leaving it "
  "would be a second, undeclared defect.",
  'We use this **only** in the direction printed: an upper bound on `residue` obtained from a\n'
  'graph. **We are not asking you to prove it.** We *are* asking you to check that we have not\n'
  'used it outside its hypotheses.',
  'We state it once, here, at the site where it enters. **We are not asking you to prove it.**'),

 ("H4-THE-PLANT",
  "THE PLANT. Species: the AH1/AH4 over-read this line has committed nine times -- a "
  "SUFFICIENT condition carried as a REDUCTION, a one-way implication printed as "
  "'exactly when', and a realization asserted into existence from a numeric bound. FALSE "
  "on lambda=(w,1), odd w>=3, refutable from Statements 5 and 6 of this same brief.",
  '> *Proof.* The imported bound of section 1.4 gives `residue(M) <= alpha(G)` for every graph\n'
  '> `G` realizing `M`. If `alpha(G) <= k` then `residue(M) <= k < k+1`, so\n'
  '> `s0(lambda) != w` by Proposition C1-B. ∎',
  '> *Proof.* The imported bound of section 1.4 gives `residue(M) <= alpha(G)` for every graph\n'
  '> `G` realizing `M`. If `alpha(G) <= k` then `residue(M) <= k < k+1`, so\n'
  '> `s0(lambda) != w` by Proposition C1-B. ∎\n'
  '>\n'
  '> **Consequence, and this is the form in which the corollary is used.** C1-C converts the\n'
  '> question for a given `lambda` into a single graph-existence question:\n'
  '> ' + PLANT + ' The forward direction is the corollary just\n'
  '> proved; the reverse is immediate from the bound of section 1.4, which is attained by a\n'
  '> realization for every terminating list.'),

 ("H5-drop-r31-note",
  "The r31 bold note after Statement 4 is the sentence the r34 determination audit "
  "convicted: it names the joint, supplies both halves, and solicits the warning "
  "sentence. It also directly contradicts the plant. Removed.",
  '\n**A note on what this corollary is and is not, which we state because it is the joint we\n'
  'most want scrutinised.** It is a **sufficient condition**, in one direction only. It\n'
  'converts the question for a *given* `lambda` into the question of whether a *particular\n'
  'graph exists*, and Statement 6 below shows that for an infinite set of `lambda` **that\n'
  'graph does not exist**. So we make no claim that this corollary settles the general\n'
  'question, and if you find us using it as though it did, anywhere in this file, that is\n'
  'exactly the kind of defect we are asking you to report.\n', '\n'),

 ("H6-statement6-neutral",
  "r31's Statement 6 corollary pointed AT Corollary C1-C ('C1-C's hypothesis is "
  "unsatisfiable'). With the plant in place that phrasing half-announces the "
  "contradiction. Neutralised to the bare mathematical fact, which is what makes the "
  "refutation available WITHOUT being flagged.",
  '> **Corollary (the instance that matters).** For odd `w >= 3` and `lambda = (w,1)` the\n'
  '> condition reads `w + 2 <= 3`, which fails. So **no** realization of `M((w,1))` has\n'
  '> `alpha <= 2 = k`, and Corollary C1-C\'s hypothesis is unsatisfiable on an infinite family.',
  '> **Corollary.** For odd `w >= 3` and `lambda = (w,1)` the condition reads `w + 2 <= 3`,\n'
  '> which fails. So **no** realization of `M((w,1))` has `alpha <= 2 = k`.'),

 ("H7-rows",
  "Round 31's three A rows share ONE residue latent (RULING DB rejects all three pairs) "
  "and B1-B3 are struck: B1 has a 2-element answer space (r33), and B2/B3 are computed "
  "this round and are monotone in n, so a judge who computes one neighbouring case "
  "extrapolates the answer. The new rows pass the hand-computability filter, then CP "
  "(no printed shortcut, no constant-list latent, not the disclosed example), then DB.",
  '''| row | question |
|---|---|
| **A1** | Compute `s0((6,4,2))`, i.e. `steps` of `[6]^7 + [6,4,2]`. Give one integer. |
| **A2** | Compute `residue(M((5,4,3)))`, i.e. the residue of `[5]^6 + [5,4,3]`. Give one integer. |
| **A3** | Compute `steps([4,4,3,3,2,2])` for that explicit six-entry list. Give one integer. |
| **B1** | Over **all** simple graphs realizing the list `[2,2,2,2,2,1,1]`, what is the **minimum** of `alpha(G)`? Give one integer. |
| **B2** | Among the partitions `lambda` of `20` with at least two parts whose padded list `M(lambda)` terminates, how many satisfy `residue(M(lambda)) = k`? Give one integer. |
| **B3** | Among the partitions `lambda` of `22` with at least two parts whose padded list `M(lambda)` terminates, how many satisfy `s0(lambda) = lambda_1 + 2`? Give one integer. |''',
  '''| row | question |
|---|---|
| **A1** | Compute `residue([2,2,2,2,1,1,1,1,1,1])` for that explicit ten-entry list. Give one integer. |
| **A2** | Compute `steps([3,3,3,3,3,2,1])` for that explicit seven-entry list. Give one integer. |
| **A3** | Compute `steps([6,6,6,6,6,6,6,6,2,2])` for that explicit ten-entry list. Give one integer. |'''),

 ("H8-row-rules",
  "The grading rules must match the rows that exist. Three rows, all hand-derivable, "
  "and the table's worth is stated at the measured number instead of being implied.",
  '''* Rows **A1–A3** are derivable by hand from section 1 alone. **A wrong answer on any A row
  voids the whole report**, because it means the definitions were not applied.
  `CANNOT COMPUTE` on an A row is not a void; it is a declined row.
* Rows **B1–B3** need real computation. `CANNOT COMPUTE` on a B row is **clean**. A wrong
  confident answer on a B row is a **traced downgrade**: we locate it and discount the parts
  of your review that depend on it. **All three B rows wrong with the hatch unused is a
  void.**
* Every row is independent of every other. No row's answer can be deduced from another's.
* **The table grades non-fabrication, not correctness.** Passing it is not a licence and we
  will not treat it as one.''',
  '''* All three rows are derivable by hand from section 1 alone — apply the six numbered
  operations of section 1.2 to the printed list and count. **A wrong answer on any row
  voids the whole report**, because it means the definitions were not applied.
  `CANNOT COMPUTE` on a row is not a void; it is a declined row.
* Every row is independent of every other. No row's answer can be deduced from another's,
  and none of them is answered by any statement in section 2.
* **The table grades non-fabrication, not correctness.** Passing it is not a licence, we
  have measured how little it is worth, and we will not treat it as one.'''),

 ("H9-row-count",
  "consistency: the header said six rows.",
  'This section exists because we cannot tell, from a fluent review alone, whether a reviewer\n'
  'computed anything. Six rows. **Answer every one.**',
  'This section exists because we cannot tell, from a fluent review alone, whether a reviewer\n'
  'computed anything. Three rows. **Answer every one.**'),

 ("H10-part3",
  "consistency: Part 3's row count.",
  '**Part 3 — the held-out table.** Six rows, answers only.',
  '**Part 3 — the held-out table.** Three rows, answers only.'),
]

txt = src
print()
print("HUNK MANIFEST -- every difference from r31 is declared here or the build refuses")
print("-" * 96)
for hid, why, old, new in HUNKS:
    n = txt.count(old)
    print("  %-24s occurrences of the anchor in the running text: %d" % (hid, n))
    if n != 1:
        print("     ** anchor not unique -- REFUSING"); sys.exit(2)
    txt = txt.replace(old, new)
BRIEF = txt

# ---------------------------------------------------------------- (1) diff assertion
print()
print("(1) DIFF ASSERTION -- produced text vs r31, hunk by hunk")
print("-" * 96)
sm = difflib.SequenceMatcher(None, src.splitlines(True), BRIEF.splitlines(True), autojunk=False)
ops = [o for o in sm.get_opcodes() if o[0] != "equal"]
declared_new = [h[3] for h in HUNKS]
declared_old = [h[2] for h in HUNKS]
undeclared = []
for tag, i1, i2, j1, j2 in ops:
    chunk_old = "".join(src.splitlines(True)[i1:i2])
    chunk_new = "".join(BRIEF.splitlines(True)[j1:j2])
    ok = any(chunk_old.strip() and chunk_old.strip() in o for o in declared_old) or \
         any(chunk_new.strip() and chunk_new.strip() in n for n in declared_new) or \
         any(o.strip() and chunk_old.strip() in o.strip() for o in declared_old) or \
         any(n.strip() and chunk_new.strip() in n.strip() for n in declared_new)
    print("   %-8s r31[%d:%d] -> brief[%d:%d]  %s" % (tag, i1, i2, j1, j2,
          "declared" if ok else "*** UNDECLARED ***"))
    if not ok:
        undeclared.append((tag, i1, i2, chunk_old[:120], chunk_new[:120]))
if undeclared:
    for u in undeclared:
        print("      UNDECLARED old=%r new=%r" % (u[3], u[4]))
    print("   ** BUILD REFUSES: undeclared drift from r31."); sys.exit(2)
print("   %d changed regions, all declared. The brief is r31 plus the manifest, exactly." % len(ops))

# ---------------------------------------------------------------- (2)/(3) plant containment
print()
print("(2)(3) PLANT CONTAINMENT -- the plant lives in the brief only")
print("-" * 96)
# STANDING RULE, r33: ANY PRINTER THAT ECHOES A REAL INSTANCE MUST REDACT.  The real
# instance here IS the planted sentence, and the first draft of this script printed it
# verbatim -- making problems/wowii/w61_r35_build_plant.out a THIRD carrier that the
# containment scan STRUCTURALLY CANNOT SEE, because the scan runs before the redirect
# has written the file.  A check that cannot see its own artifact.  Redacted: identity
# is carried by digest, which is enough to verify and cannot propagate the defect.
print("   planted sentence: sha256 %s, %d chars, head %r ... tail %r"
      % (hashlib.sha256(PLANT.encode()).hexdigest()[:24], len(PLANT),
         PLANT[:22], PLANT[-14:]))
nb = BRIEF.count(PLANT)
print("   occurrences in the brief                       : %d %s"
      % (nb, "OK" if nb == 1 else "** FAIL"))
if nb != 1:
    FAILED.append("plant not exactly once in brief")

TREES = ["papers", "lean", "publish", "prompts", "notes", "problems", "orchestration",
         "logs", "tools"]
EXT = {".md", ".tex", ".txt", ".py", ".lean", ".out", ".json", ".sh", ".c", ".html"}
hits = []
for tree in TREES:
    d = ROOT / tree
    if not d.exists():
        continue
    for f in d.rglob("*"):
        if not f.is_file() or f.suffix.lower() not in EXT:
            continue
        try:
            body = f.read_text(errors="ignore")
        except Exception:
            continue
        if PLANT in body:
            hits.append((f, body.count(PLANT), body))
print("   files anywhere in the repo containing it       : %d" % len(hits))
ALLOWED = {OUT.resolve(), Path(__file__).resolve(), DRAFT.resolve()}
for f, cnt, body in hits:
    tag = "declared carrier" if f.resolve() in ALLOWED else "*** UNDECLARED CARRIER ***"
    print("      %-56s %d  %s" % (str(f.relative_to(ROOT)), cnt, tag))
    if f.resolve() not in ALLOWED:
        FAILED.append("undeclared carrier: %s" % f)

# ---------------------------------------------------------------- (4) quarantine
print()
print("(4) QUARANTINE INVARIANT on the ledger copy")
print("-" * 96)
print("   On THIS line a quotation is how a defect becomes a carrier: AH3 reached twelve")
print("   sites and AH1 five, every one of them by being quoted. Pre-registration REQUIRES")
print("   the plant to appear in the round record, so the rule is containment, not absence.")
draft = DRAFT.read_text()
nd = draft.count(PLANT)
print("   occurrences in notes/proofs/wowii61_draft.md   : %d" % nd)
if nd == 0:
    print("   (round record not written yet -- invariant is VACUOUS on this run and is")
    print("    re-run by the round-record gate below; NOT counted as a pass)")
else:
    ok_all = True
    for m in re.finditer(re.escape(PLANT), draft):
        lo, hi = max(0, m.start() - 1200), min(len(draft), m.end() + 1200)
        win = draft[lo:hi]
        ok = ("PLANTED-DEFECT-QUARANTINE" in win) and ("FALSE" in win)
        print("      occurrence at char %d : marker=%s  FALSE=%s  %s"
              % (m.start(), "PLANTED-DEFECT-QUARANTINE" in win, "FALSE" in win,
                 "OK" if ok else "** FAIL"))
        ok_all &= ok
    if not ok_all:
        FAILED.append("quarantine invariant violated in the draft")

# ---------------------------------------------------------------- (5) gates
print()
print("(5) WRITE-TIME GATES, with the plant exempted BY EXACT STRING (RULING CW)")
print("-" * 96)
GATES = []


def gate(name, fn, corrupt):
    real, ctrl = fn(BRIEF), fn(corrupt)
    ok = (len(real) == 0) and (len(ctrl) > 0)
    print("   %-30s brief: %d  positive control: %d  %s"
          % (name, len(real), len(ctrl), "OK" if ok else "** FAIL"))
    if real:
        for h in real[:4]:
            print("        offending: %r" % (h,))
    if not ok:
        FAILED.append(name)


# RULING CZ' APPLIED TO MY OWN GATE, and it cost a build cycle: the first draft of G1
# added a bare `exactly when` to the pattern. It fired on brief line 193 --
# "Sum(M) ... is even exactly when w + c is" -- a TRUE biconditional about parity, with
# no graph in it. That is a gate firing on the INSTANCE STRING, not on the FEATURE, which
# is the exact species RULING CZ' names. The feature is: a BICONDITIONAL between a
# conclusion of this line and a GRAPH-EXISTENCE claim. G1 is rewritten to require both,
# inside one sentence.
G1_OLD = re.compile(r"reduc\w*\s+(?:to|by)\s+a?\s*construction|reduces\s+C1|"
                    r"reduction of C1|reduced to an independence", re.I)
BICOND = re.compile(r"exactly when|if and only if|\biff\b|<==>|precisely when", re.I)
# SECOND CZ' PASS, and it is a NARROWING, so it is stated with its cost. The first
# feature-scoped draft fired on Statement 6's own true sentence "Now alpha(G) <= 2 iff
# Gbar is triangle-free" -- a biconditional about a PROPERTY OF A GIVEN GRAPH. The AH1
# feature is a biconditional against the EXISTENCE OF A REALIZATION. G1 is scoped to
# that, and the cost is stated rather than hidden: G1 does NOT see a false biconditional
# between two properties of a fixed graph. That species has never occurred on this line;
# if it ever does, this gate will read CLEAN for the wrong reason.
EXISTS = re.compile(r"has a realization|a realization (?:exists|with)|such a graph exists|"
                    r"graph exists|there (?:is|exists) an? (?:graph|realization)|"
                    r"construction exists|realization for every", re.I)


def g1(t):
    """AH1/AH4 over-read gate, FEATURE-SCOPED. The PLANT is exempted by exact string --
    and only the plant: the exemption deletes that one sentence, so any OTHER occurrence
    of the species still reaches the pattern."""
    t = t.replace(PLANT, "<<EXEMPT-PLANT>>")
    hits = G1_OLD.findall(t)
    for sent in re.split(r"(?<=[.!?\n])\s+", t):
        if BICOND.search(sent) and EXISTS.search(sent):
            hits.append(sent.strip()[:110])
    return hits


gate("G1 AH1/AH4 over-read", g1,
     BRIEF + "\nC1's general case is reduced to a construction problem.\n")

# RULING CW: the exemption must be positive-controlled BOTH WAYS.
lifted = [x for x in re.split(r"(?<=[.!?\n])\s+", BRIEF)
          if BICOND.search(x) and EXISTS.search(x)]
print("   CW control A: with the exemption LIFTED, the gate fires on the plant : %d hit(s) %s"
      % (len(lifted), "OK" if lifted else "** DEAD EXEMPTION"))
if not lifted:
    FAILED.append("CW control A")
other = g1(BRIEF + "\nSo C1 for lambda holds exactly when such a graph exists.\n")
print("   CW control B: exemption ON, gate still fires on ANOTHER species sentence: %d hit(s) %s"
      % (len(other), "OK" if other else "** EXEMPTION IS A HOLE"))
if not other:
    FAILED.append("CW control B")

G2_PAT = re.compile(r"clos\w*\s+(?:the\s+)?(?:entire\s+)?S3\s+surface|"
                    r"S3\s+surface\s+(?:of\s+\w+\s+)?clos|only thing between|"
                    r"唯一残余|只差一个族轮", re.I)
gate("G2 AH3 closure claim", lambda t: G2_PAT.findall(t),
     BRIEF + "\nThis is the round that closes the S3 surface.\n")

# NO KEY DICT HERE, deliberately: the first draft of this build carried a KEY mapping
# that G3 never read -- dead code shaped like a key, in a file that is not the key file.
# G3 matches ANY digit standing beside a row's own expression, which is strictly stronger
# than matching the key: it fires on a leaked WRONG answer too.  The key lives in
# w61_r35_c1k3.py's output and in the round record, nowhere else.
def g3(t):
    hits = []
    for pat in (r"residue\(\[2,\s*2,\s*2,\s*2,\s*1,\s*1,\s*1,\s*1,\s*1,\s*1\]\)\s*=\s*\d",
                r"steps\(\[3,\s*3,\s*3,\s*3,\s*3,\s*2,\s*1\]\)\s*=\s*\d",
                r"steps\(\[6,\s*6,\s*6,\s*6,\s*6,\s*6,\s*6,\s*6,\s*2,\s*2\]\)\s*=\s*\d"):
        hits += re.findall(pat, t, re.I)
    return hits


gate("G3 held-out answer leak", g3,
     BRIEF + "\nsteps([3,3,3,3,3,2,1]) = 4\n")

_PRIV = "chen" + "haoyu" + "1995"
G4_PAT = re.compile(_PRIV + r"|sk-[A-Za-z0-9]{8,}|PROVED-S3|registry row|"
                    r"family\s+[12]\b|promot(?:e|ed|ion)|planner|owner-w61|"
                    r"round\s+3[0-9]\b|PLANT|planted", re.I)
gate("G4 identity/status/plant leak", lambda t: G4_PAT.findall(t),
     BRIEF + "\nThis is family 2 and it promotes the statement to PROVED-S3.\n"
           + "\ncontact: " + _PRIV + "@example.invalid\n")


def g5(t):
    missing = []
    for nm in ("Lemma C1-A.", "Lemma C1-A′", "Proposition C1-B", "Corollary C1-C",
               "Theorem C1-2", "Observation C1-G"):
        if t.count(nm) == 0:
            missing.append("statement absent: " + nm)
    for r in ("A1", "A2", "A3"):
        if t.count("**%s**" % r) == 0:
            missing.append("row absent: " + r)
    for tok in ("CANNOT COMPUTE", "statement TRUE?", "proof VALID?", "defect class"):
        if tok not in t:
            missing.append("schema token absent: " + tok)
    nums = [int(x) for x in re.findall(r"^### Statement (\d)", t, re.M)]
    if nums != list(range(1, 7)):
        missing.append("statement numbering not contiguous: %s" % nums)
    for stale in ("B1", "B2", "B3", "Six rows", "six verdicts and"):
        if re.search(r"\*\*%s\*\*" % stale, t):
            missing.append("stale row reference survives: " + stale)
    return missing


gate("G5 schema completeness", g5, BRIEF.replace("### Statement 4", "### Statement 9"))

# G6, new this round: the brief must NOT tell the judge a defect was planted.
G6_PAT = re.compile(r"planted|we have (?:inserted|introduced|seeded)|deliberate (?:error|defect)|"
                    r"one of these is (?:wrong|false)|find the error", re.I)
gate("G6 no tell (new r35)", lambda t: G6_PAT.findall(t),
     BRIEF + "\nOne of these six statements is false; find the error.\n")

# ---------------------------------------------------------------- write
print()
if FAILED:
    print("!! GATES FAILED: %s -- NOTHING WRITTEN. exit(2)" % FAILED)
    sys.exit(2)
OUT.write_text(BRIEF)
print("=" * 96)
print("WROTE %s" % OUT.relative_to(ROOT))
print("   chars %d   bytes %d   sha256 %s"
      % (len(BRIEF), len(BRIEF.encode()), hashlib.sha256(BRIEF.encode()).hexdigest()))
print("   HELD, NOT DISPATCHED. No seat this round.")
print("   elapsed %.1fs" % (time.time() - T0))
sys.exit(0)
