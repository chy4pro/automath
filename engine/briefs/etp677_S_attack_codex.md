# CODEX TICKET (sol tier, DEEP ATTACK, 3 h) — the SIMPLE case of ETP 677→255:
# prove or refute (S): every finite SIMPLE 677-magma is a quasigroup (Latin table).
# Repo: $HOME/workspace/claudecode/automath. English. Do not search the internet.
# Local compute: pure Python only (benchmark tables are in the repo; see below); no SAT.

## Read first (in this order; cite facts by their names, do not restate them at length)
1. problems/etp677/REGISTER_A.md — the skeleton (P) ⟸ NTS + (B) + (Prop) + [(Q')⟹E255],
   with (S) ⟸ (B) + (Prop): (B) "ϱ* is a congruence", (Prop) "ϱ* ≠ ∇", where a ϱ b iff
   some column t has a*t = b*t. Both legs OPEN; the two dead routes to (Prop) and the WARN-2
   trap for (B) are described there. The extension case is being decided separately (R46);
   THIS ticket is the other half: a minimal counterexample that is simple.
2. prompts/etp677_R3_common.md — the toolkit (PROVED facts: KEY, T1, T1', T3, L1, L4, (N),
   NEW-ID, the R9-x entries; and the BLOCKED routes B1–B6 — do not re-tread them).
3. The mandatory benchmark discipline: any identity or structural claim you conjecture MUST
   be tested on m77D, m385canon, A7psiE, m176, m496, M9 before you build on it. Tables and
   loaders: problems/etp677/R9A_scripts/r9a_DO.py (m77D), problems/etp677/R8_invariants.py
   (loads the whole benchmark set — read it to see how each model is constructed).
   (WARN-2): every known finite 677-magma satisfies E255, so "holds on all models" is zero
   evidence for the main line; a claim needs a DERIVATION from E677.

## Task
Attack (S) by whatever global mechanism you can find; three concrete openings, in order:
 O1 (B) directly: show that the transitive closure ϱ* of the column-collision relation is a
    congruence of (M,*): i.e. a ϱ* b ⟹ (c*a) ϱ* (c*b) and (a*c) ϱ* (b*c). The pointwise
    transport law (T) is FALSE (m77D), so the argument must be global/closure-level. Test
    candidate lemmas on m77D (ϱ* has 11 classes there) and m385canon.
 O2 (Prop) via the collision structure: in a simple non-Latin 677-magma, ϱ* = ∇ would be
    forced by (B); show ϱ* = ∇ is impossible using (N) [(R9-E/N-is-B3)] plus KEY. The
    extremal sub-case (every pair collides exactly once ⟺ column kernels form a projective
    plane) is the campaign's (N-Prop) branch and is being decided by SAT at q=3 — do NOT
    spend time there; the NON-extremal case (some pair collides ≥ 2 times) has never been
    specified: specify it and attack it.
 O3 The dictionary theorem (registry R8-A): congruences ⟺ ⟨L⟩-block systems + a kernel
    condition; ⟨L⟩ primitive ⟹ simple. If ⟨L⟩ is primitive and the table is not Latin,
    derive a contradiction from (N)/T1'/KEY (permutation-group flavour: O'Nan–Scott is
    available, fine T3 says a displacement with a fixed point moves ≥ n/2 points).
For each opening deliver either a DERIVATION every step of which cites a named toolkit fact
or a proved lemma (with Python verification of every finite claim on the benchmark set,
positive AND negative controls), or a PRECISELY NAMED OBSTRUCTION (the exact statement that
would close it, and why the available facts do not entail it — with a witness model if one
exists). Any new identity you claim must come with the benchmark test output.

## Deliverables
`problems/etp677/S_attack_codex/{notes.md, scripts…, outputs}` and
`engine/out/codex/etp677_S_attack_report.md` ending with DONE-SATTACK. Honesty rules: label
every statement PROVED / VERIFIED-ON-MODELS / CONJECTURED; a statement true on all models
and not derived is CONJECTURED. Do not stop at the first partial reduction; push each
opening to a proof or a named obstruction, then switch.
