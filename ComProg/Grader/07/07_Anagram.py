sen1 = [c.lower() for c in input().replace(' ','')]
sen1.sort()
sen2 = [c.lower() for c in input().replace(' ','')]
sen2.sort()

if sen1 == sen2:
    print("YES")
else:
    print("NO")