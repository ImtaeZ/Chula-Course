def letter_point(c):
    if c in 'AEILNORSTU':
        return 1
    if c in 'DG':
        return 2
    if c in 'BCMP':
        return 3
    if c in 'FHVWY':
        return 4
    if c == 'K':
        return 5
    if c in 'JX':
        return 8
    if c in 'QZ':
        return 10
    
def word_point(w):
    point = 0
    for c in w:
        point += letter_point(c)
    return point

words = input().split()
w_p = [[-word_point(w), w] for w in words] # HIGHLIGHTS
w_p.sort()
for i in range(len(w_p)):
    print(w_p[i][1], -w_p[i][0])