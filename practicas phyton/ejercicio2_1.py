cad = input("Introduzca su cadena: ")
cad = cad.lower()
vocales = "aeiou"
consonantes = "bcdfghjklmnñpqrstvwxyz"
nVocales = 0
nConsonantes = 0
for caracter in cad:
    if caracter in vocales:
        nVocales += 1
    elif caracter in consonantes:
        nConsonantes += 1

print(f"numero de vocales : {nVocales}")
print(f"numero de consonantes : {nConsonantes}")