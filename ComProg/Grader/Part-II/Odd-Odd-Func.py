def is_odd(n):
    return n%2 != 0

def has_odds(x):
    for num in x:
        if num%2 != 0:
            return True
    return False

def all_odds(x):
    for num in x:
        if num%2 == 0:
            return False
    return True

def no_odds(x):
    for num in x:
        if num%2 != 0:
            return False
    return True

def get_odds(x):
    return [e for e in x if e%2 != 0]

def zip_odds(a, b):
    odd_a = [e for e in a if e%2 != 0]
    odd_b = [e for e in b if e%2 != 0]
    result = []
    while True:
        if len(odd_a) == 0 or len(odd_b) == 0:
            break
        result.append(odd_a[0])
        result.append(odd_b[0])
        odd_a.pop(0)
        odd_b.pop(0)
    if len(odd_a) == 0:
        result += odd_b
    else:
        result += odd_a
    return result

exec(input().strip())