# data  = {clip : set(hastag)}
# clips = [clip1,clip2,...]
# user = set()
# for c in input().split():
# if c in data: user.add(data[c])
# for c in clips:
# if c not in clip1,clip2:
#    max.append(len(user.intersection((data[c])))
# else:
#    max.append(0)
# max_v = max(max)
# if max != 0:
#   for h_no in max:
#       if h_no = max: ans.append(h_no)
# else: no suggest clip

info = {}
clips = []
while True:
    data = input().split()
    if data == ['q']:
        break
    clip = data[0]
    hastag = data[1:]
    info[clip] = set(hastag)
    clips.append(clip)
    
u = input().strip().split()
user = set()
for c in u:
    if c in info:
        user = user.union(info[c])

check = []
for c in clips:
    if c not in u:
        check.append(len(user.intersection(info[c])))
    else:
        check.append(0)
max_i = max(check)
if max_i != 0:
    ans = []
    for i in range(len(check)):
        if check[i] == max_i: ans.append(clips[i])
    ans.sort()
    print(' '.join(ans))
else:
    print('No suggested clip')
