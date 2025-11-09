numeros = [1, 2, 3, 4, 5, 3, 2, 6, 7, 8, 5, 9, 1]
maximo = numeros[0]
minimo = numeros[0]

for numero in numeros:
    if numero > maximo:
        maximo = numero
    if numero < minimo:
        minimo = numero

print(f"{maximo} es el numero más grande, y {minimo} el más pequeño.")