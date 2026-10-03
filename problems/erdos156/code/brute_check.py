import itertools
def sidon(A):
    s=set()
    for i in range(len(A)):
        for j in range(i,len(A)):
            t=A[i]+A[j]
            if t in s: return False
            s.add(t)
    return True
def maximal(A,N):
    S=set(A)
    return all((x in S) or not sidon(sorted(A+(x,))) for x in range(1,N+1))
res={}
for N in range(1,31):
    k=1
    while True:
        if any(sidon(A) and maximal(A,N) for A in itertools.combinations(range(1,N+1),k)): break
        k+=1
    res[N]=k
print(res)
