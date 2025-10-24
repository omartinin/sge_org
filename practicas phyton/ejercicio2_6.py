entrada = list(input("introduce una palabra: "))
entrada_upperlower = ""

for caracter in entrada:
    caracter = caracter.lower() if caracter.isupper() else caracter.upper()
    entrada_upperlower += caracter
    
print(entrada_upperlower)