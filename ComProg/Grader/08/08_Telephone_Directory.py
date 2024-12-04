info_map = {}
for i in range(int(input())):
    info = input().split()
    info_map[info[0] + ' ' + info[1]] = info[2]
    info_map[info[2]] = info[0] + ' ' + info[1]
for i in range(int(input())):
    check = input()
    # check = ' '.join(check)
    if check in info_map:
        print(check, '-->',info_map[check])
    else:
        print(check, '--> Not found')