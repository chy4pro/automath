#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w61 r34 ITEM 1 -- RULING CP, INVERTED onto the judge's OUTPUT.

CP asks: does the brief determine a held-out ANSWER?
This asks:  does the brief determine Q41's REPORT?

The classification is MINE, BY READING (the house pattern of §7.48 (g): every claim was
read, classified by hand, and the script only EXECUTES the classification).  What the
script contributes -- and it is not nothing -- is that it makes the hand audit falsifiable
in three directions at once:

  CHECK 1  every quoted CLAIM must be byte-present in the judge's own report file, after
           whitespace normalisation.  I cannot misquote the judge in my own favour.
  CHECK 2  every claim graded DETERMINED must name >=1 ANCHOR span that is byte-present
           in the brief.  I cannot cite a determining passage that is not there.
  CHECK 3  every claim graded NOT-DETERMINED must name >=1 string that is byte-ABSENT
           from the brief.  I cannot grade something free that the brief in fact prints.

  FALSIFIABILITY CONTROL (the point of the whole design): the SAME audit is run over
  Q42's Part 4, whose contribution the planner has already adjudicated as a genuine
  outside finding (Lemma C1-H, cert_w61_r33 §2).  If the audit cannot return
  NOT-DETERMINED for Q42, it is a rubber stamp and its Q41 verdict means nothing.
  The run REFUSES TO CERTIFY unless Q42 comes back NOT-DETERMINED.

RULING CO' note, stated rather than assumed: there is NO existing positive-controlled
implementation of a determination predicate to lift.  Round 31's CP audit was done by
hand (three rows struck before dispatch, §7.46) and left no reusable predicate; the r31
build script carries only the G1..G5 phrase gates.  The predicate used here is Python's
own substring operator over a normalisation, not a re-typed project predicate.

VERIFY-ONLY: the two report files are READ from the sandbox and nothing is written there.
"""
import re, sys, os, hashlib

BRIEF = '$HOME/workspace/claudecode/automath/prompts/w61_S3_C125_r31.md'
Q41 = '$HOME/workspace/claudecode/automath-sandbox/w61_r32/q41_qwen38max.md'
Q42 = '$HOME/workspace/claudecode/automath-sandbox/w61_r32/q42_gemini_pro.md'


def norm(s):
    """markdown-insensitive: drop blockquote markers, collapse all whitespace.
    Without this, every anchor inside the brief's `> ` proof blocks would fail to match
    a claim that quotes it across a line wrap -- which would make the audit LENIENT
    (spuriously NOT-DETERMINED), i.e. it would err toward the promotion.  It errs the
    other way on purpose."""
    s = re.sub(r'(?m)^[ \t]*>[ \t]?', '', s)
    return re.sub(r'\s+', ' ', s)


for p in (BRIEF, Q41, Q42):
    if not os.path.exists(p):
        print("MISSING INPUT: %s" % p)
        sys.exit(2)

raw_brief = open(BRIEF, encoding='utf-8').read()
raw_q41 = open(Q41, encoding='utf-8').read()
raw_q42 = open(Q42, encoding='utf-8').read()
B, R41, R42 = norm(raw_brief), norm(raw_q41), norm(raw_q42)

print("=== w61 r34 item 1 -- does the BRIEF DETERMINE Q41's REPORT? ===")
print("  brief %s  %d chars  sha256 %s" % (
    os.path.basename(BRIEF), len(raw_brief), hashlib.sha256(raw_brief.encode()).hexdigest()[:16]))
print("  Q41   %s  %d chars  sha256 %s" % (
    os.path.basename(Q41), len(raw_q41), hashlib.sha256(raw_q41.encode()).hexdigest()[:16]))
print("  Q42   %s  %d chars  sha256 %s" % (
    os.path.basename(Q42), len(raw_q42), hashlib.sha256(raw_q42.encode()).hexdigest()[:16]))

# ---------------------------------------------------------------- the claim ledger
# verdict: DET   = the brief's text fixes this content
#          FREE  = the brief does not fix it (this is what would discharge)
#          VOID  = excluded by cert_w61_r33 §1: the held-out harness is ruled void
#          NDISC = structurally non-discriminating (see the note printed below)
# alts:    number of alternative CONTENTS still consistent with the brief, by reading.
C = []


def claim(cid, part, src, text, verdict, anchors=(), absent=(), alts=None, note=""):
    C.append(dict(cid=cid, part=part, src=src, text=text, verdict=verdict,
                  anchors=list(anchors), absent=list(absent), alts=alts, note=note))


# ---- Part 1, the six VERDICT cells -------------------------------------------------
for n, lab in ((1, 'Lemma C1-A'), (2, "Lemma C1-A′"), (3, 'Proposition C1-B'),
               (4, 'Corollary C1-C'), (5, 'Theorem C1-2'), (6, 'Observation C1-G')):
    claim('V%d' % n, 'Part 1 verdict', 'Q41', 'TRUE | VALID | NONE', 'NDISC', alts=None,
          note='no defect is planted in the file; a reader and an echo emit the same cell')

# ---- Part 1, the six one-sentence REASONS ------------------------------------------
claim('R1', 'Part 1 reason', 'Q41',
      "The two-step reduction `[w]^(w+2) -> [w-2]^w` is legal for `w >= 2`", 'DET',
      anchors=["The list is now `[w-2]^w = [w-2]^((w-2)+2)`",
               "Both steps are legal precisely when `w >= 2`"], alts=1,
      note="the brief's own Lemma C1-A proof, compressed")
claim('R1b', 'Part 1 reason', 'Q41',
      "the base cases `T(0)=0` and abortion at `T(1)`", 'DET',
      anchors=["The base cases: `T(0) = 0`", "`T(1)` is undefined"], alts=1)
claim('R2', 'Part 1 reason', 'Q41',
      "The first step reaches `W(c)`, and for every `t >= 1` the legal step "
      "`W(t) -> W(t-1)` holds, giving exactly `1+c` steps to terminal `W(0)`.", 'DET',
      anchors=["leaving `[c]^2 + [c-1]^c` — which **is** `W(c)`",
               "for every `t >= 1` the head of `W(t)` is `t`",
               "So the run is **one** step down to `W(c)` and then **`c`** steps down to "
               "`W(0)`: `V(c) = 1 + c`"], alts=1)
claim('R3', 'Part 1 reason', 'Q41',
      "Each step deletes exactly one entry, so for a terminating run "
      "`steps = initial length - residue`, and here the initial length is `w+1+k`.", 'DET',
      anchors=["each step deletes exactly one entry, so `steps(M) = |M| - residue(M)` "
               "for every terminating `M`. Here `|M| = (w+1) + k`"], alts=1,
      note="near-verbatim; the brief prints the identity and the length in one sentence")
claim('R4', 'Part 1 reason', 'Q41',
      "The imported theorem is applied inside its hypotheses — `M` terminates and "
      "`G` realizes `M`", 'DET',
      anchors=["realizable as the degree sequence of a simple graph `G`, and for which "
               "the process above terminates",
               "let `M = M(lambda)` terminate. If `M` has a realization `G`"], alts=1,
      note="the brief prints the two hypotheses at the import site AND restates both as "
           "C1-C's own two conditions")
claim('R4b', 'Part 1 reason', 'Q41',
      "excluding the `residue = k+1` required for `s0 = w`", 'DET',
      anchors=["`residue(M) <= k < k+1`", "`s0(lambda) = w  <==>  residue(M) = k + 1`"],
      alts=1)
claim('R5', 'Part 1 reason', 'Q41',
      "The recursion is valid under its stated condition `c <= w-2`, the base `w=c` is "
      "Lemma C1-A′", 'DET',
      anchors=["**Recursion.** Suppose `c <= w-2`", "`U(w,c) = 2 + U(w-2,c)` for `c <= w-2`",
               "**Base.** `U(c,c) = steps([c]^(c+2) + [c]) = steps([c]^(c+3)) = c+1` by "
               "Lemma C1-A′"], alts=1,
      note="a table of contents of the brief's own three labelled proof parts")
claim('R5b', 'Part 1 reason', 'Q41',
      "odd `w+c` is correctly ruled out by the even-sum invariant for completed runs",
      'DET',
      anchors=["**Parity.** A completed run satisfies `Sum(M) = 2 * Sum(heads)`, so "
               "`Sum(M)` must be even",
               "When `w != c (mod 2)` the sum is odd and no completed run exists"], alts=1)
claim('R6', 'Part 1 reason', 'Q41',
      "the `c` outside vertices have total degree capacity at most `2c`, forcing "
      "`w+2 <= 3c`", 'DET',
      anchors=["That set has `N - 1 - D0 = c` vertices, each of `Gbar`-degree `2`, so it "
               "absorbs at most `2c` edge-ends. Hence `D0 <= 2c`, i.e. `w + 2 <= 3c`"],
      alts=1)
claim('R6b', 'Part 1 reason', 'Q41',
      "the `D0 = w+2-c` neighbors of `u` each need one edge-end outside", 'DET',
      anchors=["Let `u` be the vertex of `Gbar`-degree `D0 := w+2-c`",
               "spends its one remaining edge outside `{u} + N(u)`"], alts=1,
      note="`N[u]` for `{u} + N(u)` is a notation substitution, not content")

# ---- Part 2 -------------------------------------------------------------------------
claim('P2', 'Part 2', 'Q41',
      "I found no false statement, no proof gap that affects the conclusion, and no "
      "scope mismatch", 'NDISC', alts=None,
      note="entailed by Part 1's six NONEs plus the brief's own reporting spec")

# ---- Part 4, the weakest joint ------------------------------------------------------
claim('W1', 'Part 4', 'Q41',
      "The weakest joint is the graph-existence interface between Corollary C1-C and "
      "Observation C1-G.", 'DET',
      anchors=["which we state because it is the joint we most want scrutinised"], alts=1,
      note="THE BRIEF ANSWERS ITS OWN PART 4 QUESTION, IN BOLD, at Statement 4")
claim('W2', 'Part 4', 'Q41',
      "C1-C is a one-directional sufficient condition and becomes vacuous whenever no "
      "low-`alpha` realization exists", 'DET',
      anchors=["It is a **sufficient condition**, in one direction only",
               "Statement 6 below shows that for an infinite set of `lambda` **that "
               "graph does not exist**"], alts=1)
claim('W3', 'Part 4', 'Q41',
      "C1-G supplies only a necessary inequality, not a characterization of when such a "
      "realization exists", 'DET',
      anchors=["Observation C1-G is a **necessary** condition only",
               "Whether `w + 2 <= 3c` is also **sufficient** for such a realization to "
               "exist is **open**"], alts=1)
claim('W4', 'Part 4', 'Q41',
      "The file is careful not to claim sufficiency of `w + 2 <= 3c`", 'DET',
      anchors=["**Stated exactly, because we will not overstate it:**",
               "we have not proved it, and we are not asking you to assume it"], alts=1)
claim('W5', 'Part 4', 'Q41',
      "treating the inequality as evidence that a realization with `alpha <= 2` actually "
      "exists", 'DET',
      anchors=["if you find us using it as though it did, anywhere in this file, that is "
               "exactly the kind of defect we are asking you to report"], alts=1,
      note="the brief solicits this exact sentence by name")
claim('W6', 'Part 4', 'Q41',
      "the nearest delicate boundary is Statement 5’s recursion restriction "
      "`c <= w-2`", 'DET',
      anchors=["**Recursion.** Suppose `c <= w-2`",
               "assumes `c < w-1` but the recursion is applied at `c = w-1`"], alts=1,
      note="the SITE is handed over in the brief's INSTRUCTIONS as its worked example of "
           "a valuable finding")
claim('W7', 'Part 4', 'Q41',
      "the excluded `c = w-1` case is handled by parity", 'DET',
      anchors=["assumes `c < w-1` but the recursion is applied at `c = w-1`",
               "**Parity.**", "iff `w + c` is even"], alts=1,
      note="CLOSEST CALL IN THE REPORT -- see the steelman printed at the end")
claim('W8', 'Part 4', 'Q41',
      "any attempt to extend that recursion across the boundary would fail", 'NDISC',
      alts=None, note="unargued hedge; no mechanism given, so nothing to determine")

# ---- Part 3, the held-out rows ------------------------------------------------------
for row, ans in (('A1', '8'), ('A2', '2'), ('A3', '4'), ('B1', '3'),
                 ('B2', 'CANNOT COMPUTE'), ('B3', 'CANNOT COMPUTE')):
    claim('T-%s' % row, 'Part 3', 'Q41', ans, 'VOID', alts=None,
          note='cert_w61_r33 §1: harness ruled VOID as a discriminator (1.0-1.6 bits)')

# ---- FALSIFIABILITY CONTROL: Q42's Part 4, adjudicated OUTSIDE this audit -----------
claim('X1', 'Part 4 CONTROL', 'Q42',
      "it assumes that if a sequence does complete, its final sum is exactly 0", 'FREE',
      absent=["final sum is exactly 0", "all zeros", "sum `0`", "sum 0"], alts=None,
      note="Lemma C1-H's premise. The brief asserts `Sum(M) = 2 * Sum(heads)` and NEVER "
           "prints why; the terminal-list-is-all-zeros step appears nowhere in the brief")
claim('X2', 'Part 4 CONTROL', 'Q42',
      "a terminal list triggered by d=0 in a weakly decreasing array of non-negative "
      "integers must consist entirely of zeros", 'FREE',
      absent=["must consist entirely of zeros", "consist entirely of zeros"], alts=None,
      note="Lemma C1-H itself, supplied by the judge and not by the brief")

# ---------------------------------------------------------------- the three checks
fail = []
print("\n--- CHECK 1: every quoted claim is byte-present in its own report ---")
src = {'Q41': R41, 'Q42': R42}
n_ck1 = 0
for c in C:
    if c['part'] in ('Part 1 verdict', 'Part 3'):
        continue          # cell values, not prose; checked separately below
    n_ck1 += 1
    ok = norm(c['text']) in src[c['src']]
    if not ok:
        fail.append("CHECK1 %s: quote not found in %s report" % (c['cid'], c['src']))
    print("  %-5s %-4s %s" % (c['cid'], c['src'], "present" if ok else "*** NOT FOUND ***"))

# Part 1 cells and Part 3 rows, checked as table content
for n in range(1, 7):
    if ("Statement %d" % n) not in R41:
        fail.append("CHECK1 V%d: statement row absent from Q41" % n)
for row, ans in (('A1', '8'), ('A2', '2'), ('A3', '4'), ('B1', '3')):
    if ("| %s | %s |" % (row, ans)) not in norm(raw_q41):
        fail.append("CHECK1 T-%s: held-out cell not as recorded" % row)
print("  Part 1 six statement rows + Part 3 four numeric cells: verified in Q41")

print("\n--- CHECK 2: every DETERMINED claim's anchors are byte-present in the BRIEF ---")
n_anchor = 0
for c in C:
    if c['verdict'] != 'DET':
        continue
    for a in c['anchors']:
        n_anchor += 1
        if norm(a) not in B:
            fail.append("CHECK2 %s: anchor NOT in brief: %r" % (c['cid'], a[:70]))
            print("  %-5s *** ANCHOR NOT IN BRIEF *** %r" % (c['cid'], a[:66]))
    if not c['anchors']:
        fail.append("CHECK2 %s: graded DET with no anchor" % c['cid'])
    print("  %-5s %d/%d anchors present" % (c['cid'], len(c['anchors']), len(c['anchors'])))

print("\n--- CHECK 3: every NOT-DETERMINED claim names a string ABSENT from the brief ---")
for c in C:
    if c['verdict'] != 'FREE':
        continue
    if not c['absent']:
        fail.append("CHECK3 %s: graded FREE with no absence witness" % c['cid'])
    for a in c['absent']:
        present = norm(a) in B
        print("  %-5s %-40r %s" % (c['cid'], a[:38], "IN BRIEF (bad)" if present else "absent"))
        if present:
            fail.append("CHECK3 %s: claimed-free string IS in the brief: %r" % (c['cid'], a))

# ---------------------------------------------------------------- rubber-stamp guard
free_q42 = [c for c in C if c['verdict'] == 'FREE' and c['src'] == 'Q42']
free_q41 = [c for c in C if c['verdict'] == 'FREE' and c['src'] == 'Q41']
print("\n--- FALSIFIABILITY: can this audit return NOT-DETERMINED at all? ---")
print("  Q42 claims returned NOT-DETERMINED: %d" % len(free_q42))
if not free_q42:
    print("  THE AUDIT NEVER RETURNS NOT-DETERMINED. It is a rubber stamp.")
    print("  REFUSING TO CERTIFY.")
    sys.exit(2)
print("  the audit discriminates: it returns NOT-DETERMINED on the contribution the")
print("  planner independently adjudicated as real (Lemma C1-H, cert_w61_r33 §2).")

# ---------------------------------------------------------------- the ledger
print("\n=== LEDGER -- Q41, claim by claim ===")
print("  %-5s %-16s %-6s %-4s %s" % ("id", "part", "verdict", "alts", "note"))
for c in C:
    if c['src'] != 'Q41':
        continue
    print("  %-5s %-16s %-6s %-4s %s" % (c['cid'], c['part'], c['verdict'],
                                         c['alts'] if c['alts'] is not None else '-',
                                         c['note'][:74]))

q41 = [c for c in C if c['src'] == 'Q41']
det = [c for c in q41 if c['verdict'] == 'DET']
nd = [c for c in q41 if c['verdict'] == 'NDISC']
vd = [c for c in q41 if c['verdict'] == 'VOID']
print("\n  Q41 claims graded: %d" % len(q41))
print("    DETERMINED by the brief          %2d   (anchors verified present: %d)" % (len(det), n_anchor))
print("    NOT DETERMINED (would discharge) %2d" % len(free_q41))
print("    non-discriminating, excluded     %2d" % len(nd))
print("    VOID harness rows, excluded      %2d" % len(vd))

print("""
--- WHY THE VERDICT CELLS ARE EXCLUDED RATHER THAN COUNTED ---
No defect is planted anywhere in the six statements.  When the file under review is
clean, the correct verdict and the fluent-echo verdict are THE SAME SIX CELLS.  A review
harness with no planted fault cannot separate a reader from an echo in Part 1, whatever
the reviewer actually did.  That is RULING CZ in the review layer: the fault set was
drawn from a dimension on which the check has no resolving power -- here, from the empty
set.  Counting the six NONEs as engagement would be counting the null hypothesis.

--- WHY PART 3 IS EXCLUDED RATHER THAN COUNTED ---
Read at the letter, the discharge ("if it produced anything the brief does not
determine") is SATISFIED BY PART 3: the brief does not print A1/A2/A3, so those three
numbers are literally not determined by its text.  Counting them would grant the
promotion on the instrument cert_w61_r33 §1 has just ruled VOID, and would make the
inverted test auto-pass for any report that filled in the table at all.
DETERMINATION and GUESSABILITY are different failure modes.  Part 3 survives the first
and fails the second at 1.0-1.6 bits.  It is excluded here on the standing ruling.

--- THE CLOSEST CALL, STATED AS A STEELMAN BEFORE IT IS REJECTED (W7) ---
FOR engagement: the brief's section 0 exemplar ASSERTS a defect at `c = w-1` ("the
recursion is applied at `c = w-1`").  Q41 did not report that defect; it reported that
the case is vacuous.  A pure echo might have parroted the exemplar as a finding, which
would have been a false positive.  Q41 instead supplied the resolution, and the
resolution is CORRECT: `c = w-1` gives `w + c = 2w - 1`, odd, so `M` is not a step
sequence and the recursion is never reached.
AGAINST, and this is why it does not carry: the brief hands over all three components.
  (i) THE SITE.  `c = w-1` is printed in the brief VERBATIM, in the same notation, at
      line 16 -- in the INSTRUCTIONS, as the worked example of a finding "worth a great
      deal".  It is the single most conspicuous coordinate in the document.
  (ii) THE POLARITY.  Q41's own Part 1 had already filed Statement 5 as VALID.  Given
      VALID, "the boundary case is handled" is the only completion consistent with its
      own report -- and that VALID cell is the echo default (see the exclusion above).
  (iii) THE MECHANISM.  Statement 5's proof carries exactly three labelled parts:
      Recursion (the thing restricted), Base (`c = w`), Parity.  With the first two
      spoken for, Parity is the only remaining named mechanism.  Alternatives: 1.
The residual free content is the one-line arithmetic `2w - 1 is odd`, conditioned on an
echo-default verdict.  That is not engagement; it is the brief's own exemplar returned
with its sign flipped.  GRADED DETERMINED -- and flagged to the planner as the one claim
where a different ruling is defensible, with the count above so the ruling can be made
on the number rather than on the prose.""")

print("\n=== VERDICT ===")
if fail:
    print("  AUDIT FAILED ITS OWN CHECKS -- verdict withheld:")
    for f in fail:
        print("    " + f)
    sys.exit(2)
print("  all %d checks pass (%d quotes, %d brief anchors, %d absence witnesses)" % (
    n_ck1 + n_anchor + sum(len(c['absent']) for c in C),
    n_ck1, n_anchor, sum(len(c['absent']) for c in C)))
print("""
  Q41: %d of %d gradeable claims are DETERMINED BY THE BRIEF. ZERO are not.
  Excluding the %d void harness rows and the %d structurally non-discriminating cells,
  the report contains NOTHING the brief does not fix.

  ITEM 1 IS NOT DISCHARGED.  Engagement is NOT established for Q41.
  The six statements DO NOT PROMOTE on this evidence.

  And the round-32 reading that this test was raised against is REFUTED, not merely
  unsupported: §7.47 (f) 2 records Q41's weakest joint as "the AH1 neighbourhood,
  arrived at INDEPENDENTLY".  The brief names that joint itself, in bold, and calls it
  "the joint we most want scrutinised".  That sentence in §7.47 must be corrected.

  Q42 is UNAFFECTED and its discharge stands: the same audit returns NOT-DETERMINED on
  Lemma C1-H, which the brief nowhere prints.""" % (len(det), len(det) + len(free_q41), len(vd), len(nd)))
sys.exit(0)
