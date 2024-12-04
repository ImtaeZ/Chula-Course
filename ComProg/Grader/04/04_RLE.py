t = input()
t += ' '
count = 0
for i in range(len(t)-1):
    if t[i] != t[i+1]:
        print(t[i], count+1,end=' ')
        count = 0
    else:
        count += 1
