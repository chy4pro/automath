import sys, time, bnb
n=int(sys.argv[1]); hs=[float(v) for v in sys.argv[2].split(',')]; maxb=int(sys.argv[3])
for h in hs:
    lo,hi=0.70,0.99   # lo: feasible/unknown, hi: certified infeasible
    t0=time.time()
    while hi-lo>0.002:
        mid=(lo+hi)/2
        res,cnt,_=bnb.run(n,h,mid,maxboxes=maxb,verbose=False)
        if res=='INFEASIBLE': hi=mid
        else: lo=mid
    print('n',n,'h',h,'certified-infeasible(float) at lam',round(hi,4),'feasible/unknown at',round(lo,4),'t',round(time.time()-t0,1),flush=True)
