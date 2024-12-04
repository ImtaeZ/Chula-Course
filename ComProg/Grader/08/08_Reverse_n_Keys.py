def reverse(d):
    r_d = {}
    for k in d:
        r_d[d[k]] = k
    return r_d

def keys(d, v):
    key_list = []
    for k in d:
        if d[k] == v:
            key_list.append(k)
    return key_list
    
exec(input().strip())