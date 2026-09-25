# CODEX TICKET (exact search engineering; any tier — verified verdicts only) — FIBRE-4 local
# cores by the gauge-free method, and a completion attempt.
# Repo: $HOME/workspace/claudecode/automath. Read problems/etp677/simple/fibre_core/
# (core7_free.py, core_joint.py: semantics, product table, instances; out/: m=3 UNSAT DRAT) and
# registry R46 STEP 48/49 (grep "STEP 49"). Local caps: ≤ 600 s per solve, ≤ 2 heavy processes.
# kissat: tools/kissat/build/kissat; drat-trim: tools/drat-trim/drat-trim; CP-SAT in
# engine/venv_item3. DONE marker: DONE-FIBRE4CORE.

## Known
Gauge-free extension (x,s)*(y,t) = (xy, σ_{x,y}(s)(t)); lifted E677 chain as in core_joint.py.
Seven-instance P* core: UNSAT for m = 2, 3 (minimal for 3), SAT for m = 4, 5. Joint 10-instance
core (all E677 instances closed under the 21-entry product table on 12 symbols): m = 3 UNSAT,
m = 4 SAT, m = 5 SAT.

## Tasks
1. Enlarge the symbol/product universe systematically: start from a, and add the unary terms
   S, U, W, P, F, H (H(x) = S(x)U(x) = F⁻¹(x)) of a, of b = F(a), of u = U(a), of w = W(a), of
   p, of d = bb, v = db, c = W(b), and the L_a-cycle terms L_a^{k}(a) for |k| ≤ 6; record every
   product between named terms that is a THEOREM of finite E677+E255 magmas — take them from
   the Lean library lean/etp677_ext (L13_*, X1_*, window_*, Ext677Pattern/PatternPairs) and
   from the identities listed in STEP 37/38/47/48 (u*x = x ⟹ x*u = W(x) ∧ U(x) = u; W(x)S(x) =
   U(x); S(x)x = U(x); P(x)x = F(x); c = p ⟺ pp = a is NOT a product — do not use
   conditional facts). VERIFY every product you use numerically on F31, T7, 4x+3y, M49ε,
   M217ε, R217 (all E677+E255) before using it — a false "universal" product invalidates
   everything. Then enumerate all E677(x,y) instances whose chain closes in the table.
2. For m = 4: solve the gauge-free core of the full instance set; if UNSAT — DRAT, drat-trim,
   then minimise (drop instances greedily, re-verify) and report the minimal core and its
   pairs; if SAT — report the largest core's satisfying σ (as explicit permutations) and try
   to complete it: CSP/SAT for a genuine E677 magma of order 4·|B| with a congruence of class
   size 4 over B ∈ {T7, 4x+3y mod 7, F13 affine, F31} (pair-indexed extension encoder
   problems/etp677/ext/ext_cnf.py with --no-defect, m = 4, base f7a/f7b/f13/f31c — these cells
   exist; run each ≤ 600 s, report verdicts; a SAT table must be verified with
   ext_decode_verify.py and its class sizes computed). Any SAT here = the first known E677
   magma with a class of size 4 (verify exhaustively before reporting).
3. Same enumeration for m = 5 as a sanity control (must be SAT: order-25/35 models have
   classes of size 5); and re-run m = 2, 3 on every core as controls (must be UNSAT).
## Deliverables
problems/etp677/simple/fibre_core/fibre4/ (universe/product tables with their verification
logs, instance lists, CNFs, DRATs, σ-solutions, completion runs) and
engine/out/codex/etp677_fibre4_core_report.md ending with DONE-FIBRE4CORE.
