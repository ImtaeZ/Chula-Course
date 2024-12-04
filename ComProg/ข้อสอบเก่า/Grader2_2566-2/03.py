filename = input()
f = open(filename, 'r')
word = []
for l in f:
    if l != '\n':
        word += l.strip().split('_')
    
print('-'*50)
t = word[0]
fw = False
for i in range(1,len(word)):
    if len(t+word[i]) + 1 <= 50:
        t += '_' + word[i]
    else:
        print(t)
        t = word[i]

print(t)