def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a


def is_coprime(a, b, c):
    if gcd(a,b) == 1:
        return True
    if gcd(a,c) == 1:
        return True
    if gcd(b,c) == 1:
        return True
    return False

def primitive_Pythagorean_triples(max_len):
    tri = []
    for c in range(3, max_len+1):
        for a in range(3, c):
            for b in range(a, c):
                if a**2 + b**2 == c**2 and is_coprime(a,b,c):
                    tri.append([a,b,c])
                    
    return tri
exec(input().strip())