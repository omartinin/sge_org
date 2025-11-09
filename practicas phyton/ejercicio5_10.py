from functools import reduce

lista1 = ['a', 'b', 'c']
lista2 = ['x', 'y', 'z']

def acumulador(acu,x):
    acu.append(x)
    return acu

lista3 = reduce(acumulador, lista2, lista1[:])

print(lista3)