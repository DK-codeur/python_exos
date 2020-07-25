from math import sqrt
def is_prime(n):
    racine = int(sqrt(n))
    premier = False
    if n==2 or n==3:
        premier=True
    else:
        i=2
        while i<racine:
            if n%i==0:
                premier=False
                break
            else:
                premier = True
            i+=1 
    return premier

def prime_interval(n):
    if 0<=n<=500:
        if n==500:
            result = [499]
        elif n==499:
            result = [491, 499]
        elif n>=2:
            if is_prime(n):
                if n==2:
                    result = [2, 3]
                else:
                    s=n-1
                    while is_prime(s)==False:
                        s-=1 
                    pre = s 
                    p=n+1
                    while is_prime(p)==False:
                        p+=1 
                    post = p 
                    result = [pre, n, post]
            elif is_prime(n)==False:
                s=n  
                while is_prime(s)==False:
                    s-=1
                pre =s
                p=n
                while is_prime(p)==False:
                    p+=1
                post = p
                result = [pre, post]
        else:
            result = [2]
        return result