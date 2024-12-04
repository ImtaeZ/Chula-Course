docs = {}

for i in range(int(input())):
    doc = input()
    words = input().split()
    docs[doc] = words
    
while True:
    w = input()
    if w == '-1':
        break
    involve = []
    for doc in docs:
        if w in docs[doc]:
            f = docs[doc].count(w)/len(docs[doc])
            fj = 1/len(set(docs[doc]))
            involve.append([f*fj,doc])
    involve.sort()
    involve.reverse()
    if involve != []:
        print(involve[0][1])
    else:
        print('NOT FOUND')
