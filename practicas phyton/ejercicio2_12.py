frase = input("Introduzca una frase: ")

resultado = ""
letra = ""
numero = 0

for c in frase:
    if c == letra:
        numero += 1
    else:
        if letra != "":
            resultado += str(numero) + letra
        letra = c
        numero = 1

# Añadir el último grupo
resultado += str(numero) + letra

print(resultado)
