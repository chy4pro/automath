import numpy as np, time, sys
sys.path.insert(0,'.')
from mu1b import slp, upsample
D='./'
p=np.load(D+'mu1_p640.npy')
p=upsample(p); n=len(p); t0=time.time()
b=slp(n,p,iters=150)
print(n,b[0],time.time()-t0,flush=True)
np.save(D+f'mu1_p{n}.npy',b[1])
