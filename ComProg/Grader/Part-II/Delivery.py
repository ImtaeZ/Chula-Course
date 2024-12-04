result = []
while True:
    month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    deli = {'E':1, 'Q':3, 'N':7, 'F':14}
    check = True
    line = input().strip()
    if line == 'END':
        break
    did, de, d, m, y = line.split()
    d, m, y = int(d), int(m), int(y)
    y1 = y - 543
    if y1%400 == 0 or (y1%4 == 0 and y1%100 != 0):
        month[2] = 29
    if y < 2558:
        print(f'Error: {line} --> Invalid year')
        check = False
    elif not 1 <= m <= 12:
        print(f'Error: {line} --> Invalid month')
        check = False
    elif not 1 <= d <= month[m]:
        print(f'Error: {line} --> Invalid date')
        check = False
    elif de not in ['E','Q','N','F']:
        print(f'Error: {line} --> Invalid delivery type')
        check = False
        
    if check:
        diff = month[m] - d
        if deli[de] > diff and m == 12:
            d = deli[de] - diff
            m = 1
            y += 1
        elif deli[de] > diff:
            d = deli[de] - diff
            m += 1
        else:
            d += deli[de]
        result.append([y,m,d,did])
result.sort()
for l in result:
    print(f"{l[3]}: delivered on {l[2]}/{l[1]}/{l[0]}")