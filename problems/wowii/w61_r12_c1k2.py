#!/usr/bin/env python3
"""owner-w61 round 12 - numerical backing for Lemma C1-A' and Theorem C1-2 (draft 7.25 d).

Claims under test (both hand-proved in the draft; this is the pre-writing check):
  V(c)      := steps([c]^{c+3})            = c + 1              for every c >= 1
  U(w,c)    := steps([w]^{w+2} + [c])      = w + 1              iff w + c is even
                                           aborts (not a step sequence) iff w + c is odd
U(w,c) is exactly s0((w,c)), the E=0 survival quantity of Theorem GFANnu at a two-part
residue.  Since a residue of Theorem GFANnu is a partition of 2*nu, w + c is always
even there, so C1 holds unconditionally for every two-part residue.
"""


def hh_steps(mult):
    s = sorted(list(mult), reverse=True)
    steps = 0
    while s and s[0] > 0:
        d = s[0]
        rest = s[1:]
        if d > len(rest):
            return None
        head, tail = rest[:d], rest[d:]
        if any(x <= 0 for x in head):
            return None
        s = sorted([x - 1 for x in head] + tail, reverse=True)
        steps += 1
    return steps


print("=== Lemma C1-A' :  V(c) = steps([c]^(c+3)) = c+1 ===")
bad = 0
for c in range(1, 80):
    v = hh_steps([c] * (c + 3))
    if v != c + 1:
        bad += 1
        print("   MISMATCH c=%d V=%s expected=%d" % (c, v, c + 1))
print("   c = 1..79 : mismatches = %d" % bad)

print()
print("=== Theorem C1-2 :  U(w,c) = w+1 iff w+c even, aborts iff w+c odd ===")
bad = n = 0
for w in range(1, 61):
    for c in range(1, w + 1):
        u = hh_steps([w] * (w + 2) + [c])
        n += 1
        if (w + c) % 2 == 0:
            if u != w + 1:
                bad += 1
                print("   MISMATCH w=%d c=%d U=%s expected=%d" % (w, c, u, w + 1))
        elif u is not None:
            bad += 1
            print("   SHOULD ABORT w=%d c=%d U=%s" % (w, c, u))
print("   %d pairs (c <= w <= 60) : mismatches = %d" % (n, bad))

print()
print("=== control: the excess is NOT lam_1 + (k-1) at k = 3 ===")
for lam in ([2, 1, 1], [3, 2, 1], [4, 3, 1], [2, 2, 2]):
    w = lam[0]
    print("   lam=%s  lam_1=%d  k=%d  s0=%s  excess=%s"
          % (lam, w, len(lam), hh_steps([w] * (w + 1) + lam),
             (hh_steps([w] * (w + 1) + lam) or 0) - w))
print("done")
