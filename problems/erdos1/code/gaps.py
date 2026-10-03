from exhaust import enum
for n, M in [(3, 4), (4, 7), (5, 13), (6, 24), (7, 44), (8, 84)]:
    opt = [a for a in enum(n, M) if a[-1] == M]
    print(n, len(opt), sorted({a[-1] - a[-2] for a in opt}), opt)
