N = int(input())
price = {}
for i in range(N):
    ic, p = input().split()
    price[ic] = float(p)
    
M = int(input())
sales = {}
t = 0
for i in range(M):
    ic, k = input().split()
    if ic in price:
        s = price[ic]*int(k)
        if ic in sales:
            sales[ic] += s
        else:
            sales[ic] = s
        t += s

if t == 0:
    print('No ice cream sales')
else:
    m = []
    for ic in sales:
        m.append([sales[ic], ic])
    mx = []
    for s, ic in m:
        if s == max(m)[0]:
            mx.append(ic)
    mx.sort()
    print('Total ice cream sales:',t)
    print('Top sales:', ', '.join(mx))
