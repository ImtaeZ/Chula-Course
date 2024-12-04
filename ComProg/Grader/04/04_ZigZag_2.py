x,y = input().split()
zig_min, zig_max = int(x), int(y)
zag_min, zag_max = int(y), int(x)
i = 2
while True:
    d = input().split()
    if len(d) == 1: 
        break
    x, y = int(d[0]), int(d[1])
    if i%2 == 0:
        x, y = y, x
    zig_min = min(zig_min,x)
    zig_max = max(zig_max,y)
    
    zag_min = min(zag_min,y)
    zag_max = max(zag_max,x)
    i += 1
    
if d[0] == 'Zig-Zag':
    print(zig_min, zig_max)
if d[0] == 'Zag-Zig':
    print(zag_min, zag_max)