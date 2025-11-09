palabras = ["perro", "gato", "elefante", "oso", "jirafa"]

palabras_largas = list(filter(lambda x: len(x)>5, palabras))
palabras_largas_mayus = list(map(lambda x: x.upper(), palabras_largas))

print(palabras_largas_mayus)