N = int(input())
names = {}
for i in range(N):
    fn, nn = input().split()
    names[fn] = nn
    names[nn] = fn

M = int(input())
for i in range(M):
    n = input()
    if n in names:
        print(names[n])
    else:
        print('Not found')
