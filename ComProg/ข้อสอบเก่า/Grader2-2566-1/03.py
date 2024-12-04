N = int(input())
character = []
for i in range(N):
    c = input()
    character.append('*' + c)

t = []
not_closed = False
while True:
    not_first = False
    line = input()
    if line == 'END':
        break
    if line[0] == '*':
        for c in character:
            if c in line:
                if line.find('"', line.find('"')+1) == -1:
                    not_closed = True
                    t.append(line[1:])
                else:
                    t.append(line[1:line.find('"', line.find('"')+1)+1])
    else:
        if not_closed:
            if line.find('"') == -1:
                t.append(line)
            else:
                t.append(line[:line.find('"')+1])
                not_closed = False

if t != []:
    for line in t:
        print(line)
else:
    print('Maybe wrong novel')