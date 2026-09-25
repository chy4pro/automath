#!/usr/bin/env python3
"""owner-w61 r21 -- ARITHMETIC self-consistency of problems/wowii/w61_r17_heldout_key.txt.

This does NOT re-enumerate.  It checks the printed key against itself and re-derives the
one row that HAS a closed form (H2) from an independently written partition function
(Euler's pentagonal recurrence), so a corrupted or mistyped key cannot pass silently.

WHAT IT DOES NOT DO, stated so the entry is not overclaimed: H3's `791` and H4's `131`
are counts over an enumeration.  Their internal sums are checked here; the counts
themselves still rest on ONE implementation and are NOT independently re-derived.
"""
ok = True
def chk(name, got, want):
    global ok
    good = got == want
    ok &= good
    print(f"  {name:<34} {str(got):>8}  expect {str(want):>8}  {'PASS' if good else 'FAIL'}")

print("=== owner-w61 r21 -- held-out key arithmetic self-check ===\n")

terms = [7920, 11286, 11760, 13475, 12474, 12705, 10560, 8910, 6060, 3234]
split = {1:6, 2:14, 3:21, 4:35, 5:47, 6:85, 7:110, 8:155, 9:170, 10:148}
shapes = {1:7920, 2:11286, 3:11760, 4:13475, 5:12474, 6:12705, 7:10560, 8:8910, 9:6060, 10:3234}
hist = {8:5, 9:70, 10:152, 11:201, 12:185, 13:131, 14:91, 15:62, 16:41,
        17:26, 18:17, 19:10, 20:6, 21:3, 22:2}

print("[A] H2 -- the printed per-E terms must sum to the printed S(11)")
chk("sum of H2 terms", sum(terms), 98384)

print("\n[B] H3 -- the per-E split must sum to the printed survivor count")
chk("sum of H3 per-E split", sum(split.values()), 791)

print("\n[C] H3 -- the per-E SHAPES TESTED must equal S(11), term by term")
chk("sum of H3 per-E shapes", sum(shapes.values()), 98384)
chk("H3 shapes == H2 terms (per E)", [shapes[e] for e in range(1, 11)] == terms, True)

print("\n[D] H4 -- the recorded histogram must sum to p(22), and its 13-bucket to the key value")
chk("sum of H4 histogram", sum(hist.values()), 1002)
chk("H4 bucket at s0 = 13", hist[13], 131)

print("\n[E] INDEPENDENT re-derivation: p(n) by Euler's pentagonal recurrence")
p = [1] + [0] * 22
for n in range(1, 23):
    tot, k = 0, 1
    while True:
        g1 = k * (3 * k - 1) // 2
        g2 = k * (3 * k + 1) // 2
        if g1 > n and g2 > n:
            break
        s = (-1) ** (k + 1)
        if g1 <= n:
            tot += s * p[n - g1]
        if g2 <= n:
            tot += s * p[n - g2]
        k += 1
    p[n] = tot
chk("p(22)", p[22], 1002)
chk("S(11) = sum (11-E) p(E) p(22-E)",
    sum((11 - E) * p[E] * p[22 - E] for E in range(1, 11)), 98384)
for E in range(1, 11):
    chk(f"  term E={E}", (11 - E) * p[E] * p[22 - E], terms[E - 1])

print("\nKEY SELF-CHECK:", "PASS" if ok else "FAIL")
print("NOT ESTABLISHED HERE: H3 = 791 and H4 = 131 remain single-implementation counts.")
