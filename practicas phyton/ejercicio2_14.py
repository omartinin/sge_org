cadena = "Omar {apellido1} {apellido2}"
diccionario = {"apellido1" : "Rey", "apellido2" : "Guijarro"}

for clave in diccionario:
    if "{" + clave + "}" in cadena:
        cadena = cadena.replace("{" + clave + "}", diccionario[clave])
print(cadena)
