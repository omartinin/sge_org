cadena = input("Introduzca un palíndromo: ")

cadena = "".join(c for c in cadena if c.isalpha()).lower()

cadena_invertida = cadena[::-1]

if (cadena == cadena_invertida):
     print("Es palíndromo")
else:
     print("no es palíndromo")