#!/usr/bin/env python3
"""Compatibility entry point for the N8 mean-zero operator experiments.

The N-involution free-model comparator is 2*sqrt(N-1)/N, not sqrt(2*N-1)/N.
Finite numerical agreement does not prove the asymptotic norm or a universal exponent.
The appendix's numerical exponent is conditional on the unresolved G0 constant chain;
see phase1/G0_gate_audit.md. No coefficient-one norm bound is certified here.

Usage: python zaremba_kappa_numerics.py <prime> [Nmax=64] [kind=T1] [iterations=150]
Uses NumPy only; matrix-free large T1 and linear-memory T2 are in N8_harness.py.
For the dependency-free Node fallback see phase0/N8_data/run_n8.js.
"""
import importlib.util
import json
import math
from pathlib import Path
import sys
import time


def main():
    path = Path(__file__).resolve().parent / 'phase0' / 'N8_harness.py'
    spec = importlib.util.spec_from_file_location('n8_harness', path)
    n8 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(n8)
    p = int(sys.argv[1])
    nmax = int(sys.argv[2]) if len(sys.argv) > 2 else 64
    kind = sys.argv[3] if len(sys.argv) > 3 else 'T1'
    iterations = int(sys.argv[4]) if len(sys.argv) > 4 else 150
    if not (2 < p <= 2_000_000 and 1 <= nmax <= min(p, 256)):
        raise ValueError('require prime 2<p<=2e6 and 1<=Nmax<=min(p,256)')
    deadline = 3500.0  # Absolute process CPU, including imports and construction.
    op = n8.Ops(p)
    for N in (2, 4, 8, 16, 32, 64, 128, 256):
        if N > nmax or time.process_time() >= deadline:
            break
        A0 = op.op(kind, N)
        remaining = deadline - time.process_time()
        if remaining <= 0:
            break
        result = n8.power_diagnostics(A0, p+1, iterations,
                                      cpu_seconds=remaining)
        s = result['sigma_lower_estimate']
        result.update(p=p, N=N, kind=kind, free_T1_comparator=2*math.sqrt(N-1)/N,
                      kappa_emp_from_lower_estimate=-math.log(s)/math.log(N) if s>0 else None,
                      bound_status='numerical lower estimate; exponent is not a theorem')
        print(json.dumps(result), flush=True)


if __name__ == '__main__':
    main()
