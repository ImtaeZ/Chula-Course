def tosec(t):
    m,s = [int(e) for e in t.split(':')]
    return m*60 + s
def tomin(t):
    m = t//60
    t -= m*60
    return str(m)+':'+('0'+str(t))[-2:]

N = int(input())
genre = {}
for i in range(N):
    line = input().split(', ')
    g = line[-2]
    t = line[-1]
    if g not in genre:
        genre[g] = tosec(t)
    else:
        genre[g] += tosec(t)

genre = [(t,g) for g,t in genre.items()]
genre.sort()
for t,g in genre[::-1][:3]:
    print(f"{g} --> {tomin(t)}")