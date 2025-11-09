departamentos = {
    "Recursos Humanos": {
        "Ana": "Gerente de Recursos Humanos",
        "Luis": "Especialista en Reclutamiento",
        "Elena": "Asistente de Recursos Humanos"
    },
    "Tecnología": {
        "Carlos": "Desarrollador Backend",
        "María": "Desarrolladora Frontend",
        "Pedro": "Administrador de Sistemas"
    },
    "Marketing": {
        "Sofía": "Directora de Marketing",
        "Jorge": "Especialista en SEO",
        "Laura": "Community Manager"
    },
    "Finanzas": {
        "Juan": "Analista Financiero",
        "Lucía": "Contadora",
        "Raúl": "Asesor Financiero"
    }
}

def mostrar_empleados():
    departamento = input("Introduzca el nombre del departamento: ")
    if departamento in departamentos.keys():
        print(departamentos[departamento])
    else:
        print("Ese departamento no forma parte de la empresa")

def contratar_empleado():
    empleado = input("Introduzca el nombre del empleado: ")
    puesto = input("Introduzca el puesto del empleado: ")
    departamento = input("Introduzca el departamento del empleado: ")

    if departamento in departamentos.keys():
        if empleado in departamentos[departamento].keys():
            print(f"{empleado} ya es parte del departamento de {departamento}")
        else:
            departamentos[departamento][empleado] = puesto
            print("Empleado contratado")
    else:
        print("Ese departamento no forma parte de la empresa")

def despedir_empleado():
    empleado = input("Introduzca el nombre del empleado: ")
    departamento = input("Introduzca el departamento del empleado: ")

    if departamento in departamentos.keys():
        if empleado in departamentos[departamento].keys():
            departamentos[departamento].pop(empleado)
            print(f"{empleado} ha sido despedido")
        else:
            print(f"{empleado} no forma parte del departamento de {departamento}")
    else:
        print("Ese departamento no forma parte de la empresa")

def menu():
    print("---------- MENU PRINCIPAL ----------")
    print("1. Mostrar los empleados de un departamento")
    print("2. Contratar a un empleado")
    print("3. Despedir a un empleado")
    print("4. Salir")

def main():
    while True:
        menu()
        opcion = input("Escoja una opción (1-4): ")
        match opcion:
            case "1":
                mostrar_empleados()
            case "2":
                contratar_empleado()
            case "3":
                despedir_empleado()
            case "4":
                break
            case _:
                print(f"{opcion} no es una opcion válida")
    


if __name__ == "__main__":
    main()
                
