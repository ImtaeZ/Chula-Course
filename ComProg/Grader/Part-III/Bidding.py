# biding = {p : [[b, price],..], ...}
# def found:

def found(bidding, b, p):
    i = 0
    for i in range(len(bidding[p])):
        if b in bidding[p][i]:
            return (True, i)
    return (False, i)

def mul_winner(bidding, p): # [(1,w),(1,a),(2,b)]
    max_price = sorted(bidding[p])[::-1]
    max_price = max_price[0][0]
    bp = bidding[p]
    winners = []
    for i in range(len(bp)):
        if bp[i][0] == max_price:
            winners.append((bp[i][0],bp[i][1],p))
    if len(winners) > 1:
        return winners[0]
    else:
        return winners[0]

def check_winner(bidding): # return = [w1,w2,w3,....]
    winner = []
    for p in bidding:
        if bidding[p] != []:
            winner.append(mul_winner(bidding,p))
    return winner

bidding = {}
bidder = set()
for i in range(int(input())):
    l = input().split()
    cmd = l[0]
    if cmd == 'B':
        b, p, price = l[1],l[2],l[3]
        if p not in bidding:
            bidding[p] = [(int(price),b)]
        else:
            if found(bidding, b, p)[0]:
                index = found(bidding, b, p)[1]
                bidding[p].pop(index)
                bidding[p].append((int(price),b))
            else:
                bidding[p].append((int(price),b))
    elif cmd == 'W':
        b, p = l[1],l[2]
        if found(bidding,b ,p)[0]:
            index = found(bidding, b, p)[1]
            bidding[p].pop(index)
    bidder.add(b)
    
winner = check_winner(bidding)
bidder = sorted(list(bidder))
def pay(winner,b):
    pay = []
    won = []
    for i in range(len(winner)):
        if b in winner[i]:
            pay.append(winner[i][0])
            won.append(winner[i][2])
    if pay != []:
        return f"${sum(pay)} -> {' '.join(sorted(won))}"
    else:
        return "$0"
    
for b in bidder:
    print(f"{b}: {pay(winner,b)}")

