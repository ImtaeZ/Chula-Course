from math import gcd

a,b,c = input().split(',') # num = [a,b,c]
up = int(a+b+c)-int(a+b)
down = 10**(len(b+c))-10**(len(b))
print(f"{up//gcd(up,down)} / {down//gcd(up,down)}")
