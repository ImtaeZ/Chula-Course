class Complex:
    def __init__(self, a, b):
        self.real = a
        self.imagine = b
    
    def __str__(self):
        if self.real == 0 and self.imagine == 0: return '0'
        elif self.real == 0:
            if self.imagine == 1:
                return 'i'
            elif self.imagine == -1:
                return '-' + 'i'
            else:
                return str(self.imagine) + 'i'
        elif self.imagine == 0:
            return str(self.real)
        elif self.imagine == 1:
            return str(self.real) + '+' + 'i'
        elif self.imagine == -1:
            return str(self.real) + '-' + 'i'
        elif self.imagine > 0:
            return str(self.real) + '+' + str(self.imagine) + 'i'
        else:
            return str(self.real) + str(self.imagine) + 'i'
        
    def __add__(self, rhs):
        sum_real = self.real + rhs.real
        sum_imagine = self.imagine + rhs.imagine
        return Complex(sum_real, sum_imagine)
    
    def __mul__(self, rhs):
        mul_real = self.real*rhs.real - self.imagine*rhs.imagine
        mul_imagine = self.real*rhs.imagine + self.imagine*rhs.real
        return Complex(mul_real, mul_imagine)
    
    def __truediv__(self, rhs):
        a = self.real
        b = self.imagine
        c = rhs.real
        d = rhs.imagine
        div_real = (a*c + b*d)/(c**2+d**2)
        div_imagine = (-a*d + b*c)/(c**2+d**2)
        return Complex(div_real, div_imagine)
        
t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a,b)
c2 = Complex(c,d)
if t == 1 : print(c1)
elif t == 2 : print(c2)
elif t == 3 : print(c1+c2)
elif t == 4 : print(c1*c2)
else : print(c1/c2)

