cadena = input("Introduzca una frase: ")

cadena_tratada = "".join(c for c in cadena if cadena.isalpha())

vocales = "aeiouáéíóúü"
consonantes = "bcdfghjklmnñpqrstvwxyz"
n_vocales = 0
n_consonantes = 0

for c in cadena:
    if c.lower() in vocales: n_vocales += 1
    elif c.lower() in consonantes: n_consonantes += 1

print(f"Tu frase contiene {n_vocales} vocales y {n_consonantes} consonantes.")
