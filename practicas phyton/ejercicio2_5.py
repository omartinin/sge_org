entrada = list(input("introduce una palabra: "))
entrada_sin_repeticiones = ""
for caracter in entrada:
    if caracter not in entrada_sin_repeticiones:
        entrada_sin_repeticiones += caracter

print(entrada_sin_repeticiones)