# TASK L04 (r45) — how many perfect rows can delta == 0 carry? Push to the ceiling.
# TIER: ChatGPT GPT-5.6 Pro, SAME conversation as L02/L03 (it holds the method + code). NOT Gemini.
# Self-contained apart from that context. Do not ask questions back. Hard cap: code + JSON + 3000 words.

## Status of your objects (verified on our side; both are now banked)
L02 (q=3, |P|=3, delta==0) and L03 (q=3, |P|=4 = q+1, delta==0, P = {4,5,6,10} a
near-pencil; q=4, |P|=3, delta==0) all passed our independent verifier. Every cap
conjecture we held ("|P| <= 2", "|P| <= q" on delta==0) is refuted at q=3. What remains:
  (ROWCAP-FULL)  on ANY branch object at order q, at most q+1 rows are perfect
                 (a theorem at q=2 by exhaustion; your L03 object attains 4 = q+1 at q=3).
  (N-PROP)       no branch object has ALL n rows perfect (equivalently: the cellwise
                 identity E == N is never satisfied on the branch).
delta == 0 is necessary for all rows perfect (column sums of E must be n). So the question
is simply: on the delta == 0 sub-branch at q=3, what is the true maximum of |P|?

## Definitions (unchanged)
n = q^2+q+1; branch object = n x n array T with (B1) rows permutations, (B2) column c has
value nu(c) exactly q+1 times on ell_c, other values at most once, q values absent (D_c),
(B3) the ell_c form a projective plane of order q, (B4) nu bijective. a\v = unique w with
a*w = v; Xi_t(x) = x\(t\x); E(t,v) = #{x : Xi_t(x) = v}; N(t,v) = #{a : a*t = v};
delta(v) = Sum_t E(t,v) - n; row r PERFECT iff E(r,.) = N(r,.).

## TASK T0 — the CODE (highest value; we will run it ourselves)
Deliver the complete, runnable source of your instrument as ONE file (Python 3, stdlib
only, or C): the inverse-table SMT seeding is optional, the ANNEALER is mandatory — the
intra-row cyclic-swap moves that preserve (B1)-(B4), the incremental E/N/delta update,
the objective (perfect-row count with delta-mass penalty), temperature schedule, restart
logic. CLI: `--q`, `--design` (cyclic difference set; nu = id) or `--random-design`,
`--seed`, `--iters`, `--target-P`, `--dump-json PATH` (dump every new best object as
{"table","lines","nu"}). Print the best (|P|, mass) every 10^6 iterations. Correctness
matters more than speed; we verify every dump independently.

## TASK T1 — the ceiling at q=3
Starting from your L03 object (and from fresh seeds), maximise |P| subject to delta == 0
at q=3. Report the largest |P| reached and dump a JSON object for EVERY new level
5, 6, ..., 13. If you reach |P| = 13 (all rows perfect, i.e. E == N cellwise), say so in
one line at the top — that is the single most important possible outcome of this task.
Also report: iterations used, wall time, whether nu = id / cyclic design was kept or
random designs helped.

## TASK T1' — q=4
Same at q=4 (n=21): push |P| on delta == 0 beyond 3; dump JSON at each new level.

## TASK T2 — if you plateau
If |P| stalls at some k < 13 across many restarts: describe the obstruction as the
annealer sees it (which perfect-row equations conflict, which values' delta refuse to
close), and state the smallest sub-configuration (rows + columns) where the conflict
lives. We will hand that to an exact solver. A plateau is NOT evidence of a theorem;
report it as a plateau.

## Output format
T0 (code, complete), T1 (max |P|, JSON per level or NONE beyond 4, run statistics),
T1' (same for q=4), T2 (obstruction or "no plateau reached"), LIMITS.
