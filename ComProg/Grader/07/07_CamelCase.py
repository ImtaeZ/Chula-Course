t = input()
word = ''
for e in t:
    if '0' <= e <= '9' or 'a' <= e.lower() <= 'z':
        word += e
    else:
        word += ' '

w_list = word.strip().split()
result = ''.join(w_list[0]).lower()
for i in range(1,len(w_list)):
    result += w_list[i].capitalize()

print(result)