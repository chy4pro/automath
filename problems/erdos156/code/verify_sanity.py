import numpy as np, bnb, verify
from mpmath import iv
# monkeypatch: run B&B, then corrupt leaves by expanding boxes, expect failures
orig=bnb.run
def corrupt_run(*a,**k):
    res,cnt,leaves=orig(*a,**k)
    new=[]
    for lf in leaves:
        if lf[0]=='vec':
            box=lf[1].copy(); w=box[:,:,1]-box[:,:,0]
            box[:,:,0]-=3*w; box[:,:,1]+=3*w
            new.append(('vec',box,lf[2],lf[3]))
        else: new.append(lf)
    return res,cnt,new
bnb.run=corrupt_run
print('corrupted run ->')
verify.run_and_verify(2,0.65,'0.853')
