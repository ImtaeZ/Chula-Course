def f1(a, b, c):
    check = [a,b,c]
    for num in check:
        if num < 0:
            check.remove(num)
    return min(check)

def f2(a, b, c):
    check = [a,b,c]
    for num in check:
        if num >= 0:
            check.remove(num)
    return max(check)

def f3(a,b,c):
    return str(abs(a+b+c))[0]

def f4(a,b,c):
    return str(abs(a+b+c))[-1]

def main():
    s1,s2,a,b,c = [int(e) for e in input().split()]
    if s1 == 0 and s2 == 0:
        print(f1(a,b,c))
    elif s1 == 0 and s2 == 1:
        print(f2(a,b,c))
    elif s1 == 1 and s2 == 0:
        print(f3(a,b,c))
    elif s1 == 1 and s2 == 1:
        print(f4(a,b,c))
    else:
        print("Error")
        

exec(input().strip())
