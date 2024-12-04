par = 0
stroke = 0
fix_stroke = []
for i in range(9):
    hole = [int(e) for e in input().split()]
    par += hole[0]
    stroke += hole[1]
    if hole[2] == 1:
        if hole[0]+2 < hole[1]:
            fix_stroke.append(hole[0]+2)
        else:
            fix_stroke.append(hole[1])
            
point_on = int(round(0.8*(1.5*sum(fix_stroke)-par)-0.5,0))
pure_point = stroke - point_on
print(stroke)
print(point_on)
print(pure_point)