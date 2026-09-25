#!/usr/bin/env python3
"""owner-w61 round 22 -- attach the dated Repair AD3 notes at both AD3 sites.

The prose fix landed in w61_r22_repair_ad.py; the closing grep [7] caught that it landed
SILENTLY -- no dated bracket at either site, so a later reader could not tell the sentence
had been repaired or why. Every repair in this document carries its diagnosis at the site.
Caught by the grep, which is what the grep is for.
"""
import hashlib, pathlib
ROOT = pathlib.Path("$HOME/workspace/claudecode/automath")
DRAFT = ROOT / "notes/proofs/wowii61_draft.md"
src = DRAFT.read_text(); out = src; n = 0

def rep(old, new, tag):
    global out, n
    assert out.count(old) == 1, f"[{tag}] anchor count {out.count(old)}"
    out = out.replace(old, new); n += 1
    print(f"  [{tag}] landed")

# --- FAN-6' (SS7.13 A) : the full note, at the site Q37 actually read
rep("> `max(M_1) ≤ p`. Contradiction. ∎\n>\n"
    "> 〔This is Lemma FAN-6 with its hypothesis stated in the form its proof actually\n",
    "> `max(M_1) ≤ p`. Contradiction. ∎\n>\n"
    "> 〔**Repair AD3 LANDED**, 2026-08-23 01:0x CDT, from Q37 Defect 4 — BOOKKEEPING, and\n"
    "> correctly spotted. The sentence read *“All of `B_hi` (DICH(b)) … lie in `block_j`”*.\n"
    "> At step `j` the current head and the `j−1` earlier heads are already **deleted**, so\n"
    "> what lies in `block_j` is the `p−j` **remaining** high vertices — which is exactly what\n"
    "> the next clause's `(p−j)` counts. **The arithmetic was already right and the\n"
    "> conclusion is unaffected**; the prose named a set larger than the one it then counted.\n"
    "> Landed as a **class** fix: the identical sentence, with the identical error, is in this\n"
    "> lemma's §7.8 E ancestor **Lemma FAN-6**, which Q37 never saw because the unprimed\n"
    "> FAN-`n` lemmas were outside its brief. Both sites now read *“all **remaining**\n"
    "> vertices of `B_hi`”*. Species: **prose names the pre-deletion set, arithmetic uses the\n"
    "> post-deletion one** — the AC1b/AC3 discipline, *fix the class, not the instance*.〕\n"
    "> 〔This is Lemma FAN-6 with its hypothesis stated in the form its proof actually\n",
    "AD3-note/FAN-6p")

# --- FAN-6 (SS7.8 E) : the pointer, at the ancestor site
rep("> the block being a **prefix** of the sorted list — they are the `a_j` largest\n"
    "> entries of `M_j`. In particular **a maximum entry of `M_j` is always\n"
    "> decremented.**",
    "> the block being a **prefix** of the sorted list — they are the `a_j` largest\n"
    "> entries of `M_j` 〔**Repair AD3**, at this site: the sentence above read *“all of\n"
    "> `B_hi`”* where the `(p−j)` beside it counts only the **remaining** high vertices —\n"
    "> diagnosis at Lemma FAN-6′, §7.13 A. Conclusion unaffected.〕. In particular **a\n"
    "> maximum entry of `M_j` is always decremented.**",
    "AD3-note/FAN-6")

DRAFT.write_text(out)
print(f"\npatches landed : {n}")
print(f"draft md5 : {hashlib.md5(src.encode()).hexdigest()} -> {hashlib.md5(out.encode()).hexdigest()}")
