frase = input("Escriba una frase: ")
frase = ''.join(c for c in frase.lower() if c.isalnum() or c == ' ')
palabras = frase.split(" ")

ocurrencias = {}
for palabra in palabras:
    ocurrencias[palabra] = 1 if palabra not in ocurrencias else ocurrencias[palabra]+1

print(ocurrencias)