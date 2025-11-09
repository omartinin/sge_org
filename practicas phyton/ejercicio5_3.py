from functools import reduce
numeros = [1, 2, 3, 4, 5]

suma = reduce(lambda acu, x: x+acu, numeros, 0)
print(suma)