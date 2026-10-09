import json, sys
sys.path.insert(0, '.')
from b4l_common import *
r1 = json.load(open('batch1_result_brute5.json')); r2 = json.load(open('batch2_result.json')); r3 = json.load(open('batch3_result.json'))
def diag(best):
    rho, D, u, N, A, W = best
    D2, u2 = brute_D(list(A), N)                     # independent brute-force recomputation
    assert (D2, u2) == (D, u), (A, N, D, D2)
    assert b4_brute(list(A))
    ss, rl = sumset_stats(list(A), u)
    return f"{rho:.4f} | N={N}, u={u}, A={list(A)} | D={D} (4u(u-1)={4*u*(u-1)}, W={W}) | F={W/(4*u*(u-1)):.5f} | {ss} | {rl}/{2*(u-1)}"
L = []
L.append("### Batch 1 (literal t-enumeration) per family, q, N-class\n")
L.append("rho = 100 D/(u(u-1)) (claim needs rho >= 1); F = W/(4u(u-1)) realised weighted fraction; |A+A|; #x (0<|x|<u) in S-S out of 2(u-1). Every row recomputed by independent brute-force 4-tuple enumeration (b4l_common.brute_D).\n")
L.append("| family | q | N-class | min rho | attaining set (min-normalised, any translate/reflection) | F | abs(A+A) | x realised by S-S |\n|---|---|---|---|---|---|---|---|")
for key, v in r1.items():
    fam, q = key.split('|')
    for b in ('256', '512', '4096'):
        d = diag(v['best'][b]).split(' | ')
        L.append(f"| {fam} | {q} | {b} | {d[0]} | {d[1]}; {d[2]} | {d[3].replace('F=','')} | {d[4]} | {d[5]} |")
L.append("\n### Batch 1 accounting\n")
L.append("| family | q | M | #b | #units | raw (b,a,t) = #b*phi*M | unique full sets | unique nonempty subsets by size | invalid | failures | ordinary translates covered (per convention; N=256/512/4096 class) | CPU s |\n|---|---|---|---|---|---|---|---|---|---|---|---|")
for key, v in r1.items():
    fam, q = key.split('|')
    L.append(f"| {fam} | {q} | {v['M']} | {v['nb']} | {v['phi']} | {v['raw']} | {v['uniq_full']} | {v['uniq_sub']} (total {sum(v['uniq_sub'].values())}) | {v['invalid']} | {v['nfail']} | {v['cover']['256']}/{v['cover']['512']}/{v['cover']['4096']} | {v['cpu']:.1f} |")
tot = sum(v['raw'] for v in r1.values()); L.append(f"\nTotal raw (family,q,b,a,t) enumerated: {tot}.")
L.append("\n### Batch 2\n")
d = r2['dense']
L.append(f"Dense: subsets of {{0..31}} of size 1..4: {d['subsets_total']}; B4 kept {d['b4_kept']} ({sum(d['b4_kept'].values())}), non-B4 rejected {d['nonb4']}; unique min-normalised shapes {d['unique_shapes']}; failures {d['nfail']}; translates covered per convention (N=256/512/4096): {d['cover']['256']}/{d['cover']['512']}/{d['cover']['4096']}.\n")
L.append("| group | N-class | min rho | set | F | abs(A+A) | x realised |\n|---|---|---|---|---|---|---|")
for b in ('256', '512', '4096'):
    x = diag(d['best'][b]).split(' | ')
    L.append(f"| dense<=4 of {{0..31}} | {b} | {x[0]} | {x[1]}; {x[2]} | {x[3].replace('F=','')} | {x[4]} | {x[5]} |")
for k, g in r2['greedy'].items():
    for b in ('256', '512', '4096'):
        x = diag(g['best'][b]).split(' | ')
        L.append(f"| greedy prefix k={k} x dilates 1..16 (+reflections) | {b} | {x[0]} | {x[1]}; {x[2]} | {x[3].replace('F=','')} | {x[4]} | {x[5]} |")
L.append(f"\nGreedy: raw (k,d) fixtures {r2['greedy_raw']}, unique shapes {r2['greedy_shapes']}, failures {sum(g['nfail'] for g in r2['greedy'].values())}, invalid {sum(g['invalid'] for g in r2['greedy'].values())}. CPU dense {r2['cpu_dense']:.2f}s, total batch 2 {r2['cpu_total']:.2f}s.")
L.append("\n### Batch 3 (hill climbing)\n")
L.append("| N | u | best set | m | W | D | rho | F | moves |\n|---|---|---|---|---|---|---|---|---|")
for N, v in r3.items():
    L.append(f"| {N} | {v['u']} | {v['A']} | {v['m']} | {v['W']} | {v['D']} | {v['rho']:.4f} | {v['F']:.5f} | {v['evals']} |")
open('tables.md', 'w').write('\n'.join(L))
print('\n'.join(L))
