def plus_petit(a, b, c):
    if a<b & b<c:
        return a
    elif b<a & a<c:
        return b
    else:
        return c


def plus_grand(a, b, c):
    if b<= a >=c:
        return a
    elif a<= b >=c:
        return b
    elif a<= c >= b:
        return c


def puissance_n(x,n):
    return x**n


def calcul_d(a, b, c):
    x = plus_petit(a,b,c)
    n = plus_grand(a,b,c)
    
    return puissance_n(x,n)


print(calcul_d(2,3,4))