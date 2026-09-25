# Q19 harvest — w133 G-DIFF PASS: the closing, diff-scoped pass deciding the Q6.1 /
Theorem G35 PROMOTION gate, Qwen3.8-Max

Source: https://chat.qwen.ai/c/b6a0c538-206a-4bdb-a3d0-48da55a5249c
Dispatched 08-18 17:07 CDT (owner-intel round 12); harvested 08-18 ~17:5x CDT (owner-intel
round 13). Completion confirmed via action-icon row present under the final message, static
page-text length across two checks 8s apart, idle composer; delivered as inline pasted text
(not a file attachment, unlike Q18).

Brief: `prompts/w133_S3_GDIFF.md` (~86 KB). Named joints: G-M1 = MATHEMATICS (the G32'/G32
split — G32 was FALSE as originally stated, omitting `C4`-free; verify the restated proof
step-by-step AND the exhaustive usage-site sweep that every application carries `C4`-free);
G-M2 = MATHEMATICS (§14.2's round-9 completion of G15(a), the upstream hole G32 inherited);
G-B1..G-B4 = bookkeeping. A mandatory statement-hypothesis audit probe (11 statements x
{hypotheses STATEMENT carries, hypotheses PROOF uses, verdict EQUAL/WIDER=>false/
NARROWER=>free generality}) was attached and delivered.

## >>> GATE VERDICT (PROMINENT) <<<

**VERDICT: PARTIAL — the repaired G32'/G32 split and the mathematical core of §20 are sound,
but some bookkeeping/rider claims (notably the presentation of G35.2 as an independent kill
and some "unconditional"/"vacuous" wording) are overstated.**

**MATHEMATICS DEFECT FOUND: NO** (quoted verbatim, stated on its own line as the brief
required)

**Per the queue row's own pre-stated gate arithmetic — "MATHEMATICS DEFECT FOUND: NO ⟹ Q6.1/
G35 promote to PROVED; YES ⟹ the promotion is held and the named joint reopens" — this
Qwen pass satisfies the promotion condition as written.** This harvest does not itself close
the gate — the verdict goes to the PLANNER for gate confirmation, per the row's own
instruction — but the reported answer to the exact question the gate was watching is NO
mathematics defect, on both G-M1 and G-M2.

## G-M1 — the G32'/G32 split and restated G32 (the joint the gate turns on)

**(a) Is G32' true, hypothesis-free except "no induced P6"?** Yes — independently re-derived
the deleted-vertex argument (delete `v_{i+1}` from an induced C6 `Z` when `w` has exactly Z-
neighbours `v_i,v_{i+1}`; remaining 5 Z-vertices form an induced P5 whose only Z-neighbour of
`w` is `v_i`, giving an induced P6). Confirmed hypotheses consumed are exactly "induced C6" +
"no induced P6" — no C4-freeness, connectedness, or radius/diameter/l hypothesis used. Gave an
explicit control graph (C6 + w adjacent to a consecutive pair {0,1}) showing this IS a real
induced P6, i.e. G32' cannot be strengthened to drop the no-P6 hypothesis.

**(b) Is the repaired G32 (0 or 2 Z-neighbours, and if 2 antipodal) true, steps (i)-(iii)
separately, correct hypothesis attribution?** Yes, all three steps independently checked with
explicit control graphs for each: Step (i) `|N(w)cap Z|!=1` consumes ONLY P6-freeness (control:
C6+leaf gives induced P6); Step (ii) `|N(w)cap Z|<=2` consumes ONLY C4-freeness via an
independently-proved combinatorial lemma "every 3-subset of a hexagon contains a pair at
cyclic distance 2" (full proof given: positive triples summing to 6 are (1,1,4),(1,2,3),(2,2,2),
each contains a 2 or 4; control: C6+w adjacent to a distance-2 pair {0,2} is P6-free but not
C4-free — this is explicitly identified as "the machine counterexample to the old unconditional
G32"); Step (iii) (exactly-2 case forces distance 3) follows since distance 1 is killed by
G32'/P6-freeness and distance 2 by the C4 argument. Control for antipodal survival also given
(C6 + w adjacent to {0,3} is both C4-free and P6-free).

**(d) Usage sweep**: swept the diff + supplied context for every application site of G32/G32.1
(table with 10+ rows: §20.1 G32 proof itself, Cor G32.1, §20.2 G33, §20.3 G34(a)/(b)/(c),
§20.4 G35/G35.1/G35.2, §20.5 numerical section, §20.7 item 3, §19/§17). **Found no live
application site lacking C4-freeness** — every site is inside RES(b) (which includes C4-free)
or explicitly states the C4-free/P6-free hypothesis.

**(e)**: confirmed no downstream consumer needs the old, false, unconditional G32 — the only
genuinely unconditional lemma is G32' itself, and G32' doesn't assert the antipodal
conclusion, only forbidding exactly-two-consecutive.

## G-M2 — §14.2 round-9 completion of Lemma G15(a)

**(a)** Independently re-derived the added `|N(w)cap Z|>=3` case: same cyclic-distance
combinatorial argument (positive triples summing to 6), correct and exhaustive.
**(b)** Confirmed hypothesis attribution: (a1) [exactly 1] uses P6-freeness, produces the
"path>=6" disjunct; (a2) [>=3] uses only C4-freeness, produces no disjunct — "this attribution
matters, and it is right."
**(c)** Confirmed completed G15(a) supports G32 step (i) (which only needs the exactly-1
exclusion under P6-freeness; G32 supplies the >=3 case independently in its own step (ii)).
**(d)** Spot-checked 3 of the patch note's claimed 11 usage sites (§14.3, §16.5b/G21,
§17.4/Cor G22.1) — all correct, all carry C4-free via RES(b) or (C6). One caveat surfaced
(logged as a defect, not mathematical damage): an indirect use through G15(c) (§19.5's proof
of G31) is not explicitly among the listed 11, though it is itself C4-free and moot after §20.

## G-B1..G-B4 (bookkeeping joints) — all essentially clean, with 5 named defects total

- **G-B1** (§20.5 dependency note): swept §20 for a 4th independent load-bearing use of §18
  beyond the claimed 3 (Cor G26.1, Theorem G26 in G33, G34(b)'s a(w)=2) — found none; G35.2 and
  Cor G35.1 are both derivative, not independent 4th uses. "If §18 falls, §20 falls entirely"
  confirmed correct.
- **G-B2** (§15.5 withdrawal of n>=14, replacement by n>=6): confirmed the withdrawal was
  justified (quoted log lines only establish `floor(l)=3`, not `l>3` strictly, so never
  actually supported the old n>=14 bound) and the n>=6 replacement is valid and is the actual
  bound G35 uses (via the induced-C6 giving n>=|Z|=6, then integer mass forces contradiction
  with the mass cap of 6). Swept the 5-row downstream table — found one additional historical
  n>=14 site not listed (§19.5 Cor G31.3) but it's moot (§19 superseded).
- **G-B3** (Remark G35.2's n<=9 "second independent kill"): re-derived the n<=9 bound itself
  as correct and genuinely independent of the mass budget (**), BUT identified that **n<=9
  alone does not contradict anything** given only the certified n>=6 lower bound — the "kill"
  as worded needs an unavailable n>=10 input, or an unstated explicit finite-frame l<=3 check.
  Model constructed an explicit n=9 witness frame (edge list given) with l=24/9=8/3<3 to show
  n<=9 is not itself a contradiction. **This is Defect 1, the most substantive finding of the
  round** — but explicitly labeled BOOKKEEPING since Theorem G35 itself remains proved via the
  mass budget regardless.
- **G-B4** (remaining §20 repairs, 5 sub-items): all independently re-verified correct
  (G34(b)'s `|N(w)cap W_P|<=1` one-liner — proved via a C4 argument; G32.1's wording change from
  "triangle-free" to `t(v_i)=0, N(v_i)` independent — confirmed necessary and sufficient for the
  `a=d-t` identity, with an explicit counterexample `N(v)=P_3` showing "triangle-free" alone is
  insufficient; §20.7 item 4's back-reference correction; §20.2's supersession-of-§19 claim
  mostly correct with one imprecision on G29/G30 vacuity wording).

## 5 Defects total (all BOOKKEEPING, zero MATHEMATICS)

1. G35.2's "second independent kill" rhetoric is under-supported as written (see G-B3 above) —
   repairable by rewording to a conditional or adding the finite-frame check; conclusion
   (Theorem G35) survives via the mass budget regardless.
2. "Unconditional" wording for G32/G32.1 is too broad (only G32' is C4-free-free; G32/G32.1
   both carry C4-free+P6-free) — repairable by saying "unconditional relative to RES(b)".
3. §20.2's G29/G30 vacuity wording imprecisely says all their subjects don't exist, when P/Q/W
   can still exist — repairable rewording.
4. §14.2 patch note's 11-site sweep may undercount one indirect G15(c) use (moot, C4-free).
5. §15.5's downstream sweep table omits one historical n>=14 use in §19.5 Cor G31.3 (moot,
   §19 superseded).

All five: repairable, conclusion survives, labeled BOOKKEEPING.

## T12 counterfactual availability (mandatory, present)

Named non-executing lemma 1: Remark G35.2's "n>=10 kill" — proves n<=9 but no n>=10 input is
ever available, so it never actually executes; the mass budget performs the real kill.
Named non-executing lemma 2: §19's G27 bound `d(h0)<=5` — after G33, `h0` doesn't exist, so
the bound is available but never executed in the §20 proof.

## Statement-hypothesis audit table (mandatory probe, 15 statements covered)

G32', G32, G32.1, G33, G34(a/b/c), G35, G35.1, G35.2, G15(a/b/c) all individually classified.
Almost all EQUAL (statement hypotheses = proof-used hypotheses). Two flagged as
**STATEMENT NARROWER THAN PROOF** (strengthening opportunities, not defects): G34(a) (once
G33's frame is known, the local proof doesn't need rad/l/R3b directly) and G15(b) (the
distance-2 exclusion doesn't need the path-disjunct, could be stated for any C4-free graph
with an induced C6). One flagged **STATEMENT WIDER THAN PROOF** on its kill-rider specifically:
G35.2 (the n<=9 claim itself is EQUAL, but the "kills the branch" rider is WIDER than what's
proved — this is the same Defect 1 surfacing again in the audit table).

## What the model could NOT check

Actual script execution (w133_r8_q61.py, w133_gplus_n13.out, judge scripts) — verified
mathematics from text and hand-checked small configurations only. Some downstream references
not in the supplied excerpt (§17.8 Cor G23.2, §18.5 item 3) assessed conditionally. Full
exhaustive line-by-line sweep of Chinese-language prose outside the diff not possible (3 rows
spot-checked). Did not verify claimed judge-independence/timing metadata. Per instruction, did
not let G25(a) affect the verdict (no substantive G25(a) finding to route).

## Caveat

Everything UNVERIFIED by an independent human/other-model party — owner-w133 re-verifies line
by line, and **the verdict goes to the PLANNER for gate confirmation; the harvest closes no
gate by itself**, per the row's own instruction. The most load-bearing single finding for
owner-w133 to check first is Defect 1 / G35.2's audit-table WIDER verdict (the n<=9 kill-rider
overstatement) — since it is the one place the model's own severity language ("the most
problematic rider") suggests real editorial cleanup is needed even though it does not affect
Theorem G35's status.
