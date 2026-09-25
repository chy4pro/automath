# Q18 harvest — w61 V-PASS: the closing, diff-scoped pass deciding TWO GATES (§7.8 and,
via its Part 2 rider, Theorem T3), Qwen3.8-Max

Source: https://chat.qwen.ai/c/7a60af6a-7c60-4575-a067-d69bccc55f98
Dispatched 08-18 16:40 CDT (owner-intel round 11); harvested 08-18 ~17:5x CDT (owner-intel
round 13). Completion confirmed via action-icon row present under the final message, static
page-text length across two checks 8s apart, idle composer.

Brief: `prompts/w61_S3_VPASS.md` (~158 KB; delivered as an auto-converted file attachment,
`Pasted_Text_1787089138186.txt`, 154.1 KB, byte count consistent with the 157 810-byte source
— NOT truncated; driver added one instruction line asking Qwen to read the attachment in full
and follow it exactly). Two named parts: Part 1 = the V-text (V1-V6; V-M1 = Lemma T''s
graphicality repair, the MATHEMATICS joint the §7.8 gate turns on), Part 2 = the T3 K-text
rider (K1-K3; K-M1/K-M2 = MATHEMATICS).

## >>> GATE VERDICT (PROMINENT) <<<

**VERDICT: CLEAN** — no MATHEMATICS defect was found in either Part 1 or Part 2; every repair
in the diff (V1-V6 and K1-K3) is mathematically sound. Only findings: three minor,
non-driving BOOKKEEPING imprecisions, all repairable, none affecting any conclusion.

Quoted verbatim from the model: "VERDICT: CLEAN — no MATHEMATICS defect was found in either
Part 1 or Part 2; every repair in the diff (V1–V6 and K1–K3) is mathematically sound, and the
only findings are three minor, non-driving BOOKKEEPING imprecisions, all repairable, none
affecting any conclusion."

**Per the pipeline's own pre-committed gate logic (this is the 4th independent judge / 2nd
model family after Q14's clean mathematics joints), this result is what §7.8 and Theorem T3's
S3 gates were waiting on. This harvest does NOT itself close the gate — per the row's own
instruction the verdict goes to the PLANNER for gate confirmation — but the verdict itself is
CLEAN with zero mathematics defects on both parts.**

Delivery-mode caveat carried forward from dispatch: planner flagged that if the file-attachment
route degraded fidelity, watch for shallow/partial-reading signatures (missing named joints,
unanswered sections). **None found** — every named joint (V-M1, V-B1..V-B4, K-M1, K-M2, K-B1)
is individually addressed below with substantive derivations, all 3 repair-species probes are
run, a computation preamble with hand-calibrated Havel-Hakimi trajectories is present, and the
T12 counterfactual-availability section names two genuinely non-executing lemmas — this is not
a shallow pass.

## Computation preamble (mandatory probe 1)

Model re-implemented `residueAux`/labelled Havel-Hakimi by hand from the spec (could not
execute scripts); calibrated on `residue(K2)=1` and `residue(Cn)=ceil(n/3)` for n=3..8 by hand,
then reused no number printed in the brief for any subsequent trajectory.

## Part 1 — the V-text (§7.8 repair layer)

| joint | class | finding |
|---|---|---|
| V-M1 | MATHEMATICS | Repair correct, no defect |
| V-B1 | BOOKKEEPING | Three-tier assignment correct, C5 handled; one over-broad blanket phrase (§D1) |
| V-B2 | BOOKKEEPING | Firewall characterisation correct, no surviving M/H-run misuse |
| V-B3 | BOOKKEEPING | V5 independently re-derived, no lemma at wrong status; one out-of-brief dependency note (§D2) |
| V-B4 | BOOKKEEPING | V6 correct on both readings; minor claimed-impact prose imprecision (§D3) |

**V-M1 in detail (the joint the gate turns on)**: model hand-traced the witness
`[4,1,1,0,0,0] -> delete 4, decrement next 4 -> [0,0,0,0,0]` (1 step, residue 5=6-1);
Erdos-Gallai at k=1 gives `4<=2`, false, so this is non-graphical — confirming truncation is
exactly the counterexample mechanism the repair addresses. Independently re-derives that
graphicality implies Lemma 1(2) (head never exceeds positive-remaining-entries count) implies
no step truncates, which is exactly what the repaired statement's "only-if" direction needs —
"nothing more is required." Confirms the "if" direction is unaffected (needs no graphicality).
Swept the whole document for call sites of T' (the prime/graphicality-repaired lemma): zero
call sites found — "T' itself has zero call sites" — while the non-prime Lemma T is cited
twice (§7.3.0, §7.3.3), always inside the reductio on real (graphical) sequences, so
graphicality is supplied wherever T-family tools are actually used. Confirms the corrected T'
still supports the general-s closure claim (checked the other three tools — F3', S', DICH/Z+
— genuinely don't need graphicality either, since truncation only lowers values and their
bounds survive).

**Repair-species probes** (run on Part 1): Probe 1 (statement riders as separate obligations)
— all four checked riders justified. Probe 2 (scope-widening contagion) — F3->F3', S->S',
T->T', H->H' all re-checked at their new boundaries, no leaked contagion found (the T'
graphicality contagion is precisely V-M1's own subject). Probe 3 (box-vs-branch artifact) —
confirmed the large Fan numerical counts (63k+, 1.09M/1.7M, 508k) are finite-box corroboration
of Theorem FAN's closed-form disposal, not presented as a family theorem.

## Part 2 — the T3 K-text rider

| joint | class | finding |
|---|---|---|
| K-M1 | MATHEMATICS | Re-scoping (J1 widening k=1 -> k<=1) is complete, no defect |
| K-M2 | MATHEMATICS | Closed-form disposal is unconditional; branch is genuinely infinite; no defect |
| K-B1 | BOOKKEEPING | K3 heading-fix correct; no other Part-2 heading/bullet contradiction found |

**K-M1**: re-read every downstream sentence touched by the k=1->k<=1 widening at k=0; confirmed
the p=3 elimination paragraph, the Lemma-U trailing sentence (correctly re-scoped to k=1 only,
with k=0 pointed at its own direct HH close), and the k=0 bullet (self-contained). Independent
hand control-instance re-derivation: `[3,3,3,3,3,2,1] -> ... -> [0,0,0]`, s=4, residue=3=alpha-1,
confirms a misapplied Lemma U would wrongly cap `m<=7` against the true `m=9` — exactly K1's
own stated point.

**K-M2**: verified the closed-form diam<=3 argument is genuinely unconditional (no box, no
reductio, no multiplicity bound) and the branch is genuinely infinite (`K_{3,3}` plus
`t=n_x>=0` pendant A-vertices at x; t=0 gives diam 2, every t>=1 gives diam 3) — confirming the
old "exactly 10 configurations" count was a box artifact, correctly demoted to a spot check.

## Defects found (3, all BOOKKEEPING, none MATHEMATICS)

- **D1**: V2's blanket "every FAN lemma [stays in the hard core]" over-assigns — FAN-3 (and
  Observation FAN-5's multiset content) are hypothesis-free value-multiset statements, not
  "about a Fan configuration"; smallest witness multiset `[2,2,2,1,1]`. Repairable (carve out
  the exception); conclusion survives (FAN-3 still valid in the hard core regardless).
- **D2**: Observation FAN-5's second half cites Lemma TAIL (§7.13 D), not in the brief, so its
  general statement/proof could not be inspected — only the `lambda=[2]` instance was verified
  by the model's own direct induction. Citation/availability gap, not a falsehood; conclusion
  survives.
- **D3**: V6's claimed-impact prose conflates Lemma T's two sentences and mis-cites §7.6 as a
  call site when it doesn't use Lemma T at all; V6's own restatement is correct and no call
  site is actually mis-licensed. Documentation-only; conclusion survives.

## T12 counterfactual-availability section (mandatory, present and substantive)

Names **DICH(b)** as claimed-available (general-s) but never executing on any real Fan graph:
its threshold is `tau+2` while the true max Fan degree is `tau+1` (since Theorem FAN already
proves the reductio `s=tau` never holds for `Fan(tau,L>=2)`) — fires on 0 heads in every real
run; "the sharpest statement of why the §7.8 numerics can only be mechanism checks." Also names
**Lemma T'** as proved-but-cited-by-nothing (never executes at all, per V-M1's own sweep).

## Hand trajectories (own, calibrated, no brief numbers reused)

`[1,1]->[0]` (residue(K2)=1); `Cn` n=3..8 residues 1,2,2,2,3,3=ceil(n/3);
`[4,1,1,0,0,0]->[0,0,0,0,0]` (1 step, residue 5, non-graphical, V1 witness);
`[2,2,2,2,2]` (C5): s=3, residue 2=alpha, diam 2, f=4 (V2 witness, reductio true/frame false);
`[3,3,3,3,3,2,1]`: s=4, residue 3=alpha-1, Sum_{i<=3}D_i=8=m-1 (K1 control);
`[L]^{L+1},2`: L steps for L=2,3,4 (V5/FAN-5); `[L]^{L+1},1,1`: L+1 steps checked at L=2 (FAN-3).

## What the model could NOT check

Lemma TAIL's general statement/proof (§7.13 D absent from brief, only the `lambda=[2]`
instance verified); the large numerical corpora (116k+ graphs, adversarial tie-break runs —
calibration and every load-bearing small instance verified by hand, scripts not re-run);
the four-judge refereeing of theorem bodies (out of scope, theorem bodies taken as given);
whether §7.13/Lemma TAIL is established outside this brief.

## Out-of-scope observations (do not drive the verdict)

FAN appendix §7.7 carries the identical stale heading K3 repairs in the T3 context appendix —
in scope for Part 1 only if that section is ever diffed. Naming collision noted (Lemma SL1 vs
Conjecture SL1 — different, both resolved, no status error).

## Caveat

Everything UNVERIFIED by an independent human/other-model party — owner-w61 re-verifies line
by line, and **the verdict goes to the PLANNER for gate confirmation; no gate is closed by
this harvest itself**, per the row's own instruction.
