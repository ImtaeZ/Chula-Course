from math import sin, pi

bd, bm, by, d, m, y = [int(e) for e in input().split()]
m1 = [0,31,28,31,30,31,30,31,31,30,31,30,31]
m2 = [0,31,28,31,30,31,30,31,31,30,31,30,31]
by -= 543
y -= 543

if by%400 == 0 or (by%4 == 0 and by%100 != 0):
    m1[2] = 29
if y%400 == 0 or (y%4 == 0 and y%100 != 0):
    m2[2] = 29
        
red = sum(m1[:bm-1:-1]) - bd + 1
black = 365*((y-by)-1)
blue = sum(m2[:m]) + d -1
day = red + black + blue
phy = sin(2*pi*day/23)
emo = sin(2*pi*day/28)
int = sin(2*pi*day/33)
print(day, "{:.2f}".format(phy), "{:.2f}".format(emo), "{:.2f}".format(int))