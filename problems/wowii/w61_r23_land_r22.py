#!/usr/bin/env python3
"""owner-w61 round 23 -- land registry row R-22 (Theorem GFANnu -> PROVED-S3, on the
planner's certification of 2026-08-23) and Repair AE1 (from the RULING AQ sweep).

PATCH, NOT REBUILD.  Every edit is an anchored replace with an exact-count assert.

R-22  Theorem GFANnu -> PROVED-S3.  Corollary GFANnu-HC STAYS AT 1 FAMILY and the status
      line says so in the same breath, because the two are adjacent and a reader will
      otherwise carry the promotion across.

AE1   From the round-23 sweep: Theorem RIG's trailing bound is glossed "In the hard core
      (i.e. adding the reductio)", which equates "the hard core" with frame + reductio and
      drops the `tau >= 4` the canonical definition (SS7.10 Repair F3) folds in.  That is an
      affirmative hypothesis-WEAKENING claim about an import -- the same class Repair AB2
      was landed on, three lines away in the same statement.  Sound, but the licence was
      never written at the site.  BOOKKEEPING: no statement and no conclusion changes.

POST-REPAIR RECORD ASSERTION (three layers deep on this line is a pattern, not an accident):
the script does not only land the repair, it asserts THE RECORD OF THE REPAIR landed --
each label present exactly once as LANDED, and the promotion's row number present.
"""
import hashlib, pathlib, re, sys

ROOT = pathlib.Path("$HOME/workspace/claudecode/automath")
DRAFT = ROOT / "notes/proofs/wowii61_draft.md"

src = DRAFT.read_text()
pre_md5 = hashlib.md5(src.encode()).hexdigest()
out = src
patches = 0


def rep(old, new, tag):
    global out, patches
    c = out.count(old)
    assert c == 1, f"[{tag}] expected 1 occurrence of anchor, found {c}"
    out = out.replace(old, new)
    assert out.count(old) == new.count(old), f"[{tag}] anchor count wrong after replace"
    assert out.count(new) == 1, f"[{tag}] replacement not unique"
    patches += 1
    print(f"  [{tag}] landed")


# ---------------------------------------------------------------- R-22, at SS7.13 D's status
rep(
"""*Status 〔**updated 2026-08-22 00:5x CDT**〕: **Lemma TAIL — PROVED-S3** (§7.22 (d),
row R-15: Q24 + Q27 two-family, planner-confirmed 08-18 20:38). **Theorem GFANν
(`ν ≤ 6`), Corollary GFANν-HC — PROVED, 0 clean S3 rounds** (Q25's J-GFANNU returned
GAP on a briefing defect, now repaired as Z2/§7.22 (c); the re-round reviews the new
text). GFANν computer-assisted as declared, with the demarcation line moved by Z2.
(C1)/(C2) — **CONJECTURE**.*""",
"""*Status 〔**updated 2026-08-23 01:4x CDT**〕: **Lemma TAIL — PROVED-S3** (§7.22 (d),
row R-15: Q24 + Q27 two-family, planner-confirmed 08-18 20:38).
**Theorem GFANν (`1 ≤ ν ≤ 10`) — PROVED-S3** (§7.38 (a), **row R-22**, planner
certification 2026-08-23; two cross-family clean readings — Meta/muse-spark and
Google/Gemini, the latter's void gate `5/5` exact including the first non-hand rows any
judge has ever computed — with the computational half separately discharged by **two
independent implementations of ours**, the second written from the §7.22 (c-1) spec alone
and diffed at roster level in both directions, `791` rows, `0` and `0`). The promotion
rests on three grounds, each checkable against this text in one step: (1) the theorem's
own quantifiers `1 ≤ ν ≤ 10`, `L ≥ ν+1` put `L = 0` outside its range; (2) it never
imports Theorem RIG — `B_lo` occurs **0** times in its statement-plus-proof block; (3)
**it is UPSTREAM** — the corollaries consume RIG *and* GFANν, so a consumer's broken
import cannot reach the supplier, which also clears Theorem GFAN2 and Theorem RIG.
**Corollary GFANν-HC does NOT move and stays at 1 family** — the promotion is Theorem
GFANν's alone, and adjacency is not inheritance. One residual is recorded rather than
waived: byte-identity of the Q37 harvest is **not** established, bounded at `+313` code
points (`+3.4 %`), direction *added* not truncated. It weakens the **transcript**, not the
**grades**: the graded content is corroborated independently of the transcript (the
judge's own code re-run here, our from-spec implementation matching its `H3`/`H4`, and the
void gate graded against our key). GFANν computer-assisted as declared, with the
demarcation line moved by Z2. (C1)/(C2) — **CONJECTURE**.*""",
"R-22/status")

# ---------------------------------------------------------------- AE1, at Theorem RIG's scope note
rep(
"""certified reduced-hypothesis Lemma 4, not asserted in a scope note.〕""",
"""certified reduced-hypothesis Lemma 4, not asserted in a scope note.〕

〔**Repair AE1 LANDED**, 2026-08-23 01:4x CDT — BOOKKEEPING, found by the round-23
RULING AQ sweep (`problems/wowii/w61_r23_import_sweep.py`), **the same species and the
same statement as Repair AB2, three lines above**. The statement's trailing sentence
glosses *"In the **hard core** (i.e. adding the reductio)"*. That gloss equates *the hard
core* with **frame + reductio**, but the canonical definition of the term (§7.10, Repair
F3) is **frame + reductio + `τ ≥ 4`**. So the sentence claims the bound `ν ≤ L−1` under a
**weaker** hypothesis than the corollary it imports (Corollary MB1, stated *in the hard
core*) is stated for — an affirmative hypothesis-weakening claim about an import, which
is exactly what AB2 exists to police. **The claim is TRUE and nothing changes**: the
chain MB1 → Theorem MB → Theorem SL consumes only `τ ≥ 2`, never `τ ≥ 4`, and `τ ≥ 2`
follows from the frame's `diam = 4` alone by the elementary argument Repair AA1 wrote out
at Corollary SL-HC (a connected graph with `τ ≤ 1` is edgeless or a star, hence
`diam ≤ 2`). **What was missing is that sentence, at this site.** Reading, licensed:
*"In the hard-core frame plus the reductio — which is the canonical hard core minus its
`τ ≥ 4` rider, a rider this chain does not consume — one has in addition `ν ≤ L−1`."*〕""",
"AE1/RIG-scope")

# ---------------------------------------------------------------- write + record assertions
assert patches == 2, patches
DRAFT.write_text(out)
post_md5 = hashlib.md5(out.encode()).hexdigest()
print(f"  draft md5 {pre_md5} -> {post_md5}")

print("\nPOST-REPAIR RECORD ASSERTIONS (the repair is not done until its RECORD is on the page)")
txt = DRAFT.read_text()
checks = [
    ("AE1 registered exactly once as LANDED", txt.count("**Repair AE1 LANDED**"), 1),
    ("row R-23 named in the SS7.13 D status line", txt.count("**row R-23**"), 1),
    ("GFANnu-HC's non-promotion said in the same breath",
     txt.count("**Corollary GFANν-HC does NOT move and stays at 1 family**"), 1),
    ("byte-identity residual recorded as transcript-not-grades",
     len(re.findall(r"weakens the \*\*transcript\*\*, not the\n\*\*grades\*\*", txt)), 1),
]
ok = True
for name, got, want in checks:
    flag = "OK " if got == want else "FAIL"
    ok &= got == want
    print(f"  [{flag}] {name}: {got} (want {want})")
print("\nRESULT:", "ALL RECORD ASSERTIONS PASS" if ok else "RECORD DID NOT LAND")
sys.exit(0 if ok else 1)
