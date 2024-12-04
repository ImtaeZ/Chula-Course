p1 = input().replace(',','').split()[::-1]
p2 = input().replace(',','').split()[::-1]
month = ['January','February','March','April','May','June','July','August','September','October','November','December']
p1[2] = month.index(p1[2])
p2[2] = month.index(p2[2])
p1[1],p1[2] = p1[2],p1[1]
p2[1],p2[2] = p2[2],p2[1]
p1[2] = int(p1[2])
p2[2] = int(p2[2])
name = [p1.pop(),p2.pop()]
if p1 == p2:
    print(' '.join(name))
else:
    if p1 < p2:
        print(name[0])
    else:
        print(name[1])
