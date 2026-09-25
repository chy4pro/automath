#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
w61 round 30, item 1 — RULING CS applied across the line.

The species: a hedge PRESENT AT THE SOURCE and DROPPED IN THE CARRIER, where a
"carrier" is any layer that hands the ledger to a consumer -- a brief going to a
judge (three instances found before), or a RESUME POINTER / next-step note /
owed-list going to the NEXT ROUND (the fourth instance, sec 7.28 (d)2, repaired as
Repair AG3 in round 29).

RULING CQ binds: PART 0 positive-controls every detector on inputs where the answer
is YES *before* any negative is trusted, and false-positive-probes it on inputs
where the answer is NO.  A detector whose output is a negative is silent when broken.

Detectors:
  D-CLOSE  a carrier that asserts a CLOSURE / "only thing remaining" while the
           ledger (or the carrier's own bullet list) records statements still open.
  D-HEDGE  a carrier claim about a named object whose SOURCE block carries a hedge
           marker that the carrier sentence does not carry.

Output is a suspect list.  Every suspect is adjudicated BY HAND against the draft;
the script does not issue verdicts.
"""
import re, sys, os, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DRAFT = os.path.join(ROOT, 'notes/proofs/wowii61_draft.md')

CARRIER_FILES = [
    ('notes/proofs/wowii61_draft.md', 'BLOCKS'),   # resume-pointer blocks only
    ('HANDOVER.md', 'WHOLE'),
    ('orchestration/STATUS.md', 'WHOLE'),
    ('orchestration/watch_ledger.md', 'WHOLE'),
    ('orchestration/PLAN.md', 'WHOLE'),
]

CARRIER_HEAD = re.compile(r'^#{2,4} .*(ext round|esume pointer|Owed from|still queued|standing records|next step)', re.I)

# ---------------------------------------------------------------- lexicons
HEDGE = [
    'claim nothing', 'not built here', 'is not a reduction', 'not a reduction',
    'sufficient condition', 'conjecture', 'unproved', 'not proved', 'not established',
    'never queued', '0 s3 rounds', '0** rounds', '0 rounds', 'at **0**', '1 family',
    'one family', 'not verified', 'single-implementation', 'measured', 'still owes',
    'not offered as', 'more cases is not a proof', 'cannot', 'untested', 'unreviewed',
    'unswept', 'not claimed', 'we do not know', 'open', 'pending', 'held',
    'if ', 'provided ', 'assuming', 'subject to', 'may ', 'might ', 'would ',
    'proposed', 'candidate', 'bounded weakening', 'not evidence', 'does not prove',
    'blocked on', 'obstructed', 'partial', 'only', 'except',
]
ASSERT = [
    'closes', 'closed', 'is the only thing', 'the only thing', 'entire', 'all that remains',
    'reduced by', 'reduces', 'reduction of', 'settled', 'discharged', 'done',
    'is proved', 'proves', 'guarantees', 'suffices', 'it suffices', 'just ', 'simply ',
    'immediately', 'trivially', 'in reach', 'natural candidate', 'must ', 'will ',
]
CLOSURE = re.compile(
    r'(closes? [^.\n]{0,40}s3 surface'
    r'|s3 surface [^.\n]{0,40}clos'
    r'|entire s3 surface[^.\n]{0,20}clos'
    r'|only thing between[^.\n]{0,40}clos'
    r'|唯一残余'
    r'|只差一个族轮'
    r'|全部\s*s3\s*面闭合'
    r'|s3 面[^。\n]{0,10}闭合'
    r'|only [^.\n]{0,30}remains?'
    r'|the one (?:re-)?round that closes)', re.I)
# counter-evidence that the SAME carrier already knows the surface is not closed
STILL_OPEN = re.compile(
    r'(0\**\s*s3 rounds|at \*\*0\*\* rounds|at \*\*0 rounds\*\*|never queued'
    r'|1 family|one family|still queued|0\s*轮|零\s*s3)', re.I)

NAMED = re.compile(
    r'(Theorem|Lemma|Corollary|Proposition|Observation|Conjecture|Repair|Row|GUARD|RULING|OPS)\s+'
    r'([A-Z][A-Za-z0-9′’\-]*(?:\s?[0-9]+)?(?:-[A-Za-z0-9′]+)*)')

def norm(s):
    return unicodedata.normalize('NFKC', s).lower()

def has(text, lex):
    t = norm(text)
    return [w for w in lex if w in t]

# ---------------------------------------------------------------- carriers
def carrier_blocks():
    out = []
    for rel, mode in CARRIER_FILES:
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            continue
        L = open(p, encoding='utf-8').read().split('\n')
        if mode == 'WHOLE':
            out.append((rel, 1, rel, '\n'.join(L)))
            continue
        starts = [i for i, l in enumerate(L) if CARRIER_HEAD.search(l)]
        for s in starts:
            e = s + 1
            while e < len(L) and not (L[e].startswith('### ') or L[e].startswith('## ')
                                      or L[e].startswith('---')):
                e += 1
            out.append((rel, s + 1, L[s].strip('# ').strip(), '\n'.join(L[s:e])))
    return out

def bullets(block):
    """split a carrier block into claim units (bullets / blockquote lines / sentences)"""
    units, cur = [], []
    for line in block.split('\n'):
        if re.match(r'^\s*(\d+\.|[-*]|>\s*\*\*|\|)', line) and cur:
            units.append('\n'.join(cur)); cur = [line]
        elif line.strip() == '' and cur:
            units.append('\n'.join(cur)); cur = []
        else:
            cur.append(line)
    if cur:
        units.append('\n'.join(cur))
    return [u for u in units if u.strip()]

# ---------------------------------------------------------------- detectors
def d_close(unit):
    """FIRE if the unit asserts closure/uniqueness-of-remainder."""
    m = CLOSURE.search(norm(unit))
    return m.group(0) if m else None

def d_hedge(unit, sources):
    """FIRE if the unit speaks assertively about a named object whose source block hedges."""
    fired = []
    u_h = has(unit, HEDGE)
    u_a = has(unit, ASSERT)
    if not u_a:
        return fired
    for kind, name in set(NAMED.findall(unit)):
        key = f'{kind} {name}'.strip()
        src = sources.get(key)
        if not src:
            continue
        s_h = has(src, HEDGE)
        dropped = [h for h in s_h if h not in u_h]
        if dropped:
            fired.append((key, dropped[:6], u_a[:4]))
    return fired

def source_index():
    """map an object name -> its source-side text in the draft.

    Two kinds, because PART 0's P5 control showed the first kind alone is BLIND to
    every object that is not a numbered statement (GUARDs, tools, rulings):
      (1) STATEMENT BLOCK  -- precise: the '> **Lemma X.**' block itself.
      (2) MENTION POOL     -- crude: every draft line naming the object, +2 lines.
    (2) over-collects and therefore over-suspects.  That is the intended direction:
    a suspect costs a hand adjudication, a miss costs a round sent at a dead route.
    """
    txt = open(DRAFT, encoding='utf-8').read()
    L = txt.split('\n')
    idx = {}
    for i, line in enumerate(L):
        m = re.match(r'^>\s*\*\*(Theorem|Lemma|Corollary|Proposition|Observation|Conjecture)\s+'
                     r'([^ .*(]+)', line)
        if m:
            key = f'{m.group(1)} {m.group(2)}'.rstrip('.').strip()
            e = i + 1
            while e < len(L) and (L[e].startswith('>') or L[e].strip() == ''):
                e += 1
            body = '\n'.join(L[i:min(e + 12, len(L))])
            idx.setdefault(key, body)
    pool = {}
    for i, line in enumerate(L):
        for kind, name in set(NAMED.findall(line)):
            key = f'{kind} {name}'.strip()
            pool.setdefault(key, []).append('\n'.join(L[i:min(i + 3, len(L))]))
    for k, v in pool.items():
        if k not in idx:
            idx[k] = '\n'.join(v[:80])
    return idx

# ---------------------------------------------------------------- PART 0
def part0(sources):
    print('=' * 78)
    print('PART 0 — CONTROLS (RULING CQ: a detector whose output is a NEGATIVE must be')
    print('         positive-controlled on inputs where the answer is YES).')
    print('=' * 78)
    ok = True

    # P1: the REAL, historical sec 7.28 (d)2 text, pre-Repair-AG3, quoted verbatim in
    #     sec 7.44 (d).  The carrier that RULING CS was issued about.  MUST fire on D-HEDGE.
    p1_carrier = ("2. **Conjecture C1 for `k >= 3`** -- reduced by Corollary C1-C to "
                  "exhibiting, for each `lambda`, one graph realizing `[w]^{w+1} u lambda` "
                  "with `alpha <= k`. This is a construction problem of the kind this line "
                  "has repeatedly solved.")
    p1_src = sources.get('Corollary C1-C', '')
    got = d_hedge(p1_carrier, {'Corollary C1-C': p1_src})
    print(f'\n[P1 POSITIVE] historical sec7.28 (d)2 pre-AG3 text vs Corollary C1-C source')
    print(f'   source block found: {bool(p1_src)}  ->  D-HEDGE fires: {bool(got)}  {got}')
    ok &= bool(got)

    # P2: the sec 7.28 (c) gate, verbatim from the draft.  MUST fire on D-CLOSE.
    p2 = ("**Pre-registered gate:** if this round is clean on the mathematics, **the entire S3 "
          "surface of WOWII-61 closes** -- the ten statements above reach two families, Theorem "
          "GFANnu reaches one, and only GFANnu's second family remains.")
    print(f'\n[P2 POSITIVE] sec7.28 (c) pre-registered gate  ->  D-CLOSE fires: '
          f'{d_close(p2)!r}')
    ok &= bool(d_close(p2))

    # P3..P5: synthetic hedge-strippings of carrier sentences that are CURRENTLY correct.
    strips = [
        ("Conjecture C1 for `k >= 3` -- Corollary C1-C gives a **sufficient condition**, "
         "**not** a reduction; Observation C1-E shows the graph does **not** exist.",
         "Conjecture C1 for `k >= 3` -- Corollary C1-C reduces it to a construction; "
         "one graph suffices and the counting condition never blocks."),
        ("Theorem GFANnu is PROVED-S3 (row R-23); **Corollary GFANnu-HC is at 1 family**.",
         "Theorem GFANnu is PROVED-S3 (row R-23); Corollary GFANnu-HC closes the S3 surface."),
        ("GUARD E proves the brief's transcription **matches the draft**. It does **not** "
         "prove the draft is right.",
         "GUARD E proves the brief's imports are right."),
    ]
    for i, (good, bad) in enumerate(strips, start=3):
        f_bad = bool(d_close(bad)) or bool(d_hedge(bad, sources))
        f_good = bool(d_close(good)) or bool(d_hedge(good, sources))
        print(f'\n[P{i}] synthetic hedge-strip   stripped fires: {f_bad}   '
              f'original (false-positive probe) fires: {f_good}')
        ok &= f_bad

    # N1..N2: false-positive probes -- correctly hedged carriers that must stay SILENT on D-CLOSE.
    negs = [
        "The bench, unchanged. If the `OR_KEY` cap lifts, `w61_S3_GFAN_r28.md` dispatches as built.",
        "Unchanged and still queued: the sec7.25 own-attack family at **0** S3 rounds.",
    ]
    for i, n in enumerate(negs, start=1):
        f = d_close(n)
        print(f'[N{i} FALSE-POSITIVE PROBE] D-CLOSE fires: {f!r}   (want None)')
        ok &= (f is None)

    print(f'\nPART 0 verdict: {"PASS -- detectors are live in both directions" if ok else "FAIL"}')
    if not ok:
        print('A detector that cannot be shown to fire on a known YES is worthless on a NO.')
        sys.exit(2)
    return ok

# ---------------------------------------------------------------- main
def main():
    sources = source_index()
    print(f'source statement blocks indexed from the draft: {len(sources)}')
    part0(sources)

    blocks = carrier_blocks()
    print()
    print('=' * 78)
    print(f'PART 1 — D-CLOSE over {len(blocks)} carrier blocks/files on this line')
    print('=' * 78)
    n_close = 0
    for rel, ln, head, block in blocks:
        for u in bullets(block):
            hit = d_close(u)
            if not hit:
                continue
            n_close += 1
            self_contra = STILL_OPEN.search(norm(block))
            print(f'\n--- SUSPECT C{n_close}  {rel}:{ln}  [{head[:60]}]')
            print(f'    trigger      : {hit!r}')
            print(f'    claim        : {" ".join(u.split())[:300]}')
            print(f'    same carrier also records an OPEN statement: '
                  f'{self_contra.group(0)!r}' if self_contra else
                  '    same carrier records no open statement (external check needed)')
    print(f'\nD-CLOSE suspects: {n_close}')

    print()
    print('=' * 78)
    print('PART 2 — D-HEDGE over the same carriers')
    print('=' * 78)
    n_h = 0
    seen = set()
    for rel, ln, head, block in blocks:
        for u in bullets(block):
            for key, dropped, asserts in d_hedge(u, sources):
                sig = (rel, key, ' '.join(u.split())[:80])
                if sig in seen:
                    continue
                seen.add(sig)
                n_h += 1
                print(f'\n--- SUSPECT H{n_h}  {rel}:{ln}  object={key}')
                print(f'    source hedges dropped by carrier: {dropped}')
                print(f'    carrier assertive markers       : {asserts}')
                print(f'    claim: {" ".join(u.split())[:260]}')
    print(f'\nD-HEDGE suspects: {n_h}')
    print()
    print('NOTE: a SUSPECT is not a verdict.  Every one is adjudicated by hand against')
    print('the draft, and the adjudication is what goes in the ledger.')

if __name__ == '__main__':
    main()
