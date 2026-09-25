#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
w61 round 32, item 3 — RULING CW: G2 must honour `<!-- RETRACTED-QUOTE -->`.

RULING CW: an occurrence of a carrier string on a line carrying the marker
`<!-- RETRACTED-QUOTE -->` is a RETRACTION, not a carrier. A corrected status file
necessarily quotes the claim it retracts; a gate that cannot tell a claim from its
retraction either produces false positives forever or gets switched off.

The ruling comes with its own trap, and the trap is the whole reason for this file:
**an exemption is a hole in the gate.** So the marker is granted the narrowest
possible scope -- ONE LINE -- and the exemption is itself positive-controlled:

  * G2 MUST still fire on the very same string with the marker removed;
  * the marker MUST NOT silence any other line, in the same file or elsewhere;
  * every one of G2's four patterns ships with an input on which it MUST return a hit.

Self-limits with sys.exit, never return. Log is repo-internal. No network, no SAT,
no exhaustive search.
"""
import re, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# G2 EXACTLY as shipped in problems/wowii/w61_r31_build_q41.py (copied by text, not
# paraphrased -- the point of this file is to measure that gate, so it must be that gate).
G2_R31 = re.compile(r"clos\w*\s+(?:the\s+)?(?:entire\s+)?S3\s+surface|"
                    r"S3\s+surface\s+(?:of\s+\w+\s+)?clos|only thing between|"
                    r"唯一残余|只差一个族轮", re.I)

# ---------------------------------------------------------------------------
# DEFECT FOUND BY THIS FILE'S OWN PART 0, round 32.
# G2_R31 does NOT match the sentence AH3 is actually about. Repair AH3 (sec 7.45 (b))
# names the carrier string as
#       "the one round that closes WOWII-61's S3 surface"
# and G2_R31 requires `clos...` to be followed by at most `the ` / `entire ` before
# `S3 surface`. An interposed possessive -- exactly the form the real carriers use --
# walks straight through it. Its round-31 positive control injected
#       "This is the round that closes the S3 surface."
# which matches the EASY form, so the gate was shown firing and was still blind to the
# species it was written for. This is the round-31 cert's own rule arriving one level
# down: a detector matches WORDING, and the wording varied.
G2_R32 = re.compile(r"clos\w*\s+(?:[\w''’‘\-]+\s+){0,3}(?:the\s+)?(?:entire\s+)?S3\s+surface|"
                    r"S3\s+surface\s+(?:[\w''’‘\-]+\s+){0,3}clos|"
                    r"only thing (?:standing )?between|"
                    r"唯一残余|只差一个族轮", re.I)

G2_PAT = G2_R32   # the gate this file ships; G2_R31 is kept only to measure the delta.

MARKER = "<!-- RETRACTED-QUOTE -->"

CARRIERS = [
    "orchestration/STATUS.md",
    "orchestration/PLAN.md",
    "orchestration/watch_ledger.md",
    "HANDOVER.md",
    "notes/proofs/wowii61_draft.md",
]


def g2_hits(text, honour_marker=True, pat=None):
    """Return [(lineno, matched_text, retracted?)] for every G2 occurrence.

    honour_marker=False is the ORIGINAL gate, kept so the exemption can be
    measured against it rather than asserted.
    """
    out = []
    p = pat or G2_PAT
    for i, line in enumerate(text.split("\n"), 1):
        for m in p.finditer(line):
            retracted = honour_marker and (MARKER in line)
            out.append((i, m.group(0), retracted))
    return out


def carriers_only(text, pat=None):
    """The gate's actual verdict input: hits that are NOT marked retractions."""
    return [h for h in g2_hits(text, pat=pat) if not h[2]]


# ------------------------------------------------------------------ PART 0
# Controls run BEFORE any file is judged. Population printed before verdict.
def part0():
    ctl = []

    # (1) Every pattern gets an input on which it MUST return a hit. A predicate
    #     whose failure mode is "unconditionally no match" is invisible otherwise.
    musts = [
        ("EN closes-<NAME>'s-S3-surface (AH3's ACTUAL carrier string)",
         "the one round that closes WOWII-61's S3 surface"),
        ("EN closes-the-S3-surface (the easy form r31 controlled on)",
         "This is the round that closes the S3 surface."),
        ("EN entire variant", "this closes the entire S3 surface"),
        ("EN only-thing-between", "the only thing standing between us and the result"),
        ("ZH 唯一残余", "这是唯一残余的问题"),
        ("ZH 只差一个族轮", "w61 的 S3 面只差一个族轮就全闭"),
    ]
    for name, s in musts:
        ctl.append(("MUST fire: " + name, len(carriers_only(s)) >= 1, True))

    # THE DEFECT, DEMONSTRATED rather than described: the round-31 gate is blind to
    # the very string Repair AH3 was raised about, while firing on the easy form.
    ah3 = "the one round that closes WOWII-61's S3 surface"
    easy = "This is the round that closes the S3 surface."
    ctl.append(("DEFECT SHOWN: G2_R31 is SILENT on AH3's actual carrier string",
                len(carriers_only(ah3, pat=G2_R31)) == 0, True))
    ctl.append(("...while G2_R31 DOES fire on the easy form it was controlled on",
                len(carriers_only(easy, pat=G2_R31)) >= 1, True))
    ctl.append(("...and the r32 repair catches BOTH",
                len(carriers_only(ah3)) >= 1 and len(carriers_only(easy)) >= 1, True))

    # (2) False-positive probe: innocent prose must be silent.
    ctl.append(("MUST be silent on innocent prose",
                len(carriers_only("The S3 surface has two halves and neither is closed.")) == 0,
                True))

    # (2b) THE PRICE OF THE REPAIR, MEASURED ON MY OWN GATE, not described.
    # The r32 pattern buys recall and pays in precision: it fires on the NEGATION of
    # the claim. This is the round-31 cert's ruling from the other side -- a detector
    # matches WORDING, so it cannot tell a claim from its denial any more than it could
    # tell a claim from its retraction. Hence the marker convention exists at all, and
    # hence the sweep's output below is a SUSPECT LIST, not a verdict.
    neg = "So the S3 surface does NOT close this cycle."
    ctl.append(("KNOWN FALSE POSITIVE, demonstrated: r32 gate fires on the NEGATION",
                len(carriers_only(neg)) >= 1, True))
    # MY EXPECTATION WAS WRONG HERE AND THE INSTRUMENT WAS RIGHT, and the incident is
    # kept in the file rather than quietly edited out. I wrote this control asserting
    # the negation false positive was INHERITED from G2_R31. It is not: G2_R31's second
    # alternative allows only `of <word> ` between `surface` and `clos`, so it is silent
    # on "does NOT close". The false positive is INTRODUCED BY MY OWN REPAIR -- the
    # price of the {0,3}-word gap that bought the recall. Recorded as the cost, not
    # laundered as an inheritance.
    ctl.append(("negation FP is INTRODUCED by the r32 repair, NOT inherited from r31",
                len(carriers_only(neg, pat=G2_R31)) == 0, True))

    # (3) THE RULED CONTROL. The real STATUS.md retraction line, verbatim from disk:
    #     with the marker -> exempt; with the marker removed -> STILL FIRES.
    status_path = os.path.join(ROOT, "orchestration/STATUS.md")
    status = open(status_path, encoding="utf-8").read()
    marked = [l for l in status.split("\n") if MARKER in l]
    if len(marked) != 1:
        print("EXPECTED exactly 1 marked line in STATUS.md, found %d -- refusing to run"
              % len(marked))
        sys.exit(2)
    line = marked[0]
    stripped = line.replace(MARKER, "")
    ctl.append(("marked line is EXEMPT (0 carriers)", len(carriers_only(line)) == 0, True))
    ctl.append(("SAME STRING without the marker MUST FIRE",
                len(carriers_only(stripped)) >= 1, True))
    ctl.append(("the raw pattern still matches the marked line (exemption is a "
                "verdict, not blindness)",
                len(g2_hits(line, honour_marker=False)) >= 1, True))

    # (4) The exemption is LINE-scoped, not file-scoped. Corrupt a copy of the real
    #     file by appending an UNMARKED carrier line: the gate must fire on it even
    #     though the file also contains a marked line.
    corrupted = status + "\n这一轮只差一个族轮就全闭。\n"
    cor = carriers_only(corrupted)
    ctl.append(("marker does NOT silence a second, unmarked line in the same file",
                len(cor) == 1, True))
    ctl.append(("...and the surviving hit is the INJECTED line, not the marked one",
                bool(cor) and cor[0][0] == len(corrupted.split("\n")) - 1, True))

    print("=== PART 0 controls (before any file verdict) ===")
    bad = 0
    for name, got, want in ctl:
        ok = (got == want)
        bad += (not ok)
        print("  [%s] %s" % ("ok" if ok else "FAIL", name))
    if bad:
        print("CONTROLS DEFECTED (%d). No sweep run, no verdict printed." % bad)
        sys.exit(2)
    print("  all %d controls pass. The exemption has been shown to be an exemption "
          "and NOT a hole: same string, marker removed, gate fires." % len(ctl))
    return status


def main():
    part0()
    print("\n=== G2 sweep over carriers, marker honoured (population first) ===")
    total_raw = total_carrier = total_retracted = total_old = 0
    for rel in CARRIERS:
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            print("  %-34s ABSENT" % rel)
            continue
        t = open(p, encoding="utf-8").read()
        hits = g2_hits(t)
        old = g2_hits(t, pat=G2_R31)
        raw = len(hits)
        retr = len([h for h in hits if h[2]])
        car = raw - retr
        total_raw += raw; total_retracted += retr; total_carrier += car
        total_old += len(old)
        print("  %-34s raw=%d  retracted=%d  CARRIERS=%d   (r31 gate would have seen %d)"
              % (rel, raw, retr, car, len(old)))
        for ln, txt, r in hits:
            print("       line %-6d %-14s %s" % (ln, "RETRACTION" if r else "CARRIER",
                                                 repr(txt)))
    print("\n  TOTAL raw=%d  retracted(exempt)=%d  CARRIERS=%d"
          % (total_raw, total_retracted, total_carrier))
    print("  The r31 gate would have seen %d of the %d raw occurrences: delta = %d MISSED."
          % (total_old, total_raw, total_raw - total_old))
    print("\n  READING, and it is a measurement not a closure claim: this is a PHRASE")
    print("  detector. Per the round-31 cert it CANNOT close the AH1/AH3 class, because")
    print("  a class is defined by its CLAIM and a detector matches its WORDING --")
    print("  AJ1 was found by reading, wearing the words 'a named reduction'.")
    sys.exit(0)


main()
