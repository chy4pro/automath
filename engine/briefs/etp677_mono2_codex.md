# CODEX TICKET (engineering + exact search; any tier — no conjectural claims) — MONOGENIC
# LADDER v2: a fully canonical encoding for one-generated E677 magmas with an E255 defect at
# the generator. Repo: $HOME/workspace/claudecode/automath. Read
# problems/etp677/simple/mono_cnf.py (current encoder: X[a][b][v] one-hot, rows permutations,
# E677 via aux terms, generation clauses OR_{a<j,b<j} X[a][b][j], defect ¬X[0][0][s] ∨
# ¬X[s][0][u] ∨ ¬X[u][0][0]), mono_canon.py (canonicaliser / decoder / verifier — keep it as
# the independent checker), simple/mono/in|out (n = 5..8 UNSAT with DRAT; 9–12 UNKNOWN at 120 s
# locally; a cloud ladder 9–30 is running with the v1 encoding). Local caps: any solve ≤ 600 s;
# heavy processes ≤ 2. kissat: tools/kissat/build/kissat; drat-trim: tools/drat-trim/drat-trim;
# CP-SAT: engine/venv_item3/bin/python. DONE marker: DONE-MONO2.

## Why
Registry R46 STEP 25: 677 ⟹ 255 (finite) ⟺ every finite one-generated E677 magma satisfies
E255 at its generator. v1's generation clauses only weakly break the S_{n−1} relabelling
symmetry of the non-generator elements; a canonical BFS numbering should cut the search by
orders of magnitude and make n = 9..14 exact decisions feasible.

## Tasks
1. Canonical BFS encoding `mono_cnf2.py`: elements are numbered in the order they are first
   produced when the table is read in a FIXED scan order (e.g. row-major over (a,b) with
   a,b ≤ current frontier, or "L_0-orbit first": 1 = 0*0, 2 = 0*1, … then row 1, …). Encode
   "element j first appears at the earliest scan position among all positions holding a new
   element" with prefix/"seen" auxiliary variables (as in canonical-form encodings for
   quasigroups / Sims-style lex-leader for the relabelling group). PROVE in a comment that
   every one-generated magma has exactly one labelling satisfying the constraint (so SAT ⇔ a
   monogenic model exists, and UNSAT is a theorem at that order). Alternative if simpler and
   provably complete: the "L_0-cycle first" numbering — 0, 0*0, 0*(0*0), … is the L_0-cycle
   through 0 (length m; m ≥ 6 by the cycle lemma), then continue BFS by products.
2. Controls (mandatory): n = 7 with F7 (4x+3y) canonicalised → SAT with defect-free variant;
   n = 5..8 with the defect → UNSAT and DRAT-verified, matching v1; the decoded model of any
   SAT run must pass mono_canon.py's verifier. Report var/clause counts and kissat times v1
   vs v2 for n = 7..12 (600 s cap) — a table, no extrapolation.
3. If v2 decides new orders (n = 9, 10, 11, 12 …) locally within the cap: produce DRAT proofs
   and verify with drat-trim; each UNSAT is the theorem "no finite E677 magma of order n has a
   generating point failing E255". Also add a CP-SAT variant if it beats kissat on n = 9.
4. Package the cloud inputs for n = 9..30 (v2) under simple/mono2/in/ with SHA256SUMS and a
   runner startup_mono2.sh (same conventions as problems/etp677/ext/startup_ext.sh). Do not
   launch.

## Deliverables
mono_cnf2.py, calibration table, DRAT files for every new decision, simple/mono2/in/, and
engine/out/codex/etp677_mono2_report.md ending with DONE-MONO2.
