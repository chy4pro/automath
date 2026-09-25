#!/usr/bin/env python3
"""owner-w61 round 24 -- PRE-DISPATCH BUILD GATE for prompts/w61_S3_GFAN_r24.md.

Three gates, run before anything is sent:

  GATE 1  brieflint (round 22's artifact, used as a BUILD GATE for the first time).
          The lint rules are NOT re-typed here: this script execs brieflint.py's
          definitions and calls its own lint().  A second copy of a rule is a rule that
          can drift.

  GATE 2  RULING AX derivability leak check.  Not occurrence -- DERIVABILITY.  For each
          held-out row the question is "could a judge produce this value from this brief
          without doing the work the row exists to test?", and the check is written per
          row, because that question has a different answer per row.  H2 is DELIBERATELY
          derivable (its closed form is printed on purpose, it is a HAND-tier row, and
          that is what makes it a fabrication discriminator rather than a capacity test);
          the check asserts that on purpose rather than passing it by accident.

  GATE 3  B6 by ROLE OF OBJECT (RULING AU's form, not the verify/use wording).
          Everything the TARGET's proof must USE is disclosed in full.  Everything held
          out lives on objects with NO mathematical role in the target -- nu = 11 and
          partitions of 22 are outside Theorem GFANnu's range and outside anything the
          corollary needs.  Same quantity family, disclosed where used and held out where
          it is test material.

Exit non-zero on any gate failure.  A gate you can ship around is decoration.
"""
import hashlib, pathlib, re, sys

ROOT  = pathlib.Path("$HOME/workspace/claudecode/automath")
BRIEF = ROOT / "prompts/w61_S3_GFAN_r24.md"
LINT  = ROOT / "problems/wowii/w61_r22_brieflint.py"
KEY   = ROOT / "problems/wowii/w61_r17_heldout_key.txt"

text = BRIEF.read_text()
print(f"gated artifact : {BRIEF.name}")
print(f"  chars {len(text)}   md5 {hashlib.md5(text.encode()).hexdigest()}")
print(f"  key    : {KEY.name} (NOT pasted; grading source)\n")

fails = []

# ============================================================ GATE 1 -- brieflint
print("=== GATE 1 : brieflint (r22 artifact, first use as a build gate) ===")
srcl = LINT.read_text().split("TARGETS = ")[0]      # definitions only, no self-run
ns = {}
exec(compile(srcl, str(LINT), "exec"), ns)
findings = ns["lint"](BRIEF)
for kind, i, ln in findings:
    print(f"   [{kind}] line {i} : {ln[:110]}")
print(f"  findings on r24 : {len(findings)}  (want 0)")
if findings:
    fails.append("brieflint")

# and the lint must still be able to FAIL -- run it on the base it was written against
base_findings = ns["lint"](ROOT / "prompts/w61_S3_GFAN_r20.md")
print(f"  liveness: same lint on the r20 BASE : {len(base_findings)} findings "
      f"({'PASS -- the gate can fail' if base_findings else 'FAIL -- decoration'})")
if not base_findings:
    fails.append("brieflint-liveness")

# ============================================================ GATE 2 -- RULING AX
print("\n=== GATE 2 : RULING AX -- DERIVABILITY, not occurrence ===")

# SCOPING, and it is the whole difference between a check and a false alarm.
# Section 0 STATES the questions -- it names `nu = 11`, prints H5's shape and writes H4's
# definition.  A leak check run over the whole file therefore reports its own question
# text as a leak.  Leakage means the ANSWER is derivable from the REST of the brief, so
# the derivability layer is run over BODY = brief minus Section 0.
#
# CALIBRATION FAILURE, RECORDED (RULING BA -- report the failures, not only the pass):
# v1 of this gate was run unscoped and returned four LEAKs, ALL FOUR of them its own
# Section 0 question text, plus (C-4)'s heading "the count is a closed form, and every
# survivor is printed" -- which is a closed form for the SHAPE count S(nu), not for the
# survivor count, in a sentence that mentions both.  Both failures are FALSE-POSITIVE
# (noisy-and-safe), not the silent-and-favourable direction of RULING BA -- but the
# second one is the same conflation the row exists to test, so it is written down.
_s0 = text.index("## Section 0")
_s0e = text.index("## What this round scores")
SEC0 = text[_s0:_s0e]
BODY = text[:_s0] + text[_s0e:]
print(f"  scoping: Section 0 = {len(SEC0)} chars held aside; BODY = {len(BODY)} chars\n")


def has(pat, scope=None):
    return re.search(pat, BODY if scope is None else scope) is not None

# -- occurrence layer first (necessary, not sufficient) --------------------------------
VALUES = {
    "H1 s0([12,6,4])=14": r"\b14\b",         # weak on its own; the real test is below
    "H2 S(11)=98384":     r"98\s?384|98384",
    "H3 survivors=791":   r"\b791\b",
    "H3 per-E split":     r"170,\s*148|\{1: 6, 2: 14",
    "H4 =131":            r"\b131\b",
}
for name, pat in VALUES.items():
    if name.startswith("H1"):
        continue     # "14" is a common numeral; H1 is tested by derivability below
    hit = has(pat)
    print(f"  occurrence  {name:22s} present={hit}  (want False)")
    if hit:
        fails.append(f"AX-occurrence:{name}")

# -- derivability layer, one question per row ------------------------------------------
def q(label, question, leaked, note=""):
    mark = "LEAK" if leaked else "OK  "
    print(f"  [{mark}] {label}: {question}")
    if note:
        print(f"          {note}")
    if leaked:
        fails.append(f"AX-derivable:{label}")

# H1: s0 of four partitions of 22.  Derivable only by RUNNING the Havel-Hakimi process
# of A.0 on a list built by (C-2).  Leak routes: (i) a closed form for s0; (ii) a printed
# s0 value for any partition of 22; (iii) an s0 table extending past nu = 10.
s0_rows = re.findall(r"s0\(\[([0-9+,\s]+)\]\)\s*=\s*(\d+)", text)
part22 = [(p, v) for p, v in s0_rows
          if sum(int(x) for x in re.findall(r"\d+", p)) == 22]
closed_form_s0 = has(r"s0\(lam\)\s*=\s*[^s].{0,40}(formula|closed form)")
q("H1", f"printed s0 values for partitions of 22 = {len(part22)}; closed form for s0 = {closed_form_s0}",
  bool(part22) or closed_form_s0,
  "s0 is defined only as the OUTPUT of the A.0 run; no formula is printed anywhere.")

# H2: DELIBERATELY derivable.  The closed form S(nu) is printed on purpose; the row is
# HAND tier for exactly that reason.  Assert the DESIGN, do not pass it by accident.
closed_S = has(r"S\(nu\)|S\(ν\)")
q("H2", f"closed form for S(nu) printed = {closed_S} -- this row is MEANT to be derivable",
  not closed_S,
  "B6: H2 tests fabrication (will it evaluate a printed formula honestly), not capacity. "
  "If the formula were absent, H2 would be miscategorised as a HAND row it cannot reach.")

# H3/H4: must NOT be derivable.  The only route to a survivor count is enumeration; the
# check is that no closed form / recurrence / extrapolable table for survivor counts is
# printed, and that the brief says extrapolation grades WRONG.
surv_closed = has(r"surviv[a-z]*\s+(count|number)s?[^.]{0,40}(closed form|formula|recurrence)"
                  r"|(closed form|formula|recurrence)[^.]{0,40}surviv[a-z]*\s+(count|number)")
warns_extrap = re.search(r"Do not extrapolate a pattern", text) is not None
q("H3", f"closed form or recurrence for SURVIVOR counts printed = {surv_closed}; "
        f"anti-extrapolation warning present = {warns_extrap}",
  surv_closed or not warns_extrap,
  "The published survivor counts 0,1,4,9,20,38,75,137,251,447 have no closed form in "
  "this document; extrapolation is the derivability route and it is named and penalised.")

hist = has(r"histogram|#\{lam.{0,30}s0")
q("H4", f"any s0 histogram over partitions printed = {hist}",
  hist,
  "H4 needs 1002 separate runs; no distributional data over partitions appears.")

# H5: one explicit shape.  Leak = the shape itself printed anywhere.
shape = has(r"5\+4\+4\+3\+3|\[5,\s?4,\s?4,\s?3,\s?3\]")
nu11row = has(r"nu\s?=\s?11.{0,40}L\s?=\s?13|ν\s?=\s?11.{0,40}L\s?=\s?13")
q("H5", f"the shape lam=[5,4,4,3,3] printed = {shape}; a nu=11 L=13 row printed = {nu11row}",
  shape or nu11row)

# global: no nu = 11 DATA anywhere (only the Section 0 prose that names the value)
nu11_data = [ln for ln in BODY.splitlines()
             if re.search(r"(nu|ν)\s?=\s?11", ln) and re.search(r"\|", ln)
             and "held-out" not in ln.lower()]
q("GLOBAL", f"table rows carrying nu = 11 data = {len(nu11_data)}", bool(nu11_data))

# ============================================================ GATE 3 -- B6 role-of-object
print("\n=== GATE 3 : B6 by ROLE OF OBJECT (RULING AU) ===")
uses = {
    "the nu <= 10 survivor rosters (C-5)": r"\(C-5\)",
    "the nu = 7..10 rosters (C-8)":        r"\(C-8\)",
    "the boundary rows (C-3)":             r"\(C-3\)",
    "the closed form S(nu)":               r"S\(nu\)|S\(ν\)",
    "the published counts 0,1,4,9,20":     r"0,1,4,9,20|0,\s?1,\s?4,\s?9,\s?20",
}
for name, pat in uses.items():
    hit = has(pat)
    print(f"  DISCLOSED (target must USE)  {name:38s} present={hit}  (want True)")
    if not hit:
        fails.append(f"B6-disclosure:{name}")

print("  HELD OUT (no mathematical role in the target):")
print("    every held-out row lives at nu = 11 or at partitions of 22.")
print("    Theorem GFANnu's range is 1 <= nu <= 10 and the corollary's conclusion is")
print("    nu >= 11 -- so nu = 11 data is test material the target's proof never touches.")
print("    Same quantity family, disclosed where it is an INPUT, held out where it is a TEST.")
sec0 = re.search(r"Every one of them lives at \*\*`nu = 11`\*\*", SEC0) is not None
print(f"    the brief states that boundary to the judge : {sec0}  (want True)")
if not sec0:
    fails.append("B6-boundary-disclosure")

# ============================================================
print("\n" + "=" * 70)
if fails:
    print("GATE RESULT: FAIL -- " + ", ".join(fails))
    sys.exit(1)
print("GATE RESULT: ALL THREE GATES PASS -- brief is dispatchable")
sys.exit(0)
