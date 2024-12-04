h = int(input())
w = 2*h - 1
# 1st row
print('.'*(h-1) + '*')
# 2nd to 2nd last row
for i in range(h-2):
    print('.'*(h-(2+i)) + '*' + '.'*(2*i+1) + '*')
# last row
print('*'*w)
