# TASK L05 (r45) — one delta pair from the last cap: finish the q=4 six-row state
# TIER: ChatGPT GPT-5.6 Pro, SAME conversation (it holds branch_anneal.c). NOT Gemini.
# Self-contained apart from that context. Do not ask questions back. Cap: JSON + 2500 words.

## What your L04 files established (all four verified on our side)
- q=4: |P| = 5 = q+1 with delta == 0 (rows {0,1,2,15,17}; NOT a line) — VERIFIED.
- q=4: |P| = 6 with delta = (+1 at value 7, -1 at value 10), mass 2 — VERIFIED.
- q=3: |P| = 5 with mass 18 — VERIFIED.
LEVEL-OF-QUANTIFICATION NOTE (please read): the statement "on ANY branch object at most
q+1 rows are perfect" is REFUTED by your own diagnostics (5 rows at q=3, 6 rows at q=4).
The only cap still standing is the delta == 0 one:
  (ROWCAP-D0)  on the delta == 0 sub-branch at order q, at most q+1 rows are perfect.
It is tight at q=3 and q=4. Your six-row mass-2 state is one delta pair away from
refuting it at q=4. That is this task.

## Definitions (unchanged)
n = q^2+q+1; branch object = n x n array T with (B1) rows permutations, (B2) column c has
value nu(c) exactly q+1 times on ell_c, other values at most once, q values absent (D_c),
(B3) the ell_c form a projective plane of order q, (B4) nu bijective. a\v = unique w with
a*w = v; Xi_t(x) = x\(t\x); E(t,v) = #{x : Xi_t(x) = v}; N(t,v) = #{a : a*t = v};
delta(v) = Sum_t E(t,v) - n; row r PERFECT iff E(r,.) = N(r,.).

## TASK T1 (decisive at q=4)
From L04_q4_P6_mass2_diagnostic.json (rows {0,1,2,5,15,17}, delta +1 at 7 / -1 at 10):
reach delta == 0 while keeping SIX perfect rows (any six rows; the set may change).
Use --hard-target on the six rows and/or free targets; vary seeds; also try six-row sets
containing your verified five-row delta==0 set {0,1,2,15,17}. Deliverable: JSON
{"table","lines","nu"} for every new (|P|, mass) frontier point with |P| >= 6, in
particular ANY object with |P| >= 6 and mass 0. Report iterations, wall time, and the
best (|P|, mass) frontier reached. If the mass-2 six-row basin is closed under your
moves, say so with the same BFS-style analysis as L04 T2 (component size, minimal exit).

## TASK T1' (q=3, the other side of the same cap)
From L04_q3_P5_mass18_diagnostic.json (rows {0,1,2,3,9}, mass 18): drive the mass down
while keeping FIVE perfect rows. Report the lowest mass reached with |P| = 5 and the JSON;
any mass-0 five-row object refutes (ROWCAP-D0) at q=3.

## TASK T2 (q=5, n=31 — extend the family one order)
PG(2,5): cyclic difference set {1,5,11,24,25,27} in Z_31 (any perfect difference set of
size 6 mod 31 is fine; state the one you use). Adapt branch_anneal.c (q=5 support:
MAXN >= 31, design table) and report the first delta == 0 objects with |P| = 1, 2, 3, ...
as far as the budget allows; JSON per level. Tell us the largest |P| with delta == 0 you
reach and whether it is again q+1 = 6.

## TASK T3 (the instrument)
Attach the updated branch_anneal.c (with q=5) and print its SHA-256 in the answer, as
you did for L04. Keep the from-scratch full_verify() before every dump.

## Output format
T1 (frontier table + JSONs), T1' (frontier + JSON), T2 (per-level JSONs + max |P|),
T3 (file + hash), LIMITS. Every JSON will be verified mechanically on our side.
