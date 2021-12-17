import math_Op


#II code
#facciamo una banale applicazione sul numero di combinazioni di n oggetti 
#presi a k a k, che è dato dalla seguente formula
#C(n,k) = n!/[k!(n-k)!]

#testo: n° combinazioni ottenibili disponendo 6 carte a 3 a 3: n=6, k=3.

p = input("Inserisci il primo numero e premi INVIO: ")
k = input("Inserisci il secondo numero e premi INVIO: ")

if p < k:
    
    print("NON è possibile prendere più oggetti di quanti ce ne siano.")
else:
    print( "Il numero di combinazioni di " + p + " oggetti presi a " + k + " a " +k+" è:")
    print(math_Op.combination(int(p),int(k)))
    
    


#can only concatenate str (not "int") to str. SOLVED USING int() in p and k.