base = input("introduzca el tamaño de la base del triángulo")
while (not base.isdigit()):
    base = input("introduzca un número válido")
base = int(base)
contador = 1
while (contador <= base):
    print("*"*contador)
    contador+=1
