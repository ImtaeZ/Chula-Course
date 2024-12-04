y = [int(e) for e in input().split()]
peak = 0
for i in range(1,len(y)-1):
    if y[i] > y[i-1] and y[i] > y[i+1]:
        peak += 1
        
print(peak)