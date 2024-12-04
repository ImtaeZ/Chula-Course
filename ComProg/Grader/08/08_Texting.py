t2k = {'a':'2','b':'22','c':'222','d':'3','e':'33','f':'333','g':'4','h':'44','i':'444','j':'5',\
       'k':'55','l':'555','m':'6','n':'66','o':'666','p':'7','q':'77','r':'777','s':'7777','t':'8','u':'88','v':'888','w':'9','x':'99','y':'999','z':'9999',' ':'0'}
k2t = {}
for alpha in t2k:
    k2t[t2k[alpha]] = alpha

def text2keys(text):
    t = []
    for c in text:
        if c == ' ' or 'a' <= c.lower() <= 'z':
            t.append(t2k[c.lower()])
    return ' '.join(t)

def keys2text(keys):
    k = keys.split()
    ans = ''
    for ids in k:
        ans += k2t[ids]
    return ans

exec(input().strip())