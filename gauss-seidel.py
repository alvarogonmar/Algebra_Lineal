import numpy as np

def gauss_seidel(A, b, x0, tol, max_iterations):
    n = len(A)
    x = x0.copy()

    for k in range(max_iterations):
        x_new = np.copy(x)
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
