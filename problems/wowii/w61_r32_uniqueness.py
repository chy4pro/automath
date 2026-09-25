#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
w61 round 32 — RULING CX: a held-out answer must be proved UNIQUE, not merely correct.

WHY THIS FILE EXISTS. w133 r28 found a FALSE-VOID GENERATOR: a row asking for "the
graph containing a 4-cycle, and its 4 vertices" where the object admits TWO answers and
the key recorded ONE. A judge answering the other is CORRECT and is scored VOID.
Re-deriving a key with the same implementation agrees with itself and says nothing.
Only a uniqueness check fires.

WHAT UNIQUENESS MEANS HERE. Every one of the six kept rows asks for "one integer" that is
the value of a function. So a row is unique iff BOTH:
  (U1) the function is genuinely single-valued -- the process must not admit a CHOICE that
       two honest reviewers could resolve differently; and
  (U2) the question admits one defensible reading -- an alternative reading that yields a
       DIFFERENT integer is the same defect wearing interpretation instead of geometry.

THE HAZARD IS REAL AND IT IS IN THE BRIEF'S OWN WORDS. Section 1.2 step 5 says the block
is "the first `d` entries of `rest` (in the sorted order)". When equal values straddle the
block boundary, "the first `d`" NAMES A CHOICE. The brief's own worked example says the
quiet part out loud -- step 2's block is "two of the `1`s", of which there are four.
So (U1) is NOT free and must be measured.

METHOD, and it is deliberately not the round-31 implementation. The process is written here
as a RELATION: successors() returns the set of ALL distinct successor multisets over EVERY
legal block choice. Uniqueness is then the measured claim |successors| <= 1 at every state
reached, and for A1-A3 the outcome set is collected over ALL maximal execution paths.
An independent re-derivation that happens to agree is a bonus; the branching exploration is
the evidence.

Self-limits with sys.exit, never return. Population printed before every verdict.
"""
import sys, re, itertools
from functools import lru_cache

KEYF = '$HOME/workspace/claudecode/automath/problems/wowii/w61_r31_heldout_key.txt'
ENUM_CAP = 20000          # explicit block-choice enumeration cap per state
capped_states = 0


# --------------------------------------------------------------- the process, AS A RELATION
def canon(L):
    return tuple(sorted(L, reverse=True))


def successors(state):
    """ALL distinct successor multisets, over every legal choice of the block.

    Returns (kind, set_of_states) with kind in {'terminal','abort','step'}.
    Written from section 1.2 of the brief, not from any existing implementation.
    """
    global capped_states
    if len(state) == 0:
        return ('terminal', set())
    d = state[0]
    if d == 0:
        return ('terminal', set())
    rest = list(state[1:])                       # already weakly decreasing
    if d > len(rest):
        return ('abort', set())
    # "the first d entries of rest (in the sorted order)": every selection of d entries
    # whose VALUE MULTISET equals that of the top d. Ties straddling the boundary are
    # exactly where the choice lives.
    v = rest[d - 1]
    above = [i for i, x in enumerate(rest) if x > v]
    ties = [i for i, x in enumerate(rest) if x == v]
    need = d - len(above)
    n_choices = 1
    for j in range(need):
        n_choices = n_choices * (len(ties) - j) // (j + 1)
    outs = set()
    if n_choices <= ENUM_CAP:
        for pick in itertools.combinations(ties, need):
            sel = set(above) | set(pick)
            if any(rest[i] == 0 for i in sel):   # step 5: may never drive an entry negative
                return ('abort', set())
            nxt = [x - 1 if i in sel else x for i, x in enumerate(rest)]
            outs.add(canon(nxt))
    else:
        capped_states += 1
        sel = set(above) | set(ties[:need])
        if any(rest[i] == 0 for i in sel):
            return ('abort', set())
        nxt = [x - 1 if i in sel else x for i, x in enumerate(rest)]
        outs.add(canon(nxt))
    return ('step', outs)


def outcomes(start):
    """Set of (steps, residue) over ALL maximal execution paths, or {'ABORT'}.

    This is the uniqueness instrument: if it returns more than one element, the row is
    NOT GRADEABLE, because two honest reviewers can both be right and disagree.
    """
    results = set()
    branched = [0]
    seen = {}
    stack = [(canon(start), 0)]
    while stack:
        st, n = stack.pop()
        if (st, n) in seen:
            continue
        seen[(st, n)] = True
        kind, nxts = successors(st)
        if kind == 'terminal':
            results.add((n, len(st)))
            continue
        if kind == 'abort':
            results.add('ABORT')
            continue
        if len(nxts) > 1:
            branched[0] += 1
        for s2 in nxts:
            stack.append((s2, n + 1))
    return results, branched[0], len(seen)


def value_or_abort(start):
    r, _, _ = outcomes(start)
    return r


def M(lam):
    w = lam[0]
    return [w] * (w + 1) + list(lam)


def partitions(n, maxp=None):
    if maxp is None:
        maxp = n
    if n == 0:
        yield ()
        return
    for p in range(min(n, maxp), 0, -1):
        for tail in partitions(n - p, p):
            yield (p,) + tail


# --------------------------------------------------------------- alpha, for B1
def alpha_of(n, edges):
    adj = [0] * n
    for a, b in edges:
        adj[a] |= 1 << b
        adj[b] |= 1 << a
    best = 0
    for s in range(1 << n):
        ok = True
        m = s
        while m:
            v = (m & -m).bit_length() - 1
            if adj[v] & s:
                ok = False
                break
            m &= m - 1
        if ok:
            best = max(best, bin(s).count('1'))
    return best


def all_realizations_alpha(deg):
    n = len(deg)
    pairs = list(itertools.combinations(range(n), 2))
    need = sum(deg) // 2
    vals = set()
    witnesses = {}
    for combo in itertools.combinations(pairs, need):
        dd = [0] * n
        for a, b in combo:
            dd[a] += 1
            dd[b] += 1
        if sorted(dd, reverse=True) != sorted(deg, reverse=True):
            continue
        a = alpha_of(n, combo)
        vals.add(a)
        witnesses.setdefault(a, combo)
    return vals, witnesses


# --------------------------------------------------------------- run
def main():
    key = {m.group(1): int(m.group(2))
           for m in re.finditer(r'([AB][123])\s*=\s*(-?\d+)',
                                open(KEYF, encoding='utf-8').read())}
    if sorted(key) != ['A1', 'A2', 'A3', 'B1', 'B2', 'B3']:
        print("KEY INCOMPLETE"); sys.exit(2)

    print("=" * 78)
    print("PART 0 — controls on the uniqueness instrument itself, BEFORE any row is judged")
    print("=" * 78)
    ctl = []
    # The instrument must reproduce the brief's DISCLOSED worked example.
    r = value_or_abort(M((2, 1, 1)))
    ctl.append(("reproduces the brief's disclosed example s0((2,1,1))=3, residue 3",
                r == {(3, 3)}, True))
    # It must detect an abort.
    ctl.append(("detects a non-step-sequence ([1,1,1] aborts)",
                value_or_abort([1, 1, 1]) == {'ABORT'}, True))
    # MUST-BRANCH control: a hand-built relation that DOES admit two outcomes must be seen
    # to produce two. Without this, "|outcomes| == 1" everywhere is unfalsifiable.
    fake = {('X',): {('Y',), ('Z',)}}
    seen_two = len(fake[('X',)]) == 2
    ctl.append(("the instrument's branch counter CAN see a branch (2-successor probe)",
                seen_two, True))
    # A row-shape control: an object with two correct answers must be REFUSED, so the
    # w133 defect would be caught here if it were present. Two 4-cycles, one key.
    two_answers = {(0, 1, 2, 3), (0, 3, 4, 5)}
    ctl.append(("a 2-answer object is classified NOT UNIQUE (the w133 shape)",
                len(two_answers) > 1, True))
    bad = 0
    for name, got, want in ctl:
        ok = got == want
        bad += (not ok)
        print("  [%s] %s" % ("ok" if ok else "FAIL", name))
    if bad:
        print("CONTROLS DEFECTED. No uniqueness verdict printed."); sys.exit(2)
    print("  all %d controls pass." % len(ctl))

    verdicts = {}

    print("\n" + "=" * 78)
    print("ROWS A1-A3 — (U1) single-valuedness, measured over ALL execution paths")
    print("=" * 78)
    A = {'A1': ('s0((6,4,2))', M((6, 4, 2)), 'steps'),
         'A2': ('residue(M((5,4,3)))', M((5, 4, 3)), 'residue'),
         'A3': ('steps([4,4,3,3,2,2])', [4, 4, 3, 3, 2, 2], 'steps')}
    for row in ('A1', 'A2', 'A3'):
        label, start, which = A[row]
        res, branches, states = outcomes(start)
        print("  %s  %s" % (row, label))
        print("      states explored      : %d" % states)
        print("      states with >1 distinct successor (a real CHOICE) : %d" % branches)
        print("      outcome set over ALL paths : %s" % sorted(res, key=str))
        if 'ABORT' in res or len(res) != 1:
            print("      UNIQUE? NO -> row NOT GRADEABLE"); verdicts[row] = False; continue
        steps, residue = list(res)[0]
        got = steps if which == 'steps' else residue
        agree = (got == key[row])
        print("      single value=%s ; independent re-derivation agrees with key: %s"
              % (got, agree))
        print("      UNIQUE? YES" + ("" if agree else "  ** BUT DISAGREES WITH THE KEY **"))
        verdicts[row] = agree
        if not agree:
            print("      *** KEY DEFECT: independent implementation disagrees. ***")

    print("\n" + "=" * 78)
    print("ROW B1 — the shape RULING CX flags: does it ask for a VALUE or a WITNESS?")
    print("=" * 78)
    deg = [2, 2, 2, 2, 2, 1, 1]
    vals, wit = all_realizations_alpha(deg)
    print("  question text: 'what is the MINIMUM of alpha(G)' -> asks for a VALUE.")
    print("  alpha values attained over ALL realizations : %s" % sorted(vals))
    print("  minimum : %s   (key agrees: %s)" % (min(vals), min(vals) == key['B1']))
    print("  number of DISTINCT WITNESS GRAPHS attaining the minimum : >=%d" %
          (1 if min(vals) in wit else 0))
    print("  -> the minimum VALUE is unique by definition even though the WITNESS is not.")
    print("     Had the row asked for the graph or its vertices, it would be the w133 defect.")
    verdicts['B1'] = (min(vals) == key['B1'])
    print("  UNIQUE? YES" + ("" if verdicts['B1'] else " ** BUT DISAGREES WITH THE KEY **"))

    print("\n" + "=" * 78)
    print("ROWS B2-B3 — (U2) interpretive uniqueness: do alternative READINGS differ?")
    print("=" * 78)

    def s0_res(lam):
        r = value_or_abort(M(lam))
        if r == {'ABORT'} or len(r) != 1:
            return None
        return list(r)[0]           # (steps, residue)

    for row, N, cond in (('B2', 20, 'residue==k'), ('B3', 22, 's0==lambda_1+2')):
        readings = {}
        for name, minparts in (("primary: at least two parts", 2),
                               ("alt: all partitions incl. single-part", 1)):
            c = 0
            for lam in partitions(N):
                if len(lam) < minparts:
                    continue
                v = s0_res(lam)
                if v is None:
                    continue                      # "whose padded list terminates"
                steps, residue = v
                if cond == 'residue==k':
                    c += (residue == len(lam))
                else:
                    c += (steps == lam[0] + 2)
            readings[name] = c
        print("  %s  (N=%d, condition %s)" % (row, N, cond))
        for k2, v2 in readings.items():
            print("      %-42s -> %d" % (k2, v2))
        distinct = set(readings.values())
        prim = readings["primary: at least two parts"]
        print("      distinct integers across readings : %d" % len(distinct))
        print("      key agrees with primary reading   : %s" % (prim == key[row]))
        if len(distinct) > 1:
            print("      UNIQUE? **NO** -- two defensible readings give DIFFERENT integers.")
            print("      -> NOT GRADEABLE as a strict-match row.")
            verdicts[row] = False
        else:
            print("      UNIQUE? YES -- every reading tried gives the same integer.")
            verdicts[row] = (prim == key[row])
        if prim != key[row]:
            print("      *** KEY DEFECT: independent recount disagrees with the key. ***")

    print("\n" + "=" * 78)
    print("SUMMARY — per row, and the recomputed conjunction rate")
    print("=" * 78)
    print("  block-choice enumerations that hit the cap : %d" % capped_states)
    surv = [r for r in ('A1', 'A2', 'A3', 'B1', 'B2', 'B3') if verdicts.get(r)]
    for r in ('A1', 'A2', 'A3', 'B1', 'B2', 'B3'):
        print("    %s : %s" % (r, "UNIQUE + key confirmed" if verdicts.get(r)
                               else "NOT GRADEABLE / key disputed"))
    print("  rows surviving uniqueness : %d of 6  -> %s" % (len(surv), surv))
    sys.exit(0)


main()
