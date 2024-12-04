class piggybank:
    def __init__(self):
        self.one = 0
        self.song = 0
        self.ha = 0
        self.sib = 0
        
    def add1(self, n):
        self.one += n
        
    def add2(self, n):
        self.song += n
    
    def add5(self, n):
        self.ha += n
        
    def add10(self, n):
        self.sib += n
    
    def __int__(self):
        return self.one + self.song*2 + self.ha*5 + self.sib*10
    
    def __lt__(self, rhs):
        return self.__int__() < rhs.__int__()
    
    def __str__(self):
        return '{' + '1:' + str(self.one) + ', 2:' + str(self.song) + ', 5:' + str(self.ha) \
               + ', 10:' + str(self.sib) + '}'
    
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)
