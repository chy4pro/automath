# N7 (Zaremba campaign, Phase 0): route R4 obstruction check.
# Question: can a uniform-in-level automorphic spectral gap (Selberg 3/16, Kim-Sarnak 975/4096),
# which controls averages over FULL lattice-point sets of well-rounded regions of SL2(R),
# replace Bourgain-Gamburd for the averaging operators of Shkredov 2603.14116 Lemma 14 / Cor. 16?
# This script measures how THIN the relevant word sets are.
#
# Objects (MMS 2212.14646 eqs (15),(16); Shkredov 2603.14116 (159); MMS 1808.05845 Thm 25):
#   u = [[1,2],[0,1]], v = [[1,0],[2,1]]  (free generators of Sanov's group Lam, index 12 in SL2(Z))
#   G_N = { x_j = v^j u^-j = [[1,-2j],[2j,1-4j^2]] : 1<=j<=N }  (free generators of a rank-N subgroup H_N < Lam)
#   g_j = [[-2j,1-4j^2],[1,2j]] (det -1): x -> 1/(x+2j) - 2j, the Lemma-14 maps; g_j g_k = n(-2j) nbar(2(j-k)) n(2k)
#   n(a)=[[1,a],[0,1]], nbar(b)=[[1,0],[b,1]], w=[[0,1],[1,0]];  Cor.16 operator P_I W P_I, P_I = sum_{i in I} n(i)
#
# Parts
#  A  exact integer counts in SL2(Z): distinct reduced words in G_N u G_N^-1 of length <= L (freeness check),
#     their Frobenius norms, and density against lattice points of Lam / SL2(Z) in the same norm ball.
#  B  Bruhat box (the support of (P_I W P_I)^*(P_I W P_I) and of T^2): words n(x) nbar(y) n(z), x,z in [0,N), y in [1,N]
#     versus ALL lattice points of the real box {n(x)nbar(y)n(z)}: exact counts for N<=50.
#  C  the congruence quotient PSL2(F_p): distinct images / first collision (d(Cay)) of reduced words mod p.
#  D  operator norms on L^2_0(P^1(F_p)) of: word box average, full-lattice box average, T_N (Lemma 14), for small p.
#  E  lattice-point asymptotic check: #{gamma in SL2(Z): ||gamma||_F^2 <= T} / T  (expected -> 6).
#  F  freeness of the Lemma-14 involutions g_j ((Z/2)^{*N}) and effective dimension delta_eff of fixed-length words.
#  G  toy quotient PSL2(F_101), PSL2(F_211): exact return probabilities (the quantity the trace method must bound).
# Usage: python N7_words.py [A|B|C|D|E|all]
import sys, math, time
import numpy as np

def xj(j):  return np.array([[1, -2*j], [2*j, 1-4*j*j]], dtype=object)
def xjinv(j): return np.array([[1-4*j*j, 2*j], [-2*j, 1]], dtype=object)

# ---------------------------------------------------------------- A
def reduced_words(N, L):
    """all reduced words of length exactly 1..L in letters (j, +-1); yields list per length of int64 arrays (M,4)
    using int64 (safe: entries <= (4N^2+2)^L, we assert < 2^62)."""
    gens = []
    for j in range(1, N+1):
        gens.append((j, +1, np.array([1, -2*j, 2*j, 1-4*j*j], dtype=np.int64)))
        gens.append((j, -1, np.array([1-4*j*j, 2*j, -2*j, 1], dtype=np.int64)))
    G = np.stack([g[2] for g in gens]); lab = np.arange(2*N); inv = lab ^ 1  # letter 2(j-1)+0 is x_j, +1 is x_j^-1
    assert (4*N*N+2)**L < 2**62
    cur = G.copy(); last = lab.copy(); out = [cur]
    for _ in range(2, L+1):
        # append every letter not inverse to the last one
        A = np.repeat(cur, 2*N, axis=0); la = np.repeat(last, 2*N)
        B = np.tile(G, (len(cur), 1)); lb = np.tile(lab, len(cur))
        keep = lb != inv[la]
        A, B, lb = A[keep], B[keep], lb[keep]
        C = np.empty_like(A)
        C[:, 0] = A[:, 0]*B[:, 0] + A[:, 1]*B[:, 2]; C[:, 1] = A[:, 0]*B[:, 1] + A[:, 1]*B[:, 3]
        C[:, 2] = A[:, 2]*B[:, 0] + A[:, 3]*B[:, 2]; C[:, 3] = A[:, 2]*B[:, 1] + A[:, 3]*B[:, 3]
        cur, last = C, lb; out.append(cur)
    return out

def partA():
    print("== A: reduced words in G_N u G_N^-1 inside SL2(Z); density vs lattice points in the same Frobenius ball")
    print("   Lam-count(R) ~ 6R^2/12 = R^2/2 (index 12), SL2(Z)-count(R) ~ 6R^2 (Part E checks the 6)")
    print(" N  L  #words(len=L)  2N(2N-1)^(L-1)  distinct_in_SL2Z  maxF  medianF  frac_Lam_ball(maxF)  frac_Lam_ball(medF) [words<=median / (med^2/2)]")
    for N, Lmax in [(2, 8), (3, 7), (5, 6), (10, 5), (20, 4), (50, 3)]:
        ws = reduced_words(N, Lmax)
        for L, W in enumerate(ws, start=1):
            nw = len(W); pred = 2*N*(2*N-1)**(L-1)
            dist = len(np.unique(W, axis=0))
            F = np.sqrt((W.astype(np.float64)**2).sum(1)); mx = F.max(); md = np.median(F)
            print(f"{N:3d} {L:2d} {nw:12d} {pred:14d} {dist:14d} {mx:10.3e} {md:10.3e} {nw/(mx*mx/2):12.3e} {(nw/2)/(md*md/2):12.3e}", flush=True)

# ---------------------------------------------------------------- B
def phi_table(n):
    ph = np.arange(n+1)
    for i in range(2, n+1):
        if ph[i] == i:
            ph[i::i] -= ph[i::i]//i
    return ph

def partB():
    print("== B: Bruhat box. words n(x)nbar(y)n(z), x,z in {0..N-1}, y in {1..N}: entries alpha=1+xy, gamma=y, delta=1+yz")
    print("   full lattice points of the real box {n(x)nbar(y)n(z): x,z in [0,N), y in [1,N]} = {gamma in [1,N], alpha,delta in [1-?]}:")
    print("   gamma=y integer, alpha in (0,N*gamma]... counted exactly as sum_gamma #{(alpha,delta) in [1,N*gamma]^2: alpha*delta=1 mod gamma}")
    ph = phi_table(60)
    print("  N   #words=N^3   #lattice(box)   ratio   N*ratio   (pi^2/3=%.4f)" % (math.pi**2/3))
    for N in [2, 3, 5, 8, 10, 16, 20, 30, 40, 50]:
        words = N**3
        # brute-force lattice count for verification at small N, closed form N^2*sum phi(gamma) always
        lat = N*N*int(ph[1:N+1].sum())
        if N <= 10:
            cnt = 0
            for g in range(1, N+1):
                a = np.arange(1, N*g+1); d = np.arange(1, N*g+1)
                cnt += int(((a[:, None]*d[None, :]) % g == 1 % g).sum())
            assert cnt == lat, (N, cnt, lat)
        # verify words are distinct and are exactly the lattice points with alpha = delta = 1 mod gamma
        x, y, z = np.meshgrid(np.arange(N), np.arange(1, N+1), np.arange(N), indexing='ij')
        al = 1+x*y; de = 1+y*z; assert len(np.unique(np.stack([al.ravel(), y.ravel(), de.ravel()]), axis=1).T) == words
        print(f"{N:3d} {words:10d} {lat:14d} {words/lat:9.5f} {N*words/lat:8.4f}")
    print("   longer Bruhat words n(x1)nbar(y1)n(x2)nbar(y2)n(x3) (x,y in [1,N]): #words=N^5 vs lattice points of SL2(Z) in the")
    print("   Frobenius ball of the max / median word norm (count ~ 6R^2)")
    for N in [3, 5, 8, 12, 16, 20]:
        r = np.arange(1, N+1, dtype=np.int64)
        def n(a): return np.stack([np.ones_like(a), a, np.zeros_like(a), np.ones_like(a)], -1)
        def nb(b): return np.stack([np.ones_like(b), np.zeros_like(b), b, np.ones_like(b)], -1)
        def mul(A, B):
            return np.stack([A[..., 0]*B[..., 0]+A[..., 1]*B[..., 2], A[..., 0]*B[..., 1]+A[..., 1]*B[..., 3],
                             A[..., 2]*B[..., 0]+A[..., 3]*B[..., 2], A[..., 2]*B[..., 1]+A[..., 3]*B[..., 3]], -1)
        X = n(r)
        for f in (nb, n, nb, n):
            X = mul(X[:, None, :], f(r)[None, :, :]).reshape(-1, 4)
        F = np.sqrt((X.astype(np.float64)**2).sum(1)); mx, md = F.max(), np.median(F)
        nd = len(np.unique(X, axis=0))
        print(f"   N={N:3d} words={len(X):9d} distinct={nd:9d} maxF={mx:.3e} words/(6 maxF^2)={len(X)/(6*mx*mx):.3e}  (words<=med)/(6 med^2)={len(X)/2/(6*md*md):.3e}  N^-3={N**-3.:.3e}")

# ---------------------------------------------------------------- C
def partC():
    print("== C: congruence quotient PSL2(F_p): reduced words of length<=L in G_N u G_N^-1 reduced mod p (sign-normalised)")
    print("   d_obs = largest L with all reduced words of length<=L distinct mod p  (MMS 1808.05845: d(Cay) >= (1/4) log_N p, Thm 25;")
    print("   MMS 2212.14646 quotes tau=1/5; Margulis bound d >= log_n(p/2), n = max generator norm)")
    print("   p   N  L  #words(<=L)  distinct_mod_p   |PSL2(F_p)|   frac_of_group  (1/4)log_N p  log_{n}(p/2)")
    for p in [10007, 100003, 1000003]:
        order = p*(p*p-1)//2
        for N, Lmax in [(5, 7), (10, 5), (20, 4), (50, 3)]:
            ws = reduced_words(N, Lmax); allw = []
            nmax = math.sqrt(1 + 8*N*N + (4*N*N-1)**2)
            dobs = None
            for L, W in enumerate(ws, start=1):
                Wm = W % p
                # normalise sign for PSL2: make first nonzero of (a,b) canonical  (choose rep with a<p/2 or a==0 and b<p/2)
                neg = (p - Wm) % p
                flip = (Wm[:, 0] > p//2) | ((Wm[:, 0] == 0) & (Wm[:, 1] > p//2))
                Wm = np.where(flip[:, None], neg, Wm)
                allw.append(Wm); cat = np.concatenate(allw)
                # identity must be counted too (length 0)
                dist = len(np.unique(np.concatenate([cat, np.array([[1, 0, 0, 1]])]), axis=0))
                tot = len(cat)+1
                if dist == tot: dobs = L
                print(f"{p:8d} {N:3d} {L:2d} {tot:11d} {dist:11d} {order:.3e} {dist/order:.3e} {0.25*math.log(p)/math.log(N):6.3f} {math.log(p/2)/math.log(nmax):6.3f}", flush=True)
            print(f"   -> p={p} N={N}: all words of length <= {dobs} distinct mod p (tested up to L={Lmax})")

# ---------------------------------------------------------------- D
def mobius_table(mats, p):
    """mats: (M,4) int64 entries mod p (det = +-1). returns (M, p+1) images of x in {0..p-1, inf=p}."""
    inv = np.zeros(p, dtype=np.int64); inv[1:] = [pow(i, p-2, p) for i in range(1, p)]
    x = np.arange(p, dtype=np.int64)
    a, b, c, d = [mats[:, k:k+1] % p for k in range(4)]
    num = (a*x + b) % p; den = (c*x + d) % p
    img = np.where(den == 0, p, (num*inv[den]) % p)
    ai, ci = mats[:, 0] % p, mats[:, 2] % p
    infimg = np.where(ci == 0, p, (ai*inv[ci]) % p)
    return np.concatenate([img, infimg[:, None]], axis=1)

def opnorm0(mats, p, weights=None):
    """||(1/sum w) sum_g w_g pi(g)|| on L^2_0(P^1(F_p)) (largest singular value off constants)."""
    n = p+1; M = np.zeros(n*n)
    w = np.ones(len(mats)) if weights is None else weights
    for s in range(0, len(mats), 4000):
        img = mobius_table(mats[s:s+4000], p)
        idx = (img*n + np.arange(n)[None, :]).ravel()
        M += np.bincount(idx, weights=np.repeat(w[s:s+4000], n), minlength=n*n)
    M = M.reshape(n, n)/w.sum() - 1.0/n
    return np.linalg.norm(M, 2)

def partD():
    print("== D: operator norms on L^2_0(P^1(F_p))")
    print("   WB = uniform on words n(x)nbar(y)n(z), x,z in [0,N), y in [1,N]  (N^3 points; density ~ pi^2/(3N) in the box)")
    print("   FB = uniform on ALL lattice points of the same real box (N^2*sum_{g<=N} phi(g) ~ 3N^4/pi^2 points)")
    print("   T  = (1/N) sum_{j<=N} g_j (Lemma 14);  Kesten = 2 sqrt(N-1)/N;  1/sqrt(#pts) = random-set scale")
    for p in [1009, 2003]:
        print(f" p={p}")
        print("   N   #WB    ||WB||_0   #FB      ||FB||_0   ||T||_0   Kesten   1/sqrt#FB")
        for N in [2, 3, 4, 6, 8, 10, 12, 14, 16]:
            x, y, z = [a.ravel().astype(np.int64) for a in np.meshgrid(np.arange(N), np.arange(1, N+1), np.arange(N), indexing='ij')]
            WB = np.stack([1+x*y, x+z+x*y*z, y, 1+y*z], 1)
            fb = []
            for g in range(1, N+1):
                a = np.arange(1, N*g+1, dtype=np.int64)
                A, D = np.meshgrid(a, a, indexing='ij'); m = (A*D) % g == 1 % g
                A, D = A[m], D[m]
                fb.append(np.stack([A, (A*D-1)//g, np.full_like(A, g), D], 1))
            FB = np.concatenate(fb)
            T = np.array([[-2*j, 1-4*j*j, 1, 2*j] for j in range(1, N+1)], dtype=np.int64)
            t0 = time.time()
            nw, nf, nt = opnorm0(WB, p), opnorm0(FB, p), opnorm0(T, p)
            print(f"  {N:3d} {len(WB):6d} {nw:9.4f} {len(FB):8d} {nf:9.4f} {nt:9.4f} {2*math.sqrt(N-1)/N:8.4f} {1/math.sqrt(len(FB)):8.4f}   ({time.time()-t0:.1f}s)", flush=True)

# ---------------------------------------------------------------- E
def partE():
    print("== E: #{gamma in SL2(Z): a^2+b^2+c^2+d^2 <= T} / T")
    for T in [10**4, 10**5, 10**6, 4*10**6]:
        R = int(math.isqrt(T)); cnt = 0
        for c in range(-R, R+1):
            ds = np.arange(-R, R+1, dtype=np.int64); ds = ds[c*c + ds*ds <= T]
            g = np.gcd(abs(c), np.abs(ds)); ds = ds[g == 1]
            if c == 0:
                # d=+-1, a=d, b free: 1+b^2+0+1 <= T
                cnt += 2*(2*int(math.isqrt(T-2))+1); continue
            for d in ds:
                # a d - b c = 1: particular (a0,b0), general a = a0 + k c, b = b0 + k d
                g_, s, t = ext_gcd(int(d), int(-c))  # s*d + t*(-c) = 1 -> a0=s, b0=t
                a0, b0 = s, t; rem = T - c*c - int(d)*int(d)
                # (a0+kc)^2+(b0+kd)^2 <= rem : quadratic in k
                A2 = c*c + int(d)*int(d); B2 = 2*(a0*c + b0*int(d)); C2 = a0*a0 + b0*b0 - rem
                disc = B2*B2 - 4*A2*C2
                if disc < 0: continue
                sq = math.isqrt(disc)
                klo = math.ceil((-B2 - sq)/(2*A2)) - 1; khi = math.floor((-B2 + sq)/(2*A2)) + 1
                for k in range(klo, khi+1):
                    if (a0+k*c)**2 + (b0+k*int(d))**2 <= rem: cnt += 1
        print(f"  T={T:9d}  count={cnt:10d}  count/T={cnt/T:.4f}", flush=True)

def ext_gcd(a, b):
    if b == 0: return (a, 1, 0) if a > 0 else (-a, -1, 0)
    g, x, y = ext_gcd(b, a % b); return g, y, x - (a//b)*y


# ---------------------------------------------------------------- F
def partF():
    print("== F: Lemma-14 maps g_j (det -1 involutions). Reduced g-words (no letter repeated consecutively) of length L:")
    print("   #=N(N-1)^(L-1) expected if <g_1..g_N> = (Z/2)^{*N}; distinct in GL2(Z)?  Frobenius norms; delta_eff = log#/log(6 R^2)")
    for N, Lmax in [(3, 9), (5, 7), (10, 5), (20, 4), (50, 3)]:
        G = np.array([[-2*j, 1-4*j*j, 1, 2*j] for j in range(1, N+1)], dtype=np.int64)
        cur, last = G.copy(), np.arange(N)
        for L in range(1, Lmax+1):
            if L > 1:
                A = np.repeat(cur, N, axis=0); la = np.repeat(last, N); B = np.tile(G, (len(cur), 1)); lb = np.tile(np.arange(N), len(cur))
                k = la != lb; A, B, lb = A[k], B[k], lb[k]
                cur = np.stack([A[:, 0]*B[:, 0]+A[:, 1]*B[:, 2], A[:, 0]*B[:, 1]+A[:, 1]*B[:, 3], A[:, 2]*B[:, 0]+A[:, 3]*B[:, 2], A[:, 2]*B[:, 1]+A[:, 3]*B[:, 3]], 1)
                last = lb
            assert np.abs(cur).max() < 2**61
            nd = len(np.unique(cur, axis=0)); idc = int(((cur[:, 0] == 1) & (cur[:, 1] == 0) & (cur[:, 2] == 0) & (cur[:, 3] == 1)).sum())
            F = np.sqrt((cur.astype(np.float64)**2).sum(1)); mx, md = F.max(), np.median(F)
            print(f"  N={N:3d} L={L:2d} #={len(cur):9d} pred={N*(N-1)**(L-1):9d} distinct={nd:9d} identity={idc} maxF={mx:.3e} medF={md:.3e} "
                  f"dEff(max)={math.log(len(cur))/math.log(6*mx*mx):.3f} dEff(med)={math.log(len(cur)/2)/math.log(6*md*md):.3f}", flush=True)

# ---------------------------------------------------------------- G
def partG():
    print("== G: what the trace method must count, in a toy quotient PSL2(F_p) (p small, so N >> p^(1/9): illustration only)")
    print("   eta = uniform on {g_j g_k : j,k in [N]} (= T^*T for the Lemma-14 maps, g_j involutions). R(l) = P(eta^(l) = e in PSL2(F_p)).")
    print("   tree(l) = P(return) for the simple walk on (Z/2)^{*N} at time 2l (the 'free' collisions); 1/|PSL2| = saturation.")
    print("   Sarnak-Xue/BG inequality (pi(eta)=T^*T >= 0): ((p-1)/2) ||T||_0^{2l} <= |PSL2| R(l) - 1  ->  bound_l = ((|PSL2|R(l)-1)/((p-1)/2))^(1/2l)")
    print("   nonfree(l) = R(l) - tree(l) = P(word of length 2l is nontrivial in (Z/2)^{*N} but = +-I mod p)  <- THE quantity to be bounded")
    print("   lattMaj(l) = tree(l) * 6 Rl^2 / |SL2(F_p)|, Rl = (max_jk ||g_j g_k||_F)^l: optimistic automorphic majorant of nonfree(l)")
    print("   (max atom of eta^(l) = tree(l) times main term of #{Gamma(p)-coset points in the Frobenius ball}); compare with nonfree(l)")
    for p in [101]:
        # enumerate PSL2(F_p)
        a, b, c, d = [x.ravel() for x in np.meshgrid(*[np.arange(p)]*4, indexing='ij')] if p <= 0 else (None,)*4
        els = []
        for a0 in range(p):
            for b0 in range(p):
                if a0 == 0 and b0 == 0: continue
                # rows (c,d) with a0 d - b0 c = 1
                cc = np.arange(p)
                if a0 != 0:
                    inva = pow(a0, p-2, p); dd = ((1 + b0*cc) * inva) % p
                    els.append(np.stack([np.full(p, a0), np.full(p, b0), cc, dd], 1))
                else:
                    # a0=0: -b0 c = 1 -> c = -1/b0, d free
                    c0 = (-pow(b0, p-2, p)) % p; dd = np.arange(p)
                    els.append(np.stack([np.zeros(p, dtype=np.int64), np.full(p, b0), np.full(p, c0), dd], 1))
        E = np.concatenate(els).astype(np.int64)
        def canon(M):
            M = M % p; neg = (p - M) % p
            flip = (M[:, 0] > p//2) | ((M[:, 0] == 0) & (M[:, 1] > p//2))
            return np.where(flip[:, None], neg, M)
        def key(M): return ((M[:, 0]*p + M[:, 1])*p + M[:, 2])*p + M[:, 3]
        K = np.unique(key(canon(E))); order = len(K); assert order == p*(p*p-1)//2
        idx_e = np.searchsorted(K, key(canon(np.array([[1, 0, 0, 1]]))))[0]
        Kel = np.stack([K//p**3, (K//p**2) % p, (K//p) % p, K % p], 1)
        for N in [3, 5, 10]:
            steps = []; Rg = 0.0
            for j in range(1, N+1):
                for k in range(1, N+1):
                    gj = np.array([-2*j, 1-4*j*j, 1, 2*j]); gk = np.array([-2*k, 1-4*k*k, 1, 2*k])
                    Rg = max(Rg, math.sqrt(sum(float(v)**2 for v in [gj[0]*gk[0]+gj[1]*gk[2], gj[0]*gk[1]+gj[1]*gk[3], gj[2]*gk[0]+gj[3]*gk[2], gj[2]*gk[1]+gj[3]*gk[3]])))
                    steps.append([gj[0]*gk[0]+gj[1]*gk[2], gj[0]*gk[1]+gj[1]*gk[3], gj[2]*gk[0]+gj[3]*gk[2], gj[2]*gk[1]+gj[3]*gk[3]])
            steps = np.array(steps, dtype=np.int64) % p
            perms = []
            for s in steps:
                P = Kel; Q = np.stack([P[:, 0]*s[0]+P[:, 1]*s[2], P[:, 0]*s[1]+P[:, 1]*s[3], P[:, 2]*s[0]+P[:, 3]*s[2], P[:, 2]*s[1]+P[:, 3]*s[3]], 1)
                perms.append(np.searchsorted(K, key(canon(Q))))
            # tree return probabilities for simple walk on N-regular tree
            dist = np.zeros(200); dist[0] = 1.0; tree = {}
            for t in range(1, 81):
                nd = np.zeros_like(dist); nd[1] += dist[0]; nd[:-1] += dist[1:] / N; nd[2:] += dist[1:-1]*(N-1)/N; dist = nd
                if t % 2 == 0: tree[t//2] = dist[0]
            mu = np.zeros(order); mu[idx_e] = 1.0
            print(f"  p={p} N={N} |PSL2|={order}")
            for l in range(1, 31):
                new = np.zeros(order)
                for P in perms: np.add.at(new, P, mu) if False else None
                new = sum(np.bincount(P, weights=mu, minlength=order) for P in perms) / len(perms)
                mu = new; R = mu[idx_e]
                bnd = max(order*R - 1, 0) / ((p-1)/2); bnd = bnd**(1/(2*l)) if bnd > 0 else 0.0
                lm = tree[l]*6*Rg**(2*l)/(p*(p*p-1))
                print(f"    l={l:2d}: R={R:.4e} tree={tree[l]:.4e} nonfree={R-tree[l]:.3e} 1/|PSL2|={1/order:.3e} lattMaj={lm:.3e}  ||T||_0<={bnd:.4f} (Kesten {2*math.sqrt(N-1)/N:.4f})", flush=True)

if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    for k, f in [("A", partA), ("B", partB), ("C", partC), ("D", partD), ("E", partE), ("F", partF), ("G", partG)]:
        if what in ("all", k): f()
