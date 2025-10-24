
cad = input("introduce un numero :")
while (not cad.isdigit()):
    cad = input("introduzca un número válido")

punto = len(cad) % 3
if punto == 0:
    punto = 3
contador = 0
salida = ""
for caracter in cad:
    salida += caracter
    contador += 1
    if contador == punto:
        salida += "."
        contador = 0
        punto = 3

print(salida)







