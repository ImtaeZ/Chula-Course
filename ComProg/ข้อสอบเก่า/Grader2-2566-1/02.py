# teach = {"AAA":[[sec1,sec2,...],F,M]}
section = {}
gender = {}
filename = input()
teacher = input()
f = open(filename, 'r')
for line in f:
    li = line.strip().split(',')
    if li[4] not in section:
        section[li[4]] = [li[3]]
    else:
        section[li[4]].append(li[3])
    if li[4] not in gender:
        gender[li[4]] = [li[1]]
    else:
        gender[li[4]].append(li[1])

new_sec = {teacher : []}
if teacher in section:
    for num in section[teacher]:
        if num not in new_sec[teacher]:
            new_sec[teacher].append(num)
    f_num = gender[teacher].count('F')
    m_num = gender[teacher].count('M')

if teacher in section and teacher in gender:
    if len(new_sec[teacher]) > 1:
        print(f"Sections: {','.join(new_sec[teacher])} --> F = {f_num}, M = {m_num}")
    else:
        print(f"Section: {','.join(new_sec[teacher])} --> F = {f_num}, M = {m_num}")
else:
    print("Not found")