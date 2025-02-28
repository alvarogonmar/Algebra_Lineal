print("Por favor introduzca la cantidad de valores que desea ingresar")
n = int(input())
quantities = []

print("Por favor introduzca los valores")
for index in range(n):
    number = float(input())
    quantities.append(number)

def prom(quantities):