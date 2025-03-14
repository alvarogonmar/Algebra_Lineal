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
        sum_row = sum(abs(A[i][j]) for j in range(n) if j != i)
        if abs(A[i][i]) <= sum_row:
            return False
    return True

print("Please enter the number of equations:")
n = int(input())

# Initialize the matrix A and the vector b
A = np.zeros((n, n))
b = np.zeros(n)

# Ask the user for the coefficients of the matrix A and the vector b
print("Please enter the coefficients of the matrix A and the vector b:")
for i in range(n):
    for j in range(n):
        A[i, j] = float(input(f"A[{i+1}][{j+1}] = "))
    b[i] = float(input(f"b[{i+1}] = "))

# Check if the matrix A is diagonally dominant
if not is_diagonally_dominant(A):
    print("The matrix is not diagonally dominant. The Jacobi method may not have a unique solution.")
else:
    x0 = np.zeros_like(b)
    tol = 0.01  # Tolerance
    max_iterations = 500  # Maximum number of iterations

    #Jacobi method
    solution, iterations = jacobi(A, b, x0, tol, max_iterations)
    print("Solution:", solution)
    print("Iterations:", iterations)