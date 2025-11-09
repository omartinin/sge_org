alumnos = [("Ana", 4), ("Bruno", 7), ("Clara", 5), ("David", 8)]

alumnos_dic = dict(map(lambda x: (x[0],x[1]), alumnos))

alumnos_aprobados = list(filter(lambda x: alumnos_dic.get(x)>=5, alumnos_dic))

print(alumnos_aprobados)