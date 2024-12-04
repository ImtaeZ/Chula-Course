c = input()
t = input()
d = input()
cf = open(c,'r')
tf = open(t, 'r')
df = open(d, 'r')
course = {}
teacher = {}
for line in cf:
    ids, co = line.strip().split(',')
    course[ids] = co
for line in tf:
    ids, co = line.strip().split(',')
    teacher[ids] = co
    
for line in df:
    ci, ti = line.strip().split(',')
    if ci in course and ti in teacher:
        print(course[ci]+','+teacher[ti])
    else:
        print('record error')
        
cf.close()
tf.close()
df.close()