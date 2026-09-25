#!/usr/bin/env python3
"""owner-w61 round 27 -- Q39 HARVEST GATE, in the pre-registered order.

  (1) VOID GATE, blind and FIRST: Section 0 against the r17 key, exact match.
  (2) RULING CD: a printed execution artifact is NOT evidence.  The report
      declares "I ran code."  It also WROTE the code to disk, so the claim is
      testable HERE -- and only re-running it here counts.
  (3) the joints, the IMPORT INTERFACE ROLL CALL, and the bracket COUNT check.

RULING AS: both populations printed before the verdict.
LEDGER NOTE, written before the dispatch and unchanged by whatever this says:
Q39 BUYS ZERO toward the two-family bar.  Corollary GFANnu-HC stays at 1 family.
"""
import hashlib, re, subprocess, sys

REPORT = "problems/wowii/w61_S3_GFAN_r26.md"
CHECK  = "problems/wowii/w61_S3_GFAN_r26_check.py"
KEY    = "problems/wowii/w61_r17_heldout_key.txt"

def md5(p): return hashlib.md5(open(p,'rb').read()).hexdigest()
for p in (REPORT, CHECK, KEY):
    print("  %-46s md5=%s  bytes=%d" % (p, md5(p), len(open(p,'rb').read())))
print()

kt = open(KEY).read()
rt = open(REPORT).read()

# --- the key, transcribed, then GUARDED against the key file itself (r25's
#     transcription guard: a hand-copied key is an unchecked import).
K = {
 "H1": ([14,12,16,10], ["s0([12+6+4]) = 14","s0([9+7+3+3]) = 12",
                        "s0([14+5+2+1]) = 16","s0([8+8+6]) = 10"]),
 "H2": (98384, ["S(11) = sum_{E=1}^{10} (11-E) p(E) p(22-E) = 98384"]),
 "H2T": ([7920,11286,11760,13475,12474,12705,10560,8910,6060,3234], []),
 "H3": (791, ["E>=1 survivors at nu = 11 : 791"]),
 "H3S": ({1:6,2:14,3:21,4:35,5:47,6:85,7:110,8:155,9:170,10:148},
         ["per-E split               : {1: 6, 2: 14, 3: 21, 4: 35, 5: 47, 6: 85, 7: 110, 8: 155, 9: 170, 10: 148}"]),
 "H4": (131, ["#{lambda |- 22 : s0(lambda) = 13} = 131"]),
 "H5": (("NO",16), ["clears in exactly L = 13 steps?  NO   (actual step count 16)"]),
}
print("=== TRANSCRIPTION GUARD: every key value re-read out of the key FILE ===")
bad = 0
for tag,(v,gs) in K.items():
    for g in gs:
        ok = g in kt
        bad += 0 if ok else 1
        print("   %-4s %-5s %s" % (tag, "OK" if ok else "FAIL", g))
if bad: sys.exit("TRANSCRIPTION GUARD FAILED -- key mis-transcribed into the gate")
print("   transcription guard: %d/%d clean\n" % (sum(len(g) for _,g in K.values()),
                                                 sum(len(g) for _,g in K.values())))

# --- POPULATION: the report's Section 0 rows, printed before grading
sec0 = rt.split("## 0.")[1].split("## 1.")[0]
print("=== POPULATION: the report's Section 0, verbatim, BEFORE grading ===")
for ln in sec0.strip().split("\n"):
    print("   | " + ln)
print()

def nums(s):
    return [int(x.replace(",","").replace(" ","")) for x in re.findall(r"\d[\d, ]*\d|\d", s)]

rows, void_hand, exact = [], 0, 0
r_h1 = re.search(r"\| H1 \|(.*?)\|", sec0, re.S).group(1)
got = [int(x) for x in re.findall(r"\]\s*:\s*(\d+)", r_h1)]
rows.append(("H1","HAND",K["H1"][0],got,got==K["H1"][0]))
r_h2 = re.search(r"\| H2 \|(.*?)\n", sec0, re.S).group(1)
g2 = nums(r_h2)
rows.append(("H2","HAND",[K["H2"][0]],[g2[1]] if len(g2)>1 else g2,
             K["H2"][0] in [n for n in nums(sec0.split("| H2 |")[1].split("\n")[0])]))
# DEFECT G-1, caught on the first run and recorded rather than tidied away:
# this line read the WHOLE H2 cell for integers and so swallowed the '1' and
# '10' of the label "Terms for `E=1..10`", producing a WRONG on ten terms that
# are in fact all correct -- and that single manufactured row VOIDED an
# admissible report.  A checker that manufactures a defect is the species this
# line has spent four rounds on; the direction of error was against the JUDGE,
# which is the safer direction but not an excuse.  Root fix: the term list is
# the PLUS-JOINED RUN, so parse that structure and nothing else.
_m2 = re.search(r"(\d+(?:\+\d+)+)", sec0.split("| H2 |")[1].split("\n")[0])
t2 = [int(x) for x in _m2.group(1).split("+")] if _m2 else []
rows.append(("H2-terms","HAND",K["H2T"][0],t2,t2==K["H2T"][0]))
h3line = sec0.split("| H3 |")[1].split("\n")[0]
g3 = int(re.search(r"`(\d+)`", h3line).group(1))
g3s = {int(a):int(b) for a,b in re.findall(r"(\d+):(\d+)", h3line)}
rows.append(("H3","NON-HAND",K["H3"][0],g3,g3==K["H3"][0]))
rows.append(("H3-split","NON-HAND",K["H3S"][0],g3s,g3s==K["H3S"][0]))
h4line = sec0.split("| H4 |")[1].split("\n")[0]
g4 = int(re.search(r"`(\d+)`", h4line).group(1))
rows.append(("H4","NON-HAND",K["H4"][0],g4,g4==K["H4"][0]))
h5line = sec0.split("| H5 |")[1].split("\n")[0]
g5 = ("NO" if re.search(r"\bNO\b", h5line) else "YES",
      int(re.search(r"step count[^0-9]*(\d+)", h5line).group(1)))
rows.append(("H5","HAND",K["H5"][0],g5,g5==K["H5"][0]))

print("=== VOID GATE (exact match; a stated wrong value voids, CANNOT COMPUTE does not) ===")
for tag,tier,k,g,ok in rows:
    exact += ok
    if not ok and tier=="HAND": void_hand += 1
    print("   %-9s %-9s key=%-58s got=%-58s %s" % (tag,tier,k,g,"EXACT" if ok else "*** WRONG ***"))
print("   %d/%d EXACT;  wrong HAND rows = %d" % (exact,len(rows),void_hand))
print("   CANNOT COMPUTE used: %d time(s)" % rt.count("CANNOT COMPUTE"))
VOID = void_hand >= 1
print("   VOID GATE: %s\n" % ("*** VOID ***" if VOID else "PASS -- the report is admissible"))

# --- RULING CD: only re-running the code HERE counts
print("=== RULING CD: re-running the judge's OWN script here (a printed Output: block is not evidence) ===")
print("   declared: %s" % rt.split("\n")[0])
r = subprocess.run([sys.executable, CHECK], capture_output=True, text=True, timeout=900)
out = r.stdout + r.stderr
print("   exit=%d  stdout bytes=%d" % (r.returncode, len(out)))
claimed = open("problems/wowii/w61_S3_GFAN_r26_check.out").read()
key_lines = [l.strip() for l in claimed.strip().split("\n")
             if re.search(r"mismatch|misses|SCRIPT_STATUS|printed=|=\d", l)]
agree = sum(1 for l in key_lines if l in out)
print("   claimed .out lines re-derived here: %d / %d" % (agree, len(key_lines)))
print("   SCRIPT_STATUS in OUR run: %s" %
      (re.search(r"SCRIPT_STATUS=\w+", out).group(0) if "SCRIPT_STATUS" in out else "ABSENT"))
print("   EXECUTION CLAIM: %s" %
      ("STANDS -- re-run here reproduces it" if r.returncode==0 and agree>=len(key_lines)*0.9
       else "*** NOT REPRODUCED HERE ***"))
open("problems/wowii/w61_r27_q39_rerun.out","w").write(out)
print()
print("=== LEDGER (written before the dispatch, unchanged by the above) ===")
print("   Q39 BUYS ZERO toward the two-family bar.  Corollary GFANnu-HC stays at 1 family.")
