def factor(N):
    ans = []
    k = 2
    while k <= N:
        if N%k == 0:
            c = 0
            while N%k == 0:
                c += 1
                N //= k
            ans.append([k,c])
        k += 1
    return ans

exec(input().strip())