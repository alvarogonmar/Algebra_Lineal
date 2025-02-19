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