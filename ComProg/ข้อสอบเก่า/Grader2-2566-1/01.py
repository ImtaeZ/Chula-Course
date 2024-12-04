data = [int(e) for e in input().split()]
data.sort()

if len(data)%2 == 0:
    Q1 = data[(len(data)//2-1)//2]
    Q3 = data[(len(data)//2)+(len(data)//2-1)//2]
else:
    Q1 = (data[(len(data)//2)//2-1] + data[(len(data)//2)//2])/2
    Q3 = (data[len(data)//2+len(data)//4] + data[len(data)//2+len(data)//4+1])/2

IQR = Q3-Q1
L = Q1 - 1.5*IQR
U = Q3 + 1.5*IQR
out = []
for num in data:
    if not L <= num <= U:
        out.append(num)
        
out = [str(e) for e in out]
if out != []:
    print(f"L = {L} U = {U}")
    print(" ".join(out))
else:
    print(f"L = {L} U = {U}")
    print("Not found")
