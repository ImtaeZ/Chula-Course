N = int(input())
k = 2
x,y = input().split()
zig_min, zig_max = int(x), int(y)
zag_max, zag_min = int(x), int(y)
for i in range(N-1):
    x,y = input().split()
    x,y = int(x), int(y)
    if i % 2 == 0:
        x,y = y,x
    zig_min = min(zig_min,x)
    zig_max = max(zig_max,y)
    zag_min = min(zag_min,y)
    zag_max = max(zag_max,x)
    k += 1
    
cmd = input()
if cmd == 'Zig-Zag':
    print(zig_min, zig_max)
else:
    print(zag_min, zag_max)
