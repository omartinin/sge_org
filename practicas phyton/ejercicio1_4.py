base = input("introduzca el tamaño de la base de la pirámide: ")
while (not base.isdigit()):
    base = input("introduzca un número válido: ")
base = int(base)
espacio = base//2
valor_inicial = 1

if (base%2 == 0):
    espacio = (base//2) -1
    valor_inicial = 2

for i in range(valor_inicial,base+1,2):
        print(" "*espacio + "*"*i + " "*espacio)
        espacio -= 1