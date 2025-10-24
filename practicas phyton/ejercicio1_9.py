def fib(n):
    if (n == 0): return 0
    elif (n == 1): return 1
    else: return fib(n-2) + fib(n-1)

n = input("introduzca un número")
while (not n.isdigit()):
    n = input("introduzca un número válido")

for i in range(int(n) + 1):
    print(fib(i))

