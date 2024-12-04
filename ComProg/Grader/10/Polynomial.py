def add_poly(p1, p2):
    add = dict([[e,c] for c,e in p2])
    for c,e in p1:
        if e in add:
            add[e] += c
        else:
            add[e] = c
    return [(add[e], e)for e in sorted(add)[::-1] if add[e] != 0]

def mult_poly(p1,p2):
    mul = []
    for s1,y1 in p1:
        for s2,y2 in p2:
            mul.append((s1*s2,y1+y2))
    return add_poly(mul, [(0,0)])

for i in range(3):
    exec(input().strip())
