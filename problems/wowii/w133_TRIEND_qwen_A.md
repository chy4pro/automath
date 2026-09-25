# Qwen TRIANGULAR-ENDPOINT attack — Entry A (bounded-degree sub-branch)

- Conversation: https://chat.qwen.ai/c/b05d82d3-dde3-4eda-aac2-9ebce60d591a
- Model: Qwen3.8-Max (confirmed via find-tool ref-click after model-selector auto-close
  broke coordinate clicks — see `notes/web_model_ops.md`).
- Brief: `prompts/w133_r6_TRIEND_qwen.md` (self-contained: S2 template set — T1 disguise,
  no-internet, T8 persistence rider, T11 known-facts preface, T12 + both amendments incl.
  the "validate the witness against EVERY defining constraint" clause, T13
  conclusion-first). Contains owner-w133's own F1–F9 facts (all owner-proved,
  machine-checked, `problems/wowii/w133_r6_adjudicate.out`), no Qwen material.
- Dispatched: 08-18 13:5x-14:0x CDT (owner-intel qwen_queue driver round 7).
- Harvested: 08-18 14:4x CDT (owner-intel qwen_queue driver round 8). Chrome lease held by
  owner-intel throughout; conversation had already finished generating (composer idle,
  page text length static across two checks ~3 min apart) — harvested per driver
  discipline.

## Overall verdict

**SOLVED-EMPTY** (`VERDICT: SOLVED-EMPTY`, self-reported): *"I prove that in branch (TRI)
with every hub of degree at most 5, no graph exists; Problem A is empty."*

This is the higher-value of the two literal sub-branch entries (A = bounded-degree, B =
high-degree) — see `w133_TRIEND_qwen_B.md` for the companion, also SOLVED-EMPTY.

## Proof sketch (as given)

- The degree bound forces `|B_p|,|B_q| ≤ 3`.
- F8(d) forces `|H∩B_p|·|H∩B_q| ≥ 6`, so **at least one of `p,q` is a hub**.
- **Case I (both p,q hubs)**: every D-vertex has one parent on each side and injects into
  `B_p × B_q`, so `|D| ≤ 9`; the total hub excess is then at most `|D|-1`, contradicting F1
  (`Σ(a(h)-2) > n`).
- **Case II (exactly one of p,q is a hub)**: sizes forced to `(3,2)` (or symmetric) and
  exactly six D-vertices have both parents; hub excess is at most `|D|+3` while
  `n = |D|+8`, again contradicting F1.
- Explicitly notes the proof uses C4-freeness, (C5), `l>3` (via F1), and the hub-degree ≤ 5
  assumption; does **not** use (C6)/F6, so it establishes a slightly stronger statement than
  the literal ask.

## Self-audit (hypothesis usage log + honesty flags)

- Flags one place where it goes **beyond the literally stated facts**: the "any edge
  `B_p`–`B_q` gives a 4-cycle" step is a strengthening of F7(c) ("at most one" B_p–B_q edge)
  specific to the triangular-endpoint setting `p∼q` — states it is confident this is correct
  under the strong C4-free definition but flags it explicitly as a strengthening rather than
  silently treating it as already-given.
- Full "every place a hypothesis was used" table: TRI (existence of distance-3 endpoint u
  with `a(u)=1`), F3/F4, C4-freeness (four separate uses), (C5) (three separate uses),
  `l>3` (only through F1), the Problem-A hub-degree≤5 premise, F8(d); explicitly notes
  C6/F6 are NOT used.
- **What was tried and failed** (three angles): direct Bonferroni counting with F2 alone
  (only gives `|H|≥6`, no contradiction); F6/P5-endpoint bounds (vacuous at degree≤5, only
  bites at degree≥6 as in the Entry-B branch); constructing explicit C4-free parent-pair
  graphs (satisfies local constraints but fails `l>3`, exactly the mass deficit the final
  proof formalizes); global algebraic bound `Σa(v)=2e-3T` (too weak without the forced
  D-parent structure).

## Owner-w133 verification duties on adoption

Line-by-line re-verification of both cases' counting arguments (particularly the F8(d)
product-bound application and the flagged F7(c) strengthening), independent check that no
step silently uses (C6); adversarial review by a NON-Qwen judge before adoption. If both
Entry A and Entry B (companion file) hold up, the triangular-endpoint branch is fully
closed. Full transcript stays live at the conversation URL above.
