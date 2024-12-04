alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
while True:
    sentence = input()
    if sentence == 'end':
        break
    res = ''
    for c in sentence:
        if c.isupper():
            if alphabets.index(c.lower()) > 12:
                res += alphabets[alphabets.index(c.lower()) - 13].upper()
            else:
                res += alphabets[alphabets.index(c.lower()) + 13].upper()
        elif c.islower():
            if alphabets.index(c.lower()) > 12:
                res += alphabets[alphabets.index(c.lower()) - 13]
            else:
                res += alphabets[alphabets.index(c.lower()) + 13]
        else:
            res += c
    print(res)