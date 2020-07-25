#Ne pas changer le nom de la fonction
# def factoriel(n):
#     if n ==1:
#         return 1
#     else:
#         result = n * factoriel(n-1)
#     return result

# print(factoriel(8))


# def iterative_factorial(n):
#     result = 1
#     for i in range(2,n+1):
#         result *= i
#     return result

# print(iterative_factorial(8))

def factoriel(n):
    if type(n) == int:
        if n < 2:
            return 1
        else:
            return n*factoriel(n-1)
    else:
        return -1