estudiantes = {
    "Ana": {"Matemáticas": 8.5, "Física": 9.0, "Programación": 7.8},
    "Carlos": {"Matemáticas": 9.2, "Física": 8.8, "Programación": 9.4},
    "Luis": {"Matemáticas": 7.6, "Física": 8.0, "Programación": 8.5},
    "María": {"Matemáticas": 9.5, "Física": 10.0, "Programación": 9.8},
    "Jorge": {"Matemáticas": 8.8, "Física": 8.4, "Programación": 7.9},
    "Sofía": {"Matemáticas": 9.1, "Física": 8.9, "Programación": 9.3}
}

promedio_estudiantes = {}
for estudiante, notas in estudiantes.items():
    promedio_estudiantes[estudiante] = sum(notas.values())/len(notas)

promedio_asignatura = {}
for notas in estudiantes.values():
    for asignatura, nota in notas.items():
        promedio_asignatura.setdefault(asignatura, []).append(nota)

for asignatura, notas in promedio_asignatura.items():
    promedio_asignatura[asignatura] = sum(notas)/len(notas)

for estudiante, promedio in promedio_estudiantes.items():
    print(f"{estudiante} : {promedio}")

for asignatura, promedio in promedio_asignatura.items():
    print(f"{asignatura} : {promedio}")



