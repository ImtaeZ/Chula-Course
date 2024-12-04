word = input()
sentence = input()

t = ''
for c in sentence:
    if c in ["\"", "(", ")", ",", ".", "'"]:
        t += ' '
    else:
        t += c

count = 0
for c in t.split():
    if word == c:
        count += 1
        
print(count)
