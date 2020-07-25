class Domino:
    """
    pass
    """
    
    def __init__(self, A, B):
        self.A = A 
        self.B = B 
        
    def affiche_points(self):
        return (self.A,self.B)
        
    def total(self):
        return self.A + self.B

d  = Domino(4, 6)
print(d.affiche_points())

x = d.total()
print(x)