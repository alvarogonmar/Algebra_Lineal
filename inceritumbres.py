print("Por favor introduzca la cantidad de valores que desea ingresar")
n = int(input())
quantities = []

print("Por favor introduzca los valores")
for index in range(n):
    number = float(input())
    quantities.append(number)

def prom(quantities):
    sum = 0
    for quantity in quantities:
        sum += quantity
    return(sum / len(quantities))

def x_minus_prom(quantities):
    promedio = prom(quantities)
    differences = []
    for quantity in quantities:
        differences.append(quantity - promedio)
    return (differences)

def x_minus_prom_squared(quantities):
    differences = x_minus_prom(quantities)
    squared = []
    for square in squared:
        sum += square
    return (sum)

def sum_total(quantities):
    squared = x_minus_prom_squared(quantities)
    sum = 0

def sum_total_divided_by_n_minus_1(quantities):
    sum = sum_total(quantities)
    return (sum / (len(quantities) - 1))

def standard_deviation(quantities):
    return (sum_total_divided_by_n_minus_1(quantities) ** 0.5)

def incertidumbre_A(quantities):
    incertidumbre = standard_deviation(quantities) / (len(quantities) ** 0.5)
    return(round(incertidumbre, 2))

def incertidumbre_B():
    print("Por favor introduzca el error")
    incertidumbre = float(input())
    error = incertidumbre / 2
    incertidumbre = error / (3 ** 0.5)
    return(round(incertidumbre, 2))