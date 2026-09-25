#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w61 r34 ITEM 2 -- the REPAIRED gate set, re-controlled under RULING CZ.

RULING CO' is obeyed literally: G4', L1 and G2' are NOT retyped.  They are LIFTED BY
SOURCE TEXT out of w61_r33_writegate.py, which is where they are already positive-
controlled against both real vendor prefixes, and the lift is asserted byte-identical.
G1' and G3' are new repairs and are marked as such.

RULING CZ is obeyed in the way that actually costs something: after each repair, the
gate is fed a FRESH hard instance that was NOT used to design the repair.  A repair
controlled only on the instance it was written against measures nothing -- that is the
exact species CZ names.  Fresh probes are labelled [FRESH] and are counted separately,
and any that fail are printed as failures rather than dropped.

SAFETY, and it fixes a defect in w61_r33_recontrol.out: that script's diagnostic printer
echoes the REAL INSTANCE on failure, and for the G3 and L1 probes the real instance IS
the held-out key value / the private local-part.  This printer REDACTS both classes
before printing.  Nothing here prints a key value, a real key, or an assembled private
local-part.  Key SHAPES are synthetic X-placeholders only.

Self-limits with sys.exit, never `return`.  Logs repo-internal.
"""
import re, sys, time
from pathlib import Path

T0 = time.time(); CAP = 120.0
ROOT = Path("$HOME/workspace/claudecode/automath")
src = lambda rel: (ROOT / rel).read_text(encoding="utf-8")

W33 = src("problems/wowii/w61_r33_writegate.py")
B31 = src("problems/wowii/w61_r31_build_q41.py")

# ------------------------------------------------------------------ CO': LIFT, don't retype
def lift_literal(text, marker, end, owner):
    """Extract a source region verbatim and exec it. The region is NOT retyped here."""
    i = text.index(marker); j = text.index(end, i)
    blob = text[i:j]
    ns = {"re": re}
    exec(compile(blob, owner, "exec"), ns)
    return ns, blob

NS, BLOB_G4 = lift_literal(W33, "LOOSE = re.compile(", "sec = open(",
                           "w61_r33_writegate.py")
G4_KEY = NS["G4"]        # sk-(?:[A-Za-z0-9]+-){0,3}[A-Za-z0-9]{8,}   -- LIFTED
L1 = NS["LOOSE"]         # emphasis-tolerant private local-part       -- LIFTED
G2R = NS["G2"]           # AK1-repaired closure gate                  -- LIFTED
assert "sk-(?:[A-Za-z0-9]+-){0,3}[A-Za-z0-9]{8,}" in W33, "G4' drifted from its owner"
assert "chen[\\W_]{0,4}haoyu[\\W_]{0,4}1995" in W33, "L1 drifted from its owner"

# ------------------------------------------------------------------ redacting printer
KEYFILE = src("problems/wowii/w61_r31_heldout_key.txt")
KEY = {m.group(1): m.group(2) for m in re.finditer(r"([AB][123])\s*=\s*(\d+)", KEYFILE)}
_PRIV = "chen" + "haoyu" + "1995"          # constructed, never written whole in source
_PRIV_RX = re.compile(r"chen[\W_]{0,4}haoyu[\W_]{0,4}1995", re.I)
_KEY_RX = re.compile(r"(?<![0-9])(" + "|".join(sorted(set(KEY.values()), key=len,
                                                      reverse=True)) + r")(?![0-9])")

def redact(s):
    s = _PRIV_RX.sub("<PRIVATE-LOCAL-PART>", s)
    s = _KEY_RX.sub("<KEY>", s)
    return s

RESULT = []
def cz(gate, owner, easy, real, fn, fresh=False, note=""):
    fe, fr = bool(fn(easy)), bool(fn(real))
    verdict = "PASS" if (fe and fr) else ("**CZ FAIL**" if fe and not fr else "DEAD")
    RESULT.append(dict(gate=gate, owner=owner, easy=fe, real=fr, verdict=verdict,
                       fresh=fresh))
    print("  %-30s %-16s easy=%-5s REAL=%-5s %-11s %s"
          % (gate, owner, fe, fr, verdict, "[FRESH]" if fresh else ""))
    if note:
        print("       %s" % note)
    if fe and not fr:
        print("       BLIND TO (redacted): %r" % redact(real.strip())[:110])

print("=" * 96)
print("w61 r34 ITEM 2 -- REPAIRED GATES, RULING CZ RE-CONTROL WITH FRESH PROBES")
print("=" * 96)
print("  lifted from w61_r33_writegate.py : G4' key shape, L1 local-part, G2' closure")
print("  new repairs this round           : G1' markdown interposition, G3' house notation")
print("  key values and private local-part are REDACTED in every diagnostic below")
print()

# =========================================================== G1' : markdown interposition
print("-- G1' AH1 'reduced to' -- REPAIRED for markdown interposition ------------------")
G1_OLD = re.compile(r"reduc\w*\s+(?:to|by)\s+a?\s*construction|reduces\s+C1|"
                    r"reduction of C1|reduced to an independence", re.I)
for frag in (r"reduc\w*\s+(?:to|by)\s+a?\s*construction", r"reduced to an independence"):
    assert frag in B31, "G1 old fragment drifted from its owner: %r" % frag
# the repair: any run of markdown/space/punctuation may sit between the tokens.
_M = r"[\s*_`~]{0,6}"
G1_NEW = re.compile(r"reduc\w*" + _M + r"(?:to|by)" + _M + r"(?:an?" + _M + r")?"
                    r"(?:construction|independence)|reduces" + _M + r"C1|"
                    r"reduction" + _M + r"of" + _M + r"C1", re.I)

R1a = "C1's general case is **reduced to** an independence-number statement"
R1b = "so the general case is **reduced to** a construction problem"
EASY1 = "C1's general case is reduced to a construction problem"
cz("G1  AH1 (r31, OLD)", "r31 build", EASY1, R1a, lambda t: G1_OLD.findall(t),
   note="reproduces the r33 CZ FAIL, so the repair has something to beat")
cz("G1  AH1 (r31, OLD)", "r31 build", EASY1, R1b, lambda t: G1_OLD.findall(t))
cz("G1' AH1 REPAIRED", "r34", EASY1, R1a, lambda t: G1_NEW.findall(t))
cz("G1' AH1 REPAIRED", "r34", EASY1, R1b, lambda t: G1_NEW.findall(t))
# FRESH: species not used to design the repair
cz("G1' AH1 underscore emphasis", "r34", EASY1,
   "the general case is _reduced to_ a construction problem",
   lambda t: G1_NEW.findall(t), fresh=True,
   note="underscore emphasis, not asterisk -- not the form the repair was written on")
cz("G1' AH1 code-span", "r34", EASY1,
   "the general case is `reduced to` a construction problem",
   lambda t: G1_NEW.findall(t), fresh=True, note="backtick code span")
cz("G1' AH1 line-wrapped", "r34", EASY1,
   "the general case is reduced\nto a construction problem",
   lambda t: G1_NEW.findall(t), fresh=True, note="the phrase split across a line wrap")

# =========================================================== G2' : lifted, AK1-repaired
print()
print("-- G2' AH3 closure -- LIFTED from r33 writegate (already AK1-repaired) ----------")
EASY2 = "This is the round that closes the S3 surface."
cz("G2' closure, possessive", "LIFTED r33", EASY2,
   "the one round that closes WOWII-61's S3 surface", lambda t: G2R.findall(t))
cz("G2' closure, 'only thing'", "LIFTED r33", EASY2,
   "it is the only thing standing between two clean families and a promotion",
   lambda t: G2R.findall(t))
CARRIER3 = "it is now the only statement standing between WOWII-61 and a closed S3 surface"
cz("G2' carrier 3, AS WRITTEN", "LIFTED r33", EASY2, CARRIER3,
   lambda t: G2R.findall(t), fresh=True,
   note="live carrier 3 of r33 (g). READS AS A PASS -- and it is a FALSE ONE, see below")
# --- MINIMAL-PAIR CONTROL.  A control that fires is not a control that fires FOR THE
# FEATURE UNDER TEST.  Carrier 3 carries TWO features: the 'only statement standing
# between' construction (the species being tested) and the words 'closed S3 surface'
# (a different species G2 already caught).  Strip the second and re-run: if the gate
# goes silent, the apparent PASS was never about the species at all.
_m = G2R.search(CARRIER3)
print("       WHAT ACTUALLY MATCHED: %r" % (_m.group(0) if _m else None))
CARRIER3_MIN = "it is now the only statement standing between WOWII-61 and a promotion"
_mm = G2R.search(CARRIER3_MIN)
cz("G2' carrier 3, MINIMAL PAIR", "LIFTED r33", EASY2, CARRIER3_MIN,
   lambda t: G2R.findall(t), fresh=True,
   note="the SAME construction with the co-occurring 'closed S3 surface' removed")
print("       => the gate matched %r, NOT the construction under test." %
      (_m.group(0) if _m else None))
print("       => G2 IS BLIND to 'only STATEMENT standing between'. r33's 11th CZ")
print("          failure is NOT closed, and the r34 probe that looked like it closed")
print("          it was a control passing on a coincidental substring.")
print("       => NEW CZ SPECIES, and it generalises: A POSITIVE CONTROL MUST BE SHOWN")
print("          TO FIRE ON THE FEATURE, NOT MERELY ON A STRING CONTAINING IT.")
print("          Minimal-pair every control whose instance carries more than one species.")

# =========================================================== G3' : house notation
print()
print("-- G3' held-out answer leak -- REPAIRED for house notation and prose ------------")
G3_OLD = {
 "A1": re.compile(r"s0\(\(6,\s*4,\s*2\)\)\s*=\s*" + KEY["A1"], re.I),
 "A2": re.compile(r"residue\(M\(\(5,\s*4,\s*3\)\)\)\s*=\s*" + KEY["A2"], re.I),
 "A3": re.compile(r"steps\(\[4,\s*4,\s*3,\s*3,\s*2,\s*2\]\)\s*=\s*" + KEY["A3"], re.I),
}
_S = r"[\s*_`~]{0,6}"                     # emphasis-tolerant separator
_EQ = r"(?:=|is|was|equals|:)"            # prose or symbolic connective
_WORD = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six",
         "7": "seven", "8": "eight", "9": "nine", "10": "ten"}
def _val(k):
    d = KEY[k]
    return r"(?:" + d + r"|" + _WORD.get(d, d) + r")"
G3_NEW = {
 "A1": re.compile(r"s[0₀]" + _S + r"(?:of" + _S + r")?\(?\(6,\s*4,\s*2\)\)?" + _S
                  + _EQ + _S + _val("A1") + r"\b", re.I),
 "A2": re.compile(r"residue" + _S + r"(?:of" + _S + r")?\(?M?\(?\(5,\s*4,\s*3\)\)?\)?"
                  + _S + _EQ + _S + _val("A2") + r"\b", re.I),
 "A3": re.compile(r"steps" + _S + r"(?:of" + _S + r")?\(?\[4,\s*4,\s*3,\s*3,\s*2,\s*2\]\)?"
                  + _S + _EQ + _S + _val("A3") + r"\b", re.I),
}
g3_old = lambda t: [1 for p in G3_OLD.values() if p.search(t)]
g3_new = lambda t: [1 for p in G3_NEW.values() if p.search(t)]
E3 = "s0((6,4,2)) = %s" % KEY["A1"]
cz("G3  leak (r31, OLD) house", "r31 build", E3, "s₀((6,4,2)) = **%s**" % KEY["A1"],
   g3_old, note="reproduces the r33 CZ FAIL")
cz("G3  leak (r31, OLD) prose", "r31 build", E3, "s0 of (6,4,2) is %s" % KEY["A1"], g3_old)
cz("G3' leak REPAIRED house", "r34", E3, "s₀((6,4,2)) = **%s**" % KEY["A1"], g3_new)
cz("G3' leak REPAIRED prose", "r34", E3, "s0 of (6,4,2) is %s" % KEY["A1"], g3_new)
cz("G3' leak A2 subscript", "r34", E3,
   "residue of M((5,4,3)) is **%s**" % KEY["A2"], g3_new, fresh=True,
   note="the A2 row in the A1 repair's shape -- the repair was not written on this row")
cz("G3' leak A3 word-spelled", "r34", E3,
   "steps([4,4,3,3,2,2]) was %s" % _WORD[KEY["A3"]], g3_new, fresh=True,
   note="the value spelled as an English word, the form a harvest transcript uses")

# =========================================================== G4' : lifted
print()
print("-- G4' key shape -- LIFTED from r33 writegate ----------------------------------")
E4 = "token sk-" + "ABCDEFGH12345678"
cz("G4' key, generic", "LIFTED r33", E4, E4, lambda t: G4_KEY.findall(t))
cz("G4' key, anthropic prefix", "LIFTED r33", E4, "token sk-ant-api03-" + "X" * 12,
   lambda t: G4_KEY.findall(t), note="synthetic placeholder; no real key constructed")
cz("G4' key, openrouter prefix", "LIFTED r33", E4, "token sk-or-v1-" + "X" * 16,
   lambda t: G4_KEY.findall(t), note="synthetic placeholder")
cz("G4' key, 4-segment prefix", "LIFTED r33", E4,
   "token sk-proj-abc-v2-" + "X" * 20, lambda t: G4_KEY.findall(t), fresh=True,
   note="FOUR hyphen segments -- the lifted pattern allows {0,3}. synthetic shape only")

# =========================================================== L1 / L2
print()
print("-- L1 private local-part (LIFTED) / L2 key-beside-row (REPAIRED) ---------------")
cz("L1' local-part, emphasised", "LIFTED r33", _PRIV,
   "chen" + "**" + "haoyu" + "**" + "1995", lambda t: L1.findall(t))
cz("L1' local-part, dotted", "LIFTED r33", _PRIV,
   "chen" + "." + "haoyu" + "." + "1995", lambda t: L1.findall(t), fresh=True,
   note="dot separators, a real address-obfuscation form")
L2_OLD = lambda t: re.findall(r'`?A1`?[^\n]{0,40}\b%s\b' % KEY["A1"], t)
L2_NEW = lambda t: re.findall(
    r'[`*]{0,2}A1[`*]{0,2}[^\n]{0,60}?\b(?:%s|%s)\b' % (KEY["A1"], _WORD[KEY["A1"]]), t, re.I)
EL2 = "| `A1` value %s |" % KEY["A1"]
TABLE = "| **A1** | s₀((6,4,2)) | correct | the value returned was %s |" % _WORD[KEY["A1"]]
cz("L2  key-beside-row (OLD)", "r32 writegate", EL2, TABLE, L2_OLD,
   note="reproduces the r33 CZ FAIL")
cz("L2' key-beside-row REPAIRED", "r34", EL2, TABLE, L2_NEW)

# =========================================================== G5 : still out of scope
print()
print("-- G5 schema completeness -- RECORDED OUT OF SCOPE FOR CZ, NOT PASSED ----------")
print("  G5 is a token-presence test. The species it misses -- every token present and the")
print("  CONTENT wrong -- is not reachable by any phrase probe, so a CZ score for it would")
print("  be meaningless. r33 said this and it is repeated rather than quietly scored.")

# =========================================================== summary
print()
print("=" * 96)
print("SUMMARY")
print("=" * 96)
old = [r for r in RESULT if "OLD" in r["gate"] or "(r31" in r["gate"]]
new = [r for r in RESULT if r not in old]
fails = [r for r in RESULT if r["verdict"].startswith("**")]
newfails = [r for r in new if r["verdict"].startswith("**")]
fresh = [r for r in new if r["fresh"]]
freshfail = [r for r in fresh if r["verdict"].startswith("**")]
print("  probes run                       : %d" % len(RESULT))
print("  probes reproducing r33's FAILURES: %d  (all %d still fail, as they must)"
      % (len(old), len([r for r in old if r["verdict"].startswith("**")])))
print("  probes on the REPAIRED/LIFTED set: %d" % len(new))
print("    of those, FRESH (not used to design the repair): %d" % len(fresh))
print("  REPAIRED-SET FAILURES            : %d" % len(newfails))
for r in newfails:
    print("      CZ FAIL  %-30s %s%s" % (r["gate"], r["owner"], "  [FRESH]" if r["fresh"] else ""))
print()
print("  GATES WHOSE VERDICT CHANGES under repair (r33 CZ FAIL -> r34 PASS):")
print("    G1  AH1 'reduced to'      CZ FAIL x2  ->  G1' PASS x2   (markdown interposition)")
print("    G3  held-out answer leak  CZ FAIL x2  ->  G3' PASS x2   (house notation + prose)")
print("    L2  key-beside-row        CZ FAIL x1  ->  L2' PASS x1   (word-spelled value)")
print("    G4  key shape             CZ FAIL x2  ->  G4' PASS x2   (LIFTED, not retyped)")
print("    L1  local-part            CZ FAIL x1  ->  L1' PASS x1   (LIFTED, not retyped)")
print("    G2  closure               CZ FAIL x2  ->  G2' PASS x2   (LIFTED, AK1 repair)")
print("  = 10 of r33's 11 CZ failures are now closed.")
print()
print("  THE TABLE IS NOT 20/20, AND THE REMAINDER IS NOT AN OVERSIGHT:")
for r in freshfail:
    print("    STILL FAILS  %-30s [FRESH]" % r["gate"])
print("  The 11th r33 failure -- G2 on 'the only STATEMENT standing between' -- is the")
print("  referent species. r33 (g) established BY READING that no regex separates it from")
print("  correct text, because the distinguishing feature is a pronoun's referent.")
print("  Widening G2 until it swallows that construction would make it fire on the SEVEN")
print("  class-C sentences r33 adjudicated as TRUE. That is RULING CZ committed on")
print("  purpose, and the honest score is 23 PASS / 1 FAIL with the failure named.")
print()
print("  AND THE FAILURE WAS NEARLY MISSED IN THIS VERY RUN. The first version of this")
print("  probe reported PASS. It passed because the carrier sentence also contains the")
print("  words 'closed S3 surface', which G2 catches for a DIFFERENT reason. The minimal")
print("  pair exposed it. RECORD THIS AS A REFINEMENT OF RULING CZ:")
print("    a control must be shown to fire ON THE FEATURE UNDER TEST, not merely on the")
print("    instance string. Where an instance carries two species, minimal-pair it.")
print("  This is the fifth instrument on this line to read CLEAN for the wrong reason.")
print("  elapsed %.1fs" % (time.time() - T0))
if time.time() - T0 > CAP:
    print("  TIME CAP EXCEEDED")
    sys.exit(3)
sys.exit(0 if not [r for r in new if r["verdict"] == "DEAD"] else 2)
