n = int(input())
su = set()
si = set()
if n > 0:
    su = set([int(e) for e in input().split()])
    si = su.copy()
for i in range(n-1):
    s = set([int(e) for e in input().split()])
    su |= s
    si &= s
    
print(len(su))
print(len(si))
