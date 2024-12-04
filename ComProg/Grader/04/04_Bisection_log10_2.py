a = float(input())
a0 = a
L = 0
U = 0
while a0 > 0:
    a0 //= 10
    U += 1

b = (U+L)/2
while not abs(a-10**b) <= 10**(-10)*max(a,10**b):
    if 10**b > a:
        U = b
    else:
        L = b
    b = (U+L)/2

print(round(b,6))
