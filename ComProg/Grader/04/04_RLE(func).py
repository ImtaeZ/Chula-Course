def RLE(t):
    t += ' '
    result = []
    count = 0
    for i in range(len(t)-1):
        if t[i] != t[i+1]:
            result.append([t[i], count+1])
            count = 0
        else:
            count += 1
    return result

exec(input())
