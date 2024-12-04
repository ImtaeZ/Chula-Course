def print_triangle(h):
    print('.'*(h-1) + '*') # 1st line
    a = h-2
    b = 1
    for i in range(h-2): # 2nd - 2ndlast
        print('.'*a + '*' + '.'*b + '*')
        a -= 1
        b += 2
    print('*'*(2*h-1)) #last line
        
exec(input())
