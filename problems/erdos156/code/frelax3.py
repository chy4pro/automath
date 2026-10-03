import numpy as np, sys
from frelax2 import relax
rng=np.random.default_rng(2)
n=int(sys.argv[1])
for h in [float(v) for v in sys.argv[2].split(',')]:
    b,c=relax(n,h,int(sys.argv[3]),rng)
    print(n,h,round(b,4),np.round(c,4) if c is not None else None,flush=True)
