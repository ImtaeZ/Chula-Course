sud = {}
while True:
    s = input().strip()
    if s == 'q':
        break
    c, a = s.split(', ')
    if a not in sud:
        sud[a] = [c]
    else:
        sud[a].append(c)

for a in sud:
    print(a+': '+', '.join(sud[a]))
