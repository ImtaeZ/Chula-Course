card = input().split()
cmd = input()
card_len = len(card)
for char in cmd:
    if char == 'C':
        card = card[card_len//2:] + card[:card_len//2]
    elif char == 'S':
        s = ['']*card_len
        s[::2] = card[:card_len//2]
        s[1::2] = card[card_len//2:]
        card = s

print(' '.join(card))