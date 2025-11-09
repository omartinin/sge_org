operaciones = ["suma","resta","multiplicación","división"]
numeros = []
for i in range(2):
    n = input("introduzca un número: ")
    while (not n.isdigit()):
        n = input("introduzca un número válido: ")
    print("Número guardado")
    n = int(n)
    numeros.append(n)

o = input(f"introduzca una de las siguientes operaciones {operaciones}: ")
while(o not in operaciones):
    o = input(f"introduzca una de las siguientes operaciones {operaciones}: ")

match o:
    case o if o == operaciones[0]:
        print(numeros[0]+numeros[1])
    case o if o == operaciones[1]:
        print(numeros[0]-numeros[1])
    case o if o == operaciones[2]:
        print(numeros[0]*numeros[1])
    case o if o == operaciones[3]:
        print(numeros[0]/numeros[1])