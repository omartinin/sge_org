numeros = [1, 2, 3, 4, 5, 6]

por_encima = []
por_debajo = []
media = sum(numeros)/len(numeros)

for numero in numeros:
    if numero > media:
        por_encima.append(numero)
    else:
        por_debajo.append(numero)

print(por_encima)
print(por_debajo)