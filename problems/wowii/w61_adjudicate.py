#!/usr/bin/env python3
"""
WOWII-61 round 3 (owner-w61): ADJUDICATION of the Qwen S3 round-2 findings
against the Spark round-1 CLEAN verdicts.  Every numeric claim made by either
reviewer is reproduced here from scratch.

Claims under adjudication
  Q-N2   Corollary N2 (draft 7.2 B) is FALSE as an unconditional statement;
         K_{2,3} is a counterexample.                       [Qwen, Theorem N]
  Q-U    Lemma U's 2nd hypothesis (Delta >= #{3s in R}) FAILS on the control
         sequence [3,3,3,3,3,2,1]; misapplying it gives m <= 7 vs true m = 9.
                                                            [Qwen, Theorem T3]
  Q-U-ok Lemma U's 2nd hypothesis DOES hold at the two real application sites
         (k=1,e_B=1 with p=2 ; k=1,e_B=0 with p<=2).        [Qwen, Theorem T3]
  Q-J5   The draft's exclusion "p>=3 => deg(y)>3" is false; witness has degree
         sequence [4,3,3,3,3,3,1].                          [Qwen, Theorem T3]
  Q-J2   The k=3 step "z is not decremented at step 2" is not forced by the
         structure; witness degree sequence [4,4,4,3,3,1,1].[Qwen, Theorem T3]
  Q-NV   Theorem N's hypotheses are non-vacuous: K_{3,4} with A the size-4 part.
                                                            [Qwen, Theorem N]
"""

def residue_steps(degs):
    """literal residueAux: returns (heads, s, residue)."""
    ent = sorted(degs, reverse=True)
    heads = []
    while ent and ent[0] > 0:
        d = ent[0]
        heads.append(d)
        rest = ent[1:]
        for k in range(min(d, len(rest))):
            rest[k] = max(rest[k] - 1, 0)
        ent = sorted(rest, reverse=True)
    return heads, len(heads), len(degs) - len(heads)


def show(tag, ok, detail):
    print(f"[{'CONFIRMED' if ok else 'REFUTED  '}] {tag}: {detail}")


print("=" * 78)
print("Q-N2 : Corollary N2 unqualified, K_{2,3} counterexample")
degs = [3, 3, 2, 2, 2]                      # K_{2,3}: B = size-2 part
heads, s, res = residue_steps(degs)
n, m, al, tau, eB, Delta = 5, 6, 3, 2, 0, 3
bound = Delta + tau * (tau + 1) // 2 - 1
print(f"   K_2,3  degs={degs} n={n} m={m} alpha={al} tau={tau} e_B={eB} "
      f"Delta={Delta}")
print(f"   HH heads={heads}  s={s}  residue={res}   (reductio needs s=tau={tau})")
print(f"   Corollary N2 bound = Delta + tau(tau+1)/2 - 1 = {bound}   m = {m}")
show("Q-N2", m > bound and s != tau,
     f"m={m} > bound={bound}, and the reductio fails here (s={s} != tau={tau}), "
     f"so N2 needs the residue=alpha hypothesis stated explicitly")
show("Q-N2-hyp(i)", min(degs[:2]) >= tau + 1,
     f"K_2,3 does satisfy hypothesis (i): B-degrees {degs[:2]} >= tau+1={tau+1}")

print("=" * 78)
print("Q-U : Lemma U second hypothesis on the control sequence [3,3,3,3,3,2,1]")
d = [3, 3, 3, 3, 3, 2, 1]
heads, s, res = residue_steps(d)
Delta = max(d)
R = sorted(d, reverse=True)[1:]
three = sum(1 for v in R if v == 3)
m = sum(d) // 2
print(f"   degs={d}  m={m}  Delta={Delta}  R={R}  #(entries of R equal 3)={three}")
print(f"   HH heads={heads} s={s} residue={res}")
show("Q-U", Delta < three,
     f"Delta={Delta} < #3s={three}, so Lemma U's 2nd hypothesis FAILS here")
show("Q-U-slack", Delta + 4 < m,
     f"misapplying Lemma U would give m <= Delta+4 = {Delta + 4} vs true m={m} "
     f"(slack {m - (Delta + 4)}, i.e. the forbidden slack>=2 behaviour)")
print(f"   NOTE: max(R)={max(R)} <= 3, so the FIRST hypothesis does hold -- it is "
      f"exactly the second one the blanket sentence omits.")
print(f"   k for this instance = #(b in B with deg>=4) = 0, so the draft's own "
      f"k=0 branch applies and it does NOT invoke Lemma U there.")

print("=" * 78)
print("Q-U-ok : does the 2nd hypothesis hold at the two REAL application sites?")
# site 1: k=1, e_B=1 -> C2 gives Y=Z=3 ; classification (II) gives p=2
# R = d(G) minus Delta=X ; entries equal to 3 in R are y, z and the p universal
#     A-vertices  -> 2+p
for (siteName, p, X) in [("k=1,e_B=1 (p=2)", 2, 4), ("k=1,e_B=1 (p=2), X=9", 2, 9),
                         ("k=1,e_B=0 (p=1)", 1, 4), ("k=1,e_B=0 (p=2)", 2, 4),
                         ("k=1,e_B=0 (p=2), X=17", 2, 17)]:
    three = 2 + p
    show(f"Q-U-ok {siteName}", X >= three,
         f"#3s in R = 2+p = {three} <= Delta = X = {X}  -> Lemma U legitimately "
         f"applies")

print("=" * 78)
print("Q-J5 : the exclusion 'p>=3 => deg(y)>3' in k=1,e_B=0")
# B = {x,y,z} independent ; p universal A-vertices ; n_x singletons at x
p, n_x = 3, 1
degx, degy, degz = p + n_x, p, p
d = sorted([degx, degy, degz] + [3] * p + [1] * n_x, reverse=True)
print(f"   p={p} n_x={n_x} -> B-degrees (x,y,z)=({degx},{degy},{degz}) ; "
      f"full degree sequence {d}")
k = sum(1 for v in (degx, degy, degz) if v >= 4)
show("Q-J5", degy == 3 and k == 1,
     f"deg(y)={degy} is NOT > 3 although p={p}>=3, and k={k} -- the draft's "
     f"stated reason fails exactly at p=3")
print("   (the configuration is still impossible, but by (F-b): the only occurring "
      "types are {x,y,z} and {x}, which are not disjoint -> diam != 4)")

print("=" * 78)
print("Q-J2 : k=3 witness that the structure alone does not force 'z undecremented'")
d = [4, 4, 4, 3, 3, 1, 1]
heads, s, res = residue_steps(d)
m = sum(d) // 2
print(f"   degs={d} m={m} HH heads={heads} s={s} residue={res}")
# replay step 1 and step 2 explicitly
ent = sorted(d, reverse=True)
rest = ent[1:]
for i in range(min(ent[0], len(rest))):
    rest[i] = max(rest[i] - 1, 0)
L1 = sorted(rest, reverse=True)
rest2 = L1[1:]
for i in range(min(L1[0], len(rest2))):
    rest2[i] = max(rest2[i] - 1, 0)
L2 = sorted(rest2, reverse=True)
print(f"   L1={L1}   L2={L2}")
show("Q-J2-reductio", sum(heads[:3]) != m,
     f"sum of first 3 heads = {sum(heads[:3])} != m = {m}, so this witness does "
     f"NOT satisfy the reductio -- Qwen states this itself; it only shows the "
     f"local HH inference is not structurally forced")

print("=" * 78)
print("Q-NV : non-vacuity of Theorem N's hypotheses, K_{3,4}")
d = [4, 4, 4, 3, 3, 3, 3]                    # K_{3,4}: B = size-3 part
heads, s, res = residue_steps(d)
al, tau, eB = 4, 3, 0
print(f"   K_3,4 degs={d} alpha={al} tau={tau} e_B={eB} m={sum(d)//2}")
print(f"   HH heads={heads} s={s} residue={res}")
show("Q-NV", min(d[:3]) >= tau + 1 and eB <= tau - 2 and min(d[:3]) >= 2 * eB + 3,
     f"(i) {min(d[:3])}>={tau+1} ; (ii) {eB}<={tau-2} ; (iii) {min(d[:3])}>="
     f"{2*eB+3}  -- all three hold, hypotheses non-vacuous")
show("Q-NV-conclusion", res <= al - 1,
     f"and Theorem N's conclusion holds: residue={res} <= alpha-1={al-1}")
print("=" * 78)
