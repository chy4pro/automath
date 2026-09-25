# Qwen S3 Round A2 — WOWII-61 Theorem T3-REPAIRED Adversarial Review (re-run)

- Conversation: https://chat.qwen.ai/c/36f3a44f-66e3-4683-b75d-9608532afb9b
- Model: Qwen3.8-Max (confirmed switched before dispatch)
- Brief: `prompts/w61_S3_R2A2.md` (supersedes `w61_S3_R2A.md`; new appendix section G = draft
  §7.7, the Round-A repairs, themselves under review; sections A/B/C/E/G kept for
  TARGET=T3-REPAIRED)
- Dispatched: 08-18 11:4x CDT (owner-intel qwen_queue driver round 4), fresh conversation,
  NOT reused from Q1 or Q5 sessions — judge independence honored. Paste text extracted
  verbatim via sed line-ranges, pasted via clipboard (pbcopy+cmd+v), no retyping of math.
- Harvested: 08-18 12:2x CDT (owner-intel qwen_queue driver round 5). Chrome lease was FREE
  at pickup (not held by owner-w61); conversation had already finished generating
  (composer idle, "Thinking completed" shown) — harvested per driver discipline (only
  harvest finished, non-in-flight conversations).

## Overall verdict

**PARTIAL** — the repaired T3 proof is logically complete except for one non-load-bearing
false terminal-shape count in the k=2, e_B=2 subcase (T-J4); the sentence claiming "exactly
one entry equal to D_3=1" is literally false (the correct list has two or four ones
depending on reading), but the argument does NOT depend on this sentence — the same
paragraph already contains a correct, sufficient sum contradiction
(`Σ_{i≤3}D_i = m−1 < m` under the reductio `s=3`, contradicting Lemma 1(2)). All other
named joints (T-J1, T-J2 incl. twice-repaired Repair R1, T-J3, T-J5) are OK, independently
re-derived. Theorem T3's conclusion is unaffected.

## Per-joint table

| Joint | Verdict | One-line summary |
|---|---|---|
| T-J1 | OK | (F-b) disjoint-pair exhaustiveness for a 3-set B is genuinely exhaustive; `k=0⟹e_B=0`, `k=1⟹e_B≤1` follow from C2/C3, independently re-derived case by case. |
| T-J2 | OK | Twice-repaired k=3 endgame is tie-break robust; Repair R1's "no entry = Z" replacement (for the old false "no entry ≥4") is valid — verified against `[5,5,5,3,3,3,2]` and `K_{3,5}` probes where a second value-4 entry survives step 2, refuting the old bound but not R1's. "Every A-entry ≤3<4≤Z" and "`w` is the only B-entry of `L¹∖{H₂}`" both check out. |
| T-J3 | OK | Lemma U's proof and both hypotheses verified; both call sites (k=1,e_B=1 and k=1,e_B=0) satisfy the second hypothesis (`Δ ≥ #{entries=3}`); revision note correctly declares the old blanket "available whenever k≤1" false — confirmed against control `[3,3,3,3,3,2,1]` where the second hypothesis fails (4 threes, Δ=3) and a false application would give `m≤7` vs actual `m=9`. |
| T-J4 | **GAP (non-load-bearing)** | The k=2/e_B=2 subcase's explicit trajectory and `ΣD_i=m−1` sum contradiction are correct, but the terminal-shape count sentence ("恰有 D₃=1 个 1") is literally false under both readings. Repair: delete the terminal-count clause (sum contradiction alone suffices) or restate as "2 ones total (head + 1 after), actual 4". |
| T-J5 | OK | p=3 repair (k=1,e_B=0) is valid — forces all occurring types to be non-disjoint, contradicting diam=4; Lemma 3 dependence for `f≥α+1` correctly identified (elementary: `A∪{b}` is a star-forest); `k∈{0,1,2,3}` case split confirmed exhaustive. |

## T-J4 gap detail (quoted)

Quoted line (§7.3, k=2/e_B=2): "故 D_3 = 1，而终止形状要求恰有 D_3=1 个 1，实有 4 个，矛盾
（等价地 Σ_{i≤3}D_i = X+(Y−1)+1 = m−1 < m）。"

Why it fails: Lemma T says if `s=τ=3`, after step 2 the list must be `[D_3, 1^{D_3}, 0^…]`.
If `D_3=1`, this is `[1,1,0^…]` — **two** entries equal to 1 (the head and one after), not
"exactly one 1" as claimed. If instead counting only post-head ones, the branch's actual
`L²=[1,1,1,1,0^…]` has three ones after the head, not four. Either reading miscounts.

Smallest configuration exposing it: concrete instance `a₀=b₀=c₀=1` gives degree sequence
`[4,4,3,3,2,1,1]` (m=9); trajectory `L0→[3,2,2,1,1,1]→[1,1,1,1,0]`; first three heads
`4,3,1` sum to `8=m−1`. The terminal-shape count sentence is wrong on this instance too, but
the sum contradiction is exactly right and is what actually closes the subcase.

Repairable: yes, trivially (drop the terminal-count clause; the sum argument in the same
sentence already suffices). This is a **textual defect, not a logical gap** in the subcase
conclusion.

## Control-case section (counterfactual availability check, full)

**Primary control**: corrected to `[3,3,3,3,3,2,1]` (n=7, m=9, α=4, τ=3, unique k=0
structure). Trajectory: `[3,3,3,3,3,2,1]→[3,2,2,2,2,1]→[2,1,1,1,1]→[1,1]→[0]`. Heads
`(3,3,2,1)`, first three sum `8=m−1`, so `s=4`, `residue=3=α−1`.

Counterfactual availability table on this control:
- C1: e_B=0 true → gives B-degrees ≥2 (correct, actual value 3).
- C2/C3: e_B=1/2 both false → unavailable.
- Lemma U: `max(R)≤3` true but `Δ=3` and `#3s=4` → second hypothesis false, unavailable;
  a false application would give `m≤7` contradicted by actual `m=9` — exactly why the old
  blanket sentence was declared false.
- Lemma T: requires `s=τ=3`; actual `s=4` → unavailable (after step 2 list is `[2,1,1,1,1]`,
  not the `[D_3,1^{D_3},0^…]` shape).
- F-a/F-b: need `f=α+1`; this graph has `f=5=α+1` → hold; codegrees ≥2 for nonedges, `{x}`
  disjoint from the pair type.
- Direct HH: always available, gives `s=4`, `residue=α−1`.

This control also refutes the nearby false claim `D_i ≤ d_i−(i−1)`: HH heads `(3,3,2)` vs
`d_2−1=2` but `D_2=3`. The T3 proof does not rely on this false claim.

Also checked: control (c) the 8-vertex tree (`f=8=α+3`, C1-C3 correctly unavailable since
`f≠α+1`); control (b) the 8-vertex diam-4 counterexample graph (`τ=3` hypothesis of T3
doesn't apply; Lemma U counterfactually true and harmless); control (d) `K_{2,3}` for the
unqualified Corollary N2 (belongs to K-chain target, included per mandatory-probe
instruction — bound `Δ+τ(τ+1)/2−1=5 < m=6`, refuted exactly because reductio `residue=α`
fails there; HH gives `residue=2=α−1`).

## Trajectories computed

Five trajectories computed by hand with full intermediate lists: the k=0 control
`[3,3,3,3,3,2,1]` (18-step detail); the Repair R1 probe `[5,5,5,3,3,3,2]`; the `K_{3,5}`
probe; the symbolic k=2/e_B=2 trajectory (parametrized `a₀,b₀,c₀`) plus its concrete
instance `a₀=b₀=c₀=1` → `[4,4,3,3,2,1,1]`. Full detail in the conversation transcript
(URL above); key numeric results folded into the per-joint/gap sections above.

## What Qwen flagged it could not check

- Lemma 3 / Lemma 4 as formal Lean artifacts (checked elementary math content only, not
  the Lean formalization).
- Numerical backing outputs ("70,017 graphical degree sequences" etc.) — treated as
  unsupported without running the scripts; not needed for the logical checks.
- Graphical realizability of every parameter choice in the symbolic k=2/e_B=2 family
  (checked the HH trajectory of the degree sequence, not full realizability — does not
  affect the contradiction, which holds for any realized graph satisfying the reductio).
- K-chain Repair R2 — explicitly out of scope for TARGET=T3-REPAIRED, deferred to the
  K-CHAIN pass (see `w61_S3_KCHAIN_qwenA2.md`).

## owner-w61 verification duties (unchanged from Q5/Q6 dispatch note)

Both this repaired-round result and the parallel K-CHAIN result below are UNVERIFIED by
owner-w61 as of harvest time. owner-w61 should verify the T-J4 textual-defect diagnosis
(does the sum-contradiction sentence alone actually suffice, independent of the erroneous
count clause?) before ruling T3-REPAIRED CLEAN. Same-source firewall for this round =
parallel opus judge (per the Q5/Q6 dispatch notes), not this Qwen pass.
