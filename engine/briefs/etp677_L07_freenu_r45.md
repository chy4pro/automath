# TASK L07 (r45) — the instrument, recoverable this time; then leave the nu = id subfamily
# TIER: ChatGPT GPT-5.6 Pro, SAME conversation (holds branch_anneal.c v3). NOT Gemini.
# Self-contained apart from that context. Do not ask questions back. Cap: code + JSON + 2500 words.

## Why this brief
Your v3 annealer (SHA-256 809649d3…df7c) could not be recovered: the attachment card did
not open, and the inline unified diff lost its leading-space context markers in page
capture. Also: every object and every plateau you have produced lives on ONE subfamily —
cyclic line set with nu = identity (your dumper writes nu = id unconditionally). Our
exact instance of (N) at q=3 has the column→line assignment AND nu free. So a plateau
of yours (e.g. 40 failing cells at q=3) is a statement about that subfamily only.

## TASK T0 — deliver the source so it survives page capture
Print the FULL v3 source (or v4, see T1) in ONE fenced code block, no diff, no
attachment, no line numbers. Avoid line continuations inside macros and avoid string
literals whose meaning depends on leading whitespace (leading indentation may be
stripped by our capture; C does not care, but a `\`-continued macro or a multi-line
string would). Print `sha256sum` of your file as well; we will accept by COMPILE
(`cc -O3 -std=c11 -Wall -Wextra -pedantic -lm`, zero warnings) + REPRODUCTION with our
own seed, not by hash.

## TASK T1 — v4: free nu and arbitrary designs
Add: (a) `--nu random|id|FILE` — a general bijection nu, with the block cells T[a][c] = nu(c)
on ell_c, moves that keep (B1)-(B4) under a non-identity nu, and the dumper writing the
actual nu; (b) `--lines-json FILE` — an arbitrary line set (any projective plane of order
q given as n lists of q+1 points; we will supply non-cyclic ones), with the column→line
assignment `--asg random|id`; (c) keep everything else (compound moves, failing-cell
objective, --lock-rows). Verify on our verified objects that v4 reproduces their
(|P|, mass, failing cells) when loaded with --start-json (they carry their own nu/lines).

## TASK T2 — (N) distance at q=3 off the subfamily
With v4: minimise failing cells at q=3 over (i) nu random, cyclic lines; (ii) nu random,
asg random. Report the minimum failing-cell count and total_defect reached in each mode
(budget: your call, but state iterations), with the JSON of the best object per mode. The
comparison against your nu = id result (40 failing cells / total 44) is the datum.
A value of 0 is (N) satisfied — say so on the first line if it happens.

## TASK T3 — delta == 0 records off the subfamily (cheap, optional)
q=3 and q=4 only: with nu random (and asg random), can the delta == 0 perfect-row record
(4 at q=3, 6 at q=4) be exceeded? JSON for any object beating it.

## Output format
T0 (code block + hash), T1 (v4 code block + hash + reproduction table on our objects),
T2 (table + JSONs), T3 (JSONs or NONE), LIMITS. Every JSON will be verified mechanically.
