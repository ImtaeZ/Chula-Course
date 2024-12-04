ids = []
grades = []
grade = ['F','D','D+','C','C+','B','B+','A']
while True:
    data = input().split()
    if len(data) == 1:
        break
    ids.append(data[0])
    grades.append(data[1])
    
uids = input().split()
for uid in uids:
    if grades[ids.index(uid)] != 'A':
        new_g = grade.index(grades[ids.index(uid)]) + 1
        grades[ids.index(uid)] = grade[new_g]
    
for i in range(len(ids)):
    print(ids[i], grades[i])
