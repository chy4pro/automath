#!/usr/bin/env python3
"""
w133 round 30 -- ITEM 2: RE-MEASURE THE RULING DA GATE'S COVERAGE AS A NUMBER.

WHY (planner, cert_w133_r29 amendment to RULING DA).  677 measured its own G14 at 0/4 on the
hard form.  DA's MEASURED coverage is "a bare decimal token in a value-shaped context near a
quantity token" -- it is NOT "any artefact containing a held-out answer".  The r29 round
reported the gate as a PASS (0 hits on the shipped brief).  A pass is not a coverage.  This
file replaces the pass with a FRACTION, measured on the three blind forms the planner names:

    F1  value inside a TUPLE          (the answer is a component of a longer bracketed group)
    F2  stated as a SUM               (the answer is never printed; it is the sum of two
                                       adjacent printed numbers)
    F3  NOUN BEFORE THE NUMBER        (the quantity's name precedes the value, with no
                                       "=", ":" or "is" between them)

RULING CZ: each form is planted in its HARDEST rendering -- no cue token adjacent to the
value -- and, for contrast and per RULING CY, also in an EASY rendering, so that the number
reported is interpretable rather than merely small.  A detector that fires on nothing and a
detector that fires on everything are equally uninformative; both directions are measured.

WHAT A MISS MEANS.  A miss here is NOT a leak in the shipped brief.  It is the gate declining
to see a leak of that shape.  The shipped brief is separately measured clean; what this file
bounds is how much that clean is worth.

Exit 0 always if the measurement completes -- this file REPORTS a number, it does not gate.
Exit 2 only if the harness itself is broken (a planting the gate MUST see is missed).
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
GATE = os.path.join(HERE, "w133_r29_da_gate.py")
KEY = os.path.join(HERE, "w133_r29_key.key.txt")
BRIEF = os.path.expanduser(
    "~/workspace/claudecode/automath-sandbox/briefs/w133_r29_q41.md")

# Load the r29 gate's machinery WITHOUT running its main section.
src = open(GATE, encoding="utf-8").read()
head = re.split(r"^# -+ main\s*$", src, maxsplit=1, flags=re.M)[0]
if head == src:
    raise RuntimeError("could not locate the gate's main-section marker")
ns = {}
exec(compile(head, GATE, "exec"), ns)
scan, load_rows = ns["scan"], ns["load_rows"]

rows = load_rows(KEY)
brief = open(BRIEF, encoding="utf-8").read()

FAIL = []


def render(ans, form, hard):
    """Return the planted CLAUSE for this answer under this blind form."""
    t = ans if isinstance(ans, tuple) else (ans,)
    if form == "F1":                       # value inside a tuple
        pad = tuple([11] + list(t) + [6])  # answer sits INSIDE a longer group
        body = "(" + ", ".join(str(x) for x in pad) + ")"
        return ("the logged profile %s" % body) if hard else ("the profile is %s" % body)
    if form == "F2":                       # stated as a sum, answer never printed
        parts = []
        for v in t:
            parts.append("%d + %d" % (v - 1, 1))
        body = " and ".join(parts)
        return ("split %s over the two halves" % body) if hard else ("total: %s" % body)
    if form == "F3":                       # noun before the number
        body = " ".join(str(x) for x in t)
        return ("the tally %s was logged" % body) if hard else ("tally: %s" % body)
    raise RuntimeError("unknown form")


def plant(row, form, hard):
    """Append the planting in an ANSWER-SHAPED CONTEXT: the row's own subject and quantity
    tokens are inside the detector's window, exactly as a real leak would be."""
    subj = row["subjects"][0]
    quant = (row["quants"] or [""])[0]
    clause = "\n\nAPPENDIX LOG. %s %s %s.\n" % (subj, quant, render(row["ans"], form, hard))
    return brief + clause


print("=" * 96)
print("RULING DA -- COVERAGE MEASUREMENT (item 2).  Rows: %d   Forms: F1 tuple / F2 sum / F3 noun-first"
      % len(rows))
print("=" * 96)
print()
print("BASELINE: the gate on the UNPLANTED shipped brief")
base = scan(brief, rows, "q41-clean")
print("  hits on the clean shipped brief: %d   (r29 reported 0; re-confirmed here)" % len(base))
if len(base) != 0:
    FAIL.append("clean-brief-baseline-moved")

results = {}
for hard in (True, False):
    tag = "HARD" if hard else "EASY"
    print()
    print("-" * 96)
    print("%s FORM -- %s" % (tag,
          "no cue token adjacent to the value (RULING CZ: the hardest rendering)"
          if hard else "a cue token adjacent to the value (RULING CY: shows the gate CAN fire)"))
    print("-" * 96)
    print("  %-5s %-6s %-8s %-8s %-8s" % ("row", "ans", "F1 tuple", "F2 sum", "F3 noun"))
    tot = {"F1": 0, "F2": 0, "F3": 0}
    for r in rows:
        cells = []
        for form in ("F1", "F2", "F3"):
            h = scan(plant(r, form, hard), r_only := [r], "planted")
            new = [x for x in h if x not in base]
            seen = len(new) > 0
            tot[form] += 1 if seen else 0
            cells.append("SEEN" if seen else "miss")
        print("  %-5s %-6s %-8s %-8s %-8s" %
              (r["rid"], "tuple" if isinstance(r["ans"], tuple) else "int",
               cells[0], cells[1], cells[2]))
    results[tag] = dict(tot)
    n = len(rows)
    print("  %-5s %-6s %-8s %-8s %-8s" %
          ("", "TOTAL", "%d/%d" % (tot["F1"], n), "%d/%d" % (tot["F2"], n),
           "%d/%d" % (tot["F3"], n)))
    print("  OVERALL %s COVERAGE: %d/%d" %
          (tag, sum(tot.values()), 3 * n))

print()
print("=" * 96)
print("THE NUMBER, and it replaces r29's 'pass':")
h, e, n = results["HARD"], results["EASY"], len(rows)
print("  RULING DA gate coverage on the HARD form: %d/%d  (F1 %d/%d, F2 %d/%d, F3 %d/%d)"
      % (sum(h.values()), 3 * n, h["F1"], n, h["F2"], n, h["F3"], n))
print("  RULING DA gate coverage on the EASY form: %d/%d  (F1 %d/%d, F2 %d/%d, F3 %d/%d)"
      % (sum(e.values()), 3 * n, e["F1"], n, e["F2"], n, e["F3"], n))
print()
print("  READ IT THIS WAY.  The gate's real predicate is 'a decimal token in a VALUE-SHAPED")
print("  context (=, :, is, total, count, equals, reads) within 140 chars of one of the row's")
print("  own quantity tokens', plus a bracketed-group matcher for tuple rows.  Everything the")
print("  hard column misses is a leak shape this gate WOULD NOT HAVE SEEN in r26 either.")
print("=" * 96)

# --- harness self-check (RULING CY): a form the gate MUST see, or the measurement is void ---
must = [r for r in rows if isinstance(r["ans"], tuple)][0]
h1 = scan(plant(must, "F1", False), [must], "selfcheck")
if not [x for x in h1 if x not in base]:
    FAIL.append("harness-void: the EASY tuple planting was missed, so misses prove nothing")
print()
print("HARNESS SELF-CHECK (RULING CY -- a measuring instrument that can only report 'miss'")
print("measures nothing): the EASY tuple planting on %s must be SEEN ... %s"
      % (must["rid"], "SEEN" if not FAIL else "MISSED"))

if FAIL:
    for f in FAIL:
        print("  BROKEN: %s" % f)
    sys.exit(2)
sys.exit(0)
