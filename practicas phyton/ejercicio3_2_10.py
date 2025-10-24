lista = [[1,2,3,4,7,9],[5,6,7,8,4],[1,4,6,3,1,1,1]]

filas = []
columnas = []
suma = 0
i = 0
for numeros in lista:
    for numero in numeros:
        suma += numero
        if len(columnas) > i:
            columnas[i] += numero
            i += 1
        else:
            columnas.append(numero)
            i += 1
    filas.append(suma)
    suma = 0
    i = 0
        
print(filas)
print(columnas)
