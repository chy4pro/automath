# CODEX TICKET (sol tier, DEEP ATTACK ROUND 2, MINIMUM 2.5 h of work) — the two sharpest
# obstructions from engine/out/codex/etp677_S_attack_report.md. Repo:
# $HOME/workspace/claudecode/automath. English. No internet. Pure Python only
# (benchmarks: problems/etp677/R8_invariants.py loaders, R9A_scripts/r9a_DO.py for m77D;
# your round-1 verifier problems/etp677/S_attack_codex/attack.py).

Round 1 stopped after 11 minutes with named obstructions and no attempt to close them.
This round is the attempt. Work each item until a proof or a witness-backed obstruction;
do not stop early — if an approach dies, record why and try the next. Report honestly
what was and was not achieved; label PROVED / VERIFIED-ON-MODELS / CONJECTURED.

## Item A — O2-HCE, Heavy-Collision Exclusion (the non-extremal branch, never attacked)
Setting: finite E677 magma (KEY holds; (N) holds cellwise), and suppose ϱ = ∇ (every pair
a ≠ b collides in some column). CSM (round 1, PROVED): Σ := Σ_{t,v} N(t,v)² = n² + 2Σ_{a<b}|F_ab|,
so ϱ = ∇ gives Σ ≥ 2n² − n with equality iff every pair collides EXACTLY once (the extremal
branch, handled elsewhere). TARGET: prove Σ ≤ 2n² − n under KEY + (N) + ϱ = ∇ — or find
the exact reason it can fail. Handles to try, in order:
 A1 (N) says N(t,v) = |Fix(L_t R_v)| = |{x : t*(x*v) = x}|. Express Σ_{t,v} N(t,v)² as a
    count of pairs (x,x') with t*(x*v) = x and t*(x'*v) = x'; use KEY to rewrite; look for a
    second identity for the same count (double counting over (x,x') first) — the campaign's
    NEW-ID Σ_z N(z*x, z) = n and (R9-E/N-form) are the known shapes.
 A2 Row-level: for fixed t, Σ_v N(t,v)² = Σ_v |Θ_t^{-1}(v)|² with Θ_t(x) = (t*x)*t = Ξ_t(x) =
    x\(t\x) (KEY). Is there a bound on the fibre sizes of Θ_t from KEY alone? (R9-G/conc-false
    says no per-cell bound < q²+1 on the ABSTRACT branch; but that branch does not have KEY.)
 A3 Pair-level: for a ≠ b with |F_ab| ≥ 2, i.e. two columns t ≠ t' with a*t = b*t and
    a*t' = b*t': apply KEY/E677 at (a,t), (b,t), (a,t'), (b,t') and derive further forced
    collisions; does ϱ = ∇ + KEY force |F_ab| = 1 for all pairs (hence extremal), or
    produce an explicit contradiction? Try to build a small witness table (n ≤ 13) with a
    pair colliding twice under all of KEY+(N)+ϱ=∇ by hand/backtracking (pure Python,
    ≤ 10 min CPU) — SAT is running separately; your job is the structure, not the search.
 A4 If a bound fails, find the smallest structure (a partial table) exhibiting Σ > 2n² − n
    consistent with KEY+(N) locally, and state precisely what global fact would kill it.

## Item B — O1-GTC, the closure transport (B)
(B): ϱ* is a congruence. Round 1 proved (B) ⟺ generator transport: a ϱ b ⟹ (c*a) ϱ* (c*b)
and (a*c) ϱ* (b*c). TARGET: prove generator transport from KEY. Handles:
 B1 Left transport: a*t = b*t. Want a path of collisions from c*a to c*b. E677 at (x,y) =
    (c*a, ·) and (c*b, ·); use KEY: (y*x)*y = x\(y\x). Compute what a*t = b*t forces about
    rows a, b (they agree at column t) and about the rows c*a, c*b via the transitivity of
    ⟨L⟩ (R7-C: x = L_y L_x L_{L_y x} y). Try to express c*a and c*b as images of a and b
    under a common word in left translations, then show a collision propagates along words.
 B2 Right transport: a*t = b*t ⟹ (a*c) ϱ* (b*c). Same, using KEY in the form
    (y*x)*y = x\(y\x) with x = c.
 B3 Test every intermediate identity you conjecture on m77D (11 ϱ*-classes) and m385canon
    (55 classes) BEFORE using it — both have many collisions; a claim that fails there is
    dead. Also test on the round-1 order-7 translation-invariant (N)-but-not-KEY control
    (h = (1,2,0,5,6,4,3)) to see whether KEY is actually used.

## Deliverables
`problems/etp677/S_attack_codex/round2/{notes.md, scripts, outputs}` and
`engine/out/codex/etp677_S_attack2_report.md` ending with DONE-SATTACK2: for each of A, B —
the derivation attempts (with the exact step that failed, if any, and the witness that
shows it fails), any new PROVED lemma with its benchmark test output, and the sharpened
obstruction statements. Time box: 3 h; minimum 2.5 h of genuine work.
