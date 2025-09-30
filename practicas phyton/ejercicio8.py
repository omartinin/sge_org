from random import *

piedra = {"lagarto", "papel"}
papel = {"spock", "piedra"}
tijera = {"lagarto", "papel"}
lagarto = {"spock", "papel"}
spock = {"tijera", "piedra"}

elecciones_validas = ["piedra", "papel", "tijera", "lagarto","spock"]

c_maquina = 0
c_jugador = 0

while (c_maquina < 5 and c_jugador < 5):
    i = randint(0, 5)-1
    eleccion_maquina = elecciones_validas[i]


    eleccion = input("introduzca su elección: ")

    while eleccion not in elecciones_validas:
        print(eleccion + " no es una elección válida, las elecciones válidas son " + elecciones_validas)
     
    match eleccion:
        case eleccion if eleccion == eleccion_maquina:
            print("empate")
        case "piedra":
            if (eleccion_maquina not in piedra):
                print(eleccion_maquina + " gana a " + eleccion)
                c_maquina+=1
            else:
                print(eleccion + "gana a " + eleccion_maquina)
                c_jugador+=1
        case "papel":
            if (eleccion_maquina not in papel):
                print(eleccion_maquina + " gana a " + eleccion)
                c_maquina+=1
            else:
                print(eleccion + " gana a " + eleccion_maquina)
                c_jugador+=1
        case "tijera":
            if (eleccion_maquina not in tijera):
                print(eleccion_maquina + " gana a " + eleccion)
                c_maquina+=1
            else:
                print(eleccion + " gana a " + eleccion_maquina)
                c_jugador+=1
        case "lagarto":
            if (eleccion_maquina not in lagarto):
                print(eleccion_maquina + " gana a " + eleccion)
                c_maquina+=1
            else:
                print(eleccion + " gana a " + eleccion_maquina)
                c_jugador+=1
        case "spock":
            if (eleccion_maquina not in spock):
                print(eleccion_maquina + " gana a " + eleccion)
                c_maquina+=1
            else:
                print(eleccion + " gana a " + eleccion_maquina)
                c_jugador+=1

