#!/usr/bin/env python3
"""owner-w61 round 22 -- land Repairs AD1 (MATHEMATICS, 3 sites) and AD3 (BOOKKEEPING, 2 sites)
on notes/proofs/wowii61_draft.md.

PATCH, NOT REBUILD.  Every edit is an anchored replace with an exact-count assert; the
script refuses to write if any anchor is missing or a count is wrong.

AD1 -- the Q37 Defect-1 class: a proof in the hard core imports Theorem RIG (or Theorem MB)
       to instantiate `1 <= nu <= L-1` without first supplying `B_lo != empty` (L >= 1),
       which those imports require and which the corollary's own scope clause ("if every
       low vertex is B-universal") does NOT supply -- that clause is vacuously true at L=0.
       Q37 named two sites (GFANnu-HC, GFAN2-HC).  Checking against the DRAFT rather than
       the judge's word finds a THIRD, upstream: Corollary MB1 itself.
       The exclusion Q37 proposed (Theorem MB forces mbar <= -1 at L=0) is NOT available:
       Theorem MB is itself stated "In the hard core, for L >= 1".  The draft's own
       exclusion is Theorem K + Observation R1, already written twice (Corollary SL-HC
       SS7.6 F, Corollary FAN-HC SS7.8 F).

AD3 -- the Q37 Defect-4 class: Lemma FAN-6' prose says "all of B_hi ... lie in block_j"
       where the arithmetic (p-j) counts only the REMAINING high vertices.  Same sentence,
       same error, in its SS7.8 ancestor Lemma FAN-6.  Fix the class, not the instance.

RULING S (COVERAGE != LIVENESS): every anchor below is asserted present exactly once on
the PRE-EDIT text and absent on the POST-EDIT text.
"""
import hashlib, pathlib

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
    assert out.count(old) == 0, f"[{tag}] anchor survived the replace"
    assert out.count(new) == 1, f"[{tag}] replacement is not unique"
    patches += 1
    print(f"  [{tag}] landed")

AD1NOTE = (
"> 〔**Repair AD1 LANDED**, 2026-08-23 00:5x CDT, from Q37 Defect 1 — a **MATHEMATICS**\n"
"> defect of the *missing-hypothesis* class, and the mirror image of the species this\n"
"> document has caught seven times: not *a true import nobody needs*, but **an import that\n"
"> is needed and was never made**. The scope clause “if every low vertex is B-universal” is\n"
"> **vacuously true when `B_lo = ∅`**, i.e. at `L = 0`, so it does not by itself supply\n"
"> Theorem RIG's `B_lo ≠ ∅` hypothesis (resp. Theorem MB's `L ≥ 1`), and the proof imported\n"
"> them anyway. **The statement is unaffected and remains true as written**, because the\n"
"> hard core has no `L = 0` case; what was missing was the sentence saying so, which is now\n"
"> the proof's first step. **Q37's own proposed exclusion is not available and was not\n"
"> used**: it argued that *“Theorem MB forces `m̄ ≤ −1` if `L = 0`”*, but Theorem MB is\n"
"> itself stated **“In the hard core, for `L ≥ 1`”** — applying it at `L = 0` is the same\n"
"> defect one level down. The draft's own exclusion is **Theorem K + Observation R1**, both\n"
"> PROVED-S3 root-reduction items strictly upstream of §7.6, and it is already written out\n"
"> twice: **Corollary SL-HC** (§7.6 F) and **Corollary FAN-HC** (§7.8 F) each open with it.\n"
"> Landed at **all three sites of the class** — Corollary MB1 (§7.6 G), Corollary GFAN2-HC\n"
"> (§7.13 B), Corollary GFANν-HC (§7.13 D). Q37 reported two; the third was found here by\n"
"> checking the class against the draft. **Theorem GFANν is NOT reached** — it neither\n"
"> cites Theorem RIG nor mentions `B_lo`, and its own hypotheses give `L ≥ ν+1 ≥ 2`.〕\n")

# ---------------------------------------------------------------- AD1 site 1: Corollary MB1
rep(
"> *Proof.* B-universality of all of `B_lo` gives `ν(B_lo) = ν(B_lo,B_hi) = 0`,\n"
"> hence `ν = m̄`, and `c = 0` (a B-universal vertex has no non-neighbour, so it\n"
"> cannot lie in `T₁ ∪ T₂`). Theorem MB then reads `m̄ ≤ L − 1`; and `ν ≥ 1` by R1. ∎\n",
"> *Proof.* First, **`B_lo ≠ ∅`**, i.e. `L ≥ 1`: at `L = 0` Theorem K makes `B` a clique,\n"
"> contradicting Observation R1. This step is what licenses the appeal to Theorem MB\n"
"> below, which is stated **for `L ≥ 1`**, and it is not supplied by the hypothesis “every\n"
"> low vertex is B-universal” — that is vacuously true when `B_lo = ∅`.\n"
"> B-universality of all of `B_lo` gives `ν(B_lo) = ν(B_lo,B_hi) = 0`,\n"
"> hence `ν = m̄`, and `c = 0` (a B-universal vertex has no non-neighbour, so it\n"
"> cannot lie in `T₁ ∪ T₂`). Theorem MB then reads `m̄ ≤ L − 1`; and `ν ≥ 1` by R1. ∎\n"
">\n" + AD1NOTE,
"AD1/MB1")

# ---------------------------------------------------------------- AD1 site 2: Corollary GFAN2-HC
rep(
"> *Proof.* Theorem RIG (§7.12) makes the instance `GFan(τ,L,ν)` with\n"
"> `1 ≤ ν ≤ L−1`; `ν = 1` is `Fan(τ,L)`, killed for `L ≥ 2` by **Theorem FAN**, and\n",
"> *Proof.* First, **`B_lo ≠ ∅`**, i.e. `L ≥ 1`, which is Theorem RIG's remaining\n"
"> hypothesis and is **not** supplied by “every low vertex is B-universal” (vacuous at\n"
"> `B_lo = ∅`): at `L = 0` Theorem K makes `B` a clique, contradicting Observation R1.\n"
"> 〔**Repair AD1**, at this site — see the note at Corollary MB1, §7.6 G.〕\n"
"> Theorem RIG (§7.12) then makes the instance `GFan(τ,L,ν)` with\n"
"> `1 ≤ ν ≤ L−1`; `ν = 1` is `Fan(τ,L)`, killed for `L ≥ 2` by **Theorem FAN**, and\n",
"AD1/GFAN2-HC")

# ---------------------------------------------------------------- AD1 site 3: Corollary GFANnu-HC
rep(
"> *Proof.* Theorem RIG gives `GFan(τ,L,ν)` with **`1 ≤ ν ≤ L−1`** — the lower bound\n"
"> is RIG (d), i.e. Observation R1 — so `L ≥ ν+1`; Theorem GFANν eliminates every\n",
"> *Proof.* First, **`B_lo ≠ ∅`**, i.e. `L ≥ 1`, which is Theorem RIG's remaining\n"
"> hypothesis and is **not** supplied by “every low vertex is B-universal” (vacuous at\n"
"> `B_lo = ∅`): at `L = 0` Theorem K makes `B` a clique, contradicting Observation R1.\n"
"> 〔**Repair AD1**, at this site — see the note at Corollary MB1, §7.6 G.〕\n"
"> Theorem RIG then gives `GFan(τ,L,ν)` with **`1 ≤ ν ≤ L−1`** — the lower bound\n"
"> is RIG (d), i.e. Observation R1 — so `L ≥ ν+1`; Theorem GFANν eliminates every\n",
"AD1/GFANnu-HC")

# ---------------------------------------------------------------- AD3 site 1: Lemma FAN-6 (SS7.8 E)
rep(
"> all of `B_hi` (DICH(b)) and all of `C` (hypothesis) lie in `block_j`, the number\n",
"> all **remaining** vertices of `B_hi` (DICH(b)) and all of `C` (hypothesis) lie in\n"
"> `block_j`, the number\n",
"AD3/FAN-6")

# ---------------------------------------------------------------- AD3 site 2: Lemma FAN-6' (SS7.13 A)
rep(
"> `B_hi` (DICH(b)) and all non-escaping `C`-vertices lie in `block_j`, so the number\n"
"> of `A′` entries in `block_j` is `a_j = D_j − (p−j) − (L+1) + e_j ≥ 1 + e_j ≥ 1`,\n",
"> **remaining** vertices of `B_hi` (DICH(b)) and all non-escaping `C`-vertices lie in\n"
"> `block_j`, so the number\n"
"> of `A′` entries in `block_j` is `a_j = D_j − (p−j) − (L+1) + e_j ≥ 1 + e_j ≥ 1`,\n",
"AD3/FAN-6p")

# the FAN-6' sentence begins "*Proof.* Write `M_j` ... . All of\n> `B_hi`" -- fix the dangling "All of"
rep("> reductio, the `A′` multiset at the start of step `p+1` **cannot** have a unique\n"
    "> maximum `w ≥ 1` whose second-largest entry is `≤ w − 2`.\n"
    ">\n"
    "> *Proof.* Write `M_j` for the `A′` value multiset at the start of step `j`. All of\n",
    "> reductio, the `A′` multiset at the start of step `p+1` **cannot** have a unique\n"
    "> maximum `w ≥ 1` whose second-largest entry is `≤ w − 2`.\n"
    ">\n"
    "> *Proof.* Write `M_j` for the `A′` value multiset at the start of step `j`. All\n",
    "AD3/FAN-6p-lead")

# and the FAN-6 lead-in "Since\n> all of `B_hi`" -> "Since\n> all **remaining**" already handled;
# confirm no bare "all of `B_hi`" survives anywhere.
assert out.count("all of `B_hi` (DICH(b))") == 0, "AD3: a bare \"all of `B_hi` (DICH(b))\" survived"
# (the remaining "all of `B_hi` high" at the GFan definition, SS7.8 G, is a different and
#  correct sentence -- it says every B_hi vertex is high, which is the definition of B_hi.)
assert out.count("all of `B_hi` high") == 1, "AD3: the GFan definition moved"

DRAFT.write_text(out)
post_md5 = hashlib.md5(out.encode()).hexdigest()
print(f"\npatches landed : {patches}")
print(f"draft md5 pre  : {pre_md5}")
print(f"draft md5 post : {post_md5}")
print(f"draft lines pre/post : {src.count(chr(10))} -> {out.count(chr(10))}")
