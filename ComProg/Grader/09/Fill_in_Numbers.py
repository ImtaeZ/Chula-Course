def pattern1(nrows, ncols):
    l = [[0]*ncols for i in range(nrows)]
    x = 1
    for i in range(nrows):
        for j in range(ncols):
            l[i][j] = x
            x += 1
    return l

def pattern2(nrows, ncols):
    l = [[0]*ncols for i in range(nrows)]
    x = 1
    for j in range(ncols):
        for i in range(nrows):
            l[i][j] = x
            x += 1
    return l

def pattern3(N):
    l = [[0]*N for i in range(N)]
    x = 1
    for i in range(N):
        for j in range(i,N):
            l[i][j] = x
            x += 1      
    return l

def pattern4(N):
    l = [[0]*N for i in range(N)]
    x = 1
    for c in range(N):
        for r in range(c,-1,-1):
            l[r][c] = x
            x += 1      
    return l

def pattern5(N):
    l = [[0]*N for i in range(N)]
    x = 1
    for d in range(N):
        for r in range(N-d):
            c = r + d
            l[r][c] = x
            x += 1
    return l

def pattern6(N):
    l = [[0]*N for i in range(N)]
    x = 1
    for d in range(N):
        if d%2 == 0:
            for r in range(N-d):
                c = r + d
                l[r][c] = x
                x += 1
        else:
            for r in range(N-d-1,-1,-1):
                c = r + d
                l[r][c] = x
                x += 1
    return l
exec(input().strip())
