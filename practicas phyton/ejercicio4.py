base = input("introduzca el tamaño de la base dela pirámide")
while (not base.isdigit()):
    base = input("introduzca un número válido")
base = int(base)
if (base%2 == 0):
    contador = 2
    espacio = (base//2) -1
    while (contador <= base):
        print(" "*espacio +"*"*contador + " "*espacio)
        contador+=2
        espacio -=1

if (base%2 != 0):
    contador = 1
    espacio = base//2
    while (contador <= base):
        print(" "*espacio +"*"*contador + " "*espacio)
        contador+=2
        espacio -=1

