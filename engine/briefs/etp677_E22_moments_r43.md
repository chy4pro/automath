# TASK E22 — independent re-derivation of two moment identities in finite projective planes

You are given a self-contained finite-geometry task. Work only from what is stated here.
Deliver mathematics and a runnable script; do NOT ask questions back.

## Setting (axioms you may use)
A projective plane of order q: n = q^2+q+1 points, n lines, every line has q+1 points,
every point is on q+1 lines, any two distinct points lie on exactly one common line,
any two distinct lines meet in exactly one point. S is an arbitrary set of points,
|S| = m. For each line c define k_c := |S ∩ c|.

## Deliverables
1. PROOFS, from the axioms alone, of the two identities:
   (I1)  Σ_c k_c = (q+1)·m
   (I2)  Σ_c C(k_c, 2) = C(m, 2)        [C = binomial coefficient]
   State precisely why both right-hand sides depend on |S| ALONE (not on the
   configuration of S).
2. THE REQUIRED NEGATIVE CONTROL (mandatory; an answer without it is incomplete):
   show that the third moment Σ_c C(k_c, 3) is NOT determined by |S| alone.
   Give explicit point sets in a plane of your choice (state the plane and the sets)
   with the SAME size and DIFFERENT third moments, and compute both values.
3. The line-vs-arc separation: for |S| = q+1, compute Σ_c C(k_c,3) when S is a line
   and when S is a (q+1)-arc (no 3 collinear), and verify the two values are
   C(q+1,3) and 0 respectively, with a proof.
4. A SELF-CONTAINED python3 script (stdlib only) that constructs PG(2,q) for
   q = 2, 3, 4, verifies (I1) and (I2) over a stated family of subsets, and
   demonstrates the negative control numerically (print the distinct third-moment
   values it finds for fixed |S|). Print every population you enumerate.

## Output format
Plain markdown. Sections: PROOF-I1, PROOF-I2, WHY-|S|-ONLY, NEGATIVE-CONTROL,
LINE-VS-ARC, SCRIPT (one fenced python block), LIMITS (anything you did not prove).
Hard cap 2500 words outside the script.
