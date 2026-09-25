# TASK L06 (r45) — the whole frontier, and how far the searcher gets from (N) itself
# TIER: ChatGPT GPT-5.6 Pro, SAME conversation (holds branch_anneal.c v2). NOT Gemini.
# Self-contained apart from that context. Do not ask questions back. Cap: code + JSON + 3000 words.

## Status (all verified on our side; banked)
delta == 0 perfect-row records: q=3: 4 (your L03), q=4: 6 (your L05), q=5: 8 (your L05).
Every cap conjecture we held is refuted. The remaining question on this line is (N)
itself: can ALL n rows be perfect (E == N cellwise)? A theorem at q=2 says no (n=7,
exhaustive: the best table has 36/49 agreeing cells, i.e. 13 failing cells minimum).

## Definitions (unchanged)
n = q^2+q+1; branch object = n x n array T with (B1) rows permutations, (B2) column c has
value nu(c) exactly q+1 times on ell_c, other values at most once, q values absent (D_c),
(B3) the ell_c form a projective plane of order q, (B4) nu bijective. a\v = unique w with
a*w = v; Xi_t(x) = x\(t\x); E(t,v) = #{x : Xi_t(x) = v}; N(t,v) = #{a : a*t = v};
delta(v) = Sum_t E(t,v) - n; row r PERFECT iff E(r,.) = N(r,.).
total_defect := Sum_t Sum_v |E(t,v) - N(t,v)| (0 iff (N) holds).

## TASK T0 — the instrument, inline this time
Your updated branch_anneal.c (SHA-256 e8aae0e7…03f7) could not be recovered from the
file viewer (both cards open the L04 file). Print the FULL updated source inline in one
code block, or a unified diff against the L04 file (SHA 546b4105…6676), and print its
SHA-256 again. This is the highest-value item of this task.

## TASK T1 — distance to (N) at q=3 (decisive datum)
Target ALL 13 rows (--target-P 13, and separately --lock-rows / --hard-target on the
best 4-perfect delta==0 object as a seed): minimise total_defect. Report the minimum
total_defect and the minimum number of FAILING CELLS (#{(t,v) : E != N}) reached, with
the JSON of the best object, iterations and wall time. (At q=2 the exhaustive minimum
is 13 failing cells; a q=3 value far above 0 is the datum we want; a value of 0 is (N)
satisfied and would be the most important object of the campaign.)

## TASK T2 — the mass-vs-|P| frontier
For q=3 (|P| = 4..13), q=4 (|P| = 6..21), q=5 (|P| = 8..31): the minimum delta-mass you
can reach with EXACTLY |P| perfect rows (any P). A table (|P|, min mass, iterations),
plus JSON for the two lowest-mass points at each q that are NOT already delivered.
At q=3 you reported 4 → mass 0 and 5 → mass 18: confirm or improve 5, and fill 6..13.

## TASK T3 — extend the ladder
q=5: push delta == 0 beyond |P| = 8. q=7 (n=57; difference set e.g. {0,1,3,13,32,36,43,52}
mod 57 — verify it is a perfect difference set before use): first delta == 0 levels
and the largest |P| reached. JSON per new record.

## Output format
T0 (code inline + hash), T1 (numbers + JSON), T2 (table + JSONs), T3 (records + JSONs),
LIMITS. Every JSON will be verified mechanically on our side.
