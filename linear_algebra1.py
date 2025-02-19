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