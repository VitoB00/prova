def sum(a,b):
    result = a + b
    return result

def difference(a,b):
    result = a-b
    return result

def product(a,b):
    result = a*b
    return result

def division(a,b):
    result = a/b
    return result

def squared(a):
    result = a ** a
    return result 

def power(a,b):
    result = a ** b 
    return result

def list_sum(N):
    somma=0
    for i in N:
        somma += i        
    return somma

#ovviamente se inizilassi prod a 0 il risultato sarebbe sempre 0.
def list_product(N):
    prod = 1
    for i in N:
        prod *= i        
    return prod

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact *= i
    
    return fact

def list_square(element):
    return element ** 2


def MCD(a,b):
    
    result = (a+b)/(b*a)
    return result

def list_avg(N):
    somma=0
    for i in N:
        somma += i
        avg = somma/len(N)
    return avg

def combination(a,b):
    
   comb = division(factorial(a),product(factorial(b),factorial(difference(a,b))))
   return comb

