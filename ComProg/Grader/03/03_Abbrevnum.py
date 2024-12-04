subs = int(input())
n = len(str(subs))
if n < 4:
    print(subs)
elif n < 7:
    if n == 4:
        print(str(round(subs/10**3,1)) + 'K')
    else:
        print(str(int(round(subs/10**3,0))) + 'K')
        
elif n < 10:
    if n == 7:
        print(str(round(subs/10**6,1)) + 'M')
    else:
        print(str(int(round(subs/10**6,0))) + 'M')
        
else:
    if n == 10:
        print(str(round(subs/10**9,1)) + 'B')
    else:
        print(str(int(round(subs/10**9,0))) + 'B')