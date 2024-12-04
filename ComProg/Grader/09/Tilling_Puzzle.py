def row_number(t,e):
    for i in range(len(t)):
        if e in t[i]:
            return i
    return None

def flatten(t):
    l = []
    for row in t:
        for num in row:
            if num != 0:
                l.append(num)
    return l

def inversions(x):
    c = 0
    for i in range(len(x)-1):
        for j in range(i+1,len(x)):
            if x[i] > x[j]:
                c += 1
    return c

def solvable(t):
    row_len = len(t)
    zerow = row_number(t, 0)
    inv_num = inversions(flatten(t))
    if (row_len%2!=0 and inv_num%2==0) or (row_len%2==0 and inv_num%2!=0 and zerow%2==0) or (row_len%2==0 and inv_num%2==0 and zerow%2!=0):
        return True
    return False

exec(input().strip())
