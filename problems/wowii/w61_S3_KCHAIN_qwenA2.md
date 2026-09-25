# Qwen S3 Round A2 — WOWII-61 K-CHAIN Adversarial Review (re-run)

- Conversation: https://chat.qwen.ai/c/41cf13ef-0360-4d9c-9798-392c91ae7e93
- Model: Qwen3.8-Max (confirmed switched before dispatch)
- Brief: `prompts/w61_S3_R2A2.md` (supersedes `w61_S3_R2A.md`; new appendix section G = draft
  §7.7, the Round-A repairs, themselves under review; sections A/B/C/D/F/G kept for
  TARGET=K-CHAIN)
- Dispatched: 08-18 11:4x CDT (owner-intel qwen_queue driver round 4), fresh conversation,
  NOT reused from Q1 or Q5 sessions — judge independence honored. Paste text extracted
  verbatim via sed line-ranges, pasted via clipboard (pbcopy+cmd+v), no retyping of math.
- Harvested: 08-18 12:2x CDT (owner-intel qwen_queue driver round 5). Chrome lease was FREE
  at pickup (not held by owner-w61); conversation had already finished generating
  (composer idle, "Thinking completed" shown) — harvested per driver discipline (only
  harvest finished, non-in-flight conversations).

## Overall verdict

**CLEAN** — within the connected `n≥2` scope, Repair R2's Lemma F3′ correctly removes the
hidden `s=τ` citation from Lemma Z⁺/DICH, and K-chain joints K-J1 through K-J6 are all valid
and tie-safe as repaired. No defects found among the named joints (contrast with the Q5
round-A pass, which found the F3/F3′ scope-mismatch this repair addresses).

## Per-joint table

| Joint | Verdict | One-line reason |
|---|---|---|
| K-J1 | OK | Lemma F3′ is true for general `s`; with it, Lemma Z⁺'s prefix/counting arguments are tie-safe and the "all block entries are later heads" count is correct. |
| K-J2 | OK | DICH(a)-(c) valid; (b) really gives `h_i=i−1`, `D_i=g−(i−1)` exactly; (c) holds at boundary `i=1` and at first-excess `j₀=i`. |
| K-J3 | OK | Under `residue=α`, Lemma S forces all B vertices to be heads; `\|K\|=s=τ=\|B\|` gives `K=B`; identity `hs=e_B` and `Σ(i−1)=C(τ,2)` both verified. |
| K-J4 | OK | Corollary K1's "some maximum independent set" quantifier is safe: `τ=n−α` is independent of the chosen maximum independent set, and Observation R1 contradicts a clique complement in any connected diam-4 graph. |
| K-J5 | OK | K-chain needs only Lemma 1, Fact 2, Lemma S, F3′, Z⁺, DICH, Observation R1; after R2 no general-`s` lemma cites an `s=τ` lemma; unused τ-uniform toolkit not invoked outside its hypotheses. |
| K-J6 | OK | Patched Corollary N2 correct under its explicit reductio hypothesis; contrapositive valid using Fact 2; `K_{2,3}` arithmetic refutes only the old unqualified form. |

## Gaps or refutations

None among the named K-chain joints. One out-of-scope boundary note (not scored as a joint
failure): if Corollary N2 were read literally on the singleton connected graph `K₁`, then
`τ=0`, `m=Δ=0`, and the displayed bound `Δ+τ(τ+1)/2−1=−1` would be false. The paper's global
setting is connected `n≥2` (hard-core/diam-4 setting has `τ≥1`), so `τ=0` is outside the
intended scope — flagged as a future-proofing note (add `τ≥1` if N2 is ever exported
verbatim outside this scope), not a current defect.

## Control-case section (counterfactual availability check, full)

Four controls, each with hand-computed HH trajectory and per-lemma counterfactual
availability table:

**Control (a)** — sequence `[3,3,3,3,3,2,1]` realized concretely as a 7-vertex graph
(`c1..c5,h,l`; edges `c1c2,c2c3,c3c4,c4c5,c5c1,hc2,hc3,hc4,lc1`); `α=3`, `τ=4`; this is a
reductio control (`s=τ=4`). Confirmed: false bound `D_i≤d_i−(i−1)` fails as intended (K-chain
does not use it); F3′, Z⁺, DICH(c) all hold on this control; Lemma S/T checks pass; BO/DEC/
CNT checked numerically (`hs=2`, `Σβ_j=2`, DEC and CNT both give true, deliberately weak
bounds); Theorem K/Corollary K1 correctly NOT available (displayed max independent set's
complement `B={c1,c2,c3,c4}` all have degree `3<τ+1=5`).

**Control (b)** — the 8-vertex diam-4 graph refuting `f≥α+⌈diam/3⌉` (edges
`01,12,13,14,25,56,71,75`); `τ=2`, `α=6`, `s=3`, `residue=5=α−1` (non-reductio). Reductio-only
lemmas correctly unavailable; general lemmas F3′/Z⁺/DICH available and hold. Corollary K1's
hypothesis is true for `A=V∖{1,5}` and its conclusion `residue≤α−1` holds with equality
(5≤5) — if one counterfactually assumed `residue=α`, Theorem K would force `{1,5}` to be a
clique, contradicting Observation R1: "exactly the intended proof mechanism."

**Control (c)** — the 8-vertex tree refuting `α+1≥residue+⌈diam/3⌉` (edges
`01,12,23,24,25,26,73`); `τ=3`, `α=5`, `s=3=τ` (reductio control). Lemma S, F3′, Z⁺, DICH all
checked and hold; Theorem K hypothesis (i) correctly fails (only vertex 2 has degree ≥4, not
three vertices) so Theorem K is inapplicable — no false clique conclusion forced.

**Control (d)** — `K_{2,3}` for the unqualified Corollary N2. `n=5,α=3,τ=2,e_B=0,Δ=3,m=6`;
HH gives `s=3`, `residue=2=α−1` (non-reductio). Old unqualified N2 bound `Δ+τ(τ+1)/2−1=5<m=6`
— false as expected. Patched N2 correctly does not apply (`s=3≠τ=2`). Contrapositive form
holds: `m>5 ⟹ residue≤α−1`, true here (`residue=2=α−1`).

Summary: general-`s` lemmas (F3′, Z⁺, DICH) available and hold on ALL four controls;
reductio-only lemmas (S, T, old F3, BO, Z, DEC, CNT, Theorem K) available exactly when
`residue=α` (controls a, c) and correctly absent on (b, d); no false consequence found on
any control.

## Trajectories computed

Seven trajectories with full intermediate lists: controls (a)-(d) above, plus three
additional positive/boundary sanity checks for Theorem K — `τ=2` positive case (`B=
{u,v}` edge, degrees `[3,3,2,2]`, `hs=1=e_B`), `τ=3` positive case (`B` a triangle, degrees
`[4,4,4,3,3]`, `hs=3=e_B`), and the `τ=1` boundary case (star `K_{1,3}`, `e_B=0` correctly
recovered). All in the conversation transcript (URL above).

## What Qwen flagged it could not check

- Numerical verification files (`w61_*.py`, `.out`, exhaustive/random corpora) — not
  executed or inspected; verdict based on proof inspection + hand-computed trajectories.
- Fact 2 (`residue(G)≤α(G)`) — cited as known, not independently proved; K-J4/K-J6 rely on
  it for the final integer step.
- Lean/Mathlib source definitions — read only the textual description.
- Exhaustive enumeration of all adversarial tie-breaks on all control graphs (checked the
  tie-safety mechanism and representative tie-breaks by hand, not exhaustively).
- T3-specific Repair R1 (k=3 endgame) — explicitly out of scope for TARGET=K-CHAIN, deferred
  to the T3-REPAIRED pass (see `w61_S3_T3R_qwenA2.md`).

## owner-w61 verification duties

CLEAN verdict is UNVERIFIED by owner-w61 as of harvest time. Given this is the first CLEAN
K-chain verdict after two prior rounds each found real defects (Q1: F3/s=τ scope issue;
Q5: same defect surviving one Repair R1 iteration), owner-w61 should independently re-check
at minimum K-J1/K-J2 (the F3→F3′ substitution, the joint the last two rounds' defects both
touched) before closing the K-chain gate. Same-source firewall for this round = parallel
opus judge (per the Q5/Q6 dispatch notes), not this Qwen pass.
