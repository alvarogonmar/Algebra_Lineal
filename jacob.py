import numpy as np

def jacobi(A, b, x0, tol, max_iterations):
    n = len(A)
    x = x0.copy()
    x_new = np.zeros_like(x0)

    for k in range(max_iterations):
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]

        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, k

        x = x_new.copy()
    return x, max_iterations

def is_diagonally_dominant(A):
    n = len(A)
    for i in range(n):
