import numpy as np
# resolver un sistema de ecuaciones usando gauss-jordan
print("Solve a system of equations")
matrix = np.array([[2, 4, 6, 18],
                  [4, 5, 6, 24],
                  [3, 1, -2, 4]], dtype=float)

# imprimir numero de

# dimMatrix = matrix.shape # dimensiones de la matriz
# numRows = dimMatrix[0] # numero de filas
# print(dimMatrix) # dimensiones de la matriz
# print(numRows) # numero de filas

def gauss_jordan(matrix):
    rows, cols = matrix.shape  # Extraer el número de filas y columnas

    for index in range(rows):
        # hacer 1 la diagonal
        matrix[index] = matrix[index] / matrix[index, index]
        # hacer 0 los demas
        for j in range(rows): # recorrer las filas
            if j != index: # si no es la fila de la diagonal
                # hacer 0 los demas
                matrix[j] = matrix[j] - matrix[j, index] * matrix[index]
    return matrix

result = gauss_jordan(matrix)
print(result)

# para obtener los valores de las variables:
solutions = result[:, -1]
print("Solutions:")
print(solutions)