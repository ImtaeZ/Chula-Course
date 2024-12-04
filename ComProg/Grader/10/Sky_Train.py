s_map = {}
while True:
    st = input().split()
    if len(st) < 2: break
    if st[0] in s_map:
        s_map[st[0]].add(st[1])
    else:
        s_map[st[0]] = {st[1]}
    if st[1] in s_map:
        s_map[st[1]].add(st[0])
    else:
        s_map[st[1]] = {st[0]}
        
on = st[0]
go = set()
if on in s_map:
    for sta in s_map[on]:
        for sta2 in s_map[sta]:
                go.add(sta2)
        go.add(sta)
    for st in sorted(go):
        print(st)
else:
    print(on)
