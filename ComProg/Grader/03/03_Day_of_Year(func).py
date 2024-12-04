def day_of_year(d, m ,y):
    y -= 543
    months = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    if (y%400) == 0 or ((y%4)==0 and y%100 != 0):
        months[2] = 29
    return d + sum(months[:m])

exec(input())

# non func ver
# d = int(input())
# m = int(input())
# y = int(input())
# y -= 543
# months = [0,31,28,31,30,31,30,31,31,30,31,30,31]
# if (y%400) == 0 or ((y%4)==0 and y%100 != 0):
#     months[2] = 29
# print(d + sum(months[:m]))