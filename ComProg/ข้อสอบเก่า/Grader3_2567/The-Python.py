em_sale = {}
linked = {}

for i in range(int(input())):
    em, boss, sale = input().split(',')
    em_sale[em] = int(sale)
    if boss not in linked:
        linked[boss] = [em]
    else:
        linked[boss].append(em)
        
BigBoss = []
for boss in linked:
    if boss not in em_sale:
        BigBoss.append(boss)
        em_sale[boss] = 0
        
def Total_sales(boss):
    total = 0
    if boss not in linked:
        return em_sale[boss]
    total += em_sale[boss]
    for em in linked[boss]:
        total += Total_sales(em)
        
    return total

salenboss = []
for b in BigBoss:
    salenboss.append([Total_sales(b), b])
    
salenboss.sort()
salenboss.reverse()
for sale, boss in salenboss:
    print('Boss',boss,sale)
