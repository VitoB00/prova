
"the code wants to use math_Op to make a variance of a randomly distributed array"
#First code
import math_Op
import numpy as np
import statistics
from numpy import var
from numpy import sort
#let's study time waste
import time
#let's plot
import scipy
from scipy.stats import norm 
import matplotlib.pyplot as plt


#Improving The Code to achieve to get confidence with the PL
T1=time.perf_counter()

#popolo l'array con numeri interi random perché più semplice fare controlli

array = np.random.randint(9, size=10)

#preSORTING
print("popolo un array di 10 slot con un numero int casuale tra 0 e 9:")
print(array)

#postSORTING
print()
print("Sortiamo!:")
array.sort(axis=-1, kind=None, order = None)
#è stato laborioso sortare poiché nel caso di array di int random list.sort
#vuole una list e ottiene un numpy.ndarray.

print(array)
print("Notiamo che un altro modo più economico (in skills) di sortare è:")
print(sorted(array))
#stupefacentemnte questa built-in function funziona anche su cose che non siano strettamente Dictionary

#calcolo la media importando la funzione dal modulo math_Op
avg = math_Op.list_avg(array)
print("\navg =", avg)

print("\n") #pulizia

#richiamando un ulteriore funzione popolo un array con (x_i - media)
discrepancy = math_Op.difference(array,avg)
print("printo l'array popolato con (x_i -avg) per verifica:")
print(discrepancy)

print("\n") #pulizia

#questa funzione fa il quadrato di ogni elemento di un array,quindi:(x_i-avg)^2
square_stuff= [math_Op.list_square(i) for i in discrepancy]
print("printo l'array con (x_i-avg)^2 per verifica:")
print(square_stuff)

print("\n") #pulizia

#list_avg,già usata su, è un'altra funzione di math_Op che si occupa di sommare  
#tutti gli elementi di un array e dividerli per il numero di elementi
variance = math_Op.list_avg(square_stuff)
print("variance = ", variance)

#richiamiamo power = a**b, e otteniamo la st_dev dalla varianza
st_dev = math_Op.power(variance,0.5)
print("standard deviation = ", st_dev)
T2 = time.perf_counter()
print("\nVogliamo vedere se è efficienete in relazione al richiamo dei metodi VAR e VARIANCE dentro NUMPY e STATISTICS rispettivamente, viceversa potrebbe nona aver avutos senso aver fatto questo lavoro:")
print("execution time:" , T2-T1, "s")

#dalle scipy otteniamo le ordinate, e plottiamo la gaussiana associata a questo
#set 
Tp1 = time.perf_counter()
x = np.arange(-15, 15, 0.1)
y = scipy.stats.norm(avg, st_dev)
plt.plot(x, y.pdf(x))
Tp2 = time.perf_counter()

print()
print("execution time to plot:", Tp2-Tp1,"s")

#controprova con la libreria numpy importando VAR
T3 = time.perf_counter()
print("\n")
print("importo VAR da NUMPY per verificare:")
print(var(array))
T4 = time.perf_counter()
print()
print("execution time:", T4-T3, "s")

#controprova con la libreria statistics varianza
T5 = time.perf_counter()
print("\n")
print("importo VARIANCE da STATISTICS per verificare:")
print(statistics.variance(array))
T6 = time.perf_counter()
print("execution time:", T6-T5, "s")

#Commento a caldo
print()
print("Dal punto di vista del tempo il mio codice è abbastanza deludente in quanto mediamente un fattore 10 più dispersivo.")
#controprova con la libreria statistics st_dev

print("\n")
print("importo STDEV da STATISTICS per verificare:")
print(statistics.stdev(array))
#dal sito è possibile controllare l'affidabilità.
#https://www.calculator.net/standard-deviation-calculator.html

#voglio stimare il tempo totale impiegato per girare il codice
T_tot= time.perf_counter()
print("whole exectuion time:", T_tot-T1, "s")
print("Il tempo totale impiegato è mediamente 3 centesimi di secondi, questo è dimostrato su derivare dal plot della Gaussiana")