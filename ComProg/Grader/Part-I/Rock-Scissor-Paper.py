m = int(input())
match_count = 0
score1 = 0
score2 = 0
check = True
while True:
    if score1 == m or score2 == m:
        break
    if match_count == 3*m:
        check = False
        break
    p1,p2 = input().split()
    if p1 != p2:
        if p1 == 'R' and p2 =='S':
            score1 += 1
        if p1 == 'R' and p2 =='P':
            score2 += 1
        if p1 == 'P' and p2 =='S':
            score2 += 1
        if p1 == 'P' and p2 =='R':
            score1 += 1
        if p1 == 'S' and p2 =='R':
            score2 += 1
        if p1 == 'S' and p2 =='P':
            score1 += 1
    match_count += 1
if check:    
    if score1 > score2:
        print(score1,score2)
        print('Player 1 wins')
    elif score2 > score1:
        print(score1,score2)
        print('Player 2 wins')
    else:
        print(score1,score2)
        print('Tie')
else:
    print(score1,score2)
    print('Tie')