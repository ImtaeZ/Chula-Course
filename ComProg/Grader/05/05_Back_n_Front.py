result = []
n1 = int(input())
k = 0
for i in range(n1):
    d1 = int(input())
    if k%2 == 0:
        result.append(d1)
    else:
        result.insert(0, d1)
    k += 1

d2 = [int(e) for e in input().split()]
for i in range(len(d2)):
    if k%2 == 0:
        result.append(d2[i])
    else:
        result.insert(0, d2[i])
    k += 1

while True:
    d3 = int(input())
    if d3 == -1:
        break
    if k%2 == 0:
        result.append(d3)
    else:
        result.insert(0, d3)
    k += 1

print(result)