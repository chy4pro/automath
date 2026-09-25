#!/usr/bin/env python3
"""
w133 round 30 -- ADJUDICATION of the Q41 harvest against the HELD-OUT key.

Harvest provenance (OPS-14, and it is an INFERENCE of finish, not an eyewitness):
  conversation d977bb6f-91cb-486f-bfea-855e6a448d5d @ chat.qwen.ai, model `qwen3.8-max`
  read from the SERVER STORE (/api/v2/chats/{id}), assistant message 92a2fa85,
  content_list[phase="answer"], status "finished", message done=true, endTime present,
  childrenIds = [] (no continuation as of the read).
  in-page SHA-256 of the stored answer == shasum -a 256 of the on-disk harvest.

WHAT THIS FILE IS FOR, and what it deliberately does NOT do:
  It grades the SEVEN held-out rows.  It does NOT grade the prose verdict (P1/P2/P3/GAPS):
  that is engine output, it stays in the sandbox, and it is promoted to the draft only by
  rewrite after adjudication -- never copied.

RULING CZ  -- every gate is shown FIRING on a corrupted copy in the SAME RUN, and every
              corruption is the HARDEST form of its species, not a canonical one.
RULING CZ' -- the control must fire ON THE FEATURE, not merely on the instance string.
              Demonstrated concretely: a NAIVE whole-document comparator is run beside the
              real grader on the same corruptions.  For the value-preserving corruptions the
              naive comparator PASSES while the real grader FIRES.  If the naive comparator
              ever failed there too, the corruption would not have proved anything.
RULING CY  -- a check that cannot PASS is as uninformative as one that cannot fail.  Every
              predicate below is fired on an input where it MUST return the clean answer.

Exit 0 iff every control passes and every gate fires where it must.  Exit 2 otherwise.
"""
import sys, os, re, ast, hashlib, itertools

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
KEY = os.path.join(REPO, "problems", "wowii", "w133_r29_key.key.txt")
HARVEST = os.path.expanduser(
    "~/workspace/claudecode/automath-sandbox/logs/w133_r30/q41_harvest.txt")
EXPECT_SHA = "cafb0146c234eb6af15696639da2e53b081942616e5ca782f8496e354f9f3ad6"

FAIL = []
NCHK = [0]


def check(label, got, want):
    NCHK[0] += 1
    ok = (got == want)
    print("  [%s] %-70s got=%s want=%s" % ("OK" if ok else "FAIL", label, got, want))
    if not ok:
        FAIL.append(label)
    return ok


# ===================================================================== graph layer
# Re-implemented here rather than imported, so that agreement with r29's key is a
# CROSS-CHECK and not a tautology.  Definitions are the ones r29's key script uses.
class G:
    def __init__(self, n, edges):
        self.n = n
        self.adj = [set() for _ in range(n)]
        for a, b in edges:
            if a == b:
                raise ValueError("loop")
            self.adj[a].add(b)
            self.adj[b].add(a)

    def deg(self, v):
        return len(self.adj[v])

    def t(self, v):
        nb = sorted(self.adj[v])
        return sum(1 for i in range(len(nb)) for j in range(i + 1, len(nb))
                   if nb[j] in self.adj[nb[i]])

    def a(self, v):
        return self.deg(v) - self.t(v)

    def connected(self):
        seen = {0}
        st = [0]
        while st:
            u = st.pop()
            for w in self.adj[u]:
                if w not in seen:
                    seen.add(w)
                    st.append(w)
        return len(seen) == self.n


def has_C4(g):
    return any(len(g.adj[x] & g.adj[y]) >= 2
               for x, y in itertools.combinations(range(g.n), 2))


def longest_induced_path(g):
    best = 0

    def ext(path, pset):
        nonlocal best
        if len(path) > best:
            best = len(path)
        for w in g.adj[path[-1]]:
            if w in pset:
                continue
            if any(w in g.adj[u] for u in path[:-1]):
                continue
            path.append(w)
            pset.add(w)
            ext(path, pset)
            path.pop()
            pset.discard(w)

    for s in range(g.n):
        ext([s], {s})
    return best


def induced_C6(g, Z):
    if len(Z) != 6 or len(set(Z)) != 6:
        return False
    for i in range(6):
        for j in range(i + 1, 6):
            if (Z[j] in g.adj[Z[i]]) != (((j - i) % 6 == 1) or ((i - j) % 6 == 1)):
                return False
    return True


ZC = [0, 1, 2, 3, 4, 5]


def trace(g, v):
    return tuple(sorted(i for i, z in enumerate(ZC) if z in g.adj[v]))


def census(g):
    W1 = Wc = Wa = W0 = 0
    for v in range(g.n):
        if v in ZC:
            continue
        T = trace(g, v)
        if len(T) == 0:
            W0 += 1
        elif len(T) == 1:
            W1 += 1
        elif len(T) == 2:
            d = (T[1] - T[0]) % 6
            if d in (1, 5):
                Wc += 1
            elif d == 3:
                Wa += 1
            else:
                raise RuntimeError("illegal 2-trace")
        else:
            raise RuntimeError("trace too large")
    return (W1, Wc, Wa, W0)


def T_Z(g):
    return sum(g.t(z) for z in ZC)


def sumZ(g):
    return sum(g.a(z) - 3 for z in ZC)


def sumV(g):
    return sum(g.a(v) - 3 for v in range(g.n))


# ============================================ PART 0 -- POSITIVE CONTROLS (RULING CY)
print("=" * 96)
print("PART 0 -- POSITIVE CONTROLS.  Every predicate fired on an input where it MUST return")
print("          the stated value.  A predicate that has not been shown returning True on a")
print("          known-True input has not been shown to work at all.")
print("=" * 96)
pet = G(10, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (5, 7), (7, 9), (9, 6), (6, 8),
             (8, 5), (0, 5), (1, 6), (2, 7), (3, 8), (4, 9)])
check("Petersen is C4-free", has_C4(pet), False)
check("Petersen longest induced path = 5 vertices", longest_induced_path(pet), 5)
check("Petersen a(v) == 3 for every v", sorted({pet.a(v) for v in range(10)}), [3])
check("C4 detector FIRES on a bare C4", has_C4(G(4, [(0, 1), (1, 2), (2, 3), (3, 0)])), True)
check("bare P7 longest induced path = 7 vertices",
      longest_induced_path(G(7, [(i, i + 1) for i in range(6)])), 7)
c6 = G(6, [(i, (i + 1) % 6) for i in range(6)])
check("induced_C6 ACCEPTS the bare hexagon", induced_C6(c6, ZC), True)
check("induced_C6 REJECTS a chorded hexagon",
      induced_C6(G(6, [(i, (i + 1) % 6) for i in range(6)] + [(0, 3)]), ZC), False)
check("bare hexagon: T_Z = 0", T_Z(c6), 0)
check("bare hexagon: every z has a(z) = 2, so sumZ = -6", sumZ(c6), -6)
check("K_{1,4}: a(centre) = 4 - 0 = 4", G(5, [(0, 1), (0, 2), (0, 3), (0, 4)]).a(0), 4)
check("triangle: a(v) = 2 - 1 = 1", G(3, [(0, 1), (1, 2), (2, 0)]).a(0), 1)

# =========================================== PART 1 -- HOSTS AND INDEPENDENT TRUTHS
print()
print("=" * 96)
print("PART 1 -- THE SEVEN TRUTHS, RECOMPUTED HERE FROM THE EDGE LISTS.")
print("          Not read off r29's key: recomputed by a second implementation, then")
print("          CROSS-CHECKED against the key file.  Disagreement would be the finding.")
print("=" * 96)
hosts = {}
keyrows = {}
for line in open(KEY, encoding="utf-8"):
    if " edges: " in line:
        nm, e = line.split(" edges: ")
        hosts[nm.strip()] = ast.literal_eval(e.strip())
    elif line.startswith("V"):
        p = line.rstrip("\n").split("\t")
        keyrows[p[0]] = (p[1], p[2], p[3], int(p[4]))

S = {}
for nm in ("K1", "K2", "K3"):
    e = hosts[nm]
    g = G(max(max(a, b) for a, b in e) + 1, e)
    S[nm] = g
    check("%s is CONNECTED" % nm, g.connected(), True)
    check("%s is C4-FREE" % nm, has_C4(g), False)
    check("%s is P7-FREE (longest induced path <= 6)" % nm, longest_induced_path(g) <= 6, True)
    check("%s: Z=[0..5] induces a C6" % nm, induced_C6(g, ZC), True)

TRUTH = {
    "V1":  (len(hosts["K1"]),),
    "V5":  (S["K1"].a(7),),
    "V7":  (T_Z(S["K1"]), sumZ(S["K1"])),
    "V9":  (T_Z(S["K3"]), sumV(S["K3"])),
    "V10": (max(S["K1"].deg(v) for v in range(S["K1"].n)),
            [v for v in range(S["K1"].n)
             if S["K1"].deg(v) == max(S["K1"].deg(u) for u in range(S["K1"].n))][0]),
    "V11": census(S["K2"]),
    "V12": (T_Z(S["K2"]), sumZ(S["K2"])),
}
# RULING CX is a per-row property: an EXISTENTIAL row must have a UNIQUE witness.
mx = max(S["K1"].deg(v) for v in range(S["K1"].n))
check("V10 is EXISTENTIAL and its witness is UNIQUE (exactly one vertex attains max degree)",
      sum(1 for v in range(S["K1"].n) if S["K1"].deg(v) == mx), 1)

KEYTRUTH = {
    "V1": (14,), "V5": (2,), "V7": (2, -3), "V9": (3, -10),
    "V10": (5, 4), "V11": (3, 1, 1, 1), "V12": (2, -1),
}
for r in ("V1", "V5", "V7", "V9", "V10", "V11", "V12"):
    got = tuple(TRUTH[r])
    check("%s recomputed HERE agrees with the r29 key file" % r, got, KEYTRUTH[r])
    check("%s key file carries the row text and space size" % r, r in keyrows, True)

# ================================================= PART 2 -- THE PARSER AND THE GRADE
print()
print("=" * 96)
print("PART 2 -- STRICT PER-ROW PARSER.  Every slot is read POSITIONALLY, from the line that")
print("          begins with that row's label.  No whole-document searching anywhere.")
print("=" * 96)

ROW_RE = {
    "V1":  re.compile(r"^V1\s*=\s*(-?\d+)\s*$", re.M),
    "V5":  re.compile(r"^V5\s*=\s*(-?\d+)\s*$", re.M),
    "V7":  re.compile(r"^V7\s*=\s*T_Z\s*=\s*(-?\d+)\s*,\s*sum_\{z in Z\}\(a\(z\)-3\)\s*=\s*(-?\d+)\s*$", re.M),
    "V9":  re.compile(r"^V9\s*=\s*T_Z\s*=\s*(-?\d+)\s*,\s*sum_\{v in V\}\(a\(v\)-3\)\s*=\s*(-?\d+)\s*$", re.M),
    "V10": re.compile(r"^V10\s*=\s*maximum degree\s*(-?\d+)\s*,\s*attained uniquely at vertex\s*(-?\d+)\s*$", re.M),
    "V11": re.compile(r"^V11\s*=\s*\|W_1\|\s*=\s*(-?\d+)\s*,\s*\|W_cons\|\s*=\s*(-?\d+)\s*,\s*\|W_anti\|\s*=\s*(-?\d+)\s*,\s*\|W_0\|\s*=\s*(-?\d+)\s*$", re.M),
    "V12": re.compile(r"^V12\s*=\s*T_Z\s*=\s*(-?\d+)\s*,\s*sum_\{z in Z\}\(a\(z\)-3\)\s*=\s*(-?\d+)\s*$", re.M),
}
ROWS = ("V1", "V5", "V7", "V9", "V10", "V11", "V12")


def parse(text):
    """Positional per-row parse.  Returns {row: tuple-or-None}."""
    out = {}
    for r in ROWS:
        m = ROW_RE[r].search(text)
        out[r] = tuple(int(x) for x in m.groups()) if m else None
    return out


def grade(text):
    """THE GATE.  Returns the set of rows that do NOT match the held-out truth.
    Empty set == the grid is clean."""
    p = parse(text)
    return {r for r in ROWS if p[r] is None or p[r] != tuple(TRUTH[r])}


def schema_defects(text):
    """Structural completeness against the schema the brief ASKED for."""
    d = set()
    for r in ROWS:
        if not re.search(r"^%s\s*=" % r, text, re.M):
            d.add("missing-row-" + r)
    if not re.search(r"^VERDICT:\s*\S", text, re.M):
        d.add("missing-VERDICT")
    if "(P1)" not in text:
        d.add("missing-P1")
    return d


def terminal_sentence(text):
    """True iff the text ends on a terminated sentence, not mid-token."""
    return bool(re.search(r"[.!?]['\"`)\]]*\s*$", text))


def naive_whole_doc_grade(text):
    """RULING CZ' INSTRUMENT -- deliberately WRONG, and here to prove the real gate is not
    this.  It asks only: does each true answer's rendering occur ANYWHERE in the document?
    It is what an 'echo detector' that greps the instance string would do."""
    bad = set()
    for r in ROWS:
        for val in TRUTH[r]:
            if not re.search(r"(?<![\d.])%s(?![\d])" % re.escape(str(val)), text):
                bad.add(r)
    return bad


harvest = open(HARVEST, encoding="utf-8").read()
sha = hashlib.sha256(harvest.encode("utf-8")).hexdigest()
check("harvest on disk matches the in-page SHA-256 of the SERVER-STORED answer",
      sha, EXPECT_SHA)
check("harvest length in codepoints", len(harvest), 4077)

parsed = parse(harvest)
print()
print("  ROW GRID (parsed answer vs held-out truth):")
print("  %-5s %-6s %-28s %-28s %-6s %s" % ("row", "tier", "answered", "truth", "grade", "1/|space|"))
for r in ROWS:
    tier = keyrows[r][0]
    space = keyrows[r][3]
    ok = parsed[r] is not None and parsed[r] == tuple(TRUTH[r])
    print("  %-5s %-6s %-28s %-28s %-6s 1/%d" %
          (r, tier, parsed[r], tuple(TRUTH[r]), "CORRECT" if ok else "WRONG", space))

check("CLEAN HARVEST: the gate returns NO wrong rows (the input where it MUST be empty)",
      sorted(grade(harvest)), [])
check("CLEAN HARVEST: schema complete", sorted(schema_defects(harvest)), [])
check("CLEAN HARVEST: ends on a terminal sentence", terminal_sentence(harvest), True)
check("CLEAN HARVEST: naive whole-doc comparator also passes (so it cannot be the gate)",
      sorted(naive_whole_doc_grade(harvest)), [])

# ============================ PART 3 -- RULING CZ: THE GATE FIRING, HARDEST FORMS ONLY
print()
print("=" * 96)
print("PART 3 -- RULING CZ.  Eight ADVERSARIAL corruptions, each the HARDEST form of its")
print("          species, each shown FIRING in this same run.  RULING CZ': for the")
print("          value-preserving ones the NAIVE whole-document comparator is shown PASSING")
print("          on the identical corrupted text -- so the gate fires on the FEATURE (the")
print("          row's asserted slot value) and not on the presence of a string.")
print("=" * 96)


def corrupt(text, old, new):
    if text.count(old) != 1:
        raise RuntimeError("corruption target not unique: %r x%d" % (old, text.count(old)))
    return text.replace(old, new)


# X1 -- HARDEST: swap V7's and V12's second slots.  BOTH rows still carry answers that are
# CORRECT ANSWERS OF THIS EXAM; the multiset of values in the document is UNCHANGED.  Only the
# host attribution moves.  Nothing short of a per-row, per-host grade can see this.
x1 = corrupt(harvest, "V7 = T_Z = 2, sum_{z in Z}(a(z)-3) = -3",
             "V7 = T_Z = 2, sum_{z in Z}(a(z)-3) = -1")
x1 = corrupt(x1, "V12 = T_Z = 2, sum_{z in Z}(a(z)-3) = -1",
             "V12 = T_Z = 2, sum_{z in Z}(a(z)-3) = -3")
check("X1 host-swap of V7/V12: GATE FIRES on exactly {V7,V12}", sorted(grade(x1)), ["V12", "V7"])
check("X1 CZ': naive whole-doc comparator PASSES on the same text (value multiset intact)",
      sorted(naive_whole_doc_grade(x1)), [])

# X2 -- HARDEST: permute V11's census across its labelled slots.  Same multiset {3,1,1,1},
# same four labels, same order of labels.  A bag-of-values check cannot see it.
x2 = corrupt(harvest, "V11 = |W_1| = 3, |W_cons| = 1, |W_anti| = 1, |W_0| = 1",
             "V11 = |W_1| = 1, |W_cons| = 1, |W_anti| = 1, |W_0| = 3")
check("X2 census permutation: GATE FIRES on exactly {V11}", sorted(grade(x2)), ["V11"])
check("X2 CZ': naive whole-doc comparator PASSES on the same text",
      sorted(naive_whole_doc_grade(x2)), [])

# X3 -- HARDEST: V10's SCALAR half left correct, only the WITNESS moved.  A grader that reads
# the quantity and ignores the witness passes.  This is the species that broke r26's V3.
x3 = corrupt(harvest, "V10 = maximum degree 5, attained uniquely at vertex 4",
             "V10 = maximum degree 5, attained uniquely at vertex 9")
check("X3 witness substitution on V10: GATE FIRES on exactly {V10}", sorted(grade(x3)), ["V10"])
check("X3 CZ': the wrong witness 9 and the right witness 4 BOTH occur in the document",
      (re.search(r"(?<![\d.])9(?![\d])", x3) is not None,
       re.search(r"(?<![\d.])4(?![\d])", x3) is not None), (True, True))

# X4 -- HARDEST: V1 replaced by a number that ALREADY OCCURS elsewhere in this very harvest
# (32, in the GAPS section).  A document-level "is there a plausible integer here" check passes.
x4 = corrupt(harvest, "V1 = 14\n", "V1 = 32\n")
check("X4 V1 -> a value occurring elsewhere in the text: GATE FIRES on exactly {V1}",
      sorted(grade(x4)), ["V1"])
check("X4 CZ': that same wrong value 32 genuinely occurs elsewhere in the harvest",
      len(re.findall(r"(?<![\d.])32(?![\d])", harvest)) >= 1, True)

# X5 -- HARDEST: V5 -> 3, which is EXACTLY the modal shortcut r29's own blind-guess table
# named as V5's plausible-space prior.  This is the answer a guesser gives.
x5 = corrupt(harvest, "V5 = 2\n", "V5 = 3\n")
check("X5 V5 -> the named modal-prior shortcut: GATE FIRES on exactly {V5}",
      sorted(grade(x5)), ["V5"])

# X6 -- HARDEST: V9's second slot -> -6, a value that appears in the harvest's own P2 algebra.
x6 = corrupt(harvest, "V9 = T_Z = 3, sum_{v in V}(a(v)-3) = -10",
             "V9 = T_Z = 3, sum_{v in V}(a(v)-3) = -6")
check("X6 V9 second slot -> a value from the response's own algebra: FIRES on exactly {V9}",
      sorted(grade(x6)), ["V9"])

# X7 -- HARDEST schema corruption: delete ONLY the `VERDICT:` line.  The token "GAP" still
# occurs later ("GAPS:"), so a whole-document "does it state a verdict" check still passes.
x7 = corrupt(harvest, "\nVERDICT: GAP\n", "\n")
check("X7 VERDICT line deleted: SCHEMA GATE FIRES", sorted(schema_defects(x7)), ["missing-VERDICT"])
check("X7 CZ': the string 'GAP' still occurs in the corrupted text, so a string check passes",
      "GAP" in x7, True)
check("X7 the ROW gate is silent on X7 (the corruption is schema, not answers)",
      sorted(grade(x7)), [])

# X8 -- HARDEST truncation: cut 12 characters, landing mid-word.  Every row, the VERDICT and
# (P1) all survive, so every other gate passes; only the terminal-sentence gate can see it.
x8 = harvest[:-12]
check("X8 mid-token truncation: TERMINAL-SENTENCE GATE FIRES", terminal_sentence(x8), False)
check("X8 the row gate is silent on X8", sorted(grade(x8)), [])
check("X8 the schema gate is silent on X8", sorted(schema_defects(x8)), [])
check("X8 CZ': the clean text passes the same terminal gate", terminal_sentence(harvest), True)

# ============================================ PART 4 -- OPS-14 FINISH, AS AN INFERENCE
print()
print("=" * 96)
print("PART 4 -- OPS-14.  The finish is settled by THREE signals and recorded as an INFERENCE.")
print("=" * 96)
check("signal 1 CONTENT STABILITY: two server-store reads, byte-identical SHA-256", sha, EXPECT_SHA)
check("signal 2 SCHEMA COMPLETENESS: all seven rows + VERDICT + (P1)",
      sorted(schema_defects(harvest)), [])
check("signal 3 TERMINAL SENTENCE", terminal_sentence(harvest), True)
print("  NOTE, stated and not resolved favourably: document.visibilityState was \"hidden\" at")
print("  BOTH reads, so per OPS-14 no UI-chrome signal was believed at any point.  The store's")
print("  own status fields (done=true, phase-answer status \"finished\", endTime present,")
print("  childrenIds empty) were used INSTEAD of chrome -- but a store status is still not an")
print("  eyewitness of the generation window.  If a continuation arrives, this harvest is a")
print("  PREFIX.  That is carried as an OPEN RISK on the harvest row.")

print()
print("=" * 96)
print("CHECKS: %d   FAILURES: %d" % (NCHK[0], len(FAIL)))
if FAIL:
    for f in FAIL:
        print("  FAILED: %s" % f)
    print("=" * 96)
    sys.exit(2)
print("ALL CHECKS PASS.")
print("=" * 96)
sys.exit(0)
