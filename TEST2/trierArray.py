def Est_trie(L):
     
    nbr_comp_croissant=0 
    nbr_comp_decroissant=0 
    n=len(L)
 
    # if n==0: 
        # return True # fin de la fonction pour la liste vide, la liste vide est une liste trié
    
    for i in range(n):
        if type(L[i]) != int:
            return False

    for i in range(n-1):
 
        if L[i]<=L[i+1]: 
            nbr_comp_croissant+=1 
        elif L[i]>=L[i+1]:
            nbr_comp_decroissant+=1 
     
    if nbr_comp_croissant==n-1: 
        return 1
    elif nbr_comp_decroissant==n-1:
        return -1
    else:
        return 0

# print(Est_trie([1,2,3,4]))
# print(Est_trie([4,3,2,1]))
print(Est_trie([4,1,3,2.1]))