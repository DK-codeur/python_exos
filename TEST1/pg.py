def plus_grand(a, b, c):
    if b<= a >=c:
        return a
    elif a<= b >=c:
        return b
    elif a<= c >= b:
        return c


print(plus_grand(3,1,2))