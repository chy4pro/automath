# CODEX TICKET (math + ATP tooling; sol tier) — a HUMAN-READABLE proof that the gauge-free
# Core-7 pattern has no fibre-3 solution (registry R46 STEP 49), i.e. the clean-tier route.
# Repo: $HOME/workspace/claudecode/automath. Read problems/etp677/simple/fibre_core/
# core7_free.py (symbols, the 14 products, the seven instances, chain semantics) and STEP 49
# (grep "STEP 49" in problems/etp677/campaign_registry.md). kissat: tools/kissat/build/kissat;
# CP-SAT: engine/venv_item3/bin/python; prover9/E under tools/. Local caps ≤ 600 s.
# DONE marker: DONE-CORE7HAND.

## The object
Unknowns: for each of the 14 ordered pairs P = (x,y) among the eight symbols a,w,u,p,b,d,v,c and
each s ∈ {0,1,2}, a permutation σ_P(s) ∈ Sym(3). Constraints: the seven lifted E677 chains
(x,y) ∈ {(p,a),(v,d),(c,b),(a,u),(b,v),(b,a),(b,b)}: for all s,t ∈ {0,1,2},
   σ_{y,x((yx)y)}(t) ( σ_{x,(yx)y}(s) ( σ_{yx,y}( σ_{y,x}(t)(s) )(t) ) ) = s,
with the base products yx, (yx)y, x((yx)y) read from the 14-entry table (all instances close
inside it). Facts: UNSAT for m = 3 (kissat + drat-trim; CP-SAT; the dialogue's independent
encoding under three solvers); the seven instances are a MINIMAL core (dropping any one makes
it SAT); for m = 2 the same system is UNSAT and the fibre-2 proof is linear over F2.

## Tasks
1. Structure first: for each instance write the chain as a relation between four
   permutation-valued maps; identify the "diagonal" instances ((a,u): products ua=a, au=w,
   aw=a, ua=a; (b,b): bb=d, db=v, bv=c, bc=b; (b,v): vb=b, bv=c, bc=b, vb=b) and derive forced
   facts (e.g. from (a,u) with s = t: what does σ_{u,a}(t) ∘ … force? fixed points? cycle
   types?). Use the solver as an oracle: add candidate lemmas as unit clauses/negations and
   test whether they are IMPLIED (negation UNSAT) — collect a list of implied facts
   (e.g. "σ_{u,a}(s) = id for all s", "σ_{a,w}(s) has a fixed point", …) each with a DRAT.
2. Assemble a proof by cases over the implied facts, aiming at a contradiction in a few
   pages; every step must be either a direct algebraic consequence of one chain equation or
   a finite case split whose exhaustiveness you verify by a tiny script. Label the final
   status PROVED (with the written proof) or PARTIAL (with the exact residual: which implied
   facts you could not turn into hand steps).
3. If PROVED: sketch how to formalise it in Lean without bv_decide (a sequence of `decide`s on
   Sym(3)-valued statements with ≤ 6³ cases each is acceptable) — no Lean coding required.
## Deliverables
problems/etp677/simple/fibre_core/handproof/ (lemma list with DRATs, scripts) and
engine/out/codex/etp677_core7_handproof_report.md ending with DONE-CORE7HAND.
