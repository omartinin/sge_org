n = input("introduzca un número")
while (not n.isdigit()):
    n = input("introduzca un número válido")

i = 0
punto = len(n)%3
salida = ""

for c in n:
    i += 1
    salida += c
    if (i%punto == 0):
        salida += "."
        punto = 3
        i = 0

print(salida[:len(salida)-1])