N = int(input())
coupon = []
for i in range(N):
    cp = input().split()
    coupon.append([int(cp[1]), cp[0]])

coupon.sort()
coupon.reverse()
money = int(input())
mon = money
spent = 0
buy = []
while True:
    again = False
    for c in coupon:
        if c[0] <= money and buy.count(c[1]) < 3:
            buy.append(c[1])
            spent += c[0]
            money -= c[0]
            if c[0] < money:
                again = True
            
        if again:
            break
    if not again:
        break

result = {}
buy.sort()
for cp in buy:
    if cp in result:
        result[cp] += 1
    else:
        result[cp] = 1
print(">", mon,mon-money,money)
if buy != []:
    for cp in result:
        print(cp, result[cp])
else:
    print("No coupon")