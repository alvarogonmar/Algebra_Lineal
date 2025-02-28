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