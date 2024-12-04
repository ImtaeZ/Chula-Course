bd, money, lenth, start = input().split()
bd_month = int(bd.split('/')[1])
money, lenth, start = int(money), int(lenth), int(start)

for i in range(1, lenth+1):
    if i % 4 == 1 :
        interest = 1/1200
    elif i % 4 == 2:
        interest = 2/1200
    elif i % 4 == 3:
        interest = 3/1200
    else:
        interest = 4/1200
    if start % 12 == bd_month or (start % 12 == 0 and bd_month == 12):
        interest += 1/1200
    money += money*interest
    start += 1
    
print(round(money,2))
