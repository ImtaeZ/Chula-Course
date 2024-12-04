class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def __str__(self):
        return '(' + str(self.value) + ' ' + str(self.suit) + ')'
    
    def getScore(self):
        if self.value == 'A': return 1
        elif self.value in ['J','Q','K']: return 10
        else: return int(self.value)
    def sum(self, other):
        return (self.getScore() + other.getScore())%10
    def __lt__(self, rhs):
        if self.value != rhs.value:
            true_val = {'J':11,'Q':12,'K':13,'A':14,'2':15}
            true_self = self.value
            true_rhs = rhs.value
            if self.value in true_val : true_self = true_val[self.value]
            if rhs.value in true_val : true_rhs = true_val[rhs.value]
            return int(true_self) < int(true_rhs)
        suit_val = {'club':1, 'diamond':2, 'heart':3, 'spade':4}
        return suit_val[self.suit] < suit_val[rhs.suit]
n = int(input())
cards = []
for i in range(n):
 value, suit = input().split()
 cards.append(Card(value, suit))
for i in range(n):
 print(cards[i].getScore())
print("----------")
for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
 print(cards[i])
