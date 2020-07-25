from math import sqrt

def eq_second(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    if a != 0:
        delta = b*b-4*a*c 
        if delta < 0:
            return False
        if delta == 0:
            r1 = -b/2*a
            return r1
        if delta > 0:
            racine = sqrt(delta)
            r1 = (-b-racine)/(2*a)
            r2 = (-b+racine)/(2*a)
            return tuple(list([r1,r2]))
    else:
        return ("a = 0")
print(eq_second(0,7,3))
