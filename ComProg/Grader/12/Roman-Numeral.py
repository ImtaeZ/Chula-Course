class roman:
    def __init__(self, r):
        v = {'I': 1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        self.ro = r
        self.num = 0
        self.i = 0
        while self.i < len(self.ro):
            if self.ro[self.i] == 'I' and self.i != len(self.ro)-1:
                if self.ro[self.i+1] == 'V':
                    self.num += 4
                    self.i += 2
                elif self.ro[self.i+1] == 'X':
                    self.num += 9
                    self.i += 2
                else:
                    self.num += 1
                    self.i += 1
            elif self.ro[self.i] == 'X' and self.i != len(self.ro)-1:
                if self.ro[self.i+1] == 'L':
                    self.num += 40
                    self.i += 2
                elif self.ro[self.i+1] == 'C':
                    self.num += 90
                    self.i += 2
                else:
                    self.num += 10
                    self.i += 1
            elif self.ro[self.i] == 'C' and self.i != len(self.ro)-1:
                if self.ro[self.i+1] == 'D':
                    self.num += 400
                    self.i += 2
                elif self.ro[self.i+1] == 'M':
                    self.num += 900
                    self.i += 2
                else:
                    self.num += 100
                    self.i += 1
            else:
                self.num += v[self.ro[self.i]]
                self.i += 1
            
    def __str__(self):
        vr = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
        ro = ''
        num = self.num
        for v, r in vr:
            n = num//v
            num -= n*v
            ro += n*r
            if num <= 0:
                break
            
        return ro
    
    def __lt__(self, rhs):
        return self.num < rhs.num
    
    def __int__(self):
        return self.num
    
    def __add__(self, rhs):
        n = self.num + rhs.num
        r = roman('I')
        r.num = n
        return r

t, r1, r2 = input().split()
a = roman(r1); b = roman(r2)
if t == '1' : print(a < b)
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b))
else : print(str(a + b))

