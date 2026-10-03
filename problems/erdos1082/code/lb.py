def minA(N,m):
    q,s=divmod(N,m)
    return (m-s)*q*(q-1)//2 + s*(q+1)*q//2
for n in range(3,31):
    N=n-1
    for m in range(1,n):
        if n*minA(N,m)<=n*(n-1): break
    tight = (n*minA(N,m)==n*(n-1))
    print(n, 'countLB',m,'ceil((n-1)/3)',-(-(n-1)//3),'tight' if tight else '', 'floor(n/2)',n//2)
