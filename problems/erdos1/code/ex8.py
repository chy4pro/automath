from exhaust import enum, check, beta
import time
for n, M in [(8, 85)]:
    t = time.time()
    sets = enum(n, M)
    for a in sets: check(list(a))
    mn = min(a[-1] for a in sets)
    print(n, M, len(sets), mn, 2*beta(n-1), beta(n), [a for a in sets if a[-1]==mn][:3], f"{time.time()-t:.1f}s")
