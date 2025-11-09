pares = [2, 4, 6, 8, 10]
impares = [1, 3, 5, 7, 9]

combinada = []
for i in range(len(pares)):
    combinada.append(impares[i])
    combinada.append(pares[i])

print(combinada)