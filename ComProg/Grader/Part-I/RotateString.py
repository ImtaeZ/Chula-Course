cmd = input().strip()
n = int(input())
check = True
pic = []
line1 = input().strip()
pic.append(line1)
for i in range(n-1):
    line = input().strip()
    if len(line) != len(line1):
        check = False
        break
    pic.append(line)
if check:
    if cmd == '90':
        for i in range(len(line1)):
            for j in range(len(pic)):
                print(pic[-(j+1)][i],end = '')
            print('')
    if cmd == 'flip':
        for i in range(len(pic)):
            print(pic[i][::-1])
    if cmd == '180':
        for i in range(len(pic)):
            print(pic[-(i+1)][::-1])
else:
    print('Invalid size')