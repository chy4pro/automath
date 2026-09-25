# R9-C battle brief: attack (Prop) by design theory

Campaign #1 (ETP Finite 677 => 255), Round 9-C. Opened 2026-08-18.
Read together with: prompts/etp677_R3_common.md (toolbox + blocked routes),
papers/etp677_structure/main.tex sections "skeleton" / "Round 9" (v7.2),
problems/etp677/campaign_registry.md (latest entries).

## Where the campaign stands

The main proposition (P) -- every finite E677 magma satisfies E255 -- reduces to

    (P)  <==  [NTS closure] + [(B): rho* is a congruence] + [(Prop): rho* != nabla]

with (Q) => E255 already known. All three legs are open. (B) lost every proof
route in Round 9. This brief targets the third leg, (Prop).

## The two readings of (Prop) -- READ THIS FIRST, it was a v7.1 correction

Let rho be the RAW collapse relation: a rho b iff some t has a*t = b*t, i.e.
iff F_ab := {t : a*t = b*t} is nonempty. Let rho* be its transitive closure.

    (Prop)        rho* != nabla          <-- what thm:twolegs actually needs
    (Prop_E)      exists a != b with F_ab = empty   <-- the existential weakening

(Prop) => (Prop_E) holds (pick a, b in different rho*-classes). THE CONVERSE IS
FALSE in general: rho* = nabla only needs the collapse graph to be CONNECTED,
while not-(Prop_E) needs it to be COMPLETE. An earlier version of the paper
glossed these as equivalent; that gloss is retracted. Consequence for this
round: an argument that merely rules out "every pair collapses directly"
establishes (Prop_E), NOT (Prop). Closing the gap from completeness to
connectivity is part of the job, not a footnote.

## Why design theory

rho = nabla says: the n partitions {ker R_t}_{t in M} cover every pair of points
of M. That is exactly a RESOLVABLE PAIRWISE COVERING DESIGN on n points with
exactly n parallel classes. Known side conditions available as constraints:

- refined T3 (thm:T3refined): for a != b, |F_ab| <= (n - odd(L_a))/2, where
  odd(L_a) = number of odd-length cycles of L_a; in particular
  F_ab cap Fix(L_a) = empty, and |F_ab| <= (n-1)/2 for odd n.
- N(v,v) <= 1 (prop:rightdual) and the right-dual statistics.
- Sigma >= 2n^2 - n whenever rho = nabla; if moreover every |F_ab| = 1 the
  design is a resolvable LINEAR SPACE with S_a = 2n - 1 for every a.
- de Bruijn--Erdos / Fisher-type inequalities apply to linear spaces: a linear
  space on n points has at least n lines, with equality iff near-pencil or
  projective plane. A resolvable linear space whose lines split into exactly n
  parallel classes is extremely rigid.

The permutation-group route is provably silent here (thm:jordan): the
displacement set D = S^{-1}S \ {1} is not a subgroup, and by refined T3 every
element of D with a fixed point moves at least n/2 points, so Jordan-type
"small support => contains A_n" theorems say nothing.

## Tasks, in priority order

T1. (Main) Prove or refute: no finite E677 magma with |M| > 1 has rho = nabla.
    Equivalently: the n column kernels of a finite E677 magma cannot form a
    resolvable pairwise covering design. Use the side conditions above; the
    intended tools are counting/Fisher-type, not group theory.
    If you prove it, you have (Prop_E). SAY SO EXPLICITLY and go to T2.

T2. (The gap that T1 does not close) Assuming rho != nabla, when is rho* still
    nabla? Give a structural criterion for connectivity of the collapse graph
    on M, and either (a) prove that E677 forces the collapse graph to be
    disconnected once it is not complete, or (b) produce the obstruction: an
    E677-compatible configuration with rho != nabla but rho* = nabla.
    Note (b) would be as valuable as (a) -- it would tell us (Prop) needs a
    genuinely different attack than (Prop_E).

T3. Benchmark discipline (MANDATORY before claiming anything general): every
    candidate law/claim must be checked against the nine-model zoo, and
    m77D FIRST, then m385canon and m385R. A claim that is not tested on m77D
    counts as zero evidence. Scripts: problems/etp677/R9_audit.py,
    R9_clean_check.py, R6_zoo.py. Note (Prop) and (Prop_E) are AUTOMATIC for
    every pair-indexed extension over a Latin base (prop:propauto), so the whole
    zoo satisfies them -- the zoo can REFUTE a general lemma you invent, but it
    can never supply positive evidence about (Prop) itself. Design accordingly.

T4. If T1 and T2 both resist, deliver the strongest unconditional partial:
    e.g. a lower bound on Sigma or on max |F_ab| that any counterexample must
    satisfy, or a proof for a restricted class (simple non-Latin magmas of odd
    order, magmas with a fixed-point-free left translation, ...).

## Hard rules

- No SAT, no exhaustive search, no heavy local computation. Verification is
  Python table lookup over archived models only.
- Nothing counts as proved until it is stated as a numbered claim with a full
  proof. Separate PROVED / COMPUTATIONAL / CONJECTURE explicitly, as the paper
  does.
- (Prop) is existential over finite structure, so no ATP applies -- do not
  propose an equational/ATP route (see the two non-first-order barriers,
  meta-theorem [C]).
- Report honestly if a route dies; a clean negative ("this cannot work because
  ...") is a first-class deliverable in this campaign.
