# CODEX TICKET (Lean 4; sol tier) — decided OBJECTS: the order-217 idempotent-free E677+E255
# magmas M217ε and R217 as Lean facts. Repo: $HOME/workspace/claudecode/automath;
# project lean/etp677_ext (conventions as in Ext677Small.lean / Ext677Core7.lean, which use
# `decide` / `native_decide` on Fin-indexed tables — follow the same axiom-labelling discipline:
# every native_decide theorem is listed in AXIOMS.txt with its native axiom). 0 sorry.
# Heavy processes ≤ 2. DONE marker: DONE-LEANOBJ.

## Objects (all arithmetic in ZMod 7 × ZMod 31, or Fin 217 via q*31+s)
M217ε : (q,s)*(r,t) = (4q+r, 5s−4t+[q=0 ∧ r=0])
R217  : (q,s)*(r,t) = (4q+3r, 5s−4t+[q=0 ∧ r=0])
F31   : s*t = 5s−4t+1 on ZMod 31 (control, already used in earlier modules — reuse if present)

## Theorems (for each of M217ε, R217)
T1 E677 holds (∀ x y).            T2 E255 holds (∀ x).           T3 no idempotent.
T4 left translations bijective (Function.Bijective (op x ·)) — derive from E677 + Finite,
   or by decide.
T5 (M217ε) the point a = (1,0) is a WINDOW: with u = U a, p = P a, b = F a, d = b*b, v = d*b,
   c = W b: v = u ∧ c = p, and a*a ≠ a. Also the seven elements a, W a, u, p, b, d, a*a are
   pairwise distinct.
T6 (R217) U is a bijection, and at a = (1,0): c = u (i.e. W (F a) = U a) while a*a ≠ a;
   and at a = (0,0): the six X_6 disequalities hold (v≠w, v≠u, c≠a, c≠w, c≠u, c≠p).
Strategy: define the ops on ZMod 7 × ZMod 31; try `decide` first for T1–T3 (217² = 47089
instances of a 4-multiplication term — likely too slow for the kernel; then `native_decide`
with the axiom recorded); for the pointwise facts T5/T6 `decide`/`norm_num` on explicit
elements should work (compute the left divisions by giving the witness explicitly, e.g.
W a = (4,0) with proof `a * (4,0) = a` by decide). Prefer a kernel-checked proof for the
pointwise facts and record which of T1–T3 needed native_decide.

## Deliverables
lean/etp677_ext/Ext677Objects.lean, AXIOMS.txt appended, and
engine/out/codex/etp677_lean_objects_report.md (which theorems are kernel-checked vs
native_decide, build time) ending with DONE-LEANOBJ.
