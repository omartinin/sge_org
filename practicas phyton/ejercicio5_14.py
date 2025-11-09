palabras = ["HOLA", "MUNDO", "SOL", "CIELO", "mar"]

palabras_mayusculas = list(filter(lambda x: x.isupper(),palabras))
palabras_largas = list(filter(lambda x: len(x)>3, palabras_mayusculas))
resultado = list(map(lambda x: x[0].lower() + x[1:], palabras_largas))
print(resultado)
