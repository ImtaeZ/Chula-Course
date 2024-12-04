num = input().split()

x1,x2,x3,x4 = [float(x) for x in num]
max = x1
min = x1
if x1 > x2:
    max = x1
if x2 > x1:
    max = x2
if x3 > max:
    max = x3
if x4 > max:
    max = x4
if x1 < x2:
    min = x1
if x2 < x1:
    min = x2
if x3 < min:
    min = x3
if x4 < min:
    min = x4
    
print(round(((x1+x2+x3+x4-min-max)/2),2))
