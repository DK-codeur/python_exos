def palindrome(s):
    s = str(s)
    rev = reversed(s)
    if list(s) == list(rev):
        p = True 
        return p  
    else:
        p = False
        return p
