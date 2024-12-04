N = int(input())
for i in range(N):
    nums = []
    face = []
    cards = input().split('|')[1:-1]
    for card in cards:
        nums.append(card[0])
        face.append(card[1])
    if nums == ['A','K','Q','J','X'] and len(set(face)) == 1:
        print("Royal Straight Flush")
    elif ''.join(nums) in 'AKQJX98765432A' and len(set(face)) == 1:
        print("Straight Flush")
    elif ''.join(nums) in 'AKQJX98765432A':
        print("Straight")
    elif len(set(face)) == 1:
        print("Flush")
    else:
        print('None')
