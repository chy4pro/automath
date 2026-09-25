# w61 S3 — §7.8 FAN-chain, cross-family round B (Qwen3.8-Max judge)

Harvested: 2026-08-18 16:06 CDT (owner-intel round-10, qwen_queue.md Q14).
Conversation: https://chat.qwen.ai/c/b5a9411f-2783-48b1-99c1-429d55272671
Brief pasted verbatim: `prompts/w61_S3_FAN_B.md` (reviewed text frozen 15:20 CDT, draft
§7.8+§7.10+§7.14). Same-source note (planner-accepted per the brief header): Qwen (Q7 tab B)
originally located the Fan target, but no Qwen step survives in the current proof — this
round judges Claude's proof, not Qwen's own prior output.

---

**VERDICT: PARTIAL** — "the FAN-chain mathematics survives every mathematics joint I checked,
but there are residual bookkeeping defects (an incomplete status repair for FAN-2 and at
least one overclaimed 'PROVED' observation); the conclusion of Theorem FAN (first sentence)
and Corollary FAN-HC survives."

TEXT VERSION REVIEWED (Qwen's own line): "§7.8 FAN-chain paste brief — WOWII-61 S3, round B
(bookkeeping-first, frozen G-text), as supplied in this prompt."

All defects found are classified **BOOKKEEPING**, none **MATHEMATICS**. The verdict line is
explicitly driven by bookkeeping, not mathematics — every one of the 12 named joints (B-J1..6,
M-J1..6) that touches the mathematics itself came back CLEAN.

## (a) Bookkeeping table B-J1..B-J6

| joint | verdict | summary |
|---|---|---|
| B-J1 Attribution sweep | CLEAN (non-load-bearing caveat) | Repair G1 correct; no other operative sentence misattributes the exact `residue=α−1`/`s=τ+1` value to Theorem FAN after F1. |
| B-J2 Orphan sweep | CLEAN | No proof in the operative chain depends on the withdrawn exact value (checked §7.8 E table, §7.8 G GFan lead, Lemma FAN-3, Corollary FAN-HC explicitly). |
| B-J3 Status-line audit | **PARTIAL** | G3 correctly diagnoses FAN-2 as tie-incomplete and strikes it from §7.8 E's PROVED list, but **§7.8 A's status line still lists FAN-2 as PROVED** (Defect D1). Also §7.8 E still lists Observation FAN-5 as PROVED though only finite-simulation-verified (Defect D2). |
| B-J4 Scope labels | CLEAN inside H/K/L | No remaining H/K/L site uses "hard core" for the frame or an operative stale `τ≥3`. (Non-target note: §7.6 B's heading reads frame-like — flagged FYI, out of scope.) |
| B-J5 Citation-scope audit | CLEAN | Lemma 1, Fact 2, S/S′, DICH(a)(b)(c), F3′, T/T′ all used only in forms available at their call sites. |
| B-J6 Repairs + new lemmas | **PARTIAL** | G1/G2/G4/G5 all CLEAN. G3 mathematically correct but bookkeeping-incomplete (see D1). Lemma S′, T′, H′-subsumed-by-DICH, and the §7.2 B closure claim all CLEAN. |

## (b) Mathematics table M-J1..M-J6 — ALL CLEAN

| joint | verdict |
|---|---|
| M-J1 FAN-1 tie-break invariance | CLEAN — equal-value swaps don't change the value-multiset trajectory; induction correctly shows first p heads can be taken as B_hi; boundary j=1,j=p checked. |
| M-J2 FAN-4 decrement bookkeeping | CLEAN — recipient classes exhaustive/disjoint; `Σ_{j≤p}D_j = Σ_{B_hi}deg − C(p,2)`, `Σ_{B_hi}deg_B = pτ−p−2` re-derived; `dec_{A′}=R−2` follows. |
| M-J3 FAN-6 backward induction | CLEAN — propagates correctly for single 2; correctly FAILS for 1+1 (non-unique maximum, matches repair F4's diagnosis). |
| M-J4 FAN-7 non-graphicality, E≤2 | CLEAN — residue-sum count gives `2−E≥0`; both E=2 terminal shapes shown non-graphical. |
| M-J5 FAN-8 count + survival of x | CLEAN — `|block_t∩A′|≥2` and `v_{p+1}(x)≥v_t(x)−(p−t+1)` (survival established: x not deleted in steps t..p since all heads are B_hi) both re-derived; full contradiction chain to `L≤1` reproduced. |
| M-J6 Corollary FAN-HC's use of Prop L2 | CLEAN — L2 supplies every Fan(τ,L) clause including "every A-vertex other than a0 attaches only inside B_hi" (derived from `deg_A(b_i)=1` + unique common A-neighbour a0). |

## (c) Refutation attempt

Small analytical box (τ≤6, L∈{2,3}, p=τ−L, |A′|≤4, A′ degrees≤p, one attempted escape E=1,
arbitrary tie-breaks) — every E=1 assignment collapses to the FAN-8 inequality L≤1, no
candidate survives. Adversarial tie-break attack at j=p also fails to produce a counterexample
(value-multiset invariance under label swap restores FAN-1). No mathematical refutation found.
Qwen explicitly did not attempt to out-enumerate the prior large numerical corpora (self-aware
of marginal value per the brief's own guidance).

## (d) Defects — all BOOKKEEPING, none MATHEMATICS

**D1 — stale FAN-2 "PROVED" line in §7.8 A.** Repairable: yes (add G3-style strike to the
§7.8 A status line). Conclusion survives: yes (FAN-2 is unused; FAN-8 proves no-escape
unconditionally).

**D2 — Observation FAN-5 listed PROVED without a full proof** (second half only verified by
simulation for L=2..8, not a universal proof as written). Qwen supplies a one-line inductive
proof itself (`[L]^{L+1},2 → [L−1]^L,2` step, clearing time = L). Repairable: yes. Conclusion
survives: yes (FAN-5 not load-bearing for Theorem FAN or Corollary FAN-HC).

**D3 — minor dependency overstatement** about Lemma T's second sentence claiming it "needs
Fact 2" — Qwen argues the arithmetic goes through without Fact 2 under the literal antecedent
reading. Repairable: yes (rewording). Conclusion survives: yes (dependency-note level only).

## (e) Control-case / counterfactual-availability (T12, mandatory section — present)

Two control instances used:
- **C1 — Fan(5,2) off-reductio**, degree sequence `[6,6,6,5,5,5,3,2]` (τ=5,L=2,p=3,α=3,n=8,
  s=6, residue=2=α−1). Full lemma-by-lemma availability table given. **Names two lemmas the
  text claims are available but which do not execute in the decisive way**: DICH(b) (needs
  original degree ≥ s+1=7, max degree here is 6) and Lemma S′'s head-forcing clause (threshold
  s+1=7, no vertex reaches it).
- **C2 — star K_{1,3}, reductio true**, degree sequence `[3,1,1,1]` (α=3,τ=1,n=4,s=1,
  residue=3=α) — shows the toolkit is non-vacuous when hypotheses genuinely hold.

## (f) Havel–Hakimi trajectories (own implementation, calibrated first)

Calibrated on K₂ (`[1,1]→[0]`, s=1, residue=1) and C₅ (`residue=2=⌈5/3⌉`) before trusting the
implementation, per the brief's mandatory calibration clause. Two Fan(τ,L≥2) trajectories
computed independently (not reusing any brief-printed number):
- Fan(5,2), A′ degrees 3,2: `[6,6,6,5,5,5,3,2]` → ... → `[0,0]`, s=6=τ+1, residue=2=α−1.
- Fan(5,3), A′ degrees 2,2: `[6,6,5,5,5,5,2,2]` → ... → `[0,0]`, s=6=τ+1, residue=2=α−1.

## (g) What Qwen could NOT check

Did not re-run the cited million-scale enumerations / adversarial tie-break corpora (own
computational contribution limited to the 4 hand-checked trajectories + small analytical
boxes); did not check against actual Lean source (worked from supplied prose only); could not
verify (F-b)'s status as theorem vs. hypothesis (proof not in the supplied text, consumed as
prior context); did not re-review Theorem T3 / τ≤3 closure (accepted as prior result); did not
inspect `w61_*.py` script outputs (numerical claims accepted as reported except where
recomputed by hand).

---

**Everything UNVERIFIED — owner-w61 re-verifies line by line before adoption.** This is the
cross-family (non-opus) round B required to meet the two-model-family S3 bar for the §7.8
FAN-chain judge round; a parallel opus round B (`problems/wowii/w61_S3_FAN_opusB.md`) already
exists per RESOURCES.md's file-mtime record (15:57 CDT) — owner-w61 should cross-check whether
Qwen's D1/D2/D3 bookkeeping defects were also caught by the opus round, and whether opus found
anything Qwen missed (mathematics joints all CLEAN here, so opus's mathematics verdict is the
higher-value cross-check).
