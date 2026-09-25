def hh(mult):
    """returns (steps, residue) or (None,None) if not a step sequence"""
    s = sorted(list(mult), reverse=True); steps = 0
    while s and s[0] > 0:
        d = s[0]; rest = s[1:]
        if d > len(rest): return None, None
        head, tail = rest[:d], rest[d:]
        if any(x <= 0 for x in head): return None, None
        s = sorted([x-1 for x in head] + tail, reverse=True); steps += 1
    return steps, len(s)
def partitions(n, maxpart=None):
    if maxpart is None: maxpart = n
    if n == 0:
        yield []; return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n-k, k): yield [k]+rest

print("A. single-part evaluation  s0([w]) = steps([w]^{w+2}) : predicted w for even w, None for odd")
bad=0
for w in range(0,31):
    st,_ = hh([w]*(w+2))
    pred = w if w%2==0 else None
    ok = (st==pred)
    if not ok: bad+=1; print("   MISMATCH", w, st, pred)
print(f"   w=0..30 checked, mismatches={bad}")
print()
print("B. reformulation:  s0(lam) = |M| - residue(M),  |M| = w+1+k   =>   s0=w  <=>  residue(M)=k+1")
print("   testing:  residue(M) <= k  for every lam with k>=2 parts, and = k+1 iff k=1")
bad=0; tot=0; tight=0; mn=99
for n in range(1,29):
    for lam in partitions(n):
        w=lam[0]; k=len(lam)
        st,res = hh([w]*(w+1)+lam)
        if st is None:
            # not a step sequence: cannot equal w, consistent with C1 for k>=2
            continue
        tot+=1
        assert st == (w+1+k) - res, ("identity broken", lam, st, res)
        if k==1:
            if res != k+1: bad+=1; print("   k=1 but residue != 2:", lam, res)
        else:
            if res > k: bad+=1; print("   VIOLATION residue>k:", lam, "k=",k, "res=",res)
            if res == k: tight+=1
            mn=min(mn,k-res)
print(f"   n=1..28: {tot} step-sequences tested, violations={bad}, tight (residue==k)={tight}, min slack k-residue={mn}")
print()
print("C. strengthened form:  is  s0(lam) >= lam_1  always, with equality iff k==1 ?")
bad=0; tot=0
for n in range(1,29):
    for lam in partitions(n):
        w=lam[0]; k=len(lam)
        st,_ = hh([w]*(w+1)+lam)
        if st is None: continue
        tot+=1
        if st < w: bad+=1; print("   s0 < lam_1 !", lam, st)
        if st==w and k>1: bad+=1; print("   equality with k>1 !", lam, st)
print(f"   {tot} tested, violations={bad}")
