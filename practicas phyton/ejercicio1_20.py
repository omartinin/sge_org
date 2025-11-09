numeros_c = input("introduzca una lista de numeros separados por comas (1,4,2,8...): ")
numeros_c = numeros_c.split(",")

numeros = [int(c) for c in numeros_c]
numeros.sort()
print(numeros)
