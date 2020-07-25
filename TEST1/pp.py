def plus_petit(a, b, c):
    if a<b & b<c:
        return print("a",a)
    elif b<a & a<c:
        return print("b",b)
    else:
        return print("c",c)

# print(plus_petit(1,2,3))
# print(plus_petit(2,1,3))
print(plus_petit(3,2,1))