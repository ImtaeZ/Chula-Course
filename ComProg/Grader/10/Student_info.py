# info = {name : [g,y,c]}
info = {}
show = {}
for i in range(int(input())):
    name, g, y, c = input().split()
    info[name] = {g,y,c}
    show[name] = [g,y,c]

check = set(input().split())
ans = []
for name in info:
    if check.issubset(info[name]):
        ans.append(name)
        
if ans != []:
    for name in sorted(ans):
        print(name, ' '.join(show[name]))
else:
    print('Not Found')
