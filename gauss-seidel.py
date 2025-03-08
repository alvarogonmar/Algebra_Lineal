import numpy as np

def gauss_seidel(A, b, x0, tol, max_iterations):
    n = len(A)
    x = x0.copy()

    for k in range(max_iterations):
        x_new = np.copy(x)
