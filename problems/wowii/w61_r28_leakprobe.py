#!/usr/bin/env python3
"""
w61_r28_leakprobe.py -- THE LEAK PROBE, RUN AT WRITE TIME.

RULING CI's second half, adopted from r27's own failure:

  "A check that runs BEFORE the thing it guards against happens is not a guard."

In r27 the probe ran inside the BUILD, so it certified the key clean and then
SS7.42 (c) printed one of that key's answers into the draft two hours later --
caught only because the probe was re-run by hand after the section was appended.
This file exists so that re-run is not by hand.  It runs AFTER any write.

RULING CH, adopted the same round:

  "Key burn is measured against the WHOLE CORPUS -- draft, ledger and every
   shipped brief -- never assumed from outing count."

nu = 11 was not burned by its four outings; its own answers were printed thirty
times in our own draft by the harvest tables that recorded each judge's rows.
So the corpus here is the draft, every shipped brief, the orchestration ledger,
and every .md/.out under problems/wowii -- not a spot check.

DEFECT E-1's root fix is preserved: THIS PROBE NEVER PRINTS WHAT IT PROBES FOR.
Values appear as digit masks.  A probe that prints the key in cleartext in order
to prove the key is not printed anywhere is the defect it hunts.
"""
import re, sys, glob, os

ROOT = "$HOME/workspace/claudecode/automath"
KEY  = os.path.join(ROOT, "problems/wowii/w61_r27_heldout_key.txt")

kt = open(KEY).read()

def mask(v):
    s = str(v)
    return "%s<%dd>%s" % (s[0], len(s), "#" * (len(s) - 1)) if len(s) > 1 else "<1d>#"

# ---------------------------------------------------- the DISCRIMINATING population
# Everything below the HELD-OUT marker is an answer.  Above it is calibration
# against published nu <= 10 data, which is public by construction and must NOT be
# probed for -- probing for public values manufactures hits (RULING CI, the other
# direction of the same error).
# DEFECT L-2, second run, same species as L-1: splitting at "H1" swept in the key
# file's own "--- controls ---" block, which quotes PUBLISHED nu <= 10 numbers.  The
# probe then reported a published value as a burned key value -- a manufactured leak.
# Bound the population by the file's OWN section markers instead of by a name.
held = kt.split("--- THE KEY ---")[1].split("--- OPS-")[0]
# DEFECT L-3, third run, third instance of the SAME species in one probe: the
# population still swept in the INTERMEDIATE FACTORS of H2's term computation,
# which are the partition numbers p(k) -- published mathematical constants that
# occur all over this corpus for perfectly good reasons.  The probe reported one
# of them as a burned key value.  CLASS rule (RULING S: names no number): an
# integer that is the value of a `p(k)=` factor is a PUBLISHED constant and is
# not a key answer.  Everything else in the key block is.
held_masked = re.sub(r"p\(\d+\)\s*=\s*\d+", "p(k)=PUB", held)
vals = sorted({int(x) for x in re.findall(r"\b\d{2,}\b", held_masked)})
shapes = sorted(set(re.findall(r"\[[0-9+]+\]", held)))
print("=== LEAK PROBE POPULATION (RULING AS), printed as MASKS before any verdict ===")
print("  key file            : %s" % KEY)
print("  discriminating ints : %d  -> %s" % (len(vals), " ".join(mask(v) for v in vals)))
print("  discriminating shapes: %d -> %s" % (len(shapes),
      " ".join("[%dp]" % s.count("+") for s in shapes)))
print()

# ------------------------------------------------------------------------ the CORPUS
corpus = []
corpus.append(os.path.join(ROOT, "notes/proofs/wowii61_draft.md"))
corpus += sorted(glob.glob(os.path.join(ROOT, "prompts/w61_*.md")))
corpus += sorted(glob.glob(os.path.join(ROOT, "orchestration/**/*.md"), recursive=True))
corpus += sorted(glob.glob(os.path.join(ROOT, "problems/wowii/*.md")))
corpus += sorted(glob.glob(os.path.join(ROOT, "problems/wowii/*.out")))
corpus = [p for p in corpus if os.path.abspath(p) != os.path.abspath(KEY)]
# the probe's OWN output is not corpus -- it would report its own masks as hits
corpus = [p for p in corpus if not p.endswith("w61_r28_leakprobe.out")]
print("=== CORPUS (RULING CH: the whole of it, not the outing count) ===")
print("  draft                : 1")
print("  shipped briefs       : %d" % len(glob.glob(os.path.join(ROOT, "prompts/w61_*.md"))))
print("  ledger + planner msgs: %d" % len(glob.glob(os.path.join(ROOT, "orchestration/**/*.md"), recursive=True)))
print("  problems/wowii md+out: %d" % (len(glob.glob(os.path.join(ROOT, "problems/wowii/*.md"))) +
                                       len(glob.glob(os.path.join(ROOT, "problems/wowii/*.out")))))
print("  TOTAL FILES SCANNED  : %d\n" % len(corpus))

texts = {}
for p in corpus:
    try:
        texts[p] = open(p, errors="ignore").read()
    except Exception:
        pass

def occurrences(tok):
    hits = {}
    for p, t in texts.items():
        n = len(re.findall(r"(?<!\d)%s(?!\d)" % re.escape(tok), t))
        if n:
            hits[p] = n
    return hits

leaks = []
print("=== PER-VALUE VERDICT (masks only; a cleartext print here would BE the leak) ===")
for v in vals:
    forms = {str(v), "{:,}".format(v), "{:,}".format(v).replace(",", " ")}
    tot, where = 0, {}
    for f in forms:
        for p, n in occurrences(f).items():
            tot += n
            where[os.path.basename(p)] = where.get(os.path.basename(p), 0) + n
    # DEFECT L-1, caught on THIS probe's first run and recorded rather than tidied:
    # the population was "every integer of 2+ digits in the held-out section", which
    # swept in two-digit values like the partition size itself.  Those collide with
    # ordinary prose in 426 files and the probe reported 60-odd "hits" that are not
    # leaks -- a MANUFACTURED defect, RULING CI's species, in the very probe written
    # to honour RULING CI, on its first run.  The r27 rule is the right one and is
    # restored here: only a value of >= 4 digits is DISCRIMINATING.  Shorter values
    # are still printed (RULING AS) and still counted; they just cannot abort.
    disc = len(str(v)) >= 4
    flag = ""
    if tot and disc:
        leaks.append((mask(v), tot, where))
        flag = "   <== DISCRIMINATING HIT"
    elif tot:
        flag = "   (non-discriminating: %d-digit, collides with prose)" % len(str(v))
    print("  %-10s hits=%-4d %s%s" % (mask(v), tot,
          ", ".join("%s x%d" % (k, c) for k, c in sorted(where.items())[:3]) or "none", flag))

print("\n=== PER-SHAPE VERDICT ===")
for s in shapes:
    tot, where = 0, {}
    for p, t in texts.items():
        n = t.count(s)
        if n:
            tot += n
            where[os.path.basename(p)] = n
    flag = "   <== DISCRIMINATING HIT" if tot else ""
    if tot:
        leaks.append(("[%dp]" % s.count("+"), tot, where))
    print("  %-10s hits=%-4d %s%s" % ("[%dp]" % s.count("+"), tot,
          ", ".join("%s x%d" % (k, c) for k, c in sorted(where.items())[:3]) or "none", flag))

print("\n" + "=" * 74)
print("  population = %d entries (%d ints + %d shapes)" % (len(vals) + len(shapes), len(vals), len(shapes)))
print("  DISCRIMINATING HITS = %d" % len(leaks))
print("  BURNED: nu <= 11.   LIVE: nu = 12 (this key).")
print("  Measured against the corpus, not inferred from the outing count.")
if leaks:
    print("\n  *** THE KEY IS BURNED.  RE-KEY BEFORE ANY DISPATCH. ***")
    for m, n, w in leaks:
        print("    %s appears %d time(s) in %s" % (m, n, ", ".join(sorted(w)[:4])))
    sys.exit(1)
print("\n  LIVE KEY CLEAN.  (This says nothing about whether the key's ANSWERS are")
print("  right -- that is the calibration's job, and it is a separate check.)")
sys.exit(0)
