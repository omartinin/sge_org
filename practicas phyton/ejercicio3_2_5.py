numeros = [1, 2, 3, 4, 5, 3, 2, 6, 7, 8, 5, 9, 1]

pares = []

for numero in numeros:
    if numero%2 == 0:
        pares.append(numero)

print(pares)