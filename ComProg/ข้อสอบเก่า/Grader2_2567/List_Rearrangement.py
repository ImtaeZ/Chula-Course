D = [int(e) for e in input().split()]
Ds = D.copy()
p = sorted(D)

sp = 0
x = []
for i in range(len(p)):
    sp += p[i]
    x.append(str(Ds[sp%len(Ds)]))
    Ds.pop(sp%len(Ds))

print(' '.join(x))