def print_square(S):
 # เรยีกใชฟ้ ังกช์ นั นเี้พอื่ แสดงคา่ ของ S ที่เป็นลิสต์ของลิสต์ของจ านวนเต็ม
 for i in range(len(S)):
     print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))
 
# = [ [],
#     [],
#     [] ]
# row = n-1//2 -> append(x) ; x = 1
# x += 1
# row.append(x); x+= 1
# row -= 1
# row.append(x),row.insert(x,0), row.insser(x,0) x+=1 each time
# row += 1 row.inser(x,0) x+= 1
# row += 1 row.append(x) 3 times x+= 1 each time
# while x <= S**2: 
# right = 2
# up = 2
# left = 3
# down = 3
# += 2 all
def spiral_square(S):
    x = 2
    right = 1
    left = 2
    up = 1
    down = 2
    res = []
    row = (S-1)//2
    stop = False
    for i in range(S):
        res.append([])
    res[row].append(1)
    while x <= S**2:
        for i in range(right):
            if x > S**2:
                stop = True
                break
            res[row].append(x)
            x += 1
        if stop:
            break
        right += 2
        for i in range(up):
            row -= 1
            res[row].append(x)
            x += 1
        up += 2
        for i in range(left):
            res[row].insert(0,x)
            x += 1
        left += 2
        for i in range(down):
            row += 1
            res[row].insert(0,x)
            x += 1
        down += 2
    return res
    
exec(input().strip())
