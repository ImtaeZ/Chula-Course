cmd = input()
if cmd == 'str2RLE':
    result = []
    count = 1
    st = input() + ' '
    for i in range(len(st)-1):
        if st[i] != st[i+1]:
            print(st[i], count, end=' ')
            count = 1
        else:
            count += 1
elif cmd == 'RLE2str':
    rle = input().split()
    lett = [rle[i] for i in range(len(rle)) if i%2 == 0]
    num = [int(rle[i]) for i in range(len(rle)) if i%2 != 0]
    for i in range(len(lett)):
        print(lett[i]*num[i],end='')
else:
    print('Error')
