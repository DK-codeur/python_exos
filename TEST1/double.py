# Ne pas changer le nom de la fonction svp!
def double(n):
    if type(n) == str:
        return print(-1)
    elif type(n) == float:
        return print(False)
    else:
        return print(n * 2)
        
double(5)
double(5.5)
double("chaine")
double("c")