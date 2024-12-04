def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append( float(e) )
        m.append(r)
    return m

def mult_c(c, A):
    new_A = []
    for row in A:
        new_A.append([c*e for e in row])
    return new_A

def mult(A,B):
    rA = len(A)
    cA = len(A[0])
    rB = len(B)
    cB = len(B[0])
    C = [[0]*cB for i in range(rA)]# rA x cB
    for i in range(rA):
        for j in range(cB):
            C[i][j] = 0
            for k in range(cA):
                C[i][j] += A[i][k]*B[k][j]
    return C
exec(input().strip())
