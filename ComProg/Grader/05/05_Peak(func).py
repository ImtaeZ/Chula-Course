def peaks(x):
    peak = []
    for i in range(1,len(x)-1):
        if x[i] > x[i-1] and x[i] > x[i+1]:
            peak.append(i)
    return peak

exec(input())
