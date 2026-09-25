#!/usr/bin/env python3
"""
w133 round 29 -- RULING DA GATE: is any held-out answer GREPPABLE from the surface we point
the reviewer at?

WHY (planner, mid-round).  677 r32 found two of three computational rows on its flagship
held-out table answerable by grep -- not from the brief, but from a log file in a directory the
brief told the reviewer to sweep, one of which printed the row's exact answer verbatim.  Its
row-quality gates all passed and none of them asked this question.

WHAT THIS ASSERTS.  For every held-out row: no rendering of its answer occurs anywhere on the
REACHABLE SURFACE -- the shipped bytes plus every filesystem/repo path or URL the brief names --
in an ANSWER-SHAPED CONTEXT (within a window of one of the row's own subject tokens).

RULING CZ AS DA REQUIRES IT.  A bare-digit positive control certifies almost nothing here: these
answers are small integers.  So each of the FOUR detectors is controlled with a DERIVED or
REFORMATTED planting -- an equation, a slash-reformatted tuple, a sum, and a per-component
equation set -- and a negative control asserts the gate is not simply always-on.

RULING CY.  The gate is shown both PASSING (on the real brief, if it is clean) and FAILING (on
five plantings), because a check that cannot pass is as uninformative as one that cannot fail.

Usage:  python3 problems/wowii/w133_r29_da_gate.py <brief.md> <key.key.txt> [--label NAME]
"""
import os, re, sys

W = 140          # context half-window, characters
MINUS = "−"

FAIL = []; NCHK = [0]
def check(label, got, want):
    NCHK[0] += 1
    ok = (got == want)
    print("  [%s] %-70s got=%s want=%s" % ("OK" if ok else "FAIL", label, got, want))
    if not ok: FAIL.append(label)
    return ok

# --------------------------------------------------------------------------- answer renderings
def ints_in(s):
    return [int(m.group(0).replace(MINUS, "-").replace(" ", "").replace(",", ""))
            for m in re.finditer(r"[-%s]?\d{1,3}(?:[ ,]\d{3})*" % MINUS, s)]

def groups_in(s):
    """Every BRACKETED or SLASH-SEPARATED numeric group, as a tuple of ints.  This is the
    'reformatted tuple' species: (3, 1, 1, 1) and 3/1/1/1 are the same answer."""
    out = []
    for m in re.finditer(r"\(([^()\n]{1,80})\)", s):
        nums = re.findall(r"-?\d+", m.group(1).replace(MINUS, "-"))
        if len(nums) >= 2:
            out.append(tuple(int(x) for x in nums))
    for m in re.finditer(r"(?<![\w.])(-?\d+(?:\s*/\s*-?\d+){1,5})(?![\w.])", s):
        try:
            out.append(tuple(int(p.strip()) for p in m.group(1).split("/")))
        except ValueError:
            pass
    return out

CUE = r"(?:=|:|\bis\b|\breads\b|\btotal\b|\bcount\b|\bequals\b|\bgives\b)"


def sums_in(s):
    """x + y (+ z) evaluated, but ONLY where the expression is itself presented AS a value
    (a cue within 30 chars before it).  The 'derived value' species: an answer never printed
    but trivially reconstructible from two adjacent printed numbers.  The answer itself is
    absent by construction, so this detector must NOT also require the answer to be
    value-shaped -- that is what made its first version unable to fire at all (RULING CY)."""
    out = []
    for m in re.finditer(r"(-?\d+)(\s*\+\s*(-?\d+)){1,3}", s):
        pre = s[max(0, m.start() - 30):m.start()]
        if re.search(CUE + r"[^.]{0,20}$", pre):
            out.append(sum(int(x) for x in re.findall(r"-?\d+", m.group(0))))
    return out

def contiguous_sub(t, big):
    n = len(t)
    return any(big[i:i + n] == t for i in range(len(big) - n + 1))

# --------------------------------------------------------------------------------- the detectors
VALUE_SHAPED = r"(?:=|:|\bis\b|\breads\b|\btotal\b|\bcount\b|\bequals\b)\s*[*`]*\s*%s\b|\b%s\s+(?:edges|vertices|occurrences|files)\b"


def value_shaped(n, window):
    """RULING DA + the r26 G1 lesson: a BARE DIGIT near the host name is not a leak -- these
    answers are single small integers and a 35 KB brief is full of digits.  A leak is a
    VALUE-SHAPED rendering: the number presented AS the value of something."""
    pat = VALUE_SHAPED % (re.escape(str(n)), re.escape(str(n)))
    return bool(re.search(pat, window))


def detect(ans, comps, window, quants):
    """Returns the set of detector ids that fire on this window.  A window with no QUANTITY
    token in it is not answer-shaped and is not scanned."""
    fired = set()
    if quants and not any(q in window for q in quants):
        return fired
    if isinstance(ans, tuple):
        gs = groups_in(window)
        if any(g == ans or contiguous_sub(ans, g) for g in gs):
            fired.add("D-B/group")
        if comps:
            got = 0
            for nm, val in zip(comps, ans):
                pat = re.escape(nm) + r"`?\s*(?:=|:|is)\s*`?\s*" + re.escape(str(val))
                if re.search(pat, window):
                    got += 1
            if got == len(ans):
                fired.add("D-D/percomponent")
    else:
        if ans in ints_in(window) and value_shaped(ans, window):
            fired.add("D-A/integer")
        if ans in sums_in(window):
            fired.add("D-C/sum")
    return fired

def scan(text, rows, surface_name):
    hits = []
    for r in rows:
        for sub in r["subjects"]:
            for m in re.finditer(re.escape(sub), text):
                lo = max(0, m.start() - W); hi = min(len(text), m.end() + W)
                win = text[lo:hi]
                f = detect(r["ans"], r.get("comps"), win, r.get("quants"))
                if f:
                    hits.append((r["rid"], surface_name, sorted(f), sub,
                                 win.replace("\n", " ")[:170]))
    return hits

# ----------------------------------------------------------------------------- key parsing
def load_rows(keypath):
    rows = []
    for line in open(keypath, encoding="utf-8"):
        parts = line.rstrip("\n").split("\t")
        if len(parts) >= 4 and parts[0].startswith("V"):
            rid, tier, q, ansraw = parts[0], parts[1], parts[2], parts[3]
            try:
                ans = eval(ansraw, {"__builtins__": {}})
            except Exception:
                ans = ansraw
            subs = sorted({t for t in re.findall(r"K\d", q)}) or ["K1"]
            KEYS = ["number of edges", "degree of vertex", "longest induced path",
                    "trace census", "4-cycle", "maximum degree", "T_Z", "n_3",
                    "a(v)-3", "|W_1|", "W_cons", "W_anti", "W_0", "a(7)", "edges",
                    "degree", "census", "induced path"]
            quants = [k for k in KEYS if k in q]
            subs = subs + quants
            comps = None
            if "W_1" in q and "W_0" in q:
                comps = ["|W_1|", "|W_cons|", "|W_anti|", "|W_0|"]
            rows.append(dict(rid=rid, tier=tier, q=q, ans=ans, subjects=subs,
                             comps=comps, quants=quants))
    return rows

# --------------------------------------------------------------------------------------- main
BRIEF = sys.argv[1]
KEY = sys.argv[2]
LABEL = sys.argv[sys.argv.index("--label") + 1] if "--label" in sys.argv else os.path.basename(BRIEF)

text = open(BRIEF, encoding="utf-8").read()
rows = load_rows(KEY)
print("=" * 92)
print("RULING DA GATE -- surface: %s   rows: %d" % (LABEL, len(rows)))
print("=" * 92)

# --- 1. THE REACHABLE SURFACE, enumerated (CG/CP: never probed for absence) -----------------
print()
print("1. THE REACHABLE SURFACE, enumerated -- the shipped bytes PLUS every path/URL named")
paths = set()
for m in re.finditer(r"(?:https?://\S+|(?:[A-Za-z0-9_.~-]+/){1,6}[A-Za-z0-9_.~-]+\.[A-Za-z0-9]{1,5}"
                     r"|`[A-Za-z0-9_./-]+\.(?:py|md|out|txt|json|c|lean)`)", text):
    p = m.group(0).strip("`")
    if re.match(r"^\d+/\d", p):        # 8/9, 406/738 -- fractions, not paths
        continue
    paths.add(p)
print("   path-shaped / URL tokens named by the brief: %s" % (sorted(paths) or "NONE"))
surfaces = [(LABEL, text)]
unresolved = []
for p in sorted(paths):
    if p.startswith("http"):
        unresolved.append(p); continue
    for base in ("", os.path.expanduser("~/workspace/claudecode/automath/")):
        fp = base + p
        if os.path.isfile(fp):
            surfaces.append((p, open(fp, encoding="utf-8", errors="replace").read())); break
        if os.path.isdir(fp):
            for fn in sorted(os.listdir(fp))[:200]:
                q = os.path.join(fp, fn)
                if os.path.isfile(q):
                    surfaces.append((p + "/" + fn,
                                     open(q, encoding="utf-8", errors="replace").read()))
            break
    else:
        unresolved.append(p)
print("   surfaces actually read: %d  (%s)" % (len(surfaces), ", ".join(s[0] for s in surfaces)))
print("   named-but-unresolvable (a reviewer could not reach these either): %s"
      % (unresolved or "NONE"))
check("the brief names no unresolved repository path", unresolved, [])

# --- 2. POSITIVE CONTROLS -- DERIVED forms, per RULING CZ as DA requires --------------------
print()
print("2. POSITIVE CONTROLS -- each detector planted in a DERIVED / REFORMATTED form.")
print("   A bare-digit control certifies nothing here: these answers are small integers.")
introw = next((r for r in rows if isinstance(r["ans"], int)), None)
tuprow = next((r for r in rows if isinstance(r["ans"], tuple) and len(r["ans"]) == 2
               and all(isinstance(x, int) for x in r["ans"])), None)
cenrow = next((r for r in rows if r.get("comps")), None)

if introw:
    a = introw["ans"]; k = introw["subjects"][0]
    q0 = (introw.get("quants") or ["edges"])[0]
    p1 = ("... %s: the %s figure -- one checks n = 11 and the number of edges = %d ..."
          % (k, q0, a))
    check("P1 D-A/integer FIRES on an EQUATION planting (m = %d, not bare digits)" % a,
          bool(scan(p1, [introw], "P1")), True)
    p3 = ("... in %s the %s count is %d + %d across the two halves ..." % (k, q0, a - 3, 3))
    check("P3 D-C/sum FIRES on a SUM planting (%d + %d, the value never printed)" % (a - 3, 3),
          any("D-C/sum" in h[2] for h in scan(p3, [introw], "P3")), True)
    pn = "... %s: the %s figure is unrelated, the count = %d ..." % (k, q0, a + 37)
    check("N1 NEGATIVE control: unrelated numbers near the same subject do NOT fire",
          bool(scan(pn, [introw], "N1")), False)
if tuprow:
    t = tuprow["ans"]; k = tuprow["subjects"][0]
    tq = (tuprow.get("quants") or ["T_Z"])[0]
    p2 = ("... for %s the %s pair reads %d/%d in the compact notation ..." % (k, tq, t[0], t[1]))
    check("P2 D-B/group FIRES on a SLASH-REFORMATTED tuple (%d/%d)" % t,
          any("D-B/group" in h[2] for h in scan(p2, [tuprow], "P2")), True)
    p2b = "... %s %s row: (path 6, %d, %d, admitted) ..." % (k, tq, t[0], t[1])
    check("P2b D-B/group FIRES on the answer EMBEDDED IN A LARGER TUPLE",
          any("D-B/group" in h[2] for h in scan(p2b, [tuprow], "P2b")), True)
if cenrow:
    c = cenrow["ans"]; k = cenrow["subjects"][0]
    p4 = ("... %s trace census: |W_1| = %d, |W_cons| = %d, |W_anti| = %d, |W_0| = %d ..."
          % (k, c[0], c[1], c[2], c[3]))
    check("P4 D-D/percomponent FIRES when the tuple is split into per-component equations",
          any("D-D/percomponent" in h[2] for h in scan(p4, [cenrow], "P4")), True)

# --- 3. THE REAL SCAN ------------------------------------------------------------------------
print()
print("3. THE SCAN over every surface")
allhits = []
for nm, txt in surfaces:
    h = scan(txt, rows, nm)
    allhits += h
    print("   %-42s %7d bytes   hits: %d" % (nm, len(txt.encode()), len(h)))
if allhits:
    print()
    print("   HITS (each is a BLOCKER, not a note):")
    seen = set()
    for rid, sn, f, sub, ctx in allhits:
        k = (rid, sn, tuple(f))
        if k in seen: continue
        seen.add(k)
        print("     %-4s on %-28s via %-16s near %r" % (rid, sn, ",".join(f), sub))
        print("          ...%s..." % ctx)
by_row = sorted({h[0] for h in allhits})
check("NO held-out row is answerable from the reachable surface", by_row, [])
print()
print("checks: %d, failures: %d" % (NCHK[0], len(FAIL)))
for f in FAIL: print("   FAIL %s" % f)
sys.exit(2 if FAIL else 0)
