def compte_car(s, c):
    result = 0
    for i in range(len(s)):
        if c in s[i]:
            result += 1
    return print(result)

compte_car("hesldsslslo", "s")