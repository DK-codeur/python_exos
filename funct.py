# filter
mylist = [1, 2, 3, 4, 5, 6, 7, 8]

# def myFonct(nbr):
#     return nbr%2 == 0

# verif = filter(myFonct, mylist)
# print(list(verif))


#lambda
verif2 = filter(lambda nbr: nbr%2 == 0, mylist) 
print(list(verif2))
