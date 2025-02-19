#Introduction to linear algebra using numpy
# First we will define 

import numpy as np

# Create different datatypes arrays
A = np.array([[1, 2],
             [3, 4]]) # int array

print(A, "\n")

A = np.array([[1.1, 2],
             [3.4, 4]]) # float array
print(A, "\n")

A = np.array([[1.1+1j, 2],
             [3, 4]], dtype = complex) # complex array, dtype es el tipo de dato
print(A, "\n")

print("*"*50)
# create a vector that is a range of numbers

vector = np.arange(0, 10, 2) # inicio, donde se para, cuantos se salta
print(vector)

vector = np.arange(9) # vector de 0 a 9
print(vector)

vector = vector.reshape(3,3) # convertir el vector en una matriz de 3x3
print(vector)

print(vector.shape) # shape es un atributo que nos dice las dimensiones de la matriz

print("*"*50)
# create a matrix of zeros
matrix = np.zeros((3,3))
print(matrix)
print("*"*50)
# create a matrix of ones
matrix = np.ones((3,3))
print(matrix)

print("*"*50)
# look for rows columns and elements in a matrix
matrix = np.arange(1,10,1).reshape(3,3) # matriz de 3x3 con numeros del 1 al 9
print(matrix)
print("*"*50)
# rows
row1 = matrix[0] # primera fila (horizontal)
print(row1)

col1 = matrix[:,0] # primera columna (vertical)
print(col1)

colt = np.array([col1]) # convertir la columna en un array
print(colt.T) # transpuesta de la columna (convertir columna en fila)

element = matrix[0,0] # primer elemento
print(element)

# Agregrar 2 matrices
print("Add two matrices")
print("MatrixA")
matrixA = np.ones((2,2))
print(matrixA)
print("*"*50)
print("MatrixB")
matrixB = np.array([[1, 2],
              [3, 4]])
print(matrixB)

print("MatrixC")
matrixC = matrixA + matrixB
print(matrixC)