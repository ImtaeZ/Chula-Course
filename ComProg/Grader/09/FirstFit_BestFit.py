def first_fit(L, e):
    for box in L:
        if sum(box)+e <= 100:
            box.append(e)
            return L
    L.append([e])
    return L

def best_fit(L, e):
    q = []
    for x in L:
        if 100-(sum(x))-e >= 0:
            q.append(100-sum(x)-e)
        else:
            q.append(100)
    if q == []:
        q.append(100)
    m = min(q)
    if m == 100:
        L.append([e])
    else:
        L[q.index(m)].append(e)
    return L
            
def partition_FF(D):
    ff = [[D[0]]]
    for i in range(1,len(D)):
        ff = first_fit(ff, D[i])
    return ff

def partition_BF(D):
    bf = [[D[0]]]
    for i in range(1,len(D)):
        bf = best_fit(bf, D[i])
    return bf

exec(input().strip())
