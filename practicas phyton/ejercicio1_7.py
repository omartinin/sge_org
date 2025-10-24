from random import *

numero_correcto = randint(0, 100)

numero = input("introduzca un número entre el 1 y el 100: ")

while (numero != numero_correcto):

    while (not numero.isdigit()):
        numero = input("introduzca un número válido: ")

    numero = int(numero)

    if(numero >= 1 and numero <= 100):
        if (numero < numero_correcto):
            numero = input("introduzca un número más grande: ")
        elif (numero > numero_correcto):
            numero = input("introduzca un número más pequeño: ")
        else:
            print("!Has acertado¡")


