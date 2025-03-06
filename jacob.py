import numpy as np

def jacobi(A, b, x0, tol, max_iterations):
    n = len(A)
    x = x0.copy()
    x_new = np.zeros_like(x0)