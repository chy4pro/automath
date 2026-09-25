#!/usr/bin/env python3
"""owner-w61 round 23 -- RULING AQ SWEEP: hunt the MIRROR import species across the whole
document.

Species hunted for seven rounds (7-for-7):  A TRUE IMPORT NOBODY NEEDS  (superfluous citation).
Species NEVER swept for until now:          AN IMPORT THAT IS NEEDED AND WAS NEVER MADE
                                            (the imported statement carries a guard hypothesis
                                            that the importing statement does not supply).

These hide precisely where the statements are TRUE: the guard is carried by ambient context
("in the hard core"), so nothing fails and nothing announces itself.  Repair AD1 (round 22)
was three instances of it in one class.  This sweeps the CLASS over the whole live maths text.

RULING AS -- every check PRINTS ITS OBSERVED POPULATION before its verdict.  Nothing here
renders a verdict over a silently under-collected population: the statement inventory, the
guarded subset, every import edge and every guarded edge are all counted and printed, and the
excluded line ranges are printed with their reason.

RULING AR -- the check is DEMONSTRATED ON A DEFECT THAT ACTUALLY HAPPENED.  Run with
`--pre-ad1` it reverses round 22's three anchored AD1 replaces in memory (the draft file is
never touched) and must re-detect all three sites Repair AD1 was written to fix.

Usage:
    w61_r23_import_sweep.py            # sweep the draft as it stands
    w61_r23_import_sweep.py --pre-ad1  # liveness: sweep the PRE-AD1 text, expect 3 hits
"""
import re, sys, pathlib, hashlib

ROOT = pathlib.Path("$HOME/workspace/claudecode/automath")
DRAFT = ROOT / "notes/proofs/wowii61_draft.md"

# ---------------------------------------------------------------- live maths ranges
# The draft is maths text + round logs.  Only the LIVE maths text carries statements that
# consumers import; the round logs (SS7.9-SS7.11, SS7.14-SS7.24, SS7.26-SS7.37) quote and
# adjudicate them.  Ranges are printed by the report so the exclusion is auditable.
LIVE = [
    (436, 3320, "SS7 .. SS7.13  -- the whole live chain (root reduction, T3, K, LOW/SL/MB, FAN, RIG, GFAN)"),
    (3321, 3556, "SS7.14 addendum -- Lemma S', Lemma T', Lemma H' (registry rows R-11/R-12)"),
    (4955, 5115, "SS7.25 own attack -- Lemma C1-A, C1-A', Proposition C1-B, Corollary C1-C, Theorem C1-2"),
]

HDR = re.compile(r"^>\s*\*\*((?:Theorem|Lemma|Corollary|Proposition|Observation)\s+"
                 r"[A-Za-z0-9ν′⁺\*\\-]+(?:[-′⁺][A-Za-z0-9′⁺]+)*)")

# Re-quotes / adjudication restatements inside the live ranges: the same name appearing a
# second time at a line where the surrounding section is a repair log.  Listed explicitly so
# that dropping them is a decision on the record, not a silent filter.
REQUOTE_LINES = {2401, 2408, 2448, 2492, 2499, 2816, 3199, 3371, 1968}

NOTE = re.compile(r"〔.*?〕", re.S)          # <> repair notes
STRIKE = re.compile(r"~~.*?~~", re.S)                 # withdrawn text


def load(pre_ad1: bool):
    src = DRAFT.read_text()
    if pre_ad1:
        # Reverse round 22's three AD1 anchored replaces, in memory only.
        import importlib.util
        rep = (ROOT / "problems/wowii/w61_r22_repair_ad.py").read_text()
        # pull the three AD1 (old,new) pairs straight out of the repair script source
        pairs = reverse_ad1_pairs(rep)
        for tag, old, new in pairs:
            assert src.count(new) == 1, f"[pre-ad1] post-AD1 text for {tag} not found exactly once"
            src = src.replace(new, old)
        print(f"  [--pre-ad1] reversed {len(pairs)} AD1 replaces in memory; draft file untouched")
    return src


def reverse_ad1_pairs(rep_src):
    """Extract the three AD1 rep(old,new,tag) calls from the round-22 repair script.

    Parsed from the SCRIPT'S OWN AST, not re-typed here: the liveness demonstration must
    run against the real anchors round 22 used, not against a paraphrase of them.
    """
    import ast
    tree = ast.parse(rep_src)
    ns = {}
    out = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", "") == "AD1NOTE":
            ns["AD1NOTE"] = ast.literal_eval(node.value)
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call) \
                and getattr(node.value.func, "id", "") == "rep":
            a = node.value.args
            tag = ast.literal_eval(a[2])
            if not tag.startswith("AD1/"):
                continue
            ev = lambda n: eval(compile(ast.Expression(n), "<anchor>", "eval"), {}, ns)
            out.append((tag, ev(a[0]), ev(a[1])))
    assert len(out) == 3, f"expected 3 AD1 sites in the repair script, found {len(out)}"
    return out


# ---------------------------------------------------------------- guard vocabulary
# A GUARD is a hypothesis a statement carries in ITS OWN TEXT that a consumer must supply.
def guards_of(stmt_text):
    g = set()
    t = stmt_text
    for m in re.finditer(r"`?L\s*≥\s*(\d+)`?", t):
        g.add(("L>=", int(m.group(1))))
    for m in re.finditer(r"`?L\s*=\s*(\d+)`?", t):
        g.add(("L>=", int(m.group(1))))
    if re.search(r"B_lo\s*≠\s*∅", t) or re.search(r"B_lo⁺\s*≠\s*∅", t):
        g.add(("L>=", 1))
    for m in re.finditer(r"`?ν\s*≥\s*(\d+)`?", t):
        g.add(("nu>=", int(m.group(1))))
    for m in re.finditer(r"1\s*≤\s*ν", t):
        g.add(("nu>=", 1))
    for m in re.finditer(r"`?τ\s*≥\s*(\d+)`?", t):
        g.add(("tau>=", int(m.group(1))))
    for m in re.finditer(r"`?τ\s*=\s*(\d+)`?", t):
        g.add(("tau>=", int(m.group(1))))
    return g


# A statement's HYPOTHESIS is what a consumer must supply; its CONCLUSION is not.  This is
# the whole point of the species: Corollary GFANnu-HC concludes `L >= 12`, and reading that
# numeral as a supplied hypothesis is exactly the mistake that let the defect live.
CONCL = re.compile(r"\bthen\b|\bThen\b|,\s*so\b|\bthere is\b|\bthere are\b|"
                   r"\bwe have\b|\bit follows\b|\ball\*{0,2} of the following\b|\bmust\b")
CUE = re.compile(r"First|Indeed|Note that|Observe|By hypothesis|we may assume|Suppose")


TITLE = re.compile(r"^>?\s*\*\*.*?\*\*", re.S)


def hypothesis_of(stmt_text):
    # The bolded title parenthetical usually ADVERTISES THE CONCLUSION ("Corollary GFAN2-HC
    # (the B-universal layer needs `L >= 4` ...)").  Reading its numerals as supplied
    # hypotheses is the same misreading as reading the conclusion; strip it.
    body = TITLE.sub("", stmt_text, count=1)
    m = CONCL.search(body)
    return body[:m.start()] if m else body


def supplies(consumer_stmt, consumer_proof, guard):
    """Does the consumer supply `guard` -- from its own HYPOTHESIS, or by an explicit
    establishing step in its proof?  A numeral occurring in a CONCLUSION supplies nothing."""
    kind, n = guard
    sym = {"L>=": "L", "nu>=": "ν", "tau>=": "τ"}[kind]
    hyp = hypothesis_of(consumer_stmt)
    # (1) the consumer's own hypothesis carries a guard on the same parameter, >= as strong
    for m in re.finditer(rf"`?{sym}\s*[≥=]\s*(\d+)`?", hyp):
        if int(m.group(1)) >= n:
            return True
    # (2) `L >= nu+1` together with `nu >= 1`, both in the hypothesis, gives `L >= 2`
    if kind == "L>=" and n <= 2 and re.search(r"L\s*≥\s*ν\s*\+\s*1", hyp) \
            and re.search(r"1\s*≤\s*ν|ν\s*≥\s*1", hyp):
        return True
    # (3) the hypothesis states the non-emptiness outright
    if kind == "L>=" and n <= 1 and re.search(r"B_lo\s*≠\s*∅", hyp):
        return True
    # (4) the PROOF establishes it explicitly -- an establishing cue with the guard inside
    #     the next 300 characters.  This is the shape Repair AD1 wrote: "First, `B_lo != 0`,
    #     i.e. `L >= 1`: at `L = 0` Theorem K makes `B` a clique, contradicting R1."
    for m in CUE.finditer(consumer_proof):
        w = consumer_proof[m.start():m.start() + 300]
        if kind == "L>=" and n <= 1 and re.search(r"B_lo\s*≠\s*∅", w):
            return True
        for g in re.finditer(rf"`?{sym}\s*[≥=]\s*(\d+)`?", w):
            if int(g.group(1)) >= n:
                return True
    # (5) nu >= 1 in the hard core is Observation R1, invoked by name in the proof
    if kind == "nu>=" and n <= 1 and re.search(r"R1", consumer_proof):
        return True
    return False


def main():
    pre = "--pre-ad1" in sys.argv
    src = load(pre)
    lines = src.split("\n")
    md5 = hashlib.md5(src.encode()).hexdigest()

    def is_live(ln):
        return any(a <= ln <= b for a, b, _ in LIVE)

    hpos = [(i, HDR.match(l).group(1).strip()) for i, l in enumerate(lines) if HDR.match(l)]
    stmts = []
    for k, (i, name) in enumerate(hpos):
        ln = i + 1
        end = hpos[k + 1][0] if k + 1 < len(hpos) else len(lines)
        j = i + 1
        while j < end and (lines[j].startswith(">") or lines[j].strip() == ""):
            j += 1
        block = "\n".join(lines[i:j])
        stmts.append(dict(line=ln, name=name.replace("**", "").strip(), block=block,
                          live=is_live(ln), requote=ln in REQUOTE_LINES))

    # split statement / proof
    for s in stmts:
        b = STRIKE.sub(" ", s["block"])
        m = re.search(r"\*Proof\.?\*|\*Proof sketch\.?\*|\*Proof \(", b)
        s["stmt"] = b[:m.start()] if m else b
        s["proof"] = b[m.start():] if m else ""
        s["proof_body"] = NOTE.sub(" ", s["proof"])   # repair notes stripped for IMPORTS
        # Repair notes 〔...〕 inside a statement block are COMMENTARY, not hypotheses:
        # Theorem GFANnu's AB1 note prints the counterexample `K5` at `L = 4`, and
        # Corollary GFAN2-HC's note prints its successor's `L >= 12`.  Reading either as
        # a guard invents a requirement the statement does not make.
        s["stmt_bare"] = NOTE.sub(" ", s["stmt"])
        # A GUARD is a HYPOTHESIS.  Numerals in a statement's conclusion, in a numerical
        # caution ("e.g. `K_6` has tau=5"), or in a repair note are not hypotheses, and
        # reading them as such invents requirements -- the same misreading, on the supplier
        # side, that reading a conclusion as a supply is on the consumer side.
        s["guards"] = guards_of(hypothesis_of(s["stmt_bare"]))

    # Re-quote / false-header detection, CONTENT-BASED rather than by line number: a
    # hard-coded line list silently decays the moment anything above it is edited, and this
    # round's own AE1 repair shifted it by 15 lines.  Rule: among blocks sharing a name, the
    # real statement is the earliest one carrying its own `*Proof.*`; if none does, the
    # longest.  Everything else is a re-quote or a mid-proof bold mention.
    from collections import defaultdict
    byname = defaultdict(list)
    for s in stmts:
        if s["live"]:
            byname[s["name"]].append(s)
    for nm, group in byname.items():
        if len(group) == 1:
            continue
        withproof = [g for g in group if g["proof"]]
        keep = withproof[0] if withproof else max(group, key=lambda g: len(g["block"]))
        for g in group:
            if g is not keep:
                g["requote"] = True
    live = [s for s in stmts if s["live"] and not s["requote"]]
    names = {}
    for s in live:
        names.setdefault(s["name"], s)

    # ---- import edges
    # RULING AS, learned the hard way in round 22: a name pattern that does not strip the
    # document's own markup under-collects the population and then renders a favourable
    # verdict over it.  `**Lemma TAIL**` and `` `FAN-4′` `` are citations; the raw pattern
    # sees neither.  Both counts are reported.
    def norm(t):
        return t.replace("**", "").replace("`", "").replace("\\", "")

    NAMEPAT = re.compile(r"\b(Theorem|Lemma|Corollary|Proposition|Observation)\s+"
                         r"([A-Za-z0-9ν′][A-Za-z0-9ν′*-]*)")
    # bare-name citations ("FAN-4′ forces ...", "TAIL is stated for ...").  Only names that
    # cannot collide with ordinary symbols: length >= 3, or carrying a hyphen.
    bare_of = {}
    for cand in names:
        b = norm(cand).split(None, 1)[1]
        if len(b) >= 3 or "-" in b:
            bare_of.setdefault(b, cand)
    BAREPAT = re.compile("|".join(sorted((re.escape(b) for b in bare_of), key=len, reverse=True)))

    edges, edges_raw = [], []
    for s in live:
        body = norm(s["proof_body"])
        raw = s["proof_body"]
        seen, seen_raw = set(), set()
        for m in NAMEPAT.finditer(raw):
            key = f"{m.group(1)} {m.group(2)}".replace("\\", "")
            for cand in names:
                if cand.replace("\\", "") == key and cand != s["name"] and cand not in seen_raw:
                    seen_raw.add(cand)
                    edges_raw.append((s, names[cand]))
        for m in NAMEPAT.finditer(body):
            key = f"{m.group(1)} {m.group(2)}"
            for cand in names:
                if norm(cand) == key and cand != s["name"] and cand not in seen:
                    seen.add(cand)
                    edges.append((s, names[cand]))
        for m in BAREPAT.finditer(body):
            cand = bare_of[m.group(0)]
            if cand != s["name"] and cand not in seen:
                seen.add(cand)
                edges.append((s, names[cand]))

    guarded_edges = [(c, q, g) for (c, q) in edges for g in q["guards"]]
    suspects = [(c, q, g) for (c, q, g) in guarded_edges
                if not supplies(c["stmt_bare"], c["proof"], g)]

    # ---------------------------------------------------------------- REPORT
    P = print
    P("=" * 94)
    P("w61_r23_import_sweep -- RULING AQ: the MIRROR species (an import that is needed and")
    P("                       was never made).  draft md5 = " + md5 + ("  [PRE-AD1]" if pre else ""))
    P("=" * 94)
    P("")
    P("OBSERVED POPULATION  (RULING AS: printed BEFORE any verdict)")
    P("-" * 94)
    P(f"  draft lines total .................................. {len(lines)}")
    for a, b, why in LIVE:
        P(f"  live maths range {a:>5}-{b:<5} .................... {why}")
    P(f"  statement blocks matched, whole document .......... {len(stmts)}")
    P(f"    of which OUTSIDE the live ranges (round logs) ... {sum(1 for s in stmts if not s['live'])}  [excluded]")
    P(f"    of which re-quotes inside live ranges ........... {sum(1 for s in stmts if s['live'] and s['requote'])}  [excluded, listed below]")
    P(f"  LIVE STATEMENTS SWEPT ............................. {len(live)}")
    P(f"    with a numeric/non-emptiness GUARD in their own")
    P(f"    statement text (importable guard) ............... {sum(1 for s in live if s['guards'])}")
    P(f"  import edges seen by the RAW pattern (markup kept) {len(edges_raw)}   [under-collected]")
    P(f"  IMPORT EDGES (consumer proof -> named statement) .. {len(edges)}")
    P(f"    of which the imported statement IS GUARDED ...... {len(guarded_edges)}   <-- the swept population")
    P("")
    P("  re-quotes excluded (line: name):")
    for s in stmts:
        if s["live"] and s["requote"]:
            P(f"    {s['line']:>5}: {s['name']}")
    P("")
    P("  every live statement, its guards, and its out-degree:")
    P(f"    {'line':>5}  {'statement':<24} {'guards':<28} imports")
    for s in sorted(live, key=lambda x: x["line"]):
        gg = ",".join(f"{k}{v}" for k, v in sorted(s["guards"])) or "-"
        outd = sum(1 for c, q in edges if c is s)
        P(f"    {s['line']:>5}  {s['name']:<24} {gg:<28} {outd}")
    P("")
    P("VERDICT")
    P("-" * 94)
    P(f"  guarded import edges checked ...................... {len(guarded_edges)}")
    P(f"  edges where the guard IS supplied by the consumer . {len(guarded_edges) - len(suspects)}")
    P(f"  SUSPECT edges (guard needed, not supplied) ........ {len(suspects)}")
    P("")
    if suspects:
        for c, q, g in sorted(suspects, key=lambda x: x[0]["line"]):
            P(f"  SUSPECT  {c['name']}  (line {c['line']})")
            P(f"           imports {q['name']} (line {q['line']}), which requires {g[0]}{g[1]}")
            P(f"           consumer's own guards: {sorted(c['guards']) or 'NONE'}")
    else:
        P("  none.")
    P("")
    if pre:
        want = {"Corollary MB1", "Corollary GFAN2-HC", "Corollary GFANν-HC"}
        got = {c["name"] for c, q, g in suspects}
        P("LIVENESS (RULING AR -- demonstrated on a defect that actually happened)")
        P("-" * 94)
        P(f"  Repair AD1's three real sites: {sorted(want)}")
        P(f"  re-detected by this sweep on the PRE-AD1 text: {sorted(want & got)}")
        P(f"  RESULT: {'PASS -- all three re-detected' if want <= got else 'FAIL -- ' + str(sorted(want - got)) + ' missed'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
