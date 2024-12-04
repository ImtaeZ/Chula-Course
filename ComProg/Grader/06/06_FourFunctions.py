def make_int_list(x):
    return [int(e) for e in x.split()]

def is_odd(e):
    if e % 2 != 0:
        return True
    return False

def odd_list(alist):
    return [e for e in alist if is_odd(e)]

def sum_square(alist):
    sqlist = [e**2 for e in alist]
    return sum(sqlist)

exec(input().strip())