import numpy as np
# resolver un sistema de ecuaciones usando gauss-jordan
print("Solve a system of equations")
matrix = np.array([[2, 4, 6, 18],
                  [4, 5, 6, 24],
                  [3, 1, -2, 4]], dtype=float)
print(matrix)

# imprimir numero de

dimMatrix = matrix.shape # dimensiones de la matriz
numRows = dimMatrix[0] # numero de filas
print(dimMatrix) # dimensiones de la matriz
print(numRows) # numero de filas