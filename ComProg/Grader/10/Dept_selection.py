mj = {}
for i in range(int(input())):
    s, a = input().split()
    mj[s] = int(a)

info = []
for i in range(int(input())):
    sid, p, _1,_2,_3,_4 = input().split()
    info.append([float(p),sid,_1,_2,_3,_4])
info.sort()
info.reverse()


ugot = []
for i in info:
    for pak in i[-4:]:
        if mj[pak] > 0:
            ugot.append([i[1],pak])
            mj[pak] -= 1
            break
ugot.sort()
for i in ugot:
    print(' '.join(i))
