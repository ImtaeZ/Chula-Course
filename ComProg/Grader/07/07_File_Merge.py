file = input().split()
f1 = open(file[0],'r')
f2 = open(file[1],'r')

def less(s1,s2):
    if s1[-1] < s2[-1]:
        return True
    if s1[-1] > s2[-1]:
        return False
    return s1 < s2

def read_next(f):
    while True:
        t = f.readline()
        if len(t) == 0: # ถ้าอ่านหมดแล้ว ออกจากวงวน
            break
        x = t.strip().split() # ลบ blank ซ้ายขวา
        if len(x) == 2: # แยกแล้วได้ 2 ส่วน --> ถูกต้อง ก็คืนผล
            return x[0], x[1]
    return "", "" 

st1, g1 = read_next(f1)
st2, g2 = read_next(f2)

while st1 != '' and st2 != '':
    if less(st1,st2):
        print(st1, g1)
        st1, g1 = read_next(f1)
    else:
        print(st2, g2)
        st2, g2 = read_next(f2)
        
while st1 != '':
    print(st1, g1)
    st1, g1 = read_next(f1)
    
while st2 != '':
    print(st2, g2)
    st2, g2 = read_next(f2)
    
f1.close()
f2.close()