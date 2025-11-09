from functools import reduce
numeros = [1, 2, 3, 4, 5, 6]

numeros_pares = list(filter(lambda x: x%2 == 0, numeros))
suma = reduce(lambda acu,x: x*acu, numeros_pares,1)
print(suma)