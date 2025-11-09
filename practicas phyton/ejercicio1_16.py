n = input("introduzca un número: ")
while (not n.isdigit()):
    n = input("introduzca un número válido: ")

numeros = [int(c) for c in n]

print(sum(numeros))