def compte_minuscule(s):
    s = str(s)
    n =  0
    alpha = ("abcdefghijklmnopqrstuvwxyz")
    for i in s:
        for j in alpha:
            if str(i) == str(j):
                n += 1
    return n