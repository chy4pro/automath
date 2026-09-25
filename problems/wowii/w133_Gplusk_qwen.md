# Q16 harvest — w133 pocket 2, the `l >= 4` layer, conjecture (G+k) at k=2, Qwen3.8-Max

Source: https://chat.qwen.ai/c/762d6bb5-b0aa-481d-b501-ed4fc7e3b7c0
Dispatched 08-18 16:11 CDT (owner-intel round 10); harvested 08-18 ~17:5x CDT (owner-intel
round 13). Completion confirmed via action-icon row (copy/thumbs-up/down/share/regenerate)
present under the final message, static page-text length across two checks 8s apart, and idle
composer.

Brief: `prompts/w133_r8_Gplusk_qwen.md`. Target: `C4`-free connected `G` with `l(G) > 4` ⟹
`path(G) >= rad(G) + 4` (conjecture (G+k), k=2), with `F8`(=Theorem G+, the `k=1` case
`l>3 ⟹ path>=rad+3`) as the proved base tool and `F9` (a large-radius corollary of G+'s proof
machinery) as the other given tool.

**VERDICT: OBSTRUCTION-IDENTIFIED** (not proved, not refuted — a precise open obstruction is
named)

5-line summary (verbatim from model):
1. Did not prove the full statement; reduced the natural proof to one missing lemma: a long
   geodesic with an F9-trigger side vertex of `a >= 4`.
2. Proved the easy large-radius case `mu>=4, rad>=5` directly from F9, and the radius-1 case
   directly.
3. The exact breakdown of the F8/F9 induction is a "3-cap": every long endpoint's usable
   side-neighbourhood has only vertices with `a <= 3`, so F9 cannot supply the fourth extra
   vertex.
4. Gives an explicit local 3-cap skeleton graph and an explicit genuine `l>4` control graph
   (the STS(15) incidence graph) satisfying the target; no counterexample found.
5. Remaining problem: prove a 3-capped periphery is incompatible with the mass identity
   `Sum_{a>=4}(a-3) > n` (and settle radii 2, 3, 4).

## What was proved

**Mass identities** (derived from `l>4 ⟹ A(G) = Sum_v a(v) = n*l(G) > 4n`, using non-hubs have
`a<=2` resp. `a<=3`):
- **(M3)**: `Sum_{h: a(h)>=3} (a(h)-2) > 2n`
- **(M4)**: `Sum_{x: a(x)>=4} (a(x)-3) > n`

**Radius 0 and 1**: trivial (`l<2` for rad<=1 by a direct C4-free neighbourhood-matching
argument), so no radius-1 graph has `l>4`.

**`mu(G)>=4, rad(G)>=5 ⟹ path>=rad+4`**: this is exactly given fact F9's stated corollary
(not new).

## The named obstruction — "3-capped periphery"

The natural induction: assume a counterexample has `path(G) = rad(G)+3` (forced by F8 once
`l>4⟹l>3`), take a diametral geodesic `u0...ud` with `d>=rad`, and try to invoke F9 (needs
`a(u0)>=3`, `a(ud)>=2`, and a side-neighbour `x` of `u0` outside `u1`'s matching-component in
`N(u0)` with `a(x)>=4`) to force `path>=d+4`, contradiction. Obstruction: because `C4`-free
forces `N(u0)` to induce a matching-plus-isolates, the "usable side set"
`S(u0,u1) = N(u0) \ (matching-component of u1)` can consist entirely of vertices with `a<=3`
("3-capped along u1"). Definition of **3-capped periphery**: every sufficiently long geodesic
endpoint is either low-`a` or 3-capped along its direction. If a graph has a 3-capped
periphery, the natural F9 induction never fires. Model states: mass (M4) proves many
`a>=4` vertices exist globally, but does NOT force one into a usable side-position — a vertex
`u0` can have large `a(u0)` itself via many independent small-`a` side-neighbours (exhibited
by an explicit local skeleton graph, `l<2` there so it's only a local, not global,
demonstration).

**Four attacks tried, all obstructed** (deletion/induction — no safe monotone parameter;
mass/hub charging — mass doesn't localize to usable side positions; local structure around a
diametral geodesic — this IS the 3-cap definition, still open; explicit counterexample search
— circulants excluded by given negative result, friendship graphs have small `l`, high-degree
incidence graphs like STS(15) have large `l` AND long paths, i.e. satisfy the target rather
than refute it).

## Control-case section (T12+amendments, mandatory)

**Control A — Petersen graph**: explicit 2-subset-of-{1..5} model, edge list given, `l=3`
(hypothesis `l>4` fails), `rad=diam=2`, `path=5=rad+3`. F9 does not execute (`mu=3<4`,
`rad=2<5`). Full per-fact counterfactual-availability table given (F1/F5/F6/F7/F8/F9).

**Control B — STS(15) point-block incidence graph** (genuine `l>4` positive control): 50
vertices (15 points + 35 blocks of the Steiner triple system = lines of PG(3,2)), explicit
block list given, proved `C4`-free (STS pairwise-intersection properties), `a(P_i)=7`,
`a(B_j)=3`, `l = 210/50 = 4.2 > 4`, `rad=3` (points ecc 3, some blocks ecc 4), and an explicit
induced path on 9 vertices exhibited (`path>=9 > 7 = rad+4`) — so the target inequality holds
comfortably on this genuine positive instance; not a counterexample. F9 does not execute here
either (`mu=3`, `rad=3<5`, diam=4 so no length-5 geodesic) — flagged as the fact whose absence
here is exactly why small/medium radii need separate handling.

## Self-audit (verbatim-derived, condensed)

**Not proved**: the central "3-capped periphery is impossible under `l>4`,`rad>=5`" claim;
radii 2/3/4 entirely open; exact induced-path number of STS(15) not computed (only `>=9`
shown via one witness path).

**Hypothesis usage table** given per fact (C4-free, connected, finite/simple, l>4, F8, F9 all
used; F7/F5 only touched in counterexample search/control checks, not load-bearing; F6 not
essential — stronger mass identities derived directly).

## Assessment for owner-w133

No proof, no counterexample. The value here is the sharply-named "3-capped periphery"
obstruction plus a genuine `l>4` control instance (STS(15)) that owner-w133 did not
previously have on file — worth adding to the fact base regardless of how (G+k) resolves.
Everything UNVERIFIED — owner-w133 re-verifies by hand before adoption; adversarial review of
anything adopted goes to a NON-Qwen judge.
