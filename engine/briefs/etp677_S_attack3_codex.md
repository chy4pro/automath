# CODEX TICKET (sol tier, ROUND 3, MINIMUM 2.5 h) — one sharp target from round 2:
# PAIR CONSERVATION  C(a,b) = |F_ab|  for every pair a ≠ b in a finite E677 magma.
# Repo: $HOME/workspace/claudecode/automath. English. No internet. Pure Python only.
# Read first: problems/etp677/S_attack_codex/round2/notes.md (your own round-2 record:
# the certificate digraph, the KEY certificate bijection, the Pair Conservation observation).

## The statement
F_ab := {t : a*t = b*t}; Xi_t(x) := x\(t\x); C(x,y) := #{t : Xi_t(x) = Xi_t(y)}.
Round 2 PROVED the bijection (a,b,t) ↦ (t\a, t\b, t) from collision certificates to common-Xi
certificates, hence Σ_{a≠b}|F_ab| = Σ_{x≠y} C(x,y) GLOBALLY, and OBSERVED (all genuine
benchmarks m77D, m385canon, m176, m496, M9 + three auxiliary models; fails on both non-KEY
controls) the PAIRWISE identity  C(a,b) = |F_ab|  — the certificate digraph
(a,b) → (t\a, t\b) (t ∈ F_ab) has indegree = outdegree at every vertex.
TARGET: derive C(a,b) = |F_ab| from E677 (KEY), or find the exact reason it cannot be
derived and a witness. This is a CONCRETE identity with a concrete bijective structure —
work it fully:
 T1 Write |F_ab| = #{t : a*t = b*t} and C(a,b) = #{t : a\(t\a) = b\(t\b)}. Look for a
    second bijection between these two t-sets (for the SAME pair (a,b)), e.g. t ↦ a*(t\a)…,
    t ↦ (t*a)*t = Θ_t(a) (KEY: = Xi_t(a)), t ↦ t\a, or the R7-C witness formula. Test each
    candidate map on m77D FIRST (does it send F_ab into the C-set bijectively?); print the
    candidate, the pairs tested, the counts.
 T2 If no pointwise bijection exists (show it by exhibiting a pair on m77D where no
    "natural" map works — or better, prove that F_ab and the C-set can be different sets
    of the same size), look for a counting argument: Σ over v of #{t ∈ F_ab : a*t = v} vs the
    fibre structure of Xi; use (N) N(t,v) = |Fix(L_t R_v)| and NEW-ID Σ_z N(z*x, z) = n.
 T3 If PROVED: state what it buys — the certificate digraph is balanced (Eulerian
    components); does balance + universal ϱ force |F_ab| = 1 (HCE)? If not, give the
    smallest balanced digraph shape with a surplus cycle that KEY does not exclude, and
    test whether that shape can be embedded consistently (bounded pure-Python search,
    ≤ 10 min CPU).
 T4 If NOT proved: the precise obstruction, plus the smallest partial table (n ≤ 9) that
    satisfies every finite consequence of KEY you can enumerate locally yet has
    C(a,b) ≠ |F_ab| for some pair — or the statement that none exists at n ≤ 7 (exhaustive
    over KEY-satisfying left quasigroups of order ≤ 7, which are few: report the population).

## Deliverables
`problems/etp677/S_attack_codex/round3/{notes.md, scripts, outputs}`,
`engine/out/codex/etp677_S_attack3_report.md` ending with DONE-SATTACK3. Labels PROVED /
VERIFIED-ON-MODELS / CONJECTURED as before; every candidate map/identity reported with the
benchmark output that killed or supported it. Do not stop before 2.5 h of genuine work.
