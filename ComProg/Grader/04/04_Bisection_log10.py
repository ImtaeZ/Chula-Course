a = float(input())
L = 0
U = a
x = (U+L)/2
while not abs(a-10**x) <= (10**-10)*max(a,10**x):
    if 10**x > a:
        U = x
    else:
        L = x
    x = (U+L)/2   

print(round(x,6))