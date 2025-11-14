data = [
{
"nombre": "Luis Pérez",
"nif": "12345678A",
"ciclo": "DAM",
"notas": {"SGE": 7.2, "DI": 5.6, "PMDM": 6.4, "AD": 8.1, "EIE": 4.9}
}]

def get_average_grandes():
    medias = []

    for alumno in data:
        dicci = {}
        dicci["nombre"] = alumno.get("nombre")
        
        notas = alumno.get("notas")
        notas = notas.values()
        media = sum(notas)/len(notas)
        dicci["nota_media"] = media
        medias.append(dicci)

    return medias

print(get_average_grandes())

def get_usernames():
    usernames = []

    for alumno in data:
        dicci = {}
        nombre = alumno.get("nombre")
        dicci["nombre"] = nombre
        
        tag = ""
        tag += nombre[0].lower()
        apellido = nombre.split(" ")
        apellido = apellido[1].lower()
        tag += apellido
        dicci["username"] = tag
        usernames.append(dicci)

    return usernames
print(get_usernames())

def get_by_subject( subject ):
    matriculados = []
    for alumno in data:
       notas = alumno.get("notas")
       if (subject in notas.keys()):
           matriculados.append(alumno.get("nombre"))
    return matriculados
print(get_by_subject("SGE"))

def set_grade( nif, subject, grade, data ):
    for alumno in data:
        if (alumno.get("nif") == nif):
            notas = alumno.get("notas")
            notas[subject] = grade
            return alumno
    print(f"El alumno con nif {nif}, no se encuentra en la base de datos.")
print(set_grade("12345678A","SGE",9.8, data))
