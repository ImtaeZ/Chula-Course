from math import pi, e, sqrt
n = int(input())
n1 = sqrt(2*pi) * n**(n+0.5) * e**(-n+(1/(12*n + 1)))
n2 = sqrt(2*pi) * n**(n+0.5) * e**(-n + (1/(12*n)))
print(n1)
print(n2)