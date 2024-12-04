# info  = {name : set(friends)}
# names.sort()
# for n in names:
# if name in : list.append(len(info[n]))
# else: list.append(('n',0))

def read_friends():
    dat = []
    N = int(input())
    for i in range(N):
        dat.append(tuple(input().strip().split()))
    return dat
def count_friends(data, names):
    info = {}
    for cp in data:
        name,friend = cp
        if name not in info:
            info[name] = {friend,}
        else:
            info[name].add(friend)
        if friend not in info:
            info[friend] = {name,}
        else:
            info[friend].add(name)
    ans = []
    for n in sorted(names):
        if n in info:
            ans.append((n, len(info[n])))
        else:
            ans.append((n, 0))
    return ans
exec(input().strip())
