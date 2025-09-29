numeros = []
numero_pequeno = 0
numero_grande = 0
while (len(numeros) < 5):
    numero = input("introduzca un numero")
    while (not numero.isdigit()):
        numero = input("introduzca un número válido")
    if(len(numeros) == 0):
        numero_pequeno = numero
        numero_grande = numero
    elif(numero > numero_grande):
        numero_grande = numero
    elif(numero < numero_pequeno):
        numero_pequeno = numero
    numeros.append(numero)
print("El número mas pequeño es: " + numero_pequeno)
print("El número mas grande es: " + numero_grande)


