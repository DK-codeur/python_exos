#diametre = 2 x r
#perimetre = 2 x pi x r
#surface = pi x r**2

def dia_cercle(r):
    if type(r) is int and r > 0:
        pi = 3.14

        d = 2 * r
        p = 2 * pi * r
        s = pi * r**2
        result = tuple(list([d,p,s]))
        return result
    else:
        return False

print(dia_cercle(3))  



