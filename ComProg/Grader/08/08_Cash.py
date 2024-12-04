def total(pocket):
    count = 0
    for key in pocket:
        count += key*pocket[key]
    return count

def take(pocket, money_in):
    for money in money_in:
        if money in pocket:
            pocket[money] += money_in[money]
        else:
            pocket[money] = money_in[money]

def pay(pocket, amt):
    pay = {}
    for m in sorted(pocket.keys())[::-1]:
        if amt >= m:
            c = min(pocket[m], amt//m)
            pay[m] = c
            pocket[m] -= c
            amt -= m*c
    if amt > 0:
        take(pocket, pay)
        pay = {}
    return pay
exec(input().strip())