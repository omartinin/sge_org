numero = input("introduzca una cantidad: ")
while (not numero.isdigit()):
    numero = input("introduzca una cantidad válida: ")

unidad = input("introduzca una unidad de medida: ")
unidades_validas = ["milímetros", "centímetros", "metros", "kilómetros"]
cadena_unidades = ', '.join(unidades_validas)

while unidad not in unidades_validas:
    print(unidad + " no es una unidad valida, las unidades validas son " + cadena_unidades)
    unidad = input("introduzca una unidad de medida: ")

unidad_conversion = input("introduzca la unidad de medida a la que quiere convertir: ")

while unidad_conversion not in(unidades_validas):
    print(unidad_conversion + " no es una unidad valida, las unidades validas son " + cadena_unidades)
    unidad_conversion = input("introduzca la unidad de medida a la que quiere convertir: ")

numero = int(numero)
match unidad:
    case unidad if unidad == unidades_validas [1]:
        numero = numero*10
    case unidad if unidad == unidades_validas [2]:
        numero = numero*1000
    case unidad if unidad == unidades_validas [3]:
        numero = numero*1000000

match unidad_conversion:
    case unidad_conversion if unidad_conversion == unidades_validas [1]:
        numero = numero/10
    case unidad_conversion if unidad_conversion == unidades_validas [2]:
        numero = numero/1000
    case unidad_conversion if unidad_conversion == unidades_validas [3]:
        numero = numero/1000000

print(str(numero) + " " + unidad_conversion)