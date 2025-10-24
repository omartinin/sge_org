cadena = input("introduce una palabra")
numero = int(input("introduce el numero de rotaciones: "))
numero = numero % len(cadena)

print(cadena[numero:] + cadena[0:numero])

