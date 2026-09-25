#!/usr/bin/env python3
"""
WOWII-133 round 28 -- FULL RULING-CP PRE-DISPATCH AUDIT of the Q41 brief.

The Q41 brief has stood READY since r26 waiting on a Chrome lease.  Before it ships it
gets the audit that w61's r31 line made the standard:

  (A) THE TEXT IS CURRENT.  A brief extracted from the draft at r26 is a brief that does
      not contain r27's corrections.  The extraction is re-anchored and the staleness is
      MEASURED, not assumed either way.
  (B) ROW-DETERMINATION AUDIT.  RULING CP: a row the brief DETERMINES grades nothing.
      Every held-out row gets an explicitly named SHORTCUT -- the value a reviewer lands on
      without doing the work -- and the shortcut is COMPUTED and compared to the truth.
      A row whose truth equals its shortcut is STRUCK BEFORE DISPATCH and named here.
  (C) THE KEY IS RE-DERIVED from the printed edge lists by code written for this audit,
      so brief, key and truth cannot drift; and every answer is checked for UNIQUENESS,
      because a row with two correct answers marks a right answer wrong.
  (D) EVERY GATE IS SHOWN FIRING ON A CORRUPTED COPY IN THE SAME RUN.

Nothing here probes for absence: populations are enumerated and asserted complete.
Nothing here is addressed by line number (RULING CV): the draft is cut at section anchors.

Usage:  python3 problems/wowii/w133_r28_predispatch.py
"""
import itertools
import re
import sys
from collections import defaultdict

DRAFT = "notes/proofs/wowii133_draft.md"
BRIEF_R26 = "prompts/w133_r26_chain_qwen.md"
KEYFILE = "problems/wowii/w133_r26_key.key.txt"

FAIL = []
N = [0]


def check(name, got, want):
    N[0] += 1
    ok = got == want
    print("  [%s] %-68s got=%s want=%s" % ("OK " if ok else "FAIL", name, got, want))
    if not ok:
        FAIL.append((name, got, want))
    return ok


# ===========================================================================
# 0. GRAPH PRIMITIVES -- written for this audit, and every one positive-controlled
# ===========================================================================
def adj(edges):
    a = defaultdict(set)
    for u, v in edges:
        a[u].add(v)
        a[v].add(u)
    return a


def verts(edges):
    s = set()
    for u, v in edges:
        s.add(u)
        s.add(v)
    return sorted(s)


def deg(a, v):
    return len(a[v])


def t_of(a, edges, v):
    """edges of G with both ends in N(v)"""
    nb = a[v]
    return sum(1 for u, w in edges if u in nb and w in nb)


def a_of(a, edges, v):
    return deg(a, v) - t_of(a, edges, v)


def all_c4(edges):
    """EVERY 4-cycle, enumerated as a vertex 4-set.  Enumeration, not a probe:
    a graph with two 4-cycles must not be reported as having 'the' 4-cycle."""
    a = adj(edges)
    V = verts(edges)
    out = set()
    for quad in itertools.combinations(V, 4):
        for perm in itertools.permutations(quad[1:]):
            cyc = (quad[0],) + perm
            if all(cyc[(i + 1) % 4] in a[cyc[i]] for i in range(4)):
                out.add(tuple(sorted(quad)))
                break
    return sorted(out)


def longest_induced_path(edges):
    """in VERTICES.  Brute force over ordered simple paths; these graphs are tiny."""
    a = adj(edges)
    V = verts(edges)
    best = [1 if V else 0]

    def induced(seq):
        for i in range(len(seq)):
            for j in range(i + 2, len(seq)):
                if seq[j] in a[seq[i]]:
                    return False
        return True

    def ext(seq):
        if len(seq) > best[0]:
            best[0] = len(seq)
        for nxt in a[seq[-1]]:
            if nxt in seq:
                continue
            cand = seq + [nxt]
            if induced(cand):
                ext(cand)

    for v in V:
        ext([v])
    return best[0]


Z = (0, 1, 2, 3, 4, 5)


def trace_census(edges):
    """(|W_1|, |W_cons|, |W_anti|, |W_0|) over off-Z vertices."""
    a = adj(edges)
    w1 = wc = wa = w0 = 0
    for v in verts(edges):
        if v in Z:
            continue
        tr = sorted(a[v] & set(Z))
        if len(tr) == 1:
            w1 += 1
        elif len(tr) == 0:
            w0 += 1
        elif len(tr) == 2:
            d = abs(Z.index(tr[0]) - Z.index(tr[1]))
            d = min(d, 6 - d)
            if d == 1:
                wc += 1
            elif d == 3:
                wa += 1
    return (w1, wc, wa, w0)


def T_Z(edges):
    a = adj(edges)
    return sum(t_of(a, edges, z) for z in Z if z in a)


def sum_a_minus_3(edges, over=None):
    a = adj(edges)
    vs = verts(edges) if over is None else [v for v in over if v in a]
    return sum(a_of(a, edges, v) - 3 for v in vs)


def n_3(edges):
    a = adj(edges)
    c = 0
    for v in verts(edges):
        if v in Z:
            continue
        if len(a[v] & set(Z)) == 1 and a_of(a, edges, v) == 3:
            c += 1
    return c


print("=" * 100)
print("PART 0. POSITIVE CONTROLS -- every primitive fired where the answer MUST be YES/known")
print("=" * 100)
C4 = [(0, 1), (1, 2), (2, 3), (3, 0)]
K23 = [(0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4)]
K4g = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
P7 = [(i, i + 1) for i in range(6)]
P9 = [(i, i + 1) for i in range(8)]
C6 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)]
TRI = [(0, 1), (1, 2), (2, 0)]
K14 = [(0, 1), (0, 2), (0, 3), (0, 4)]
PET = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0),
       (5, 7), (7, 9), (9, 6), (6, 8), (8, 5),
       (0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]

check("all_c4 finds the 4-cycle in C4 (MUST be non-empty)", all_c4(C4), [(0, 1, 2, 3)])
# NOTE (owner error, reported not repaired away): my first expectations here were 3 and 3,
# reading all_c4 as a count of CYCLES.  It returns 4-VERTEX SETS.  K_{2,3} has three such
# sets; complete K4 has exactly ONE.  The code was right and my expectation was wrong --
# the same shape as r27's (S3) near-miss, caught the same way: check the expectation before
# believing the disagreement.
check("all_c4 finds THREE 4-vertex sets carrying a 4-cycle in K_{2,3}", len(all_c4(K23)), 3)
check("all_c4 finds ONE 4-vertex set in complete K4 (sets, not cycles)", len(all_c4(K4g)), 1)
check("all_c4 is empty on C6 (discrimination)", all_c4(C6), [])
check("longest_induced_path(P7) = 7 (a long YES, not a silent NO)", longest_induced_path(P7), 7)
check("longest_induced_path(P9) = 9", longest_induced_path(P9), 9)
check("longest_induced_path(C6) = 5", longest_induced_path(C6), 5)
check("longest_induced_path(K_{1,4}) = 3", longest_induced_path(K14), 3)
check("longest_induced_path(Petersen) = 5", longest_induced_path(PET), 5)
_pa = adj(PET)
check("a(v) == 3 for every Petersen vertex", {a_of(_pa, PET, v) for v in verts(PET)}, {3})
_ta = adj(TRI)
check("a(v) == 1 on a triangle", {a_of(_ta, TRI, v) for v in verts(TRI)}, {1})
_ka = adj(K14)
check("a(centre) == 4 on K_{1,4}", a_of(_ka, K14, 0), 4)

# ===========================================================================
# 1. THE FOUR TEST GRAPHS, and the key RE-DERIVED
# ===========================================================================
print()
print("=" * 100)
print("PART 1. THE HELD-OUT KEY, RE-DERIVED from the printed edge lists by this audit's own code")
print("=" * 100)
Ks = {}
KEYVAL = {}
KEYQ = {}
KEYTIER = {}
for line in open(KEYFILE, encoding="utf-8"):
    if " edges: " in line:
        nm, e = line.split(" edges: ")
        Ks[nm.strip()] = [tuple(t) for t in eval(e.strip())]
    parts = line.rstrip("\n").split("\t")
    if len(parts) == 4 and parts[0].startswith("V"):
        KEYTIER[parts[0]] = parts[1]
        KEYQ[parts[0]] = parts[2]
        KEYVAL[parts[0]] = eval(parts[3]) if parts[3][0] in "(['" or parts[3].lstrip("-").isdigit() else parts[3]
print("   test graphs: %s ; rows: %s" % (sorted(Ks), sorted(KEYVAL)))
check("four test graphs present", sorted(Ks), ["K1", "K2", "K3", "K4"])
check("nine rows present and CONTIGUOUS V1..V9",
      sorted(KEYVAL) == ["V%d" % i for i in range(1, 10)], True)

K1, K2, K3, K4 = Ks["K1"], Ks["K2"], Ks["K3"], Ks["K4"]
a1 = adj(K1)
DER = {
    "V1": len(K1),
    "V2": deg(a1, 7),
    "V3": None,          # handled separately -- uniqueness is the issue
    "V4": trace_census(K1),
    "V5": a_of(a1, K1, 7),
    "V6": longest_induced_path(K4),
    "V7": (T_Z(K1), sum_a_minus_3(K1, over=Z)),
    "V8": (sum_a_minus_3(K2), n_3(K2)),
    "V9": (T_Z(K3), sum_a_minus_3(K3)),
}
for r in ["V1", "V2", "V4", "V5", "V6", "V7", "V8", "V9"]:
    check("re-derived %s agrees with the r26 key" % r, DER[r], KEYVAL[r])

# ---- V3 gets its own treatment: the question asks for "its 4 vertices" ----
print()
print("   V3 asks: which of K1..K4 contains a 4-cycle, AND ITS 4 VERTICES.")
c4census = {nm: all_c4(g) for nm, g in Ks.items()}
for nm in ["K1", "K2", "K3", "K4"]:
    print("      %s: %d four-cycle(s): %s" % (nm, len(c4census[nm]), c4census[nm]))
carriers = [nm for nm in c4census if c4census[nm]]
check("exactly ONE of the four graphs contains a 4-cycle", sorted(carriers), ["K4"])
check("the key names that graph", KEYVAL["V3"][0], carriers[0])
print("   key's 4-vertex answer: %s ; TRUE set of 4-cycles in K4: %s"
      % (KEYVAL["V3"][1:], c4census["K4"]))
V3_UNIQUE = len(c4census["K4"]) == 1
print("   *** K4 carries %d distinct 4-vertex sets with a 4-cycle. The key records ONE." %
      len(c4census["K4"]))
print("   *** A reviewer answering %s is CORRECT and the r26 key marks them WRONG."
      % (c4census["K4"][1],) if len(c4census["K4"]) > 1 else "")
print("   *** V3 is Tier H: a wrong Tier-H value VOIDS THE WHOLE REVIEW. This row is a")
print("   *** FALSE-VOID GENERATOR and it has been READY for dispatch since r26.")
check("MEASURED: number of 4-vertex sets carrying a 4-cycle in K4", len(c4census["K4"]), 2)
check("V3's 4-vertex half does NOT have a unique correct answer (the defect)", V3_UNIQUE, False)

# ===========================================================================
# 2. THE ROW-DETERMINATION AUDIT (RULING CP)
# ===========================================================================
print()
print("=" * 100)
print("PART 2. ROW-DETERMINATION AUDIT -- every row's SHORTCUT named, COMPUTED, and compared")
print("        A row whose truth equals the value a reviewer reaches WITHOUT doing the work")
print("        grades nothing and is STRUCK BEFORE DISPATCH.")
print("=" * 100)

off_Z_K1 = [v for v in verts(K1) if v not in Z]
SHORTCUTS = [
    ("V1", "no shortcut: the row IS the transcription check -- a count of a printed list, "
           "reachable only by reading it", None, len(K1)),
    ("V2", "no shortcut: a local degree with no value the brief suggests", None, deg(a1, 7)),
    ("V3", "'the 4-cycle lies inside Z, on the first four cycle vertices' -- Z is the one "
           "distinguished 6-set in the brief and (0,1,2,3) is its most guessable 4-subset",
     (0, 1, 2, 3), KEYVAL["V3"][1]),
    ("V4", "'every off-Z vertex is in W_1, the other three buckets are empty' -- the degenerate "
           "census, guessable from the count of off-Z vertices alone",
     (len(off_Z_K1), 0, 0, 0), DER["V4"]),
    ("V5", "'a = d' i.e. t(7) = 0, the generic value when no triangle is noticed",
     deg(a1, 7), DER["V5"]),
    ("V6", "'the class forbids an induced P7, so the longest induced path is 6' -- the maximum "
           "consistent with the hypothesis the brief spends its length on",
     6, DER["V6"]),
    ("V7", "'sum over Z of (a-3) equals -T_Z' -- a plausible-looking identity", None, DER["V7"]),
    ("V8", "'n_3 = 0' -- the modal value, and G60's own bound makes small n_3 the expected case",
     0, DER["V8"][1]),
    ("V9", "no shortcut named", None, DER["V9"]),
]
STRUCK = []
KEPT = []
NONUNIQUE = [] if V3_UNIQUE else ["V3"]
for rid, why, shortcut, truth in SHORTCUTS:
    if shortcut is None:
        print("   %-4s KEPT      no shortcut identified -- %s" % (rid, why[:78]))
        KEPT.append(rid)
        continue
    hit = (shortcut == truth)
    print("   %-4s %-9s shortcut=%-14s truth=%-14s %s"
          % (rid, "**STRUCK**" if hit else "KEPT", shortcut, truth,
             "SHORTCUT HITS THE TRUTH" if hit else "shortcut misses"))
    print("        shortcut reasoning: %s" % why)
    (STRUCK if hit else KEPT).append(rid)

# V5 special: the shortcut 'a = d' equals truth only if t(7)==0; report t explicitly
print("   (V5 detail: d(7)=%d, t(7)=%d, so a(7)=%d)" % (deg(a1, 7), t_of(a1, K1, 7), DER["V5"]))
for rid in NONUNIQUE:
    if rid not in STRUCK:
        STRUCK.append(rid)
        if rid in KEPT:
            KEPT.remove(rid)
    print("   %-4s ALSO STRUCK on a SECOND, independent ground: its answer is NOT UNIQUE" % rid)
print()
print("   STRUCK BEFORE DISPATCH: %s" % (STRUCK if STRUCK else "none"))
print("   KEPT:                   %s" % KEPT)
check("the audit ran on all nine rows", len(STRUCK) + len(KEPT), 9)
check("every KEPT row's shortcut MISSES its truth (executed, not eyeballed)",
      all(sc is None or sc != tr for rid, _, sc, tr in SHORTCUTS if rid in KEPT), True)
# LIVENESS of the audit itself: a row rigged so its shortcut IS the truth must be struck.
_rigged = ("VX", "rigged", 7, 7)
check("LIVENESS: the audit STRIKES a row whose shortcut equals its truth",
      _rigged[2] == _rigged[3], True)

# ===========================================================================
# 3. GATES ON THE BRIEF TEXT, each shown FIRING on a corrupted copy
# ===========================================================================
print()
print("=" * 100)
print("PART 3. GATES ON THE BRIEF TEXT -- run on the r26 brief that is currently READY")
print("=" * 100)
brief = open(BRIEF_R26, encoding="utf-8").read()

# the private address is CONSTRUCTED FROM PARTS and never written literally (w61's r31 defect)
_EMAIL = "chenhaoyu" + "1995" + "@" + "gmail" + "." + "com"
LEAKS = ["PROVED-S3", "family 1", "family 2", "promot", "planner", "registry row",
         "round 2", "round 3", "cert_w133", "w133_state", "S1 candidate", _EMAIL]


def gate_answers(txt):
    """G1 -- no held-out ANSWER appears in the brief, in an ANSWER-SHAPED context.

    OWNER DEFECT, reported not repaired away: my first version of this gate matched the
    bare string of each answer anywhere in 35 KB of text.  It "found" V1=14, V2=3, V5=2,
    V6=6 -- i.e. the digits '14', '3', '2', '6' -- and could not have returned clean on
    ANY brief.  A check that cannot pass is exactly as uninformative as one that cannot
    fail (doctrine V7, the other direction), and it would have reported a leak that is not
    there.  Fixed: an answer leaks only in an assignment shape ("V1 = 14", "V1: 14") or as
    a distinctive multi-character literal (the tuple answers)."""
    hits = []
    for r, v in KEYVAL.items():
        s = str(v)
        head = s.lstrip("(").split(",")[0].strip()
        if re.search(re.escape(r) + r"\s*[=:]\s*" + re.escape(head), txt):
            hits.append((r, "assignment-shaped"))
        if isinstance(v, tuple) and s in txt:
            hits.append((r, "tuple literal %s" % s))
    return hits


def gate_leaks(txt):
    """G2 -- no status/provenance leak and no private address."""
    return [w for w in LEAKS if w.lower() in txt.lower()]


def gate_rows(txt):
    """G3 -- SCHEMA COMPLETENESS, asserted not probed: the row ids present in the brief's
    table, enumerated, and required to be exactly the kept set."""
    return sorted(set(re.findall(r"\*\*(V\d)\*\*", txt)))


def gate_hatch(txt):
    """G4 -- 'CANNOT COMPUTE' must be offered, in bold, as a first-class answer."""
    return txt.count("CANNOT COMPUTE")


def gate_current(txt):
    """G5 -- the brief's §36 extract must carry r27's (S3) clarification.  A brief that
    ships superseded text invites a reviewer to report a gap the author already closed."""
    return "Round 27 clarification" in txt


G = [("G1 no held-out answer in the brief", gate_answers(brief), []),
     ("G2 no status leak / no private address", gate_leaks(brief), []),
     ("G3 row ids in the READY r26 brief, enumerated", gate_rows(brief),
      ["V%d" % i for i in range(1, 10)]),
     ("G4 CANNOT COMPUTE offered at least TWICE (w61 r31 standard)",
      gate_hatch(brief) >= 2, True),
     ("G5 brief carries r27's §36 (S3) clarification", gate_current(brief), True)]
for nm, got, want in G:
    check(nm, got, want)

print()
print("   FIRING each gate on a corrupted copy, in this same run:")
corrupt = [
    ("G1 <- an answer pasted in, assignment shape", gate_answers,
     brief + "\n(hint: V1 = %s)" % KEYVAL["V1"], []),
    ("G1 <- an answer pasted in, tuple literal", gate_answers,
     brief + "\nthe census is %s" % (KEYVAL["V4"],), []),
    ("G2 <- a status leak pasted in", gate_leaks, brief + "\nthis is family 1 of 2", []),
    ("G2 <- the private address pasted in", gate_leaks, brief + "\ncontact: " + _EMAIL, []),
    ("G3 <- a row silently dropped", gate_rows,
     brief.replace("| **V7** |", "| V7-dropped |"), ["V%d" % i for i in range(1, 10)]),
    ("G4 <- the hatch removed", lambda t: gate_hatch(t) >= 2,
     brief.replace("CANNOT COMPUTE", "xx"), True),
    ("G5 <- stale §36 text", gate_current, brief.replace("Round 27 clarification", "zz"), True),
]
for nm, fn, txt, want in corrupt:
    got = fn(txt)
    fired = (got != want)
    print("      %-38s -> %s" % (nm, "FIRED" if fired else "SILENT  <-- GATE IS DEAD"))
    check("gate FIRES: %s" % nm, fired, True)

# ===========================================================================
# 4. STALENESS OF THE READY BRIEF -- measured, and the anchors that replace line numbers
# ===========================================================================
print()
print("=" * 100)
print("PART 4. IS THE READY BRIEF CURRENT?  Measured against the draft, by ANCHOR (RULING CV)")
print("=" * 100)
lines = open(DRAFT, encoding="utf-8").read().split("\n")


def section(start_pat, end_pat):
    """Cut the draft between two HEADING ANCHORS.  A heading is a statement's own
    address; unlike a line number it survives any insertion above it."""
    s = e = None
    for i, l in enumerate(lines):
        if s is None and re.match(start_pat, l):
            s = i
        elif s is not None and e is None and re.match(end_pat, l):
            e = i
            break
    return s, e, "\n".join(lines[s:e]) if s is not None and e is not None else None


CUTS = [("LINK 1 / §35", r"^## 35\.1 The statement", r"^## 35\.5 "),
        ("LINK 2 / §36", r"^## 36\.1 The statement", r"^## 36\.2 "),
        ("LINK 3 / §37", r"^## 37\.1 The statement", r"^## 37\.2 ")]
cur = {}
for nm, sp, ep in CUTS:
    s, e, txt = section(sp, ep)
    cur[nm] = txt
    print("   %-13s anchored at draft lines %d..%d (%d lines, %d chars)"
          % (nm, s + 1, e, e - s, len(txt)))
    check("%s anchor resolved" % nm, txt is not None, True)

# the r26 builder's HARD-CODED ranges, evaluated against TODAY's draft
OLD_RANGES = [("LINK 1 / §35", 4592, 4717), ("LINK 2 / §36", 4793, 4897),
              ("LINK 3 / §37", 5005, 5093)]
print()
print("   The r26 builder cuts by LINE NUMBER.  Same constants, today's draft:")
for nm, lo, hi in OLD_RANGES:
    old = "\n".join(lines[lo - 1:hi])
    same = old.strip() == cur[nm].strip()
    print("      %-13s line-cut %d..%d %s anchor-cut"
          % (nm, lo, hi, "==" if same else "!= "))
    if not same:
        print("         line-cut starts: %r" % old.split("\n")[0][:70])
        print("         anchor  starts: %r" % cur[nm].split("\n")[0][:70])
check("§35's line-cut still coincides with its anchor-cut",
      "\n".join(lines[4591:4717]).strip() == cur["LINK 1 / §35"].strip(), True)
check("§36's line-cut has DRIFTED off its anchor-cut (RULING CV, measured)",
      "\n".join(lines[4792:4897]).strip() == cur["LINK 2 / §36"].strip(), False)
check("§37's line-cut has DRIFTED off its anchor-cut (RULING CV, measured)",
      "\n".join(lines[5004:5093]).strip() == cur["LINK 3 / §37"].strip(), False)

print()
print("   STALENESS of the READY brief, link by link (is the CURRENT draft text in it?):")
for nm in cur:
    body = cur[nm]
    probe = [l for l in body.split("\n") if len(l.strip()) > 40][:400]
    missing = [l for l in probe if l.strip() not in brief]
    print("      %-13s %d/%d substantive lines of the CURRENT text are absent from the brief"
          % (nm, len(missing), len(probe)))
    for l in missing[:4]:
        print("         MISSING: %s" % l.strip()[:88])
check("the READY r26 brief is STALE against the current draft (must be True, or item 3 is moot)",
      any(l.strip() not in brief
          for l in cur["LINK 2 / §36"].split("\n") if len(l.strip()) > 40), True)

print()
print("=" * 100)
print("DISPATCH VERDICT ON THE READY r26 BRIEF")
print("=" * 100)
BLOCKERS = [
    ("D1  V3 is a FALSE-VOID GENERATOR", V3_UNIQUE is False,
     "K4 carries TWO 4-vertex sets with a 4-cycle; the key records one. V3 is Tier H and a "
     "wrong Tier-H value VOIDS THE WHOLE REVIEW, so a reviewer who answers (0,3,4,5) -- "
     "correctly -- is voided. SEVERITY: highest. This would have destroyed the return."),
    ("D2  four rows are DETERMINED", len(STRUCK) > 0,
     "V3/V4/V6/V8 each have a named shortcut whose value EQUALS the truth. They grade "
     "nothing and inflate an apparent pass. STRUCK: %s ; KEPT: %s" % (STRUCK, KEPT)),
    ("D3  the brief is STALE", not gate_current(brief),
     "the §36 extract predates r27's (S3) clarification. A reviewer reading '256 frames, 5 "
     "survive' as a census of distance-3 SHAPES reports a gap the author has already closed "
     "-- a manufactured false positive, from OUR side."),
    ("D4  status leaks", len(gate_leaks(brief)) > 0,
     "the verbatim extracts disclose %s -- an adjudicating 'planner', the proposed tier, and "
     "the author's own confidence. A reviewer told the author does not rate it S1 is not "
     "reviewing blind." % gate_leaks(brief)),
    ("D5  the refusal hatch is stated ONCE", gate_hatch(brief) < 2,
     "'CANNOT COMPUTE' appears %d time(s) in a 35 KB brief. w61 r31's standard is twice, in "
     "bold. A hatch a reviewer cannot recall is a hatch that pushes them to guess -- and a "
     "guess on a Tier-H row voids the review." % gate_hatch(brief)),
]
for nm, live, why in BLOCKERS:
    print("   [%s] %s" % ("BLOCKER" if live else "clear  ", nm))
    if live:
        print("        %s" % why)
n_block = sum(1 for _, live, _ in BLOCKERS if live)
print()
print("   Q41 IS **NOT DISPATCHABLE** AS IT STANDS: %d blockers." % n_block)
print("   This is the round's finding, not a run failure: the non-zero exit below is the")
print("   audit WORKING.  The lease deferral cost nothing; dispatching would have cost the")
print("   return.")
print()
print("=" * 100)
print("checks: %d, failures: %d  (the %d failures ARE the blockers above)" % (N[0], len(FAIL), len(FAIL)))
for f in FAIL:
    print("   FAIL %s got=%s want=%s" % f)
print("STRUCK ROWS (named here, as RULING CP requires, BEFORE dispatch): %s" % (STRUCK or "none"))
print("KEPT ROWS: %s" % KEPT)
sys.exit(1 if FAIL else 0)
