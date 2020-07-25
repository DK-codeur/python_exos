#ne pas changer le nom de la fonction SVP!!
def compte_chiffres_pairs(n):
    convert = str(n)
    result = 0
    for i in range(len(convert)):
        if int(convert[i]) % 2 == 0:
            result += 1
    return result


print(compte_chiffres_pairs(1258123))