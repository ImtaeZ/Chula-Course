class Card:
    def __init__(self, value, suit):
        self.v = value
        self.s = suit
        
    def __str__(self):
        return '(' + self.v + ' ' + self.s + ')'
    
    def next1(self):
        val = ['3','4','5','6','7','8','9','10','J','Q','K','A','2','3']
        sui = ['club','diamond','heart','spade']
        if self.s != 'spade':
            next_val = self.v
            next_sui = sui[sui.index(self.s) + 1]
        else:
            next_val = val[val.index(self.v) + 1]
            next_sui = 'club'
        return Card(next_val, next_sui)
                
    def next2(self):
        val = ['3','4','5','6','7','8','9','10','J','Q','K','A','2','3']
        sui = ['club','diamond','heart','spade']
        if self.s != 'spade':
            self.s = sui[sui.index(self.s) + 1]
        else:
            self.v = val[val.index(self.v) + 1]
            self.s = 'club'

n = int(input())
cards = []
for i in range(n):
 value, suit = input().split()
 cards.append(Card(value, suit))
for i in range(n):
 print(cards[i].next1())
print("----------")
for i in range(n):
 print(cards[i])

print("----------")
for i in range(n):
 cards[i].next2()
 cards[i].next2()
 print(cards[i])

