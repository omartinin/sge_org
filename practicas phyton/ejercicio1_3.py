final = input("introduzca un número: ")
while (not final.isdigit()):
    final = input("Introduzca un número válido: ")
final = int(final)

for i in range(1, final + 1):
    print("*" * i)