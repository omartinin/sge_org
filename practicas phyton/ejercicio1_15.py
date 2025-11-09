n = input("introduzca un número: ")
while (not n.isdigit()):
    n = input("introduzca un número válido: ")
n = int(n)

pares = []
inpares = []
for i in range(1,n+1):
    if (i%2 == 0):
        pares.append(i)
    else:
        inpares.append(i)

print(f"Pares: {pares}")
print(f"Inpares: {inpares}")