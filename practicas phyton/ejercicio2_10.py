entrada = input("Introduce una cadena: ")
salida = "".join(c for c in entrada if c.isalnum())
print(salida)