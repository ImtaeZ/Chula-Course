def convex_polygon_area(p):
    area = 0
    p += [p[0]]
    for i in range(len(p)-1):
        area += (p[i][0] * p[i+1][1])/2
        area -= (p[i][1] * p[i+1][0])/2
    return abs(area)

def is_heterogram(s):
    check = []
    for c in s:
        if c.lower() in 'abcdefghijklmnopqrstuvwxtz':
            if c.lower() not in check:
                check.append(c.lower())
            else:
                return False
    return True

def replace_ignorecase(s, a, b):
    t = ''
    k = 0
    for i in range(len(s)):
        if k == len(s):
            break
        if s[k:len(a)+k].lower() == a.lower():
            t += b
            k += len(a)
        else:
            t += s[k]
            k += 1
    return t

def top3(votes):
    name = []
    score = []
    vote = dict(sorted(votes.items()))
    print(vote)
    for k in vote:
        name.append(k)
        score.append(vote[k])
    result = [] 
    while name != []:
        result.append(name[score.index(max(score))])
        name.pop(score.index(max(score)))
        score.pop(score.index(max(score)))
    return result[:3]

for k in range(2):
    exec(input().strip())