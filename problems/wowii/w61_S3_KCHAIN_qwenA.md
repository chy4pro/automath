# Qwen S3 Round A — WOWII-61 K-CHAIN Adversarial Review

- Conversation: https://chat.qwen.ai/c/73a7da27-98f7-49bd-a8e6-66bc1dd63974
- Model: Qwen3.8-Max (confirmed switched before dispatch)
- Brief: `prompts/w61_S3_R2A.md` (self-contained; amended T12 counterfactual-availability
  clause baked in; verbatim draft appendix, sections A/B/C/D/F kept for TARGET=K-CHAIN)
- Dispatched: 08-18 ~09:2x CDT (owner-intel qwen_queue driver, fresh conversation)
- Harvested: 08-18 11:08 CDT (owner-intel qwen_queue driver round 3), after the 09:28–11:00
  CDT platform-wide 5h-window outage — Qwen's browser-side generation is a separate free web
  channel, unaffected by the Claude quota outage.
- Target context (per owner-w61's dispatch decision, recorded in
  `notes/reviews/wowii61_s3_dispatch.md`): the N-side target is the post-K consolidated chain
  (Lemma Z⁺ / DICH / Theorem K / Corollary K1), NOT legacy Theorem N — this closes N's S3 gate,
  with the patched Corollary N2 re-read folded in as named joint K-J6.
- Same-source firewall: the independent round-B judge is opus (`w61_S3_K_opusB.md`, run in
  parallel by owner-w61); no Spark/opus/Q1 output was pasted into this conversation.

## Overall verdict

**PARTIAL** — Theorem K and Corollary K1 ARE correct, but only after repairing a hidden
dependence in Lemma Z⁺/Lemma DICH on the reductio-only Lemma F3. As literally written, Z⁺ and
DICH are not proved in their stated (non-reductio) generality — Qwen supplies the repair, and
confirms Theorem K's own proof (which operates entirely inside the reductio) is unaffected.

## Per-joint table

| Joint | Verdict | One-line summary |
|---|---|---|
| K-J1 | **GAP (repairable)** | Lemma Z⁺'s counting/tie-breaking is fine, but its proof cites Lemma F3 for an s-bound while F3 is stated only under `residue=α` (i.e. `s=τ`) — a hidden-hypothesis mismatch. |
| K-J2 | OK | Lemma DICH parts (a),(b),(c) are correct, including boundary `i=1` and `j₀=i`, once Z⁺ is repaired; no independent defect. |
| K-J3 | OK | `K=B`, `hs=e_B`, and `Σ(i-1)=C(τ,2)` are all valid under Theorem K's stated reductio hypotheses. |
| K-J4 | OK | Corollary K1 uses Observation R1 consistently; the existential choice of maximum independent set A is harmless (argument survives any choice). |
| K-J5 | **GAP (repairable, same root cause as K-J1)** | Toolkit lemmas (S, T, F3, BO, Z, DEC, CNT, N′) are individually sound within their stated hypotheses; the K-chain's Z⁺/DICH use F3 outside its stated reductio (same defect as K-J1). Lemma C* not fully checkable (appendix doesn't define "occurring types realising (F-b)") but is NOT needed by the K-chain, so this is unchecked rather than a defect. |
| K-J6 | OK | The patched Corollary N2 is true as written; the `K_{2,3}` counterexample computation is correctly reproduced (`Δ+τ(τ+1)/2-1=5 < m=6`); the contrapositive form correctly repairs the reductio-dependent use. |

## The K-J1 / K-J5 gap in detail

Attacked lines: Z⁺'s claimed generality ("Write s for the number of HH steps (no reductio
needed unless stated)") combined with its proof step "If some block entry is a survivor then
`min(block) ≤ s-j+1` by Lemma F3" — but Lemma F3 in appendix §C is explicitly stated under
the standing assumption `residue(G)=α` (`s=τ`) and gives the bound `τ-j+1`, not `s-j+1`. If
`s≠τ`, these are different numbers and the cited lemma doesn't support the claim as written.

**Concrete exposing instance**: `K_{2,3}` (size-3 part as A, size-2 as B) has `α=3`, `τ=2`,
HH heads `(3,2,1)` giving `s=3≠τ=2` — so Lemma F3 (stated only for `s=τ`) is not available
there, exactly the gap.

**This does not break Theorem K** — Theorem K explicitly assumes `residue(G)=α(G)` (hence
`s=τ`) throughout its own proof, so it never actually needs the general-`s` version. The
defect is only that Z⁺/DICH are *stated* more generally than they're proved.

**Repair options Qwen offers** (either suffices):
1. Prove the general survivor-decay bound directly: at the start of step j, every survivor
   has value ≤ `s-j+1` (same proof as F3, with `τ` replaced by general `s` — a survivor can be
   decremented at most once per remaining step and must reach 0 by the end).
2. Or simply restrict Z⁺/DICH's stated scope to the reductio setting (replace the threshold
   by `τ-j+1`) — sufficient since Theorem K only ever invokes them there.

Also independently re-verified as correct within K-J1: the counting branch "all `D_j` block
entries are later heads … so `D_j ≤ s-j-1`" (valid: `D_j+1` distinct later heads among `s-j`
later head slots ⟹ `D_j+1 ≤ s-j`), and tie-breaking safety (a prefix of a non-increasing list
dominates its complement regardless of tie-break, so `v ≤ min(block)` survives adversarial
ties). One wording-only nit flagged (not a gap): "the block is a prefix of the non-head
entries" should read "a prefix of the remaining sorted entries after deleting the step-j
head" — as written it could be misread to exclude later heads from the block, which is false.

## Mandatory counterfactual-availability check (control instance)

Noted a discrepancy in the prompt's own control-case description: the prompt's probe 4(d)
states HK heads `(3,3,2)` for `[3,3,3,3,3,2,1]` summing to `m-1=8`, but Qwen recomputed the
**full** trajectory per Lemma 1's own definition and got heads `(3,3,2,1)` with `s=4`,
summing to `m=9` exactly (not `m-1`) — the prompt's `(3,3,2)` is a truncation, not the full
head sequence. Qwen used the full-trajectory (Lemma-1-compliant) convention throughout, since
the appendix's own `Σ D_i = m` (Lemma 1(2)) requires it.

On this instance (residue=3≠α=4, so most reductio-only lemmas are correctly unavailable),
Qwen also constructed a **second, more informative control graph** with `residue=α` (a 7-
vertex, 9-edge graph with independent set `{A,E,G}`, `α=3`, `τ=4`, min B-degree 2 < τ+1=5) to
test the K-J1/K-J5 lemmas in a regime where they *are* nominally available: verified Lemma
S/F3/H/BO/DEC/CNT all hold correctly there and give only weak/true bounds (e.g. Corollary CNT
gives `m≤13`, true and non-tight) — Theorem K/N/N′ correctly do NOT apply since
`min_B deg=2 < τ+1`. Conclusion: **no accepted lemma, checked against its actual hypotheses on
either control instance, yields a false or over-strong (slack≥2) conclusion.**

## Trajectories computed (5 total, per mandatory probe 5)

1. Full labelled HH run on `[3,3,3,3,3,2,1]` (`A,B,C,D,E`=3, `F`=2, `G`=1) — heads `(3,3,2,1)`,
   `s=4`, sum=9=m.
2. `K_{2,3}` for the patched Corollary N2 check — heads `(3,2,1)`, `s=3`, residue=2, α=3;
   confirms `Δ+τ(τ+1)/2-1=5 < m=6`, and since `residue≠α` the direct implication doesn't
   apply but the contrapositive correctly gives `residue≤α-1`.
3. Positive Theorem K example, τ=2: `K_4` minus one edge (B=2-clique, A=independent 2-set) —
   `s=2=τ`, every B-degree `=τ+1=3`, `h=(0,1)`, `hs=1=e_B=C(2,2)` — Theorem K holds exactly.
4. Positive Theorem K example, τ=3: `K_5` minus an independent edge (B=3-clique, A=2-set) —
   `s=3=τ`, `hs=3=e_B=C(3,2)` — Theorem K holds exactly.
5. Boundary τ=1: star `K_{1,r}` — `s=1=τ`, Theorem K gives `e_B=C(1,2)=0` (correct, B is a
   single vertex); patched N2 gives `m≤Δ` with equality — boundary is safe.

## What Qwen could not check

Lemma C*'s hypotheses (the appendix doesn't define "occurring types realising (F-b)" in the
K-CHAIN-relevant section) — noted as unchecked, and confirmed NOT needed by the K-chain
itself so this doesn't block the K-J1-K-J6 verdicts. Did not run/inspect numerical
verification scripts or Lean definitions — verdicts are from text + hand computation only.
Fact 2 (`residue≤α`) is treated as standing prior material per the text's own convention, not
independently reproved.

## Same-source / independence note

No Spark, opus, or Q1-round output was pasted into this conversation, per the brief's
instruction. Independence firewall for this round is the parallel opus judge
(`w61_S3_K_opusB.md`).
