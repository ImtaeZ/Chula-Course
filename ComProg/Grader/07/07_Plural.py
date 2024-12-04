word = input()
if word[-1] == 's' or word[-1] == 'x':
    word += 'es'
elif word[-2:] == 'ch':
    word += 'es'
elif word[-1] == 'y' and word[-2] not in 'aeiou':
    word = word[:-1] + 'ies'
else:
    word += 's'
    
print(word)