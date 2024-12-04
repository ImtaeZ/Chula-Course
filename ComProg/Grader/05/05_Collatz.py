n = int(input())
result = []
result.append(n)
while n != 1:
    if n % 2 == 0:
        n = n//2
    else:
        n = 3*n+1
    result.append(n)
result = [str(e) for e in result]
print('->'.join(result[-15:]))