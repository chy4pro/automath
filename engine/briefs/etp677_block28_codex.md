# CODEX TICKET (ATP engineering; any tier — output is machine proofs, no conjectural claims) —
# prove the 28 unproved entries of the R46 "window block" with first-order provers.
# Repo: $HOME/workspace/claudecode/automath. Provers: tools/E/PROVER/eprover,
# tools/ladr_build/LADR-2009-11A/bin/prover9 (+ mace4). You may build Vampire or Twee under
# tools/ (self-contained, no system installs) if it helps. Local caps: ≤ 600 s per prover run,
# ≤ 2 heavy processes, run sequentially or 2 in parallel. DONE marker: DONE-BLOCK28.

## Axioms (TPTP; use exactly these, plus the lemma cascade below)
fof(e677, axiom, ![X,Y]: m(Y, m(X, m(m(Y,X),Y))) = X).
fof(ld1, axiom, ![X,Y]: m(X, ld(X,Y)) = Y).
fof(ld2, axiom, ![X,Y]: ld(X, m(X,Y)) = Y).
fof(e255, axiom, ![X]: m(m(m(X,X),X),X) = X).
fof(defs, axiom, (w = ld(a,a) & u = ld(a,w) & p = ld(a,u) & b = ld(a,p) & d = m(b,b)
                  & e = ld(p,p) & m(d,b) = u & ld(b,b) = p)).          % the window: v = u, c = p
Finiteness-only facts, allowed as EXTRA axioms but every proof using them must be labelled
"(fin)": fof(fh, axiom, ![X]: f(h(X)) = X). fof(hf, axiom, ![X]: h(f(X)) = X). with
fof(fdef, axiom, ![X]: f(X) = ld(X, ld(X, ld(X, ld(X,X))))). fof(hdef, axiom, ![X]: h(X) =
m(m(X,X), ld(X, ld(X,X)))). Also allowed (PROVED, pure FO): fof(la, axiom, ![U,X]: (m(U,X) = X
=> (m(X,U) = ld(X,X) & ld(X, ld(X,X)) = U))). fof(wsu, axiom, ![X]: m(ld(X,X), m(X,X)) =
ld(X, ld(X,X))).

## The block (row s, column t ↦ s*t); 20 entries already PROVED — reuse them as axioms
              a  w  u  p  b  d  e
        a  |  e  a  w  u  p  b  d
        w  |  p  b  d  e  a  w  u
        u  |  a  w  ?  p  b  d  e
        p  |  b  d  e  a  w  u  p
        b  |  w  u  p  b  d  e  a
        d  |  d  e  a  w  u  p  b
        e  |  u  p  b  d  e  a  w
PROVED (FO, E and prover9 120 s): aw au ap ab ad ua ub up pa pp pd pe pu bb bp bu db ea wa;
PROVED (fin): du. TARGET: the other 28 (aa=e, ae=d, ww=b, wu=d, wp=e, wb=a, wd=w, we=u, uw=w,
ud=d, ue=e, pw=d, pb=w, bw=u, ba=w, bd=e, be=a, da=d, dw=e, dp=w, dd=p, de=b, ep=d, eb=e,
ed=a, ee=w, ew=p, eu=b). All hold in every finite model (0/864 window instances) — they are
either FO consequences that E/prover9 miss in 300 s, or need (fin), or need a cycle argument
(the L_a-cycle through a is a, e, d, b, p, u, w of length exactly 7 in every model: a*a = e,
a*e = d, a*d = b, a*b = p, a*p = u, a*u = w, a*w = a — the entries a*a = e and a*e = d are
exactly "the cycle closes at length 7"; if these two resist, add the cycle-length-7 fact as an
extra labelled axiom "(cyc7)" and see what follows).
## Tasks
1. Lemma cascade: iterate — prove what you can (E --auto-schedule, prover9 with hints /
   max_weight tuning, Vampire if built), add each proved entry as an axiom, repeat until no
   progress; then repeat with (fin); then with (cyc7). Keep every proof (TSTP / prover9 proof
   text) under problems/etp677/simple/window/atp/.
2. mace4 / a finite-model finder (domain ≤ 12) on each REMAINING entry negated: a
   counter-model would show the entry is not a consequence of the axioms used (report it —
   that is a valuable fact, not a failure).
3. Report table: entry → status (FO / fin / cyc7 / open) → prover → time → proof file.
## Deliverables
problems/etp677/simple/window/atp/ (inputs, proofs, driver script) and
engine/out/codex/etp677_block28_report.md ending with DONE-BLOCK28.
