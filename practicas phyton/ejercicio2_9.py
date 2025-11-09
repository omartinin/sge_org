cadena = input("introduzca una flase: ")

coincidencias = {}
for c in cadena:
    if c in coincidencias:
        coincidencias[c] += 1
    else:
        coincidencias[c] = 1

coincidencias = dict(sorted(coincidencias.items()))

for c, n in coincidencias.items():
    print(f"{c} : {n}")