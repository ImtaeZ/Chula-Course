filename, year = input().split()
f = open(filename, 'r')
score = []
check = False
for line in f:
    mark = line.strip().split()
    mark = float(mark[-1])
    if line[:2] == year[-2:]:
        score.append(mark)
        check = True
        
if check:
    print(min(score), max(score), sum(score)/len(score))
else:
    print('No data')