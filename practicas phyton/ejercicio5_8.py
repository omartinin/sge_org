lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]

repetidos = list(filter(lambda x: x in lista1, lista2 ))
print(repetidos)