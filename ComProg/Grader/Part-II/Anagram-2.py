x1 = input()
x2 = input()
w1 = [e.lower() for e in x1 if 'a' <= e.lower() <= 'z']
w2 = [e.lower() for e in x2 if 'a' <= e.lower() <= 'z']
w1.sort()
w2.sort()
c1 = w1.copy()
c2 = w2.copy()
ana = []
if len(w1) >= len(w2):
    for c in w1:
        if c in w2:
            ana.append(c)
            w2.remove(c)
else:
    for c in w2:
        if c in w1:
            ana.append(c)
            w1.remove(c)

for c in ana:
    if c in c1:
        c1.remove(c)
    if c in c2:
        c2.remove(c)

r1 = {}
for c in c1:
    if c not in r1:
        r1[c] = 1
    else:
        r1[c] += 1
r2 = {}
for c in c2:
    if c not in r2:
        r2[c] = 1
    else:
        r2[c] += 1
        
print(x1)
if r1 != {}:
    for k in r1:
        if r1[k] > 1:
            print(f' - remove {r1[k]} {k}\'s')
        else:
            print(f' - remove {r1[k]} {k}')
else:
    print(' - None')
print(x2)
if r2 != {}:
    for k in r2:
        if r2[k] > 1:
            print(f' - remove {r2[k]} {k}\'s')
        else:
            print(f' - remove {r2[k]} {k}')
else:
    print(' - None')