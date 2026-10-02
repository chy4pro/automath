# 038 Sidon (#30): beat the coefficient 2√2/3 with an argument outside the fixed-kernel scalar method
priority: high · parallel: yes (use the full agent/parallel budget) · clean-room: yes (for every attacking agent) · report: /work/problems/erdos30/beyond/astra/REPORT.md

Context for you (the dispatcher), not for the attackers' reading list: 037 is closed — `sidon_second_order` is kernel-checked (CI 37060176909, f8e9766). Thank you; that loop worked. The coordinator independently confirmed the run via the jobs API and audited Statement/Basic.

Target (v3 shape: one target, large budget, 20–30M tokens is acceptable):
  prove F(N) ≤ √N + c·N^{1/4} + o(N^{1/4}) for some explicit c < 2√2/3 = 0.942809…,
  F(N) = max size of a Sidon set in {1..N} (all pair sums a+b, a ≤ b, distinct; diagonal included).
A fully explicit version (all N ≥ N₀) is better but not required for a first hit. Any proved c < 2√2/3 is a hit; state c exactly.

What every attacker is given (and nothing else — no web, no papers, no campaign files, no /work/problems/erdos30/** files, no other attacker's output):
1. The definition and target above.
2. One paragraph of what is already proved by us: weighted difference counting with a kernel f on window length L, Cauchy–Schwarz against the interval capacity C_f(L), ramp kernel 2(1−t), boundary constant 2/3, giving 2√2/3; and the barrier theorem: for every even nonnegative f ∈ C₀∩L¹ with ∫f=1, liminf(C_f(L)−L) ≥ 8/(9f(0)), so no single fixed kernel in the scalar capacity inequality can beat 2√2/3.
3. A route seed (different per attacker; they may abandon it). Seeds, at least these, plus your own: (a) two or more window scales coupled in one inequality; (b) position-dependent weights / non-translation-invariant quadratic forms; (c) using sums as well as differences (A+A is also injective on unordered pairs); (d) exploiting the slack in Cauchy–Schwarz: equality forces near-uniform window counts — derive a stability statement and contradict it with the Sidon property at another scale; (e) LP/SDP duality over density profiles of A on sub-intervals, solved by hand; (f) higher-moment (third/fourth) counts of window occupancy; (g) modular reduction / embedding into a cyclic group where the boundary term vanishes, with the cost of wrap-around bounded; (h) unseeded control tickets.
4. The standard of proof: every inequality justified, every o(·) term bounded, exact quantifiers. An honest "OPEN with exact obstruction" is an acceptable outcome and must not be dressed up as progress.

Gates on your side before you report a hit: (i) a second fresh Astra agent re-derives the key inequality from the written proof alone and attempts to break it; (ii) a small exact/numeric check of every identity that can be checked (python in ~/.venv-automath; no solvers); (iii) confirm the claimed c is really < 2√2/3 with exact arithmetic. The coordinator will then run cross-vendor Claude referees and the literature-status check (do not do literature search inside the attack).

Also wanted: for failed routes, a one-paragraph obstruction each (these go into a barrier map; three or more routes dying for the same reason is itself a publishable-quality observation).

Note: two isolated Claude Opus probes on the same target write to /work/problems/erdos30/beyond/PROBE_A.md and PROBE_B.md. Do not let attackers read them; you may read them yourself after your own first round is complete.

Push back if you judge another target more valuable for Astra right now (say which and why, with evidence) — e.g. the explicit onset N₀ far below 120⁴, or a different problem from the 025 probe table. A transfer scout report may appear at /work/notes/selection/transfer_targets_20261002.md; if a transfer target there looks like a surer hit than this one, say so in QUESTIONS.md and proceed with your better judgement.
