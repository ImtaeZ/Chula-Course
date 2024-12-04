fname = input().strip()
k = int(input())

ruler = ''
for i in range(k//10) :
 ruler += '-'*9 + str(i+1) # เพิ่มรอบละ 9 ขีด ตามด้วยตัวเลข
if len(ruler) < k :
 ruler += '-'*(k-len(ruler)) # เพิ่มที่เหลือ (ถ้ามี)
print(ruler)


f = open(fname,'r')
t = []
for l in f:
    w = l.strip().split('.')
    for ew in w:
        t.append(ew)

start = 0
end = 0
while start < len(t):
    line = '.'.join(t[start:end]).strip('.')
    if end > len(t):
        print(line)
        break
    elif end-start == 1 and len(line) > k:
        print(line)
        start = end
    elif len(line) > k:
        line = '.'.join(t[start:end-1]).strip('.')
        print(line)
        start = end-1
        end = end-1
    else:
        end += 1
