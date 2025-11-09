
frase = input("Introduzca una frase: ")
palabras = frase.split(" ")

frase_camel = palabras[0].lower() + ''.join(p.capitalize() for p in palabras[1:])

print(frase_camel)