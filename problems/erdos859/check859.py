# -*- coding: utf-8 -*-
"""Work in L = log t to avoid overflow. y = t/L^2, z = t, so log(z/y)=2 log L, log y = L-2 log L."""
import math
delta = 1.0 - (1.0 + math.log(math.log(2.0))) / math.log(2.0)

def u_of(L):
    return 2.0*math.log(L) / (L - 2.0*math.log(L))

print(" log t        u            ford=u^d (log(2/u))^-3/2     clean=(log t)^-d (loglog t)^(d-3/2)   ratio      2/log t     class1/class2")
for L in [20, 100, 1e3, 1e5, 1e8, 1e12, 1e20, 1e40, 1e80]:
    u = u_of(L)
    ford = u**delta * math.log(2.0/u)**(-1.5)
    clean = L**(-delta) * math.log(L)**(delta-1.5)
    print(" %-10.4g %-12.6g %-27.6e %-36.6e %-10.5f %-11.3e %.3f"
          % (L, u, ford, clean, ford/clean, 2.0/L, ford/(2.0/L)))
print()
print("limit of ratio should be 2^delta = %.6f" % (2.0**delta))
# -*- coding: utf-8 -*-
"""Regime checks and asymptotic sanity for the Erdos #859 upper bound."""
import math

delta = 1.0 - (1.0 + math.log(math.log(2.0))) / math.log(2.0)
print("delta = %.10f   (Ford: 0.086071...)" % delta)
print("delta - 3/2 = %.10f" % (delta - 1.5))

def params(t):
    L = math.log(t)
    y = t / L**2
    z = t
    u = math.log(z / y) / math.log(y)          # z = y^(1+u)
    return y, z, u, L

# Regime conditions of Ford Theorem 1(v), third line: 100 <= y, 2y <= z <= y^2.
# 2y <= z  <=>  (log t)^2 >= 2 ;  z <= y^2 <=> (log t)^4 <= t ; y >= 100 <=> t >= 100 (log t)^2
def ok(t):
    y, z, u, L = params(t)
    return (y >= 100.0, 2*y <= z, z <= y*y, u <= 1.0)

lo, hi = 10.0, 10.0**9
while hi / lo > 1.0000001:
    mid = math.sqrt(lo*hi)
    if all(ok(mid)): hi = mid
    else: lo = mid
print("all Theorem 1(v) conditions hold from t_0 = %.1f onwards" % hi)
for t in [hi*0.99, hi*1.01, 1e4, 1e5, 1e6]:
    print("   t=%.4g -> y>=100:%s  2y<=z:%s  z<=y^2:%s  u<=1:%s" % ((t,) + ok(t)))

print()
# NOTE 2026-09-09: these two loops used to build t = math.exp(e) and overflowed at e = 1000
# (OverflowError: math range error) -- the tail of the script never ran. Reported by the incoming
# Codex handoff session. Everything here depends on t only through L = log t, so both loops now
# take L directly, matching the log-space half of this file. Fixed.
print(" log t      u            u^d*(log(2/u))^-1.5   (log t)^-d (loglog t)^(d-1.5)  ratio   2/log t")
for L in [20.0, 50.0, 100.0, 300.0, 1000.0, 5000.0]:
    u = u_of(L)
    ford = u**delta * math.log(2.0/u)**(-1.5)
    clean = L**(-delta) * math.log(L)**(delta - 1.5)
    print(" %-10.4g %-12.6g %18.6e   %28.6e  %6.3f  %.3e"
          % (L, u, ford, clean, ford/clean, 2.0/L))

print()
print("class-1 term / class-2 term (should -> infinity):")
for L in [20.0, 100.0, 1000.0, 1e4, 1e6]:
    u = u_of(L)
    ford = u**delta * math.log(2.0/u)**(-1.5)
    print("   log t = %-8g  class1 ~ %.4e   class2 = %.4e   ratio %.2f"
          % (L, ford, 2.0/L, ford/(2.0/L)))
