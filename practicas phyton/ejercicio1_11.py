n = input("introduzca un número")
while (not n.isdigit()):
    n = input("introduzca un número válido")
n = int(n)

def factorial(n):
    fac = 1
    for i in range (2, n+1):
        fac *= i
    return fac