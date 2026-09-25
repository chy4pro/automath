"""Search 3-layer line systems: layers S1,S2,S3 subset of [0,N); a 'line' is a 3-term AP x<y<z (x in S1, y in S2, z in S3)
with slope a=y-x=z-y; lines must have DISTINCT slopes. Want #lines > |S1|+|S2|+|S3| with as few points as possible.
(Loops-only model; a real instance follows by CRT embedding, giving f(#lines) >= 4.)  Hard time cap inside."""
import random, sys, time
T0=time.time(); LIMIT=float(sys.argv[1]) if len(sys.argv)>1 else 540; N=int(sys.argv[2]) if len(sys.argv)>2 else 40
random.seed(int(sys.argv[3]) if len(sys.argv)>3 else 1)
def score(S1,S3,S2):
    slopes=set()
    for x in S1:
        for z in S3:
            if (x+z)%2==0 and (x+z)//2 in S2 and z>x: slopes.add((z-x)//2)
    return len(slopes)
def best_S2(S1,S3):
    # candidate midpoints; greedy add while (new slopes) >= 1, then local improve
    mids={}
    for x in S1:
        for z in S3:
            if z>x and (x+z)%2==0: mids.setdefault((x+z)//2,set()).add((z-x)//2)
    S2=set(); got=set()
    items=sorted(mids.items(),key=lambda kv:-len(kv[1]))
    changed=True
    while changed:
        changed=False
        for y,sl in items:
            if y in S2: continue
            new=len(sl-got)
            if new>=2 or (new==1 and len(S2)<1):
                S2.add(y); got|=sl; changed=True
    return S2, len(got)
best=None
while time.time()-T0<LIMIT:
    s1=random.randint(3,7); s3=random.randint(3,7)
    S1=set(random.sample(range(N),s1)); S3=set(random.sample(range(N),s3))
    S2,lines=best_S2(S1,S3)
    pts=len(S1)+len(S2)+len(S3)
    if lines>pts:
        key=(lines, -pts)
        if best is None or (lines-pts>best[0]-best[1]) or (lines-pts==best[0]-best[1] and lines<best[0]):
            best=(lines,pts,sorted(S1),sorted(S2),sorted(S3)); print("lines=%d points=%d  S1=%s S2=%s S3=%s"%best, flush=True)
print("done; best",best)
