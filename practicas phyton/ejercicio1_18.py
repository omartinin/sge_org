n = input("introduzca un número: ")
while (not n.isdigit()):
    n = input("introduzca un número válido: ")
n = int(n)

unidades = ["Celsius","Fahrenheit","Kelvin"]

unidad = input(f"introduzca una unidad de origen {unidades}: ")
while(unidad not in unidades):
    unidad = input(f"introduzca una unidad de origen válida {unidades}: ")

match unidad:
    case unidad if unidad == unidades[1]:
        n = (n - 32) * 5 / 9
    case unidad if unidad == unidades[2]:
        n = n-273.15

unidad_salida = input(f"introduzca una unidad de salida {unidades}: ")
while(unidad_salida not in unidades):
    unidad_salida = input(f"introduzca una unidad de salida válida {unidades}: ")

match unidad_salida:
    case unidad_salida if unidad_salida == unidades[1]:
        n = (n * 9 / 5) + 32
        print(f"{n} Fahrenheit")
    case unidad_salida if unidad_salida == unidades[2]:
        n = n+273.15
        print(f"{n} Kelvin")
    case _:
        print(f"{n} Celsius")

