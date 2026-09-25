import hashlib, pathlib, re, sys
ROOT = pathlib.Path("$HOME/workspace/claudecode/automath")
D = ROOT / "notes/proofs/wowii61_draft.md"
src = D.read_text(); pre = hashlib.md5(src.encode()).hexdigest()
out = src

# --- BB1: the stale address in SS7.38's own Slice line, found by w61_mint.py at mint time
old = "**Slice.** One promotion executed (row R-22), one repair landed (AE1, BOOKKEEPING), one"
new = "**Slice.** One promotion executed (row R-23), one repair landed (AE1, BOOKKEEPING), one"
assert out.count(old) == 1, out.count(old)
out = out.replace(old, new)

body = pathlib.Path("/tmp/w61_r24_sec739.md").read_text()
assert out.endswith("\n")
out = out + "\n" + body
D.write_text(out)
post = hashlib.md5(out.encode()).hexdigest()
print(f"draft md5 {pre} -> {post}")

t = D.read_text()
checks = [
 ("SS7.39 present exactly once", t.count("## §7.39 owner-w61 round 24:"), 1),
 ("SS7.39 is the LAST section", t.rfind("## §7.3") == t.rfind("## §7.39 owner-w61 round 24:"), True),
 ("Q38 dispatch named once", t.count("**Q38 DISPATCHED**"), 1),
 ("sol's strength stated, not glossed", t.count("has never judged the Corollary"), 1),
 ("the r20 structural withdrawal called before dispatch",
  t.count("stated BEFORE the harvest and not after"), 1),
 ("BB1 stale-address fix recorded", t.count("**BB1**"), 1),
 ("no stale R-22 in SS7.38's Slice", t.count("One promotion executed (row R-22)"), 0),
 ("sweep limits carried at the citation", t.count("numeric/non-emptiness only"), 1),
]
ok = True
for n,g,w in checks:
    f = "OK " if g == w else "FAIL"
    ok = ok and g == w
    print(f"  [{f}] {n}: {g} (want {w})")
print("ALL RECORD ASSERTIONS PASS" if ok else "RECORD ASSERTIONS FAILED")
sys.exit(0 if ok else 1)
