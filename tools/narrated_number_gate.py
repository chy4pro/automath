#!/usr/bin/env python3
"""narrated_number_gate -- find NARRATED numbers: multi-digit literals that live inside a
print/log string but are never computed by the program that prints them.

Bought by: w61 r38 block [3] printed "(184 distinct counterexamples)" as a bare string
literal. `184` occurred exactly once in the file -- inside that print. A byte-identical
re-run reproduces such a literal perfectly, every time, forever, so RULING CD reproduction
is STRUCTURALLY BLIND to this class. This gate is not.

A hit is not automatically a defect (years, section numbers, round labels are fine). A hit
is a number that must be traced to the run that produced it, or removed.

WHAT THIS GATE CANNOT TELL YOU -- widened 2026-08-23, after it mis-served its own author.
It answers only "is this computed by the file AS IT STANDS?", and returns NO for BOTH:
  (a) INVENTED -- no run ever produced it;                    -> remove; no basis.
  (b) STALE    -- really measured, but under a counter or      -> re-state with the correct
      population the file has since abandoned, then carried       population; the measurement
      forward in prose.                                           survives, the sentence does not.
These need OPPOSITE responses. The `184` that bought this gate turned out to be (b), NOT (a):
it is the POSITIONAL-counter violation count of that very sweep (ok=5842 / VIOL=184), while
the sentence around it had moved to the DISTINCT counter (ok=635 / VIOL=97). Verified by
re-running both counters side by side (problems/wowii/w61_r40_pop.out [1]).
This gate's author read the NO as invention and certified it as fabrication -- wrongly.
**When a number fails this gate, the FIRST question is what it WAS measured on, not whether
it was measured.**

Usage:  python3 tools/narrated_number_gate.py FILE [FILE ...]
Exit:   1 if any suspect literal found, else 0.
"""
import ast
import re
import sys

# Numbers that are conventional labels, not measurements.
ALLOW = re.compile(r"^(19|20)\d\d$")           # years
MIN_DIGITS = 2


def suspects(path):
    src = open(path, encoding="utf-8", errors="replace").read()
    try:
        tree = ast.parse(src)
    except SyntaxError as e:
        return [(0, "UNPARSEABLE: %s" % e)]

    # Every numeric literal the program actually computes with or assigns.
    computed = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            computed.add(str(node.value))

    out = []
    for node in ast.walk(tree):
        if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)):
            continue
        if node.func.id not in ("print", "log", "warn", "info"):
            continue
        for arg in ast.walk(node):
            if not (isinstance(arg, ast.Constant) and isinstance(arg.value, str)):
                continue
            text = arg.value
            # %-format and {}-format specifiers mean the number arrives from the program.
            pat = r"(?<![\d.%])(\d{" + str(MIN_DIGITS) + r",})(?![\d.])"
            for m in re.finditer(pat, text):
                n = m.group(1)
                if ALLOW.match(n):
                    continue
                # DECLARED BLIND SPOT: a literal that also appears as a real numeric
                # constant in the program is treated as a reference to that constant.
                # A narrated number that coincides with a program constant is missed.
                if n in computed:
                    continue
                # %-58s / %20d are FORMAT WIDTHS -- the value arrives from the program.
                if re.search(r"%[-+ #0]*$", text[:m.start()]):
                    continue
                # Digits glued to letters are identifiers (w61, w133, C4, PG, R36),
                # not counts.
                if m.start() and (text[m.start() - 1].isalpha()
                                  or text[m.start() - 1] == "_"):
                    continue
                # A reference like "round 38" / "PART 2" / "step=5" is a label.
                before = text[max(0, m.start() - 8):m.start()].lower()
                if re.search(r"(round|part|block|step|item|sec|§)\s*$", before):
                    continue
                out.append((node.lineno, "NARRATED %s in: %s" % (n, text.strip()[:90])))
    return out


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 0
    bad = 0
    for path in argv[1:]:
        hits = suspects(path)
        if hits:
            bad = 1
            print("=== %s ===" % path)
            for line, msg in hits:
                print("  line %d: %s" % (line, msg))
        else:
            print("=== %s === clean" % path)
    if bad:
        print("\nA hit is not automatically a defect. It is a number that must be traced to")
        print("the run that produced it, or removed. Reproduction cannot do this for you.")
    return bad


if __name__ == "__main__":
    sys.exit(main(sys.argv))
