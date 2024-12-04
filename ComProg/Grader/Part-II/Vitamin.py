n = int(input())
f_list_str = []
f_list = []
for i in range(n):
    fr_list = []
    fr_str = []
    f = input().split()
    fr_list.append(f[0])
    fr_str.append(f[0])
    for i in range(1,len(f)):
        fr_str.append(f[i])
        fr_list.append(float(f[i]))
    f_list.append(fr_list)
    f_list_str.append(fr_str)
    
c = input().split()
if c[0] == 'show':
    for fruit in f_list_str:
        print(' '.join(fruit))
elif c[0] == 'max':
    v = int(c[1])
    v_max = 0
    f_list.sort()
    for fruit in f_list:
        if fruit[v] > v_max:
            f_max, v_max = fruit, fruit[v]
    print(f_max[0], f_max[v])
elif c[0] == 'avg':
    v = int(c[1])
    sums = 0
    for fruit in f_list:
        sums += fruit[v]
    print(round(sums/len(f_list), 4))
elif c[0] == 'get':
    for i in range(len(f_list_str)):
        if f_list_str[i][0] == c[1]:
            s = i
            break
        else:
            s = -1
    if s != -1:
        print(' '.join(f_list_str[s]))
    else:
        print(c[1], 'not found')
elif c[0] == 'sort':
    v = int(c[1])
    v_list = []
    for fruit in f_list:
        v_list.append([fruit[v], fruit[0]])
    v_list.sort()
    for vitamins, fruit in v_list:
        print(fruit, end=' ')