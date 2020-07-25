import math

# reduire les fraction
# def simplifier(a, b):
#      facteur_com = math.gcd(a, b)
#      return facteur_com

# class Fraction:
#     def __init__(self, num, denom):
#         self.num = num
#         self.denom = denom

#     def affiche(self):
#         fc = simplifier(self.num, self.denom)
#         a = self.num/fc
#         b = self.denom/fc
#         return ("{0}/{1}".format(int(a), int(b)))


import math

class Fraction:
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom
        
    def affiche(self):
        return print(str(self.num)+"/"+str(self.denom))
        
    def __add__(self, fraction):
        if fraction.denom == self.denom:
            newnum = self.num + fraction.num
            newden = self.denom + fraction.denom
            common = math.gcd(newnum, newden)
            return Fraction(newnum//common, newden//common)
        else:
            newden = (self.num*fraction.denom)-(fraction.num*self.denom)
            newnum = self.denom*fraction.denom
            common = math.gcd(newnum, newden)
            return Fraction(newnum//common, newden//common)
        
    def __sub__(self, fraction):
        if fraction.denom == self.denom:
            newnum = self.num - fraction.denom
            newden = self.denom - fraction.denom
            common = math.gcd(newnum, newden)
            return Fraction(newnum//common, newden//common)
        else:
            newnum = (self.num*fraction.denom)-(fraction.num*self.denom)
            newden = self.denom*fraction.denom
            common = math.gcd(newnum, newden)
            return Fraction(newnum//common, newden//common)
            
    def __mul__(self, fraction):
        newnum = self.num*fraction.num
        newden = self.denom*fraction.denom
        common = math.gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)
        
    def __div__(self, fraction):
        newnum = self.num*fraction.denom
        newden = self.denom*fraction.num
        common = math.gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    


