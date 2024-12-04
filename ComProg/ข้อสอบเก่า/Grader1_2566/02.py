n,a,b = [int(e) for e in input().split()]
if a > b:
    d,e = -1,-1
    while n < a:
        c = int(input())
        if c > d:
            d,e = c,d
        else:
            if c > e:
                e = c
        n = n+b
else:
    c = int(input())
    d = int(input())
    e = int(input())
    f = int(input())
    if e < f:
        e,f = f,e
    if d < e:
        d,e = e,d
    if c < d:
        c,d = d,c
    if d > e:
        if not d > f:
            d,f = f,d
    elif e > f:
        d,e = e,d
    else:
        d,f = f,d
print(d,e)
