asignaturas = {
    "Matemáticas": ["Ana", "Carlos", "Luis", "María", "Jorge"],
    "Física": ["Elena", "Luis", "Juan", "Sofía"],
    "Programación": ["Ana", "Carlos", "Sofía", "Jorge", "Pedro"],
    "Historia": ["María", "Juan", "Elena", "Ana"],
    "Inglés": ["Carlos", "Sofía", "Jorge", "María"],
}

def comprobar_asignatura(asignatura):
    if asignatura not in asignaturas:
        print(f"La asignatura {asignatura}, no existe.")
        return False
    else:
        return True

def listar_matriculados():
    asignatura = input("Introduzca la asignatura: ")
    if comprobar_asignatura(asignatura):
        print(asignaturas.get(asignatura))
        return asignatura
    else:
        return None

def matricular_alumno():
    asignatura = input("Introduzca la asignatura: ")
    if comprobar_asignatura(asignatura):
        alumno = input("Introduzca el nombre del alumno a matricular: ")
        asignaturas.get(asignatura).append(alumno)

def desmatricular_alumno():
    asignatura = listar_matriculados()
    if asignatura is None:
        return
    alumno = input("Introduzca el nombre del alumno a desmatricular: ")

    if alumno in asignaturas.get(asignatura):
        asignaturas.get(asignatura).remove(alumno)
        print(f"{alumno} ha sido desmatriculado de {asignatura}")
    else:
        print(f"{asignatura} o {alumno} incorrecto")



def menu():
    print("---------- MENU PRINCIPAL ----------")
    print("1. Consultar alumnos matriculados")
    print("2. Matricular alumno en una asignatura")
    print("3. Desmatricular alumno de una asignatura")
    print("4. Salir")

def main():
    while True:
        menu()
        opcion = input("Escoja una opción (1-4): ")
        match opcion:
            case "1":
                listar_matriculados()
            case "2":
                matricular_alumno()
            case "3":
                desmatricular_alumno()
            case "4":
                break

if __name__=="__main__":
    main()