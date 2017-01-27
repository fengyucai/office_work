def gcd(a, b):
    while b != 0:
        r = a % b 
        a = b
        b = r
    return a 
        

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + '/' + str(self.den)
    
    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den +\
                 otherfraction.num * self.den
        newden = self.den * otherfraction.den
        # convert to the lowest form
        common = gcd(newden, newnum)
        return Fraction(newnum // common, newden // common)
    
    def __eq__(self, other):
        return self.num * other.num == other.num * self.den
        



myf = Fraction(3, 5)
print(myf)
f1 = Fraction(1, 2)
f2 = Fraction(1, 4)
f3 = f1 + f2
print(f3)
print(f1 == f2)

