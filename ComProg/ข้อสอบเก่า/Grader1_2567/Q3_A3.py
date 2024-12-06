Q1 = [int(e) for e in input().split()]
Q2 = [int(e) for e in input().split()]
Q3 = [int(e) for e in input().split()]
alls = []
for i in range(len(Q1)):
    alls.append([Q1[i],Q2[i],Q3[i]])
    
for i in range(len(Q1),len(Q2)):
    alls.append([Q2[i],Q3[i]])
    
for i in range(len(Q2),len(Q3)):
    alls.append([Q3[i]])
    
score = []
for q in alls:
    score.append(max(q))
    
print(sum(score))
