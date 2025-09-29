from random import *

piedra = {"lagarto", "papel"}
papel = {"spock", "piedra"}
tijera = {"lagarto", "papel"}
lagarto = {"spock", "papel"}
spock = {"tijeras", "piedra"}

elecciones_validas = ["piedra", "papel", "tijera", "lagarto","spock"]
i = randint(0, 5)-1
eleccion_maquina = elecciones_validas[i]


eleccion = input("introduzca su elección")

while eleccion not in elecciones_validas:
    print(eleccion + " no es una elección válida, las elecciones válidas son " + elecciones_validas)
    
match eleccion:
    case "piedra":
        if (eleccion_maquina not in piedra):
            print(eleccion_maquina + " gana a " + eleccion)
        else:
            print(eleccion + "gana a " + eleccion_maquina)
    case "papel":
        if (eleccion_maquina not in papel):
            print(eleccion_maquina + " gana a " + eleccion)
        else:
            print(eleccion + "gana a " + eleccion_maquina)
    case "tijera":
        if (eleccion_maquina not in tijera):
            print(eleccion_maquina + " gana a " + eleccion)
        else:
            print(eleccion + "gana a " + eleccion_maquina)
    case "lagarto":
        if (eleccion_maquina not in lagarto):
            print(eleccion_maquina + " gana a " + eleccion)
        else:
            print(eleccion + "gana a " + eleccion_maquina)
    case "spock":
        if (eleccion_maquina not in spock):
            print(eleccion_maquina + " gana a " + eleccion)
        else:
            print(eleccion + "gana a " + eleccion_maquina)
