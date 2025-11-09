cadena1 = input("Introduzca una frase: ")
cadena2 = input("Introduzca otra frase: ")

ascii1=0
ascii2=0
for c in cadena1:
    ascii1 += ord(c)

for c in cadena2:
    ascii2 += ord(c)
print(f"{cadena1} {ascii1}" if ascii1 > ascii2 else f"{cadena2} {ascii2}")