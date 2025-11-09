from functools import reduce
numeros = [[-3, 2, 7], [10, -5, 3], [0, 8, -2]]

numeros_deslistados = reduce(lambda acu,x: acu + x, numeros, [])
numeros_positivos = list(filter(lambda x: x>0, numeros_deslistados))
suma = reduce(lambda acu, x: acu+x, numeros_positivos, 0)

print(suma)



