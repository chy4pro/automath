#!/bin/zsh
# owner-w61 round 22 closing grep -- RUN AFTER SS7.37 was written (RW61-4 as amended).
# A grep is only ever live for what it greps; every check below names its zero-tolerance line.
cd $HOME/workspace/claudecode/automath
D=notes/proofs/wowii61_draft.md
echo "=== owner-w61 r22 closing grep  ($(date '+%Y-%m-%d %H:%M:%S %Z')) ==="

echo "\n[1] AD1 landed at all THREE sites (each proof opens with B_lo != empty)"
grep -c 'First, \*\*`B_lo ≠ ∅`\*\*' $D
echo "    want 3"

echo "\n[2] AD1 sites are the three named ones, in order (MB1 / GFAN2-HC / GFANnu-HC)"
grep -n 'Corollary MB1 (a floor on L)\|Corollary GFAN2-HC (the B-universal\|\*\*Corollary GFANν-HC\.\*\*\|First, \*\*`B_lo ≠ ∅`\*\*' $D | head -8

echo "\n[3] ZERO TOLERANCE: no hard-core proof still imports RIG/MB off the bare vacuous clause"
echo "    LIVENESS FIRST: the check must SEE all three sites before its verdict means anything."
python3 - <<'PY'
import re,pathlib
T=pathlib.Path("notes/proofs/wowii61_draft.md").read_text()
T=T.split("## §7.37 owner-w61 round 22")[0]      # SS7.37 legitimately QUOTES the defects
L=T.splitlines()
IMP=re.compile(r"Theorem RIG\b.*\b(gives|makes)\b|Theorem MB then reads")
VAC=re.compile(r"if every low vertex is\s*$|if every low vertex is B-universal")
# a ledger/adjudication TABLE row quoting an old defect report is not a proof step
sites=[(i+1,l.strip()[:78]) for i,l in enumerate(L)
       if IMP.search(l) and not l.lstrip().startswith("|")]
print("  import sites SEEN by this check :",len(sites)," (want 4 -- MB1, RIG-2, GFAN2-HC, GFANnu-HC)")
for s_ in sites: print("     line %d: %s"%s_)
# a site is GUARDED if the B_lo != empty step is in the window, OR the statement pins L
# numerically in its own hypothesis (Corollary RIG-2: "with `L >= 2` and every low vertex ...")
NUM=re.compile(r"`L = \d`|`L ≥ [1-9]`|`L ≤ 2ν")
bad=[]
for s_ in sites:
    win="\n".join(L[max(0,s_[0]-8):s_[0]])
    if "`B_lo ≠ ∅`" in win: continue
    if NUM.search(win):
        print("     line %d GUARDED by a numeric L floor in its own hypothesis"%s_[0]); continue
    bad.append(s_)
print("  UNGUARDED import sites :",len(bad)," (want 0)")
for b in bad: print("     ",b)
vac=[(i+1,l.strip()[:78]) for i,l in enumerate(L) if VAC.search(l)]
print("  statements carrying the vacuous scope clause :",len(vac))
for v in vac: print("     line %d: %s"%v)
PY

echo "\n[4] Theorem GFANnu is NOT reached: its statement still carries its own L floor"
grep -c '\*\*Theorem GFANν (`1 ≤ ν ≤ 10`).\*\* For every `τ`, every `ν` with \*\*`1 ≤ ν ≤ 10`\*\* and' $D
echo "    want 1"
echo "    -- RIG is cited NOWHERE inside Theorem GFANnu's statement+proof block; B_lo never occurs there:"
python3 - <<'PY'
import re,pathlib
L=pathlib.Path("notes/proofs/wowii61_draft.md").read_text().splitlines()
a=[i for i,l in enumerate(L) if l.startswith("> **Theorem GFANν (`1 ≤ ν ≤ 10`).**")][0]
b=[i for i,l in enumerate(L) if l.startswith("> **Corollary GFANν-HC.**")][0]
blk="\n".join(L[a:b])
print("    block = draft lines %d..%d (Theorem GFANnu through, but excluding, Corollary GFANnu-HC)"%(a+1,b))
print("    'Theorem RIG' as a PROOF STEP in the block :",len(re.findall(r"Theorem RIG\b.*\b(gives|makes)\b",blk)),"(want 0)")
print("    'Theorem RIG' mentioned at all in the block :",blk.count("Theorem RIG"),"(want 1 -- Repair AB1's downstream-consumer note)")
for i,l in enumerate(L[a:b]):
    if "Theorem RIG" in l: print("       line %d: %s"%(a+i+1,l.strip()[:88]))
print("    'B_lo' anywhere in the block :",blk.count("B_lo"),"(want 0)")
print("    statement's own floor present :", "`1 ≤ ν ≤ 10`" in blk and "`L ≥ ν + 1`" in blk)
PY

echo "\n[5] the facts AD1 RESTS on are unmoved"
grep -c '\*\*Theorem MB (master budget).\*\* In the hard core, for `L ≥ 1`' $D; echo "    want 1 (MB really is L>=1, so Q37's exclusion route is really unavailable)"
grep -c '\*\*Theorem K is the case `L = 0`.\*\* Then (LOW1) reads `ν ≤ 0`' $D; echo "    want 2 (SS7.6 A + the SS7.37 quotation)"
grep -c '`L = 0` is impossible: Theorem K would make B a clique' $D; echo "    want 1 (Corollary SL-HC)"
grep -c '`L = 0` is Theorem K + Observation R1' $D; echo "    want 2 (Corollary FAN-HC + the SS7.37 quotation)"
grep -c 'Theorem SL (slack positivity).\*\* Assume the reductio' $D; echo "    want 1"

echo "\n[6] AD3, checked on the MATHEMATICS TEXT ONLY (SS7.37 quotes the defect verbatim, as it must)"
awk '/^## §7.37 owner-w61 round 22/{exit} {print}' $D > /tmp/w61_r22_pre737.md
printf "    bare \"all of B_hi (DICH(b))\" in the maths text : "; grep -c 'all of `B_hi` (DICH(b))' /tmp/w61_r22_pre737.md
echo "    want 0  [ZERO TOLERANCE]"
printf "    \"remaining vertices of B_hi (DICH(b))\"          : "; grep -c '\*\*remaining\*\* vertices of `B_hi` (DICH(b))' /tmp/w61_r22_pre737.md
echo "    want 2"
printf "    legitimate \"all of B_hi high\" (GFan definition)  : "; grep -c 'all of `B_hi` high' /tmp/w61_r22_pre737.md
echo "    want 1"

echo "\n[7] repair labels registered exactly once each as LANDED"
for t in AD1 AD3; do printf "    %s LANDED : " $t; grep -c "\*\*Repair $t LANDED\*\*" $D; done
echo "    want 1 each; AD2 is a lint, not a draft edit:"
printf "    AD2 in draft as a LANDED repair (want 0): "; grep -c '\*\*Repair AD2 LANDED\*\*' $D

echo "\n[8] draft md5 matches the repair script's recorded post-value + SS7.37 appended once"
md5 -q $D
echo "    (repair-script post-md5 was 5508104694060d84cb29ab8901cdecae BEFORE SS7.37 was appended)"
grep -c '^## §7.37 owner-w61 round 22' $D; echo "    want 1"
grep -c '^## §7.36 owner-w61 round 21' $D; echo "    want 1 (r21 entry not clobbered)"

echo "\n[9] ZERO TOLERANCE: nothing in SS7.37 promotes anything"
awk '/^## §7.37/,0' $D | grep -c 'moves to PROVED-S3\|→ PROVED-S3\|is PROMOTED\|promotes to'
echo "    want 0"
awk '/^## §7.37/,0' $D | grep -c 'Nothing promotes here'; echo "    want 1"

echo "\n[10] held-out key still not leaked into any brief"
printf "    98384/791/131/f4965d68 anywhere under prompts/ : "
grep -rl '98384\|98 384\|: 791\|= 131' prompts/ 2>/dev/null | wc -l
echo "    want 0"

echo "\n[11] H3/H4 second implementation + two-way roster diff"
printf "    second impl roster rows : "; wc -l < problems/wowii/w61_r22_h34_second_roster.txt
echo "    want 791"
grep -E 'TWO-WAY DIFF CLEAN|IN impl-1 NOT IN impl-2|IN impl-2 NOT IN impl-1|ORDERED IDENTITY' problems/wowii/w61_r22_h34_rosterdiff.out | sed 's/^/    /'
grep -E '^(CHECK A|CHECK B|H4      |H3 total|H3 per-E|SHAPES  )' problems/wowii/w61_r22_h34_second_impl.out | sed 's/^/    /'

echo "\n[12] brief lint LIVENESS (RULING S) -- it must FAIL on the artifact that motivated it"
grep -E 'r20 findings|toolkit-as-xref present|doubled-article present|LIVENESS:' problems/wowii/w61_r22_brieflint.out | sed 's/^/    /'

echo "\n[13] the blind regex is quoted correctly and the historical builder is UNTOUCHED"
grep -n 'the certified toolkit", out)' problems/wowii/w61_r14_build_gfan_brief.py | sed 's/^/    /'
printf "    r14 builder mtime (must predate this round) : "; stat -f '%Sm' problems/wowii/w61_r14_build_gfan_brief.py
printf "    r20 brief   mtime (must predate this round) : "; stat -f '%Sm' prompts/w61_S3_GFAN_r20.md
printf "    Q37 harvest mtime (must predate this round) : "; stat -f '%Sm' problems/wowii/w61_S3_GFAN_r20_gemini_Q37.md

echo "\n[14] harvest byte-identity is described as NOT established, in the file AND in SS7.37"
grep -c 'Byte-identity against the page was NOT re-established' problems/wowii/w61_S3_GFAN_r20_gemini_Q37.md; echo "    want 1"
awk '/^## §7.37/,0' $D | grep -c 'NOT established'; echo "    want >=1"

echo "\n[15] OPS-11 / auto-title rules still registered exactly once (r21 carry-forward)"
printf "    OPS-11 headings in notes/web_model_ops.md : "; grep -c '^## OPS-11' notes/web_model_ops.md
echo "    want 1 (the forward reference at the OPS-10 write-up is a pointer, not a second registration)"
echo "=== end ==="
