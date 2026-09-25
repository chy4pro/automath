#!/usr/bin/env python3
"""
w133 round 19 — ADJUDICATION of the ox-alpha return against the gate pre-registered BLIND
at `orchestration/results/w133_state.md` section "Round 19" 1 (written 22:06 CDT, dispatch
22:09 CDT).

GATE A runs FIRST and is graded before any mathematics in the return is read.
HARD SELF-LIMIT 120 s.
"""
import sys, re, time
T0=time.time()
OUT="$HOME/workspace/claudecode/automath-sandbox/out/ox-alpha/w133_r19_D3C6_out.md"
KEY="$HOME/workspace/claudecode/automath/problems/wowii/w133_r19_key.key.txt"
txt=open(OUT).read()
rows=[l.rstrip("\n").split("\t") for l in open(KEY) if l.strip()]
print("="*78); print("[GATE A] held-out table, graded BEFORE any mathematics is read"); print("="*78)
print(f"  return: {len(txt)} B   first line: {txt.splitlines()[0][:100]!r}")
tbl_present = bool(re.search(r"\bU1\b",txt)) and bool(re.search(r"\bU9\b",txt))
print(f"  A3 — held-out table present? {tbl_present}")
def engine_answer(rid):
    # find the line containing the row id and pull the last field of a markdown row,
    # or the first number / YES / NO / CANNOT COMPUTE after it
    for l in txt.splitlines():
        if re.search(r"(^|[^A-Za-z0-9])"+rid+r"([^0-9]|$)",l):
            if "CANNOT COMPUTE" in l.upper(): return "CANNOT COMPUTE", l.strip()
            cells=[c.strip() for c in l.split("|") if c.strip()]
            if len(cells)>=3:
                for c in reversed(cells):
                    m=re.fullmatch(r"\*{0,2}(YES|NO|\d+)\*{0,2}",c.upper().replace("**",""))
                    if m: return m.group(1), l.strip()
                    m2=re.search(r"\b(YES|NO)\b|\b(\d+)\b",c.upper())
                    if m2: return (m2.group(1) or m2.group(2)), l.strip()
            m=re.search(r"\b(YES|NO)\b|=\s*(\d+)|\b(\d+)\b",l.upper())
            if m: return (m.group(1) or m.group(2) or m.group(3)), l.strip()
    return None, ""
H_wrong=[]; C_wrong=[]; cc=[]; missing=[]
print()
print(f"  {'row':<4}{'tier':<6}{'key':<10}{'engine':<16}verdict")
for rid,tier,g,q,ans in rows:
    e,line=engine_answer(rid)
    if e is None: v="MISSING"; missing.append(rid)
    elif e=="CANNOT COMPUTE": v="CANNOT COMPUTE (A2: accepted, no penalty)"; cc.append(rid)
    elif str(e).upper()==str(ans).upper(): v="correct"
    else:
        v="**WRONG**"
        (H_wrong if tier=="H" else C_wrong).append((rid,ans,e))
    print(f"  {rid:<4}{tier:<6}{str(ans):<10}{str(e):<16}{v}")
print()
if not tbl_present:
    print("  A3 FIRES -> ROUND IS VOID (table absent)"); verdict="VOID"
elif H_wrong:
    print(f"  A1 FIRES -> ROUND IS VOID. Wrong Tier-H rows: {H_wrong}"); verdict="VOID"
else:
    verdict="NOT VOID"
    print(f"  A1 does not fire: all Tier-H rows correct or CANNOT COMPUTE -> {verdict}")
    if C_wrong: print(f"  A4 -> TRACEABLE DOWNGRADE on Tier-C rows: {C_wrong}")
    else: print("  A4 does not fire: no Tier-C row is wrong")
print(f"  CANNOT COMPUTE rows (A2, accepted): {cc if cc else 'none'}")
print(f"  MISSING rows: {missing if missing else 'none'}")
print()
print("="*78); print("[GATE B] compliance probes, mechanical"); print("="*78)
def probe(name,cond,detail=""):
    print(("  HIT   " if cond else "  clear ")+name+(f"   [{detail}]" if detail else ""))
    return cond
u=txt.upper()
probe("B4 — the return uses an n-bound (refused at adjudication, G49)",
      bool(re.search(r"\bN\s*(>=|<=|≥|≤)\s*\d",u)) and "CLOSED ROUTE" not in u[:0] , 
      "grep for 'n >= <int>' / 'n <= <int>'")
probe("B5 — the return claims path >= 7 from Case-2-forcedness",
      "CASE-2-FORCED" in u and "PATH >= 7" in u.replace("PATH ≥ 7","PATH >= 7"))
probe("B6 — the return asserts diam(CE-2) = 2 (a fact the brief refutes explicitly)",
      "DIAM(CE-2) = 2" in u or "DIAMETER 2" in u and "CE-2" in u)
probe("PART 7.4 — does it state where it fails on CE-1, CE-2 and R?",
      all(k in txt for k in ("CE-1","CE-2")) and re.search(r"\bR\b",txt) is not None)
probe("does it treat M1/M2 as mathematical material (brief forbids it)",
      bool(re.search(r"M1|M2",txt)) and bool(re.search(r"counterexample.{0,40}M[12]",txt,re.I)))
print()
print(f"GATE A VERDICT: {verdict}")
print(f"elapsed {time.time()-T0:.1f}s")
