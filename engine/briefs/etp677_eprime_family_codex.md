# CODEX TICKET (exhaustive parametric search; engineering, any tier — no claims about the
# conjecture, only verified tables) — enumerate the SWITCHING-TYPE family of finite E677
# magmas and profile X_6 against Im(U).
# Repo: $HOME/workspace/claudecode/automath. Python 3 (numpy ok). Local caps: each
# script ≤ 600 s per parameter block, ≤ 2 heavy processes. DONE marker: DONE-EPRIME.

## Background (all verified facts)
E677: x = y*(x*((y*x)*y)); E255: ((xx)x)x = x. For a magma with bijective left translations,
W(x) = x\x, U(x) = (xx)x, P(x) = x\U(x), F(x) = x\P(x). For a: u = U(a), p = P(a), b = F(a),
d = bb, v = db, c = W(b), w = W(a); X_6(a) :⟺ v≠w ∧ v≠u ∧ c≠a ∧ c≠w ∧ c≠u ∧ c≠p.
Known idempotent-free E677+E255 magmas of the form F7 × F_p:
  (q,s)*(r,t) = (αq + βr, γ s + δ t + κ(q,r))  with (α,β) ∈ {(4,1), (4,3)}, p = 31,
  (γ,δ) = (5,−4), κ(q,r) = 1 if q = r = 0 else κ₀ ∈ {0, 2}.
  κ₀ = 2, (4,1): X_6 everywhere.  κ₀ = 0, (4,1): X_6 fails (v = u, c = p) at all q ≠ 0.
  κ₀ = 0, (4,3): U is a bijection, X_6 fails (c = u) at all q ≠ 0, holds at q = 0.
OPEN QUESTION (E'): does every finite idempotent-free E677+E255 magma have a point of Im(U)
satisfying X_6? All known examples do (the hub q = 0 always works). We want a member of a
broad family where X_6 fails at EVERY point of Im(U) — or the exhaustive statement that none
exists in the family.

## The family to enumerate (exhaustively; report counts, not impressions)
Base: any E677 magma on F7 of the form αq + βr + γ₀ (enumerate all (α,β,γ₀) ∈ F7³ satisfying
E677 by direct check; you will find the two affine types and their translates). Fibre: F_p for
p ∈ {7, 13, 31} (also p = 5 as a control). Law:
  (q,s)*(r,t) = (αq + βr + γ₀,  γ(q,r)·s + δ(q,r)·t + κ(q,r))
where (γ,δ,κ) : F7 × F7 → F_p³ may depend on the PAIR (q,r) — but restrict to laws that are
constant on the orbits of a chosen structure to keep the space finite and meaningful:
  (F1) (γ,δ) constant, κ arbitrary function of (q,r)  [p^{49} is too big: restrict κ to depend
       on the first coordinate of the PRODUCT class αq+βr+γ₀ and on whether q = r = 0, i.e.
       κ = κ₁(αq+βr+γ₀) + κ₂·[q=r=0]: p^8 laws];
  (F2) (γ,δ) depending on [q=r=0] only (two affine fibre laws, hub vs off-hub), κ as in (F1);
  (F3) (γ,δ,κ) depending on the product class αq+βr+γ₀ only (7 affine laws): p^{21}, prune by
       requiring each fibre law to be E677-affine on its own (γδ(1+δ²) = 1, γ + γ²δ² + δ³ = 0)
       first, then enumerate constants.
For every law: check E677 on all pairs (49p² instances), E255, idempotents, bijectivity of
left translations; for the E677+E255 idempotent-free survivors compute Im(U), the U-cycle
structure, the set of X_6 points, which of the six conditions fail where, and whether
Im(U) ∩ X_6 = ∅. Print a table per (α,β,p, family) with counts and ALL laws achieving
Im(U) ∩ X_6 = ∅ (if any) as explicit formulas; save every idempotent-free survivor to
problems/etp677/eprime/survivors_p{p}.json (law + 3 profile numbers).
Controls (mandatory, in the report): the three known laws above must be found with the
stated profiles; the F31 affine law alone (p = 31, base trivial) must show X_6 everywhere.

## Deliverables
problems/etp677/eprime/{enum_family.py, profile.py, survivors_*.json, report tables} and
engine/out/codex/etp677_eprime_report.md ending with DONE-EPRIME. No conjectural language:
tables + explicit witnesses only.
