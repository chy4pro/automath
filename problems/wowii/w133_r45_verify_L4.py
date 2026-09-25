#!/usr/bin/env python3
"""STANDALONE re-verification of round 45's L4 (anchor-free) certificates.  PROTOCOL 105.

Shares NO code with the builder `w133_r45_ladder.py`.  It reads two data files and nothing
else:
    problems/wowii/w133_r44_W44a.txt      (round 44's W44a edge list)
    problems/wowii/w133_r43_W43a.txt      (and W43b, W43c)
    problems/wowii/w133_r45_L4certs.txt   (one certificate per host)

and re-derives every quantity by a DIFFERENT algorithm from the builder's:
  * distances by BITSET frontier relaxation on integer masks (the builder uses a deque BFS);
  * a(v) = alpha(G[N(v)]) by a RECURSIVE branch-and-bound maximum independent set (the
    builder uses the C4-free identity a = deg - (matching edges));
  * C4-freeness by a from-scratch pair-count over common-neighbour masks;
  * the certificate re-checked edge by edge AND non-edge by non-edge.

WHAT IS BEING CERTIFIED.  For each host H and its certificate P:
    P is an induced path of H on diam(H)+4 vertices whose first vertex v has
    ecc_H(v) = diam(H).
Hence path(H) >= diam(H)+4.  For EVERY condition-4 vertex w of H (ecc_H(w) = rad(H)+1 and
d(c,w) = rad(H) for every centre c), the route A2 instance G := H + one pendant at w has
rad(G) = rad(H)+1 by (RAD-1P), floor(l(G)) = 4, and target rad(G)+floor(l(G)) = rad(H)+5 =
diam(H)+4 at offset +1.  Since H is an induced subgraph of G, path(G) >= path(H) >= the
certificate's length >= the target.  ONE certificate discharges EVERY condition-4 vertex of
its host -- which is exactly what an ANCHOR-FREE lane buys and what round 44's L3 could not
do.

Interpreter: system python3 (pure stdlib).  Exit 0 iff every check passes.
"""
import sys

NCHK = 0
NBAD = 0


def chk(cond, msg):
    global NCHK, NBAD
    NCHK += 1
    if not cond:
        NBAD += 1
        print("FAIL: %s" % msg)


def read_graph(path):
    n = None
    es = []
    fh = open(path)
    for ln in fh:
        ln = ln.strip()
        if ln == "" or ln[0] == "#":
            continue
        f = ln.split()
        if len(f) == 1:
            n = int(f[0])
        elif len(f) == 2:
            es.append((int(f[0]), int(f[1])))
    fh.close()
    nb = [0] * n
    m = 0
    for (u, v) in es:
        if u == v:
            continue
        if not (nb[u] >> v) & 1:
            m += 1
        nb[u] |= (1 << v)
        nb[v] |= (1 << u)
    return n, nb, m


def dist_row(n, nb, s):
    """distances from s by BITSET frontier relaxation."""
    d = [-1] * n
    d[s] = 0
    seen = 1 << s
    front = 1 << s
    k = 0
    while front:
        nxt = 0
        f = front
        while f:
            b = f & (-f)
            u = b.bit_length() - 1
            f ^= b
            nxt |= nb[u]
        nxt &= ~seen
        k += 1
        seen |= nxt
        g = nxt
        while g:
            b = g & (-g)
            g ^= b
            d[b.bit_length() - 1] = k
        front = nxt
    return d


def alpha_mask(nb, mask):
    """maximum independent set inside `mask`, recursive branch and bound."""
    if mask == 0:
        return 0
    b = mask & (-mask)
    v = b.bit_length() - 1
    rest = mask ^ b
    take = 1 + alpha_mask(nb, rest & ~nb[v])
    skip = alpha_mask(nb, rest)
    return take if take > skip else skip


def c4_free(n, nb):
    for u in range(n):
        for v in range(u + 1, n):
            c = nb[u] & nb[v]
            if c and (c & (c - 1)):
                return False, (u, v)
    return True, None


def is_induced_path(n, nb, P):
    if len(set(P)) != len(P):
        return False
    for i in range(len(P) - 1):
        if not (nb[P[i]] >> P[i + 1]) & 1:
            return False
    for i in range(len(P)):
        for j in range(i + 2, len(P)):
            if (nb[P[i]] >> P[j]) & 1:
                return False
    return True


def main():
    certs = {}
    fh = open("problems/wowii/w133_r45_L4certs.txt")
    for ln in fh:
        ln = ln.strip()
        if ln == "" or ln[0] == "#":
            continue
        f = ln.split()
        certs[f[0]] = (int(f[1]), [int(x) for x in f[2:]])
    fh.close()
    print("STANDALONE re-verification of round 45's L4 certificates (105)")
    print("interpreter: system python3 %s (pure stdlib)" % sys.version.split()[0])
    print("certificates read: %s" % ", ".join(sorted(certs)))
    chk(len(certs) > 0, "at least one certificate was read")

    files = {"W43a": "problems/wowii/w133_r43_W43a.txt",
             "W43b": "problems/wowii/w133_r43_W43b.txt",
             "W43c": "problems/wowii/w133_r43_W43c.txt",
             "W44a": "problems/wowii/w133_r44_W44a.txt"}
    for tag in sorted(certs):
        if tag not in files:
            print("  %s: no edge list known here -- SKIPPED, and said so" % tag)
            continue
        n, nb, m = read_graph(files[tag])
        anchor, P = certs[tag]

        ok, wit = c4_free(n, nb)
        chk(ok, "%s is C4-free (witness %s)" % (tag, wit))
        D = [dist_row(n, nb, v) for v in range(n)]
        chk(all(min(row) >= 0 and -1 not in row for row in D), "%s is connected" % tag)
        ecc = [max(row) for row in D]
        rad = min(ecc)
        diam = max(ecc)
        ctr = [v for v in range(n) if ecc[v] == rad]
        a = [alpha_mask(nb, nb[v]) for v in range(n)]
        mu = min(a)
        lH = sum(a) / float(n)
        print("  %-5s n=%d |E|=%d rad=%d diam=%d |Ctr|=%d mu=%d l(H)=%.6f"
              % (tag, n, m, rad, diam, len(ctr), mu, lH))
        chk(diam == rad + 1, "%s is at offset +1 (diam = rad+1)" % tag)
        chk(mu >= 2, "%s has mu >= 2" % tag)

        # --- the certificate
        chk(P[0] == anchor, "%s certificate is anchored at the declared vertex" % tag)
        chk(ecc[anchor] == diam, "%s certificate's anchor is a DIAMETRAL vertex" % tag)
        chk(is_induced_path(n, nb, P), "%s certificate is an INDUCED path of H" % tag)
        chk(len(P) == diam + 4, "%s certificate has diam+4 = %d vertices (it has %d)"
            % (tag, diam + 4, len(P)))

        # --- every condition-4 vertex, and the target it needs
        cond4 = [w for w in range(n)
                 if ecc[w] == rad + 1 and all(D[c][w] == rad for c in ctr)]
        chk(len(cond4) > 0, "%s carries at least one condition-4 vertex" % tag)
        nrow = 0
        for w in cond4:
            # G := H + one pendant p at w, p = n
            aG = list(a)
            aG[w] = a[w] + 1
            sumG = sum(aG) + 1              # the pendant has a = 1
            lG = sumG / float(n + 1)
            kG = int(lG)
            # rad(G): ecc_G(c) = max(ecc_H(c), d(c,w)+1) for c in V(H); ecc_G(p)=ecc_H(w)+1
            eccG = [max(ecc[v], D[v][w] + 1) for v in range(n)] + [ecc[w] + 1]
            radG = min(eccG)
            chk(radG == rad + 1, "%s w=%d: rad(G) = rad(H)+1" % (tag, w))
            chk(kG == 4, "%s w=%d: floor(l(G)) = 4 (it is %.6f)" % (tag, w, lG))
            need = radG + kG
            chk(len(P) >= need,
                "%s w=%d: the ONE anchor-free certificate (%d vertices) already meets the "
                "target %d" % (tag, w, len(P), need))
            nrow += 1
        print("        condition-4 vertices: %d; ONE certificate of %d vertices discharges "
              "ALL of them (target %d)." % (nrow, len(P), rad + 1 + 4))

    print("CHECKS %d   FAILS %d" % (NCHK, NBAD))
    return 1 if NBAD else 0


if __name__ == "__main__":
    sys.exit(main())
