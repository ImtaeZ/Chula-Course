n = int(input())
k = int(input())

if  n < 1 and k < 1:
    print('Invalid n and k')
elif n < 1:
    print('Invalid n')
elif k < 1:
    print('Invalid k')
else:
    out = ''
    for i in range(1,k+1):
        if i < k:
            out += (str(i) + '-'*(n))[:n+1]
        else:
            out += (str(i) + '-'*(n))[:n]
    print(out)
    st = ['0','1']
    for i in range(n-1):
        st_r = st.copy()
        st += st[::-1]
        for i in range(len(st)//2):
            st[i] = '0' + st[i]
        for i in range(len(st)//2,len(st)):
            st[i] = '1' + st[i]
    j = 0
    while True:
        ans = st[j:j+k]
        if len(ans) < k:
            print(','.join(ans))
            break
        print(','.join(ans))
        j += k
