from random import *

n = input("introduzca la longitud de su contraseña: ")
while (not n.isdigit()):
    n = input("introduzca longitud válida: ")
n = int(n)
contrasena =""
for i in range(n):
    ascii = randint(32,254)
    contrasena += chr(ascii)

print(contrasena)