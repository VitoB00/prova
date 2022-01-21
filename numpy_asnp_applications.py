import numpy as np 
print("Esercitazione 1")
b=np.array([5,6,7,8])
c=np.arange(1,5)
d=c+b
print("Sum " ,b,"+",c, "= ", b+c)
b+=1
print("Autoincrement b +=1 b=", b)
print("Multiply c*3 " ,c, "* 3= ",c*3)
print("Sin (c)", np.sin(c))

print()
v1=np.array([1,2,3])
v2=np.array([10,20,30])

print(v1*v2)

print()
print("Esercitazione 2")
m1=np.matrix(v1)
m2=np.matrix(v2)
print(m1)
print(m2)


print()
print("Esercizio 3, COPY:")

a=np.arange(5)
c=a.copy()
print("id(a): ", id(a), "id(c):", id(c))
b=a
b[0]=100
c[0]=122
print("c",c,"a",a)