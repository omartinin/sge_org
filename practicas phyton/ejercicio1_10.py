n = input("introduzca un número")
while (not n.isdigit()):
    n = input("introduzca un número válido")
n = int(n)

def primo(n):
    n = int(n)
    if (n < 2): return False
    
    for i in range(2,int(n**0.5) + 1):
        if (n%i == 0):
            return False
    return True

if (primo (n)):
    print(str(n) + " es primo.")
else:
    print(str(n) + " no es primo.")