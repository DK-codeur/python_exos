def compte_chiffre(n, c):
    result = 0
    convert = str(n)
    for i in range(len(convert)):
        if int(convert[i]) == c:
            result += 1
    return result


print(compte_chiffre(9239094, 9))
        