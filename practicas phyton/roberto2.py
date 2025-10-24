n_porciones = input("introduce un numero: ")
while (not n_porciones.isdigit()):
    n_porciones = input("introduzca un número válido: ")

n_porciones = int(n_porciones)

cad = input("introduce una palabra: ")
if len(cad) < n_porciones+1:
    cad = input("introduce una palabra más larga: ")

espacio = round(len(cad) / n_porciones)

salida = ""
contador = 0

for caracter in cad:
    contador += 1
    salida += caracter
    if contador == espacio:
        salida += " "
        contador = 0

if ((len(cad) / n_porciones) - (len(cad)// n_porciones)) <= 0.5:
    ultimo_espacio = salida.rfind(" ")
    salida = salida[:ultimo_espacio] + salida[ultimo_espacio+1:]
    
print(salida)
