import Mat_Op
import numpy as np
 
a = int(input("Enter the number of rows:"))
b = int(input("Enter the number of columns:"))

print("Enter the number in a single line separated by space:")
val = list(map(int, input().split()))
matrix = np.array(val).reshape(a,b)

print(matrix)        
            
print("Enter the number in a single line separated by space:")
val = list(map(int, input().split()))
matrix1 = np.array(val).reshape(a,b)

print(matrix1)

print("the product of these 2 matrices is:")
print(Mat_Op.product(matrix,matrix1))

print("proviamo a fare un determinante della matrice: matrix")
print(Mat_Op.determinant(matrix))