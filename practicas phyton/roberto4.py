
palabra = input("introduce una palabra: ")

letra = input("introduce una letra: ")
while len(letra) > 1:
    letra = input("introduce solo una letra: ")

errores = 0
palabra_sin_aciertos = ""
for caracter in palabra:
    palabra_sin_aciertos.replace(caracter, "_")

while errores != 11 or palabra_sin_aciertos == palabra:
    aciertos = palabra.find(letra)
    if(len(str(aciertos)) == 0):
        errores += 1
    
    for caracter in palabra:
        if caracter == letra:
            palabra_sin_aciertos.replace(caracter, letra)
    print(palabra_sin_aciertos)
    letra = input("introduce una letra: ")
    while len(letra) > 1:
        letra = input("introduce solo una letra: ")

if palabra_sin_aciertos == palabra:
        print("has ganado.")
else:
    print("has perdido.")




