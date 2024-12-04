def knows(R, x, y):
    return y in R[x]

def is_celeb(R,x):
    if len(R[x]) > 1:
        return False
    for n in R:
        if x not in R[n] and n != x:
            return False
    return True

def find_celeb(R):
    for x in R:
        if is_celeb(R,x):
            return x
    return None

def read_relations():
    R = dict()
    while True:
        d = input().split()
        if len(d) == 1: break
        if d[0] not in R:
            R[d[0]] = set()
        if d[1] not in R:
            R[d[1]] = set()
        R[d[0]].add(d[1])
    return R

def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None :
        print('Not Found')
    else:
        print(c)
exec(input().strip())

