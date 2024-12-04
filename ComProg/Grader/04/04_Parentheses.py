n = input()
t = ''
for ch in n:
    if ch == '(':
        t += '['
    elif ch == '[':
        t += '('
    elif ch == ')':
        t += ']'
    elif ch == ']':
        t += ')'
    else:
        t += ch

print(t)
