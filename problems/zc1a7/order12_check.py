"""order12_check.py -- ROUND 2 falsification test #3.
The paper states that HeLP alone shows V(ZA_7) contains NO element of order 12
(and that this needs Prop 2.7(iii), which Salim 2011 did not use).  Re-run it
with the complete 5- and 7-modular tables."""
from help_full import (load_ordinary, load_brauer, characters_for_order,
                       solve_order)

names, degrees, otab = load_ordinary()
btab = load_brauer()
ch12 = characters_for_order(12, names, degrees, otab, btab)
ch6 = characters_for_order(6, names, degrees, otab, btab)
ch4 = characters_for_order(4, names, degrees, otab, btab)
print("characters usable for order 12 (p must not divide 12 => p in {5,7}): %d"
      % len(ch12))

s4, _ = solve_order(4, {2: {'2a': 1}}, ch4)
print("order-4 solutions for u^3 : %s" % [ (s['2a'], s['4a']) for s in s4 ])

total = 0
found = []
for cube in ('3a', '3b'):
    s6, al6 = solve_order(6, {2: {cube: 1}, 3: {'2a': 1}}, ch6)
    for v6 in s6:
        for v4 in s4:
            pa = {2: v6, 3: v4, 4: {cube: 1}, 6: {'2a': 1}}
            sols, al = solve_order(12, pa, ch12)
            total += 1
            for s in sols:
                found.append((cube, tuple(v6[c] for c in al6),
                              (v4['2a'], v4['4a']), tuple(s[c] for c in al)))
print("branches examined (choice of u^2, u^3, u^4): %d" % total)
print("order-12 HeLP solutions found: %d  %s" % (len(found), found))
print("paper: 'elements of order 12 do not exist in V(ZG)'  ->  %s"
      % ("REPRODUCED" if not found else "*** MISMATCH ***"))
