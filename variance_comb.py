
"the code wants to use math_Op to make a variance of a randomly distributed array"
#First code
from math_Op import list_avg
from math_Op import difference
from math_Op import list_square
from math_Op import power
import numpy as np
import statistics
from numpy import var
#Secondo Code
from math_Op import factorial
from math_Op import division
from math_Op import product
from math_Op import combination


#I code
#popolo l'array con numeri interi random perché più semplice fare controlli
array = np.random.randint(9, size=10)
print(array)

#calcolo la media importando la funzione dal modulo math_Op
avg = list_avg(array)
print("\navg =", avg)

print("\n") #pulizia

#richiamando un ulteriore funzione popolo un array con (x_i - media)
discrepancy = difference(array,avg)
print(discrepancy )

print("\n") #pulizia

#questa funzione fa il quadrato di ogni elemento di un array,quindi:(x_i-avg)^2
square_stuff= [list_square(i) for i in discrepancy]
print(square_stuff)

print("\n") #pulizia

#list_avg,già usata su, è un'altra funzione di math_Op che si occupa di sommare  
#tutti gli elementi di un array e dividerli per il numero di elementi
variance = list_avg(square_stuff)
print("variance = ", variance)

#richiamiamo power = a**b, e otteniamo la st_dev dalla varianza
st_dev = power(variance,0.5)
print("standard deviation = ", st_dev)

#controprova con la libreria numpy importando VAR

print("\n")
print(var(array))

#controprova con la libreria statistics
print("\n")
print(statistics.variance(array))
#dal sito è possibile controllare l'affidabilità.
#https://www.calculator.net/standard-deviation-calculator.html


print("\n")



#II code
#facciamo una banale applicazione sulle Il numero di combinazioni di n oggetti 
#presi a k a k è dato dalla seguente formula
#C(n,k) = n!/[k!(n-k)!]

#testo: n° combinazioni ottenibili disponendo 6 carte a 3 a 3: n=6, k=3.

p = input("Scrivi un primo numero maggiore del secondo e premi INVIO: ")
k = input("Scrivi un secondo numero e premi INVIO: ")

print( "Il numero di combinazioni di " + p + " oggetti presi a " + k + " a " +k+" è:")
print(combination(int(p),int(k)))

#can only concatenate str (not "int") to str. SOLVED USING int() in p and k.