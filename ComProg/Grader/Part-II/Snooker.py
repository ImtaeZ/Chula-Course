score = {'R':1, 'Y':2, 'G':3, 'W':4, 'B':5, 'P':6, 'K':7, 'X':0}
p1 = 0
p2 = 0
while True:
    play = input()
    if play[1] == 'R':
        if play[0] == '1':
            p1 += 1 + score[play[2]]
        else:
            p2 += 1 + score[play[2]]
    else:
        if play[0] == '1':
            p1 += score[play[1]]
        else:
            p2 += score[play[1]]
    if play[1] == 'K':
        break
    
print(p1,p2)
if p1 > p2:
    print("Player 1 wins")
elif p1 < p2:
    print("Player 2 wins")
else:
    print("Tie")