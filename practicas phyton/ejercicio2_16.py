cadena = list(input("Introduzca una frase: ").split(" "))

palabra_larga = ""
longitud = 0

for palabra in cadena:
    if len(palabra) > longitud:
        longitud = len(palabra)
        palabra_larga = palabra

print(f"La palabra más larga ha sido {palabra_larga}, con una logitud de {longitud} caracteres.")