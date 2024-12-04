x = input().split()
c = float(x[0])
n = int(x[1])
ans = []
for i in range(n):
    c_floor = int(c//1)
    ans.append(str(c_floor))
    if c-c//1 <= 10**-10 or c-c//1 == 0:
        break
    c = 1/(c-c_floor)
    
print(', '.join(ans))