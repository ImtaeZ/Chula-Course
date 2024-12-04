card_value = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13}
deck_value = {'C':1, 'D':2, 'H':3, 'S':4}
cards = input()
pairs = []
for i in range(0,len(cards),2):
    pairs.append(cards[i:i+2])
    
result = ''
for i in range(len(pairs)-1):
    if pairs[i][0] != pairs[i+1][0]:
        diff = card_value[pairs[i][0]] - card_value[pairs[i+1][0]]
        if diff > 0:
            result += '+' + str(diff)
        else:
            result += str(diff)
    elif pairs[i][1] != pairs[i+1][1]:
        diff = deck_value[pairs[i][1]] - deck_value[pairs[i+1][1]]
        if diff > 0:
            result += '+' + str(diff)
        else:
            result += str(diff)
    else:
        result += '0'
        
print(result)