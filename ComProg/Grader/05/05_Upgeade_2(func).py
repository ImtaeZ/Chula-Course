def index_of(grades, ID):
    id = []
    for item in grades:
        id.append(item[0])
    if ID in id:    
        return id.index(ID)
    else:
        return -1

def upgrade(grades, IDs):
    grade_levels = ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A']
    grades.sort()
    for item in IDs:
        i = index_of(grades, item)
        if i != -1:
            g_i = grade_levels.index(grades[i][1])
            if g_i < 7:
                grades[i][1] = grade_levels[g_i+1]

exec(input())
exec(input())
exec(input())