n = int(input())
result = []
for i in range(n):
    x,y = input().split()
    d = (float(x)**2+float(y)**2)**0.5
    result.append([d, i+1, x, y])
result.sort()
print(f"#{result[2][1]}: ({result[2][2]}, {result[2][3]})")