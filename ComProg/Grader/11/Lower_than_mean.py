import numpy as np
def read_data():
 # อ่านข ้อมูลจากแป้นพิมพ์ จากนั้นสร้างและคืนอาเรย์สองตัว
 # weight เป็นอาเรย์สามชอ่ งเก็บน ้าหนักของคะแนนกลางภาค ปลายภาค และโครงงาน (float)
 # data เป็นอาเรย์ขนาด n4 เก็บข ้อมูลนักเรียน n คน แต่ละคนมีข ้อมูล
 # เลขประจ าตัว คะแนนกลางภาค ปลายภาค และโครงงาน (int)
 w = [float(e) for e in input().split()]
 weight = np.array(w)
 n = int(input())
 data = np.ndarray((n, 4), int)
 for i in range(n):
     data[i] = [int(e) for e in input().split()]
 return weight, data



def report_lower_than_mean(w,d):
    total = 0
    for r in range(len(d)):
        total += float(d[r,1:].dot(w))
    avg = total / len(d)
    noob = []
    for r in range(len(d)):
        if float(d[r,1:].dot(w)) < avg:
            noob.append(str(d[r][0]))
        
    if noob != []:
        print(', '.join(noob))
    else:
        print('None')
    
exec(input().strip())
