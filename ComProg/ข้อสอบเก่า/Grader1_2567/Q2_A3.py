pic = []
for i in range(int(input())):
    pic.append(input().strip())
    
cmd = input()
if cmd == 'hflip':
    for line in pic:
        for c in line[::-1]: print(c,end = '')
        print()
elif cmd == 'vflip':
    for line in pic[::-1]:
        for c in line: print(c,end = '')
        print()
