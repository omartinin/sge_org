lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [4, 5, 6, 7, 8, 9]
lista1 = list(set(lista1))
lista2 = list(set(lista2))

comunes = []

for numero in lista1:
    if numero in lista2:
        comunes.append(numero)

print(comunes)