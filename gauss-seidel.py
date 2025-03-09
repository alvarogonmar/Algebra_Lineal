import numpy as np

def gauss_seidel(A, b, x0, tol, max_iterations):
    n = len(A)
    x = x0.copy()

    for k in range(max_iterations):
        x_new = np.copy(x)
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]

        # Calculate the error index
        error = np.abs(1 - np.linalg.norm(x) / np.linalg.norm(x_new))
        if error < tol:
            return x_new, k

        x = x_new
    return x, max_iterations

def is_diagonally_dominant(A):
    n = len(A)
    for i in range(n):
        sum_row = sum(abs(A[i][j]) for j in range(n) if j != i)
        if abs(A[i][i]) <= sum_row:
            return False
    return True
