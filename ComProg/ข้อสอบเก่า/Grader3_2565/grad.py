# s_f = [student:faculty]
# g_s = [guset : [student]]
# for i in range(k):
# guests = input().split()
# check = set()
# for  s in g_s[guests[0]]:
#    check.add(s_f[s])
# for g in guests[1:]:
#    fac = set()
#    for s g_s[g]:
#       fac.add(s_f[s])
#    check = check.intersection(fac)

N,M,K = [int(e) for e in input().split()]
s_f = {}
for i in range(N):
    st, fa = input().split()
    s_f[st] = fa

g_s = {}
for i in range(M):
    x = input().split()
    gu = x[0]
    st = x[1:]
    g_s[gu] = st
    
for i in range(K):
    guests = input().split()
    check = set()
    for s in g_s[guests[0]]:
        check.add(s_f[s])
    for g in guests[1:]:
        fac = set()
        for s in g_s[g]:
            fac.add(s_f[s])
        check = check.intersection(fac)
    
    if check != set():
        print(' '.join(sorted(check)))
    else:
        print('None')
