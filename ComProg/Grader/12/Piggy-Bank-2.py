class piggybank:
    def __init__(self):
        self.coins = {}
        self.c = 0
        
    def add(self, v, n):
        self.c += n
        if self.c > 100:
            self.c -= n
            return False
        v = float(v)
        if v not in self.coins:
            self.coins[v] = 0
        self.coins[v] += n
        return True
    
    def __float__(self):
        t = 0
        for coin in self.coins:
            t += coin*self.coins[coin]
        return float(t)
    
    def __str__(self):
        res = ''
        for coin in sorted(self.coins.keys()):
            res += str(coin) + ':' + str(self.coins[coin]) +', '
            
        return '{' + res[:-2] + '}'
            
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)
