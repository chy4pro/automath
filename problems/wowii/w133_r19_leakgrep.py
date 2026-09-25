#!/usr/bin/env python3
"""
w133 round 19 — MANDATORY PRE-DISPATCH BRIEF PASS.
Implements planner RULING V / DEBT-5 (adopted from this owner's round-18 finding):
*a held-out row must be checked for leakage against EVERY section of its own brief, not
only against the rest of the table* — plus RULING W (refuse by name and citation, never by
restating the refused route's content).

Runs BEFORE dispatch. Exit != 0 blocks the dispatch.
"""
import sys, re, itertools
BRIEF="$HOME/workspace/claudecode/automath-sandbox/briefs/w133_r19_D3C6.md"
KEY="$HOME/workspace/claudecode/automath/problems/wowii/w133_r19_key.key.txt"
FAIL=[]
def check(n,c,d=""):
    print(("  PASS  " if c else "  FAIL  ")+n+(f"   [{d}]" if d else ""))
    if not c: FAIL.append(n)
txt=open(BRIEF).read()
rows=[l.rstrip("\n").split("\t") for l in open(KEY) if l.strip()]
print("="*78); print("[1] RULING V / DEBT-5 — every held-out ANSWER grepped against the FULL brief"); print("="*78)
# 1a. the graph tokens must appear ONLY in PART 6 and the one sentence introducing it
i6=txt.index("PART 6 — HELD-OUT TABLE")
head,tail=txt[:i6],txt[i6:]
for tok in ("M1","M2"):
    hits=[m.start() for m in re.finditer(r"\b"+tok+r"\b",head)]
    check(f"the token `{tok}` appears NOWHERE before PART 6", not hits,
          f"{len(hits)} occurrences before PART 6")
# 1b. no answer value may appear in the brief attached to its own quantity name
qpat={"Is M1 C4-free?":None,"a(0)":r"a\(0\)\s*=\s*",
      "a(7)":r"a\(7\)\s*=\s*","dist(1,4)":r"dist\(1,\s*4\)\s*=\s*",
      "Does {0,1,2,3,4,5} induce a 6-cycle?":None,
      "path(M1)":r"path\(M1\)\s*=\s*","sum_v a(v) over all 10 vertices":r"sum a\(M1\)\s*=\s*",
      "diam(M2)":r"diam\(M2\)\s*=\s*","path(M2)":r"path\(M2\)\s*=\s*"}
for rid,tier,g,q,ans in rows:
    pat=qpat.get(q)
    if pat is None:
        # boolean rows: the brief must not assert the answer word next to the graph token
        ctx=[l for l in txt.split("\n") if g in l and re.search(r"\b(YES|NO)\b",l)
             and "YES / NO" not in l]
        check(f"{rid} ({q}) — no YES/NO verdict about {g} is stated anywhere in the brief",
              not ctx, "; ".join(ctx)[:120])
    else:
        m=re.search(pat+re.escape(str(ans)),txt)
        check(f"{rid} ({q} = {ans}) — the answer is not printed anywhere in the brief", m is None,
              "" if m is None else txt[max(0,m.start()-40):m.end()+10])
# 1c. the round-18 failure mode, generalised: any line that mentions a held-out graph AND
#     an equals-sign statistic, outside the edge-list lines
badlines=[]
for l in txt.split("\n"):
    if ("M1" in l or "M2" in l) and "=" in l and "edges" not in l and "n = 1" not in l \
       and "|" not in l and "TEST GRAPHS" not in l:
        badlines.append(l.strip())
check("no line outside the table/edge-lists states an `=` fact about M1 or M2",
      not badlines, "; ".join(badlines)[:200])
# 1d. each edge list appears exactly once
for tok,ne in (("0-1, 1-2, 2-3, 3-4, 4-5, 5-0, 0-6, 1-6",1),("0-6, 2-7, 4-8, 1-9, 3-10, 5-11",1)):
    check(f"the fragment `{tok[:28]}...` appears exactly {ne} time(s)", txt.count(tok)==ne,
          f"{txt.count(tok)}")

print(); print("="*78); print("[2] RULING W — the refused route is cited by NAME, not restated"); print("="*78)
forbidden=[("10 + 2k","G49's size formula"),("10+2k","G49's size formula"),
           ("25 + 3k","G49's a-value sum"),("25+3k","G49's a-value sum"),
           ("pendant triangle","G49's construction"),("F_k","G49's family symbol"),
           ("path(F_k)","G49's path value")]
for s,why in forbidden:
    check(f"the brief does NOT reprint {why} (`{s}`)", s not in txt)
check("the brief DOES cite G49 by name and registry location",
      "Theorem G49" in txt and "28.2" in txt)
check("and states only G49's CONCLUSION, with the omission declared",
      "deliberately not reproduced here" in txt)

print(); print("="*78); print("[3] the round-18 false facts must be CORRECTED, not merely dropped"); print("="*78)
check("the brief states diam(CE-2) = 3", "`diam(CE-2) = 3`, NOT 2" in txt)
check("the brief states path(R) = 6 with an induced witness",
      "`path(R) = 6`" in txt and "1-2-3-5-4-6" in txt)
check("the false PART-5 hint is replaced AND named as an error",
      "pairwise opposite" in txt and "IMPOSSIBLE" in txt)
check("the corrected classification F8 ships with its proof", "F8 (off-cycle attachment" in txt)

print(); print("="*78); print("[4] gate-shape obligations from the pre-registration"); print("="*78)
tiers=re.findall(r"\|\s*U\d\s*\|.*?\|\s*\*\*([HC])\*\*\s*\|",txt)
check("the table has exactly 9 rows", len(tiers)==9, f"{len(tiers)}")
check("at least 2 hand-derivable and at least 2 non-hand-derivable rows, tiers disclosed",
      tiers.count("H")>=2 and tiers.count("C")>=2, f"H={tiers.count('H')} C={tiers.count('C')}")
check("CANNOT COMPUTE is offered on every row", "accepted on **every** row" in txt)
check("all three controls are mandatory and named", all(k in txt for k in ("CE-1","CE-2","`R`")))
check("no API key or secret appears in the brief",
      not re.search(r"sk-|OR_KEY|OC_GO_KEY|Bearer",txt))
print()
print(f"FAILURES: {len(FAIL)}"+("" if not FAIL else "  -> "+"; ".join(FAIL)))
print("DISPATCH BLOCKED" if FAIL else "DISPATCH CLEARED")
sys.exit(1 if FAIL else 0)
