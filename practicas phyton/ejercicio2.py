n = input("introduzca un número")
while (not n.isdigit()):
    n = input("introduzca un número válido")

k = input("introduzca el numero de elementos de la tabla de multiplicar que quiere mostrar")
while (not k.isdigit()):
    k = input("introduzca un número de elementos válido")
n = int(n)
k = int(k)

contador = 1

while (contador <= k):
    print(n*contador)
    contador+=1